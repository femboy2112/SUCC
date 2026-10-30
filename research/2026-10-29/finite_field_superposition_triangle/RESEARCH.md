# SUCC — Primitive finite-field ↔ superposition-point triangle: original BBP, harmonic readout, and first-source jet

**Research-only, 2026-10-29.** Exact parent: draft [#383](https://github.com/femboy2112/SUCC/pull/383) at `e02933591e7b7486376acb9847e00fd01d9ae498`, through #381/#379/#373/#367. Read-only independent siblings: #368 (Oily order-statistic and Gamma/Poisson coupling), #369 (harmonic/Gamma ranks), #370 (original Pascal sensor), #376 (q6 rank/carry), #382 (orthogonal literal carry). No sibling code is silently merged. Main, original four signed poles, the selected initial state `U_0=0`, historical source archives and theorem IDs are unchanged. This is new-to-program assembly of classical conditional probability and exact original-source identities, **not** a claim of academic priority. π base-16 normality and RH remain OPEN.

## The corrected primitive vertices

The three constants `H_m`, `gamma`, `lambda=phi^(-1)` are not three independent generators. `gamma=lim(H_m-log m)` is a finite-part reference of the harmonic process. `lambda` is selected only after declaring the *two-stage* endpoint packet generating function. In particular `Omega=lambda-gamma` is a **rank-two marked readout**, not an independently imposed equation on π's digits.

The more primitive, operational triangle is:

1. **Finite history and field update.** An actual source `mu_a` and a sequence of likelihood multiplications (one per recorded outcome).
2. **Superposed endpoint.** Sum the weights of all histories reaching the same finite grade `j`, retaining the *posterior carrier* as part of the endpoint.
3. **Observer/selected point.** Apply harmonic, Mellin, Laplace, phase and/or literal-carry readouts, explicitly declaring whether a nonlinear observer is before or after the sum.

A point here means a **coarse endpoint of a specified classical path-sum model**, not a coherent quantum state. Complex phase marks below are explicitly defined arithmetic characters, not a physical measurement device.

## 1. Exact original four-pole source and truthful state separation

For `a>0`, let

```text
Q(x) = 4 - 2 exp(-3x) - exp(-4x) - exp(-5x) > 0   (x>0)
R(a) = ∫_0∞ exp(-ax) Q(x) dx
     = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5)
     = (15a²+121a+240) / [a(a+3)(a+4)(a+5)]
mu_a(dx) = exp(-ax) Q(x) dx / R(a)
a_n = 8n-7,     r(n)=R(a_n)
U_0(s)=s,       U_n(s)=16U_(n-1)(s)+r(n).
```

The continuous `a` is a source-tilt parameter; the discrete `n` is the actual arithmetic clock; `m` below counts declared auxiliary observations; `j` is the endpoint grade; `s=0` is the authentic deterministic BBP seed. None of these indices is interchangeable by notation.

The original source-tilt law is exact:

```text
Z_a = E_mu_a exp(-8X) = R(a+8)/R(a)
(exp(-8x) mu_a(dx))/Z_a = mu_(a+8)(dx).
```

This is a source-relative update, not a random generator of π digits.

## 2. Literal finite triangular sheet, posteriors and superposition

Keep one latent `X~mu_a` throughout a length-`m` observation word. Conditional on `X=x`, trials are independent with **failure** likelihood `f(x)=exp(-8x)` and **success** likelihood `g(x)=1-exp(-8x)`. For a word with `j` successes and `m-j` failures, its integrated probability is

```text
c_(a,m,j) = E_mu_a [(1-exp(-8X))^j exp(-8X(m-j))]
          = [Σ_(k=0)^j (-1)^k C(j,k) R(a+8(m-j+k))] / R(a).
```

Set `c=0` outside `0<=j<=m`. Words with the same grade have the same likelihood, so their **superposed endpoint mass** is precisely

```text
q_(a,m)(j)=C(m,j)c_(a,m,j),  Σ_(j=0)^m q_(a,m)(j)=1.
```

The endpoint **posterior field** is the measure proportional to
`(1-exp(-8x))^j exp(-8x(m-j)) mu_a(dx)`, normalized by `c_(a,m,j)`.
The current predictive likelihoods for one more failure/success are

```text
F_(a,m,j)=c_(a,m+1,j)/c_(a,m,j)
S_(a,m,j)=c_(a,m+1,j+1)/c_(a,m,j),   F+S=1.
```

Consequently the finite triangle obeys the exact Markov conservation law

```text
q_(a,m+1)(j) = q_(a,m)(j) F_(a,m,j)
             + q_(a,m)(j-1) S_(a,m,j-1).
```

All displayed finite values are rational at rational `a>0`. The whole posterior (not merely `j` under an unspecified rule) ensures that the next update uses the field left by the preceding update.

**Flat commutation with the full posterior:** the likelihood multipliers `f` and `g` commute. Thus the route `fail -> success` and the route `success -> fail` have the identical `c_(a,2,1)` and posterior; their local log path-odds curvature is zero. This is a **proved absence of order curvature**, not a flaw to fill by imagining physical interaction. Nonlinear selected/carry readouts below need not commute with averaging even though these positive likelihood updates do.

### Exact cross-source transport identity

Define `q_(a,m)(j)=0` beyond its allowed grade range. The generating polynomial is

```text
G_(a,m)(z)=E_mu_a [z+(1-z)exp(-8X)]^m.
```

Since `exp(-8x)mu_a=Z_a mu_(a+8)` and
`[z+(1-z)f]^(m+1)=z[z+(1-z)f]^m+(1-z)f[z+(1-z)f]^m`,

```text
G_(a,m+1)(z)=z G_(a,m)(z)+(1-z) Z_a G_(a+8,m)(z).
```

**Coefficient identity (FFT-1):**

```text
q_(a,m+1)(j) = q_(a,m)(j-1)
             + Z_a [q_(a+8,m)(j)-q_(a+8,m)(j-1)].
```

This is an **exact finite field-update ↔ path-sum point** commuting identity. At `a=a_n`, the source normalization is `Z_a=r(n+1)/r(n)`, so the shift is along the *native* BBP clock. It is not an arbitrary fitted Gamma approximation.

## 3. A new exact harmonic observer directly expressed through original BBP forcing

Let `H_0=0` and `H_j=Σ_(k=1)^j 1/k`. Write

```text
A_(a,m)=Σ_(j=0)^m q_(a,m)(j)H_j = E[H_J].
```

For fixed `X=x`, `J|X~Binomial(m,1-exp(-8x))`. The elementary harmonic-binomial identity gives
`E[H_J|X=x]=H_m-Σ_(k=1)^m exp(-8kx)/k`. Taking the **original** source expectation yields:

**Exact harmonic superposition theorem (FFT-2):**

```text
A_(a,m) = H_m - [1/R(a)] Σ_(k=1)^m R(a+8k)/k.
A_(a,m+1)-A_(a,m) = [1-R(a+8(m+1))/R(a)]/(m+1).
```

Every one of these is exact for all `a>0` and finite `m>=0`. The second line exposes a local *harmonic update* whose correction is the **entire composed source-tilt cocycle**, not an externally imposed `gamma`.

The native BBP diagonal `a=a_n,m=n` gives the especially concrete formula

```text
A_n := A_(8n-7,n)
     = H_n - (1/r(n)) Σ_(k=1)^n r(n+k)/k.
```

Thus the same object is obtained by (A) assigning genuine BBP-based weights to a finite Pascal triangle and measuring `H_j`, or (B) summing a **finite shifted-BBP forcing convolution**. This is the mathematically load-bearing triangle intended here.

The update identity is **for fixed `a`**: do not silently substitute the diagonal `a_n` into both sides while simultaneously advancing `n`.


### The exact four-pole **digamma dilation** bridge (FFT-2b)

The finite identity above is already a statement about the logarithmic derivative of **Gamma**, with no limit needed. Write the authentic four source shifts and signed coefficients as

```text
(d,c_d) = (0,4), (3,-2), (4,-1), (5,-1)
beta_d = (a+d)/8.
```

The partial fraction identity
`1/[k(a+d+8k)]=(1/(a+d))[1/k-1/(k+beta_d)]`,
together with `R(a)=Σ_d c_d/(a+d)`, gives

```text
A_(a,m) = (1/R(a)) Σ_d [c_d/(a+d)]
           [psi(m+1+beta_d) - psi(1+beta_d)].
```

Here `psi(z)=Gamma'(z)/Gamma(z)`, and the digamma difference equals the **finite rational sum**
`Σ_(k=1)^m 1/(k+beta_d)` by the classical recurrence. Thus the Euler–Mascheroni additive reference is **absent from the finite update**: each digamma difference cancels its common reference identically. Introducing `gamma` as a separate vertex or edge here would double-count it.

For the native BBP diagonal `a=8n-7,m=n`, put `delta∈{1,4,5,6}`, `b_delta=delta/8` and `c_delta=(4,-2,-1,-1)`. Then

```text
A_n = [1/(8r(n))] Σ_(delta=1,4,5,6)
       [c_delta/(n-1+delta/8)]
       [psi(2n+delta/8)-psi(n+delta/8)].
```

**This is an exact Gamma/digamma expression using the four *original* BBP offsets** `1,4,5,6` over 8. The doubling `n→2n` is produced by the **declared matched Pascal observation depth**, not assumed from the base-16 digit map. It is a mathematically real dyadic dilation inside the BBP source, but no theorem yet identifies that dilation with four-bit digit equidistribution. Every term can be checked as a rational finite sum; a second exact Fraction implementation matches both earlier routes for native clocks and multiple observation depths.

### Reset-the-field negative control (strict and exact)

If one averages `X` first and then incorrectly reuses that same average failure probability at each step, one obtains `[R(a+8)/R(a)]^2` for two failures. The genuine retained-field result is `R(a+16)/R(a)`. Since `log R` is strictly convex (`(\log R)''=Var_mu_a X>0`),

```text
R(a+16)/R(a) > [R(a+8)/R(a)]²   for every a>0.
```

At `a=1` these are respectively `829/61523` and `280900/164634561`; their difference is exactly `362310761/30786662907>0`. **Resetting the finite field breaks the triangle**. This is the finite distinction between superposing actual histories and averaging away the source microstate before updating.

## 4. The limiting Gamma/golden/harmonic constants are derived readouts

At native `a_n=8n-7`, the scaled microstate `Y_n=a_nX_n` converges in law to `Gamma(2,rate=1)`. Conditionally, the `n` Bernoulli trials converge to `J|Y~Poisson(Y)`, hence their **joint** limiting law is Gamma–Poisson and the marginal generating function is

```text
G(z)=E[z^J]=E[exp((z-1)Y)]=(2-z)^(-2).
P(J=j)=w_j=(j+1)/2^(j+2), j>=0.
```

This *marginal* matches the inherited two-geometric Oily endpoint PGF. **Do not identify latent variables or joint couplings merely from the common marginal**: the independent-packet model of #368 has a different joint log/grade transform. The present Gamma–Poisson model is the declared original-source Pascal observer of #370 and has its own valid joint.

The unique interior fixed point of `G(p)=p` is `p_*=lambda²`, with `lambda=(sqrt(5)-1)/2`. It is selected by the **two-stage generating law**, not by a free-standing golden axiom. The harmonic endpoint readout is

```text
lim_(n→∞) A_n = Σ_(j>=0) w_j H_j = 1/2 + log 2.
```

Proof: integrate `[1-G(z)]/(1-z)=(3-z)/(2-z)^2` over `0<=z<=1`; tight exponential grade tails justify exchanging limit and the unbounded but logarithmic `H_j`.

Separately, the original positive carrier is Gamma rank two in the source-scale limit. For `Y_r~Gamma(r,1)`,

```text
D(r)=E log Y_r - E exp(-lambda Y_r)
    = psi(r) - lambda^r
    = H_(r-1) - gamma - lambda^r  (positive integer r).
D(2)=lambda-gamma=Omega_OM,
D(r+1)-D(r)=1/r+lambda^(r+2).
```

**The primal objects are the path law, its update algebra, and the observer maps.** `gamma` is a common renormalized logarithmic reference, harmonic numbers are discrete digamma values, and `lambda` is a marked PGF fixed point; `Omega_OM` is one marked evaluation, *not* a structural axiom.

### One more constant from the same triangle (FFT-3)

Under the **declared Gamma–Poisson joint**, `Y|J=j~Gamma(j+2, rate=2)`. Therefore `2Y|J=j~Gamma(j+2,1)`, and the *grade-conditioned rank readout* yields

```text
E[D(J+2)] = E[log(2Y)-exp(-2 lambda Y)]
          = 1+log 2-gamma-(1+2 lambda)^(-2)
          = 1+log 2-gamma-lambda²/(2-lambda)².
```

This is a second, different legitimate harmonic/golden/Euler constant in the *same* operational triangle. It is not `Omega_OM` and does not need to be. Every choice of admissible source-attached observable provides a different coordinate; primitive nodes must not be inferred from whichever constants appear after measuring.

## 5. First authentic BBP source fingerprint: a new harmonic 59-jet

The original source is not merely Gamma-shaped. Its exact endpoint jet is

```text
Q(x)=15x-(59/2)x²+O(x³),
R(a)=15a^(-2)-59a^(-3)+O(a^(-4)).
```

At `a_n=8n-7`, expand the normalized density of `Y_n=a_nX_n` and the conditional binomial PGF (real `0<=z<=1`). Uniform integrable Taylor expansion gives

```text
G_n(z)=G_(a_n,n)(z)
      =(2-z)^(-2)
       +(1-z)(511z-302)/[120n(2-z)^4]+O(n^(-2)).
```

For clarity, the density contribution at order `1/n` is `(59/240)(2-y)y exp(-y)`; the conditional-binomial exponent contribution is
`(z-1)(7y/8-y²/2)-(z-1)²y²/2`, against the leading `y exp(-(2-z)y)`. Their exactly integrated sum is the rational first-jet shown above. A region split at `y=n^(1/3)` bounds the polynomial Taylor remainder in the lower region and the exponentially suppressed upper region; differentiating once in `z` controls the removable `(1-z)` divisor needed for the harmonic integral. All constants are finite on `0<=z<=1`.

At `z=0`, the expansion recovers the already-known #370 original finite source witness
`q_n(0)=1/4-151/(960n)+O(n^(-2))`. Integrating the *whole* PGF rather than selecting only `j=0` gives the new harmonic result:

```text
A_n = 1/2+log 2 - 49/(320n)+O(n^(-2)).
```

**Gamma-matched adversary.** Replace only the positive source by `Q_fake(x)=15x`, so `R_fake(a)=15/a²`, keeping the *same native clock* and the *same conditional Bernoulli sensor*. Its limiting `Gamma(2)` and `G(z)` are identical, but its harmonic coefficient is

```text
A_n(fake)=1/2+log 2+1/(32n)+O(n^(-2)).
A_n(original)-A_n(fake)= -59/(320n)+O(n^(-2)).
```

The difference is exactly the authentic `Q''(0)=-59` contribution. An independent SymPy oracle reconstructs the rational PGF correction and integrates it exactly; an exact-Fraction native recurrence plus numerical asymptotic holdouts test the finite expression. These are paper-level derivation and reproducible finite receipts, **not a Lean or interval-uniform certificate**.

The two distinct first jets show why `Omega_OM` or a universal Gamma limit cannot alone authenticate π. Source-specific *finite defects*, attached to correctly labeled observations, are the right objects to preserve.

## 6. The selected BBP point, frequency transport and literal carry: the missing boundary

For the genuine deterministic orbit, define `x_n(s)={U_n(s)}` and

```text
kappa_n(s) = floor(16x_(n-1)(s)+r(n)),
U_(n+j)(s)=16^j U_n(s)+Σ_(ell=1)^j 16^(j-ell) r(n+ell).
```

The selected initial value is exactly `s=0`. Do not confuse a source-sampled random `J` with a digit of π. We can legitimately **mark** each source-superposed endpoint with its deterministic phase, however:

```text
Xi_(n,h)(z;s) = Σ_(j=0)^n q_(a_n,n)(j) z^j exp(2πih U_(n+j)(s)),
h integer nonzero.
```

This is a rigorously specified finite **source-conditioned, selected-point transfer**. Every coefficient `q` is exact rational and original-four-pole; the phase keeps the actual seed and the transported frequencies `16^j h`. For full carry tomography retain

```text
Xi_(n,h,c)(z;s)=Σ_j q_(a_n,n)(j) z^j
                 1_[kappa_(n+j)(s)=c] exp(2πih U_(n+j)(s)).
```

The binomial endpoint sum is classical superposition; the selected circle phase/carry is an *additional* mark. Averaging before applying nonlinear floor loses branch information. The authentic clock map obeys
`exp(2πih U_(n+1))=exp(2πih r(n+1))exp(2πi(16h)U_n)`: **frequency scales by 16**, so one must not model the process as a stationary fixed-frequency Markov character.


### Exact two-step carry-composition triangle (FFT-C)

For any real seed s and integer n>=1, the ordinary circle representative satisfies
`16 x_(n-1)(s)+r(n)=kappa_n(s)+x_n(s)`. Composing this **actual deterministic update twice**, without discarding the intermediate branch integer, yields

```text
256 x_(n-1)(s)+16r(n)+r(n+1)
  = 16 kappa_n(s)+kappa_(n+1)(s)+x_(n+1)(s)
```

and hence the exact two-step branch law

```text
kappa^(2)_n(s) = floor(256x_(n-1)(s)+16r(n)+r(n+1))
               = 16 kappa_n(s) + kappa_(n+1)(s).
```

This is an elementary but **load-bearing typed carry cocycle**: the composed finite field update and the final circle point agree only after transporting the intervening integer with the correct radix factor. Exponentiating a character forgets this integer, so the lifted trajectory retains strictly more information than its phase quotient. This is not a claim of antisymmetric holonomy, physical gauge curvature, or digit equidistribution. Exact rational tests preserve all three original objects `(grade weight, selected fractional point, literal carry)` for seeds `0`, `1/7`, `-1/5`, and `13/16`, including the composition law.

The **gluing gap** is now exact: the Bayesian triangle supplies `q_(a_n,n)(j)`; the arithmetic triangle supplies `(x_(n+j)(0),kappa_(n+j)(0))`. Their joint marked tensor is a valid, source-typed *observation definition*, but a causal theorem forcing **signed long-time cancellation** of its selected phases has not been derived.

**Hostile coherent counterseed:** `s_*=-π/16` has the identical source, weights, update triangle and finite 59-jet, but `U_n(s_*)=-T_n`, `T_n→0`, and therefore `Xi_(n,h)(1;s_*)→1`. The triangle is **not itself a π-normality theorem**. Any signed-cancellation claim derived from just its positive sector is refuted by this exact same-forcing control. Main unknown: a source- and zero-seed-sensitive estimate on the *common-mode*, literal-carry-resolved signed point transfer that remains noncircular under this counterseed and a four-pole mutant.

## Verdict and provenance

- **PROVED LOCAL (paper plus exact finite tests):** posterior-conserving finite triangular path sums; native source-shift recursion FFT-1; exact harmonic readout FFT-2; strict failure of resetting the latent field.
- **CLASSICAL with specified joint model:** Gamma–Poisson rank-two limit; golden PGF fixed point; digamma/harmonic finite part; derived second rank constant FFT-3.
- **PROVED LOCAL (analytic expansion, independent exact symbolic oracle, numerical holdouts):** authentic harmonic `-49/320` and fake `+1/32` first jets. Global paper-level remainder argument supplied; no formal proof kernel.
- **UNVERIFIED/OPEN:** source-to-actual-digit causal identification; zero-seed-sensitive common-mode signed saving; π normality and RH; physical quantum interpretation or a universal irreducible triangular geometry.

Primary identities: [BBP 1997 original author paper](https://www.davidhbailey.com/dhbpapers/digits.pdf), [NIST DLMF gamma/digamma recurrence §5.5](https://dlmf.nist.gov/5.5), [DLMF integer digamma values §5.4](https://dlmf.nist.gov/5.4). Local lineage: #367, #368, #369, #370, #376, #379, #381, #382, #383. All references to earlier results retain their original scope and proof status.
