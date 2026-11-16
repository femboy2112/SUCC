# Constructor: structural evidence, Haar detail and preparatory probe value

Date: 2026-11-15. Parent: `2c73e6388b24c7a66683d089733105d14acda08a`.
Branch: `research/observer-haar-causal-volume-2026-11-15`.

## Scope and status

**Disclosed within the stated finite source model:** a probe can reveal a
connection without revealing the target, increase the expected value of a
subsequent target probe, and have positive two-stage value even when every
one-step information-minus-cost value is negative. The increase has an exact
weighted Haar energy and a quantitative mutual-information lower bound.

**Refuted as an unconditional claim:** a repeated pattern always raises probe
value; policy reweighting creates an unavailable instrument; copying a report
creates new evidence; a marginal connection probability suffices after every
history; statistical dependence or successful feedback implies entanglement.
Explicit controls below distinguish these statements.

**Not supplied:** a physical source law or an authentic BBP arithmetic law
instantiating this four-state model. Its source, conditional freshness, prior,
target, permitted actions, costs and policy reference measure are declared.
The existing BBP source and its zero seed are untouched. No constant, phase,
normality or physical-force conclusion follows from this experiment.

The model's deep probe is already in the admissible frame. It may be unused or
poorly valued at the current knowledge slice. Promoting its score is different
from constructing a new instrument, adding a missing hypothesis, or proving an
unobserved source law. Those changes require a new declared frame and source
checks. All probability claims below are conditional on the chosen frame.

## Inherited work and the incremental interface

Read before implementation:

- `observational_succ/recursive_observer.py`: exact joint source instruments
  `J_a(x,x',o)`, original/current posteriors, and finite cost-aware Bayes policy.
- `observational_succ/contextual_heuristics.py`: exact target-relative Gini
  reduction, probe ranking, source/epoch/basis receipts, zero-support failure,
  and explicit conditional-law requirements for correlated evidence.
- `observational_succ/heuristic_shape_learning.py`: finite hyper-Bayesian
  learning from declared independent solved tasks; source reuse guards.
- `observational_succ/heuristic_evidence_martingales.py`: classical
  likelihood-ratio martingales under a public-history-predictable policy.
- `observational_succ/source_authentication.py`: model/record separation and
  a finite adaptive null census. Transcript commitment is not source-law proof.
- `observational_succ/aphex_haar_feedback.py` and
  `research/2026-11-09/aphex_haar_feedback/PROOFS.md`: exact centered
  least-squares sign coupling and descent. APH-03 already demonstrates that
  perfect finite fit is not evidence of the original source's Haar behavior.

The increment here is the explicit chain

\[
\text{structural posterior}
\longmapsto \text{mixed binary Haar coefficient}
\longmapsto \text{exact projection energy}
\longmapsto \text{information/option value}
\longmapsto \text{conditional policy odds},
\]

with full joint-state retention and discriminating mutations. Bayesian
conditioning, martingale orthogonality, the information criterion, Jensen's
inequality and the Gibbs variational identity are classical. This is a scoped
repository bridge, not a claim of a new general learning theorem.

Primary classical provenance: C. E. Shannon, *A Mathematical Theory of
Communication* (1948), especially the entropy/conditional-entropy identities
and noisy-channel formulation; the original paper was retrieved at
[Harvard's copy](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf).
D. V. Lindley's *On a Measure of the Information Provided by an Experiment*,
Annals of Mathematical Statistics 27(4), 986–1005 (1956),
[DOI](https://doi.org/10.1214/aoms/1177728069), is the classical experimental-design
reference; the publisher's full text was blocked by a service check in this
run, so none of the proofs below depends on an uninspected passage from it.
All model-specific results are proved directly here.

## C-01. Source, family and exact mixed Haar law

Let `S` be a persistent bit with `P(S=1)=p`, `0<=p<=1`, and let `theta` be an
independent fair sign in `{-1,+1}`. A deep report `Y` obeys

\[
P(Y=y\mid S=1,\theta=t)=\mathbf1_{y=t},\qquad
P(Y=y\mid S=0,\theta=t)=\tfrac12.
\]

When probes are repeated, every fresh noise draw is conditionally independent
given `(S,theta)`. The state itself does not change. A preparatory history `E`
depends on `S` and auxiliary noise only; it has no additional dependence on
`theta`, and prospective deep noise is conditionally independent of that
history given `(S,theta)`. Actions may depend on already public history and
independent policy randomness. On every positive-probability preparatory
history, put `p_E=P(S=1|E)`.

**Claim.** Conditional on `E`, `theta` is still fair and independent of `S`,
and

\[
 P(\theta=t,Y=y\mid E)=\frac{1+p_Ety}{4}.                 \tag{1}
\]

**Proof.** The likelihood of `E` given `(S,theta)` is a function of `S` only.
Bayes' rule therefore preserves the fair `theta` factor. Summing the deep
kernel against the conditional `S` law gives
`(1/2)[p_E 1_{t=y}+(1-p_E)/2]=(1+p_Ety)/4`. Both report and target marginals
are uniform. Relative to the **uniform product reference measure** on
`(theta,Y)`, the density is `1+p_E theta Y`. The functions
`1,theta,Y,theta Y` are orthonormal for that reference measure, so the sole
nonconstant mixed Haar coefficient is `p_E`. This does not say that the same
four functions are orthogonal under the correlated joint law. In particular,

\[
 E[\theta Y\mid E]=p_E,\qquad
 E[\theta\mid E,Y]=p_EY.
\]

Thus the reduction in squared-error Bayes risk for the target sign is exactly

\[
\operatorname{Var}(E[\theta\mid E,Y]\mid E)=p_E^2,         \tag{2}
\]

and the remaining risk is `1-p_E^2`. This is an orthogonal projection energy
in a declared probability space, not a physical energy.

For arbitrary joint beliefs the exact valid replacement is

\[
 D(B;K)=\sum_y P_B(y)
   \big(E_B[\theta\mid y]-E_B\theta\big)^2.
\]

This is implemented as `target_detail_energy`; it does not assume the
independent fair-target family.

## C-02. Information and certified rational enclosures

For the family in C-01, information in natural logarithm units is

\[
 I(p)=I(\theta;Y)
 =\log 2-h\!\left(\frac{1+p}{2}\right)
 =\frac{(1+p)\log(1+p)+(1-p)\log(1-p)}2,                 \tag{3}
\]

with `0 log 0=0`. Consequently

\[
 I(0)=0,\quad I(1)=\log2,\quad
 I'(p)=\operatorname{atanh}p,\quad
 I''(p)=\frac1{1-p^2}\quad(0<p<1).                      \tag{4}
\]

Expanding `atanh p` and integrating from zero yields

\[
 I(p)=\sum_{k\ge1}\frac{p^{2k}}{2k(2k-1)}.              \tag{5}
\]

The endpoint follows by monotone convergence. The positive coefficients and
their sum `log 2` prove the sharp quadratic comparisons

\[
 \frac{p^2}{2}\le I(p)\le(\log2)p^2.                   \tag{6}
\]

The lower constant is approached as `p` tends to zero; the upper constant is
attained at `p=1`. `I` is strictly increasing on `[0,1]` and strictly convex.

For rational `0<=p<1`, define `S_N(p)` as the first `N` terms of (5). Since
the coefficients decrease,

\[
0\le I(p)-S_N(p)
\le\frac{p^{2N+2}}{(2N+2)(2N+1)(1-p^2)}.               \tag{7}
\]

There is also the bound

\[
 I(p)-S_N(p)\le\frac{p^{2N+2}}{2N+1},                  \tag{8}
\]

because the coefficient tail at `p=1` is the positive alternating harmonic
remainder after `2N` terms, bounded by `1/(2N+1)`. The implementation takes
the smaller upper bound. At `p=1` it instead uses

\[
\log2=2\sum_{j\ge0}\frac{(1/3)^{2j+1}}{2j+1},\qquad
R_N\le\frac{2(1/3)^{2N+1}}{(2N+1)(1-1/9)}.             \tag{9}
\]

These formulas give exact rational certificates without a numerical log
oracle. Tests additionally compare them against an independent 90-digit
Decimal logarithm evaluation on a finite grid. The tests check the code;
(7)–(9), not the grid, prove the enclosure for every valid rational input.

## C-03. Fresh patterns, structural Haar detail and option value

Let a coarse sign `C` satisfy

\[
 P(C=+1\mid S=1)=a,\qquad P(C=+1\mid S=0)=b,
 \qquad a,b\in[0,1].
\]

Write `q=pa+(1-p)b`. On positive-probability outcomes,

\[
 p_+=\frac{pa}{q},\qquad
 p_-=\frac{p(1-a)}{1-q}.                               \tag{10}
\]

In the independent fair-target family, `I(theta;C)=0` exactly. The target
remains unresolved even if `C` determines `S` perfectly.

For `0<p<1` and `a>b>0`, a fresh positive observation strictly increases
`p`, and a sequence of `n` conditionally independent positive observations
has posterior

\[
 p_n=\frac{pa^n}{pa^n+(1-p)b^n}.                        \tag{11}
\]

Its odds multiply by `(a/b)^n`, and both (2) and (3) increase. If `a=b`,
they remain fixed; if `0<a<b`, they decrease on that positive sequence.
If `b=0<a`, one possible positive observation establishes `S=1` within the
model. If the record has total probability zero, Bayes' rule supplies no
posterior. Positive-probability observations never create mass on a zero-prior
state. Formula (11) assumes fresh conditional likelihoods; repeated copies
of one realized datum do not satisfy that assumption.

### Exact preparatory Haar energy

For `0<q<1`, let

\[
 h_C=\frac{\mathbf1_{C=+1}-q}{\sqrt{q(1-q)}}.
\]

This has mean zero and squared norm one in the report probability space.
The coefficient of `S` on this weighted binary Haar detail is

\[
 \kappa=E[S h_C]
       =\frac{p(1-p)(a-b)}{\sqrt{q(1-q)}}.
\]

There are only two report values, hence
`E[S|C]-p=kappa h_C`, and

\[
 V:=\operatorname{Var}(p_C)
   =\kappa^2
   =\frac{p^2(1-p)^2(a-b)^2}{q(1-q)}.                  \tag{12}
\]

If `q` is zero or one, `C` is deterministic and `V=0`. The posterior is a
martingale, `E[p_C]=p`, so

\[
 E[p_C^2]-p^2=V.                                      \tag{13}
\]

Thus (12) is simultaneously the coarse structural Haar energy and the
increase in the **expected** deep target-projection energy. It does not
imply that every realized path increases it.

### Preparatory information value

Jensen and (4) give

\[
 E[I(p_C)]\ge I(p),\qquad
 E[I(p_C)]-I(p)\ge\tfrac12 V.                         \tag{14}
\]

For the second inequality, the function `I(x)-x^2/2` is convex on `[0,1]`,
as its second derivative is `x^2/(1-x^2)>=0` in the interior; continuity
extends convexity to the endpoints. Applying Jensen to that function and
using (13) proves the claim. The first inequality is strict exactly when
`p_C` is nonconstant with positive probability. In the coarse binary family,
this occurs precisely when `0<p<1` and `a!=b`. At a degenerate prior or an
uninformative probe there is no promotion.

There is no conflict with zero immediate target information. The chain rule
gives

\[
 I(\theta;C,Y)=I(\theta;Y\mid C)=E[I(p_C)]
              =I(\theta;Y)+I(\theta;C\mid Y).
\]

The coarse report helps interpret a later deep report. Conditional relevance
can be present despite zero marginal target information.

If a deep probe has fixed information cost `d>=0`, the decision to use it or
stop has value `max(I(p)-d,0)`. This function is convex because `I` is convex.
Therefore a free coarse report cannot lower its expected value:

\[
 E[\max(I(p_C)-d,0)]\ge\max(I(p)-d,0).                 \tag{15}
\]

A positive coarse cost must be subtracted. The inequality need not be strict
if all posterior states lie in the stopping region. No monotone-optimal-policy
claim is made for other changing utilities, targets or costs.

### Certified example where one-step greed stops too early

Take `p=1/2`, `a=3/4`, `b=1/4`, deep cost `d=3/20=0.15` nats, and coarse
cost `c=1/100=0.01` nats. Both coarse outcomes have probability `1/2` and give
posteriors `p_-=1/4`, `p_+=3/4`. The exact `N=16` bounds (7) certify

\[
 .031<I(1/4)<.032,\quad .130<I(1/2)<.131,\quad
 .316<I(3/4)<.317.
\]

Every one-step probe has negative net value: the coarse probe gives `-0.01`
and the direct deep probe gives less than `0.131-0.15<0`. But after coarse
success the deep probe is worthwhile; after coarse failure it is not. Thus

\[
 V_{\mathrm{coarse\ then\ optional\ deep}}
  =\tfrac12(I(3/4)-.15)-.01>.073>0.                    \tag{16}
\]

Numerical display only: direct deep `-0.019187964058863027`, coarse-only
`-0.01`, coarse followed by optional deep `0.07318850965175425` nats.
The signs are certified by rational interval inequalities, independently of
the displayed floating-point values. The implemented planner compares only
`stop`, `one deep`, and `coarse then optional deep`; it does not claim an
unrestricted multistep optimum.

The fixed plan that always performs both probes is also beneficial:
`(I(1/4)+I(3/4))/2-c-d>0.0135>0`, using the same rational enclosures.
Its numerical value is `0.013980480852735875` nats. The optional continuation
policy improves on this by avoiding the deep cost after a negative coarse
report. The focused test now certifies both inequalities; the planner returns
the optional-policy value, not the always-deep value.

## C-04. Temporal Haar accumulation is bounded, not pathwise attraction

Let `(H_t)` be any increasing public-history filtration in a single fixed
probabilistic source model. Set `p_t=E[S|H_t]`, and suppose `p_0` is constant.
Adaptive probe selection is allowed; all selection and observation laws must
be represented correctly. Since `S` is bounded, the posterior is a bounded
square-integrable martingale. Write `D_t=p_t-p_{t-1}`. For `s<t`, `D_s` is
`H_{t-1}`-measurable and

\[
 E[D_sD_t]=E[D_sE(D_t\mid H_{t-1})]=0.
\]

The same calculation with `p_{t-1}` removes the cross term in the square.
Telescoping gives the exact orthogonal-energy identity

\[
 E[p_n^2]-p_0^2
 =\sum_{t=1}^n E[(p_t-p_{t-1})^2]
 \le p_0(1-p_0),                                     \tag{17}
\]

where the last step uses `0<=p_n<=1`, hence `p_n^2<=p_n`, and `E[p_n]=p_0`.
For binary history refinements these are weighted Haar details; for general
finite refinements they are orthogonal martingale differences. The energy is
resolved structural variation. Neither the mean belief `E[p_t]` nor every
realized `p_t` increases. Histories consisting only of structural observations
retain the independent fair-target family, so (17) is also the accumulated
expected increase of the potential deep energy `p_t^2`. With arbitrary deep
observations, (17) remains true for `S`, but `p_t^2` need not be the current
deep target-probe energy: the full joint belief is then required.

The exact test enumerates all 32 outcomes at five adaptively chosen coarse
steps, verifies each telescoping increment and the global bound, and includes
adverse paths. The proof, not that finite enumeration, covers all finite `n`.

## C-05. Stochastic action choice and likelihood accounting

For a finite admissible action menu, let reference masses `q_a>=0` sum to one,
real utilities be `V_a`, and `tau>0`. On distributions supported by `q`,

\[
 \pi^*_a=\frac{q_a e^{V_a/\tau}}{\sum_b q_b e^{V_b/\tau}}              \tag{18}
\]

uniquely maximizes `sum_a pi_a V_a - tau KL(pi||q)`. Indeed, with
`Z=sum q exp(V/tau)`, the objective equals

\[
 \tau\log Z-\tau\operatorname{KL}(\pi\Vert\pi^*).
\]

Nonnegativity of KL proves maximality and equality only at `pi=pi*` on that
support. In particular, for supported deep and rival actions,

\[
 \frac{\pi^*_{\rm deep}}{\pi^*_{\rm rival}}
 =\frac{q_{\rm deep}}{q_{\rm rival}}
   \exp\frac{V_{\rm deep}-V_{\rm rival}}\tau.            \tag{19}
\]

In the fair-target family, a rising `p` strictly raises these odds if the deep
utility is `I(p)` minus a fixed cost, the competitor utility and reference
masses are fixed, and both actions are supported. If the rival value also
changes, the conclusion can fail. If `q_deep=0`, no finite score rescues it.
Adding support is an explicit menu/frame change. The numerical implementation
also documents possible floating-point underflow for very unfavorable
supported actions; that is not an exact support theorem.

Writing `beta=1/tau`, the exact low-temperature statement is a limit: as
`beta` tends to infinity with utilities and reference fixed, mass concentrates
on the utility-maximizing supported set, and within that set the limiting
weights are proportional to the reference masses. Factor `exp(beta V_max)`
from numerator and denominator of (18); every strictly lower-utility term
vanishes, proving the statement. Entropy or largest-atom concentration need
not be monotone in `beta` for nonuniform references. For instance,
`q=(99/100,1/100)` and `V=(0,1)` give a uniform policy at `beta=log(99)`;
the initial 99:1 preference has become less concentrated. A dedicated control
checks this distinction.

### Adaptive likelihood ratios

Consider fixed source hypotheses `S=0` and `S=1`. For each history `h`, assume
the same recorded randomized policy `pi_t(a|h)` under both hypotheses and
conditional observation laws `L_s(o|a,h)`. The policy's randomization is
independent of the hidden state conditional on public history. Then a path
likelihood under `s` factors as

\[
 P_s(a_1,o_1,\ldots,a_n,o_n)
 =\prod_t\pi_t(a_t\mid h_{t-1})L_s(o_t\mid a_t,h_{t-1}).
\]

On a path supported by the policy, common selection factors cancel:

\[
 \Lambda_n=\prod_t\frac{L_1(o_t\mid a_t,h_{t-1})}
                              {L_0(o_t\mid a_t,h_{t-1})}.             \tag{20}
\]

Assume full null support for the allowed observation kernels, as the inherited
elementary implementation does. Then

\[
 E_0[\Lambda_{t+1}\mid H_t]
 =\Lambda_t\sum_a\pi_t(a\mid H_t)\sum_o L_1(o\mid a,H_t)
 =\Lambda_t.                                                       \tag{21}
\]

The observation and policy laws may depend on history; they need not be
stationary. Full null support can be weakened to suitable conditional absolute
continuity, but that extension is not needed here.

Two controls are essential. First, if a selector uses unrecorded
state-dependent information, its laws `pi_0` and `pi_1` need not coincide;
the action itself carries an additional `pi_1/pi_0` likelihood factor.
Ignoring it is selection confounding. Second, a public policy's preference
for a promising action is not a new confirmation of the source hypothesis.
Multiplying the common action probability into the evidence a second time
breaks (21). The exact adaptive test enumerates 256 action/outcome paths,
compares the posterior to their full raw likelihoods, obtains `E_0 Lambda=1`,
and rejects the extra-policy-factor mutation.

## C-06. Full joint retention, replay and failure controls

### Marginal reset is unsound

Begin at `p=1/2`. After the deep report `Y=+1`, in state order
`(0,-1),(0,+1),(1,-1),(1,+1)`, the posterior is

\[
 B=(1/4,1/4,0,1/2).
\]

The connection probability remains `1/2`, but the target-positive probability
is now `3/4` and `S` and `theta` are correlated. A second fresh deep probe has
exact target-detail energy `1/12`, not the reset value `p^2=1/4`. This follows
from its joint target/report table

\[
 \begin{pmatrix}1/8&1/8\\1/8&5/8\end{pmatrix}.
\]

At `p=1`, one deep observation determines the target. Its future target
information and projection energy are zero, although `P(S=1)` is still one.
Resetting the joint belief to the fair family would invent one bit of target
uncertainty and one unit of projection energy. The module retains all four
weights. `hidden_link_haar_coefficient` explicitly rejects a belief outside
the fair independent family; the bare family function `I(p)` describes that
family only, not every posterior with the same marginal `p`.

### Copies and zero support

After a recorded coarse `+1`, its perfect copy has conditional likelihood one
for `+1` under every hidden state, so its likelihood ratio is one and its
posterior update is the identity. In contrast, another genuinely fresh
observation from `a=3/4,b=1/4` raises the initial `p=1/2` success posterior
from `3/4` to `9/10`. A name, event ID or source label cannot make a copy fresh.
The inherited receipt layer can reject known duplicates and demand conditional
likelihood declarations; neither that layer nor this finite instrument proves
the empirical independence assumption.

At zero prior mass a positive-probability update preserves zero mass. An event
with zero predictive probability returns no posterior; the repeated-success
helper raises instead. This is a model/support failure to repair, not a
license to invent certainty. Similarly, a zero-reference action stays outside
the mathematical Gibbs support.

### No implication of entanglement or physical attraction

The entire experiment is a classical finite probability model with
identity-state observation kernels. It already exhibits structural relevance,
cross-time dependence, feedback, increasing conditional probe value, and
nontrivial Haar coefficients. Those properties therefore cannot alone
discriminate a quantum mechanism from a classical one. No operational phase
transport or physical-force law is asserted by the word “energy.”

## Implementation and verification receipt

Owned new files only:

- `observational_succ/adaptive_haar_observer.py`.
- `tests/test_adaptive_haar_observer.py`.
- This note.

No added dependencies, branch changes, commits or publication. No full-suite
run was started by this constructor; root owns the inherited baseline.

Exact interfaces require `int`/`Fraction` probabilities and reject bools,
floats, out-of-range values, malformed laws and invalid outcomes. All joint
weights are immutable normalized tuples. Repetition count is capped at 256,
information-series terms at 128, and policy actions at 16. The planner has
only two stages. These bounds constrain operation counts; arbitrary rational
input bit sizes are not capped. Physical source metadata is not inserted into
mathematical values.

The source instrument adapter preserves each `(S,theta)` state exactly and
uses the inherited `JointInstrument`; the tests cross-check every posterior
against the inherited `update_current` implementation. A balanced finite sign
table additionally cross-checks APHEX's covariance/variance normalization. That
calibration does not infer the population model from a finite fit.

Focused execution on 2026-11-15:

```text
python -m unittest tests.test_adaptive_haar_observer -v
Ran 23 tests in 0.030s
OK
```

Coverage includes independent Decimal logs, inherited posterior/instrument
oracles, the 256-path randomized-policy census, 32-path temporal energy
identity, exact two-stage cost certificates, copied evidence, target already
learned, p-only reset, adverse correlations, changing competitors, missing
action support, sign reversal and malformed/budget inputs. Finite checks are
observed evidence of implementation agreement; the universal claims have the
separate proofs above.

Reviewed file SHA-256 at this receipt:

```text
208e5a566b50ff53fc14d38a75ba36c7e7b47bf358d7d1fd0ab790a888de58b8  observational_succ/adaptive_haar_observer.py
58ddfd2257f8c43d59ce21e8ce31617610805ed9197fded19f183429a9f4582e  tests/test_adaptive_haar_observer.py
```

## Closing scoped review — 2026-11-15

**PASS for AH-01 through AH-04** in the root synthesis `THEOREMS.md` at
SHA-256
`eb7c26b99eac112364db19a746e45e979cfc0abf98f34a29e34487586f0b9125`.
The reviewed text was read from the same byte snapshot used to compute this
hash. The full-file hash binds the version; this receipt does not extend the
constructor's audit to AH-05 or later sections.

The initial review at `56e9ddfa3b26493d62a092ce537365fe501a9b00e37f5cdf825b0f853aa21fb3`
identified the need to state the constant initial posterior assumption in the
martingale energy formula, use a complex modulus in the Haar squared norm,
declare conditional independence of policy randomness, specify reference
support and finite utilities, distinguish the fixed and optional two-stage
plans, give the Ville parameter domain, and replace unqualified monotone
temperature/concentration language by the actual asymptotic law.

**All these corrections are resolved in the final reviewed snapshot.** The
full four-state boundary is correctly retained, the Haar metric stays fixed
within each orthogonal decomposition, almost-surely constant reports are
distinguished from informative deterministic kernels, zero action support
cannot be repaired by score reweighting, and both cost examples are scoped to
their finite menus. The probabilistic source model and conditional freshness
remain explicit premises. The inherited/classical provenance labels agree
with the source inventory above; no claim of a new general Bayesian,
martingale or Haar theorem is introduced. Root owns the separate bibliography
and the remaining synthesis sections.

The focused tests were extended by an exact assertion for the always-deep
cost inequality and a nonuniform-reference temperature counterexample. The
final owned-code execution was:

```text
python -m unittest tests.test_adaptive_haar_observer -v
Ran 24 tests in 0.031s
OK
```

This supersedes the initial 23-test receipt while preserving its history.
Final owned code/test hashes:

```text
208e5a566b50ff53fc14d38a75ba36c7e7b47bf358d7d1fd0ab790a888de58b8  observational_succ/adaptive_haar_observer.py
6efcf657b5f782602af59db32844e9e941dc61d5256061cd586f748117e2a080  tests/test_adaptive_haar_observer.py
```

This is a bounded constructor consistency/proof audit, not a new independent
source observation. No main theorem or other agent's production file was edited.
