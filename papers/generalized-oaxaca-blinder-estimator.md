|                                            | The | Generalized |          | Oaxaca-Blinder |           |       | Estimator∗ |     |
| ------------------------------------------ | --- | ----------- | -------- | -------------- | --------- | ----- | ---------- | --- |
|                                            |     |             | Kevin    | Guo            | Guillaume | Basse |            |     |
|                                            |     |             | Stanford |                | Stanford  |       |            |     |
| 0202 rpA 42  ]TS.htam[  1v51611.4002:viXra |     |             |          | April          | 27, 2020  |       |            |     |
Abstract
After performing a randomized experiment, researchers often use ordinary-least
squares (OLS) regression to adjust for baseline covariates when estimating the average
treatment effect. It is widely known that the resulting confidence interval is valid
even if the linear model is misspecified. In this paper, we generalize that conclusion
to covariate adjustment with nonlinear models. We introduce an intuitive way to use
any “simple” nonlinear model to construct a covariate-adjusted confidence interval
for the average treatment effect. The confidence interval derives its validity from
randomizationalone,andwhennonlinearmodelsfitthedatabetterthanlinearmodels,
|     | it  | is narrower | than the usual | interval from | OLS adjustment. |     |     |     |
| --- | --- | ----------- | -------------- | ------------- | --------------- | --- | --- | --- |
KeyWords: Agnosticcovariateadjustment;Randomizationinference;NeymanModel.
1 Introduction
1.1 Motivation
In this paper, we study how covariates can be used to construct more precise estimates
of the sample average treatment in a completely randomized experiment. Our investigation
was inspired by Lin (Lin, 2013), who suggests performing covariate adjustment by simply
|     | fitting | an OLS | model with treatment-by-covariate |                   | interactions.   |         |     |     |
| --- | ------- | ------ | --------------------------------- | ----------------- | --------------- | ------- | --- | --- |
|     |         |        | Y =                               | µ+τZ +β(cid:62)(x | −x¯)+γ(cid:62)Z | (x −x¯) |     | (1) |
|     |         |        | i                                 | i                 | i               | i i     |     |     |
R
In the above display, Y ∈ is an outcome variable, Z ∈ {0,1} denotes the treatment
|     |     |     | i   |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rd
status of unit i (1 for “treatment”, 0 for “control”), and x ∈ is a vector of baseline
i
covariates. Remarkably, Lin showed that even if the model (1) is arbitrarily misspecified,
random assignment of Z is enough to justify standard inferences based on the regression
i
coefficient τˆ. This result is summarized (informally) in Theorem 1.
∗Email: gbasse@stanford.edu. We thank Avi Feller, Winston Lin, Peng Ding and the participants of
|     | the Berkeley | Causal | Group for helpful | comments. |     |     |     |     |
| --- | ------------ | ------ | ----------------- | --------- | --- | --- | --- | --- |
1

| Theorem |     | 1. (Lin’s | result, | informal) |     |     |
| ------- | --- | --------- | ------- | --------- | --- | --- |
Let n be the size of the treatment group, and let n be the size of the control group. If
|       | 1    |                  |         |     | 0   |     |
| ----- | ---- | ---------------- | ------- | --- | --- | --- |
| min(n | ,n ) | (cid:29) d, then | we have |     |     |     |
|       | 0 1  |                  |         |     |     |     |
√
|     |     |     |     | n(τˆ−τ) | ∼˙ N(0,σ2) | (2) |
| --- | --- | --- | --- | ------- | ---------- | --- |
where τ is the sample average treatment effect. Moreover, τˆ is at least as efficient as Ney-
man’s (Neyman, 1923) unadjusted difference-of-means estimator, and the usual confidence
interval for τ based on Huber-White “robust” standard errors is valid.
Unlike earlier work by Yang & Tsiatis (Yang and Tsiatis, 2001), Lin’s proof does not use
any probabilistic assumptions other than that the treatment assignments Z are assigned
i
completely at random. It applies even if the experimental units are not randomly sampled
from a larger population, which is the case in most social science experiments and clinical
trials (Abadie et al., 2020; Olsen et al., 2013; Rosenberger et al., 2019).
Theorem 1 has since been generalized to other experimental designs (Fogarty, 2018; Li
and Ding, 2020; Liu and Yang, 2019) and to high-dimensional linear regression (Bloniarz
et al., 2016). It is now widely known that covariate adjustment with linear models is never
“wrong” (at least when n (cid:29) d). However, that does not mean it is always “right.” For
example, when the outcome variable is binary, nonnegative, or highly skewed, one suspects
that it may be possible to further improve precision by using nonlinear models. There have
been various clever proposals for how this might be done, but none of them have all four of
| the | appealing      | properties | of  | Lin’s result: |     |     |
| --- | -------------- | ---------- | --- | ------------- | --- | --- |
|     | 1. Statistical | inference. |     |               |     |     |
The method produces a confidence interval with rigorous mathematical guarantees.
|     | 2. Robustness | to  | misspecification. |     |     |     |
| --- | ------------- | --- | ----------------- | --- | --- | --- |
The method does not require any specific assumptions about the relationship between
|     | covariates | and | outcomes | to be valid. |     |     |
| --- | ---------- | --- | -------- | ------------ | --- | --- |
3. Randomization-based.
The only probabilistic assumption is that treatment assignments Z are randomly as-
i
signed. Validity should not be compromised if the experimental units are not randomly
|     | sampled          | from | a larger    | population. |     |     |
| --- | ---------------- | ---- | ----------- | ----------- | --- | --- |
|     | 4. Computational |      | simplicity. |             |     |     |
The estimator can be computed by practitioners without extensive programming abil-
ity, using only functions that already exist in most statistical software packages.
Many proposals come close. Rosenbaum (Rosenbaum, 2002) suggests forming a confi-
dence interval by inverting a Fisher randomization test based on the residuals of an arbitrary
(possibly nonlinear) model; this satisfies 1, 3 and (arguably) 4, but the validity of the con-
fidence interval requires a constant additive treatment effect. The leave-one-out potential
outcomes method of Wu and Gagnon-Bartsch (2018) uses any regression model to construct
2

a randomization-unbiased estimate of τ, but it is not simple to implement1 and does not
come with a confidence interval. The literature on doubly-robust methods (Robins et al.,
1994; Kang and Schafer, 2007; Cao et al., 2009; Chernozhukov et al., 2018) is full of proposals
satisfying 1, 2, and 4, but their theoretical justifications always assume random sampling of
| experimental | units. |     |     |     |
| ------------ | ------ | --- | --- | --- |
The purpose of this paper is to introduce a general-purpose method for using any suf-
ficiently “simple” nonlinear regression model to perform covariate adjustment in a manner
that satisfies 1 – 4. Almost every widely-used parametric model is simple enough to work,
and so are some nonparametric models. As long as the chosen nonlinear models fit the
data better than linear models, then our confidence intervals are narrower than the robust
| standard | error confidence | interval | from OLS adjustment. |     |
| -------- | ---------------- | -------- | -------------------- | --- |
| 1.2 The  | potential        | outcomes | model                |     |
In this paper, we use the Neyman-Rubin potential outcomes model of causality (Neyman,
1923; Rubin, 1974). We consider a finite population of n experimental units, indexed by the
Rd
set I = {1,2,··· ,n}. Each experimental unit consists of a triple (y ,y ,x ), where x ∈
1i 0i i i
is a vector of covariates and y ,y are potential outcomes2. The goal is to estimate the
|     |     | 1i  | 0i  |     |
| --- | --- | --- | --- | --- |
1 (cid:80)n
| sample | average treatment | effect τ | = (y −y ). |     |
| ------ | ----------------- | -------- | ---------- | --- |
n i=1 1i 0i
We adopt the framework of randomization inference, which treats all of the quantities
{(y ,y ,x )}n as fixed constants (Bloniarz et al., 2016; Fogarty, 2018; Li and Ding, 2020;
| 1i 0i | i   |     |     |     |
| ----- | --- | --- | --- | --- |
i=1
Liu and Yang, 2019). The only randomness is in the treatment assignments (Z ,··· ,Z ) ∼
1 n
P , where P is the uniform distribution on length-n binary vectors v with ||v|| = n .
| n1,n | n1,n |     |     | 1 1 |
| ---- | ---- | --- | --- | --- |
The observed outcome is Y = Z y +(1−Z )y , and it is a random variable.
|                |        | i i            | 1i i 0i |     |
| -------------- | ------ | -------------- | ------- | --- |
| 2 Generalizing |        | Oaxaca-Blinder |         |     |
| 2.1 Beyond     | linear | adjustment     |         |     |
In order to motivate our procedure, we first present another way of looking at Lin’s
“interactions” estimator. Although the estimator is defined as a coefficient in a regression
model, that characterization of τˆ does not illuminate why it works. For example, it is not
obvious from that characterization that covariates must be centered – including dummy
variables coding categorical features – in order for τˆ to have model-free validity. Without
centering, the “interactions” estimator may be badly biased even in large samples.
The reason why centering is so important is that, if all covariates are centered, then
fitting the model (1) is equivalent to separately estimating two vectors of OLS coefficients:
ˆ ˆ
θ is estimated using only data from the treatment group, and θ is estimated using only
1 0
1An
R package exists, but implementing the method in STATA (for example) would still be challenging.
2Thistacitlyassumesthatthereisnointerferencebetweenexperimentalunits, e.g. thetreatmentassign-
| ment of unit | i does not affect | the outcome | of unit j if i(cid:54)=j. |     |
| ------------ | ----------------- | ----------- | ------------------------- | --- |
3

data from the control group. The estimator τˆ can be recovered from these two regressions
| by first imputing |     | the | unobserved | potential |     | outcomes, |     |     |     |     |     |
| ----------------- | --- | --- | ---------- | --------- | --- | --------- | --- | --- | --- | --- | --- |
(cid:26)
|     |     |     |     |     |     | y          | Z = t         |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --- | --- | --- |
|     |     |     |     | yˆ  | =   | ti         | i             |     |     |     | (3) |
|     |     |     |     |     | ti  | ˆ(cid:62)x |               |     |     |     |     |
|     |     |     |     |     |     | θ          | Z (cid:54)= t |     |     |     |     |
|     |     |     |     |     |     | t i        | i             |     |     |     |     |
and then computing τˆ = 1 (cid:80)n (yˆ −yˆ ). Since fitted values are not affected by centering,
|     |     |     |     | 1i  | 0i  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | n   | i=1 |     |     |     |     |     |     |     |
covariates can live on their original scale in these auxiliary regressions. In that sense, it is
more natural to think of Lin’s “interactions” estimator as an imputation estimator. This
viewpoint is also discussed by Ding (Ding and Li, 2018) and Chapter 7 of the textbook
by Imbens & Rubin (Imbens and Rubin, 2015). In econometrics, this double-imputation
procedure is known as the Oaxaca-Blinder3 method (Kline, 2011; Oaxaca, 1973; Blinder,
1973).
Thisperspectivesuggestsanaturalwayofusinganarbitraryregressionmodeltoestimate
ˆ(cid:62)x
the sample average treatment effect: simply replace θ in (3) with µˆ (x ), where µˆ is
|     |     |     |     |     |     |     | t   | i   | t   | i   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
estimated (using any method) on the subset of observations with Z = t, t ∈ {0,1}. We will
i
call this procedure the generalized Oaxaca-Blinder method – see Algorithm 1.
| Algorithm | 1   | The generalized |     | Oaxaca-Blinder |     |     | method |     |     |     |     |
| --------- | --- | --------------- | --- | -------------- | --- | --- | ------ | --- | --- | --- | --- |
)}n
| 1: Input. | Data | {(x | ,Y ,Z | .   |     |     |     |     |     |     |     |
| --------- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|           |      |     | i i i | i=1 |     |     |     |     |     |     |     |
Using data from treatment group, fit a regression model µˆ that predicts y using x .
| 2:  |     |     |     |     |     |     |     | 1   |     | 1i  | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Use the model µˆ to “ fill in” the unobserved values of y using (4).
| 3:  |     | 1   |     |     |     |     |     | 1i  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:26)
|     |     |     |     |     |     | y     | Z =   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
|     |     |     |     | yˆ  | =   | 1i    | i     |     |     |     | (4) |
|     |     |     |     |     | 1i  | µˆ (x | ) Z = | 0   |     |     |     |
|     |     |     |     |     |     | 1     | i i   |     |     |     |     |
4: Using data from control group, fit a regression model µˆ that predicts y using x .
|     |           |     |          |         |            |     |        | 0      |     | 0i  | i   |
| --- | --------- | --- | -------- | ------- | ---------- | --- | ------ | ------ | --- | --- | --- |
| Use | the model | µˆ  | to “fill | in” the | unobserved |     | values | of y . |     |     |     |
| 5:  |           | 0   |          |         |            |     |        | 0i     |     |     |     |
(cid:26)
|     |     |     |     |     |     | µˆ (x | ) Z = | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
|     |     |     |     | yˆ  | =   | 0     | i i   |     |     |     | (5) |
|     |     |     |     |     | 0i  | y     | Z =   | 0   |     |     |     |
|     |     |     |     |     |     | 0i    | i     |     |     |     |     |
(cid:80)n
| 6: Return | τˆ  | := 1 | (yˆ    | −yˆ ). |     |     |     |     |     |     |     |
| --------- | --- | ---- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
|           |     | n    | i=1 1i | 0i     |     |     |     |     |     |     |     |
Thisprocedureissosimplethatithasbeenproposed(inoneformoranother)manytimes
in different communities. Education researchers have known about this idea since Peters
(1941) (Peters, 1941), and it has since appeared in applied statistics (Belson, 1956; Hansen
and Bowers, 2009), survey sampling (Firth and Bennett, 1998; S¨arndal and Wright, 1984),
epidemiology (Westreich et al., 2015), and economics (Kline, 2011; Oaxaca, 1973; Blinder,
3Although
the “interactions” estimator is algebraically equivalent to the Oaxaca-Blinder estimator, Lin
(2013) derives its asymptotic properties in a randomization-based framework – quite distinct from the infer-
| ential framework |     | adopted | in the | econometrics | literature. |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------ | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
4

1973; Fairlie, 1999; Bauer and Sinning, 2008). Its theoretical properties are studied4 for
certain choices of µˆ , µˆ in Rosenblum & van der Laan (Rosenblum and van der Laan, 2009)
0 1
and Bartlett (Bartlett, 2018), but under the assumption that experimental units are sampled
randomlyfromahypotheticalsuperpopulation. Withoutthatassumption, theoreticalresults
have only been established in the special case where µˆ and µˆ are linear or logistic models
|             |            |     |              |        |     |         |        | 1   | 0   |     |     |     |
| ----------- | ---------- | --- | ------------ | ------ | --- | ------- | ------ | --- | --- | --- | --- | --- |
| (Lin, 2013; | Freedman,  |     | 2008c;       | Hansen | and | Bowers, | 2009). |     |     |     |     |     |
| 2.2         | Prediction |     | unbiasedness |        |     |         |        |     |     |     |     |     |
Although any regression model can, in principle, be plugged into Algorithm 1, not every
regression model will result in an estimator that is robust to misspecification. The key
property that is required of such a model is prediction unbiasedness.
| Definition | 1.  | (Prediction |     | unbiasedness) |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
For t ∈ {0,1}, we say that the regression model µˆ is prediction unbiased if (6) holds with
t
| probability | one. |     |     |     |          |         |      |          |     |     |     |     |
| ----------- | ---- | --- | --- | --- | -------- | ------- | ---- | -------- | --- | --- | --- | --- |
|             |      |     |     | 1   | (cid:88) |         | 1    | (cid:88) |     |     |     |     |
|             |      |     |     |     |          | µˆ (x ) | =    | y        |     |     |     | (6) |
|             |      |     |     |     |          | t i     |      | ti       |     |     |     |     |
|             |      |     |     | n   |          |         | n    |          |     |     |     |     |
|             |      |     |     |     | t        |         | t    |          |     |     |     |     |
|             |      |     |     |     | Zi=t     |         | Zi=t |          |     |     |     |     |
In words, a regression model is prediction unbiased if the average prediction on the
training data always exactly matches the average outcome in the training data. In survey
| sampling, | this | condition | is  | called “calibration.” |     |     |     |     |     |     |     |     |
| --------- | ---- | --------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
unbiased5.
Many widely-used regression models are automatically prediction For ex-
ample, the first-order conditions of a canonical-link GLM imply (6), so linear regression,
logistic regression, and Poisson regression are prediction unbiased. Given an arbitrary pre-
diction model µˆ , it is always possible to construct a related model µˆdb which is prediction
|          |           | 1           |     |         |           |           |          |       |      | 1   |     |     |
| -------- | --------- | ----------- | --- | ------- | --------- | --------- | -------- | ----- | ---- | --- | --- | --- |
| unbiased | by simply | subtracting |     | off     | the       | estimated | bias     | as in | (7). |     |     |     |
|          |           |             |     |         |           | 1         | (cid:88) |       |      |     |     |     |
|          |           |             |     | µˆdb(x) | = µˆ (x)− |           | (µˆ      | (x)−y | )    |     |     | (7) |
|          |           |             |     |         | 1         |           |          | 1     | 1i   |     |     |     |
|          |           |             |     | 1       |           | n         |          |       |      |     |     |     |
1
Zi=1
|     |     |     |     |     |     | (cid:124) |     | (cid:123)(cid:122) | (cid:125) |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------------ | --------- | --- | --- | --- |
estimatedbias
Another possibility is to use the fitted values µˆ (x ) as a covariate in an OLS regression
|     |     |     |     |     |     |     | 1   | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as in (8). The first order condition characterizing β ˆ in the least-squares problem guarantees
0
| that µˆols2 | will also | be  | prediction | unbiased. |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     | µols2(x) |     | ˆ ˆ |         | ˆ   | ˆ      |         | (cid:88) |      |       | )])2 |     |
| --- | -------- | --- | --- | ------- | --- | ------ | ------- | -------- | ---- | ----- | ---- | --- |
|     |          | = β | +β  | µˆ (x), | (β  | ,β ) = | argmin  | (y       | −[β  | +β µˆ | (x   | (8) |
|     | 1        |     | 0   | 1 1     | 0   | 1      |         |          | 1i 0 | 1     | 1 i  |     |
|     |          |     |     |         |     |        | (β0,β1) | Zi=1     |      |       |      |     |
4Theseworksstudyaslightvariantwhereonlyonemodelisestimated(usingallthedata),butitcontains
Z as a covariate.
5Such estimators are called “internally bias calibrated” by Firth & Bennett (Firth and Bennett, 1998).
5

In view of these simple adjustments, prediction unbiasedness does not seriously restrict
the class of permissible nonlinear models. That being said, certain desirable features of µˆ
1
may not be present in µˆdb or µˆols2, e.g. respecting the binary nature of the outcome variable.
1 1
When the debiasing trick (7) is used, the generalized Oaxaca-Blinder estimator is alge-
braically equivalent to the the augmented inverse-propensity weighted (AIPW) treatment
effect estimator with known (and constant) treatment propensity (see Glynn and Quinn
(2010) for an overview). In the survey sampling literature, that estimator is known as the
generalized difference estimator (Cassel et al., 1976; Breidt and Opsomer, 2017). The idea
of using fitted values in an OLS regression has also appeared before in the survey sampling
community, under the name “model calibration estimator” (Wu and Sitter, 2001). Although
those connections are mathematically fruitful, we believe that the formulation we present
(“estimate τ by filling in missing values with unbiased prediction models”) is much more
intuitive in the context of completely randomized experiments.
2.3 Statistical inference
Under some additional constraints on the regression models µˆ and µˆ (to be discussed
1 0
in Section 3), the confidence interval (9) has large-sample validity.
(cid:115)
(cid:91) (cid:91)
MSE(1) MSE(0)
τˆ±z + (9)
1−α/2
n n
1 0
In the above display, M (cid:91) SE(t) = 1 (cid:80) [y −µˆ (x )]2 is an estimate of the mean-squared
nt−1 Zi=t ti t i
error of the prediction model µˆ . The form of the confidence interval (9) has some intuitive
t
appeal: when more accurate models are used to “fill in” the missing values, the resulting
estimator τˆ is more precise.
When the regression models are constant (i.e. µˆ (x) ≡ 1 (cid:80) y ), we recover the con-
t nt Zi=t ti
fidence interval suggested by Neyman (Neyman, 1923) for the difference-of-means estimator.
The robust standard error confidence interval based on Lin’s “interactions” estimator is –
in large samples – statistically equivalent to the interval (9) when both regression models
are linear models. Therefore, when nonlinear regression models fit the data better than
linear models, the interval (9) is shorter than the “robust” standard error interval from OLS
adjustment.
2.4 An illustration
Before going into theoretical details, we briefly illustrate the computational and numer-
ical properties of the generalized Oaxaca-Blinder estimator with a simple example. The
Fatalities dataset in R was introduced by Ruhm (Ruhm, 1995), and contains the number
of traffic fatalities in each continental US state between 1982 and 1988 along with a few
covariates. To study the effect of a (fictional) randomized intervention designed to reduce
traffic fatalities, Lin’s “interactions” estimator is a natural baseline. However, statistical
6

intuition suggests that Poisson models might fit better, since the outcome variable counts
| the occurrences | of a | rare event. |     |     |     |     |     |
| --------------- | ---- | ----------- | --- | --- | --- | --- | --- |
ComputingthegeneralizedOaxaca-BlinderbasedonPoissonregressionanditsassociated
confidence interval using Algorithm 1 and formula (9) is not too difficult, but there are two
observations that can make it even simpler. First, for prediction unbiased regression models
(like Poisson regression), the right-hand side of the identity (10) is often easier to work with6.
|     |     |      | n          | n          |             |       |      |
| --- | --- | ---- | ---------- | ---------- | ----------- | ----- | ---- |
|     |     |      | 1 (cid:88) | 1 (cid:88) |             |       |      |
|     |     | τˆ = | (yˆ −yˆ    | ) =        | [µˆ (x )−µˆ | (x )] | (10) |
|     |     |      | 1i         | 0i         | 1 i         | 0 i   |      |
|     |     |      | n          | n          |             |       |      |
|     |     |      | i=1        | i=1        |             |       |      |
Second, the interval (9) can be computed by simply adding τˆ to the endpoints of the
t-test7
confidence interval from a two-sample on the residuals of µˆ and µˆ . Using these two
0 1
computational shortcuts, the estimator and it’s confidence interval can be computed in only
| four lines | of code. |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- |
R
| mu1 = glm(Y | ~ .-Z, | family=poisson, |     | subset(data, | Z==1)) |     |     |
| ----------- | ------ | --------------- | --- | ------------ | ------ | --- | --- |
| mu0 = glm(Y | ~ .-Z, | family=poisson, |     | subset(data, | Z==0)) |     |     |
tau.hat = mean(predict(mu1, data, "r") - predict(mu0, data, "r"))
tau.hat + t.test(residuals(mu1, "r"), residuals(mu0, "r"))$conf.int
For comparison, computing Lin’s “interactions” estimator in R requires roughly the same
amount of code, at least when the features include at least one factor variable. In fact, it
may be easier for some users to use this method to compute τˆ even when µˆ and µˆ are
1 0
linear models, because centering factors in STATA/SAS/Excel is nonstandard.
We ran the above code 50,000 times on the dataset, rerandomizing the
Fatalities
treatment assignments (Z ,··· ,Z ) in each replication. Each time, we also computed the
|     |     | 1   | 336 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
robust standard error confidence interval based on Lin’s “interactions” estimator. Figure 1
plots the randomization distributions of these two estimators. Two features are immediately
clear: (i) both estimators have an approximately normal randomization distribution; (ii)
the Poisson regression generalized Oaxaca-Blinder estimator is much more efficient than the
| “interactions” | estimator. |     |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- | --- |
This efficiency gain is also reflected in the width of the associated confidence intervals:
95% confidence intervals based on Poisson imputation were about 45% shorter (on average)
than the robust standard error confidence intervals8 based on Lin’s “interactions” estimator.
| Both confidence | intervals | had | approximately | nominal | coverage. |     |     |
| --------------- | --------- | --- | ------------- | ------- | --------- | --- | --- |
6The right-hand side of (10) is reminiscent of a “marginal effects” calculation, and of the “g-formula”.
We have not pursued that connection because the interpretation does not make sense in the randomization
model.
7This changes the normal quantile z to a t-quantile, which we recommend.
1−α/2
8We
used the “HC3” version of the robust standard errors. The “HC0” standard errors studied in Lin
| (2013) did | not have good | coverage | properties | in this example. |     |     |     |
| ---------- | ------------- | -------- | ---------- | ---------------- | --- | --- | --- |
7

|     |     |     | Poisson |     | OLS |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
0.020
0.015
ytisneD
0.010
0.005
0.000
|     |     | −100 −50 | 0 50 | 100 | −100 −50 0 | 50 100 |     |
| --- | --- | -------- | ---- | --- | ---------- | ------ | --- |
Estimated Treatment Effect
Figure 1: The randomization distribution of the Poisson regression generalized Oaxaca-
Blinder estimator (left) and Lin’s “interactions” estimator (right), estimated over 50,000
randomizations. The experimental design is completely randomized, with half of all state
× year pairings receiving the “treatment” in each randomization. Both models control for
state population, average miles per driver, and per capita income. In the Poisson model,
| covariates    | are log-transformed. |         |     |     |     |     |     |
| ------------- | -------------------- | ------- | --- | --- | --- | --- | --- |
| 3 Theoretical |                      | results |     |     |     |     |     |
In this section, we state our main theoretical results concerning the consistency and
asymptotic normality of generalized Oaxaca-Blinder estimators. The assumptions in this
section are deliberately high-level, since the results are intended to cover a wide variety
of examples. More low-level assumptions are used to specialize these results to specific
| regression | methods | in Section | 4.  |     |     |     |     |
| ---------- | ------- | ---------- | --- | --- | --- | --- | --- |
Like the results of prior work on covariate adjustment with linear models (Bloniarz
et al., 2016; Fogarty, 2018; Freedman, 2008a,b; Li and Ding, 2020; Lin, 2013; Liu and Yang,
2019), our theoretical guarantees are asymptotic. In Neyman’s finite-population model,
this means triangular-array asymptotics with respect to a sequence of finite populations
Π = {(y ,y ,x )}n of increasing size, each with its own completely randomized ex-
| n   | 1i,n 0i,n | i,n i=1 |     |     |             |     |     |
| --- | --------- | ------- | --- | --- | ----------- | --- | --- |
|     |           | P       |     |     | 1 (cid:80)n |     |     |
periment(Z ,··· ,Z ) ∼ andtreatmenteffectτ = (y −y ). Wefocuson
|     | 1,n | n,n | n1,n |     | n n i=1 | 1i,n 0i,n |     |
| --- | --- | --- | ---- | --- | ------- | --------- | --- |
the low-dimensional regime where d stays fixed as n grows. Although we do not assume that
these experiments are related in any way, we will assume in what follows that the fraction
of treated units p = n /n satisfies 0 < p ≤ p ≤ p < 1 for some bounds p ,p
|         |          | n 1,n   |     | min n | max |     | min max |
| ------- | -------- | ------- | --- | ----- | --- | --- | ------- |
| that do | not vary | with n. |     |       |     |     |         |
Some remarks on notation: for simplicity, we will often drop the n-subscript on various
quantities, e.g. we will write x in place of x . For two symmetric matrices A,B ∈ Rd×d,
|     |     |     | i   | i,n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Rd R,
we will write A (cid:23) B if A−B is positive semidefinite. For any functions f,g : → we
(1 (cid:80)n
| define | ||f −g|| | = [f(x | )−g(x | )]2)1/2. |     |     |     |
| ------ | -------- | ------ | ----- | -------- | --- | --- | --- |
|        | n        | n i=1  | i,n   | i,n      |     |     |     |
8

3.1 Consistency
Under very weak conditions, generalized Oaxaca-Blinder estimators based on prediction-
unbiased regression models are consistent. To build some intuition for why this is true,
consider the Poisson regression example presented in Section 2.4. The regression models are
|        |      |        |         | ˆ(cid:62)x), |       | ˆ   |              |     |     |     |     |
| ------ | ---- | ------ | ------- | ------------ | ----- | --- | ------------ | --- | --- | --- | --- |
| of the | form | µˆ (x) | = exp(θ |              | where | θ   | solves (11). |     |     |     |     |
|        |      | t      |         | t            |       | t   |              |     |     |     |     |
(cid:88)
|     |     |     |     |     | ˆ        |     | x(cid:62)θ+exp(θ(cid:62)x |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | ------------------------- | --- | --- | --- | ---- |
|     |     |     |     | θ   | = argmin |     | [−y                       |     | )]  |     | (11) |
|     |     |     |     |     | t        |     | ti i                      |     | i   |     |      |
θ∈Rd
Zi=t
Since the subset of observations with Z = t is a random sample of all the experimental units,
i
we would expect that θ ˆ is close to the solution of the population version of the problem (11),
t
where the sum is taken over all i instead of only those with Z = t. Let θ∗ be the solution
|     |     |     |     |     |     |     |     |     | i   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of the “population” problem. When the covariates x include an intercept, the first-order
i
| condition |     | characterizing |     | θ∗  | implies | (12). |     |     |     |     |     |
| --------- | --- | -------------- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- |
t
|            |     |          |                 |          | 1        | n               | 1        | n        |     |     |      |
| ---------- | --- | -------- | --------------- | -------- | -------- | --------------- | -------- | -------- | --- | --- | ---- |
|            |     |          |                 |          |          | (cid:88)        |          | (cid:88) |     |     |      |
|            |     |          |                 |          |          | exp(θ∗(cid:62)x | ) =      | y        |     |     | (12) |
|            |     |          |                 |          |          |                 | t i      | ti       |     |     |      |
|            |     |          |                 |          | n        |                 | n        |          |     |     |      |
|            |     |          |                 |          |          | i=1             |          | i=1      |     |     |      |
| Therefore, |     | we could | (heuristically) |          |          | argue:          |          |          |     |     |      |
|            |     | n        |                 | (cid:32) |          |                 | (cid:33) |          |     |     |      |
|            | 1   | (cid:88) | 1               | (cid:88) | (cid:88) |                 |          |          |     |     |      |
ˆ(cid:62)x
|     |     | yˆ  | =   | y        | +            | exp(θ | )        |     |     |     |     |
| --- | --- | --- | --- | -------- | ------------ | ----- | -------- | --- | --- | --- | --- |
|     | n   | ti  | n   |          | ti           |       | t i      |     |     |     |     |
|     |     | i=1 |     | Zi=t     | Zi(cid:54)=t |       |          |     |     |     |     |
|     |     |     |     | (cid:32) |              |       | (cid:33) |     |     |     |     |
1
|     |     |     |     | (cid:88) | ˆ(cid:62)x |     | (cid:88) ˆ(cid:62)x |     |             |           |     |
| --- | --- | --- | --- | -------- | ---------- | --- | ------------------- | --- | ----------- | --------- | --- |
|     |     |     | =   | exp(θ    |            | )+  | exp(θ )             |     | (Prediction | unbiased) |     |
|     |     |     |     |          | t          | i   | t i                 |     |             |           |     |
n
|     |     |     |     | Zi=t |     |     | Zi(cid:54)=t |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ------------ | --- | --- | --- | --- |
n
1 (cid:88)
|     |     |     | ≈   | exp(θ∗(cid:62)x |     | )   |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |                 | t   | i   |     |     |     |     |     |
n
i=1
|     |     |     | 1   | n   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     |     | =   | y   |     |     |     |     |     | (By (12)) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
ti
n
i=1
Since this argument works for both t = 0 and t = 1, we have τˆ = 1 (cid:80)n (yˆ − yˆ ) ≈
|     |     |     |     |     |     |     |     |     |     | 1i  | 0i  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n i=1
| 1 (cid:80)n | (y  | −y  | ) = τ. |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1i 0i
n i=1
This simple argument is well-known in the survey sampling community (see Firth and
Bennett (1998); S¨arndal and Wright (1984); Kang and Schafer (2007)), and it is the main
idea behind Freedman’s consistency result for logistic regression (Freedman, 2008b). It is
almost completely rigorous. The only step that needs to be justified is the claim that
ˆ(cid:62)x
exp(θ ) ≈ exp(θ∗(cid:62)x) (at least on average). A sufficient9 condition to make this argument
|          | t i |            | t   |     |     |     |     |     |     |     |     |
| -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rigorous | is  | stability. |     |     |     |     |     |     |     |     |     |
9This condition is not necessary for consistency, but it plays a key role in our later results on asymptotic
normality.
9

| Definition |     | 2.  | (Stability) |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We say that a sequence of random functions {µˆ } is stable if (13) holds for some deter-
|     |     |     |     |     |     |     |     | n n≥1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
{µ∗}
| ministic |     | sequence | of  | functions |     |     | .   |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n n≥1
|     |     |     |     |     |     | (cid:32) |     |     |     | (cid:33)1/2 |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ----------- | --- | --- | --- |
n
1 (cid:88)
|     |     |     |      | −µ∗|| |     |     |     | )−µ∗(x |     | )]2 | p    |     |      |
| --- | --- | --- | ---- | ----- | --- | --- | --- | ------ | --- | --- | ---- | --- | ---- |
|     |     |     | ||µˆ |       | :=  |     | [µˆ | (x     |     |     | →− 0 |     | (13) |
|     |     |     |      | n n   | n   | n   |     | n i,n  | n   | i,n |      |     |      |
i=1
The deterministic sequence in the definition of stability is not uniquely determined, but
there is usually a natural choice. For example, if µˆ = µ is a parametric regression model
|     |     |     |     |     |     |     |     | n   |     | θˆ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | n   | µ∗  |     |     |
estimated via maximum likelihood or empirical risk minimization, = µ is the clear
|     |     |     |     |     |     |     |     |     |     |     | n   | θ n ∗ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
µ∗
candidate. For this reason, we will typically call “the” population regression function,
n
even without specifying exactly which choice of µ∗ we are making.
n
Perhaps surprisingly, the definition of stability does not assume that the deterministic
sequence {µ∗} satisfies a property like (12). It turns out that if {µˆ } is both pre-
|     |     | n   | n≥1 |     |     |     |     |     |     |     |     | 1,n n≥1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
diction unbiased and stable, then we may always choose the sequence {µ∗ } to satisfy
|           |     |     |     |           |     |     |     |     |     |     |     | 1,n n≥1 |     |
| --------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| (cid:80)n |     |     |     | (cid:80)n |     |     |     |     |     |     |     |         |     |
1 µ∗ (x ) = 1 y . Therefore, prediction unbiasedness and stability are sufficient
| n   | i=1 | 1,n i | n   | i=1 1i |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to carry through the heuristic argument from above – Theorem 2 gives a formal statement.
| Theorem |     | 2. (Consistency) |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let {µˆ } and {µˆ } be two stable sequences of prediction-unbiased models, and let
|     | 1,n | n≥1 |     | 0,n n≥1 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{τˆ } be the resulting sequence of generalized Oaxaca-Blinder estimators. For t ∈ {0,1},
n n≥1
| let | MSE | (t) be | defined | by (14). |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
n
1 (cid:88)
|     |     |     |     |     |     |        |     | [µ∗ |     | ]2   |     |     |      |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- | --- | --- | ---- |
|     |     |     |     |     | MSE | (t) := |     | (x  | )−y |      |     |     | (14) |
|     |     |     |     |     | n   |        | n   | t,n | i,n | ti,n |     |     |      |
i=1
| If MSE | (1) | = o(n) | and | MSE | (0) | = o(n), | then | (τˆ −τ | ) →− p | 0.  |     |     |     |
| ------ | --- | ------ | --- | --- | --- | ------- | ---- | ------ | ------ | --- | --- | --- | --- |
|        | n   |        |     |     | n   |         |      | n      | n      |     |     |     |     |
Note that Theorem 2 does not depend on the specific choice of the sequences {µ∗ }
n≥1
1,n
and {µ∗ } . As long as any nonrandom sequence {µ∗ } satisfying ||µˆ −µ∗ || → 0
|     | 0,n | n≥1 |     |     |     |     |     |     | t,n | n≥1 |     | t,n t,n | n p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
has MSE (t) = o(n), then all such sequences will have that property. In most cases, the
n
mean-squared error of even a grossly misspecified model is not diverging at all, so we would
have MSE (1) = O(1), MSE (0) = O(1). We have used the weaker assumption in Theorem
|        |     | n   |         |             | n   |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 only | for | the | sake of | generality. |     |     |     |     |     |     |     |     |     |
Proving that a sequence of random functions {µˆ } is stable is typically an exercise in
n n≥1
translating some standard arguments from the theory of M-estimation into the language of
finite populations. This may or may not be simple, depending on the regression function.
In Section 4, we give a few examples of widely-used regression methods where this can be
done,includinglogisticregression,Poissonregression,andOLSregressionwithatransformed
outcome variable. In Section 5, we outline a general strategy that works for a large class of
smoothparametricmodels. Theargumentisespeciallysimpleinthecaseoflinearregression,
| so we | present | it  | as an | example. |     |     |     |     |     |     |     |     |     |
| ----- | ------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10

Example 1. (OLS is stable)
Let µˆ (x) = β ˆ(cid:62) x, where β ˆ = argmin (cid:80) (y −x(cid:62) β)2. Assume that 1 (cid:80)n ||x ||4 =
o(n), 1 1 ,n (cid:80)n y4 1, = n o(n), and 1 1 (cid:80)n (y ,x ) Z ( i y =1 ,x 1i ) ,n (cid:62) con i v ,n ergestoaninvertibl n ema i= tr 1 ix. i Then
n i=1 1i n i=1 1i i 1i i
{µˆ } is a stable sequence.
1,n n≥1
Proof. We can write β ˆ = ( 1 (cid:80) x x(cid:62))−1( 1 (cid:80) x(cid:62)y ). Let Σ be the limit of
1 (cid:80)n x x(cid:62) and Σ b 1 e ,n the l n im 1 it Z o i f =1 1 (cid:80) i n i x y n1 . B Z y i= t 1 he i co 1i mpletely r x a x ndomized law of
n i=1 i i xy n i=1 i 1i
large numbers10 and the continuous mapping theorem, β ˆ →− p β∗ = Σ−1Σ . If we set
1,n 1 xx xy
µ∗ (x) ≡ β∗(cid:62)x, we may write:
1,n 1
n
||µˆ −µ∗ ||2 = 1 (cid:88) [(β ˆ −β∗)(cid:62)x ]2 ≤ Tr(Σ )||β ˆ −β∗||2 →− p 0
1,n 1,n n n 1,n 1 i n 1,n 1
i=1
Thus, {µˆ } is stable.
1,n n≥1
3.2 Asymptotic normality
In order prove the asymptotic normality of generalized Oaxaca-Blinder estimators, we
require that the regression functions µˆ and µˆ satisfy one additional property, which we call
1 0
typically simple realizations. The role of this assumption is to give more precise control on
the errors that are incurred in the approximation 1 (cid:80)n µˆ (x ) ≈ 1 (cid:80)n µ∗(x ).
n i=1 1 i n i=1 1 i
Definition 3. (Typically simple realizations)
We say that a sequence of random functions {µˆ } has typically simple realizations there
n n≥1
exists a sequence of function classes {F } such that P (µˆ ∈ F ) → 1 and (15) holds.
n n≥1 n1,n n n
(cid:90) 1
(cid:112)
sup logN(F ,||·|| ,s)ds < ∞ (15)
n n
0 n≥1
In the above display, N(F ,|| · || ,s) denotes the s-covering number11 of the metric space
n n
(F ,||·|| ).
n n
The integral in (15) measures the “complexity” of the possible realizations of µˆ . In plain
n
language, µˆ has typically simple realizations if it usually falls in a set with small complexity.
The integral (15) is essentially the uniform entropy integral from classical empirical process
theory, but the function class F is allowed to change with n and the supremum is only
n
over distributions of the form 1 (cid:80)n δ . As a result, the conditions needed for “typically
n i=1 xi,n
simple realizations” are a bit weaker than the conditions used to prove the triangular-array
Donsker property (see Theorems 2.8.9 in van der Vaart and Wellner (1996) for details). For
example, marginal asymptotic normality (which requires n /n → p for some limit p) is not
1
needed.
Although Definition 3 is a somewhat technical definition, it can be fairly easy to check.
For illustration, we show how it can be established in the case of OLS regression.
10See Lemma 2 in the appendix.
11Thes-coveringnumberofametricspace(T,d)isthesizeofthesmallestcollectionofpoints{t ,··· ,t }
1 N
with the property that every point in T is within distance s of one of the t ’s.
i
11

| Example |     | 2. (OLS | has | typically |     | simple | realizations). |     |     |     |     |     |
| ------- | --- | ------- | --- | --------- | --- | ------ | -------------- | --- | --- | --- | --- | --- |
ˆ(cid:62)
Let µˆ (x) = β x, and assume that the conditions in Example 1 are satisfied. Then
|     | 1,n |               | 1,n |        |               |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| {µˆ | }   | has typically |     | simple | realizations. |     |     |     |     |     |     |     |
1,n n≥1
|     |     | ˆ   | p   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. Since β →− β∗, the function µˆ typically takes values in the “simple” set F =
|     |     | 1,n |     | 1   |     |     | 1,n |     |     |     |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{µ (x) := β(cid:62)x : ||β − β∗|| ≤ 1}. To see that this set is simple, use the fact for all β,γ,
| β   |       |        |      | 1   |      |     |      |     |     |     |     |     |
| --- | ----- | ------ | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
| ||µ | −µ || | ≤ M||β | −γ|| | for | some | M   | < ∞. |     |     |     |     |     |
| β   | γ     | n      |      |     |      |     |      |     |     |     |     |     |
|     |       |        |      | 1   | n    |     |      |     |     |     |     |     |
(cid:88)
||µ −µ ||2 = |(β −γ)(cid:62)x |2 ≤ Tr(Σ )||β −γ||2 ≤ M2||β −γ||2
|     |     | β   | γ n |     |     |     | i   | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
i=1
M2
The last inequality is valid with = 2Tr(Σ) for large enough n, since Σ → Σ. As a
n
consequence, the s-covering number of F can be bounded using the (s/M)-covering number
n
of the Euclidean ball B (β∗) := {β ∈ Rd : ||β − β∗|| ≤ 1}. A simple volume argument12
1
|     |     |     |     | 1   |     |     |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
shows that the s-covering number of a B (β∗) is less than or equal to (1+2/s)d. Thus, we
1
1
have:
|     |     | (cid:90) |           |     |        |       | (cid:90) |                |     |       |     |     |
| --- | --- | -------- | --------- | --- | ------ | ----- | -------- | -------------- | --- | ----- | --- | --- |
|     |     | 1        | (cid:112) |     |        |       | 1        | (cid:112)      |     |       |     |     |
|     |     | sup      | logN(F    |     | ,||·|| | ,s)ds | ≤        | dlog(1+2M/s)ds |     | ≤ 3dM | < ∞ |     |
|     |     |          |           | n   |        | n     |          |                |     |       |     |     |
|     |     | 0 n      |           |     |        |       | 0        |                |     |       |     |     |
The argument above works whenever θ ˆ → θ∗ for some limit θ∗ and θ (cid:55)→ µ is smooth near
θ
θ∗. More general nonparametric function classes can also be shown to have the “typically
simple realizations” property, using combinatorial arguments. For example, if F is any
n
| bounded | Vapnik-Chervonenkis |     |     |     | class, |     | then (15) | is satisfied. |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | ------ | --- | --------- | ------------- | --- | --- | --- | --- |
If stable prediction-unbiased models with typically simple realizations are used in the im-
1 (cid:80)n
putation step of the generalized Oaxaca-Blinder method, then the imputed means yˆ
|     |     |     |     |     |     |     |     |     |     |     | n   | i= 1 1 i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
1 (cid:80)n
and yˆ both have asymptotically linear expansions. This is stated formall y in T he -
|     | n i=1 | 0i  |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orem 3.
| Theorem |     | 3. (Asymptotically |     |     |     | linear | expansion) |     |     |     |     |     |
| ------- | --- | ------------------ | --- | --- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
Let {µˆ } and {µˆ } satisfy the assumptions of Theorem 2, and further suppose that
|     | 1,n | n≥1 | 0,n | n≥1 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
these models have typically simple realizations. Then we have the following asymptotically
linear expansions:
n
|     |     |     |     | 1   | (cid:88) |     | 1   | (cid:88)     |         |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | --- | ------------ | ------- | --- | --- | ---- |
|     |     |     |     |     | (yˆ      | −y  | ) = | (cid:15)∗ +o | (n−1/2) |     |     | (16) |
|     |     |     |     |     |          | 1i  | 1i  |              | p       |     |     |      |
|     |     |     |     | n   |          |     | n   | 1i           |         |     |     |      |
1
|     |     |     |     |     | i=1 |     |     | Zi=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
n
|     |     |     |     | 1   | (cid:88) |     | 1   | (cid:88)     |         |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | --- | ------------ | ------- | --- | --- | ---- |
|     |     |     |     |     | (yˆ      | −y  | ) = | (cid:15)∗ +o | (n−1/2) |     |     | (17) |
|     |     |     |     |     |          | 0i  | 0i  |              | p       |     |     |      |
|     |     |     |     | n   |          |     | n   | 0i           |         |     |     |      |
0
|     |     |     |     |     | i=1 |     |     | Zi=0 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
where (cid:15)∗ := y −µ∗ (x ) and (cid:15)∗ := y −µ∗ (x ). Moreover, µ∗ and µ∗ may be chosen
|         | 1i        | 1i        | 1,n  | i         | 0i          |     | 0i 0,n | i   | 1,n | 0,n |     |     |
| ------- | --------- | --------- | ---- | --------- | ----------- | --- | ------ | --- | --- | --- | --- | --- |
|         | (cid:80)n |           |      | (cid:80)n |             |     |        |     |     |     |     |     |
| so that | 1         | (cid:15)∗ | = 1  |           | (cid:15)∗ = | 0.  |        |     |     |     |     |     |
|         | n         | i=1       | 1i n | i=1       | 0i          |     |        |     |     |     |     |     |
12Let
β 1 be any point in the ball, β 2 any point not within distance s of β 1 , β 3 any point not within s of
either β or β , and so on. The process has to terminate within (1+2/s)d steps or else the total volume of
|       | 1      | 2              |     |        |     |             |           |           |         |     |     |     |
| ----- | ------ | -------------- | --- | ------ | --- | ----------- | --------- | --------- | ------- | --- | --- | --- |
| balls | around | the previously |     | chosen | β   | will exceed | the total | volume of | B (β∗). |     |     |     |
|       |        |                |     |        | i   |             |           |           | 1 1     |     |     |     |
12

(cid:80)n
In words, Theorem 3 says that 1 (yˆ − y ) is essentially just a sample average of
|     |     |     |     |     |     | n i=1 | ti  | ti  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
some mean-zero constants. Thus, under some Lindeberg-type conditions, the completely
randomized central limit theorem (Li and Ding, 2017) can be used to prove the joint asymp-
|     |     |     | 1 (cid:80)n |     |     |     | 1 (cid:80)n |     |     |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
totic normality of (yˆ − y ) and (yˆ − y ), which implies the asymptotic
|     |     |     | n i=1 | 1i  | 1i  |     | n   | i=1 0i | 0i  |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
normality of (τˆ −τ ). Corollary 1 gives some sufficient conditions.
|           |     | n              | n   |            |     |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Corollary |     | 1. (Asymptotic |     | normality) |     |     |     |     |     |     |     |     |
Assume the conclusion of Theorem 3. Further assume that MSE (t) is bounded away from
n
zeroandmax ((cid:15)∗)2 = o(n)fort ∈ {0,1}. Iftheresidualcorrelationρ := (cid:104)(cid:15)∗,(cid:15)∗(cid:105)/(||(cid:15)∗|| ||(cid:15)∗|| )
|     |         | i    | ti       |      |          |     |     |     |     | n   | 1 0 | 1 2 0 2 |
| --- | ------- | ---- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | ------- |
| is  | bounded | away | from −1, | then | we have: |     |     |     |     |     |     |         |
√
|     |     |     |     |     |     | n(τˆ | −τ ) | d         |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --------- | --- | --- | --- | ---- |
|     |     |     |     |     |     | n    | n    | →− N(0,1) |     |     |     | (18) |
σ
n
|       | σ2  | 1     |      | 1    |     |      | 2 (cid:80)n | ((cid:15)∗ | −(cid:15)∗ )2 |     |     |     |
| ----- | --- | ----- | ---- | ---- | --- | ---- | ----------- | ---------- | ------------- | --- | --- | --- |
| where |     | = MSE | (1)+ | MSE  |     | (0)− |             |            |               |     |     |     |
|       |     | n pn  | n    | 1−pn | n   |      | n i=1       | 1i         | 0i            |     |     |     |
|       |     |       |      |      |     |      |             |            | {µ∗           | {µ∗ |     |     |
Corollary 1 holds for any choice of the sequences } and } that satisfy the
|     |     |     |     |     |     |     |     |     | 1,n n≥1 | 0,n | n≥1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
stated conditions. The requirement that MSE (0), MSE (1) are bounded away from zero
|     |     |     |     |     |     |     |     | n   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and ρ is bounded away from −1 are only used to rule out the degenerate situation where
√ n
n(τˆ − τ ) = o(1). In those cases, τˆ is still a very good estimate of τ , but confidence
|     | n   | n   |     |     |     | n   |     |     |     |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
intervals may not have asymptotically valid coverage. Although this assumption is not used
in the works by Lin (2013) and Bloniarz et al. (2016), that seems to be an oversight. In
practice, users should check the R2 from their regression models; if they are both very close
| to  | one, | there may | be reason | for | concern. |     |     |     |     |     |     |     |
| --- | ---- | --------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Unlike Lin’s result (Theorem 1), Corollary 1 does not contain any “noninferiority” claim,
i.e. there is no guarantee that a generalized Oaxaca-Blinder estimator is never worse than
Neyman’s unadjusted difference-of-means estimator. That is the price of generality. Since
theclassofregressionmethodstowhichCorollary1appliesissobroad, itinevitablycontains
some bad apples. In practice however, it is quite difficult to construct an explicit example
where a regression method that is actually used has worse performance than the unadjusted
estimator. For logistic regression, we have not been able to construct any such example
| despite |            | some effort. |           |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.3     | Confidence |              | intervals |     |     |     |     |     |     |     |     |     |
In order to use Corollary 1 to construct confidence intervals for τ , it is necessary to
n
construct an estimate of σ . Although σ is not (in general) identifiable from observed
|     |     |     |     | n   |     |     | n   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
data, there is an identifiable upper bound which follows from the calculations by Neyman
| (Neyman, |     | 1923) |     |     |     |     |      |     |          |     |     |      |
| -------- | --- | ----- | --- | --- | --- | --- | ---- | --- | -------- | --- | --- | ---- |
|          |     |       |     |     |     | 1   |      | 1   |          |     |     |      |
|          |     |       |     | nσ2 | ≤   | MSE | (1)+ |     | MSE (0). |     |     | (19) |
|          |     |       |     |     | n   |     | n    |     | n        |     |     |      |
|          |     |       |     |     |     | n   |      | n   |          |     |     |      |
|          |     |       |     |     |     | 1   |      | 0   |          |     |     |      |
One way to estimate the upper bound in (19) is to first use in-sample residual variance
(20) as an estimate of MSE (t), and then plug the MSE estimates back into (19). Then,
n
13

confidence intervals may be constructed using the estimated upper bound.
1
|     |     | (cid:91) |        | (cid:88) |        |     |      |
| --- | --- | -------- | ------ | -------- | ------ | --- | ---- |
|     |     | MSE      | (t) := | [y −µˆ   | (x )]2 |     | (20) |
|     |     |          | n      | ti       | t,n i  |     |      |
|     |     |          | n −1   |          |        |     |      |
t
Zi=t
µ∗
Theorem 4 says that this will work, as long as the residuals from the “population” model
1
µ∗
| and | are not too heavy-tailed. |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- | --- | --- |
0
| Theorem | 4. (Confidence |     | intervals) |     |     |     |     |
| ------- | -------------- | --- | ---------- | --- | --- | --- | --- |
(cid:80)n
AssumetheconditionsofTheorem3andCorollary1. IfMSE (t)staysboundedand 1 ((cid:15)∗)4 =
n
n i=1 ti
o(n) for t ∈ {0,1}, then we may construct an asymptotically valid confidence interval for τ:
|     |     |    |    |     |   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:115)
|     |         |      |         | M(cid:100)SE (1) | M(cid:100)SE (0) |       |      |
| --- | ------- | ---- | ------- | ---------------- | ---------------- | ----- | ---- |
|     | liminfP | τ ∈ | τˆ ±z  | n +              | n                | ≥ 1−α | (21) |
|     |         | n    | n 1−α/2 |                  |                |       |      |
|     | n→∞     |      |         | n                | n                |       |      |
|     |         |      |         | 1                | 0                |       |      |
When the treatment has no effect (i.e. y = y for all i) and the same method is used to
1i 0i
estimate both µˆ and µˆ (e.g. both logistic regression with the same covariates), then the
|            | 1        | 0                 |          |            |      |     |     |
| ---------- | -------- | ----------------- | -------- | ---------- | ---- | --- | --- |
| asymptotic | coverage | of the confidence | interval | is exactly | 1−α. |     |     |
3.4 Extensions
Theorem 3 has a host of other consequences, which we briefly allude to. The tools in Li
and Ding (2020) can be used to study the asymptotic distribution of an asymptotically linear
statistic under Mahalanobis rerandomization, and the delta method can be used to derive
the asymptotic distribution of other smooth functions of the imputed means. Therefore, it
should be possible to use generalized Oaxaca-Blinder estimators in rerandomized designs,
and also to study generalized Oaxaca-Blinder odds-ratio estimators. We leave the technical
| details | of those extensions | for | future work. |     |     |     |     |
| ------- | ------------------- | --- | ------------ | --- | --- | --- | --- |
4 Examples
In this section, we give some examples of specific regression methods that satisfy the
assumptions of stability, prediction unbiasedness, and typically simple realizations. We have
chosen examples that cover a variety of situations in which Lin’s “interactions” estimator
might be deficient: (i) binary outcomes; (ii) count outcomes; (iii) skewed outcomes; and (iv)
| highly | nonlinear relationships. |     |     |     |     |     |     |
| ------ | ------------------------ | --- | --- | --- | --- | --- | --- |
| 4.1    | Logistic regression      |     |     |     |     |     |     |
With binary outcomes, OLS covariate adjustment is intuitively “wrong.” For example,
if the perspective on Lin’s “interaction” estimator presented in Section 2 is taken up, im-
putation with linear models is unsatisfactory because values less than 0 or larger than 1
14

may be imputed. This deficiency has led many authors to consider procedures similar to
the logistic-regression-based Oaxaca-Blinder estimator (Freedman, 2008c; Ding and Li, 2018;
Firth and Bennett, 1998; Hansen and Bowers, 2009), but none have given a truly satisfying
proof that covariate adjustment with logistic models is valid in the randomization model.
The closest result we have seen is the work of Hansen and Bowers (Hansen and Bowers,
(cid:80)n
2009), which establishes the asymptotic normality of 1 (yˆ −y ) when yˆ is imputed
|     |     |     |     |     |     |     | 1i  | 1i  | 1i  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n i=1
using logistic regression. However, the authors assume stability instead of proving it from
low-level assumptions on the finite population. Theorem 5 goes beyond that and establishes
(cid:80)n
theasymptoticallylinearexpansionfor 1 (yˆ −y )underonlyprimitiveassumptionson
|     |     |     |     |     | n   | i=1 | 1i 1i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
thepopulation. AsymptoticnormalityfollowsundertheadditionalrequirementsofCorollary
1.
| Theorem | 5.  | (Logistic | regression) |     |     |     |     |     |     |     |
| ------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Suppose that the potential outcomes y are binary and µˆ is estimated using logistic regres-
|     |     |     |     |     | 1i  |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sion. Assume that, for all large n, there exists a vector θ∗ solving the “population” logistic
1,n
| regression | problem | (22). |     |          |     |     |     |          |     |     |
| ---------- | ------- | ----- | --- | -------- | --- | --- | --- | -------- | --- | --- |
|            |         |       |     | (cid:40) |     | n   |     | (cid:41) |     |     |
1 (cid:88)
|     |     | θ∗  |          | L   |         |     | x(cid:62)θ+log(1+eθ(cid:62)xi) |     |     |      |
| --- | --- | --- | -------- | --- | ------- | --- | ------------------------------ | --- | --- | ---- |
|     |     |     | = argmin |     | (θ) : − |     | −y                             |     |     | (22) |
|     |     | 1,n |          | n   |         | n   | 1i i                           |     |     |      |
θ
i=1
(cid:80)n
Further suppose that 1 ||x ||4 is uniformly bounded and ∇2L (θ∗ ) (cid:23) λ I for
|     |     |     |       | i   |     |     |     | n 1,n | min | d×d |
| --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     | n i=1 |     |     |     |     |       |     |     |
some positive constant λ not depending on n. Then the sequence {µˆ } satisfies the
|            |     |         | min |     |     |     |     | 1,n n≥1 |     |     |
| ---------- | --- | ------- | --- | --- | --- | --- | --- | ------- | --- | --- |
| conditions | of  | Theorem | 3.  |     |     |     |     |         |     |     |
At least qualitatively speaking, the assumptions of Theorem 5 cannot be improved (al-
though the uniform bounds could, with additional effort, be relaxed to depend on n). It is
widely known that the logistic MLE fails to exist when the design matrix X is rank-deficient
or the 1s and 0s among the outcomes can be perfectly separated by a hyperplane (Albert
and Anderson, 1984). If either of these properties hold in the population, then they neces-
sarily hold in a subsample. The existence of the population MLEs is, therefore, necessary to
| guarantee | the | existence | of  | the sample | MLEs. |     |     |     |     |     |
| --------- | --- | --------- | --- | ---------- | ----- | --- | --- | --- | --- | --- |
However, it is not sufficient. Consider for instance the following possibilities:
|     | • Near-perfect | separation. |     |     |     |     |     |     |     |     |
| --- | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
If only a single exceptional point prevents the y s from being perfectly separated by
1i
a hyperplane, then θ∗ exists. However, in 100(1−p )% of the possible realizations of
|     |     |     | 1   |     |     |     | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the treatment assignments (Z ,··· ,Z ), the exceptional point will not be observed. In
|     |     |     |     |     | 1   | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
|     | those samples, |     | θ will | fail to | exist and | τˆ will | not be well-defined. |     |     |     |
| --- | -------------- | --- | ------ | ------- | --------- | ------- | -------------------- | --- | --- | --- |
1
|     | • Near-perfect | collinearity. |     |     |     |     |     |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
If two columns of the design matrix X have perfect correlation except for a few excep-
tions, then in many realizations of the treatment assignments (Z ,··· ,Z ), the design
|     |     |     |     |     |     |     |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
matrix used to estimate µˆ will be rank-deficient. Again, θ will fail to exist. This
|     |     |     |     | 1   |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
might occur if one of the predictors is a very sparsely populated indicator variable.
15

TheassumptionthattheFisherinformation∇2L
(θ∗ )isboundedawayfromzeroisusedto
n 1,n
rule out such pathological populations. Some indications that these assumptions are violated
are (i) many fitted values very close to 0.00 or 1.00, and (ii) “unnaturally large” standard
errors on the regression coefficients. Chapter 6 of the textbook by Agresti (Agresti, 1990)
| has | a more  | detailed | discussion. |     |     |     |     |     |     |     |
| --- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| 4.2 | Poisson |          | regression  |     |     |     |     |     |     |     |
Although OLS adjustment is not as obviously “wrong” in the case of count outcomes
as in the case of binary outcomes, the example presented in Section 2.4 shows that Poisson
models can lead to substantial efficiency gains in such settings. Theorem 3 gives some
sufficient conditions to justify the validity of the Poisson regression generalized Oaxaca-
| Blinder | estimator. |             |     |             |     |     |     |     |     |     |
| ------- | ---------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| Theorem |            | 6. (Poisson |     | regression) |     |     |     |     |     |     |
Suppose that the potential outcomes y are nonnegative integers and µˆ is estimated us-
|     |     |     |     |     | 1i  |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θ∗
ing Poisson regression. Assume that, for all large n, there exists a vector solving the
1,n
| “population” |     | Poisson |     | regression | problem (23). |     |     |     |          |     |
| ------------ | --- | ------- | --- | ---------- | ------------- | --- | --- | --- | -------- | --- |
|              |     |         |     |            | (cid:40)      |     |     |     | (cid:41) |     |
n
1 (cid:88)
|     |     |     | θ∗  |          | L      |     | x(cid:62)θ+exp(θ(cid:62)x |     |     |      |
| --- | --- | --- | --- | -------- | ------ | --- | ------------------------- | --- | --- | ---- |
|     |     |     |     | = argmin | (θ) := | [−y |                           |     | )]  | (23) |
|     |     |     | 1,n |          | n n    |     | 1i                        | i   | i   |      |
θ
i=1
|     |     |     | (cid:80)n |     |     |     |     | (cid:80)n |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --------- | --- | --- |
Let MSE (1) = 1 [y −exp(θ∗(cid:62)x )]2. Assume that ||x ||, 1 y2, MSE (1) are uni-
|     | n   |     | n i=1 | 1i  | 1,n i |     |     | i n | i=1 1i n |     |
| --- | --- | --- | ----- | --- | ----- | --- | --- | --- | -------- | --- |
∇2L
formly bounded and (θ∗ ) (cid:23) λ I for some positive constant λ not depending
|     |     |     |     | n   | 1,n min d×d |     |     |     | min |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
on n. Then the sequence {µˆ } satisfies the conditions of Theorem 3.
1,n n≥1
Theconditionsarea bitstrongerthanthoserequiredforlogisticregression. Thisis partly
(cid:80)n
duetothenatureofthedata; theboundednessof 1 y andMSE (1)areautomaticwith
|     |     |     |     |     |     |     | i=1 | 1i  | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
binary outcomes, but needs to be assumed for count outcomes. In any case, the assumption
that MSE (1) is bounded is needed in Theorem 4. The requirement that covariates are
n
bounded is more restrictive than what was assumed in Theorem 5, but in Poisson regression
it is typical to log-transform covariates (since the inverse link is exponential). On the log
| scale, | boundedness         |     | is  | more palatable. |            |     |     |     |     |     |
| ------ | ------------------- | --- | --- | --------------- | ---------- | --- | --- | --- | --- | --- |
| 4.3    | Transformed-outcome |     |     |                 | regression |     |     |     |     |     |
Our next example covers the case of skewed outcomes. When the distribution of outcome
variables has a long right tail, linear models typically fit better after a log transformation.
This was the modeling strategy chosen in the original paper by Oaxaca (Oaxaca, 1973),
which studied wage data. However, since treatment effect estimates are more interpretable
on the original scale, it is not enough just to use Lin’s “interactions” estimator with a log-
transformed outcome and then report the coefficient τˆ as the causal effect. Even researchers
willing to assume that (x ,y ,y ) are i.i.d. samples from a probability distribution P and
|     |     |     |     | i 0i | 1i  |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
E[log(y )|x ] = θ(cid:62)x cannot recover the average treatment effect E[y − y ] from θ ,θ
|     | ti  | i   | t i |     |     |     |     |     | 1i 0i | 1 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
16

alone. Additional distributional assumptions are needed to relate averages on the log scale
| to averages | on  | the original |     | scale. |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
There are two ways to get around making these assumptions. One way is to estimate the
|     |     |     | ˆ ˆ |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regression coefficients θ , θ on the log scale, and then use the generalized Oaxaca-Blinder
|           |       |     | 0            | 1     |     |       |     |     |     |     |     |
| --------- | ----- | --- | ------------ | ----- | --- | ----- | --- | --- | --- | --- | --- |
| estimator | based | on  | the debiased | model |     | µˆdb. |     |     |     |     |     |
t
1 (cid:88)
|     |     |     | µˆdb(x) |         | ˆ(cid:62)x)− |     |        | ˆ(cid:62)x |     |     |      |
| --- | --- | --- | ------- | ------- | ------------ | --- | ------ | ---------- | --- | --- | ---- |
|     |     |     |         | = exp(θ |              |     | [exp(θ | )−y        | ]   |     | (24) |
|     |     |     | t       |         | t            | n   |        | t i        | ti  |     |      |
t
Zi=t
ˆ(cid:62)x)
The other way (which we recommend) is to use the fitted values exp(θ as a covariate
t
in a second-stage OLS regression, and then use the generalized Oaxaca-Blinder estimator
µˆols2.
based on
t
|     |     |     |     |           |     | ˆ      | ˆ     | ˆ(cid:62)x) |     |     |      |
| --- | --- | --- | --- | --------- | --- | ------ | ----- | ----------- | --- | --- | ---- |
|     |     |     |     | µˆols2(x) |     | = β +β | exp(θ |             |     |     | (25) |
|     |     |     |     | t         |     | 0,t    | 1,t   | t           |     |     |      |
Theorem 7 says that under assumptions similar to those used in the case of logistic and
| Poisson | regression, | either | of        | these           | strategies | will      | “work.” |     |     |     |     |
| ------- | ----------- | ------ | --------- | --------------- | ---------- | --------- | ------- | --- | --- | --- | --- |
| Theorem | 7. (OLS     |        | with      | log-transformed |            | outcome)  |         |     |     |     |     |
|         |             |        | (cid:80)n |                 |            | (cid:80)n |         |     |     |     |     |
Assume that the ||x ||, 1 y2, and 1 (logy )4 are uniformly bounded. Further
|     |     |     | i n | i=1 1i |     | n i=1 |     | 1i  |     |     |     |
| --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- |
suppose that 1X(cid:62)X (cid:23) λ I for some positive constant λ not depending on n. Then
|     | n   |     | min | d×d   |     |     |     | min |     |          |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | -------- | --- |
|     |     |     |     | {µˆdb |     |     |     |     |     | {µˆols2} |     |
both the debiased estimator } and the second-stage OLS estimator satisfy
|                |     |            |     | 1,n | n≥1 |     |     |     |     | 1,n n≥1 |     |
| -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| the conditions |     | of Theorem |     | 3.  |     |     |     |     |     |         |     |
In practice, we recommend the estimator based on µˆols2 over the estimator based on µˆdb.
|     |     |     |     |     |     |     |     | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The extra degree of freedom β ˆ can make a big difference in terms model fit. For example,
1,t
when the true data-generating process is y = exp(θ(cid:62)x ) + (cid:15) where (cid:15) ∼ N(0,σ2), the
|         |           |     |                  |     |       | ti             |     | t i | i   | i   |     |
| ------- | --------- | --- | ---------------- | --- | ----- | -------------- | --- | --- | --- | --- | --- |
| optimal | predictor | is  | β exp(θ(cid:62)x | )   | where | β = exp(σ2/2). |     |     |     |     |     |
|         |           |     | 1                | t i |       | 1              |     |     |     |     |     |
We illustrate the difference using an example. We used the dataset and experimental set-
up from Example 2.4 to compare the two transformed-outcome methods. The outcome in
this dataset (number of traffic fatalities) is highly skewed, and linear models fit much better
after a log transformation of outcomes and covariates. Figure 2 plots the randomization
distributionofthegeneralizedOaxaca-Blinderestimatorbasedon(i)OLSregressionwithout
any transformations13; (ii) the debiased estimator µˆdb; (iii) the second-stage OLS estimator
t
µˆols2. The estimator based on µˆols2 comes out as the clear winner in terms of precision. This
| t   |     |     |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is reflected in the average width of the 95% confidence intervals, which were (i) 106 deaths;
(ii) 84 deaths; (iii) 78 deaths. All three intervals had approximately nominal coverage
| 13This | is the same | as  | Lin’s “interactions” |     | estimator. |     |     |     |     |     |     |
| ------ | ----------- | --- | -------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
17

|     |     |     | OLS |     |     | Debiased |     | OLS2 |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- |
0.020
0.015
ytisneD
0.010
0.005
0.000
|     |     | −100 | −50 0 | 50 100 | −100 | −50 0 50 | 100 −100 | −50 0 50 100 |     |
| --- | --- | ---- | ----- | ------ | ---- | -------- | -------- | ------------ | --- |
Estimated Treatment Effect
Figure 2: The randomization distribution of Lin’s “interactions” estimator (left), the gen-
ˆ(cid:62)x
eralized Oaxaca-Blinder estimator based on “debiasing” the predictions exp(θ ) (center),
t i
ˆ(cid:62)x
and the generalized Oaxaca-Blinder estimator based on using the predictions exp(θ ) as a
t i
covariate in a linear model (right). All models control for state population, average miles per
driver, and per capita income. The covariates are log transformed in the right two panels.
| 4.4 Isotonic |     | regression |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Our last example is nonparametric. Suppose that the covariate dimension d is equal to
one, and the outcome y is bounded in the interval [a,b]. When the relationship between
1i
x and y is expected to be monotone increasing, isotonic regression is a common modeling
| i         | 1i   |        |       |            |     |             |     |     |     |
| --------- | ---- | ------ | ----- | ---------- | --- | ----------- | --- | --- | --- |
| strategy. | This | method | finds | a function | µˆ  | by solving: |     |     |     |
1
1 (cid:88)
|     |     |     |     | µˆ ∈ argmin |     | (y  | −µ(x ))2 |     | (26) |
| --- | --- | --- | --- | ----------- | --- | --- | -------- | --- | ---- |
|     |     |     |     | 1           |     | 1i  | i        |     |      |
n
|     |     |     |     |     | µ∈M | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zi=1
R
where M = {µ : → [a,b] nondecreasing}. Although the argmin in (26) is not unique,
the value of µˆ at the gridpoints is determined uniquely (Barlow and Brunk, 1972). For
1
| concreteness, |     | we will | choose | the piecewise |     | linear solution. |     |     |     |
| ------------- | --- | ------- | ------ | ------------- | --- | ---------------- | --- | --- | --- |
The theoretical properties of isotonic regression in the i.i.d. setting are well-studied
(see the review paper Guntuboyina and Sen (2018)), but no previous works have studied
this method from the perspective of randomization inference. Theorem 8 says that, under
almost no assumptions, isotonic regression satisfies all of the conditions needed to use it in
| the generalized |     | Oaxaca-Blinder |             | procedure. |     |     |     |     |     |
| --------------- | --- | -------------- | ----------- | ---------- | --- | --- | --- | --- | --- |
| Theorem         | 8.  | (Isotonic      | regression) |            |     |     |     |     |     |
Let x be a real-valued covariate, and y ∈ [a,b] a bounded outcome. Let µˆ be the piecewise-
| i   |     |     |     |     | 1i  |     |     | 1,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
linear solution to (26). Then the sequence {µˆ } satisfies the conditions of Theorem 3.
|     |     |     |     |     |     | 1,n n≥1 |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
Since the isotonic class M contains all constant functions, the (in-sample) mean-squared
error from isotonic regression is never larger than the mean-squared error from a constant
18

fit. Therefore, the generalized Oaxaca-Blinder estimator based on two isotonic regressions
shares “non-inferiority” property of Lin’s “interactions” estimator: the confidence interval
will never be wider than Neyman’s (Neyman, 1923) confidence interval for the difference-of-
means estimator.
Thatbeingsaid, wehavefoundthatusingthein-samplepredictionerrorasanestimateof
MSE (t) performs poorly with isotonic regression, due to overfitting. In a simple synthetic-
n
data example shown in Figure 3, about 600 samples were needed per treatment arm before
95%confidenceintervalsachieved>93%coverage. Oneexplanationforwhysomanysamples
are needed is that the “degrees of freedom” in the isotonic class (whatever that means) is
too large – see the jagged regression function in Figure 3. The smoothed variants of isotonic
regression that have been proposed in the literature (Barlow and Brunk (1972)) may perform
| better in smaller | samples. |     |     |     |     |
| ----------------- | -------- | --- | --- | --- | --- |
1.00
80
|     | 0.75    |              | 60      |                            |           |
| --- | ------- | ------------ | ------- | -------------------------- | --------- |
|     | 1y = 0y |              | ytisneD |                            |           |
|     | 0.50    |              | 40      |                            |           |
|     | 0.25    |              | 20      |                            |           |
|     | 0.00    |              |         | 0                          |           |
|     | −5.0    | −2.5 0.0 2.5 | 5.0     | −0.02 −0.01 0.00           | 0.01 0.02 |
|     |         | x            |         | Estimated Treatment Effect |           |
Figure 3: The “population” isotonic regression fit (left), and the randomization distribution
of the generalized Oaxaca-Blinder estimator based on two isotonic regressions (right). There
are 1200 observations in total, with y = y for each i. In each replication, half of the
0i 1i
observations are assigned to the “treatment” group and half of the observations are assigned
| to the “control” | group. |           |        |                |        |
| ---------------- | ------ | --------- | ------ | -------------- | ------ |
| 5 Extension:     |        | a generic | recipe | for parametric | models |
TheparametricexamplespresentedinSection4canallbeprovedbytranslatingstandard
arguments from the theory of M-estimation into the language of finite populations. This
section gives a “master theorem” that lightens the effort of performing that translation in
many cases. The result applies to parametric models where the parameter θ ˆ is estimated by
| solving a convex | M-estimation | problem.       |     |     |     |
| ---------------- | ------------ | -------------- | --- | --- | --- |
| Assumption       | A1. (Convex  | loss function) |     |     |     |
19

ˆ
Assume that θ is the solution to the following (random) optimization problem (27).
n
|     |     |     | (cid:40) |     |     | (cid:41) |     |     |
| --- | --- | --- | -------- | --- | --- | -------- | --- | --- |
1 (cid:88)
|     |     | θ ˆ ∈ | argmin | Lˆ (θ) | :=  | (cid:96)(θ,x ,y ) |     | (27) |
| --- | --- | ----- | ------ | ------ | --- | ----------------- | --- | ---- |
|     |     | n     |        | n      |     | i 1i              |     |      |
n
|     |     |     | θ   |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zi=1
where (cid:96)(θ,x,y) is a loss function that is convex in its first argument.
The convexity condition is likely stronger than necessary. In the classical i.i.d. setting,
consistencyinconvexM-estimationproblemscanbeprovedunderessentiallynoassumptions
(Niemiro, 1992), and a similar phenomenon holds in the randomization setting. In principle,
our arguments (based on uniform convergence) can handle nonconvex loss functions as well,
but solving the problem (27) when the loss function Lˆ is nonconvex is computationally
n
challenging (except in highly specialized problems). Therefore, theoretical results for non-
convex M-estimators are unlikely to have practical relevance and we have not pursued that
direction.
The next assumption asks for the existence of a stable solution to the “population”
| version of | (27). |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Assumption A2. (Existence and stability of population optima)
θ∗
Assume that, for all large n, there exists a vector solving the “population” M-estimation
n
| problem | (28). |     |     |          |     |          |     |     |
| ------- | ----- | --- | --- | -------- | --- | -------- | --- | --- |
|         |       |     |     | (cid:40) |     | (cid:41) |     |     |
n
1 (cid:88)
|     |     | θ∗ = | argmin | L (θ) | :=  | (cid:96)(θ,x ,y ) |     | (28) |
| --- | --- | ---- | ------ | ----- | --- | ----------------- | --- | ---- |
|     |     | n    |        | n     |     | i 1i              |     |      |
n
θ
i=1
|     |     |     |     |     |     |     | R R |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Furthermore, suppose that there exists a strictly increasing function f : → so that
|         |                    |     |         |      |     |       | ≥0 ≥0 |     |
| ------- | ------------------ | --- | ------- | ---- | --- | ----- | ----- | --- |
| L (θ)−L | (θ∗) ≥ f(||θ−θ∗||) |     | for all | θ.   |     |       |       |     |
| n       | n                  |     |         |      |     |       |       |     |
|         | n                  | n   |         |      |     |       |       |     |
|         |                    | L   | L       | (θ∗) |     | θ∗||) |       | θ∗  |
The assumption that (θ) − ≥ f(||θ − guarantees the minimizer is
|     |     |     | n   | n n |     | n   |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
unique and rules out population sequences where the objective function becomes flatter and
flatter as n → ∞. A useful tool for verifying this assumption is the following Lemma.
| Lemma | 1. (Curvatures | implies | growth) |     |     |     |     |     |
| ----- | -------------- | ------- | ------- | --- | --- | --- | --- | --- |
Suppose that the map θ (cid:55)→ (cid:96)(θ,x,y) is twice continuously differentiable for every x,y and the
minimizer θ∗ occurs at a point where ∇L (θ∗) = 0. Assume that for some radius r > 0 and
n
|     | n   |     |     |     | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
some constant λ > 0 not depending on n, we have ∇2L (θ) (cid:23) λ I for all θ ∈ B (θ∗).
|                 | min |               |     |     |     | n   | min d×d | r n |
| --------------- | --- | ------------- | --- | --- | --- | --- | ------- | --- |
| Then Assumption | A2  | is satisfied. |     |     |     |     |         |     |
The final assumption needed for the convergence of θ ˆ to θ∗ is that L is smooth near
|     |     |     |     |     |     | n   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
its minimum.
| Assumption | A3. (Smooth |     | loss function) |     |     |     |     |     |
| ---------- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
Assume that there exists a radius r > 0 and a constant L < ∞ (not depending on n) such
| that (29) | holds for all | θ,φ ∈    | B (θ∗). |     |     |             |     |     |
| --------- | ------------- | -------- | ------- | --- | --- | ----------- | --- | --- |
|           |               |          | r n     |     |     |             |     |     |
|           |               | (cid:32) |         |     |     | (cid:33)1/2 |     |     |
n
1 (cid:88)
|     |     | [(cid:96)(θ,x | ,y  | )−(cid:96)(φ,x | ,y )]2 | ≤ L||θ−φ|| |     | (29) |
| --- | --- | ------------- | --- | -------------- | ------ | ---------- | --- | ---- |
|     |     |               | i   | 1i             | i 1i   |            |     |      |
n
i=1
20

Under the above assumptions, ||θ ˆ −θ∗|| tends to zero in probability. If the map θ (cid:55)→ µ
n n θ
is also smooth near θ∗, then that implies stability and typically simple realizations.
n
Theorem 9. (General results for parametric models)
Assume that A1, A2, and A3 are satisfied. Then ||θ ˆ −θ∗|| →− p 0. If, in addition, ||µ −µ || ≤
n n θ φ n
M||θ−φ|| for all θ,φ ∈ B (θ∗), then the sequence {µ } is stable and has typically simple
r n θˆ
n
n≥1
realizations.
6 Conclusion
In this paper, we introduced an intuitive approach to performing covariate adjustment
in randomized experiments. It can be summarized in a single sentence: “fill in the missing
outcomes with an unbiased prediction model.” From a theoretical perspective, our main
idea is that a little randomization goes a long way. As long as treatment assignments
are randomized, then tools from empirical process theory can be applied even if all other
quantities are nonrandom.
Many open questions remain. Perhaps the most important one is whether the Donsker-
type “typically simple realizations” assumption can be removed. If one is willing to assume
that (x ,y ,y ,Z ) are i.i.d. samples from a larger population, clever use of sample split-
i 0i 1i i
ting can circumvent these assumptions (Chernozhukov et al., 2018; Wager et al., 2016).
Are similar results available in Neyman’s finite-population model? Recent work (Wu and
Gagnon-Bartsch, 2018) suggests that the answer might be “yes”, but establishing the sta-
bility condition for these complex models remains challenging. We consider this to be an
exciting direction for future work.
21

References
Abadie, A., S. Athey, G. W. Imbens, and J. M. Wooldridge (2020). Sampling-based versus
design-based uncertainty in regression analysis. Econometrica 88(1), 265–296.
Agresti, A. (1990). Categorical data analysis. A Wiley-Interscience publication. New York
[u.a.]: Wiley.
Albert, A. and J. A. Anderson (1984). On the existence of maximum likelihood estimates
| in logistic | regression |     | models. | Biometrika |     | 71(1), 1–10. |
| ----------- | ---------- | --- | ------- | ---------- | --- | ------------ |
Barlow, R. E. and H. D. Brunk (1972). The isotonic regression problem and its dual. Journal
| of the | American | Statistical |     | Association |     | 67(337), 140–147. |
| ------ | -------- | ----------- | --- | ----------- | --- | ----------------- |
Bartlett, J.W. (2018). Covariate adjustment andestimation ofmeanresponsein randomised
| trials. | Pharmaceutical |     | Statistics |     | 17(5), | 648–666. |
| ------- | -------------- | --- | ---------- | --- | ------ | -------- |
Bauer, T. K. and M. Sinning (2008). An extension of the blinder–oaxaca decomposition to
nonlinear models. AStA Advances in Statistical Analysis 92(2), 197–206.
Belson, W. A. (1956). A technique for studying the effects of a television broadcast. Journal
of the Royal Statistical Society. Series C (Applied Statistics) 5(3), 195–202.
Blinder, A. S. (1973). Wage discrimination: Reduced form and structural estimates. The
| Journal | of Human |     | Resources | 8(4), | 436–455. |     |
| ------- | -------- | --- | --------- | ----- | -------- | --- |
Bloniarz, A., H. Liu, C.-H. Zhang, J. S. Sekhon, and B. Yu (2016). Lasso adjustments
of treatment effect estimates in randomized experiments. Proceedings of the National
| Academy | of Sciences |     | 113(27), | 7383–7390. |     |     |
| ------- | ----------- | --- | -------- | ---------- | --- | --- |
Breidt, F. J. and J. D. Opsomer (2017, 05). Model-assisted survey estimation with modern
| prediction | techniques. |     | Statist. | Sci. | 32(2), | 190–205. |
| ---------- | ----------- | --- | -------- | ---- | ------ | -------- |
Cao, W., A. A. Tsiatis, and M. Davidian (2009, 08). Improving efficiency and ro-
bustness of the doubly robust estimator for a population mean with incomplete data.
| Biometrika | 96(3), |     | 723–734. |     |     |     |
| ---------- | ------ | --- | -------- | --- | --- | --- |
Cassel, C. M., C. E. Sarndal, and J. H. Wretman (1976). Some results on general-
ized difference estimation and generalized regression estimation for finite populations.
| Biometrika | 63(3), |     | 615–620. |     |     |     |
| ---------- | ------ | --- | -------- | --- | --- | --- |
Chernozhukov, V., D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, W. Newey, and
J. Robins (2018). Double/debiased machine learning for treatment and structural pa-
| rameters. | The | Econometrics |     | Journal |     | 21(1), C1–C68. |
| --------- | --- | ------------ | --- | ------- | --- | -------------- |
Ding, P. and F. Li (2018, 05). Causal inference: A missing data perspective. Statist.
| Sci. 33(2), | 214–237. |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- |
22

Fairlie, R. W. (1999). The absence of the african-american owned business: An analysis of
the dynamics of self-employment. Journal of Labor Economics 17(1), 80–108.
Firth, D. and K. E. Bennett (1998). Robust models in probability sampling. Journal of the
Royal Statistical Society: Series B (Statistical Methodology) 60(1), 3–21.
Fogarty, C. B. (2018, 06). Regression-assisted inference for the average treatment effect in
| paired | experiments. | Biometrika |     | 105(4), | 994–1000. |
| ------ | ------------ | ---------- | --- | ------- | --------- |
Freedman, D. (2008a, 02). On regression adjustments to experimental data. Advances in
| Applied | Mathematics | 40, | 180–193. |     |     |
| ------- | ----------- | --- | -------- | --- | --- |
Freedman, D. A. (2008b, 03). On regression adjustments in experiments with several treat-
| ments. | Ann. Appl. | Stat. | 2(1), | 176–196. |     |
| ------ | ---------- | ----- | ----- | -------- | --- |
Freedman, D. A. (2008c, 05). Randomization does not justify logistic regression. Statist.
| Sci. 23(2), | 237–249. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
Glynn, A. N. and K. M. Quinn (2010). An introduction to the augmented inverse propensity
| weighted | estimator. | Political |     | Analysis | 18(1), 36–56. |
| -------- | ---------- | --------- | --- | -------- | ------------- |
Guntuboyina, A. and B. Sen (2018, 11). Nonparametric shape-restricted regression. Statist.
| Sci. 33(4), | 568–594. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
Hansen, B. B. and J. Bowers (2009). Attributing effects to a cluster-randomized get-out-
the-vote campaign. Journal of the American Statistical Association 104(487), 873–885.
Imbens, G. W. and D. B. Rubin (2015). Causal Inference for Statistics, Social, and Biomed-
ical Sciences: An Introduction. USA: Cambridge University Press.
Kang, J. D. Y. and J. L. Schafer (2007, 11). Demystifying double robustness: A comparison
of alternative strategies for estimating a population mean from incomplete data. Statist.
| Sci. 22(4), | 523–539. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
Kline, P. (2011, May). Oaxaca-blinder as a reweighting estimator. American Economic
| Review | 101(3), 532–37. |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- |
Kosorok, M. (2008). Introduction to empirical processes and semiparametric inference.
| Springer | series in | statistics. | Springer. |     |     |
| -------- | --------- | ----------- | --------- | --- | --- |
Li, X. and P. Ding (2017). General forms of finite population central limit theorems with
applications to causal inference. Journal of the American Statistical Association 112(520),
1759–1769.
Li, X. and P. Ding (2020). Rerandomization and regression adjustment. Journal of the Royal
| Statistical | Society: | Series | B (Statistical |     | Methodology). |
| ----------- | -------- | ------ | -------------- | --- | ------------- |
23

Lin, W. (2013, 03). Agnostic notes on regression adjustments to experimental data: Reex-
| amining | freedman’s | critique. |     | Ann. | Appl. | Stat. 7(1), | 295–318. |
| ------- | ---------- | --------- | --- | ---- | ----- | ----------- | -------- |
Liu, H. and Y. Yang (2019). Regression-adjusted average treatment effect estimates in
| stratified | randomized |     | experiments. |     |     |     |     |
| ---------- | ---------- | --- | ------------ | --- | --- | --- | --- |
Neyman, J. (1923, 11). On the application of probability theory to agricultural experiments.
| essay on | principles. | section |     | 9. Statist. |     | Sci. 5(4), 465–472. |     |
| -------- | ----------- | ------- | --- | ----------- | --- | ------------------- | --- |
Niemiro, W. (1992, 09). Asymptoticsform-estimatorsdefinedbyconvexminimization. Ann.
| Statist. | 20(3), | 1514–1533. |     |     |     |     |     |
| -------- | ------ | ---------- | --- | --- | --- | --- | --- |
Oaxaca, R. (1973). Male-female wage differentials in urban labor markets. International
| Economic | Review | 14(3), | 693–709. |     |     |     |     |
| -------- | ------ | ------ | -------- | --- | --- | --- | --- |
Olsen, R., L. Orr, S. Bell, and E. Stuart (2013, 12). External validity in policy evaluations
thatchoosesitespurposively. Journal of Policy Analysis and Management 32(1), 107–121.
Peters, C.C.(1941). Amethodofmatchinggroupsforexperimentwithnolossofpopulation.
| The Journal |     | of Educational |     | Research | 34(8), | 606–612. |     |
| ----------- | --- | -------------- | --- | -------- | ------ | -------- | --- |
Robins, J. M., A. Rotnitzky, and L. P. Zhao (1994). Estimation of regression coefficients
when some regressors are not always observed. Journal of the American Statistical Asso-
| ciation | 89(427), | 846–866. |     |     |     |     |     |
| ------- | -------- | -------- | --- | --- | --- | --- | --- |
Rosenbaum, P. R. (2002, 08). Covariance adjustment in randomized experiments and obser-
| vational | studies. | Statist. | Sci. | 17(3), | 286–327. |     |     |
| -------- | -------- | -------- | ---- | ------ | -------- | --- | --- |
Rosenberger, W. F., D. Uschner, and Y. Wang (2019). Randomization: The forgotten
component of the randomized clinical trial. Statistics in medicine 38 1, 1–12.
Rosenblum, M. and M. J. van der Laan (2009). Consultant’s forum: Using regression models
to analyze randomized trials: Asymptotically valid hypothesis tests despite incorrectly
| specified | models. | Biometrics |     | 65(3), | 937–945. |     |     |
| --------- | ------- | ---------- | --- | ------ | -------- | --- | --- |
Rubin, D. (1974). Estimating causal effects of treatments in randomized and nonrandomized
| studies. | Journal | of Educational |     | Psychology |     | 66(5), 688–701. |     |
| -------- | ------- | -------------- | --- | ---------- | --- | --------------- | --- |
Ruhm, C. J. (1995, July). Alcohol policies and highway vehicle fatalities. Working Paper
| 5195, National |     | Bureau | of Economic |     | Research. |     |     |
| -------------- | --- | ------ | ----------- | --- | --------- | --- | --- |
Sa¨rndal, C.-E. and R. L. Wright (1984). Cosmetic form of estimators in survey sampling.
| Scandinavian |     | Journal | of Statistics |     | 11(3), | 146–156. |     |
| ------------ | --- | ------- | ------------- | --- | ------ | -------- | --- |
van der Vaart, A. and J. Wellner (1996). Weak Convergence and Empirical Processes: With
| Applications |     | to Statistics. |     | Springer | Series | in Statistics. | Springer. |
| ------------ | --- | -------------- | --- | -------- | ------ | -------------- | --------- |
24

Vershynin, R. (2018). High-Dimensional Probability: An Introduction with Applications in
Data Science. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge
| University | Press. |     |     |     |
| ---------- | ------ | --- | --- | --- |
Wager, S., W. Du, J. Taylor, and R. J. Tibshirani (2016). High-dimensional regression
adjustments in randomized experiments. Proceedings of the National Academy of Sci-
| ences 113(45), | 12673–12678. |     |     |     |
| -------------- | ------------ | --- | --- | --- |
Westreich, D., J. Edwards, S. Cole, R. Platt, S. Mumford, and E. Schisterman (2015, 07).
Imputation approaches for potential outcomes in causal inference. International journal
| of epidemiology | 44. |     |     |     |
| --------------- | --- | --- | --- | --- |
Wu, C. and R. R. Sitter (2001). A model-calibration approach to using complete auxiliary
information from survey data. Journal of the American Statistical Association 96(453),
185–193.
Wu, E. and J. A. Gagnon-Bartsch (2018). The loop estimator: Adjusting for covariates in
| randomized | experiments. | Evaluation | Review 42(4), | 458–488. |
| ---------- | ------------ | ---------- | ------------- | -------- |
Wu, J. and P. Ding (2018). Randomization tests for weak null hypotheses in randomized
experiments.
Yang, L. and A. A. Tsiatis (2001). Efficiency study of estimators for a treatment effect in a
| pretest–posttest | trial. | The American | Statistician | 55(4), 314–321. |
| ---------------- | ------ | ------------ | ------------ | --------------- |
25

7 Appendix
7.1 Proofs
| 7.1.1 | Randomization |     |     | law | of large |     | numbers |     |     |     |     |     |
| ----- | ------------- | --- | --- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- |
Lemma 2. Let A = {a }n be a sequence of finite subsets of R, and define a¯ :=
|           |     |        | n         | i,n  | i=1   |            |          |           |               |     |     | n    |
| --------- | --- | ------ | --------- | ---- | ----- | ---------- | -------- | --------- | ------------- | --- | --- | ---- |
| (cid:80)n |     |        | (cid:80)n |      |       |            |          |           |               |     |     |      |
| 1         | a   | . If 1 |           | a2 = | o(n), | then       | we have: |           |               |     |     |      |
| i=1       | i,n |        | i=1       | i,n  |       |            |          |           |               |     |     |      |
| n         |     | n      |           |      |       |            |          |           |               |     |     |      |
|           |     |        |           |      |       | (cid:12)   |          |           | (cid:12)      |     |     |      |
|           |     |        |           |      |       | (cid:12)   |          |           | (cid:12)      |     |     |      |
|           |     |        |           |      |       | 1 (cid:88) |          |           | p             |     |     |      |
|           |     |        |           |      |       | (cid:12)   | a        | −a¯       | (cid:12) →− 0 |     |     | (30) |
|           |     |        |           |      |       | (cid:12)n  | i,n      | n(cid:12) |               |     |     |      |
|           |     |        |           |      |       | (cid:12) 1 |          |           | (cid:12)      |     |     |      |
Zi=1
| where | Z are | defined | in  | the | main body | of  | the | paper. |     |     |     |     |
| ----- | ----- | ------- | --- | --- | --------- | --- | --- | ------ | --- | --- | --- | --- |
i
1 (cid:80)
Proof. By Proposition 1 in Freedman (2008a), the variance of a has a simple
|     |     |     |     |     |     |     |     |     |     | n1  | Zi=1 i,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
expression:
|     |     |     | (cid:32) |            | (cid:33) |          |     |                  |     |            |       |     |
| --- | --- | --- | -------- | ---------- | -------- | -------- | --- | ---------------- | --- | ---------- | ----- | --- |
|     |     |     |          |            |          | (cid:18) |     | (cid:19)(cid:18) |     | (cid:19) n |       |     |
|     |     |     |          | 1 (cid:88) |          |          | 1−p |                  | 1   | 1 (cid:88) |       |     |
|     |     |     | Var      |            | a        | =        |     | n                |     | (a         | −a¯)2 |     |
|     |     |     |          |            | i,n      |          |     |                  |     | i,n        |       |     |
|     |     |     |          | n          |          |          | p   |                  | n−1 | n          |       |     |
|     |     |     |          | 1          |          |          | n   |                  |     |            |       |     |
|     |     |     |          | Zi=1       |          |          |     |                  |     | i=1        |       |     |
Since 1 (cid:80)n (a − a¯)2 ≤ 1 (cid:80)n a2 = o(n), this variance tends to zero. From this,
i, n
|              | n   | i=1 |        |         | n i=    | 1 i ,n         |     |             |     |     |     |     |
| ------------ | --- | --- | ------ | ------- | ------- | -------------- | --- | ----------- | --- | --- | --- | --- |
| | 1 (cid:80) | a   | −   | a¯ | → | 0 follo | ws fr o | m C hebyshev’s |     | inequality. |     |     |     |     |
|              |     | i,n | p      |         |         |                |     |             |     |     |     |     |
n1 Zi=1
| 7.1.2 | A   | maximal | inequality |     |     |     |     |     |     |     |     |     |
| ----- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition 1. For any function f : Rd → R, define G (f) as follows:
n
|     |     |     |     |     |     | 1   | n        | (cid:20) Z f(x | )    | (cid:21) |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | ---- | -------- | --- | ---- |
|     |     |     |     |     | G   |     | (cid:88) | i              | i    |          |     |      |
|     |     |     |     |     | (f) | = √ |          |                | −f(x | )        |     | (31) |
|     |     |     |     |     | n   |     |          |                |      | i        |     |      |
|     |     |     |     |     |     | n   |          | p              |      |          |     |      |
|     |     |     |     |     |     |     | i=1      | n              |      |          |     |      |
where p = n /n. If F is any collection of functions, f ∈ F is any fixed function, and δ > 0
|        | n       | 1        |     |      |                 |     |          |     | 0   |            |     |     |
| ------ | ------- | -------- | --- | ---- | --------------- | --- | -------- | --- | --- | ---------- | --- | --- |
| is any | radius, | then     | we  | have | the inequality: |     |          |     |     |            |     |     |
|        |         | (cid:34) |     |      |                 |     | (cid:35) |     |     |            |     |     |
|        |         |          |     |      |                 |     |          |     |     | (cid:90) δ |     |     |
(cid:112)
|     | E   |                 | sup | |G  | (f)−G | (f  | )|  | ≤ (C/p | )   | logN(F,||·|| | ,s)ds | (32) |
| --- | --- | --------------- | --- | --- | ----- | --- | --- | ------ | --- | ------------ | ----- | ---- |
|     |     |                 |     |     | n     | n   | 0   |        | min |              | n     |      |
|     |     | f∈F:||f−f0||n≤δ |     |     |       |     |     |        |     | 0            |       |      |
(cid:80)n
where ||f −f ||2 := 1 [f(x )−f (x )]2 and C < ∞ is a universal constant.
|     |     | 0   |     |     | i,n | 0   | i,n |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | n   | n   | i=1 |     |     |     |     |     |     |     |     |
{G
Proof. First, we show that (f) : f ∈ F} is a (c/p )-sub-Gaussian process indexed
|     |     |     |     |     | n   |     |     |     |     | min |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by the metric space (F,|| · || ). Lemma A2 in Wu & Ding (Wu and Ding, 2018) gives
n
the following exponential tail bound for the distance between sample averages and their
| population |     | counterparts: |                  |            |         |      |                   |          |        |              |          |     |
| ---------- | --- | ------------- | ---------------- | ---------- | ------- | ---- | ----------------- | -------- | ------ | ------------ | -------- | --- |
|            |     |               | (cid:32)(cid:12) |            |         |      | (cid:12)          | (cid:33) |        |              |          |     |
|            |     |               | (cid:12)1        | n (cid:20) | Z f(x ) |      | (cid:21) (cid:12) |          |        | (cid:18) nt2 | (cid:19) |     |
|            |     |               |                  | (cid:88)   | i i     |      |                   |          |        |              |          |     |
|            |     |               | P (cid:12)       |            |         | −f(x | ) (cid:12)        | > t      | ≤ 2exp | −            |          |     |
|            |     |               | (cid:12)n        |            |         |      | i (cid:12)        |          |        |              |          |     |
|            |     |               |                  |            | p       |      |                   |          |        | 2σ2(f)/p2    |          |     |
|            |     |               | (cid:12)         | i=1        | n       |      | (cid:12)          |          |        |              | n        |     |
26

where σ2(f) = 1 (cid:80)n [f(x )−f ¯ ]2 and p = n /n. We may loosen the upper bound using
n i=1 i n 1
the inequality σ2(f)/p2 ≤ ||f||2/p2 . That implies the following tail bound for G (f):
n n min n
(cid:18) t2 (cid:19)
P(|G (f)| > t) ≤ 2exp −
n 2||f||2/p2
n min
Since the above bound holds for any function f, it also holds for functions of the form
f = g −h with g,h ∈ F. Since G (g −h) = G (g)−G (h), this yields a sub-Gaussian tail
n n n
bound for the increments of the process.
(cid:18) t2 (cid:19)
P(|G (g)−G (h)| > t) ≤ 2exp −
n n 2||g −h||2/p
n min2
Hence, {G (f) : f ∈ F} is a sub-Gaussian process. Moreover, this process is separable since
n
the map f (cid:55)→ G (f) is always continuous in the ||·|| -norm on F. Therefore, by Dudley’s
n n
entropy integral (Corollary 2.2.8 in van der Vaart and Wellner (1996)), there exists some
universal constant C < ∞ such that (32) holds.
7.1.3 Population regression is always prediction unbiased
Lemma 3. (Prediction unbiasedness in the population)
Let {µˆ } be a sequence of prediction-unbiased regression functions. Assume that there
1,n n≥1
exists a nonrandom sequence {µ∗ } such that ||µˆ −µ∗ || →− p 0 and 1 (cid:80)n [µ∗ (x )−
1,n n≥1 1,n 1,n n n i=1 1,n i,n
y ]2 = o(n). Then it is always possible to choose the sequence {µ∗ } so that (33) holds
1i,n 1,n n≥1
for every n.
n n
1 (cid:88) 1 (cid:88)
µ∗ (x ) = y (33)
n 1,n i,n n 1i,n
i=1 i=1
Proof. Let {µ∗ } be any fixed sequence of functions satisfying ||µˆ − µ∗ || →− p 0 and
1,n n≥1 1,n 1,n n
1 (cid:80)n [µ∗ (x )−y ]2 = o(n). A simple calculation shows that the prediction bias must be
n i=1 1,n i 1i
vanishing:
(cid:12) (cid:12) (cid:12) (cid:12)
(cid:12)1 (cid:88) n (cid:12) (cid:12) 1 (cid:88) (cid:12)
(cid:12) [µ∗ (x )−y ](cid:12) = (cid:12) [µ∗ (x )−y ](cid:12)+o (1)
(cid:12)n 1,n i 1i (cid:12) (cid:12)n 1,n i 1i (cid:12) p
(cid:12) (cid:12) (cid:12) 1 (cid:12)
i=1 Zi=1
(cid:12) (cid:12)
(cid:12) 1 (cid:88) (cid:12)
= (cid:12) [µ∗ (x )−µˆ (x )](cid:12)+o (1)
(cid:12)n 1,n i 1,n i (cid:12) p
(cid:12) 1 (cid:12)
Zi=1
n
11 (cid:88)
≤ |µ∗ (x )−µˆ (x )|+o (1)
pn 1,n i 1,n i p
i=1
1
≤ ||µ∗ −µˆ || +o (1)
p 1,n 1,n n p
27

The right-hand side of the above display is o (1) by stability, and the left-hand side is
p
nonrandom. Therefore, it must be the case that 1 (cid:80)n [µ∗ (x )−y ] = o(1). Then, we may
define ν∗ (x) = µ∗ (x) − 1 (cid:80)n [µ∗ (x ) − y ] n (i.e i . =1 sub 1, t n rac i t off 1 t i he bias). The property
1,n 1,n n i=1 1,n i 1i
||ν∗ −µˆ || →− p 0 still holds, as does 1 (cid:80)n [ν∗ (x )−y ]2 = o(n). Therefore, we may
1,n 1,n n n i=1 1,n i,n 1i,n
as well have chosen the original sequence µ∗ so that (33) is satisfied.
1,n
7.1.4 Proof of Theorem 2
Proof. Let {µ∗ } be the population prediction unbiased sequence which is guaranteed to
1,n n≥1
exist by Lemma 3. We may write:
(cid:12) (cid:12) (cid:12) (cid:12)
(cid:12)1 (cid:88) n (cid:12) (cid:12)1 (cid:88) n (cid:12)
(cid:12) (yˆ −y )(cid:12) = (cid:12) [µˆ (x )−y ](cid:12)
(cid:12)n 1i 1i (cid:12) (cid:12)n 1,n i 1i (cid:12)
(cid:12) (cid:12) (cid:12) (cid:12)
i=1 i=1
(cid:12) (cid:12) (cid:12) (cid:12)
(cid:12)1 (cid:88) n (cid:12) (cid:12)1 (cid:88) n (cid:12)
≤ (cid:12) [µ∗ (x )−y ](cid:12)+(cid:12) [µˆ (x )−µ∗ (x )](cid:12)
(cid:12)n 1,n i 1i (cid:12) (cid:12)n 1,n i 1,n i (cid:12)
(cid:12) (cid:12) (cid:12) (cid:12)
i=1 i=1
≤ 0+||µˆ −µ∗ ||
1,n 1,n n
= o (1)
p
A symmetric argument shows that 1 (cid:80)n (yˆ −y ) = o (1). Thus, τˆ −τ = o (1).
n i=1 0i 0i p n n p
7.1.5 Proof of Theorem 3
Proof. We start by proving (16). Let {µ∗ } be a sequence of nonrandom functions such
1,n n≥1
that ||µˆ − µ∗ || → 0 and 1 (cid:80)n µ∗ (x ) = 1 (cid:80)n y . Such a sequence is always
1,n 1,n n p n i=1 1,n i n i=1 1i
guaranteed to exist (Lemma 3). By rearranging terms, we may write:
n n n
1 (cid:88) 1 (cid:88) 1 (cid:88) Z [y −µˆ (x )]
i 1i 1,n i
(yˆ −y ) = [µˆ (x )−y ]+
1i 1i 1,n i 1i
n n n p
n
i=1 i=1 i=1
= 1 (cid:88) (cid:15)∗ + 1 (cid:88) n (cid:20)Z i µ∗ 1,n (x i ) −µ∗ (x ) (cid:21) − 1 (cid:88) n (cid:20) Z i µˆ 1,n (x i ) −µˆ (x ) (cid:21)
n 1i n p 1,n i n p 1,n i
1 n n
Zi=1 i=1 i=1
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
√ √
nG n(µ∗
1,n
) nG n(µˆ1,n)
The quantity G (µ∗ ) − G (µˆ ) is vanishing in probability. To see this, let (cid:15),δ > 0 be
n 1,n n 1,n
arbitrary. For every r > 0, Proposition 1 and the “typically simple realizations” assumption
28

imply the following tail bound:
(cid:32) (cid:33)
C (cid:90) r(cid:113)
P sup |G (µ)−G (µ∗ )| > (cid:15) ≤ logN(F ∪{µ∗ },||·|| ,s)ds
n n 1,n p (cid:15) n 1,n n
µ∈Fn, ||µ−µ∗
1,n
||n≤r min 0
C (cid:90) r (cid:112)
≤ log(1+N(F ,||·|| ,s)ds
n n
p (cid:15)
min 0
C (cid:90) r (cid:112)
≤ 1+ logN(F ,||·|| ,s)ds
n n
p (cid:15)
min 0
Cr C (cid:90) r (cid:112)
≤ + sup logN(F ,||·|| ,s)ds
n n
p (cid:15) p
min min 0 n≥1
In the second-to-last step, we used the fact that log(1 + N) ≤ 1 + logN since the covering
number is always at least one. The upper bound is vanishing as r ↓ 0 so there exists r∗
sufficiently small so that the upper bound is less than δ/3.
For large enough n, P (µˆ ∈ F ) and P (||µˆ − µ∗ || ≤ r∗) are both at least
n1,n n n n1,n n 1,n n
1 − δ/3. Thus, with probability at least 1 − δ, |G (µˆ ) − G (µ∗ )| ≤ (cid:15). Since (cid:15),δ are
n 1,n n 1,n
arbitrary, this shows that |G (µ∗ ) − G (µˆ )| = o (1). Therefore, 1 (cid:80)n (yˆ − y ) =
n 1,n n 1,n p n i=1 1i 1i
1 (cid:80) (cid:15)∗ +o (n−1/2).
n1 Zi=1 1i p
7.1.6 Proof of Theorem 4
Proof. By the reverse triangle inequality, we have:
(cid:12) (cid:12)
(cid:12)
(cid:32) (cid:33)1/2(cid:12) (cid:32) (cid:33)1/2
(cid:12) (cid:16) (cid:91) (cid:17)1/2 1 (cid:88) (cid:12) 1 (cid:88)
(cid:12) MSE (1) − ((cid:15)∗ )2 (cid:12) ≤ [µˆ (x )−µ∗ (x )]2
(cid:12) n n 1i (cid:12) n 1,n i 1,n i
1 1
(cid:12) Zi=1 (cid:12) Zi=1
(cid:32)
n
(cid:33)1/2
1 (cid:88)
≤ [µˆ (x )−µ∗ (x )]2
n 1,n i 1,n i
1
i=1
1
= √ ||µˆ −µ∗ ||
p 1,n 1,n n
n
= o (1)
p
Since 1 (cid:80) ((cid:15)∗ )2 ≤ p−1MSE (1) = O(1), convergence of square roots implies the con-
n1 Zi=1 1i n n
vergence of the left-hand side of the above display without the square roots. By the
fourth moment assumption on (cid:15)∗ and the randomization law of large numbers (Lemma
1i
2), | 1 (cid:80) ((cid:15)∗ )2 − MSE (1)| →− p 0. Therefore, |M (cid:91) SE (1) − MSE (1)| →− p 0. A symmetric
n1 Zi=1 1i n n n
(cid:91) p
argument shows that |MSE (0)−MSE (0)| →− 0.
n n
The assumptions of Corollary 1 imply that n[ 1 MSE (1)+ 1 MSE (0)] is bounded away
n1 n n0 n
from zero. Therefore, consistent estimation of MSE (1) and MSE (0) implies the following:
n n
(cid:91) (cid:91)
1 MSE (1)+ 1 MSE (0)
n1 n n0 n →− p 1
1 MSE (1)+ 1 MSE (0)
n1 n n0 n
29

The asymptotic validity of the confidence intervals then follows from Slutsky’s theorem. In
the case where the treatment has no effect and µˆ and µˆ are estimated by the same method,
1 0
then µ∗ = µ∗ so (cid:15)∗ −(cid:15)∗ = 0. This means that the upper bound on σ is exactly σ , and
1,n 0,n 1i 0i n n
again Slutsky’s theorem implies asymptotically exact coverage.
7.1.7 Proof of Theorem 5
Proof. We will use Theorem 9 to prove the result. Define ψ(s) = log(1+es). Assumption
A1 is satisfied, because the loss function is (cid:96)(θ,x,y) = −yx(cid:62)θ+ψ(θ(cid:62)x), which is convex in
θ. The existence of a population solution is assumed, so the first half of assumption A2 does
not require any calculation to verify. However, the growth condition requires an argument.
Let L be a uniform bound on 1 (cid:80)n ||x ||4. Since ψ ¨ is a 1-Lipschitz function, the map
n i=1 i
θ (cid:55)→ ∇2L (θ) is an L-Lipschitz function.
n
(cid:12)(cid:12) (cid:12)(cid:12)
(cid:12)(cid:12)1 (cid:88) n (cid:12)(cid:12)
||∇2L (θ)−∇2L (θ∗ || = (cid:12)(cid:12) (ψ ¨ (θ(cid:62)x )−ψ ¨ (θ∗(cid:62)x )x x(cid:62)(cid:12)(cid:12)
n n 1,n op (cid:12)(cid:12)n i 1,n i i i (cid:12)(cid:12)
(cid:12)(cid:12) (cid:12)(cid:12)
i=1 op
n
1 (cid:88)
≤ |ψ ¨ (θ(cid:62)x )−ψ ¨ (θ∗(cid:62)x )|·||x x(cid:62)||
n i 1,n i i i op
i=1
n
1 (cid:88)
≤ |(θ−θ∗ )(cid:62)x |·||x ||2
n 1,n i i
i=1
(cid:32) (cid:33)
n
1 (cid:88)
≤ ||x ||3 ||θ−θ∗ ||
n i 1,n
i=1
≤ L||θ−θ∗ ||
1,n
This implies that for all θ in a ball of radius 1λ /L around θ∗ , ∇2L (θ) (cid:23) 1λ I .
2 min 1,n n 2 min d×d
Λ (∇2L (θ)) = inf v(cid:62)∇2L (θ)v
min n n
||v||=1
≥ inf v(cid:62)∇2L (θ∗ )v − sup v(cid:62)[∇2L (θ)−∇2L (θ∗ )]v
n 1,n n n 1,n
||v||=1 ||v||=1
≥ λ −||∇2L (θ)−∇2L (θ∗ )||
min n n 1,n op
≥ λ −L||θ−θ∗ ||
min 1,n
The lower bound is at least 1λ since L||θ − θ∗ || ≤ 1λ . From this, assumption A2
2 min 1,n 2 min
follows from Lemma 1.
Next, we verify assumption A3. This is a straightforward consequence of the inequality
30

(a−b)2 ≤ 2a2 +2b2 and the fact that ψ is a 1-Lipschitz function.
n n
2 (cid:88) 2 (cid:88)
||(cid:96) −(cid:96) ||2 ≤ [x(cid:62)(φ−θ)]2 + (ψ(θ(cid:62)x )−ψ(φ(cid:62)x ))2
θ φ n n i n i i
i=1 i=1
n n
2 (cid:88) 2 (cid:88)
≤ ||x ||2||φ−θ||2 + ||x(cid:62)(θ−φ)||2
n i n i
i=1 i=1
≤ 4L||θ−φ||2
√
Thus, ||(cid:96) −(cid:96) || ≤ 2 L||θ−φ||.
θ φ n
Finally, we need to check that ||µ −µ || ≤ M||θ−φ|| for some constant M < ∞. This
θ φ n n
˙
is simple, since ψ is also a 1-Lipschitz function.
n
1 (cid:88)
||µ −µ ||2 = [ψ ˙ (θ(cid:62)x )−ψ ˙ (φ(cid:62)x )]2
θ φ n n i i
i=1
n
1 (cid:88)
≤ [(θ−φ)(cid:62)x ]2
i
n
i=1
≤ L||θ−φ||2
√
Thus, we may take M = L. Since all the conditions of Theorem 9 are satisfied, the
conclusion follows.
7.1.8 Proof of Theorem 6
Proof. Once again, we will use Theorem 9. Assumption A1 is satisfied because the loss func-
tion (cid:96)(θ,x,y) = −yx(cid:62)θ+exp(θ(cid:62)x) is convex in θ. The existence requirement of Assumption
A2 is a condition of the theorem, and the “growth” condition will be verified using the same
strategy that was used in the proof of Theorem 5. Let L < ∞ be a uniform bound on ||x ||
i
and 1 (cid:80)n y2. For any θ ∈ B (θ∗ ), the triangle inequality and the mean-value theorem
n i=1 1i 1 1,n
imply:
(cid:12)(cid:12) (cid:12)(cid:12)
(cid:12)(cid:12)1 (cid:88) n (cid:16) (cid:17) (cid:12)(cid:12)
||∇L n (θ)−∇2L n (θ 1 ∗ ,n )|| op = (cid:12) (cid:12) (cid:12) (cid:12)n eθ(cid:62)xi −eθ 1 ∗ , (cid:62) n xi x i x(cid:62) i (cid:12) (cid:12) (cid:12) (cid:12)
(cid:12)(cid:12) (cid:12)(cid:12)
i=1 op
1 (cid:88) n (cid:12) (cid:12)
≤ n (cid:12) (cid:12) eθ(cid:62)xi −eθ 1 ∗ , (cid:62) n xi(cid:12) (cid:12) ·||x i x(cid:62) i || op
i=1
n
1 (cid:88)
= eci|θ(cid:62)x −θ∗(cid:62)x |·||x ||2
n i 1,n i i
i=1
In the above display, c is some number between θ(cid:62)x and θ∗(cid:62)x . Since θ is within distance
i i 1,n i
one of θ∗ and ||x || is bounded by L, |c − θ∗(cid:62)x | ≤ |θ(cid:62)x − θ∗(cid:62)x | ≤ L. In particular,
1,n i i 1,n i i 1,n i
31

| c ≤ | θ(cid:62)x +L. | We  | may | then | further | bound |     | the above |     | by: |     |     |     |     |     |
| --- | -------------- | --- | --- | ---- | ------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| i   | i              |     |     |      |         |       |     |           |     |     |     |     |     |     |     |
n
1
|     |     | ||∇L | (θ)−∇2L |     |     | ∗    |     | (cid:88) | eθ ∗ (cid:62) | xi+L||θ−θ |     | ∗      | ||3 |     |     |
| --- | --- | ---- | ------- | --- | --- | ---- | --- | -------- | ------------- | --------- | --- | ------ | --- | --- | --- |
|     |     |      |         |     | (θ  | )||  | ≤   |          | 1 , n         |           |     | ||·||x |     |     |     |
|     |     |      | n       |     | n   | 1 ,n | op  | n        |               |           |     | 1 ,n   | i   |     |     |
i=1
|     |     |     |     |     |     |     |     |     | (cid:32) | n   | (cid:33) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
1
|     |     |     |     |     |     |     |     | L3eL |     | (cid:88) eθ | ∗ (cid:62) xi | ||θ−θ∗ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----------- | ------------- | ------ | --- | --- | --- |
|     |     |     |     |     |     |     | ≤   |      |     |             | 1 , n         |        | ||  |     |     |
|     |     |     |     |     |     |     |     |      | n   |             |               |        | 1,n |     |     |
i=1
|     |     |     |     |     |     |     |     |     | (cid:32) | n   | (cid:33) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
1
|     |     |     |     |     |     |     |     | L3eL |     | (cid:88) | ||θ−θ∗ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     |     | =   |      |     | y        |        |     | ||  |     |     |
|     |     |     |     |     |     |     |     |      | n   |          | 1i     | 1,n |     |     |     |
i=1
L3.5eL||θ−θ∗
|     |     |     |     |     |     |     | ≤   |     |     |     | ||  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,n
SetM = min{1λ /[L3.5eL],1}. Foranyθ ∈ B (θ∗ ),wehaveΛ (∇2L (θ)) ≥ Λ (∇2L (θ∗ ))−
|     |     | 2   | min |     |     |     |     | M   | 1,n |     |     | min | n   | min | n 1,n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
||∇2L (θ)−∇2L
(θ∗ )|| ≥ 1λ , so Lemma 1 can be used to verify Assumption A2.
|     | n   |     | n 1,n | op  | 2 min |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B
Next, we check Assumption A3. Let θ,φ ∈ (θ∗ ) be arbitrary. Again by the mean-
|     |     |     |     |     |     |     |     |     | 1 1,n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | ¯   | ¯   | B   | (θ∗   |     |     |     |     |     |     |
value theorem, there exists vectors θ ,··· ,θ ∈ ) such that the following calculations
|     |     |     |     |     |     | 1   |     | n   | 1 1,n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
hold:
|     | 1 n                           |     |     |      |       | 1        | n          |               |      |                 |          |     |     |     |     |
| --- | ----------------------------- | --- | --- | ---- | ----- | -------- | ---------- | ------------- | ---- | --------------- | -------- | --- | --- | --- | --- |
|     | (cid:88)                      |     |     |      |       | (cid:88) |            | ¯             |      |                 |          |     |     |     |     |
|     | [(cid:96)(θ,x,y)−(cid:96)(φ,x |     |     | ,y   | )]2 = |          | (cid:104)∇ | (cid:96)(θ ,x | ,y   | ),θ−φ(cid:105)2 |          |     |     |     |     |
|     |                               |     |     | i 1i |       |          |            | θ i           | i 1i |                 |          |     |     |     |     |
|     | n                             |     |     |      |       | n        |            |               |      |                 |          |     |     |     |     |
|     | i=1                           |     |     |      |       | i=1      |            |               |      |                 |          |     |     |     |     |
|     |                               |     |     |      |       | (cid:32) |            |               |      |                 | (cid:33) |     |     |     |     |
|     |                               |     |     |      |       | 1        | n          |               |      |                 |          |     |     |     |     |
|     |                               |     |     |      |       |          | (cid:88)   |               | ¯    |                 |          |     |     |     |     |
|     |                               |     |     |      | ≤     |          | ||∇        | (cid:96)(θ    | ,x   | ,y )||2         | ||θ−φ||2 |     |     |     |     |
|     |                               |     |     |      |       |          |            | θ             | i i  | 1i              |          |     |     |     |     |
n
i=1
|     |     |     |     |     |     | (cid:32) |          |     |      |       |            | (cid:33) |          |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ---- | ----- | ---------- | -------- | -------- | --- | --- |
|     |     |     |     |     |     | 1        | n        |     |      |       |            |          |          |     |     |
|     |     |     |     |     |     |          | (cid:88) |     |      |       | ¯(cid:62)x |          |          |     |     |
|     |     |     |     |     | =   |          | ||−y     |     | x +x | exp(θ |            | )||2     | ||θ−φ||2 |     |     |
|     |     |     |     |     |     |          |          | 1i  | i    | i     | i          | i        |          |     |     |
n
i=1
|     |     |     |     |     |     | (cid:32) |          |      |       |          |               |     |            | (cid:33) |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ----- | -------- | ------------- | --- | ---------- | -------- | --- |
|     |     |     |     |     |     | 1        | n        |      |       | 1 n      |               |     |            |          |     |
|     |     |     |     |     |     |          | (cid:88) |      |       | (cid:88) |               |     | ¯(cid:62)x |          |     |
|     |     |     |     |     | ≤   |          | y2||x    |      | ||2 + |          | ||x ||2(exp(θ |     | ))2        | ||θ−φ||2 |     |
|     |     |     |     |     |     |          |          | 1i i |       |          | i             |     | i i        |          |     |
|     |     |     |     |     |     | n        |          |      |       | n        |               |     |            |          |     |
|     |     |     |     |     |     |          | i=1      |      |       | i=1      |               |     |            |          |     |
|     |     |     |     |     |     | (cid:32) |          |      |       |          | (cid:33)      |     |            |          |     |
1 n
|     |     |     |     |     |     |     |     | (cid:88) |       | ¯(cid:62)x |     |          |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --- | -------- | --- | --- | --- |
|     |     |     |     |     | ≤   | L3  | +L2 |          | exp(θ |            | ))2 | ||θ−φ||2 |     |     |     |
i i
n
i=1
|     |     |     |     |     | 1 (cid:80)n |     | ¯(cid:62)x | ))2 |     |     |     | ¯   |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
It only remains to show that (exp(θ is bounded. Since θ is between θ and φ
|     |     |     |     |     | n   | i=1 |     | i i |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which are both in B (θ∗ ), ||θ ¯ − θ∗ || ≤ 1. Therefore, exp(θ ¯(cid:62)x ) ≤ exp(θ∗(cid:62)x + L), and
|     |     |     | 1   |     | i   |     |     |     |     |     |     | i   |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 1,n |     | 1,n |     |     |     |     | i   |     |     | 1,n |     |
it suffices to show that 1 (cid:80)n exp(θ∗(cid:62)x )2 is bounded. However, this follows immediately
i
|      |          |      | (cid:80)n | n i= | 1    | 1 ,n |      |          |          |     |     |     |     |     |     |
| ---- | -------- | ---- | --------- | ---- | ---- | ---- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- |
| from | the fact | that | 1         | y2   | a nd | MS E | (1 ) | are both | bounded. |     |     |     |     |     |     |
|      |          |      |           | 1i   |      |      | n    |          |          |     |     |     |     |     |     |
|      |          |      | n         | i=1  |      |      |      |          |          |     |     |     |     |     |     |
Finally, we need to prove that ||µ −µ || ≤ M||θ −φ|| for some M < ∞. This follows
|     |     |     |     |     |     | θ   | φ   | n   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
32

by essentially the same argument as above. For any θ,φ ∈ B (θ∗ ), we have:
1 1,n
n
1 (cid:88)
||µ −µ ||2 = |exp(θ(cid:62)x )−exp(φ(cid:62)x )|2
θ φ n n i i
i=1
n
1 (cid:88)
= [exp(θ ¯(cid:62)x )(x(cid:62)θ−x(cid:62)φ)]2
n i i i i
i=1
(cid:32) (cid:33)
n
1 (cid:88)
≤ L2 exp(θ ¯(cid:62)x )2 ||θ−φ||2
n i i
i=1
By the above argument, 1 (cid:80)n exp(θ ¯(cid:62)x )2 is bounded.
n i=1 i i
7.1.9 Proof of Theorem 7
ˆ
Lemma 4. (Consistency of θ )
1
Let θ ˆ = argmin (cid:80) [log(y ) − θ(cid:62)x ]2 and let θ∗ = argmin (cid:80)n [log(y ) − θ(cid:62)x ]2.
1,n θ Zi=1 1i i 1,n θ i=1 1i i
Then ||θ ˆ −θ∗ || →− p 0.
1,n 1,n
Proof. We will use Theorem 9. The loss function is (cid:96)(θ,x,y) = [log(y) − θ(cid:62)x]2, which is
convex in θ. The existence of θ∗ is guaranteed by the assumption that 1X(cid:62)X is invertible,
1,n n
and the growth condition is verified by the assumption that ∇2L (θ) = 1X(cid:62)X (cid:23) λ I .
n n min d×d
To check Assumption A3, we need to do some calculations. First, we show that ||θ∗ || is
1,n
bounded. Let L be a uniform bound on ||x ||2 and 1 (cid:80)n log(y )2. Then we have:
i n i=1 1i
(cid:32) (cid:33)1/2
d
1 (cid:88)
||θ∗ || = ||(X(cid:62)X)−1X(cid:62)log(y )|| ≤ λ−1 [X log(y )]2 ≤ L/λ
1,n 1 min n2 •j 1 min
j=1
Then for any θ,φ ∈ B (θ∗ ), the mean-value theorem allows us to write:
1 1,n
n n
1 (cid:88) 1 (cid:88)
[(cid:96)(θ,x ,y ))−(cid:96)(φ,x ,y )]2 = [2(logy −θ ¯(cid:62)x )x(cid:62)(θ−φ)]2
n i 1i i 1i n 1i i i i
i=1 i=1
(cid:32) (cid:33)
n
1 (cid:88)
≤ 4L [logy −θ ¯(cid:62)x ]2 ||θ−φ||2
n 1i i i
i=1
(cid:32) (cid:33)
n n
1 (cid:88) 1 (cid:88)
≤ 8L (logy )2 + L||θ ¯ ||2 ||θ−φ||2
1i i
n n
i=1 i=1
≤ 8L[L+L(L/λ +1)2]·||θ−φ||2
min
Hence, all the assumptions of Theorem 9 are satisifed, so ||θ ˆ −θ∗ || →− p 0.
1,n 1,n
Lemma 5. (Stability of the exponentiated model)
We have ||exp((cid:104)θ ˆ ,·(cid:105))−exp((cid:104)θ∗ ,(cid:105))|| →− p 0.
1,n 1,n n
33

Proof. We use the fact that |ea−eb| ≤ ec|a−b| if |a|,|b| ≤ c. Since with probability tending
√
to one, |θ ˆ(cid:62) x | ≤ L(L/λ +1) ≡ L(cid:48) for all i, we may write:
1,n i min
(cid:32) (cid:33)
n n
1 (cid:88) 1 (cid:88)
[exp(θ ˆ(cid:62) x )−exp(θ∗(cid:62)x )]2 ≤ e2L(cid:48)||x ||2 ||θ ˆ −θ∗ ||2 +o (1)
n 1,n i 1,n i n i 1,n 1,n p
i=1 i=1
The upper bound is vanishing because ||x ||2 is bounded while ||θ ˆ −θ∗ || tends to zero by
i 1,n 1,n
Lemma 4.
Lemma 6. (Consistency of the debiased intercept)
Define a∗ = 1 (cid:80)n [exp(θ∗(cid:62)x ) − y ]. Define aˆ = 1 (cid:80) [exp(θ ˆ(cid:62) x ) − y ]. Then
n n i=1 1,n i 1i n n1 Zi=1 1,n i 1i
|aˆ −a∗| →− p 0.
n n
Proof. We may upper bound |a∗ −aˆ | by the sum of two terms.
n n
(cid:12) (cid:12)
(cid:12) 1 (cid:88) (cid:12)
|a∗ −aˆ | ≤ (cid:12) [exp(θ ˆ(cid:62) x )−exp(θ∗(cid:62)x )](cid:12)
n n (cid:12)n 1,n i 1,n i (cid:12)
(cid:12) 1 (cid:12)
Zi=1
(cid:12) (cid:12)
(cid:12) 1 (cid:88) 1 (cid:88) n (cid:12)
+(cid:12) [exp(θ∗(cid:62)x )−y ]− [exp(θ∗(cid:62)x )−y ](cid:12)
(cid:12)n 1,n i 1i n 1,n i 1i (cid:12)
(cid:12) 1 (cid:12)
Zi=1 i=1
The first of these terms tends to zero by Jensen’s inequality and Lemma 5. The second
term tends to zero by the completely randomized law of large numbers (Lemma 2). The
conditions needed to use the completely randomized law of large numbers are satisfied be-
cause 1 (cid:80)n [exp(θ∗(cid:62)x )−y ]2 ≤ 2 (cid:80)n (exp(θ∗(cid:62)x ))2+ 2 (cid:80)n y2. Since θ∗ and ||x || are
n i=1 1,n i 1i n i=1 1,n i n i=1 1i 1,n i
bounded (see the proof of Lemma 4), the first term in this sum is O(1). The second term is
bounded by the assumption of Theorem 7.
Lemma 7. (Consistency of second-stage OLS coefficients)
Define the following quantities:
(cid:88)
β ˆ ≡ (β ˆ ,β ˆ ) = argmin (y −[β +β exp(θ ˆ(cid:62) x )])2
n 0,n 1,n 1i 0 1 1,n i
(β0,β1)
Zi=1
n
(cid:88)
β∗ ≡ (β∗ ,β∗ ) = argmin (y −[β +β exp(θ∗(cid:62)x )])2
n 0,n 1,n 1i 0 1 1,n i
(β0,β1)
i=1
Then ||β ˆ −β∗|| →− p 0.
n n
Proof. We start by proving that |β ˆ −β∗ | →− p 0. Both can be written explicitly:
1,n 1,n
1 (cid:80) y exp(θ ˆ(cid:62) x )
β ˆ = n1 Zi=1 1i 1,n i (34)
1,n 1 (cid:80) [exp(θ ˆ(cid:62) x )]2
n1 Zi=1 1,n i
1 (cid:80)n y exp(θ∗(cid:62)x )
β∗ = n i=1 1i 1,n i (35)
1,n 1 (cid:80)n [exp(θ∗(cid:62)x )]2
n i=1 1,n i
34

The difference between the numerator of (34) and the numerator of (35) is converging to
zero. To prove this, we first add and subtract a term, then apply the triangle inequality.
|     | (cid:12)   |              |     |          |            | (cid:12) (cid:12) |          |          |              |     | (cid:12)         |     |     |
| --- | ---------- | ------------ | --- | -------- | ---------- | ----------------- | -------- | -------- | ------------ | --- | ---------------- | --- | --- |
|     | (cid:12) 1 |              | 1   | n        |            | (cid:12) (cid:12) | 1        | (cid:16) |              |     | (cid:17)(cid:12) |     |     |
|     | (cid:88)   | eθˆ (cid:62) |     | (cid:88) | ∗ (cid:62) |                   | (cid:88) |          | eθˆ (cid:62) |     | ∗ (cid:62)       |     |     |
(cid:12) y 1 ,n xi − y eθ 1 , n xi (cid:12) ≤ (cid:12) y 1 ,n xi −eθ 1 , n xi (cid:12)
|     | (cid:12)n 1i |     |     | 1i  |     | (cid:12) (cid:12)n |     | 1i  |     |     | (cid:12) |     |     |
| --- | ------------ | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | -------- | --- | --- |
n
|     | (cid:12) 1 Zi=1 |     |     | i=1 |     | (cid:12) (cid:12) | 1 Zi=1 |     |                    |     | (cid:12)  |     |     |
| --- | --------------- | --- | --- | --- | --- | ----------------- | ------ | --- | ------------------ | --- | --------- | --- | --- |
|     |                 |     |     |     |     | (cid:124)         |        |     | (cid:123)(cid:122) |     | (cid:125) |     |     |
(a)
|     |     |     |     |     |     | (cid:12)  |          |      |            |          |      | (cid:12)         |     |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ---- | ---------- | -------- | ---- | ---------------- | --- |
|     |     |     |     |     |     | (cid:12)  | 1        |      |            | 1 n      |      | (cid:12)         |     |
|     |     |     |     |     |     |           | (cid:88) |      | ∗ (cid:62) | (cid:88) |      | ∗ (cid:62)       |     |
|     |     |     |     |     |     | +(cid:12) |          | y eθ | 1 , n xi − |          | y eθ | 1 , n xi(cid:12) |     |
|     |     |     |     |     |     | (cid:12)n |          | 1i   |            |          | 1i   | (cid:12)         |     |
n
|     |     |     |     |     |     | (cid:12)  | 1 Zi=1 |     |                    | i=1 |     | (cid:12)  |     |
| --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ------------------ | --- | --- | --------- | --- |
|     |     |     |     |     |     | (cid:124) |        |     | (cid:123)(cid:122) |     |     | (cid:125) |     |
(b)
|     |     |     |     | (cid:80)n |     | (cid:80)n |     | ˆ(cid:62) |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- |
The term (a) is less than ( 1 y2)1/2( 1 [exp(θ x ) − exp(θ∗(cid:62)x )]2)1/2. Since
|     |     |     | n1  | i=1 | 1i  | n1  | i=1 | 1,n | i   |     | 1,n | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 (cid:80)n y2 isboundedbytheassumptionsofTheorem7and 1 (cid:80)n [exp(θ ˆ(cid:62) x )−exp(θ∗(cid:62)x )]2 →
|        |     |     |     |     |     |     |     |     |        |     |     | i   | i p |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
| n1 i=1 | 1i  |     |     |     |     |     |     |     | n1 i=1 |     | 1,n |     | 1,n |
0 by Lemma 5, the term (a) is vanishing in probability. The term (b) is vanishing by the
completely randomized law of large numbers (Lemma 2). The assumptions needed to use
the completely randomized law of large numbers are satisfied because exp(θ∗(cid:62)x ) is bounded
|     |     |     |     |     |     |     |     |     |     |     | 1,n | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)n
| (see the | proof of Lemma |     | 4) and | so is | 1     | y2. |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |                |     |        |       | n i=1 | 1i  |     |     |     |     |     |     |     |
By exactly the same argument, the difference between the denominators of (34) and
|     |     |     |     |     |     |     |     |     |     | ˆ   |     | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(35) can also be seen to be vanishing. This is enough to prove |β −β∗ | →− 0, since the
|             |         |            |          |      |          |          |          |          |     | 1,n | 1,n      |     |             |
| ----------- | ------- | ---------- | -------- | ---- | -------- | -------- | -------- | -------- | --- | --- | -------- | --- | ----------- |
| denominator | in (35) | is bounded |          | away | from     | zero.    |          |          |     |     |          |     |             |
|             |         |            |          |      |          |          |          |          |     |    |          |     |            |
|             |         |            | (cid:32) |      | (cid:33) | (cid:32) |          | (cid:33) |     |     | (cid:34) |     | (cid:35)1/2 |
| 1 n         |         |            | 1        | n    |          |          | 1 n      |          |     |     | 1 n      |     |             |
| (cid:88)    |         |            | (cid:88) |      |          |          | (cid:88) |          |     |     | (cid:88) |     |             |
[exp(θ ∗ (cid:62) x )]2 ≥ exp θ ∗ (cid:62) x = exp y ≥ exp− (logy )2
|     | 1 , n i |     |     | 1 , n | i   |     |     | 1i  |     |     |     |     | 1i  |
| --- | ------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| n   |         |     | n   |       |     |     | n   |     |     |     | n   |     |      |
| i=1 |         |     | i=1 |       |     |     | i=1 |     |     |     | i=1 |     |      |
Since 1 (cid:80)n (logy )2 is bounded above, the lower bound is bounded below.
1i
|     | n i=1 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |       |     | ˆ   |     | p   |     |     |     |     |     |     |     |     |
Next, we prove that |β −β∗ | →− 0. Again, both can be written explicitly:
|     |     |     | 0,n | 0,n |          |     |         |           |      |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | ------- | --------- | ---- | --- | --- | --- | ---- |
|     |     |     |     | 1   | (cid:88) |     |         |           |      |     |     |     |      |
|     |     |     | β ˆ | =   | [y       | −β  | ˆ exp(θ | ˆ(cid:62) | x )] |     |     |     | (36) |
|     |     |     | 0,n |     |          | 1i  | 1,n     |           | i    |     |     |     |      |
|     |     |     |     | n   |          |     |         | 1,n       |      |     |     |     |      |
1
Zi=1
n
|     |     |     |     | 1   | (cid:88) |     |                 |     |     |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     | β∗  | =   | [y       | −β∗ | exp(θ∗(cid:62)x |     | )]  |     |     |     | (37) |
|     |     |     |     |     | 1i       |     |                 |     | i   |     |     |     |      |
|     |     |     | 0,n | n   |          | 1,n |                 | 1,n |     |     |     |     |      |
i=1
35

The difference between these two is bounded by the sum of of three terms:
(cid:12) (cid:12)
(cid:12) 1 (cid:88) 1 (cid:88) n (cid:12)
|β ˆ −β∗ | ≤ (cid:12) y − y (cid:12)
0,n 0,n (cid:12)n 1i n 1i(cid:12)
(cid:12) 1 (cid:12)
Zi=1 i=1
(cid:124) (cid:123)(cid:122) (cid:125)
(i)
(cid:12) (cid:12)
(cid:12) 1 (cid:88) (cid:12)
+(cid:12) [β ˆ exp(θ ˆ(cid:62) x )−β∗ exp(θ∗(cid:62)x )(cid:12)
(cid:12)n 1,n 1,n i 1,n 1,n i (cid:12)
(cid:12) 1 (cid:12)
Zi=1
(cid:124) (cid:123)(cid:122) (cid:125)
(ii)
(cid:12) (cid:12)
(cid:12) 1 (cid:88) 1 (cid:88) n (cid:12)
+(cid:12) β∗ exp(θ∗(cid:62)x )− β∗ exp(θ∗(cid:62)x )(cid:12)
(cid:12)n 1,n 1,n i n 1,n 1,n i (cid:12)
(cid:12) 1 (cid:12)
Zi=1 i=1
(cid:124) (cid:123)(cid:122) (cid:125)
(iii)
The first and third terms are o (1) by the completely randomized law of large numbers (to
p
verify the assumptions on (iii), use the fact that the denominator of β∗ is bounded below
1,n
and also exp(θ∗(cid:62)x ) is bounded). To kill the second term, add and subtract β ˆ exp(θ∗(cid:62)x )
1,n i 1,n 1,n i
ˆ
and then use the Cauchy-Schwarz inequality along with Lemma 5 and the conclusion |β −
1,n
β∗ | →− p 0.
1,n
Lemma 8. (Smoothness of debiased and post-OLS models)
Let φ = (β ,β ,θ). Define µ (x) = β +β exp(θ(cid:62)x). Then for all φ,φ(cid:48) with ||φ|| ,||φ(cid:48)|| ≤
0 1 φ 0 1 ∞ ∞
B, we have:
||µ −µ || ≤ M||φ−φ(cid:48)||
φ φ(cid:48) n
for some M not depending on n.
Proof. First, we use the triangle inequality to split up ||µ −µ || into more easily manage-
φ φ(cid:48) n
able terms.
||µ −µ || ≤ |β −β(cid:48)|+||µ −µ || +||µ −µ ||
φ φ(cid:48) n 0 0 0,β1,θ 0,β
1
(cid:48),θ n 0,β
1
(cid:48),θ 0,β
1
(cid:48),θ(cid:48) n
To analyze the second term, let L < ∞ be a uniform bound on ||x || .
i 1
(cid:32)
n
(cid:33)1/2
1 (cid:88)
||µ −µ || = (β −β(cid:48))2exp(θ(cid:62)x )2 ≤ exp(2LB)|β −β(cid:48)|
0,β1,θ 0,β 1 (cid:48),θ n n 1 1 i 1 1
i=1
To analyze the third term, we use the local Lipschitz property of the exponential function.
(cid:32)
n
(cid:33)1/2
1 (cid:88)
||µ −µ || = (β(cid:48))2[exp(θ(cid:62)x )−exp(θ(cid:48)(cid:62)x )]2
0,β 1 (cid:48),θ 0,β 1 (cid:48),θ(cid:48) n n 1 i i
i=1
≤ B(eLB)|θ(cid:62)x −θ(cid:48)(cid:62)x |
i i
≤ LBeLB ·||θ−θ(cid:48)||
36

Putting things together gives ||µ −µ || ≤ |β −β(cid:48)|+M |β −β(cid:48)|+M ||θ−θ(cid:48)|| for some
|      |        |             |        |         | φ          | φ(cid:48) | n   | 0            | 0     | 1 1        | 1          | 2           |     |
| ---- | ------ | ----------- | ------ | ------- | ---------- | --------- | --- | ------------ | ----- | ---------- | ---------- | ----------- | --- |
| M ,M | . Then | if          | we set | M       | = 2max{1,M |           | ,M  | } we         | have: |            |            |             |     |
| 1    | 2      |             |        |         |            |           | 1   | 2            |       |            |            |             |     |
|      |        |             |        |         |            |          |     |              |       |            |            |             |    |
|      |        |             |        |         |            |           |     |              |       |            | (cid:32) d | (cid:33)1/2 |     |
|      |        |             |        |         |            |           |     | (cid:48)|+|β |       | (cid:48)|+ | (cid:88)   | (cid:48))2  |     |
|      | ||µ    | −µ          | || ≤   | max{1,M | ,M         | }|β      | −β  |              |       | −β         |            | (θ −θ       |    |
|      |        | θ θ(cid:48) | n      |         | 1          | 2         | 0   | 0            | 1     | 1          |            | j j         |     |
j=1
|     |     |     |     |     |     |     | (cid:32) |     |     |     |     |     | (cid:33)1/2 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ----------- |
d
(cid:88)
|     |     |     | ≤   | 2max{1,M |     | ,M } | |β  | −β(cid:48)|2 | +|β | −β(cid:48)|2 | +   | (θ −θ(cid:48))2 |     |
| --- | --- | --- | --- | -------- | --- | ---- | --- | ------------ | --- | ------------ | --- | --------------- | --- |
|     |     |     |     |          | 1   | 2    | 0   | 0            |     | 1 1          |     | j j             |     |
j=1
|             |     |          | =          | M||φ−φ(cid:48)|| |              |     |            |     |        |     |     |     |     |
| ----------- | --- | -------- | ---------- | ---------------- | ------------ | --- | ---------- | --- | ------ | --- | --- | --- | --- |
|             |     |          |            |                  | √            | √   | √ √        |     |        |     |     |     |     |
| where       | we  | used the | inequality |                  | a+           | b ≤ | 2          | a+b | twice. |     |     |     |     |
| Proposition |     | 2.       | (Proof     | for              | the debiased |     | estimator) |     |        |     |     |     |     |
The sequence of debiased estimators {µˆdb } is stable and has typically simple realizations.
1,n
µdb∗
Proof. Define the “population” debiased regression function by:
1,n
n
1 (cid:88)
|     |     |     |     | µdb∗(x) | := exp(θ∗(cid:62)x)− |     |     |     | [exp(θ∗(cid:62)x | )−y   |     | ].  |     |
| --- | --- | --- | --- | ------- | -------------------- | --- | --- | --- | ---------------- | ----- | --- | --- | --- |
|     |     |     |     | 1,n     |                      | 1,n |     |     |                  | 1,n i | 1i  |     |     |
n
i=1
|     |     |     |     |     |     |     |     | (cid:124) |     | (cid:123)(cid:122) | (cid:125) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------ | --------- | --- | --- |
|     |     |     |     |     |     |     |     |           |     | =a∗ n              |           |     |     |
where θ∗ is defined in Lemma 4. The following calculation shows that ||µˆdb − µdb∗|| is
n
|           | 1,n |                 |     |      |         |     |          |           |     |     |     | 1,n | 1,n |
| --------- | --- | --------------- | --- | ---- | ------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
| vanishing |     | in probability, |     | i.e. | {µˆdb } | is  | a stable | sequence. |     |     |     |     |     |
|           |     |                 |     |      | 1,n     | n≥1 |          |           |     |     |     |     |     |
ˆ
|     |     | ||µˆdb | −µdb∗|| |       | ≤ ||exp((cid:104)θ |     | ,·(cid:105))−exp((cid:104)θ∗ |     |     | ,·(cid:105))|| | +||aˆ | −a∗|| |     |
| --- | --- | ------ | ------- | ----- | ------------------ | --- | ---------------------------- | --- | --- | -------------- | ----- | ----- | --- |
|     |     |        | 1,n     | 1,n n |                    | 1,n |                              |     | 1,n | n              | n     | n n   |     |
ˆ
|     |     |     |     |     | = ||exp(θ |     | ,·(cid:105))−exp(θ∗ |     | ,·(cid:105))|| | +         | |a        | −a∗|                         |     |
| --- | --- | --- | --- | --- | --------- | --- | ------------------- | --- | -------------- | --------- | --------- | ---------------------------- | --- |
|     |     |     |     |     |           | 1,n |                     |     | 1,n            | n         |           | n n                          |     |
|     |     |     |     |     | (cid:124) |     | (cid:123)(cid:122)  |     |                | (cid:125) | (cid:124) | (cid:123)(cid:122) (cid:125) |     |
=op(1)byLemma6
=op(1)byLemma5
Tocheckthat{µˆdb } hastypicallysimplerealizations,defineF = {µ (x) = exp(θ(cid:62)x)−
|     |     |     | 1,n n≥1 |     |     |     |     |     |     |     | n   | −a,1,θ |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
a : |a − a∗| ≤ 1,||θ − θ∗ || ≤ 1}. Then P (µˆdb ∈ F) ≥ 1 − P (|aˆ − a∗| >
|     |     | n   |     |     | 1,n |     |     | n1,n | 1,n |     |     | n1,n | n n |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- |
1) − P (||θ ˆ − θ∗ || > 1). Since these two probabilities are vanishing by Lemma 5
|     | n1,n | 1,n |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,n
and Lemma 6, we have P (µˆdb ∈ F) → 1. Since a∗ and θ∗ are bounded, Lemma 8 and
n1,n
|     |     |     |     |     | 1,n |     |     |     | n   | 1,n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the argument from Example 2 show that F satisfies the entropy integral condition.
n
| Proposition |     | 3.  | (Proof | for | the second-stage |     |     | OLS |     | estimator) |     |     |     |
| ----------- | --- | --- | ------ | --- | ---------------- | --- | --- | --- | --- | ---------- | --- | --- | --- |
The sequence of second-stage OLS estimators {µˆols2} is stable and has typically simple
|     |     |     |     |     |     |     |     | 1,n | n≥1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
realizations.
Proof. Define the “population” second-stage OLS regression function µols2∗ by:
1,n
|     |     |     |     |     | µols2∗(x) | :=  | β∗  | +β∗ | exp(θ∗(cid:62)x) |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |     |     |     |     | 1,n       |     | 0,n | 1,n |                  | 1,n |     |     |     |
37

p
where β∗ and β∗ are defined in Lemma 7. Then ||µˆols2 − µols2∗|| →− 0 by first splitting
|      | 0,n          | 1,n |     |     |     |     |     | 1,n | 1,n n |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
| into | three terms, |     |     |     |     |     |     |     |       |     |     |
ˆ
|     |     | ||µˆols2 | −µols2∗|| | ≤     | |β  | −β∗            | |               |                |                |     |     |
| --- | --- | -------- | --------- | ----- | --- | -------------- | --------------- | -------------- | -------------- | --- | --- |
|     |     | 1,n      |           | 1,n n | 0,n | 0,n            |                 |                |                |     |     |
|     |     |          |           |       | ˆ   |                | ˆ               |                | ˆ              |     |     |
|     |     |          |           | +||β  |     | exp((cid:104)θ | ,·(cid:105))−β∗ | exp((cid:104)θ | ,·(cid:105))|| |     |     |
|     |     |          |           |       | 1,n |                | 1,n             | 1,n            | 1,n            | n   |     |
ˆ
|     |     |     |     | +||β∗ |     | exp((cid:104)θ | ,·(cid:105))−β∗ | exp((cid:104)θ∗ | ,·(cid:105))|| |     |     |
| --- | --- | --- | --- | ----- | --- | -------------- | --------------- | --------------- | -------------- | --- | --- |
|     |     |     |     |       | 1,n |                | 1,n             | 1,n             | 1,n            | n   |     |
then applying Lemma 7 and Lemma 5 to kill off each term in the upper bound. Lemma 5 ca
be applied on the final summand because β∗ is bounded. This can be seen by examining
1,n
the ratio formula for β∗ given in the proof of Lemma 4. The proof of that Lemma gives a
1,n
uniformlowerboundofthedenominatorinthatratio, andtheboundednessofthenumerator
(cid:80)n
| follows | because | 1   | y2,    | ||x ||, and | θ∗  | are | all bounded. |     |     |     |     |
| ------- | ------- | --- | ------ | ----------- | --- | --- | ------------ | --- | --- | --- | --- |
|         |         | n   | i=1 1i | i           | 1,n |     |              |     |     |     |     |
The “typically simple realizations” condition is checked in the same way as in the case
of the debiased estimator, using Lemma 8 and the argument from Example 1.
| 7.1.10 | Proof | of Theorem |     | 8   |     |     |     |     |     |     |     |
| ------ | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. Prediction unbiasedness is established in Barlow & Brunk (Barlow and Brunk, 1972).
First, we will prove that {µˆ } has “typically simple realizations.” Without loss of gener-
1,n n≥1
ality, suppose that [a,b] = [0,1]. By Lemma 9.11 in Kosorok (2008), the class M of monotone
R
functions taking into [0,1] satisfies the following metric entropy bound
K
|     |     |     |     |     | logN(M,||·|| |     | ,s) | ≤   |     |     | (38) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ---- |
n
s
for all s ∈ (0,1) and any n ≥ 1. In the above display, K < ∞ is a universal constant. Let
| F = | M. Using | (38), | we may | write: |     |     |     |     |     |     |     |
| --- | -------- | ----- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
n
|     |     |     | (cid:90) 1 |           |        |       |     | (cid:90) 1 |     |     |     |
| --- | --- | --- | ---------- | --------- | ------ | ----- | --- | ---------- | --- | --- | --- |
|     |     |     |            | (cid:112) |        |       |     | (cid:112)  |     |     |     |
|     |     |     | sup        | logN(F    | ,||·|| | ,s)ds | ≤   | K/sds      | < ∞ |     |     |
|     |     |     |            |           | n      | n     |     |            |     |     |     |
|     |     |     | 0 n≥1      |           |        |       |     | 0          |     |     |     |
Since P(µˆ ∈ F ) = 1 for all n, this shows that {µˆ } satisfies the “typically simple
|               | 1,n | n          |     |     |     |     |     | 1,n |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| realizations” |     | condition. |     |     |     |     |     |     |     |     |     |
Next, we need to show that {µˆ } is stable. Let µ∗ be the solution to the “population”
|     |     |     |     | 1,n |     |     |     | 1,n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ(x))2.
isotonic regression problem. For any µ ∈ M, define (cid:96) (y,x) by (cid:96) (y,x) = (y −
|     |     |     |     |     |     |     |     | µ   | µ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distance14
The between (cid:96) and (cid:96) can be controlled by ||µ − ν|| . This uses the fact that
|     |     |     | µ   | ν   |     |     |     |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14Technically, thedistance||·|| onthefunctions(cid:96) isnotthesameasthedistance||·|| onthefunctions
|     |     |     |     | n   |     | µ   |     |     |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ,becausetheinputisonedimensionhigher. Fornotationalcleanliness,weavoidedintroducinganewnorm.
38

(y −µ(x ))2 is between 0 and 1 for any i.
1i i
n
1 (cid:88)
||(cid:96) −(cid:96) ||2 = [(y −µ(x ))2 −(y −ν(x ))2]2
µ ν n n 1i i 1i i
i=1
n
1 (cid:88)
≤ |(y −µ(x ))2 −(y −ν(x ))2|2
1i i 1i i
n
i=1
n
1 (cid:88)
= |y −µ(x )+y −ν(x )|2 ·|µ(x )−ν(x )|2
1i i 1i i i i
n
i=1
n
4 (cid:88)
≤ |µ(x )−ν(x )|2
i i
n
i=1
= 4||µ−ν||2
n
Hence, the s-covering number of the set L = {(cid:96) : µ ∈ M} in the ||·|| -norm is upper bounded
µ n
by the s/2-covering number of the set M. Thus, if we define R(µ) = 1 (cid:80)n (y − µ(x ))2
n i=1 1i i
and R ˆ (µ) = 1 (cid:80) (y −µ(x ))2, then Proposition 1 implies:
n1 Zi=1 1i i
(cid:20) (cid:21) (cid:20) (cid:21)
1
E sup|[R ˆ (µ)−R ˆ (µ∗ )]−[R(µ)−R(µ∗ )]| = √ E sup|G ((cid:96))−G ((cid:96) )|
1,n 1,n n n n µ∗ 1,n
µ∈M (cid:96)∈L
≤ C/ √ p min (cid:90) 1 (cid:112) logN(M,||·|| ,s/2)ds
n
n
0
≤ C/ √ p min (cid:90) 1 (cid:112) 2K/sds
n
√ 0
≡ C(cid:48)/ n
Hence, for any (cid:15) > 0, the quantity in the expectation on the LHS of the above display is less
than (cid:15) with probability tending to one. On that event, we have:
0 ≤ R(µˆ )−R(µ∗ ) ≤ R ˆ (µˆ )−R ˆ (µ∗ )+(cid:15) ≤ (cid:15)
1,n 1,n 1,n 1,n
Since (cid:15) is arbitrary, this proves |R(µˆ ) − R(µ∗ )| tends to zero in probability. Finally,
1,n 1,n
to prove that ||µˆ − µ∗ || is tending to zero, we appeal to the convexity of the set
1,n 1,n n
M := {µ ∈ Rn : µ ≤ µ ≤ ··· ≤ µ }. With a slight abuse of notation, let µ∗ =
n 1 2 n 1,n
(µ∗ (x ),··· ,µ∗ (x )) ∈ M and let µˆ ∈ M be defined similarly. Then µ∗ is the
1,n (1) 1,n (n) n 1,n n 1,n
projection of y onto M , so (cid:104)µ∗ −y ,µˆ −µ∗ (cid:105) ≥ 0. This allows us to write:
1 n 1,n 1 1,n 1,n
||µˆ −y ||2 = ||(µˆ −µ∗ )+(µ∗ −y )||2
1,n 1 1,n 1,n 1,n 1
= ||µˆ −µ∗ ||2 +||µ∗ −y ||2 +2(cid:104)µˆ −µ∗ ,µ∗ −y (cid:105)
1,n 1,n 1,n 1 1,n 1,n 1,n 1
≥ ||µˆ −µ∗ ||2 +||µ∗ −y ||2
1,n 1,n 1,n 1
||µˆ −µ∗ ||2 ≤ ||µˆ −y ||2 −||µ∗ −y ||2
1,n 1,n 1,n 1 1,n 1
= R(µˆ )−R(µ∗ )
1,n 1,n
p
→− 0
39

| 7.1.11 |     | Proof | of Lemma |     | 1   |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. For all θ ∈ B (θ∗), the mean-value theorem allows us to write:
r
n
1
|     |     | L   |       | L (θ∗)+∇L |            | (θ∗)(θ−θ∗)+ |     |     | (θ−θ∗)(cid:62)∇2L |     | ¯   | )(θ−θ∗) |      |
| --- | --- | --- | ----- | --------- | ---------- | ----------- | --- | --- | ----------------- | --- | --- | ------- | ---- |
|     |     |     | (θ) = |           |            |             |     |     |                   |     | (θ  |         |      |
|     |     |     | n     | n         | n          | n n         |     | n   | 2                 | n   | n   | n       |      |
|     |     |     |       | ¯         | λθ+(1−λ)θ∗ |             |     |     |                   |     |     | ∇L      | (θ∗) |
In the above display, θ = for some λ ∈ [0,1]. Using the fact that = 0
|     |     |     |     |     |     | n   |     |     |     |     |     |     | n n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and Λ (∇2L (θ ¯ )) ≥ λ , we may conclude L (θ)−L (θ∗) ≥ 1λ ||θ−θ∗||2. Therefore,
|     | min |     | n   | min |     |     |     | n   | n   |     | min |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | n   | 2   | n   |     |
Assumption A2 is satisfied with the following choice of the function f:
(cid:26)
|     |     |     |     |     |     |     | 1λ  | t2  | t < r |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
min
|     |     |     |     |     |     | f(t) = | 2   |     |       |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     |        | (1λ | r)t | t ≥ r |     |     |     |     |
min
2
| The    | extension |       | to t ≥     | r was | by convexity. |     |     |     |     |     |     |        |     |
| ------ | --------- | ----- | ---------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | ------ | --- |
| 7.1.12 |           | Proof | of Theorem |       | 9             |     |     |     |     |     |     |        |     |
|        |           |       |            |       |               |     |     |     |     |     |     | Rd+1 R |     |
Proof. First, we prove a useful uniform convergence result. Let (cid:96) : → be defined
θ
by (cid:96) (x,y) = (cid:96)(θ,x,y). For any radius κ ≥ 0, define F (κ) := {(cid:96) : ||θ − θ∗|| ≤ κ}. If
|     | θ   |     |      |       |     |     |     |     |     | n   | θ   |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | √    |       |     |     |     |     |     |     |     | n   |     |
|     | G   |     | n[Lˆ | (θ)−L |     |     |     |     |     |     |     |     |     |
we set (θ) = (θ)], then Proposition 1 gives an average-case bound for the
|          |     | n   |       | n    | n   |     |     |     |     |     |     |     |     |
| -------- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| supremum |     | of  | G (θ) | near | θ∗. |     |     |     |     |     |     |     |     |
n
n
|     |     | (cid:34) |     |     |     | (cid:35) |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
|     |     |     |            |          |     |       |        |     | ∞ (cid:112) |        |                   |       |      |
| --- | --- | --- | ---------- | -------- | --- | ----- | ------ | --- | ----------- | ------ | ----------------- | ----- | ---- |
|     |     | E   |            | |G (θ)−G |     | (θ∗)| |        |     |             |        |                   |       |      |
|     |     |     | sup        |          |     |       | ≤ (C/p |     | )           | logN(F | (κ),||·||(cid:48) | ,s)ds | (39) |
|     |     |     |            | n        |     | n n   |        | min |             |        | n                 | n     |      |
|     |     |     | ||θ−θ∗||≤κ |          |     |       |        |     | 0           |        |                   |       |      |
n
(cid:80)n
In the above display, C is a universal constant and ||f − g||(cid:48) := (1 [f(x ,y ) −
|     |     |     |     |     |     |     |     |     |     | n   |     | n i=1 i,n | 1i,n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- |
g(x ,y )]2)1/2. If κ is smaller than the radius r from assumption A3, then the s-covering
i,n 1i,n
number of (F (κ),|| · || ) can be bounded by the (s/L)-covering number of the Euclidean
|     |         |     | n   | n   |     |     |     |     |      |      |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
|     | B (θ∗); |     |     |     |     |     |     |     | }N B | (θ∗) |     |     | }N  |
ball this is because any (s/L)-covering {θ of gives an s-covering {(cid:96) .
|     | κ   | n   |     |     |     |     |     | i   | i=1 | κ n |     |     | θi i=1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
It can be shown that the (s/L)-covering number of a Euclidean ball of radius κ is bounded
by κd(1+2L/s)d (see Chapter 4 of Vershynin (2018)). Therefore, the upper bound can be
| further |     | bounded  | as        | follows: |                   |       |     |            |                  |               |         |     |     |
| ------- | --- | -------- | --------- | -------- | ----------------- | ----- | --- | ---------- | ---------------- | ------------- | ------- | --- | --- |
|         |     | (cid:90) | ∞         |          |                   |       |     | (cid:90) ∞ |                  |               |         |     |     |
|         |     |          | (cid:112) |          |                   |       |     |            | (cid:112) logN(B |               |         |     |     |
|         |     |          | logN(F    |          | (κ),||·||(cid:48) | ,s)ds | ≤   |            |                  | (θ∗),(cid:96) | ,s/L)ds |     |     |
|         |     |          |           |          | n                 | n     |     |            |                  | κ             | n 2     |     |     |
|         |     |          | 0         |          |                   |       |     | 0          |                  |               |         |     |     |
(cid:90) κ
(cid:112)
|     |     |     |     |     |     |     | ≤   |     | dlogκ+dlog(1+2L/s)ds |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 0   |                      | √   |     |     |     |
(cid:112)
|     |     |     |     |     |     |     | ≤   | κ   | dlogκ+ | 8dLκ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | --- | --- |
In particular, for any κ, the upper bound in (39) is bounded by a constant M(κ) :=
|     |     | √   |     | √   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Lˆ
(C/p )(κ dlogκ + 8dLκ) not depending on n. The conclusion sup (θ) −
|     | min      |     |       |        |     |           |      |          |     |             |     | ||θ−θ∗||≤κ | n   |
| --- | -------- | --- | ----- | ------ | --- | --------- | ---- | -------- | --- | ----------- | --- | ---------- | --- |
| Lˆ  |          |     |       |        |     |           |      |          |     |             |     | n          |     |
|     | (θ∗)]−[L |     | (θ)−L | (θ∗)]| | →   | 0 follows | from | Markov’s |     | inequality. |     |            |     |
|     | n n      |     | n     | n      | n   | p         |      |          |     |             |     |            |     |
40

ˆ
Now, we are ready to prove ||θ −θ∗|| → 0. Let (cid:15) ∈ (0,r) be arbitrary. For all large n,
|     |     |     | n   | n p |     |     |
| --- | --- | --- | --- | --- | --- | --- |
L (θ)−L
(θ∗) ≥ f((cid:15)) > 0 whenever ||θ −θ∗|| = (cid:15). By the preceding uniform convergence
| n   | n n |     |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Lˆ (θ)−Lˆ
result, that means (θ∗) ≥ f((cid:15))/2 simultaneously for all θ satisfying ||θ−θ∗|| = (cid:15)
|     |     | n   | n n |     |     | n   |
| --- | --- | --- | --- | --- | --- | --- |
ˆ B
with probability going to one. By convexity, that event implies θ ∈ (θ∗). Since (cid:15) is
n (cid:15) n
ˆ −θ∗||
| arbitrary, | that proves | ||θ | →   | 0.  |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
|            |             | n   | n p |     |     |     |
B (θ∗),
Ifthemapθ (cid:55)→ µ isalsosmoothinthesense||µ −µ || ≤ M||θ−φ||forallθ,φ ∈
|     |     | θ   |     |     | θ φ n | r n |
| --- | --- | --- | --- | --- | ----- | --- |
then stability follows immediately by setting µ∗ = µ . The “typically simple realizations”
θ ∗
|     |     |     |     |     | n n |     |
| --- | --- | --- | --- | --- | --- | --- |
condition can be verified by setting F = {µ : ||θ −θ∗|| ≤ 1}. This follows by once again
|     |     |     |     | n θ |     |     |
| --- | --- | --- | --- | --- | --- | --- |
n
using the covering numbers of the ball B (θ∗) to upper bound the covering number of F –
|              |     |                |         | 1 n |     | n   |
| ------------ | --- | -------------- | ------- | --- | --- | --- |
| the argument | is  | spelled out in | Example | 2.  |     |     |
41