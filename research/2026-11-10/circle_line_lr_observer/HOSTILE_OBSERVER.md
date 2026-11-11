# Circle–line observer: adversarial proof audit

Date: 2026-11-11. Scope: an independent adversarial audit of a proposed finite program which derives a geometric real from a Euclidean circle and line, then emits an infinite Stern–Brocot L/R word recovering that real. Baseline inspected: SUCC branch `aletheia/cursed-categories-dedekind-yoneda-2026-11-10`, commit `964768cd1fa5116f521625abfaaad8d8fab0f222`.

This audit supplies proofs, explicit countermodels, and mutation controls. It does not claim a proof of base-16 normality, hexadecimal parity cancellation, or RH. The small executions below verify implementation conventions and finite examples; the universal conclusions come from the stated arguments.

## 1. Contract and verdict

**Steelman.** The requested construction is possible. A finite program can contain exact definitions of a Euclidean unit circle, a line with the same length unit, a rational parametrization, and a certified integration procedure. It can derive shrinking rational enclosures for the circumference/diameter ratio, compare these enclosures with successive rational mediants, and produce every finite L/R prefix in finite time. The nested rational intervals then have the geometric number π as their unique intersection. No stored digits of π or branch oracle are needed.

**Crucible.** The following are load-bearing rather than decorative:

1. The shared Euclidean metric and the circumference/diameter normalization.
2. Correct right multiplication and endpoint orientation for L/R.
3. Sound shrinking enclosures, and the irrationality theorem when demanding a decision at every rational mediant.
4. Unbounded working memory despite a finite program.
5. A distinction between radians on the geometric circle and turns on the arithmetic phase circle.
6. Authentication of the literal zero-seed BBP orbit when transferring the construction into the existing program.

**Verdict.** A successful observer proves computability and exact representation of geometric π. That is a real theorem with a useful independently derived implementation. Its bare finite-program shape, L/R grammar, nonperiodicity, or transcendence cannot prove digit cancellation: an explicit computable transcendental countermodel below satisfies those broad properties and has hexadecimal digit-parity average tending to +1. A future theorem must use additional source-specific arithmetic retained by the geometric construction.

## 2. Where geometry actually enters

Let the observer's line be the real coordinate axis with its Euclidean length. Let its circle be

$$
C=\{(x,y):x^2+y^2=1\}
$$

with the metric induced from the Euclidean plane. Use the rational map

$$
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),\qquad 0\le t\le1.
$$

Direct algebra proves that its image is the first-quadrant arc from `(1,0)` to `(0,1)`. Its derivative satisfies

$$
x'(t)=\frac{-4t}{(1+t^2)^2},\quad
y'(t)=\frac{2(1-t^2)}{(1+t^2)^2},\quad
\|P'(t)\|^2=\frac4{(1+t^2)^2}.
$$

Consequently the quarter-circle length is

$$
\int_0^1\frac2{1+t^2}\,dt.
$$

Reflection symmetry gives four equal quarters; the diameter has length 2. Thus the circumference/diameter ratio is

$$
\pi_{\rm geom}=4\int_0^1\frac{dt}{1+t^2}.
\tag{G}
$$

This derivation does not start with a numerical value or digit sequence for π. It does use the ordinary arc-length theorem, reflection invariance, and a shared Euclidean metric. Those are the internal semantics that make the symbol “circle” operational.

### An independent, deliberately slow rational certificate

For the decreasing function `f(t)=4/(1+t²)`, define

$$
\ell_N=\sum_{j=1}^N\frac{4N}{N^2+j^2},\qquad
u_N=\sum_{j=0}^{N-1}\frac{4N}{N^2+j^2}.
$$

Every term is rational; strict monotonicity yields

$$
\ell_N<\pi_{\rm geom}<u_N,\qquad
u_N-\ell_N=\frac2N.
\tag{R}
$$

The gap identity follows by cancellation of the common summands: only `f(0)/N-f(1)/N` remains. Dyadic refinement gives nested enclosures. Already `N=8` verifies `3<ℓ₈<u₈<4` by exact rational arithmetic, so initialization at `[3,4]` needs no decimal π constant.

This quadrature is a useful independent correctness route, not a proposed performance benchmark. A faster proved arctangent, polygon, or other rational compiler may replace it without changing the interface.

### Metric mutations

| Mutation | Predicted result | What it tests |
|---|---|---|
| Replace the arclength weight `1/(1+t²)` in (G) by `1` | The alleged ratio becomes 4 | A rational parametrization is not itself an arclength parametrization |
| Drop the circumference or diameter normalization | A multiple such as π/2 or 2π is produced | The ratio, not an unnamed arc length, is the target |
| Retain only the circle's topology and allow an independently scaled intrinsic circle metric | The ratio against the fixed line unit can change | Topology alone does not determine a length ratio |
| Scale the entire Euclidean configuration, circle and line units coherently | The ratio stays π | A required positive scale-invariance control |
| Reverse parametrization orientation | Unsigned arclength stays the same | The observer must distinguish length from signed angle |

The third row is a countermodel only to the topology-only claim. It is not a countermodel to the fully specified Euclidean circle, whose metric fixes the ratio. Similarly, merely changing radius within Euclidean geometry cannot refute the construction: circumference and diameter both scale.

## 3. Correct L/R typing and the infinite-run theorem

Write an endpoint state as

$$
E=\begin{pmatrix}a&c\\b&d\end{pmatrix},\qquad
\frac ab<\frac cd,\quad b,d>0,\quad bc-ad=1.
$$

The endpoint determinant is `ad-bc=-1`. The generators themselves have determinant +1:

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

They act **on the right**:

$$
EL=\begin{pmatrix}a&a+c\\b&b+d\end{pmatrix},\qquad
ER=\begin{pmatrix}a+c&c\\b+d&d\end{pmatrix}.
$$

Thus `L` selects the left child and `R` the right child of the mediant `m=(a+c)/(b+d)`. This matches the existing Round III convention. Multiplying on the left is a different action, not a harmless notation change.

For `E₀=[[3,4],[1,1]]` the exact mutation outcomes are

$$
EL=[3,7/2],\quad ER=[7/2,4],\quad
LE=[4,5],\quad RE=[3/4,4/5].
$$

### Proposition: a finite program emits the entire geometric π word

At a current mediant `m`, repeatedly refine the rational geometric enclosure until either `u_N<m` or `ℓ_N>m`. Emit `L` in the first case and `R` in the second, update the endpoint matrix, and repeat.

**Halting of each comparison.** π is irrational, so the current rational mediant differs from π by some positive distance. The sound interval width `2/N` tends to zero, so a sufficiently refined enclosure lies strictly on the correct side. The search terminates. Irrationality is a theorem used in the totality proof; it is not a hidden numerical branch oracle.

**Preservation.** Exact integer arithmetic proves the endpoint determinant condition and strict enclosure of π after each update.

**Convergence.** At each step one of the positive denominators `b,d` is replaced by `b+d`. Hence `b+d` increases by at least 1. Since

$$
bd\ge b+d-1,
$$

the product `bd` tends to infinity. The interval width is exactly

$$
\frac cd-\frac ab=\frac1{bd}\longrightarrow0.
$$

The nested closed intervals all contain π and have vanishing width, so their unique common point is π. A reader can recover π to any requested rational tolerance by running until `1/(bd)` is below that tolerance.

**Dependency boundary.** This proof imports the classical irrationality theorem for geometric π. Certified intervals alone do not decide equality to a rational for a generic computable real. If a generic target equals a mediant, this strict comparison loop need never terminate. Exact rational termination requires an additional representation or equality certificate; it cannot be silently supplied by a Cauchy-name oracle. If only a shrinking sequence of intervals is requested, irrationality is unnecessary.

### Finite description is not finite state

The program has finitely many instructions but uses integers, denominators, and precision counters of unbounded size. This is necessary for the intended autonomous exact output.

An autonomous deterministic finite-state machine eventually revisits a state and thereafter repeats its output cycle. An eventually periodic L/R word has a limit of degree at most two:

- An eventual constant tail converges to a rational endpoint.
- A periodic tail containing both letters corresponds to a positive integer matrix in `SL₂`. Its projective fixed point satisfies a quadratic equation. A finite prefix acts by a rational Möbius map and preserves algebraic degree at most two.

Therefore the transcendence of π rules out an autonomous finite-state machine emitting this exact infinite word. This argument does not exclude finite-state transducers receiving an infinite informative input; the information would then be in the input. It also says nothing about normality.

A useful explicit control is the periodic word `(LR)^∞` from `[3,4]`. Its limit is

$$
\frac{9-\sqrt5}{2},
$$

the root in `[3,4]` of `x²-9x+19`. Its existence demonstrates that the same legal matrix grammar also produces a completely different exact real.

## 4. The dangerous normalization: there are two circle clocks

The geometric unit circle receives angles in radians:

$$
\theta\longmapsto \exp(i\theta),\qquad
\theta\in\mathbb R/(2\pi\mathbb Z).
$$

The existing digit/Fourier observer uses turns:

$$
e(x)=\exp(2\pi ix),\qquad x\in\mathbb R/\mathbb Z.
$$

These circles are isomorphic, but the isomorphism includes division or multiplication by `2π`. Forgetting that normalization destroys the source orbit.

The authenticated completed BBP source is

$$
U_n+T_n=16^{n-1}\pi.
$$

Its phase is `e(16^(n-1)π)`, with π interpreted as a **number of turns** in this expression. It is not `exp(i16^(n-1)π)`. The latter equals `-1` at `n=1` and equals `1` for every `n≥2`, since `16^(n-1)` is then even. Thus a superficially plausible “feed the geometric angle into the expanding circle map” implementation collapses the orbit after one sample.

This is an exact, decisive negative control. The proper observer retains its units and never identifies those two expressions. Because π is irrational, the proper phase `e(16^(n-1)π)` is not a root of unity for any finite `n`.

### Rotation is also different from expansion

For an irrational `α` and fixed nonzero integer `h`, the additive rotation has the elementary geometric-series estimate

$$
\left|\frac1N\sum_{n=1}^N e(hn\alpha)\right|
\le \frac2{N|1-e(h\alpha)|}\longrightarrow0.
$$

The source asks about `e(h16^n α)`, whose phases are generated by an expanding map. Their successive ratios are not constant, so the rotation proof does not transfer. Knowing that a point is irrational on a circle does not establish equidistribution under multiplication by 16.

## 5. A computable transcendental countermodel to algorithm-shape inference

Define

$$
\alpha=3+\sum_{k=1}^{\infty}16^{-k!}.
\tag{C}
$$

Its hexadecimal fractional digits are 1 in positions `1,2,6,24,120,720,…` and 0 elsewhere. There are no carries. If

$$
\alpha_n=3+\sum_{k=1}^n16^{-k!},
$$

then a geometric majorant gives

$$
0<\alpha-\alpha_n
<\frac{16}{15}\,16^{-(n+1)!}
<2\,16^{-(n+1)!}.
\tag{T}
$$

This is an effective exact rational enclosure. The same mediant comparison program therefore emits every finite L/R prefix of α, with strict comparison guaranteed by irrationality.

**Irrationality.** There are infinitely many 1s, but the zero runs between them have unbounded length. Its digit string is not eventually periodic, so α is irrational.

**Transcendence, if that extra property is demanded.** Write `α_n=p_n/q_n` with `q_n=16^(n!)`. Bound (T) yields

$$
0<|\alpha-p_n/q_n|<2q_n^{-(n+1)}.
$$

If α were algebraic with nonzero integer polynomial `P` of degree `d`, then `P(p_n/q_n)` would be a nonzero integer divided by `q_n^d`. A bound `M` on `|P'|` in a compact neighborhood of α would imply

$$
|\alpha-p_n/q_n|\ge\frac1{M q_n^d}
$$

for all sufficiently large `n`, contradicting the previous bound. Thus α is transcendental.

**Failure of the target statistic.** The number of factorial positions up to `N` is at most `1+log₂N`, since `k!≥2^(k-1)`. Hence the frequency of hexadecimal 1s tends to zero, the frequency of 0s tends to one, and

$$
\frac1N\sum_{j=1}^N(-1)^{d_j(\alpha)}\longrightarrow1.
$$

The same conclusion holds over dyadic epochs. This defeats the inference

> finite exact program + infinite L/R refinement + irrationality + transcendence ⇒ digit parity cancellation or normality.

It does **not** defeat a genuinely Euclidean-source-specific theorem. That distinction is the useful outcome of the control: a proposed bridge must identify precisely which additional property of (G), absent from (C), forces the needed signed cancellation. Merely calling the source geometric, natural, or coherent does not state that property.

## 6. What the construction can actually contribute to the frontier

### A proved precision-transfer interface

Suppose a rational reconstruction `x` satisfies `|π-x|≤δ`. For integer `h≠0` and an epoch `A≤n<2A`, the elementary Lipschitz bound for the character gives

$$
\begin{aligned}
&\left|\frac1A\sum_{n=A}^{2A-1}e(h16^{n-1}\pi)
-\frac1A\sum_{n=A}^{2A-1}e(h16^{n-1}x)\right|\\
&\qquad\le
\frac{2\pi|h|\delta}{15A}
\left(16^{2A-1}-16^{A-1}\right).
\end{aligned}
\tag{P}
$$

This makes the cost of transporting an approximation through the expanding observer explicit. L/R accuracy is genuine information, but expansion amplifies it exponentially in the epoch. A small error in the real number is not automatically a small error in a long digit block.

For the discontinuous digit-parity observable, propagate the entire rational enclosure. The digit is certified whenever the scaled interval stays within one cell of the boundary set `(1/16)ℤ`. If `B_A` indices in an epoch remain ambiguous, the discrepancy between two allowed parity sequences is at most `2B_A/A`. Irrationality guarantees that each fixed digit eventually becomes decidable, but does not by itself bound the fraction of near-boundary observations over growing epochs.

These are useful implementation/proof interfaces. They certify finite epoch values; they do not prove their limiting cancellation.

### A precise limit of rational-shadow arguments

For a rational approximation `p/q`, the expanding phases can be computed from residues `16^(n-1)p mod q`. Any argument invoking modular orbits must keep the 2-primary part of `q` as well as its odd part, and must state coprimality assumptions before treating multiplication by 16 as a permutation.

If only the ordinary upper error bound of order `q^(-2)` is available, choosing `q` much larger than `16^A` is a sufficient way to keep the entire epoch through roughly `2A` accurate. This is a sufficient precision criterion, not a necessary lower bound: exceptionally good approximants may behave better. At that denominator scale the orbit segment has length only logarithmic in `q`; a complete-period average or an error bound of size `sqrt(q)` does not automatically yield useful cancellation on that segment.

The new theorem would therefore need to control the actual, source-selected denominator and residue arithmetic on the required interval. An arbitrary rational approximant alone does not supply that control.

### The weaker existing target worth attacking

The current source frontier already isolates a weaker target than full normality. With the authenticated zero seed and the actual selected-prime/complement split,

$$
s_n=a_nb_n,\qquad
u_\pm(A)=\mathbb E[b_n\mid a_n=\pm1],
$$

the imported prime-balance hypothesis reduces parity cancellation to the conditional contrast

$$
u_+(A)-u_-(A)\longrightarrow0.
\tag{F}
$$

The balance hypothesis ensures both fibers eventually have the needed positive mass. A geometry-informed proof of (F) must still retain the complement, winding, exact seed, and tail. A generic prime witness or a different coherent seed is insufficient, as the existing frontier's rational epoch and coherent-seed controls show.

A result that merely rewrites (F) in L/R coordinates is an exact reformulation. A result deriving a new quantitative bound on that signed contrast, from a property of the geometric source which fails for the countermodel (C), would be a genuine new edge. Nothing in this audit establishes that bound.

## 7. Categorical scope guard

Yoneda faithfully records an object through its actual morphisms. It does not recreate a metric, length form, coordinate unit, seed, or observation map discarded before the embedding. A category of cut presentations can organize compatible rational refinements and their common real value. An equivalence of such presentations is useful if its functors and natural isomorphisms preserve the designated observer data.

Encoding arrows by natural numbers is a computable presentation only after domains, codomains, identity codes, and the composition operation are specified. Splitting those codes into families can preserve and expose composition, but the coding step does not itself introduce a cancellation estimate. Similarly, the line and circle are not homeomorphic; any claimed equivalence must name the categories being compared rather than equating those two underlying spaces.

The category-level hostile question is therefore concrete: after transporting around the proposed equivalence, does one recover the same rational enclosure, the same normalized geometric ratio, and the same literal BBP observation at every finite stage? If not, a coherence square has lost load-bearing data.

## 8. Executed controls and reproducibility

The following checks ran in Python using `fractions.Fraction`, not floating-point branch decisions. Process exit code was 0 and the script emitted `status: PASS`.

| Executed control | Exact scope | Observed outcome |
|---|---|---|
| L/R side mutation | Four matrix actions at `E₀` | All four endpoint pairs match Section 3 and are distinct |
| Geometric lower/upper sums | `N=2,4,8,16,32` | Exact width `2/N`; for `N≥8`, `3<ℓ_N<u_N<4` |
| Periodic word control | Forty successive `LR` products | Determinant, width, and opposite polynomial signs at endpoints all hold |
| Sparse-digit countermodel | First 1000 fractional digits | 6 ones, 994 zeros |
| Countermodel tail certificate | `n=1,…,6` | The geometric upper bound is strictly below `2·16^(-(n+1)!)` |

Decimal values printed for display only were:

| N | ℓ_N, approximate | u_N, approximate |
|---:|---:|---:|
| 2 | 2.6000000000 | 3.6000000000 |
| 4 | 2.8811764706 | 3.3811764706 |
| 8 | 3.0139884945 | 3.2639884945 |
| 16 | 3.0784416120 | 3.2034416120 |
| 32 | 3.1101798932 | 3.1726798932 |

The radians/turns control and infinite sparse-digit countermodel are proved symbolically above; no empirical phase plot is needed for those verdicts. This audit has not yet inspected the final implementation of the new observer, so implementation conformance beyond these isolated controls remains unverified.

### Reproduction script

```python
from fractions import Fraction as Q
from math import factorial

def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

def endpoints(E):
    return Q(E[0][0], E[1][0]), Q(E[0][1], E[1][1])

E = ((3, 4), (1, 1))
L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
assert endpoints(mul(E, L)) == (Q(3), Q(7, 2))
assert endpoints(mul(E, R)) == (Q(7, 2), Q(4))
assert endpoints(mul(L, E)) == (Q(4), Q(5))
assert endpoints(mul(R, E)) == (Q(3, 4), Q(4, 5))

for n in (2, 4, 8, 16, 32):
    lo = sum((Q(4*n, n*n+j*j) for j in range(1, n+1)), Q())
    hi = sum((Q(4*n, n*n+j*j) for j in range(n)), Q())
    assert hi - lo == Q(2, n)
    if n >= 8:
        assert 3 < lo < hi < 4

W = mul(L, R)
for _ in range(40):
    E = mul(E, W)
    (a, c), (b, d) = E
    lo, hi = endpoints(E)
    assert b*c - a*d == 1
    assert hi - lo == Q(1, b*d)
    assert lo*lo - 9*lo + 19 > 0
    assert hi*hi - 9*hi + 19 < 0

positions = {factorial(k) for k in range(1, 8)}
assert sum(i in positions for i in range(1, 1001)) == 6
for n in range(1, 7):
    assert Q(16, 15*16**factorial(n+1)) < Q(2, 16**factorial(n+1))
print('PASS')
```

## 9. Claim ledger and sources

| Claim | Status and boundary |
|---|---|
| Metric-aware geometric ratio has a rational enclosure algorithm | Disclosed by (G), (R), and the arc-length assumptions |
| Every L/R decision halts and the resulting intervals recover π | Disclosed, importing classical irrationality of π |
| A finite-state autonomous machine can emit the exact π word | Refuted, importing classical transcendence of π |
| The same broad algorithm shape forces hexadecimal parity cancellation | Refuted by (C) |
| Radians and turns may be interchanged in the BBP observer | Refuted by the exact eventually-constant mutation |
| Geometry plus the new observer proves the source-specific contrast (F) | UNVERIFIED; no bound supplied |
| The final new repository implementation satisfies every contract above | UNVERIFIED at the time this independent note was written |

Baseline references, pinned to the inspected commit:

- [SUCC source frontier](https://github.com/femboy2112/SUCC/blob/964768cd1fa5116f521625abfaaad8d8fab0f222/docs/PI_NORMALITY_FRONTIER.md): authenticated source, zero-seed distinction, prime/complement frontier, and existing seed/epoch countermodels.
- [Round III computation graph](https://github.com/femboy2112/SUCC/blob/964768cd1fa5116f521625abfaaad8d8fab0f222/research/2026-11-10/cursed_categorical_computation/round_iii_dedekind/COMPUTATION_GRAPH.md): right-action endpoint conventions and earlier BBP-based comparison oracle.
- [SUCC method](https://github.com/femboy2112/SUCC/blob/964768cd1fa5116f521625abfaaad8d8fab0f222/docs/METHOD.md): steelman/crucible/verdict and source-specific claim boundaries.

Primary mathematical sources checked during this audit:

- David H. Bailey, [An elementary, self-contained proof that π is transcendental](https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf), dated July 24, 2026. Contains explicit proofs of irrationality and transcendence used as classical dependencies here.
- David H. Bailey, [The BBP Algorithm for Pi](https://www.davidhbailey.com/dhbpapers/bbp-alg.pdf), September 17, 2006. Confirms the exact BBP expansion and the distinction between digit extraction and the normality question. The 2006 discussion is not used as a claim about the entire present-day literature.

The geometric quadrature, matrix mutations, sparse-digit countermodel argument, and precision-transfer inequality in this note are supplied with their own derivations. They do not depend on numerical agreement with a stored value of π.

## 10. Versioned implementation audit

This section was added after the production implementation became available. It updates the earlier implementation-conformance `UNVERIFIED` entry with the exact inspection and execution scope below. It does not change the normality or parity proof frontier.

### Artifact and version history

Audited file: `circle_line_observer.py` in the same directory as this note. The final audited bytes had SHA-256

```text
a7b02e06e5e53a7a9d66b0b2d6fd8b4b0a8529b1fdecdfb995a01bc5cb9239fa
```

The hash was checked before and after the final execution and remained unchanged. The adversarial audit did not edit production code, a checkout, or remote state. The implementation owner repaired the reported issues.

| Inspected version | Finding | Resolution observed |
|---|---|---|
| `acfdbc66221b126e836f6e7f4e87a8bacd6165347e2c98ee6e7dc958f6fab4f0` | Natural integer inputs to `point`, `tangent`, `arc_speed`, and `metric_jacobian` could produce Python floats | Coercion to `Fraction` at those four entrypoints; exact return types verified |
| Same initial version | An unknown `finite_run` source name silently selected the rotation source | Unknown names now raise `ValueError`; verified |
| `36f8a3e518916df6ae51353627d1b3c1d9436429f98a70b48a5cc7e53c530d83` | Imported `finite_run(0,600,'matrix')` failed under Python's permitted 640-digit integer-display cap, although CLI mode already worked | Final `rational_text` uses bounded integer chunks for oversized rational strings; imported calls and unchanged process settings verified |
| Final version above | No blocking mathematical or implementation defect found within the audit scope | Finite certificates and algebraic laws checked as recorded below |

The digit helper's exponent-zero character is the **units digit**, not the entire integer part in bases 2 or 3. Its `floor` field retains the whole scaled integer. The revised docstring states this; the hexadecimal-facing `finite_run` output is unaffected because its integer part is one hexadecimal digit.

### Primary source semantics: beta integrals

The primary source uses

$$
Z_k=\begin{pmatrix}k&4k+2\\0&2k+1\end{pmatrix},
\qquad Z_k(t)=2+\frac{k}{2k+1}t,
\qquad A_k=Z_1\cdots Z_k.
$$

Let

$$
W_0=1,\qquad W_n=\frac{2^n(n!)^2}{(2n+1)!},\qquad
\frac{W_n}{W_{n-1}}=\frac n{2n+1}.
$$

The beta integral identity is

$$
W_n=\int_0^1[2u(1-u)]^n\,du.
$$

Because `0≤2u(1-u)≤1/2`, uniform convergence of the geometric series justifies summation under the integral. The substitution `t=2u-1` and evenness give

$$
2\sum_{n\ge0}W_n
=2\int_0^1\frac{du}{1-2u(1-u)}
=4\int_0^1\frac{dt}{1+t^2}
=\pi_{\rm geom}.
$$

Each shifted normalized tail is

$$
T_k=2\sum_{j\ge0}\frac{W_{k+j}}{W_k}.
$$

Every successive ratio is less than `1/2` and at least `1/3`, with strict improvement over `1/3` eventually. Therefore `3<T_k<4`. Direct composition yields

$$
A_k(t)=2\sum_{j=0}^{k-1}W_j+W_kt,
$$

and hence the strict geometric enclosure

$$
A_k(3)<\pi_{\rm geom}<A_k(4),\qquad
A_k(4)-A_k(3)=W_k\le2^{-k}.
$$

The implementation's removal of a common integer matrix factor does not change its projective action. These equations justify its initial bounds, refinements, strict endpoint semantics, and effective convergence without a stored π value. They are the mathematical semantic certificate for the source, not a conclusion inferred from agreement of output digits.

### Independent source semantics: rational circle rotations

Exact circle multiplication gives

$$
P(1/2)=(3/5,4/5),\quad P(1/3)=(4/5,3/5),\quad
P(1/2)P(1/3)=(0,1).
$$

Both input arcs lie in the first quadrant, so their positively oriented sum is the quarter-circle arc, without an extra winding. Expanding `1/(1+t²)` on each of the shorter intervals `[0,1/2]` and `[0,1/3]` supplies alternating rational integral sums. The code adds the next positive term to form a strict upper bound, then subtracts the next negative term to form a strict lower bound. The index increment consumes two series terms per stage and is correct.

This is an independent arithmetic compilation of the same Euclidean ratio. It shares the Euclidean circle, arclength semantics, and classical irrationality dependency with the primary source. Agreement is valuable corroboration across implementations; it is not independence of all premises.

### Guards, totality, and the three matrix conventions

The comparison conditions `source.upper <= mediant` and `source.lower >= mediant` are sound because the source endpoints are **strict** bounds on the target. Equality between an endpoint certificate and the mediant is therefore a valid branch decision, not an undecidable equality to π. Both equality guard cases were executed with fixed strict-enclosure sources whose `refine()` would raise if called.

For the two implemented sources, shrinking strict rational enclosures and the irrationality theorem prove that each mediant comparison terminates. The same reasoning proves termination of each digit certificate: for a fixed base and exponent, the scaled target is irrational and therefore is a positive distance from the nearest integer boundary. The upper-floor test is conservative when the upper endpoint is an integer, but does not threaten termination.

The endpoint updates implement the right action exactly. The residual-chart convention additionally needs a letter swap:

$$
E=\begin{pmatrix}a&c\\b&d\end{pmatrix},\quad
G=E\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\begin{pmatrix}c&a\\d&b\end{pmatrix},\quad
G(t)=\frac{a+ct}{b+dt}.
$$

Thus `det(E)=-1`, `det(G)=+1`, and

$$
E\mapsto EL\quad\Longleftrightarrow\quad G\mapsto GR,
\qquad
E\mapsto ER\quad\Longleftrightarrow\quad G\mapsto GL.
$$

Production code keeps these conventions distinct. A proof diagram using residual charts must retain the swap.

The source generators `Z_k` are a third action. They are generally not L/R words: `det(Z_k)=k(2k+1)`, while every L/R word has determinant 1. Already `det(Z_1)=3` obstructs equality up to rational projective scaling, since such scaling changes determinant by a rational square. The implementation correctly joins source contraction and endpoint refinement through certified comparisons. Their common conic lift does not identify their generating monoids.

### Conic lift and metric transport

For parameter coordinates `(U,V)`, the conic coordinates are

$$
(X,Y,Z)=(V^2-U^2,\ 2UV,\ V^2+U^2).
$$

Substitution of `(U',V')=(aU+bV,cU+dV)` gives the implemented symmetric-square coefficients. In particular, for the lifted map `S(M)`,

$$
S(MN)=S(M)S(N),\qquad
X'^2+Y'^2-Z'^2=\det(M)^2(X^2+Y^2-Z^2).
$$

The code's metric Jacobian is the positive arclength ratio

$$
J_M(t)=\frac{|\det M|(1+t^2)}{(at+b)^2+(ct+d)^2}.
$$

It follows directly by multiplying the stereographic arclength density at `M(t)` by `|M'(t)|`, then dividing by the density at `t`. Its cocycle law is

$$
J_{MN}(t)=J_M(N(t))J_N(t)
$$

where the stated affine charts are defined. The routine intentionally rejects an affine chart pole or a singular matrix. The conic action provides the projective extension; the finite-chart Jacobian routine does not claim to evaluate an undefined affine parameter.

Preserving the conic does not make these maps Euclidean isometries. The nonconstant Jacobian is precisely the metric data that a geometry-to-computation bridge must retain.

### Actual final-version executions

Every run below executed against the final SHA-256 above. The final combined Python audit exited 0. It used `Fraction` for decision checks, imported production bytes without writing bytecode, captured subprocess output in memory, and made no output-file or remote mutation.

| Requested arrows | Requested fractional hexadecimal digits | Primary source final stage | Rotation source final stage | Agreement |
|---:|---:|---:|---:|---|
| 0 | 0 | 1 | 1 | Exact word and digits |
| 1 | 0 | 1 | 1 | Exact word and digits |
| 32 | 8 | 31 | 8 | Exact word and digits |
| 512 | 64 | 254 | 63 | Exact word and digits |
| 4096 | 128 | 1443 | 360 | Exact word and digits |

The large prefix audit independently rebuilt each source up to every claimed stage. It verified all 4,096 reported mediants, consumed-stage counts, guard inequalities, endpoint updates, and determinant identities, and all 129 digit certificates, **for each source**. It also checked the final width against `1/(bd)`.

Additional executed controls on the same version:

| Control | Exact executed scope | Result |
|---|---|---|
| Repaired geometry input types | Integer zero at four entrypoints | Exact `Fraction` values |
| Repaired source-name rejection | `finite_run(0,0,'typo')` | `ValueError` |
| Primary-source factorial certificate | Stages 1 through 256 | Exact affine formula, width, and nesting |
| Symmetric-square functoriality | 49 pairs from seven invertible integer/rational matrices | Exact equality |
| Metric cocycle | 322 valid chart combinations | Exact equality |
| Conic action versus rational parametrization | 47 finite-chart cases | Exact equality |
| Quadratic-form scaling off the conic | 14 cases | Exact determinant-squared law |
| Quarter-arc product | Parameters 1/2 and 1/3 | Exactly `(0,1)` |
| Equality branch guards | Upper equals mediant; lower equals mediant | Correct `L` and `R`, no refinement |
| Oversized signed rational text | Six cases, including zero, negative values and internal zero chunks | Matches uncapped `Fraction` text |
| Imported API display cap | Both sources, 600 fractional digits, cap 640 | Equal output; cap remains 640 |
| Infinite-stream finite consumer | First 64 lines from each source | Sequential certificates; closed pipe exits 0 with no stderr |
| Invalid CLI arguments | Negative steps, negative digits, unknown source, `--forever` plus output path | All exit 2 |
| CLI with inherited display cap | 600 fractional digits with `PYTHONINTMAXSTRDIGITS=640` | Exit 0 |
| Source inspection | AST numeric literal check and read-through | Zero floating-point literals; no numerical π, digit, trigonometric, BBP, file-read, or network source used by production computation |

The tested matrices were the identity, `L`, `R`, the coordinate swap, `diag(2,3)`, `[[1,2],[3,5]]`, and `[[1/2,-2/3],[3/5,7/4]]`. Parameter probes were `-3,-1,-1/2,0,1/3,1,5`, omitting only charts whose displayed denominator vanished. The off-conic vectors were `(1,2,3)` and `(3/7,-5/4,2)`.

The six serialization values were `0`, `1`, `-1`, `10^700+10^351+7`, `-(10^1000+10^500+9)`, and `(10^701+1)/(10^699+3)`. They test both signs, the integer/fraction distinction, and padding of internal decimal chunks. The imported API returns exact integer fields; a caller subsequently serializing those integer fields with an external JSON encoder remains responsible for that encoder's integer-display policy. The documented CLI sets that policy before serializing its own records.

### Implementation verdict and limits

**Observed:** the finite runs, guards, exact-source replays, algebraic controls, API repairs, and CLI behavior above passed on the recorded bytes.

**Disclosed by the given derivations:** the two specified source algorithms enclose geometric π; right-action refinement preserves its enclosure; every finite decision halts under the classical irrationality dependency; widths tend to zero. These arguments concern ideal unbounded integer/rational computation, not physical infinite storage or uninterrupted hardware operation.

**Scope:** the geometry class is a fixed, compiled semantic model with explicit operations and an accompanying mathematical derivation. It is not a parser that accepts arbitrary equation strings and discovers their meanings, and it is not a proof assistant checking the derivation internally. Changing a descriptive equation string would not automatically compile a different source algorithm.

**Still unproved:** a source-specific signed cancellation estimate or base-16 statistical law. The conic representation and exact decoder do not invalidate the countermodel in Section 5 or remove the expansion-precision issue in Section 6.
