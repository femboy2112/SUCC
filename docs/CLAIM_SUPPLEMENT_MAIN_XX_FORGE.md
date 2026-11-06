# Claim supplement — Operation Main XX proof forge (2026-11-05)

Namespace `MAIN_XX_FORGE` (bare prefix `MXX`). These are research-only claims from [`research/2026-11-05/main_xx_forge/`](../research/2026-11-05/main_xx_forge/README.md). Each row maps to its front-ledger id and gives the source dossier.

Statuses use the `docs/METHOD.md` vocabulary, with the finer label in parentheses. **π base-16 normality, the selected signed Weyl gate `S_N(h)=o(N)`, and RH remain OPEN.** No row promotes any of them. All reviews were same-model; none was independently refereed.

| ID | Claim | Status | Front id / receipt |
|---|---|---|---|
| MXX-01 | The critical carry bit is exactly `1[S_m(n+k)≤x_{n+d}<S_d(n)]` with `δ=S_d(n)-S_m(n+k)` (any seed, positive forcing, `S_d(n)<1`); gauge form with `z_j=\{16^j(s+π/16)\}` | PROVED LOCAL (PROVED) | CB-1/CB-1g; front_b/PROOFS.md; 591,175 + 118,235 exact cases |
| MXX-02 | Admissible ⟺ `A≥2^{2d-3}` ⟺ #521 CT-03 domain | TESTED MODEL (CERTIFIED-FINITE, `d≤200`) | CB-0; front_b/admissibility_law.py |
| MXX-03 | Frequency existence + lattice smallness of `J` ⟹ Haar; the converse holds | PROVED LOCAL (PROVED-CONDITIONAL; not π progress) | CB-2, Lemma 2.5 |
| MXX-04 | Log-scale local stationarity (LS) + lattice smallness ⟹ normal | PROVED LOCAL (PROVED-CONDITIONAL) | CB-2′ |
| MXX-05 | A non-normal seed with the same forcing has `\sup_{\rm admissible}|J|\to0`. "J-family ⟹ normality" is REFUTED as an unconditional transport | PROVED LOCAL (PROVED) | CB-3; front_b/numerics |
| MXX-06 | normal ⟺ (LS) ∧ (H2\*); both conjuncts strictly weaker | PROVED LOCAL (EQUIVALENT-REFORMULATION; not progress) | CB-4 |
| MXX-07 | The second-order statistic `J2` separates CB-3 from Haar in exact expectation (`≈1.44e-5`); first-order `J` does not | TESTED MODEL (OBSERVED-FINITE) | CB-5; front_b/numerics/data/j2.json |
| MXX-08 | Hierarchy: every finite-order selected carry family can be silenced on a non-normal seed with the same forcing | HYPOTHESIS (CONJECTURE) | CB-6 |
| MXX-09 | `P_{A,2A,r}=-Q_r(μ_A)+O(1/A)` exactly. #520's finite-cut Clausen inequality is the fixed-h Weyl gate | PROVED LOCAL (PROVED / EQUIVALENT-REFORMULATION) | FA-1/FA-2; front_a/PROOFS.md |
| MXX-10 | A ×b-invariant measure that dominates Lebesgue on an open arc is Haar | PROVED LOCAL (PROVED) | FA-3 |
| MXX-11 | "Clausen energy ≤ C·carries" (seed-uniform) | REFUTED | FA FL, receipt CB-3 |
| MXX-12 | Seed-uniform compactness factorization of `Q_{1/2}` by carries + stationarity | PROVED LOCAL (PROVED; not progress) | FA-5 |
| MXX-13 | `\sup_{V(a)\le1}|\sum a_ne(hU_n)|=\max_L|S_L|` exactly. A mixed angular–radial saving beyond the marginals is REFUTED | PROVED LOCAL / REFUTED | FC-C1-2, FC-C1-V; front_c/PROOFS.md |
| MXX-14 | Character–period dictionary over `\mathbb Q(ζ_8)`. χ₋₄ orientation as a normality lever is REFUTED | PROVED LOCAL / REFUTED | FC-C2-3, FC-C2-V |
| MXX-15 | A mesoscopic pair budget ⟺ normality. Microscopic exclusion ⇏ normality (15-symbol orbit, `β>2/κ`) | PROVED LOCAL / REFUTED | FC-C3-1, FC-C3-2, FC-C3-V |
| MXX-16 | `J_{A,m,k}(0)\to0` for the zero seed; (LS) for the zero seed | HYPOTHESIS (OPEN) | front_b/NEXT.md, docs/PI_NORMALITY_FRONTIER.md §6 |
