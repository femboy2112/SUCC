# Round III: irrational numbers as certified rational computation graphs

**Status:** the interval, Pell, and observer statements proved below are `PROVED`; the attached executions are `VERIFIED_FINITE`. These constructions do not establish a radix-frequency theorem for either pi or sqrt(2), any all-epoch BBP signed cancellation estimate, or decidability of arbitrary real equality.

**Scope and provenance.** This is an additive research note. It retains the literal four-pole source and original-zero recurrence. It does not alter frozen imports, source contracts, or historical dossiers. The local preparation directory was an exported source directory with AGENTS.md, not a Git checkout; publication provenance belongs to the containing research round. No claim of a repository-wide test run or Lean verification is made here.

The source convention was checked against [Main XXII's pinned frontier](https://github.com/femboy2112/SUCC/blob/43886e830cee5ff6d6b37719e18d809819673bd9/docs/PI_NORMALITY_FRONTIER.md), section 1, which explicitly states `U_n+T_n=16^(n-1)pi`. The governing [steelman–crucible–verdict method](https://github.com/femboy2112/SUCC/blob/43886e830cee5ff6d6b37719e18d809819673bd9/docs/METHOD.md) was read from that checkout. The bounds below are independently derived elementary tools; no priority or novelty claim is made.

## 1. The object is a labelled refinement graph

Let `RatInt` have closed rational intervals of positive width as objects and one arrow

$$
I\longrightarrow J\quad\Longleftrightarrow\quad J\subseteq I.
$$

A nested sequence of bounded intervals with widths tending to zero is a functor from the ordered category of natural numbers into `RatInt`. Its unique real intersection follows from completeness of the real line. An irrational singleton is not already a rational-endpoint object of `RatInt`: the limiting interpretation is a completion, not a finite terminal computation.

The essential structure is the **interval-label functor**. The bare index category of every such sequence is just the same ordered category of natural numbers. Forgetting labels makes presentations of sqrt(2), pi, and a rational constant indistinguishable at this level.

This yields a useful compiler contract. A node contains a rational interval and a sound inclusion certificate. An edge refines the interval. Arithmetic nodes propagate intervals: addition adds endpoints; multiplication takes the minimum and maximum of the four endpoint products; reciprocal requires a certified exclusion of zero. A branch node returns a discrete decision only when the entire interval lies in one branch. A limit node is semantic data supported by a convergence theorem, not an instruction claiming that infinitely many steps have elapsed.

## 2. A two-register integer machine for sqrt(2)

Define, for every integer k at least one,

$$
(p_1,q_1)=(1,1),\qquad
p_{k+1}=p_k+2q_k,\qquad q_{k+1}=p_k+q_k.
$$

### CG-01: exact Pell interval theorem — PROVED

The recurrence gives

$$
p_k+q_k\sqrt2=(1+\sqrt2)^k,
\qquad p_k^2-2q_k^2=(-1)^k.
$$

Define

$$
J_k=\left[
\min\left(\frac{p_k}{q_k},\frac{2q_k}{p_k}\right),
\max\left(\frac{p_k}{q_k},\frac{2q_k}{p_k}\right)
\right].
$$

Its endpoints lie strictly on opposite sides of sqrt(2), and

$$
|J_k|=\frac{1}{p_kq_k}\le 4^{1-k}.
$$

The first equality follows directly from the Pell identity. Since p_k is at least q_k and q_(k+1) is at least 2q_k, the inequality follows by induction. The intervals are strictly nested. For a direct verification, put r=p_k/q_k. The new ratio is `(r+2)/(r+1)`; subtracting either old endpoint and clearing positive denominators proves that this ratio and its reciprocal partner lie strictly between the old endpoints. Thus J_k is an integer-only refinement graph with an explicit error modulus.

The same ratios are the successive convergents of the continued fraction `[1;2,2,2,...]`. This follows from the standard convergent recurrence, with the index shifted by one. The general recurrence and its determinant identities are recorded in [DLMF §1.12](https://dlmf.nist.gov/1.12). No theorem about ordinary radix digit frequencies is inferred from the repeated continued-fraction instruction.

### CG-02: an explicit safe hexadecimal-floor schedule — PROVED

For j at least zero set B=16^j. Every nearest integer m to B sqrt(2) lies between zero and 2B. Since `2B^2` is not a square,

$$
|B\sqrt2-m|
=\frac{|2B^2-m^2|}{B\sqrt2+m}
>\frac{1}{4B}.
$$

At Pell depth `k=4j+3`, the interval BJ_k has width at most `1/(16B)`. It therefore cannot cross an integer while containing B sqrt(2). Both endpoint floors agree, giving a finite rational certificate for

$$
\lfloor16^j\sqrt2\rfloor.
$$

Taking this integer modulo 16 gives the hexadecimal digit at radix exponent j; j=0 denotes the units digit. This schedule is intentionally conservative. The proof supplies a uniform margin because the target satisfies a fixed quadratic equation. The implementation independently checks each reported floor m by the exact integer inequalities

$$
m^2<2\,16^{2j}<(m+1)^2.
$$

## 3. Stern–Brocot paths: unimodular instructions with rational labels

Take positive-denominator endpoints a/b<c/d satisfying `bc-ad=1`. Their mediant is `(a+c)/(b+d)` and their interval width is exactly `1/(bd)`. Choosing the left or right child updates the endpoint matrix by right multiplication with, respectively,

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

Both update matrices lie in SL(2,Z); the endpoint matrix itself has determinant -1 with the column convention used here. Every refinement preserves the unimodular identity. These claims follow by matrix multiplication and subtraction of the endpoint fractions.

For sqrt(2), compare a positive mediant m/n with the target by comparing `m^2` with `2n^2`. For pi, use the BBP interval oracle in the next section and refine until the mediant is excluded. A fixed rational comparison eventually resolves because pi is irrational and the enclosure widths tend to zero. This is an adaptive algorithm, not a uniform bounded-lookahead claim for arbitrary real inputs.

The probe produces 128-step paths from `[1,2]` for sqrt(2) and `[3,4]` for pi. Each checks the exact determinant and endpoint gap. The pi path is generated from BBP intervals and checked against an independently constructed Machin interval. A run of 128 letters is finite evidence; it cannot establish eventual periodicity, its absence, or a radix-frequency law.

## 4. The authentic BBP graph has a simple rational error certificate

For n at least one retain

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}
-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Define

$$
\pi_N=\sum_{n=1}^N16^{1-n}r(n).
$$

The classical BBP identity gives `pi_N -> pi`; the shifted normalization matches [Bailey's author-hosted description of the BBP formula](https://www.davidhbailey.com/dhbpapers/bbp-alg.pdf). In this convention

$$
U_N=16^{N-1}\pi_N\quad(N\ge1).
$$

In particular, summing `16^(-n)r(n)` instead gives pi/16. Losing this factor changes the selected constant.

### CG-03: exact BBP tail and phase-completion bounds — PROVED

Let

$$
Q(t)=t^4+2t^3+4t^2+4t+4.
$$

Direct integration and polynomial multiplication give

$$
r(n)=\int_0^1t^{8n-8}(1-t)Q(t)\,dt,
\qquad 4\le Q(t)\le15\quad(0\le t\le1).
$$

Consequently the source is positive, and for every N at least zero,

$$
\begin{aligned}
\pi-\pi_N
&=16^{-N}\int_0^1
\frac{t^{8N}(1-t)Q(t)}{1-t^8/16}\,dt\\
&<16^{1-N}\int_0^1t^{8N}(1-t)\,dt\\
&=\frac{16^{1-N}}{(8N+1)(8N+2)}.
\end{aligned}
$$

The lower bound is strictly positive. The inequality is strict because the dominating factors are strict on the interval interior. Interchanging sum and integral is justified by nonnegative terms, or by the uniform geometric bound.

Thus the graph node

$$
I_N=\left[\pi_N,\,
\pi_N+\frac{16^{1-N}}{(8N+1)(8N+2)}\right]
$$

is a rational enclosure. These intervals are strictly nested: lower endpoints increase, while the source bound

$$
r(N+1)<\frac{15}{(8N+1)(8N+2)}
$$

shows that the increase in lower endpoint is smaller than the decrease in the allowed tail budget. Explicitly, writing `D_N=(8N+1)(8N+2)`, the upper-endpoint decrease exceeds `16^(-N)(1/D_N-1/D_(N+1))>0`.

For the authenticated source clock this yields the useful certificate

$$
\boxed{0<16^{N-1}\pi-U_N<\frac1{(8N+1)(8N+2)}}
\qquad(N\ge1).
$$

This is an enclosure theorem, not a statement that the small error cannot cross a digit boundary. For any fixed radix exponent j, use `16^j I_N` and refine N until its endpoint floors agree.

## 5. Nonlinear observers must carry their own contracts

### CG-04: floor and fractional part — PROVED

For x in a certified closed interval `[a,b]`, agreement of `floor(a)` and `floor(b)` certifies `floor(x)`. Otherwise this sufficient test returns **unresolved**. If it certifies m, then the fractional part lies in `[a-m,b-m]`.

At a crossing such as `[255/256,257/256]`, returning the lower endpoint's floor is unsound. The two rational endpoints already have different floors. Shrinking intervals around the exact integer one remain ambiguous for this interval-only test at every finite depth.

This is a real discontinuity, not a numerical inconvenience. It does not forbid symbolic handling of a known exact rational, or termination on a promised irrational input. It forbids a general total floor operation computed from arbitrary real approximation names without an appropriate domain restriction. [Brattka, *Realistic models of computability on the real numbers*](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1169-5.pdf), Theorem 2.5 and Proposition 2.6, supplies the standard computable-analysis context.

### CG-05: characters remain certifiable through the cut — PROVED

For integer h and real x,y,

$$
|e^{2\pi ihx}-e^{2\pi ihy}|\le2\pi|h|\,|x-y|.
$$

In particular, CG-03 gives a source-completion error at most

$$
\frac{44|h|}{7(8N+1)(8N+2)}
$$

using `pi<22/7`. A character is continuous on the circle even where the chosen real-valued fractional-part coordinate jumps. The implementation reduces a **rational midpoint** modulo one, retaining a separate error radius for the true input. It never claims the true input's floor has been decided.

For a rational angle center c, it evaluates finite sine and cosine Taylor sums. With `terms=t`, the respective remainder bounds are

$$
\frac{|c|^{2t+1}}{(2t+1)!},\qquad
\frac{|c|^{2t}}{(2t)!}.
$$

These follow by including the next zero Taylor coefficient and applying the ordinary derivative bound. An interval radius in the angle adds the same radius to either error, since sine and cosine are 1-Lipschitz. Rational inputs and pi enclosures are rounded outward to a dyadic grid before evaluation; this controls denominator growth without losing enclosure validity. All acceptance comparisons remain exact rational comparisons.

The general arithmetic-function background is [DLMF §4.24](https://dlmf.nist.gov/4.24) and [§4.45](https://dlmf.nist.gov/4.45). These references are background, not a substitute for the remainder bounds just given.

The h=8 certificate here concerns the real-circle character `exp(2*pi*i*8x)`. It is not the step-function parity of the leading hexadecimal digit. The pinned frontier makes that distinction explicit; a digit-parity certificate must first resolve the appropriate digit boundaries.

## 6. Independent computation and hostile controls

The second pi implementation uses

$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$

and the alternating rational arctangent series, enclosed between a partial sum and that sum plus its next term. A short identity proof is available: the tangent of `4 arctan(1/5)` is `120/119`; subtracting `arctan(1/239)` gives tangent one, in the interval `(0,pi/2)`. This identifies the angle as pi/4. The arctangent series is [DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3).

Run:

```sh
python computation_probe.py --output computation_receipt.json
```

The saved receipt binds the executed script's SHA-256. On Python 3.12.14 it records:

- 200 exact source-versus-integral identities and positive source bounds;
- 270 source-recurrence normalizations and strict BBP interval refinements;
- 11 BBP tail enclosures containing the independent Machin enclosure, including N=256;
- 36 pi digit certificates: exponents 0 through 32, then 63, 127, and 255, all agreeing with the independent implementation;
- 200 exact Pell identities, widths, and strict refinements;
- 35 sqrt(2) digit certificates, each independently verified by integer squares;
- two 128-step Stern–Brocot paths with 129 unimodularity checks each;
- 15 character rectangles at clocks 1, 2, 7, 23, and 64, for h=1,8,32, checked against independent Machin input intervals;
- rejection of a missing factor 16 in the tail and an off-by-one source-clock normalization;
- abstention on 64 shrinking intervals around the floor discontinuity;
- a quarter-circle sign control and a character enclosure across a floor cut.

The two character calculations share their Taylor evaluator; they are not independent implementations of trigonometry. Its rational remainder proof and exact quarter-circle controls supply separate calibration. These are same-model derivations and implementations, not external refereeing. The finite receipt is subordinate to the universal proofs in this note.

### Known-result recovery: a source-specific mixed prime defect

The graph also recovers a previously established finite arithmetic witness,
rather than merely agreeing with a generic decimal oracle. In the pinned
[prime-defect dossier](https://github.com/femboy2112/SUCC/blob/75dc9f9a230c5c71b3f580c5ac2f17780ba1d560/research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/DIRICHLET_PRIME_DEFECT.md),
put Y_n=16^(n-1)pi and a_n=exp(2*pi*i*Y_n). Using I_12 above, exact rational
scaling and floor checks certify

| Phase | Strict fractional cell |
|---|---|
| Y_1 | (1/8,1/6) |
| Y_2 and Y_3 | (1/6,1/3) |
| Y_6 | (1/2,1) |
| Y_2-Y_1 | (1/10,1/8) |
| Y_6-Y_3 | (2/5,5/12) |
| Y_3-Y_1 | (1/10,1/9) |
| Y_6-Y_2 | (3/8,2/5) |

The implementation checks eight individual cells, because the second row
contains two values. All interval endpoint floors agree before reduction.
Elementary sine bounds then give sin(2*pi*Y_2)>sqrt(3)/2 and the same bound
for Y_3, while sin(2*pi*Y_6)<0 and sin(2*pi*Y_1)<=1. Therefore

$$
\operatorname{Im}(a_6-a_3-a_2+a_1)<1-\sqrt3<0.
$$

This is the nonzero two-prime interaction from Round II, now recovered by the
new certified cut graph. It rejects an additive single-prime-coordinate model
on this complete four-cell contrast. The coherent wrong seed u=-pi/16 makes
all completed Y_n(u)=16^n(u+pi/16) zero and makes the defect zero, so source/seed
binding is visibly consequential. This is a finite known-result recovery,
not a new proof of an all-epoch sign or normality statement.

## 7. What the graph cannot identify

### CG-06: finite-prefix identification fails — PROVED / countermodels

Any finite Stern–Brocot prefix leaves a rational interval with nonempty interior. It contains infinitely many distinct rational and irrational numbers. The prefix identifies that interval, not one exact real. Likewise, the bare category of any single infinite refinement chain is the same natural-number order. The rational labels and the limiting semantics cannot be discarded.

There are countably many finite programs, so only countably many reals have algorithmic names of the specified kind. A countable binary graph can still have uncountably many infinite paths; this does not turn every path into a computable one. The graph, the chosen infinite path, and an effective rule generating that path are different data.

Finally, arbitrary computable-real equality is undecidable. Given a machine, let x be `2^(-t)` if it halts at step t at least one, and zero if it never halts. Simulating N steps gives a rational approximation of x with error at most `2^(-N)`, uniformly in the machine. A general test `x=0` would decide nonhalting. Likewise `floor(1-x)` distinguishes the same alternatives. This is a concrete obstruction to a general-purpose exact branch oracle.

## 8. Verdict and next discriminator

**Earned result:** the proposed irrational computation graphs have precise integer/rational realizations; sqrt(2) admits an explicit uniform digit-margin theorem, and the authentic BBP graph admits exact tail, floor, and Fourier-character certificates. This makes the representation operational and calibrates the branch boundary.

**Remaining arithmetic debt:** none of these constructions controls the signed statistics of infinitely many authenticated BBP clocks. A small per-clock representation error does not imply that the accurately represented phases cancel.

**Next probe:** attach these certified observers to an independently specified arithmetic pairing or signed-overlap rule. Require the rule to act on original-zero clock indices, reject coherent wrong seeds, and expose both its unmatched boundary mass and phase mismatch. Passing a finite comparison would remain finite evidence; an all-epoch bound requires a new theorem.
