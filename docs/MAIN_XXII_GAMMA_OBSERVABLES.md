# Main XXII — typed Gamma observables

These identities have different domains and normalizations. None proves the original-zero signed cancellation estimate. Source coefficients w_d in the Mellin row are (4,-2,-1,-1) at d=(0,3,4,5).

## Typed Gamma definition table

Notation: r(n) is the immutable four-pole forcing; g≥1 is fixed integer block size; R_g(k)=Σ_{j=1}^g16^{g-j}r(g(k−1)+j); Q(x)=4−2e^(−3x)−e^(−4x)−e^(−5x); Q_g(x)=Q(x)Σ_{j<g}16^{g−1−j}e^(−8jx); a_i=(1/8,1/2,5/8,3/4), w_i=(28,−8,−3,−2)/64 and c=15/64. Domains below are part of the definitions.

| Object | Domain and normalization | Source dependence and exact identity | Role / boundary |
|---|---|---|---|
| Classical γ | Harmonic clock N→∞ | lim(H_N−log N)=−ψ(1) | Source-independent reference. |
| Source weighted-harmonic γ_BBP (#560/#569) | Original source time, coefficient c | lim[Σ_{n≤N}n r(n)−c logN]=−Σ_iw_iψ(a_i)=cγ+Σ[nr(n)−c/n] | Forcing-specific finite part, ≈3.3224979111064. Independent of seed/digit statistics. #560 already has cγ+D; #569 adds closed form/recursion. |
| Source Gamma coordinate C_BBP(z) (#569) | Real z>−1/8 | C_BBP(z)=−Σ_iw_iψ(z+a_i), C(n)−C(n−1)=−nr(n) | Exact functional recursion; C(0)=γ_BBP. |
| Source Gamma quotient G_BBP(z) (#569) | Real z≥0, positive branches | ∏Γ(z+a_i)^{w_i}; logarithmic derivative of G(z+1)/G(z) is Σw_i/(z+a_i) | Chosen exact source function, not a transfer matrix. |
| Logarithmic block free energy F_g (#570) | N→∞ at fixed g; subtract 2H_{N−1} | log[64g²R_g(1)/(16^g−1)]−2γ | Depends on source and grouped clock. The g=1 mechanism is inherited Oily Macaroni III. |
| Original-time block γ_g^BBP (#570) | N→∞ at fixed g; harmonic time gN | γ−½log C_g, C_g=64R_g(1)/(16^g−1)>0 | Distinct from γ_BBP above. C_g↓4π and γ_g↑γ−½log4π by classical BBP; this uses a known period identity, not normality. Limits are iterated. |
| Local Mellin γ^M_{a,g} (#570) | a>0, g fixed; normalized density μ=e^(−ax)Q_g(x)dx/Z_g(a) | 1−E_μlog(aX)=γ+1+[Σ_{j,d}16^{g−1−j}w_d log((a+8j+d)/a)/(a+8j+d)]/Z_g(a) | One-time normalized log moment. As a→∞ it equals γ+(5/2−8g/(16^g−1))/a+O_g(a^-2). Not either finite part above. |
| Gamma(2,1) endpoint law (#564/#568/#570) | a→∞ at fixed g, Y=aX under μ | Q_g'(0)>0 gives density y e^(−y)dy | Universal endpoint-rank limit, shared by counterfeit two-pole sources; higher jets retain source details. |
| q-Gamma blocking (#568/#570) | q=e^(−8x)/16∈(0,1/16]; integer g≥1 | B_g=16^{g−1}[g]_q=16^{g−1}Γ_q(g+1)/Γ_q(g) | Exact finite radix blocking. Universal factor for any radix-16 Laplace forcing. No q→1 occurs. |
| Canonical classical γ_q (#569/#570) | Canonical DLMF Γ_q product, 0<q<1 | −ψ_q(1)=log(1−q)−log q Σ_{n≥1}q^n/(1−q^n) | At q=1/16 ≈0.1318958182224; not γ_BBP or γ_g. Recurrence/integer values alone do not fix it: e^{t sin2πz}Γ_q(z) changes derivative while preserving them. |
| Chosen 16x16 source-Gamma operator (#569) | Row-stochastic P, H=J/16, X=P−H, spectral norm ||X||<1/8 | C_BBP(X)=γ_BBP I+Σ_{m≥1}(−1)^m[Σ_iw_iζ(m+1,a_i)]X^m | Analytic observer of empirical transition defect. On ||X||≤1/32, 13||X||≤||C(X)−γ_BBP I||≤43||X||. This is equivalence of local defects, not decay of either. |

Proof locations: `research/2026-11-08/laplace_critical_adic/THEOREMS.md:29`; `research/2026-11-09/bbp_gamma_matrix_deformation/THEOREMS.md:15,50,74,109,129,144`; `research/2026-11-09/bbp_euler_mascheroni/PROOFS.md:38,70,99,189`; `research/2026-11-09/gamma16_yoneda/PROOFS.md:139`.

All forcing-only Gamma quantities survive the mathematical same-forcing wrong seed s*=−π/16, whose completed orbit is0. That irrational control is not a rational p-integral seed. Dyadic rational epoch-dependent shadows supply the separate p-integral finite controls. No Gamma quantity in the table currently supplies an all-epoch real signed cancellation estimate.


[Full review](main_xxii_evidence/gamma-audit.md) · [Claim supplement](CLAIM_SUPPLEMENT_MAIN_XXII.md)
