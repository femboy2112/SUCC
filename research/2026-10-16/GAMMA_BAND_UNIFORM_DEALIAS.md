# Band-uniform Gamma de-aliasing from source-indexed SUCC clocks

**Source and scope:** Continuation of the Dirac-comb Gamma research (DGC-1–5,
PR #141, commit `849b241801578542997972eb46f3c8d309b36d0c`), itself based on
main `02fc9f46ad3b914d49df7a658e304d06ed8a6200`.
**New branch:** `research/gamma-band-dealias-interleaving-2026-10-16`.
**Claims:** BGD-1–7 below: CLASSICAL ANALYSIS with source-typed exact rational
certificates and independent numerical controls; **no claimed academic priority**.
**RH PROVED: NO.** No nontrivial zeros are inputs. This work does not make a
positive Weil form or derive the Archimedean factor from prime coefficients.

## Source and observation contract

Let `h>0` be rational. The original genuine, two-sided, Gaussian real-place
source is

\[
f_s(u)=\exp(su/2-\pi e^u),\quad
\Gamma_{\mathbb R}(s)=\int_{\mathbb R}f_s(u)\,du
=\pi^{-s/2}\Gamma(s/2),\quad \Re s>0.
\]

The continuous object is the **real-place** Tate factor, not the ordinary
Gamma(s), and `pi`, the `s/2` slope, and the two-sided logarithmic carrier are
load-bearing. The infinite sampled clock
`R_h(s)=h sum_(n in Z) f_s(nh)` is a mathematical chart; finite source histories
are the truncated sums below. All equalities involving `R_h` are initially in
`Re(s)>0`, with meromorphic continuation kept separate.

Poisson summation (DGC-3) gives

\[
R_h(s)=\sum_{k\in\mathbb Z}
\Gamma_{\mathbb R}(s-4\pi i k/h).
\]

This is the exact premise for every exponential bound; replacing the source
with a fake impulse or arbitrary Tate test does **not** inherit that bound.

## BGD-1. Coherent q-observer interference (PROVED PAPER, exact algebra)

For an integer `q>=1`, stagger q clocks by `jh/q`, `j=0,...,q-1`:

\[
R_{h,j/q}(s)=h\sum_{n\in\mathbb Z}f_s(h(n+j/q)).
\]

Its Poisson alias coefficient at harmonic `k` is
`exp(2*pi*i*k*j/q)`. The equal-weight observer fusion satisfies

\[
\frac1q\sum_{j=0}^{q-1}R_{h,j/q}(s)
=R_{h/q}(s)
=\sum_{\ell\in\mathbb Z}
\Gamma_{\mathbb R}(s-4\pi i q\ell/h).
\tag{1}
\]

**Proof:** The integer pairs `(n,j)` map bijectively onto `m=qn+j`.
Finite Fourier orthogonality gives
`q^-1 sum_j exp(2*pi*i*k*j/q) = 1_{q|k}`.
This is an exact cancellation of all nonmultiples of q, including negative
harmonics. The first surviving alias height is `P_q=4*pi*q/h`.

**Optimality in the declared observation grammar:** With arbitrary complex
weights `w_j` on these exact q equally spaced offsets and `sum w_j=1`, the
coefficient of harmonic `k=q` is `sum w_j=1`. Thus **no normalized linear
combination of these q charts can remove alias q**. If harmonics
`1,...,q-1` are also killed, finite DFT inversion forces all `w_j=1/q`.
Changing the offsets, nonlinear observables, adding a source oracle, or
admitting more samples changes the grammar and is not covered by the no-go.
The q-fold gain incurs q times the sampling density; it is not a speedup.

## BGD-2. Sharp spectral horizon (PROVED PAPER)

Write `d=h/q` and `P_d=4*pi/d`. For any *fixed* real sigma>0 and any family
d->0 of exact clocks, define

\[
E_d(T)=\sup_{|t|\le T}|R_d(\sigma+it)-\Gamma_{\mathbb R}(\sigma+it)|.
\]

For any nonnegative horizon `T=T(d)`, the following is a **necessary and
sufficient** condition for absolute-error uniform convergence:

\[
\boxed{E_d(T(d))\to0\quad\Longleftrightarrow\quad
P_d-T(d)\to+\infty.}\tag{2}
\]

**Sufficiency:** The contour bound below makes all nonzero aliases uniformly
small when `P_d-T->infinity`.
**Necessity:** If `T>=P_d` along a subsequence, evaluate at `t=P_d`.
Periodicity gives `R_d(sigma+iP_d)=R_d(sigma)->Gamma_R(sigma)>0`, whereas
`Gamma_R(sigma+iP_d)->0`. Otherwise, if `P_d-T` is bounded along a subsequence,
choose `t=T=P_d-D` with `0<=D<=C`. The `k=1` Poisson replica is
`Gamma_R(sigma-iD)`, uniformly separated from zero on the compact D-range
because Gamma has no zeros. Every other replica, and the genuine target,
vanishes uniformly by vertical Gamma decay. Thus the error cannot tend to 0.

This criterion is for **absolute errors** on the right half-plane, not relative
errors near tiny target amplitudes, and not a theorem that finite primes or the
signed Weil form share this spectral horizon. At fixed h, all-height uniform
convergence is impossible.

## BGD-3. Exponential, band-uniform analytic bound (PROVED PAPER)

Let `0<a<=sigma<=b`, `|t|<=T`, and set `d=h/q`. For
`theta=pi/3`, move the log-Euler integral contour by
`u -> u + i*theta*sgn(v)` to obtain, for every real v,

\[
|\Gamma_{\mathbb R}(\sigma+iv)|
\le \Gamma(\sigma/2)
(\pi\cos\theta)^{-\sigma/2} e^{-\theta|v|/2}.
\tag{3}
\]

The contour shift is justified on `Re(s)>0`: the left tail decays like
`exp(sigma*u/2)` and the right like `exp(-pi*cos(theta)*exp(u))`.
With `M(a,b)=2/a+(ceil(b/2)-1)!`, positivity of Euler's integral and
`pi*cos(pi/3)=pi/2>1` show that the prefactor in (3) is <= M for the entire
strip. Indeed split the Gamma integral at x=1, bounding its first piece by
`2/a` and its second by `Gamma(ceil(b/2))`.

The Poisson aliases, summed as a geometric series, obey whenever `T<P_d`:

\[
\boxed{
|R_d(s)-\Gamma_{\mathbb R}(s)|\le
\frac{2M(a,b)\exp[-\frac\pi6(P_d-T)]}
{1-\exp[-2\pi^2/(3d)]}.}\tag{4}
\]

This is absolute and uniform simultaneously in sigma and t on the band.
The right-hand side falls exponentially as the first alias moves away from
the band's edge. The result is stronger than DGC's O(h) derivative estimate
on such bands, but specifically depends on the *analytic Gaussian* source.

## BGD-4. Entirely rational, finite-observer certificate (PROVED PAPER)

No `mpmath`, numerical Gamma evaluations, directed rounding, or estimates
of the positions of nontrivial zeros are required for the bound.
Choose exact rational `a,b,d,T`, `a>0`, and a rationally guarded band
`0<=T<12/d` (the true alias period is `4*pi/d > 12/d`). Define

\[
P_N(x)=\sum_{j=0}^N\frac{x^j}{j!},\quad
D=6/d-T/2>0,\quad M=2/a+(\lceil b/2\rceil-1)!.
\]

Since `pi>3`, `e^x>=P_N(x)` and
`1/(1-e^{-x})<=1+1/x` for x>0, (4) implies the
**exact rational majorant**

\[
E_{\rm alias}=
\frac{2M(1+d/6)}{P_N(D)}.
\tag{5}
\]

For the actual **finite** sample
`F_{d,A,B}(s)=d sum_{n=-A}^B f_s(nd)`, A,B>=0, define

\[
X=a(A+1)d/2,\quad U=(B+1)d,\quad
L=3(1+U)-b/2,\quad
Y=3(1+U+U^2/2)-bU/2.
\]

Assume `L>0` and `Y>=0`. The **left** omitted samples satisfy

\[
E_{\rm left}\le \frac{2/a+d}{P_N(X)}.
\tag{6}
\]

The **right** omitted samples satisfy

\[
E_{\rm right}\le\frac{d+1/L}{P_N(Y)}.
\tag{7}
\]

**Proof of (6):** For u<0, |f_s(u)|<=exp(a*u/2). Sum the exact geometric
tail from u=-(A+1)d, and use
`1/(1-exp(-a*d/2)) <= 1+2/(a*d)`.
**Proof of (7):** For u>=U, Euler's weight has modulus
`exp(sigma*u/2-pi*exp(u))`. With `pi>3` and
`exp(U)>=1+U+U^2/2`, its first term is <= exp(-Y).
Successive terms have modulus ratio <=exp(-Ld), since
`exp(d)-1>=d` and `exp(u)>=1+U`; sum geometrically.
Replace both exponentials by `1/P_N` and the geometric denominator
by `1+1/(Ld)`.

Thus the implemented **all-s uniform finite-source theorem** is

\[
\boxed{\sup_{a\le\Re s\le b,|\Im s|\le T}
|F_{d,A,B}(s)-\Gamma_{\mathbb R}(s)|
\le E_{\rm alias}+E_{\rm left}+E_{\rm right}.}\tag{8}
\]

All three terms are `fractions.Fraction`; they form a reproducible **paper
inequality certificate**, not an interval enclosure of evaluated floats.
The guarantee assumes the actual sampled values come from the declared
Gaussian source, including pi, s/2 and the complete chosen index range.

Illustration: `h=1/2`, q=2, d=1/4, a=1/2, b=3/2, T=8,
A=350, B=16, N=80, exactly 367 retained events. The rational total bound
is below `1/10^7`. mpmath at selected points observes considerably smaller
errors; those observations do **not** justify the theorem.

## BGD-5. Uniform derivative jets via Cauchy (PROVED PAPER)

The actual finite clock and Gamma_R are holomorphic on `Re(s)>0`.
For a target band `[a,b] x [-T,T]` and exact rational collar `0<r<a`,
apply (8) on the expanded band `[a-r,b+r] x [-T-r,T+r]` to obtain a
rational bound `B_ext`. Every disk of radius r around any target point lies
within that expanded rectangle. Cauchy's estimate yields

\[
\boxed{|F_{d,A,B}^{(j)}(s)-\Gamma_{\mathbb R}^{(j)}(s)|
\le j!\,B_{\rm ext}/r^j.}\tag{9}
\]

This covers the original Gamma **derivative jets** required in analytic
interfaces, but does not automatically control log derivatives, since those
also require authenticated nonvanishing and a sufficiently sharp **relative**
error bound. A derivative bound is not signed Weil positivity.

## BGD-6. Extension to compactly supported Tate–Mellin tests (conditional)

For `phi in C_c^infty((0,infty))`, the positive-axis Mellin chart is

\[
M_\phi(s)=\int_{\mathbb R}\phi(e^u)e^{su/2}\,du.
\]

Set `g_sigma(u)=phi(e^u)e^{sigma*u/2}`. Suppose a **source-derived and
separately verified** uniform norm bound
`sup_(a<=sigma<=b) ||g_sigma^(N)||_1 <= C_N` holds for some integer N>=2.
The Fourier transform of `g_sigma` at frequency
`2*pi*k/d-t/2` has modulus <= `C_N/|2*pi*k/d-t/2|^N`
by N integrations by parts. Set `x=d*T/12 < 1`.
With `pi>3` and the monotone integral test,

\[
\boxed{|M_{\phi,d}(s)-M_\phi(s)|\le
2C_N(d/6)^N\left[(1-x)^{-N}+
\frac{(1-x)^{1-N}}{N-1}\right].}\tag{10}
\]

The `compact_mellin_band_bound` code **does not authenticate** its supplied
`C_N`; it reports a conditional exact rational consequence. For a concrete
W^{2,1} (not C-infinity) positive-axis test, take
`phi(x)=x^{-1/2} (1-(log x)^2)^2_+` and sigma=1.
Then `g_1(u)=(1-u^2)^2_+`, with
`||g_1''||_1=32/(3*sqrt(3))<7`. An actual independent source norm bound
`C_2=7` thus validates the theorem at this fixed sigma.
Smooth compact test families work analogously when their derivative norm
certificate is supplied. This is not the full Schwartz–Bruhat adelic theory,
nor the completed signed Weil distribution.

## BGD-7. Mutation and impossibility controls (PROVED/REFUTED as scoped)

1. **Wrong amplitude/source:** Alter the weight of a single retained u=0
   event by `eta != 0`. The readout changes by exactly
   `d*eta*exp(-pi)`, independent of spectral height. Analytic exponential
   alias bounds for the original source no longer apply. This falsifies a
   source-blind transplantation of (8) to arbitrary observed sequences.
2. **Unshifted duplicate observers:** q copies of the *same* grid have
   identical Fourier alias coefficients; adding their reports does not
   cancel any harmonic. Distinct source-indexed offsets are essential.
3. **Finite horizon sharpness:** Sampling cannot give uniform all-height
   approximation of Gamma_R; (2) is an explicit observer-band frontier.
4. **Persistent pole lattice:** Interleaving moves the artificial poles
   to `s=-2m+4*pi*i*q*k/h`. At each finite q, nonzero k aliases remain;
   multiplying by authentic zeta still cannot cancel poles at m>=1.
   This retains DGC-5's non-cancellation obstruction.
5. **Against false transfer to Weil positivity:** An absolute Gamma
   approximation is not a positive Hilbert covariance, a signed Weil
   quadratic-form certificate, or a proof of RH. Low Schur sign, high/low
   coupling and all-support positivity remain open in SUCC.

## Reproduction, tool closure, and next falsifier

Source files (native SUCC, no imported archive modifications):

- `observational_succ/gamma_band_dealias.py`
- `tests/test_gamma_band_dealias.py`
- `scripts/gamma_band_dealias_probe.py`

Run narrowly (full CI is slow and must not be advertised as passed):

```
python -m unittest discover -s tests -p 'test_gamma_band_dealias.py' -v
python scripts/gamma_band_dealias_probe.py --verify
```

The next best mathematical probe is an **authenticated source-norm certificate
for a basis of real-place Schwartz–Bruhat Mellin tests**, with explicit
conductor/parity and prime-channel controls. Then seek operator/multiplier
comparison on a full Weil test space. A finite band result alone cannot pay
the global all-a positivity debt.

**Source literature:** NIST DLMF §5.9, Euler Gamma integral,
https://dlmf.nist.gov/5.9 ; classical shifted Poisson summation,
finite DFT character orthogonality and Cauchy estimates; previous DGC-1–5.
No credit for establishing these classical analytical tools is claimed.
