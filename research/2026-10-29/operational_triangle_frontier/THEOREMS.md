# Exact operational triangle: joint field/grade transform, Gamma specialization, and signed interface

**Status:** new-to-SUCC assembly of classical probability, special functions, and original-BBP-specific finite algebra. Paper derivations below; finite exact and numerical checks have separately scoped receipts. Original BBP signed recurrence and `U_0=0` are unchanged. No assertion of a quantum superposition, RH, normality or academic theorem priority.

## 0. Source and precise objects

Let, for every `a>0`,

`Q(x)=4-2 exp(-3x)-exp(-4x)-exp(-5x)>0` (`x>0`),

`R(a)=int_0^infty exp(-ax)Q(x)dx=4/a-2/(a+3)-1/(a+4)-1/(a+5)`.

The **same retained latent** `X~mu_a(dx)=exp(-ax)Q(x)dx/R(a)` is observed in `m` conditionally independent trials with failure `f(X)=exp(-8X)`, success `g(X)=1-f(X)`. The finite word `W=(W_1,...,W_m)∈{0,1}^m`, grade `J=sum W_i`, and selected deterministic BBP orbit are DIFFERENT types of object:

`a_n=8n-7`, `r(n)=R(a_n)`, `U_0(s)=s`, `U_n(s)=16U_(n-1)(s)+r(n)`. The authentic seed is `s=0`. None of the classical sensor's `W_i` are asserted to equal digits of π.

For every ordered word with `j` successes, define the **unnormalized posterior measure**

`M_(a,m,j)(dx)=binom(m,j) f(x)^(m-j) g(x)^j mu_a(dx)`.

This is the actual endpoint superposition over `binom(m,j)` histories; set `q_(a,m)(j)=M_(a,m,j)(whole space)` and `nu_(a,m,j)=M_(a,m,j)/q_(a,m)(j)`. Every finite mass is strictly positive for `0<=j<=m`; `sum_j M_(a,m,j)=mu_a`. A point means `(j,q_(a,m)(j),nu_(a,m,j))`, not only the integer grade.

## TG-01: exact measure-valued Pascal gluing and linear observer triangle

The full posterior measures satisfy, as identities of finite measures,

`M_(a,m+1,j) = f M_(a,m,j) + g M_(a,m,j-1)`

with the out-of-range measure zero. The integral of this identity gives the endpoint probability update; the sum over all grades is `mu_a` at every depth because `f+g=1`. For any bounded measurable `A(j,x)` the two paths (enumerate word histories, or first push forward to `(j,x)` then observe) agree exactly:

`sum_w int A(|w|,x) [product_i p_(w_i)(x)] mu_a(dx) = sum_j int A(j,x) M_(a,m,j)(dx)`.

If an observer depends on the **order** of bits, it is not an `A(j,x)` observer; the grade quotient is then an invalid replacement. If the observer is nonlinear, `A(E X)` and `E A(X)` are not generally equal. E.g. strict Jensen for `log` gives `log R(a+8)/R(a) + 8 E_mu_a X >0` for all `a>0`, since `f(X)` is nonconstant.

## TG-02: superposed endpoint is an exact sufficient statistic ONLY in this model

The joint density of a word `w` conditional on `X=x` depends on `w` only through `j=|w|`:

`P(W=w | X=x) = f(x)^(m-j)g(x)^j`.

Conditioning on `(J=j,X=x)` makes the full word uniform on the `binom(m,j)` admissible orders. Therefore `X ⟂ W | J`, and the mutual-information chain rule yields the **exact all-finite-depth identity**

`I(X;W)=I(X;J)`.

For this **latent-source question**, the superposed endpoint is sufficient. This does NOT mean the ordered history, source-seed pair or selected BBP carry is reconstructed from `j`. Replacing the posterior `nu_(a,m,j)` by the original prior `mu_a` destroys predictive sufficiency. Explicit source-only witness:

`P(00)-P(0)^2 = R(a+16)/R(a) - [R(a+8)/R(a)]² = Var_mu_a(f(X)) > 0`.

After observing `J=j`, prediction of a new failure is `E[f(X)|J=j]`. Its variation across grades is strictly positive for every `a>0,m>=1`. For the parity (or q=2 primitive/nonprimitive) quotient, at `m=2` the grades `j=0` and `j=2` are both even but have distinct posterior laws: their density ratio is proportional to `[f(x)/(1-f(x))]^2`, a strictly decreasing function of `x`. Thus `I(X;J | J mod 2)>0`: projecting to parity before updating has irrecoverable source information loss.

**Nonuniversal countermodel:** latent A/B with equal prior; two paths `LR` and `RL` reach the same grade 1 but have likelihoods `(3/8,1/8)` and `(1/8,3/8)` respectively under `(A,B)`. Their posterior probabilities of A are respectively `3/4` and `1/4`. This is realized by a two-step history-dependent sensor with first letter fair, and subsequent conditional letter probabilities `3/4` or `1/4` depending on the first letter and latent state. Consequently grade-1 superposition would lose information about X. This refutes *unqualified* sufficient-statistic and flatness claims in arbitrary SUCC spaces.

## TG-03: source-shift / posterior / observation are one exact joint transform

For `m>=0`, `a>0`, `0<=z<=1`, `t>=0` define

`F_(a,m)(z,t) = E_mu_a[e^(-taX) (z+(1-z)e^(-8X))^m]`.

It has **two exactly equal** finite representations:

```
F_(a,m)(z,t) = (1/R(a)) sum_(k=0)^m binom(m,k) z^(m-k)(1-z)^k R(a(1+t)+8k)
             = sum_(j=0)^m z^j int e^(-ta x) M_(a,m,j)(dx).
```

First equality: expand the binomial in `f=e^-8x` and integrate each term using R. Second: expand with `g=1-f` and group all words by grade, while retaining the latent posterior. Hence `F_(a,m)(1,t)=R(a(1+t))/R(a)` for **every** m, and `F_(a,m)(z,0)` is the endpoint PGF. The earlier exact harmonic observer is the integral

`E H_J = int_0^1 (1-F_(a,m)(z,0))/(1-z) dz`

(the value at z=1 is taken by continuity), equal to

`H_m - R(a)^(-1)sum_(k=1)^m R(a+8k)/k`.

The same finite expression equals a four-pole digamma difference with the true BBP offsets, inherited from #386. The additive Euler–Mascheroni reference cancels in each finite digamma difference; it does not create a separate finite update.

## TG-04: boundary-rank theorem and the spaces characterized by the author's triangle

More generally, suppose an admissible positive kernel has `Q(x)~c x^(r-1)` as `x downarrow 0`, with `c>0`, `r>0`, sufficient Laplace integrability, and the required locally uniform domination/regular-variation estimates. Then `R(a)~c Gamma(r)/a^r`, hence `Y_a=aX_a ⇒ Gamma(r,1)` by the Laplace continuity theorem. If observation depths `m(a)` satisfy `8m(a)/a→theta>0`, conditionally `J|Y_a` tends to `Poisson(theta Y)`. Joint transforms converge for `0<=z<=1, t>=0`:

`F_(a,m(a))(z,t) → F_(r,theta)(z,t) = [1+t+theta(1-z)]^(-r)`.

Proof: given `Y_a=y`, `g(X_a)=1-exp(-8y/a)=8y/a+O_y(a^-2)` and `(z+(1-z)e^(-8y/a))^m → exp(-theta(1-z)y)`. Bounded convergence after weak convergence/tightness (or a standard Skorokhod coupling) gives the joint limit. The Gamma Laplace integral is exact.

For native original four-pole Q, `Q(x)=15x-(59/2)x²+O(x³)` so `r=2`; with `a_n=8n-7,m=n`, `theta=1`. Hence

`F_n(z,t) → (2+t-z)^(-2)`, `G_2(z)=F_infty(z,0)=(2-z)^(-2)`.

If **separately** used as an offspring PGF, `G_(r,theta)(z)=[1+theta(1-z)]^(-r)` has mean `r theta` and positive mass at zero. It is strictly convex on [0,1]; the smallest fixed point `q` obeys `q<1` **iff** `r theta>1`, and is then attracting (the supercritical Galton–Watson extinction root). Otherwise the only fixed point is `q=1`. At `(r,theta)=(2,1)`, the polynomial factors as

`q(2-q)^2-1=(q-1)(q²-3q+1)`;

therefore the unique interior root is `q=phi^(-2)=lambda²=(3-sqrt5)/2`, and `1-q=lambda=phi^(-1)`. Its derivative is `2/(2-q)^3=2 lambda³<1`. With `Y~Gamma(2,1)`,

`E log Y=psi(2)=1-gamma`, `E exp(-lambda Y)=(1+lambda)^(-2)=lambda²`;

therefore `Omega_OM=lambda-gamma`. **The author's triangle is recovered from the operational triangle under declared rank, scaling, and observer assumptions**, rather than imposed as three algebraically independent primary vertices. For general supercritical `(r,theta)` define `q_(r,theta)` as above and the **self-consistent** contrast

`D_self(r,theta)=psi(r)-q_(r,theta)`;

it is generated by the Gamma log observable and the Laplace probe at rate `theta(1-q)`. At `(2,1)` this specializes exactly to Oily–Macaroni. This differs from the **fixed-golden** rank family `D_lambda(r)=psi(r)-lambda^r` inherited from #369; the two families agree at rank 2, but no generic equality is asserted. This is a testable distinction between genuine emergence and artificially holding a golden mark fixed across unrelated ranks.

**Independent models WARNING:** the inherited two-stage Oily packet law and the present Gamma–Poisson sensor have identical **grade marginal** `G_2`, but not automatically the same joint latent coupling. The displayed `F_(r,theta)` belongs to the declared Pascal observation sensor, not any other matching packet model.

## TG-05: two-variable first finite original-four-pole defect, with exact fake control

For the authentic native diagonal `a_n=8n-7,m=n`, write `F_n(z,t)=F_(a_n,n)(z,t)` and `d=2+t-z`. Uniformly on any fixed compact rectangle `0<=z<=1,0<=t<=T`,

```
F_n(z,t)=d^(-2)+J_BBP(z,t)/n+O_T(n^(-2)),
J_BBP(z,t)=[59 t² +92tz -33t -511z² +813z -302]/[120d^4].
```

The derivation is a direct **joint source/observer expansion**, not a fitted coefficient. With `Y=a_nX`, the scaled original source density is

`y exp(-y) [1+(59/(240n))(2-y)+O(n^-2 P(y))]`.

For `b=z-1`, the sensor's binomial factor is

`[z+(1-z)e^(-8y/a_n)]^n = exp(by){1+(1/n)[b(7y/8-y²/2)-b² y²/2]+O(n^-2 P(y))}`.

Multiply, include `exp(-ty)`, and use the exactly computable Gamma integrals `int_0^infty y^k exp(-dy)dy=k!/d^(k+1)`. The first coefficient is

`(59/240)(2/d²-2/d³) + (7b/4)/d³ - 3(b+b²)/d⁴ = J_BBP`.

A rigorous uniform-remainder route: split at `y=n^(1/3)`; on the lower range, the Taylor remainders are bounded by `C_T n^-2 P(y)` times an integrable exponential; on the complement, positivity plus `Q(x)<=15x` and bounded `0<=z<=1,t>=0` give an `O(exp(-n^(1/3)/2))` tail. The displayed finite polynomial and first derivative remainder are thus controlled for fixed T. We do **not** claim formal Lean verification or independent universal error constants.

**Gamma-matched fake** `Q_fake(x)=15x`, `R_fake(a)=15/a²` has precisely the same limiting F. Repeating the calculation with its source density exactly `y exp(-y)` gives

```
J_fake(z,t)=7(z-1)/[4d³]-3z(z-1)/d⁴,
J_BBP(z,t)-J_fake(z,t)=59(1+t-z)/[120d³].
```

This is **nonzero** whenever `1+t-z>0`, a genuine source-visible joint readout absent at `(z,t)=(1,0)` by mass conservation. Setting `t=0`, integrating the difference divided by `(1-z)` recovers the original-vs-fake harmonic first-jet `-59/(320n)` from #386. At `(z,t)=(0,0)`, `J_BBP=-151/960` (inherited zero-grade first jet). The hostile `Q_epsilon=Q+epsilon(1-e^-x)^3` preserves `Q'(0), Q''(0)` and therefore matches this FIRST jet; higher joint derivatives or source poles are needed to identify the whole source. This does not constrain π's signed phase.

## TG-06: exact selected-frequency tomography and its universal seed-smearing no-go

Keep the original **deterministic** `U_n(s)` and positive endpoint mass `q_(a_n,m)(j)`. For integer `h!=0`, real central seed `s`, auxiliary displacement `u∈[0,1]`, define

```
H_(n,m,h)(u;s)=sum_(j=0)^m q_(a_n,m)(j)
    exp(2pi i h U_(n+j)(s+u/16^n)).
```

The affine recurrence gives `U_(n+j)(s+u/16^n)=U_(n+j)(s)+16^j u`. Therefore **without any approximations**,

`H(u;s)=sum_j q_j exp(2pi i h U_(n+j)(s)) exp(2pi i h16^j u)`.

Every integer frequency `h16^j` is distinct. Exact Fourier orthogonality thus yields

`int_0^1 H(u;s) exp(-2pi i h16^k u)du=q_(a_n,m)(k)exp(2pi i h U_(n+k)(s))`.

All `q_j>0`, so all finite **complex selected phase marks** can be recovered after dividing by their exact masses. The variance/conditioning warning is quantitative: if an instrument sees `H` with an `L²([0,1])` error of size <=epsilon, then each recovered weighted Fourier coefficient has absolute error <=epsilon (Cauchy-Schwarz), but normalized phase error can be as large as `epsilon/q_j`. For moving grades with small `q_j`, stable recovery requires correspondingly better precision. Literal carry `kappa_(n+j)` remains extra integer-lift information; it cannot be recovered from its exponentiated character alone.

**Crucial universal no-go:** `int_0^1 H(u;s)du=0` for EVERY seed `s`, including the coherent same-forcing `s*=-pi/16` with `U_n(s*)=-T_n→0` and phase mean →1. Thus *virtual seed averaging* can produce perfect cancellation when the selected deterministic orbit is nonnormal. Recovering the phases is a **representation/observability theorem**, not a Weyl estimate.

The original literal carry is `kappa_n(s)=16{U_(n-1)(s)}+r(n)-{U_n(s)}∈Z`; composition `kappa_n^(2)=16 kappa_n+kappa_(n+1)` is inherited from #386. Keep these lift integers as full marks alongside grades and phases in any q=3/6/16 observer. Exponentiation and parity reduction before attaching them are not justified.

## TG-07: precise next proof lamp (signed boundary)

The weighted phase `H(u;s)` exposes the selected phases, but its reconstruction is exact for every seed and does not by itself diminish `|(1/N) sum e(hU_n(0))|`. Any proposed new source/carry estimate must (i) use **all four original signed poles** with `U_0=0`, (ii) retain selected integer branch information and full sixteen digit/Walsh sectors, (iii) predict a genuine intertime signed gain not obtainable by applying an invertible positive filter, (iv) FAIL under `s*=-pi/16` and appropriate changed poles, Gamma-matched `Q_fake`, parity/totient projection and fake conditional-iid resetting, and (v) use a fresh independent holdout instead of fitting and validating on the same finite BBP prefixes. Kepler III #384 supplies moving-grade/shrinking-target resolution cost, not the missing cancellation. These conditions are **open proof obligations**, not a theorem that π is normal or that the claimed mechanism exists.

## Primary/classical dependencies and status

- Original Bailey–Borwein–Plouffe rational radix-16 source: Bailey, Borwein, Plouffe, *On the rapid computation of various polylogarithmic constants*, Math. Comp. 66 (1997), 903–913; NASA source https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19970009337.pdf .
- Digamma recursion, Gamma integral: NIST DLMF §5.5 https://dlmf.nist.gov/5.5 ; earlier SUCC #369/#386 already contains the finite harmonic/Gamma bridge.
- Branching extinction is the least fixed point of an offspring PGF: classical Galton–Watson theorem; here the branching process is separately **declared**, not an extra physical source claim.
- Existing four-pole positive-source atomic/convolution laws: #367; original finite sensor and q_j bounds: #370; Gamma rank/Oily provenance: #368/#369; exact finite triangle: #386; Kepler III frequency resolution: #384; exceptional-prime/complete-alphabet comparison: #385.

**Verdict:** structural finite laws PROVED LOCAL (paper and exact tests), joint first jet PROVED LOCAL with independent symbolic/numerical checks, generalized Gamma class CLASSICAL under explicit regularity, Oily/rank-two SPECIALIZATION, selected π normality and source-selected signed Weyl saving OPEN / UNVERIFIED. High-precision numerical agreement and multiple same-model tests are not independent universal proof authorities.
