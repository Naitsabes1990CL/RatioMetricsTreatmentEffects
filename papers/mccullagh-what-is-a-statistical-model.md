TheAnnalsofStatistics
2002,Vol.30,No.5,1225–1310
|     | WHAT |     | IS A     | STATISTICAL | MODEL?1 |     |     |
| --- | ---- | --- | -------- | ----------- | ------- | --- | --- |
|     |      |     | BY PETER | MCCULLAGH   |         |     |     |
UniversityofChicago
Thispaperaddressestwocloselyrelatedquestions,“Whatisastatistical
model?”and“Whatisaparameter?”Thenotionsthatamodelmust“make
sense,”andthataparametermust“haveawell-definedmeaning”aredeeply
| ingrained   | in     | applied | statistical | work, reasonably | well     | understood   | at an |
| ----------- | ------ | ------- | ----------- | ---------------- | -------- | ------------ | ----- |
| instinctive | level, | but     | absent      | from most formal | theories | of modelling | and   |
inference.Inthispaper,theseconceptsaredefinedinalgebraicterms,using
morphisms,functorsandnaturaltransformations.Itisarguedthatinference
| on the    | basis | of a model | is  | not possible unless | the model | admits | a natural     |
| --------- | ----- | ---------- | --- | ------------------- | --------- | ------ | ------------- |
| extension | that  | includes   | the | domain for which    | inference | is     | required. For |
example,predictionrequiresthatthedomainincludeallfutureunits,subjects
| or time | points. | Although | it  | is usually not | made explicit, |     | every sensible |
| ------- | ------- | -------- | --- | -------------- | -------------- | --- | -------------- |
statisticalmodeladmitssuchanextension.Examplesaregiventoshowwhy
| such        | an extension | isnecessary     |     | and whya       | formal theory | isrequired. | In the      |
| ----------- | ------------ | --------------- | --- | -------------- | ------------- | ----------- | ----------- |
| definition  | of           | a subparameter, |     | it is shown    | that certain  | parameter   | functions   |
| are natural |              | and others      | are | not. Inference | is meaningful | only        | for natural |
parameters.Thisdistinctionhasimportantconsequencesfortheconstruction
ofpriordistributionsandalsohelpstoresolveacontroversyconcerningthe
Box–Coxmodel.
1. Introduction. According to currently accepted theories [Cox and Hink-
ley (1974), Chapter 1; Lehmann (1983), Chapter 1; Barndorff-Nielsen and
Cox (1994), Section 1.1; Bernardo and Smith (1994), Chapter 4] a statistical
modelisasetofprobabilitydistributionsonthesamplespaceS.Aparameterized
→
statistical model is a parameter set (cid:1) together with a function P :(cid:1) P(S),
which assigns to each parameter point θ ∈(cid:1) a probability distribution P on S.
θ
HereP(S)isthesetofallprobabilitydistributionsonS.Inmuchofthefollowing,
:(cid:1)→P(S),and
itisimportanttodistinguishbetweenthemodelasafunctionP
theassociatedsetofdistributionsP(cid:1)⊂P(S).
In the literature on applied statistics [McCullagh and Nelder (1989); Gelman,
Carlin,SternandRubin(1995);CoxandWermuth(1996)],soundpracticaladvice
is understandably considered to be more important than precise mathematical
ReceivedJanuary2000;revisedJuly2001.
1SupportedinpartbyNSFGrantsDMS-97-05347andDMS-00-71726.
AMS2000subjectclassifications.Primary62A05;secondary62F99.
Keywordsandphrases.Aggregation, agricultural field experiment, Bayes inference, Box–Cox
model, category, causal inference, commutative diagram, conformal model, contingency table,
embedding,exchangeability,extendability,extensivevariable,fertilityeffect,functor,Gibbsmodel,
harmonicmodel,intensivevariable,interference,Kolmogorovconsistency,latticeprocess,measure
process, morphism, natural parameterization, natural subparameter, opposite category, quadratic
exponentialmodel,representation,spatialprocess,splinemodel,typeIIImodel.
1225

1226 P.MCCULLAGH
definitions. Thus, most authors do not offer a precise mathematical definition of
a statistical model. Typically, the preceding definition is taken for granted, and
appliedtoarangeofsensiblyconstructedmodels.
At a minimum, a Bayesian model requires an additional component in the
form of a prior distribution on (cid:1). A Bayesian model in the sense of Berger
(1985), Smith (1984) or Bernardoand Smith (1994)requires an extra component
in the form of a judgment of infinite exchangeability or partial exchangeability
in whichparametersare defined bylimits ofcertain statistics.AlthoughBayesian
formulations are not the primary focus of this paper, the notion that the model is
extendabletoasequence,usuallyinfinite,isakeyconcept.
The parameterization is said to be identifiable if distinct parameter values
give rise to distinct distributions; that is, P θ = P θ(cid:5) implies θ = θ (cid:5) . Thus, the
parameter is identifiable if and only if P :(cid:1) → P(S) is injective. Apart from
theseconditions,thestandarddefinitionpermitsarbitraryfamiliesofdistributions
toserveasstatisticalmodels,andarbitrarysets(cid:1)toserveasparameterspaces.
Forappliedwork,theinadequacyofthestandarddefinitionismatchedonlyby
the eccentricity of the formulations that are permitted. These examples make it
abundantly clear that, unless the model is embedded in a suitable structure that
permits extrapolation, no useful inference is possible, either Bayesian or non-
Bayesian.
To be fair, most authors sound a note of warning in their discussion of
statisticalmodels.Thus,forexample,CoxandHinkley[(1974),Chapter1],while
admitting that “it is hard to lay down precise rules for the choice of the family
of models,” go on to offer a range of recommendations concerning the model
and the parameterization. In particular, “the model should be consistent with
knownlimiting behavior”andthe parameterizationshouldbe suchthat“different
parameter[components]haveindividuallyclear-cutinterpretations.”Theintention
ofthisarticleistodefinesomeoftheseconceptsinpurelyalgebraicterms.
2. Examples.
2.1. Twelvestatisticalexercises. Thefollowinglistbeginswithfourexercises
inwhichthemodelsareplainlyabsurd.Thepointoftheexercises,however,isnot
somuchthedetectionofabsurdmodelsasunderstandingthesourcesofabsurdity.
Fromamorepracticalviewpoint,themoreinterestingexercisesarethoseinwhich
theabsurdityisnotobviousatfirstsight.
EXERCISE 1 (Abinaryregressionmodel). Consideramodelforindependent
binary responses in which certain covariates are prespecified. One of these
covariates is designated the treatment indicator. The model specifies a logit link
ifthenumberofsubjectsiseven,andaprobitlinkotherwise.Inferenceisrequired
forthetreatmenteffect.Predictionsarerequiredfortheresponseofafuturesubject
withspecifiedcovariatevalues.

|     |     |     | WHATISASTATISTICALMODEL? |     |     |     | 1227 |
| --- | --- | --- | ------------------------ | --- | --- | --- | ---- |
EXERCISE 2 (A randomized blocks model). Consider a randomized blocks
design with b blocks and k varieties. In the statistical model, all observationsare
independent and normally distributed with unit variance. The expected yield µ ij
of variety i in block j is assumed to be expressible in the following manner for
| somereal-valuedfunctionα |     |     | onvarietiesandβ | onblocks: |     |     |     |
| ------------------------ | --- | --- | --------------- | --------- | --- | --- | --- |
(cid:1)
|     |     |     | α +β , | ifk+biseven, |     |     |     |
| --- | --- | --- | ------ | ------------ | --- | --- | --- |
|     |     | =   | i j    |              |     |     |     |
µ
|     |     | ij  | exp(α +β | ), otherwise. |     |     |     |
| --- | --- | --- | -------- | ------------- | --- | --- | --- |
|     |     |     | i j      |               |     |     |     |
Onthebasisofthismodel,inferenceisrequiredintheformofaconfidenceinterval
| orposteriordistributionforaparticularvarietycontrastα |     |     |     |     | −α . |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- |
1 2
EXERCISE 3 (A linear regression model). In the standard linear regression
modelY ∼N(Xβ,σ2I )onRn,theparameter(β,σ2),isapointinRp×[0,∞).
n
|        |          |           |              |                 | (cid:1)=Rp | ×[n,∞), |     |
| ------ | -------- | --------- | ------------ | --------------- | ---------- | ------- | --- |
| In our | modified | eccentric | version, the | parameter space | is         |         | so  |
that σ2 ≥n. A prediction interval is required for the value of the response on a
newsubjectwhosecovariatevalueisx∈Rp.
EXERCISE 4 [An i.i.d. normal model (Section 6.6)]. In this model, the
observations are independent, identically distributed and normal. The parameter
spaceis(cid:1)=R2.Ifniseven,themeanisθ andthevarianceisθ2:otherwise,the
1
2
mean is θ and the variance is θ2. On the basis of observed values (y ,...,y ),
|     | 2   |     | 1   |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- |
inference is required in the form of confidence limits or a posterior distribution
on(cid:1).
EXERCISE 5 [The type III model (Section 6.6)]. Consider a randomized
blocksdesign as in Exercise2 above,all observationsbeing independent,normal
withunitvariance.AccordingtothetypeIIImodelasdescribedintheSASmanual
[Littell,FreundandSpector(1991),pages156–160],thevectorµliesinthelinear
subspaceIII ofdimensionbk−k+1suchthatthek varietymeansareequal,
kb
|     |     | III | ={µ∈Rkb:µ¯ | =···=µ¯ | }.  |     |     |
| --- | --- | --- | ---------- | ------- | --- | --- | --- |
|     |     |     | kb         | 1.      | k.  |     |     |
On the assumption that the fit is adequate, what conclusions can be drawn about
variety differences on either a subset of the blocks or on other blocks similar to
someofthoseusedintheexperiment?
EXERCISE 6 [The Box–Cox model (Section 7)]. In the Box–Cox model
[Box and Cox (1964)], it is assumed that after some componentwise power
(cid:17)→Yλ,
transformation Y the transformed response variable satisfies the standard
|     |     | i i |     |        |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     | E(Yλ)= |     |     | σ2. |
normal-theory linear model with mean Xβ and constant variance
In the problem posed by Bickel and Doksum (1981), inference is required in the
form of confidence intervals or a posterior distribution for the parameter β or a
componentthereof.

| 1228 |     |     | P.MCCULLAGH |     |     |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- | --- | --- |
EXERCISE 7 [A model for clustered data (Section 6.6)]. In a cluster of
size k, the response Y has joint density with respectto Lebesguemeasureon Rk
proportionalto
|     |     |     | (cid:2) |         |           | (cid:4) |     |     |
| --- | --- | --- | ------- | ------- | --------- | ------- | --- | --- |
|     |     |     | 1       | (cid:3) | 1 (cid:3) | y y     |     |     |
|     |     |     | −       | y2+     |           | i j     |     |     |
|     |     | exp | θ       |         | θ         |         |     |     |
|     |     |     | 2 1     | i       | 2 2       | k−1     |     |     |
i(cid:18)=j
for some θ >0 and 0≤θ <θ . Thus, the vector Y is normally distributed with
|     | 1   |     | 2 1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
zero mean and exchangeable components. Observations on distinct clusters are
|     |     |     |     |     |     | (k ,Y ),...,(k | ,Y ), |     |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | --- |
independent. On the basis of the observed data 1 1 n n in which
k is the size of cluster r and Y normally distributed on Rkr, a confidenceset is
| r   |     |     | r   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
required for θ. In particular, if the observedclusters are all of size 2, inference is
requiredforthedistributionoftheclustermeaninaclusterofsize8.
EXERCISE 8 [An i.i.d. Cauchy model (Section 6.6)]. By the two-parameter
| CauchyfamilyismeantthesetofdistributionsonR |     |         |     |     |     | withdensities |     |     |
| ------------------------------------------- | --- | ------- | --- | --- | --- | ------------- | --- | --- |
|                                             |     | (cid:5) |     |     |     | (cid:6)       |     |     |
|θ |dy
|     |     |           | 2   |     | (cid:18)=0, | ∈R  |     |     |
| --- | --- | --------- | --- | --- | ----------- | --- | --- | --- |
|     |     |           |     |     | :θ          | θ . |     |     |
|     |     | π(θ2+(y−θ |     | )2) | 2           | 1   |     |     |
1
2
LetY ,...,Y benindependentandidenticallydistributedrandomvariableswith
| 1   | n   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
distributioninthetwo-parameterCauchyfamily.Aconfidenceintervalorposterior
distribution is required for the parameter θ . The catch here is that the Cauchy
1
family isclosedundertherealfractionallineargroup,andtheconfidenceinterval
isrequiredtohavethecorrespondingproperty.Inotherwords,foranyrealnumbers
|              |      | −bc(cid:18)=0, |     |        |           | =(aY | +b)/(cY | +d) |
| ------------ | ---- | -------------- | --- | ------ | --------- | ---- | ------- | --- |
| a,b,c,d such | that | ad             | the | random | variables | Z i  | i       | i   |
arei.i.d.Cauchy.Ifwewriteθ =θ ±iθ asaconjugatepairofcomplexnumbers,
|                 |           |     |      | 1 2     |     |            |        |         |
| --------------- | --------- | --- | ---- | ------- | --- | ---------- | ------ | ------- |
|                 |           |     | =(aθ | +b)/(cθ | +d) |            |        |         |
| the transformed | parameter |     | is ψ |         |     | [McCullagh | (1992, | 1996)]. |
TheprocedureusedmustbesuchthatifthevaluesZ 1 ,...,Z n arereportedasi.i.d.
Cauchy(ψ),andaconfidenceintervalisrequestedforθ =(cid:22)((dψ−b)/(a−cψ)),
1
thesameanswermustbeobtainedregardlessofthevaluesa,b,c,d.
EXERCISE 9 (A model for a spatial process). The temperature in a room
is modelled as a stationary isotropic Gaussian process in which the mean
|                          |                               |     | )=µ,andthecovariancefunctionis |     |     |     |       | x(cid:5))= |
| ------------------------ | ----------------------------- | --- | ------------------------------ | --- | --- | --- | ----- | ---------- |
| temperatureisconstantE(Y |                               |     | x                              |     |     |     | cov(Y | x ,Y       |
| σ2exp(−λ|x−x             | (cid:5)|).Theparameterspaceis |     |                                |     |     |     |       |            |
(µ,σ2,λ)∈R×(0,∞)2.
=µ/σ.
Aconfidenceintervalisrequiredforθ
EXERCISE 10 [Regression and correlation (Section 6.2)]. Consider the
standard normal-theory linear regression model with one covariate in which

WHATISASTATISTICALMODEL? 1229
the observations are independent, normally distributed with conditional mean
E(Y|x)=α+βx andconstantvarianceσ2.Theparameterspaceis
(α,β,σ2)∈R2×[0,∞).
A confidence interval or posterior distribution is required for the correlation
coefficient.
EXERCISE 11 [Spatialsimultaneousequationmodel(Section6.5)]. LetY be
aspatialprocessobservedonarectangularlatticeofsites.Thejointdistributionis
definedbyasetofsimultaneousequations
(cid:3)
Y = βY +ε ,
i j i
j∼i
in which j ∼i means that site j (cid:18)=i is a neighbour of site i. This expression is
interpreted to mean that (I −B)Y =ε is standard normal. The componentsof B
are zero except for neighboring sites for which b =β. The system is such that
ij
I −B is invertible, so that Y is normal with zero mean and inverse covariance
matrix(I −B)T(I −B).Aconfidenceintervalisrequiredforβ.
EXERCISE 12 [Contingency table model (Section 6.4)]. All three factors in
a contingency table are responses. In principle, each factor has an unbounded
number of levels, but some aggregation has occurred, and factor B is in fact
recorded in binary form. The log-linear model AB +BC is found to fit well, but
nolog-linearsubmodelfits.Whatconclusionscanbedrawn?
2.2. Remarks. These exercises are not intended to be comparable in their
degreeofabsurdity.Theyareintendedto illustrate a rangeofmodelformulations
and inferential questions, some clearly artificial, some a little fishy, and others
bordering on acceptability. In the artificial class, I include Exercises 1, 2, 4,
and possibly 3. Exercise 9 ought also to be regarded as artificial or meaningless
on the grounds of common sense. The type III model has been criticized from
a scientific angle by Nelder (1977) in that it represents a hypothesis of no
scientificinterest.Despitethis,thetypeIIImodelcontinuestobepromotedintext
books[Yandell(1997), page172]andsimilar modelsobeyingthe so-calledweak
heredity principle [Hamada and Wu (1992)] are used in industrial experiments.
Theabsurdityintheotherexercisesisperhapslessobvious.Althoughtheyappear
radically different, from an algebraic perspectiveExercises 2 and 5 are absurd in
rathersimilarways.
Eachofthe formulations satisfiesthe standarddefinition ofa statistical model.
With respect to a narrowly defined inferential universe, each formulation is
also a statistical model in the sense of the definition in Sections 1 and 4.
Inference, however, is concerned with natural extension, and the absurdity of

1230 P.MCCULLAGH
each formulation lies in the extent of the inferential universe or the scope of the
model. Although a likelihood function is available in each case, and a posterior
distributioncanbecomputed,noinferentialstatementcanbreachtheboundsofthe
inferentialuniverse.Totheextentthatthescopeofthemodelisexcessivelynarrow,
noneoftheformulationspermitsinferenceinthesensethatonemightreasonably
expect.We concludethat, in the absenceofa suitableextension,a likelihood and
apriorarenotsufficienttopermitinferenceinanycommonlyunderstoodsense.
3. Statisticalmodels.
3.1. Experiments. Each statistical experiment or observational study is built
fromthefollowingobjects:
1. AsetUofstatisticalunits,alsocalledexperimentalunits,plots,orsubjects;
2. Acovariatespace);
3. AresponsescaleV.
The design is a function x:U→ ) that associates with each statistical unit
i ∈U a point x in the covariate space ). The set D =)U of all such functions
i
fromtheunitsintothecovariatespaceiscalledthedesignspace.
Theresponseisafunctiony:U→V thatassociateswitheachstatisticaluniti,
a response value y in V. The set S = VU of all such functions is called the
i
sample spacefor the experiment.In the definition givenin Section 1, a statistical
model consists of a design x:U→), a sample space S =VU and a family of
distributionsonS.
A statistical model P :(cid:1) → P(S) associates with each parameter value θ
adistributionPθ onS.Ofnecessity,thismapdependsonthedesign,forexample,
ontheassociationofunitswithtreatments,andthenumberoftreatmentlevelsthat
occur. Thus, to each design x:U→), there correspondsa map P :(cid:1)→P(S)
x
suchthat P θ is a probability distribution on S. Exercise2 suggestsstrongly that
x
thedependenceofP onx∈D cannotbearbitraryorcapricious.
x
3.2. The inferential universe. Consider an agricultural variety trial in which
the experimental region is a regular 6 × 10 grid of 60 rectangular plots, each
seven meters by five meters, in which the long side has an east–westorientation.
It is invariably understood, though seldom stated explicitly, that the purpose of
such a trial is to draw conclusions concerning variety differences, not just for
plots of this particular shape, size and orientation, but for comparable plots of
various shapes,sizes and orientations. Likewise,if the trial includessevenpotato
varieties, it should ordinarily be possible to draw conclusions about a subset of
three varieties from the subexperiment in which the remaining four varieties are
ignored.Theseintroductoryremarksmayseemobviousandunnecessary,butthey
havefar-reachingimplicationsfortheconstructionofstatisticalmodels.

WHATISASTATISTICALMODEL? 1231
The first point is that before any model can be discussed it is necessary to
establishaninferentialuniverse.Themathematicaluniverseofexperimentalunits
might be defined as a regular 6 × 10 grid of 7 × 5 plots with an east–west
orientation. Alternatively, it could be defined as the set of all regular grids of
rectangular plots, with an east–west orientation. Finally, and more usefully, the
universecouldbedefinedasasuitablylargeclassofsubsetsoftheplane,regardless
of size, shape and orientation. From a purely mathematical perspective, each of
these choices is internally perfectly consistent. From the viewpoint of inference,
statisticalorotherwise,thefirstandsecondchoicesdeterminealimiteduniversein
which all inferential statements concerning the likely yields on odd-shaped plots
ofarbitrarysizeareoutofreach.
In addition to the inferential universe of statistical units, there is a universe
of response scales. In an agricultural variety trial, the available interchangeable
response scales might be bushels per acre, tones per hectare, kg/m2, and so on.
◦ ◦ ◦
In a physics or chemistry experiment, the response scales might be C, K, F,
or other suitable temperature scale. In a food-tasting experiment, a seven-point
orderedscalemightbeusedinwhichthelevelsarelabelledas
V={unacceptable,mediocre,...,excellent},
orathree-pointscalewithlevels
V
(cid:5)={unacceptable,satisfactory,verygood}.
It is then necessary to consider transformations V →V (cid:5) in which certain levels
of V are, in effect, aggregatedto form a three-levelscale. Finally, if the response
scaleisbivariate,includingbothyieldandquality,thisshouldnotusuallypreclude
inferentialstatementsconcerningqualityorquantityinisolation.
Similar comments are in order regarding the covariate space. If, in the
experimentactuallyconducted,fertilizer wasappliedattherates,0, 100,200and
300 kg/ha, the inferential universe should usually include all nonnegativedoses.
Likewise, if seven varieties of potato were tested, the inferential universe should
includeall setsof varietiesbecausetheseparticularvarieties are a subsetofother
setsofvarieties.Thisdoesnotmeanthatinformativestatementscanbemadeabout
the likely yield for an unobserved variety, but it does mean that the experiment
performed may be regarded as a subset of a larger notional experiment in which
furthervarietiesweretestedbutnotreported.
3.3. Categories. Every logically defensible statistical model in the classical
sensehasanaturalextensionfromthesetofobservedunits,orobservedvarieties,
orobserveddoselevels,tootherunobservedunits,unobservedblocks,unobserved
treatments, unobserved covariate values and so on. Thus, in constructing a
statisticalmodel,itisessentialtoconsidernotonlytheobservedunits,theobserved
blocks, the observed treatments and so on, but the inferential universe of all

1232 P.MCCULLAGH
relevant sample spaces, all relevant sets of blocks, all relevant covariate values
and so on. Every sensible statistical model does so implicitly. The thesis of this
paperisthatthelogicofeverystatisticalmodelisfounded,implicitlyorexplicitly,
on categories of morphisms of the relevant spaces. The purpose of a category is
toensurethatthefamiliesofdistributionsondifferentsamplespacesarelogically
related to one another and to ensure that the meaning of a parameter is retained
fromonefamilytoanother.
AcategoryCisasetofobjects,togetherwithacollectionofarrowsrepresenting
maps or morphisms between pairs of objects. In the simplest categories, each
objectisaset,andeachmorphismisamap.However,inthecategoryofstatistical
designs,eachdesignisamapandeachmorphismisapairofmaps,soamorphism
(cid:5)
neednotbeamapbetweensets.Toeachorderedpair(S,S )ofobjectsinC,there
correspondsasethom (S,S (cid:5) ),alsodenotedbyC(S,S (cid:5) ),ofmorphismsϕ:S →S (cid:5) ,
C
(cid:5)
withdomainS andcodomainS .Forcertainorderedpairs,thissetmaybeempty.
Two conditions are required in order that such a collection of objects and arrows
should constitute a category. First, for each object S in C, the identity morphism
1:S→S isincludedinhom(S,S).Second,foreachpairofmorphismsϕ:S→S (cid:5)
and ψ:S (cid:5) → S (cid:5)(cid:5) , such that domψ = codϕ, the composition ψϕ:S → S (cid:5)(cid:5) is a
(cid:5)(cid:5)
morphism in hom(S,S ) in C. In particular, the set hom(S,S) of morphisms
of a given object is a monoid, a semigroup containing the identity and closed
undercomposition.A glossary of certain categoryterminology is providedin the
Appendix.Forallfurtherdetailsconcerningcategories,seeMacLane(1998).
In the discussion that follows, the symbol cat represents the category of
U
(cid:5)
morphisms of units. The objects in this category are all possible sets U,U,...
of statistical units. These sets may have temporal, spatial or other structure.
The morphisms ϕ:U→ U (cid:5) in cat are maps, certainly including all insertion
U
maps ϕ:U→U (cid:5) (such that ϕu=u) whenever U⊂U (cid:5) . In general, cat is the
U
categoryofmorphismsthatpreservesthestructureoftheunits,suchasequivalence
relationships in a block design [McCullagh (2000), Section 9.5] or temporal
structureintimeseries.Intypicalregressionproblemstherefore,cat isidentified
U
with thethegenericcategoryI ofinjective,or1–1,mapsonfinitesets.Theseare
the maps that preserve distinctness of units: u(cid:18)=u (cid:5) in U implies ϕ(u)(cid:18)= ϕ(u (cid:5) )
(cid:5)
inU.
Aresponseisavaluetakenfromacertainset,orresponsescale.Iftheresponse
is a temperature, each object in cat is a temperature scale, including one object
V
◦ ◦ ◦
for each of the conventional scales C, F and K. To each ordered pair of
(cid:5)
temperaturescales(V,V ) therecorrespondsasingleinvertible map,whichis an
affine transformation V →V (cid:5) . Likewise, yield in a variety trial may be recorded
onanumberofscalessuchasbushels/acre,tones/haorkg/m2.Toeachresponse
scale there corresponds an object V in cat , and to each pair of response scales
V
there correspondsa singleinvertible map,which is a positivescalarmultiple. For
atypicalqualitativeresponsefactorwithorderedlevels,themorphismsareorder-
preserving surjections, which need not be invertible. Special applications call for

WHATISASTATISTICALMODEL? 1233
other sorts of morphisms, such as censoring in survival data. The essential point
hereisthateachresponsescaledeterminesadistinctobjectincat ,andthemaps
V
V →V (cid:5) aresurjective(onto).
Sincestatisticalinferencesareinvariablyspecifictothescaleofmeasurement,it
isabsolutelyessentialthatthevariousquantitativeresponsescalesnotbefusedinto
+
oneanonymousscalelabelled R or R . An affinetransformation oftemperature
scalesisatransformationϕ:V →V (cid:5) fromonescaleintoanother.UnlessV =V (cid:5) ,
suchatransformationisnotcomposablewithitself,acriticaldistinctionthatislost
ifallscalesarefusedintoR.Thus,althoughcat maybeacategoryofinvertible
V
maps,itisordinarilynotagroup.
Likewise, the symbol cat represents the category whose objects are the
)
covariate spaces, and whose morphisms are maps, ordinarily injective, between
covariatespaces.Becauseof the greatvariety of covariatespaces,these mapsare
more difficult to describe in general. Nonetheless, some typical examples can be
described.
A quantitativecovariatesuchas weight is recordedon a definite scale,such as
pounds, stones or kg. To each scale ) there corresponds a set of real numbers,
(cid:5)
and to each pair (),)) of quantitative scales there corresponds a 1–1 map
) → ) (cid:5) , usually linear or affine. The objects in cat are some or all subsets
)
of each measurement scale. For some purposes, it is sufficient to consider only
bounded intervals of each scale: for other purposes, all finite subsets may be
sufficient. Generally speaking, unless there is good reason to restrict the class of
sets,theobjectsincat areallsubsetsofallmeasurementscales.Themorphisms
)
are those generated by composition of subset insertion maps and measurement-
scale transformation. Thus, cat may be such that there is no map from the set
)
{tenstones,elevenstones} into {140lbs,150lbs,160lbs} but there is one map
into{x lbs:x≥0}whoseimageisthesubset{140lbs,154lbs}.
For a typical qualitative covariate such as variety with nominal unordered
levels, the objects are all finite sets, and cat may be identified with the generic
)
category I, of injective maps on finite sets. If the levels are ordinal, cat may
)
be identified with the subcategory of order-preserving injective maps. Factorial
designshaveseveralfactors,inwhichcasecat isacategoryinwhicheachobject
)
isaproductset)=) ×···×) .Therelevantcategoryofmorphismsisusually
1 k
the product category, one component category for each factor. For details, see
McCullagh(2000).
4. Functorsandstatisticalmodels.
4.1. Definitions. Itisassumedinthis sectionthattheresponseis anintensive
variable, a V-valued function on the units. Extensive response variables are
discussedin Section 8. In mathematicalterms, an intensive variable is a function
on the units: an extensive variable such as yield is an additive set function. The
importance of this distinction in applied work is emphasized by Cox and Snell

| 1234 |     | P.MCCULLAGH |     |     |     |     |
| ---- | --- | ----------- | --- | --- | --- | --- |
[(1981), Section 2.1]. The implications for the theory of random processes are
discussedbrieflybyKingman[(1984),page235].
In terms of its logical structure, each statistical model is constructed from the
followingthreecomponents:
1. A category cat in which each object U is a set of statistical units. The
U
→ (cid:5)
morphisms U U in cat U are all injective maps preserving the structure
of the units. In typical regression problems, cat may be identified with the
U
categoryIofallinjectivemapsonfinitesets.
2. A category cat in which each object ) is a covariate space. The morphisms
)
(cid:5)
)→) areallinjectivemapspreservingthestructureofthecovariatespaces.
3. A category cat V in which each object V is a response scale. The morphisms
(cid:5)
V →V are all mapspreservingthe structure of the responsescale.Theseare
typicallysurjective.
Thesethreecategoriesare thebuilding blocksfrom whichthe designcategory,
thesamplespacecategoryandallstatisticalmodelsareconstructed.
Uandacovariatespace),thedesignisamapx:U→)
Givenasetofunits
associatingwith eachunit u∈U a point x in the covariatespace). In practice,
u
this information is usually coded numerically for the observed units in the form
of a matrix X whose uth row is the coded version of x u . The set of all such
designsisacategorycat inwhicheachobjectx isapair(U,))togetherwitha
D
x:U→).Sincethe
| map |     | domainandcodomainare |     | understoodto | bepartofthe |     |
| --- | --- | -------------------- | --- | ------------ | ----------- | --- |
definition of x, the set of designs is the set of all such maps with U in cat and
U
)in cat ,in effect,thesetofmodelmatricesX withlabelledrowsandcolumns.
)
|     | →x  | (cid:5) | (cid:5) (cid:5) →) | (cid:5) |     |     |
| --- | --- | ------- | ------------------ | ------- | --- | --- |
Each morphism ϕ:x in which x :U , may be associated with a pair
|     |     | (cid:5) |     | (cid:5) |     |     |
| --- | --- | ------- | --- | ------- | --- | --- |
of injective maps ϕ :U → U in cat , and ϕ :)→ ) in cat such that the
|     | d   |     | U c |     | )   |     |
| --- | --- | --- | --- | --- | --- | --- |
diagram
−→x
|     |     | U          | )          |     |     |     |
| --- | --- | ---------- | ---------- | --- | --- | --- |
|     |     |            |          |     |     |     |
|     |     |            |          |     |     |     |
|     |     |            |          |     |     |     |
|     |     | ϕ d(cid:8) | ϕ c(cid:8) |     |     |     |
(cid:5)
|     |     |     | (cid:5) −x→ (cid:5) |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | --- |
|     |     | U   | )                   |     |     |     |
(cid:5)
commutes [Tjur (2000)]. In other words x ϕ d and ϕ c x represent the same design
U→) (cid:5) . In matrix notation, X (cid:5) =UXW in which U is a row selection matrix,
andW isacode-transformationmatrix.
The general idea behind this construction can be understood by asking what
it means for one design to be embedded in another. Here we consider simple
embeddings obtained by selection of units or selection of covariate values. First,
consider the effect of selecting a subset U⊂U (cid:5) of the units and discarding the
|                | :U→U | (cid:5) | insertionmapthatcarrieseachu∈U |     |     |          |
| -------------- | ---- | ------- | ------------------------------ | --- | --- | -------- |
| remainder.Letϕ |      | bethe   |                                |     |     | toitself |
d
| asanelementofU.ThedesignthatremainswhentheunitsnotinUarediscarded | (cid:5) |         |     |     |         |     |
| ----------------------------------------------------------------- | ------- | ------- | --- | --- | ------- | --- |
|                                                                   | (cid:5) | (cid:5) |     |     | (cid:5) |     |
isthecompositionx ϕ :U→) ,whichistherestrictionofx toU.Thediagram
d

|     |     |     | WHATISASTATISTICALMODEL? |     |     |     |     |     |     | 1235 |
| --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | ---- |
may thus be completed by taking )=) (cid:5) , ϕ the identity, and x =x (cid:5) ϕ . Next,
|     |     |     |     |     |     | c   |     |     | d   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consider the effect of selection based on covariate values, that is, selecting only
|       |         |       |           |        |     |               | )⊂) | (cid:5) | :)→)      | (cid:5) |
| ----- | ------- | ----- | --------- | ------ | --- | ------------- | --- | ------- | --------- | ------- |
| those | units U | whose | covariate | values | lie | in the subset |     |         | . Let ϕ c |         |
(cid:5)
and ϕ :U→U be theassociatedinsertionmaps.Thedesignmap x:U→) is
d
|          | (cid:5) restrictedtothedomainUandcodomain)⊂) |     |     |     |     |     |     | (cid:5) .Finally,ifU=U |     | (cid:5) |
| -------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------- |
| givenbyx |                                              |     |     |     |     |     |     |                        |     | ,       |
)=) (cid:5) andϕ isapermutationof),thedesignϕ x issimplythedesignx witha
|     |     | c   |     |     |     | c   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rearrangementoflabels.Thesamedesigncouldbeobtainedbysuitablypermuting
| theunitsbeforeusingthedesignmapx,thatis,thedesignxϕ |     |     |     |     |     |     |     | d . |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.2. Model. Let V be a fixed response scale. A response y on U is a
function y:U → V, a point in the sample space VU. To each set U there
VU
corresponds a sample space of V-valued functions on U. Likewise, to each
injectivemorphismϕ:U→U (cid:5) incat therecorrespondsacoordinate-projection
U
|     |     | (cid:5) |     |     | (cid:5) |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
map ϕ ∗ :VU → VU. For f ∈ VU , the pullback map defined by functional
∗
composition ϕ f =f◦ϕ is a V-valued function on U. Thus (V,∗) is a functor
VU,
on cat U , associating with each set U the sample space and with each
|     |     |     | (cid:5) | ∗   | (cid:5) |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |
morphism ϕ:U→U the map ϕ :VU →VU by functional composition. The
identitymapU→UiscarriedtotheidentityVU→VU
andthecompositemap
(cid:5)(cid:5)
| ψϕ:U→U |     | (cid:5)(cid:5) tothecompositeϕ |     | ∗ ψ | ∗ :VU | →VU | inreverseorder. |     |     |     |
| ------ | --- | ------------------------------ | --- | --- | ----- | --- | --------------- | --- | --- | --- |
Beforepresentingageneraldefinitionofastatisticalmodel,itmaybehelpfulto
giveadefinitionofalinearmodel.LetVbeavectorspace,sothatthesamplespace
VU isalsoavectorspace.AlinearmodelisasubspaceofVU,suitablyrelatedto
the design. In the functor diagram below, each map in the right square is a linear
V)(cid:5)
transformation determined by functional composition. Thus, for f ∈ , the
|                |     |          | ∗ =f◦ϕ  |                   |              |             | V).Likewise,ψ |         | (cid:5)∗ =f | (cid:5) |
| -------------- | --- | -------- | ------- | ----------------- | ------------ | ----------- | ------------- | ------- | ----------- | ------- |
| pullbackbyϕ    |     | is ϕ     | f       | ,whichisavectorin |              |             |               |         | f           | ◦ψ      |
|                |     | c        | c       | c                 |              |             |               |         |             |         |
| isavectorinVU, |     | (cid:5)  |         |                   |              |             |               |         |             |         |
|                |     |          | Design  |                   |              | Linearmodel |               |         |             |         |
|                |     |          | −ψ→     |                   |              |             | ←ψ− ∗         |         |             |         |
|                |     | U        |         | )                 | S=VU         |             |               | (cid:1) | ⊂V)         |         |
|                |     |         |         |                  |              | (cid:9)     |               | )       | (cid:9)     |         |
|                |     |         |         |                  |              |            |               |         |            |         |
|                |     | ϕ       |         | ϕ                | ϕ            | ∗          |               |         |  ϕ ∗      |         |
|                |     | d(cid:8) |         | c(cid:8)          |              | d          |               |         | c           |         |
|                |     |          | −ψ→     | (cid:5)           |              | (cid:5)     | ←ψ(cid:5) ∗   |         | ⊂V)(cid:5)  |         |
|                |     | U        | (cid:5) | ) (cid:5)         | S (cid:5)=VU |             | −             | (cid:1) | .           |         |
)(cid:5)
AsdefinedinMcCullagh(2000),alinearmodelisdeterminedbyasubrepresenta-
|             | ⊂V),togetherwiththedesignpullbackmapψ |     |     |     |     |     |     | ∗                          |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
| tion(cid:1) |                                       |     |     |     |     |     |     | .Asubrepresentation(cid:1) |     |     |
)
inthestandardrepresentationV) isasequenceofsubspaces{(cid:1) ⊂V)},indexed
)
(cid:5)
bytheobjectsincat suchthat,foreachmapϕ :)→) incat ,thelineartrans-
|            |     |              | )   |                |     | c                |     |     | )   |     |
| ---------- | --- | ------------ | --- | -------------- | --- | ---------------- | --- | --- | --- | --- |
|            |     | ∗ :V)(cid:5) | →V) |                | ∗   | =(cid:1)         |     |     |     |     |
| formationϕ |     |              |     | alsosatisfiesϕ |     | (cid:1) )(cid:5) | ) . |     |     |     |
|            | c   |              |     |                | c   |                  |     |     |     |     |
Thisskeletondescriptionofalinearmodelfocusesonlyonthelinearsubspace,
andsaysnothingaboutprobability distributionsonthesamplespace.In theusual
completeformulation,theparameterspaceisextendedto(cid:1)×R + bytheinclusion
of a dispersion parameter σ2. For the design ψ:U → ), the sample space is

1236 P.MCCULLAGH
S=VU,andthefullnormal-theorylinearmodelisthesetofnormaldistributions
∗
with mean vectorin the subspaceψ (cid:1) , andvariancematrix proportional to the
)
identity.
Theskeletaldescriptionissharedbynonnormallinearmodels,certainnonlinear
models and all generalized linear models [McCullagh and Nelder (1989)]. The
onlymodificationrequiredisthestepbywhichtherepresentation(cid:1)determinesa
family of distributions on S. In generalizedlinearmodels,this step is determined
by the linear predictor η=ψ ∗ θ from (cid:1) into VU, an invertible link function η=
g(µ) that is also a natural componentwise transformation VU → VU, together
withasuitableerrordistributionwithindependentcomponents.
Thegeneralconstructionfollowsthesamelines.ForeachfixedV,theparameter
((cid:1),∗)is acontravariantfunctorcat →K associatingwith eachcovariateset)
)
a parameter set (cid:1) , and with each (injective) covariate morphism ϕ :)→) (cid:5)
) c
a surjective parameter map ϕ c ∗ :(cid:1) )(cid:5) → (cid:1) ) . Frequently, K is the category of
surjective linear transformations on vector spaces, in which case (cid:1) is called a
representation of cat . A statistical model is a functor on cat associating with
) D
each design object ψ:U→) a model object, which is a map P :(cid:1) →P(S)
ψ )
such that P θ is a probability distribution on S. The set of distributions thus
ψ
generated is F = P (cid:1) . To each morphism (ϕ ,ϕ ):ψ → ψ (cid:5) in cat , the
ψ ψ ) d c D
functorassociatesamap(ϕ d † ,ϕ c ∗ ):P ψ(cid:5) →P ψ asillustratedbelow:
Design Samplespace Model
U −ψ→ ) S=VU P(S) ← Pψ− (cid:1)
  (cid:9) (cid:9) (cid:9))
(1)     
ϕ d

(cid:8) ϕ c

(cid:8) ϕ d
∗
 ϕ d
†
 ϕ c
∗

U (cid:5) −ψ→ (cid:5) ) (cid:5) S (cid:5)=VU (cid:5) P(S (cid:5) ) ← P ψ− (cid:5) (cid:1) )(cid:5) .
As usual in such diagrams, the maps in both squares are assumed to commute.
Someconsequencesofthisdefinitionareasfollows:
1. The sample-space transformation ϕ ∗ :S (cid:5) →S also carries each distribution F
d
onS (cid:5) tothetransformeddistributionϕ†F =F ◦ϕ ∗−1 onS.
d d
2. Commutativity: P ψ ϕ c ∗ = ϕ d †P ψ(cid:5):(cid:1) )(cid:5) → P(S). In other symbols, for each
θ ∈(cid:1) )(cid:5),P
ψ
ϕ
c
∗ θ =ϕ
d
† P ψ(cid:5)θ.
Condition(1)ensuresthatthefamilyofdistributionsonS issuitablyembedded
in the family of distributions on S (cid:5) . The maps ϕ ∗ :S (cid:5) → S that define this
d
embedding depend on the category of morphisms on units. For ϕ equal to the
c
∗
identityon),andthusϕ theidentityon(cid:1) ,theconsistencycondition(2)asserts
c )
that the distribution P
ψ
θ on S is the same as the marginal distribution of P ψ(cid:5)θ
onS
(cid:5)
bytheembeddingmapϕ
∗
:S
(cid:5)→S.
d

WHATISASTATISTICALMODEL? 1237
The association U (cid:17)→ VU,ϕ (cid:17)→ ϕ ∗ determines the structure of the sample
d d
spacesasfunctoroncat ,andthusasafunctoroncat .Thesetofmorphismsof
U D
op
sample spaces is in fact a category isomorphic with cat , the category obtained
U
byreversingallarrowsincat .Likewise,theassociationU(cid:17)→P(VU),ϕ (cid:17)→ϕ †
U d d
op
is also a functor on cat whose image is isomorphic with cat . The mapping
U U
S (cid:17)→ P(S),ϕ ∗ (cid:17)→ ϕ † is an isomorphism of categories. The parameter (cid:1) is a
d d
functor on cat and thus also a functor on cat . The model P :(cid:1) → P(S) is
) D
thusanaturaltransformationoffunctorsoncat .
D
Let P,Q:(cid:1) → P(S) be two models having the same domain (cid:1). For each
0≤α≤1,the convexcombinationαP +(1−α)Q is alsoa statisticalmodel, so
thesetofmodels(cid:1)→P(S)isconvex.Themajorityofnon-Bayesianmodelsthat
occurinpracticeareextremepointsofthisset[Lauritzen(1988)].
Aglanceatalmostanybookonstatisticalmodellingshowsthattheconceptsof
amodel“makingsense,”andaparameter“havingameaning”aredeeplyingrained
in statistical thinking and well understood at an instinctive level. The purpose of
the preceding definitions is to state in purely mathematical terms what is meant
by a model “making sense” logically (as opposed to making sense physically or
biologically). The sense of a model and the meaning of a parameter, whatever
they may be, must not be affected by accidental or capricious choices such as
†
samplesizeorexperimentaldesign.Thedefinitionofthemapϕ ,togetherwiththe
d
commutativitycondition(2),ensuresthatthemeaningoftheparameterisretained
for families on different sample spaces and different designs. The parameter
∗
sets (cid:1) , and the maps P and ϕ are not otherwise prescribed, so the framework
) c
providesampleopportunityforimaginativeconstructionofspecificmodels.Note,
forexample,thatifϕ istheidentityon),ϕ†istheidentityon(cid:1) ,sothemarginal
c c )
†
distributionofP ψ(cid:5)θ bythemapϕ
d
isequaltoP
ψ
θ.
4.3. Composition, mixtures and hierarchical models. To each set S we
associatethevectorspacevect(S)offormallinearcombinationsα s +α s +···
1 1 2 2
of the elements of S. By restricting these formal linear combinations to formal
(cid:10)
convex combinations in which α ≥0 and α =1, we obtain the set P(S)⊂
i i
vect(S) of probability distributions on S. If S is countable, each formal convex
combination α s + α s + ··· may be interpreted as an actual operation in
1 1 2 2
whichanelementof{s ,s ,...}ischosenaccordingtotheprobabilitydistribution
1 2
{α ,α ,...}.Thepointofthisabstractconstructionisthateachfunctionh:S→T
1 2
determinesalineartransformationh ∗ :vect(S)→vect(T)by
h ∗ (α s +α s +···)=α h(s )+α h(s )+··· .
1 1 2 2 1 1 2 2
∗
Evidently h also carries the subset P(S) into P(T). The extreme points of
P(S)maythusbeidentifiedwiththeelementsofS.Thiscorrespondencebetween
h:S → T and h ∗ :vect(S) →vect(T) is so natural that, wherever possible, the

1238 P.MCCULLAGH
notational distinction is avoided. Given h:S → T, formal linearity determines
h:P(S)→P(T).
Consider a design ψ:U → ) and a distribution F on (cid:1) . The model
)
P :(cid:1) → P(S) associates with each point θ ∈ (cid:1) a distribution P θ on S .
) ψ U
Since F is a formal convex combination of points in (cid:1) , P F is a similar
) ψ
formal combination of points in P(S), that is, a joint distribution on (cid:1) ×S .
) U
In other words, to each model component P :(cid:1) →P(S ) there corresponds
ψ ) U
a map P :P((cid:1) )→P((cid:1) ×S ), associating with each prior distribution F
ψ ) ) U
on(cid:1) ajointdistributionP F on(cid:1) ×S byformalconvexcombinations.The
) ψ ) U
marginaldistributiononS isobtainedbyintegrationover(cid:1) ,thatis,bytreating
U )
theformallinearcombinationF asanactuallinearcombination.
Ahierarchicalmodelisachain(cid:1)1,(cid:1)2,...,(cid:1)k ofparameterfunctors,together
withachainofnaturaltransformations,
P :(cid:1)1→P((cid:1)2), P :(cid:1)2→P((cid:1)3),..., P :(cid:1)k →P(S).
1 2 k
Bythecompositionaloperationdescribedabove,wehave
(P k P k−1 ···P 1 ):(cid:1)1→P((cid:1)2×···×(cid:1)k×S).
This composite function is not a statistical model according to the definition,
but it can be converted into one by the natural transformation of integration in
which the formal linear combination P k−1 ···P 1 is interpreted as an actuallinear
combination,
(cid:1)1P−k · → ··P1P((cid:1)2×···×(cid:1)k×S)→P(S).
A Bayesian model is a hierarchical model in which k >1 and (cid:1)1 ={0} is the
trivialfunctor,aone-pointsetwithidentitymap.
4.4. Submodel. Let(cid:1),6:cat →K betwocontravariantfunctorsfromcat
) )
into the category of surjective maps. To each model P :(cid:1)→P(S) and natural
transformation h:6 → (cid:1) there corresponds a submodel Ph:6 → P(S) by
restriction of P to the image of h. These relationships are illustrated by the
commutativediagram
ψ P(S) ←
Pψ−
(cid:1) ←
h
)− 6
 (cid:9) (cid:9)) (cid:9))
   
 † ∗ (cid:5)
(ϕ d ,ϕ c )(cid:8) ϕ d  ϕ c  ϕ c 
ψ (cid:5) P(S (cid:5) ) ← P ψ− (cid:5) (cid:1) )(cid:5) ← h )− (cid:5) 6 )(cid:5) .
4.5. Subparameter. The notion that only certain functions of a parameter
“make sense,” or “have a meaning” is well understood and formalized to some
extent by dimensional analysis in physics. Thus, in an i.i.d. normal model for
the weight distribution of apples at harvest, it might make sense to compare the

WHATISASTATISTICALMODEL? 1239
subparameter σ/µ for different varieties, but the “subparameters” µ + σ2 and
µ + σ/µ are clearly meaningless. We are thus led to the concept of a natural
subparameter.
A natural subparameter is a natural transformation g:(cid:1) → 6 of functors
.Toeachdesignψ:U→)thenaturaltransformationg
oncat associatesamap
D
| g :(cid:1) →6 | insuchawaythatthediagramshownbelowcommutes |     |     |     |
| ------------- | ------------------------------------------ | --- | --- | --- |
| )             | )                                          |     |     |     |
ψ
g
|     |      | ψ             | (cid:1) −→ψ      | 6            |
| --- | ---- | ------------- | ---------------- | ------------ |
|     |      |              | (cid:9))         | (cid:9))     |
|     |      |              |                 |             |
|     |      |              | ∗               | (cid:5)     |
|     | (ϕ d | ,ϕ c )(cid:8) | ϕ               | ϕ           |
|     |      |               | c                | c            |
|     |      |               | g                | (cid:5)      |
|     |      | (cid:5)       | −→ψ              |              |
|     |      | ψ             | (cid:1) )(cid:5) | 6 )(cid:5) . |
∗=ϕ (cid:5)
| Inotherwordsg | ϕ   | g .        |     |     |
| ------------- | --- | ---------- | --- | --- |
|               | ψ c | c ψ(cid:5) |     |     |
| →             |     |            | →   |     |
Let g:(cid:1) 6 and h:(cid:1) 7 be two natural subparameters such that
(g,h):(cid:1)→6×7 isanaturalisomorphismoffunctors.Whensuchapairexists,
we say that g,h are complementary subparameters in (cid:1). In general, for a given
subparameter g there need not exist a complementary subparameter. When a
complementaryparameterexists,it neednotbe unique.Thenotion of orthogonal
parameters[CoxandReid(1987)]doesnotarisehereunlesstheparametersets(cid:1)
)
are innerproductspaces,andthe maps ϕ ∗ preserveinnerproducts.Suchfunctors
c
doariseinratherspecializedapplications.
4.6. Identifiability. The parameter (cid:1) is said to be identifiable at the design
→
ψ:U ) if distinct parameter values give rise to distinct distributions on
the sample space. In other words, (cid:1) is identifiable at ψ if the associated map
P :(cid:1) →P(S)isinjective.
ψ )
Likewise, a natural subparameter 6 is identifiable at ψ if distinct ξ-values
give rise to nonoverlapping sets of distributions. To each point ξ ∈ 6 there
)
−1ξ −1ξ
corresponds a set of points g in (cid:1) , and a set of distributions P g
|     |     |     | ψ ) | ψ ψ |
| --- | --- | --- | --- | --- |
| =   |     |     | →   |     |
in F ψ P ψ (cid:1) ) . The subparameter g(cid:1) 6 is said to be identifiable at ψ if,
(cid:5)
| foreachξ (cid:18)=ξ | in6 | ,thesets |     |     |
| ------------------- | --- | -------- | --- | --- |
)
|     |     |     | −1ξ     | −1ξ (cid:5) |
| --- | --- | --- | ------- | ----------- |
|     |     | P   | g and P | g           |
|     |     | ψ   | ψ       | ψ ψ         |
are nonempty and nonoverlapping.An identifiable subparameteris thus a surjec-
tivenaturaltransformationg:(cid:1)→6thatgeneratesapartitionofF
bynonover-
ψ
lappingsets.
4.7. Response-scalemorphisms. Inthediscussionthusfar,theresponsescale
hasbeenkeptfixed.Thatistosay,theanalysishasnotconsideredtheeffectonthe
modelofchangingtheunitsofmeasurementfrom,say,bushelsperacretotonnes
per hectare, or of aggregating selected levels of an ordinal response variable. To
(cid:5)
complete the story, it is necessaryto considerthe various morphisms γ :V →V

| 1240 |     |     | P.MCCULLAGH |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- |
of the response scale and their effect on the sample space and model. For each
responsescaleV incat ,thesamplespaceisacontravariantfunctoroncat ,and
|     |     | V   |     |     |     | U   |
| --- | --- | --- | --- | --- | --- | --- |
→V (cid:5)
| themodelisacontravariantfunctoronthedesign.Toeachmorphismγ |     |     |     |     |     | :V  |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
incatV therecorrespondsanaturaltransformationofsamplespacesasillustrated
inthecommutativediagrambelow:
−γ→
|     |     |     | V   | V (cid:5) |     |     |
| --- | --- | --- | --- | --------- | --- | --- |
γ
|     |     |          | VU − →U | (cid:5)U    |     |     |
| --- | --- | -------- | ------- | ----------- | --- | --- |
|     |     | U        |         | V           |     |     |
|     |     |         | (cid:9) | (cid:9)     |     |     |
|     |     |         |        |            |     |     |
|     |     |         | ∗      |  ∗         |     |     |
|     |     | ϕ(cid:8) | ϕ      | ϕ V(cid:5) |     |     |
V
|     |     |           | (cid:5) γ | (cid:5) (cid:5) |     |     |
| --- | --- | --------- | --------- | --------------- | --- | --- |
|     |     | U (cid:5) | VU − →U   | V (cid:5)U .    |     |     |
Thecategoryofmorphismsofsamplespaces,cat , isthe categorywhoseobjects
S
are all sample spaces S = VU with V ∈ cat and U ∈ cat . The morphisms
|         |          |              |       | V                 | U      |         |
| ------- | -------- | ------------ | ----- | ----------------- | ------ | ------- |
| (cid:5) | (cid:5)U |              | ∗     | ∗                 |        | (cid:5) |
| VU → V  | are all  | compositions | γ ϕ = | ϕ γ in which      | γ :V → | V is a  |
|         |          |              | U V   | V(cid:5) U(cid:5) |        |         |
∗
morphism of the codomain, and ϕ is a functional composition with the domain
morphism ϕ:U→U (cid:5) . In this way, the categoryof morphisms on sample spaces
is built up from a category of injective morphisms on units, and a category of
morphismsonresponsescales.
Infact,cat isisomorphicwiththeproductcategorycat ×cat op ,wherecat op is
|     | S   |     |     | V   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | U   | U   |
theoppositecategoryderivedfromcat bytheprocessofreversingallarrows.The
U
|     | op  | op  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
categories cat and cat are defined in the same way. The logical structure of a
|     | D   | )   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
statisticalmodelisthenillustratedbythefollowingfunctorsequences,whichshow
op
| thatcat andtheparameter(cid:1)arecovariantfunctorsoncat |     |             |      |             | ×cat . |     |
| ------------------------------------------------------- | --- | ----------- | ---- | ----------- | ------ | --- |
| S                                                       |     |             |      | V           | D      |     |
|                                                         |     |             | op∼  | ∼           |        |     |
|                                                         |     | ×cat op→cat | ×cat | =cat =P(S), |        |     |
|                                                         | cat | V           | V    | S           |        |     |
|                                                         |     | D           | U    |             |        |     |
op→(cid:1)
| (2) | cat     | ×cat op→cat    | ×cat | K.  |     |     |
| --- | ------- | -------------- | ---- | --- | --- | --- |
|     |         | V D            | V )  |     |     |     |
|     | Model:P | :(cid:1)→P(S). |      |     |     |     |
Thefunctorcat →P(S)isanisomorphism,associatingwitheachsamplespace
S
S = VU the set of all probability distributions on S, and with each morphism
| →S  | (cid:5) |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
f :S ofsamplespacesamorphismon distributions definedbycomposition
with the inverse image of f. A model is a natural transformation P :(cid:1)→P(S)
associatingwitheachpair(V,ψ:U→))amapP :(cid:1)→P(VU)satisfyingthe
ψ
propertiesin(1).
In the absence of covariate effects, the commutative diagram of a statistical
model takes the following simplified form in which the model P :(cid:1) → P(S)
(cid:5)
is indexed by sample spaces S,S ,.... First, the parameter space ((cid:1),†) is a
covariant functor on the category cat , associating with each response scale V,
V
(cid:5)
a parameter set (cid:1) , and with each morphism γ :V →V a parameter morphism
V

WHATISASTATISTICALMODEL? 1241
γ†:(cid:1)
V
→(cid:1) V(cid:5). Second, to each morphism of sample spaces γϕ ∗ :VU (cid:5) →VU,
thetransformationonthemodelisdescribedbythecommutativediagram,
S (cid:5)=V
(cid:9)
(cid:5)U P(
(cid:9)
S (cid:5) ) ← P S− (cid:5) (cid:1) (cid:9)V(cid:5)
  
γϕ ∗   ◦(γϕ ∗ ) −1  γ†
S=VU (cid:5) P(S) ←PS− (cid:1) .
V
To see what this means, consider a random variable Y taking values in S =VU (cid:5)
withdistributionP θ forsomeθ ∈(cid:1) .EachmorphismS→S (cid:5) isthecomposition
S V
∗
ofacoordinateprojectionmapϕ andaresponse-scalemorphismγ.Themarginal
distribution of Y is (P θ)◦(γϕ
∗
)
−1
on S
(cid:5)
. Commutativity ensures that this
S
distribution is also equal to the image under P S(cid:5) of the induced parameter γ†θ.
Inotherwords,P :(cid:1)→P(S)isanaturaltransformationoffunctors.
5. Special cases. The statement in equations (1) and (2), that a statistical
model is a natural transformation P :(cid:1) → P(S) of functors, is a consistency
condition ensuring that different ways of computing the probability of equivalent
events give the same answer. As a consequence,equivalent events determine the
samelikelihood.Somefamiliarinstancesareasfollows.
Equivariance and transformation models. Let C = G be a group acting on
the response scale V. The group induces a homomorphic action S → S on
the sample space, usually by componentwise transformation. Likewise, the same
group inducesa homomorphicaction (cid:1)→(cid:1) on the parameterspace.The group
actions on S and on (cid:1) are conventionally denoted by the same symbol y (cid:17)→gy
andθ (cid:17)→gθ, respectively.Ordinarily,thisabuseofnotationleadstonoconfusion
because the functors G → S and G → (cid:1) are usually group isomorphisms. The
group transformation formulation is an assertion that the event-parameter pairs
(E;θ) and (gE;gθ) are equivalent. The commutativity condition may then be
written in the form P(E;θ)=P(gE;gθ). Examples include the Cauchy model,
location-scalemodels,andtheBox–Coxmodel(Section7).
A natural, or equivariant, subparameter [Lehmann and Casella (1998),
page 160], or a permissible subparameter [Helland (1999a,b)] is a function
h:(cid:1)→6 such that h(θ )=h(θ ) implies h(gθ )=h(gθ ) for each g∈G. Pro-
1 2 1 2
vided that h is surjective, this condition ensures that hgh
−1:6→6
is well de-
fined,andisagrouphomomorphism.Theterm“invariantlyestimableparameter”
hasbeenusedbyHoraandBuehler(1966),butthisterminologyisdoublymislead-
ing.First,anaturalparameterisequivariantandnotordinarilyinvariantunderthe
group,thatis, hgh
−1
neednotbetheidentity on6.Second,estimability depends
on the design, and a natural parameter need not be estimable or even identifiable
atagivendesign.

| 1242 |     |     | P.MCCULLAGH |     |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- | --- |
Insertion maps and Kolmogorov consistency. Let cat be the category of
U
insertion maps on finite sets, V =R a fixed set, cat ={0} a one-point set, and
)
=RU
let S be the standard contravariant representation. Then (cid:1) is necessarily
a set with one object and identity map. For each finite set U = {i ,...,i } ⊂
|     |     |     |     |     |     |     | 1 m |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)={1,...,n}theinsertionmapϕ:U→U (cid:5) carrieseachi∈Utoitself(ϕi=i)
U
(cid:5)
as an element in (cid:5) . The pullback map ϕ ∗ :RU →RU is a linear coordinate-
U
projection map that deletes all coordinates except those in U. For simplicity of
|                      |     | =r,sothatUconsistsofthefirstmelementsofU |     |     |     |     | (cid:5) |
| -------------------- | --- | ---------------------------------------- | --- | --- | --- | --- | ------- |
| notation,assumethati |     | r                                        |     |     |     |     | .The    |
implication of using insertion maps is that the event E =A ×···×A ⊂RU
|     |     |     |     |     |     | 1   | m   |
| --- | --- | --- | --- | --- | --- | --- | --- |
andtheevent
|     | (cid:5)=ϕ | ∗−1E=A |        |             |     | (cid:5) |     |
| --- | --------- | ------ | ------ | ----------- | --- | ------- | --- |
|     | E         |        | ×···×A | ×R×···×R⊂RU |     |         |     |
|     |           |        | 1      | m           |     |         |     |
are equivalent. The natural transformation P :(cid:1) → P(R)) in equation (1)
|            |           |           |         | ∈                     |     |              | (·;θ) |
| ---------- | --------- | --------- | ------- | --------------------- | --- | ------------ | ----- |
| associates | with each | parameter | point θ | (cid:1) a probability |     | distribution | P U   |
on RU in such a way that these equivalent events have the same probability
| (E;θ) | =   | (cid:5);θ). |     |     |     |     |     |
| ----- | --- | ----------- | --- | --- | --- | --- | --- |
P P U(cid:5)(E Commutativity is equivalent to the statement that the
U
Kolmogorov existence condition for a stochastic process [Billingsley (1986),
equation(36.3)],issatisfiedateachparameterpoint.
Interference and insertion maps. Let cat be the category of insertion maps
U
on finite sets, V =R a fixed set, and let S =RU be the standard contravariant
|                 |     | U={1,...,m}, | (cid:5) | ={1,...,n} |     | :U→U    | (cid:5) |
| --------------- | --- | ------------ | ------- | ---------- | --- | ------- | ------- |
| representation. | Let |              | U       |            | and | let ϕ d | be the  |
(cid:5)
insertionmap,implyingm≤n.Consideramorphismofdesignsψ (cid:17)→ψ inwhich
| :)→) |     |     |     |     |     | (cid:5) |     |
| ---- | --- | --- | --- | --- | --- | ------- | --- |
ϕ is the identity. In other words, ψ is obtained from ψ by ignoring, or
c
forgetting,theunits{m+1,...,n}.Thecommutativityconditioninequation(1)is
(cid:5)
simplythestatementthat,foreachθ ∈(cid:1) , theeventsE andE asdefinedabove
)
|     |     |     | (E;θ)= | (cid:5);θ). |     |     |     |
| --- | --- | --- | ------ | ----------- | --- | --- | --- |
have the same probability P ψ P ψ(cid:5)(E This is a stronger condition
than Kolmogorov consistency because the design ψ (cid:5) carries information on the
associationofcovariates,orassignmentoftreatments,to allunitsincludingthose
unobserved units {m + 1,...,n} for which the event E (cid:5) does not determine a
value. In the literature on experimental design, this assumption is called lack of
interference[Cox(1958),Section2.4;Rubin(1986)].
If cat includesinsertionmaps,ϕ :)→) (cid:5) neednotbetheidentitymap.The
| )   |     |     | c           |     |            |     |     |
| --- | --- | --- | ----------- | --- | ---------- | --- | --- |
|     |     |     | (E;ϕ ∗ θ)=P |     | (cid:5);θ) |     |     |
commutativity condition (1) P ψ(cid:5)(E implies not only that lack
|                                   |     |     | ψ c        |                                   |     |     |         |
| --------------------------------- | --- | --- | ---------- | --------------------------------- | --- | --- | ------- |
|                                   |     |     |            | →P(RU),butalsothat,for)(cid:18)=) |     |     | (cid:5) |
| ofinterferenceholdsforeachfamilyP |     |     | ψ :(cid:1) | )                                 |     |     |         |
the distributions in eachfamily are related in a naturalway. Foreach θ (cid:5) suchthat
| ∗ (cid:5)=θ,P | (E;θ)=P |            | (cid:5);θ (cid:5) |     |     |     |     |
| ------------- | ------- | ---------- | ----------------- | --- | --- | --- | --- |
| ϕ θ           |         | ψ(cid:5)(E | ).                |     |     |     |     |
| c             | ψ       |            |                   |     |     |     |     |
Exchangeabilityandinjectionmaps. Letcat =Ibethecategoryofinjective
U
|     |     | =Rafixedset,cat |     | ={0}aone-pointset,andletS=RU |     |     |     |
| --- | --- | --------------- | --- | ---------------------------- | --- | --- | --- |
mapsonfinitesets,V
)
bethe standardcontravariantrepresentation.Then(cid:1) is necessarilya setwith one
(cid:5)
object and identity map. To each injective map ϕ:U → U in I, the standard

|     | WHATISASTATISTICALMODEL? |     |     |     | 1243 |
| --- | ------------------------ | --- | --- | --- | ---- |
∗ :RU (cid:5) →RU
(contravariant)representationassociatesthesurjectivelinearmapϕ
|     |     | ∗   |     | (cid:5) |     |
| --- | --- | --- | --- | ------- | --- |
byfunctionalcomposition:(ϕ f)(i)=f(ϕ(i))fori∈U.ForU=U ,thelinear
| ∗   |     |     | ∗   |     |     |
| --- | --- | --- | --- | --- | --- |
mapϕ permutescoordinates:moregenerally,ϕ isacoordinate-projectionmap.
∈(cid:1)
The commutativity condition in (1) is the statement that, to each θ there
correspondsadistribution P θ onRU thatsatisfiesthefollowingconditions.
U
| Foreachpermutationϕ:U→U,thecoordinate-permutationmapϕ |     |     |     | ∗ :RU→ |     |
| ----------------------------------------------------- | --- | --- | --- | ------ | --- |
1.
RU carries P θ to itself. In other words, P θ is invariant under coordinate
|     | U   |     | U   |     |     |
| --- | --- | --- | --- | --- | --- |
permutation.
| Foreachinjectionϕ:U→U   |     | (cid:5)                       |         | ∗ :RU (cid:5) →RU |     |
| ----------------------- | --- | ----------------------------- | ------- | ----------------- | --- |
| 2.                      |     | ,thecoordinate-projectionmapϕ |         |                   |     |
| carriesthedistributionP |     | U(cid:5)θ onRU (cid:5) toP    | θ onRU. |                   |     |
U
|     |     | ∈(cid:1) |     | {P  | θ}  |
| --- | --- | -------- | --- | --- | --- |
In other words, to each point θ there corresponds a sequence that
U
is the distribution of an infinitely exchangeable sequence of random variables in
the sense of de Finetti [(1975), Section 11.4]. The set Inv (RU) of all natural
I
transformations{0}→P(RU)isthesetofallinfinitelyexchangeableprobability
modelsonthestandardrepresentation.
| Partial exchangeability |     | and I2.       |             |             |     |
| ----------------------- | --- | ------------- | ----------- | ----------- | --- |
|                         |     | The preceding | example may | be modified | by  |
restricting the objects and maps in cat . Let cat be the product category I2
|     |     | U   | U   |     |     |
| --- | --- | --- | --- | --- | --- |
U×W
in which the objects are all Cartesian product sets and the morphisms
| U×W →U (cid:5)×W | (cid:5) |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
areall injectivemapspreservingtheproductstructure.Each
|                           |     |              | (cid:5)   |       | (cid:5) |
| ------------------------- | --- | ------------ | --------- | ----- | ------- |
| morphismisanorderedpair(ϕ |     | ,ϕ )inwhichϕ | :U→U andϕ | :W →W | are     |
|                           |     | 1 2          | 1         | 2     |         |
injectivemapsactingcomponentwise.ThestandardrepresentationofI2associates
|                   | U×W |                  | = RU×W, |          |      |
| ----------------- | --- | ---------------- | ------- | -------- | ---- |
| with each product | set | the vector space | S UW    | and with | each |
(cid:5)×W (cid:5)
injectivemorphism(ϕ ,ϕ ),asurjectivelinearmap(ϕ ,ϕ ) ∗ :RU →RU×W
|     | 1 2 |     | 1 2 |     |     |
| --- | --- | --- | --- | --- | --- |
byfunctionalcomposition,
(cid:11) (cid:12)
∗ f(i,j)=f
|               | (ϕ 1    | ,ϕ 2 ) | ϕ 1 (i),ϕ 2 (j) |     |     |
| ------------- | ------- | ------ | --------------- | --- | --- |
| ∈RU (cid:5)×W | (cid:5) |        |                 |     |     |
for f . For simplicity, assume that (cid:1) is a set containing one element.
The commutativity condition in (1) is the statement that, to each rectangular
{1,...,m}×{1,...,n}
| indexarray |     | there correspondsa | distribution | P on | Rmn |
| ---------- | --- | ------------------ | ------------ | ---- | --- |
mn
|     | (cid:5) ≥ | (cid:5) ≥ |     |     |     |
| --- | --------- | --------- | --- | --- | --- |
such that, for m m and n n, P mn is the marginal distribution of P m(cid:5)n(cid:5)
under all coordinate-projection maps (ϕ ,ϕ ) ∗ in the standard representation. In
1 2
particular, P is invariant under row permutation and column permutation. In
mn
otherwords,P isthedistributionofaninfinitepartiallyexchangeablearrayinthe
sense of Aldous (1981). Conversely,each infinite partially exchangeablearray of
randomvariableshasadistributionthatcorrespondstoanI2-invariantdistribution.
A model is thus a set of such distributions indexed by (cid:1). The set Inv I2 (S) of
all I2-natural transformations {0}→P(S) is the set of all invariant probability
modelsonthestandardI2-representation.

| 1244 |     | P.MCCULLAGH |     |     |     |
| ---- | --- | ----------- | --- | --- | --- |
Acompletelyrandomizeddesign. Consideradesigninwhichcat =Iimply-
U
ing that the units are infinitely exchangeable.We assume also that cat includes
)
allinsertionmaps.Inalinearorgeneralizedlinearmodel,(cid:1)isarepresentationof
cat by surjective linear transformations. For generalized linear models with un-
)
=R⊕R),
knowndispersion,themostcommonchoiceistherepresentation(cid:1)
)
orthesubrepresentationR⊕1implyingequaltreatmenteffects.Dependingonthe
choice of P :(cid:1)→P(S), the representation (cid:1) may serveas an index set for var-
∼N(θ ,θ2),
| ious families, | typically | with independentcomponents,such |     | as Y |     |
| -------------- | --------- | ------------------------------- | --- | ---- | --- |
i ψ(i) 0
| Y ∼Cauchy(θ | ,|θ  | |),Y ∼Po(exp(θ | )),Y | ∼Bi(1,1/(1+exp(−θ | )))in |
| ----------- | ---- | -------------- | ---- | ----------------- | ----- |
| i           | ψ(i) | 0 i            | ψ(i) | i                 | ψ(i)  |
which ψ(i) is the treatment associated with unit i. In addition to the two com-
|     |     | ∈   | ∈ R), |     |     |
| --- | --- | --- | ----- | --- | --- |
ponent parameters θ 0 R and θ the only natural linear subparameter
g:(cid:1)→6 is the quotient projection R) →R)/1, corresponding to the space
oftreatmentcontrasts[McCullagh(1999)].
Block designs. Let cat =ND be the category in which each object U is
U
|     |     |     |     | (cid:5) | (cid:5) |
| --- | --- | --- | --- | ------- | ------- |
a set together with the equivalence relation, u ∼u if units u and u belong to
ϕ:U→U (cid:5)
the same block. The morphisms are all injective maps that preserve
|     |     |     | (cid:5) |     | (cid:5) (cid:5) |
| --- | --- | --- | ------- | --- | --------------- |
the equivalence relationship: u ∼ u in U if and only if ϕu ∼ ϕu in U . To
say the same thing in a slightly different way, each object in ND is a set of
plots together with a map b:plots → blocks. If b is surjective, we may write
(cid:5)
U={(i,b(i)):i ∈plots}.Themorphismsϕ:b→b areallorderedpairs(ϕ ,ϕ )
d b
ofinjectivemapssuchthatthefollowingdiagramcommutes:
−→b
|     |     | plots    | blocks      |          |     |
| --- | --- | -------- | ----------- | -------- | --- |
|     |     |         |             |         |     |
|     |     |         |             |         |     |
|     |     |         |             |         |     |
|     |     | ϕ        | ϕ           |          |     |
|     |     | d(cid:8) |             | b(cid:8) |     |
|     |     | (cid:5)  | −b→ (cid:5) | (cid:5)  |     |
|     |     | plots    | blocks      | .        |     |
Letcat ={0}beaone-pointset,sothat(cid:1)isalsoaset.Accordingto(1),amodel
)
for a block design with no specific factors is a natural transformation P :(cid:1) →
P(S)inwhichSistherepresentationRU,meaningreal-valuedfunctionsonplots.
| Inotherwords,eachPθ |     | isadistributioninInv |     | (RU). |     |
| ------------------- | --- | -------------------- | --- | ----- | --- |
ND
|      | ,{ε },{η }beindependentstandardnormalrandomvariables.LetY |     |     |     |      |
| ---- | --------------------------------------------------------- | --- | --- | --- | ---- |
| Letε |                                                           |     |     |     | bean |
| 0    | i b                                                       |     |     |     |      |
infinitesequenceofrandomvariablesindexedbytheobjectsUsuchthat,forsome
measurable function g:R3 →R, Y has the same distribution as X on RU,
|     |     |     | U   |     | U   |
| --- | --- | --- | --- | --- | --- |
where
|     |     | X (i)=g(ε | ,ε ,η | )    |     |
| --- | --- | --------- | ----- | ---- | --- |
|     |     | U         | 0 i   | b(i) |     |
for i ∈ U. Then Y has a distribution in Inv (S). The usual normal-theory
ND
variance-components model is obtained if g is a linear combination of ε and
i
η . Thus, we may have (cid:1)=R3, and Pθ equal to the distribution of Y, where
b(i)
| Y =θ +θ | ε +θ  | η .  |     |     |     |
| ------- | ----- | ---- | --- | --- | --- |
| i 0     | 1 i 2 | b(i) |     |     |     |

WHATISASTATISTICALMODEL? 1245
Causality and nonspecificeffects. Although the same category of morphisms
arises in these last two examples, the standard models are quite different. If the
unitsareregardedashavingtheinfinitelyexchangeableblockstructureassociated
with ND, we arrive at a random-effects model. If the units are regarded as
infinitely exchangeable modulo specific covariate effects, the model contains
specificparametersforthoseeffects.Nonspecificfactorssuchasblocks,temporal
structureandspatialstructure,forwhichnolevel-specificinferenceisrequired,are
bestregardedasapropertydefiningthestructureoftheunits.Specificfactorssuch
astreatment,variety,age,race,sexorreligion,forwhichlevel-specificinferences
may be required, must be regarded as objects in cat . Level-specificeffects may
)
be ascribed to specific factors, whether intrinsic or not, but causal effects are
not ordinarily ascribed to intrinsic factors [Holland (1986); Cox (1986)]. Thus,
longevitymay varywith race,sexandreligion, in a specificmanner, butit would
be at best an abuse of language to assert that race, sex or religion is a cause of
longevity.
The definitions given in Section 4 deliberately avoid all reference to causal
mechanisms, which are necessarily context dependent in ways that categories
and morphisms are not. A given model such as quasi-symmetry, arising in very
different fields of application from linkage disequilibrium in genetics to citation
studiesinscience,maybecapableofnumerousmechanisticinterpretations.Also,
models exist for which no mechanististic interpretation is readily available, or
which are in conflict with accepted scientific laws. Such alternative models are
necessaryinorderthatscientificlawsmaybetested.
6. Examples.
6.1. Location-scale models. For simplicity of exposition in this section, we
consideronlymodelsforindependentandidenticallydistributedscalarresponses.
Such models are determined by their one-dimensional marginal distributions on
theresponsescale,sowemayignore cat andcat .Themotivationforlocation-
U )
scale models comes from transformations of the response scale, that is, the
morphisms in cat . For definiteness, take cat to be the category of morphisms
V V
◦
of temperature scales. The objects in this category are all temperature scales, F,
◦ ◦
C, K, and possibly others not yet invented. Associated with each scale V is a
(cid:5)
certain set of real numbers, and to each pair (V,V ) of scales there corresponds
asingleinvertible affinemap (a,b):V →V (cid:5) , whichtransforms y onthe V-scale
into a +by on the V (cid:5) -scale. If V =◦ C and V (cid:5) =◦ F, the map (32,9/5) carries y
in ◦ Cto32+9y/5in ◦ F.
One example of a functor is the map T :cat →GA(R) in which each object
V
in cat is associatedwith R, andeachmap (a,b):V →V (cid:5) is associatedwith an
V
affinetransformation(a,b)†:R→Rdefinedbyx(cid:17)→a+bx.Ifcat containsthe
V
threeobjects ◦ C, ◦ Fand ◦ K,andninemaps,theimagemapsR→RinT cat are
V
the identity, the affine maps (32,9/5), (273,1), (523.4,9/5) and their inverses,

| 1246 |     |     | P.MCCULLAGH |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- |
making a total of seven maps. These are not closed under composition, so the
image T cat is not a category. However, if all conceivable scales are included
V
incat ,theimageofT isequaltotheaffinesubgroupwithb>0actingonR.
V
→GA(R2)
Another example of a functor is the map (cid:1):cat in which each
V
| (a,b):V→V | (cid:5) isassociatedwiththeaffinemapR2→R2 |           |                    |     |     | definedby |
| --------- | ----------------------------------------- | --------- | ------------------ | --- | --- | --------- |
|           |                                           | (a,b)†:(θ | ,θ )(cid:17)→(a+bθ |     | ,bθ | ),        |
|           |                                           |           | 1 2                |     | 1 2 |           |
and we may take (cid:1) as the parameter space for a location-scale model. Two
examplesofmodels(cid:1)→P(VU)withindependentcomponentsare
|     | (θ ,θ | )(cid:17)→N(θ ,θ2) | and | (θ ,θ | )(cid:17)→Cauchy(θ | +iθ ). |
| --- | ----- | ------------------ | --- | ----- | ------------------ | ------ |
|     | 1 2   | 1 2                |     | 1 2   |                    | 1 2    |
Since the points (θ ,±θ ) give rise to the same distribution, the parameter
1 2
× +
is not identifiable. Provided that b > 0, the subobject R R determines a
≥0generatesthesamefamily.Thesemodels
| subfunctor,andthesubmodelwithθ |     |     | 2   |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- |
are equivalent to the usual group formulation by affine transformations acting
componentwise on RU only if cat contains all scales, that is, all pairs (a,b)
V
withb>0.Otherwise,theimageof(cid:1)isnotagroup.
To each affine transformation (a,b) of response scales, there corresponds a
transformation (a,b)†:R2 → R2 on the object in (cid:1). The first component of
this transformation θ (cid:17)→ a + bθ does not depend on θ , so the coordinate
|     |     | 1   | 1   |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- |
(cid:17)→
projection (θ ,θ ) θ is a natural transformation. The mean or median is a
|     | 1 2 | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
natural subparameter. The same is true for the second component, so θ (cid:17)→θ is
2
alsoa naturalsubparameter.Howeverthe coefficientofvariation τ =θ /θ isnot
1 2
)(cid:17)→θ
anaturalsubparameterbecausethetransformation (θ ,θ /θ isnotnatural
|     |     |     |     |     | 1   | 2 2 1 |
| --- | --- | --- | --- | --- | --- | ----- |
for the category of location-scale transformations. The location-scale morphism
(a,b)carriesτ =θ /θ to|b|θ /(a+bθ ),whichcannotbeexpressedasafunction
|     |     | 1 2 2 |     | 1   |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
of(τ,a,b)alone.Ontheotherhand,forthesubcategory(0,b)ofcomponentwise
nonzeroscalarmultiplication,thecoefficientofvariationisanaturalsubparameter.
| Theinducedtransformationisτ |     |     | (cid:17)→sign(b)τ. |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- |
Theanalysisforotherlocation-scalefamilies followsthesamelines.Consider,
| forexample,thelocation-scalet |     |               | family, |       |           |          |
| ----------------------------- | --- | ------------- | ------- | ----- | --------- | -------- |
|                               |     | (cid:13)      |         |       |           | (cid:14) |
|                               |     | = (µ,σ2):µ∈R, |         | σ2≥0, | ν=1,2,... |          |
|                               | F   | t             |         |       |           |          |
ν
withintegerdegreesoffreedom.Thenν isinvariantunderallmapsinthecategory,
and the induced transformations for (µ,σ2) are those described above. Relative
to the category of location-scale and coordinate-projection maps, µ and σ2 are
|     |     |     |     |     | =   | +   |
| --- | --- | --- | --- | --- | --- | --- |
natural subparameters, but combinations such as τ σ/µ or µ σ are not.
Howeverµ+σ and eachpercentile is a naturalsubparameterrelative to the sub-
categoryinwhichb≥0.

|     |     | WHATISASTATISTICALMODEL? |     |     |     |     | 1247 |
| --- | --- | ------------------------ | --- | --- | --- | --- | ---- |
6.2. Regressionandcorrelation. TheissueinExercise10concernstheeffect
on the parameter θ =(α,β,σ), and on the correlation coefficient of selection of
experimentalunits.Thecorrelationcoefficient
βσ
ψ
ρ= (cid:15)
(σ2+β2σ2)
ψ
depends on the design through the design variance σ2. To show that the map
ψ
| (α,β,σ)(cid:17)→ρ |     |             |               |     | =1   |               |             |
| ----------------- | --- | ----------- | ------------- | --- | ---- | ------------- | ----------- |
|                   | is  | notnatural, | observethatif |     | ϕ in | the diagramin | Section4.5, |
c
the induced maps ϕ ∗ ,ϕ (cid:5) are both identities. In other words, for any design
|     |     | c   | c   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
morphism (ϕ ,1), the induced parameter map is the identity and gθ is invariant
d
σ2
under these maps. But is not invariant under selection of units, so ρ is not a
ψ
naturaltransformation.
Anyinferentialstatementconcerningρ mustnecessarilybeinterpretedrelative
to a suitable model and category for which ρ is a natural transformation of
functors.Onewaytoachievethisistoregardthepair(y,x)asabivariateresponse
)={0}
on the units. Then and there is only one design. Let cat be the group
V
|                  |     |        |                  |     | R2 → R2. |          | (cid:5) = + |
| ---------------- | --- | ------ | ---------------- | --- | -------- | -------- | ----------- |
| of componentwise |     | affine | transformations, |     |          | We write | y a by,     |
(cid:5)=c+dx
x inwhichbd (cid:18)=0.Theinducedmorphismontheparameterspaceis
|     | α (cid:5)=a+bα−bcβ/d; |     |     |     | β (cid:5)=bβ/d; | σ (cid:5)=|b|σ; |     |
| --- | --------------------- | --- | --- | --- | --------------- | --------------- | --- |
so(cid:1)isafunctororgrouphomomorphismR3→R3.Inaddition,thescalarmul-
tiplesign(bd),actingasamap[−1,1]→[−1,1],isalsoagrouphomomorphism.
(cid:5)=sign(bd)ρ,thecorrelationcoefficientisanaturalsubparameter.Within
Sinceρ
| thelimitationsofthissubcategory,inferenceforρ |     |     |     |     | maybesensible. |     |     |
| --------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- |
6.3. Splines and curve estimation. Let the objects in cat be all bounded
)
|     |     |     |     | )→) | (cid:5) |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
intervals of R, and let the morphisms be all invertible affine maps.This
is a subcategory of the category of injective maps on subsets of R because each
object in cat is a bounded interval, and each map is invertible (injective and
)
|     |     | (k) |     |     |     | +4  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
surjective). Let H be the vector space, of dimension 2k of cubic splines
)
on)=(a,b)withk knotsandk+1intervalsofequallength.Foreachinvertible
| affinemapϕ:)→) |     | (cid:5)          |                 |                                  | (k)                       |     | ∗ =f     |
| -------------- | --- | ---------------- | --------------- | -------------------------------- | ------------------------- | --- | -------- |
|                |     | andf             | acubicsplineinH |                                  | )(cid:5) ,thecompositionϕ |     | f ◦ϕ     |
|                |     | (k) .ThusH(k)={H |                 | (k)}isacontravariantfunctoroncat |                           |     |          |
| isavectorinH   |     |                  |                 |                                  |                           |     | .        |
|                |     | )                |                 | )                                |                           |     | )        |
|                |     | (k)              |                 |                                  |                           | ∗   | (k ) (k) |
Since the objects H are vector spaces and the maps ϕ :H →H are
|     |     | )   |     |     |     |     | ) (cid:5) ) |
| --- | --- | --- | --- | --- | --- | --- | ----------- |
linear, H(k) is a representation of cat , a finite-dimensional subrepresentation
)
{R)}.
in the standard representation Note that the subrepresentations of this
categoryin{R)}areverydifferentfromthesubrepresentationsoftheaffinegroup
GA(R)in thestandardrepresentationbyreal-valuedfunctionsonR. Eachfinite-
dimensional subrepresentation of the affine group in RR is a vector space of
nonhomogeneouspolynomialsonR.

1248 P.MCCULLAGH
ThelinearmodelinwhichtheresponseY satisfies
E(Y|x)=µ(x); cov(Y|x)=σ2I
n
for some µ∈H (k) satisfies the conditions for a statistical model. The parameter
)
functoris(cid:1)=H(k)×R + .
The preceding category includes only invertible affine maps, and the models
are notclosedunderrestriction to subintervalsofthe x-scale.Ifit is requiredthat
themodelalsobeclosedunderrestriction,wemayconstructastatisticalmodelas
follows.Letcat bethecategoryinwhicheachobject)isanintervalofthereal
)
line, including infinite intervals if so desired. The morphisms are all affine maps,
(k)
not necessarily invertible. Let H be the set of functions on ) such that each
)
f ∈H (k) is a cubic spline with k or fewer knots, not necessarily equally spaced.
)
This setis nota vectorspacebecauseit is notclosedunderaddition offunctions.
But,foreachf ∈H
)
(k
(cid:5)
) ,and)⊂) (cid:5) ,therestrictionoff to)isafunctionintheset
H (k) .Moreover,foreachinjectivemapϕ:)→) (cid:5) ,thepullbackmapϕ ∗ f =f ◦ϕ
)
satisfiesϕ
∗
H
(k)=H (k)
,soϕ
∗
issurjective.Withthismodification,theconditions
)(cid:5) )
forastatisticalmodelrelativetotheextendedcategoryaresatisfied.
6.4. Contingency-table models. In Exercise 12, the model AB +BC invites
the conclusion that variables A and C are conditionally independent given B.
This unqualified conclusion does not stand up to scrutiny because it is not
invariant under aggregation of levels of B as the context appears to demand.
The statement cannot be true at every level of aggregation unless either A is
independent of (B,C) or C is independent of (A,B), and the data indicate that
neitherofthesemodelsfits.Thestatedconclusion,thatAandC areconditionally
independentgiventhatB isrecordedataparticularlevelofaggregation,evidently
accords preferential status to a particular response scale. In practice, although
considerable aggregation may have occurred, the nature of such aggregation
is seldom arbitrary. For convenience of tabulation, aggregation tends to occur
over levels that are sparse or levels that are considered to be homogeneous.
Thus, despite the preferential status accorded to the aggregated levels of B,
the conditional independence conclusion may be defensible. The point of this
discussion is that the bald statement of conditional independence is not an
automaticconsequenceofthefittedmodel.
From the viewpoint of categories and functors, to each response scale with
unstructuredlevelsitisnaturaltoassociatethecategorySurjofsurjectivemapson
finite nonemptysets, or atleast a suitable subcategoryof certain surjectivemaps.
Sincetherearethreeresponsefactors,cat =Surj3,theparameter(cid:1)isacovariant
V
functor on Surj3, and P(cid:1) is a class of distributions that is closed undermarginal
transformations.Amonglog-linearmodels,the onlyfamilies havingthis property
arethoseassociatedwiththemodelformulas
A+B+C, AB+C, AC+B, A+BC, ABC,

WHATISASTATISTICALMODEL? 1249
inwhicheachletteroccursexactlyonce.NoformulationsuchasAB+BC whose
interpretation necessarilyaccordspreferential status to the recorded levelscan be
astatisticalmodelinthesenseofbeingacovariantfunctoronSurj3.
If in fact, some or all factors have ordered levels, we may restrict Surj to the
subcategory Surj of weakly monotone surjective maps. The set of models is
ord
thereby greatly increased. In the bivariate case, the set of distributions having
constantglobalcross-ratio[Pearson(1913);Plackett(1965);Dale(1984)]isclosed
undermonotonemarginaltransformation.Thesetsofdistributionshavingadditive
orlog-additiveglobalcross-ratiosarelikewiseclosed.
The importance of the distinction between response and explanatory factor
is evident in the functor sequence (2). Suppose that A is the response and
B,C are explanatory, all having unordered levels. It may then be appropriate
to choose cat = Surj for surjective morphisms on the levels of A, and
V
cat =I2 for selection of the levels of B and C. Then (cid:1) is a covariant functor
)
onSurj×Iop×Iop.Amonglog-linearformulations,eachfactorialexpressionthat
includes A+BC represents a model in the sense of (2). For two-way tables, the
set of nonnegative matrices of rank ≤ k is a functor corresponding to a model
notof thelog-linear type.If thelevelsof A are orderedand attention is restricted
to order-preserving surjective maps, further models are available in the form of
cumulative logit and related formulations [McCullagh (1980)]. Apart from the
rank 2 canonical correlation models, none of the association models described
by Goodman (1979, 1981) for two-way tables with ordered levels is a covariant
functor on either Surj2 or Surj ×I op . Goodman’s association structure is not
ord ord ord
preserved under aggregation of adjacent response levels. In the absence of an
extensionto other levelsof aggregation,all conclusionsderivedfrom fitting such
models are necessarilyspecificto the particular levelof aggregationobserved,so
thescopeforinferenceisrathernarrow.
6.5. Embeddabilityandstochasticprocesses. ThepointofExercise11isthat
such a specification need not define a process that extends beyond the observed
lattice. Let the observed 3 × 3 lattice be embedded as the central square of a
larger n × n lattice. The distribution of the response on the sublattice may be
computedfromthen2-dimensionalnormaldistributionwithzeromeanandinverse
variance matrix (I − B )T(I − B ) by integrating out the n2 − 9 unwanted
n n n n
variables. The matrices I and B are of order n2 × n2. But the result of this
n n
computation is different for each n, and is not equal to the normal distribution
with inverse covariancematrix (I −B )T(I −B ). In other words, Exercise11
3 3 3 3
does not identify an embeddable process. Similar issues arise in connection with
edge effects in Gibbs models for finite lattice systems:for details, see Besag and
Higdon[(1999),Section2.3.1].

1250 P.MCCULLAGH
6.6. Commentsonselectedexercises. Withtheusualunderstandingofwhatis
meantby natural embedding,the formulations in Exercises1–5 do not determine
a unique probability distribution or likelihood function. In Exercise 1, which
asks for predictions for a future subject, the observed event is either E ⊂ Rn
or the equivalent set E (cid:5) = E × R ⊂ Rn+1. The likelihood function may thus
legitimately be calculated either by P n (E;θ) or by P n+1 (E (cid:5);θ). The absurdity
ofExercise1liesinthefactthattheseexpressionsarenotequal.Totheextentthat
thisembeddingisnatural,thelikelihoodfunctionisnotwelldefined.Thenatureof
theembeddingsmaybedifferent,butthesameobjectionappliestoExercises1–5
and 11. Although the set P(cid:1) in Exercise 4 is the set of all i.i.d. normal models,
theparameterizationisunnaturalandthelikelihoodfunctionisnotwelldefined.
ThelogicalcontradictioninthetypeIIImodelinExercise5isexactlythesame
asinExercises1and2,buttheformulationislessflagrantandconsequentlymore
persistent. Let F be the family of normal distributions on Rkb with constant
kb
varianceσ2>0,suchthatµliesinthelinearsubspaceIII .Itisunderstoodthat
kb
thesamplespacemorphismsincludethecoordinateprojectionmapRkb+k →Rkb
inwhichoneentireblockisdeletedorignored.Itiseasytoseethatthefixed-sum
constraintisnotsatisfiedbytheblocksthatremain.Inotherwords,thesequenceof
vectorspaces{III }isnotclosedundersuchmaps,andconsequentlythesequence
kb
F ={F } of families is not closedeither. Put more bluntly, the observation y ⊂
kb
Rkb is equivalent to the incomplete observation y (cid:5) = y ×Rk ⊂ Rk(b+1) taken
from a larger design in which one entire block is unobserved.But the likelihood
function based on (y,F ) is not equivalent to the likelihood function based
kb
(cid:5)
on (y ,F k(b+1) ). Given this embedding, no unique likelihood can be associated
withthetypeIIImodel.
Gibbsian models have the property that the conditional distribution of certain
subsets of the variables given the values of all other variables is also of the
same type. This property makes it straightforward to construct families that are
closed under conditioning. Exercise 7 illustrates a familiar problem in the use of
quadratic exponential families and Gibbs models. Although the normal family is
closedundercoordinateprojection,theimpliedparameterization,inwhich(θ ,θ )
1 2
does not depend on cluster size, does not yield a commutative model diagram.
In other words, if (Y ,...,Y ) have the exchangeable normal distribution with
1 k
parameter(θ 1 ,θ 2 ),themarginaldistributionof(Y 1 ,...,Y k−1 )isexchangeableand
normal,buttheparameterisnotθ.Bycontrast,theconventionalparameterization
by variance and nonnegative covariance independent of cluster size, does yield
a commutative model diagram. Even though the two formulations may coincide
whenappliedto anexamplein whichthe clustersizeis constant,their extensions
tovariable-sizedclustersaredifferent,andthisdifferenceiscriticalforprediction
and inference. The version in which the variance and covarianceare nonnegative
and independent of cluster size is a statistical model. The version described in
Exercise7isnot.

|     |     | WHATISASTATISTICALMODEL? |     |     |     |     |     | 1251 |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | ---- |
TheproblemwiththeCauchymodelisthat,althoughthefamilyisclosedunder
the group of real fractional linear transformations, the projection (θ ,θ )(cid:17)→θ is
|     |     |     |     |     |     |     | 1 2 | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
notanaturaltransformation.Sincethecomponentsareindependent,itissufficient
| totakeS=R | andϕy=(ay+b)/(cy+d)inthediagrambelow: |         |     |         |     |        |                    |     |
| --------- | ------------------------------------- | ------- | --- | ------- | --- | ------ | ------------------ | --- |
|           | y                                     | C(θ)    | ←−  | θ       | −→  | g(θ)=θ |                    |     |
|           |                                      |        |     |        |     |        |  1                |     |
|           |                                      |        |     |        |     |        |                   |     |
|           |                                      | ϕ†     |     | ∗      |     |        |                   |     |
|           | ϕ                                     |         |     | ϕ       |     |        | (cid:8)ϕ (cid:5)=? |     |
|           | (cid:8)                               | (cid:8) |     | (cid:8) |     |        |                    |     |
ay+b
|     |      | C(ψ) | ←−  | ψ = aθ+b | −→  | g(ψ)=ψ |     |     |
| --- | ---- | ---- | --- | -------- | --- | ------ | --- | --- |
|     | cy+d |      |     | cθ+d     |     |        | 1   |     |
In fact, ψ = (cid:22)((aθ + b)/(cθ + d)) depends on θ and is not expressible as
|     | 1   |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
a function of (θ ,ϕ) alone. The real part is not a natural parameter relative to
1
the group of fractional linear transformations. It appears that the only natural
transformationsaretheidentityon(cid:1)andtheconstantfunction(cid:1)→{0}.
Ineachparticularapplication,itisessentialtoestablishthecategoryofrelevant
morphismsofsamplespacesattheoutset.Eventhoughtheobservationsaremod-
elled by Cauchy distributions, it is perfectly acceptable, and frequently entirely
reasonable,tochoosethefamilyoflocation-scaleandcoordinateprojectionmaps.
Unlesstheresponseisanovertratioofoutcomes,fractionallineartransformations
are seldom appealing in applied work, and they should be excluded on that ba-
sis. The category of morphisms on sample spacesmust not be determined by the
chosenfamily of distributions, but by the context. The mere fact that the Cauchy
family happens to be closed under reciprocals does not mean that the category
mustincludereciprocals.
The implicit category of morphisms in Exercise 9 is generated by affine
transformationsoftemperature,togetherwithscalarandrotationaltransformations
of physical space. When the temperature scale is morphed from Fahrenheit to
Celsius,thereisacorrespondingmorph,
|     |     |                   | (cid:11)            |     |     | (cid:12) |     |     |
| --- | --- | ----------------- | ------------------- | --- | --- | -------- | --- | --- |
|     |     | (µ,σ2,λ)(cid:17)→ | 5(µ−32)/9,(5σ/9)2,λ |     |     |          |     |     |
of the parameter space. But there exists no corresponding morph for θ =µ/σ
1
| =µ/λ,orforanyothernonsensicalcombinationsuchasσ |     |     |     |     |     |     | +λ. |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
orθ 2
7. TheBox–Coxmodel.
7.1. Natural subparameter. It is sufficient in what follows to consider the
simplified Box–Cox model in which the observationsy 1 ,...,y n are independent
andidenticallydistributed.Thesamplespacesareallfinite-dimensionalrealvector
| spaces{Rn:n≥0}. |     | Form≥n, |               |     | Rm→Rn |                      |     |     |
| --------------- | --- | ------- | ------------- | --- | ----- | -------------------- | --- | --- |
|                 |     |         | the morphisms |     |       | includeallcoordinate |     |     |
permutation and coordinate projection maps. In addition, all scalar multiples
| (cid:17)→γy |          |                       |     |                      |     |     | (cid:17)→±|y|λ |     |
| ----------- | -------- | --------------------- | --- | -------------------- | --- | --- | -------------- | --- |
| y           | for γ >0 | and all componentwise |     | powertransformations |     |     | y              | for |
λ(cid:18)=0, are also included in C. The inferential difficulties that arise in the Box–
Coxmodelaredueprincipallytotheinteractionbetweenthepowertransformation

| 1252 |     | P.MCCULLAGH |     |     |     |
| ---- | --- | ----------- | --- | --- | --- |
and the multiplicative scalar maps rather than coordinate projection maps. In the
discussion of sample-spacemorphisms, therefore, we restrict our attention to the
powertransformationandscalarmultiplicationmaps.
Since the observations are independentand identically distributed by assump-
Rn
tion, the family of distributions on is determined by the one-dimensional
|                  | N(β,σ2,λ) |                     |           |           | Y ∼ |
| ---------------- | --------- | ------------------- | --------- | --------- | --- |
| marginal family. | Let       | be the distribution | on R such | that when |     |
N(β,σ2,λ), then Yλ ∼ N(β,σ2). Minor complications associated with nega-
Yλ |Y|λsign(Y).
tive values may be handled by interpreting as It follows that
Yα ∼ N(β,σ2,λ/α) for α (cid:18)= 0. In addition, for each scalar γ > 0, γY ∼
N(γλβ,γ2λσ2,λ).
Theparameteris(β,σ2,λ),andtheparametersetis(cid:1)=R×R +×{R\0}.To
∗
eachscalarmultipleγ >0theassociatedparametermapγ :(cid:1)→(cid:1)isthegroup
homomorphism,
∗ :(β,σ2,λ)(cid:17)→(γλβ,γ2λσ2,λ).
γ
(cid:17)→yα
For each power transformation map y on the sample space, the parameter
| ∗ :λ(cid:17)→λ/α, |      | σ2                |             |               |     |
| ----------------- | ---- | ----------------- | ----------- | ------------- | --- |
| map is α          | with | β and unaffected. | The Box–Cox | model is thus | a   |
parameterizedstatisticalmodelaccordingtoourdefinition.
The fundamental difficulty, clearly evident in the discussion [Box and Cox
(1982)] is that the coordinate projection (β,σ2,λ)(cid:17)→β is not a natural transfor-
:R→R
mationoffunctors.Theproblemisevidentfromthediagraminwhichγ
isapositivescalarmultiple:
|     | R       | (β,σ2,λ)      | −→ β                 |     |     |
| --- | ------- | ------------- | -------------------- | --- | --- |
|     |        |              |                     |     |     |
|     |        |              |                     |     |     |
|     | γ      | γ ∗          |  (cid:8)γ (cid:5)=? |     |     |
|     | (cid:8) | (cid:8)       |                      |     |     |
|     | R       | (γλβ,γ2λσ2,λ) | −→ γλβ               |     |     |
(cid:5)
Commutativity requires the map γ acting on β ∈R, that is, the pair (γ,β), to
|     | γλβ, |     |     | σ2  |     |
| --- | ---- | --- | --- | --- | --- |
deliver the value an impossible task. Consequently, neither β nor nor
(β,σ2)isanaturalparameter.Someexamplesofnaturalparametersinclude
|     | λ, β/σ, | β1/λ, (β,λ) | and (σ2,λ). |     |     |
| --- | ------- | ----------- | ----------- | --- | --- |
Thefactthatβ isnotanaturalparameteraccordingtoourdefinitionisanimplicit
statementthatinferenceforβ ismeaninglessinthissystem,thatis,relativetothe
givencategoryofmorphisms,powertransformationsandpositivescalarmultiples.
One objection to the preceding analysis runs as follows: “The data Y were
,σ2,λ
generated according to a particular distribution N(β ), and I want to
|     |     |     | 0 0 | 0   |     |
| --- | --- | --- | --- | --- | --- |
know the true value β .” The difficulty here is that the equivalent data 2Y were
0
generatedaccordingto thedistribution N(2λ0β ,22λ0σ 2,λ ).Butthereis noway
|     |     |     | 0 0 0 |     |     |
| --- | --- | --- | ----- | --- | --- |
2λβ.
to transform the true value of β into the true value of Evidently, the phrase
“the true value of β” is meaningless within the context of the group of scalar
multiplesactingonthesamplespace.

WHATISASTATISTICALMODEL? 1253
7.2. The modified power transformation. The problem of parameter inter-
pretability is greatly reduced, though not entirely eliminated, by considering the
modified power transformation Rn →Rn in which y(α) is a vector with compo-
nents
y
(α)=yα/y˙α−1,
i i
where y˙ is the geometric mean of {y ,...,y } [Hinkley and Runger (1984)].
1 n
The first algebraic obstacle is that, for cat =I, the transformation y (cid:17)→y(α) is
U
not a natural transformation Rn →Rn on the standard representation. Although
the geometric mean is invariant under permutation of units, it is not invariant
under coordinate projection maps. The geometric mean of a proper subset of
{y ,...,y }isnotthesameasthegeometricmeanofallnvalues.Inotherwords,
1 n
modified Box–Cox transformation followed by coordinate projection is not the
same as coordinate projection followed by modified Box–Cox transformation.
Suchdifferencesmay,however,besufficientlysmalltobeoverlookedinpractice.
In the following analysis, the category is reduced by restriction to a single
object, a particular set of n units and the associated sample space, S = Rn.
The morphisms are coordinate permutation, modified power transformation, and
positive scalar multiplication, each of which commutes with the modified power
transformation. The modified transformation is natural relative to the restricted
category.LetN (β,σ2,λ)bethedistributiononRn suchthatifY ∼N (β,σ2,λ)
n n
then Y(λ)∼N (β,σ2,1), with independentnormal components.This family is a
n
functor on the restricted category: for multiplicative scalar morphisms Y (cid:17)→γY,
theassociatedparametermorphismis
γ ∗ :(β,σ2,λ)(cid:17)→(γβ,γ2σ2,λ).
For modified power morphisms Y (cid:17)→ Y(α) on the sample space, the parameter
morphism is λ(cid:17)→λ/α with (β,σ2) fixed. In both cases, the transformation acts
componentwise.
Thus, relative to this restricted and artificial category, the modified Box–Cox
family is a parameterized statistical model in which each component is a natural
subparameter.Itshouldcomeasnosurprisethatβ/λisnotanaturalsubparameter.
8. Extensiveresponsevariable.
8.1. Spatialaggregationandmeasureprocesses. LetD beafixeddomainin
the plane. An algebra A={A ,...} is a collection of subsets of D, containing
1
theempty setandclosedunderfinite setunionsandsetdifferences.A measure Y
onAisanadditivesetfunctiontakingthevaluezeroontheemptysetandadditive
fordisjointsets.IfA,B areelementsofA,thenA∪B,A\B andA∩B arealso
inA,and
Y(A∪B)+Y(A∩B)=Y(A)+Y(B).

| 1254 |     |     | P.MCCULLAGH |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- |
The yield of crop in a field trial is an additiveset function. Typically, the process
isdefinedonBorelsets,andobservedonthealgebrageneratedbytheplots.
In the discussion that follows, it is assumed that the process Y takes values in
a set V that includes zero and is closed under addition (an additive semigroup).
In practice,this usuallymeansthat V is thesetofnonnegativeintegers,thesetof
nonnegativereals,thesetofrealorcomplexnumbers,ortheCartesianproductof
suchsets.
Let C be the category in which each object A is a finite algebra of Borel-
(cid:5)
measurable subsets of D, and each morphism ϕ:A → A is the insertion map
| inwhichA⊂A | (cid:5)                                   |     |     |     |                |     |
| ---------- | ----------------------------------------- | --- | --- | --- | -------------- | --- |
|            | .ThesamplespaceisacontravariantfunctoronC |     |     |     | thatassociates |     |
with each algebra A the set meas (A) of V-valued additive set functions
V
|           |           |           | →       | (cid:5)   | ∗       | (cid:5) → |
| --------- | --------- | --------- | ------- | --------- | ------- | --------- |
| on A, and | with each | insertion | map ϕ:A | A the map | ϕ :meas | (A )      |
V
meas (A) by restriction to A ⊂ A (cid:5) . A probability model P for the process
V
is a contravariant functor on C that associates with each A a probability
⊂
distribution P A on meas V (A) in such a way that, when S meas V (A) is
|     |     |     | ∗−1S | (cid:5) |     |     |
| --- | --- | --- | ---- | ------- | --- | --- |
P -measurable, the inverse image ϕ ⊂meas (A ) is P A(cid:5)-measurable, and
| A     |                      |         |                              | V          |     |           |
| ----- | -------------------- | ------- | ---------------------------- | ---------- | --- | --------- |
| (S)=P | ∗−1S).Inotherwords,P |         |                              |            |     |           |
| P     | A(cid:5)(ϕ           |         | isthemarginaldistributionofP |            |     | A(cid:5), |
| A     |                      |         | A                            |            |     |           |
|       |                      | A       | meas (A)                     | P          |     |           |
|       |                      |        | (cid:9)V                     | (cid:9)A   |     |           |
|       |                      |        |                             |           |     |           |
|       |                      | ϕ      | ϕ ∗                         |  ◦ϕ ∗−1  |     |           |
|       |                      | (cid:8) |                             |            |     |           |
|       |                      | (cid:5) | (cid:5)                      |            |     |           |
|       |                      | A       | meas (A)                     | P A(cid:5) | .   |           |
V
This is a category-style statement of the Kolmogorov consistency condition that
mustbesatisfiedbythefinite-dimensionaldistributionsofameasureprocessonD
[Kingman (1984)]. The term “process” refers both to the random variable Y and
| totheprobabilitymodelP |     | onD | satisfyingtheprecedingconditions. |     |     |     |
| ---------------------- | --- | --- | --------------------------------- | --- | --- | --- |
A point process is a process for which each outcome is a countable set of
points in D. In other words, a point process is a nonnegative integer-valued
random measure such that, with probability 1, Y has countable support and no
multiple points. Then Y(A) is the number of points in A. A Poisson process
[Kingman (1993)] is a point process in which, for some weakly finite nonatomic
measure µ on D, (a) Y(A) has the Poisson distribution with mean µ(A); (b) for
nonoverlapping sets A ,A ,..., the random variables Y(A ),Y(A ),... are
|     |     | 1 2 |     |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- |
independent.Aprocesssatisfyingcondition(2)issaidtobecompletelyrandom.
A measure process is called Gaussian if, for each finite collection of subsets
{A ,...,A },therandomvariable(Y(A ),...,Y(A ))isnormallydistributed.
| 1   | n   |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
8.2. Domainmorphisms. Weconsiderfirstsomeoftheissuesconnectedwith
statisticalmodelsforprocessesin whichcovariateeffectsdonotarise. Ordinarily
we require a family that is extendable to a large class of subsets of the plane.
(cid:5)
Accordingly, we begin with a category cat in which the objects D,D ,... are
D
someorallsuchsubsetsoftheplane.Theclassofmorphismsϕ:D →D (cid:5) depends
on the context, but is restricted to injective maps that preserve Borel sets. In

|     |     |     | WHATISASTATISTICALMODEL? |     |     |     |     | 1255 |
| --- | --- | --- | ------------------------ | --- | --- | --- | --- | ---- |
practice, the morphisms are usually translations, rotations and scalar multiples
(cid:5)
thatpreservesomeaspectofEuclideanstructure.Everyinjectivemapϕ:D →D
⊂D, ϕ(A∪B)=ϕ(A)
| preserves | Boolean | structure | in  | the sense that, | for A,B |     |     |     |
| --------- | ------- | --------- | --- | --------------- | ------- | --- | --- | --- |
∪ϕ(B), and ϕ(A ∩B) = ϕ(A)∩ϕ(B). Thus, ϕ carries each algebra of Borel
(cid:5)
| subsetsofD | intoanalgebraofBorelsubsetsofD |     |     |     |     | .   |     |     |
| ---------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Inthediagrambelow,toeachdomainD therecorrespondsasamplespace,S ,
D
∈
of V-valued measures on (the Borel subsets of) D. For each point Y S D(cid:5),
|             |     | (cid:5) ∗ | Y)(A)=Y(ϕA)isthecompositionmeasureonD. |     |     |     |     |     |
| ----------- | --- | --------- | -------------------------------------- | --- | --- | --- | --- | --- |
| ameasureonD |     | ,(ϕ       |                                        |     |     |     |     |     |
←PD−
|     |     | D        | Y◦ϕ     | S          | P(S )         |                | 6          |     |
| --- | --- | -------- | ------- | ---------- | ------------- | -------------- | ---------- | --- |
|     |     |         | (cid:9) | (cid:9)D   | (cid:9)D      |                | (cid:9)D   |     |
|     |     |         |        |           |              |                |           |     |
|     |     |         |        |  ∗        |              |                |  (cid:5)  |     |
| (3) |     | (cid:8)ϕ |        | ϕ         | ϕ†           |                | ϕ         |     |
|     |     | (cid:5)  |         |            |               | ← P D− (cid:5) |            |     |
|     |     | D        | Y       | S D(cid:5) | P(S D(cid:5)) |                | 6 D(cid:5) | .   |
ϕ†
The map on probability models is defined by composition with the inverse
| imageofϕ | ∗ ,thatis,(ϕ†F)(S)=F(ϕ |     |     | ∗−1S)forS⊂S |     | andF | ∈P(S | D(cid:5)). |
| -------- | ---------------------- | --- | --- | ----------- | --- | ---- | ---- | ---------- |
D
Typically,theprocessY tobestudiedismodelledasameasureonD,assigning
valuesto eachofthe Borelsets. Although we refer to the sample spaceas the set
of measures on D it is important to understand that Y is ordinarily not observed
ontheBorelsets,butonthefinitesubalgebrageneratedbytheplots.
An invariant probability model is a natural transformation {0} → P(S) that
associates with each object D a process, P on meas(D), in such a way that,
D
for each domain morphism ϕ:D →D (cid:5) , the sample-space map ϕ ∗ :S →S
D(cid:5) D
|     | =   |     | ∗−1. |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
satisfies P P D(cid:5)◦ϕ For example, the Poisson process with constant unit
D
intensityfunctionisinvariantundertranslationandrotationofdomains.Formany
categories of domain morphisms, however, invariant processes do not exist. For
example, there exists no nontrivial process that is invariant under translation and
scalar multiplication. However, the family of Poisson processes with constant
intensityfunctionis closedundersimilarity transformations.Likewise,thefamily
of stationary Gaussian processeswith constant intensity and isotropic covariance
density
|     |     | σ2exp(−γ|x−x |     | (cid:5)|)dxdx | (cid:5) | σ2,γ | ≥0, |     |
| --- | --- | ------------ | --- | ------------- | ------- | ---- | --- | --- |
,
isalsoclosedundersimilaritytransformations.
A statistical model P :6 → P(S) is a natural transformation of functors
on cat . For example, if cat is the group of similarity transformations acting
| D   |     |     | D   |           |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- |
| R2, |     |     | =R  | + (cid:5) |     |     |     |     |
on we may take 6 D and ϕ equal to the Jacobian of ϕ. If P D ξ is the
homogeneousPoissonprocessonD withintensityξ,thediagramcommutes.
More generally, let 6 be the set of nonnegative measures on D. For each
D
ϕ:D →D (cid:5) the induced map ϕ (cid:5) on measures is given by (ϕ (cid:5) µ)(A)=µ(ϕA) for
| ∈6  |     | ⊂D. |     |     |     | (cid:5) |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
µ D(cid:5) and A If µ is nonatomic, so also is ϕ µ. The set of nonatomic
measures is thus a subfunctor of 6. If P D(cid:5)µ is the Poisson process on (cid:5) with
D
nonatomic mean measure µ, the induced process ϕ†P D(cid:5)µ on D is Poisson with

| 1256 |     |     |     |     | P.MCCULLAGH |     |     |     |     |     |
| ---- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
nonatomic mean measure ϕ (cid:5) µ, and the diagramcommutes. An arbitrary measure
µ with atomsgivesriseto aprocessin whichmultiple eventsoccurwith nonzero
probabilityatthesamepoint.AlthoughP D µisaPoissonprocess,itisnotapoint
process according to the usual definition [Kingman (1993)]. Further submodels
| existifcat |     | isrestrictedtocontinuousmaps. |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
D
8.3. Covariate effects in spatial processes. In a field trial over a domain D,
the design is a map ψ:D →), associating with each point u in the domain a
point ψu in ).In practice,sinceobservationsaremadeonplots, notpoints, ψ is
(cid:5)
constant on each plot. Each morphism ψ →ψ of designs is a pair of injective
|        |     |               |     | (cid:5) | =ϕ  |     |     |     |     |     |
| ------ | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| maps(ϕ |     | ,ϕ )suchthatψ |     | ϕ       | ψ.  |     |     |     |     |     |
|        | d   | c             |     |         | d c |     |     |     |     |     |
To constructa model for the effect of covariateson a measure-valuedprocess,
it is essential to begin with a suitable baseline family, or uniformity model, for
the processwhencovariateeffects are absent.Sucha family is necessarilyclosed
underthecategoryofmorphismsofthedomains.Inthediagramshownbelow,the
→)
parameterspaceisacontravariantfunctorassociatingwitheachdesignψ:D
|     |     |     |     | ×   |     |     |     |     | → (cid:5) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
a parameter set 6 D (cid:1) ) , and with each morphism (ϕ d ,ϕ c ):ψ ψ a map
(cid:5) (cid:5)
(ϕ ,ϕ ):6 D(cid:5) ×(cid:1) )(cid:5) →6 ×(cid:1) .Astatisticalmodelisanaturaltransformation
|     | d c |     |     | D   | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
offunctorsonthedesign.Thebaselineuniformity modelis obtainedbychoosing
(cid:1)={0}.
|     |     | Design |     |     | Samplespace |     |          | Model |            |          |
| --- | --- | ------ | --- | --- | ----------- | --- | -------- | ----- | ---------- | -------- |
|     |     | −ψ→    |     |     |             |     |          | Pψ−   |            |          |
|     |     | D      |     | )   | S =meas(D)  |     | P(S      | ) ←   | 6 ×(cid:1) |          |
|     |     |       |     |    | D (cid:9)   |     | (cid:9)D |       | (cid:9)D   | (cid:9)) |
(4)
|     |          |            |          |        |           |         |              |     |            |             |
| --- | -------- | ----------- | -------- | ------- | ---------- | ------- | ------------- | --- | ----------- | ------------ |
|     | ϕ        |            | ϕ        |        | ϕ ∗       |         | ϕ †          |     | ϕ (cid:5)  |  ϕ (cid:5) |
|     | d(cid:8) |             | c(cid:8) |         |           |         |              |     |            | c            |
|     |          |             |          |         | d          |         | d             |     | d           |              |
|     |          |             | (cid:5)  |         |            |         |               | P   | (cid:5)     |              |
|     |          | (cid:5) −ψ→ |          | (cid:5) | =meas(D    | (cid:5) |               | ←   | ψ− ×(cid:1) |              |
|     | D        |             |          | )       | S D(cid:5) | )       | P(S D(cid:5)) |     | 6 D(cid:5)  | )(cid:5)     |
|     |          |             |          |         |            |         |               |     | → (cid:5)   |              |
In order to see what this diagram means in √ practice, let ϕ:D D be a
similarity transformation with scalar multiple 2. Then the area of the image
|     |     | (cid:5) |     |     |     |     |     |     | ∗   |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ϕ D ⊂D is twice the area of D, and the mean intensity of Yϕ =ϕ Y on D
| d   |     |     |     |     |     |     |     |     | d d |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)
is twice the intensity of Y on D . Thus, in the baseline model, we may choose
| 6   | =R  | andϕ | (cid:5) =|∂ϕ | /∂u|=2asascalarmultiple. |     |         |     |     |     |     |
| --- | --- | ---- | ------------ | ------------------------ | --- | ------- | --- | --- | --- | --- |
| D   |     |      |              | d                        |     |         |     |     |     |     |
|     |     |      | d            |                          |     | (cid:5) |     |     |     |     |
Let ϕ be the identity on ), so that ϕ is the identity on (cid:1) . Suppose
|     |     | c   |         |         |     | c   |     |     | )   |     |
| --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
|     |     |     | (cid:5) | (cid:5) |     |     |     |     |     |     |
that the design ψ on D uses two varieties and that the yield for variety 2
exceeds the yield for variety 1 by one ton per acre. As observed on D, the yield
per unit area for each variety is doubled, and the difference is also doubled.
(cid:5)
For the two varieties, the processes on D are P ψ(cid:5)(ξ,θ 1 ) and P ψ(cid:5)(ξ,θ 2 ) with
intensity functions λ(ξ,θ ),λ(ξ,θ ).On D we obtain P (2ξ,θ ) and P (2ξ,θ )
|     |     |     |     | 1   | 2   |     | ψ   | 1   | ψ   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with intensity functions λ(2ξ,θ ),λ(2ξ,θ ). Commutativity requires a model
|     |     |     |     |     | 1   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameterized in such a way that the difference between the intensity functions
(cid:5)
on D is twice the difference between the intensity functions on D . So far as

WHATISASTATISTICALMODEL? 1257
expected yields are concerned, the variety effects must be multiplicative, not
additive.
Definition (4) is sufficiently flexible to accommodate interference in the form
of carry-over effects such as fertilizer seepage, or prolonged residual effects in
cross-overtrials. To do so, however,the covariatespacemustbe extendedso that
ψ associates with each unit the treatment applied to that unit and the treatments
appliedtotheneighbouringunits.Themorphismsψ →ψ (cid:5) preservedesignsinthis
extendedsense,andP mayincorporatespecificcarry-overeffects.
ψ
A model for yield in agricultural field trials that is closed under spatial
aggregation has obvious conceptual advantages. However, there are competing
issues to be considered, including model flexibility and ease of fitting. First,
uniformitytrialsseemtoindicatethatmostagriculturalprocessesarenotspatially
stationary, so a family of nonstationary baseline processes may be required. It is
not at all clear what sorts of nonstationarity should be accommodated in such a
baselinemodel.Partlyforthesereasons,themodelpresentedbyBesagandHigdon
(1999) uses a baseline family that is not closed under spatial aggregation. For
furthercommentaryonthispoint,seethediscussionbyBest,IckstadtandWolpert
(1999),Harville andZimmerman(1999)andthe reply bythe authors(page740).
The Besag–Higdon formulation is thus not a statistical model for an extensive
variable in the sense of the present paper. Algebra does not easily deal with
approximationsorinequalities,soitishardtosayinwhatsensetheBesag–Higdon
formulation might be approximately closed underspatial aggregation,rotation or
otherdomainmorphisms.
8.4. Conformal models. A conformal model is a natural transformation of
functorsinwhichcat isthecategoryofconformalmapsactingondomainsinthe
D
plane.Thecategoryofconformalmapsisanaturalchoiceforrealspatialprocesses
becauseitpreserveslocalEuclideanstructure.
A completely random process on D is characterized by its one-dimensional
distributions. Because it represents an additive set function, such a process on
Borelsets is necessarilyinfinitely divisible, so thatthe log characteristicfunction
oftheone-dimensionaldistributionshastheform
logE(eitY(A))=m(A)×logφ(t)
forsomenonnegativemeasuremonD.Afamilyofcompletelyrandomprocesses
is determined by a particular choice of characteristic function φ together with a
suitablefamilyofintensitymeasuresclosedundertherequiredcategoryofdomain
morphisms. For example, if the category includes scalar multiples, the family of
measures must be closed under scalar multiplication. Likewise, under conformal
mapping,ϕ:D →D (cid:5) ,theprocessϕ ∗ Y =YϕonD haslogcharacteristicfunction
(cid:11) (cid:12)
logE(eit(ϕ∗Y)(A))=logE(eitY(ϕA))=m
ϕA ×logφ(t)

| 1258 |     |     | P.MCCULLAGH |     |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- | --- |
forA⊂D.ThemeasuremonD (cid:5) isthustransformedtothemeasuremϕ onD by
functional composition.If m has a density dm with respectto Lebesguemeasure
| (cid:5) |     |     |     | (cid:5) |     |     |     |
| ------- | --- | --- | --- | ------- | --- | --- | --- |
onD ,theinducedmeasurehasadensityϕ dmwithrespecttoLebesguemeasure
onD givenby
(cid:5)
|     |     | ϕ dm(x)=dm(ϕx)×|∂ϕ(x)/∂x|. |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- |
As will be shown below, the family of intensity measures whose log densities
are harmonic functions is closed under conformal mapping. Thus, an infinitely
divisible distribution together with such a family of mean measures determines a
conformalfamilyofcompletelyrandomprocesses.
Some further examples of conformal models can be described in terms of
cumulantmeasures.ThefirstcumulantmeasureoftheprocessY onD isassumed
tohaveapositivedensitysuchthat
|     |     |     | (cid:11) | (cid:12) (cid:11) | (cid:12) |     |     |
| --- | --- | --- | -------- | ----------------- | -------- | --- | --- |
|     |     | E   | Y(dx)    | =exp              | λ (x)    | dx. |     |
1
Thus
(cid:16)
|     |     |     | (cid:11) (cid:12) |       | (cid:11) | (cid:12) |     |
| --- | --- | --- | ----------------- | ----- | -------- | -------- | --- |
|     |     | E   | Y(A)              | = exp | λ (x)    | dx       |     |
1
A
for A⊂D. The variance measure on D and covariance measure on D ×D are
alsoassumedtohavedensitiesexpressibleasfollows:
|     |     |     | (cid:11) | (cid:12) | (cid:11) | (cid:12) |     |
| --- | --- | --- | -------- | -------- | -------- | -------- | --- |
=exp
|     |     | var            | Y(dx)   |          | λ 2 (x)  | dx,            |           |
| --- | --- | -------------- | ------- | -------- | -------- | -------------- | --------- |
|     |     | (cid:11)       |         | (cid:12) | (cid:11) | (cid:12)       |           |
|     |     | cov Y(dx),Y(dx | (cid:5) | ) =exp   | λ (x,x   | (cid:5) ) dxdx | (cid:5) , |
11
forx (cid:18)=x (cid:5) .Thus,
|          |     | (cid:16) |          |          | (cid:16) |          |          |
| -------- | --- | -------- | -------- | -------- | -------- | -------- | -------- |
| (cid:11) |     | (cid:12) | (cid:11) | (cid:12) |          | (cid:11) | (cid:12) |
(cid:5) (cid:5)
| cov Y(A),Y(B) |     | =   | exp λ   | (x) dx+ |     | exp | λ (x,x ) dxdx .         |
| ------------- | --- | --- | ------- | ------- | --- | --- | ----------------------- |
|               |     |     |         | 2       |     |     | 11                      |
|               |     | A∩B |         |         | A×B |     |                         |
|               |     |     | (cid:5) |         |     |     | (cid:5) (cid:5) (cid:5) |
Let Y be a process on D with logarithmic intensity functions λ ,λ ,λ . Let
1 2 11
→D (cid:5)
ϕ:D beaconformaltransformation,andletYϕbethecompositionprocess
onD.Thenthefirstandsecondcumulantmeasuresofthetransformedprocessat
x inD havelogarithmicintensitiessuchthat
|     |     | (x)=λ | (cid:5) (ϕx)+logJ(x), |     |     |     |     |
| --- | --- | ----- | --------------------- | --- | --- | --- | --- |
λ 1
1
|     |     | λ (x)=λ | (cid:5) (ϕx)+logJ(x), |     |     |     |     |
| --- | --- | ------- | --------------------- | --- | --- | --- | --- |
2
2
|     |     | (cid:5)  | (cid:5) | (cid:5)          |     |     | (cid:5) |
| --- | --- | -------- | ------- | ---------------- | --- | --- | ------- |
|     | λ   | (x,x )=λ | (ϕx,ϕx  | )+logJ(x)+logJ(x |     |     | ),      |
|     |     | 11       | 11      |                  |     |     |         |
(cid:5)
where J(x)=|∂ϕ(x)/∂x| is the Jacobian of the transformation. If ϕ:D →D
|     |     | →R  |     |     |     |     | −λ  |
| --- | --- | --- | --- | --- | --- | --- | --- |
is conformal, logJ :D is harmonic. Note also that λ 2 1 is an absolute
invariant.
Let H be the vector space of harmonic functions on D. In particular, if
D
ϕ:D → (cid:5) is conformal, logJ is harmonic and thus a vector in . If the
| D   |     |                 |     |     |     |     | H D     |
| --- | --- | --------------- | --- | --- | --- | --- | ------- |
|     |     | (cid:5) (cid:5) |     |     |     |     | (cid:5) |
intensity functions λ ,λ are also in H , it is evident that λ = λ ◦ϕ and
|     |     | 1 2 |     | D   |     |     | 1 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

|     |         |     | WHATISASTATISTICALMODEL? |     |     |     |     |     | 1259 |
| --- | ------- | --- | ------------------------ | --- | --- | --- | --- | --- | ---- |
| =   | (cid:5) |     |                          |     | ∈   | ⊗2, |     |     |      |
λ 2 λ ◦ϕ are in H D(cid:5). Further, if λ 11 H the corresponding transformed
|     | 2         |     |     |     |     | D     |             |     |     |
| --- | --------- | --- | --- | --- | --- | ----- | ----------- | --- | --- |
|     | λ (cid:5) |     |     | ⊗2. |     | log|x | −x (cid:5)| |     | ⊗2  |
parameter is a vector in H D(cid:5) For example, is a vector in H D(cid:5)
|     | 11  |     |     | (cid:5) |     |     |     | (cid:5) |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------- | --- |
(excluding the diagonalset x =x in D ×D), and log|ϕ(x)−ϕ(x )| is a vector
⊗2,alsoexcludingthediagonal.
inH
D
The baseline processes considered here are those conformal processes for
which the log-transformed cumulant densities are harmonic functions. The sub-
|        |               |        |           |     |           | =−∞, |     |            | (x)= |
| ------ | ------------- | ------ | --------- | --- | --------- | ---- | --- | ---------- | ---- |
| family | of completely | random | processes |     | for which | λ    |     | and thus λ |      |
|        |               |        |           |     |           | 11   |     |            | 2    |
λ (x)+const,isofparticularinterestintheanalysisoffieldexperiments.
1
8.5. A conformal model with covariates. We consider a model in which,
conditionallyonthereal-valuedfunctionλ,themeanandvarianceoftheprocessY
| atx∈D | aremodelledasfollows: |     |          |          |          |     |          |     |     |
| ----- | --------------------- | --- | -------- | -------- | -------- | --- | -------- | --- | --- |
|       |                       |     | (cid:11) | (cid:12) | (cid:11) |     | (cid:12) |     |     |
∗
|     | µ(dx)=E |            | Y(dx)     | =             | exp λ(x)+(ψ | θ)(x) | dx, |     |     |
| --- | ------- | ---------- | --------- | ------------- | ----------- | ----- | --- | --- | --- |
|     |         |            | (cid:11)  | (cid:12)      |             |       |     |     |     |
| (5) |         |            | var Y(dx) | =σ2µ(dx),     |             |       |     |     |     |
|     |         | (cid:11)   |           | (cid:12)      |             |       |     |     |     |
|     |         | Y(dx),Y(dx |           | (cid:5) ) =0, |             |       |     |     |     |
cov
for some volatility parameter σ2 > 0. Following Besag and Higdon (1999),
we may interpret the term λ(x) as the fertility intensity at x. Although the
notation (ψ ∗ θ)(x) may appear unfamiliar, the effects of variety, treatment and
othercovariatesaremodelledintheusualmanner,thoughtheireffectsonthemean
aremultiplicative ratherthanadditive.Themultiplicativeform in (5)is necessary
to ensure that the diagram (4) is commutative for the category of conformal
transformations. It is possible but not necessary that Y should be a Gaussian
process.
Thekey issueconcernsthe assumptionsto be madeaboutfertility effects.It is
generallyunderstoodthat,forfieldexperiments,theassumptionofuniformfertility
isundulyoptimistic.Neighboringplotstendtohavesimilarfertilities,buttherecan
besubstantialfertility gradientsoverthedomainofinterest.Attheotherextreme,
if no assumptions are made about fertility patterns, that is, if λ is regarded as
RD,
an arbitrary continuous function in the variety effects are not identifiable.
One intermediate option is to assume that fertility variation can be modelled as
a quadratic function or a rational function of suitable low order. In this section,
weexploreathird option,namelyassumingthatthefertility intensityλonD lies
in the vector space of harmonic functions H . This assumption means that the
D
|     | ∈D  |     |     |     |     |     | D(x,r)⊂D |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
fertility at x is equal to the average fertility on each disk with
center x and radius r >0. The model allows considerable flexibility for fertility
gradients,butitdoesimplythatthefertilityfunctioncannothavealocalmaximum
or minimum in the interior of D. As with all such assumptionsborn of algebraic
convenience,empiricalworkisneededtoseeiftheassumptionisreasonable.The
availablenumericalevidenceislimited,butverypositive.

| 1260 |     |     |     | P.MCCULLAGH |     |     |     |     |
| ---- | --- | --- | --- | ----------- | --- | --- | --- | --- |
A harmonic function has the property that the Laplacian at x = (x ,x )
1 2
vanishes:
|     |     |     |        | ∂2λ | ∂2λ |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     | ∇λ(x)= |     | +   | =0  |     |     |
|     |     |     |        | ∂x2 | ∂x2 |     |     |     |
|     |     |     |        |     | 1   | 2   |     |     |
∈D.FormalapplicationoftheLaplacianoperatortoourmodelgives
foreachx
|     |     |     |      | dµ  | ∗    |       |     |     |
| --- | --- | --- | ---- | --- | ---- | ----- | --- | --- |
|     |     |     | ∇log |     | =∇(ψ | θ)(x) |     |     |
dx
since the Laplacian is a linear operator. Provided that the the fertility function is
sufficiently smooth to be approximated by a vector in H D , no prior distribution
is required. Even though the vector space H of fertility intensities is infinite
D
dimensional,certaintreatmentandvarietycontrastsareidentifiable.Identifiability
requiresthat∇(ψ ∗ θ)notbeidenticallyzero.Numericalcalculationshowsthat,in
manycases,allvarietycontrastsremainidentifiable.
8.6. Lattice approximation. We assume here that the response measure Y is
observed on a regular m × n grid of rectangular plots, D × D , sufficiently
x y
small that the Laplacian can be approximated at each internal plot. Let the rows
be indexed by 1 ≤ i ≤ m, and the columns by 1 ≤ j ≤ m. On the assumption
that the plot sizesare sufficientlysmall that λ is effectivelyconstanton plots, the
multiplicativemodelintheprecedingsectiongives
|     |        |     | (cid:11) | (cid:12) | (cid:11) |      | (cid:12) |     |
| --- | ------ | --- | -------- | -------- | -------- | ---- | -------- | --- |
|     | µ(A)=E |     |          | =exp     | +(ψ      | ∗    | ×|A|,    |     |
|     |        |     | Y(A)     |          | λ        | θ) A |          |     |
A
|     |     |     | (cid:11) | (cid:12) |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
=σ2µ(A)
|     |     | var | Y(A) |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
∗
in which (ψ θ) is the effect of the treatment or variety associated with plot A.
A
Reverting to more classical notation in which the plots are indexed by (i,j) ∈
m×n,wehave
|     |     | logµ | =λ  | +(Xθ) |     | +log|A | |.  |     |
| --- | --- | ---- | --- | ----- | --- | ------ | --- | --- |
|     |     |      | ij  | ij    | ij  | ij     |     |     |
In the terminology of generalized linear models [McCullagh and Nelder (1989)],
theoffsetislog|A|,thelinkfunctionislog,andthevariancefunctionisthemean.
Providedthattheplotareasareconstant,thetermlog|A|canbeabsorbedintothe
harmonicλ.
ThesimplestlatticeversionoftheLaplacianisproportionalto
| (∇Y) | =(Y i−1,j | −2Y | +Y  | i+1,j | )/D2 +(Y | i,j−1 −2Y | +Y i,j+1 | )/D2 |
| ---- | --------- | --- | --- | ----- | -------- | --------- | -------- | ---- |
| ij   |           |     | ij  |       | y        |           | ij       | x    |
for 2≤i ≤m−1 and 2≤j ≤n−1. It is absolutelyessentialto take accountof
the geometry of the plots by including the factors D and D in the definition of
|     |     |     |     |     |     | x   | y   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
theLaplacian.Iftheplotsaresquare,theLaplacianat(i,j)maybeapproximated
bythesumofthefourneighborsminusfourtimesthevalueat(i,j).

WHATISASTATISTICALMODEL? 1261
The kernel of the linear transformation ∇:Rmn → R(m−2)(n−2) is the sub-
space H of lattice harmonic functions, of dimension equal to the number of
boundaryplots.ThelinearprojectionRmn→Rmn,
H =I −∇(cid:5) (∇∇(cid:5) ) −1∇
hasthepropertythattheimageofH isthekernelof∇,whichisthesubspaceH.
The model formula is thus ker∇ + X, or H + X, with log link and variance
proportional to the mean. An approximate estimate of the variety contrasts may
beobtainedbysolving
(X
(cid:5)
WX)β
˜=X (cid:5)
W(logY),
where W =∇(cid:5) (∇∇(cid:5) ) −1∇. Since ∇ annihilatesconstantsandlinearfunctions,the
(cid:5)
matrixX WX isnotinvertible.Atbest,onlycontrastsareestimable.
In principle, the nonlinear model can be fitted by standard software such as
GLIM or the glm() function in Splus. In practice, since H is mn×mn of rank
h=2(m+n−2),itisnecessarytoeliminatetheredundantcolumns.Thiscanbe
done by using an equivalent full-rank matrix H (cid:5) =HJ in which J is mn×h of
full rank. A matrix of independent uniform random numbers is adequate for this
purpose.
The data from the wheat uniformity trial reported by Mercer and Hall (1911),
and reproduced in Andrews and Herzberg (1985), were reanalysedin the light of
theprecedingdiscussion.Thedesignisagridof20×25nearlysquareplots,each
1/500ofanacreinarea.Eachplotcontains11drillrows10.82feetlong.Fromthe
given total area, we infer that the drill rows are approximately nine inches apart
andthattheplotsizeis10.82×8.05infeet.Afterallowingformultiplicativerow
andcolumneffects,it isfoundthatthemeansquareduetoharmonicvariationsis
0.304on82degreesoffreedom,whereastheresidualmeansquareis0.107on374
degreesoffreedom.Attheexpenseofthe boundaryplots,a25%reductioninthe
varianceoftreatmentcontrastsis achievedbytheeliminationofharmonictrends.
The observedvariance ratio of 2.85 provides strong evidencefor the presence of
at least two variance components in these data, and the ratio might well have
been considerably larger had the region not been selected on the basis of its
uniform appearance. Numerically, it matters little whether the model is additive
ormultiplicative.
The real and imaginary parts of (x +ix )k are homogeneous polynomials of
1 2
degree k, both of which are harmonic functions. The set H ⊂H of harmonics
k
of degree k or less on D = R2 is a subspace of dimension 2k + 1 closed
under similarity transformations, that is, planar rotation, translation and scalar
multiplication. That is to say, H and H/H are representations of this group,
k k
and there is a corresponding invariant decomposition of the harmonic sum of
squares.In the Mercer–Hall data, low-order harmonics tend to dominate, but this
dominance is much less pronounced than I had anticipated. After allowing for

1262 P.MCCULLAGH
row and column effects, the seven unaliased harmonics of degree five or less
account for only 17% of the total harmonic sum of squares. The F-ratio of 2.19
on7, 75degreesoffreedomgivesa p-valueof4.5%.Itshouldbeborneinmind,
however,thatthisone-acreregionofthefieldwasselectedbyvisualinspectionon
accountofitsevidentuniformity.Hadtheharvestedregionbeenpredetermined,or
otherwise selected at random, large-amplitude low-order harmonic trends might
wellhavebeenmorepronounced.
Curiously, Besag [(1974), Table 16] obtains exactly the same residual mean
square using a second-order Gibbs model with a linear trend adjustment. This
coincidence can be explained in part by noting that the average of the four first-
order coefficients in the fitted Gibbs model is almost exactly 0.25, while the
second-order coefficients are very small. These values suggest nonstationarity
[Besag and Kooperberg (1995)], and are consistent with the hypothesis that the
process is white noise plus a (random) harmonic function. An intrinsic Gaussian
processwithaharmonicgeneralizedcovariancedensityoftheform−log|x−x (cid:5)|
forx(cid:18)=x (cid:5) isapossibility.Itshouldbenotedthattheorientationoftheplotsisnot
entirely clear from the description given. If the plots were in fact 8.05×10.82,
so that the total area is 201.25×216.4 rather than 161.0×270.5, the preceding
analysis would give a residual mean square of 0.114. The Gibbs model, which
ignoressuchphysicalspatialinformation,isunaffected.
8.7. Apartingproposal. Manytraditionalfieldexperimentsuseblockdesigns,
in which the model matrix X includes block effects in addition to treatment
and variety effects. Certain directional block effects and discontinuities may
be attributable to drainage, ploughing, harvesting or other field management
practices, and specific allowance for these may be required. Other artificial
block effects may also be included to compensate for natural spatial variation.
The fertility patterns modelled by block effects are constant on blocks but
discontinuous at block boundaries. The fertility patterns modelled by harmonic
functions are smooth trends having the characteristic mean-value property. In
the absence of a compelling argument for fertility discontinuities beyond those
described above, it should not be necessary to include artificial block effects in
the model in addition to harmonic variations. This line of argument leads to the
modest, but challenging, proposal to augment the theory of block designs with
a theory of efficient harmonic designs for field experiments. It is inefficient, for
example,toassignthesametreatmenttoneighboringplots.
APPENDIX
Glossaryon categories. Category theoryasks of everytype of mathematical
object: “What are the morphisms?”; it suggests that these morphisms should be
described at the same time as the objects [Mac Lane (1998)]. The morphisms

|     |     |     |     | WHATISASTATISTICALMODEL? |     |     |     |     |     | 1263 |
| --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | ---- |
determine the structure of the objects, and, in a sense, they are more important
thantheobjects.
(cid:5)
A category C is determined by the objects ),),... it contains, and the
|     |     |     |     |     | →   | (cid:5) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
morphisms, maps or arrows, ϕ:) ) between pairs of objects. The set of
|              |     |     | (cid:5)             |     |     |     | (cid:5)     | (cid:5)         |     |     |
| ------------ | --- | --- | ------------------- | --- | --- | --- | ----------- | --------------- | --- | --- |
| morphisms)→) |     |     | inCisdenotedbyC(),) |     |     |     | )orhom (),) | ).Twoconditions |     |     |
C
arerequiredinorderthatagivencollectionofobjectsandarrowsshouldconstitute
|     |     |     |     |     | ),  |     | 1:)→) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
a category. First, for each object the identity arrow is a morphism
|     |     |     |     |     |     |     | (cid:5) (cid:5) | (cid:5)(cid:5) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | --- | --- |
in C. Second,to each pair of arrows ϕ:)→) , ψ:) →) in C suchthat the
|          |     |      |         |                |     |     |                      |     | ψϕ:)→) | (cid:5)(cid:5) |
| -------- | --- | ---- | ------- | -------------- | --- | --- | -------------------- | --- | ------ | -------------- |
| domainof |     | ψ is | equalto | the codomainof |     | ϕ,  | the compositionarrow |     |        |                |
is a morphism in C(),) (cid:5)(cid:5) ). A category is thus a collection of morphisms that
containseachidentityandisclosedundercompositionofcomposablearrows.
Each set C(),)) contains the identity and is closed under composition, that
is, C(),)) is a monoid (semigroup with identity). A category with all arrows
invertible is a groupoid; a category with all arrows identities is a set, the set of
objects;acategorywithexactlyoneobjectisamonoid;acategorywithoneobject
andinvertiblearrowsisagroup.
Product category. Let C,K be two categories. The objects in the product
|          |     | ×K  |         |           |          |     | )×G      | )∈C |     | ∈K. |
| -------- | --- | --- | ------- | --------- | -------- | --- | -------- | --- | --- | --- |
| category |     | C   | are the | Cartesian | products |     | in which |     | and | G   |
Themorphisms)×G→) (cid:5)×G (cid:5) (ϕ:)→) (cid:5) ,ψ:G→G (cid:5)
|     |     |     |     |     | are | allorderedpairs |     |     |     | )   |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
ofmorphismsactingcomponentwise:(ϕ,ψ)(i,j)=(ϕi,ψj).
→
Functor. A functor T :C K is a morphism of categories, preserving
category structure (identity and composition). Since the functor acts on objects
as well as arrows, we sometimes write T =(T,∗) in which T is the object map
|     | ∗   |     |     |     |     |     |     |     | T)=T |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
and is the arrow map. The object map carries ) to the object in K.
)
ϕ:)→) (cid:5)
In a covariant functor, the arrow map carries the arrow to the arrow
∗
ϕ :T →T in K. Two conditions are required. First, the identity 1:)→)
|                              | )   | )(cid:5) |        |     |                |                       |     |     |           |                |
| ---------------------------- | --- | -------- | ------ | --- | -------------- | --------------------- | --- | --- | --------- | -------------- |
|                              |     |          |        |     | →T             |                       |     |     | (cid:5)→) | (cid:5)(cid:5) |
| inCiscarriedtotheidentity1:T |     |          |        |     |                | inK.Second,foreachψ:) |     |     |           | ,the           |
|                              |     |          |        |     | )              | )                     |     |     |           |                |
|                              |     |          | ψϕ:)→) |     | (cid:5)(cid:5) |                       |     | ψ   | ∗ ϕ ∗ :T  | →T             |
composition arrow is carried to the composition ) )(cid:5)(cid:5)
inK.
|     |     |     |     |     |     |     | ϕ:)→) | (cid:5) | ∗   | →T  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- |
In a contravariantfunctor, the arrow map carries to ϕ :T )(cid:5) ,
)
reversing the sense of the arrow. Apart from this reversal, the functor preserves
category structure. First, each identity 1:)→ ) in C is carried to an identity
|              | →T  |     |                      |                                    |                  |     | ψϕ:)→) | (cid:5)(cid:5) |            |        |
| ------------ | --- | --- | -------------------- | ---------------------------------- | ---------------- | --- | ------ | -------------- | ---------- | ------ |
| 1:T          |     | in  | K. Second,the        |                                    | compositionarrow |     |        |                | is carried | to the |
|              | )   | )   |                      |                                    |                  |     |        |                |            |        |
|              |     | ∗   | ∗                    | →T                                 |                  |     |        |                |            |        |
| compositionϕ |     |     | ψ :T )(cid:5)(cid:5) | ) ,reversingtheorderofcomposition. |                  |     |        |                |            |        |
TheexampleinSection6.1showsthatthesetofarrowsintheimageofT need
notbeclosedundercomposition;thatis,TC neednotbeasubcategoryofK.
AgrouphomomorphismisafunctorinwhichC andK aregroups.Onaccount
ofisomorphism,thedistinctionbetweencovariantandcontravariantfunctorsdoes
| notarise.TheimageTC⊂K |     |     |     | isasubgroupinK. |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |

| 1264 |     |     |     | P.MCCULLAGH |     |     |     |     |     |
| ---- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Isomorphism. AnisomorphismofcategoriesisacovariantfunctorT :C→K
thatisabijectiononbothobjectsandarrows.AcontravariantfunctorT :C→K
→
that is a bijection on both objects and arrows is an opposite-isomorphism C
∼
Cop=K.
Representation. Let K be the category of linear transformations on vector
spaces. A functor T :C → K is said to be a representation of C by linear
transformations,orsimplyarepresentationofC.
The standard contravariant representation of associates with each object )
C
(cid:5)
the vectorspace R), and with eachmorphism ϕ:)→) the linear transforma-
| ∗ :R)(cid:5) |     |                           |     |     |     | ∗   |        |     |     |
| ------------ | --- | ------------------------- | --- | --- | --- | --- | ------ | --- | --- |
| tionϕ        | →R) | byfunctionalcomposition:ϕ |     |     |     | f   | =f ◦ϕ. |     |     |
Dual representation. Let K be the category of linear transformations on
vector spaces. The dual functor associates with each vector space V in K
(cid:5)
the dual vector space V of linear functionals on V. To each morphism,
or linear transformation, A:V → W in K there corresponds a dual linear
|     |     | (cid:5) (cid:5) | →V (cid:5) |     |     |     |     |     |     |
| --- | --- | --------------- | ---------- | --- | --- | --- | --- | --- | --- |
transformation A :W , also called the vector-spaceadjointtransformation.
This operation reverses the direction of each arrow, so the dual is a contravariant
(cid:5)
| functorK | →K.Inmatrixnotation,A |     |     |     | isthetransposeofA. |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
C→T
| The dual | of  | a covariant | representation |     | T :C | →   | K is | the composition |     |
| -------- | --- | ----------- | -------------- | --- | ---- | --- | ---- | --------------- | --- |
(cid:5)
| K→            |     |                                 |             | )   |          |        |         | T (cid:5) |               |
| ------------- | --- | ------------------------------- | ----------- | --- | -------- | ------ | ------- | --------- | ------------- |
| K associating |     | with                            | each object |     | the dual | vector | space,  | ,         | and with each |
|               |     | (cid:5)                         |             |     |          |        | (cid:5) | (cid:5) ) | (cid:5)       |
| morphismϕ:)→) |     | theduallineartransformation(Tϕ) |             |     |          |        |         | :T →T     | .             |
|               |     |                                 |             |     |          |        |         | )(cid:5)  | )             |
Opposites. ToeachcategoryC wemakecorrespondanabstractcategoryCop
by retaining the objects, and reversing all arrows. The functor C → Cop is
contravariant,andtheorderofcompositionisreversed.Eachcategoryofinvertible
maps (groupoid) is isomorphic with its opposite. The category obtained by
(cid:5)
replacingeachobject)ofC bythepowerset2),andeachmapϕ:)→) byits
|               |     | −1:2)(cid:5) | →2), |            |     | Cop. |       |          |           |
| ------------- | --- | ------------ | ---- | ---------- | --- | ---- | ----- | -------- | --------- |
| inverse image | ϕ   |              | is   | isomorphic |     | with | Other | concrete | instances |
of opposites include the standard representation and the dual category of linear
transformations.
Natural transformation. Let C,K be two categories, and let S,T be two
covariant functors C →K. A natural transformation g:S →T associates with
→T
eachobject ) in C an arrow g :S ) ) in sucha way that the arrow diagram
)
commutes.
g
|     |     |     | )        | S          | −→)  | T          |     |     |     |
| --- | --- | --- | -------- | ---------- | ---- | ---------- | --- | --- | --- |
|     |     |     |         | )         |      | )         |     |     |     |
|     |     |     |         |           |      |           |     |     |     |
|     |     |     |         | ∗         |      | ∗         |     |     |     |
|     |     |     | ϕ(cid:8) | ϕ          |      | ϕ          |     |     |     |
|     |     |     |          | s (cid:8)  |      | t (cid:8)  |     |     |     |
|     |     |     | (cid:5)  |            | g    | (cid:5)    |     |     |     |
|     |     |     | )        | S )(cid:5) | − →) | T )(cid:5) |     |     |     |

WHATISASTATISTICALMODEL? 1265
In other words, for each ϕ:) → ) (cid:5) in C the image arrows ϕ ∗ and ϕ ∗ satisfy
s t
ϕ
t
∗ g
)
=g
)(cid:5)
ϕ
s
∗ :S
)
→T )(cid:5).
∗ ∗
If S and T are contravariant functors, the direction of the arrows ϕ and ϕ is
s t
reversed.Thecommutativityconditionthenbecomesϕ t ∗ g )(cid:5) =g ) ϕ s ∗ :S )(cid:5) →T ) .
Acknowledgments. IamgratefultoYaliAmit,SteenAndersson,JimBerger,
Peter Bickel, David Cox, Art Dempster, Gary Glonek, Inge Helland, Saunders
MacLane,NickPolson,NancyReid,MichaelStein,StephenStigler,BurtTotaro,
ErnstWitandtherefereesforhelpfuldiscussionandcommentsonvariouspoints.
REFERENCES
ALDOUS, D. (1981). Representations for partially exchangeable arrays of random variables.
J.MultivariateAnalysis11581–598.
ANDREWS,D.F.andHERZBERG,A.(1985).Data.Springer,NewYork.
BARNDORFF-NIELSEN,O. E. and COX, D. R. (1994). InferenceandAsymptotics.Chapman and
Hall,London.
BARTLETT, M. S. (1978). Nearest neighbour models in the analysis of field experiments (with
discussion).J.Roy.Statist.Soc.Ser.B40147–174.
BERGER, J. O. (1985). Statistical Decision Theory and Bayesian Analysis, 2nd ed. Springer,
NewYork.
BERNARDO,J.M.andSMITH,A.F.M.(1994).BayesianTheory.Wiley,NewYork.
BESAG,J.(1974).Spatialinteractionandthestatisticalanalysisoflatticesystems(withdiscussion).
J.Roy.Statist.Soc.Ser.B36192–236.
BESAG, J. and HIGDON, D. (1999). Bayesian analysis of agricultural field experiments (with
discussion).J.Roy.Statist.Soc.Ser.B61691–746.
BESAG,J.andKOOPERBERG,C.(1995).Onconditionalandintrinsicautoregressions.Biometrika
82733–746.
BEST,N.G.,ICKSTADT,K.andWOLPERT,R.L.(1999).ContributiontothediscussionofBesag
(1999).J.Roy.Statist.Soc.Ser.B61728–729.
BICKEL,P.andDOKSUM,K.A.(1981).Ananalysisoftransformationsrevisited.J.Amer.Statist.
Assoc.76296–311.
BILLINGSLEY,P.(1986).ProbabilityandMeasure,2nded.Wiley,NewYork.
BOX, G. E. P. and COX, D. R. (1964). An analysis of transformations (withdiscussion). J. Roy.
Statist.Soc.Ser.B26211–252.
BOX,G.E.P.andCOX,D.R.(1982).Ananalysisoftransformationsrevisited,rebutted.J.Amer.
Statist.Assoc.77209–210.
COX,D.R.(1958).PlanningofExperiments.Wiley,NewYork.
COX,D.R.(1986).CommentonHolland(1986).J.Amer.Statist.Assoc.81963–964.
COX,D.R.andHINKLEY,D.V.(1974).TheoreticalStatistics.ChapmanandHall,London.
COX, D. R.andREID, N.(1987).Parameterorthogonalityandapproximateconditionalinference
(withdiscussion).J.Roy.Statist.Soc.Ser.B491–39.
COX,D.R.andSNELL,E.J.(1981).AppliedStatistics.ChapmanandHall,London.
COX,D.R.andWERMUTH,N.(1996).MultivariateDependencies.ChapmanandHall,London.
DALE,J.R.(1984).Localversusglobalassociationforbivariateorderedresponses.Biometrika71
507–514.
DEFINETTI,B.(1975).TheoryofProbability2.Wiley,NewYork.
GELMAN, A., CARLIN, J. B., STERN, H. and RUBIN, D. B. (1995). Bayesian Data Analysis.
ChapmanandHall,London.

1266 P.MCCULLAGH
GOODMAN, L. A. (1979). Simple models for the analysis of association in cross-classifications
havingorderedcategories.J.Amer.Statist.Assoc.74537–552.
GOODMAN, L. A. (1981). Association models and canonical correlation in the analysis of cross-
classificationshavingorderedcategories.J.Amer.Statist.Assoc.76320–334.
HAMADA, M.and WU, C. F. J.(1992).Analysisofdesignedexperimentswithcomplexaliasing.
J.Qual.Technology24130–137.
HARVILLE,D.A.andZIMMERMANN,D.L.(1999).ContributiontothediscussionofBesag(1999).
J.Roy.Statist.Soc.Ser.B61733–734.
HELLAND,I.S.(1999a).Quantummechanicsfromsymmetryandstatisticalmodelling.Internat.J.
Theoret.Phys.381851–1881.
HELLAND,I.S.(1999b).Quantumtheoryfromsymmetriesinageneralstatisticalparameterspace.
Technicalreport,Dept.Mathematics,Univ.Oslo.
HINKLEY, D. V. and RUNGER, G. (1984). The analysis of transformed data (with discussion).
J.Amer.Statist.Assoc.79302–320.
HOLLAND, P. (1986). Statisticsandcausalinference(withdiscussion). J.Amer.Statist.Assoc.81
945–970.
HORA, R. B. and BUEHLER, R. J. (1966). Fiducial theory and invariant estimation. Ann. Math.
Statist.37643–656.
KINGMAN, J. F. C. (1984). Present position and potential developments: Some personal views.
Probabilityandrandomprocesses.J.Roy.Statist.Soc.Ser.A147233–244.
KINGMAN,J.F.C.(1993).PoissonProcesses.OxfordUniv.Press.
LAURITZEN, S. (1988). Extremal Families and Systems of Sufficient Statistics. Lecture Notes in
Statist.49.Springer,NewYork.
LEHMANN,E.L.(1983).TheoryofPointEstimation.Wiley,NewYork.
LEHMANN, E. L. and CASELLA, G. (1998). Theory of Point Estimation, 2nd ed. Springer, New
York.
LITTELL,R., FREUND,R.J.andSPECTOR,P.C.(1991).SASSystemforLinearModels,3rded.
SASInstitute,Cary,NC.
MACLANE,S.(1998).CategoriesfortheWorkingMathematician,2nded.Springer,NewYork.
MCCULLAGH,P.(1980).Regressionmodelsforordinaldata(withdiscussion).J.Roy.Statist.Soc.
Ser.B42109–142.
MCCULLAGH,P.(1992).ConditionalinferenceandCauchymodels.Biometrika79247–259.
MCCULLAGH,P.(1996).MöbiustransformationandCauchyparameterestimation.Ann.Statist.24
787–808.
MCCULLAGH,P.(1999).Quotientspacesandstatisticalmodels.Canad.J.Statist.27447–456.
MCCULLAGH,P.(2000).Invarianceandfactorialmodels(withdiscussion).J.Roy.Statist.Soc.Ser.
B62209–256.
MCCULLAGH, P. and NELDER, J. A. (1989). Generalized Linear Models, 2nd ed. Chapman
andHall,London.
MCCULLAGH.P.andWIT,E.(2000).NaturaltransformationandtheBayesmap.Technicalreport.
MERCER,W.B.andHALL,A.D.(1911).Theexperimentalerroroffieldtrials.J.Agric.Research
50331–357.
NELDER, J. A. (1977). A re-formulation of linear models (with discussion). J. Roy. Statist. Soc.
Ser.A14048–77.
PEARSON,K.(1913).Noteonthesurfaceofconstantassociation.Biometrika9534–537.
PLACKETT,R.L.(1965).Aclassofbivariatedistributions.J.Amer.Statist.Assoc.60516–522.
RUBIN,D.(1978).Bayesianinferenceforcausaleffects:Theroleofrandomization.Ann.Statist.6
34–58.
RUBIN,D.(1986).CommentonHolland(1986).J.Amer.Statist.Assoc.81961–962.

WHATISASTATISTICALMODEL? 1267
SMITH, A. F. M. (1984). Present position and potential developments: some personal views.
Bayesianstatistics.J.Roy.Statist.Soc.Ser.A147245–259.
TJUR,T.(2000).ContributiontothediscussionofMcCullagh(2000).J.Roy.Statist.Soc.Ser.B62
238–239.
WHITTLE,P.(1974).ContributiontothediscussionofBesag(1974).J.Roy.Statist.Soc.Ser.B36
228.
YANDELL, B. S. (1997). Practical Data Analysis for Designed Experiments. Chapman and Hall,
London.
DEPARTMENTOFSTATISTICS
UNIVERSITYOFCHICAGO
5734UNIVERSITYAVENUE
CHICAGO,ILLINOIS60637–1514
E-MAIL:pmcc@galton.uchicago.edu
DISCUSSION
BY JULIAN BESAG 1
UniversityofWashington
Introduction. I am glad of the opportunity to discuss some aspects of Peter
McCullagh’s paper. Parametric statistical formulations have recently come under
intense attack [e.g., Breiman (2001)] but I strongly disagree with the notion
that they are no longer relevant in contemporary data analysis. On the contrary,
they are essential in a wealth of applications where one needs to compensate
for the paucity of the data. Personally, I see the various approaches to data
analysis (frequentist, Bayesian, machine learning, exploratory or whatever) as
complementarytooneanotherratherthanascompetitorsforoutrightdomination.
Unfortunately, parametric formulations become easy targets for criticism when,
as occurs rather often, they are constructed with too little thought. The lack of
demandsontheusermadebymoststatisticalpackagesdoesnothelpmattersand,
despite my enthusiasm for Markov chain Monte Carlo (MCMC) methods, their
abilitytofitverycomplicatedparametricformulationscanbeamixedblessing.So,
inthatsense,McCullagh’spaperistimelyandofcourseitmakesmanyvalidpoints
butI alsothink it is misconceived,both in its generalaimsand in the agricultural
applicationdiscussedinSection8.
Generalcomments. MyoverallimpressionofMcCullagh’sframeworkisthat
itreallyconcernsmathematicalmodels,whereasstatisticalmodelsaremoresubtle,
which makes the subject in some ways more difficult and more rewarding. That
1Supported in part by the Center for Statistics and the Social Sciences with funds from the
UniversityInitiativesFundattheUniversityofWashington.

1268 DISCUSSION
said,Ihavealwaysdislikedtheterm“statisticalmodel”becauseIthinkitaccordsa
statustoformulationsthatisseldomearnedinpractice.Inspatialstatistics,Ifailed
to persuade anyone to adopt the term “scheme” [Besag (1974)] or “prescription”
[Besag(1975)]andthesedaysoftenfallbackon“representation”(withorwithout
itsBayesianconnotations).Iprefertoreservetheterm“model”forsomethingthat
has a physical justification, such as the Poisson process in certain applications.
I doubt whether generalized linear models, for example, usually fall into this
category, any more than do spatial autoregressions.McCullagh seems to demand
the universality of a physical model, but without doing any of the physics, and
surely this is too much to ask? A statistical formulation can still be very useful
without universality, so long as one restricts inferences to what might loosely
be described as “interpolation” rather than “extrapolation.” Is this not what we
teach our students? Yet several of McCullagh’s criticisms and examples involve
“extrapolation” to parts of a space in which there is no claim that the original
formulation holds. This is different from the valid points that are made about
ensuringconsistencybetweendifferentmeasurementscales,say.
Moreover, if I were forced by law to call something a statistical model, then
Iwouldinsistthatitmustbeuseableforandassessablebydataanalysis,whereas
a McCullagh statistical model is a mathematical object involving data but not
necessarily data analysis. As a concrete example, I think McCullagh views the
formulationinSection8.6asalattice-basedapproximationtoapreviousstatistical
model,whereasIwouldinterpretitasastatisticalschememotivatedbyaprevious
(Ibelieveuntenable)mathematicalmodel.
Maybe the above point is a minor one, but it is related to another that to
me is crucial and yet seems absent from McCullagh’s framework, namely the
role of approximation. Indeed, he writes, “Algebra does not easily deal with
approximations or inequalities.” It seems to me that, except for some rather
limited randomization analyses, the initial choice of an appropriate level of
approximation is a vital ingredient in almost any statistical investigation (though
maybe requiring review in the light of the available data) and is perhaps the
most creative aspect of our subject. McCullagh seeks to produce rules within
which creativity must operate, but it is not obvious that his formalism takes us
constructively beyond sound common sense. Furthermore, it can impose quite
unreasonable constraints. Obviously, I agree that one should always recognize
andseektorectifymathematicalinconsistenciesbutnotslavishlysoifthismeans
abandoninga scientifically useful approximation in favor of a formulation that is
universallyself-consistentbutunsustainableintheregionofinterest.
Although, in principle, the purpose of an investigation should govern the
formulation and the type and the amount of data collected, practice is often
harsher and the specification one adopts depends qualitatively on the available
sample size. Fisher (1922) wrote, “More or less elaborate forms will be suitable
according to the volume of the data.” Indeed, this interdependence provides the
salvation of frequentist p-values against the argument that failure to “reject” a

WHATISASTATISTICALMODEL? 1269
model occurs merely because the sample size is too small. That is, the argument
becomesirrelevantifonerecognizesthatthegeneralityofstatisticalformulations
should normally increase with sample size, until ultimately one may indeed be
allowedtheluxuryofmachinelearning.Imayneedtoaddthatmyinterpretationof
ap-valueismerelyasanexploratorydevicethatquantifiesinconsistencybetween
the observed data and a particular formulation. McCullagh seems not to accept
that sample size should be an important ingredient in statistical modeling; see
Section 4.2. Of course, I agree that generally there should be coherence between
formulations in going from sample size n to n+1 but this process also takes us
fromnton2andthentherewilloftenbeoverridingconcernsandaneedforgreater
flexibility.
Markov random fields. Markov random fields (MRFs) are distributions
specified via their full conditionals (originally called local characteristics). The
identificationbetweenanyparticularMRFandacorrespondingGibbsdistribution
and vice versa follows from the Hammersley–Clifford theorem [e.g., Besag
(1974)]. The only restriction on either class is a minor positivity condition, so
Gibbs(say)distributionsarenotrequiredtohavethepropertyMcCullaghascribes
totheminSection6.6.
Exercise 7 is supposedly an example of the inconsistencies that plague MRFs
but seems badly chosen. I agree of course that the formulation is bizarre but,
without a context, there is no reason why the distribution of Y in a cluster of
size k, marginalized over its kth component, should be required to coincide with
thatof Y in aclusterofsizek−1.Forexample,supposethatk referstothelitter
sizes in a study of piglets and that a measurement is made on each piglet. Then
exchangeabilitywithinlittersmightbeareasonableassumptionbutmarginalizing
overapigletinalitterofsizekdoesnotproducealitterofsizek−1.Andwhatever
the formulation, it seems reckless even to contemplate drawing inferences about
littersofsizeeightfromdatamerelyonlittersofsizetwo!
A better example of the contradictions that arise in MRF formulations is
mentionedinMcCullagh’sdiscussionofExercise11.Thatis,aparametricMRFon
agrid(say)isgenerallyinconsistentwiththecorrespondingMRFonasubsetofthe
grid. In principle, consistency can be restored by conditioning on an appropriate
boundarybutthisisusuallytoowastefulinpractice.Partialfixesmaybeavailable
by using marginalizations of MRFs on Z2 or otherwise; see Besag and Kooper-
berg(1995),BesagandHigdon(1999)andRueandTjelmeland(2002).However,
spatialeffectsareoftenofsecondaryimportance,asinvarietytrials,andthemain
intention is to absorb an appropriate level of spatial variation in the formulation,
rather than produce a spatial model with scientifically interpretable parameters.
Nevertheless,McCullagh’s basic point is well taken. For example,I view the use
of MRFs in geographicalepidemiology [e.g., Besag, York and Mollié (1991)] as
mainly of exploratory value, in suggesting additional spatially related covariates
whose inclusion would ideally dispense with the need for a spatial formulation;

1270 DISCUSSION
see Byers and Besag (2000) for an example on prostate cancer and ethnicity.
A particularly blatant abuse of MRFs occurs in the analysis of social networks,
where the parameters in Markov random graphs are often ascribed substantive
interpretationsthataremeaningless,ifonlybecausetheydependonthesizeofthe
system. I anticipate that MRFs will play a diminishing role in statistical analysis
but currently they still have useful computational advantages when MCMC is
used.
Agricultural field experiments. Although field experiments no longer fea-
ture in most graduate programs, their design and analysis comprise an important
area of application for statistics. Variety trials usually involve say 25 to 75 vari-
eties of a crop, with very limited replication, perhaps three or, even worse, only
twoplotsbeingassignedtoeachvariety.HereIexcludeearlygenerationtrials,of-
tenhavingverylargenumbersofvarietiesandnoreplicationbutwith checkplots
ofastandardvarietyusedascontrols.
It has always been recognized that generally a crop will perform much more
similarly on two plots close together than on plots further apart. Thus, Fisher
[(1928), page 229] wrote, “... the peculiarity of agricultural field experiments
lies in the fact, verified in all careful uniformity trials, that the area of ground
chosen may be assumed to be markedly heterogeneous, in that its fertility varies
in a systematic, and often a complicated manner from point to point.” Soil
measurements, such as pH, are not generally available to make adjustments for
fertility. Fisher’s solution to the problem resulted in the design and analysis
of experiments, an approach that provides rigorous inference via randomization
analysisbut,formodern-dayexperiments,canbeveryinefficientwhencompared
tomodel-basedanalysis.
McCullagh refers frequently to agricultural experiments and in Section 8
proposes a spatial formulation based on harmonic functions. Despite initial
resistance, spatial methods have become increasingly popular: for example,
frequentist spatial analysis is now used in some 5000 experiments annually in
Australia alone [Gilmour, Cullis, Smith and Verbyla (1999)]. In several places,
McCullagh mentions Besag and Higdon (1999), henceforth BH, though with
no obvious enthusiasm. As background, BH describes a Bayesian approach to
statistical analysis, with some emphasis on variety trials, and examines several
complicateddatasets;easierexamplesareanalyzedinBesagandHigdon(1993),
in Besag, Green, Higdon and Mengersen[(1995), Section 5] and in the rejoinder
to discussion in BH. A first-order Gaussian intrinsic autoregression is used as
a simple but flexible baseline representation of the spatial variation in fertility.
BH does not pretend to provide a complete solution and indeed discusses some
current deficiencies. Below I will confine my comments to points raised by
McCullagh.

WHATISASTATISTICALMODEL? 1271
Responsescale(Section3.2). McCullaghmakesthebasicpointthatstatistical
analysis should not depend on responsescale. BH achievesthis by standardizing
therawdata,whichiseffectivebutratheruntidyinaBayesianframework.
Covariate space (Section 3.2). McCullagh states that, for a trial in which
fertilizer is applied at rates in the range 0–300 kg/ha, he requires the inferential
universe to extend to all nonnegative rates. Yet this seems pointless without a
corresponding extension of the model itself, even though any such extension
cannotbeassessed.Indeed,IpresumethatMcCullaghhimselfwouldbeunwilling
to draw inferences at a rate of, say, 400 kg/ha, without additional information.
Similarly, inhisexampleonpotatoes,Iwouldnotaddressvarietiesthatarenotin
the experimentor remain yet to be invented. Of course, this is not the case if the
testedvarietiesformarandomsamplefromadefinitepopulation.
Experimental units (Section 3.2). In discussing variety trials, McCullagh
claims, “It is invariably understood, though seldom stated explicitly, that the
purpose of such a trial is to draw conclusionsconcerning variety differences, not
justforplotsofthisparticularshape,sizeandorientation,butforcomparableplots
of various shapes, sizes and orientations.” Here I would replace “invariably” by
“almost never.” McCullagh seems to confuse variety trials with uniformity trials
in which a single variety is grown. Uniformity trials (e.g., the Mercer and Hall
datainSection8.6)wereusedlongagotoinvestigateoptimalplotsizeforgenuine
experiments,buttheyareperformedveryrarelynowandplotdimensionsareoften
determinedbymanagementpracticeratherthanbystatisticalcriteria.However,in
passing I note that the asymptotic logarithmic behavior of the variogram for the
BHintrinsicautoregressionisingoodagreementwiththeempiricalfindingsfrom
uniformitytrialsinFairfieldSmith(1938)andPearce(1976).
Of course, in a genuine variety trial, one might want to predict what the
aggregate yield over the entire field would have been for a few individual
varietiesbutthisdoesnotrequireanyextensionoftheformulationtoMcCullagh’s
conceptual plots. Indeed, such calculations are especially well suited to the
Bayesian paradigm, both theoretically, because one is supposed to deal with
potentially observable quantities rather than merely with parameters, and in
practice, via MCMC, because the posterior predictive distributions are available
rigorously. That is, for the aggregate yield of variety A, one uses the observed
yields on plots that were sown with A and generates a set of observations from
thelikelihoodforthosethatwerenotforeachMCMCsampleofparametervalues,
hencebuildingacorrespondingdistributionoftotalyield.Onemayalsoconstruct
credible intervalsfor the difference in total yields betweenvarieties A and B and
easilyaddressallmannerofquestionsinrankingandselectionthatsimplycannot
be considered in a frequentist framework; for example, the posterior probability
that the total yield obtained by sowing any particular variety (perhaps chosen in
the light of the experiment) would have been at least 10% greater than that of
growinganyothertestvarietyinthefield.

1272 DISCUSSION
Iamawarethatthepreviousparagraphmaybemisconstrued.DavidHigdonand
I are primarily “spatialists” rather than card-carrying Bayesians and BH merely
exploressomeconsequencesofaBayesianapproach.Thereareothercaveats.The
aboveargumentsassumethattheformulationiscorrect,thoughonecanandshould
carryoutsensitivityanalysis;alsoanymodel-basedformulationshouldleaveroom
foroutliersandotheraberrations,whichBHdiscussesviahierarchicalt’sandother
robustproceduresthatrelaxthebaselineGaussiandistributions.
Moretothepoint,neithertheagronomistswhomakerecommendationsnorthe
farmers themselvescare too much aboutthe difference in yield between varieties
AandB grownononeparticularexperimentalfield.IpresumeMcCullaghwould
includeother“similar”fieldsinhisinferentialuniverse,somethingIfeelisuseful
only if there is additional external information. Ideally, and often in practice,
severaltrialsarecarriedoutinarangeofenvironments,inwhichcaseprogresscan
be made, perhapsinvoking a hierarchicalformulation; see BH for an example on
corn(maize)grownatsix differentsitesin North Carolina. Thisalsodowngrades
the importanceof the specificassumptionsthatare madeat plot level(and atany
finer scale). If trials are not conducted at several sites, then recommendations
need to be moderated appropriately. Incidentally, the use of posterior predictive
distributions, with their additional variability, might be helpful in curbing the
frustration of plant breeders when the “best” variety experimentally does not
subsequentlyperformaswell.
Fertility (Section 8). Some care is required in what is meant by “fertility”:
both McCullagh and BH are rather vague. Fertility does not exist in abstraction,
noreveninaparticularfield,becauseitmeansdifferentthingsfordifferentcrops.
To me, “fertility” represents the plot-to-plot variation due to the environment,
if a single variety in the trial is grown throughout. This is well defined only
if one can make the usual assumption that variety effects are additive, perhaps
after a transformation of yield. My version of fertility usually includes standard
fixed effects caused by human intervention, such as those due to blocks (if these
haveaphysicalpresence)orto boustrophedonharvesting,buthereIshallassume
such fixed effects are taken into account separately. However, fertility must also
cater for all other environmental (usually thought of as random) effects and it is
generally recognized that these include indeterminate plot-aligned effects due to
managementpractice.McCullaghwrites,“Itisabsolutelyessentialtotakeaccount
of the geometry of the plots” but he ignores the influence of other effects that
destroy any assumed isotropy in the natural variation of the soil; and underlying
isotropy is itself a somewhat dubious assumption in the first place. I agree that
McCullagh’s rule would often be adequate in practice (e.g., for the Mercer and
Hall data); indeed, many trials these days use plots that are sufficiently long
and narrowfor one-dimensionalrepresentationsto suffice.However,I would still
prefer to include a parameter for directionality, as in BH, rather than rely on the
rule. This may involve a substantial computational overhead, which McCullagh

WHATISASTATISTICALMODEL? 1273
conveniently avoids, but it sacrifices negligible information even when the rule
holds. For an example where one-dimensional adjustment suffices but in the
opposite direction to that expected, see Besag and Higdon [(1993), Section 1].
McCullagh’s “absolutely essential” seems to me to indulge an inappropriate
mathematicalassumption.
Variety effects (Section 8.3). McCullagh claims, “variety effects must be
multiplicative,” as a result of certain mathematical assumptions. This would lead
metorejecttheassumptions!Varietyeffectscannotbeperfectlyadditiveonyield
itself,becauseyieldscannotbenegative,butthisisadifferentpointandisusually
irrelevantinpractice.Ofcourse,Iagreethatoneoftenneedstotransformthedata
toachieveapproximateadditivity.
Incidentally, the needto attach a prior to variety effects in a Bayesiananalysis
will be seen by many as a handicap but I think this is mistaken. Experience
suggestsclosenumericalagreementbetweenfrequentist and Bayesianresults for
corresponding spatial formulations when an approximately uniform variety prior
isadopted.However,inpractice,varietieswithinknowngroupsmaybegenetically
verysimilar,inwhichcaseitisnaturaltoadoptappropriateGaussian(orperhapst)
priors, which result in appropriate shrinkage of the estimates, particularly when
there is little replication. This would again help prevent the frustration of plant
breedersmentionedabove.
Stationarity (Section 8.3). McCullagh agrees that stationarity of the environ-
mental(random)effectsisdubious(atthescaleoftheexperiment).Myexperience
in fitting stationary lattice schemesis that typically one obtains parameter values
onthenonstationaryedgeoftheparameterspace,afindingthatisnotrestrictedto
agricultural data. Thus, following Künsch (1987), I have preferred instead to use
limitingintrinsicversions.Forexample,inonespatialdimension,afirst-ordersta-
tionaryautoregressionbecomesarandomwalk,withanarbitrarylevelratherthan
beingtieddownsomewhere.TheincrementsneednotbeGaussian.Intwodimen-
sions, a first-order Gaussian intrinsic autoregression can be interpreted in terms
of locally planar interpolation, in the same sense that a Gaussian random walk,
viewedbilaterally,islocallylinear.Againthelevelisarbitrary,inaccordancewith
adefinitionoffertility basedonvariation.Mathematically,theschemeisaninde-
pendentincrementsprocess,subjecttothelogicalconstraintthattheincrementson
anyloopsumtozero.Thismaybeausefulinterpretationindevisingnon-Gaussian
versions.BHalsodiscusseslocallyquadraticrepresentationsthatdonotattenuate
peaksandtroughsbutsuggeststhatthesemayoverfitfertility.
Spatial scale (Section 8). Scale invariance, at least to a very good approxi-
mation, is a requirement for any genuine model of “fertility” and so it is natural
to begin in continuous space, even if eventual interest is in discrete plots. How-
ever, it is less clear whether one should work in four-dimensional space–time, in

1274 DISCUSSION
three-dimensional space or merely in two dimensions. Even in two dimensions,
there has been rather limited success in devising plausible formulations that are
amenabletointegration.In geography,theissueofinvarianceis referredto asthe
modifiablearealunitproblemandhasalonghistory.Instatistics,earlyreferences
areHeine(1955),Whittle (1962)andMatérn(1986),firstpublished(remarkably)
in1960.However,itseemsextremelyunlikelythatanyformulationcanbethought
ofas anaccuratemodelfor variationin fertility withoutadditionalmeasurements
offactorsthatinfluencethegrowthoftheparticularcropunderstudy.Thesecould
be in the form of extensive soil measurements, such as pH levels, or the use of
checkplotsofastandardvariety,dispersedovertheexperimentalsite,asoccursin
single-replicateearlygenerationtrials.
Fortunately, the sole purpose of variety trials is to compare varieties, not
to assess spatial variation, which enters the formulation merely as a nuisance
factor. With the benefit of some replication, it seems reasonable to expect that
an approximate representation of “fertility” is generally adequate for statistical
analysis.AlltheinvestigationsthatIknowofsupportthisview.Suchinvestigations
usuallyinvolveuniformitydatatowhichdummyvarietyeffectsareadded,sothat
the true values are known to be zero. An early example is in Besag and Kemp-
ton (1986). The findings typically suggest that the gains from spatial analysis in
a badly designedexperimentprovideimprovementscommensuratewith standard
analysis and optimal design. This is not a reason to adopt poor designs but the
simplefactisthat,despitetheeffortsofstatisticians,manyexperimentsarecarried
outusingnothingbetterthanrandomizedcompleteblocks.
It is highly desirable that the representation of fertility is flexible but is also
parsimonious because there are many variety effects to be estimated, with very
limited replication. McCullagh’s use of discrete approximations to harmonic
functions in Section 8 fails on both counts:first, local maxima or minima cannot
exist except (artificially) at plots on the edge of the trial; second, the degrees of
freedomlostinthefitequalsthenumberofsuchplotsandisthereforesubstantial
(in fact, four less in a rectangular layout because the corner plots are ignored
throughouttheanalysis!).
Nevertheless, there is something appealing about the averaging property of
harmonic functions, if only it were a little more flexible. What is required is a
random effects (in frequentist terms) version and that is precisely the thinking
behind the use of intrinsic autoregressions in BH and elsewhere. Indeed, such
schemesfitMcCullagh’sdiscretizedharmonicfunctionsperfectly,exceptforedge
effects (because BH embeds the array in a larger one to cater for such effects),
and they also provide a good fit to more plausible fertility functions. For specific
commentsontheMercerandHalldata,seebelow.
Ofcourse,spatialscaleremainsanimportantissueforvarietytrialsandindeed
is discussed empirically in Section 2.3 and in the rejoinder of BH. For one-
dimensional adjustment, the simplest plausible continuum process is Brownian
motion with an arbitrary level, for which the necessary integrations can be

WHATISASTATISTICALMODEL? 1275
implemented rigorously in the analysis. In the example in BH, there is close
agreement between the estimates from the discrete and continuous formulations
(which are not quite consistent mathematically). In two-dimensional adjustment,
one can experiment with splitting the plots and comparing the results obtained
fromthefertility priorsatthetwoscales.ThiscanbedonerigorouslyviaMCMC
by treating the yields in each pair of half plots as unknown but summing to the
observed value. The few examples I have tried again suggest close agreement
but, of course, I would much rather see a sound mathematical justification of
approximate closure under spatial aggregation. This might be available via an
appropriateextensionofMcCullagh’sharmonicprocesses.
Mercer and Hall data (Section 8.6). McCullagh does not draw a clear
distinction between the purposes of analyzing data from uniformity trials and
from genuine variety trials. He also comments on a purely illustrative analysis
of mine from more than 25 years ago about which I wrote [Besag (1974)], “It
cannot be claimed that the present auto-normal schemes have been successful
in reflecting the overall probabilistic structure of the wheat plots process.” The
perhaps definitive discussion of the Mercer and Hall data is McBratney and
Webster (1981), which uses the original records from Rothamsted Experimental
Station to explain the characteristics noted by McCullagh, in terms of a previous
ridgeandfurrowsystem.McCullagh’sformulationincludesfixedeffectsforrows
and columns in addition to those for the harmonic approximation, so that more
than120parametersarefitted.Thistypeofapproachdoesnotseemwellsuitedto
varietytrials.TheBHformulationfitstwoparameters,oneofwhichprovidesdata-
drivendirectionalflexibility,whichMcCullaghdoesnotallow.Although,after90
years, the Mercer and Hall data are now very tired indeed and deserve a decent
burial, it might be worth noting that the basic BH fit at least retains all of the
peaksandtroughs in McBratneyandWebster’s Table1, though it is certainly not
aphysicalmodel.
Spatialdesign(Section8.7). McCullaghproposesthedevelopmentofatheory
ofefficientharmonicdesignsforagriculturalexperiments.Suchdesignswouldbe
verycloseto thosethatexistalreadyformorerelevantspatialformulations.Fora
recentreview,seeAtkinsonandBailey(2001),especiallySection10.
Conclusion. Although McCullagh’s paper makes many valuable points,
Ibelievethattheapproachistoorigidandplacesanemphasisonpuremathematics
that is inappropriate for applied statistics. The paper promotes a universality in
statistical modeling that is seldom present or necessary in practice. The role of
approximation and its interrelationship with sample size seem to be ignored. As
regards spatial statistics, the paper rediscovers old problems but does not yet
provide effective solutions. Nevertheless, I am glad to end on a positive note by
agreeing that the generalized covariance function in Section 8.6, known as the

1276 DISCUSSION
deWijsmodelingeostatisticsanddatingbacktotheearly1950s,maybeusefulin
developingmorecoherentspatialformulationsfortheanalysisofagriculturalfield
experiments.
Acknowledgments. IamgratefultoTedHardingforveryhelpfuldiscussions
on this topic and to Peter McCullagh for his patience in arguing about specific
points.
REFERENCES
ATKINSON,A. C.andBAILEY,R. A.(2001).Onehundredyearsofthedesignofexperimentson
andoffthepagesofBiometrika.Biometrika8853–97.
BESAG, J. E. (1974). Spatial interaction and the statistical analysis of lattice systems (with
discussion).J.Roy.Statist.Soc.Ser.B36192–236.
BESAG,J.E.(1975).Statisticalanalysisofnon-latticedata.TheStatistician24179–195.
BESAG, J. E., GREEN, P. J., HIGDON, D. M. and MENGERSEN, K. L. (1995). Bayesian
computationandstochasticsystems(withdiscussion).Statist.Sci.103–66.
BESAG, J. E. and HIGDON, D. M. (1993). Bayesian inference for agricultural fieldexperiments.
Bull.Internat.Statist.Inst.55121–136.
BESAG,J.E.andHIGDON,D.M.(1999).Bayesiananalysisofagriculturalfieldexperiments(with
discussion).J.Roy.Statist.Soc.Ser.B61691–746.
BESAG, J. E. and KEMPTON, R. A. (1986). Statistical analysis of field experiments using
neighbouringplots.Biometrics42231–251.
BESAG, J. E. and KOOPERBERG, C. L. (1995). On conditional and intrinsic autoregressions.
Biometrika82733–746.
BESAG, J. E., YORK, J. C. and MOLLIÉ, A. (1991). Bayesian image restoration, with two
applicationsinspatialstatistics(withdiscussion).Ann.Inst.Statist.Math.431–59.
BREIMAN,L.(2001).Statisticalmodeling:thetwocultures(withdiscussion).Statist.Sci.16199–
231.
BYERS, S. D. and BESAG, J. E. (2000). Inference on a collapsed margin in disease mapping.
StatisticsinMedicine192243–2249.
FAIRFIELD SMITH, H. (1938). An empirical law describing heterogeneity in the yields of
agriculturalcrops.J.Agric.Sci.281–23.
FISHER,R.A.(1922).Onthemathematicalfoundationsoftheoreticalstatistics.Philos.Trans.Roy.
Soc.LondonSer.A222309–368.
FISHER, R. A. (1928). Statistical Methods for Research Workers, 2nd ed. Oliver and Boyd,
Edinburgh.
GILMOUR,A.R.,CULLIS,B.R.,SMITH,A.B.andVERBYLA,A.P.(1999).Discussionofpaper
byJ.E.BesagandD.M.Higdon.J.Roy.Statist.Soc.B61731–732.
HEINE,V.(1955).Modelsfortwo-dimensionalstationarystochasticprocesses.Biometrika42170–
178.
KÜNSCH,H.R.(1987).Intrinsicautoregressionsandrelatedmodelsonthetwo-dimensionallattice.
Biometrika74517–524.
MATÉRN,B.(1986).SpatialVariation.Springer,NewYork.
MCBRATNEY,A. B.and WEBSTER,R.(1981).Detectionofridgeandfurrowpatternbyspectral
analysisofcropyield.Internat.Statist.Rev.4945–52.
PEARCE,S.C.(1976).AnexaminationofFairfieldSmith’slawofenvironmentalvariation.J.Agric.
Sci.8721–24.

WHATISASTATISTICALMODEL? 1277
RUE,H.andTJELMELAND,H.(2002).FittingGaussianMarkovrandomfieldstoGaussianfields.
Scand.J.Statist.2931–49.
WHITTLE, P. (1962). Topographic correlation, power-law covariance functions, and diffusion.
Biometrika49305–314.
DEPARTMENTOFSTATISTICS
UNIVERSITYOFWASHINGTON
BOX354322
SEATTLE,WASHINGTON98195-4322
E-MAIL:julian@stat.washington.edu
DISCUSSION
BY PETER J. BICKEL
UniversityofCalifornia,Berkeley
Peter McCullagh is to be congratulated for this formidable paper reexamining
thequestionsofwhatisastatisticalmodelandwhatisaparameterintermsofone
ofthemajormathematicaldevelopmentsofthelatetwentiethcentury,thealgebraic
theoryofcategories.
I cannot but agree with the major points that McCullagh makes in connection
withdesignedexperimentswhichareatthebaseofhisanalysis.
1. Models must be embedded in suitable structures that permit extrapolation.
A rather practical example of this issue not explicitly raised in this paper
arises in well-designed clinical trials where permutation and rank tests assure
us that any inference we make about the null hypothesis is valid without
any assumptions on the nature of the subjects. This is, however, essentially
irrelevantsinceweareinterestednotinthegrouponwhichthetrials arebeing
performed but a putative population of interest from which they were drawn.
Thatis,oneneedstotalkaboutprobabilitydistributionsreferringtopopulations
intheendratherthanexperimentalrandomization.
2. One must also consider a world of experiments in which to embed the
experiment one performs. This seems an entirely correct and novel insight.
That means one must consider collections of sets of probability distributions
withspecifiedallowablerelationsbetweenthem.
3. One must only consider parameters viewed as functions on the set of
distributions to be relevant if they map properly in terms of the relations
betweenexperiments.
Unfortunately, I find the mathematics of category theory which McCullagh,
Ithinknecessarily,hastoinvoke,entirelyunfamiliar.Since,ingeneral,Ihavebeen

1278 DISCUSSION
interested in data not from designed experiments, hopefully such mathematics is
nottoonecessary.
Having said this I would like to comment on an example discussed by
McCullagh,Box–Coxtransformations,whichDoksumandIdiscussedmanyyears
ago. As McCullagh notes, Hinkley and Runger validly criticized the analysis in
whichweconcludedthatonecouldnotactasiftheshapeparameterswereknown
in estimating regression parameters β, that is, that there was variance inflation
due to the correlation between the estimates of the shape parameter λ and the
estimate of β. Their critique was that statements about β in the absence of λ
were meaningless. McCullagh gives a formal argument in his framework why β
byitselfisnotaparameterwhenonetakesintoaccountthatparametersmustmap
appropriatelyunderthemappingsbetweenexperimentsinwhichonechangesunits
byscalarmultiplicationortakingpowers.
There are two attractive choices among the parameters he lists as allowable,
β/σ and (β,λ). The first has been considered by a number of authors, most
recentlybyChen,LockhartandStephens(2002).Onereasonforitsattractiveness
tomeisthatifoneconsidersthemorerealisticsemiparametricmodel,
(6) a(Y)=βX+ε,
whereaisanarbitrarymonotonetransformationandεhasaN(µ,σ2)distribution
thenβ/σ isidentifiableandestimableatthen
−1/2
ratewhileβ isnotidentifiable.
Bickel and Ritov (1997) discuss ways of estimating β/σ and a which is also
estimable at rate n
−1/2
optimally and suggest approaches to algorithms in their
paper.
Thechoice(β,λ)isofinteresttomebecauseitsconsiderationistheappropriate
responseto the Hinkley–Rungercritique. One needsto specifya jointconfidence
regionfor(β,λ)makingstatementssuchas“theeffectmagnitudeβ ontheλscale
isconsistentwiththedata.”
Theeffectoflackofknowledgeofλonthevarianceofβ remainsinterpretable.
It would be more attractive if McCullagh could somehow divorce the calculus
of this paper from the language of functors, morphisms and canonical diagrams
formoreanalysis-orientedstatisticianssuchasmyself.
REFERENCES
BICKEL, P. and RITOV, Y. (1997). Local asymptotic normality of ranks and covariates in the
transformationmodels.InFestschriftforLucienLeCam:ResearchPapersinProbability
andStatistics(D.Pollard,E.TorgersenandG.Yang,eds.)43–54.Springer,NewYork.
CHEN, G., LOCKHART, R. A. and STEPHENS, M. A. (2002). Box–Cox tranformations in linear
models:Largesampletheoryandtestsofnormality(withdiscussion).Canad.J.Statist.
30177–234.
DEPARTMENTOFSTATISTICS
UNIVERSITYOFCALIFORNIA
411EVANSHALL
BERKELEY,CALIFORNIA94720-3860
E-MAIL:bickel@stat.berkeley.edu

WHATISASTATISTICALMODEL? 1279
DISCUSSION
BY HANS BRØNS
UniversityofCopenhagen
PeterMcCullagh’spaperisexciting,becauseitcanbeseenasthestartofanew,
longoverduediscussionofthemathematicalfoundationofthetheoryofstatistics.
He rightly points out that only part of the thinking in theoretical statistics is
formalized mathematically and tries to extend the existing theory of statistical
modellingusingmodernabstractmathematicaltools.Thisisagreatphilosophical
challenge,butitisaformidablepedagogicaltasktocommunicatetheresultstothe
statisticians.
Thepapercontainsbeyondthe abstractdefinitionof thenewextendedconcept
ofastatisticalmodelatreasuretroveofexamplesandcounterexamples,butIshall
concentrate on an analysis of the definition of models. McCullagh’s idea is that
parameterspacesand sample spaceswhich are usually treated as sets or measure
spacesin applicationshavea richerstructure definingwhatonecouldbe tempted
to calltheir “physicalnature,”which shouldbe reflectedin the models andin the
choice of transformations between them. This is done by giving them an inner
structure, symmetry for example, and by considering each model as a unit in a
greateruniverseofmodels.Togivethisamathematicalexpression,themuchloved
andmuchhatedtheoryofcategoriesisused.
McCullagh’s categories are a little bushy. Any object in any category can be
connectedby an arrow with any other object in any of the categoriesconsidered.
Theyare evidentlyassumedto bebuilt onsetsandcantherefore beconnectedby
functions; that is, they are all concrete categories [Mac Lane (1998), page 26].
A category A is concrete, if it is equipped with a faithful (injective on hom-
sets) functor to the category Set of sets and functions. Let this forgetful functor
bedenotedbyU .
A
Several of the categories constructed by McCullagh are so-called comma
categories[MacLane(1998),page46].Consideradiagram
B
→T A←S
C
ofthreecategoriesandtwofunctorswiththesamecodomain.Thecommacategory
from T to S, denoted (T,S) or (T ↓ S) as we shall do, has as objects triples
(b,c,f), where b is an object in category B, c an object in category C, and
f :Tb → Sc is an arrow in category A. Arrows between objects (b,c,f) and
(b (cid:5) ,c (cid:5) ,f (cid:5) ) in the category (T ↓ S) are all pairs (g,g (cid:5) ) consisting of an arrow
g:b → b (cid:5) in category B and an arrow g (cid:5) :c → c (cid:5) in category C such that the

| 1280 |     |     | DISCUSSION |     |     |     |     |
| ---- | --- | --- | ---------- | --- | --- | --- | --- |
diagram
Tg
|     |     |     | Tb  | Tb  | (cid:5) |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
f(cid:5)
f
Sg (cid:5)
(cid:5)
|     |     |     | Sc  | Sc  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
↓S)iscoordinatewise,andidentitiesarepairs
iscommutative.Compositionin(T
ofidentities.
By taking the first and second coordinates of the objects and arrows in the
commacategoryitisprovidedwithapairofnatural(forgetful)projectionfunctors
|     |     |     | ←P−rB−(T | ↓S)−P−→rC |     |     |     |
| --- | --- | --- | -------- | --------- | --- | --- | --- |
|     |     | B   |          |           | C.  |     |     |
Let D be a category with object class obj(D) and let D:D → (T ↓ S) be a
functor (if D is small enough D would be called a diagram over D in the
|                  |     | ∈obj(D) |     | D(d)=(D |         |                     |      |
| ---------------- | --- | ------- | --- | ------- | ------- | ------------------- | ---- |
| comma category). | For | d       | put |         | 1 (d),D | 2 (d),D 3 (d)) such | that |
D (d):T(D (d))→S(D (d)) in A. By joggling the symbols it is seen that the
| 3 1 |     | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | ◦   | → ◦ | →   |
family (D (d)) d∈obj(D) is a natural transformation T D S D:D A.
3
ThemappingD(cid:17)→(Pr ◦D,Pr ◦D,(D (d)) )is a1–1correspondence
|     |     | B   | C   | 3   | d∈obj(D) |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- |
|     |     | →   | ↓   |     |          |     |     |
between functors D:D (T S) and triples (D ,D ,π) consisting of a
B C
|     | →   |     |     | →   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
functor D B :D B, a functor D C :D C, and a natural transformation
π:T ◦D →S ◦D :D →A. In this way a diagram in (T ↓S) is identified
B C
withanaturaltransformationbetweencertainfunctors.
In his most general definition of a statistical model McCullagh starts with
three categories: (1) the category cat of statistical units, (2) the category cat
|     |     |     | U   |     |     |     | V   |
| --- | --- | --- | --- | --- | --- | --- | --- |
of response scales, and (3) the category cat ) of covariate spaces. From these he
firstconstructsthecategorycat ofdesignsasacommacategory,inournotation:
D
|                       |     | cat                               | =(U | ↓U   | )    |     |     |
| --------------------- | --- | --------------------------------- | --- | ---- | ---- | --- | --- |
|                       |     |                                   | D   | catU | cat) |     |     |
| andthenthecategorycat |     | ofsamplespacesasaproductcategory, |     |      |      |     |     |
S
|     |     | cat | =cat | ×cat | op . |     |     |
| --- | --- | --- | ---- | ---- | ---- | --- | --- |
|     |     |     | S    | V    |      |     |     |
U
×cat op
| Finally,thebasiccategoryistheproductcategorycat |     |     |     |     | V   | .Let |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- |
D
Pr op
|     |     | ←P−rV−cat | ×cat | op−−−ca−t→D | op  |     |     |
| --- | --- | --------- | ---- | ----------- | --- | --- | --- |
|     |     | cat       |      |             | cat |     |     |
|     |     | V         | V    | D           | D   |     |     |
bethediagramofprojections.Since
|                |                                   | i    | dc at × P r | o p    |        |     |     |
| -------------- | --------------------------------- | ---- | ----------- | ------ | ------ | --- | --- |
|                |                                   | op−  | V           | c−at   | op=cat |     |     |
|                | cat                               | ×cat | − − − − − − | U→ cat | ×cat   | ,   |     |
|                | V                                 | D    |             |        | V U    | S   |     |
| bothcat andcat | canbederivedfromthebasiccategory. |      |             |        |        |     |     |
| D              | S                                 |      |             |        |        |     |     |

WHATISASTATISTICALMODEL? 1281
The objects of cat are the sample spaces S which are carriers of probability
S
distributionswithP(S)thesetofprobabilitydistributionsonS.Samplespacesare
thereforenotjustsetsingeneral,butmustbesetswithsomekindofmeasurability
propertybyhavinganattachedσ-algebraofsubsetstosupportabstractprobabilitiy
measures,byhavingthestructureofalocallycompacttopologicalspacetobethe
basis for a normed Radon-measure, or by having some similar structure. Arrows
betweentwosuchspacesshouldbemeasurable,properorsomethingsimilar,such
that transformation of probability measures is defined. These properties should
be part of the definition of the basic category, and they ensure the existence of a
(faithful) functor V from cat to the concrete category MeasSet of measurable
S
| setsandmeasurablemappings.Iftoanarrowt:S→S |     |     |     | (cid:5) |
| ------------------------------------------ | --- | --- | --- | ------- |
inMeasSetweassignthe
mapping P(t):P(S)→P(S (cid:5) ) that carries a probability measure on S into the
(cid:5)
| t-transformedprobabilityonS |     | ,wegetafunctorP | :MeasSet→Set. |     |
| --------------------------- | --- | --------------- | ------------- | --- |
The parameter (cid:1) in McCullagh’s model is a contravariant functor on cat ) to
a not very accurately specified concrete category K, and the model is a natural
transformation,
P :U ◦(cid:1)◦Pr ◦Pr →P ◦(cid:1)◦(id ×Pr op):cat ×cat o p→Set
| K   | cat op cat | op  | catV | cat V D |
| --- | ---------- | --- | ---- | ------- |
|     | D          | U   |      | U       |
orinmoredetail,
op
cat ×cat
|     |     | V   | D          |         |
| --- | --- | --- | ---------- | ------- |
|     | Pr  | op  | idcatV ×Pr |         |
|     |     | cat |            | cat op  |
|     |     | D   |            | U       |
|     | op  |     |            | ×cat op |
|     | cat |     |            | cat     |
|     | D   |     |            | V U     |
Pr
cat) op
o p
|     | cat | ⇒P  |     | cat S |
| --- | --- | --- | --- | ----- |
)
|     | (cid:1) |     |     | V       |
| --- | ------- | --- | --- | ------- |
|     | K       |     |     | MeasSet |
|     |         | UK  | P   |         |
Set
BesidesconsideringthisoverallstructureMcCullaghputsspecificcontraintson
thearrowsinsomeofthecategories,constraintsofthesamesortaslimitingfactors
to be surjective mappings in the multifactor analysis of variance models. Such
restrictionstendtomakethemathematicalformalizationheavierandarereallynot
needed.
The simplest statistical models in McCullagh’s paper are the (parametrized)
statistical models, which are triples ((cid:1),S,P) consisting of a parameter set, a

1282 DISCUSSION
samplespace,andamappingP :(cid:1)→P(S).Theobviouschoiceofanarrowfrom
(cid:5) (cid:5) (cid:5)
a statistical model ((cid:1),S,P) to another ((cid:1),S ,P ) is a pair (φ,t) of a mapping
φ:(cid:1)→(cid:1) (cid:5) andameasurablemappingt:S→S (cid:5) suchthatthediagram
P
(cid:1) P(S)
φ P(t)
(cid:5)
P
(cid:1) (cid:5) P(S) (cid:5)
iscommutative.InthiswayacategoryStatModiscreated,whichispreciselythe
commacategory(id ↓P).Thiscategoryofstatisticalmodelscanbeinterpreted
Set
as the sea in which statisticians maneuveror the universein which theylive their
mathematicallivesandcanneverescape.Toincludeallstatisticaltransformations
Markovkernelsmustbeallowed,butletusleavethataside.
Returning to McCullagh’s general model we find, using the result above, that
thenaturaltransformation
P :id Set ◦U K ◦(cid:1)◦Pr cat op ◦Pr cat op →P◦(cid:1)◦(id catV ×Pr cat op):cat V ×cat o D p→Set
D U U
isequivalenttoafunctor
P :cat ×cat op→(id ↓P),
V D Set
or a “diagram” over the basic category in StatModel. McCullagh’s models are
therefore diagrams over a special kind of category in the category of statistical
models. If we consider the complicated definition of the basic category and the
difficulty with which McCullagh argues for the “scale of measurement,” it is
hard to see why only this special kind of category is included in the theory. The
basic principle is that the elementary models consideredare object valuesfor the
functorP andthearrowsbetweenthemarearrowvaluesofP.Itseemsnaturalto
consider diagrams overarbitrary categories. This will then include inbeddings of
subcategories,whichseemstobeverydesirable.
McCullagh has some considerations on product sets, product categories, and
repetitivemodels.Hisdefinitionofaproductcategoryisnotcompletelyclearand
not the usual one. Technically, the best way to treat structures of this kind is to
usemonoidalcategories,monoidalfunctorsandmonoidalnaturaltransformations,
thatis,categorieswithatensorproduct,functorsbetweentwomonoidalcategories
with a monoidal structure connecting the tensor products in the two categories
and natural transformations respecting the monoidal structures of the monoidal
functors they go between [see Mac Lane (1998), page 161]. In the category Set
theCartesianproductisatensorproduct,inMeasSettheCartesianproductoftwo
measurable sets equipped with, for example, the product σ-algebra, is a tensor
product, and the functor P :MeasSet→Set has a monoidal structure from the
mappingoftwoprobabilitiesintotheproductprobability.Themonoidalstructure

WHATISASTATISTICALMODEL? 1283
of the functors defining a comma category extends to a tensor product on the
commacategory,in ourexampleproducingthe productofstatistical models.The
diagramsinStatModshouldbeovermonoidalcategoriesandshouldbemonoidal
functors,etc.
McCullagh’s definition of a natural parameter or subparameter seems to be
in accordance with the definition of the extended models. It is sad that he does
not consider the consequences on the sample side. His main achievement is to
haveconvincinglyemphasizedtheimportanceofimposingfurtherstructureonthe
statisticalmodelstogivethemmoreofaphysicallifeandtohavemadeasuccesful
attemptatformalizingthisidea.Weshouldbethankfulforhisdriveandcourage.
REFERENCE
MACLANE,S.(1998).CategoriesfortheWorkingMathematician,2nded.Springer,NewYork.
DEPARTMENTOFSTATISTICS
ANDOPERATIONSRESEARCH
UNIVERSITYOFCOPENHAGEN
UNIVERSITETSPARKEN5
DK-2100COPENHAGEN
DENMARK
E-MAIL:hbrons@stat.ku.dk
DISCUSSION
BY D. A. S. FRASER AND N. REID
UniversityofToronto
This is an important and very original examination of statistical modelling,
which is such a ubiquitous part of statistical theory and statistical practice that
it is usually nearly overlooked. McCullagh provides a substantial examination
andstructuringofthis seriousfoundationalissue;indeed,the examinationisboth
intensiveandextensive.Foundationalissueshavenotbeenprominentin statistics
for some time, perhaps not since the shift away from the decision theoretic
approach to the more pragmatic addressing of individual applied problems. It is
gratifying now to see this substantial examination of the foundational issue of
statisticalmodelling.
McCullagh motivates his development with a series of examples that display
various logical or structural anomalies that can arise in the use and application
of the examples. Most of the examples are extreme, but this is appropriate for
highlightingpotentialdifficulties.
His development works from the familiar definition of a model as a set of
probability distributions on a sample space and a parameterized model as having

1284 DISCUSSION
in addition a mapping from a parameter space into the set of distributions. The
discussionfocusseson how a model impacts on the contextbeing examined,and
howitmightextendinapplicationstobroadercontexts.Categorytheoryisusedto
providethegeneralframeworkforthis.
One could reasonably question the familiar definition of a model in various
simple ways. Do we wish to speakof just a set of possibleresponsedistributions
as providing the core model of statistics? Why not perhaps the minimal step up
to the perception of a black box mechanism, with the output being the response
variableandaninputdialgivingtheparametervaluethatdeterminestheresponse
distribution, or are we so influenced by set theory that we would view these as
the same? One could argue that the two formulations are isomorphic, but the
perception and accessibility and influence for the latter are quite different. The
formerdescribesanessentiallyunrelatedsetofpossiblestatisticalbehaviorswhile
the latter at least conceptualizesa behavioralpattern that is changedby the input
dial[Fraser(1968a)].
The modelling should perhaps be more elaborate still. Most deterministic sys-
tems identify discrete component elements with linkages among these. The sys-
temisnotmodelledbyjustrecordingthesetofpairsconsistingofthedetermined
outcome response with the corresponding input values. The components and the
directions of causes and influences are modelled as well. Why should it be less
for the statistical model? While the theory of graphical models does attempt to
describesuchlinkages,muchofappliedstatisticsdoesnot.
Inmanycontextsthereareidentifiablesourcesforvariationanderrorcontribu-
tion. Shouldn’t these individual sources, rather than the global effect, be directly
modelled?Thediscussioninthepaperdoesnotaddresssuchmoreelaboratemod-
elling. Does it matter when the response behavior is the same? It can matter in
termsofwhatisknownaboutthesystemwhenoutputvaluesareobserved.When
the detailed modelprovidesmore information, oneshouldcertainly expectto ob-
tain moreforinference.Anexaminationofstatisticalmodelsthatdoesnotgobe-
yondthepre-blackboxmodellingtoincludespecificelementsofstructuresuchas
the error variablesand otherinternal componentelementscan be viewedas short
onthe“extensive”sideofcoverage.
Theattentiongiventocomponentparametersisneededandverywelcome.The
artificiality ofthe regressionparametersfor the Box–Coxmodelhastakena long
time to emerge with such clarity as it does here. It is also very interesting to
have a mathematical explanation of the widely (but not uniformly) adopted rule
in applied work that models with interactions and no corresponding main effects
arenotsensible.
In the context of transformation models there is some discussionof the nature
of particular component parameters in Fraser [(1968b), page 65]. Consider a
transformation model with parameter θ taking values in a transformation group
and with identifiable error variable, say z; thus y = θz. In this transformation
model setting what does it mean to say a component parameter ϕ is natural?

WHATISASTATISTICALMODEL? 1285
It is argued in Fraser [(1968b), page 65] that a component parameter is natural
if it indexes the left cosets of a subgroup. The arguments are not dissimilar to
thosearguinginreversethattheregressionparameterβ isnotanaturalparameter
for the Box and Cox model. Also, suppose for simplicity that the application of
the group is unitary and that left and right invariant measures on the group are
available. The model is invariant in the sense that y˜ =gy has distribution with
parameter value θ ˜ = gθ. The application of the group to the parameter space
wouldsuggesttheleftinvariantmeasuredµ(θ)asthenaturaldefaultpriormeasure
for the parameter. But if we view the transformation θ as being relative to some
initial errorpresentationthenwemightchangethatpresentationandhaveθ
¯=θh
appliedtothemodifiederrorash
−1z.Wemightthenwantinvariancerelativetothe
transformation θ ¯ =θh. This then suggests that we should use the right invariant
measuredν(θ)asthenaturaldefaultmeasurefortheparameter,adefaultmeasure
oftenpreferredintheBayesiancontext.
The weighing in of category theory leading to the definition of a natural
parameter would seem to need to be qualified by an acceptance that a statistical
model in an application is only providing some reasonable approximation to the
reality under investigation. Thus, for example, in Section 6.1 it is noted that
the coefficient of variation is not a natural component parameter; but in many
applicationsitcanbeaveryusefulandinformativeparameter.
McCullagh shows how category theory provides a frame of reference for
examining various simple but anomalous examples. But can category theory
do more than provide a frame of reference? Can it provide a positive way of
implementingandextractinganomaliesinmodelling?Itisclearthatthesubjectof
categorytheory is difficult to master. Perhapsit would be better to extractsimple
and broadly based principles for modelling. Or will the approach need to be one
ofseekingtheanomalousexamplesandthenseekingtherelatedprinciple.
The Cauchy example highlights an important point. McCullagh notes that
the location parameter is not a natural parameter in the context of the linear
fractional group. The concerns for the linear fractional group should perhaps go
further. A typical transformation is not a mapping of the real line to itself, but
can map a point to the point at infinity and vice versa; a rather severe lack of
continuity.McCullagh(1992)usedthesetransformationstoillustratetheapparent
nonuniqueness of the common ancillary statistic for location scale analysis. For
this the proposed reference set from the use of the linear fractional group is the
contourcorrespondingtotheobservedvalueoftheancillary,andwillhavemultiple
points with one or another coordinate at infinity, hardly a reference set with the
reasonable continuity expected for applications. It would seem appropriate that
such anomalies be avoided at the foundational assessment level for the model.
Thustheuseofthelinearfractionalgroupforassessingthelocationmodelshould
be rejected less for the anomalous nature of the location parameter and more for
thefactthatitdoesnotprovidemappingsofthesamplespacetoitself.

1286 DISCUSSION
This is a very comprehensive examination of serious foundational issues for
statistical theory and practice. We look forward to new examples of anomalies
uncoveredbycategorytheoryandalsotoawiderconcernforfoundationalissues.
REFERENCE
FRASER,D.A.S.(1968a).Ablackboxoracomprehensivemodel.Technometrics10219–229.
FRASER,D.A.S.(1968b).TheStructureofInference.Wiley,NewYork.
MCCULLAGH,P.(1992).ConditionalinferenceandCauchymodels.Biometrika79247–259.
DEPARTMENTOFSTATISTICS
UNIVERSITYOFTORONTO
100ST.GEORGESTREET
TORONTO,ONTARIOM5S3G3
CANADA
E-MAIL:reid@utstat.utoronto.ca
DISCUSSION
BY INGE S. HELLAND
UniversityofOslo
Theoretical statistics has since the beginning been founded on the idea that a
statistical model is just a parametric family of probability measures. Now Peter
McCullagh has given us a much richer model concept, and, importantly, this is
strictlymotivatedfromappliedscienceconsiderations.
In fact this new model conceptis so rich and at the same time so abstract that
it will take time for us to absorb it and for the statistical community to assess its
implications.ThereforeIwilllimitthesecommentstothesimplestsituation,which
is a model under symmetry, so that the categories involved are groups. The idea
thatitmightbeusefultosupplementthechoiceofastatisticalmodel—inthesense
of a parametric class of measures—bythe choice of a symmetry group, is an old
one,albeitstillsomewhatcontroversialregardingitsimplications.Onethingthatis
newherein McCullagh’sapproachis thesystematicuseofthe conceptofnatural
subparameter. I will expand a little on this concept, using parallel developments
fromHelland(2002).
Leta group G be definedon the parameterspace (cid:1) of a model. A measurable
function ξ from (cid:1) to anotherspace6 is calleda naturalsubparameterif ξ(θ )=
1
ξ(θ )impliesξ(gθ )=ξ(gθ )forallg∈G.
2 1 2
For example, in the location and scale case the location parameter µ and the
scaleparameterσ arenatural,whilethecoefficientofvariationµ/σ isnotnatural
(it is if the group is changed to the pure scale group). In general the parameter ξ
is natural iff the level sets of the function ξ =ξ(θ) are transformed onto other

WHATISASTATISTICALMODEL? 1287
levelsetsbyelementsofthegroupG.Usingthisonthelocationandscalegroup,
and making some smoothness assumptions, one can prove that ξ is natural iff
ξ =u(k µ+k σ)forsome1–1functionuandsomeconstantsk andk .
1 2 1 2
Thustheassumptionthatagivensubparameterisnaturalisdefinitelyarestric-
tion. Yet McCullagh indicates through his examples that in general statistical in-
ference should be limited to natural subparameters. I will give some additional
argumentstosupportthisratherradicalstatement.
˜
First, ξ is a natural subparameter if and only a new group G can be defined
consistently on 6 by g˜ξ(θ)=ξ(gθ). This means that for natural subparameters,
group-basedinferencecanbedoneinasimilarwayaswiththeoriginalparameter.
To illustrate this, consider a general and useful result on equality between
confidence sets and credibility sets. Let ξ(θ) be a one-dimensional continuous
ˆ ˆ
naturalparametricfunction,andletξ (x)andξ (x)betwoequivariantestimators.
1 2
[An estimator is called equivariant if ξ ˆ (gx) = g˜(ξ ˆ (x)) for all g,x.] Let the
group G be locally compact, transitive and proper; that is, the actions of G on
the sample space should be continuous, and the inverse image of compact sets
under the mapping (g,x)→(gx,x) should be compact, a rather weak technical
requirement.DefineC(x)={θ:ξ ˆ (x)≤ξ(θ)≤ξ ˆ (x)},andletθ haveapriorgiven
1 2
by the right Haar measure from the group G. Then C(x) is both a credibility set
andaconfidencesetwiththesameassociatedprobability/confidencelevel.
Therequirementthatasubparametershouldbenaturalmayalsohelptoresolve
certain inconsistencies in statistical inference, in particular the marginalization
inconsistency discussed in detail by Dawid, Stone and Zidek (1973). Their main
problem is a violation of the plausible reduction principle: assume that a general
methodofinference,appliedtodata(y,z),leadstoananswerthatinfactdepends
onzalone.Thenthesameanswershouldappearifthesamemethodisappliedtoz
alone.
A Bayesian implementation of this principle runs as follows: assume first that
the probability density p(y,z|η,ζ) dependson the parameter θ =(η,ζ) in such
awaythatthemarginaldensityp(z|ζ)onlydependsuponζ.Thenthefollowing
implication should hold: if (a) the marginal posterior density π(ζ |y,z) depends
on the data (y,z) only through z, then (b) this π(ζ |z) should be proportional to
a(ζ)p(z|ζ)forsomefunctiona(ζ),sothatitisproportionaltoaposteriorbased
solelyonthezdata.Foraproperpriorπ(η,ζ)thiscanbeshowntoholdwitha(ζ)
being the appropriate marginal prior π(ζ). Dawid, Stone and Zidek (1973) gave
severalexampleswheretheimplicationaboveisviolatedbyimproperpriorsofthe
kindthatwesometimesexpecttohaveinobjectiveBayesinference.
Forourpurpose,theinterestingcaseiswhenthereisatransformationgroupG
definedontheparameterspace.Undertheassumptionthatζ ismaximalinvariant
under G and making some regularity conditions, it is then first shown by Dawid,
Stone and Zidek (1973) that it necessarily follows that p(z|η,ζ) only depends
upon ζ, next (a) is shown to hold always, and finally (b) holds if and only if the
prior is ofthe form ν (dη)dζ, where ν is right Haarmeasure,andthe measure
G G

1288 DISCUSSION
dζ isarbitrary.Thusforthissituationwithsuchapriornotonlydoesthereduction
principle hold; we also have that the premises of the principle are automatically
satisfied.
The strong assumption made above was that ζ is invariant. In a second class
ofexamplesDawid,Stone andZidek(1973)showthat this assumptioncannotbe
violatedarbitrarily.InHelland(2002)weshowthatitisessentiallyenoughtomake
themuchweakerassumptionthatζ isanaturalsubparameter.
Specifically,assumethatζ isnatural,andletK bethesubgroupofGgivenby
K ={g:ζ(gθ)=ζ(θ) forall θ}. Then ζ is maximal invariant under K. Assume
also that z is maximal invariant under the corresponding group acting on the
samplespace.ThenusingrightHaarpriorunderGontheparameterspace(cid:1),we
havethatanydata(y,z)leadstoaposteriorofζ proportionaltotheoneobtained
fromonlydataz.
A simple example is provided by letting G be the location and scale group
definedby µ→a+bµ, σ →bσ (b>0),and thentaking ζ =µ or ζ =σ when
the right invariant prior is dµdσ/σ. There is no marginalization paradox in this
case.
Inallsuchexamplesthechoiceofgroupiscrucial.Somegeneralrequirements
on this choicecanbe specified:(i) the classofprobability distributions shouldbe
closed under the transformations in the group; (ii) if the problem is formulated
in terms of a loss function, this should be unchanged when observations and
parametersaretransformedconformablybythegroup;(iii)therightHaarmeasure
of the group should be chosen as the uninformative prior for the problem.
Afurtherrequirementisthatallparametricfunctionsofinterestshouldbenatural
subparameters with respect to the group. It is this last requirement which makes
thelocationandscalegroup,notthegroupofrealfractionallineartransformations,
thecanonicalchoicefortheCauchydistributioncase.
Statistical models can be reduced by keeping one subparameter constant and
focusing on the remaining parameter. Reduction of statistical models is often
useful in prediction settings. Every model reduction should be via a natural
subparameter.Wealsoknowquitegenerallythattheparameteralonganorbitofthe
group can be estimated in an optimal way by a Pitman type estimator. Therefore,
tobeofuseinestimationorprediction,modelreductionshouldbelimitedtoonly
concerning the orbit indices of the group. This was used in Helland (2001) to
motivatemodelreductioninregressionproblemswhichgivesarelationshiptothe
chemometricians’partialleastsquaresregression.
There is a situation resembling model reduction, however, which should
not necessarily be done via natural subparameters: assume that ψ ∈ 7 is a
superparameter that can be used to describe several experiments, among which
a choice must be made. Assume also that a group is defined on 7. Then the
parameters of the single experiments are not necessarily natural subparameters
of ψ. It may namely be the case that the subparametermakes sense only relative
tothisparticularsubexperiment,notinanyglobalway.

WHATISASTATISTICALMODEL? 1289
Consider as an example the following situation: assume that the model of two
experimentsonthe sameunitdependsuponwhichexperimentis carriedoutfirst,
say that the parameter of the first experiment is θ (ψ,α) if this is done first,
1
otherwise θ (ψ,β), where there is a given relationship between α and β. Let the
1
morphismscontainpermutationoftheorderoftheexperiments.Then,ingeneral,
θ willnotbeanaturalsubparameter.
1
It is tempting to approach quantum physics from a statistical point of view
by saying that it contains a number of situations with similar properties. In fact,
one can proceed quite a bit from this, but there are also very difficult questions
in this approach, in particular in understanding the formal structure of quantum
mechanics. It seems, however, that group representation theory may be of some
help,combinedwithasystematicreductionofstatisticalmodels.
Inworkinginsuchnewdirectionsitisveryimportantthatwenowhaveabetter
characterization of what a statistical model is. The kind of precise link between
common sense and formal theory which Peter McCullagh has demonstrated so
forcefully in his paper, is indeed useful for several purposes, and it may set a
standardformuchtheoreticalworkinstatistics.
REFERENCE
DAWID, A. P., STONE, M. and ZIDEK, J. V. (1973). Marginalization paradoxes inBayesian and
structuralinference(withdiscussion).J.Roy.Statist.Soc.Ser.B35189–233.
HELLAND,I.S.(2001).Reductionofregressionmodelsundersymmetry.InAlgebraicMethodsin
StatisticsandProbability(M.VianaandD.Richards,eds.)139–153.Amer.Math.Soc.,
Providence,RI.
HELLAND, I. S. (2002). Statistical inference under a fixed symmetry group. Available at http://
www.math.uio.no/∼ingeh/.
DEPARTMENTOFMATHEMATICS
UNIVERSITYOFOSLO
P.O.BOX1053BLINDERN
N-0316OSLO
NORWAY
E-MAIL:ingeh@math.uio.no
DISCUSSION
BY PETER J. HUBER
Klosters,Switzerland
McCullagh’s paper is a plea for more realistic statistical models. He hopes
to enforce sensibility of models through category theory, by imbedding some
equivalentof “having a well-defined meaning” into the formal theory. I certainly
agreewithhisaimsandthatitisnecessarytopayattentiontotheinferencedomain

1290 DISCUSSION
andthatcategorytheorymayhelpyoutodoso.ButImustconfessthatIstumbled
over some telltale idiosyncrasies of his terminology. He variously denotes bad
models as “absurd,” “eccentric,” “arbitrary” or “capricious.” For me, a statistical
model ordinarily is supposed to model some real-world situation, and as such it
either is adequate, or it is not. His attributes do not apply, except to straw-man
models concocted by a mathematical statistician. Correspondingly, he may go
too far with his attempts to discuss sensibility of models in the abstract; in my
opinion,constantreferencetotheunderlyingreal-worldsituationisadvisableand
even necessary. If the latter is capricious, the model should faithfully render this
capriciousness!Iamthinkinghere,forexample,ofthedistinctionbetweenintegral
and half-integral spin values in quantum mechanics, which to the uninitiated
looks no less absurd or artificial than the even-odd distinction in McCullagh’s
Exercises1,2and4.
In the following, I shall concentrate on the category theory aspects of the
paper. I should begin by recounting some bygone experiences of my own. More
than forty years ago—I had just finished a thesis in category theory [Huber
(1961)]—I went to Berkeley to learn statistics. There, I sat in Lucien Le Cam’s
courses on decision theory. He devoted much time, I believe an entire term, to
the comparison of experiments in the style of his recently submitted, but as yet
unpublished 1964 paper in the Annals. One should know that Le Cam loved
abstractnessandatthattime wasenthusiasticaboutGrothendieck’s(1955)thesis.
ToavoidpossiblemisunderstandingsIshouldaddthatthatthesiswasinfunctional
analysis, not in homological algebra [see Cartier (2001), page 392 for some
of the background]. In Le Cam’s terminology, an “experiment” is exactly the
same as a “model” in McCullagh’s sense, namely a parameter set (cid:1) together
with a function P :(cid:1) → P(X), which assigns to each parameter point θ ∈ (cid:1)
a probability distribution P on the sample space X. Le Cam, however, found it
θ
convenient to replace this classical notion of experiment by a weaker structure
consisting of a vectorlattice with a unit, E, together with a family indexedby (cid:1)
of positive normalized linear functionals on E [Le Cam (1964), pages 1420–
1421]. With some restriction of generality, E may be thought of as the space of
bounded observable random variables on X, and to facilitate this interpretation,
the set X was retained by Le Cam as a part of the structure. Moreover, since he
wanted to handle sufficiency, simple pointwise maps would not do, and Le Cam
hadtoreplacethembyrandomizedmaps,ortransitionfunctions(seetheexample
below).Anyway,thingsgotprettycomplex,andtosortthemoutinmyownmind,
IrephrasedthefundamentalsofLeCam’stheoryincategoricallanguage.
Example: Sufficient statistics. Let Experiment A consist in observing X =
(X ,...,X ), where the X are i.i.d. (cid:1)(µ,σ2), while Experiment B consists in
1 n i
observingtwo independentvariables (U,V), where U is (cid:1)(µ,σ2/n), and V/σ2
(cid:10)
is χ2 . There is a natural map from A to B [U = X = n −1 X ,V = S2 =
n−1 i

WHATISASTATISTICALMODEL? 1291
(cid:10)
(X − X)2]. On the other hand, since the conditional distribution of X =
i
(X ,...,X ) given (X,S2) does not depend on (µ,σ2), there is a randomized
1 n
map(ortransitionfunction)fromBtoA,reconstructingasampleY =(Y ,...,Y )
1 n
having the same stochastic properties as the original sample X for all values of
(µ,σ). With suitably chosen definitions, these two morphisms from A to B and
fromBtoAwouldbeinversetoeachother.
Inordertodealwithsituationsoccurringintheanalysisofvariance,onehadto
considerrandomizedmapsnotonlyofthesamplespaces,butalsooftheparameter
spaces. Thus, morphisms in the category of statistical experiments really were
suitably defined equivalence classes at least of pairs of transition functions, and
built-inredundancies(vectorlatticesandsamplespaces)complicatedmatterseven
further.
Categorical thinking, that is: thinking in terms of morphisms, functors and
commutative diagrams, always helps to clarify the underlying structure of
mathematicalobjects,todefinestructuralisomorphismsproperly,andinparticular,
to recognize morphisms that are natural (or canonical). Rephrasing statistical
problems in categorical language had clarified my thinking about some of them
in a crucial fashion. In particular, it had helped me to understand and properly
formalize the concept of invariance of a statistical experiment within Le Cam’s
framework of topological vector lattices, and hence to formulate and prove the
Hunt–SteintheoreminwhatIstillbelievetobeitsnaturalhabitat;seetheremarks
byBrown[(1984),page407].
For my own purposes I collected the categorized foundations of Le Cam’s
theory of statistical experiments in a memo which ultimately grew to about 10
to 12 pages, all of it definitions. But then, why did I not expand my little memo
andprepareitfor publication?Therewere two reasons:First, abstractcategorical
thinking had helped me only because I already was fluent in that language. Very
fewpeoplewouldprofitfromapaperpilingmoreabstractiononLeCam’salready
veryabstractsetup,andIforesawthatIwouldhaveevenmoredifficultiesgetting
it accepted than Lucien had with his papers (he told us some anecdotes about
his prolonged fights with editors and referees). Second, while my translation
into categorese had streamlined the exposition, it had not added content to these
particular problems.It did not unify different lines ofthought(as I hadbeen able
to do in my thesis, for example), it did not lead to new theorems, except very
indirectly, and did not even simplify the proof of a central statement such as the
Blackwell–Sherman–Stein theorem. Apart from that, around that time I became
engrossedinmuchmoreexcitingrobustnessproblems.
Now, how about McCullagh’s paper? First, when we compare what he does
now to what I did 40 years ago, it is quite illuminating to notice that basically
the same situation can be categorized in more than one fashion. But I think the
same comments, benefits and difficulties apply here too. It may be heartening
to learn that such papers have become publishable in statistical journals now.
McCullagh certainly is able to clarify thinking about models (but I must admit

1292 DISCUSSION
that even I myself found it hard to get back into the categorical lingo after 40
years). On the other hand, also in his case, category theory does not seem to
add content. Moreover, against McCullagh I doubt that categories have enough
normative powerto preventone from doing absurd things. This may be the price
wepayfortheabilitytomodelalsocapriciousreal-worldsituations.
REFERENCE
BROWN, L. D. (1984). Theresearchof JackKieferoutsidetheareaof experimental design. Ann.
Statist.12406–415.
CARTIER, P. (2001). A mad day’s work: From Grothendieck to Connes and Kontsevich. The
evolutionofconceptsofspaceandsymmetry.Bull.Amer.Math.Soc.38389–408.
GROTHENDIECK, A. (1955). Produits tensoriels topologiques et espaces nucléaires. Mem. Amer.
Math.Soc.16.
HUBER,P.J.(1961).Homotopytheoryingeneralcategories.Math.Ann.144361–385.
LECAM,L.(1964).Sufficiencyandapproximatesufficiency.Ann.Math.Statist.351419–1455.
P.O.BOX198
CH-7250KLOSTERS
SWITZERLAND
E-MAIL:peterj.huber@bluewin.ch
DISCUSSION
BY RUDOLF KALMAN
ETHZurich
“Model” and “modeling” are the most abused, distorted, misleading, self-
servingtermsin thecontemporaryscientificdictionary.Takinga hardlookatthis
very soft and messy business is most commendable. So is the author’s careful
restrictionofhisinvestigationtostatisticalmodels,defined,asusual,tobefamilies
of probability distributions, and I am sure he would not object to the further
qualification of mathematical statistical models. Indeed, the paper is a model of
mathematicalclarity.
It is very nice also to have attention focused on the technical mathematical
questions of parametrization, motivated via the idea of a “natural map” first
made precise by category theory, which is given a nicely organized summary
in the Appendix, intended for the uninitiated enthusiast. While I cannot pretend
to be an expert, has-been or to-be, as regards the examples in Section 2 around
which the development of the paper is structured, common sense suggests that
statistics cannotbut benefitfrom a more careful look at the storehouseof current
models. McCullagh’s initiative should add much momentum to the constructive
criticism of these models, serving as a substitute for real-world experiments,

WHATISASTATISTICALMODEL? 1293
which are notusually feasiblein the problemarea coveredby the paper. In short,
criticism=experimentation,andstatistics,todaystillanonempiricalscience,will
beinvigoratedbyadiscussionofthekindofissuesraisedinthepaper.
IfInowcometomorecriticalcommentsconcerning“models”and“modeling”
it should be clear that these do not apply specifically to McCullagh’s work but
refer to (it is sad that this has to be said) the mainstream statistical literature as
a whole. My critique is that the currently accepted notion of a statistical model
is not scientific; rather, it is a guess at what might constitute (scientific) reality
withoutthevitalelementoffeedback,thatis, withoutcheckingthe hypothesized,
postulated, wished-for, natural-looking (but in fact only guessed) model against
that reality. To be blunt, as far as is known today, there is no such thing as a
concrete i.i.d. (independent, identically distributed) process, not because this is
notdesirable,nice,orevenbeautiful,butbecauseNaturedoesnotseemtobelike
that.(Historicalaside:recallthatphysicistshadthoughtatonetimethatetherwas
sucha necessary,unavoidable,appealing,clearandbeautifulconceptthat it must
perforceexist;alas,allphysicistsnowlivinghadtolearnthatsuchargumentation
cannotleadtogoodscience.)AsBertrandRussellputitattheendofhislonglife
devotedtophilosophy,“Roughlyspeaking,whatweknowisscienceandwhatwe
don’tknowisphilosophy.”Inthescientificcontext,butperhapsnotintheapplied
area,Ifearstatisticalmodelingtodaybelongstotherealmofphilosophy.
Tomakethis pointseemslesserudite,let me rephraseit in cruderterms. What
wouldascientistexpectfromstatisticians,oncehebecameinterestedinstatistical
problems?Hewouldaskthemtoexplaintohim,insomeclear-cutcases,theorigin
of randomnessfrequently observedin the real world, and furthermore, when this
explanation depended on the device of a model, he would ask them to continue
to confront that model with the part of reality that the model was supposed to
explain. Something like this was going on three hundred years ago, for example,
in discussions involving male and female births [Arbuthnott (1712)]. But in our
timestheideasomehowgotlostwheni.i.d.becamethepamperednewbaby.
Without trying to fix the blame for all this (why not? someone may well be
responsible, though certainly not the author) it is instructive to look at current
popular hype. A random example is the recent book by Edward J. Beltrami
[(1999), What Is Random?: Chance and Order in Mathematics and Life, 201
pages,Copernicus(aSpringerimprint)].Inthistheauthor,veryproperly,askswhat
randomness is in the real world; he notices that “probability” describes a certain
kind of randomness, takes that as his definition of randomness and from then on
speculatesontheconsequences,apparentlyforgettingthathedidnotgetaroundto
explainingor evento describingrandomnessin Nature. He merelyfilters through
his own mind great thoughts of great thinkers about probability. Lightweight
reading, a sophisticated joke, not scientific. It is ironic that a serious scientific
publisher,Springer,shouldbehijackedintoputtingsuchshallowphilosophical(in
Russell’s sense) stuff into a new series named after a scientific icon, a towering
andindependentintellect,anincorruptiblecriticofsoft“applicable”knowledge.

1294 DISCUSSION
REFERENCE
ARBUTHNOTT,J. (1712). Anargument for DivineProvidence, taken fromtheconstant regularity
observedinthebirthsofbothsexes.Philos.Trans.Roy.Soc.London27186–190.
DEPARTMENTOFMATHEMATICS
ETHZURICH
WENB17ZURICH
SWITZERLAND
E-MAIL:kalman@ufl.edu
DISCUSSION
BY STEVE PINCUS
Guilford,Connecticut
Thisisaveryinterestingandthought-provokingpaper,whichIenjoyedreading.
While the notions of sound statistical models and parameters are essential to
the core of a classical statistical framework, heretofore a broadly applicable,
single (parsimonious) unifying conceptualapproach and formalism had not been
put forth, nor one addressing the caveats pointed out in the Introduction in the
presentpaper.ProfessorMcCullaghnowsuccessfullyadvancessuchaformalism,
based on the natural algebraic methodology given by category theory, building
on previous work on invariance and factorial models [McCullagh (2000)] and
on quotient spaces and statistical models [McCullagh (1999)]. The author shows
thatadiverserangeofsensiblestatisticalapplications,oftenconsideredasdistinct
settings, all can be handled within the framework of this formalism. The breadth
oftherangeofthe12examplesinSection2reinforcesthescopeoftheformalism.
Some might argue that this unification could be achieved without introducing
the technologic machinery of category theory or algebra. The crucial point, to
my sensibilities, clarifying that the present (or similar) technology is required
for a general formalism is the discussion of the naturality of subparameter
specification, Section 4.5, with its implications to inference. The concept of a
natural transformation is a central notion within group and category theory, but
notubiquitousthroughoutmathematics.
Insofar as cross-pollination between and from algebra to (probability and)
statistics, there is a long and rich history that goes back at least half a century.
ThustheutilityofProfessorMcCullagh’sapproachisnotunprecedented,although
the extensive application at the level of generality of category theory may be so.
Theseriesofcontributionsto avarietyofstatisticalproblems,includingtopicsas
diverseasexperimentaldesignandcardshufflingmadebyPersiDiaconis,Graham
and Kantor (1983), Diaconis (1988) and Rosemary Bailey (1981, 1991), among
others, exploiting group invariance and symmetries are probably well known

WHATISASTATISTICALMODEL? 1295
to the readers here. Notably, as well, the history also includes significant and
influential contributions made by Ulf Grenander [e.g., Grenander (1963)] to the
study of patterns, and by Harry Furstenberg (1963) to the study of products of
randommatrices(fromwhichtheLyapunovspectraandrelateddynamicalsystems
theoryparametersarederived).Iespeciallynotetheselattertwomathematiciansas
eachintegrallyfeaturesLiegroupandLiealgebratheorythroughouttheirefforts.
Thus,disciplesofthesedevelopments,alreadyfacilewiththealgebraicmachinery
utilizedherein,maybeabletomakeadditionalcontributionsatopthosedeveloped
todatebytheauthor.
I havetwo stylistic comments.First, the organization is fine for someonerela-
tively familiar with category theory, but for other readers it may be considerably
more challenging, as it leads heavily with this theory in Sections 3–5. Without a
roadmap,theinterestedreadermightgiveupbeforerecognizingthe“meat”ofthe
approach.I’dstronglysuggestthatrelativelyearlyon,beforedivingheadlonginto
Sections3–5,thereaderjumptoSection6andfindanexampleofparticularinter-
est,thengobackandforthbetweenthetheorysectionsandtheexamples.Onecan
thenappreciatetheformaldevelopments“concretely”fromwhichtheabstractions
and generalizations become much clearer. One illuminating example for me was
the example in 6.2, Exercise 10 of Section 2, regarding inference concerning the
correlation coefficient ρ derived from the standard linear regression model with
onecovariate.
The second (and cosmetic) comment is that I prefer the adjective ad hoc to
absurd in describing, for example, the models of Section 2. I agree with the
substanceoftheauthor’spoint,thatthereisnohopeofabroadornaturaltheoretic
general framework or basis for these models. Nonetheless, such models are of
course used by well-intended yet (somewhat) naïve practitioners to produce, for
example, figures of merit within specific contexts,and I see no need to embarass
thetargetuser.
My major concern is primarily a recognition of a limitation of the algebraic
approach. Namely, the (category theory) technology utilized herein cannot be
readily extended or adapted to address some spiritually related operational
questionsthatarecentraltothecoreofstatisticalpractice.Tomysensibilities,this
paper is probabilistic (rather than statistical) in spirit, albeit evidently applied to
modeltypesandproblemsclassicallyconsideredbystatisticians.Iwouldprobably
be happier with the title “What is a parametrized probabilistic (or stochastic
process) model?” This is not “bad,” as I am a probabilist, but the formalism
inferentially bears on processes and distributions, not short and moderate length
sequences apart from their definition as possible initial segments from typical
realizationsofaprocess.Thespecifictechnicalissueisthatanalgebraicapproach
hasaconsiderablelimitation,inthelackofanaturalmetric.Thispointisnotedby
ProfessorMcCullaghin Section8.3, albeit towardsa very different consideration
(theBesag–Higdonformulationofyieldinagriculturalfieldtrials):“Algebradoes
not easily deal with approximations or inequalities....” The presenceof a metric

1296 DISCUSSION
is not required in the present paper, and the lack thereof within category theory
doesnotobviateanyoftheformaldevelopments.Butsupposewewishtoconsider
which model form is better, given one or several (necessarily finite) realizations,
among two proposed forms? As David Cox (1990) states, “In particular, choice
of an appropriate family of distributions may be the most challenging phase of
analysis.” Most sensible means to resolve such a question, and there are many
such, require a metric, and thus primarily algebraically (particularly category
theory) based attempts would likely be artificial and inadequate. I do wish to
point out if there is topological as well as algebraic structure in a formal model
framework (e.g., a Lie group), then convergence defined by the topology can
resolvethemetricquestionintermsofsomelimitingorasymptoticbehavior;thus
someprobabilistic,thatis,infinitesequencecomparisonscanpossiblyberesolved
withinanalgebraicframework.Butfordecidedlynonasymptoticdatalengths,and
statistical procedures based on them, many formal descriptions will still require
nonalgebraicapproaches.
Finally, also on a related topic, I would like to mention that for discrete state
data, there is a means of assessing the “extent of randomness” or irregularity of
a finite or infinite sequence that does not require a model-based (or stochastic
process) setting, parametrized or otherwise, in the classical sense [Pincus and
Singer(1996);PincusandKalman(1997)].Aformalismisdevelopedstrictlyona
combinatorialbasis,againforbothfiniteandinfinitelengthsequences.Thiscould
be used, for example,in both discrimination and classificationcontexts,although
thisisaseparatediscussionaltogether.
REFERENCE
BAILEY,R.A.(1981).Aunifiedapproachtodesignofexperiments.J.Roy.Statist.Soc.Ser.A144
214–223.
BAILEY,R.A.(1991).Strataforrandomizedexperiments(withdiscussion).J.Roy.Statist.Soc.Ser.
B5327–78.
COX,D.R.(1990).Rolesofmodelsinstatisticalanalysis.Statist.Sci.5169–174.
DIACONIS,P.(1988).GroupRepresentationsinProbabilityandStatistics.IMS,Hayward,CA.
DIACONIS,P.,GRAHAM,R.L.andKANTOR,W.M.(1983).Themathematicsofperfectshuffles.
Adv.inAppl.Math.4175–196.
FURSTENBURG,H.(1963).Noncommutingrandomproducts.Trans.Amer.Math.Soc.108377–428.
GRENANDER,U.(1963).ProbabilitiesonAlgebraicStructures.Wiley,NewYork.
MCCULLAGH,P.(1999).Quotientspacesandstatisticalmodels.Canad.J.Statist.27447–456.
MCCULLAGH,P.(2000).Invarianceandfactorialmodels(withdiscussion).J.Roy.Statist.Soc.Ser.
B62209–256.
PINCUS,S.andKALMAN,R.E.(1997).Notall(possibly)“random”sequencesarecreatedequal.
Proc.Nat.Acad.Sci.U.S.A.943513–3518.
PINCUS,S.andSINGER,B. H.(1996).Randomnessanddegreesofirregularity.Proc.Nat.Acad.
Sci.U.S.A.932083–2088.
990MOOSEHILLROAD
GUILFORD,CONNECTICUT06437
E-MAIL:stevepincus@alum.mit.edu

WHATISASTATISTICALMODEL? 1297
DISCUSSION
BY TUE TJUR
CopenhagenBusinessSchool
Peter McCullaghs article is an overwhelming cascade of interesting and
provoking ideas, related to the vague and intutitive concept of “a model making
sense.” As stressed by the author, many of the conclusions coming out of this
are already part of good statistical tradition. But I agree that it is interesting
to investigate to what extent such traditions can be stated as consequences of a
mathematically coherent models concept. What I think is missing, so far, is an
applicationthatresultsin aconclusionwhichis nontrivialorevensurprising.But
thisisprobablytoomuchtoaskforatthepresentstageofdevelopment.
Some statistical models are canonical. Canonicalstatistical models include, as
a minimum, the linear normal models (regression and analysis of variance), the
multiplicative Poissonmodels andthe multinomial modelsderivedfrom theseby
conditioning, and the logit linear models for binary data. Very few statisticians
would probably dare to disagree here. A question closely related to the present
paperis:Whyarethesemodelscanonical?Andwhatis—ifanything—acanonical
model?
A partial answer to this question is that a canonical model is a model which
is constructed from other canonical models in a canonical way. Perhaps this
statementisnotofmuchhelp,butitneverthelessjustifiesasuccessfulconstruction
whichI wouldlike to reconsiderhere,sincetheauthorhasonly mentionedit in a
briefremark(inSection6.4).Iamthinkingofthemodelsforordinaldatapresented
inMcCullagh(1980).
Supposewe are dealingwith a universewhere the naturalmodelsfor handling
of binary responses are the logistic regression models. This could be some
socioeconomicresearchareawherepeoples’attitudestovariousfeaturesofbrands
or service levels are recorded on a binary scale, and the interest lies in the
dependence of these attitudes on all sorts of background variables. How do we
extend this universe to deal with ordered categorical responses, for example, on
three-pointpositive/indifferent/negativescales?Anaturalrequirementseemstobe
thatifdataaredichotomizedbythe(arbitrary)selectionofacutpoint(putting,for
example,negativeandindifferenttogetherinasinglecategory),thenthemarginal
model coming out of this is a logistic regression model. This is, after all, just a
wayofrecordingabinaryresponse,andeventhoughitwouldhurtanystatistician
to throw away information in this way, it is done all the time on more invisible
levels. Another natural requirement is that the parameters of interest—with the
constant term as an obvious exception—should not depend on how the cutpoint
is selected. It is easy to show that these two requirements are met by one and
only one class of models for ordered responses, namely the models that can

1298 DISCUSSION
be described by an underlying continuous linear position parameter model with
logisticerrordistribution,wheretheresponsesaregroupedbyunknowncutpoints.
Theunderlyingcontinuousmodelcanberegardedasasortoflimitofthediscrete
models as the number of ordered categories grows to infinity. A projective limit,
totalkcategorylanguage.
Anotherconstructioninthesamespirit,thoughsomewhatlesssuccessfulfroma
theoreticalpointofview,istheconstructionofoverdispersionmodelsfromsimple
generalizedlinearmodels.Isthereanaturalextensionoflogisticregressionmodels
for binomial data or multiplicative Poisson models that can be used in situations
wherethegoodness-of-fittestshowsthatthemodelisincorrect,butpointestimates
ofparametersandfitted valuesare,nevertheless,consideredrelevantandcorrect?
Canwefindaclassofstatisticalmodelsthatextendstheoriginalgeneralizedlinear
modelbysomescaleparameter,insuchawaythat:
1. theoriginalgeneralizedlinearmodelcomesoutasaspecialcasewhenthescale
parameterisfixedandequalto1;
2. themaximumlikelihoodestimatesinthemodelfortheoriginal“link-function-
linear” parameters coincide with those of the original model (ignoring the
overdispersion).
The answer to this question is no. At least for logistic regression it is
obviousthat no such model exists,becausethe boundedsupports of the response
distributions determined by the given binomial totals or indices do not allow for
afreelyvaryingscaleparameterintheusualsense.Nevertheless,thehypothetical
answer to this question is the driving force behind the development of the very
useful methods for handling of generalized linear models with overdispersion as
indicatedbyNelderandWedderburn(1972)andfurtherdevelopedbyMcCullagh
and Nelder (1989). Thus, we have here the absurd situation that the potentially
canonical—but unfortunately nonexisting—answer to a simple and canonical
questionresultsinacollectionofveryusefulmethods.Theoverdispersionmodels
existasperfectlyrespectableoperationalobjects,butnotasmathematicalobjects.
Mypersonalopinion[Tjur(1998)]isthatthesimplestwayofgivingthesemodels
a concrete interpretation goes via approximation by nonlinear models for normal
dataandasmalladjustmentoftheusualestimationmethodforthesemodels.But
neitherthis,northeconceptofquasi-likelihood,answersthefundamentalquestion
whetherthereisawayofmodifyingtheconditions(1)and(2)aboveinsuchaway
that a meaningfultheory of generalized linear models with overdispersioncomes
outastheuniqueanswer.
It is tempting to ask, in the present context, whether it is a necessity at all
that these models “exist” in the usual sense.Is it so, perhaps, that after a century
or two people will find this question irrelevant, just as we find old discussions
aboutexistenceofthenumber+∞irrelevant?Ifthisisthecase,anewattitudeto
statisticalmodelsiscertainlyrequired.

WHATISASTATISTICALMODEL? 1299
Statisticsaspracticedtodaysuffersfrommanysimilarproblemsandparadoxes.
In survival analysis we have Cox’s likelihood, which undoubtably is a canonical
thing, but unfortunately not a likelihood in any model that we know of. In basic
statistical inference, paradoxes related to sequential situations and Birnbaum’s
paradox are among the problems we have learned to ignore and live with. This
doesnothavemuchto dowith PeterMcCullaghspaper,butitillustrates theneed
for a clarification of basic concepts. A more restrictive definition of a statistical
model than the usual one by arbitrary families of probability distributions on a
samplespacemayturnouttobeanecessaryingredienthere.
CertainaspectsofPeterMcCullagh’sexpositiontakeusbacktotheroots,inthe
sensethatmanyoftheideasthatheexpressesintermsofcategorytheoryarevery
similar to ingredients of the slightly old-fashioned way of expressing models in
termsofpopulationsandsamples,ratherthanprobabilitydistributionsandrandom
variables.Iwouldlike to stressthis byrepeatingasinglepointhehasconcerning
regressionanalysis.Justto emphasizethatcategorytheoryis nota necessarytool
here,butonlyaconvenientlanguage,Iwilltrytodoitwithoutthistool.
Thestandardtextbookwayofspecifyingasimpleregressionmodelistosaythat
wehaveobservationsy ofindependentnormalrandomvariablesY ,i=1,...,n,
i i
withthesamevarianceσ2 andexpectationsoftheformα+βx ,wherex ,...,x
i 1 n
are known quantities. This is undoubtably a useful way of saying it, but it has
the drawback that it does not specify the parameters that can be meaningfully
estimated.Quantitieslikethesamplesizenandtheaverageexpectationα+βx¯ (or,
more complicated, the correlation coefficient as suggested by the author) can be
estimatedwithout problemsin this model,butthis is irrelevantfor mostpurposes
because these quanties are related not only to the unknown parameters, but also
to the design—in this case represented by the choice of the values x ,...,x
1 n
of the independent variable. A way of stating the model that takes this into
accountgoesasfollows.Takeasthestartingpointaninfinitepopulation{(x ,y )}
i i
of x-values and corresponding y-values. Only the x-values are visible from the
beginning,andwhatwedowhenweperformtheexperimentisactuallytodraw—
not at random, but rather by some criterion for selection of a representative set
of x-values—asamplefrom thispopulation.Now,defineaparameterfunctionas
a rule which to each such selection x ,...,x of finitely many x-values assigns
1 n
a parameter in the usual sense, that is, a function of the unknown distribution in
the correspondingstatistical model. This includes any function of (α,β,σ2), and
also,so far, expressionslike n or α+βx¯. Here, atechnicalcondition is required,
statingthatatleasttwodistinctx-valuesshouldbepresent,butwewillignorethis
irrelevantdetailin thefollowing.Now,defineameaningfulparameterfunctionas
a parameter function which is invariant under the formation of marginal models,
that is, when a design is reduced by removal of some of the x’s, the parameter
associated with the marginal distribution should equal the parameter associated
withthedistributioninthemodelforthebiggersample.Thisreducesthepossible
parameter functions to the set of functions of (α,β,σ2). A quantity like α+βx¯,

1300 REJOINDER
where x¯ is the average of the x-values in the design we happened to select, is
clearly not a meaningful parameter function in this sense. Moreover, this kind of
set-upisexactlywhatisrequiredifonewantsatheorythatdoesnotallowforsuch
absurditiesasthosesuggestedin“exercises”1,2,3,4and5ofSection2.1.
REFERENCE
MCCULLAGH,P.(1980).Regressionmodelsforordinaldata(withdiscussion).J.Roy.Statist.Soc.
Ser.B42109–142.
MCCULLAGH,P.and NELDER,J. A.(1989). GeneralizedLinearModels,2nd.ed.Chapmanand
Hall,London.
NELDER,J. A. and WEDDERBURN,R. W. M. (1972). Generalizedlinearmodels.J.Roy.Statist.
Soc.Ser.A135370–384.
TJUR, T. (1998). Nonlinear regression, quasi likelihood, and overdispersion in generalized linear
models.Amer.Statist.52222–227.
STATISTICSGROUP
COPENHAGENBUSINESSSCHOOL
SOLBJERGPLADS3
DK-2000FREDERIKSBERG
DENMARK
E-MAIL:tt.mes@cbs.dk
REJOINDER
BY PETER MCCULLAGH
UniversityofChicago
Jourdain: Andwhatarethey,thesethreeoperationsofthemind?
Philosopher: Thefirst,thesecondandthethird.
Thefirsttoconceivebymeansofpremises;
thesecondtoreasonbymeansofcategories;
andthethirdtodrawconclusionsbymeansoffigures.
Molière.Lebourgeoisgentilhomme.
Majorthemes. Thediscussantscoverawiderangeoftopics.Beforerespond-
ingindividually,Iwillfirstaddressafewofthemajorthemes.
Abstraction. Thepurposeofabstractionistoincorporateintothemathematics
thoseessentialrelationshipsthataretakenforgrantedinthedomainofapplication.
Yet that is seldom how it is seen from the outside. In my view, necessity is the
mother of abstraction, so there can be no virtue in abstractionfor its own sake.It
follows that this paper should not have been written had I not judged the need to
beclearandtheproposedsolutionreasonablycompelling.Unlesstheinformation

WHATISASTATISTICALMODEL? 1301
is suitably encoded, individual plots, pigs, varieties, treatments and subjects are,
in mathematical terms, simply elements in a set. We can, and we must, do better
thanthat.Aneighborrelationshiponagraphisapossiblestepinthisdirection,but
this paper pushes that idea a little further by expecting each object (graph) to be
embeddedinotherobjectsinsuchawaythatrelationshipsarepreserved.Manyof
thediscussantsareclearlymorecomfortablewithalgebraicabstractionthanIam,
others evidently less so. To those floating in the abstract wing it may appear that
my hesitant steps have not gone far enough. To others anchored in the concrete
it may appear that I have fallen into an abyss of mindless nonsense. The tension
between the concrete and the abstract is seldom comfortable, but I believe it is
healthy and central to the art of statistical modelling. One does not have to look
farin probability,statisticsorphysicstoseethattoday’sconcretefoundationsare
yesterday’sabstractions.Ontheotherhand,itmustruefullybeadmittedthatmost
ofyesterday’sabstractionsareburiedelsewhere.
Model versusanalysis. Statistical models are usually encounteredin connec-
tionwiththestatisticalanalysisofdata,andforthatreasonmanystatisticiansseem
toregardthemodelandtheanalysisasinextricablyintertwinedconcepts.Thesitu-
ationisquitedifferentinclassicalappliedmathematics,whereitisacceptedprac-
ticetodiscusspropertiesofthewaveequationorPoisson’sequationindependently
of any data that might (or might not) be collected. While it is difficult to discuss
statistical models without also mentioning analysis, it seems to me that the two
notionsarelogicallydistinct.AsIhaveusedthetermin thispaper,amodelisdi-
vorcedfromanyparticularareaofapplicationinmuchthesamewaythattheheat
equation is not necessarily tied to heat transmission. Although I do not recom-
mend the practice, one might talk of the Bradley–Terrymodel without indicating
whethertheintendedapplicationis tocompetitionexperimentsorcitationstudies
or transmission disequilibrium in genetics. In that sense, I am interested in what
Tjurcallscanonicalmodels.
An analysis might well involve the comparison of two or more mutually
incompatiblemodelsbymethodsthatrequirenumericalapproximationofintegrals
using MCMC. Model checking is an essential component of every analysis, and
thismightwellleadtotheconsiderationoffurthermodels.Ananalysisoffinancial
transaction data might well lead to the conclusion that Brownian motion is not
consistent with the data but that an alternative long-tailed model is satisfactory.
Thus, in any definition of the term “statistical model,” it is essential to bear in
mind that models must exist that are not compatible with any data likely to be
collected. By comparison with models, statistical analysis is a complicatedtopic,
and I have tried in the paper to say as little on the matter as I could hope to get
away with. As the title suggests, the topic of the paper is narrow. So far as I can
tell, it hasnothing to sayaboutcomputation,designor modelchecking,and very
littletosayaboutmodelselection,orBayesianversusfrequentistanalysis.

1302 REJOINDER
Prediction. Forpurposesofprediction,itisofteneffectivetouseonemodelin
oneregionandadifferentmodelinanotherregion.Onefamiliarexampleistheuse
ofquantummechanicsforatomic-scalecalculations,andNewtonianorrelativistic
mechanics at celestial scales. Despite its success in prediction, every physicist is
well aware that this patchwork does not constitute a single model. A black box
containingalistofrulesthatgiveeffectivepredictionsmaybeveryuseful,butthis
isnotamodelinthesensethatIusetheterm.
Extension and embedding. Self-consistencyforces the condition that P θ be
m
the marginal distribution of P θ whenever m is a subobject in n. Here m,n are
n
two sets of units, or more generally two designs, in which m is deemed to be an
embeddedsubdesignin n.TheonlyexceptionsIcanseeto thisconditioninvolve
systems in which the act of observation perturbs the system in an appreciable
manner, as in quantum-mechanical systems and possibly a few social science
applications. Julian Besag has hit the pig on the snout with his well-chosen
examplethatasubsetofalitterofpigsdoesnotconstitutealitter.Intheformalism
of the paper, this embedding must be coded in the category, so the category
includesasobjectsalllittersorsetsoflitters,butnotsublittersorsetsofsublitters.
This is not a problem, but it must be spelled out explicitly by the morphisms.
However,if the pigs were weaned,say6–12weeksold, it mightbe bestto takea
differentviewofthematter.Thechoiceofcategoryisessentialtoallthatfollows,
butcategorytheoryitselfhasnothingtosayonthematter.Morelikelythannot,the
choiceismadeongroundsofanimalhusbandryandstatisticaldesign.Inprinciple,
itissimplytheconsequencesofthischoicethatareexploredinthepaper.However,
the choice of category does have a constraining influence on the nature of the
inferencesthatcansubsequentlybedrawn.
Extrapolation. Onmacroscopicscalestheinversesquarelawforgravitational
or electrostatic forces is in good agreement with observation, but when extrapo-
lated to the atomic level it gives predictions in clear violation of everyday expe-
rience. I doubt that Newton ever intended that his law should be applied at the
angstromlevel,butatthe sametime Ido notviewit as“recklessto contemplate”
such extreme extrapolation. On the contrary, it was an essential step in the early
development of quantum mechanics. Julian Besag seems inclined to say that the
Newtonian model does not apply to atomic scales. In the sense that it does not
workwell,heiscorrect.Iaminclinedtosaythatthemodeldoesextendtoatomic
andsubatomicscalesandthatitpredictsacatastrophiccollapsethatdoesnotagree
withtheobservedfacts.Providedthatonedoesnotconfusemodelwithfact,there
is no contradiction in entertaining and comparing models whose consequences
may be absurd. To some extent, this difference in terminology is a matter of se-
mantics, but I think there is a little more to it than that. If the inverse square law
does not extend to atomic scales, I need to know where it stops and why it stops

WHATISASTATISTICALMODEL? 1303
there.Sofarasfertilizerlevelsinagriculturalexperimentsareconcerned,themod-
els are more mundane and more numerous but the principle is the same. The po-
tential to make falsifiable predictions is one of the properties that distinguishes a
modelfromanalgorithm.
Approximation. Approximationsofvarioussortsarehardtoavoidinstatistical
work. But an approximation must have a target; otherwise it might as well be
exact.Providedthereisatarget,Iseenoobjectioninprincipletoapproximations.
Besag makes the point that there exist “schemes” that are perfectly adequate in
practice as approximations to models, and I agree that the evidencesupports this
view. However, I do not agree that a statistical model, as a mathematical object,
is necessarily an approximation to anything, any more than a vector space or a
process is an approximation. In most applications several competing models vie
for supremacy. The hope is that one of these is an adequate description of the
observedfacts,butthedefinitiondoesnotdemandthisorguaranteeit.
Natural transformation. Natural transformations are more widespread in
statistical work than I have indicated in the paper. Consider, for example,
transformation of sample space(s) in the usual regression context. The condition
ofnaturalityamountstothestatementthattransformationg :Rn→Rn followed
n
by coordinate projection is the same as coordinate projection followed by
transformation g :Rn−1 → Rn−1. The conclusion might alarm coordinate-
n−1
free theorists, butcomesasno greatsurpriseto appliedstatisticians.Eachnatural
transformation is a scalartransformation g:R→R acting componentwise,such
as the link function in a generalized linear model. The only restriction is that
g should be measurable. Most linear transformations are not natural because the
componentsarenotpreserved.
For processes, the transformation W = N −1 on covariance matrices is not
natural because the inverse of the restriction is not the restriction of the
inverse. Within the class of stationary Markov processes, noncommutativity is
restricted to the boundary, so the transformation is “almost” natural. In that
sense,thesequenceofGaussianMarkovrandomfieldswithstationaryinteraction
coefficients W independent of the lattice size is an approximation to a process.
ij
This approximation may beperfectly adequatein practice,particularly if Besag’s
suggestionsforboundaryadjustmentsareincorporated.
Field trials. Julian Besag points out that the sole purpose of a variety trial
is the comparison of varieties, not the study of fertility patterns. I agree. Even
so, it is hard to see how anything useful can be said unless it is assumed that
variety effects are proportional to plot area, or, if defined in ratio form, that
variety effects are independent of plot area. Without admitting plots of various
sizes the proposition cannot be stated, so it cannot be a consequence of other
assumptions,suchasadditivityorlackofinterference,definedforplotsofstandard

1304 REJOINDER
size. One may be inclined to regard the proposition as an matter of established
agriculturalfact,somuchsothatitdoesnotcountasanassumption.Whatmakes
ittrue,agriculturallyspeaking,isthatagronomyknowssomethingaboutplotsand
varieties that mathematics does not. Agronomy knows that variety v planted in
a 2×2 plot is equivalent to the same variety planted in each of the individual
subplots. On the scale of scientific insights this revelation may achieve a record
low, but it not vacuous. First, it admits the existence of larger and smaller plots,
and their relation to one another by subset inclusion. Second, it says something
substantiveabouttherelationshipbetweenvarietiesandplotsthatistrue formost
agricultural treatments but is not true in general. Remember that mathematics
knows nothing about anything except mathematics, so mathematics must be
instructed in the facts of rural life. In the formalism of the present paper these
facts and relationships are encoded in the category and thereby made available
explicitly. It seems that everyone does this instinctively, much like Molière’s
M. Jourdain who was delighted to learn that he had been speaking prose all his
life.
Responses to individual discussants. Many of Julian Besag’s remarks are
concernedwith the more complicated subjectof statistical strategy, ranging from
model construction and statistical analysis to model adequacy and numerical
approximation.Idonotdisputetheimportanceorthesubtletyofstatisticalstrategy
and model construction,but I view it as complementaryto the topic of the paper.
Even if we cannot agree on a definition, or even the need for one, I welcome
Besag’sremarksconcerningtherelevanceofmodelsinapplications.Itisalsohard
todisagreeopenlywithhispreferenceformodelsthathaveaphysicaljustification,
orwhataresometimescalledmechanisticorcausalmodels.Whilethispreference
is understandable, it must be tempered with the knowledge that certain rather
successful models, such as Maxwell’s theory of electromagnetism, are hard to
justify on such grounds. The universality that I demand of a model is only the
universality that follows from the category of embeddings, and one can always
opt for a smaller category if this seems sensible. One interpretation of definition
[equation (1)] is that it states in an unfamiliar language only what is intuitively
obvious. Thus, Besag is entirely correct in his assertion that the commutativity
conditions amount to nothing more than common sense. But where I demand
internal consistency for a range of plot sizes, it seems that Besag attaches little
weight to this. Deep down, though, I’ll bet he must! Aside from this point, I aim
to show below that the extentof our disagreementis considerablyless than I had
originallythought.
I agree with essentially all of Peter Bickel’s remarks, including the plea for
expressingcategoricalideasinmoreacceptablelanguage.Inthelastsectionofhis
remarks, Tue Tjur goes some way in this direction, explaining what is meant by
anaturalparameterinregression.Theconnectionbetweennaturalparametersand
identifiable parameters is not an obvious one, so I wonder whether it is a lucky

WHATISASTATISTICALMODEL? 1305
coincidencethat β/σ in the Box–Cox model is both natural and also identifiable
inalargermodel.
A bushy category is evidence, if any were needed, of a novice gardener at
work, one who hasacquireda few sharp tools but notyetmasteredthe principles
of effective pruning. Brøns takes the formal definition, dissects it, extends it,
reassemblesitandreinterpretsitwithadexterityIcanadmirebutnotemulate.The
comma category StatMod is a very naturaland familiar statistical objectwith the
rightpropertiesandonlythoseproperties.Thenewproposal,todefineastatistical
model as a functor C →(id ↓P) from an arbitrary category C into StatMod,
set
achievesa degreeofsimplicity and generality through a new levelof abstraction.
Theparameterspaceandthesamplespaceremainaccessiblebycompositionwith
the natural projections, so nothing has been sacrificed. The pedagogical hurdles
remainformidable,butBrøns’sconstructionisrightonthemark,andIthankhim
forit.
One difficulty in constructing a general theory of models is to determine
where various conditions belong most naturally. In my view, no theory of linear
models can be considered satisfactory unless, to each subrepresentation (cid:1) (cid:5) ⊂(cid:1)
(cid:5)
there corresponds a quotient representation (cid:1)/(cid:1) in a natural way. This is not
a consequence of the extended definition, and is the reason for the additional
surjectivity condition that I had included. If this is unnecessary in the general
definition,Isuspectitmustbeapartofthedefinitionoflinearmodels.
Peter Huber is right to point out that, in some circumstances at least, what
appears to be absurd might well be real. After all, most of quantum mechanics
appears absurd and yet we must suppose it to be real. At some stage, one must
ask where the category comes from, and the answer here must depend on the
applicationinwaysthatarenoteasytodescribe.Averysparsecategorycontaining
manyobjectsbutfewmorphismsisnotveryuseful,buttheinclusionoftoomany
morphisms may lead to the exclusion of otherwise useful formulations. I was
fascinatedto readofHuber’searliercategorizationofaspectsofstatisticaltheory,
whichseemstobeconnectedwithmorphismsonthesampleside.
Inge Helland brings a fresh quantum-mechanical perspective to the subject,
and particularly to the matter of natural subparameters. I must confess that
I was initially skeptical of the restriction to natural subparameters when I first
encountered this in Helland (1999a), and I took an opposing view at the time,
but I have to agree now that the arguments are convincing. The arguments in
Fraser(1968b)areessentiallythesame.Itisinstructivetonotethattheobjections
raised in the paper to the correlation coefficient in regression do not apply to
autocorrelationcoefficientsintimeseriesorspatialprocesses.
Kalmanhasmuchtosayaboutmodelsandstatisticalpractice,allnegative.I’m
sure glad he’s not pinning the blame entirely on me! By the statement that there
doesnotexistaconcretei.i.d.processinnature,Ipresumethathemeansthatthis
mathematicalmodelis not a satisfactory descriptionof observedprocesses.If so,
weneedsomethingbetter,mostlikelyafamilyofnon-i.i.d.processes.

1306 REJOINDER
History offers ample support for Kalman’s assertion that scientists demand a
physical or mechanical explanation, in our case an explanation for the origin of
randomness in nature. But this demand does not persuade me that a mechanical
explanation should necessarily be forthcoming. The existence of the ether was
widely accepted in the nineteenth century, not for its beauty as Kalman claims,
but for its supposed mechanicalproperties which were deemed necessaryfor the
transmissionof light. In 1839,the currently acceptedmathematicalmodelfor the
transmission of light was put forward by James MacCullagh (no relation), but
rejected by physicists of the day because no mechanical explanation could be
provided. Although the date is given as 1842 and the name is misspelled, other
details provided by Feynman, Leighton and Sands [(1964) 2, Section 1–5] are
reliable.Twoquotesfromthe1839papersufficetoillustratemypoint.Concerning
the peculiar constitution of the ether, we know nothing and shall assume nothing
except what is involved in the foregoing assumptions (symmetry!). And later, by
wayofsummary,thereasoningwhichhasbeenusedtoaccountforthe[potential]
function is indirect, and cannot be regarded as sufficient in a mechanical point
of view. It is, however, the only kind of reasoning that we are able to employ, as
the constitution of the luminiferous ether is entirely unknown. Indeed it was, and
remainedsoformuchoftherestofthecentury,evenafterthesameequationswere
resurrected as one leg of Maxwell’s theory in 1864. Incidentally, the 1839 paper
maybethefirsttoemploythecombinationofpartialderivativesnowknownasthe
curl operator, andto showthat it transforms asa vectorundercoordinaterotation
inR3.
StevePincuspointsoutthattheinferentialformalismemphasizesprocessesand
familiesofprocessesratherthanfamiliesofdistributions.Thisistrue,buttosome
extent a matter of presentation. There is no objection in principle to considering
a truncated category containing a finite number of objects, such as the category
of injective maps on sets of size 12 and smaller. A process that is exchangeable
relativetothiscategoryisnotnecessarilyextendabletoaninfinitelyexchangeable
process,soinferencesextendingbeyond12elementsareinaccessible.Theabsence
of a metric may look odd, but we must bear in mind that each sample space
objectmustbeameasurespacewithanattachedσ-algebra,andpossiblyadditional
topological structure that I would rather not think about. One generic example is
thecategoryCinwhichtheobjectsarefinite-dimensionalinnerproductspacesand
themorphismsareinjectivelinearmapsϕ:X→X (cid:5) suchthat)ϕx,ϕy*=)x, y*.
IfS istheopposite,ordual,functorC→C,theobjectsareimplicitlyassumedto
be equipped with the usual Borel σ-algebra, and each ϕ is sent to the conjugate
lineartransformationϕ
∗
:X
(cid:5)→X.
These maps also preserveinner products, but in a different sense such that the
induced map (kerϕ ∗ ) ⊥ ∼ = X (cid:5) /kerϕ ∗ → X is an isomorphism of inner product
spaces.AprocessrelativetoC isnecessarilyorthogonallyinvariant,orspherically
symmetric, and is characterized by scale mixtures of normals [Kingman (1972)].

WHATISASTATISTICALMODEL? 1307
A similar characterization for symmetric and Hermitian matrix-valued processes
hasrecentlybeenobtainedbyWichura(2001).
Fraser and Reid ask whether category theory can do more than provide a
framework.MyexperiencehereissimilartoHuber’s,namelythatcategorytheory
is well suited for this purpose but, as a branch of logic, that is all we can expect
from it. Regarding the coefficient of variation, I agree that there are applications
inwhichthisisausefulandnaturalparameterorstatistic,justasthereare(afew)
applicationsin whichthecorrelation coefficientis useful.Thegroupsusedin this
paperaresuchthattheoriginiseitherfixedorcompletelyarbitrary. Ineithercase
there is no room for hedging. In practice, things are rarely so clear cut. In order
to justify the coefficientofvariation, it seemsto me thatthe applicationsmust be
such that the scale of measurement has a reasonably well-defined origin relevant
totheproblem.
The Cauchy model with the real fractional linear group was originally used
as an example to highlight certain inferential problems. I do not believe I have
encountered an application in which it would be easy to make a convincing case
for the relevance of this group. Nevertheless, I think it is helpful to study such
examples for the light they may shed on foundational matters. The fact that the
median is not a natural subparameter is an insight that casts serious doubt on
the relevance of the group in “conventional” applications. To turn the argument
around, the fact that the Cauchy model is closed under real fractional linear
transformation is not, in itself, an adequate reason to choose that group as the
basecategory.In that sense,I agree with a primary thesisof Fraser’s Structureof
Inferencethatthegroupsupersedestheprobabilitymodel.
Tjur’sremarkscapturethespiritofwhatIamattemptingtodo.Inthecumulative
logitmodel,itisclearintuitivelywhatismeantbythestatementthattheparameter
of interest should not depend on how the cutpoints are selected. As is often the
case, what is intuitively clear is not so easy to express in mathematical terms. It
doesnotmeanthatthemaximum-likelihoodestimateisunaffectedbythischoice.
Forthatreason,althoughTjur’s secondconditiononoverdispersionmodelshasa
certain appeal,I do notthink it carries the sameforce as the first. His description
ofnaturalsubparametersinregressionisamodelofclarity.
ConformalinvarianceandMarkovrandomfields. TueTjurremarksthatit
would be more convincing if I could produce an example of a new model using
category ideas.I agree, but this is not easy.It was in the hope of coming up with
something different that I sought to explore the consequencesfor spatial models
ofusingthe categoryofconformalmapsratherthanthemoreconventionalgroup
of rigid motions. Section 8 of the paper is a bit of a disappointment, at least if
judgedbythesuitabilityofthemodelsfortheirintendedapplication.Nevertheless,
it may yet be worth pursuing the same line of argument using the subcategoryof
invertibleconformalmapsonplanardomains.Forsimplicity ofexposition,I take
D =D (cid:5) to bethe Riemannsphere,ortheextendedcomplexplane.Thiscategory

| 1308 |     |     |     | REJOINDER |     |     |     |     |
| ---- | --- | --- | --- | --------- | --- | --- | --- | --- |
is a group in which each map is a fractional linear transformation of the form
ϕ:z(cid:17)→(az+b)/(cz+d) and inverse w (cid:17)→(dw−b)/(a −cw), with complex
suchthatad−bc(cid:18)=0.
coefficientsa,b,c,d
By the symbol Y ∼W is meant the planar Gaussian process with covariance
σ
| −σ2log|z−z |     | (cid:5)|. |     |     |     |     |     |     |
| ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
function The principal departure from Section 8, is that Y is a
function,notameasure.ForthemomentIpretendthatitisdefinedpointwise,and
(cid:5) =Y
the group acts by composition sending Y to Y ◦ϕ. The process is such that
pointwisedifferencesY(z )−Y(z )arezero-meanGaussianwithcovariances
|          |       |         | 1     | 2        |             |           |            |            |
| -------- | ----- | ------- | ----- | -------- | ----------- | --------- | ---------- | ---------- |
|          |       |         |       |          | (cid:17)    |           | (cid:17)   |            |
| (cid:11) |       |         |       | (cid:12) | (cid:17)(z  | −z )(z −z | )(cid:17)  |            |
|          | )−Y(z |         | )−Y(z | =σ2log   | (cid:17) 1  | 4 2       | 3 (cid:17) |            |
| cov Y(z  | 1     | 2 ),Y(z | 3     | 4 )      | (cid:17)    |           | (cid:17)   |            |
|          |       |         |       |          | (z          | −z )(z −z | )          |            |
|          |       |         |       |          | 1           | 3 2       | 4          |            |
|          |       |         |       |          | (cid:17)    |           |            | (cid:17)   |
|          |       |         |       |          | (cid:17)(ϕz | −ϕz       | −ϕz        | )(cid:17)  |
|          |       |         |       |          | (cid:17)    | 1 4 )(ϕz  | 2          | 3 (cid:17) |
|          |       |         |       | =σ2log   | (cid:17)    |           |            | (cid:17)   |
|          |       |         |       |          |             | −ϕz       | −ϕz        |            |
|          |       |         |       |          | (ϕz         | 1 3 )(ϕz  | 2          | 4 )        |
for each set of distinct points z 1 ,z 2 ,z 3 ,z 4 . The second line, which follows from
the invariance of the cross-ratio under fractional linear transformation, shows
(cid:5) ∼W
that the transformed process also satisfies Y . The fact that variances are
σ
infinite is not a problem in practice because of regularization. Each regularized
(cid:18)
|     |     |     |     |     |     |     |     | +−ρ − |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
observationisanintegratedcontrast,Y(ρ)= Y(z)dρ,inwhichρ =ρ is
asignedmeasuresuchthatρ(D)=0.Technically,Y
isdefinedasarandomlinear
| functionalontheL |     | -spaceofcontrastmeasuressuchthat |     |     |     |     |     |     |
| ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
2
(cid:16)
|     |     | |ρ|2 =− | log|z−w|dρ(z)dρ(w)<∞, |     |     |     |     |     |
| --- | --- | ------- | --------------------- | --- | --- | --- | --- | --- |
w
D2
whereaswhitenoiseisdefinedonthespacesuchthat
(cid:16)
|     |     | |ρ|2= | δ(z,w)dρ(z)dρ(w)<∞, |     |     |     |     |     |
| --- | --- | ----- | ------------------- | --- | --- | --- | --- | --- |
D2
where δ(z,w) is Dirac’s delta. Both are defined on the intersection, as are
|                                                    |     |      |     |     |     | −1,andY |     | (cid:5)  |
| -------------------------------------------------- | --- | ---- | --- | --- | --- | ------- | --- | -------- |
| convolutionsandmixtures.Thegroupelementϕsendsρtoρϕ |     |      |     |     |     |         |     | toY such |
| (cid:5)                                            |     | −1), |     |     |     | (cid:5) |     |          |
that Y (ρ)=Y(ρϕ with the same distribution Y ∼Y ∼W . This argument
σ
shows that logarithmic variograms are preserved under invertible conformal
maps.
Both white noiseand W are Markovrandomfields in the sensethat, for each
σ
closed contour, values in the interior and exterior are conditionally independent
given the values on the contour (Matheron, 1971). Both processes are also
conformal, but the similarity ends there. The set of conformal processes is also
closed under addition of independent processes. Thus, the sum of white noise
and W is conformal but not Markov. Beyond convolutions of white noise and
σ
W , it appears most unlikely that there exists another conformal process with
σ
Gaussianincrements.Whittle’s(1954)familyofstationaryGaussianprocesseshas
theMarkovproperty[ChilèsandDelfiner(1999)]butthefamilyisnotclosedunder
conformalmapsnorunderconvolution.

WHATISASTATISTICALMODEL? 1309
Ignoring variety effects, the Besag–Higdonmodel is a sum of white noise and
a Markov randomfield on the lattice. Besag’sremark that the variogram exhibits
logarithmic behavior suggests that the fitted MRF is close to W for some σ.
σ
This is certainly plausible since W is Markov and can be well approximated by
σ
a low-order lattice scheme, in which the MRF coefficients in the interior are an
approximation to the Laplacian. If this speculation is confirmed in applications,
thefittedmodelisapproximatelyasumofwhitenoiseandW ,whichisinfacta
σ
conformalprocess.In principle, the relation betweenthe MRF coefficientsand σ
(in W ) can be determined. Thus, if the fitted MRF is close to W , or even to a
σ σ
lineardeformationofW ,thefittedBesag–Higdonprocesshasanaturalextension
σ
beyondthe lattice to plots ofarbitrary sizeand shape,in which casemy criticism
onthesegroundsdoesnotapply.
At the time I wrote Section 8, I was aware of certain peculiarities of the
de Wijs process connected with its interpretation as the Newtonian potential,
or inverse of the Laplace operator. But I did not fully appreciate the Markov
property,andIwasunawareofitsconformalinvariance.Sothisrevelationcomes
as a pleasant surprise, and helps me to understand better the connection with
MRF lattice schemes in the analysis of field trials. With twenty years of first-
hand experience in farming I thought I understood the meaning of fertility, but
I knew of no plausible argument to suggest that fertility processes should be
spatially Markov, and I failed to see why this proposition should be so readily
accepted.Awiderangeofargumentssuggestedthatfertilitymightbeacompound
process or sum of elementary processes, indicating that a model, as a set of
processes, should be closed under convolution. From the present viewpoint of
conformal transformation, this mechanistic reasoning is replaced by an argument
of an entirely different sort in which the entire concept of fertility is absent. The
setofconformalGaussianprocessesisaconvexconeofdimensiontwogenerated
bywhitenoiseandW ,inessencetherandomeffectsmodelthatBesagsuggests.
σ
Although the Besag–Higdon scheme is not closed under convolution, all of the
conformal processes are already included at least as lattice approximations. It
would be good to have this important subset explicitly labelled. This analysis
suggests that two very different lines of argument may, in practice, lead to very
similarconclusions.
The application of conformal transformations to agricultural processes in
muddyfieldsmayseemfrivoloustothepointofabsurdity,butthatisnothowIsee
it. The driving thesis is that, whateverthe generating process,it shouldlook very
much the same after any transformation that preservesthe relevantaspects of the
geometry. Conformal maps preserve Euclidean geometry locally with no angular
distortion, which is the only argument for their relevance. However, Euclidean
geometry is only the visible side of a corn field. Specific nonisotropic effects
connectedwithtopography,ploughing,harvestinganddrainageareinevitableand
may even dominate the nonspecific variations. To the extent possible, these are
included in the category, and are carried along with the conformal maps. Even

1310 REJOINDER
with this adjustment, we should not delude ourselves by pretending that we have
learnedanythingaboutthelawsofbiologyoragriculturalsciencebystudyingthe
axiomsofalgebra.Tolearnthelawsofagriculture,wemuststudyagriculturaldata,
but it undoubtedly helps to do so in the light of potential models. The observed
logarithmic behavior of variograms suggests that some field processes have a
strong W component, consistent with conformal processes, but we should not
σ
besurprisedtofindadditionalcomponentsthatarenotconformal.
Acknowledgments. IwanttothankJohnMardenforarrangingthisdiscussion
paper and also the discussants for their remarks. My colleagues Michael Stein,
Steve Lalley, Norman Lebovitz, Steve Stigler and Sydney Webster have given
advicefreelyonarangeofpoints.ButIamespeciallyindebtedtoJulianBesagfor
hisgeneroushelpandforthrightremarks,whichhavehelpedtoclarifymythinking
onspatialprocessesandMarkovrandomfields.
REFERENCE
CHILÈS,J.-P.andDELFINER,P.(1999).Geostatistics.Wiley,NewYork.
FEYNMAN, R. P., LEIGHTON,R. B. and SANDS, M. (1964). TheFeynman LecturesonPhysics.
Addison-Wesley,Reading,MA.
FRASER,D.A.S.(1968b).TheStructureofInference.Wiley,NewYork.
HELLAND, I. S. (1999a). Quantum mechanicsfromsymmetryand statisticalmodelling. Internat.
J.Theoret.Phys.381851–1881.
KINGMAN,J.F.C.(1972).Onrandomsequenceswithsphericalsymmetry.Biometrika59492–494.
MACCULLAGH, J. (1839). An essay towards the dynamical theory of crystalline reflexion and
refraction.Trans.Roy.IrishAcademy2117–50.
MATHERON,G.(1971).Thetheoryofregionalizedvariablesanditsapplications.CahiersduCentre
deMorphologieMathématiquedeFontainbleu5.
WHITTLE,P.(1954).Onstationaryprocessesintheplane.Biometrika41434–449.
WICHURA,M.(2001).SomedeFinettitypetheorems.Preprint.
DEPARTMENTOFSTATISTICS
UNIVERSITYOFCHICAGO
5734UNIVERSITYAVENUE
CHICAGO,ILLINOIS60637-1514
E-MAIL:pmcc@galton.uchicago.edu