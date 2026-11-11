# Productive geometry, maximal runs, and rational probes

Round V translator note. Baseline: `4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b`.
The formulas below use the endpoint convention of
`research/2026-11-10/circle_line_lr_observer/circle_line_observer.py`.
This note was prepared outside the checkout while baseline validation ran.
It changes no production code or remote state.

## 1. What the finite program is allowed to do

The program has finite syntax, exact integer/rational arithmetic, and
unbounded registers. Its next-output procedure terminates at each reachable
state; its stream has no prescribed last output. This is the appropriate
meaning of a finite algorithm run indefinitely. It is stronger than merely
exhibiting many finite prefixes and does not assert a physically completed
infinity, bounded storage, or a uniform small latency per output.

Let `S` be the countable set of valid finite source/endpoint records reachable
from the geometric input. After proving productivity, the procedure which
consumes as many source factors as necessary and emits the next arrow defines
a total map

\[
\operatorname{advance}:S\longrightarrow\{L,R\}\times S.
\]

This is a stream coalgebra. The stream of arrows is its unique behavior map
to the final coalgebra of infinite binary streams, with head/tail structure.
The coalgebra terminology records the all-time object; it does not discharge
the proof that the source-consumption loop terminates. That proof is the
rational comparison argument below. Source steps are silent transitions;
each `advance` removes only a finite block of them.

Distinct source precisions may have the same future observable word. Thus a
behavior map need not be injective on implementation states. We distinguish
interval-state nonrecurrence, normalized-real nonrecurrence, and output
nonperiodicity explicitly.

## 2. Source, endpoint matrix, and the swap that must survive

The geometric source from Round IV has

\[
 Z_j=\begin{pmatrix}j&4j+2\\0&2j+1\end{pmatrix},\qquad
 W_k=\prod_{j=1}^k\frac{j}{2j+1},\qquad
 A_k(x)=2\sum_{n<k}W_n+W_kx.
\]

Here `W_0=1`. The source interval is `I_k=A_k([3,4])`; the proved circle
integral identity gives `pi` strictly inside every such interval. Its width
is `W_k`, and each new factor reduces that width by less than one half.
The lower endpoint need not change strictly at every step: the first lower
endpoint is still `3`. The width always decreases strictly. No decimal
value, digit table, or trigonometric evaluation is an input to the program.

Write the current Farey bracket and matrix as

\[
 J=(a/b,c/d),\qquad
 E=\begin{pmatrix}a&c\\b&d\end{pmatrix},\qquad
 bc-ad=1,\quad b,d>0.
\]

The initial tuple is `(3,1,4,1)`. The output generators are

\[
 L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

Right multiplication `E -> EL` changes the upper endpoint, while `E -> ER`
changes the lower endpoint. The increasing residual chart uses a column
swap:

\[
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 B=ES=\begin{pmatrix}c&a\\d&b\end{pmatrix},\qquad
 B(t)=\frac{a+ct}{b+dt}.
\]

It has determinant one. Define the normalized residual

\[
 z=B^{-1}(\pi)=\frac{b\pi-a}{c-d\pi}>0.
\]

The residual moves are

\[
 \begin{array}{c|c|c}
 \text{output}&\text{guard}&\text{new residual}\\\hline
 L&0<z<1&z/(1-z)=R^{-1}(z)\\
 R&z>1&z-1=L^{-1}(z).
 \end{array}
\]

The letter swap is essential: `B_(EG)=B_E(SGS)`. In a combined source/output
residual matrix `T=B_E^{-1}A_k`, source consumption acts on the right,
`T -> TZ`, and output acts on the left, `T -> (SGS)^{-1}T`. These operations
commute by associativity. There is no identification of an endpoint matrix
with its unswapped standard fractional-linear action.

## 3. Two all-time nonreturn results, with different hypotheses

### 3.1 Semantic interval states do not recur

At a completed source or output transition put

\[
 \Phi(I_k,J)=|I_k|\,|J|=\frac{W_k}{bd}>0.
\]

The multiplicative change is `j/(2j+1)` for source factor `j`, `d/(b+d)`
for `L`, and `b/(b+d)` for `R`. Each is strictly less than one. Therefore
the pair of actual rational intervals cannot recur, even after removing
counters, output history, and source-stage labels from the record.

This argument applies to completed semantic transitions, not every Python
instruction. A decreasing positive rational can descend forever; this is
an anti-cycle potential, not a termination ranking into the natural numbers.
The argument alone says nothing about eventual repetition of output labels.

### 3.2 Normalized residuals never recur for a nonquadratic input

Let `m>n`. The chart identity gives `B_m=B_n H`, where `H` is the nonempty
positive word obtained by swapping the output generators between these
states. Hence `z_n=H(z_m)`. If `z_n=z_m=z` and

\[
 H=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix},
\]

then

\[
 \gamma z^2+(\delta-\alpha)z-\beta=0. \tag{1}
\]

A nonempty positive generator word has a positive off-diagonal entry, so it
is not scalar and this polynomial is nonzero. Thus `z` is algebraic of degree
at most two. The rational fractional-linear relation `pi=B_n(z)` would make
`pi` algebraic of degree at most two as well, a contradiction. The weakest
hypothesis used here is nonquadraticity; classical transcendence supplies it
for pi. The runtime does not call a transcendence oracle.

This proves pairwise distinction of the normalized *real* states. They have
computable rational names, not finite exact numerical values stored by the
program. The separation algorithms in Section 6 convert that semantic
distinction into finite checkable observations.

An eventual single-letter tail converges to a rational endpoint. An eventual
mixed periodic tail has a quadratic fixed residual as in (1), since its
repeated cylinder intervals shrink to the positive fixed point. Consequently
the pi word is not eventually periodic. This is an all-time proof with an
explicit classical dependency, not a conclusion drawn from a long trace.

**Quadratic negative control.** The input `(9-sqrt(5))/2` in `(3,4)` has
local word `(LR)^infinity`. Its initial residual is `(sqrt(5)-1)/2`, which
returns after `L` then `R`. Its interval states still refine strictly.
Therefore the interval potential cannot by itself prove output aperiodicity.

## 4. A maximal-run observer with exact guards

Assume the target is irrational and the rational source shrinks strictly
around it. First refine until

\[
 a/b<l<u<c/d,\qquad I_k=[l,u]. \tag{2}
\]

This is always eventually possible at a fixed reachable state. Set

\[
 z_-=\frac{bl-a}{c-dl},\qquad
 z_+=\frac{bu-a}{c-du}.
\]

Both denominators are positive. The target residual lies strictly between
`z_-` and `z_+`. We use these conservative, exact guards:

| Candidate run | Interval guard | Integer length |
|---|---|---|
| `R` | `1<z_-` and `floor(z_-)=floor(z_+)` | `r=floor(z_-)>=1` |
| `L` | `z_+<1` and `floor(1/z_+)=floor(1/z_-)` | `r=floor(1/z_+)>=1` |

If neither guard succeeds, refine the source and retry. Equal endpoint
floors are a sufficient test. They intentionally make no special attempt
to exploit the target's strict interior when an endpoint is an integer.
They cannot accept a floor cell crossed by the target.

For `R`, the maximal repeated run has length `floor(z)`, because each step
subtracts one and the final residual `z-r` is in `(0,1)`. For `L`, write
`y=1/z`; each `L` subtracts one from `y`. The maximal length is `floor(y)`,
and the final residual is

\[
 z'=\frac{z}{1-rz}=\frac1{1/z-r}>1.
\]

The residual, and also its reciprocal, are irrational because they are
nondegenerate rational fractional-linear transforms of the irrational
target. They therefore have positive distance from the nearest integers.
Source refinement eventually certifies the relevant floor cell. This
productivity proof needs **irrationality only**, not nonquadraticity.

Closed updates avoid emitting every arrow merely to locate the next run:

\[
 EL^r:\ (a,b,c,d)\mapsto(a,b,c+ra,d+rb),
\]
\[
 ER^r:\ (a,b,c,d)\mapsto(a+rc,b+rd,c,d).
\]

The records should retain direction, length, input chart, source stage and
interval, transformed floor interval, and resulting chart. The certificate
verifier checks these exact equalities and inequalities. Merely returning a
positive integer with an alternating branch label loses the proof of
maximality.

### 4.1 Exact precision transfer near chart poles

The exact width identities are

\[
 z_+-z_-=\frac{u-l}{(c-du)(c-dl)}, \tag{3}
\]
\[
 \frac1{z_-}-\frac1{z_+}
 =\frac{u-l}{(bl-a)(bu-a)}. \tag{4}
\]

They follow by subtraction and `bc-ad=1`. In differential form the factors
are `1/(c-dx)^2` and `1/(bx-a)^2`. A tiny source interval can become a large
residual interval near a chart endpoint. Source stage, individual-arrow
index, and maximal-run index are distinct clocks. None may be substituted
for another in a quantitative claim without this conditioning information.

The strict-interior test (2) is necessary for these interval formulas as
written. Monotonicity cannot justify using the endpoints across a pole.
The existing single-arrow cross-product algorithm does not need this extra
test; the accelerated residual algorithm does.

## 5. Natural-number streams preserve the whole computation

Every infinite irrational LR path has both letters infinitely often: an
eventually constant path names a rational endpoint. Its unique maximal-run
decomposition therefore has the form

\[
 (\varepsilon;r_0,r_1,r_2,\ldots),\qquad
 \varepsilon\in\{L,R\},\quad r_i\in\mathbb N_{>0},
\]

with the letter alternating at each run. Expansion repeats the current
letter `r_i` times. Compression scans to the next different letter; every
run is finite, so this scan is productive on the stated domain. These maps
are inverse on infinite words containing both letters infinitely often.
The direct floor observer computes the same lengths without the scan.

Finite arrow products and the corresponding powered-generator products are
equal. Thus the number stream determines every endpoint chart and the same
limiting real. It retains the geometry-selected semantics, not only a hash
of a finite word. In the local `(3,4)` chart the pi stream begins

\[
 (L;6,15,1,292,1,1,1,2,1,3,1,14,\ldots).
\]

The first length is `6`, not `7`: the global root prefix `RRRL` already
contains the first `L` of the global run.

If the positive-integer length stream were eventually periodic with period
`q`, the sequence of labelled runs would have period dividing `2q`; after
expansion this would produce an eventual periodic binary word. Hence the
pi length stream is not eventually periodic. **The branch-label sequence
of maximal runs is periodic by construction.** Lengths must be retained.

This is a useful semantic compression and a productive change of output
type. It is not a new theorem about continued fractions. It proves neither
that these lengths are bounded nor that their empirical distribution has
any specified limit.

## 6. Effective rational probes separating normalized states

### 6.1 One finite family, one common source stage

Take `m` distinct states from the pi orbit, with charts `E_1,...,E_m`.
Refine a single copy of the original source until (2) holds for all charts.
Apply each increasing inverse chart to obtain rational intervals
`[l_i,u_i]`. Continue refining until, after sorting by lower endpoint,

\[
 u_i<l_{i+1}\qquad(1\le i<m). \tag{5}
\]

The normalized residuals are pairwise distinct by Section 3.2. A finite
family has a positive minimum pairwise separation, and each transformed
interval converges to its own residual. Therefore this algorithm halts.
Its runtime operations are rational; no exact ordering oracle is supplied.

Define the rational separators

\[
 q_i=(u_i+l_{i+1})/2.
\]

The `m-1` truth values `q_i<z` have a different profile at each state. This
gives a finite certificate of distinction using only rational tests. The
certificate consists of the common source interval, charts, sorted
transformed intervals and separators; every displayed inequality is
checkable by exact arithmetic.

**Optimality within this probe class.** A fixed nonadaptive collection of
`t` ordered threshold predicates `q<z` has at most `t+1` different profiles
on the real line. Consequently `m-1` thresholds are necessary and sufficient
to distinguish `m` ordered states this way. Arbitrary binary predicates and
adaptive questions are different probe classes. After storing the ordered
thresholds, binary search identifies an unknown member of the certified
finite family in at most `ceil(log2(m))` adaptive comparisons.

No positive lower bound for the gaps of the entire infinite orbit follows.
Finite-family uniformity means that a **given finite family** shares one
computed source stage. It is not a uniform Diophantine estimate over all
state indices.

### 6.2 A quantitative deadline from correlated polynomial certificates

There is a useful refinement beyond independently shrinking every interval.
In this subsection take `m>=2`; a singleton needs no pairwise gap.
For two charts, write their entries as `(a,b,c,d)` and `(A,B,C,D)`. At a
common real argument `x`,

\[
 z_1(x)-z_2(x)=\frac{P_{12}(x)}{(c-dx)(C-Dx)}, \tag{6}
\]

where

\[
 P_{12}(x)=(Bd-bD)x^2+(bC+aD-Bc-Ad)x+(Ac-aC).
\]

This comparison keeps the common input correlated. A nonzero polynomial of
degree at most two cannot vanish at the nonquadratic target. For
`P(x)=p_2x^2+p_1x+p_0` and `x in [3,4]`, put

\[
 M=|p_1|+8|p_2|,\qquad h=(l+u)/2,
\]

so the mean value theorem gives the rational enclosure

\[
 P(\pi)\in[P(h)-M(u-l)/2,\ P(h)+M(u-l)/2]. \tag{7}
\]

Refinement eventually makes (7) exclude zero for every pair. Suppose a
single stage `k_0` satisfies that condition and lies strictly inside every
chart. Let `delta_ij>0` be the distance of the polynomial enclosure from
zero. The denominator in (6) is positive and at most its value at `l`, so

\[
 |z_i-z_j|\ge
 \frac{\delta_{ij}}{(c_i-d_i l)(c_j-d_j l)}.
\]

Take the minimum of these finitely many rational bounds to obtain `Delta>0`,
and set

\[
 \eta=\min_i(c_i-d_i u)>0,\qquad W=u-l.
\]

Future source intervals stay inside `[l,u]`. Equation (3) and source
contraction imply that after `s` further beta factors every transformed
interval has width at most `W*2^(-s)/eta^2`. Therefore

\[
 \frac{2W\,2^{-s}}{\eta^2}<\Delta \tag{8}
\]

is an explicit sufficient deadline for **all** transformed intervals to be
pairwise disjoint. The least sufficient `s` can be found by incrementing
`s` while successively doubling `2^s`, using rational comparisons; no
logarithm evaluation is required.

Indeed the gap between two true residuals exceeds the sum of their interval
widths, so their intervals cannot overlap. This turns a finite nonvanishing
certificate into a finite-family separation horizon. This local argument
does not provide a useful a priori stage bound from coefficient height
alone. The companion [UNIFORM_BOUNDS.md](UNIFORM_BOUNDS.md) supplies an
astronomical pi-specific uniform bound using an additional classical
transcendence measure. Mere qualitative nonquadraticity does not supply
that quantitative estimate.

## 7. The cut is a family of rational representables

Let `Q` be the category of rational numbers with one arrow `q -> r` when
`q<=r`. For a real `z`, define the subterminal presheaf

\[
 D_z:\mathbb Q^{op}\to\mathbf{Set},\qquad
 D_z(q)=\begin{cases}\{*\}&q<z,\\\varnothing&q\ge z.\end{cases}
\]

Restrictions take a successful larger rational test to a smaller one.
Directly, with no faithfulness assumption hidden,

\[
 \operatorname{Nat}(D_x,D_y)=
 \begin{cases}\{*\}&x\le y,\\\varnothing&x>y.\end{cases} \tag{9}
\]

If `x<=y`, every occupied component of `D_x` is occupied in `D_y`, and all
maps are forced. If `x>y`, rational density supplies `y<q<x`; the component
would require a map from a singleton to the empty set. Thus `z -> D_z` is a
fully faithful embedding of the real order category into rational
presheaves. Restricted to irrationals, it gives the requested category of
irrational cuts. Its image consists of the inhabited proper lower-cut
presheaves with no greatest successful rational and no least unsuccessful
rational. Rational cuts fail the latter condition at their rational boundary.

For `y(q)=Q(-,q)`, the category of elements of `D_z` is just the ordered
category of rationals strictly below `z`. It is filtered. Pointwise,

\[
 D_z\cong\operatorname*{colim}_{q<z}y(q). \tag{10}
\]

To check (10) at a rational `r`, the colimit is inhabited exactly when some
`q<z` satisfies `r<=q`, equivalently `r<z`; filteredness identifies all its
inhabitants. This is the concrete Yoneda/density link: a real state becomes
a coherent family/category of rational representables. The finite probes
from Section 6 expose separating components of those presheaves, together
with exact computational witnesses.

For an irrational residual, every fixed rational query is eventually
decidable by its shrinking interval name: it cannot equal the threshold.
This effectiveness is extra structure supplied by the finite source. The
abstract category of all irrational cuts includes noncomputable objects;
category theory does not give each of them a finite generating program.

**Chronology has a different type.** Consecutive residuals do not always
increase. An `R` step decreases `z`; an `L` step increases it. Consequently
one must not claim an order-natural transformation `D_(z_n) -> D_(z_(n+1))`
at every time. Computational arrows are labelled fractional-linear changes
of chart. On their increasing domains, rational tests transport by inverse
image: `q<g(z)` iff `g^(-1)(q)<z`, with the range/domain qualifications
retained. The rational map and its chart identify this transport. The cut
embedding classifies order comparisons; the labelled action records time.

Equations (9) and (10) are standard categorical phenomena specialized and
proved here. The useful additional local result is the certified finite
observation interface and the quantitative horizon (8). No claim of
literature novelty is made.

**An equivalence can forget the computational problem.** The same quadratic
fixed-point argument shows that `PGL_2(Q)` acts freely on the orbit of a
nonquadratic real. A transitive free action has exactly one groupoid arrow
between any two orbit objects, so its action groupoid is equivalent to the
terminal category. This is a valid equivalence and a poor model of cost or
observation by itself. Source names, rational probes, chart labels and
resource measures must be retained when an equivalence is intended to
transport computational information. Replacing the enriched data by the
bare action groupoid would discard the structure doing the useful work.

## 8. Independent finite arithmetic receipt

An inline Python standard-library calculation was run against the frozen
baseline checkout. It used a **separate scalar recurrence**

```python
partial += 2 * weight
k += 1
weight *= Fraction(k, 2*k + 1)
lower, upper = partial + 3*weight, partial + 4*weight
```

and its own run guards and closed endpoint updates from Section 4. It did
not call production matrix multiplication to choose its runs. It checked
both exact width identities at every successful guard. The resulting
expanded word was compared with the existing single-arrow observer using
each of the beta-matrix and independent circle-rotation sources. One extra
arrow verified that the last emitted run was maximal.

| Check | Observed result |
|---|---|
| Maximal runs computed independently | 48 |
| Expanded arrows | 637 |
| Scalar source stage for the last run | 178 |
| Matrix-source stage through one extra arrow | 178 |
| Rotation-source stage through one extra arrow | 44 |
| Expanded word agreement | exact for all 637 arrows, both sources |
| Expanded word SHA-256 | `417a4bfbc390a5de7a507d418358ba1ef4c1b2ae1a0763a333a0526507e7007b` |
| Normalized states probed | indices 0 through 24 |
| Common beta-source stage | 28 |
| Rational threshold count | 24 |
| Distinct threshold profiles | 25 |

The first twelve triples `(letter, length, source_stage)` were

```text
(L,6,6), (R,15,17), (L,1,17), (R,292,28),
(L,1,31), (R,1,31), (L,1,33), (R,2,34),
(L,1,36), (R,3,39), (L,1,40), (R,14,48).
```

The exact minimum gap between adjacent transformed enclosures of the 25
states was

```text
528188371393502173132049257454527930698409 /
16210922654502751565513716621244010562272668
```

Their increasing residual order, expressed as original time indices, was

```text
0,1,2,3,4,5,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,24,23,22
```

This visibly distinguishes order from chronology. These finite observations
validate the arithmetic formulas and conventions at the stated scope. The
all-time claims rest on the proofs above. Shared observer code means that
the two source runs are not completely independent implementations; the
scalar maximal-run computation is the separate arithmetic route.

The quadratic difference identity was additionally checked exactly at the
source midpoint for all 300 pairs of these 25 charts. All 300 polynomial
enclosures exclude zero simultaneously at beta-source stage 44; the direct
interval algorithm had already separated this particular family at stage
28. Thus the general certificate deadline is useful as a verified bound,
but the coarse derivative bound in (7) is not a performance improvement in
this example. Examining each pair separately gave 77 cases with a positive
additional deadline; all 77 had disjoint intervals at that predicted stage.
For states `0` and `7`, the certificate was found at stage `6`, predicted
`17` additional source factors, and the intervals were disjoint at stage
`23`. The deadline was computed before those additional factors were read.
This illustrative pair was selected from the finite exploration; it is not
an independently held-out example.

### 8.1 Subsequent staged-implementation audit

The staged `RunObserver` and `rational_pinbed` implementations were read and
executed without editing their code. The test harness relocated only the
module's `__file__` value to its intended sibling-source layout, so its
unchanged import expression could find the preceding round's module.

For each geometric source, 48 run certificates were checked against source
intervals recomputed by scalar beta recurrences or direct finite alternating
rotation sums. The audit also checked the transformed intervals, equal
floors, integer run length, closed chart update, accumulated arrow offsets,
letter alternation and the next-arrow boundary. Both expanded streams had
the 637-arrow hash recorded above.

Singleton pinbeds `[0]` and unsorted sparse pinbeds
`[24,0,7,3,6,21,22,100,314]` passed for both sources. The audit reconstructed
all selected charts directly from the certified output word and checked the
common source interval, value ordering, rational thresholds and distinct
cut profiles. Empty, negative and duplicate index inputs were rejected.

The staged run implementation uses `zlo>=1` or `zhi<=1`, slightly weaker
than the conservative strict guards of Section 4. This is sound because the
target is strictly inside its source interval. Synthetic exact-interval
fixtures checked both equality cases and checked that an upper endpoint on
the next integer floor boundary forces refinement, for both the `R` and
reciprocal-`L` guards. All four fixtures passed. No algorithmic correction
was needed in these two implementations. This finite code audit supplements
the all-time proofs; it is not a formal verification.

## 9. Claim ledger and next discriminating probes

| Claim | Status and exact boundary |
|---|---|
| Finite program gives a total stream coalgebra | Disclosed by the comparison/productivity proof; arbitrary-size registers |
| Interval pairs never repeat | Disclosed by the rational anti-cycle potential; semantic transition scope |
| Normalized pi residuals are pairwise distinct | Disclosed conditional on imported nonquadraticity |
| Maximal-run floor algorithm is productive | Disclosed for a shrinking strict source of an irrational |
| Compression preserves the represented real | Disclosed on paths with both letters infinitely often |
| Pi run-length stream is not eventually periodic | Disclosed using the nonquadraticity dependency |
| Every finite residual family has computable rational separators | Disclosed for pairwise distinct named residuals |
| `m-1` separators are minimal | Disclosed only for fixed nonadaptive rational threshold tests |
| Polynomial certificate gives separation deadline (8) | Disclosed under its explicit chart, sign and interval premises |
| 48 maximal runs and 25-state separator family | Observed with the scope and hashes above |
| Uniform small runtime, global minimum residual gap, digit normality | Not established |
| Novel theorem in the literature | Not claimed; no novelty search supports that label |

The strongest direct falsifiers are a wrong chart sign, a floor interval
crossing an integer, an omitted final run boundary, or a quadratic input
incorrectly classified as nonperiodic. The pairwise polynomial denominator
bound should also be mutated: reducing a certified denominator upper bound
can produce a false claimed gap even if its numerator sign is correct.

A further proof frontier is a practical a priori estimate on the separation
certificates as functions of state/period size. The local method supplies
a computable horizon *after* finite sign separation. The additional import
in `UNIFORM_BOUNDS.md` supplies a uniform but astronomical estimate; neither
result establishes source-specific signed temporal cancellation in the
larger research program.

## 10. Primary literature and provenance

- Jeremy Gibbons, **Metamorphisms: Streaming Representation-Changers**,
  *Science of Computer Programming* 65(2), 2007, 108–139.
  [Author manuscript](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/metamorphisms-scp.pdf).
  Sections 4 and 5 discuss safe streaming and continued-fraction conversion.
  Theorem 6 explicitly states a finite-input theorem; it must not be cited
  alone as proof that a particular infinite-source program is productive.
  The local guards and productivity proof above supply the needed argument.
- Jeremy Gibbons, **Unbounded Spigot Algorithms for the Digits of Pi**.
  [Author manuscript](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf).
  The safe interval/fractional-linear method is relevant. The later
  conjectural guard-removal shortcut is not used by this construction.
- J. J. M. M. Rutten, **Universal coalgebra: a theory of systems**,
  *Theoretical Computer Science* 249(1), 2000, 3–80.
  [CWI publication record](https://ir.cwi.nl/pub/48).
  This is background for the stream-coalgebra language. The publication
  record was retrieved; the linked 14 MB final PDF exceeded the retrieval
  limit. No detailed theorem attribution depends on an unread page of it.
- Emily Riehl, **Category Theory in Context**,
  [author-hosted text](https://emilyriehl.github.io/files/context.pdf),
  Chapter 2, especially Yoneda and the category of elements, and the density
  theorem6.5.9 for the canonical colimit of representables.
  The elementary subterminal-presheaf arguments needed here are given in
  full in Section 7, rather than delegated to the text.

All source checks were performed on 2026-11-11. The circle integral, beta
source, metric qualifications and baseline observer correctness remain
those proved in the preceding repository round. This note derives the
new local formulas directly and records which claims use imported
irrationality or nonquadraticity.

## Appendix: reproducing the finite receipt

Run from the repository root using Python 3. The script is intentionally
small and uses the frozen baseline module only for the comparator streams;
the accelerated scalar source and maximal-run computation are separate.

```python
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

sys.path.insert(0, str(Path(
    "research/2026-11-10/circle_line_lr_observer").resolve()))
from circle_line_observer import (
    MatrixCircleSource, RotationCircleSource, SternBrocotObserver,
)

k, weight, partial, lo, hi = 0, Q(1), Q(0), Q(3), Q(4)

def refine_scalar():
    global k, weight, partial, lo, hi
    partial += 2 * weight
    k += 1
    weight *= Q(k, 2*k + 1)
    lo, hi = partial + 3*weight, partial + 4*weight

a, b, c, d = 3, 1, 4, 1
records = []
for _ in range(48):
    while True:
        if Q(a,b) < lo < hi < Q(c,d):
            zl = (b*lo-a)/(c-d*lo)
            zu = (b*hi-a)/(c-d*hi)
            assert zu-zl == (hi-lo)/((c-d*hi)*(c-d*lo))
            if zl > 1:
                rl, ru, letter = zl, zu, "R"
            elif zu < 1:
                rl, ru, letter = 1/zu, 1/zl, "L"
                assert ru-rl == (hi-lo)/((b*lo-a)*(b*hi-a))
            else:
                refine_scalar()
                continue
            r = rl.numerator // rl.denominator
            if r >= 1 and r == ru.numerator // ru.denominator:
                break
        refine_scalar()
    records.append((letter, r, k))
    if letter == "L":
        c, d = c+r*a, d+r*b
    else:
        a, b = a+r*c, b+r*d
    assert b*c-a*d == 1

word = "".join(letter*r for letter, r, _ in records)
for Source in (MatrixCircleSource, RotationCircleSource):
    observer = SternBrocotObserver(Source())
    actual = "".join(observer.next_arrow()["arrow"]
                     for _ in range(len(word)+1))
    assert actual[:-1] == word
    assert actual[-1] != records[-1][0]

observer = SternBrocotObserver(MatrixCircleSource())
charts = [(observer.a, observer.b, observer.c, observer.d)]
for _ in range(24):
    observer.next_arrow()
    charts.append((observer.a, observer.b, observer.c, observer.d))

def image(chart, source):
    a, b, c, d = chart
    l, u = source.lower, source.upper
    assert Q(a,b) < l < u < Q(c,d)
    return ((b*l-a)/(c-d*l), (b*u-a)/(c-d*u))

source = MatrixCircleSource()
while True:
    if all(Q(a,b) < source.lower < source.upper < Q(c,d)
           for a,b,c,d in charts):
        intervals = sorted((*image(chart, source), i)
                           for i, chart in enumerate(charts))
        if all(left[1] < right[0]
               for left, right in zip(intervals, intervals[1:])):
            break
    source.refine()
thresholds = [(left[1]+right[0])/2
              for left, right in zip(intervals, intervals[1:])]
profiles = set()
for l, u, _ in intervals:
    assert all(q < l or q > u for q in thresholds)
    profiles.add(tuple(q < l for q in thresholds))
assert len(profiles) == len(charts)
assert source.stage == 28

# Correlated polynomial deadline for the illustrative pair 0,7.
# No future source factors are read until the deadline has been computed.
(a,b,c,d), (A,B,C,D) = charts[0], charts[7]
p2, p1, p0 = B*d-b*D, b*C+a*D-B*c-A*d, A*c-a*C
future = MatrixCircleSource()
while True:
    l, u = future.lower, future.upper
    if Q(a,b) < l < u < Q(c,d) and Q(A,B) < l < u < Q(C,D):
        h = (l+u)/2
        value = p2*h*h+p1*h+p0
        delta = abs(value) - (abs(p1)+8*abs(p2))*(u-l)/2
        assert ((b*h-a)/(c-d*h) - (B*h-A)/(C-D*h)
                == value/((c-d*h)*(C-D*h)))
        if delta > 0:
            break
    future.refine()
gap = delta/((c-d*l)*(C-D*l))
eta = min(c-d*u, C-D*u)
extra = 0
while 2*(u-l)/(2**extra*eta**2) >= gap:
    extra += 1
certificate_stage = future.stage
for _ in range(extra):
    future.refine()
pair = sorted(image(charts[i], future) for i in (0,7))
assert pair[0][1] < pair[1][0]
assert (certificate_stage, extra, future.stage) == (6,17,23)

print(json.dumps({
    "runs": len(records), "arrows": len(word),
    "sha256": hashlib.sha256(word.encode()).hexdigest(),
    "probe_stage": source.stage, "profiles": len(profiles),
    "deadline_pair": [0,7], "certificate_stage": certificate_stage,
    "extra_source_factors": extra, "deadline_stage": future.stage,
}, indent=2))
```
