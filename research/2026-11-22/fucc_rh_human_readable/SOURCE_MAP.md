# Sources, provenance and access boundary

Date: 22 November 2026. The external theorem is attributed entirely to Levent Alpöge and Claude. This SUCC packet is an independent *expository/mathematical translation project*, not a claim to their priority.

## Primary external proof

1. Levent Alpöge, announcement, 20 November 2026, https://alpo.ge/remark.pdf (4 pages); describes Stepanov, theta lifts as multiplicity and suggested chain length √X; it is not the proof text.
2. Released Lean archive, linked in the announcement (14 parts), containing ~175,187 Lean files; this packet **did not download, compile or audit that archive**.
3. Lean/Mathlib communities verification statement, 21 November 2026, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ — verified statement, compilation, theorem matching and multiple kernels. Independent MIT verification receipts: https://math.mit.edu/~drew/grh/. These support the external formal theorem but do not turn our prose into a checked proof.

## Human-readable expositions used as sources, with differing scope

4. M. O. Rubinstein et al., *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, working draft 21 November 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf. Used: Part I §§I.0–I.8 (overview), Part II §§1–6 (Mellin, local formal logarithm, characteristic sums, main inequality M, parameter balancing), Part III status inventory §§III.4–III.9 (what the guide still quotes from Lean). It explicitly states (M) is NOT fully derived in the prose.
5. Siniša Slijepčević, *Outline of Alpöge’s proof of the generalised Riemann hypothesis*, 21 November 2026, https://hexagonmath.org/pdf/2611.00812v1, especially §1.1–§1.3 and §2. Independent-style mathematical outline, not a complete independent audit of the Lean archive.
6. Robin Zhang, *A Preliminary Note on Alpöge’s Proposed Proof of the Generalized Riemann Hypothesis*, 20 November 2026, https://hexagonmath.org/pdf/2611.00809v1, §§1–5. Historical interpretation and additional explanation; author explicitly warns that the synopsis is AI-assisted and not a checked complete conventional proof. We do not use it as independent confirmation of the deep lemmas.

## User-owned mathematical antecedents actually inspected

7. `femboy2112/FuckingRH`, `research/aletheia_2026-10-05/FUCC_MULTIPLICATIVE_OPERATOR.md` on main (prime isometries, critical tower weighting). https://github.com/femboy2112/FuckingRH/blob/main/research/aletheia_2026-10-05/FUCC_MULTIPLICATIVE_OPERATOR.md
8. `femboy2112/FuckingRH`, `research/aletheia_2026-10-06/FUCC_WITH_SUCC_COMPOSITION_CARRY.md` on main (SUCC/FUCC affine braid, augmentation ideal and radix carries). https://github.com/femboy2112/FuckingRH/blob/main/research/aletheia_2026-10-06/FUCC_WITH_SUCC_COMPOSITION_CARRY.md
9. SUCC main, `research/2026-10-17/SOURCE_COVARIANT_IMS_AND_BAND_CUTOFF.md` (log placement, Gamma+FUCC nonlocal jump, signed corrections, genuine prime powers). https://github.com/femboy2112/SUCC/blob/main/research/2026-10-17/SOURCE_COVARIANT_IMS_AND_BAND_CUTOFF.md
10. SUCC main, `research/2026-10-17/PRIME_JET_GENESIS_AFFINE_RIGIDITY.md` (Euler logarithmic prime jets and precise Beurling controls). https://github.com/femboy2112/SUCC/blob/main/research/2026-10-17/PRIME_JET_GENESIS_AFFINE_RIGIDITY.md
11. SUCC main, `research/2026-10-17/GAMMA_FUCC_FINITE_BATH_FREDHOLM.md` (true Gamma/FUCC signatures and limits; no RH proof). https://github.com/femboy2112/SUCC/blob/main/research/2026-10-17/GAMMA_FUCC_FINITE_BATH_FREDHOLM.md
12. SUCC main, `research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/WEIL_PACKET_PROOFS.md` (complete Guinand–Weil formula, with source-specific signed/prime and Gamma firewall). https://github.com/femboy2112/SUCC/blob/main/research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/WEIL_PACKET_PROOFS.md
13. SUCC `AGENTS.md` and `docs/METHOD.md` on main. SUCC prior draft #686 is the parent in the research stack; provenance of its contents is unchanged.

## Intellectual honesty and scope

`[D,V_p]=(log p)V_p`, Euler-logarithm differentiation, Mellin transform, formal inverse-valuation induction and determinant bounds are established mathematical methods. This packet assembles them into a FUCC-language account to help build a human-readable proof, **without claiming mathematical priority or independent rederivation of (M)**. The Lean archive has external verification. The additional SUCC-notation derivation has only this packet's paper arguments plus scoped Python checks, not Lean verification. We explicitly do not claim any theorem about π base-16 normality from the RH proof.
