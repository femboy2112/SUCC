# Balanced prime-clock rescue: 12/5 epoch geometry, Fourier completion, and original signed-lag transport

**2026-11-08, source-specific research extension of TCP-01–07.** The original BBP rational forcing and literal `U_0=0` are frozen. These theorems do **not** prove base-16 normality of π or RH. Mathematical proof claims are paper derivations with explicit classical inputs, not Lean or independent scholarly refereeing. All notation for the channel-resolved original-zero recurrence is inherited from [`PROOFS.md`](PROOFS.md).

## BEC-01: The 4A prime clock loses an exact transverse channel on the actual epoch — PROVED NEGATIVE

Take a prime `p≡1 (mod8)`, `k=(p−1)/8`, and the BBP epoch `J_A=[A,2A)`. The first p-birth is at `k+1`; channel-4 and channel-5 *split* only at `5k+1=(5p+3)/8`, even though both were born together at `k+1`.

If `k+1≤A` and `2A≤5k+1` and the epoch lies in the first complete p-shell, then **for every** `n∈J_A`,

`C_{4,p}(n)=C_{5,p}(n)` exactly in F_p.

Consequently the actual epoch Hermitian phase Gram `M_A,de=A^−1 Σ_(n∈J_A)e_p(h(C_{d,p}(n)−C_{e,p}(n)))` has `M_A,45=1` and the **exact null vector** `(0,1,−1)` for every integer h. It has rank ≤2, no matter how strong the subgroup character estimate is. In particular, every selector `p_A=(4+o(1))A`, `p_A≡1 mod8`, eventually has this null vector, as in the original 4A-style prime clocks of #544. This is a finite exact *observable-rank obstruction*, not a counterexample to π normality. The full `p`-shell frame of TCP-04 is not the same observer as the `[A,2A)` frame.

## BEC-02: Balanced complete four-stage epoch for p≈(12/5)A — PROVED

Choose a prime `p=8k+1` with `9A/4≤p≤5A/2`, and assume `A` is sufficiently large for the explicit inequalities `k+1≤A<4k+1<5k+1<6k+1<2A≤k+1+p` (all automatically valid for `A≥16` when such a p exists). The entire actual epoch is within the **first** simple-pole p-shell; hence the exact channel residue factorization TCP1 applies. Its four chronological stage intervals and sizes are

| Stage | Original epoch times | Exact length |
|---|---|---|
| 1 | `[A,4k+1)` | `4k+1−A` |
| 2 | `[4k+1,5k+1)` | `k` |
| 3 | `[5k+1,6k+1)` | `k` |
| 4 | `[6k+1,2A)` | `2A−6k−1` |

If `p_A/A→12/5`, their normalized masses are

`(w1,w2,w3,w4)→(1/5,3/10,3/10,1/5)`.

This *balanced* clock observes all three transverse pulse births at macroscopic fractions of the epoch. The chronology is derived from original denominators `(8n−7,8n−4,8n−3,8n−2)`, never from a fitted π digit pattern.

## BEC-03: Guaranteed order-qualified prime arbitrarily close to (12/5)A — PROVED WITH CLASSICAL QUANTITATIVE PNT/AP

Fix `C=2`, `B=3`. For all sufficiently large **integer A** there exists a prime

`p_A≡1 (mod8), |p_A−(12/5)A|≤ A/(log A)^3`

with `m_A=ord_(p_A)(16)> sqrt(p_A)/(bitlength(p_A))^2` and `m_A^3>p_A`. No explicit starting A is claimed.

**Proof (prime selection, not a numerical search).** The standard *quantitative fixed-modulus* prime number theorem in progressions modulo 8 counts `~ (2A/log³A)/(4log A)=A/(2log⁴ A)` primes in the stated short window; its classical exponentially small relative error is smaller than the main term. To exclude primes of order at most `sqrt(p)/(bitlength(p))²`, upper-bound their orders by `J_A=O(sqrt A/log² A)` uniformly throughout the window. Every such prime divides the nonzero integer `P_A=∏_{j=1}^{J_A}(16^j−1)`. The elementary bound `log P_A≤(log16)J_A(J_A+1)/2=O(A/log⁴ A)` proves that at most `O(A/log⁵ A)` primes `p≈(12/5)A` can be bad, because each contributes `log p≈log A` to `log P_A`. Thus good primes remain in the window. The cubic order condition is automatic for sufficiently large A because `p^(1/2)/(log p)^6→∞`.

For this selector, #544's **separately imported** Cochrane–Pinner monomial estimate supplies, with explicit classical hypotheses, a uniform subgroup Fourier bound

`δ_(p_A) := max_(c≠0) |m_A^−1 Σ_(u<m_A)e_(p_A)(c16^u)| = O(p_A^(−1/16)(log p_A)^(3/4))=o(1)`.

The exponent and log factor match the C=2 case of #544; this is a **classical imported input**, not a newly proved sum estimate. This result does **not** import #544's single-principal-pole epoch theorem unchanged: the four separate born channels require the next section's fresh incomplete-period analysis.

## BEC-04: Elementary incomplete-cycle completion to genuine macroscopic stages — PROVED WITH CLASSICAL GAUSS SUM

For every prime p, nonzero `c∈F_p`, `m=ord_p(16)` and any integer temporal interval I of L consecutive exponents, write `L=qm+r`, `0≤r<m`. Let `S_j=Σ_(u=0)^(m−1)e_p(c16^u) exp(−2πiju/m)`. The map `16^u→e^(−2πiju/m)` defines a character of `H=<16>≤F_p×`; each such character extends to the cyclic group F_p×. The indicator of H is the average over characters trivial on H, so `S_j` is an average of `(p−1)/m` complete Gauss sums, each of modulus ≤sqrt(p) by the classical finite-field Gauss estimate (the trivial multiplicative character contributes modulus 1). Hence `|S_j|≤sqrt(p)` for *every* j.

Fourier-invert the indicator of an r-long consecutive interval modulo m. Its Fourier coefficients have absolute value bounded by `min(r,m/(2min(j,m−j)))`; consequently their normalized ℓ¹ norm is at most `2+log m`. Therefore the incomplete period contributes at most `sqrt(p)(2+log m)`. The q complete cycles contribute at most `qmδ_p`. Thus:

`|Σ_(n∈I)e_p(c16^n)| ≤ L δ_p + sqrt(p)(2+log m)`.

This bound is **uniform in c and in the starting exponent**, including p-dependent coefficients. The intermediate complete Gauss bound alone would not control *many* full cycles when m<sqrt(p); retaining the separate `δ_p` term is essential.

## BEC-05: Actual-epoch joint Fourier decomposition and nondegenerate Gram — PROVED CONDITIONALLY ON THE SELECTOR/IMPORTS

Write `v_s=v_(0,s)` for the exact rational vectors of TCP3, and `L_s` for the genuine four epoch lengths of BEC-02. For any integer h and integer Fourier mode t∈Z³ put

`c_s=h t·v_s (mod p)`, `w_s=L_s/A`, `ρ_A(t)=Σ_s w_s 1_(c_s=0)`,

`νhat_A(t)=A^−1 Σ_(n∈[A,2A)) e_p(h t·C_p(n))`.

Splitting the **actual**, time-labelled history at all four pole births, with BEC-04 applied to each nonzero mode, gives for *all* (including p-dependent) t and h:

`|νhat_A(t)−ρ_A(t)| ≤ E_A`, `E_A=δ_p+4sqrt(p)(2+log m)/A`.

With BEC-03, `E_A=o(1)` for every integer A→∞. For each fixed t the epoch triple-phase measure thus converges weakly (Fourier character uniqueness) to the four-subtorus mixture with weights `(1/5,3/10,3/10,1/5)` and the **same four exact primitive rational directions** as TCP-03. It is *not* Haar measure on T³.

For the Hermitian 3×3 **epoch** character Gram `M_A`, let `σ_A=(L_1+L_2)/A=(5p+3−8A)/(8A)`. The source-specific resonances imply

`M_A = [[1,0,0],[0,1,σ_A],[0,σ_A,1]] + E^(matrix)_A`, with each off-diagonal entrywise error ≤E_A and zero diagonal error. Hence, from Frobenius and eigenvalue perturbation,

`λ_min(M_A) ≥ 1−σ_A−sqrt(6) E_A`.

Under BEC-03 `σ_A→1/2`, so `M_A→[[1,0,0],[0,1,1/2],[0,1/2,1]]`, eigenvalues `3/2,1,1/2`, and the smallest tends to **1/2**. This **repairs BEC-01's exact missing channel** on a selected BBP epoch, not just on a longer full shell. It does **not** imply that the real complementary phase is independent.

## BEC-06: Balanced epoch supplies #544's local marginal input at every forcing-corrected lag — PROVED REDUCTION

The original diagonal phase is `a_n(k)=e_p(k Σ_d C_(d,p)(n))` for any integer k, with its original zero-seeded real completion `b_n(k)=e(k[U_n−(ΣC modp)/p])`. Their product is *exactly* `e(k U_n)`. Every four-stage scalar pulse sum `(4,7/2,33/10,47/15)` is nonzero modulo primes `p≡1 mod8`, p>5; hence for every k with `p∤k` the diagonal mode is nonresonant in **all four** stages. BEC-05 therefore proves

`|E_(n∈[A,2A)) a_n(k)| ≤ E_A` uniformly for all integers `k` nonzero mod p.

For fixed h≠0, use #544's **exact forcing** `F_ℓ(n)=Σ_(j=1)^ℓ16^(ℓ−j)r(n+j)` and `k_ℓ=h(16^ℓ−1)`. If `1≤H≤m` and eventually p∤h, then p∤k_ℓ for every 1≤ℓ<H. The proof of #544 H2 works verbatim with this **fresh four-stage** marginal (no truncation of later pole births):

`|W_A(h)|² ≤ ((A+H−1)/A)[1/H + R^bal_(A,h)(H) + (1−1/H)E_A + (H²−1)/(3HA)]`,

where `R^bal` is the **actual sign-preserving covariance** of the balanced prime principal part against the real complementary part with full original `F_ℓ`. Set `H_A=min(m_A,floor(sqrt A))`. Then `H_A→∞`, `H_A=o(A)` and all **other** terms vanish. Thus the single still-open requirement is `limsup_(A→∞)R^bal_(A,h)(H_A)≤0` for each fixed h. Its implication to π-normality is proved exactly as in #544, but **its truth is not established**. A p-clock change alone cannot produce signed decay.

## BEC-07: Conditional complement resonance budget, explicit source-dependent countermodels

For the actual p-principal part at each original n, define 
`a_n=e_p(hΣC_(d,p)(n))`, `b_n=e(h(U_n−(ΣC modp)/p))`, so `a_n b_n=e(hU_n)`. For any finite p-dependent trigonometric complement `B_n=Σ_t c_t e_p(h t·C_p(n))`, put `η_A=A^−1Σ|b_n−B_n|`. BEC-05 proves:

`|W_A(h)| ≤ η_A + Σ_t |c_t|[ρ_A(1+t)+E_A]`.

In the large-A fixed-mode limit, the four dangerous affine planes are **exactly TCP-12**, but their weights are now `(1/5,3/10,3/10,1/5)`. The coherent counterfeit `B_n=conjugate(a_n)` has one coefficient `t=(-1,-1,-1)` and `ρ_A(1+t)=1`, so no cancellation follows from the full-rank frame. Rational p-integral seed changes preserve the p-local channels, while changing real characters. The matched-Gamma source mutant of TCP-06 changes the prime birth schedule and is excluded by the exact four-pole source passport. All such controls are logically distinct from the authentic zero-selected complement.

The exact missing estimate is a source-derived bound on `η_A` **and** the four resonant coefficient masses, or a direct original-zero `R^bal≤o_h(1)` estimate. Neither has been proved. The weaker main theorem BEC-05 *already* proves that the full source's local arithmetic channels are visible and nondegenerate on appropriate BBP epochs; it is not a proof of the global real Archimedean normality.

## Sources, independent checks and epistemic boundaries

- **Repository lineage:** #497 PF-01..04 original scalar prime events; #499 eight-tap rational source action; #544 selected Weyl/signed covariance and separately imported Cochrane–Pinner, quantitative PNT/AP; #552 positive source Gram; draft TCP-01…07 three-channel lift. The **new-to-this-branch** result is the balanced epoch clock, prime selector and genuine time-truncated four-stage Fourier reconstruction, not the inherited original scalar p-shell law.
- **Classical Gauss estimate:** L. Babai, *Fourier Analysis*, Theorem 6.6, https://people.cs.uchicago.edu/~laci/reu02/fourier.pdf; independent mathematical source https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf (Gauss bound). **Cochrane–Pinner:** *Explicit bounds on monomial and binomial exponential sums*, Q. J. Math. 62 (2011), 323–349, https://academic.oup.com/qjmath/article-abstract/62/2/323/1529799. All external facts are imported with their hypotheses; author/source priority unverified.
- **Finite scope:** root-discoverable tests verify independent termwise rational source residues and full histograms, exact 4A null-vector control, balanced partition, Gram symmetry and genuine four-plane resonance. Float evaluations are diagnostics, not rigorous signed-lag certificates. The analytic source-selective covariance bound, zero-seed normality and RH remain **OPEN**.

## BEC-08: Explicit all-three-channel-invisible near-coherent rational counterseeds — PROVED HOSTILE CONSTRUCTION

The *entire* source-labelled prime-phase history, including the balanced full-rank Gram, is still seed-blind to any additional rational initial value `s` whose denominator is prime to p. Indeed `pV_(3,n)(s)≡pV_(3,n)(0)` modp if `V_3` alone receives the seed, since `p16^ns≡0` modp; the other two channels are unchanged. Yet the real total state acquires the expanding term `16^n s`.

A fully constructive hostile family needs **no π digits or π oracle**. Fix any integer A≥16 and set `N=2A+10`, `M=8A+80`, and compute **exactly from the original rational four poles**

`α_N=Σ_(j=1)^N 16^(−j)r(j)`, `s_A=−floor(2^M α_N)/2^M`.

Every `s_A` has dyadic denominator, so it is a p-unit for every odd p. The original completed source constant `α=π/16` obeys the elementary tail enclosure from `r(j)<j^−2` (j≥2):

`0<α−α_N ≤16^(−N)/(15(N+1)²)`.

For every original time `n∈[A,2A)`, the exact **seeded** Green identity is `U_n(s_A)+T_n=16^n(s_A+α)`, with `0<T_n≤1/[15(n+1)²]`. Consequently, uniformly over the entire epoch,

`|U_n(s_A)| ≤ 2^(−80) + 16^(−10)/[15(2A+11)²] + 1/[15(A+1)²] =: B_A →0`.

Thus for each fixed integer h, `|W_A(h;s_A)−1|≤2π|h|B_A→0`, **while every three-channel p-character history on this same epoch is exactly the original-zero history** for any odd p (including the balanced p_A). If the balanced local-marginal estimate BEC-06 is applied, the corresponding signed prime/complement covariance of this coherent counterfeit tends to **1**, not zero. This proves an exact source-selected *finite observation nonidentifiability* across epoch-dependent seeds; it does not refute or decide π normality for the fixed genuine seed zero. It extends the earlier #544 rational terminal-shadow control specifically to the entire three-channel balanced prime frame, with a completely explicit no-π-oracle dyadic construction.

**Verdict:** the full-rank balanced local frame is real progress on local observability and cancellation; the missing selected-zero **Archimedean complement** remains unavoidable. Source-typed phase and chronological memory must be transported across that boundary rather than inferred from seed-blind Gram spectra.
