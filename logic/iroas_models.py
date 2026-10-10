"""Geo-experiment iROAS case study (ratio-metric treatment effects).

Simulates a growth-marketing budget "negativization" experiment: in
treated geo-units, marketing cost drops multiplicatively (down to
-99%), and the estimand of interest is iROAS = incremental revenue /
incremental cost. The model registers four competing estimators —
average of per-geo ratios, ratio of aggregates, a trimmed ratio, and a
weighted regression — whose contrasting behavior under geo-size
heterogeneity mirrors examples 2 and 4-5 of Battey & Edgar (2026).

Built on the same :class:`PotentialOutcomeModel` contract as the paper
examples, with a richer data payload (:class:`RatioTrialData`).
"""

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

from logic import likelihoods
from logic.simulation_engine import PotentialOutcomeModel

#: Geo-size populations. "zipf_like" is heavy-tailed (few huge
#: regions, many tiny ones — the realistic case); "homogeneous" keeps
#: geos near-equal (the control case).
GEO_POPULATIONS: dict[str, stats.rv_continuous] = {
    "zipf_like": stats.lognorm(s=1.5, scale=1.0),
    "homogeneous": stats.lognorm(s=0.2, scale=1.0),
}


@dataclass(frozen=True)
class RatioTrialData:
    """Geo-level potential outcomes, arrays shaped ``(n_reps, n)``.

    Attributes:
        gamma: Geo sizes (known baseline parameters).
        rho: Per-geo true iROAS values (constant across geos in the
            constant-rho world).
        revenue0: Control-arm revenue.
        revenue1: Treated-arm revenue.
        cost0: Control-arm marketing cost.
        cost1: Treated-arm (negativized) marketing cost.
    """

    gamma: np.ndarray
    rho: np.ndarray
    revenue0: np.ndarray
    revenue1: np.ndarray
    cost0: np.ndarray
    cost1: np.ndarray


class GeoiROASModel(PotentialOutcomeModel):
    """Budget-negativization geo experiment with iROAS estimand.

    Data-generating process per geo i (all arrays ``(n_reps, n)``):

    - cost0 = spend_rate * gamma_i * exp(eta_i), a size-proportional
      spend with lognormal noise;
    - cost1 = kappa * cost0, the multiplicative negativization
      (kappa = 0.01 means a -99% budget cut) — a scale-family action,
      the paper's example-2 structure on the cost side;
    - rho_i = rho0 * (gamma_i / median(gamma))**rho_size_exponent
      (constant iROAS when the exponent is 0);
    - revenue(t) = organic_rate * gamma_i + rho_i * cost(t) + eps,
      with eps ~ N(0, scale^2) drawn independently per arm and
      scale = sigma_revenue_floor + sigma_revenue * gamma_i: the
      floor is measurement noise that does NOT shrink with geo size,
      so per-geo ratios dR/dC explode for tiny geos (whose dC is
      tiny) — the example-4 "gamma near zero" pathology for ratio
      metrics.
    """

    name = "geo_iroas"

    def __init__(
        self,
        baseline: stats.rv_continuous,
        rho0: float,
        kappa: float,
        rho_size_exponent: float = 0.0,
        spend_rate: float = 1.0,
        organic_rate: float = 5.0,
        sigma_cost: float = 0.2,
        sigma_revenue: float = 0.5,
        sigma_revenue_floor: float = 0.5,
        trim: float = 0.05,
    ) -> None:
        """Configure the geo experiment.

        Args:
            baseline: Geo-size population (positive support).
            rho0: True iROAS at the median-size geo.
            kappa: Cost multiplier in treated geos, in ``(0, 1]``
                (0.01 = -99% negativization).
            rho_size_exponent: Elasticity of per-geo iROAS with
                respect to geo size (0 = constant-rho world).
            spend_rate: Baseline spend per unit of geo size.
            organic_rate: Organic (ad-independent) revenue per unit
                of geo size.
            sigma_cost: Lognormal sigma of baseline-cost noise.
            sigma_revenue: Revenue noise scale per unit of geo size.
            sigma_revenue_floor: Size-independent revenue noise floor
                (measurement noise) — the ingredient that makes tiny
                geos' per-geo ratios explode.
            trim: Tail fraction for the trimmed-ratio estimator.

        Raises:
            ValueError: If ``kappa`` is outside ``(0, 1]``.
        """
        if not 0.0 < kappa <= 1.0:
            raise ValueError(f"kappa must be in (0, 1], got {kappa}")
        self._baseline = baseline
        self.rho0 = rho0
        self.kappa = kappa
        self.rho_size_exponent = rho_size_exponent
        self.spend_rate = spend_rate
        self.organic_rate = organic_rate
        self.sigma_cost = sigma_cost
        self.sigma_revenue = sigma_revenue
        self.sigma_revenue_floor = sigma_revenue_floor
        self.trim = trim

    def noise_scale(self, gamma: np.ndarray) -> np.ndarray:
        """Revenue noise scale: floor plus size-proportional part."""
        return (
            self.sigma_revenue_floor + self.sigma_revenue * gamma
        )

    @property
    def true_value(self) -> float:
        """True iROAS at the median-size geo."""
        return self.rho0

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> RatioTrialData:
        """Simulate geo sizes, costs, and revenues (vectorized)."""
        shape = (n_reps, n)
        gamma = self._baseline.rvs(size=shape, random_state=rng)
        eta = rng.normal(0.0, self.sigma_cost, size=shape)
        cost0 = self.spend_rate * gamma * np.exp(eta)
        cost1 = self.kappa * cost0
        med = np.median(gamma, axis=-1, keepdims=True)
        rho = self.rho0 * (gamma / med) ** self.rho_size_exponent
        organic = self.organic_rate * gamma
        noise_scale = self.noise_scale(gamma)
        revenue0 = (
            organic
            + rho * cost0
            + rng.normal(0.0, noise_scale, size=shape)
        )
        revenue1 = (
            organic
            + rho * cost1
            + rng.normal(0.0, noise_scale, size=shape)
        )
        return RatioTrialData(
            gamma, rho, revenue0, revenue1, cost0, cost1
        )

    def estimators(
        self,
    ) -> dict[str, Callable[[RatioTrialData], np.ndarray]]:
        """Four competing iROAS estimators (see module docstring)."""
        return {
            "avg_of_geo_ratios": _avg_of_geo_ratios,
            "ratio_of_aggregates": _ratio_of_aggregates,
            "trimmed_ratio": lambda d: likelihoods.trimmed_ratio(
                d.revenue1 - d.revenue0,
                d.cost1 - d.cost0,
                trim=self.trim,
            ),
            "wls_regression": lambda d: (
                likelihoods.wls_through_origin(
                    d.revenue1 - d.revenue0,
                    d.cost1 - d.cost0,
                    weights=1.0 / self.noise_scale(d.gamma) ** 2,
                )
            ),
        }

    def analytic_tau(self, data: RatioTrialData) -> np.ndarray:
        """Large-n target of the per-geo ratio average: mean(rho_i).

        E[dR_i / dC_i] = rho_i because revenue noise is independent
        of the cost draws, so the eq.-3.1 analog for this ratio
        metric is the unweighted mean of the realized rho_i.
        """
        return np.mean(data.rho, axis=-1)

    def reference_values(self) -> dict[str, float]:
        """rho0 for all estimators in the constant-rho world.

        In the heterogeneous world (nonzero size exponent) no single
        stable iROAS exists — every estimator targets a different
        rho_i average, so all references are ``nan`` and the notebook
        computes each estimator's own large-n limit explicitly.
        """
        if self.rho_size_exponent == 0.0:
            return {name: self.rho0 for name in self.estimators()}
        return {name: np.nan for name in self.estimators()}


def _avg_of_geo_ratios(data: RatioTrialData) -> np.ndarray:
    """Unweighted mean of per-geo ratios dR_i / dC_i, per rep."""
    dr = data.revenue1 - data.revenue0
    dc = data.cost1 - data.cost0
    return np.mean(dr / dc, axis=-1)


def _ratio_of_aggregates(data: RatioTrialData) -> np.ndarray:
    """Standard geo-experiment estimator sum(dR) / sum(dC), per rep."""
    dr = data.revenue1 - data.revenue0
    dc = data.cost1 - data.cost0
    return np.sum(dr, axis=-1) / np.sum(dc, axis=-1)


def iroas_inference(
    model: GeoiROASModel, data: RatioTrialData
) -> pd.DataFrame:
    """Per-replication estimates AND standard errors, tidy format.

    Pairs each of the model's four estimators with the confidence
    interval a practitioner would attach to it: the i.i.d. SE for the
    average of per-geo ratios, the delta-method linearization SE for
    the (trimmed) aggregate ratio, and the HC1 sandwich SE for the
    WLS slope. Used for the bias/coverage tables in the case-study
    notebook.

    Args:
        model: The configured geo experiment.
        data: Payload returned by ``model.draw``.

    Returns:
        Tidy DataFrame with columns ``estimator``, ``rep``,
        ``estimate``, ``se`` and ``true_value`` (``rho0`` in the
        constant-rho world, ``nan`` in the heterogeneous world where
        no single target exists).
    """
    dr = data.revenue1 - data.revenue0
    dc = data.cost1 - data.cost0
    weights = 1.0 / model.noise_scale(data.gamma) ** 2
    keep = likelihoods.trim_mask(dr, dc, model.trim)
    results: dict[str, tuple[np.ndarray, np.ndarray]] = {
        "avg_of_geo_ratios": (
            _avg_of_geo_ratios(data),
            likelihoods.se_avg_of_ratios(dr, dc),
        ),
        "ratio_of_aggregates": (
            _ratio_of_aggregates(data),
            likelihoods.se_aggregate_ratio(dr, dc),
        ),
        "trimmed_ratio": (
            likelihoods.trimmed_ratio(dr, dc, trim=model.trim),
            likelihoods.se_aggregate_ratio(dr, dc, keep=keep),
        ),
        "wls_regression": (
            likelihoods.wls_through_origin(dr, dc, weights),
            likelihoods.se_wls_through_origin(dr, dc, weights),
        ),
    }
    true = (
        model.rho0 if model.rho_size_exponent == 0.0 else np.nan
    )
    n_reps = dr.shape[0]
    frames = [
        pd.DataFrame(
            {
                "estimator": name,
                "rep": np.arange(n_reps),
                "estimate": est,
                "se": se,
                "true_value": true,
            }
        )
        for name, (est, se) in results.items()
    ]
    return pd.concat(frames, ignore_index=True)


def randomize_assignment(
    data: RatioTrialData,
    p_treated: float,
    rng: np.random.Generator,
) -> dict[str, np.ndarray]:
    """Mask one potential outcome per geo, as in a real experiment.

    Args:
        data: Full potential-outcome payload.
        p_treated: Probability a geo is assigned to treatment.
        rng: NumPy random generator.

    Returns:
        Dict with ``"treated"`` (bool assignment matrix),
        ``"revenue"`` and ``"cost"`` (the observed arm's values only),
        all shaped ``(n_reps, n)``.
    """
    treated = (
        rng.random(size=data.gamma.shape) < p_treated
    )
    revenue = np.where(treated, data.revenue1, data.revenue0)
    cost = np.where(treated, data.cost1, data.cost0)
    return {"treated": treated, "revenue": revenue, "cost": cost}


def randomized_iroas(
    revenue: np.ndarray,
    cost: np.ndarray,
    treated: np.ndarray,
) -> np.ndarray:
    """Feasible difference-in-means iROAS from a randomized design.

    Estimates incremental revenue and cost as treated-minus-control
    group means and returns their ratio, per replication — the
    feasible analog of the ratio-of-aggregates estimator when only
    one arm is observed per geo.

    Args:
        revenue: Observed revenue, shape ``(n_reps, n)``.
        cost: Observed cost, shape ``(n_reps, n)``.
        treated: Boolean assignment matrix, shape ``(n_reps, n)``.

    Returns:
        Per-replication iROAS estimates.
    """
    t = treated.astype(float)
    n_t = np.sum(t, axis=-1)
    n_c = np.sum(1.0 - t, axis=-1)
    d_revenue = (
        np.sum(revenue * t, axis=-1) / n_t
        - np.sum(revenue * (1.0 - t), axis=-1) / n_c
    )
    d_cost = (
        np.sum(cost * t, axis=-1) / n_t
        - np.sum(cost * (1.0 - t), axis=-1) / n_c
    )
    return d_revenue / d_cost
