# Summary: "What Is a Statistical Model?" (McCullagh, 2002, Annals of Statistics)

## Key Insights

- The textbook definition of a statistical model — a parameter set Θ together
  with a map P: Θ → P(S) assigning each θ a distribution on a sample space S
  — is far too permissive: it admits models that are "plainly absurd" (e.g., a
  model whose link function depends on whether the sample size is even or
  odd). Identifiability (P injective) does nothing to rule these out.
- McCullagh gives **twelve worked "exercises"** (binary regression with a
  parity-dependent link, a randomized-blocks model with a parity-dependent
  mean, an eccentric linear regression, an i.i.d. normal model with
  parity-dependent mean/variance roles, the SAS Type III model, the Box–Cox
  model, a clustered-data/quadratic-exponential model, an i.i.d. Cauchy model,
  a spatial Gaussian process, regression/correlation, a spatial simultaneous
  equation (CAR-type) model, and a three-way contingency table) that satisfy
  the standard definition yet are absurd, fishy, or only borderline acceptable.
  The point is not spotting absurdity but diagnosing its **source**.
- The diagnosed source: a model only supports meaningful inference if it
  admits a **natural extension to an "inferential universe"** beyond the
  observed units/covariates/treatments — e.g., to future subjects, unobserved
  blocks, or doses not actually tried. Without such an extension, no
  likelihood-based or Bayesian inference can legitimately reach beyond the
  literal sample, no matter how the model is fit.
- McCullagh formalizes "admits a natural extension" using **category
  theory**: statistical units, covariate spaces, and response scales are each
  organized into a category (objects + structure-preserving morphisms, e.g.
  injective maps on units, injective maps on covariate spaces, surjective
  maps on response scales). A **statistical model is a natural
  transformation** P: Θ → P(S) between functors built from these categories —
  i.e., a family of models indexed by design/units/covariates that is
  internally consistent under every morphism (restriction to subsets,
  relabeling, rescaling, aggregation, etc.).
- A **parameter is only meaningful ("natural") if it is itself a natural
  transformation** of functors — concretely, a subparameter g: Θ → Ψ is
  natural if it commutes with every relevant morphism. This is exactly the
  property that fails for quantities like β in the Box–Cox model, the
  correlation coefficient ρ under selection of covariate values, or μ/σ in a
  temperature-scale model — these are **not meaningful targets of inference**
  relative to the stated category, however easy they are to compute a
  likelihood or posterior for.
- This is the **direct conceptual ancestor of the group-action formalism**
  used in Battey & Edgar's critique of model-free treatment effects
  (see `battey-edgar-2026-treatment-effect-a-critique-summary.md`): a
  treatment effect is modeled as a group G acting on a baseline parameter
  space Γ (addition for location models, multiplication for rate/odds
  models), and the treatment parameter is meaningful only if it is a natural
  subparameter of this structure. McCullagh's "natural transformation /
  natural subparameter" machinery is precisely the formal apparatus that
  Battey & Edgar invoke to argue that *model-based* treatment effects are
  stable in a sense that *model-free* (counterfactual-average) treatment
  effects generally are not.
- Section 6.4 (contingency tables) is directly relevant to **ratio metrics**:
  a fitted log-linear model such as AB + BC (implying A ⊥ C | B) is not a
  statistical model in the categorical sense unless it is invariant under
  aggregation of the levels of B — conditional-independence or association
  conclusions that depend on an arbitrary level of aggregation are not
  natural conclusions. More generally, naturality is what separates a
  parameter/ratio that genuinely characterizes a relationship from one that
  is an artifact of how categories, cutpoints, or units happen to be defined
  (cf. the cumulative-logit/ordinal-regression construction in the Tjur
  discussion, built exactly so that the parameter of interest does not depend
  on an arbitrary dichotomization cutpoint).
- The paper also formalizes **exchangeability** (de Finetti) and **partial
  exchangeability** (Aldous) as special cases: a model that is a natural
  transformation on the category of injective maps on finite sets is
  precisely an infinitely exchangeable family; restricting to a product
  category of injective maps gives partially exchangeable arrays. This ties
  McCullagh's abstract framework back to familiar foundations of i.i.d.
  modeling and justifies why "exchangeable-within-group, not globally i.i.d."
  is often the right default structure.
- Section 7 resolves a long-running **controversy over the Box–Cox model**:
  the regression coefficient β (and σ²) are not natural parameters under the
  group of power transformations and positive scalar multiples, so posterior
  or confidence statements about "β" alone are formally meaningless in that
  system; natural (and hence meaningful) parameters include λ, β/σ, β^(1/λ),
  (β,λ) and (σ²,λ). This explains and resolves the Bickel–Doksum vs.
  Hinkley–Runger dispute about variance inflation from estimating λ.
- Causality is explicitly **not** built into this formalism (Section 5,
  "Causality and nonspecific effects"): the definitions avoid any reference
  to causal mechanisms, which are inherently context-dependent; the same
  categorical model (e.g., quasi-symmetry) can have many different
  mechanistic interpretations or none. Nonspecific factors (blocks, spatial
  position) are structural properties of the units, while specific factors
  (treatment, variety) for which level-specific inference is wanted must be
  objects in the covariate category — but causal effects are not ordinarily
  ascribed to intrinsic factors like race or sex, only to manipulable ones.

## Section-by-Section Summary

### Abstract / 1. Introduction
States the two motivating questions — "what is a statistical model?" and
"what is a parameter?" — and argues that the informal requirements that a
model "make sense" and a parameter "have a well-defined meaning" are not
captured by the standard definition (a parameter set Θ plus P: Θ → P(S), with
identifiability meaning P injective). Apart from identifiability, arbitrary
families of distributions and arbitrary parameter sets are permitted, which
is far too liberal. Notes that applied authors (Cox & Hinkley, etc.) give
informal warnings (e.g. "the model should be consistent with known limiting
behaviour") but no precise definition. The paper's goal is to formalize these
informal requirements algebraically via categories, morphisms, functors, and
natural transformations.

### 2. Examples
**2.1 Twelve statistical exercises.** Presents twelve model specifications
(summarized under Key Insights above) ranging from flagrantly absurd
(Exercises 1, 2, 4: models whose functional form depends arbitrarily on
whether n is even or odd) to subtly problematic (Exercise 5, the SAS Type
III model; Exercise 7, a clustered quadratic-exponential/Gibbs model whose
parameterization doesn't respect cluster size; Exercise 8, the i.i.d. Cauchy
model, where confidence procedures must be equivariant under the real
fractional linear group; Exercise 11, a spatial simultaneous-equations/CAR
model whose fit is not independent of lattice size; Exercise 12, a
contingency-table log-linear model AB+BC whose "conditional independence"
conclusion privileges a particular level of aggregation).

**2.2 Remarks.** Each exercise individually satisfies the standard
definition and admits a likelihood/posterior, but inference is limited to
a narrow "inferential universe," and the absurdity lies in how narrow that
universe is relative to what one would want to say. A likelihood/prior alone
is not sufficient for inference in any meaningful sense without a suitable
extension.

### 3. Statistical models
**3.1 Experiments.** Builds up the raw ingredients: a set of units U, a
covariate space Ψ, a response scale V; a design is a function x: U → Ψ; the
sample space is S = V^U. The model P: Θ → P(S) necessarily depends on the
design x (e.g. on treatment assignment and number of treatment levels), so
this dependence "cannot be arbitrary or capricious" (motivated by Exercise 2).

**3.2 The inferential universe.** Using an agricultural variety trial as a
running example, argues that before any model can be built one must fix an
inferential universe — of units (plots of varying shape/size/orientation),
response scales (bushels/acre vs. kg/m² vs. ordered category scales), and
covariate values (fertilizer doses, variety sets) — that is broader than the
literally observed data, because conclusions are implicitly meant to
generalize across these dimensions.

**3.3 Categories.** Introduces categories of morphisms: cat_U (injective maps
of statistical units, generically the category I of injective maps on finite
sets), cat_Ψ (injective maps of covariate spaces), cat_V (response-scale
morphisms, typically surjective, e.g. affine maps between temperature scales
or positive scalar multiples between yield units — crucially, these scales
must never be fused into one anonymous ℝ, since doing so destroys
composability). The central thesis: the logic of every sensible statistical
model is founded on categories of morphisms that keep families of
distributions on different sample spaces logically related and preserve
parameter meaning across them.

### 4. Functors and statistical models
**4.1 Definitions.** Builds the three foundational categories (cat_U, cat_Ψ,
cat_V) as the "building blocks" from which the design category cat_D and the
sample-space category cat_S are constructed, via functorial pullback/pushback
maps (coordinate projections for units, parameter restriction for covariates).

**4.2 Model.** Gives the formal definition: for each design ψ: U → Ψ there is
a sample space S = V^U and a parameter functor Θ_Ψ; a statistical model is a
**natural transformation** P: Θ → P(S) of functors on cat_D, meaning that for
every morphism (φ_d, φ_c): ψ → ψ′ of designs, the induced maps on parameters
and on distributions commute (Equation (1)/(2) in the paper). Key
consequence: the sample-space map φ_d* also carries distributions on S′
forward, and commutativity ensures the marginal distribution of P_ψ′θ under
restriction equals P_ψ of the corresponding restricted parameter — i.e. the
meaning of a parameter does not change across sample sizes, designs, or
scales.

**4.3 Composition, mixtures and hierarchical models.** Formalizes Bayesian
and hierarchical models as chains of natural transformations Θ1 → P(Θ2) → …
→ P(S), composed via "formal convex combinations" (treating a prior as a
point in the space of probability measures) and converted back into an
ordinary model by integration. A Bayesian model is the special case where Θ1
is the trivial one-point functor.

**4.4 Submodel.** A submodel is obtained via a natural transformation
h: Ξ → Θ restricting P to the image of h.

**4.5 Subparameter.** Defines a **natural subparameter** as a natural
transformation g: Θ → Ξ between parameter functors — i.e., it commutes with
every relevant design morphism. Motivating example: for i.i.d. normal weights,
σ/μ can make sense as a comparison across varieties, but μ+σ² or μ+σ/μ do
not. Complementary subparameters (g,h): Θ → Ξ×Υ a natural isomorphism are
defined but need not exist or be unique.

**4.6 Identifiability.** Θ is identifiable at design ψ if P_ψ is injective; a
natural subparameter is identifiable if distinct values give rise to
non-overlapping sets of distributions (a partition of the model).

**4.7 Response-scale morphisms.** Extends the natural-transformation
machinery to morphisms γ: V → V′ of the response scale itself (e.g. unit
changes), completing the three-way (units × covariates × response-scale)
functorial structure of a general statistical model, shown to be isomorphic
to a product category construction (Equations (1)-(2)).

### 5. Special cases
Shows the general definition specializes to familiar structures:
- **Equivariance/transformation models**: a group G acting on V, S, and Θ
  simultaneously; P(E;θ) = P(gE;gθ). A natural (equivariant) subparameter
  h: Θ → Ξ satisfies h(θ1)=h(θ2) ⟹ h(gθ1)=h(gθ2); this generalizes but
  corrects the misleading term "invariantly estimable parameter" (Hora &
  Buehler), since a natural parameter is equivariant, not invariant, and
  naturality is unrelated to estimability.
- **Insertion maps / Kolmogorov consistency**: with cat_U = insertion maps on
  finite sets and V = ℝ, naturality of P reduces exactly to the Kolmogorov
  consistency condition for a stochastic process.
- **Interference and insertion maps**: a stronger condition than Kolmogorov
  consistency, corresponding to "lack of interference" (Cox 1958; Rubin
  1986) — the design ψ′ carries treatment-assignment information for
  unobserved units too, and commutativity forces consistency of the
  distributions even accounting for that.
- **Exchangeability and injection maps**: with cat_U = I (all injective maps)
  and a trivial Θ, naturality is exactly **infinite exchangeability** in the
  sense of de Finetti.
- **Partial exchangeability**: restricting to the product category I² (pairs
  of injective maps on rows/columns) recovers Aldous's partially exchangeable
  arrays.
- **Completely randomized design**, **block designs**, and a worked
  variance-components model (Y_i = θ0 + θ1εi + θ2η_b(i)) are given as further
  instances.
- **Causality and nonspecific effects**: nonspecific factors (blocks, time,
  space) are properties of the unit structure; specific factors (treatment,
  variety, age, race) needing level-specific inference must be covariate
  objects — but causal effects are ordinarily ascribed only to manipulable
  (extrinsic), not intrinsic, factors (citing Holland 1986; Cox 1986). The
  framework is explicitly agnostic about causal mechanism.

### 6. Examples (revisited formally)
**6.1 Location-scale models.** Using cat_V = temperature-scale morphisms
(affine maps), shows the mean and the scale parameter are each natural
subparameters, but the coefficient of variation τ=θ1/θ2 is **not** a natural
subparameter under the full affine group (since the induced transformation
of τ depends on more than τ itself) — though it **is** natural under the
restricted subcategory of pure scalar multiplication. Same analysis applied
to the location-scale t-family.

**6.2 Regression and correlation.** Resolves Exercise 10: the map
(α,β,σ) ↦ ρ (correlation coefficient) is **not a natural transformation**
because ρ depends on the design variance σ_ψ² of the covariate, which is not
preserved under selection of units. Reformulating (x,y) as a bivariate
response with an affine group acting on both components componentwise
restores naturality (up to a sign depending on sign(bd)), giving a
restricted sense in which inference about ρ can be sensible.

**6.3 Splines and curve estimation.** Constructs a finite-dimensional spline
subrepresentation H^(k) of the standard representation, satisfying the
functorial conditions for a statistical model relative to the category of
affine (or more general injective) maps on intervals.

**6.4 Contingency-table models.** Resolves Exercise 12: for log-linear models
on three-way tables, only formulas in which each factor appears exactly once
(A+B+C, AB+C, AC+B, A+BC, ABC) are covariant functors on Surj³ (surjective
maps modeling aggregation of levels); a formula like AB+BC, which asserts
conditional independence given a particular level of aggregation of B, is
**not** such a functor and so is not a statistical model in this categorical
sense — its conclusion is not preserved under re-aggregation. Ordinal
extensions (Surj_ord) and models with constant (log-)cross-ratio are also
discussed; Goodman's ordinal association models fail to be functors on
Surj²_ord.

**6.5 Embeddability and stochastic processes.** Resolves Exercise 11: the
spatial simultaneous-equations (CAR) model on a 3×3 lattice does not define
an embeddable process, because integrating out the extra variables from a
larger n×n lattice gives a different marginal distribution for each n (a
concrete instance of the general edge-effect problem in Gibbs/MRF models on
finite lattices).

**6.6 Comments on selected exercises.** Walks back through Exercises 1–5, 7,
8, 9, 11 explaining precisely which naturality condition fails in each
(e.g., Exercise 1: predicting a future subject gives two inequivalent ways
to compute the same likelihood; Exercise 5, Type III model: the set of
valid mean vectors is not closed under the embedding that drops an entire
block; Exercise 7: the exchangeable-normal clustered model's natural
parameterization does not commute with marginalizing out one cluster member,
unlike the conventional variance/covariance parameterization; Exercise 8: the
real part of the Cauchy location parameter is not natural under the real
fractional linear group — only the identity and the trivial map are;
Exercise 9: no morph of the spatial Gaussian process parameters corresponds
to θ=μ/σ or other dimensionally nonsensical combinations under
temperature-scale morphisms).

### 7. The Box–Cox model
**7.1 Natural subparameter.** Formalizes the simplified (i.i.d.) Box–Cox
model with parameter (β,σ²,λ) and shows that the coordinate projection
(β,σ²,λ) ↦ β is **not** a natural transformation under the combined group of
power transformations and positive scalar multiplication on the sample
space — commutativity would require γ ↦ γ^λβ for the transformed parameter,
which is not expressible as a function of (γ,β) alone. Hence "the true value
of β" is meaningless in this system; natural (meaningful) subparameters
include λ, β/σ, β^(1/λ), (β,λ), (σ²,λ). This formally resolves the
Hinkley–Runger critique of Bickel & Doksum's earlier variance-inflation
analysis (further discussed by Bickel in the Discussion).

**7.2 The modified power transformation.** Shows that Hinkley & Runger's
geometric-mean-standardized Box–Cox transformation is natural only relative
to a restricted category (a single fixed set of n units, excluding general
coordinate-projection/subset morphisms), under which β/λ is still not
natural but other combinations are.

### 8. Extensive response variable
**8.1 Spatial aggregation and measure processes.** Extends the whole
framework from *intensive* variables (e.g. temperature, which doesn't
aggregate) to *extensive* variables (e.g. crop yield, an additive set
function on an algebra of plots), defining measure processes, point
processes, Poisson processes, and Gaussian measure processes category-
theoretically via the Kolmogorov consistency condition on an algebra of
Borel sets.

**8.2 Domain morphisms.** Builds the category cat_D of spatial domains with
morphisms restricted to injective Borel-structure-preserving maps
(translations, rotations, scalar multiples), and defines invariant
probability models (e.g. the homogeneous Poisson process, invariant under
translation/rotation; stationary isotropic Gaussian processes, invariant
under similarity transformations).

**8.3 Covariate effects in spatial processes.** Shows that for a model to be
closed under similarity transformations of the domain (so that doubling the
plot area doubles expected yield), variety/treatment effects on
intensity-type extensive responses **must enter multiplicatively, not
additively** — a direct, non-obvious consequence of requiring naturality
under domain scaling. Also shows the framework can incorporate interference/
carry-over effects by extending the covariate space to include neighbors'
treatments.

**8.4 Conformal models.** Defines a conformal model as a natural
transformation under the category of conformal (angle-preserving) maps on
planar domains; shows the family of completely random processes with
harmonic log-intensity is closed under conformal mapping, using the
transformation rule for cumulant densities under a conformal map's Jacobian.

**8.5 A conformal model with covariates.** Proposes a concrete field-trial
model in which log-mean fertility λ(x) is assumed to lie in the (infinite-
dimensional) space of harmonic functions H_D — so fertility has the
mean-value property (no local max/min in the interior) — while variety
effects enter multiplicatively; shows many variety contrasts remain
identifiable despite the infinite-dimensional nuisance space.

**8.6 Lattice approximation.** Derives a discretized Laplacian-based
estimator (projecting onto the orthogonal complement of the lattice-harmonic
subspace) and reanalyzes the classic Mercer & Hall (1911) wheat uniformity
trial, finding a statistically significant harmonic ("fertility trend")
variance component and a ~25% variance reduction for treatment contrasts
after removing it (at the cost of excluding boundary plots from inference).

**8.7 A parting proposal.** Argues that if fertility is adequately captured
by smooth harmonic trends, artificial discontinuous block effects may be
unnecessary, and proposes developing a theory of efficient "harmonic
designs" for field experiments (e.g., not assigning the same treatment to
neighboring plots).

### Appendix: Glossary on categories
A self-contained primer defining category, product category, functor
(covariant/contravariant), representation, dual representation, opposites,
and natural transformation, to make the main text accessible to readers
unfamiliar with category theory.

### Discussion
Nine discussants respond:
- **Julian Besag** largely disputes the paper's practical relevance: argues
  McCullagh conflates mathematical models with statistical ones, that
  "extrapolation" (vs. interpolation) is rarely the real goal, that his
  Exercise 7 (clustered data) is a bad example once context (e.g. litters of
  piglets) is supplied, and gives a detailed critique of the harmonic-function
  field-trial proposal (Section 8) versus his own Bayesian intrinsic-
  autoregression (Besag–Higdon) approach, including re-analysis of the
  Mercer–Hall data.
- **Peter Bickel** broadly agrees with the main design-theoretic points but
  finds the category-theoretic machinery personally unfamiliar; elaborates on
  the Box–Cox β/σ vs. (β,λ) naturality result in connection with
  semiparametric transformation models.
- **Hans Brøns** gives a rigorous category-theoretic reformulation of
  McCullagh's definitions using comma categories and monoidal structure,
  arguing the framework can be stated more cleanly (and generally) than
  presented.
- **Fraser & Reid** welcome the paper, connect natural subparameters to
  Fraser's earlier (1968) work on structural inference and cosets of
  transformation groups, and raise concerns about whether black-box/graphical
  structure should be modeled more explicitly.
- **Inge Helland** connects natural subparameters to marginalization
  paradoxes (Dawid, Stone & Zidek) and to quantum-mechanics-inspired
  statistical formalism, giving conditions under which Bayesian inference
  with right-Haar priors avoids such paradoxes precisely when the
  subparameter is natural.
- **Peter Huber** gives historical context from Le Cam's theory of
  statistical experiments and category-theoretic treatments of sufficiency,
  but is skeptical that category theory adds genuinely new content beyond
  clarifying exposition.
- **Rudolf Kalman** is broadly critical of the entire enterprise of
  "statistical models" as currently practiced (not specifically of
  McCullagh), arguing models are rarely checked against reality.
- **Steve Pincus** praises the unification but argues the framework is
  "probabilistic" rather than "statistical" in spirit (since it concerns
  processes/infinite families rather than finite-sample inference) and notes
  the lack of a metric limits its use for model comparison with finite data.
- **Tue Tjur** asks what makes a model "canonical," reconstructs
  McCullagh's ordinal-regression (cumulative logit) result without category
  theory by requiring invariance under choice of dichotomization cutpoint,
  and discusses the (negative) existence question for a fully natural
  overdispersion extension of GLMs.

### Rejoinder (McCullagh)
Responds to major cross-cutting themes — abstraction, model vs. analysis,
prediction, extension/embedding, extrapolation, approximation — defending
the view that a model is a mathematical object logically prior to any
particular analysis or approximation, and that falsifiable extension beyond
the observed domain is what separates a model from a mere predictive
algorithm. Responds point-by-point to each discussant (notably agreeing with
Helland's natural-subparameter/marginalization-paradox connection, and with
Bailey/Besag's practical concerns while maintaining the formal critique
stands). Closes with a substantial extension of Section 8's spatial model to
the **full conformal group of fractional linear transformations** on the
Riemann sphere, showing that the covariance structure −σ² log|z−z′|
(connected to the "de Wijs process"/Newtonian potential) is both Markov and
conformally invariant, and that this may reconcile McCullagh's harmonic-
function proposal with Besag's Markov-random-field-based spatial models for
field trials.
