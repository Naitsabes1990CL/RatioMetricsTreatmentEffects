|     |     | TREATMENT |     |     | EFFECT: |     | A CRITIQUE |     |     |     |
| --- | --- | --------- | --- | --- | ------- | --- | ---------- | --- | --- | --- |
H.S.BATTEYANDCHARLOTTEEDGAR
|     | Summary.         | Two         | broad positions | within      | statistics        | define | a treatment |           | effect, on     | the one   |
| --- | ---------------- | ----------- | --------------- | ----------- | ----------------- | ------ | ----------- | --------- | -------------- | --------- |
|     | hand, as         | a parameter | of a            | statistical | model,            | and    | on the      | other, as | an appropriate |           |
|     | population-level |             | difference in   | outcomes    | or counterfactual |        | outcomes    | under     | the            | different |
6202 naJ 12  ]TO.tats[  1v76451.1062:viXra treatmentregimes. Thisshortexpositorypaperpresentssomesimplebutconsequential
|     | insights on | the two      | formulations, |                | contrasting | the answers | under | the          | most | favourable  |
| --- | ----------- | ------------ | ------------- | -------------- | ----------- | ----------- | ----- | ------------ | ---- | ----------- |
|     | fictitious  | idealisation | for the       | counterfactual | framework.  |             | These | observations |      | clarify the |
relationshipbetweenFisherianmodel-basedinferenceandmoderncounterfactualformu-
lations,andemphasiseconcerns,raisedbyCoxandothers,regardingthesuitabilityof
model-freedefinitionsastargetsofinferencewhenscientificconclusionsareintendedto
|     | generalisebeyondtheobservedsample. |     |     |     | Partsofthepaperarenecessarilycontroversial; |     |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
wefollowCox(1958a)innotputtingtheseforwardinanydogmaticspirit.
|     | Some key | words: | causation; | counterfactuals; |     | foundations | of modelling; |     | scientific | prac- |
| --- | -------- | ------ | ---------- | ---------------- | --- | ----------- | ------------- | --- | ---------- | ----- |
tice.
1. Introduction
When the aim is scientific understanding rather than immediate predictive success, es-
tablishing causation is usually the idealised objective even when the word is not explicitly
used. Theterminologycausal inference has,however,cometobeprimarilyassociatedwith
aspecificformulationbasedoncounterfactuals,intheveinofRubin(1974)andRosenbaum
and Rubin (1983). This has gained popularity as a basis for methodological development,
particularlyinconnectionwiththepropertyofdoublerobustnessfirstintroducedbyRobins
et al. (1994). Of two primary aspects that are open to discussion, we focus here on the
wayinwhichtheeffectofpotentialcausesismeasured,revisitingthefundamentalquestion
| what | is a treatment | effect | (McCullagh, |     | 2002)? |     |     |     |     |     |
| ---- | -------------- | ------ | ----------- | --- | ------ | --- | --- | --- | --- | --- |
The model-free definition of treatment effect implicit in the counterfactual formulations
differs strikingly from a framing in which the treatment effect is defined as a parameter
of a statistical model, in the vein of Fisher (1922), who appears to have been the first
to use the word parameter in the general modern sense (Stigler, 1976). In view of this
and also Bailey’s (2017) correction to a historical misnomer, it is appropriate to associate
with Fisher’s name the model-based definition of treatment effect rather than a definition
implicitinwhatissometimesreferredtoasFisher’ssharpnullhypothesis. Themodel-based
definition encompasses a style of discussion often suggestive of causation and reflected in
regression-type formulations (e.g. Cox, 1958b, 1968, 1972, 2007; McCullagh and Nelder,
1989).
The issue considered here is not whether model-free treatment effects based on counter-
factualscanbeidentifiedorconsistentlyestimatedundersuitableassumptions,butwhether
they define appropriate quantities in settings where a stable treatment effect is unambigu-
ously defined. We do not claim any great originality for the points made; the merits of the
work are instead to clarify the issues in an incisive form based on some idealised examples.
Our position echoes concerns raised by Cox (1958b, 2012), who questioned the suitability
DepartmentofMathematics,ImperialCollegeLondon,180Queen’sGate,LondonSW72AZ,UK.
m h.battey@imperial.ac.ukandc.edgar24@imperial.ac.uk.
1

2 H.S.BATTEYANDCHARLOTTEEDGAR
of model-free averages as targets of inference when conclusions are intended to generalise
beyond the observed sample.
2. Model-based treatment effect
2.1. Introduction. Parametric statistical inference starts from a provisional assumption
that data correspond to random variables, that these are drawn from an unknown prob-
ability distribution, and that this distribution belongs to a parametrised family P :=
Θ
{P : θ ∈ Θ}, the statistical model. Dependence or independence between observations is
θ
reflected in P . While there is considerable flexibility in how a statistical model might be
Θ
constructed, a core principle is that P should stress commonalities between observational
Θ
or experimental units, the purpose being to provide subject-matter understanding in such
a way that any conclusions drawn remain relevant to units different from those already
observed. Suchcommonalitiesareencapsulatedinstableparameters, ofwhichatreatment
parameter, quantifying treatment effect, is one example.
McCullagh (2002) formalised some principles underpinning the construction of sensible
statisticalmodels,pointingoutthatthetextbookdefinitiondoesnotincorporatebydefault
aspects usually invoked, with the implication that four “plainly absurd” examples are in
principle valid. His work can be viewed as an attempt to put scientific common sense on
a more rigorous mathematical footing and stems to some extent from an earlier technical
report (McCullagh, 1999) establishing a group theoretic perspective on generalised linear
models via exponential tilting. McCullagh (2022, Ch. 11 and 14) gives an accessible expo-
sition of some of the main ideas. An important point is that this formalisation is detached
fromanycausalmechanism; itisratherthecontextthatdetermineswhethercausationcan
be securely established.
2.2. McCullagh’s formalisation. Atreatmenthasaneffect,notontheoutcome,buton
theprobabilitydistributionoftheoutcome. McCullagh(2022,p.231,p.399)expressesthis
as a transformation induced by the action of a group G on {P :γ ∈Γ}, the set of baseline
γ
distributionsfortheoutcomepriortopossibletreatment. Inthesimplestmodelsthegroup
acts on the baseline distributions via the baseline parameter space Γ as G×Γ→Γ, i.e. for
any g ∈ G and γ ∈ Γ, (g,γ) → gγ ∈ Γ. As two simple examples: if Γ = R, the natural
group action is addition, g =(ψ,+) say, so that gγ =γ+ψ; if Γ=R+, the natural group
action is multiplication, g = (ψ,×) say, and gγ = γψ. In each case the null treatment
effect is the identity element of the group, i.e. addition of zero in the first example and
multiplication by one in the second.
In what follows, we will use the imprecise terminology individual to refer to an exper-
imental or observational unit of any kind. The effect of the treatment is to modify the
response distribution, altering the control distribution by the same group action for all
treated individuals. Implicit in this is the requirement that outcome distributions are no-
tionally compared for individuals i and i′, perhaps hypothetical, that are comparable in
the sense that for all events A in the sample space for the outcome,
pr(Y ∈A|T =0)=pr(Y ∈A|T =0)
i i′
(2.1)
pr(Y ∈A|T =1)=pr(Y ∈A|T =1),
i i′
wherehereandhenceforthwerestrictattentiontoabinarytreatmentvariabletakingvalues
t ∈ {0,1}. In the simplest parametrised models within this simplest setting, (2.1) implies
that i and i′ share the same baseline parameter γ = γ , and if both are treated, both
i i′
are perturbed from baseline in the same way. Dependence on intrinsic features, w say,
recoversstandardregressionformulations. Specifically,ifΓ=R,apopularmodelwouldbe
the linear regression with γ = wTβ, while if Γ = R+, the common modelling assumption
i i
γ =exp(wTβ)wouldrecoversomeotherpopularregressionformulations. Whilethegroup
i i
element defining the treatment effect is stable over individuals, the control distribution is

3
individual-specificinviewofγ . Interactionoftreatmentwithintrinsicvariablesisdiscussed
i
on pp. 232-240 of McCullagh (2022), allowing some variation of treatment effects by unit
while respecting the stability requirement.
3. Model-free treatment effect and counterfactuals
Inmodel-freesettingsthereisnooutcomemodelinwhichtoembedanaturalandstable
treatment parameter. For a binary treatment, a common choice is therefore an average
difference in potential outcomes, the simplest model-free counterfactual treatment effect
being
n
1 (cid:88)
τ := E (Y (1)−Y (0)), (3.1)
n n i i i
i=1
where Y (t) is the outcome on individual i for values t∈{0,1} of the treatment indicator.
i
Seee.g.ImbensandRubin(2015)foramoreexhaustivediscussionoftheframework. Since,
for a given i, only one of Y (1) or Y (0) is observable, two broad approaches are common,
i i
basedonassumptionsabouttheunobservable“crossworld”oftheextendedcounterfactual
process: oneistoimputethecounterfactualonthebasisofcovariateinformation,requiring
anoutcomemodel;theotherispropensity-scorereweighting(RosenbaumandRubin,1983),
which models the treatment assignment mechanism instead. Under the strong assumption
of no unmeasured confounding and several further assumptions, it can be shown that the
resulting observable statistic, τˆ say, estimates τ .
n n
Although Imbens and Rubin (2015, Chapter 8) refer to model-based approaches, such
models are only used as a means for performing inference on (3.1) or a similarly defined
model-freetreatmenteffect. Theirusageofthisterminologyisthusdifferent,intherelevant
sense, from that of §2.
4. Some prompts for reflection
4.1. Twoaspects. Therearetwodistincttypesofconsiderationregardingthesestrikingly
different definitions of treatment effect. One concerns the security of causal claims and the
strength of untestable assumptions, and the other concerns the way in which the effect
of the potential cause is measured. The first of these has been covered elsewhere in the
literature, notably by Dawid (2000) and McCullagh (2022, p. 244). The criticism is that a
formulationintermsofobjectsthatareinherentlyunobservablecanneverbefalsified, and
therefore violates core principles of the scientific method, as put forward by e.g. Popper
(1963). We will not repeat any of this earlier discussion, focussing instead on the second
consideration, which can be decoupled from the first under a fictitious idealisation for the
counterfactuals.
4.2. Fictitious idealisation. To detach concerns over the use of counterfactuals from
those over what is being measured, we suppose, notionally, that the process through which
the counterfactuals become factual is completely known, and that both outcomes are ob-
servable. This fictitious idealisation is the most favourable one for the counterfactual for-
mulation and permits isolation of key issues in an incisive form.
Under the fictitious idealisation, the counterfactual formulation reduces to a matched-
pair problem in which each individual is twinned with a perfect copy of itself. From
individual i and his or her fictitious twin, one of the two is randomised to treatment, the
other to control, yielding notionally observable outcomes (Y ,Y ). Given an outcome
i1 i0
model for (Y ,Y ) with a stable treatment parameter, the question we seek to address is
i1 i0
to what extent the model-free definition of treatment effect (3.1) recovers it, and how this
depends on the structure of the outcome model. If the answers are drastically different
undersimpleidealisedsettings, thismustraiseconcernsovertherelevanceof (3.1)inmore
difficult contexts.

| 4   |     |     |     | H.S.BATTEYANDCHARLOTTEEDGAR |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
4.3. Five examples. The simplest example in which the two formulations give identical
answers is a linear model of the form Y i0 =γ i +ε i and Y i1 =γ i +∆+ε i with ε i a mean-
zeroerrorterm. Thisencompassesthelinearregressionmodelwithintrinsicvariablesw by
taking γ =wTβ. Implicit in the model just presented is an assumption of unit treatment
|     | i   | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
additivity that underpinned R. A. Fisher’s early work on the design of experiments. The
model-free treatment effect (3.1) recovers the model-based treatment effect ∆ in this case.
ThisexampleisessentiallythesameasthatdiscussedbyImbensandRubin(2015,pp.122).
AsimilarlysimpleexampletakesY andY asexponentiallydistributedofratesγ and
|     |     |     |     |     | i0  | i1  |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ θrespectively,sothatthemodel-basedtreatmenteffectismultiplicativeontheratescale.
i
It is appropriate, since the outcomes are positive, to construct the model-free treatment
effect (3.1) after logarithmic transformation, giving τ =−logθ, which is the model-based
n
treatmenteffectθ convertedtoadifferentscale. Thetwoapproachesareagaincompatible.
The previous example can be elaborated by extending the outcome distribution to
Weibull with shape parameter α, the rate parameters being specified as above, with mul-
tiplicative treatment effect θ on the rate scale. Since the density function of the ratio
| Z =Y | /Y  | is  |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i    | i1  | i0  |     |     |     |     |     |     |     |     |
αθzα−1
|     |     |     |     | f (z)= |     |     | , z ≥0, |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | ------- | --- | --- | --- |
Z
(1+θzα)2
| the | definition | (3.1) | yields,      | after logarithmic |     | transformation, |                |     |      |     |
| --- | ---------- | ----- | ------------ | ----------------- | --- | --------------- | -------------- | --- | ---- | --- |
|     |            |       | 1 (cid:88) n |                   |     | (cid:90)        | ∞ log(z)αθzα−1 |     | logθ |     |
E(logY
|     |     | τ n = |     | i1 −logY |     | i0 )= |          | dz  | =− , |     |
| --- | --- | ----- | --- | -------- | --- | ----- | -------- | --- | ---- | --- |
|     |     |       | n   |          |     |       | (1+θzα)2 |     | α    |     |
|     |     |       | i=1 |          |     |       | 0        |     |      |     |
showingthatthetruetreatmenteffectθcanonlybeidentifieduptothesignoflogθ,unless
α is known, as in the previous exponential example with α = 1. This is an example in
which the answers are semi-compatible, being qualitatively reasonable and stable across
samples.
We now present two examples in which the disagreement seems more severe. Suppose
thatY andY areexponentiallydistributedofratesγ andγ +∆respectively. Sincethe
|         | i0       | i1  |           |        |       |       | i   | i   |     |     |
| ------- | -------- | --- | --------- | ------ | ----- | ----- | --- | --- | --- | --- |
| density | function | of  | the ratio | Z i =Y | i1 /Y | i0 is |     |     |     |     |
γ (γ +∆)
i i
|     |     |     |     | f Zi (z)= |     |            | , z | ≥0, |     |     |
| --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |     |           | (γ  | +(γ +∆)z)2 |     |     |     |     |
i i
| equation | (3.1) | yields, | after | logarithmic | transformation |     |     |     |     |     |
| -------- | ----- | ------- | ----- | ----------- | -------------- | --- | --- | --- | --- | --- |
n
|     |     |     |     |     | 1 (cid:88) |        |          |     |     |       |
| --- | --- | --- | --- | --- | ---------- | ------ | -------- | --- | --- | ----- |
|     |     |     |     | τ   | =          | log((γ | +∆)/γ ). |     |     | (4.1) |
|     |     |     |     | n   | n          |        | i i      |     |     |       |
i=1
At ∆ = 0, the model-based and model-free treatment effects agree, otherwise τ depends
n
onthesamplechosenvia(γ )n . Considertheexampleof∆=2andtwoextremecases: if
i i=1
alltheγ i areconcentratednearzero,τ n islarge,whileifalltheγ i arelarge,thenτ n istiny.
Thus, (3.1)convertsawell-definedproblemwithastabledefinitionoftreatmenteffectinto
one that is unstable with respect to sampling new individuals, and in which extrapolation
ofconclusionstonewindividualsisimpossible. Althoughitmaybearguedthatdeviations
induced by (γ )n should approximately average out to a value close to ∆, this seems in
i i=1
many contexts an unreasonable assumption. R. A. Bailey (2017) writes, in her critique of
| a paper | in           | Statistical    | Science: |                   |        |        |                |                    |               |     |
| ------- | ------------ | -------------- | -------- | ----------------- | ------ | ------ | -------------- | ------------------ | ------------- | --- |
|         | I            | have practised |          | as a statistician |        | for 40 | years [...],   | in no              | case were the |     |
|         | experimental |                | units    | a random          | sample | from   | a fixed        | finite population. | They          |     |
|         | were         | convenient,    |          | and were          | deemed | to be  | representative | enough             | that results  |     |
|         | on           | them           | could be | extrapolated      | to     | other  | units.         |                    |               |     |

5
One final example with a similar conclusion takes the outcomes to be binary, from the
logistic model
|     |     |     |            | (cid:18) |       | (cid:19) |              |     | (cid:18) | (cid:19) |     |
| --- | --- | --- | ---------- | -------- | ----- | -------- | ------------ | --- | -------- | -------- | --- |
|     |     |     |            |          | eγi   |          |              |     | eγi+∆    |          |     |
|     |     | Y   | ∼Bernoulli |          |       | ,        | Y ∼Bernoulli |     |          | ,        |     |
|     |     |     | i0         |          |       |          | i1           |     |          |          |     |
|     |     |     |            |          | 1+eγi |          |              |     | 1+eγi+∆  |          |     |
logisticregressionbeingrecoveredbymodellingγ =wTβ. Themodel-freetreatmenteffect
|     |     |     |     |     |     |     | i   | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(3.1) is
n
|     |     |     |     |     | 1 (cid:88) |     | eγi(e∆−1) |     |     |     |       |
| --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- | --- | ----- |
|     |     |     |     | τ   | =          |     |           |     | .   |     | (4.2) |
n
|     |     |     |     |     | n   | (1+eγi)(eγie∆+1) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
i=1
Except at τ =∆=0, there is a complicated dependence on the sample, as in (4.1).
n
The model-based and model-free definitions give identical answers for any sample if and
| only | if the | following | criteria | are | all satisfied: |     |     |     |     |     |     |
| ---- | ------ | --------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
(1) The group action defining the treatment effect acts on the baseline distribution P
γ
|     | via | the baseline | parameter |     | space, | transforming |     | it to | P . |     |     |
| --- | --- | ------------ | --------- | --- | ------ | ------------ | --- | ----- | --- | --- | --- |
gγ
(2) The group action can be described by the same group action on the observations.
(3) There are no other nuisance parameters needed to characterise the relevant expec-
|     | tation | (on | the original | or  | logarithmic |     | scale) | under P | γ besides | γ.  |     |
| --- | ------ | --- | ------------ | --- | ----------- | --- | ------ | ------- | --------- | --- | --- |
Ifanyoftheseconditionsisviolated,(3.1)dependsingeneralonthevaluesofothernuisance
parameters or on the sample chosen via the baseline parameters. Conditions (1) and (2)
imply that the model belongs to a transformation family (e.g. Barndorff-Nielsen and Cox,
§2.8).
1994,
4.4. ClarificationofFisher’sposition. Theapproachbasedon(3.1)issometimescalled
Neymannian following Neyman (1923) and particularly Neyman et al. (1935). Within the
causalinferencecommunity,anotherhypothesisoftheformY (1)=Y (0)foralli=1,...,n
|     |     |     |     |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
issometimescontemplated. ThishascometobeassociatedwithR.A.Fisher’snameinthe
formof“Fisher’ssharpnull”. Bailey(2017)correctedthishistoricalmisnomer,pointingout
thatFisher’sformulationwasinsteadbasedonunittreatmentadditivityonanappropriate
scale, as in the first two examples of §4.3, which implicitly uses the model-based definition
specialised to the situation where the outcome distribution belongs to a location family,
§6)confusion
| perhapsafterlogarithmictransformation. |     |     |     |     |     | ThisalsoresolvesHolland’s(1983, |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
regarding D. R. Cox’s position. McCullagh’s (2002, 2022) formalisation unifies these early
| contributions |     | in  | the analysis | of  | field experiments |     | with | the other | examples. |     |     |
| ------------- | --- | --- | ------------ | --- | ----------------- | --- | ---- | --------- | --------- | --- | --- |
Thelasttwoexamplesof§4.3showthattheFisheriannotionoftreatmenteffecttypically
violates the sharp null even under the fictitious idealisation in which the counterfactuals
are observable.
|     |     |     |     |     | 5. Differing |     | positions |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- |
Three arguments are commonly put forward in favour of the model-free definition of
| treatment |     | effect: |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A.1 That (3.1) allows the treatment to affect different individuals in different ways.
| A.2 | That | (3.1) | does not | require       | an  | outcome     | model. |     |     |     |     |
| --- | ---- | ----- | -------- | ------------- | --- | ----------- | ------ | --- | --- | --- | --- |
| A.3 | That | (3.1) | admits   | doubly-robust |     | estimators. |        |     |     |     |     |
Here we expand on each of these arguments and summarise our own position.
In connection with the so-called sharp null, defined above, Ding and Dasgupta (2016)
argued that the assumption of constant causal effect across individuals is unrealistic for
binary outcomes on the scale of expectations, a conclusion with which we agree in view of
(4.2). This was noted in support of an argument that individual units should be allowed
to contribute a different treatment effect to a composite, which is permissible under (3.1);
this is where our positions differ. The last example of §4.3 indicates an appropriate way

6 H.S.BATTEYANDCHARLOTTEEDGAR
of achieving stability, in this case via a stable additive treatment effect on the log-odds
scale, while allowing individuals to have different probabilities for the event of interest.
A treatment effect that differs according to individual-specific features is incorporated in
the model-based definition through an interaction component, which retains the necessary
stability of parameters; see McCullagh (2022, pp. 232–240).
The most legitimate objection (argument A.2) of the model-based formulation is the
possibility of model misspecification. By eschewing the model, stability and interpretation
is lost through the use of (3.1) or similar, but if the model is misspecified, this may also
lead to a loss of stability across samples. This underscores the importance of assessments
of model adequacy; see e.g. Barndorff-Nielsen and Cox (1994, p. 29) for some discussion
from a Fisherian position.
Double robustness (argument A.3) of an estimator of τ is the property of being consis-
n
tent for τ either under a valid outcome model, or under a valid model for the treatment
n
assignment, provided that other assumptions such as no unmeasured confounding are sat-
isfied. The property of double robustness is only relevant if the definition τ is accepted in
n
the first place, and it is this that we have sought to challenge in §4.
6. Conclusions and reflections on a burgeoning literature
Section 4.3 exemplifies how the model-free treatment effect (3.1), and other model-free
definitions,areliabletochangedependingontheparticularsamplechosen,evenwhenthere
is a clearly defined treatment effect that is stable over individuals. The implication is that
the conclusions of inference from one study do not generalise to other populations. This
observation is not new, and indeed, the ability of (3.1) to accommodate individual-specific
differences is viewed as a strength by some authors. Our view, echoing Cox (1958b, 2012),
is that if there is a systematic difference in treatment effect between units, then that needs
to be explained. If, in a traditional modelling setting, parameters representing treatment
effects were allowed to depend in an arbitrary way on the observation index, this would be
in clear violation of the foundations of modelling, as formalised by McCullagh (2002).
Instability in the definition of the model-free treatment effect (3.1) or similar is the
implicitreasonbehindseveraldevelopmentsinthecausalinferenceliterature. Forinstance,
Jin and Rothenh¨ausler (2024) proposed an approach to inference with conditional validity
in finite populations, motivated by the observation that versions of τ for sub-populations
n
are typically more relevant to individuals in those populations than a version specified as
an average over a larger population. The need to introduce different values of τ for sub-
n
populations is an inherent feature of their instability. In a similar vein, Chernozhukov et
al. (2024) developed conditional influence functions to improve the efficiency of average
treatment effect estimators conditional on a subset of covariates.
Other developments in the causal inference literature have emerged to address aspects
that do not arise in the model-based formulation. Inverse probability weighting as dis-
cussed in Rosenbaum and Rubin (1983) is one way to correct for a lack of balance among
the treatment groups prior to comparison by the model-free treatment effect (3.1) or gen-
eralisations thereof. Other approaches have been proposed, for instance imputation of the
missing counterfactual outcomes.
In a standard regression model, there is no need for covariate classes to be balanced;
maximum-likelihoodinferenceontreatmentparametersisreliableunderstandardregularity
conditions and, while balance typically improves the precision of estimators, imbalance
does not systematically bias the conclusions unless there are unmeasured confounders, a
situation that is precluded by Rosenbaum and Rubin (1983) and, to our knowledge, all
subsequent discussions. Moreover, since Fisherian inference is made either conditionally
on the observed values of the covariates or on a lower dimensional ancillary statistic if one
exists, extreme imbalance in the classes is reflected in the reference sets used for inference.

7
An approach that averages over the covariate values observed for all individuals is, from a
| Fisherian | perspective, | too unconditional. |     |     |
| --------- | ------------ | ------------------ | --- | --- |
Funding. H. Battey was supported by a UK Engineering and Physical Sciences Research
| Fellowship | (EP/T01864X/1) |     |     |     |
| ---------- | -------------- | --- | --- | --- |
References
Bailey, R. A. (2017). Inference from randomized (factorial) experiments. Statist. Sci.,
32, 352–355.
Chernozhukov,V.,Newey,W.K.andSyrgkanis,V.(2024). ConditionalInfluenceFunc-
| tions. arXiv: | 2412.18080. |     |     |     |
| ------------- | ----------- | --- | --- | --- |
Cox,D.R.(1958a). Someproblemsconnectedwithstatisticalinference. Ann.Math.Statist.,
29, 357–372.
Cox, D. R. (1958b). The interpretation of the effects of non-additivity in the Latin
| square. | Biometrika, 45, | 69–73. |     |     |
| ------- | --------------- | ------ | --- | --- |
Cox,D.R.(2000). Causalinferencewithoutcounterfactuals: comment. J.Amer.Statist.As-
soc., 95, 424–425
Cox,D.R.(2012). Statisticalcausality: somehistoricalremarks. Pages1-5inCausality:
statistical perspectives and applications. Edited by C. Berzuini, P. Dawid, L. Bernardinelli.
Wiley, Chichester.
Dawid, A. P. (2000). Causality without counterfactuals. J. Amer. Statist. Assoc., 95,
407–424.
Dawid, A. P. (2024). Potential outcomes and decision-theoretic foundations for statisti-
cal causality: Response to Richardson and Robins. J. Causal Inference, 12, paper number
20230058.
Ding,P.andDasgupta,T.(2016). Apotentialtaleoftwobytwotablesfromcompletely
| randomized | experiments. | J. Amer. Statist. | Assoc., 111, | 157–168. |
| ---------- | ------------ | ----------------- | ------------ | -------- |
Fisher, R. A (1922). On the mathematical foundations of theoretical statistics. Phi-
| los. Trans. | Roy. Soc. | London Ser A, 222, | 309–368. |     |
| ----------- | --------- | ------------------ | -------- | --- |
Fisher, R. A (1935). The Design of Experiments. Oliver and Boyd, Edinburgh.
Holland,P.(1983). Statisticsandcausalinference. J.Amer.Statist.Assoc.,81,945–960.
Imbens, G. W. and Rubin, D. B. (2015). Causal Inference for Statistics, Social, and
Biomedical Sciences: An Introduction. Cambridge University Press, Cambridge.
Jin, Y. and Rothenh¨ausler, D. (2024). Tailored inference for finite populations: condi-
| tional validity | and transfer | across distributions. | Biometrika, | 111, 215–233. |
| --------------- | ------------ | --------------------- | ----------- | ------------- |

| 8   |     | H.S.BATTEYANDCHARLOTTEEDGAR |     |     |     |
| --- | --- | --------------------------- | --- | --- | --- |
McCullagh, P. and Nelder, J. (1989). Generalized Linear Models. Chapman and Hall,
London.
McCullagh, P. (1999). The algebraic structure of generalised linear models. University
| of Chicago, | technical report | number |     |     |     |
| ----------- | ---------------- | ------ | --- | --- | --- |
McCullagh, P. (2002). What is a statistical model? Ann. Statist., 30, 1225–1310.
| McCullagh, | P. (2022). | Ten Projects | in Applied | Statistics. | Springer, Cham. |
| ---------- | ---------- | ------------ | ---------- | ----------- | --------------- |
Neyman,J.,Iwaszkiewicz,K.andKolodziejczyk,S.(1935). Statisticalproblemsinagri-
cultural experimentation (with discussion). J. R. Statist. Soc. Suppl., 2, 107–180.
Popper, K. (1963). Conjectures and Refutations: The Growth of Scientific Knowledge.
| Routledge, | London. |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
Richardson, T. S. and Robins, J. M. (2023). Potential outcome and decision theoretic
foundations for statistical causality. J. Causal Inference, 11, paper number 20220012.
Rosenbaum, P. and Rubin, D. B. (1983). The central role of the propensity score in
| observational | studies for | causal | effects. Biometrika, | 70, 41–55. |     |
| ------------- | ----------- | ------ | -------------------- | ---------- | --- |
Robins, J., Rotnitzky, A. and Zhao, L. P. (1994). Estimation of regression coefficients
when some regressors are not always observed. J. Amer. Statist. Assoc., 89, 846–866.
Rubin, D. B. (1974). Estimating causal effects of treatments in randomized and non-
| randomized | studies. J. Educational |     | Psychology, | 66, 688–701. |     |
| ---------- | ----------------------- | --- | ----------- | ------------ | --- |
Stigler,S.(1976). Discussionof‘OnrereadingR.A.Fisher’byL.J.Savage. Ann.Statist.,
4, 441–500.
| Department | of Mathematics,                  | Imperial | College | London |     |
| ---------- | -------------------------------- | -------- | ------- | ------ | --- |
| Email      | address: h.battey@imperial.ac.uk |          |         |        |     |