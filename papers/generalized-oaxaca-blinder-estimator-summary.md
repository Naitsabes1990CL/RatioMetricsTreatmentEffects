# Summary: "The Generalized Oaxaca-Blinder Estimator" (Kevin Guo & Guillaume Basse, 2020)

## Key Insights

- The paper generalizes Lin's (2013) "interactions" regression-adjustment
  estimator — which uses OLS with treatment-by-covariate interactions to
  estimate the average treatment effect (ATE) in a randomized experiment — to
  **any sufficiently "simple" nonlinear regression model** (logistic, Poisson,
  transformed-outcome OLS, isotonic regression, and broad classes of
  parametric M-estimators), while preserving the four properties that make
  Lin's estimator attractive: (1) rigorous statistical inference, (2)
  robustness to model misspecification, (3) validity from randomization alone
  (no superpopulation/i.i.d. sampling assumption needed), and (4)
  computational simplicity.
- The key reinterpretation: Lin's estimator is algebraically equivalent to
  the classical econometric **Oaxaca-Blinder decomposition** — fit separate
  outcome models in the treatment and control arms, use them to **impute the
  missing potential outcome** for every unit, and average the imputed
  treatment/control differences. Framing it as an imputation method (rather
  than a regression coefficient) immediately suggests plugging in *any*
  prediction model µ̂₁, µ̂₀ in place of linear OLS — this is the "generalized
  Oaxaca-Blinder" (GOB) estimator, defined via Algorithm 1.
- Validity (consistency + asymptotic normality + a valid confidence interval)
  holds under **randomization inference alone** — treating potential outcomes
  and covariates as fixed and only the treatment assignment as random — as
  long as the plugged-in models satisfy three abstract conditions:
  **prediction unbiasedness** (in-sample average prediction equals in-sample
  average outcome — "calibration"), **stability** (the fitted model converges
  to some fixed population-level function), and **typically simple
  realizations** (a Donsker-type complexity/entropy-integral condition
  bounding how complex the fitted model usually is).
- Prediction unbiasedness is nearly automatic: canonical-link GLMs (linear,
  logistic, Poisson regression) satisfy it exactly from their first-order
  conditions; any other model can be forced to satisfy it via a simple
  **debiasing correction** or by using fitted values as a covariate in a
  second-stage OLS regression ("OLS2"), which the authors recommend in
  practice.
- **Nonlinear covariate adjustment can substantially reduce confidence
  interval width relative to OLS/Lin adjustment** when the nonlinear model
  fits the outcome better — demonstrated empirically with ~45% shorter
  intervals using Poisson regression on count outcomes, and smaller but
  real gains (78 vs. 106-unit average CI width) using a log-link/OLS2
  approach on skewed (traffic fatality) outcomes.
- Unlike Lin's original noninferiority guarantee (never worse than the
  unadjusted Neyman estimator), the generalized method gives **no universal
  noninferiority guarantee** — it's "the price of generality," since the
  class of permissible models is broad enough to include some that could, in
  principle, hurt precision (isotonic regression is a notable exception that
  *does* retain noninferiority, since its function class contains the
  constant fit).
- Directly relevant to **ratio metrics / treatment effect estimation**: the
  paper explicitly discusses the case of skewed, log-transformed outcomes
  (§4.3) and shows that naively exponentiating a log-scale regression
  coefficient does **not** recover the additive ATE on the original scale
  without further distributional assumptions — the correct fix is to use the
  model's *fitted values* (via debiasing or a second-stage OLS) as the
  imputation function in the GOB/Oaxaca-Blinder recipe, rather than
  interpreting the log-scale coefficient directly as the causal effect. This
  is a direct, actionable template for constructing valid, randomization-
  robust confidence intervals for treatment effects on outcomes that are
  naturally modeled multiplicatively/on a ratio scale (counts, skewed
  continuous outcomes), which is squarely the use case of this project.
- The method requires no assumption that experimental units are a random
  sample from a superpopulation — a point of close conceptual alignment with
  the companion paper in this project's `papers/` folder (Battey & Edgar,
  "Treatment Effect: A Critique"), which also stresses that treatment-effect
  inference should not lean on fictitious superpopulation sampling
  assumptions; here, however, the target estimand is explicitly the
  model-free finite-population average treatment effect τₙ, estimated via a
  model-based imputation device — a different resolution of model-based vs.
  model-free concerns than Battey & Edgar advocate.

## Section-by-Section Summary

### 1 Introduction

**1.1 Motivation.** Motivates covariate adjustment for precision in completely
randomized experiments. Reviews Lin's (2013) "interactions" estimator: fit OLS
of Y on treatment Z, centered covariates x, and their interaction (eq. 1);
the coefficient τ̂ on Z is the adjusted ATE estimator. **Theorem 1 (Lin's
result, informal):** if min(n₁,n₀) ≫ d (sample sizes in each arm large
relative to covariate dimension), √n(τ̂−τ) is asymptotically N(0,σ²), τ̂ is at
least as efficient as Neyman's unadjusted difference-in-means estimator, and
Huber-White robust-SE confidence intervals are valid — using **only** the
assumption that treatment is completely randomized (no superpopulation
sampling assumption), unlike earlier work (Yang & Tsiatis, 2001). The authors
note this has been extended to other designs and high-dimensional regression,
but ask whether an analogous guarantee exists for **nonlinear** models (useful
for binary, count, or skewed outcomes). They define four desiderata any such
method should have: (1) rigorous statistical inference, (2) robustness to
misspecification, (3) randomization-based validity (no superpopulation
sampling needed), (4) computational simplicity — and argue that no existing
proposal (Rosenbaum's randomization test inversion; Wu & Gagnon-Bartsch's
leave-one-out estimator; the doubly-robust literature) satisfies all four
simultaneously for general nonlinear models.

**1.2 The potential outcomes model.** Sets up the Neyman-Rubin finite-
population framework: n units, each with a fixed triple (y₁ᵢ, y₀ᵢ, xᵢ)
(potential outcomes under treatment/control, and covariates), no interference
across units (SUTVA). The target is the **finite-sample ATE** τ = (1/n)Σ(y₁ᵢ
− y₀ᵢ). Only the treatment vector (Z₁,...,Zₙ) is random, drawn uniformly
from binary vectors with exactly n₁ ones (completely randomized design); the
observed outcome Yᵢ = Zᵢy₁ᵢ + (1−Zᵢ)y₀ᵢ is the only source of randomness.

### 2 Generalizing Oaxaca-Blinder

**2.1 Beyond linear adjustment.** Re-derives Lin's estimator as an imputation
procedure: when covariates are centered, fitting model (1) is equivalent to
running two separate OLS regressions — θ̂₁ on the treated units, θ̂₀ on
controls — and imputing the missing potential outcome for each unit via
ŷₜᵢ = yₜᵢ if Zᵢ=t, else θ̂ₜᵀxᵢ (eq. 3); τ̂ = mean(ŷ₁ᵢ − ŷ₀ᵢ). This
"double-imputation" procedure is the classical econometric **Oaxaca-Blinder**
method (Oaxaca 1973; Blinder 1973). This reframing motivates the paper's main
proposal, the **Generalized Oaxaca-Blinder (GOB) method, Algorithm 1**: fit
any regression model µ̂₁ on the treated subsample to predict y₁ from x; use it
to impute unobserved y₁ᵢ for controls (eq. 4); symmetrically fit µ̂₀ on
controls and impute unobserved y₀ᵢ for the treated (eq. 5); return τ̂ = mean
of imputed differences (eq. 6/eq. 10 equivalent form τ̂ = mean[µ̂₁(xᵢ) −
µ̂₀(xᵢ)]). Notes this basic idea has independently arisen across many fields
(education, epidemiology, survey sampling, econometrics) but prior theory
required superpopulation sampling assumptions, except for linear/logistic
special cases.

**2.2 Prediction unbiasedness.** Introduces **Definition 1 (prediction
unbiasedness):** a model µ̂ₜ is prediction unbiased if its average fitted
value on its own training subsample exactly equals the average outcome on
that subsample (eq. 6) — called "calibration" in survey sampling. Canonical-
link GLMs (OLS, logistic, Poisson) satisfy this automatically via their
first-order conditions. Any model can be made prediction unbiased via a
**debiasing correction** (eq. 7: subtract the estimated bias) or by using the
fitted values as a single covariate in a second-stage OLS regression (eq. 8,
"OLS2") — the first-order condition of the OLS2 regression guarantees
unbiasedness. Notes the debiased GOB estimator is algebraically equivalent to
the augmented inverse-propensity-weighted (AIPW) estimator with known/
constant propensity, and to the "generalized difference estimator" /"model
calibration estimator" from survey sampling — but argues the imputation
framing is the most intuitive for randomized experiments.

**2.3 Statistical inference.** States the headline large-sample confidence
interval (eq. 9): τ̂ ± z₁₋α/2·√(MSȆ(1)/n₁ + MSȆ(0)/n₀), where MSȆ(t) is the
in-sample mean-squared residual of model µ̂ₜ. When µ̂ₜ is a constant (the
subsample mean), this recovers Neyman's classical interval for the
difference-in-means estimator. When both models are linear, (9) is
asymptotically equivalent to Lin's robust-SE interval. Hence: **better-fitting
nonlinear models produce narrower intervals.**

**2.4 An illustration.** Empirical demonstration using the `Fatalities`
dataset (US traffic deaths, 1982–1988) with a fictional randomized
intervention. Poisson regression (appropriate for count data) is compared to
Lin's OLS interactions estimator across 50,000 re-randomizations. Both
estimators are approximately normal in their randomization distribution, but
the **Poisson GOB estimator is far more efficient**: 95% CIs were ~45%
shorter on average, with both intervals achieving approximately nominal
coverage. Gives the exact 4-line R implementation, exploiting (i) the
simplified formula (10) for prediction-unbiased models and (ii) that the CI
can be computed from a two-sample t-test on the two models' residuals.

### 3 Theoretical results

Sets up asymptotics as a triangular array of growing finite populations with
fixed covariate dimension d and treated fraction pₙ bounded away from 0, 1.

**3.1 Consistency.** Builds intuition via the Poisson example: since treated/
control subsamples are effectively random subsamples of the full population,
the sample-restricted M-estimate θ̂ₜ should be close to the "population"
M-estimate θ*ₜ (eq. 11–12), giving the heuristic argument that mean(ŷₜᵢ) ≈
mean(yₜᵢ) for both arms, hence τ̂ₙ ≈ τₙ. Formalizes the needed condition as
**Definition 2 (stability):** a sequence of fitted functions {µ̂ₙ} is stable
if it converges (in a root-mean-square sense over the population's covariate
values, eq. 13) to some deterministic sequence {µ*ₙ}. **Theorem 2
(Consistency):** if µ̂₁,ₙ and µ̂₀,ₙ are both stable and prediction-unbiased,
and the population-level MSE of each population limit function is o(n), then
τ̂ₙ − τₙ →ᵖ 0. This holds for *any* choice of valid population-limit
sequences. **Example 1** proves OLS regression is stable under mild moment
conditions (bounded 4th moments of x and y, invertible limiting covariance).

**3.2 Asymptotic normality.** Introduces the extra condition needed:
**Definition 3 (typically simple realizations):** {µ̂ₙ} has typically simple
realizations if it usually lies in a function class Fₙ with a finite uniform
entropy integral (eq. 15) — a Donsker-type complexity condition, weaker than
the classical triangular-array Donsker property since it doesn't require
marginal convergence n₁/n → p. **Example 2** verifies this for OLS. **Theorem
3 (Asymptotically linear expansion):** under the Theorem 2 conditions plus
typically simple realizations, the imputed-mean differences mean(ŷ₁ᵢ−y₁ᵢ) and
mean(ŷ₀ᵢ−y₀ᵢ) are each asymptotically equal to a sample average of mean-zero
residual terms ε*₁ᵢ, ε*₀ᵢ (eq. 16–17), plus a negligible remainder — i.e., τ̂ₙ
behaves like a simple average, enabling use of the completely-randomized CLT.
**Corollary 1 (Asymptotic normality):** under Theorem 3 plus boundedness
conditions on the residual 4th moments and the residual correlation ρ staying
away from −1, √n(τ̂ₙ−τₙ)/σₙ →ᵵ N(0,1), with σₙ² expressed via MSE(1), MSE(0),
and the residual covariance. Notes, unlike Lin's result, **no noninferiority
guarantee** holds in general (price of generality), though the authors could
not construct a realistic counterexample for logistic regression.

**3.3 Confidence intervals.** Since σₙ is not identifiable, uses Neyman's
classical **conservative upper bound** (eq. 19): nσₙ² ≤ MSE(1)/p + MSE(0)/
(1−p). **Theorem 4 (Confidence intervals):** under the prior assumptions plus
bounded 4th moments of residuals, the interval in eq. (21) (same form as eq.
9, using in-sample residual-variance estimates, eq. 20) is asymptotically
conservative (coverage ≥ 1−α), and exactly 1−α under a true null effect with
matched estimation methods for µ̂₁, µ̂₀.

**3.4 Extensions.** Briefly notes the asymptotically-linear-expansion
machinery (Theorem 3) should extend to Mahalanobis rerandomization designs
(via Li & Ding 2020) and to smooth functions of imputed means via the delta
method (e.g., odds-ratio GOB estimators) — left as future work.

### 4 Examples

Verifies the stability/prediction-unbiasedness/typically-simple-realizations
conditions for four concrete model classes chosen to cover binary, count,
skewed, and nonlinear-monotone outcome settings.

**4.1 Logistic regression.** Motivates nonlinear adjustment for binary
outcomes (linear imputation can produce predictions outside [0,1]).
**Theorem 5:** given existence of a well-behaved "population" logistic MLE
θ*₁,ₙ (eq. 22), bounded 4th moments of x, and a Fisher information bound
∇²Lₙ(θ*₁,ₙ) ⪰ λmin·I, the fitted logistic model satisfies Theorem 3's
conditions. Discusses pathologies that can violate these assumptions even
when the "population" MLE exists: near-perfect separation or near-perfect
collinearity in a subsample can make the sample MLE fail to exist entirely in
many randomizations — diagnosable via fitted values near 0/1 or unnaturally
large SEs.

**4.2 Poisson regression.** **Theorem 6:** analogous result for Poisson
regression (eq. 23), requiring additionally that ||xᵢ||, the outcome's second
moment, and the population MSE are uniformly bounded (stronger than the
logistic case, because these quantities aren't automatically bounded for
count data as they are for binary data) plus a Fisher-information curvature
bound. Notes covariates are typically log-transformed in practice, making
boundedness more plausible.

**4.3 Transformed-outcome regression.** Addresses skewed outcomes (e.g. wage
data, as in the original Oaxaca 1973 paper), which often fit better after a
log transform. Key point: naively reporting the coefficient from Lin's
estimator fit on log(y) does **not** recover the ATE on the original scale —
even under strong i.i.d. assumptions, E[log yₜᵢ|xᵢ] = θᵗxᵢ does not pin down
E[y₁ᵢ−y₀ᵢ] without further distributional assumptions. Two fixes avoid
needing those assumptions: (i) fit θ̂ₜ on the log scale, then use the
**debiased** exponentiated model µ̂ᵗᵃᵇ (eq. 24) in the GOB recipe; (ii) fit
θ̂ₜ on the log scale, then use exp(θ̂ᵗxᵢ) as a covariate in a second-stage OLS
(eq. 25, "OLS2") — the authors' **recommended** approach, since it has an
extra degree of freedom (β̂₁) that better matches model fit (illustrated with
the lognormal-error case, where the OLS2 approach can recover the correct
multiplicative bias factor β₁=exp(σ²/2) that the plain debiased/exponentiated
model misses). **Theorem 7:** under bounded-moment and invertibility
conditions, both the debiased estimator and the OLS2 estimator satisfy
Theorem 3's conditions. Empirically (same Fatalities dataset), OLS2 gives the
narrowest average 95% CI (78 fatalities) vs. debiased (84) vs. plain OLS/Lin
on log scale (106), all with approximately nominal coverage.

**4.4 Isotonic regression.** For a single covariate (d=1) and bounded outcome,
with an expected monotone relationship, considers isotonic regression (eq.
26: least-squares fit over nondecreasing functions, using the piecewise-
linear representative of the (non-unique) isotonic solution). **Theorem 8:**
under almost no additional assumptions, isotonic regression fitted functions
satisfy Theorem 3's conditions. Because the isotonic function class contains
all constants, the GOB estimator built from two isotonic fits inherits Lin's
**noninferiority property**: its CI is never wider than Neyman's unadjusted
interval. However, a simulation shows the naive in-sample MSE badly
underestimates the true MSE for isotonic regression (overfitting from the
large effective degrees of freedom of the isotonic class), requiring ~600
samples per arm before 95% CIs reach >93% coverage — smoothed isotonic
variants are suggested as a possible remedy.

### 5 Extension: a generic recipe for parametric models

Provides a "master theorem" to streamline verifying the paper's conditions
for new parametric M-estimation models. **Assumption A1 (convex loss):** θ̂ₙ
solves a convex empirical-risk-minimization problem (eq. 27) on one
treatment arm. **Assumption A2 (existence/stability of population optima):**
a population-level minimizer θ*ₙ exists and the population loss has a
strictly-increasing growth bound away from θ*ₙ (eq. 28) — ensuring a well-
separated, unique minimizer; **Lemma 1** shows this follows from a uniform
positive lower bound on the Hessian (curvature) of the population loss near
θ*ₙ. **Assumption A3 (smooth loss):** a Lipschitz-type smoothness bound on
the loss near θ*ₙ (eq. 29). **Theorem 9 (General results for parametric
models):** under A1–A3, θ̂ₙ →ᵖ θ*ₙ; if additionally the map θ↦µ_θ is Lipschitz
near θ*ₙ, then the induced sequence of fitted regression functions is both
stable and has typically simple realizations — i.e., automatically eligible
for use in the GOB method with valid inference.

### 6 Conclusion

Summarizes the core idea in one sentence: "fill in the missing outcomes with
an unbiased prediction model," built on the theoretical insight that
randomization of treatment alone (via empirical process theory) is enough to
justify the method even when all other population quantities are treated as
fixed/nonrandom. Flags the main open question: whether the Donsker-type
"typically simple realizations" condition can be relaxed, as can be done
under i.i.d.-superpopulation sampling assumptions via sample splitting
(citing Chernozhukov et al. 2018; Wager et al. 2016) — unclear whether an
analogous relaxation exists purely within Neyman's finite-population
randomization model (early evidence from Wu & Gagnon-Bartsch 2018's "loop"
estimator suggests it might be possible, but proving stability for such
complex models remains open).

### 7 Appendix: Proofs

Technical appendix containing the proofs omitted from the main text,
including a **randomization law of large numbers** (Lemma 2, built on a
variance formula from Freedman 2008a and Chebyshev's inequality) and a
**maximal inequality** (Proposition 1) used to control the uniform-
convergence arguments underlying the stability and typically-simple-
realizations proofs throughout Sections 3–5.
