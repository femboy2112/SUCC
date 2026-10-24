# BBP Fourier transport, rational shift obstructions, and counterfeit dynamics

Research date: 2026-10-21. Base: PR #232 at
`9894d39250021bbbc2615c33dee0d286ddf0950f`.
This independent analytic lane owns only its module, tests, probe, and dossier.
The proofs below are paper proofs, **not Lean kernel receipts**. Exact tests are
finite cross-checks; they do not authenticate an infinite theorem.

## 1. Target and earned result

The missing theorem is: for every nonzero integer `h`,

\[
 N^{-1}\sum_{n=1}^N\exp(2\pi i h16^{n-1}\pi)\longrightarrow0. \tag{OPEN}
\]

By Weyl's criterion and the radix-orbit characterization of normality, this is
equivalent to base-16 normality of pi. It is not proved here. Its transfer to a
BBP forced orbit is an equivalent formulation, not newly obtained cancellation.

The actual advances are a substantially sharper, asymptotically sharp shadow
error; explicit Fourier, Wasserstein and arc-discrepancy transport; a complete
rational-pole obstruction to telescoping the **actual** BBP forcing; and exact
counterfeit families that defeat decay-only and finite-prefix reasoning.

| Local identifier | Statement | Repository status | Boundary |
|---|---|---|---|
| DA-TAIL | Positive decomposition, sharp leading shadow coefficient `1/64` | PROVED LOCAL, paper | Uses classical BBP identity only to identify pi |
| DA-TRANSPORT | Fourier-sum difference at most `abs(h)/5`, moving-window budget; arc discrepancy difference `O(N^(-2/3))` | PROVED LOCAL, paper | Neither individual Fourier sum is bounded sublinearly |
| DA-RESIDUE | Weighted pole invariants decide rational shift-coboundaries on the specified class; actual BBP fails | PROVED LOCAL, paper; classical mechanism | No implication from non-coboundary to normality |
| DA-FAKE | Positive leading-matched fake; arbitrary exact finite-prefix fake | PROVED LOCAL, paper | Prefix fake need not be positive; both have rational shadows |
| DA-APPROX | Every weighted neighborhood of the actual BBP forcing contains positive rational-shadow counterfeits with the same leading term | PROVED LOCAL, paper | Does not assert discontinuity of normality at an unproved-normal source |
| DA-DEGREE | A rational correction of degree at most `d` must fail one of `2d+5` exact probes | PROVED LOCAL, paper; executable | Requires nonsingular presentations at all declared probes |
| DA-MU | Irrationality exponent 2 alone does not imply base-16 normality | CLASSICAL input plus elementary corollary | Imported Bugeaud theorem, not an assertion about pi |
| DA-VD | Van der Corput correlations return the same source-specific family | PROVED LOCAL identity | A reduction requiring an unproved cancellation seed |
| DA-OPEN | Source-specific cancellation / uniform no-hotspot estimate | HYPOTHESIS / UNVERIFIED | Base-16 normality remains open in this work |

These are local dossier labels, not additions to the central claim namespace.
No mathematical originality is asserted. The coordinator owns status promotion
and central registration after independent review.

## 2. Source definitions and indexing

Write `e(t)=exp(2*pi*i*t)` and use circle distance
`d(u,v)=inf_{j in Z}|u-v-j|` on `R/Z`. For integers `m>=1`, put

\[
r(m)=\frac4{8m-7}-\frac2{8m-4}-\frac1{8m-3}-\frac1{8m-2}.
\]

Define `x_0=0`, `x_n={16x_(n-1)+r(n)}` for `n>=1`. The classical BBP identity,
as used in Bailey--Crandall [BC01], says

\[
\pi=\sum_{m\ge1}16^{1-m}r(m).
\]

Consequently, for `n>=1`,

\[
 T_n=\sum_{k\ge1}16^{-k}r(n+k),\qquad
 y_n=\{16^{n-1}\pi\}=\{x_n+T_n\}. \tag{1}
\]

Indeed, unfolding the recurrence gives
`x_n={sum_(m=1)^n 16^(n-m)r(m)}`; multiplying the BBP identity by
`16^(n-1)` gives precisely that finite sum plus `T_n`. The exponent is `n-1`,
not `n`. An exact rational truncated-source test rejects the shifted exponent.
The abstract transport below works for any two circle sequences with its stated
distance bound, independently of any name attached to their source.

## 3. A stronger source-specific tail theorem

**Theorem DA-TAIL.** For every integer `m>=1`,

\[
r(m)=\frac6{(8m-7)(8m-4)}+
      \frac4{(8m-7)(8m-3)}+
      \frac5{(8m-7)(8m-2)}. \tag{2}
\]

Thus `r(m)>0`, it is strictly decreasing on the positive integers, and
`r(m)<=15/(8m-7)^2`. For every integer `n>=1`,

\[
 0<T_n\le\frac{r(n+1)}{15}\le\frac1{(8n+1)^2},\qquad
 \lim_{n\to\infty} n^2T_n=\frac1{64}. \tag{3}
\]

After retaining the first `K>=0` tail terms, the remaining tail is bounded by

\[
 0\le T_n-\sum_{k=1}^{K}16^{-k}r(n+k)
 \le16^{-K}\frac{r(n+K+1)}{15}. \tag{4}
\]

**Proof.** Split the first term of `r` into `2+1+1` copies of
`1/(8m-7)` and pair each with one negative term. The three numerator differences
are `6,4,5`, proving (2). Every denominator factor is positive and increasing.
Monotonicity bounds each `r(n+k)` by `r(n+1)`; summing the geometric series
`sum_(k>=1)16^(-k)=1/15` proves (3)'s upper bounds. Reindex the remainder to
obtain (4).

For the limit, each fixed `k` has `n^2r(n+k)->15/64`. Also
`n^2r(n+k)<=15/64` because `8(n+k)-7>=8n+1`. For any fixed `K`, the finite
sum converges termwise; the omitted part after multiplication by `n^2` is at
most `16^(-K)/64`, uniformly in `n`. First take `n->infinity`, then
`K->infinity`. This proves the asserted limit without an unproved limit
interchange. The leading coefficient `1/64` cannot be decreased in an
eventually valid bound of the form `C/n^2`. QED.

This improves the previous `8/[15(n+1)^2]` enclosure. It does not measure how
uniformly either orbit occupies the circle.

## 4. Explicit transport theorems

For integers `M>=1` and `N>=0`, define

\[
 J_{M,N}=\frac18\left(\frac1{8M-3}-\frac1{8(M+N)-3}\right).
\]

The elementary inequality

\[
\frac1{(8n+1)^2}\le\frac1{(8n-3)(8n+5)}
=\frac18\left(\frac1{8n-3}-\frac1{8n+5}\right)
\]

holds for `n>=1` and telescopes. Therefore

\[
 \sum_{n=M}^{M+N-1}d(x_n,y_n)\le J_{M,N}\le\frac1{40}. \tag{5}
\]

**Fourier transport.** For every integer `h`,

\[
\left|\sum_{n=M}^{M+N-1}e(hx_n)-\sum_{n=M}^{M+N-1}e(hy_n)\right|
\le\min(2N,2\pi|h|J_{M,N})
\le\min(2N,8|h|J_{M,N})\le\frac{|h|}{5}. \tag{6}
\]

Proof: choose the closest lifts for each pair on the circle and use the
derivative bound `|e(hu)-e(hv)|<=2*pi*abs(h)*d(u,v)`, then triangle inequality.
The rational implementation uses the safe classical inequality `pi<4`.
No value of the exponential function is numerically certified by that code.

For `N>=1`, the normalized Fourier difference is at most `|h|/(5N)`, uniformly
over moving windows `M>=1`. Hence transfer remains `o(1)` for `|h|=o(N)`.
For fixed `h`, a proved bound `O_h(N^(1-delta))`, `0<delta<=1`, for either
unnormalized sum transfers to the other. This theorem supplies no such seed.
For a frequency family `|h|<=H(N)`, the transfer budget is `H(N)/(5N)`;
the small-frequency condition must not silently be dropped.

**Wasserstein transport.** Couple the two empirical measures by matching
equal indices. With circle distance as transport cost, for `N>=1`,

\[
 W_1\left(N^{-1}\sum_{n=1}^N\delta_{x_n},
          N^{-1}\sum_{n=1}^N\delta_{y_n}\right)
 \le J_{1,N}/N\le1/(40N). \tag{7}
\]

**Arc discrepancy transport.** Let `D_N^arc(z)` be the supremum of
`|N^(-1) #{1<=n<=N:z_n in I}-length(I)|` over all oriented half-open circle
arcs `I`, including wrap-around arcs. For `N>=1` and every integer `0<=K<=N`,

\[
 |D_N^{arc}(x)-D_N^{arc}(y)|
 \le\min\left(1,\frac K N+\frac{2r(K+2)}{15}\right)
 \le\min\left(1,\frac K N+\frac2{(8K+9)^2}\right). \tag{8}
\]

Proof: remove the first `K` paired points, costing at most `K/N` in an
interval count. Every remaining pair has distance at most
`delta=r(K+2)/15`, by (3) and monotonicity. Enlarge a given arc at both ends
by `delta+epsilon`. Its length grows by at most `2(delta+epsilon)`; if it
becomes the entire circle the bound is immediate. Compare counts, then let
`epsilon` decrease to zero. This avoids half-open endpoint mistakes. The same
comparison with complements controls negative discrepancy; reversing the two
sequences gives the absolute difference. If `K=N`, the bound is trivial.

Choose `K=floor(N^(1/3))`, which lies in `[0,N]`. Then `K/N<=N^(-2/3)` and
`8K+9>=8N^(1/3)+1`, so

\[
 |D_N^{arc}(x)-D_N^{arc}(y)|\le\frac{33}{32}N^{-2/3}. \tag{9}
\]

The code minimizes the sharper rational expression in (8) over all integer
`K`, rather than evaluating a floating-point cube root. A test against an
independently computed exact empirical arc discrepancy checks finite cases.
Two equal constant sequences have zero transport error and discrepancy one:
transport is never itself equidistribution.

## 5. A complete rational shift obstruction

Let `b>=2` be an integer. Work first with proper rational functions over `Q`
whose complete finite partial fraction lists have rational poles. For each
pole residue class `a+Z`, choose `0<=a<1`. For each order `k>=1`, let `r_j`
denote the coefficient of `(z-(a+j))^(-k)` in `r(z)`, zero when absent. Put

\[
 I_{a,k}(r)=\sum_{j\in\mathbb Z}b^{-j}r_j. \tag{10}
\]

**Theorem DA-RESIDUE.** There is a proper rational `q` in this class with
`r(z)=bq(z-1)-q(z)` if and only if every invariant (10) is zero. Such `q` is
unique and is constructible by finite rational arithmetic.

**Proof.** Coefficient comparison gives `r_j=bq_(j-1)-q_j`. Weighted summation
telescopes to zero, since all supports are finite. Conversely, in a nonempty
orbit/order group with minimum support `m` and maximum support `M`, set
`q_(m-1)=0` and recursively `q_j=bq_(j-1)-r_j` for `m<=j<=M`. Then
`q_M=-b^M sum_(j=m)^M b^(-j)r_j=0`. Take all coefficients outside this
interval to be zero. The recurrence now holds everywhere, so reconstruction
gives the desired finite partial fraction expansion. The zero input returns
zero. Any nonzero finite homogeneous coefficient chain would have a leftmost
nonzero coefficient contradicting the recurrence. This proves uniqueness. QED.

For **any** rational `q` over `C` solving a proper rational forcing with only
rational poles, a polynomial part is impossible: its highest coefficient in
`bq(z-1)-q(z)` is multiplied by `b-1`. An orbit of nonrational poles is also
impossible, since its extremal finite chain produces an uncanceled pole absent
from `r`. Thus the obstruction also excludes a rational solution with hidden
nonrational poles or a polynomial part.

The actual BBP partial fractions are

| Pole `a` | Order | Residue / invariant at `b=16` |
|---|---:|---:|
| `7/8` | 1 | `1/2` |
| `1/2` | 1 | `-1/4` |
| `3/8` | 1 | `-1/8` |
| `1/4` | 1 | `-1/8` |

All four poles lie in distinct classes modulo integer translation. Therefore
there is **no rational function** `q` with `r(z)=16q(z-1)-q(z)`.
This rules out one explicit rational-telescoping simplification of the actual
source. It does not rule out nonrational corrections, other analytic
representations, exceptional orbits, or nonnormality.

The exact solver accepts a **complete supplied** partial fraction list. It
does not discover missing poles or authenticate that a list describes some
external source. Returned solutions are checked by direct partial-fraction
replay. Tests cover negative and positive pole shifts, multiple orders,
several bases, an unweighted-residue mutant, and a tiny exact nonzero mutant.
Shift summability and discrete residues are classical symbolic-summation
machinery [AS25]; this weighted finite proof and its BBP application are
new-to-project, with no originality claim.

## 6. Counterfeit dynamics with exact receipts

### 6.1 Positive and leading-asymptotic matched

Let `q(n)=1/[64(n+1)^2]` and

\[
 r_*(n)=16q(n-1)-q(n)=\frac1{64}\left(\frac{16}{n^2}-\frac1{(n+1)^2}\right).
\]

For every positive integer `n`, this is a positive rational function, and
`n^2r_*(n)->15/64`, the same limit as the actual BBP forcing. Its orbit from
zero is exactly

\[
 x_n^*=\{16^n/64-1/[64(n+1)^2]\}.
\]

This follows by telescoping, or induction on the forced recurrence. For
`n>=2`, `16^n/64` is integral, so `x_n^*=1-1/[64(n+1)^2]` and the orbit
converges to zero on the circle. It is not equidistributed. Even the shadow
error has the same asymptotic coefficient `1/64` as DA-TAIL.

**REFUTED:** positivity, proper rational forcing, decay of order `n^-2`, and
these leading coefficients together imply equidistribution. This example has
a rational shadow, so it does not refute a statement explicitly assuming an
irrational shadow, and does not refute Bailey--Crandall's finite-attractor/
equidistribution dichotomy. Its weighted pole invariants vanish, so the actual
BBP invariant genuinely discriminates it.

### 6.2 Any finite forcing prefix can be matched

**Theorem DA-FAKE.** For every integer `L>=0`, integer `b>=2`, rational
samples `a_1,...,a_L`, and rational `q_0`, there is a rational function
`q(n)=P(n)/(n+1)^(L+2)`, with `deg P<=L`, such that
`r_L(n)=bq(n-1)-q(n)` matches all `L` samples and is `O(n^-2)` on positive
integers. The orbit from zero has the same first `L` states as the sampled
forcing and is asymptotic on the circle to the rational radix orbit
`{b^n q_0}`. It is not equidistributed.

**Proof.** Set `q_j=bq_(j-1)-a_j` successively. Interpolate a degree at most
`L` polynomial through `P(j)=q_j(j+1)^(L+2)`, `0<=j<=L`. All data and
coefficients are rational. The formula is nonsingular for `n>=0`, has the
specified values, and is `O(n^-2)`. Its shifted forcing has the same decay
and matches every sample. Telescoping gives
`x_n={b^n q_0-q(n)}`. The rational orbit `{b^n q_0}` is eventually periodic:
its numerator residues modulo a fixed denominator form a finite deterministic
orbit. Since `q(n)->0`, choose an arc a positive distance from this finite
attractor; eventually it is never visited, contradicting equidistribution.
For `q_0=0`, the orbit simply converges to zero on the circle. QED.

The exact implementation uses Newton forward differences for interpolation.
Tests fit BBP prefixes through length 12, then check the telescoping identity
beyond the fitting region. There is no positivity promise for this family.
The assertion quantified over **all** finite prefixes is proved above; the
finite computations do not prove that quantifier.

**REFUTED:** any inference of global normality solely from finitely many exact
forcing/state matches plus rational `O(n^-2)` forcing. This does not impersonate
the full BBP rational function: its global pole invariant exposes the fake.

### 6.3 Counterfeits uniformly approximate the actual source

The pole obstruction cannot yield a positive approximation-residual gap in a
natural weighted norm without further restrictions. The following construction
uses the actual BBP rational function, rather than a separate toy source.

For a sequence `f` on the positive integers define
`||f||_(2,infinity)=sup_(n>=1) n^2|f(n)|`. For every integer `K>=1`, put

\[
 Q_K(n)=\frac{\sum_{k=1}^K16^{K-k}r(n+k)}{16^K-1}\quad(n\ge0),
 \qquad
 \widetilde r_K(n)=\frac{16^K r(n)-r(n+K)}{16^K-1}\quad(n\ge1). \tag{13}
\]

**Theorem DA-APPROX.** Every `Q_K` and `rtilde_K` is rational, and

\[
 \widetilde r_K(n)=16Q_K(n-1)-Q_K(n)>r(n)>0,
 \qquad
 \lim_{n\to\infty}n^2\widetilde r_K(n)=15/64. \tag{14}
\]

Moreover,

\[
 0<\widetilde r_K(n)-r(n)
 \le\frac{47}{15(16^K-1)n^2},\qquad
 \|\widetilde r_K-r\|_{2,\infty}
 \le\frac{47}{15(16^K-1)}\longrightarrow0. \tag{15}
\]

For each fixed `K`, the forced orbit from zero is

\[
 \widetilde x_{K,n}=\{16^nQ_K(0)-Q_K(n)\}; \tag{16}
\]

it has a rational shadow and is not equidistributed. Nevertheless, for every
fixed finite `N`, these orbits approach the actual forced orbit uniformly on
`0<=n<=N` as `K->infinity`. Thus every open weighted-norm neighborhood of
the actual BBP forcing contains such positive counterfeits with the identical
leading `n^-2` term.

**Proof.** Multiplying the sum for `Q_K(n-1)` by 16 and subtracting `Q_K(n)`
telescopes: only `16^K r(n)` and `-r(n+K)` remain. Since `r` is positive and
strictly decreasing, subtracting `r(n)` from (13) gives the positive expression

\[
 \widetilde r_K(n)-r(n)=\frac{r(n)-r(n+K)}{16^K-1}. \tag{17}
\]

For each positive term in (2), multiplication by `n^2` produces a product
`[n/(8n-a)][n/(8n-b)]` times a positive constant, where `0<a,b<8`. Each
factor decreases for real `n>=1`, since it equals `1/(8-a/n)`. Hence
`n^2r(n)<=r(1)=47/15`. This proves (15). Its uniform constant `47/15` cannot
be improved uniformly over `K`: at `n=1`, multiplying (17) by `16^K-1`
gives `r(1)-r(K+1)->47/15`. For fixed `K`, both `n^2r(n)` and
`n^2r(n+K)` tend to `15/64`, proving (14)'s leading coefficient.

Telescoping the forced recurrence proves (16). `Q_K(0)` is rational and
`Q_K(n)->0`; the finite-attractor argument in section 6.2 proves
nonequidistribution for every fixed `K`.

For the finite-window comparison, lift both recurrences before reducing
modulo one. Their difference is
`sum_(m=1)^n 16^(n-m)[rtilde_K(m)-r(m)]`, so for all `n>=0`,

\[
 d(\widetilde x_{K,n},x_n)
 \le\min\left(\frac12,
       \frac{47(16^n-1)}{225(16^K-1)}\right). \tag{18}
\]

Here (15) and `m^-2<=1` reduce the sum to a geometric series. This tends to
zero for every fixed finite window. The growing factor `16^n` is explicit;
no statement uniform in all orbit times is being smuggled in. QED.

**What fails quantitatively.** Each `rtilde_K` has zero weighted invariants,
whereas the actual `r` has the four nonzero values in section 5. Thus this
pole functional is discontinuous in the weighted norm on these rational
functions sampled at positive integers. This does **not** assert discontinuity
of normality at the actual source, because its normality has not been proved.
It proves that a small forcing residual, positivity, a leading asymptotic,
and arbitrarily long finite-window agreement do not exclude a rational shadow.

The construction makes the lost complexity visible. `Q_K` has `4K` distinct
simple poles `a-k`, for the four BBP poles `a` and `1<=k<=K`; the pole range
escapes to the left and the coefficient denominators involve `16^K-1`.
The forcing itself has only eight distinct poles, `a` and `a-K`. Consequently,
a bound on the **degree of the forcing alone** does not remove this example;
restrictions on pole locations, heights, or correction complexity matter.

There is a valid coefficient-space lower bound: if a residual has coefficients
`R_j` on one orbit/order, supported on `A<=j<=B`, and invariant `I`, then

\[
 \max_{A\le j\le B}|R_j|
 \ge\frac{|I|}{\sum_{j=A}^B16^{-j}}. \tag{19}
\]

This follows from triangle inequality in (10). It is a bound on partial
fraction coefficients with **specified pole range**, not on values along the
positive integers. For the unnormalized truncated correction
`sum_(k=1)^K16^-k r(n+k)`, the residual is exactly `16^-K r(n+K)`: its poles
are at `a-K`, with coefficients `16^-K` times the original residues. The
weight in (10) compensates exactly. This is the mechanism preventing a
uniform real-axis residual gap from following from qualitative nonvanishing.

The exact tests replay both the finite-sum correction and the independently
constructed pole list for `K=1,2,4,9`, then check values out to `n=10^9` using
fractions. These checks support the formulas; the universal bounds are proved
above. A successful next approximation argument must control the complexity
and norm conversion that (13)--(19) expose.

### 6.4 A finite universal discriminator under a degree bound

The previous counterfeits do not make every finite probe powerless. A declared
complexity bound changes what exact finite tests can establish. This theorem
was proposed by the coordinator and independently checked in the analytic lane.

**Theorem DA-DEGREE.** Let `d>=0` be an integer and `q=A/B`, where `A,B` have
rational coefficients, `B` is nonzero, and both degrees are at most `d`.
Suppose `B(j)!=0` for every integer `0<=j<=2d+5`. Then at least one integer
`n` with `1<=n<=2d+5` satisfies

\[
 r(n)-16q(n-1)+q(n)\ne0. \tag{20}
\]

**Proof.** Use the exact reduced source presentation

\[
 r(z)=N(z)/D(z),\quad N(z)=120z^2-89z+16,
\quad D(z)=512z^4-1024z^3+712z^2-206z+21.
\]

Here `D(n)=(8n-7)(8n-4)(8n-3)(8n-2)/8>0` for every positive integer `n`.
Put the residual over the common denominator `D(z)B(z-1)B(z)`. Its numerator
is

\[
 F(z)=N(z)B(z-1)B(z)-16A(z-1)D(z)B(z)+A(z)D(z)B(z-1).
\]

The first summand has degree at most `2d+2`; the other two have degree at
most `2d+4`. Thus `deg F<=2d+4`. It is not the zero polynomial, by the
actual-source rational coboundary obstruction in section 5. If (20) failed
at all `2d+5` probe points, the nonvanishing denominator hypotheses would
give that many distinct roots of `F`, a contradiction. The standard root
bound follows by the factor theorem: successive distinct roots give a
product of distinct linear factors dividing `F`, whose degree cannot exceed
`deg F`. QED.

`bbp_degree_bounded_counterexample` takes exact ascending polynomial
coefficient lists and the integer degree bound, verifies the domain, and
returns the first sample index and its nonzero rational residual. It rejects
a denominator presentation vanishing at a probe point, rather than treating
that as a valid residual or guessing how to cancel a removable factor.
Each returned nonzero residual independently refutes that candidate rational
identity. Universal termination within `2d+5` probes is supplied by the paper
proof, not by a finite implementation census.

Tests include a constant candidate fitting the first point exactly, and
Lagrange-interpolated candidates fitting BBP prefixes of lengths `0,1,2,4,6`.
Every returned failure lies outside the fitted prefix and within the proven
bound; each residual is recomputed independently. The Lagrange code is
different from the Newton interpolation in the generic counterfeit builder.
Undeclared degrees, inexact coefficients, boolean degrees and singular
presentations are rejected. This is a finite source-specific discriminating
probe with an explicit guarantee, not a probe that decides pi normality.

## 7. Attempts at the genuinely global theorem

### 7.1 Van der Corput: a valid reduction, no seed

For `z_n=e(h16^n*pi)`, `0<=n<N`, and integers `1<=H<=N`, zero-extend `z`.
Each term occurs `H` times in
`H sum z_n=sum_(m=0)^(N+H-2) sum_(j=0)^(H-1) z_(m-j)`.
Cauchy--Schwarz followed by expansion proves

\[
 |S_N(h)|^2\le\frac{N+H-1}{H^2}
 \left(HN+2\sum_{d=1}^{H-1}(H-d)\Re C_d\right),
\quad
 C_d=\sum_{n=0}^{N-d-1}e\big(h(16^d-1)16^n\pi\big). \tag{11}
\]

The diagonal is `HN`; each lag `d` occurs `H-d` times. Equation (11) is
classical differencing, derived here to make its exact remaining input visible.
The correlations are the same unknown source family at new frequencies. A
claimed bound on them would be a new analytic hypothesis, not a consequence
of the small BBP forcing. Multiplication of `h` by 16 only shifts a Weyl sum
and changes two endpoints. Neither identity supplies cancellation.

### 7.2 Diophantine separation is not enough

A hypothetical irrationality measure bound
`|pi-p/q|>=c q^(-mu)` gives `||q*pi||>=c q^(1-mu)`. At denominators
comparable to `16^n`, this is exponentially small and does not estimate (11).
More decisively, [B11] proves that, for every integer `b>=2`, the
Thue--Morse--Mahler number

\[
 \tau_b=\sum_{k\ge0}t_k b^{-k},\quad t_0=0,\quad
 t_{2n}=t_n,\quad t_{2n+1}=1-t_n
\]

has irrationality exponent exactly 2. At `b=16` its canonical digits are all
zero or one, so the digit 2 has frequency zero: it is not base-16 normal.
Thus even the optimal exponent 2 does not force base-16 normality. The
irrationality-exponent assertion is an explicitly imported theorem; the digit
exclusion is elementary. No statement about the best known measure for pi
is needed, and none is inferred.

### 7.3 Expanding dynamics and the right remaining hole

Almost-everywhere normality for the map `u -> 16u mod 1` does not identify the
specific initial point supplied by the BBP sum. Nor does a transfer operator
bound on absolutely continuous densities control a single Dirac initial law.
Lagarias [L02] explicitly separates a general decaying-forcing shadow relation
from the special arithmetic hypotheses needed by the Bailey--Crandall program.
The counterexamples in section 6 supply exact failure receipts in our class.

A potentially more tractable **criterion**, imported from the weak hotspot
theorem [BM06, Theorem 1.1], is a uniform upper occupation estimate: find one
finite `B`, independent of the arc `I`, such that

\[
 \limsup_{N\to\infty}\frac1N\#\{n\le N:x_n\in I\}
 \le B|I| \quad\hbox{for every circle arc }I. \tag{12}
\]

The shadow bound transfers (12) to `y` with the same `B`, by enlarging arcs
and discarding a finite prefix. The hotspot criterion then yields normality.
This is an **equivalent source-level criterion**, not a theorem established
for pi, and it pays no novelty tax by itself. A genuinely new intermediate
goal is a source-dependent bound on a specified increasing family of arcs
or on the lag correlations in (11), with constants controlled before limits.

Known positive calibration is provided by the classical Stoneham family
`alpha_(b,c)=sum_(k>=1)1/(c^k b^(c^k))`, normal in base `b` when integers
`b,c>1` are coprime [BC02]. In particular `alpha_(16,3)` supplies a positive
source where a separate arithmetic mechanism proves normality. Its sparse
forcing and modular permutation argument are not the BBP rational forcing.

## 8. Final hole contract and discriminating probes

- **Exact missing claim:** (OPEN), or equivalently the uniform no-hotspot
  estimate (12) for the actual rational BBP forcing with `x_0=0`.
- **Truth state:** UNVERIFIED; no source-specific cancellation bound proved.
- **Quantifiers:** every fixed nonzero integer frequency, all sufficiently
  large sample lengths; any growing-frequency assertion must state its range.
  In (12), one finite `B` must work for every arc, before taking its limsup.
- **Weakest presently sufficient criterion:** the classical one-sided
  occupation criterion (12), explicitly recognized as equivalent at the
  source level. No weaker sufficient lemma has yet been proved here.
- **Edges closed:** actual rational source to positive tail; tail to explicit
  Fourier/discrepancy transfer; rational source to non-telescoping invariant.
  The approximation extension proves that this invariant supplies no uniform
  weighted residual gap without further complexity restrictions. A declared
  degree bound does supply the exact finite discriminator in section 6.4.
- **Edges still open:** nonzero pole invariants to any global cancellation;
  irrationality to normality; a.e. dynamics to this source-specific point.
- **Novelty tax:** the sharper source tail is a proved quantitative gain;
  the pole test is a proved discriminant; (11) and (12) are classical
  reductions. None is represented as a new proof of normality.
- **Cheapest falsifiers:** positive leading-matched fake; exact finite-prefix
  fake; Thue--Morse exponent-2 nonnormal source; zero and wrong-index mutants.
- **Fresh test region:** prefix lengths `0,1,2,3,5,8,12`, then indices beyond
  fitting; pole orders through 3 and bases `2,3,16,257`, including a perturbation
  of `10^(-30)` that floating-point screening could lose.
- **Candidate proof languages:** rational difference equations and pole
  invariants; exponential-sum differencing with an independently proved seed;
  interval occupation estimates with uniform constants.
- **Finite boundary:** no census or exact test licenses an infinite frequency
  limit. The probe emits no normality verdict.
- **Next lamp:** a quantified arithmetic estimate for BBP orbit occupation or
  the lag family in (11), surviving both counterfeit controls. A rational
  approximation to the cohomological correction must control degree, height,
  approximation domain, and residual; section 6.3 proves that qualitative
  nonexistence of an exact rational correction supplies no uniform gap in the
  specified weighted norm.

## 9. Primary-source map and proof dependencies

Only short paraphrases and independently derived reductions are included;
no papers are copied into the repository.

| Source inspected | Actual role and scope | Missing bridge |
|---|---|---|
| [BC01] Bailey--Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), 175--190, [author preprint](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf), DOI `10.1080/10586458.2001.10504441` | BBP forced orbit; conditional arithmetic dynamical hypothesis; source identification of the pi sum | The hypothesis is not established for pi here |
| [L02] Lagarias, *On the Normality of Arithmetical Constants*, [arXiv math/0101055v2](https://arxiv.org/html/math/0101055v2) | General shadow/perturbation statements hold under much weaker conditions than normality; arithmetic restrictions matter | General decaying perturbations do not establish the special arithmetic assertion |
| [AS25] Arreche--Sitaula, *A computational approach to rational summability and its applications via discrete residues*, [arXiv 2503.15636v1](https://arxiv.org/html/2503.15636v1) | Classical discrete-residue context for rational shift summability | Our constant-weight finite proof is given explicitly; no borrowed theorem silently changes its shift convention |
| [B11] Bugeaud, *On the rational approximation to the Thue--Morse--Mahler numbers*, Ann. Inst. Fourier 61 (2011), 2065--2076, [primary PDF](https://www.numdam.org/article/AIF_2011__61_5_2065_0.pdf), DOI `10.5802/aif.2666` | Irrationality exponent 2 for the stated family; theorem on printed p.2068 | Excludes measure-only inference; does not estimate pi sums |
| [BC02] Bailey--Crandall, *Random Generators and Normal Numbers*, Experimental Mathematics 11 (2002), 527--546, [author PDF](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf), DOI `10.1080/10586458.2002.10504704` | Normality of coprime Stoneham families provides a genuinely proved positive comparison | Sparse modular arithmetic does not automatically apply to rational BBP forcing |
| [BM06] Bailey--Misiurewicz, *A Strong Hot Spot Theorem*, Proc. AMS 134 (2006), 2495--2501, [author PDF](https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf), DOI `10.1090/S0002-9939-06-08551-0` | Theorem 1.1 supplies the uniform one-sided occupation criterion | Its uniform estimate remains unproved for the BBP source |

The directly proved algebra in sections 3--6 does not require Hypothesis A,
RH, ABC, a mixing hypothesis, or an assumed digit-cancellation statement.
Only the BBP identity identifies the shadow with pi. Source URLs and stated
versions identify consulted literature, not cryptographically authenticated
formal environments. Source PDF hashes are not claimed.

## 10. Reproduction, failures, and authority boundary

From the repository root:

```sh
python -m unittest discover -s tests -p test_duck_bbp_fourier.py -v
python scripts/duck_bbp_fourier_probe.py
```

The probe emits exact fractions, source-file hashes, the base Git state and
finite checks. It does not claim to be a trusted proof checker. The Python
partial-fraction interface requires complete inputs and trusted execution;
caller-supplied descriptions are not proof authority. Nothing in this lane
changes a source archive, central claim registry, shared CI, or imported proof.

An early test incorrectly demanded that the optimized discrepancy budget
strictly decrease at every selected sample length. The sharper budget can use
`K=0` across several lengths, giving equality. This **invalid test assumption**
was corrected to nonincrease plus an eventual strict gain, and supplemented by
an independent exact empirical-discrepancy comparison. No mathematical theorem
was weakened to hide a counterexample.

The coordinator separately owns whole-repository tests and formal review. This
lane has no Lean declaration, axiom audit, hosted CI receipt, or mainline merge
claim. Independent paper review is requested; its outcome must be recorded
separately from the author's proof and the finite arithmetic checks.

A separate referee agent independently checked the proofs through section 6.2,
the sharp tail limit, Fourier/discrepancy constants and van der Corput identity
on 2026-10-21 and found no substantive concern. This is internal same-model
review, not an external human referee or a proof-assistant certificate. The
section 6.3 continuation was sent for a separate review after that checkpoint.
The initial finite receipt remains preserved at its original source commit;
the approximation continuation receives a new receipt instead of rewriting
that historical evidence.

The referee and the BBP formalization agent subsequently independently checked
the section 6.3 telescoping, weighted norm constant, finite-attractor argument,
finite-window bound and pole counts; both reported that the proof survives.
The referee also inspected the primary weak-hotspot theorem and confirmed the
uniform constant's quantifier scope. Section 6.4 has a coordinator derivation
and analytic-lane algebraic check; this is still internal same-model review.
