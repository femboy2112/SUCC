# PRIME-FORM HEAT — Pascal bulk, affine residue transport, and the completed Archimedean Mellin bridge

**Research date:** 2026-10-14. **Parent:** `research/pascal-rotated-gamma-transport-2026-10-14@a29170d4ff76899b18f2ac17748f42cb336cd20d`, itself stacked on structural-coupling PR #65; intended draft-only successor `research/prime-form-heat-mellin-2026-10-14`. Do not merge or publish a release without authorization. **Mathematical domain:** precisely the declared integer/rational/lattice source, the standard real Schwartz Gaussian, and the ordinary prime-power von Mangoldt source. **No physical source authentication, RH proof, completed Weil positivity, novel number-theoretic theorem, physical Higgs carrier, or claimed quantum speedup.** Classical analysis/group operators/elementary arithmetic are given below as complete derivations or explicitly sourced imports; Python simulations and mpmath evaluations are independent finite checks of scoped statements, not proof of analytic continuation.

## 0. Question recovered and what the construction must distinguish

The maintainer proposes that *heat runs inside the infinite Pascal/Gamma/SUCC triangle* and that recursive prime-form chains `p*q+b` connect arithmetic depth to a rotated/global Archimedean description. This has a precise strongest reading:

1. A **graded Pascal bulk** enumerates ordered successor paths and their finite observational multiplicities, without assuming the actions commute.
2. A **source-specified unbiased joint law** on those paths produces Gaussian heat under diffusive scaling; individual marginal fairness is insufficient.
3. The **integer affine digit family** `F_(p,b)(q)=pq+b` realizes a nested residue carrier and exact operators, including arithmetic prime-power fibers. The *same* digit algebra is available at composite p, so the Euler-source gate is separate.
4. Spatial ↔ spectral “rotation” is **Fourier/Poisson transform**, with its character/basis, rate/metric and lattice/Haar normalization declared, NOT a literal physical 90-degree rotation of a finite diagram.
5. Analytic heat-parameter ↔ Mellin transport gives the real Gamma factor `Gamma_R(s)=π^(-s/2)Γ(s/2)`; **both** the full-lattice source and the genuine prime-power source have honest but different completed outputs.

We test it with a split/nonsplit Pascal source, same-step correlated negative control, altered spectral power/scale, q-digit fake-prime mutation, incorrect multiplicity weighting, and finite-support versus global-limit obstructions. The resulting laws are exact within the stated mathematical source model. Nothing in a model/source tag authenticates a laboratory instrument.

## 1. Finitely generated arithmetic bulk: `p q+b` is an exact affine successor

Let `m≥2`, `b∈{0,...,m−1}`, and `q∈Z`. Set

`F_(m,b)(q)=mq+b`.

**PH-01 (Euclidean carrier partition, CLASSICAL/PROVED):** each integer `n` uniquely decomposes as `n=mq+b`, `0<=b<m`. Thus on `ℓ²(Z)` define `S_(m,b)e_q=e_(mq+b)`. Direct orthonormal-basis computation gives `S_b* S_c=δ_(bc) I` and `Σ_(b=0)^(m−1) S_b S_b*=I`. Every stated operator is a bona fide isometry. These are the standard finite-digit Cuntz-family relations in this representation. **Composite m=6 passes identically**, so these relations are *not evidence of prime multiplicativity*. For a word of radices `(m1,...,mL)`, successive maps yield `(∏m_i)q+r` and every residue `0<=r<∏m_i` has exactly one such mixed-radix word *for this fixed order*. Reverse Euclidean division is the exact inverse. Existing SUCC`s ordered-word fibers, not a scalar Pascal coefficient, are the natural carrier for mixed prime-form paths.

**PH-02 (nontrivial affine-order defect, CLASSICAL/PROVED):** two differently ordered transformations differ by

`F_(p,b)∘F_(q,c) - F_(q,c)∘F_(p,b) = (p−1)c−(q−1)b`, independent of input state. For p=2,q=3,b=c=1 the signed defect is −1. Equal multiplicative depth `pq` does NOT make the actual residues or action paths equal. This is a concrete joint-source curvature/holonomy diagnostic; not a physical gravitational curvature.

The integer Gaussian `h_t(n)=exp(−πt n²)` pulls back as

`h_t(F_(p,b)(q))=exp(−π p²t (q+b/p)²)`.

Hence the multiplication/dilation piece rescales heat time by `p²`, while the addition piece creates a **nontrivial rational shift** `b/p`. Treating the whole affine operation as pure dilation loses the residue phase in the spectral basis.

## 2. How heat is *inside* the Pascal bulk: exact polynomial action and a uniform finite-limit bound

Let `D=d/dx`. The continuous heat semigroup `H_t=exp(tD²)` acts on every polynomial exactly, because its power series truncates:

`H_t x^n = Σ_(j=0)^floor(n/2) n!/[j!(n−2j)!] t^j x^(n−2j)`.

This is a **two-degree-lowering operator through the interior grading** of a Pascal/path algebra, not an assertion that each Pascal cell is itself a physical heat packet. In the one-dimensional commutative translation frame, `H_t T_d=T_d H_t` for `T_d f(x)=f(x+d)` since `D` commutes with `T_d`. Finite coefficient arrays and rational `t` provide exact zero-rounding checks. They do not require analytic continuation or a probabilistic source.

For an actual Pascal source, let `ε_j` be IID fair ±1 and set `X_N=sqrt(2t/N) Σ_(j=1)^N ε_j`. The binomially weighted successor operator is

`P_(N,t) f(x)=2^(-N) Σ_(k=0)^N C(N,k) f(x+(2k−N)sqrt(2t/N))`.

**PH-03 (Pascal → Gaussian heat, CLASSICAL/DERIVED):** for every polynomial `f`, `P_(N,t)f→H_t f` as N→∞. Proof: at fixed polynomial degree, `D` is nilpotent; the one-step operator is `cosh(sqrt(2t/N) D)=I+(t/N)D²+O(N^-2)` in this finite nilpotent algebra, and its Nth power tends to `exp(tD²)` coefficientwise. Equivalently the fair independent steps have Fourier characteristic `cos(u sqrt(2t/N))^N→exp(−tu²)`. For `f=x^4` at 0, *exactly for every N≥1*,

`P_(N,t)x^4(0)=12t²−8t²/N`, while `H_t x^4(0)=12t²`.

**Quantitative Fourier certificate (all N in declared regime):** writing `x=u sqrt(2t/N)`, for `|x|≤1/2`, let `F(x)=−log cos x−x²/2`. Then `F''(x)=tan²x≤4x²` (using `|tan x|≤2|x|` in this interval), hence `0≤F(x)≤x⁴/3`. Therefore

`|cos(u sqrt(2t/N))^N−exp(−tu²)|≤4t²u⁴/(3N)`, **provided** `8tu²≤N`, `t≥0`, `u∈R`. The algorithm returns this bound as an *exact Fraction* for rational t,u,N. This is an analytic proof; tests only calibrate it.

**Hostile source law:** replace independent signs with ONE shared fair latent sign. Every marginal successor still appears fair, but the final character is `cos(u sqrt(2tN))`, not `cos(u sqrt(2t/N))^N`; it does not converge to the same heat law. The joint/path law is thus load-bearing in precisely the sense of SUCC's NO-GHOST coupling warnings. A uniformly sampled radix-p digit can also be centered and variance-normalized to a Gaussian limit for any p≥2, **including p=6**; therefore the Pascal heat limit alone is prime-blind.

## 3. Precisely licensed 90° spectral transport: finite residue Fourier and global theta

**Source:** integers `Z`, real Gaussian `g_t(x)=e^(−πt x²)`, Fourier convention `fhat(ξ)=∫_R f(x)e^(−2πixξ)dx`, standard Lebesgue measure, and the dual lattice `Z`. From the standard Gaussian integral,

`g_t hat(ξ)= t^(−1/2) exp(−π ξ²/t)`.

For m≥2 and one affine residue b, set `Θ_(m,b)(t)=Σ_(q∈Z) exp(−πt(mq+b)²)`. Poisson summation on the shifted lattice gives

`Θ_(m,b)(t)= (1/(m sqrt(t))) Σ_(r∈Z) exp(−πr²/(m²t)) exp(2πi r b/m)`.

The **phase** `exp(2πir b/m)` is essential. If `C_b=Θ_(m,b)`, its finite Fourier character is

`Σ_(b mod m) exp(−2πi j b/m) C_b(t)
    =t^(−1/2) Σ_(k∈Z) exp[−π(k+j/m)²/t]`.

**PH-04 (affine-coset/dual-phase, CLASSICAL/DERIVED):** the equality follows by substituting the residue Poisson identity and using orthogonality of finite characters `Σ_b exp(2πi(r−j)b/m)=m 1_(r=j mod m)`. This is a genuine Fourier change between residue localization and spectral characters, not an undefined geometrical 90° rotation. It is exact for **all** m≥2, including composite m. Numerical independent direct-lattice and finite-Fourier evaluations are cross-checked at high precision; tails are not silently assumed zero.

Summing all residues gives the classical Jacobi theta modular identity:

`θ(t)=Σ_(n∈Z)e^(−πt n²)=t^(−1/2) θ(1/t)`.

It holds for all real t>0 from Gaussian Poisson summation. Primary reference: NIST DLMF §20.7(viii), (20.7.32). The finite q-digit recursion only *reindexes* the whole lattice; Fourier duality itself uses the independently chosen Gaussian/real Haar normalization and lattice self-duality. A physical carrier with different geometry, measure, phase or boundary law would require a different source-specific proof.

## 4. Real Archimedean local factor: the Gaussian is the source, not a slogan

On `R^×`, choose Haar measure `d^×x=dx/|x|` and the self-Fourier real Gaussian `φ(x)=exp(−πx²)`. For `Re(s)>0`, substitution `y=πx²` gives the exact *local zeta integral*

`Z_∞(φ,s) = ∫_(R^×) φ(x)|x|^s d^×x
   = 2∫_0^∞ exp(−πx²)x^(s−1)dx
   = π^(−s/2) Γ(s/2) = Γ_R(s)`.

**PH-05 (ARCH-GAMMA ID, CLASSICAL/DERIVED)** follows without zeta zeros. The real Gaussian scale matters: replacing φ by `exp(−πc x²)` multiplies the result by `c^(−s/2)`. Replacing quadratic energy x² by x^a produces `(πc)^(−s/a)Γ(s/a)` with the corresponding Mellin power; hence the *shape* `Γ(s/2)` specifically encodes quadratic spectral energy (and the chosen parameterization). Pascal coefficients alone select neither c nor a. The scalar `π` is fixed by the Fourier self-dual normalization.

The same factor appears as the heat Mellin identity, for any `n≥1` and `Re(s)>0`:

`∫_0^∞ exp(−πt n²)t^(s/2−1)dt = Γ_R(s)n^(−s)`.

This equality is the sought **source-identified analytical intertwiner**, conditional only on declared mathematical carriers, Gaussian form and domain. At fixed n it is elementary; its use with an infinite source requires justified interchange and bounds.

## 5. Integer theta completes ζ, including its functional equation, without importing any zeros

For `Re(s)>1`, let `ω(t)=Σ_(n≥1)e^(−πt n²)=(θ(t)−1)/2`. Absolute convergence and Tonelli give

`Λ(s) := Γ_R(s)ζ(s) = ∫_0^∞ ω(t)t^(s/2−1)dt`.

Split at t=1. Substitute `θ(t)=t^(−1/2)θ(1/t)` in the t<1 part, change variable t↦1/t, and integrate the two elementary zero-mode terms. One obtains

`Λ(s) = 1/[s(s−1)]
       + ∫_1^∞ ω(t)[t^(s/2−1)+t^((1−s)/2−1)]dt.`  **(PH-06)**

The right-hand integral converges absolutely locally uniformly for *all complex s* because ω decays exponentially for t≥1. It therefore provides the meromorphic continuation with simple poles at 0 and 1, and is manifestly invariant under `s↔1−s`. Hence the classical `ξ(s)=s(s−1)Λ(s)/2` extends to an entire function with `ξ(s)=ξ(1−s)` and `ξ(0)=ξ(1)=1/2`. The computation uses **zero-free inputs**; it is a classical Poisson/theta proof of the functional equation, NOT an RH or zero-distribution proof. Sources: NIST DLMF §20.10 (20.10.2), §25.5(ii) (25.5.13–14), §25.4 (25.4.3–4).

The runnable program evaluates the convergent `t≥1` integral via upper incomplete-Gamma terms:

`Λ(s)=1/[s(s−1)] + Σ_(n≥1){(πn²)^(−s/2) Γ(s/2,πn²)
                           +(πn²)^(-(1−s)/2) Γ((1−s)/2,πn²)}`.

This *does not query zeros*. At negative even integers it gives finite values directly, while a naïve pointwise `Γ(s/2)*ζ(s)` call encounters `∞·0`. This is a limit/domain issue repaired by the source-derived analytic representation. On `0≤Re(s)≤1`, truncation after n=N has rigorously derived absolute error at most

`2 exp(−π(N+1)²)/[π(N+1)²(1−exp(−π(2N+3)))]`.

**Proof of the bound:** each `t≥1` power is at most 1 in modulus on this strip; for k≥N+1 successive squares grow by at least `2N+3`, so the Gaussian tail is dominated by a geometric series, followed by ∫_1∞ exp(−πt(N+1)²)dt. The bound is a mathematical majorant; the mpmath numbers used to evaluate it are still floating-point approximations, not certified directed-rounding intervals.

## 6. The decisive arithmetic sieve: prime-form zero residue isolates an Euler logarithmic jet

Let `Λ(n)` be the genuine von Mangoldt function: `Λ(p^k)=log p` for prime p, k≥1, and zero otherwise. For *any radix* m≥2, take the actual prime-power source restricted to the affine zero-coset `n≡0 mod m`.

**PH-07 (source-dependent arithmetic depth isolation, CLASSICAL/DERIVED):**

* If `m=p^a` for ONE prime p and a≥1, the only contributing terms are `n=p^k` with k≥a.
* If m has at least two distinct prime factors, the intersection is empty: `Λ(n)=0` for every positive multiple of m.

Proof: `m|p^k` implies every prime dividing m equals p, conversely all k≥a work. Thus for `Re(s)>1` (and in fact Re(s)>0 for this fixed local series),

`Σ_(m|n) Λ(n)n^(−s)=
     (log p) p^(−as)/(1−p^(−s))    if m=p^a,
     0                             otherwise.`

For genuine prime radix m=p this becomes

`(log p)/(p^s−1) = −d/ds log[(1−p^(−s))^(−1)]`.

Under the Gaussian heat Mellin, the full *source-local identity* is

`∫_0^∞ [Σ_(k≥1)(log p)e^(−πt p^(2k))]t^(s/2−1)dt
       = Γ_R(s) (log p)/(p^s−1)`,

valid for Re(s)>0. This is the exact logical point where arbitrary radix geometry acquires **source-specific prime multiplicativity**. A fake radix 6 has a perfectly good digit Cuntz family and Gaussian Fourier transform but has **zero** genuine prime-power contribution in the zero residue class; radix 4 isolates only powers 2^k with k≥2 and thus carries a *truncated*, differently normalized local factor. A prime p=5 isolates all p-powers. These are exact arithmetic mutation controls, not fitted numerics.

Summing over all genuine primes and k with `Re(s)>1` gives, by the Euler product and absolute convergence,

`Σ_p (log p)/(p^s−1) = −ζ'(s)/ζ(s)`.

Consequently the genuine arithmetic jet heat

`J(t)=Σ_p Σ_(k≥1)(log p) exp(−πt p^(2k))`

obeys **PH-08 (zero-independent prime→Arch Mellin):**

`∫_0^∞ J(t)t^(s/2−1)dt = Γ_R(s)[−ζ'(s)/ζ(s)]`,  `Re(s)>1`.

This is a classical identity, not a replacement for the full completed Weil distribution. It uses no nontrivial zero positions as inputs, and it reads authentic `log p` rather than synthetic p label weights. Source-derivation does *not* imply positivity of the completed Weil form; positive J(t) for t>0 is logically far weaker.

**PH-09 (rigorous arithmetic finite tail).** Truncate prime-power terms to n≤N. For σ=Re(s)>1, N≥3, `0≤Λ(n)≤log n`, and `f(x)=log x/x^σ` is decreasing for x≥N. Then

`|Σ_(n>N)Λ(n)n^(−s)|≤N^(1−σ)[log N/(σ−1)+1/(σ−1)²]`.

Multiply by `|Γ_R(s)|` for a bound on the Mellin-transformed truncated `J`. The termwise integration of a **finite** `J_N` and the Dirichlet sum was checked independently with numerical quadrature; the infinite interchange is justified by absolute convergence and the analytic inequality, not by that quadrature.

## 7. The multiplicity trap: a prime-form depth tree does not determine its Euler weight

At depth k of a full radix-p tree there are `p^k` distinct digit words. Assign the same positive spectral energy `E_k=p^(2k)` to each node. The *ordinary Hilbert trace* is

`Tr(e^(−πt E))=Σ_(k≥0)p^k exp(−πt p^(2k))`.

Its Mellin-Dirichlet coefficient (stripping `Γ_R(s)`) is `Σ p^(k(1−s))=(1−p^(1−s))^(−1)`, valid for Re(s)>1. It is a **shifted** Euler-looking factor. Now introduce an *additional explicitly chosen weighted trace functional* giving each depth-k node mass `p^(−k)`, so each whole depth has total mass 1:

`Tr(W e^(−πt E))=Σ_(k≥0)exp(−πt p^(2k))`, with `W|_depth k=p^(−k)I`.

Its Mellin multiplier is `(1−p^(−s))^(−1)`, for Re(s)>0. The weighting is not an ordinary trace invariant under a Hilbert basis change; it is independent source/measure data. Even composite p=6 yields the same formal geometric multiplier, so primality is STILL a separate source check. This exposes a meaningful **dimension/degeneracy shift** in the proposed finite↔Archimedean depth picture without upgrading a numerology to RH.

A still simpler countermodel assigns energy E_k=k and raw degeneracy p^k. Then `Σ_k p^k e^(−tk)` is not trace class at small t (diverges for t≤log p). Therefore a globally defined heat trace cannot be manufactured by merely declaring an infinite prime-depth tree: an actual spectral-energy growth, measure and summability theorem are required.

## 8. One global Archimedean gate after multiplicative finite-place assembly (the most consequential synthesis)

This is the sharpest rigorous interpretation found of “infinitely many finite places flowing through one global Archimedean successor.” **Do not attach a separate Gamma factor to every prime. First multiply the genuine arithmetic sources; apply one global Gaussian heat/Mellin gate afterward.**

Let `P={p1,...,pr}` be a **finite set of distinct genuine primes**, fix finite exponent depth `K`, and define the multiplicative multi-index carrier

`C_(P,K)={α∈{0,...,K}^r}`, `n(α)=∏_(p∈P) p^(α_p)`.

The fundamental theorem of arithmetic makes `n(α)` injective. Define ONE heat observable over the jointly realized carrier:

`H_(P,K)(t)=Σ_(α∈C_(P,K)) exp[−πt n(α)^2]`.

**PH-13 (one-Gamma finite Euler/heat gluing, CLASSICAL/PROVED):** for `Re(s)>0`, finite summation and the Gaussian Mellin identity give

`∫_0^∞ H_(P,K)(t)t^(s/2−1)dt
      = Γ_R(s) Σ_α n(α)^(-s)
      = Γ_R(s) ∏_(p∈P) Σ_(k=0)^K p^(-ks).`

**Only one `Γ_R(s)` occurs.** The tempting product `∏_(p∈P) [Γ_R(s)Σ_(k=0)^K p^(-ks)]` would instead introduce `Γ_R(s)^r` and is a WRONG identification when r>1. This is a precise analytic coupling law, not a metaphor about superconducting infinity. Independent algorithms check the exact rational product against an independently enumerated original-integer source; a separate finite Gaussian integral numerically checks the analytic gate. At `P={2,3,5}`, `K=3`, `s=2`, the 64 distinct smooth integers produce exactly `Σ n^-2=2836093/1822500` and one-Gamma Mellin `≈0.495339610445347291`. The incorrect per-prime-Gamma construction differs by approximately `0.445151214810090205`.

For a **fixed finite** P, let K→∞. Each geometric series converges on Re(s)>0, so the corresponding infinite P-smooth source has an honest holomorphic Euler product `E_P(s)=∏_(p∈P)(1−p^(-s))^(-1)`. Let P grow through all primes. By unique factorization and absolute convergence, `E_P(s)→ζ(s)` for Re(s)>1; hence the **one global Gamma gate** gives `Γ_R(s)ζ(s)` on that domain, precisely matching the separately constructed additive integer-theta heat route. This is a classical source-justified local/global identification in the convergence region, not a Weil-sign theorem.

**PH-14 (rigorous finite-place→global error, CLASSICAL/PROVED):** let P be the cutoff bound on allowed primes, so `E_P(s)=∏_(p≤P)(1−p^(-s))^(-1)`. For real σ>1, positive Dirichlet terms give

`0≤ζ(σ)−E_P(σ)≤Σ_(n>P)n^(−σ)≤P^(1−σ)/(σ−1)`.

The first inequality follows because every excluded integer has a prime factor >P, hence itself >P; the second is the elementary integral comparison for decreasing `x^(−σ)`. For complex s with Re(s)=σ>1 the analogous modulus bound holds. At P=29, σ=2 the exact rational bound is `1/29`, while the numerical residual is approximately `0.0118635763524872161`. This is not a claim to know ζ via finite computation alone: it is a theorem-backed enclosing majorant.

**PH-15 (a sharp global domain obstruction, CLASSICAL/PROVED):** every finite-prime E_P(s) is defined for Re(s)>0, but **the prime-set limit does NOT converge on the positive real axis for 0<s≤1**. Every integer 1≤n≤P factors entirely over primes≤P, so for real σ>0,

`E_P(σ)≥Σ_(n=1)^P n^(−σ)`.

The right side diverges as P→∞ for 0<σ≤1. Thus finite-place completeness individually does not provide a **uniformly valid global Euler convergence domain**. Theta/Poisson analytic continuation is a genuine extra bridge with its own source, phase, topology and limit hypotheses. It cannot be treated as ordinary positive-term limit gluing into the critical strip. This gives SUCC a mathematically clean example of its environmental hard-field/finite-to-infinite transport debt.

**Interpretation:** One Archimedean factor after multiplicative assembly is a valid *global analytic functional* on the declared integer source. It is not a proven unique global physical SUCC, and applying Mellin or theta continuation does not supply the missing arithmetic positivity.

## 9. Triangulated verdict / next verdict-changing proofs

| Candidate proposition | Verdict | Independent discriminator / remaining proof debt |
|---|---|---|
| Pascal internal paths create Gaussian heat | CLASSICAL/PROVED under IID fair source; exact finite error | Correlated but marginally fair source fails; scale mutation |
| Every p-ary digit tree gives source-specific prime data | REFUTED | m=6 preserves digit Hilbert algebra but lacks true-prime jets |
| Affine residue Fourier is a spectral 90° transport | CLASSICAL/PROVED for declared lattice Gaussian | Nonzero phase and finite Fourier tests; not literal coordinate rotation |
| The real Gaussian yields `π^(−s/2)Γ(s/2)` | CLASSICAL/PROVED for Re(s)>0 | Wrong Gaussian scale/power changes it |
| Theta supplies completed ζ and s↔1-s | CLASSICAL/PROVED with Poisson and analytic split | Full meromorphic continuation; **not** zero locations |
| Zero-residue prime-form cut isolates authentic local Euler log factor | CLASSICAL/PROVED for actual Λ | m=4 truncated p=2; m=6 zero; fake additive primes rejected |
| Source-identified prime-heat Mellin equals `Γ_R(s)(−ζ'/ζ)` | CLASSICAL/PROVED, Re(s)>1 | Exact analytic tail; valid only after summing authentic prime jets |
| Arbitrary pure depth trace recovers the local Euler factor | REFUTED | Raw multiplicity shifts s to s−1; weighted functional is extra structure |
| One global Gamma after finite-prime multiplicative assembly | CLASSICAL/PROVED on Re(s)>0 (finite P); Re(s)>1 (global P) | Separate per-prime Gamma factors give wrong multiplicity; no global Euler limit for real 0<s≤1 |
| Finite-place prime limit transports through critical strip as positive Euler product | REFUTED | Source lower bound E_P(σ)≥Σ_(n≤P)n^-σ diverges for 0<σ≤1 |
| Constructed heat is the global completed Weil form and automatically PSD | UNVERIFIED | Need full explicit formula/test-domain identification plus an *independent sign theorem* |
| Construction proves RH | UNVERIFIED / NO PROOF | No globally identified positive Weil form, spectral zero exclusion, or Nyman limit |

**Next first theorem to attempt:** build source-faithful distributional *test-function intertwiner* from (i) exact genuine-prime jet heat and (ii) Gaussian/theta Archimedean/pole terms to **the full completed Weil/Suzuki quadratic form on a specified dense core**. Separate arithmetic identity, domain regularization, and sign; require completed Γ/poles/conductor/half-density, matched Dirichlet/non-Euler controls, support-changing causal history, and independently certified error terms. This is mathematically hard and still open. The exact `Γ_R(s)(−ζ'/ζ)` identity above must not be misreported as that stronger identification or as positivity.

**Parallel fruitful offshoot:** characterize source-weighted finite p-digit heat functors and their exchange/holonomy defects as operators on projective limits; test whether they form a bona fide natural transformation under `pq+b` composition with a declared Fourier/character transport. The finite type checks in this branch are a foundation, not a global physical transport functor.

## 10. Provenance, reproduction, and outside literature

New-to-repo code: `observational_succ/prime_form_heat.py`; adversarial tests `tests/test_prime_form_heat.py`; deterministic receipt compiler `scripts/prime_form_heat_probe.py`; frozen output `research/2026-10-14/PRIME_FORM_HEAT_RECEIPT.json`; separate ledger `docs/CLAIM_SUPPLEMENT_PRIME_FORM_HEAT.md`. The isolated overlay includes the exact published parent modules and receipts for parent regression; 121 tests PASS in Python 3.13.5, of which 60 are new prime-form heat tests. This is *not* the full-repository CI report, and the basic classical theorems have not been translated to Lean here. Source file SHA/replay need to be checked against the published Git commit before upgrading operational statuses.

Primary/reference sources (their mathematical content is classical):
- NIST DLMF [20.7(viii)](https://dlmf.nist.gov/20.7#viii), modular theta / Fourier Gaussian transform.
- NIST DLMF [20.10](https://dlmf.nist.gov/20.10), theta Mellin completed zeta.
- NIST DLMF [25.4](https://dlmf.nist.gov/25.4), completed ξ normalization and functional equation.
- NIST DLMF [25.5(ii)](https://dlmf.nist.gov/25.5#ii), theta integral and analytic continuation.
- NIST DLMF [5.2](https://dlmf.nist.gov/5.2), Euler Γ integral and domain.
- Classical frameworks: Cuntz digit representations; Poisson summation; von Mangoldt Euler-log derivative; Fourier heat semigroup; elementary moment/CLT. No independent academic novelty priority is claimed for these tools or their combination without external independent assessment.
