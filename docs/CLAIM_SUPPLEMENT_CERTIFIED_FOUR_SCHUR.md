# Claim supplement — Certified four-mode Suzuki/Weil Schur trial (CFS)

Branch `research/original-four-schur-certified-trial-2026-10-16`. Dossier:
[`research/2026-10-16/ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md`](../research/2026-10-16/ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md).
Status vocabulary: [`AGENTS.md`](../AGENTS.md) + the 8-level navigation crosswalk. **RH PROVED: NO.**
Fully-qualified namespace `CERTIFIED_FOUR_SCHUR` / `CFS` (single file; governed by
[`CLAIM_NAMESPACE_REGISTRY.json`](CLAIM_NAMESPACE_REGISTRY.json), no prefix collision).

| ID | Status | Statement | Boundary / receipt |
|---|---|---|---|
| CFS-01 | PROVED LOCAL | Residual theorem `A_4 − L_U − (1/κ)T_{r_U} ⪯ S_4 ⪯ A_4 − L_U` for every finite rational parity-respecting `U`, `κ=1/50`, `K^{-1}=−Δ_N` | Re-derived independently (§2 dossier); inherits `D_4 ⪰ κK`, not proved here |
| CFS-02 | VERIFIED EXACT MODEL | Exact-interval two-sided Loewner enclosure of `S_4` at `a=1/2` (`certified_four_schur_trial`) | Interval outward-rounded; Gamma-`J` truncation PSD-capped |
| CFS-03 | VERIFIED EXACT MODEL | `A_4 ≻ 0` certified at `J=64` (both parity blocks; odd margin ≈`2.64·10⁻⁵`, even ≈`9.25·10⁻⁸` unnormalized, vs interval radius ≈`1.7·10⁻¹⁴`) | Not certifiable at `J≤48` (even interval lower `≈−3.6·10⁻⁶` at `J=48`); sign coordinate-independent |
| CFS-04 | UNVERIFIED / OPEN | Sign of `S_4 = A_4 − R_4` | CERTIFIED AMBIGUOUS: upper bracket PSD (no negative witness), lower bracket indefinite |
| CFS-05 | NUMERICAL OBSERVATION + CONDITIONAL | Binding constraint is the `1/κ=50` residual amplification, not Young conservatism | Tight numerical residual bracket is itself negative-definite (eigs ≈`−5·10⁻²…−1·10⁻⁵`) |
| CFS-06 | PROVED LOCAL | Haynsworth transitivity `S_4 = Short_{F_4}(S_30)` | Exact rational finite model (`four_thirty_schur_transport`) |
| CFS-07 | PROVED LOCAL | `κ_30=369/10000 > κ_4=1/50` does **not** transport through the signed modes-5..30 shorting | Exact countermodel: `Short_low[0,0]=1−b²/ε` independent of high coercivity `c` |
| CFS-08 | CONJECTURED (named wall) | Certified high-Legendre-coefficient decay / derivative-Gram tail modulus (§3C) | Necessary for a tight certified lower bracket; **not** sufficient for a decisive sign (see CFS-05) |

**Firewall.** `S_4` sign OPEN (CFS-04). A certified positive `S_4` is a first-window (`a=1/2`)
theorem, **not** RH; a certified negative direction would be extraordinary and is emitted with an
exact rational witness for hostile verification — none found. No nontrivial zeta-zero coordinates are
construction inputs. The completed signed Weil **distribution** is classically identified (CTW-08);
its source-derived **positive factorization** remains OPEN / RH-hard.
