"""The five worked examples of Battey & Edgar (2026, section 4.3).

Each example is one :class:`PotentialOutcomeModel` subclass bundling
its data-generating process (under the paper's fictitious idealisation:
both potential outcomes observable, baseline parameters gamma_i known),
its closed-form analytic tau_n, and its model-based MLE. The generic
model-free estimator lives in :mod:`logic.simulation_engine`, outside
the classes, mirroring the paper's dichotomy: model-based estimation
uses the model, model-free estimation is model-agnostic.

``GAMMA_POPULATIONS`` and ``LOGODDS_POPULATIONS`` provide the named
baseline-parameter populations used in the tutorial notebook,
including the paper's two extreme cases for example 4.
"""

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
from scipy import stats
from scipy.special import expit

from logic import likelihoods
from logic.simulation_engine import (
    PotentialOutcomeModel,
    model_free_effect,
)

#: Positive baseline-rate populations (examples 1-4). "near_zero" and
#: "large" reproduce the paper's two extreme cases for example 4
#: ("if all the gamma_i are concentrated near zero, tau_n is large,
#: while if all the gamma_i are large, then tau_n is tiny").
GAMMA_POPULATIONS: dict[str, stats.rv_continuous] = {
    "near_zero": stats.gamma(a=2.0, scale=0.05),
    "large": stats.uniform(loc=5.0, scale=5.0),
    "moderate": stats.lognorm(s=0.5, scale=1.0),
}

#: Real-line baseline log-odds populations (example 5).
LOGODDS_POPULATIONS: dict[str, stats.rv_continuous] = {
    "balanced": stats.norm(loc=0.0, scale=1.0),
    "rare_events": stats.norm(loc=-3.0, scale=0.5),
    "common_events": stats.norm(loc=1.5, scale=0.5),
}


@dataclass(frozen=True)
class TrialData:
    """One study's potential outcomes, arrays shaped ``(n_reps, n)``.

    Attributes:
        gamma: Known unit-level baseline parameters.
        y0: Control potential outcomes.
        y1: Treated potential outcomes.
    """

    gamma: np.ndarray
    y0: np.ndarray
    y1: np.ndarray


class _PaperExample(PotentialOutcomeModel):
    """Shared baseline-sampling plumbing for the five examples."""

    def __init__(self, baseline: stats.rv_continuous) -> None:
        """Store the baseline-parameter population.

        Args:
            baseline: Frozen scipy distribution for gamma_i.
        """
        self._baseline = baseline

    def _draw_gamma(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> np.ndarray:
        """Draw the ``(n_reps, n)`` baseline-parameter matrix."""
        return self._baseline.rvs(size=(n_reps, n), random_state=rng)


class LinearAdditiveModel(_PaperExample):
    """Example 1: Y_i0 = gamma_i + eps_i, Y_i1 = gamma_i + Delta + eps_i.

    Draws ONE eps_i per unit, reused for both potential outcomes.
    This shared-noise construction is what realizes Fisher's unit
    treatment additivity and yields exact, zero-variance recovery of
    Delta by the model-free average — independent per-outcome draws
    would silently break the compatibility demonstration.
    """

    name = "ex1_linear_additive"

    def __init__(
        self,
        baseline: stats.rv_continuous,
        delta: float,
        sigma: float = 1.0,
    ) -> None:
        """Configure the model.

        Args:
            baseline: Population of baseline parameters gamma_i.
            delta: True additive treatment effect.
            sigma: Standard deviation of the shared unit noise.
        """
        super().__init__(baseline)
        self.delta = delta
        self.sigma = sigma

    @property
    def true_value(self) -> float:
        """True additive effect Delta."""
        return self.delta

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> TrialData:
        """Simulate with one shared eps_i per unit (see class doc)."""
        gamma = self._draw_gamma(n, n_reps, rng)
        eps = rng.normal(0.0, self.sigma, size=(n_reps, n))
        return TrialData(gamma, gamma + eps, gamma + self.delta + eps)

    def estimators(
        self,
    ) -> dict[str, Callable[[TrialData], np.ndarray]]:
        """Model-free mean difference and (identical) MLE."""
        return {
            "model_free": lambda d: model_free_effect(d.y1, d.y0),
            "model_based": lambda d: likelihoods.mle_linear(
                d.y1, d.y0
            ),
        }

    def analytic_tau(self, data: TrialData) -> np.ndarray:
        """tau_n = Delta for every sample."""
        return np.full(data.gamma.shape[0], self.delta)


class ExponentialMultiplicativeModel(_PaperExample):
    """Example 2: exponential rates gamma_i and gamma_i * theta.

    A scale family: after log transform, tau_n = -log(theta) for every
    gamma-sample — the model-free and model-based definitions agree.
    The model-free estimate is reported back on the theta scale via
    exp(-tau_hat).
    """

    name = "ex2_exponential_multiplicative"

    def __init__(
        self, baseline: stats.rv_continuous, theta: float
    ) -> None:
        """Configure the model.

        Args:
            baseline: Population of baseline rates gamma_i (> 0).
            theta: True multiplicative rate effect (> 0).
        """
        super().__init__(baseline)
        self.theta = theta

    @property
    def true_value(self) -> float:
        """True rate multiplier theta."""
        return self.theta

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> TrialData:
        """Simulate independent exponential potential outcomes."""
        gamma = self._draw_gamma(n, n_reps, rng)
        y0 = rng.exponential(scale=1.0 / gamma)
        y1 = rng.exponential(scale=1.0 / (gamma * self.theta))
        return TrialData(gamma, y0, y1)

    def estimators(
        self,
    ) -> dict[str, Callable[[TrialData], np.ndarray]]:
        """Model-free (log scale, mapped to theta) and closed-form MLE."""
        return {
            "model_free": lambda d: np.exp(
                -model_free_effect(d.y1, d.y0, transform=np.log)
            ),
            "model_based": lambda d: (
                likelihoods.mle_exponential_multiplicative(
                    d.y1, d.gamma
                )
            ),
        }

    def analytic_tau(self, data: TrialData) -> np.ndarray:
        """tau_n = -log(theta), invariant to the gamma-sample."""
        return np.full(data.gamma.shape[0], -np.log(self.theta))


class WeibullMultiplicativeModel(_PaperExample):
    """Example 3: Weibull (shape alpha), rate effect theta.

    Survival ``exp(-rate * y**alpha)``. tau_n = -log(theta)/alpha for
    every gamma-sample: stable, but theta and alpha are confounded in
    tau_n ("semi-compatible"). With ``alpha_known=True`` the
    model-free estimate maps back to the theta scale; otherwise the
    raw tau is reported alongside the joint (alpha, theta) MLE, which
    remains well-identified.
    """

    name = "ex3_weibull_multiplicative"

    def __init__(
        self,
        baseline: stats.rv_continuous,
        theta: float,
        alpha: float,
        alpha_known: bool = True,
    ) -> None:
        """Configure the model.

        Args:
            baseline: Population of baseline rates gamma_i (> 0).
            theta: True multiplicative rate effect (> 0).
            alpha: True Weibull shape parameter (> 0).
            alpha_known: Whether estimators may use the true alpha.
        """
        super().__init__(baseline)
        self.theta = theta
        self.alpha = alpha
        self.alpha_known = alpha_known
        self._joint_cache: tuple[int, dict[str, np.ndarray]] | None = (
            None
        )

    @property
    def true_value(self) -> float:
        """True rate multiplier theta."""
        return self.theta

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> TrialData:
        """Simulate independent Weibull potential outcomes."""
        gamma = self._draw_gamma(n, n_reps, rng)
        shape = (n_reps, n)
        inv_alpha = 1.0 / self.alpha
        y0 = rng.weibull(self.alpha, shape) * gamma ** (-inv_alpha)
        y1 = rng.weibull(self.alpha, shape) * (
            gamma * self.theta
        ) ** (-inv_alpha)
        return TrialData(gamma, y0, y1)

    def _joint(self, data: TrialData) -> dict[str, np.ndarray]:
        """Joint (alpha, theta) MLE, cached per data payload."""
        if (
            self._joint_cache is None
            or self._joint_cache[0] != id(data)
        ):
            fit = likelihoods.mle_weibull_joint(
                data.y1, data.y0, data.gamma
            )
            self._joint_cache = (id(data), fit)
        return self._joint_cache[1]

    def estimators(
        self,
    ) -> dict[str, Callable[[TrialData], np.ndarray]]:
        """Estimator set depends on whether alpha is known."""

        def tau(d: TrialData) -> np.ndarray:
            return model_free_effect(d.y1, d.y0, transform=np.log)

        if self.alpha_known:
            return {
                "model_free": lambda d: np.exp(-self.alpha * tau(d)),
                "model_based": lambda d: (
                    likelihoods.mle_weibull_known_alpha(
                        d.y1, d.gamma, self.alpha
                    )
                ),
            }
        return {
            "model_free": tau,
            "model_based": lambda d: self._joint(d)["theta"],
            "model_based_alpha": lambda d: self._joint(d)["alpha"],
        }

    def analytic_tau(self, data: TrialData) -> np.ndarray:
        """tau_n = -log(theta)/alpha for every gamma-sample."""
        value = -np.log(self.theta) / self.alpha
        return np.full(data.gamma.shape[0], value)

    def reference_values(self) -> dict[str, float]:
        """Per-estimator targets; tau-scale when alpha is unknown."""
        if self.alpha_known:
            return {
                "model_free": self.theta,
                "model_based": self.theta,
            }
        return {
            "model_free": -np.log(self.theta) / self.alpha,
            "model_based": self.theta,
            "model_based_alpha": self.alpha,
        }


class ExponentialAdditiveModel(_PaperExample):
    """Example 4: exponential rates gamma_i and gamma_i + Delta.

    The paper's key negative example: tau_n (eq. 4.1, log scale)
    depends on the realized gamma-sample, so the model-free estimator
    has NO stable reference value (``nan`` in
    :meth:`reference_values`), while the model-based MLE recovers the
    stable Delta regardless of the gamma-population.
    """

    name = "ex4_exponential_additive"

    def __init__(
        self, baseline: stats.rv_continuous, delta: float
    ) -> None:
        """Configure the model.

        Args:
            baseline: Population of baseline rates gamma_i (> 0).
            delta: True additive rate shift (>= 0, so that all
                treated rates gamma_i + Delta stay positive).

        Raises:
            ValueError: If ``delta`` is negative.
        """
        if delta < 0.0:
            raise ValueError(
                f"delta must be >= 0 to keep rates positive, "
                f"got {delta}"
            )
        super().__init__(baseline)
        self.delta = delta

    @property
    def true_value(self) -> float:
        """True additive rate shift Delta."""
        return self.delta

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> TrialData:
        """Simulate independent exponential potential outcomes."""
        gamma = self._draw_gamma(n, n_reps, rng)
        y0 = rng.exponential(scale=1.0 / gamma)
        y1 = rng.exponential(scale=1.0 / (gamma + self.delta))
        return TrialData(gamma, y0, y1)

    def estimators(
        self,
    ) -> dict[str, Callable[[TrialData], np.ndarray]]:
        """Model-free log-scale tau and the stable model-based MLE."""
        return {
            "model_free": lambda d: model_free_effect(
                d.y1, d.y0, transform=np.log
            ),
            "model_based": lambda d: (
                likelihoods.mle_exponential_additive(d.y1, d.gamma)
            ),
        }

    def analytic_tau(self, data: TrialData) -> np.ndarray:
        """Per-rep -mean(log((gamma_i + Delta) / gamma_i)) (eq. 4.1).

        Follows definition (3.1), treated minus control, matching the
        -log(theta) convention of example 2; the paper prints eq. 4.1
        with the opposite sign. The gamma-sample dependence — the
        point of the example — is identical either way.
        """
        return -np.mean(
            np.log((data.gamma + self.delta) / data.gamma), axis=-1
        )

    def reference_values(self) -> dict[str, float]:
        """No stable reference for the model-free estimator."""
        return {"model_free": np.nan, "model_based": self.delta}


class LogisticAdditiveModel(_PaperExample):
    """Example 5: Bernoulli(expit(gamma_i)) vs Bernoulli(expit(gamma_i+Delta)).

    Like example 4, the model-free tau_n (eq. 4.2, probability scale)
    depends on the gamma-sample except at Delta = 0, while Delta is a
    stable additive effect on the log-odds scale, recovered by an
    offset logistic GLM.
    """

    name = "ex5_logistic_additive"

    def __init__(
        self, baseline: stats.rv_continuous, delta: float
    ) -> None:
        """Configure the model.

        Args:
            baseline: Population of baseline log-odds gamma_i.
            delta: True additive effect on the log-odds scale.
        """
        super().__init__(baseline)
        self.delta = delta

    @property
    def true_value(self) -> float:
        """True log-odds shift Delta."""
        return self.delta

    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> TrialData:
        """Simulate independent Bernoulli potential outcomes."""
        gamma = self._draw_gamma(n, n_reps, rng)
        y0 = rng.binomial(1, expit(gamma)).astype(float)
        y1 = rng.binomial(1, expit(gamma + self.delta)).astype(float)
        return TrialData(gamma, y0, y1)

    def estimators(
        self,
    ) -> dict[str, Callable[[TrialData], np.ndarray]]:
        """Probability-scale model-free tau and offset-GLM MLE."""
        return {
            "model_free": lambda d: model_free_effect(d.y1, d.y0),
            "model_based": lambda d: likelihoods.mle_logistic_offset(
                d.y1, d.gamma
            ),
        }

    def analytic_tau(self, data: TrialData) -> np.ndarray:
        """Eq. 4.2: mean of expit(gamma+Delta) - expit(gamma)."""
        return np.mean(
            expit(data.gamma + self.delta) - expit(data.gamma),
            axis=-1,
        )

    def reference_values(self) -> dict[str, float]:
        """No stable reference for the model-free estimator."""
        return {"model_free": np.nan, "model_based": self.delta}


def make_default_examples(
    population: str = "moderate",
    logodds_population: str = "balanced",
) -> dict[str, PotentialOutcomeModel]:
    """Build the five examples with paper-matching default parameters.

    Args:
        population: Key into :data:`GAMMA_POPULATIONS` used as the
            baseline-rate population for examples 1-4.
        logodds_population: Key into :data:`LOGODDS_POPULATIONS` used
            as the baseline log-odds population for example 5.

    Returns:
        Mapping of model name to a freshly configured instance
        (Delta = 2 for the additive examples, matching the paper's
        example-4 discussion; theta = 0.5, alpha = 2 elsewhere).

    Raises:
        KeyError: If either population key is unknown.
    """
    gamma_dist = GAMMA_POPULATIONS[population]
    logodds_dist = LOGODDS_POPULATIONS[logodds_population]
    models: list[PotentialOutcomeModel] = [
        LinearAdditiveModel(gamma_dist, delta=2.0, sigma=1.0),
        ExponentialMultiplicativeModel(gamma_dist, theta=0.5),
        WeibullMultiplicativeModel(
            gamma_dist, theta=0.5, alpha=2.0, alpha_known=True
        ),
        ExponentialAdditiveModel(gamma_dist, delta=2.0),
        LogisticAdditiveModel(logodds_dist, delta=2.0),
    ]
    return {model.name: model for model in models}
