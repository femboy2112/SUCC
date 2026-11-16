# Angular aperture: exact projection, finite aliases, and changing resolution

This addendum records a classical alternative to real damped extrapolation.
Its full-circle observation is a stable exact projector, while its finite
phase bank has explicit aliases. The distinction is the amount and type of
boundary data supplied. No new Cauchy/Fourier theorem, Goldbach result,
computational speedup, or optimal sampling theorem is claimed.

The algebra and controls below were specified before their new execution:
four phases at `R=1/2`; a synthetic grade-four alias; an equality-budget
and a noisy-rounding mutation; the unit-circle support distinction; and
the already inspected arithmetic midpoints `67,263`. Those midpoints are
calibration cases, not fresh holdouts. The standalone
[phase_aperture.py](phase_aperture.py) uses the existing exact `Q(i)`
representation, exposes a deterministic `report()`, and writes no files.
The earlier unittest files are unchanged.

Let `c_h>=0`, `h in N_0`, have finite total mass `M`, and put

\[
F(z)=\sum_{h\ge0}c_hz^h.
\]

This series is analytic on the open unit disc and continuous on the
closed disc by absolute uniform convergence. The same source, grading,
normalization, and complex orientation must be used at every phase.

## PA01: the continuum is an exact norm-one projector — PROVED LOCAL

For every fixed `0<R<=1`,

\[
\boxed{c_0=\frac1{2\pi}\int_0^{2\pi}F(Re^{i\theta})\,d\theta.}
\tag{PA1}
\]

**Proof.** Uniform absolute convergence allows termwise integration.
The integral of `exp(i h theta)` is zero for every integer `h>=1`
and one after normalization for `h=0`. QED.

For `R<1` this is also Cauchy's integral formula at zero, using the
positively oriented circle `z=R exp(i theta)`; see
[NIST DLMF 1.9.30](https://dlmf.nist.gov/1.9.E30).
The endpoint `R=1` follows directly from the same uniformly convergent
Fourier-series calculation.

If a supplied angular profile has uniform complex error at most `eta`,
its averaged error is at most `eta`. The projection has operator norm
exactly one in the sup norm: a constant perturbation attains the bound.
An authenticated integrable error envelope can instead be paid by its
angular average. The theorem supplies stability of an already supplied
profile; it does not obtain that continuum of source observations at
finite cost.

This requires the phase-calibrated complex response, not just its power.
On the unit circle, `F(z)=M` and `F(z)=M z^k`, `k>=1`, have identical
magnitudes at every angle and the same total mass, but zero counts `M`
and zero. Their complex angular averages differ. Thus even a continuum
of power measurements cannot replace the declared signed profile.

## PA02: a finite phase bank has positive aliases — PROVED LOCAL

Fix integer `L>=1`, `0<R<1`, and the declared phases
`z_j=R exp(2πi j/L)`, `0<=j<L`. Root-of-unity orthogonality gives

\[
A_L:=\frac1L\sum_{j=0}^{L-1}F(z_j)
=\sum_{L\mid h}c_hR^h.
\tag{PA2}
\]

The value is real. Every surviving nonzero grade is at least `L`.
With `r=R^L`, positivity therefore gives

\[
0\le A_L-c_0\le r(M-c_0).
\tag{PA3}
\]

Thus `A_L>0` alone is not evidence of a zero grade: `c_L=1,c_0=0`
already gives `A_L=R^L>0`. A mass-corrected lower certificate is

\[
\boxed{B_L=\frac{A_L-rM}{1-r}\le c_0\le A_L,\qquad
0\le c_0-B_L\le\frac{r(M-c_0)}{1-r}.}
\tag{PA4}
\]

If only an upper bound for `M` is authenticated, substituting it in
the lower certificate remains conservative.

When `c_0` is integral, the budget

\[
\boxed{Mr<1}
\tag{PA5}
\]

implies both `B_L>0 iff c_0>0` and `floor(A_L)=c_0`. For the first
claim, a positive integer zero count gives `A_L>=1>rM`; absence
gives `A_L<=rM`. For the second, PA3 gives `c_0<=A_L<c_0+1`.
For `L>=2`, the positivity budget is sharp over the mass-only integer
class: `c_0=1,c_1=M−1` has `A_L=1` and
`B_L=(1−rM)/(1−r)`. At `R=1/2,L=4,M=16` the lower certificate
is exactly zero despite one zero-grade witness.

### Noise and integer rounding

Suppose a real averaged report satisfies `|Ahat−A_L|<=E`. If the complex sample errors have bounds
`eta_j`, taking the real part of their average gives
`E<=(1/L)Σ eta_j`. The validated interval is

\[
\boxed{
\max\left(0,\frac{\widehat A-E-rM}{1-r}\right)
\le c_0\le\min(M,\widehat A+E).
}
\tag{PA6}
\]

Its width is at most `rM+2E`, since the lower endpoint is at least
`Ahat−E−rM`. Consequently `rM+2E<1` suffices for unique-integer
recovery from an authentic interval. It also ensures positivity of
the lower certificate for every allowed noise realization whenever
`c_0>=1`. Intersect with the integers; do not round the noisy center
by itself. Even a tiny downward error at a true integral `A_L` makes
`floor(Ahat)` wrong.

### Why this finite bank does not escape the fixed-bank obstruction

With exact mass `M=F(1)`, PA4 is the finite complex bank

\[
B_L=\frac1{L(1-r)}\sum_jF(z_j)-\frac r{1-r}F(1).
\tag{PA7}
\]

The node at positive real `1` has a negative coefficient. Its all-grade
response is

\[
q_L(h)=\frac{R^h\mathbf1_{L\mid h}-r}{1-r},
\]

which equals one at zero and is nonpositive at every positive integer
grade. This lies in the fixed complex-bank obstruction's class.
For the actual arithmetic source there is also a direct check: with
`L,R` fixed, `0<=A_L(n)<=F_n(R)` and prior FR01 gives
`Σ_(n<=X)F_n(R)=o(X²)`, whereas `Σ_(n<=X)(n−1)~X²/2`. Hence

\[
\sum_{n\le X}B_L(n)\sim-\frac r{2(1-r)}X^2.
\tag{PA8}
\]

The infinite angular projector is outside that fixed finite observation
class. Omitting the mass correction instead gives the positive aliases,
not a universal lower certificate.

## PA03: adaptive sampling cost and the unit-circle endpoint

At fixed `0<R<1`, choosing

\[
L>\frac{\log M}{\log(1/R)}
\]

ensures PA5, with the trivial zero-mass case handled separately. This
uses `O(log M)` phase samples for exact integer recovery. The previous
fixed-base geometric real-node filter has a sufficient
`O(sqrt(log M))` response count. These are channel counts in different
access models, not total running times or a universal optimality
comparison. Source acquisition, precision, and exact phase realization
are still paid obligations. Normalizing the histogram also rescales the
accuracy needed to resolve one witness.

At `R=1`, continuum PA1 remains exact and stable. Finite PA2 instead
has undamped aliases:

\[
A_L=\sum_{L\mid h}c_h.
\]

There is no mass-only decaying-tail budget as `L` varies uniformly over
all unbounded histograms. Indeed, the two sources `c_0=M` and `c_L=M`
have exactly the same values at **all** `L` sampled roots of unity.

An authenticated finite grade ceiling `H<L` changes the conclusion:
the only supported multiple of `L` is zero, so `A_L=c_0` exactly.
This is a finite norm-one average; sample errors average with no
coefficient amplification. For integral counts, an average-error
interval of width below one, for example `E<1/2`, identifies the count.

The genuine Goldbach grades have the a priori ceiling

\[
h_n(a)\le\left\lfloor\log_2(n^2)\right\rfloor-2=:H_n.
\tag{PA9}
\]

Indeed, `Ω(m)<=log_2 m` and
`(n+a)(n−a)<=n²`; the grade is an integer. Thus choosing `L>H_n`
at the unit circle gives an exact finite phase projection using
`O(log n)` points. The ceiling is established before measuring any
prime-pair count. Its use is support-informed and its sampling bank
depends on `n`; a fixed all-grade minorant hypothesis does not apply.
The executable controls retain only `L=4` roots in `Q(i)`; no irrational
root arithmetic is represented as exact code here.

### Frozen controls and their interpretation

The deterministic report checks four complex responses against the
surviving-grade average and the mass-corrected bank. It includes the
synthetic grade-four false witness, the strict positivity-budget
boundary, noisy-floor failure, indistinguishable unit-circle sources,
and a supported `H<4` positive control. At `n=67,263`, factorization
grades are also compared with direct trial primality, and both alias
and corrected bounds are checked exactly.

The standalone report was then executed successfully: **19 exact checks**
passed. Its two arithmetic calibrations returned:

| Midpoint | Four-phase average `A_4` | Corrected lower `B_4` | Direct zero count |
|---:|---:|---:|---:|
| 67 | `105/16` | `13/5` | 6 |
| 263 | `2227/128` | `131/120` | 15 |

Both corrected lower bounds certify positivity. Neither mass satisfies
`MR^4<1`, so the universal rounding guarantee is unavailable. At `n=263`,
the naive floor of the phase average is 17 while the actual count is 15:
positive aliases also occur in this genuine finite arithmetic source.

Reproduce the standalone controls from the repository root:

```sh
python research/2026-11-12/adaptive_boundary_resolution/phase_aperture.py
```

These are algebraic and finite arithmetic controls. Their shared source
code and pre-inspected midpoints do not constitute independent or blind
arithmetic validation. The full-circle theorem and finite alias proofs
establish the general statements; the report detects implementation
and convention errors. It is a classical access-model comparison, with
the pointwise source-acquisition obligation intact.
