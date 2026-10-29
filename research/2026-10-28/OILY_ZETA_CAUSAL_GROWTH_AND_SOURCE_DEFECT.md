# Operation OILY → PÓLYA → SUCC: source-marked prime wavefronts and the additive observer obstruction

**Date:** 2026-10-28. **SUCC target:** child of draft PR #347 (`research/origin-locked-oily-prime-frames-2026-10-28@8345ce2854663b1c40924db5d4efe020bcad521c`), itself descended from PRs #346 and #344; Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`. **No original imported source, zero seed, archived receipts, theorem IDs or main edits.** Local exact tests + independent symbolic checks, not a Lean/full-suite/academic-priority certificate. **π normality and RH OPEN.**

## 0. Mathematical steelman: what is actually being generated?

The author's proposal is that the *origin-locked* Oily two-mode source is the first finite causal atom of a family of prime-indexed virtual wavefronts. Require (i) preservation of the original integer n and its prime factorization, (ii) correct Oily endpoint *and* full-x packet probabilities, (iii) lawful local one-step generation of the path prior, (iv) separate proof whether the observer transport carries probabilities, Hilbert amplitudes or actual expanding zero-seeded BBP circle phases, and (v) hostile controls against a forged source. We do NOT assert a physical Pólya urn inside BBP, fundamental hbar, a new gauge law of nature, or a signed Weyl estimate from positive probabilities.

Source provenance: the actual SUCC positive BBP packet source has `u=x-x²/2`, `v=x²/2`, `p_j=(1-x)/4 Σ_{k=0}^j u^k v^(j-k)` and endpoint `w_j=(j+1)/2^(j+2)`. Source-specific signed forcing is **separately** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)=(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]`. The source-indexed phase is `f_h(n)=exp(2π i h U_n)` with `U_0=0`, `U_n=16 U_(n-1)+r(n)`. None is redefined by this work.

Prior SUCC source identities: `research/2026-10-28/WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md` (WOC-01..), `research/2026-10-28/ORIGIN_LOCKED_OILY_ZETA_FRAME_DOSSIER.md`, `research/2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md` (RSFP-01..05), `research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md` (lawful quotient/source labels). All are reused, not replaced.

## 1. WCG-01: unique *local* Oily packet compiler (PAPER-PROVED, exact Fraction checks)

Let `0<x≤1`, `u=x-x²/2`, `v=x²/2` and `h_j=Σ_{k=0}^j u^k v^(j-k)`. The source-conditioned terminal law of the *two independent constructed geometric wait variables* is

`P_x(J=j,K=k)=(1-u)(1-v) u^k v^(j-k)`, for `j≥0` and `0≤k≤j`,

where `J=K+L` and `K,L≥0`. The source grade law is `q_j=(1-u)(1-v)h_j`. Conditional on reaching grade j with no stopping, require the split law

`μ_j(k)=u^k v^(j-k)/h_j`.

We construct a causal Markov path `(j,k)` with only two permitted births `(j+1,k)` or `(j+1,k+1)` and stop decision independent of k given grade j.

**Stop hazard:** Let `C_j=P(J≥j)`; then

`C_j=[(1-v)u^(j+1)-(1-u)v^(j+1)]/(u-v)` if `u≠v`,

`C_j=u^j[(j+1)-ju]` if `u=v`, with `C_0=1`.

The required stop chance is `s_j=q_j/C_j`. The continue chance is `C_(j+1)/C_j`.

**Unique nearest-neighbor local allocation:** Let `a_(j,k)` be the chance of adding the next excitation to the first channel. CDF conservation forces

`F_j(k)-F_(j+1)(k)=μ_j(k) a_(j,k)`, `F_j(k)=Σ_(i≤k)μ_j(i)`.

Direct simplification gives the unique choice

`a_(j,k)=[Σ_(r=0)^k u^(j+1-r)v^r]/h_(j+1)`, `0≤k≤j`.

Its numerator is a nonnegative subset of the terms in `h_(j+1)`, so `0<a_(j,k)<1` at interior `0<x≤1`. Substitution proves the exact transition law `μ_j -> μ_(j+1)` for all grades. Induction gives **exactly the authenticated normalized positive Oily packets** at every finite stopping grade. At x=0, J=0 almost surely and birth transitions are unobservable/unconstrained; we do not claim uniqueness on unreachable states.

**Scope of uniqueness:** the stop rule is independent of k, the conditional split distributions at EVERY reached grade are fixed, and the only births are k→k/k+1. Relaxing any of these premises permits other hidden-path realizations with identical terminal source distribution. This is an explicit *causal compiler*, not a theorem that the physical BBP observation process uses it.

## 2. WCG-02: exact Oily endpoint as a stopped Pólya urn (PAPER-PROVED; classical ingredients)

At x=1, u=v=1/2. The full-joint grade/split law is

`P(J=j,K=k)=2^(-j-2)` for `k=0,...,j`; `P(J=j)=(j+1)/2^(j+2)`.

The local compiler reduces to the one-red/one-blue *Pólya urn*:

`a_(j,k)=(k+1)/(j+2)` and `s_j=(j+1)/[2(j+2)]`.

This is a nontrivial, fully explicit, causal construction of the actual Oily packet law. A legitimate finite prefix is generated online; the completed packet distribution arises from the limit. The reinforcement law is classical (beta-binomial with parameters 1,1); the identification with the SUCC Oily terminal distribution and the exact stopping hazard is the source-specific synthesis. It does not assert that the **internal time-ordered microhistory** is the original BBP signed-carry history.

## 3. WCG-03: same local allocation, different stopping: the bridge to every prime (PAPER-PROVED)

Fix `0<q<1`, in a genuine prime-local zeta Gibbs mode `q=p^(-β)` with `p` prime and real β>1. Let the grade J have the *one-mode* geometric law `(1-q)q^j`, and conditional on J=j let K be uniform on `{0,...,j}`. The joint law is

`P_Z(J=j,K=k)=(1-q)q^j/(j+1)`.

The **same Pólya** birth rule `(k+1)/(j+2)` generates all split marginals; only the stop hazard differs: `s_j^Z=1-q`, independently of j.

The balanced **two-mode Oily-type** local law instead has

`P_O(J=j,K=k)=(1-q)^2 q^j`, `s_j^O=(j+1)(1-q)^2/[(j+1)-j q]`.

Thus the *exact Radon–Nikodym ratio* on grade/split states is

`P_O/P_Z=(j+1)(1-q)`.

At `(p,β)=(2,1)` this gives the literal authenticated **local** Oily endpoint `q=1/2`. The global ζ(1) Gibbs state is not normalizable, so this is a strictly local boundary identity. **Oily is the size-biased (by j+1) prime-local zeta path law**; different end-of-wavefront stopping is what changes the single-mode geometric state into the double-mode negative-binomial state. The local split allocation rule is unchanged.

## 4. WCG-04: an all-prime source prior with a certified finite-observer cut (CLASSICAL/PAPER-PROVED)

For real `β>1`, choose independent prime exponents `J_p∼Geom(q_p)` with `q_p=p^(-β)`, and conditionally generate `K_p∈{0,...,J_p}` using the source-preserving Pólya split. Unique factorization sets

`N=Π_p p^(J_p)`, `A=Π_p p^(K_p)`, `B=Π_p p^(J_p-K_p)`, `AB=N`.

Since `Σ_p q_p≤Σ_{n≥2}n^(-β)<∞`, only finitely many primes are present almost surely. In fact

`P(N=n)=n^(-β)/ζ(β)` and `P(A=a,B=b|AB=n)=1/d(n)`.

Thus this local-urn construction realizes **the ordinary single-source zeta law with origin-locked paths**, not the double-counted ζ(β)² law. Turning ALL prime-local geometric stopping rules into two-mode Oily-type stopping biases the source by d(n), giving precisely the unrestricted two-mode product ζ(β)²; source identity is not preserved by that change.

For a finite prime cutoff `P≥2`, couple the truncated and complete models using the same prime exponents, setting p>P to zero in the finite model. The total variation discrepancy is at most the probability that any omitted prime is active:

`TV ≤ Σ_(p>P)p^(-β) ≤ Σ_(n>P)n^(-β) ≤ P^(1-β)/(β-1)`.

This bound is exact and explicit for every β>1, and becomes noninformative as β→1+, precisely where global normalization fails. This is a **certified finite observer coverage** theorem, not a physical inflation model.

## 5. WCG-05: classical probability preservation ≠ coherent amplitude preservation (PAPER-PROVED)

At grade j define the column-stochastic Pólya matrix `K_j:C^(j+1)→C^(j+2)` with entries `K_j[k,k]=1-a_(j,k)`, `K_j[k+1,k]=a_(j,k)` and all others zero. It sends the **uniform classical probability** vector to the uniform probability vector exactly:

`K_j 1_(j+1)/(j+1) = 1_(j+2)/(j+2)`.

However, let `ω_j=1_(j+1)/sqrt(j+1)` be the **normalized coherent pure amplitude**. The same *linear matrix* acts as

`K_j ω_j = sqrt((j+1)/(j+2)) ω_(j+1)`.

The squared norm is `(j+1)/(j+2)`; after J grades the product is `1/(J+1)`. This is the same local squared loss observed for naive one-sided prime-fiber raising. Comparing the exact log cost `log(J+1)` with the declared harmonic register clock `H_J` leaves

`H_J−log(J+1)→γ`.

**Critical typing:** K_j is a stochastic matrix and **not a quantum/Hilbert isometry**. Treating probabilities as complex amplitudes is an intentionally hostile control, not a physical process. A genuine coherent quantum implementation needs explicit ancilla/source phase handling and an isometry/CPTP map; the classical Pólya preservation result alone does not provide it. The log-vs-harmonic gamma finite part comes from a declared clock comparison, not a universal physical constant.

## 6. WCG-06: Schwinger SU(2) lives naturally in each prime fiber (CLASSICAL/PAPER-PROVED)

For n=p^j, the origin fiber has basis `|k,j-k>`, `k=0,...,j`, dimension j+1. Introduce

`J3|k>=(k-j/2)|k>`,

`J+|k>=sqrt((k+1)(j-k))|k+1>`,

`J-|k>=sqrt(k(j-k+1))|k-1>`.

Then the standard Schwinger identities hold:

`[J3,J±]=±J±`, `[J+,J-]=2J3`, `J²=j(j+2)I/4`.

This is the canonical spin-j/2 irreducible representation of SU(2), not a newly derived physical ℏ. The origin-locked uniform split has

`E_ω[J3]=0`, `Var_ω(J3)=j(j+2)/12`,

so `Var(log(a/b)|ab=p^j)=[j(j+2)/3] (log p)^2`, matching the previously established origin-locked zeta phase susceptibility coefficient. **No nonzero SU(2)-invariant vector exists for j>0**; thus the original uniformly split source must be transported as a *marked state* under internal rotations, not treated as a gauge-neutral vacuum. The standard spin-coherent binomial-amplitude state is **not** the original uniform split for j≥2.

For general n=Π p^j, the divisor fiber is a finite tensor product of those local symmetric-power representations, with a distinct genuine prime label per factor. This is compatible with SUCC's quaternionic Hopf/SU2 *analogy* at the level of known group theory, not an established BBP quaternionic physical coupling.

## 7. WCG-07: additive SUCC is a **divisor-jump** under origin-locked compression (PAPER-PROVED)

Define J:ℓ²(N≥1)→ℓ²(N≥1×N≥1) by `J|n>=ω_n=d(n)^(-1/2)Σ_(ab=n)|a,b>`, and `C(X)=J* X J`. On pair space let `A_p|a,b>=|pa,b>` for genuine primes p and `S_A|a,b>=|a+1,b>`.

Then **prime** raising stays in the target source fiber:

`C(A_p)|n>=sqrt(d(n)/d(pn)) |pn> = sqrt((j+1)/(j+2)) |pn>`, `j=v_p(n)`.

But the additive first-factor operation acts by

`C(S_A)|n> = 1/sqrt(d(n)) Σ_(b|n) |n+b>/sqrt(d(n+b))`.

The output is a sum over DIFFERENT source integer targets, and

`||C(S_A)|n>||²=[1/d(n)]Σ_(b|n)1/d(n+b) ≤1/2`.

Equality is attained at n=1; n>1 gives strict inequality because the b=n term reaches composite 2n. The genuine |n+1> coefficient is `1/sqrt(d(n)d(n+1))`; along n=2^k this tends to zero. Hence no uniformly bounded *diagonal scalar reweighting of this selected nearest-successor component* can produce the exact isometric SUCC shift S. This does NOT forbid a distinct coherent source-conditioned lift `J S J*`; that lift uses the full globally marked original source rather than only one-factor addition.

## 8. WCG-08: source/observer compression fails to preserve composition (PAPER-PROVED)

For arbitrary pair-space operators A,B,

`C(AB)-C(A)C(B)=J* A (I-JJ*) B J`.

This identity follows by inserting `I=(JJ*)+(I-JJ*)` and using J*J=I. The defect measures information eliminated by an intermediate origin-locked observation.

Concrete exact witness at input |1>, with A=S_A and B=A_2:

`C(S_A A_2)|1>=|3>/sqrt2`,

`C(S_A)C(A_2)|1>=|3>/(2sqrt2)+|4>/sqrt12`.

Therefore

`||(C(S_A A_2)-C(S_A)C(A_2))|1>||²=5/24>0`.

This is a receipt-level obstruction: a genuine source action diagram can be lawful before compression yet fail when an observer forgets the intermediate paths. It directly complements SUCC's existing causal-descent/fiber-congruence requirements.

## 9. WCG-09: an ORIGINAL BBP carry-sensitive *cross-time* observer (EXACT IDENTITY; no cancellation)

On pair space declare the original source-diagonal circle phase operator `F_h|a,b>=f_h(ab)|a,b>`, where

`f_h(n)=exp(2π i h U_n(0))`, `U_n(0)` the **genuine** zero-seeded original four-pole BBP recurrence. Its compressed commutator with first-factor addition is exactly

`C([F_h,S_A])|n> = [1/sqrt(d(n))] Σ_(b|n) [f_h(n+b)-f_h(n)] |n+b>/sqrt(d(n+b))`.

The corresponding positive energy on each source basis input is

`E_h(n) = [1/d(n)]Σ_(b|n)|f_h(n+b)-f_h(n)|²/d(n+b)`.

This is a legitimate original-carry-SENSITIVE cross-time observable. It is **not** a signed Weyl saving: source-selected ∑f_h(n)=o(N) remains unproved, and positive differences alone can certify neither the seed nor normality. The signed values f_h(n) must not be replaced by auxiliary positive packet grades or a synthetic Pisot rotation.

**Two hostile same-forcing changed-seed controls:**

1. For each `s=k/15 (mod 1)`, `U_n(s)=U_n(0)+16^n s`, and `16^n s≡s (mod 1)`. Therefore `f_h(n;s)=exp(2π i h s)f_h(n;0)` for all n. Every *relative-phase-only* observable (including E_h) is identical. A zero-seed authenticity test must retain the absolute origin/source label. This is a true 15-torsion stabilizer of the phase-difference model, not an RH result.
2. The coherent counterseed `s*=−π/16` gives `U_n(s*)=−Σ_(j≥1)16^-j r(n+j)`. The true original rational source satisfies `0<r(m)≤1/m²` for m≥2. A polynomial certificate is

`D(m)-m² A(m)=392(m−2)^4+2201(m−2)^3+4494(m−2)^2+3902(m−2)+1185 >0`.

Thus, for every n≥1, `|U_n(s*)|≤1/[15(n+1)²]` (improving earlier convenient 1/9 bounds), and the commutator energy obeys

`sqrt(E_h(n;s*)) ≤ 4π|h|/[15 sqrt(2) (n+1)²]`.

This is an adversarial *near-zero* energy nonnormal orbit, proving that small cross-time energy alone is not the missing signed BBP normality gate. The all-n proof uses only the displayed original rational forcing and its classical BBP series equality, with no exotic numerical input. The seed s* is a COUNTERMODEL, never an input to any purported proof for s=0.

## 10. WCG claim/validation ledger and independent-priority firewall

| ID | Result | Status | Boundary / next falsifier |
|---|---|---|---|
| WCG-01 | All-x Oily conditional packet birth/stop compiler, unique under local monotone + split-independent stop assumptions | PROVED PAPER + exact tests | Hidden microhistory and physically optimal sensor unverified |
| WCG-02 | Oily x=1 = stopped one/one Pólya urn | PROVED PAPER, CLASSICAL urn | No original BBP carry identification |
| WCG-03 | Zeta prime-local and balanced Oily share Pólya allocation but have different stop hazard; exact size bias | PROVED PAPER | q=1/2 at p=2,β=1 is **local only**, global ζ(1) diverges |
| WCG-04 | Countably many independent prime-urn modes realize ordinary ζ(β) with a finite TV cutoff | CLASSICAL/PAPER-PROVED | β>1, observer prior vs realized path |
| WCG-05 | Stochastic Pólya preserves uniform PROBABILITY but contracts uniform AMPLITUDE, squared loss (j+1)/(j+2) | PAPER-PROVED | Stochastic matrix is not quantum isometry; no physical hbar |
| WCG-06 | Schwinger SU2 spin-j/2 prime fibers with exact Casimir and imbalance variance | CLASSICAL | No natural SU2-invariant source vacuum for j>0 |
| WCG-07 | First-factor additive SUCC compresses to divisor jumps; nearest-S obstruction unbounded | PAPER-PROVED | Other source-aware lifts allowed |
| WCG-08 | Exact nonfunctoriality defect 5/24 | PAPER-PROVED | Not universal curvature, or GR |
| WCG-09 | True selected BBP phase enters a divisor-jump commutator; 15-torsion gauge and coherent seed refute simple gates | EXACT ALGEBRA/PAPER-PROVED | No original fixed-h signed `o(N)` Weyl bound |

Original source, historical supplement namespace registry, Lean and hosted CI remain untouched by the child draft PR. Paper derivations are subject to independent review and are not academic-priority claims. Run `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*growth*.py'` plus the explicit exact test files; `python scripts/oily_prime_growth_independent_oracle.py`. Full SUCC required gates are `AGENTS.md`; no unperformed gate is claimed.

### Sources and previous work

- SUCC main source and prime/FUCC law: https://github.com/femboy2112/SUCC/blob/main/research/2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md
- Oily prior integration: https://github.com/femboy2112/SUCC/blob/main/research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md
- Source-causal observer operator: https://github.com/femboy2112/SUCC/blob/research/pisot-hopf-arithmetic-relativity-2026-10-28/research/2026-10-28/WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md
- Classical one/one Pólya urn distributions: https://www.randomservices.org/random/urn/Polya.html
- Classical Jordan–Schwinger `su(2)` two-boson modes: https://pmc.ncbi.nlm.nih.gov/articles/PMC10743218/
- Standard Euler products and Dirichlet series: https://dlmf.nist.gov/27.4

**Codex research continuation:** `handoffs/CODEX_ULTRA_ORIGIN_LOCKED_GROWTH_2026-10-28.md`.

## 11. WCG-10: authentic BBP Dirichlet wavefront has a zeta pole and exact Gamma–π–silver finite part

**PAPER-PROVED from the original four-pole rational forcing plus classical zeta/digamma identities; academic priority UNVERIFIED.** This is an independently checkable analytic result on the authentic *signed four-pole source*, rather than an arbitrary positive Oily prior or a synthetic zeta Gibbs state.

Define for `Re(s)>-1` the absolutely convergent original-forcing Dirichlet response

`F_BBP(s)=Σ_(n≥1) r(n)n^(−s)`, where

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`.

Its Laurent expansion at infinity starts

`r(n)=15/(64n²)+151/(512n³)+1209/(4096n⁴)+O(n^-5)`.

**Meromorphic continuation theorem.** For every integer M≥2, subtract the first M−1 terms of the rational asymptotic expansion. The residual `r(n)−Σ_(k=2)^M a_k/n^k` is `O(n^(-M-1))`, so the remainder Dirichlet series is analytic on `Re s > −M`. The matching identity

`F_BBP(s) = Σ_(k=2)^M a_k ζ(s+k) + Σ_(n≥1)[r(n)−Σ_(k=2)^M a_k/n^k] n^(-s)`

therefore continues the function meromorphically to that half-plane. These overlap consistently, giving a **global meromorphic continuation** with possible simple poles at negative integers `s=1−k`, residues `a_k`. In particular the poles at `s=−1` and `s=−2` are genuine, of residues `15/64` and `151/512`. This is a standard analytic subtraction method applied source-faithfully; no Riemann hypothesis, nontrivial zero positions or Euler product is used. The signed forcing r(n) is not generally multiplicative.

**Exact principal finite part.** Put `a₂=15/64`. The limit

`C_BBP = lim_(s→−1)[F_BBP(s)−a₂/(s+1)]`

exists. Write

`n r(n) = (7/16)/(n−7/8) − (1/8)/(n−1/2) − (3/64)/(n−3/8) − (1/32)/(n−1/4)`.

The four displayed rational coefficients sum to `15/64`, so

`C_BBP = (15/64) γ + Σ_(n≥1)[n r(n)−15/(64n)]`.

Using `Σ_(n≥1)(1/(n−a)−1/n)=−ψ(1−a)−γ` gives the exact digamma expression

`C_BBP = −(7/16) ψ(1/8)+(1/8)ψ(1/2)+(3/64)ψ(5/8)+(1/32)ψ(3/4)`.

Gauss's digamma theorem at denominator eight then simplifies the result to

`C_BBP = (15/64)γ + ((27+31sqrt(2))/128)π + (39/32)log 2 + (31sqrt(2)/64)log(1+sqrt(2))`.

Numerically, `C_BBP≈3.322497911106404756594732387823797909453952...`. The √2 and silver-log terms result from the **actual eighth-scale pole positions** after digamma reduction, not from an assumed silver-ratio physical oscillator. The γ coefficient is **the residue** `15/64`, because the ζ(s+2) subtraction carries the Euler constant at its pole; this is a concrete analytic bridge from original signed forcing to ζ/Gamma normalization.

**Rigorous finite verification:** the independent oracle `scripts/bbp_dirichlet_finite_part_oracle.py` derives all displayed rational coefficients and digamma identities with exact SymPy algebra and checks the closed formula to 55 decimal places with mpmath. It also verifies a direct N=4000 partial-sum approximation with an explicit tail bound: if `δ_n=n r(n)−15/(64n)`, then from the four partial fractions `|δ_n| ≤ (241/512)/[n(n−7/8)] ≤ (241/64)n^-2`, and hence `|Σ_(n>N)δ_n|≤(241/64)/N`. This bound is conservative but fully elementary. It is not an RH or normality argument.

**Remaining analytical program:** derive the full residue tower and any functional relation (if one exists) from the original source without inventing an Euler product. Study whether the source-specific additive-to-multiplicative commutator has a genuinely *signed* transfer estimate into original fixed-h BBP Weyl sums. Audit priority against classical BBP, Hurwitz, digamma and Dirichlet-series literature rather than claiming novelty by agreement of familiar constants. A nontrivial source-derived estimate or sharp no-go theorem is required for academic significance.

**WCG-10 status:** exact paper proof + independent symbolic/numeric checks, **academic novelty UNKNOWN**, π normality/RH OPEN.
