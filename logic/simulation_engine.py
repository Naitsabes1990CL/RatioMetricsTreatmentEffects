"""Generic Monte Carlo engine for treatment-effect simulations.

Defines the contract every data-generating process implements
(:class:`PotentialOutcomeModel`), the generic model-free estimator of
Battey & Edgar (2026, eq. 3.1), and the study runners that turn a model
into tidy result DataFrames. The engine never introspects the data
payload a model produces: it only forwards it to the model's own named
estimator callables, so models with arbitrary data shapes (single
outcome, ratio metrics, ...) plug in without engine changes.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

import numpy as np
import pandas as pd


class PotentialOutcomeModel(ABC):
    """Contract for a simulated potential-outcomes experiment.

    A concrete model bundles a data-generating process, its named
    estimators, and (where available) the closed-form analytic value of
    the model-free estimand tau_n for the realized baseline sample.

    Attributes:
        name: Human-readable model identifier used in result frames.
    """

    name: str = "unnamed-model"

    @property
    @abstractmethod
    def true_value(self) -> float:
        """True target parameter on its natural scale."""

    @abstractmethod
    def draw(
        self, n: int, n_reps: int, rng: np.random.Generator
    ) -> Any:
        """Draw ``n_reps`` replications of ``n`` units, vectorized.

        Args:
            n: Number of units per replication.
            n_reps: Number of Monte Carlo replications.
            rng: NumPy random generator.

        Returns:
            An opaque data payload understood by this model's own
            estimator callables (arrays shaped ``(n_reps, n)``).
        """

    @abstractmethod
    def estimators(self) -> dict[str, Callable[[Any], np.ndarray]]:
        """Named estimators mapping a data payload to per-rep estimates.

        Returns:
            Mapping of estimator name to a callable that takes the
            payload returned by :meth:`draw` and returns an array of
            shape ``(n_reps,)`` with one estimate per replication.
        """

    def analytic_tau(self, data: Any) -> np.ndarray | None:
        """Closed-form tau_n for the realized baseline sample, if any.

        Args:
            data: Payload returned by :meth:`draw`.

        Returns:
            Per-replication analytic values of the model-free estimand
            (eq. 3.1, on its transformed scale), or ``None`` when no
            closed form is implemented.
        """
        return None

    def reference_values(self) -> dict[str, float]:
        """Per-estimator reference values for comparison plots.

        Returns:
            Mapping of estimator name to the value that estimator is
            expected to recover. Defaults to :attr:`true_value` for
            every estimator; models may override (``nan`` marks an
            estimator with no stable reference — the paper's unstable
            model-free cases).
        """
        return {name: self.true_value for name in self.estimators()}


def model_free_effect(
    y1: np.ndarray,
    y0: np.ndarray,
    transform: Callable[[np.ndarray], np.ndarray] | None = None,
    axis: int = -1,
) -> np.ndarray:
    """Empirical plug-in for the model-free effect (eq. 3.1).

    Computes the average difference in (optionally transformed)
    potential outcomes, vectorized over leading axes.

    Args:
        y1: Treated potential outcomes, shape ``(..., n)``.
        y0: Control potential outcomes, shape ``(..., n)``.
        transform: Optional monotone transform (e.g. ``np.log``)
            applied to both arrays before differencing.
        axis: Axis indexing units within one replication.

    Returns:
        Average transformed outcome difference per replication.
    """
    if transform is not None:
        y1 = transform(y1)
        y0 = transform(y0)
    return np.mean(y1 - y0, axis=axis)


def run_study(
    model: PotentialOutcomeModel,
    n: int,
    n_reps: int,
    seed: int | np.random.Generator,
) -> pd.DataFrame:
    """Run one Monte Carlo study for a single model.

    Args:
        model: The data-generating process with its estimators.
        n: Number of units per replication.
        n_reps: Number of replications.
        seed: Integer seed or an existing generator.

    Returns:
        Tidy long DataFrame with columns ``model``, ``estimator``,
        ``rep``, ``n``, ``estimate``, ``analytic_tau`` (``nan`` when
        no closed form exists) and ``true_value`` (that estimator's
        reference value; ``nan`` marks "no stable reference").
    """
    rng = np.random.default_rng(seed)
    data = model.draw(n=n, n_reps=n_reps, rng=rng)
    tau = model.analytic_tau(data)
    if tau is None:
        tau_col = np.full(n_reps, np.nan)
    else:
        tau_col = np.broadcast_to(
            np.asarray(tau, dtype=float), (n_reps,)
        )
    references = model.reference_values()
    frames = []
    for est_name, est_fn in model.estimators().items():
        estimates = np.asarray(est_fn(data), dtype=float)
        frames.append(
            pd.DataFrame(
                {
                    "model": model.name,
                    "estimator": est_name,
                    "rep": np.arange(n_reps),
                    "n": n,
                    "estimate": estimates,
                    "analytic_tau": tau_col,
                    "true_value": references.get(est_name, np.nan),
                }
            )
        )
    return pd.concat(frames, ignore_index=True)


def run_scenarios(
    scenarios: dict[str, PotentialOutcomeModel],
    n: int,
    n_reps: int,
    seed: int,
) -> pd.DataFrame:
    """Run several named scenarios and stack the tidy results.

    Each scenario receives an independent child generator spawned from
    one parent seed, so scenarios are individually reproducible and
    may later be parallelized without changing this API.

    Args:
        scenarios: Mapping of scenario label to configured model.
        n: Number of units per replication.
        n_reps: Number of replications per scenario.
        seed: Parent seed for the spawned child generators.

    Returns:
        Concatenation of :func:`run_study` results with an extra
        leading ``scenario`` column.
    """
    parent = np.random.default_rng(seed)
    children = parent.spawn(len(scenarios))
    frames = []
    for (label, model), child in zip(scenarios.items(), children):
        df = run_study(model, n=n, n_reps=n_reps, seed=child)
        df.insert(0, "scenario", label)
        frames.append(df)
    return pd.concat(frames, ignore_index=True)
