# Summary: "Treatment Effect: A Critique" (Battey & Edgar, 2026)

## Key Insights

- There are **two fundamentally different definitions of "treatment effect"** in
  statistics: (1) a **model-based** definition, where the treatment effect is a
  stable *parameter* of a statistical model (Fisher's tradition, formalised by
  McCullagh, 2002); and (2) a **model-free** definition, where the treatment
  effect is a *population-level average difference* in (counterfactual)
  outcomes (Neyman/Rubin tradition, the basis of most modern causal inference).
- These two definitions can give **strikingly different answers**, even under
  the most favourable possible scenario for the counterfactual approach: a
  fictitious world where both potential outcomes are actually observable (no
  missing-data problem, no confounding, no identification issues at all).
- Using five worked examples (linear, exponential, Weibull, exponential with
  additive rate shift, logistic), the authors show the model-free average
  effect (3.1) **agrees with the stable model parameter only in special cases**
  (e.g., additive linear models). In other common models (e.g., logistic
  regression, rate-shifted exponentials) the model-free average depends on the
  particular sample of individuals drawn — i.e., it is **not stable** and does
  **not generalise** to new populations, even though a perfectly stable,
  well-defined treatment effect exists in the underlying model.
- They give precise **necessary and sufficient conditions** under which the two
  definitions coincide for every sample: the treatment must act as a group
  transformation on the baseline distribution, that action must correspond to
  the same transformation on the observations, and no other nuisance
  parameters may enter the relevant expectation.
- The paper **clarifies a historical misattribution**: "Fisher's sharp null"
  (Y_i(1) = Y_i(0) for all i) is a misnomer; Fisher's actual position was
  **unit treatment additivity** on an appropriate scale (a model-based idea),
  not the model-free sharp-null hypothesis.
- Core argument/critique: model-free average effects, by allowing treatment
  effects to vary arbitrarily across individuals, trade away the stability
  that makes scientific generalisation possible. If treatment effects truly
  differ systematically across units, the authors argue (following Cox) that
  this heterogeneity should be **explained within a model** (e.g., via
  interaction terms), not absorbed into an unstable average.
- Model misspecification is acknowledged as the main legitimate weakness of
  the model-based approach, but the authors note that under misspecification
  the model-free approach also loses stability — so this is not a decisive
  argument in favour of model-free methods.
- Double robustness, often cited as a strength of the counterfactual framework,
  is only a meaningful property if the model-free target (τ_n) is itself an
  appropriate estimand — which is precisely what the paper disputes.

## Section-by-Section Summary

### 1. Introduction
Establishes that causal inference is often treated as synonymous with the
counterfactual/potential-outcomes framework (Rubin, 1974; Rosenbaum & Rubin,
1983), which has grown in popularity partly due to double robustness (Robins
et al., 1994). The paper revisits McCullagh's (2002) question "what is a
treatment effect?" and focuses specifically on *how the effect of treatment is
measured* — not on whether counterfactual effects can be identified or
consistently estimated. The authors attribute the model-based definition of
treatment effect to Fisher (who coined "parameter" in its modern sense),
correcting a historical misnomer per Bailey (2017). Their position echoes Cox
(1958b, 2012), who questioned model-free averages as inference targets when
conclusions must generalise beyond the observed sample.

### 2. Model-based treatment effect
**2.1 Introduction.** Describes the standard parametric setup: data are random
variables drawn from a distribution in a parametrised family P_Θ. The guiding
principle is that the model should capture *commonalities* across units via
stable parameters, so that conclusions generalise to unobserved units. A
treatment parameter is one such stable parameter. References McCullagh (2002)
for formal principles of model construction, noting that the plain textbook
definition of a statistical model permits "plainly absurd" cases unless
further structure is imposed.

**2.2 McCullagh's formalisation.** Formalises treatment effect as a group
action G acting on baseline distributions {P_γ : γ ∈ Γ} via the baseline
parameter space (G × Γ → Γ). Example group actions: addition (Γ = ℝ, additive
treatment effect) or multiplication (Γ = ℝ⁺, multiplicative effect). The null
effect corresponds to the group identity element. Comparability of individuals
i and i′ requires their baseline and treated-outcome distributions to match
(equation 2.1). Under this structure, linear regression (γ = w^Tβ) and
log-linear/multiplicative regression (γ = exp(w^Tβ)) emerge as standard special
cases. Interactions between treatment and individual-level covariates can be
incorporated while preserving parameter stability (McCullagh, 2022, pp.
232–240).

### 3. Model-free treatment effect and counterfactuals
Defines the standard model-free average treatment effect τ_n = (1/n)Σ E(Y_i(1)
− Y_i(0)) over potential outcomes. Since only one of Y_i(1), Y_i(0) is ever
observed for a given i, estimation relies on either (a) imputing the missing
counterfactual via an outcome model, or (b) propensity-score reweighting
(Rosenbaum & Rubin, 1983), modelling the treatment assignment instead. Under
no unmeasured confounding plus further assumptions, an observable statistic
τ̂_n estimates τ_n. Notes that even when Imbens & Rubin (2015) use "outcome
models," these only serve as nuisance tools for estimating the model-free
estimand τ_n — a different usage of "model" than in §2.

### 4. Some prompts for reflection
**4.1 Two aspects.** Distinguishes concerns about (i) the *credibility* of
causal claims/untestable assumptions (covered elsewhere, e.g. Dawid 2000;
not falsifiable per Popper) from (ii) *how the effect is measured* — the focus
of this paper, which can be studied independently of (i).

**4.2 Fictitious idealisation.** To strip away identification/observability
issues, the authors imagine both potential outcomes are actually observed (a
matched-pair design with each individual twinned with a perfect copy, one
twin treated, one control). This is the *most favourable* case for the
counterfactual formulation, isolating purely how (3.1) relates to a stable
model-based treatment parameter.

**4.3 Five examples.** Works through five generative models under the
fictitious idealisation:
1. **Linear, additive errors** (Y_i0 = γ_i + ε_i, Y_i1 = γ_i + Δ + ε_i): the
   model-free τ_n exactly recovers the model-based Δ — the two definitions
   agree perfectly (links to unit treatment additivity, Fisher's early
   design-of-experiments work).
2. **Exponential rates** (rates γ_i and γ_iθ): on the log scale, τ_n = −log θ,
   compatible with the model-based multiplicative effect θ.
3. **Weibull extension** (shape α, rate effect θ): τ_n after log transform
   equals −log θ/α — effect is only identified up to sign/scale unless α is
   known; "semi-compatible," stable but scale-confounded.
4. **Exponential with additive rate shift** (rates γ_i, γ_i+Δ): τ_n = average
   of log((γ_i+Δ)/γ_i), which depends heavily on the sample's γ_i values —
   e.g., huge if γ_i near zero, tiny if γ_i large. Demonstrates that a
   perfectly stable model-based effect Δ maps to a wildly *unstable*,
   sample-dependent model-free estimand. Quotes Bailey (2017) that
   experimental units are essentially never literal random samples from a
   fixed population, undermining the "representative sampling" defence.
5. **Logistic/binary outcomes** (Bernoulli with logits γ_i and γ_i+Δ): τ_n
   (eq. 4.2) again depends intricately on the sample's γ_i except at Δ=0 —
   same instability as example 4.

Gives **three necessary-and-sufficient conditions** for model-based and
model-free definitions to coincide for *any* sample: (1) the group action on
baseline distributions transforms P_γ to P_gγ; (2) that action corresponds to
the same group action on the observations; (3) no other nuisance parameters
enter the relevant expectation besides γ. Violation of any condition makes
(3.1) depend on nuisance parameters/sample composition — these conditions
jointly imply the model belongs to a *transformation family*.

**4.4 Clarification of Fisher's position.** Explains that "Fisher's sharp
null" (Y_i(1)=Y_i(0) ∀i) is a misnomer corrected by Bailey (2017): Fisher's
real position was **unit treatment additivity** on an appropriate (possibly
transformed) scale — a model-based notion, not a model-free sharp null. This
also resolves Holland's (1983) confusion about Cox's position. McCullagh's
framework unifies these early ideas with the other examples. The last two
examples of §4.3 show that the (model-free) sharp null is typically violated
even under the fictitious idealisation where counterfactuals are observable.

### 5. Differing positions
Lays out and responds to three common arguments for the model-free definition:
- **A.1** It allows treatment effects to vary by individual. The authors
  counter that heterogeneity should be *explained* via model structure (e.g.
  interactions on an appropriate scale, as in example 5 of §4.3 — stable
  additive effect on the log-odds scale), not folded into an unstable average;
  cites Ding & Dasgupta (2016) on unrealistic constant-effect assumptions for
  binary outcomes, agreeing with their empirical point but disagreeing with
  their conclusion.
- **A.2** It needs no outcome model. Conceded as the most legitimate critique
  of model-based approaches (misspecification risk), but note misspecification
  also destabilises model-free estimators — so this isn't a clean win either.
- **A.3** It admits doubly-robust estimators. Doubly robust estimation of τ_n
  is only meaningful if τ_n itself is an appropriate target — which the paper
  disputes throughout §4.

### 6. Conclusions and reflections on a burgeoning literature
§4.3 shows model-free effects like τ_n are sample-dependent even when a
perfectly stable treatment effect exists — so conclusions from one study need
not generalise to other populations. The authors view this instability (not
flexibility) as the real takeaway, echoing Cox: systematic treatment-effect
heterogeneity should be modelled explicitly rather than tolerated as sampling
variability, since arbitrary dependence of parameters on observation index
would violate basic modelling principles (McCullagh, 2002). They connect this
instability to recent methodological developments that implicitly try to work
around it — e.g. Jin & Rothenhäusler (2024) on conditional validity for
sub-populations, and Chernozhukov et al. (2024) on conditional influence
functions — framing these as responses to the inherent instability of
population-averaged model-free effects. They also note that inverse
probability weighting and imputation approaches exist to correct covariate
imbalance across treatment groups, a problem that does not arise in standard
regression models, where maximum-likelihood inference on treatment parameters
remains reliable under imbalance (absent unmeasured confounding) because
Fisherian inference conditions on observed covariates or ancillary statistics,
whereas model-free averaging over all covariate values is, from this
perspective, "too unconditional."
