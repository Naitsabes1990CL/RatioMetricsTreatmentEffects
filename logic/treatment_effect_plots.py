"""Plot helpers for treatment-effect simulation results.

Consumes the tidy DataFrames produced by
:mod:`logic.simulation_engine` (``run_study`` / ``run_scenarios``).
Styling follows a small validated palette: categorical series colors
are assigned in fixed slot order (never cycled), text wears ink tokens
rather than series colors, and grid/axis chrome stays recessive.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#: Fixed-order categorical series colors (validated palette, light
#: mode). Assigned by position, never cycled or re-ranked.
SERIES_COLORS: list[str] = [
    "#2a78d6",  # blue
    "#eb6834",  # orange
    "#1baf7a",  # aqua
    "#eda100",  # yellow
]

_SURFACE = "#fcfcfb"
_INK = "#0b0b0b"
_INK_SECONDARY = "#52514e"
_INK_MUTED = "#898781"
_GRID = "#e1e0d9"
_BASELINE = "#c3c2b7"


def _style_axes(ax: plt.Axes) -> None:
    """Apply recessive chart chrome to one axes object."""
    ax.set_facecolor(_SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(_BASELINE)
    ax.tick_params(colors=_INK_MUTED, labelcolor=_INK_SECONDARY)
    ax.xaxis.label.set_color(_INK_SECONDARY)
    ax.yaxis.label.set_color(_INK_SECONDARY)
    ax.title.set_color(_INK)
    ax.grid(True, axis="x", color=_GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def plot_estimate_stability(
    df: pd.DataFrame,
    title: str = "",
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Jittered per-replication estimates, one row per estimator.

    Each estimator's reference value (the ``true_value`` column) is
    marked with a black tick on its own row; estimators with ``nan``
    reference (the paper's unstable model-free cases) get none.

    Args:
        df: Tidy output of ``run_study`` for a single model.
        title: Optional axes title.
        ax: Existing axes to draw on; a new figure is created when
            omitted.

    Returns:
        The axes drawn on.
    """
    if ax is None:
        _, ax = plt.subplots(
            figsize=(7.0, 2.8), facecolor=_SURFACE
        )
    names = list(df["estimator"].unique())
    rng = np.random.default_rng(0)
    for row, name in enumerate(names):
        sub = df[df["estimator"] == name]
        jitter = rng.uniform(-0.18, 0.18, size=len(sub))
        color = SERIES_COLORS[row % len(SERIES_COLORS)]
        ax.scatter(
            sub["estimate"], row + jitter,
            s=18, color=color, alpha=0.55, linewidths=0,
        )
        ref = sub["true_value"].iloc[0]
        if np.isfinite(ref):
            ax.scatter(
                [ref], [row], marker="|", s=420,
                color=_INK, zorder=3,
            )
    ax.set_yticks(range(len(names)), names)
    ax.set_ylim(-0.6, len(names) - 0.4)
    ax.set_xlabel("estimate")
    if title:
        ax.set_title(title, loc="left", fontsize=11)
    _style_axes(ax)
    return ax


def plot_population_sensitivity(
    df: pd.DataFrame,
    true_value: float | None = None,
    quantiles: tuple[float, float] = (0.05, 0.95),
    title: str = "",
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Dot-range plot of estimates across scenarios and estimators.

    Shows, per scenario row and estimator color, the mean estimate
    (dot) and a quantile range (line) — the headline figure for the
    paper's "two extreme gamma-populations" argument and the iROAS
    negativization-depth sweep.

    Args:
        df: Tidy output of ``run_scenarios``.
        true_value: Optional stable reference drawn as a dashed
            vertical line (omit when no stable target exists).
        quantiles: Lower/upper quantiles for the range line.
        title: Optional axes title.
        ax: Existing axes to draw on; created when omitted.

    Returns:
        The axes drawn on.
    """
    scenarios = list(df["scenario"].unique())
    estimators = list(df["estimator"].unique())
    if ax is None:
        height = 1.0 + 0.55 * len(scenarios)
        _, ax = plt.subplots(
            figsize=(7.0, height), facecolor=_SURFACE
        )
    offsets = np.linspace(0.22, -0.22, len(estimators))
    for k, est in enumerate(estimators):
        color = SERIES_COLORS[k % len(SERIES_COLORS)]
        for row, scen in enumerate(scenarios):
            vals = df[
                (df["scenario"] == scen) & (df["estimator"] == est)
            ]["estimate"].dropna()
            lo, hi = np.quantile(vals, quantiles)
            y = row + offsets[k]
            ax.plot([lo, hi], [y, y], color=color, linewidth=2)
            ax.scatter(
                [vals.mean()], [y], s=34, color=color, zorder=3
            )
        ax.plot([], [], color=color, linewidth=2, label=est)
    if true_value is not None and np.isfinite(true_value):
        ax.axvline(
            true_value, color=_INK_MUTED, linestyle="--",
            linewidth=1, zorder=1,
        )
    ax.set_yticks(range(len(scenarios)), scenarios)
    ax.set_ylim(len(scenarios) - 0.5, -0.5)
    ax.set_xlabel("estimate")
    if len(estimators) > 1:
        # Reason: a single series needs no legend box — the title
        # names it.
        ax.legend(
            frameon=False, fontsize=8, labelcolor=_INK_SECONDARY,
            loc="best",
        )
    if title:
        ax.set_title(title, loc="left", fontsize=11)
    _style_axes(ax)
    return ax


def plot_geo_ratio_diagnostics(
    gamma: np.ndarray,
    dr: np.ndarray,
    dc: np.ndarray,
    true_value: float | None = None,
    ylim_quantiles: tuple[float, float] = (0.005, 0.995),
    title: str = "",
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Per-geo ratio dR/dC against geo size (log x), one replication.

    Visualizes the "explosive small-geo ratios" mechanism: with a
    revenue-noise floor, tiny geos' incremental costs are tiny while
    their noise is not, so their per-geo ratios scatter wildly.

    Args:
        gamma: Geo sizes for one replication, shape ``(n,)``.
        dr: Revenue differences, shape ``(n,)``.
        dc: Cost differences, shape ``(n,)``.
        true_value: Optional true iROAS, drawn as a dashed line.
        ylim_quantiles: Quantiles used to clip the y-axis so a few
            extreme ratios do not flatten the display.
        title: Optional axes title.
        ax: Existing axes to draw on; created when omitted.

    Returns:
        The axes drawn on.
    """
    if ax is None:
        _, ax = plt.subplots(
            figsize=(7.0, 3.2), facecolor=_SURFACE
        )
    ratios = dr / dc
    ax.scatter(
        gamma, ratios, s=18, color=SERIES_COLORS[0],
        alpha=0.55, linewidths=0,
    )
    if true_value is not None and np.isfinite(true_value):
        ax.axhline(
            true_value, color=_INK_MUTED, linestyle="--",
            linewidth=1,
        )
    ax.set_xscale("log")
    lo, hi = np.quantile(ratios, ylim_quantiles)
    pad = 0.08 * (hi - lo)
    ax.set_ylim(lo - pad, hi + pad)
    ax.set_xlabel("geo size (log scale)")
    ax.set_ylabel("per-geo ΔR / ΔC")
    if title:
        ax.set_title(title, loc="left", fontsize=11)
    _style_axes(ax)
    ax.grid(True, axis="y", color=_GRID, linewidth=0.8)
    return ax
