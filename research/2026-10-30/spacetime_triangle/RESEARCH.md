# SUCC — Extrude, rotate, tile: an exact BBP zero-spine and Fourier spacetime strip

**Research only; candidate new SUCC application of classical posterior/Bratteli/Pascal and Fourier facts.** No claim of academic novelty, quantum amplitude, physical selection, normality of pi, or RH. Based on the unchanged original four-pole `main` source at `e18ba565ca540adb7edf3292f5593929e76d91c5` (Main XVI). The Bernoulli path law is an **auxiliary declared observer**, not a stochastic account of actual pi digits. The authentic selected recurrence `U_0=0, U_n=16U_{n-1}+r(n)` is retained separately.

## Geometry: triangle fibers, sideways rectangle, triangular tiling

A triangle is a finite update, superposed endpoint/posterior, and observation. Excluding the boundary, a **triangle extruded in time** is a triangular prism; its side *projection* is a rectangle. To retain its structure, subdivide the time strip into elementary Pascal triangles/diamonds. A slice at observation depth `m` has grades `j=0,...,m`. The discrete lattice `(m,j)` is a wedge, not literally a uniform rectangular grid; `j/m` is a strip coordinate with nonuniform spacing, so a naive 2D stationary Fourier multiplier is unjustified.

```
TIME / observations  --->
       m=0           m=1             m=2             m=3
        [0]       /[0] [1]       /[0] [1] [2]     /[0] [1] [2] [3]
                   \\ /            \\ / \\ /          \\ / \\ / \\ /
        latent X, signed pi phase, and integer-carry marks are DISTINCT layers
```

All `m` updates here share **one** latent `X`, and `f(x)=exp(-8x)`, `g(x)=1-f(x)` are the zero and one likelihoods. Start at `X~mu_1`, `mu_a(dx)=e^{-ax}Q(x)dx/R(a)`, with

```
Q(x)=4-2exp(-3x)-exp(-4x)-exp(-5x)
    =2(1-exp(-3x))+(1-exp(-4x))+(1-exp(-5x)) >0
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)>0, a>0
r(n)=R(8n-7), R(1)=47/15.
```

## ST-01: exact 2D Pascal measure and its Fourier symbol — PROVED LOCAL

Define finite **unnormalized positive measures**

```
M_(m,j)(dx) = C(m,j) f(x)^(m-j) g(x)^j mu_1(dx), 0<=j<=m.
```

Their sum is exactly `mu_1` (every observation level) and their update law is

```
M_(m+1,j) = f M_(m,j) + g M_(m,j-1),
M_(0,0)=mu_1, M_(m,j)=0 outside 0<=j<=m.
```

This is the precise triangular tiling of the side-view strip. Conditional posteriors follow by normalizing the measure at `(m,j)`; a bare grade without posterior is generally not a full predictive state. For `z=exp(i eta)` Fourier in grade,

```
Mhat_m(z;dx)=sum_j z^j M_(m,j)(dx)
            =[f(x)+z g(x)]^m mu_1(dx),
Mhat_(m+1)(z;dx)=[f(x)+z g(x)] Mhat_m(z;dx).
```

Its two-variable time generating/resolvent identity is exact for `|w|<1`:

```
sum_(m>=0) w^m Mhat_m(z;dx)
  =mu_1(dx)/[1-w(f(x)+z g(x))].
```

For `|z|=1`, the *local* spectral defect is

```
1-|f+z g|^2=4 f g sin^2(eta/2).
```

For `eta` not a multiple of `2pi`, this is strictly positive at **every fixed** `x>0`. Yet it tends to zero as `x -> 0` and as `x -> infinity`. Since `mu_1` gives mass to neighborhoods of both ends, the multiplication operator on `L^2(mu_1)` has **norm exactly 1 for all eta**: no **uniform** nonzero-grade spectral gap follows from this tiling. For fixed `mu_1`, the *integrated* grade characteristic does tend to zero by dominated convergence, but without a uniform operator norm bound. These statements are compatible. This operator is classical positive-state Fourier bookkeeping, not the Koopman map of pi's selected orbit.

## ST-02: zero-spine realization of the AUTHENTIC native BBP source clock — PROVED LOCAL

Let `C_(n-1)` be the event that the first `n-1` outcomes were **all zero**. Because `X` is retained,

```
P(C_(n-1))=E_mu_1[f(X)^(n-1)]
           =R(1+8(n-1))/R(1)=r(n)/R(1),
X | C_(n-1) ~ mu_(8n-7),
P(next zero | C_(n-1)) = r(n+1)/r(n).
```

Thus the actual arithmetic clock `a_n=8n-7` is the **successive posterior** along one selected (zero) edge of a single consistent infinite classical path space. This is stronger than treating `mu_(8n-7)` as unrelated normalized snapshots. It is *rare-event conditioning / a tilted posterior spine*, akin to a finite-horizon Doob transform; **not** a constructed stationary Markov chain or a positive-probability eternal all-zero trajectory.

General branch words with `j>0` successes have a posterior proportional to `f^(m-j) g^j mu_1`, generally *not* a single member `mu_(a+8k)`; retain the measure-valued field rather than resetting to a one-parameter prior. This guards the desired "next triangle = virtual field of the realized endpoint" rule.

For the genuine four-pole source, expansion at large `n` gives

```
r(n)=15/(64 n^2)+151/(512 n^3)+O(n^-4),
P(C_(n-1))~ C_spine/n^2, C_spine=225/3008.
```

Therefore the all-zero infinite path has original probability **zero**. Conditional measures nevertheless exist at each finite `n`. Unscaled `mu_(8n-7) -> delta_0` weakly, while the blown-up `Y_n=(8n-7) X | C_(n-1)` converges to `Gamma(2,1)`. Nontrivial Gamma geometry survives in the **tangent/blow-up at the zero boundary**, not as a positive-mass eternal path. The `Gamma(2)`/negative-binomial observer is what yields `G(z)=(2-z)^(-2)` and, under its *separately declared* branching fixed-point reading, the historical golden Oily–Macaroni specialization `lambda-gamma`.

The zero-spine hazard satisfies the source-specific expansion

```
h_n=1-r(n+1)/r(n)=2/n-209/(120n^2)+O(n^-3).
```

For the Gamma-matched comparison `R_fake(a)=15/a^2` on the **same clock**,

```
h_n(fake)=2/n-5/(4n^2)+O(n^-3),
h_n(original)-h_n(fake)=-59/(120n^2)+O(n^-3).
```

The arithmetic `59` from the authentic `Q''(0)=-59` is carried *along time* at the second-order hazard level, not just through static harmonic/Gamma snapshots. These are scalar positive-source distinctions, **not** signed pi cancellation.

**Exact harmonic/Euler finite part of the extruded spine**:

```
lim_(n->infinity) [-log P(C_(n-1)) -2 H_(n-1)]
    = log(3008/225)-2 gamma.
```

This is an exact original-source normalization of harmonic vs logarithmic time, with no golden constant inserted by hand. At native rank two the golden fixed point arises in the **fan observation** described next.

## ST-03: native fan glued at every zero-spine tile — PROVED LOCAL

At the conditional source `mu_(8n-7)` launch `n` additional trials and let `J_n` be their grade. Define the **unconditional spine-and-fan mass** (not a probability distribution over different n):

```
B_(n,j)=P(C_(n-1), J_n=j)
       =[r(n)/R(1)] q_(8n-7,n)(j)
       =C(n,j)/R(1) * sum_(k=0)^j (-1)^k C(j,k) r(2n-j+k).
```

These two calculations agree exactly and `sum_j B_(n,j)=r(n)/R(1)`. The fan grade transform is

```
B_n(z)=sum_j B_(n,j) z^j
      =1/R(1) * sum_(k=0)^n C(n,k) z^(n-k)(1-z)^k r(n+k).
```

This is an exact **four-pole Fourier/Pascal arithmetic polynomial**. As `n` grows, `J_n` under the conditioned fan converges to the Gamma–Poisson/negative-binomial law

```
w_j=(j+1)/2^(j+2),  G(z)=sum_j w_j z^j=1/(2-z)^2.
```

Hence for every `|z|=1`,

```
lim_(n->infinity) n^2 B_n(z)=(225/3008)/(2-z)^2.
```

In particular the **conditional parity Fourier mode** is **not damped**:

```
lim E[(-1)^J_n | C_(n-1)] = G(-1) = 1/9 != 0.
```

This is an exact obstruction to mistaking the native conditioned extrusion for a uniformly mixing, stationary Fourier strip. The fixed-prior forward process and the rare-conditioned native process have different grade-frequency asymptotics.

### A rigorous high-grade occupancy bound through the wedge

From `15 x exp(-5x) <= Q(x) <= 15 x` for `x>=0` one obtains

```
15/(a+5)^2 <= R(a) <= 15/a^2.
```

For `z>=1`, `a_n>8n(z-1)`, and `J_n|C_(n-1)` as above,

```
E[z^J_n] <= R(a_n-8n(z-1))/R(a_n).
```

The first inequality follows from `(f+zg)^n <= exp(n(z-1)g) <= exp(8n(z-1)X)`. Choose `z=2-2/L`, `n>=L>=4`. Chernoff, the R bounds and elementary algebra give

```
P(J_n>=L | C_(n-1))
 <= [(8n-2)/(16n/L-7)]^2 (2-2/L)^(-L)
 <= (256/81) L^2 2^(-L) .
```

If `n<L`, the left side is exactly zero, so the final bound holds for **every** native clock `n>=1` and integer `L>=4`. Taking `L=floor(log_16 n^2)` (for `n` sufficiently large),

```
P(J_n>=L | C_(n-1)) = O((log n)^2/sqrt(n)).
```

This is a genuine **arithmetic bound on the position within the extruded, conditioned positive path wedge**. It does NOT bound how often the *deterministic selected pi orbit* enters any digit/carry region. The latter still needs a coupling theorem; Kepler III already has a distinct all-seed `O(N/log N)` bound on sparse carry-correction events, insufficient for digit normality.

## ST-04: Fourier along TIME of the zero-spine strip — PROVED LOCAL

The one-sided time generating function is

```
T(w) = sum_(n>=1) [r(n)/R(1)] w^(n-1), |w|<=1.
```

Because `r(n)~15/(64n^2)`, it is absolutely convergent on the unit circle. For `|w|<1`, it has an **exact four-pole Lerch-transform**:

```
T(w)= [4 Phi(w,1,1/8)-2 Phi(w,1,1/2)
       -Phi(w,1,5/8)-Phi(w,1,3/4)]/[8 R(1)]
```

with `Phi(w,1,a)=sum_(k>=0) w^k/(k+a)`. The singular `-log(1-w)` terms of the separate poles cancel because `4-2-1-1=0` (take their *combined* limit at w=1; **do not** numerically evaluate the individually divergent Lerch terms at 1). In digamma form,

```
T(1)= -[4 psi(1/8)-2 psi(1/2)-psi(5/8)-psi(3/4)]/[8R(1)].
```

For real `t -> 0`, `w=exp(i t)`, the sharp temporal Fourier cusp is

```
T(exp(i t)) - T(1) = i (225/3008) t log(1/|t|) + O(|t|).
```

**Proof:** write `p_n=r(n)/R(1)=C/n^2+O(n^-3)`. The `O(n^-3)` remainder changes the Fourier difference by `O(|t|)` because `sum n*|remainder|<infinity`. For `C/n^2`, split the series at `n=floor(1/|t|)`: for `n<=1/|t|`, `exp(i n t)-1=i n t+O(n^2t^2)` and the linear term is `i C t H_floor(1/|t|) = i C t log(1/|t|)+O(t)`; the quadratic remainder contributes `O(t)`. The tail `n>1/|t|` is `O(t)`. Changing `n` to `n-1` in the phase likewise costs `O(t)` because `sum p_n<infinity`. QED.

This is a **genuine Fourier signature** of the original source's rank-two time-spine. It is *not* a selected pi Weyl gain: the same temporal continuity holds for arbitrary bounded phase marks attached to the rare spine, because all weights are absolutely summable. If one attaches authentic `e(h U_(n+j)(0))` to the fan, the spectral symbol is a representation but no sign saving follows from the summable `n^-2` weight.


### ST-04c: the joint TIME x GRADE Fourier cusp (actual triangle-on-triangle)

Take the Fourier/generating transform in both directions: for `|w|<=1, |z|<=1`,

```
D(w,z) := sum_(n>=1) w^(n-1) B_n(z)
        = sum_(n>=1) w^(n-1) [r(n)/R(1)] G_n(z),
G_n(z) := sum_j q_(8n-7,n)(j) z^j.
```

The native Pascal fan has `G_n(z) -> G(z)=(2-z)^(-2)` uniformly for
`|z|<=1`, with explicit `O(1/n)` uniform error: the inherited original-source
TV estimate from the Pascal/q6 program gives
`sum_j |q_(8n-7,n)(j)-w_j| <= 44/n`, where
`w_j=(j+1)/2^(j+2)` (see
`research/2026-10-29/q6_gamma_abel_tiling/CESARO_FIREWALL.md`).
The original spine has `p_n=C_spine/n²+O(n^-3)`. Therefore

```
B_n(z) = C_spine (2-z)^(-2) n^(-2) + O(n^-3),
```

**uniformly on the closed unit disk**: boundedness of `G` and the TV bound
control the remainder. Apply the elementary Fourier cusp proof above to these
complex coefficients. Uniformly for `|z|<=1`, as real `t -> 0`,

```
D(exp(i t),z)-D(1,z)
  = i (225/3008) (2-z)^(-2) t log(1/|t|) + O(|t|).
```

This is a rigorous **separable two-axis singularity** of the actual tiled
source strip, with original-four-pole time coefficient and a nontrivial
vertical Pascal/Fourier shape. For `z=-1` (genuine parity character) the
coefficient is `i C_spine/9`. For `z=1` it is `i C_spine`.

At the *marked real PGF* coordinate `z=lambda²`, where
`lambda=phi^(-1)` and `G(lambda²)=lambda²`, the coefficient is exactly
`i C_spine lambda²`. This is an exact mathematical place where the
**old harmonic/golden/Euler–Mascheroni triangle sits inside the new
time-extruded operational apparatus**: rank 2 supplies the temporal
harmonic cusp, and the declared two-channel endpoint evaluation supplies
the golden vertical factor. It is a **PGF evaluation**, not a unit-circle
Fourier frequency, and does **not** imply any pi digit cancellation.

The statement is not a theorem for an arbitrary array of complex marks
attached to the selected pi orbit: the factorization uses the genuine
positive conditional grade weights and their proven O(1/n) approach to
the source-derived `w_j`. Those weights do not constrain the signs of
`exp(2pi i h U_n(0))`.

### Why rank two is a Fourier regularity threshold

The logarithm is not an artifact of the four particular poles. For any positive
source with `Q(x) ~ c x^(r-1)` as `x -> 0`, `R(a) ~ c Gamma(r) a^-r`.
Conditioning on a length-`n` zero spine from a fixed `a_0>0` makes the spine
survival `p_n ~ C n^-r`. Its unweighted time series on the unit circle has:

- `r <= 1`: `sum p_n = infinity` (no finite continuous boundary value at time-frequency 0);
- `1 < r < 2`: at least the universal Holder bound
  `|T(e^(it))-T(1)| = O(|t|^(r-1))`;
- `r = 2`: the *borderline* `i C t log(1/|t|)+O(t)` behavior when the
  coefficient has a controlled `O(n^-3)` remainder (as the authentic BBP source does);
- `r > 2`: `sum n p_n < infinity` and `T(e^(it))` is differentiable at `t=0`.

Proof of the regularity bounds: use
`|e^(int)-1| <= min(2,n|t|)` and split the sum at `1/|t|`.
For the rank-two coefficient, the harmonic divergence of `sum 1/n` gives the
explicit logarithmic cusp. **Thus the authentic rank-two Gamma boundary is also
a critical time-Fourier smoothness boundary.** That gives the
Harmonic/Gamma side of the original triangle an additional exact geometric role.
It does not select the golden fixed point without the separate two-channel fan
grammar, and it does not constrain the selected pi circle orbit.

## ST-05: why one more gluing theorem is needed — OPEN

The triangle's positive source `X` and its Bernoulli histories do not generate the selected real BBP `U_n(0)`: the latter obeys the deterministic affine recurrence. If a phase mark is attached to the fan, its actual time transport obeys

```
e(h U_(n+1))=e(h r(n+1)) e(16h U_n),
```

which shifts integer Fourier frequencies `h -> 16h` and has modulus one. A Fourier transform of the side-rectangle and triangular tiling alone therefore has **no spectral-gap implication** for the selected zero seed. (In fact the grade multiplier has `L^2` operator norm 1 and the native fan keeps parity mode 1/9.)

The missing theorem is a **seed-sensitive signed intertime correlation bound** generated from *additional arithmetic coupling*, not from positivity, posterior conditioning, or a spectral representation alone. A proposed bound must still reject the coherent same-forcing counterseed `s*=-pi/16` while respecting observationally equivalent rational seed translations. Separately inspect and repair Main XVI's too-strong claims that every rational periodic twist must fail asymptotically and every nonzero integer-shift alias changes the carry: neither claim is true as written. No merge/status promotion without those reviews.

## Source/provenance and adversarial controls

- Original source `R(a)`, clock `a_n=8n-7`, deterministic `U_0=0` immutable.
- Counterseed `s*=-pi/16` retains all positive source/Pascal/spine/Fourier geometry but has nonnormal selected phase; thus the new positive theorems cannot force normality.
- Gamma-matched fake `Q_fake=15x` has the same rank-two tangent and limiting grade `G(z)`, but differing second-order spine hazard `-59/(120n^2)`.
- Nonzero successes do not stay on the pure `mu_a` clock; full posterior is needed.
- Infinite all-zero spine has probability zero, though finite conditional triangles exist and their blown-up tangent has Gamma rank two.
- No self-contained proof of positive physical observation, pi normality, RH, or unique academic originality is claimed.

**Next:** construct and test source-coupled *selected* phase/carry correlations in this strip; check if any analytic inequality is available beyond universal telescoping or Haar-over-seeds, with independent arithmetic holdouts and corrected rational seed aliases.
