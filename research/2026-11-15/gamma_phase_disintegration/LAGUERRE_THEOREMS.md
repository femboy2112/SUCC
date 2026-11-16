# GP-L — Gamma log phase, orthogonal modes, and reconstruction cost

**Status:** PROVED LOCAL (paper proofs; no formal-kernel or external referee claim).
All Gamma, Laguerre, hypergeometric and Hilbert-space ingredients are classical;
academic novelty of the assembly is unverified. See `PROVENANCE.md`,
`CLAIM_LEDGER.json`, and `VALIDATION.md`.

## 1. Scope and existing repository precedents

The concurrent atlas lineage #645, head
`895c0ae63af7b09548c608a1b0b6f298cea0e6d1`, was searched with `rg`.
It already contains:

- `research/2026-10-16/FACTORIAL_GAMMA_FUCC_SUCC.md`: moment determinacy,
  finite Gauss–Laguerre counterfeit sources and Gamma characteristic clocks.
- `research/2026-11-08/theta_extruded_interference/PROOFS.md`: generalized
  Laguerre/Pascal coefficients for completed theta/Cayley coordinates.
- `research/2026-11-15/pi_carrier_collision/THEOREMS.md`, PC-07: forgotten
  independent Gamma-clock attenuation, samplewise demodulation and inverse
  variance/statistical costs.
- The exact native source/Green Gamma(2) mixture and its
  Mellin factorization are already in `research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md`.

The searched files did not expose the particular orthogonal expansion of the
log-Gamma unit character with its exact modal energy, moment and tail laws below.
This is a scoped repository search, not a global novelty claim.

## 2. General shape theorem

Fix `a>0`. Let `mu_a(dt)=t^(a-1) exp(-t) dt/Gamma(a)` on `(0,infinity)` and
`H_a=L2(mu_a)`. Use the positive Fourier convention `exp(i*omega*log(t))`.
For `m>=0`, define

```
q_m(t)=sqrt(m!/(a)_m) L_m^(a-1)(t),
f_omega(t)=t^(i omega),
phi_a(omega)=Gamma(a+i omega)/Gamma(a).
```

The `q_m` form an orthonormal basis. Every `f_omega` has norm one. Its coefficients
(the inner product is linear in its first argument) are

```
c_m(omega)=<f_omega,q_m>
           =phi_a(omega) (-i omega)_m/sqrt(m! (a)_m).          (L1)
```

Consequently, in `H_a`,

```
f_omega=sum_(m>=0)c_m q_m,
sum_(m>=0)|c_m|^2=1,
c_0=phi_a(omega),
||f_omega-c_0||^2=1-|phi_a(omega)|^2.                       (L2)
```

Interpretation: the scalar normalized Gamma value is the constant-coordinate
projection of a unit vector. Its smaller modulus is explained exactly by the
orthogonal component discarded by that projection. The scalar alone does not
contain those coordinates. Retaining the complete coefficient sequence is an
isometric representation, not a mechanism that restores missing data for free.

### Proof of the coefficient formula

The finite polynomial formula is

```
L_m^(a-1)(t)=(a)_m/m! * sum_(j=0)^m (-m)_j t^j/((a)_j j!).
```

Integrate each of its finitely many terms against `t^(a+i omega-1) exp(-t)`.
The resulting terminating sum is

```
Gamma(a+i omega) (a)_m/m! * 2F1(-m,a+i omega;a;1)
=Gamma(a+i omega) (-i omega)_m/m!,
```

by Chu–Vandermonde. Divide by `Gamma(a)` and multiply by the normalization of
`q_m` to get (L1). There is no interchange of an infinite series with integration.

### Completeness without a moment-problem black box

If `g in H_a` is orthogonal to all polynomials, then
`F(z)=integral g(t) exp(z t) mu_a(dt)` is analytic for `Re z<1/2` by
Cauchy–Schwarz and the exponential Gamma tail. All its derivatives at zero
vanish. Analytic continuation on that half-plane yields `F(iu)=0` for real `u`.
Uniqueness of the Fourier transform of the finite complex measure `g mu_a`
(finite by Cauchy–Schwarz) gives `g=0` almost everywhere. Hence polynomials,
and therefore their orthonormal Laguerre basis, are complete. Parseval gives L2.

### A separate coefficient-sum verification

Set `p_m=|c_m|^2`. The power series has nonnegative coefficients:

```
sum p_m z^m=|phi_a(omega)|^2 * 2F1(-i omega,i omega;a;z).
```

Gauss's sum at 1 is applicable because `Re(a-(-i omega)-(i omega))=a>0`.
It gives exactly `sum p_m=1`. This also calibrates normalization independently
of an appeal to basis completeness.

## 3. Degree moments and finite projections

For integer `k>=1` and `a>k`, hypergeometric differentiation and Gauss's sum give

```
sum_(m>=0) m(m-1)...(m-k+1) p_m
  =|(-i omega)_k|^2 Gamma(a-k)/Gamma(a).                    (L3)
```

Indeed the k-th derivative of the hypergeometric power series multiplies it
by `(-i omega)_k(i omega)_k/(a)_k`; Gauss then has remaining gap `a-k>0`.
The limit as `z` increases to 1 is justified by monotone convergence of the
nonnegative coefficient series. In particular,

```
sum m p_m=omega^2/(a-1),                                  (L4)
```

when `a>1`. For `P_M` the projection onto degrees `0..M`,

```
||f_omega-P_M f_omega||^2=sum_(m>M)p_m
 <=min(1,omega^2/((a-1)(M+1))).                            (L5)
```

The L2 norm error is the square root of this bound. For any other unit-norm
test vector, its scalar reporting error is at most that norm error by
Cauchy–Schwarz. Do not confuse squared energy error with norm error.

For every fixed finite `M`, `sum_(m=0)^M p_m ->0` as `|omega|->infinity`.
This follows from Stirling's exponential decay of `phi_a` times a finite
polynomial in omega. No fixed finite rank retains all log-Fourier modes.

## 4. Native Gamma(2): sharp bounds and infinite second degree moment

Set `a=2`. Then

```
q_m=L_m^1/sqrt(m+1),
c_m=Gamma(2+i omega)(-i omega)_m/sqrt(m!(m+1)!),
sum p_m=1,
sum m p_m=omega^2.                                       (L6)
```

At `omega=0`, only `p_0=1` survives. For `omega!=0`, put
`C=omega^2(1+omega^2)`. For every `m>=1` the following identity is exact:

```
p_m=C/[m^2(m+1)] * |Gamma(m+i omega)/Gamma(m)|^2.           (L7)
```

Proof: use `(-i omega)_m=Gamma(m-i omega)/Gamma(-i omega)` and
`Gamma(2+i omega)=(1+i omega)i omega Gamma(i omega)`.
The square-modulus ratio of the two constant Gamma factors is `C`.
Also `m!(m+1)!=m^2(m+1) Gamma(m)^2`.

Since `Gamma(m+i omega)/Gamma(m)` is the characteristic function of
`log Gamma(m,1)`, its modulus is at most one. For any integer `M>=1`,

```
E_M=sum_(m>M)p_m
 <=min(1,omega^2/(M+1), C/[2M(M+1)]).                     (L8)
```

For the last bound use, for `m>=2`,

```
1/[m^2(m+1)] <= 1/[m(m-1)(m+1)]
 =1/2*(1/[(m-1)m]-1/[m(m+1)]),
```

and telescope from `m=M+1` to infinity.

A matching rational lower bound is

```
E_M >= C max(0,1-omega^2/M)/[2(M+1)(M+2)].               (L9)
```

Proof: the Gamma product is

```
|Gamma(m+i omega)/Gamma(m)|^2
 =prod_(j=m)^infinity (1+omega^2/j^2)^(-1)
 >=max(0,1-omega^2 sum_(j=m)^infinity j^(-2))
 >=max(0,1-omega^2/(m-1)).
```

The first inequality follows by multiplying `1/(1+x)>=1-x` or inducting
the stronger product inequality and passing to the limit. For `m>=M+1`
the last expression is at least `max(0,1-omega^2/M)`. Finally

```
1/[m^2(m+1)] >=1/[m(m+1)(m+2)]
 =1/2*(1/[m(m+1)]-1/[(m+1)(m+2)]).
```

Thus for every fixed nonzero real omega,

```
E_M ~ C/(2M^2),
p_m ~ C/m^3,
sum_(m<=M) m^2 p_m ~ C log M,
sum_(m>=0) m^2 p_m=infinity.                             (L10)
```

The first asymptotic follows directly by squeezing L8–L9, so no unproved
Gamma-ratio estimate is needed. For the term asymptotic use the same product
bounds in L7. The logarithmic second-moment divergence then follows by comparison
with the harmonic series. These are fixed-omega asymptotics, not joint-uniform
claims in `M` and omega.

The degree law therefore has finite mean but infinite variance whenever
`omega!=0`. This is the degree distribution of an orthogonal expansion;
it is not a distribution of physical particle energies.

## 5. Large-frequency degree law

Let `D_omega` be a formal integer random variable with probabilities `p_m` from
L6. As `|omega|->infinity`,

```
D_omega/omega^2 => V,
dP_V(y)=y^(-3) exp(-1/y) dy, y>0.                         (L11)
```

Thus `V` is inverse-Gamma with shape 2 and scale 1. This is an elementary
asymptotic consequence of L7, not a claim of academic novelty.

Proof: put `beta=omega^2` and take `m/beta` in a fixed compact subset of `(0,infinity)`.
Using `0<=x-log(1+x)<=x^2/2` for `x>=0`,

```
log |Gamma(m+i omega)/Gamma(m)|^2
 =-beta sum_(j=m)^infinity j^(-2)+O(beta^2 sum_(j=m)^infinity j^(-4))
 =-beta/m+O(beta/m^2+beta^2/m^3)
 =-1/(m/beta)+O(1/beta),
```

uniformly on such compacts. L7 now gives the local limit
`beta p_m -> y^(-3) exp(-1/y)`. Riemann sums converge on every compact
subinterval. The limiting density integrates to one (substitute `u=1/y`),
so those compact mass limits leave no escaping mass and yield weak convergence.
Alternatively the exact first moment gives upper tightness by Markov.
This proves a distributional quadratic scale, not a worst-case deterministic
degree bound.

For every fixed `L>0`, the exact captured-fraction limit is

```
sum_(m<=floor(L omega^2))p_m
 ->F_V(L)=(1+1/L) exp(-1/L).                             (L11b)
```

The distribution function follows by the substitution `u=1/y`; it is continuous
and strictly increasing from 0 to 1 on `(0,infinity)`. Therefore for any fixed
captured fraction `alpha in (0,1)`, define

```
M_alpha(omega)=min{M>=0:sum_(m<=M)p_m>=alpha}.
```

Then

```
M_alpha(omega)/omega^2 ->L_alpha,
(1+1/L_alpha) exp(-1/L_alpha)=alpha.                     (L11c)
```

To prove the quantile convergence, bracket `L_alpha` by two continuity points
whose limiting captured fractions straddle alpha, then apply L11b. This shows
quadratic degree is necessary and sufficient for any fixed nontrivial captured
fraction, in this particular basis and large-frequency regime. For a squared
energy tolerance eta in `(0,1)`, use `alpha=1-eta`; for an L2 norm tolerance
epsilon in `(0,1)`, use `alpha=1-epsilon^2`. These are different tolerances.
If `M(omega)/omega^2 ->0`, captured energy tends to zero. If that ratio tends
to infinity, the exact Markov bound in L8 gives captured energy tending to one.
No claim is made about other bases, adaptive nonlinear representations, the
computational complexity of the deterministic Gamma function, or the actual
circle phase's arithmetic access cost.

## 6. Source-labelled tensor extension

Use the inherited, rechecked native mixture with
`G~Gamma(2,1)` independent of the source label B under its specified tilted law,
and `Y=aG/(a+B)` with `a>0`, `a+B>0` almost surely. Define

```
v(B)=(a/(a+B))^(i omega),
F(B,G)=v(B)G^(i omega),
Psi=E v(B),
Phi=Gamma(2+i omega).
```

In the declared product Hilbert space,

```
F=(F-Phi v)+Phi(v-Psi)+Phi Psi.                           (L12)
```

These are pairwise orthogonal: the first term has conditional mean zero given
B; the second is B-measurable with mean zero; the third is constant.
All factors before averaging have modulus one. Consequently,

```
1=(1-|Phi|^2)+|Phi|^2(1-|Psi|^2)+|Phi Psi|^2.             (L13)
```

The first energy belongs to discarded Gamma modes; the second to discarded
source-label variation; the last is the fully compressed scalar coefficient.
This is an exact Pythagorean decomposition of two conditional projections.
It is not an entropy decomposition, a probability-of-truth statement, or
evidence of physical quantum entanglement.

The Gamma-coordinate truncation is

```
P_M^G F(B,G)=v(B) sum_(m=0)^M c_m q_m(G),
||F-P_M^G F||^2=E_M,
```

with the same sharp L8–L10 bounds, because `|v|=1`. Source labels are retained
exactly in this truncation. Forgetting those labels is an additional operation
whose error is not controlled merely by the Gamma degree bound.

This construction preserves the native *log-scale character*. No map from it
to the chronological real circle sequence `e(hU_n)` is supplied by L12–L13.
The original four-pole source determines B's law. The recurrence seed is
additional data, and no signed temporal Weyl estimate follows from this law alone.

If B's tilted law varies with chronological n, this construction is initially
a statement about each marginal. A cross-time Gram or interference assertion
requires an explicit joint law, for example a common underlying source measure
with declared reweighting and shared marks. Independent redraws at different
n define another joining and cannot silently replace the authentic one.

## 7. Scalar inverse cost and limits of the no-go

For `a>0`,

```
|phi_a(omega)|^2=prod_(k=0)^infinity (1+omega^2/(a+k)^2)^(-1)>0,
|phi_a(omega)|~sqrt(2pi)/Gamma(a) |omega|^(a-1/2) exp(-pi|omega|/2).
```

Convolution on logarithmic space by the log-Gamma density is injective on L2:
its Fourier multiplier is nonzero everywhere. Its inverse is unbounded, since
the multiplier tends to zero. On Fourier support `[-Omega,Omega]`, the exact
inverse norm is `|phi_a(Omega)|^(-1)`; monotonicity in absolute frequency follows
from the product. This is an exponential high-frequency inverse cost.

It is not proved that the actual BBP phase requires the choice
`omega=16^n`. That substitution is one possible encoding, not a universal
lower bound on every arithmetic algorithm. The real-circle harmonic h is
fixed while chronological n changes; the two frequency coordinates are distinct.

## 8. No random unit-phasor exact lift of a mean

If `|Z|<=1` almost surely and `E Z=c` with `|c|=1`, then

```
E|Z-c|^2=E|Z|^2-1<=0.
```

Hence `Z=c` almost surely. Therefore a genuinely random unit-phasor average
cannot exactly reconstruct the unit phase of a mean unless it was already
that constant phase samplewise. The complex Poisson source lift avoids this
obstruction because its random factors need not have modulus one.

For iid copies of real X with finite variance, a legal approximate many-copy
repair is

```
|(E exp(i theta X/M))^M-exp(i theta E X)|
 <=theta^2 Var(X)/(2M).
```

Center X, use `|exp(iu)-1-iu|<=u^2/2`, and telescope `a^M-1` for `|a|<=1`.
This is a limit theorem with an explicit approximation cost, not finite exact
recovery and not a new cancellation theorem for pi.

## 9. Scoped hostile endpoint models

The density `R_0(t)=1-t` has the same leading endpoint coefficient as authentic
`R(t)=(1-t)/((2-t^2)(t^2-2t+2))`. It has

```
T_n^0=1/((8n+1)(8n+2)), x_0=1/2,
(-1)^k Delta^k T_n^0 ~Gamma(k+2)/(64 n^(k+2))
```

for each fixed k, the same strict complete monotonicity/Hankel positivity, and
a legal coin realization. Its completed circle phase is identically one for
integer n>=1 and h. Thus the shared Gamma endpoint hierarchy does not force
normality.

More strongly, choose a nonnegative smooth unit-mass bump b supported in
`[c,d] subset (0,1)`. For a sufficiently close rational q>x, the perturbed
density `R_q=R+(q-x)b` remains in `[0,1]`, has integral q, and agrees exactly
with R near t=1. Every endpoint jet agrees. For all n>=0,

```
|T_n^q-T_n| <=(q-x)d^(8n).
```

Every fixed forward-difference face has the same bound because
`0<=(1-t^8)^k<=1`. All algebraic-order endpoint asymptotics therefore agree,
but q has a periodic or eventually periodic radix orbit. These mutants change
the forcing. They do not refute a theorem explicitly fixing the original
four poles and literal zero seed.

## 10. Primary sources and independent numerical checks

- DLMF 5.2.1: Euler Gamma integral and Gamma nonvanishing.
  https://dlmf.nist.gov/5.2
- DLMF 5.8.3: exact normalized Gamma modulus product.
  https://dlmf.nist.gov/5.8#E3
- DLMF 5.11.3: Stirling asymptotic with its sector condition.
  https://dlmf.nist.gov/5.11#E3
- DLMF Table 18.3.1: generalized Laguerre normalization/orthogonality.
  https://dlmf.nist.gov/18.3
- DLMF 18.5.12: finite Laguerre polynomial / terminating 1F1 expression.
  https://dlmf.nist.gov/18.5#E12
- DLMF 15.4.24: Chu–Vandermonde terminating sum.
  https://dlmf.nist.gov/15.4#E24
- DLMF 15.4.20: Gauss sum, valid for Re(c-a-b)>0.
  https://dlmf.nist.gov/15.4#E20
- DLMF 15.5.2: hypergeometric differentiation.
  https://dlmf.nist.gov/15.5#E2
- DLMF 18.8, Laguerre row: differential operator with eigenvalue m.
  https://dlmf.nist.gov/18.8

Numerical diagnostic (not interval certification) used 40-digit mpmath with
explicit finite polynomial coefficients and direct Gamma-weighted quadrature
for m=0..5 at (a,omega)=(2,1),(2,10),(3.5,0.7). Max formula/quadrature errors
were respectively 6.42e-42, 1.01e-43, 2.87e-42. A preliminary implementation
using mpmath's generic hypergeometric Laguerre evaluator failed to converge at
some quadrature nodes; replacing that evaluator with its finite polynomial
fixed the instrument. No failed run was counted as evidence.

The first 1001 modal weights summed to 0.9999990023, 0.9952821689,
0.9999999999748 respectively. Truncated means were 0.998003, 90.3980,
0.1959999646 versus exact 1,100,0.196. The slowly converging omega=10 degree
mean is consistent with the heavy-tail theorem and was not silently rounded
to the exact total.
