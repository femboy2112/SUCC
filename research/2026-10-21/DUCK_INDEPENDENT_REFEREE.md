# Independent referee: Duck structure, BBP transport and hostile controls

Date: 2026-10-21. Historical target: PR #232,
`9894d39250021bbbc2615c33dee0d286ddf0950f`. This report was developed in a
separate worktree before reading the other lanes' constructor reports.
The reviewer is a separate agent of the same model, **not an external human
referee or a different-model replication**. Later cross-reviews are identified
separately below. No frozen imported source was modified.

**Verdict:** the original eight Duck declarations express sound, narrow
structural implications. The BBP rational identity and circle transport have
the correct index. A sharper global forcing bound is proved below. Several
tempting upgrades fail by explicit counterexamples. None of these results
establishes source-specific Fourier cancellation or normality of π.

Status convention: **PROVED LOCAL (paper)** means the proof is given here;
**EXACT FINITE CHECK** describes executable controls only; **REFUTED** names
the precise false implication; **UNVERIFIED** retains missing proof debt.
Formal status is separate. The original source hash is
`3e56d9346167726ac6e9981b79420d3c7dba63bceba4f03090a5f6527afe372c`
for `formal/DuckPrinciple.lean` (Git blob
`4d72da20f41b0ff06305b6f19acd7fa864b87924`). The local Lean replay attempted
here failed with `error: failed to locate application`; this is an access gap,
not a successful kernel check. The coordinator's exact-head hosted receipt
must supply actual elaboration, theorem-type and axiom results. This report
does not turn a claimed JSON build success into proof authority.

## 1. Original Duck types versus prose

All eight declarations were inspected, including their hypotheses and proof
bodies. Their namespace is `ObservationalSUCC.Duck`.

| Declaration | Licensed conclusion and essential premise |
| --- | --- |
| `factor_all_words` | One-step commutation implies commutation for every finite word. |
| `factor_preserves_observations` | The preceding law transports an observation composed with the map. |
| `factors_compose` | Two commuting maps compose. |
| `faithful_probe_certifies_factor` | Equality after an injective probe implies the actual action square. |
| `bounded_separating_probes_certify_factor` | A universally supplied bounded-length separating family detects that square. |
| `failed_factor_yields_separating_experiment` | A failed square and the stated separating family give a distinguishing experiment. |
| `erased_systems_mimic_every_word` | The declared constant observations agree for all words. |
| `erased_resemblance_does_not_certify_identity` | The specific identity map between the erased flip and idle systems fails commutation. |

Two semantic restrictions must survive every summary. `IsFactor` asserts
commutation, **not surjectivity**; an onto dynamical factor needs a separate
onto condition. The types `Act`, `X`, and `Y` are arbitrary, not finite. A
bound on word length is not a finite probe family unless the action alphabet
is finite. The first four laws are classical equivariance/induction; the probe
laws explicitly assume separation, rather than deriving it from resemblance.
The final identity counterexample does not exclude a common trivial quotient.

The reported historical axiom audit lists the first five and last two as
axiom-free; the classical existential extraction uses standard Lean axioms.
This is a historical receipt claim, not a newly observed local build result.
The source's older candidate wording and any unregistered supplement namespace
are documentation reconciliation tasks for the coordinator, not new theorem
evidence.

### Stronger common-factor and budget countermodels

Give the one-action cycles C₂ and C₃ the same erased output. Every finite
observation agrees. Suppose both map onto a dynamical system `(Y,T)` by
commuting maps. Surjectivity implies `T²=id` and `T³=id`, hence `T=id`.
The image of the transitive C₂ orbit is then a single point; thus Y is a
singleton. **REFUTED:** identical all-word observations imply a common
nontrivial onto factor. This proof is universal; exhaustive two-state target
enumeration in the independent script is a separate exact check.

For every proposed length budget B, take states `0,...,B+2`, transition
`s ↦ min(s+1,B+2)`, and output one only at `B+2`. Initial states 0 and 1
agree for all lengths at most B and disagree at length B+1. **REFUTED:** a
fixed unproved observation budget guarantees all-word equivalence. The model
depends on B; no claim of a single model fooling all lengths is made.

## 2. Independent BBP arithmetic, source index and sharper tail

For every real x≥1 put

\[
A(x)=120x^2-89x+16,\quad
D(x)=(2x-1)(4x-1)(8x-7)(8x-3),\quad r(x)=A(x)/D(x).
\]

Expansion gives `D=512x⁴−1024x³+712x²−206x+21`. Clearing the nonzero
denominators gives the exact identity

\[
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}.
\]

All four factors of D are positive on x≥1. With u=x−1,
`A=120u²+151u+47>0`, so r>0. A direct polynomial identity gives

\[
47D(x)-15x^2A(x)=22264u^4+42263u^3+26429u^2+5443u\ge0.
\]

Consequently

\[
\tag{R1}0<r(x)\le\frac{47}{15x^2}\qquad(x\ge1).
\]

The constant 47/15 is optimal on this domain because r(1)=47/15. This is
a **PROVED LOCAL (paper)** strengthening of the handoff bound 8/x², with
no claim of academic novelty. The polynomial computation and exact values
at large integers are checked independently by the script.

Using the classical BBP identity for π and shifting its index gives
`π/16 = Σ_{m≥1}16^{-m}r(m)`. This use of BBP is an explicit external source
identity. If x₀=0 and `x_n={16x_{n−1}+r(n)}`, induction gives

\[
x_n=\left\{\sum_{m=1}^n16^{n-m}r(m)\right\},\qquad
t_n=\sum_{k\ge1}16^{-k}r(n+k).
\]

The series is absolutely convergent by R1. For n≥0,

\[
\tag{R2}0<t_n\le\frac{47}{225(n+1)^2},
\]

because `Σ_{k≥1}16^{-k}=1/15` and `(n+k)^{-2}≤(n+1)^{-2}`.
For n≥1 the exact phase identity and its circle metric consequence are

\[
\{16^{n-1}\pi\}=\{x_n+t_n\},\qquad
d_{\mathbb R/\mathbb Z}(x_n,16^{n-1}\pi)\le t_n.
\]

The shift n−1 is essential. The script independently encloses π using
Machin's identity `π=16 atan(1/5)−4 atan(1/239)` and alternating rational
remainders. Twelve phase comparisons overlap the correct interval; replacing
n−1 by n makes all twelve disjoint. These finite comparisons authenticate
neither infinite BBP identity by themselves nor any digit asymptotic.
For completeness, the independent Machin source has an elementary check:
with a=atan(1/5), double-angle arithmetic gives tan(4a)=120/119;
the subtraction formula gives tan(4a−atan(1/239))=1 exactly. The angle is
strictly between zero and π/2, so it equals π/4. The alternating series
remainders used by the script then rigorously enclose that same geometric π.

## 3. A smooth rational forcing with exactly the same leading coefficient

For x>0 define

\[
\widetilde r(x)=\frac1{64}\left(\frac{16}{x^2}-\frac1{(x+1)^2}\right).
\]

This rational forcing is positive and O(x⁻²), has numerator degree 2 and
denominator degree 4, and its leading coefficient is 15/64, the same as r.
For every integer j≥0,

\[
(-1)^j\widetilde r^{(j)}(x)=\frac{(j+1)!}{64}
\left(\frac{16}{x^{j+2}}-\frac1{(x+1)^{j+2}}\right)>0.
\]

It is therefore completely monotone. For the recurrence starting at zero,
telescoping yields the exact formula

\[
\widetilde x_n=
\left\{\frac{16^n}{64}-\frac1{64(n+1)^2}\right\}.
\]

For n≥2 this equals `1−1/[64(n+1)²]`; hence it approaches zero on the
circle. Every fixed nonzero integer Fourier mode has mean tending to one,
not zero. Explicitly, for N≥1 and integer h,

\[
\left|\frac1N\sum_{n<N}e^{2\pi ih\widetilde x_n}-1\right|
\le\frac{2+|h|/16}{N}.
\]

Proof: n=0 contributes no error, n=1 contributes at most 2, and the remaining
chord errors sum to at most
`(8|h|/64)Σ_{m≥3}m^{-2}≤|h|/16`, using π<4 and the integral bound 1/2.
**REFUTED:** rational decay, complete monotonicity and the correct leading
coefficient force equidistribution. This example belongs to the rational
finite-attractor alternative, so it is **not** a counterexample to
Bailey–Crandall Hypothesis A. Nor does it share the actual BBP pole structure.

### A source-specific obstruction to that telescoping mechanism

The actual r has four simple poles with nonzero residues:

| Pole | Residue |
| --- | --- |
| 1/4 | −1/8 |
| 1/2 | −1/4 |
| 3/8 | −1/8 |
| 7/8 | 1/2 |

Each pole is alone in its class modulo integer translation. There is no
rational F∈ℂ(z) such that `r(z)=16F(z−1)−F(z)`. Indeed, in any occupied
pole class of F choose the smallest and largest integer indices a,c.
The right side has an uncancellable pole at the first location (from −F)
and at the last location shifted by one (from 16F(z−1)). They are distinct
and in the same class, contradicting the displayed r pole set. If F has no
finite poles it is polynomial, whose difference cannot equal r.

This is **PROVED LOCAL (paper)** and rules out one rational coboundary route.
It does not establish irrationality, equidistribution or Fourier cancellation.
After this proof was recorded, the analytic constructor supplied a weighted
pole-invariant argument for the same obstruction. Those are distinct algebraic
derivations by same-model agents, not an external referee confirmation.

## 4. Nonautonomous clocks and finite-attractor wording

The forced clock map on `ℕ×(ℝ/ℤ)` is
`F(n,x)=(n+1,16x+r(n+1))`. It has **no invariant countably additive probability
measure**. If μ were invariant, its time marginal ν would satisfy ν({0})=0
(the preimage is empty), then ν({k+1})=ν({k})=0 for every k. Countable
additivity contradicts ν(ℕ)=1. Time-indexed Haar distributions can still be
pushed to the next slice, but are not a stationary probability on this space.
Compactifying time changes the system and needs a fresh source map. Even a
stationary measure elsewhere would not make the selected π orbit generic.

The inspected Bailey–Crandall author manuscript is dated 03 October 2000;
its publication is from 2001. Hypothesis A is a finite-attractor-or-uniform-
distribution dichotomy for the specified rational forcing. Its Theorem 3.1
relates rationality to the finite-attractor branch without assuming that
hypothesis. The normality upgrade requires the hypothesis.

There is a literal wording issue in Definition 2.5 and Theorem 2.8 of that
manuscript: a finite covering attractor W is not required to be minimal,
but the theorem describes W itself as a rational cycle. The orbit x_n=0 in
base 2 is covered by `W={0,1/3}`, which is not invariant; `W={0,√2−1}` even
contains an irrational unused point. These are counterexamples to that
nonminimal-W reading, **not** to the existential rationality result.

A corrected proof uses the actual omega-limit set Ω. Compactness makes Ω
nonempty, and finite covering makes it finite. Continuity gives TΩ=Ω for
T(x)=bx on the circle, so T permutes Ω. Choose disjoint small neighborhoods
of Ω. Eventual nearest labels satisfy `s_{n+1}=T(s_n)`, since the distance
to Ω tends to zero and T is b-Lipschitz. Thus Ω is one periodic cycle.
Choose a sufficiently late orbit tail with signed errors e_n from that
cycle satisfying `|e_n|<1/(4b)`. Since `e_{n+1}−b e_n` is an integer of
absolute value less than one, `e_{n+1}=b e_n`. Boundedness for all future
n forces e_n=0. The orbit is eventually periodic and
`(b^P−1)b^N α∈ℤ` for some N,P, so α is rational. Conversely rational
orbits are eventually periodic, including when the denominator shares factors
with b. This repairs the assertion without importing an unused-point premise.

## 5. Irrationality measure is insufficient

Let `t₀=0, t_{2k}=t_k, t_{2k+1}=1−t_k`. Bugeaud's published theorem gives
irrationality exponent exactly 2 for
`ξ_b=Σ_{k≥0}t_k b^{-k}`, for every integer b≥2. In base 16 its digits use
only 0 and 1, so it is not normal. In base 2 any three consecutive indices
contain an aligned pair 2k,2k+1 with opposite digits; the words 000 and 111
never occur. **REFUTED:** even the optimal exponent 2 implies normality.
The digit argument is elementary and independent; the exponent-2 theorem
is imported, not inferred from our finite census. This does not refute any
future π-specific implication from RH or ABC plus additional structure.

## 6. Subsequent independent cross-review of new lane statements

This section was written after the independent findings above. It reviews
source types and paper arguments, not an unobserved compiler outcome.

* `DuckObserver.lean`: all thirteen proposed statements keep arbitrary action
  and state types, current-readout preservation, and all-word quantifiers.
  The quotient is the coarsest observation-preserving action congruence.
  Descent of a morphism through it correctly requires a behaviorally separated
  target. `closed_relation_all_words` has both report agreement and transition
  closure. The Python checker checks those entire tables, exact model binding
  and root inclusion. The BFS proof visits at most |X||Y| pairs; a shortest
  witness has length at most |X||Y|−1. A smaller exhausted budget returns no
  verdict. The common-factor routine finds an onto separated observed factor
  for one fixed interface; `None` excludes neither a hidden nonseparated factor
  nor a different observation interface. The stationary unit-cost adapters
  preserve their explicit restrictions. No Lean-to-Python refinement or
  physical-source authentication is asserted.
* `BaileyCrandall.lean`: the candidate proves the rational function's actual
  analytic series tail, lifted recurrence and circle transport. Its
  `pi_circle_transport` has the explicit premise `seriesValue = Real.pi`.
  This source identity has not been proved just by proving the generic series
  theorem. Its index `(n+1)` against `16^nπ`, and bound with `(n+2)²`, agree
  exactly with R2 above.
* `Normality.lean`: the proposed normality predicate uses canonical floor-
  selected blocks and every starting position, hence overlapping frequencies.
  The half-open interval convention handles rational endpoints. The implication
  from interval equidistribution to normality has its actual equidistribution
  premise; it does not prove Weyl's criterion, the Haar/interval equivalence,
  base-16 to base-2 conversion, or cancellation for π. Those remain distinct
  debts unless subsequently checked declarations explicitly close them.
* `LogisticFactor.lean`: the actual map on ℝ/ℤ is `sin²(πt)`. Its target is
  the subtype [0,1], with proved-on-paper surjectivity, noninjectivity and
  doubling/logistic semiconjugacy. Using `Real.pi` in this map does not give
  information about genericity of the particular digit orbit of π.

Follow-on source review at observer lane commit `52733cb` and normality lane
commit `0b93f4f`: `logisticHat_continuous` now explicitly states continuity
of the actual quotient map. The observer lane also supplies a complete finite
Boolean table validator, `validated_table_all_words`, and positive/negative
table controls. Its `by decide` premise checks finite laws; the conclusion
then follows for all words by the preceding induction, not by extrapolation
from bounded words. The Python exporter produces literal numeric transition,
output and relation tables with a shared injective encoding of output strings.
Inspection confirms exact array correspondence and escaped one-line JSON
metadata, including the empty action alphabet. A valid initial state prevents
an empty state-carrier export. The JSON/hash comment is still external source
metadata; the Lean kernel does not authenticate that comment or prove a
universal refinement theorem about the Python generator. Actual successful
kernel compilation and independent source/artifact comparison remain required.

The normality dossier's base-power descent proof also survives paper review:
for B=bʳ, split base-b starts into their r residues, group enough base-B
digits to cover each desired word, and sum its finitely many chunk-code
frequencies. This gives base-16 ⇒ base-2 normality. It is not yet among the
inspected Lean declarations, and gives no base-10 implication.

Further candidate review: `DuckPiIntegral.bbp_hasSum_pi` supplies a proposed
unconditional source proof. Its integrand is
`(4−2x³−x⁴−x⁵)/(1−x⁸/16)` on [0,1], its rational decomposition is
`4x/(x²−2)−4(x−2)/(x²−2x+2)`, and an antiderivative is
`2 log(2−x²)−2 log(x²−2x+2)+4 atan(x−1)`. Independent differentiation
and endpoint evaluation give the integral π. The geometric-series terms are
bounded in norm by the summable constant majorant `8·16^{-n}` throughout
[0,1]; termwise integration gives exactly the BBP offsets 1,4,5,6. Thus no
mathematical source-identification premise is hidden in this proposed proof.
The separate standard-series `HasSum` uniqueness bridge then connects it to
`seriesValue`. These are semantically accepted candidates; their promotion
still depends on actual successful kernel output, not this paper check.

The observer lane's stronger **paper** witness bound also survives: for
carriers of sizes n,m, a shortest distinguishing word has length at most
n+m−2; within one carrier it is at most n−2. On the disjoint union, partition
by all observations of length at most j. Any plateau is stable forever.
Hence a pair first distinguished at depth r requires r strict refinements
from at least two initial output classes among n+m states. A unary chain
whose only nonzero output is terminal, compared with a single zero state,
attains the cross-model bound; adjacent initial chain states attain the
within-model bound. This does not claim a formalized cardinality argument.

### Analytic lane: a stronger summable transport budget

The analytic constructor's independently supplied positive decomposition is

\[
r(m)=\frac6{(8m-7)(8m-4)}+
\frac4{(8m-7)(8m-3)}+\frac5{(8m-7)(8m-2)}.
\]

Clearing denominators verifies it. Each term decreases for real m≥1 and
is bounded by its numerator divided by `(8m−7)²`. Thus
`t_n≤r(n+1)/15≤(8n+1)^{-2}`. For integers M,N≥1,

\[
\sum_{n=M}^{M+N-1}t_n
\le\frac18\left(\frac1{8M-3}-\frac1{8(M+N)-3}\right)
\le\frac1{40}.
\]

The telescoping step uses `(8n+1)²−16=(8n−3)(8n+5)>0`.
The Fourier sum difference is consequently at most `2π|h|` times this
budget, and hence less than or equal to `|h|/5` after using 2π<8.

For the N samples indexed j=0,...,N−1 compare the actual digit point
`16^jπ` with forced point `x_{j+1}`. Delete the first K samples, where
0≤K≤N. Every remaining distance is at most `δ=r(K+2)/15`. Expanding a
circle arc by δ at both ends increases its length by at most 2δ; the K
deleted points cost at most K/N. Applying this in both directions to the
supremum over oriented half-open arcs gives

\[
|D_N(16^j\pi)-D_N(x_{j+1})|
\le\min_{0\le K\le N}\left(\frac KN+\frac{2r(K+2)}{15}\right)
\le\frac{33}{32}N^{-2/3}.
\]

Indeed choose K=⌊N^{1/3}⌋. Then K/N≤N⁻²ᐟ³ and
`δ≤(8K+9)^{-2}≤(64N^{2/3})^{-1}`. Empty and full arcs, including
expansions reaching the full circle, obey the same inequality. Endpoints
are handled by the canonical half-open convention; the arc argument does
not assume no orbit point lies on an endpoint. These constants and index
conventions survive independent paper review. This sharper **difference**
budget still proves neither orbit's discrepancy tends to zero. These
Fourier/discrepancy theorems are paper results unless an exact hosted Lean
declaration and receipt subsequently cover them.

Two later quantitative refinements also passed this referee's independent
derivation. With x=n+1, the BBP lane obtains

\[
-\frac1{480x^3}\le t_n-\frac1{64x^2}
\le\frac{2783}{14400x^3}.
\]

The upper rational inequality is
`r(x)≤15/(64x²)+2783/(960x³)`. Its cleared numerator, with u=x−1,
is `1279936u⁴+2414792u³+1499906u²+306607u≥0`. The lower bound follows
from `r(x+k)≥15/[64(x+k)²]` and the exact convexity remainder
`(x+k)^{-2}−x^{-2}+2kx^{-3}=k²(3x+2k)/[x³(x+k)²]≥0`.
The geometric zeroth and first moments are 1/15 and 1/225, producing the
displayed constants. Independent symbolic subtraction returned zero for
both polynomial identities. Since `0<t_n<1/2`, the actual circle distance
is t_n, and `n²t_n→1/64` proves the pointwise shadow exponent 2 is sharp.

For each integer K≥1 the analytic lane defines
`Q_K(n)=Σ_{k=1}^K16^{K-k}r(n+k)/(16^K−1)`. Direct shift cancellation gives

\[
\widetilde r_K(n)=16Q_K(n-1)-Q_K(n)
=\frac{16^Kr(n)-r(n+K)}{16^K-1}>r(n)>0.
\]

Its orbit has rational shadow Q_K(0), so is not equidistributed. The
positive partial-fraction decomposition shows n²r(n) decreases on n≥1;
consequently
`sup_{n≥1} n²|rtilde_K(n)−r(n)|≤47/[15(16^K−1)]→0`.
Accumulating the recurrence errors through a finite horizon gives circle
distance at most `min(1/2,47(16^n−1)/[225(16^K−1)])`. Both constants
survive independent review. This demonstrates arbitrarily close rational-
shadow counterfeits in that weighted forcing norm; it does not assert that
normality is discontinuous at the actual, still unresolved π source.
The corrective function has 4K poles; the counterfeit forcing has eight
poles, with positions and heights escaping as K increases. A lower bound
based on source complexity would need explicit restrictions on these data.

The new `WeylBridge.lean` candidate was also inspected: convergence on all
genuine integer characters extends to complex continuous circle tests using
their dense linear span and norm-one empirical/Haar averages, then to real
continuous tests. Its Fourier cancellation hypothesis remains explicit.
This closes a classical **candidate** direction of Weyl transport, but
does not supply cancellation or, by itself, the continuous-test-to-interval
bridge. Exact exported types and successful kernel output govern promotion.

### Conditional-source lane: independently reconstructed constants

The inspected conditional dossier and exact helper retain the right scope.
For `f(u)=u^{-2}/log u`, `E(u)=ψ(u)−u`, and the premise
`|E(u)|≤C√u(log u)²` for every real u≥X>1, Stieltjes integration on `(X,T]`
and passage to infinity give

\[
\sum_{n>X}\frac{\Lambda(n)}{n^2\log n}
-\int_X^\infty f(u)\,du
=-f(X)E(X)-\int_X^\infty E(u)f'(u)\,du.
\]

The right-continuous ψ(X) matches inclusion of the boundary prime power in
the finite sum. Direct integration bounds the absolute value by
`C X^{-3/2}[(7/3)log X+14/9]`: the boundary contributes log X; the integral
contributes `(4/3)log X+14/9`. Lee–Nosal v4 Theorem 1.2 was independently
inspected and gives the required RH premise for X≥101 with C=1/24 after
weakening its explicit bound.

Writing ε for that error, the reconstructed approximant satisfies
`|a_X−π|≤4ε` when ε≤1. The mean difference is therefore bounded by
`min(2,32|h|ε(16^N−1)/(15N))`. Both constants and the exponential cutoff
dependence survive review. **No cancellation estimate follows for either
mean**. The conditional code correctly calls this a budget, not an evaluated
approximant or a successful proof of RH.

For the ABC lane set `g=gcd(pb^n,qA)`, `U=pb^n/g`, `V=qA/g`,
`D=|U−V|>0`, `H=max(U,V)`. The triple is primitive, and
`rad(UVD)=rad(UV)rad(D)≤rad(UV)D`. Thus the premise
`H≤K rad(UVD)^{1+ε}` implies
`D≥H^{1/(1+ε)}/[K^{1/(1+ε)}rad(UV)]`. Multiplying by `g/(qb^n)` and
subtracting an independently proved rational approximation error gives the
stated prefix lower bound. The helper's ε=1 square version checks the
particular finite premise and does not assert one universal K. A useful π
application still needs joint approximation and reduced-radical estimates.

## 7. Reproducible evidence and remaining proof cut

Run from this worktree:

```sh
python -m unittest discover -s tests -p 'test_duck_hostile_referee.py' -v
python scripts/duck_hostile_referee.py
```

The first observed run passed all ten tests. The script imports none of the
new Duck, BBP or conditional production implementations. Its exact receipt
includes 100 rational forcing checks (including 10³⁰), 12 independently
enclosed correct-phase and wrong-index controls, 129 telescoping-orbit checks,
216 derivative checks, exhaustive C₂/C₃ factor rejection, 25 delayed-probe
models and 16,384 Thue–Morse digits. These are finite implementation evidence;
the universal arguments are the proofs above. Root owns broad regression,
provenance, exact candidate CI, axiom audits and publication.

| Result or boundary | Status | Next decisive probe |
| --- | --- | --- |
| Eight original Duck implications | Historical kernel receipt; semantic audit survives | Replay exact pinned source and export full types/axioms |
| Sharp forcing and analytic tail bounds | PROVED LOCAL (paper); independent exact controls | Kernel-check actual real inequalities and infinite series |
| Generic series-to-circle transport | PROVED LOCAL (paper) | Check BBP source identity separately before unconditional π specialization |
| C₂/C₃, delayed probes, rational forcing impostor, one-way clock | REFUTED precise stronger implications | Require the missing onto/separation/source/dynamical hypothesis |
| Rational coboundary of actual r | REFUTED by source pole structure | Attack cancellation beyond rational telescoping |
| Optimal irrationality measure ⇒ normality | REFUTED using published independent theorem | Identify genuinely joint phase information |
| Conditional prime and primitive-radical bounds | PROVED LOCAL (paper), conditional | Supply useful phase cancellation or π-specific low-radical approximants |
| π Fourier cancellation, π normality, RH, integer ABC | UNVERIFIED / OPEN | A source-specific global theorem, not a renamed target premise |

The strongest surviving new-to-project quantitative gain in this referee lane
is the optimal forcing constant 47/15 and its 47/225 tail corollary. The strongest
negative gain is a rational completely monotone forcing matching the BBP leading
coefficient but having noncancelling Fourier means. The source pole obstruction
shows why this particular counterfeit does not settle the actual π source.

## 8. Primary references and reproduction boundary

1. D. H. Bailey and R. E. Crandall, *On the Random Character of Fundamental
   Constant Expansions*, Experimental Mathematics 10 (2001), 175–190,
   DOI [10.1080/10586458.2001.10504441](https://doi.org/10.1080/10586458.2001.10504441).
   [Author manuscript](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf),
   dated 03 October 2000, Definitions 2.5–2.6, Theorems 2.8–2.10 and 3.1.
   Only precise scoped statements are imported; the corrected attractor proof
   above and the explicit counterexamples are independently derived.
2. Y. Bugeaud, *On the rational approximation to the Thue–Morse–Mahler numbers*,
   Annales de l'Institut Fourier 61 (2011), 2065–2076,
   [DOI 10.5802/aif.2666](https://www.numdam.org/articles/10.5802/aif.2666/).
   The published exponent-2 theorem is an external mathematical dependency.
3. E. S. Lee and P. Nosal, *Sharper bounds for the error in the prime number
   theorem assuming the Riemann Hypothesis*,
   [arXiv:2312.05628v4](https://arxiv.org/html/2312.05628v4), 2 October 2025,
   Theorem 1.2. Its conditional prime estimate is imported, not formalized here.

These links identify inspected primary sources. No publisher PDF hash, external
human review, academic novelty, successful local Lean execution, or formal
verification of imported analytic literature is claimed.

## 9. Resumed referee checkpoint: actual kernel exports and finite-degree probes

This checkpoint independently inspected the completed hosted
[run 39613723244](https://github.com/femboy2112/SUCC/actions/runs/39613723244),
at commit `6fbe9d29355aaccca5ebf2753d34eee2e2ece627`, tree
`5cb5f94f9f06eeaeff16c27e5c21bdb3d53e8c0c`. It supersedes the earlier
**candidate** descriptions only for the exact successfully compiled declarations
listed by that run. The combined build failed in `WeylBridge`; its success must
not be inferred from the success of other modules.

### Actual proof scope

The compressed observation in the hosted log was decoded, every one of its
97 exported theorem-type SHA256 values was recomputed, and all reported axiom
lists were inspected. Their union is exactly `propext`, `Classical.choice`,
`Quot.sound`; no exported successful theorem depends on `sorryAx` or a new
source/normality axiom. The separately generated two-action and empty-alphabet
fixtures each exported three additional proofs. Their axiom lists use at most
`propext`. Nine source/proposition mutants were rejected with successful
positive controls; the Haar-normalization mutant was correctly blocked by the
failed positive Weyl module.

The following actual types were compared with their source definitions and
the prior paper reconstruction:

| Declaration | Observed proposition and boundary |
|---|---|
| `DuckPiIntegral.bbp_hasSum_pi` | The standard infinite BBP coefficient series has sum `Real.pi`. The exported type has no hypothesis binder supplying the BBP identity, RH, ABC or cancellation. |
| `ObservationalSUCC.DuckPi.Source.bbp_series_eq_pi` | The declared rational-forcing `seriesValue` equals `Real.pi`, obtained by uniqueness of the two independently established sums. This is an unconditional equality, not an English source label. |
| `ObservationalSUCC.DuckPi.Source.pi_orbit_identity` | For every natural n, `16^n * Real.pi = liftedOrbit (n+1) + tail (n+1)`. The index shift is explicit and correct. |
| `ObservationalSUCC.DuckPi.Source.pi_circle_transport_shifted` | For every natural n, the distance on the actual `AddCircle 1` is at most `1/(8*n+9)^2`. The only outer quantified input is n; no source-identification or equidistribution premise is hidden. |
| `ObservationalSUCC.Duck.Observer.validated_table_all_words` | Complete finite relation laws and initial membership imply agreement of the exact encoded readouts for every action word. The universal closure theorem's axiom list is empty. |

Representative exact exported type hashes are:

* `bbp_hasSum_pi`: `2b8dc9dfd3d31bbfa95a24a4c08bdd6f2b75248d8b85da2a69c9e5cd63a51e0d`.
* `bbp_series_eq_pi`: `51f9467120886fe8bd87b6bbf6657796541eb1c13fd7363b29abe40d8d662517`.
* `pi_circle_transport_shifted`: `c7d6826b1cdae2439615a41039ba0be2390b3c94bf06748c84800ef9ed3fe9ac`.
* `validated_table_all_words`: `c07c7379bf46d705e04dc57c539b584675acfd3323326d83206f34bcd6c76ad1`.

These are observations of a real build, not self-authenticating JSON authority.
The record explicitly has `authority_admitted=false`. New declarations are not
silently installed in the existing Level-C proof-authority catalogue. The source
hashes matched the inspected `BBPIntegral`, `PiSource`, `Normality`,
`LogisticFactor` and `DuckObserver` files. Three subsequent additions to
`BaileyCrandall` were not part of this build and require their own replay.

### Generated certificates and source identity

The finite generator emits complete literal transition/readout/relation tables.
A shared injective coding of output strings preserves equality. The kernel
checks both exhaustive relation laws and the initial pair before applying the
all-word theorem. There is no imported Python Boolean or caller callback in the
proof. Empty action alphabets use the genuine `Fin 0` eliminator. Hostile label
text stays in JSON-escaped line comments rather than executable Lean syntax.

The JSON/hash comments bind a declared model only when compared externally to
the emitted artifact; they are not part of the logical proposition and do not
authenticate a physical source. Compilation certifies those literal models,
not universal correctness of the Python generator or an unrelated model. The
current interface and dossier preserve this distinction. No authority-transfer
defect was found within that advertised domain.

### Independently reconstructed finite discriminator

For `q=A/B` with rational polynomial numerator and denominator of degrees at
most d, put the residual over `D(z)B(z-1)B(z)`, where the authentic forcing has
numerator N of degree two and denominator D of degree four. The numerator is

\[
F=N B(z-1)B(z)-16 A(z-1)D B(z)+A(z)D B(z-1).
\]

Its degree is at most `2d+4`. The previously established source-pole obstruction
ensures F is not identically zero. If `B(j)` is nonzero for `0<=j<=2d+5`, all
the positive probe denominators are nonzero; consequently, vanishing at all
`2d+5` distinct probe points contradicts the polynomial root bound. This
independently reconstructs DA-DEGREE, including the otherwise essential
nonsingularity and declared-degree hypotheses. Rejection of a singular
presentation is legitimate even when cancellation might remove its pole.

As an implementation cross-check, a separate symbolic construction formed F
from the coefficients, checked its degree, and independently evaluated its
residual at the returned point for 48 deterministic coefficient cases across
degrees 0 through 5. All passed. The 14 analytic tests and 13 observer tests
also passed in the combined root worktree. These are finite corroboration;
the universal sample guarantee is the polynomial argument above, and is not
claimed Lean formalized.

**Verdict:** no blocking mathematical defect was found in these scopes. A
source-faithful classical identity and quantitative π transport are now actual
kernel-checked results at the cited commit. Global π Fourier cancellation,
π normality and the failed/unreplayed formal extensions remain outside this
verdict. This is a separate internal same-model referee investigation, not an
external human review or an independent model-family witness.

## 10. Second resumed checkpoint: exact shadow distance and Weyl transport

The referee separately decoded the actual observation from hosted
[run 39632926557](https://github.com/femboy2112/SUCC/actions/runs/39632926557),
commit `eb106f74455d1579c041d4cf2e5be80ef0492f23`, tree
`0b4ccbb8069b0e2c02506e4f2c35838dc8ac32e0`. All 123 exported type hashes were
recomputed. The axiom union remains exactly `propext`, `Classical.choice`,
`Quot.sound`. The combined run failed in `HaarBoundary`; the dependent
`HaarIntervals` and `AsymptoticTransport` modules were not successfully checked.
This checkpoint does not report a green whole-project build.

The seven `PiSource` declarations and 21 `WeylBridge` declarations now have
successful module builds and actual exports. Their source hashes match the
inspected files:

* `PiSource.lean`: `37699406dc52caa814dd20dd1602060bd08e896d50e66b637d3e4077b8ace4e2`.
* `WeylBridge.lean`: `e71eaf5beccac80cad05db3e3022c71e8fc7f304da0c61006ff2a7531ed3b358`.
* `BaileyCrandall.lean`, now including its three additions:
  `5ea46de978c6969509adf0fca71811a0cf18909b9c525ecaeb9e15cd4582de50`.

The newly checked `pi_circle_distance_eq_tail` identifies the actual circle
distance with `tail(n+1)`. Its exported type has only the natural index n as
an outer argument. The strictly positive quadratic lower bound
`15/[1024(n+2)^2] < distance` is also unconditional and universally quantified
in n. Together with the earlier upper bound this establishes the pointwise
order of this particular shadow distance. It is not a discrepancy lower
bound and does not obstruct cancellation of either orbit.

The Weyl theorem's actual exported type explicitly has the arguments
`u : Nat → Real` and `hu : FourierCancellation u`, and concludes the existing
`HaarUniformDistribution` predicate on the quotient sequence. The referee
reconstructed its mechanism: norm-at-most-one empirical and Haar functionals;
closure of the submodule of convergent continuous tests; convergence of the
constant character to one and every nontrivial character to zero; density of
the genuine integer characters; and passage from complex to real tests.
The normalization at period one and the exceptional value N=0 are both
handled explicitly. All ten registered source/proposition mutations, including
Haar normalization, were rejected with successful positive controls in this
run. The cancellation hypothesis is not discharged by this theorem.

### Semantic review of the subsequent candidates

The following mathematical review is **not a kernel-success claim**:

* `HaarIntervals` uses the actual representative in `[0,1)` and half-open
  preimages. Away from the cut at zero the representative is a local
  homeomorphism, so a cylinder's frontier lies among zero and its two endpoint
  classes. These three singleton sets have Haar measure zero. Quotient
  integration identifies the cylinder's mass with its length. The statement
  remains valid for a degenerate interval; the measure identity with a>c is
  the empty-set/zero-positive-part case. These statements correctly supply
  the geometric premises for Portmanteau rather than assuming interval
  equidistribution.
* `AsymptoticTransport` uses compact uniform continuity to make continuous
  observation differences tend to zero, then Cesaro convergence to make their
  empirical-mean differences tend to zero. Subtracting that difference from
  the known source mean transports the Haar limit. The actual π bound supplies
  vanishing distance with the exact `n+1` forced-orbit index. No scalar-source
  identity or convergence premise is silently inserted.
* Its final conditional normality declaration requires global Fourier
  cancellation of `liftedOrbit(n+1)` for every nonzero integer frequency.
  Passing to circle classes does not change those characters. This premise
  is precisely an outstanding arithmetic obligation, not a newly proved
  consequence of the tail bound. Base-power descent from 16 to 2 remains a
  separate classical paper result unless a later kernel receipt states more.

No mathematical defect was found in these candidate statements or their paper
mechanisms. Successful elaboration and exact exported propositions remain
required before promoting them. Neither this review nor the checked Weyl
implication establishes a source-specific cancellation estimate.
