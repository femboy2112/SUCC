# Future access, the minimal carry register, and an arithmetic intervention pin

**Date:** 2026-10-23. **Parent:** PR #244,
`5e2ba04c8b4ab627b6b0add588609c347346a1a2`.
**Authority:** paper proofs, exact finite controls, and rational interval
certificates. These are mathematical instruments and synthetic readings. No
physical measurement, universal quantum minimizer, or new spectral-cyclicity
proof is claimed. No archival source was modified.

## Hole contract

The target is a universal factorization of an observation together with **all
permitted future continuations**, followed by a sharp arithmetic example. On the
source `N_{>=1}`, can the quotient `q_p(n)=floor((n-1)/p)+1` support successor
without remembering a residue? If not, what is the smallest repair and the
shortest permitted intervention that demonstrates its necessity? A second target
is whether authenticated off-diagonal access identifies the two parameters of
the existing arithmetic operator even with unknown common energy calibration.

The missing edge is action descent after forgetting. It is weaker than a claim
that all observer representations are equivalent, or that an observable
realization determines a physical source. The cheapest falsifier is `p=2`,
`n=1,2`, followed by one successor. Fresh controls use composite radices 4,6 and
primes 11,13; the phenomenon is not itself a prime-selection theorem. Classical
Moore/Mealy behavioral equivalence supplies the language. Finite computation
calibrates the implementation; the all-source result is the proof below.

Read before implementation: `AGENTS.md`, `docs/FOUNDATIONS.md`,
`docs/METHOD.md`, `docs/ARCHITECTURE.md`, `provenance/IMPORT_MANIFEST.json`,
`future_safe_quotient.py`, `operational_yoneda_descent.py`,
`reality_pin_arithmetic.py`, their tests and the Reality Pin arithmetic manuscript.
The foundation import is pinned to originating commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. This lane adds files only.

## OBS-SF1. The arbitrary-carrier behavioral quotient

Let `X` be any set, `A` a set of authorized action names, `T_a:X->X` a total
function for each `a in A`, and `o:X->Y` the declared present observation. No
finiteness, topology, computability or probabilistic premise is required. Words
are executed left to right: `T_(wa)=T_a T_w`, and `T_empty=id`. Set

\[
 x\sim y\quad\Longleftrightarrow\quad
 \forall w\in A^*,\quad o(T_wx)=o(T_wy).
\]

**Theorem.** This is the largest equivalence relation contained in `ker(o)`
that is stable under every authorized action. The quotient `Q=X/~` carries
unique actions `Tbar_a[x]=[T_a x]` and observation `obar[x]=o(x)`. It is the
coarsest autonomous observation-preserving quotient. For every surjective
observation-preserving equivariant map `q:X->Z`, there is a unique
equivariant observation-preserving map `f:Z->Q` satisfying `[x]=f(q(x))`.

**Proof.** An intersection of equality kernels is an equivalence relation;
the empty word gives observation agreement. If `x~y`, then for each `a,w`,
`o(T_w T_a x)=o(T_(aw)x)=o(T_(aw)y)=o(T_w T_a y)`, proving stability.
If `E` is any observation-compatible stable equivalence, induction on word
length gives `x E y => o(T_wx)=o(T_wy)`, so `E subset ~`. This proves maximality,
and stability makes the displayed quotient maps well-defined. For `q`, its
kernel is a stable observation-compatible equivalence, hence is contained in
`~`. Consequently `f(q(x))=[x]` is well-defined; surjectivity makes it unique.
Equivariance and observation preservation follow on representatives. QED.

**Actual category.** Fix `(X,A,T,o)`. Objects are the preceding surjective
quotient maps `q`, with their induced actions and observation. An arrow
`q->q'` is a map `f` with `q'=f q` preserving actions and observation.
Composition is composition of functions, and identities are identity maps;
the preceding proof makes `X->Q` terminal in this category. Thus “minimal” has
an explicit order and a universal property, not merely a bit-count intuition.
Equivalently, the behavior map `B(x)(w)=o(T_wx)` takes values in `Y^(A*)`; on its
image, an action is the derivative `D_a b(w)=b(aw)`.

**Important distinction.** A representation `q` from which the whole behavior
can be decoded need only satisfy `ker(q) subset ~`. That alone does not make its
own update autonomous. For example, take four states a,b,c,d, constant `o`, and
`T(a)=c,T(b)=d,T(c)=c,T(d)=d`. The representation that merges only a,b is
future-sufficient for the constant observation, but its merged state has two
different represented successors c,d. The old `audit_representation` already
separates `future_safe` from `autonomous`; this theorem preserves that distinction.

**Adaptive consequences.** Two `~`-equivalent states cannot be distinguished by
any deterministic finite adaptive policy using only these actions and these
observations: induction keeps public transcripts equal, hence the policy chooses
the same next action. Randomizing the policy independently of the unknown source
does not help: couple the same random seed and use the same induction. No
computable global decision procedure for `~` on arbitrary infinite sources is
asserted. In particular, an infinite behavioral image is not a finite-memory
implementation.

**Partial actions.** Either restrict to a common invariant authorized domain,
or include lawful availability/rejection observations in the state output and
use a corresponding Mealy behavior. One must not declare “unavailable” an
observable unless the actual interface supplies it. Budgets belong in the state
when future access depends on remaining budget; the existing finite
`future_safe_quotient.py` supplies that model.

**Status/provenance.** CLASSICAL, reproved here to expose its source and access
hypotheses. The finite algorithm is already in SUCC; no replacement is added.
This is the behavioral quotient/final-semantics principle of Moore-machine and
coalgebra theory. See Moore, *Gedanken-Experiments on Sequential Machines*
(1956), [original chapter scan](https://www.cs.cmu.edu/~cdm/resources/Moore1956-gedanken-experiments.pdf),
and Rutten, *Universal coalgebra: a theory of systems*, TCS 249 (2000), 3–80,
[primary paper](https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf),
[institutional record](https://ir.cwi.nl/pub/48/).
The current primary records were checked in this round; the proof above is
self-contained and does not rely on an unexplained imported theorem.

## OBS-SF2. Sharp carry repair and finite-horizon information

Fix any integer `p>=2`, not necessarily prime. Write uniquely

\[
 n=p(m-1)+r+1,\qquad m\ge1,\quad 0\le r<p.
\]

The present observer sees `m=q_p(n)`, and its authorized source action is
`S(n)=n+1`. For every `t>=0`,

\[
 q_p(S^tn)=m+\left\lfloor\frac{r+t}{p}\right\rfloor.
\]

**Theorem.** Its all-future equivalence is equality on `N_{>=1}`. In each present
quotient fiber, the minimal supplemental register has exactly `p` states, or
`ceil(log2 p)` bits in a globally fixed-width binary encoding. The pair `(m,r)`
realizes this minimum and transports successor by the controlled carry law.
For a horizon `h>=0`, retaining all observations at times `0,...,h` produces
exactly `min(p,h+1)` classes in each quotient fiber. If `h<p`, those classes are

\[
 \{0,\ldots,p-h-1\},\quad\{p-h\},\quad\ldots,\quad\{p-1\}.
\]

For `h>=p-1` all residues are singletons. The bit lower bound for this bounded
**report task**, given `m`, is `ceil(log2 min(p,h+1))`; such a bounded report
encoding need not be autonomous under indefinitely continued successor.

**Proof.** Different `m` are already separated. In one block let `r<s`. Their
first different quotient occurs at `t=p-s`, where residue `s` crosses the next
block and `r` does not; before that time neither crosses. Since `1<=p-s<=p-1`,
all distinct sources are future-separated. Thus every autonomous future-safe
refinement is injective. Restricting an injective representation to one block
requires at least p supplemental symbols. The actual carry register attains p,
and binary coding gives the stated ceiling. Through `h<p` steps, residues below
`p-h` all give a constant quotient; each remaining residue has a different first
carry time in `1,...,h`, proving the partition formula. For later horizons the
already separated singletons cannot merge. QED.

The smallest failure is `p=2`: `q_2(1)=q_2(2)=1`, while
`q_2(S1)=1 != 2=q_2(S2)`. Thus the failed square is an actual source equation,
not a numerical approximation. No function `Sbar` can satisfy
`q_2 S=Sbar q_2` on all positive integers.

**The repair is probe-relative.** If the present observation instead is
`r=(n-1) mod p`, then residue alone *is* stable under successor and under every
integer multiplier: `S:r->r+1 mod p`, `V_a:r->a(r+1)-1 mod p`. Its future quotient
for those observations and actions stays finite. Adding the quotient-coordinate
probe changes the minimum retained information. “The entire source must always
be retained” is therefore not this theorem.

**No universal history claim.** `(m,r)` reconstructs the current integer address.
Distinct action histories can have the same endpoint; recovering their identity
requires an explicitly retained journal or a history-sensitive probe.

## OBS-SF3. Frozen intervention protocol, calibration and cost

Before inspecting test outcomes, fix the following synthetic interface:
`S` acts once on the current positive integer, and `q_p` is an exact,
nondestructive read of that state. The original `m` is read at time zero.
Read after each successor, stop at the first increase, and otherwise stop after
`p-1` successors. A first carry at time `t` means original residue `r=p-t`;
no carry by `p-1` means `r=0`. Reconstruct `n=p(m-1)+r+1`.

If each successor costs `c_S>=0` and each read costs `c_R>=0`, a transcript
stopping at time t costs exactly `t c_S+(t+1)c_R`. The worst case is
`(p-1)c_S+p c_R`. This protocol uses at most `p-1` successor actions, and this
worst-case action count is optimal in the declared single-source interface:
residues 0 and 1 yield identical observations through time `p-2`, so no adaptive
policy using only unit forward successors and quotient reads can distinguish
them earlier. This is an action lower bound, not a theorem minimizing reads
when reset, jumps, inverse actions or copies become separately available.

Calibration cases are `n=p(m-1)+1` (no carry through p-1 steps) and `n=pm`
(carry on the first step). The null control has a constant observation and remains
aliased forever. Incorrect origin `n//p`, premature stopping, skipped/continued
readings, a wrong quotient jump, and negative costs are rejected. The fresh
holdout radices 11 and 13 and blocks beyond the initial block exercise the same
frozen rule. All are synthetic source interventions; actual physical source
access has not been supplied.

The finite closed-clock test additionally exercises the existing Moore minimizer.
It is explicitly a different carrier with wraparound; its results are not used
to prove the unwrapped theorem above.

## OBS-SF4. The observer object has separately typed authority

A suitable deterministic observer contract consists of the following actual
objects; a metadata string naming one does not construct it.

| Component | Mathematical type / responsibility |
|---|---|
| Carrier and source | Set X, plus a specified map to an authenticated source-label set |
| Dynamics | Authorized alphabet A and total/partial maps T_a on declared domains |
| Histories | Actual words and recorded outcomes; endpoint evaluation is a separate map |
| State / observations | Initial state or law; algebra of permitted functions and output map o |
| Instruments | Outcome-and-poststate maps, not merely scalar output distributions |
| Access language | Legal continuation words or policies, with lawful availability semantics |
| Resources | Cost functions and residual budget; lifted into state when they change access |
| Representation | Map q, its discarded fibers, and explicitly requested descent squares |
| Completion | Chosen topology and convergence maps; no default equivalence across limits |
| Physical realization | External preparation/readout/calibration evidence, separate from existence |

A controlled finite Markov quotient additionally requires, for every action and
each pair in one fiber, equal pushed-forward transition laws on all quotient
fibers (and matching observable costs/availability). This strong lumpability
condition makes one-step quotient transition probabilities well-defined; repeated
conditioning then transports every finite outcome law. It is not implied by
matching only present marginal observations.

For quantum instruments a sufficient transport condition is a trace-preserving
completely positive map `q` and, for each allowed action a and outcome z,

\[
 q\,\mathcal I_{a,z}=\overline{\mathcal I}_{a,z}\,q
\]

on the declared trace-class state domain, with all instruments completely
positive and their sums trace preserving. Composition preserves the square;
trace preservation equates every unnormalized branch weight. This is a scoped
sufficiency theorem by induction, not an existence or minimality theorem for q.
Equality of POVM effects alone supplies no such poststate square. No claim about
physical availability or signed arithmetic positivity follows.

## OBS-SF5. Three arithmetic entries identify shape under affine energy calibration

Retain the exact existing operator from Reality Pin on `ell²(N_{>=1})`:

\[
 K=\log N+\lambda(S+S^*)+
 \sum_{p\ \mathrm{prime}}p^{-\sigma}(V_p+V_p^*)+cI,
 \quad\lambda\in\mathbb R,\quad\sigma>1.
\]

Finite basis vectors and their finite superpositions belong to `D(log N)`.
Let the measured operator be `M=gK+bI`, with common **positive** unknown gain
`g>0` and arbitrary unknown scalar offset `b`. Source basis, relative phases,
shared calibration and access to the stated entries are hypotheses. Set

\[
 x=M_{23}=g\lambda,\quad y=M_{13}=g3^{-\sigma},\quad
 z=M_{15}=g5^{-\sigma}.
\]

The successor/prime overlap at `(1,2)` is deliberately not substituted for x:
`K_12=lambda+2^-sigma`.

**Theorem.** Exact x,y,z uniquely identify `(lambda,sigma,g)` in this source class:

\[
 \boxed{\sigma=\frac{\log(y/z)}{\log(5/3)},\qquad
 g=y3^\sigma,\qquad\lambda=x/g.}
\]

They contain no information about b. For every b the same three entries occur.

**Proof.** The three source entries follow directly from authenticated S and Vp
basis actions: 2 and 3 are consecutive but not an integer-multiplier pair; 1 to
3 and 1 to 5 are prime multiplications and not successor. The scalar terms have
zero off-diagonal matrix elements. Dividing y by z cancels g and gives
`(5/3)^sigma`, a strictly increasing function of sigma. Recover g and then
lambda. Conversely these formulas determine the unique parameters, while changing
b affects none of the entries. QED.

**An explicit energy-mean interface.** These entries need not be assumed as
primitive hardware readings. With separately authorized preparations
`v_ij^+/-=(e_i +/- e_j)/sqrt(2)` and energy expectations, polarization gives

\[
 \frac{\langle v^+_{ij},Mv^+_{ij}\rangle-
              \langle v^-_{ij},Mv^-_{ij}\rangle}{2}
 =\operatorname{Re}M_{ij}.
\]

Here the entries are real. Six such energy-mean readings provide x,y,z; common
additive energy-readout offset cancels in each difference, and the common gain
remains. A null contrast (same preparation on both sides) calibrates zero; the
relative plus/minus phase fixes orientation. Different offsets in the two members
of a pair do not cancel. Six **exact expectation-oracle calls** are not six
quantum shots. No finite-sample exact-real estimation claim is made; genuine
experimental bands would need independently justified sampling/calibration bounds.

**Quantitative statement.** Suppose measured positive prime entries obey
`yhat=y(1+e_y)`, `zhat=z(1+e_z)`, with `|e_y|<=delta_y<1` and
`|e_z|<=delta_z<1`. Then

\[
 |\widehat\sigma-\sigma|
 \le \frac{\delta_y/(1-\delta_y)+\delta_z/(1-\delta_z)}{\log(5/3)}.
\]

Indeed, subtract the two logarithmic formulas and use
`|log(1+e)|<=|e|/(1-|e|)`. Also

\[
 |\log(\widehat g/g)|\le
 \delta_y/(1-\delta_y)+\log3\,|\widehat\sigma-\sigma|.
\]

The implementation accepts exact rational intervals for x,y,z, uses the parent's
positive atanh logarithm series and proved tail bound, interval multiplication
and division, and the parent's exponential Taylor tail bound. Outward dyadic
rounding controls rational growth. It returns conservative boxes for all three
parameters, including signed or zero lambda. It refuses bands that do not certify
positive gain and sigma>1; refusal is an unresolved precision/domain contract,
not a refutation of the source. Computation-budget failure supplies no certificate.

**Frozen holdout.** The first unused prime is 7: predict `M_17=g7^-sigma` from
the fitted boxes, then compare its independently supplied band. Prime 11 is an
additional fresh control. Under the model the source interference entry also
predicts `M_12-x=g2^-sigma`. A symmetric bounded rank-two perturbation
`eta(|1><7|+|7><1|)` preserves all three fitting entries while violating the
7-holdout when eta is large enough. Thus fitting x,y,z does not authenticate the
whole arithmetic operator. The interval tests use integer sigma and rational
lambda/gain to give exact truths independent of transcendental numerical oracles.

**Additive-bias counterexample.** If “offset” instead means an unknown common
bias d added *to each already extracted off-diagonal entry*, the map becomes
`x=g lambda+d`, `y=g3^-sigma+d`, `z=g5^-sigma+d`. Three entries no longer identify
four unknowns. An exact alternative to `(sigma,g,d,lambda)=(2,1,0,1)` is

\[
 \sigma'=3,\quad
 g'=\frac{1/9-1/25}{1/27-1/125},\quad
 d'=1/9-g'/27,\quad\lambda'=(1-d')/g'.
\]

It reproduces exactly `x=1,y=1/9,z=1/25`. This is a source-respecting calibration
counterexample, not roundoff. Polarization removes a common **energy** bias,
but not an arbitrary subsequent bias introduced into each extracted contrast.

## OBS-SF6. Relationship to observable geometry and the remaining boundary

A canonical Krylov realization preserves its declared scalar boundary response.
The parent gives a fully cyclic positive grounded RC path and triangle with the
same complete scalar response; that hostile control remains intact. Their
physical coordinate graphs differ. Adding a source-labelled interior probe can
split them only because it enlarges the authorized observation language. The
source-labelled zero-forcing reconstruction theorem likewise needs its known
graph/sign/source hypotheses. Exact Schur gluing preserves an interface response
only after its trace maps and exterior source have been specified; it does not
create missing internal probe access.

The arithmetic pin has this same structure. It replaces an impractical passive
identification task with a small *conditionally available* intervention task.
It does not prove that `e_1` is spectrally cyclic at `(lambda,sigma)=(1,2)`, does
not follow merely from generic cyclicity, and does not make its preparation
operators physically executable. The named passive theorem remains open.
No inequality in the authentic signed Weil/Suzuki low/high Schur problem is
improved by these observer results.

## Verification and source-preservation ledger

Executed focused commands:

```
python -m unittest discover -s tests -p 'test_source_faithful_observers.py' -v
python -m unittest discover -s tests -p 'test_reality_pin_hostile.py' -v
```

The new suite has 15 passing tests; the inherited hostile suite has 8 passing
tests, including the positive cyclic path/triangle isoresponse construction.
Direct integer-trajectory enumeration is independent of the closed-form carry
partition; the existing finite Moore minimizer supplies a differently implemented
finite control. The arithmetic entries are compared to the parent's independently
assembled source-channel matrix. Rational interval proofs, not floating agreement,
supply the transcendental enclosures. Full-suite/CI authority belongs to the root
integration receipt, not this lane's tests.

| Map | Identity/actions/future | Norm/phase/topology | Availability and open boundary |
|---|---|---|---|
| `n -> q_p(n)` | Current quotient only; successor descent fails | Classical state map, no Hilbert claim | Exact p=2 counterexample |
| `n -> (m,r)` | Current address and all declared deterministic source actions; not history identity | One-based labels; discrete bijection | Register storage is explicit; physical acquisition conditional |
| `X -> behavior(X)` | All declared observations and action continuations | Set quotient; no topology/physical completion implied | May be infinite/noncomputable |
| Future-sufficient representation -> behavior | Unique report factorization | Does not alone certify autonomous representation updates | Existing sufficiency/autonomy split retained |
| Polarized energy readings -> x,y,z | Authenticated real source entries, common gain, common offset cancellation | Plus/minus orientation required; exact finite-support domain | Mean oracle or calibrated bands are extra access |
| x,y,z -> parameter boxes | Identifies lambda,sigma,g within assumed source class | Rational enclosures; no offset recovery | Source identity requires holdouts; named cyclicity remains open |
| CP instrument intertwiner | All finite outcome branch laws under explicit commuting squares | TP/CP/domain hypotheses essential | Existence/minimality and hardware are not proved |

**What was taken for granted?** Forgetting a currently invisible residue was
being treated as harmless compression before asking whether the next source
operation depends on that residue. The exact failed equation is `q S=Sbar q`.
Retaining the carry register repairs that particular equation. It does not
repair every source map, select a completion, authenticate a physical graph,
or establish Weil positivity.

**Scholarly significance.** The general behavioral quotient is classical and
already partly implemented in SUCC. The exact arithmetic specialization, sharp
finite-horizon partition/cost account, affine-calibration formulas and executable
source/holdout controls are new to this project. Academic originality beyond this
application is UNVERIFIED. They are genuine scoped proof steps, not a universal
observer theory or a new coalgebra theorem.

**Next verdict-changing access theorem.** Give a separately authenticated
instrument on the actual arithmetic carrier that supplies uniform error bounds
for the six polarized energy expectations while preserving the source labels
and common calibration. Its cheapest falsifier is a relative-phase or differential
offset mutation that leaves three fitted magnitudes plausible but violates the
predeclared 7-entry and source-interference holdouts. This is separate from the
root's remaining signed-source theorem target.
