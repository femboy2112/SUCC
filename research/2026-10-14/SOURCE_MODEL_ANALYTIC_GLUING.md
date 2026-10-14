# Operation SOURCE-INTERACTION — constructing all-place zeta analysis inside a source-indexed SUCC carrier

**Research checkpoint:** October 14, 2026. Parent: SUCC `research/real-place-weil-identification-2026-10-14@55307fec354be0c671562233ca744907cf716ca5`, draft PR #71, itself stacked on prime-form Pascal/heat PR #69. Child: `research/source-interaction-adelic-analytic-gluing-2026-10-14`. **RH PROVED: NO.** No nontrivial zero locations supplied, queried, used for a construction, or established. No actual physical apparatus, new field ontology, original scholarly priority, or Lean kernel refinement is claimed. The deepest analytic identities are **CLASSICAL**, with precise source and domain hypotheses; the new project contribution is source-indexed integration, quantitative finite error certificates, explicit model-vs-model obstructions, and a contact-constant link into the other SUCC Suzuki lineage.

## 0. Maintainer hypothesis, sharpened without swapping its meaning

> Once E has a series of lawful models relative to its carrier, E can model the models' interactions; proving compatibility and source-preserving normalization permits E to derive analytic statements outside the convergent Euler-product region without physically leaving its carrier.

The mathematical realization is not a magical sum of divergent local Euler series. It is one **original rational lattice source** read through two distinct analytic operations:

1. **Multiplicative**: unique factorization of integers and normalized local multiplicative Haar measures yield finite-prime Euler factors and one Archimedean Gamma factor. Their infinite product converges only for `Re(s)>1`.
2. **Additive/Poisson**: the same diagonal rational source, filtered through all finite p-adic integral carriers and the self-dual real Gaussian, yields the integer theta series. Its verified Fourier interaction yields a global modular transport law.
3. **Mellin/analytic gluing**: the full theta Poisson relation supplies a second, convergent representation that agrees with the first on the open half-plane `Re(s)>1`. Identity of holomorphic continuations, plus explicit pole removal, establishes a **unique entire completed ξ(s)**; it is not a conclusion about signs of an unknown Weil operator.

Mathematical E proves universal source laws with a finite derivation, then can evaluate the model at any designated non-pole argument using a convergent finite integral plus controlled tails. This does not mean E physically performs infinitely many observations or that finitely many source readings alone authenticate the real universe.

### Actual theorem imports

Classical ingredients: additive and multiplicative Haar normalization on Q_p, Schwartz–Bruhat functions on the adele ring, Poisson summation on A_Q/Q (Tate's thesis), the real Gaussian Fourier fixed point, Euler product / unique factorization, Jacobi theta modularity, Mellin/Gamma integral, identity theorem, Gamma poles and digamma special values. See NIST DLMF 20.7(viii), 20.10 and 25.5; Tate's thesis; original SUCC dossier `PRIME_FORM_HEAT_MELLIN_SOURCE.md` §3–5 and `COMPLETED_WEIL_SOURCE_TRANSPORT.md` §1–6. The present tests **do not** re-prove adelic Poisson from first principles.

## 1. SI-01: the local p places and real place have ONE original diagonal source (CLASSICAL / PROVED elementary identities)

Let `A_Q=R ×' ∏_p Q_p` be the restricted adeles. At the real place choose `f_∞(x)=exp(-πx²)`; at each **actual prime** p choose `f_p=1_{Z_p}`. For a rational q, all local finite filters satisfy

    ∏_p 1_{Z_p}(q) = 1 if q in Z, and = 0 otherwise.                 (SI1)

**Proof:** Write q=a/b in lowest terms, b>0. For each p, q∈Z_p iff p∤b. Thus all p accept q iff b=1. A finite set P can be fooled by q=1/ℓ for any prime ℓ outside P: all observed finite models say integral, while the original rational q is not in Z. The infinite family of local tests identifies Z relative to the **known full rational source and its factorization law**, not through a physical infinite scan.

The rational diagonal product formula is likewise source-fixed:

    |q|_∞ ∏_p |q|_p = 1                                           (SI2)

with only finitely many nonunit contributions for any q. Tested for signed rational mixtures, not promoted to an arbitrary-idele norm identity.

Normalize multiplicative Haar on Q_p^× so `vol(Z_p^×)=1`. For Re(s)>0 the genuine finite-place test integral is

    Z_p(s) = ∫_{Q_p×}1_{Z_p}(x)|x|_p^s d×x
           = ∑_{k>=0}p^{-ks} = (1-p^{-s})^{-1}.                  (SI3)

For integer s>=1 exact Fraction truncated shells give tail `p^{-s(K+1)}/(1-p^{-s})`; fake composite 6 is not a local prime. The real Mellin integral with `d×x=dx/|x|` is

    Z_∞(s) = ∫_{R×}exp(-πx²)|x|^s dx/|x|
           = π^{-s/2} Γ(s/2) = Γ_R(s), Re(s)>0.                    (SI4)

The infinite finite product `∏_p Z_p(s)` is ordinarily convergent only when Re(s)>1, and there equals ζ(s). The completed product `Λ(s)=Γ_R(s)ζ(s)` therefore initially has the unambiguous open domain Re(s)>1. **Gamma occurs exactly once after assembling the finite places**; one Gamma per Euler prime changes the object (see inherited PR #69 PH-13–15).

## 2. SI-02: model-to-model interaction is global Poisson transport (CLASSICAL)

On diagonal rationals the source Schwartz–Bruhat tensor restricts by (SI1) to

    ∑_{q∈Q} f_t(q) = ∑_{n∈Z} exp(-π t n²) = Θ(t), t>0,

where `f_t=(exp(-π t x_∞²),1_{Z_2},1_{Z_3},...)` and the real test is obtained by a positive scaling, not a new finite source. Choose the standard global additive characters and self-dual Haar normalizations so `1_{Z_p}` is locally Fourier-self-dual and the real Gaussian transforms by `t↔1/t` with factor `t^{-1/2}`. The **adelic Poisson summation theorem**, an established import with these exact hypotheses, supplies

    Θ(t) = t^{-1/2} Θ(1/t).                                       (SI5)

This is the source/observer *2-cell*: the lattice count after Fourier change agrees with the dual lattice count on the **same original rational diagonal**, not merely a fitted equation. Replacing the 2-adic source `1_{Z_2}` by `1_{2 Z_2}` selects even integers and changes the dual Haar/conductor factor: `Θ(4t)=(2√t)^{-1}Θ((4t)^{-1})`. An unchanged self-dual normalization would be a false diagram.

Poisson (SI5) and the Euler factorization (SI3) are different legitimate mathematical models of one source. They are compatible via the Mellin overlap **only** on the initially justified open region Re(s)>1. The new continuation comes from the Poisson side, not pointwise convergence of an Euler product in the critical strip.

## 3. SI-03: the exact completed analytic gluing theorem (CLASSICAL, derived)

Put `ψ(t)=∑_{n>=1}e^{-π n²t}=(Θ(t)-1)/2`. For Re(s)>1, one Mellin/Gamma gate gives

    Λ(s)=Γ_R(s)ζ(s)=∫_0^∞ ψ(t)t^{s/2-1}dt.

By (SI5),

    ψ(t)=t^{-1/2}ψ(1/t)+(t^{-1/2}-1)/2.

Split the integral at t=1, apply this identity for t<1 and change t↦1/t. This yields the **same source** in a new convergence geometry:

    Λ(s)=1/[s(s-1)]+J(s),
    J(s)=∫_1^∞ ψ(t)[t^{s/2-1}+t^{(1-s)/2-1}]dt.                (SI6)

For each compact complex s-set the integrand and every s-derivative have an absolutely integrable Gaussian majorant. Thus J is **entire**, and

    ξ(s)=1/2+1/2 s(s-1)J(s)                                       (SI7)

is entire and satisfies ξ(s)=ξ(1-s) on ALL C. It agrees with `1/2 s(s-1)Γ_R(s)ζ(s)` on Re(s)>1 and therefore is its UNIQUE holomorphic continuation by the identity theorem. This is classical Jacobi/Tate theory, not a novel proof of anything about nontrivial zeros.

It is crucial to distinguish ξ (entire) from ζ (meromorphic) and Λ (meromorphic with poles at 0 and 1). For s away from their normalization singularities,

    ζ(s)=2 ξ(s)/[s(s-1)Γ_R(s)]

is the source-identified meromorphic continuation, not a convergent prime sum at that point.

## 4. SI-04: exact rational analytic-tail and derivative certificates on vertical strips (PROVED LOCAL)

For a finite model `ψ_N(t)=∑_{1<=n<=N}e^{-πn²t}` and integer endpoint T>=1, let

    J_{N,T}(s)=∫_1^T ψ_N(t)[t^{s/2-1}+t^{(1-s)/2-1}]dt.

Fix real bounds σ_-≤Re(s)≤σ_+, with **no restriction on Im(s)**, and set

    B=max(0,ceil(σ_+/2-1),ceil((1-σ_-)/2-1)).

For r=0,1,2, using |log t|^r≤t^r on t≥1, and the derivative factor `2^{-r}`,

    |J^(r)(s)-J_(N,T)^(r)(s)|
     ≤ (4/2^r)[I_(B+r)(3(N+1)²,1)+I_(B+r)(3,T)],              (SI8)

where `I_m(λ,L)=∫_L^∞t^m e^{-λt}dt`. The proof uses `π>3`, `∑_{n>N}e^{-πn²t}≤2e^{-3(N+1)²t}` and `ψ(t)≤2e^{-3t}`. All these estimates hold for t≥1. Repeated integration by parts yields

    I_m(λ,L)=e^{-λL} ∑_(j=0)^m [m!/(m-j)!] L^(m-j)/λ^(j+1).       (SI9)

The exponential is bounded entirely in **exact rationals**, for integer M>=1, via `exp(-x)≤(M/(M+x))^M`. The implementation produces an outward positive Fraction upper bound for (SI8), with NO floating-point numerical sign assumption and no nontrivial-zero input. The bound is **uniform along the entire vertical strip for J and its derivatives**, because `|t^{iy}|=1`. Multiplication by `s(s-1)` means a ξ/ξ'/ξ'' bound must additionally specify `|s|≤R` (code checks this condition).

**Critical distinction:** the error bound certifies omitted theta modes and the omitted `t>T` integral. It does **not** certify a finite numerical quadrature for the remaining `[1,T]` integral. A separate 65-digit mpmath oracle cross-checks seven complex arguments and ξ' against independently evaluated ζ, with errors below the rigorous *tail* envelope; its quadrature is explicitly labeled numerical. To claim full complex interval evaluation, a certified bounded-domain quadrature must still be implemented. Never infer a zero-free disk from an uncertified complex midpoint.

### SI-04b: completely certified finite-integral enclosures on a non-Euler real cross-section (PROVED LOCAL)

We went beyond the theta **tail-only** bound: on the real arguments `s∈{1/2,-2,3}`, every individual finite theta integrand is strictly decreasing for `t≥1`. Indeed its summands have the form `e^{-π n²t} t^b`, with `b∈{-3/4,-2,+1/2}`; the logarithmic derivative is `b/t−πn²<0`, using only `π>3`. Therefore the exact right/left endpoint Riemann sums on a rational grid furnish a **two-sided enclosure** for the entire finite integral:

    Δ∑_(j=1)^M f(t_j) ≤ ∫_1^T f(t)dt ≤ Δ∑_(j=0)^(M-1)f(t_j),
    t_j=1+jΔ, Δ=(T-1)/M.

Every sampled `e^{-π n²t_j}` is enclosed with **outward rational arithmetic**, using Machin's formula for π, finite positive exponential Taylor series with a geometric remainder, and interval recursion along the grid. Every `t_j^(1/2)` and `t_j^(1/4)` is enclosed using integer-square-root bounds. These are not `mpmath` approximations or floating-point signs. Add SI-04's certified omitted-theta tail to the *upper* Riemann sum; the missing tail is nonnegative and cannot lower the integral. Finally propagate through `ξ(s)=1/2+s(s-1)J(s)/2`, reversing endpoints when the prefactor is negative.

The proof works on the stated real points and parameter ranges; it does **not** certify arbitrary complex integrals. The program `observational_succ/source_model_interval_quadrature.py` provides the complete rational endpoints and rejects unsupported arguments. With `N=2` integer modes, `T=8`, and `M=1024` rational subintervals, independently generated exact rational intervals have these approximate decimal displays (the stored **Fraction bounds**, not these displays, are proof witnesses):

| Real input | Certified `ξ(s)` interval, displayed decimally | Independent reference (numeric only) |
|---|---|---|
| `s=1/2` | `(0.49708368544, 0.49715754336)` | `0.497120778188314...` |
| `s=-2` | `(0.57305752989, 0.57483012814)` | `0.573939894046755...` |
| `s=3` | `(0.57305752989, 0.57483012814)` | `0.573939894046755...` |

The exact certificates for `s=-2` and `s=3` are **identical**, because their source integrands coincide termwise: one concrete instance of transporting an analytic truth across the critical strip using a common source. The intervals separately prove `ξ(1/2)>0`, `ξ(-2)>1/2` and `ξ(-2)=ξ(3)` (the equality is an analytic theorem; identical intervals alone would not prove equality).

**Hostile falsification saved:** an initial proposed midpoint source weight incorrectly used `t^{-3/4}+t^{-5/4}` instead of the *actual* `2t^{-3/4}`. Its purported enclosure excluded the independently computed value of `ξ(1/2)`, and it was rejected and repaired. The regression now checks the midpoint integrand at `t=1,16` and both real dual arguments. This is a proof-first example of why a valid finite integral bound requires the **correct** source model, not just correct interval arithmetic.

## 5. SI-05: the finite-prime modular obstruction is sharp (PROVED LOCAL; quantified nonuniformity)

Let P be ANY **fixed finite** set of actual primes, r=#P, and S(P) its P-smooth positive integers. Define

    Θ_P(t)=1+2∑_{n∈S(P)}e^{-πn²t}.

Each local Euler model is genuine and convergent for Re(s)>0, with `∫ Θ_P` giving `Γ_R(s)ζ_P(s)` and `ζ_P(s)=∏_(p∈P)(1-p^{-s})^{-1}`. But the local models do NOT carry the global lattice Poisson law.

**Theorem (sharp normalized defect):** for `t_h=4^{-h}`,

    lim_(h→∞) 2^{-h}[Θ_P(4^{-h})-2^h Θ_P(4^h)]=-1.            (SI10)

**Proof with a finite rational certificate.** Since p≥2, at most `(h+1)^r` distinct P-smooth integers are ≤2^h. Partition n>2^h into dyadic shells `2^(h+j)<n≤2^(h+j+1)`; each has at most `(h+j+2)^r` P-smooth integers and `exp(-πt_h n²)≤exp(-3·4^j)≤20^{-(j+1)}`. The last inequality uses the independently certified rational Taylor fact `∑_(k=0)^8 3^k/k! >20`, hence `e^3>20`, and `4^j≥j+1`. Therefore

    Θ_P(4^{-h}) ≤ 1+2[(h+1)^r+(h+2)^r∑_(m≥1)m^r/20^m].       (SI11)

The sum is a convergent rational power series; the code bounds it from above by a finite exact Fraction prefix plus a certified contractive geometric tail. It follows that `2^{-h}Θ_P(4^{-h})→0`. Also `Θ_P(4^h)→1`, since it lies between 1 and `1+4exp(-3·4^h)`. Therefore (SI10).

By contrast, at each **fixed** t>0, monotone addition of all prime places gives `Θ_P(t)→Θ(t)`, and the full Θ has exact modular defect zero. Thus the two directed limits DO NOT commute:

    lim_(P↑all primes) lim_(h→∞) normalized_defect = -1,
    lim_(h→∞) lim_(P↑all primes) normalized_defect =  0.      (SI12)

This is a genuinely quantitative source-observer obstruction: arbitrarily many individually lawful finite Euler models cannot be promoted to a **uniform modular completion** by extrapolating their internal dynamics. A new global interaction theorem (SI5) is indispensable. We do not claim (SI10) is a new classical number-theory theorem; its exact envelope and SUCC scope are new-to-project.

A second obstruction is at s=0. For r>=1, ζ_P has pole order r there and Γ_R has a simple pole, so the finite-place completed Mellin object has pole order r+1, whereas the genuine Λ(s) has only a simple pole. Local place models do not already encode the required global regularization. A fake modular factor cannot repair this while preserving the Euler overlap.

## 6. SI-06: exact analytic truths OUTSIDE the Euler region, derived without zero data

### 6a. Real critical segment: a uniform strict ξ bound (PROVED LOCAL)

For real `0≤s≤1`, both powers of t in J(s) are ≤1. Since `π>3`, `n²≥n`, and `e³>20`,

    ψ(t)≤∑_(n>=1)e^{-3nt}=e^{-3t}/(1-e^{-3t})<2e^{-3t}

for t≥1. Hence `0<J(s)<4e^{-3}/3<1/15`. Using `0≤s(1-s)≤1/4` in SI7 gives

    ξ(s)=1/2 - s(1-s)J(s)/2 > 1/2-(1/8)(1/15)=59/120.        (SI13)

Consequently **ζ(s)<0 for every real 0<s<1**, because Γ_R(s)>0 and `s(s-1)<0` there. This is a classical fact obtained with a concrete zero-independent SUCC real-source certificate. It is NOT a vertical-strip zero-free theorem and does NOT imply RH.

### 6b. Trivial zeros, residues and negative-integer derivatives (CLASSICAL derived)

For real s<0, J(s)>0 and s(s-1)>0, hence ξ(s)>1/2. Since Γ_R(s) has simple poles at s=0,-2,-4,..., the unique meromorphic ζ source satisfies

    ζ(-2m)=0, m>=1, each zero simple; ζ(0)=-1/2;
    Res_(s=1) ζ(s)=1.                                           (SI14)

Using the Gamma pole residue and ξ(-2m)=ξ(2m+1), and then the **convergent** Euler definition of ζ(2m+1), yields the exact classical identity

    ζ'(-2m)=(-1)^m (2m)!/[2(2π)^(2m)] ζ(2m+1), m>=1.          (SI15)

This explicitly transports true positive-half-plane prime arithmetic to derivative data at each negative trivial zero, entirely through model interactions. For m=1, `ζ'(-2)=-ζ(3)/(4π²)`. No nontrivial zeros enter.

### 6c. Full meromorphic continuation of the PRIME CURRENT (CLASSICAL derived)

On Re(s)>1, the source Euler identity gives `∑Λ(n)n^{-s}=-ζ'/ζ(s)`. By differentiating the source-identified completed relation, the same function continues meromorphically as

    -ζ'/ζ(s)=-ξ'/ξ(s)+1/s+1/(s-1)
             +[ψ_digamma(s/2)-log π]/2.                         (SI16)

Its poles must be treated as meromorphic singularities; finite evaluation at an unknown zero cannot be asserted without a separate nonvanishing certificate. **Do not read (SI16) as convergence of the Euler prime-power series in Re(s)≤1.** This is precisely the distinction between E deriving an analytic statement internally and E physically traversing all primes.

### 6d. The exactly matched Suzuki contact constant (CLASSICAL; source bridge)

By symmetry `ξ'(1/2)=0` and SI13 assures `ξ(1/2)>0`. At the symmetry point the pole logarithmic derivatives `1/s+1/(s-1)` cancel, hence

    2 ζ'(1/2)/ζ(1/2) = log π - ψ_digamma(1/4)
       = γ + π/2 + 3log2 + log π = C_G.                        (SI17)

This **equals the original Suzuki/Carleman Gamma scalar** `C_G` in the sibling `SUZUKI_MARKOV_GLUING_ROUND.md` and source-proved real-place operator, with no unknown-zero input. The digamma special value is classical. This matches the mathematical source; it is not itself a novel dominance bound, positivity criterion, or RH proof.

## 7. SI-07: model interaction *must* be source faithful (EXACT countermodels)

(a) Finite P modular defect SI10. (b) A finite set of p-adic integrality probes aliases the noninteger rational `1/ℓ` at an unseen prime. (c) Changing `1_{Z_2}` to `1_{2 Z_2}` changes the additive Fourier dual conductor and real lattice; ignoring it produces an incorrect theta relation. (d) Composite 6 has valid generic affine/mixed-radix dynamics but no independent primitive Euler place. (e) The model

    ξ_fake(s) = [1+10s(s-1)] ξ(s)

is entire, symmetric under `s→1-s`, and satisfies `ξ_fake(0)=ξ_fake(1)=1/2` but has EXTRA off-critical real zeros at `(1±sqrt(3/5))/2`. It disagrees with the authentic Euler/Mellin source already at s=2, where the multiplier is 21. This **REFUTES** the assertion that reflection symmetry and endpoint normalization alone determine the arithmetic completion. It does not construct a competing ζ with the original local Euler factors.

(f) Finite certified theta *tail* plus uncertified quadrature is not a full pointwise complex interval. (g) A positive-Gamma representation is not completed signed Weil positivity. In particular none of these results settles the sign of Suzuki's full operator for every a, nor his conditional global spectral limit equation (1.12).

## 8. Algebraic structure for E's model-of-model program

The useful categorical object is a diagram of **source-indexed partial operators with contracts**, not one vertex labelled infinity:

    Q diagonal source --[local Zp integral place gates]--> Z_lattice
           |                                              |
       integer factorization                            Poisson + Fourier
           |                                              |
           v                                              v
       Euler product (Re>1) ----[ONE Gaussian Mellin]--> Λ(s) on Re>1
                                                          |
                                                    overlap uniqueness
                                                          |
                                                          v
                                               completed entire ξ(s)
                                                          |
                                   Gamma/pole correction + log derivative
                                                          |
                                                          v
                                               meromorphic prime current

The **2-cell** is the Poisson/Mellin overlap equality, not a freely invented commutator. The Gamma and finite-prime models are typed separately; where their actions are not naturally intertwined the boundary term/conductor must be retained. The model interaction adds certified facts to E's **mathematical** knowledge without altering its original carrier or promoting finite observations to an actualized infinite process. The square does not magically give RH: that still requires a true completed Weil sign theorem or an equivalent alternative.

## 9. Reproducibility and next verdict-changing theorem

- Core source/finite identities + rational analytic-tail bounds: `observational_succ/source_model_interaction.py`.
- 42 exact regression methods across `tests/test_source_model_interaction.py` and `tests/test_source_model_interval_quadrature.py`; independent finite-P product enumerator and certified real-point quadrature.
- Freeze/replay: `scripts/source_model_interaction_probe.py` + `SOURCE_MODEL_INTERACTION_RECEIPT.json`, including `ξ(-2),ξ(3),ξ(1/2)` exact rational brackets.
- Independent 65-digit numerical oracle (NOT a quadrature certificate): `scripts/source_model_analytic_oracle.py` + `SOURCE_MODEL_ANALYTIC_ORACLE.json`.
- Claim ledger: `docs/CLAIM_SUPPLEMENT_SOURCE_MODEL_INTERACTION.md`.
- Scoped downstream RH handoff candidate, NOT forwarded into the separate RH repository: `handoffs/rh/2026-10-14-source-model-analytic-gluing.md`.

**The next non-classical target:** extend the present **real-point** fully rational quadrature to a *fully interval-certified complex finite theta integral* with source-authenticated analytic derivatives (not merely missing-tail intervals). Combine its interval enclosure with a zero-count/nonvanishing certificate on a declared compact contour and an independent completed Weil-form gluing with the correct test domain. A contour certificate can establish bounded-region facts but never substitute for the global `all a` sign or Suzuki compact-uniform operator limit. Repeat the entire construction for a properly completed non-Euler control (e.g. Davenport–Heilbronn), where the functional equation alone is insufficient and the original Euler source gate must refuse.

**External references:**

- NIST Digital Library of Mathematical Functions, [theta modular and Fourier transformations](https://dlmf.nist.gov/20.7#viii), [theta Mellin](https://dlmf.nist.gov/20.10), [zeta integral/continuation](https://dlmf.nist.gov/25.5), [Gamma reflection and special values](https://dlmf.nist.gov/5.5).
- Tate's thesis / additive Fourier on adeles, local zeta integrals and Poisson summation. Exposition: https://web.stanford.edu/~dkim04/blog/tate-thesis-1/ .
- Suzuki, [*Weil's quadratic form via the screw function*, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3).
- Parent SUCC, `research/2026-10-14/PRIME_FORM_HEAT_MELLIN_SOURCE.md` (PH source/gluing) and `research/2026-10-14/COMPLETED_WEIL_SOURCE_TRANSPORT.md` (completed signed form). Sibling `research/2026-10-14/SUZUKI_MARKOV_GLUING_ROUND.md` under PR #70 (Carleman first prime). No assumption that PR #70 is an ancestor of this branch.

---

## 10. SI-13–16: a genuinely DIFFERENT all-place character model — χ₄ and the Γ/PRIME-SPHERE bridge

**Research addendum, 2026-10-14.** This directly tests whether our model interaction construction is general enough to respect an independently specified finite-place parity/conductor source. It does not change the original ζ model, SUCC physical source claims, completed Weil form, or RH status. The classical modular theta/Dirichlet beta theory is an IMPORT with exact source-signed finite proofs and independent numerical controls.

### SI-13 — true prime-local χ₄ source and the indispensable ramified place (CLASSICAL / EXACT source tests)

Take the primitive, nonprincipal **odd** Dirichlet character of conductor 4:

    χ₄(n) = 0 if n is even,
            +1 if n ≡1 mod 4,
            −1 if n ≡3 mod 4.

At all unramified odd primes, the original character has the genuine Euler local factor `(1−χ₄(p)p^{-s})^{-1}`. The place p=2 is **RAMIFIED**, and its Euler local factor is 1—not the same unramified local setup as ζ's `1_{Z₂}`. The real local Gamma/parity factor is

    Γ_χ₄,R(s)=(4/π)^((s+1)/2) Γ((s+1)/2),
    Λ_χ₄(s)=Γ_χ₄,R(s) β(s),
    β(s)=∑_(n>=1) χ₄(n)n^{-s}, Re s>1.

The source's complete multiplicativity and prime-vs-composite controls are verified exactly. This is not an arbitrary interchange of Gamma models: the conductor `q=4` and odd parity `ε=1` originate with the specified primitive χ₄ and its local Fourier law. The finite Gauss sum, computed exactly in Gaussian integers, is

    τ(χ₄)=∑_(a mod4)χ₄(a)i^a = 2i,
    ε_root=τ(χ₄)/(i^ε sqrt4)=1.                                 (SI18)

A composite dilation such as 6 does NOT become a primitive Euler place; a wrong *even*-parity theta would vanish identically because χ₄(-n)=−χ₄(n).

### SI-14 — signed theta interaction yields an entire different completion (CLASSICAL)

The correct odd source theta is

    Θ_χ₄(t)=∑_(n∈Z) nχ₄(n) exp(−πn²t/4)
            =2∑_(n>=1)nχ₄(n)exp(−πn²t/4).

The primitive χ₄ finite Fourier/Gauss law (SI18), plus Gaussian Poisson on the same lattice source, supplies the classical transformation

    Θ_χ₄(t)=t^{-3/2} Θ_χ₄(1/t).                             (SI19)

Compare ζ's theta exponent `-1/2`: **the parity changes the source's scaling dimension**. For Re s>1, ordinary Mellin gives

    Λ_χ₄(s) = (1/2)∫_0^∞ Θ_χ₄(t)t^((s+1)/2-1)dt.

Split at t=1 and apply (SI19). Unlike the ζ case, there is no scalar zero-mode pole: `nχ₄(n)=0` at n=0. We obtain an entire, symmetric continuation

    Λ_χ₄(s)=(1/2)∫_1^∞ Θ_χ₄(t)[t^((s-1)/2)+t^(−s/2)]dt,
    Λ_χ₄(s)=Λ_χ₄(1−s).                                       (SI20)

For every real t≥1 the series defining Θ_χ₄ is a strictly positive alternating series with monotonically decreasing term magnitudes: the ratio of successive terms is bounded by `3e^{-2πt}<1`, using `π>3`. For 0<t<1, (SI19) transports positivity back from 1/t. Hence Θ_χ₄(t)>0 for all t>0, and the completed Λ_χ₄(s) is **strictly positive at every real s**. In particular, the Gamma poles at `s=-1,-3,...` are cancelled by **simple** trivial zeros of β there. This is a classical analytic fact derived without reading any nontrivial zeros.

**Explicit source difference:** from the beta(1)=π/4 Leibniz series, the root-one symmetry gives `Λ_χ₄(1)=Λ_χ₄(0)=1`, so `β(0)=1/2`. This illustrates why a parity-blind Gamma chart cannot reproduce the right analytic statements.

### SI-15 — certified character-tail enclosures, all imaginary ordinates (PROVED LOCAL)

The odd source is signed, so we cannot use the positive θ tail unchanged. Absolute values satisfy, for t≥1,

    |Θ_χ₄(t)|≤2∑_(n>=1)n e^{-πn²t/4}≤8e^{-3t/4}.

For N≥1 the omitted n>N terms satisfy

    |Θ_χ₄(t)−Θ_χ₄,N(t)|≤4(N+2)e^{−3(N+1)²t/4}.

**Proof:** replace n² by n in the first bound and by `(N+1)n` in the second; the resulting weighted geometric sums are bounded using `exp(3/4)>2`, certified by a finite rational exponential Taylor polynomial, and `π>3`. No assumption that a signed Euler factor is a positive measure is made.

For σ_-≤Re(s)≤σ_+, let

    B=max(0,ceil((σ_+−1)/2),ceil(−σ_-/2)).

Then for r=0,1,2,

    |Λ_χ₄^(r)(s)−Λ_χ₄,N,T^(r)(s)|
     ≤2^{-r}[4(N+2)I_(B+r)(3(N+1)²/4,1)
              +8 I_(B+r)(3/4,T)],                            (SI21)

where `I_m` and its exact rational exponential enclosure are defined in SI-04. This is **uniform along the entire vertical strip** because the oscillatory factors have absolute value 1. It bounds missing theta modes/time tail; it does NOT certify the finite complex quadrature. The implementation uses exact rational values and has hostile signed-factor controls.

### SI-16 — PRIME-SPHERE chiral diagonal meets a negative trivial-zero derivative (CLASSICAL; cross-branch source identity)

The older PRIME-SPHERE PR #68 constructs the auxiliary signed chiral Gamma-kernel difference `C=B_+−B_-`, whose diagonal is exactly

    k_C(0)=4∑_(j>=0)[1/(4j+1)^2−1/(4j+3)^2]
          =4β(2)=4 Catalan.                                    (SI22)

From (SI20), the pole of Γ((s+1)/2) at s=-1 has residue 2, and Λ_χ₄(-1)=Λ_χ₄(2). At s=2,

    Λ_χ₄(2)=(4/π)^(3/2)Γ(3/2)β(2)=4β(2)/π.

Therefore the negative trivial-zero derivative is

    β'(-1)= Λ_χ₄(-1)/2 = 2β(2)/π,

and the chiral diagonal becomes

    **k_C(0)=4β(2)=2πβ'(-1).**                            (SI23)

This is an exact new-to-SUCC **source-interaction bridge** across two independently developed models: one Gamma-mode operator, one conductor/parity-correct all-place analytic continuation. Every special-function identity is classical; no new number-theoretic theorem or Weil positivity is inferred. The sibling PRIME-SPHERE branch is not imported or silently merged into this child.

**Independent oracle:** `scripts/source_character_analytic_oracle.py` tests the true finite Gauss/modular law, completed Λ_χ₄ across seven Euler and non-Euler complex arguments, and the Catalan/β'(-1) relation at 60 digits. It uses signed θ integrals plus `mpmath.dirichlet` reference evaluations (not nontrivial zero inputs). The numerical errors fit the independent rigorous SI21 *omitted-tail* envelope, but finite quadrature is explicitly not certified. The exact source and 12 new regression methods are in `observational_succ/source_character_interaction.py` and `tests/test_source_character_interaction.py`; frozen source and numeric receipts accompany them.

**Math-falsifying negative controls:** wrong χ parity annihilates the unweighted theta; fake composite 6 is not a primitive prime; p=2 must be treated as ramified; signed local p≡3 factor cannot be called positive local mass; wrong Γ(s/2) rather than Γ((s+1)/2) fails the theta scaling/source law. This is a constructive successful alternate-character test, not the requested completed non-Euler Davenport–Heilbronn stress test. That remains a downstream obligation.
