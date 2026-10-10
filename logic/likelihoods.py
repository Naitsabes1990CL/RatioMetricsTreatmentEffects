"""Maximum-likelihood and regression fit routines.

Stateless, array-in/estimate-out numerical routines used by the model
classes in :mod:`logic.battey_edgar_models` and
:mod:`logic.iroas_models`. All functions accept arrays shaped
``(n_reps, n)`` and return per-replication estimates of shape
``(n_reps,)`` (vectorized closed forms where available, otherwise a
loop over replications, each a tiny 1-2 parameter solve).

The Weibull parametrization throughout is the proportional-hazards
form with survival ``S(y) = exp(-rate * y**shape)``, matching Battey &
Edgar (2026, section 4.3).
"""

import numpy as np
import statsmodels.api as sm
from scipy import optimize
from statsmodels.tools.sm_exceptions import PerfectSeparationError


def mle_linear(y1: np.ndarray, y0: np.ndarray) -> np.ndarray:
    """MLE of the additive effect Delta in the linear model (ex. 1).

    Coincides with the model-free estimator by construction — the
    reason the paper calls example 1 "compatible".

    Args:
        y1: Treated outcomes, shape ``(n_reps, n)``.
        y0: Control outcomes, shape ``(n_reps, n)``.

    Returns:
        Per-replication ``mean(y1 - y0)``.
    """
    return np.mean(y1 - y0, axis=-1)


def mle_exponential_multiplicative(
    y1: np.ndarray, gamma: np.ndarray
) -> np.ndarray:
    """Closed-form MLE of theta in the exponential model (ex. 2).

    Uses the scaling property ``gamma_i * Y_i1 ~ Exp(rate=theta)``
    when ``Y_i1 ~ Exp(rate=gamma_i * theta)``; ``y0`` carries no
    information about theta.

    Args:
        y1: Treated outcomes, shape ``(n_reps, n)``.
        gamma: Known baseline rates, shape ``(n_reps, n)``.

    Returns:
        Per-replication ``n / sum(gamma * y1)``.
    """
    n = y1.shape[-1]
    return n / np.sum(gamma * y1, axis=-1)


def mle_weibull_known_alpha(
    y1: np.ndarray, gamma: np.ndarray, alpha: float
) -> np.ndarray:
    """Closed-form MLE of theta in the Weibull model, alpha known.

    ``Y**alpha`` is exponential, reducing example 3 to example 2:
    ``gamma_i * Y_i1**alpha ~ Exp(rate=theta)``.

    Args:
        y1: Treated outcomes, shape ``(n_reps, n)``.
        gamma: Known baseline rates, shape ``(n_reps, n)``.
        alpha: Known Weibull shape parameter.

    Returns:
        Per-replication MLE of the rate multiplier theta.
    """
    n = y1.shape[-1]
    return n / np.sum(gamma * y1**alpha, axis=-1)


def _weibull_profile_nll(
    log_alpha: float,
    y1: np.ndarray,
    y0: np.ndarray,
    gamma: np.ndarray,
) -> float:
    """Profile negative log-likelihood in log(alpha), theta profiled.

    For fixed alpha the MLE of theta is closed-form
    (``n / sum(gamma * y1**alpha)``); substituting it leaves a scalar
    criterion in alpha only. Additive constants in the baseline rates
    are dropped.

    Args:
        log_alpha: Log of the Weibull shape parameter.
        y1: Treated outcomes for one replication, shape ``(n,)``.
        y0: Control outcomes for one replication, shape ``(n,)``.
        gamma: Known baseline rates for one replication, shape
            ``(n,)``.

    Returns:
        Profile negative log-likelihood value.
    """
    alpha = np.exp(log_alpha)
    n = y1.shape[-1]
    s_log = np.sum(np.log(y0)) + np.sum(np.log(y1))
    s1 = np.sum(gamma * y1**alpha)
    loglik = (
        2.0 * n * np.log(alpha)
        + (alpha - 1.0) * s_log
        - np.sum(gamma * y0**alpha)
        - n
        + n * np.log(n)
        - n * np.log(s1)
    )
    return -loglik


def mle_weibull_joint(
    y1: np.ndarray, y0: np.ndarray, gamma: np.ndarray
) -> dict[str, np.ndarray]:
    """Joint MLE of (alpha, theta) in the Weibull model (ex. 3).

    Profiles theta out in closed form and minimizes the resulting
    scalar criterion over ``log(alpha)`` per replication.

    Args:
        y1: Treated outcomes, shape ``(n_reps, n)``.
        y0: Control outcomes, shape ``(n_reps, n)``.
        gamma: Known baseline rates, shape ``(n_reps, n)``.

    Returns:
        Dict with per-replication arrays ``"alpha"`` and ``"theta"``.
    """
    n_reps, n = y1.shape
    alpha_hat = np.empty(n_reps)
    theta_hat = np.empty(n_reps)
    for r in range(n_reps):
        result = optimize.minimize_scalar(
            _weibull_profile_nll,
            bounds=(-3.0, 3.0),
            method="bounded",
            args=(y1[r], y0[r], gamma[r]),
        )
        alpha_hat[r] = np.exp(result.x)
        theta_hat[r] = n / np.sum(gamma[r] * y1[r] ** alpha_hat[r])
    return {"alpha": alpha_hat, "theta": theta_hat}


def mle_exponential_additive(
    y1: np.ndarray, gamma: np.ndarray
) -> np.ndarray:
    """MLE of the additive rate shift Delta (ex. 4), via root-finding.

    ``Y_i1 ~ Exp(rate=gamma_i + Delta)``; the score
    ``sum(1 / (gamma_i + Delta) - y_i1)`` is strictly decreasing with
    a unique root on ``(-min(gamma), inf)``, located with Brent's
    method after expanding the upper bracket.

    Args:
        y1: Treated outcomes, shape ``(n_reps, n)``.
        gamma: Known baseline rates, shape ``(n_reps, n)``.

    Returns:
        Per-replication MLE of Delta.
    """
    n_reps = y1.shape[0]
    delta_hat = np.empty(n_reps)
    for r in range(n_reps):
        g, y = gamma[r], y1[r]

        def score(delta: float) -> float:
            return float(np.sum(1.0 / (g + delta) - y))

        lo = -np.min(g) * (1.0 - 1e-9) + 1e-12
        hi = max(1.0, float(np.mean(g)))
        while score(hi) > 0.0:
            hi *= 10.0
        delta_hat[r] = optimize.brentq(score, lo, hi)
    return delta_hat


def mle_logistic_offset(
    y1: np.ndarray, gamma: np.ndarray
) -> np.ndarray:
    """MLE of the log-odds shift Delta (ex. 5) via offset GLM.

    Fits, per replication, a binomial GLM with canonical logit link,
    a single intercept-only design column and the known baselines
    ``gamma_i`` passed as offset — so the lone coefficient is Delta.

    Args:
        y1: Treated binary outcomes, shape ``(n_reps, n)``.
        gamma: Known baseline log-odds, shape ``(n_reps, n)``.

    Returns:
        Per-replication MLE of Delta (``nan`` on perfect separation,
        i.e. an all-zero or all-one replication).
    """
    n_reps, n = y1.shape
    ones = np.ones((n, 1))
    delta_hat = np.full(n_reps, np.nan)
    totals = y1.sum(axis=-1)
    for r in range(n_reps):
        if totals[r] in (0.0, float(n)):
            # Reason: an intercept-only offset GLM has a finite MLE
            # only when 0 < sum(y) < n; skip separated replications.
            continue
        model = sm.GLM(
            y1[r],
            ones,
            family=sm.families.Binomial(),
            offset=gamma[r],
        )
        try:
            delta_hat[r] = model.fit().params[0]
        except (PerfectSeparationError, ValueError):
            # Reason: an all-0/all-1 replication has no interior MLE;
            # nan keeps the replication visible instead of crashing.
            continue
    return delta_hat


def wls_through_origin(
    dy: np.ndarray, dx: np.ndarray, weights: np.ndarray
) -> np.ndarray:
    """Weighted least squares through the origin, vectorized.

    Closed form ``sum(w * dx * dy) / sum(w * dx**2)`` per replication
    — the model-based iROAS fit when revenue noise scales with geo
    size (weights ``1 / size**2`` match that heteroskedasticity).

    Args:
        dy: Response differences, shape ``(n_reps, n)``.
        dx: Regressor differences, shape ``(n_reps, n)``.
        weights: Per-unit weights, shape ``(n_reps, n)``.

    Returns:
        Per-replication slope estimates.
    """
    num = np.sum(weights * dx * dy, axis=-1)
    den = np.sum(weights * dx**2, axis=-1)
    return num / den


def fit_size_interaction(
    dy: np.ndarray,
    dx: np.ndarray,
    gamma: np.ndarray,
    weights: np.ndarray,
) -> dict[str, np.ndarray]:
    """Fit dy = rho0 * (gamma/median)**delta * dx by weighted LS.

    The model-based resolution of the heterogeneous-iROAS world:
    instead of averaging unit-level ratios, the size interaction is
    modelled explicitly, recovering the stable pair (rho0, delta) —
    McCullagh-style interactions as advocated in Battey & Edgar
    (2026, section 5).

    Args:
        dy: Response differences, shape ``(n_reps, n)``.
        dx: Regressor differences, shape ``(n_reps, n)``.
        gamma: Unit sizes, shape ``(n_reps, n)``.
        weights: Per-unit weights, shape ``(n_reps, n)``.

    Returns:
        Dict with per-replication arrays ``"rho0"`` and ``"delta"``.
    """
    n_reps = dy.shape[0]
    rho0_hat = np.empty(n_reps)
    delta_hat = np.empty(n_reps)
    for r in range(n_reps):
        u = gamma[r] / np.median(gamma[r])
        w, yy, xx = weights[r], dy[r], dx[r]

        def loss(params: np.ndarray) -> float:
            rho0, delta = np.exp(params[0]), params[1]
            resid = yy - rho0 * u**delta * xx
            return float(np.sum(w * resid**2))

        result = optimize.minimize(
            loss, x0=np.array([0.0, 0.0]), method="Nelder-Mead"
        )
        rho0_hat[r] = np.exp(result.x[0])
        delta_hat[r] = result.x[1]
    return {"rho0": rho0_hat, "delta": delta_hat}


def trimmed_ratio(
    dy: np.ndarray, dx: np.ndarray, trim: float = 0.05
) -> np.ndarray:
    """Aggregate ratio after trimming extreme per-unit ratios.

    Drops the units whose per-unit ratio ``dy/dx`` falls in the lower
    or upper ``trim`` tail (per replication), then returns
    ``sum(dy) / sum(dx)`` on the remainder — a Trimmed-Match-flavored
    robustification of the aggregate iROAS estimator.

    Args:
        dy: Response differences, shape ``(n_reps, n)``.
        dx: Regressor differences, shape ``(n_reps, n)``.
        trim: Tail fraction trimmed on each side, in ``[0, 0.5)``.

    Raises:
        ValueError: If ``trim`` is outside ``[0, 0.5)``.

    Returns:
        Per-replication trimmed aggregate ratios.
    """
    if not 0.0 <= trim < 0.5:
        raise ValueError(f"trim must be in [0, 0.5), got {trim}")
    ratios = dy / dx
    lo = np.quantile(ratios, trim, axis=-1, keepdims=True)
    hi = np.quantile(ratios, 1.0 - trim, axis=-1, keepdims=True)
    keep = (ratios >= lo) & (ratios <= hi)
    num = np.sum(np.where(keep, dy, 0.0), axis=-1)
    den = np.sum(np.where(keep, dx, 0.0), axis=-1)
    return num / den
