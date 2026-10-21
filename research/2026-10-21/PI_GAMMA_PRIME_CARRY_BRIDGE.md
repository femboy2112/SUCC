# π / Gamma / joint prime-power carries: exact source-to-digit transport

**Date:** 2026-10-21. **Research status:** classical exact identities, paper-proved transport and period lemmas, tested exact finite implementation. **Neither π normality nor RH is proved.** Academic novelty of the SUCC presentation is UNVERIFIED.

**Parent:** Academic Main VIII `b116841f12b41aaf7600da39bbb40577f25b6295`. Builds on merged polygon SUCC POL-01–09, the prime-phase-clock/CRT investigations, and references draft PR #226's independently certified finite Fourier oracle without assuming that draft is merged. No historical sources, claim authority registries or imported archives are modified.

## Target and existing mathematical gate

The author's route is **circle → Gamma → integers/factorials → all prime-power clocks → hierarchical base-b digit transitions**. We do **not** replace the joint prime system by a single arbitrary modulus or assert that fair sampling of polygon vertices makes the selected π orbit generic.

Let `e(t)=exp(2πit)` and, for b≥2 and nonzero integer h,

`A_(b,h,N)(x) = N^(-1) sum_(j=0)^(N-1) e(h b^j x)`.

By Weyl, π is normal in base b iff `A_(b,h,N)(π)→0` for **every** nonzero h. In base 2 positive odd h suffice: negative frequencies conjugate, and `h=2^k h0` shifts the orbit by k, affecting its normalized sum by at most `2k/N`. Testing only h=1 cannot prove normality.

## PCG-00: literal circle–Gamma–Euler analytic interface

For a geometric circle of circumference L, its Laplacian heat trace is

`H_L(t) = sum_(m in Z) exp(-t (2πm/L)^2)`.

For `Re(s)>1`, an absolutely convergent Mellin integral yields

`integral_0^infinity t^(s/2-1)(H_L(t)-1)dt = 2 Gamma(s/2)(L/(2π))^s ζ(s)`.

Euler's product `ζ(s)=prod_p(1-p^(-s))^(-1)` supplies **every prime**. The circle's Fourier normalization already involves π; this is a mathematically honest analytic interface, not a derivation of normality or an independent creation of π from π-free input.

## PCG-01: Wallis → Gamma(n) → Kummer's collective prime-power carries

For `n≥1`, Wallis's circle-integral product gives the rational lower approximant

`R_n = 2 prod_(k=1)^n 4k²/(4k²-1)`
`    = 2^(4n+1) Gamma(n+1)^4/[Gamma(2n+1)Gamma(2n+2)]`
`    = 2^(4n+1)/[(2n+1)binom(2n,n)^2]`.

For each prime p set

`c_p(n) = v_p(binom(2n,n)) = sum_(a≥1)(floor(2n/p^a)-2floor(n/p^a))`.

By Legendre's factorial formula, each prime-power summand equals 0 or 1. Kummer's theorem identifies their sum with the number of carries in the base-p addition `n+n`. This is a **system of all prime-power clocks at once**, not a collection of first residues.

Therefore the following is exact, with no π digits as input:

`R_n = 2^(4n+1)/[(2n+1)prod_(p≤2n)p^(2c_p(n))]`.

Also `log R_n = (4n+1)log2-log(2n+1)-2sum_(p≤2n)c_p(n)log p`.

### Strict rational interval (paper proof)

Write `t_n=log(π/R_n)=sum_(k>n)-log(1-1/(4k²))`. Since `-log(1-u)<u/(1-u)` for `0<u<1`,

`0<t_n<sum_(k>n)1/(4k²-1)=1/(4n+2)`.

Using `exp(t)≤1/(1-t)` for `0≤t<1` gives

**`R_n<π<U_n=R_n(4n+2)/(4n+1)`.**

The actual exact width is `U_n-R_n=R_n/(4n+1)`; no hidden floating rounding. This is O(1/n), not exponential convergence.

## PCG-02: independent full-prime Euler route to π²

Basel plus Euler gives `π²=6 ζ(2)=6prod_p(1-p^(-2))^(-1)`.

Let `P_Q=6prod_(p≤Q)p²/(p²-1)`, integer Q≥2. Because every omitted factor is >1 and primes are a subset of integers,

`1<π²/P_Q<prod_(k=Q+1)^infinity(1-k^(-2))^(-1)=(Q+1)/Q`.

**`P_Q<π²<P_Q(Q+1)/Q`**, width `P_Q/Q`. Intersecting this interval with `[R_n²,U_n²]` produces a two-source exact π² enclosure. The implementation uses integer square roots to certify base-b digit prefixes; a cylinder boundary yields no answer, never a guessed digit.

This second route independently checks the Wallis/Kummer source. It does not imply that the resulting digits are equidistributed.

## PCG-03: a genuinely signed prime-character alternative

The quarter-circle integral gives

`π/4=∫_0^1 dx/(1+x²)=L(1,χ_4)`, with `χ_4(p)=+1` for `p≡1 mod 4`, `-1` for `p≡3 mod 4`, and 0 at p=2. Thus, in **increasing prime order**,

`π/4=prod_(p≡1 mod4) p/(p-1) × prod_(p≡3 mod4) p/(p+1)`.

Comparing with ζ(2) gives the conjugate signed product

`π/2=prod_(p≡1 mod4) p/(p+1) × prod_(p≡3 mod4) p/(p-1)`.

These s=1 products are **conditionally convergent**, not absolutely convergent; the standard prime-number-theorem-in-progressions input handles natural-order convergence. No reordering or unproved uniform prime cutoff is licensed. This supplies real signed prime phases, but still no base-b orbit cancellation.

## PCG-04: exact finite digit successor and normality transfer

Let `y_n=(R_n+U_n)/2=A_n/B_n` in lowest terms. Its rational phase orbit is the modular transition

`r_0=hA_n mod B_n; r_(j+1)=b r_j mod B_n;`
`e(hb^j y_n)=e(r_j/B_n)`.

This is a literal Kummer prime-power source → arithmetic finite-orbit interface. Long division of the same rational yields digit SUCC transitions.

For every integer `b≥2,h≠0,N≥1` the circle Fourier character is `2π|h|<8|h|` Lipschitz. Since `|π-y_n|<(U_n-R_n)/2`,

`|A_(b,h,N)(π)-A_(b,h,N)(y_n)|`
` < 4|h| (U_n-R_n)(b^N-1)/(N(b-1)).`

Taking `n=b^N` and using `R_n<π<4` gives the **all-horizon bound**

**`|A_(b,h,N)(π)-A_(b,h,N)(y_(b^N))|<4|h|/[N(b-1)]`.**

Consequently, for each fixed b,

**π is normal in base b iff the exact Wallis/Kummer midpoint Fourier sums `A_(b,h,N)(y_(b^N))→0` for all h≠0.**

**Caution:** This is an arithmetically structured, quantitatively proved equivalent *proof obligation*, not a resolution. The outstanding right-hand-side cancellation is as hard as the normality target until a noncircular independent estimate is found. The symbolic error budget is cheap; enumerating the n=b^N prime carry-vector is exponentially large in N.

## PCG-05: dyadic Wallis midpoint has rigorously growing binary period

**Theorem (paper proof).** Set n=2^m, m≥0. The reduced denominator D_m of y_n is odd, divisible by both coprime integers

`q_m=2^(m+1)+1,` `r_m=2^(m+2)+1,`

and the **least binary orbit period** is divisible by

**`2(m+1)(m+2)`.**

**Proof:** Kummer's base-2 carry count gives `v_2(binom(2n,n))=1` for n a power of two. Put `binom(2n,n)=2u` with u odd. Algebra yields

`y_n=2^(4n-2)(8n+3)/[(2n+1)(4n+1)u²]`.

Because `8n+3=4(2n+1)-1=2(4n+1)+1`, neither odd factor can cancel, and `gcd(2n+1,4n+1)=1`. For each k≥1, `ord_(2^k+1)(2)=2k`: 2^k is -1 modulo 2^k+1, while no exponent j<k or k<j<2k can give +1 by the elementary magnitude argument. Thus the period is divisible by the lcm of `2(m+1)` and `2(m+2)`, namely `2(m+1)(m+2)`. QED.

**Joint source/period corollary:** for each `m≥1` and fixed odd h,

`|A_(2,h,m)(π)-A_(2,h,m)(y_(2^m))|<4|h|/m`,

yet y_(2^m) has period ≥`2(m+1)(m+2)`. Thus the source approximants track π for the specified growing observation horizon without a short rational cycle collapsing the representation. This is an **arithmetic improvement in source-path construction**, not an automatic mixing theorem.

## PCG-06: hostile counterexample refutes "long period ⇒ mixing"

Set `x_N=1/(2^(N²)-1)`, N≥2. It has multiplicative order **exactly N²** in base 2: `2^(N²)≡1`, while `0<2^k-1<2^(N²)-1` for every `0<k<N²`. Yet

`|A_(2,1,N)(x_N)-1|<8(2^N-1)/[N(2^(N²)-1)]→0`.

So its length-N Fourier mean tends to **1**, the opposite of normality, despite a quadratic period. PCG-05 cannot replace the missing phase-cancellation theorem.

## PCG-07: RH is relevant to precision, not yet to digit equidistribution

Under RH, the classical `π_prime(x)=Li(x)+O(x^(1/2)log x)` error and partial summation yield

`sum_(p>x)p^(-2)=integral_x^infinity dt/(t²log t)+O(x^(-3/2)log x)`.

Using `log(1-u)^(-1)=u+O(u²)`, one obtains the RH-conditional Euler-tail expansion

`log π = (1/2)log6-(1/2)sum_(p≤x)log(1-p^(-2))`
`        +(1/2)integral_x^infinity dt/(t²log t)+O(x^(-3/2)log x)`.

**This is source-precision control, not selected-digit orbit mixing.** It neither establishes π normality assuming RH nor its converse. An actual RH iff π-normality theorem would require **two independent implications** with growing digit-base conductors; fixed-modulus prime equidistribution is not a substitute.

## PCG-08: required discriminating proof, and next research sequence

For each fixed b and h≠0, put n=b^N and reduce `y_n=A_N/B_N`. An independently proved, source-specific estimate

`sum_(j<N) exp(2πih(A_N b^j mod B_N)/B_N)=o(N)`

would prove π base-b normality by PCG-04. Any uniform power saving `O(N^(1-δ))` would be stronger. **UNVERIFIED.** The issue is a highly structured *incomplete* exponential sum: its observation interval N is far shorter than the full denominator scale, so complete-period order/distribution cannot establish it.

Seek independent mechanisms and hostile tests: (1) exact Kummer carry-vector cancellations versus rad-only/depth-dropped mutants, (2) Bailey–Crandall's BBP perturbed-doubling representation and Lagarias's two-orbit analysis as a separate genuine analytic route, (3) signed χ4 and Gamma/Mellin observables with explicit phase transport and error budgets, and (4) counterexamples to any proposed short-orbit estimate **before** extrapolating fitted finite data. Finite tests alone cannot certify the limit.

**Claim ledger:** PCG-00/01/02/03 are classical sources and exact/proved paper derivations; PCG-04 is a proved equivalence with **open cancellation**; PCG-05 is a proved paper period lemma (academic novelty unverified); PCG-06 is an explicit refutation of period⇒mixing; PCG-07 is classical RH-conditional prime-tail analysis; PCG-08 is **UNVERIFIED**. No claim here is Lean-formalized, independently refereed or promoted to installed theorem authority.

**Reproduce, from repository root:**
`python -m unittest discover -s tests -p 'test_pi_prime_carry_transport.py' -v`
`python scripts/pi_prime_carry_probe.py --output /tmp/pi-carry.json`
`python scripts/verify_provenance.py`

**Primary work:** Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, [author's paper](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf) (the normality assertion is conditional on their **Hypothesis A**, not proven); Lagarias, *On the Normality of Arithmetical Constants*, [arXiv:math/0101055](https://arxiv.org/abs/math/0101055); NIST DLMF [§25.15](https://dlmf.nist.gov/25.15) for Dirichlet L-functions and [§25.16](https://dlmf.nist.gov/25.16) for RH-equivalent prime errors. Wallis, Euler's Basel identity, Kummer, Legendre, and Weyl are credited classical machinery.


## PCG-09: exact simultaneous CRT character transport (proved paper)

The **source** vector c_p(n) from Kummer is not the **observation conductor** after rational normalization. Reduce the Wallis midpoint as y_n=a_n/D_n with gcd(a_n,D_n)=1. Its denominator has a unique complete prime-power factorization D_n=prod_(q in Q_n)q, with q=p^v_p(D_n). These primes can include normalization factors (2n+1)(4n+1): do not identify the conductor with the central binomial valuations.

For each q, define the **explicit transport unit** u_q=(D_n/q)^(-1) mod q. The CRT idempotents satisfy

`sum_(q in Q_n) (D_n/q)u_q = 1 (mod D_n)`.

Therefore for any base b, frequency h, and time j,

`h b^j a_n/D_n = sum_(q in Q_n) h b^j a_n u_q/q (mod 1)`.

In the **declared common additive-character basis** e(t)=exp(2pi it) this gives the exact identity

**`e(h b^j y_n) = prod_(q in Q_n)e(h b^j a_n u_q/q)`.**

Hence the Wallis-carry midpoint Weyl mean is an explicitly synchronized product of prime-power clock characters:

`A_(b,h,N)(y_n) = N^(-1)sum_(j<N)prod_(q in Q_n)e(h b^j a_n u_q/q)`.

This is classical CRT, but it is an essential SUCC interface: **joint** time coherence, not independent marginal prime-clock statistics, governs global Fourier cancellation. A local uniform distribution does not by itself establish a small mean for a product of coupled phases.

For any nonempty partition Q_n=S∪T, set F_S(j)=prod_(q in S)e(h b^j a_n u_q/q), similarly F_T(j). A genuinely new proof could show quantitative cross-family time **decorrelation** `N^(-1)sum_(j<N)F_S(j)F_T(j)→0` for the authentic source-selected n=b^N. As formulated this is still an equivalent open exponential-sum problem, not an unearned bound. The dyadic period theorem supplies at least two nontrivial coprime conductor subfamilies but gives no independence.

**Reproduction and hostile mutation:** exact integer-residue character reconstruction holds in tests 17–19 for several n, bases and frequencies. Replacing every transport inverse u_q by 1 demonstrably breaks the identity (n=2). The finite trial-factorization checker rejects large denominators; this computational resource boundary does not restrict the general CRT theorem.

**PCG-09 status: PROVED PAPER / EXACT FINITE TESTED MODEL; academic novelty unverified.** Decisive remaining task: obtain genuine new incomplete-orbit cancellation at unbounded horizons, with source-map and long-period nonmixing controls.
