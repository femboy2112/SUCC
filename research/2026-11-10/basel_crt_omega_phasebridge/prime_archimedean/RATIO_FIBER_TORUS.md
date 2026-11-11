# Prime-phase tomography inside the half-to-double ratio interval

**Research date:** 2026-11-10. **Status:** exact elementary identities, finite executable probes, an elementary almost-everywhere theorem, and unproved source-selected cancellation. **Lineage:** this is a continuation of the completed Weil wavepacket and original-zero BBP source investigation in this directory, stacked above SUCC draft #585, itself above integration #584. The original four-pole BBP forcing, literal `U_0=0`, imported archives, existing formal source contracts, and main are unchanged.

## I. Steelman: a bounded real window can conceal every finite prime coordinate

For an integer `A>=2`, let `I_A={A,...,2A-1}` and define `R_A={(n/m):n,m in I_A}`. The real ratios satisfy

```math
1/2<n/m<2,\qquad |\log(n/m)|<\log 2.
```

The interval has ordinary additive length `3/2`; its natural **multiplicative** logarithmic support `(-log 2,+log 2)` spans two octaves. For a rational `r=n/m`, unique factorization and the rational product formula yield

```math
\boxed{\log r=\sum_p\big(v_p(n)-v_p(m)\big)\log p,\quad
 |r|_\infty\prod_p|r|_p=1.}\tag{PF}
```

Every prime `p<2A` is visible as a nonzero valuation of **some** ratio in `R_A`. Indeed, if `p<=A` there is a multiple of `p` in the `A` consecutive integers of `I_A`, and also an integer not divisible by `p`; if `A<p<2A`, use `n=p` and any other `m` in `I_A`. Conversely, no integer in the band has a prime factor `p>=2A`. This is **not** a claim that every prime phase is a direct Weil prime-power argument: there are no prime powers strictly inside the ratio interval.

Define the **prime–Archimedean compensation defect** (not a Berry phase or a new cohomology class)

```math
\mathfrak D(n,m)=\sum_p |v_p(n)-v_p(m)|\log p-|\log(n/m)|.
```

With `g=gcd(n,m)`, write the reduced ratio `n/m=a/b`, `gcd(a,b)=1`; then the positive and negative prime-valuation logarithms are exactly `log a` and `log b`. Therefore

```math
\boxed{\mathfrak D(n,m)=2\min(\log a,\log b)
=2\log\frac{\min(n,m)}{\gcd(n,m)}.}\tag{COMP}
```

Despite the strict `log 2` Archimedean bound, the *total* prime-log variation is typically of order `2 log A`.

**Quantitative finite-band theorem.** Let `n,m` be independent uniform integers from `I_A`. By the elementary divisor identity `log gcd(n,m)=sum_(p^j|n,m)log p`, and the fact that the count of multiples of `d` in `I_A` is `A/d+O(1)` uniformly for `1<=d<2A`, one obtains

```math
\mathbb E\log\gcd(n,m)
=\sum_{p^j<2A}(\log p)\left(\frac{\#\{n\in I_A:p^j\mid n\}}{A}\right)^2
=-\frac{\zeta'(2)}{\zeta(2)}+O\left(\frac{\log^2 A}{A}\right).
```

The error uses only `0<=Λ(d)<=log d`, bounds on sums of `log d/d` and `log d`, and the absolutely convergent Euler product at `2`: no PNT, RH or π statistics. A two-dimensional Riemann sum gives

```math
\mathbb E\log\min(n,m)=\log A+4\log2-\frac52+O(A^{-1}).
```

Consequently

```math
\boxed{\mathbb E\mathfrak D(n,m)
=2\log A+8\log2-5+2\frac{\zeta'(2)}{\zeta(2)}
+O\left(\frac{\log^2 A}{A}\right).}\tag{AVERAGE-DEFECT}
```

By Markov's inequality for `log gcd`, `D(n,m)/(2 log A)->1` in probability under these uniform pairs. This is a **proven arithmetic compression phenomenon**, not source-selected signed cancellation.

## II. Every prime-phase coordinate is available in the Bohr torus

Fix finite `A` and let `\mathcal P_A={p\text{ prime}:p<2A}`. The finite prime-valuation torus is `\mathbb T^{\mathcal P_A}`. For any complex numbers `a(n)` with `|a(n)|=1`, define the finite Dirichlet/Bohr polynomial

```math
\mathcal B_A(z)=\sum_{n\in I_A}\frac{a(n)}{\sqrt n}\prod_{p\in\mathcal P_A}z_p^{v_p(n)}.
```

The one-real-parameter Archimedean flow `z_p(t)=exp(-it log p)` yields the exact Dirichlet polynomial `\mathcal B_A(z(t))=sum_(n in I_A) a(n)n^(-1/2-it)`. Unique factorization implies that the finite set `{log p:p in P_A}` is rationally independent: `sum k_p log p=0` with integral `k_p` forces `prod p^(k_p)=1` and all `k_p=0`. Thus Kronecker's theorem makes the line flow **dense and equidistributed on the entire finite prime torus**. This is an established Bohr correspondence, not new SUCC intellectual priority.

However, Haar/long-time Parseval erases the source-selected phases:

```math
\boxed{\lim_{T\to\infty}\frac1T\int_0^T|\mathcal B_A(z(t))|^2dt
=\sum_{n\in I_A}\frac1n.}\tag{BOHR-PARSEVAL}
```

This exact equality holds for the authentic BBP phase, a coherent wrong seed, or any unimodular labels. Therefore the finite torus **exists**, but its averaged energy is seed-blind; sign information resides in its nonaveraged Fourier/cross coefficients.

## III. A real 2/3 **ratio-fiber obstruction to descent**

The ratio `q=3/2` lies **strictly inside** `(1/2,2)`. Its label fiber at epoch `A` consists of the integers

```math
J_A=\{\ell\ge1:2\ell,3\ell\in I_A\}
=\{\lceil A/2\rceil,\ldots,\lfloor(2A-1)/3\rfloor\}.
```

Its size `L_A=|J_A|` is `A/6+O(1)` and tends to infinity. Let `u\in\mathbb R` be the BBP initial seed and keep the **authenticated source**

```math
Y_n(u)=16^n(u+\pi/16)=\alpha_u16^{n-1},\quad
\alpha_u=\pi+16u,\quad
 a_h(n;u)=\exp(2\pi i hY_n(u)),\quad h\in\mathbb Z\setminus\{0\}.
```

The phase on the `3/2` edge through `\ell` is exactly

```math
\boxed{a_h(3\ell;u)\overline{a_h(2\ell;u)}
=e\!\left(h\alpha_u K_\ell\right),\qquad
K_\ell=16^{2\ell-1}(16^\ell-1).}\tag{FIBER-PHASE}
```

**Irrational-seed non-descent theorem.** `K_\ell` is a strictly increasing sequence of *integers*. If `h\alpha_u` is irrational, then for any distinct `\ell,\ell'`, the displayed two edge phases differ: equality would make `h\alpha_u(K_\ell-K_{\ell'})` an integer. Thus there is **no function depending only on rational ratio `n/m`** (in particular, no multiplicative prime character) reproducing all the authentic ratios' phase transports on an epoch whenever `|J_A|>=2`. For original zero seed, `\alpha_0=\pi` is irrational. The coherent wrong seed `u_*=-\pi/16` instead gives `\alpha_{u_*}=0` and *all* fiber transports equal to 1.

This is an obstruction to **descending an observer through the lossy map `(n,m)\mapsto n/m`**, not a nontrivial Wilson-loop/Berry holonomy: the original unit-modulus vertex phases telescope around any closed path and yield holonomy 1. Retaining absolute successor indices/height is load-bearing.

### Exact all-prime passport within a single `q=3/2` fiber

For every `\ell>=1`, the integer `K_\ell` obeys

```math
v_2(K_\ell)=8\ell-4,
\quad v_3(K_\ell)=1+v_3(\ell),
\quad v_5(K_\ell)=1+v_5(\ell).
```

The odd-prime identities use the elementary lifting-the-exponent lemma, valid since `3,5|16-1`. For an **arbitrary odd prime** `p`, `16` is invertible modulo `p`, so

```math
\boxed{p\mid K_\ell\quad\Longleftrightarrow\quad
\operatorname{ord}_p(16)\mid\ell.}\tag{ALL-PRIME-PASSPORT}
```

Every `L_A` consecutive integers contain a multiple of any `d<=L_A`. Because `ord_p(16)|p-1` by Fermat, for every epoch with `L_A>=1` **every prime `p<=L_A+1` divides at least one exponent `K_\ell` with `\ell\in J_A`** (the prime 2 divides all). Across growing epochs every fixed prime appears. The familiar `2,3,5` are singled out by the powers-of-16 factor and `16-1=15`, not an unexplained numerological selection.

**Type firewall:** `p|K_\ell` is a divisibility fact about an integer exponent in the authentic BBP phase. It is *not* the statement that `q=3/2` is an Euler prime power, nor that a Weil prime-power distribution acquires a new atom at `3/2`. The completed Weil formula samples `\pm\log(p^j)`, whereas the source-phase passport lives in the coefficient attached to this non-prime-power rational ratio. A new source-preserving pairing would be needed to access both simultaneously.

### Genuine source-selected odd-eight sign contrast in one epoch

There is also a non-asymptotic, **certified original-zero source witness** in the same-ratio fiber. Take epoch `A=14`, the actual SUCC `h=8` odd-eight Fourier mode, and `\ell=7,8`. Both index pairs `(m,n)=(14,21)` and `(16,24)` belong to `[14,28)`, and both ratios are **exactly `3/2`**. Nevertheless

```math
\boxed{\Re e(8[Y_{21}(0)-Y_{14}(0)])>0,\qquad
\Re e(8[Y_{24}(0)-Y_{16}(0)])<0.}\tag{CERTIFIED-H8-DEFECT}
```

**Exact certificate.** Evaluate `P_32=\sum_(j=1)^32 16^(-j)r(j)` using *only* the original four signed poles (or their independently verified common-denominator rational form). Its positive remainder obeys the strict bound `0<P_infty-P_32<16^(-32)/(257*258)`. Multiply the complete rational interval by `8*(16^(3ell)-16^(2ell))` **before** taking any fractional parts, and check that its two endpoints have the same integer floor. Exact `Fraction` comparisons then certify

```math
\{8(Y_{21}-Y_{14})\}\in(17/20,19/20),
\qquad\{8(Y_{24}-Y_{16})\}\in(1/4,3/4).
```

The first interval lies in the positive-cosine quarter, and the second in the negative-cosine half-circle. This is a source-selected **finite** sign distinction that is absent for the coherent wrong seed `u_*=-\pi/16`, for which both edge phases equal `1`. It does not show that the *mean over growing `J_A`* cancels, and therefore proves neither original-zero parity balance nor π normality. The `h=1` epoch `A=10` also has a certified opposite-sign pair (`ell=5,6`), but `h=8` is directly aligned with SUCC's parity front.

### Exact finite-dimensional toral lift

Since `K_\ell=(4096^\ell-256^\ell)/16`, it satisfies the integer recurrence

```math
\boxed{K_{\ell+2}=4352K_{\ell+1}-1048576K_\ell.}\tag{2x3-RECURRENCE}
```

Therefore the phase-angle vector `(x_\ell,x_{\ell+1})`, with `x_\ell={h\alpha_u K_\ell}`, evolves exactly modulo 1 under the integer toral endomorphism

```math
\begin{pmatrix}x_{\ell+1}\\x_{\ell+2}\end{pmatrix}
=\begin{pmatrix}0&1\\-1048576&4352\end{pmatrix}
\begin{pmatrix}x_\ell\\x_{\ell+1}\end{pmatrix}\pmod 1.
```

Its eigenvalues are `16^2` and `16^3`. It preserves Haar measure but does **not** make the *selected point* `\alpha=\pi` equidistributed. Generic Haar mixing and deterministic original-zero orbit behavior are distinct logical statements.

## IV. Calibrated null and hostile cases

For a random parameter `\alpha` uniform in `[0,1]`, the distinct-integer Fourier characters `e(h\alpha K_\ell)` are exactly orthogonal. Therefore, for any consecutive `L` indices,

```math
\boxed{\int_0^1\left|\frac1L\sum_{\ell\in J}
e^{2\pi i h\alpha K_\ell}\right|^2d\alpha=\frac1L.}\tag{HAAR-NULL}
```

This is an **exact** finite second moment, not a model of the selected π phase. It implies (via square-index Borel–Cantelli and interpolation) that `K_\ell\alpha mod 1` is equidistributed for Lebesgue-almost every `\alpha`; it does not settle the exceptional specified `\alpha=\pi`.

Negative controls: `\alpha=0` (coherent wrong seed) yields a constant phase and mean 1; a rational `\alpha` can give periodic/non-normal behavior; and the original four-pole source may be replaced by extra-pole matched-moment mutants, so the exact BBP contract must be retained. The torus Haar mean and the valuation passport survive the wrong seed; neither proves cancellation.

## V. An even sharper finite 2/3 **multiplicativity rigidity** test

Normalize the phase by the distinguished vertex 1:

```math
 b_h(n;u)=a_h(n;u)/a_h(1;u)=e\!\left(h\alpha_u(16^{n-1}-1)\right),\quad b_h(1;u)=1.
```

The multiplicativity defect in the **declared prime-character comparison class** is

```math
\delta_h(p,q;u)=\frac{b_h(pq;u)}{b_h(p;u)b_h(q;u)}
=e\!\left(h\alpha_u[16^{pq-1}+1-16^{p-1}-16^{q-1}]\right).
```

For the first two 2/3 probes, the integer exponents are

```math
D_{2,2}=4065,\quad D_{2,3}=1048305,
\quad \gcd(D_{2,2},D_{2,3})=15,
\quad 9026D_{2,2}-35D_{2,3}=15.
```

Thus **both defects equal 1 if and only if `15h\alpha_u\in\mathbb Z`**. But `16^{n-1}-1` is always divisible by 15; so this is equivalent to `b_h(n;u)=1` for every `n`. Therefore

```math
\boxed{b_h\text{ completely multiplicative}
\iff \delta_h(2,2)=\delta_h(2,3)=1
\iff b_h\equiv1.}\tag{TWO-PLAQUETTE-RIGIDITY}
```

The authentic `\alpha_0=\pi` cannot satisfy these conditions, since π is irrational. The seed `\alpha=0` does. Despite the name *defect*, `\delta` is an exact **multiplicative 2-coboundary** of `b`: `\delta(p,q)\delta(pq,r)=\delta(q,r)\delta(p,qr)` and it has trivial cohomology class in the unrestricted space of phases. Nontriviality is relative to the **multiplicative-character comparison**, not proof of novel topology/physical curvature.

## VI. Verdict and next falsification gate

- **DISCLOSED / classical derivation:** PF, COMP, average defect asymptotic, finite Bohr torus, fiber non-descent, all-prime passport, 2×3 recurrence, Haar-null identity and two-plaquette rigidity. No novelty priority claim; the interest is their common source-typed assembly.
- **OBSERVED:** exact finite integer probes and deliberately separate direct implementations; tests do not certify an infinite π estimate.
- **REFUTED within the declared model:** assuming prime-power Weil atoms fill `(1/2,2)`; interpreting scalar vertex phases as nontrivial closed-loop holonomy; deriving signed π phase cancellation from valuations, generic Haar mixing or pairwise defect nonzero.
- **UNVERIFIED:** an original-zero source-selected bound for `T_{A,h}(3/2)=L_A^{-1}\sum_{\ell\in J_A}e(h\pi K_\ell)` or for the full signed Basel/Weyl criterion, and a valid completed-Weil pairing transferring information from non-prime-power rational ratios to a signed phase estimate.

**Target discriminating probe:** fix an odd-eight `h` and a fresh non-dyadic epoch `A`; rigorously enclose the `3/2` fiber mean with the authentic four-pole rational prefix and integer floor/carry data, and compare to coherent wrong seed, PPP-08 and an additional-pole Mellin alias. Evaluate the *full* completed Weil Γ/pole and prime-power sides when expanding across multiplicative scales. The finite certificate is only calibration; an asymptotic original-zero bound, rather than another representation, would pay the π-normality truth debt.

**External provenance:** Bohr/Kronecker finite prime torus, unique factorization, the classical rational product formula, Euler product and classical lifting-the-exponent lemma. See the prime/archimedean completed-Weil discussion in [WEIL_PACKET_PROOFS.md](WEIL_PACKET_PROOFS.md) and source-specific [DIRICHLET_PRIME_DEFECT.md](DIRICHLET_PRIME_DEFECT.md). For a modern exposition of the finite-prime Bohr lift see https://www.research-collection.ethz.ch/server/api/core/bitstreams/46e42910-1148-47a5-a381-12f68033e5c1/content .
