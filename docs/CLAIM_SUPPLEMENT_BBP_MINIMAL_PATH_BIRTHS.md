# BBP Minimal Path / Births & Galois Selection — Claim Ledger

Research date 2026-10-24. Source PR #261 head `4b52cb87a19c2f599e5386fc12a9758bab12cba8`,
stacked on draft #258 at `9aa55b3a6e1150d1690612c740a38e86adc081db`. No main merge, release,
revision of historical archives or scientific-priority claim. Original BBP source #252, Green
#254 and prime windows #256 source ancestry remain exact. The later #256 p² Witt contribution
is reviewed as a separate sibling (gauge family, `CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH_GAUGE.md`).

**Integration note (coherent-main 2026-10-24).** This supplement was renamed from the shared
`docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md` path so it can coexist with the independent #260
gauge family. Its bare `MP-` IDs are preserved and resolve to fully-qualified `MP.BIRTHS-xx`
via `docs/CLAIM_NAMESPACE_REGISTRY.json`. The original #261 table reused `MP-05` for two
distinct claims; the second occurrence and every later ID were renumbered by +1 (old second
`MP-05` → `MP-06`, old `MP-06` → `MP-07`, old `MP-07` → `MP-08`, old `MP-08` → `MP-09`) so each
bare ID is unique within this file. `docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md` is the crosswalk
recording the original-to-canonical mapping.

| ID | Claim | Status / authority boundary / falsifier |
|---|---|---|
| MP-01 | Exact odd-prime first births B(N), B(N)~6N/log N | DISCLOSED PAPER / exact finite; first forcing p valuation and PNT-AP; counts first events, not independent entropy |
| MP-02 | EVERY p^k gives a new full-state valuation −k; fixed-depth power-law count | DISCLOSED PAPER / exact finite; four source denominator residue classes; no filtered-to-full Witt promotion; k fixed before N |
| MP-03 | Minimal homogeneous rational recurrence is order two | DISCLOSED PAPER / exact rational intervals; uses classical irrationality of π and 16·T_n−r(n+1)=T_(n+1); inhomogeneous order one remains |
| MP-04 | Positive infinite Hankel, all-prime-birth, but a periodic counterfeit | DISCLOSED PAPER / exact finite; different forcing, rational t0=1/2, selected orbit zero |
| MP-05 | Authentic p-free complementary Galois trace and full twisted second moment | DISCLOSED PAPER / exact formal group ring; actual cyclotomic p-free conductor; not a selected-embedding theorem |
| MP-06 | Almost-all-embeddings bound p/[(p−1)·L·ε²] | DISCLOSED PAPER; finite Markov from exact second moment; no sampled-embedding typicality inference — *renumbered from #261's second MP-05* |
| MP-07 | Selected p=97 squared amplitude >1/20 and true Galois RMS²<1/40 | EXACT FINITE INTERVAL / paper identity; source-rational BBP, Machin π and outward Taylor; no p→∞ conclusion — *renumbered from #261 MP-06* |
| MP-08 | Minimal p-free autonomous clock can resonate | REFUTED as a generic local-to-global implication; coprime-conductor counterfeit, not authentic BBP forcing — *renumbered from #261 MP-07* |
| MP-09 | Selected amplification A_p=o(L_p) implies normality | CONDITIONAL PROVED / PREMISE UNVERIFIED; subgroup/Galois RMS and CBCW-05; no actual A_p bound — *renumbered from #261 MP-08* |

**Explicitly OPEN / NOT ADDRESSED:** the existing `I_p(h)` or `J_(p,d)(h) → 0` still requires a
BBP-selected signed high-mode theorem (UNVERIFIED); π normality, RH and signed Weil positivity
are not addressed (no signed global Weyl theorem, no new Lean assertion); external academic
novelty is UNVERIFIED (distinct source typing and implementation do not prove literature priority).

The exact mathematical dossier is at `research/2026-10-24/BBP_MINIMAL_PATH_GALOIS_SELECTION.md`.
Source modules: `observational_succ/bbp_minimal_path_births.py` and
`observational_succ/bbp_galois_tomography.py`. Source-conserving independent integer/Fraction
oracle: `scripts/bbp_minimal_path_births_probe.py`.

**Operational next theorem:** prove a non-tautological exact-source estimate of exceptional
selected-embedding amplification A_p(h)=o(L_p) for every fixed nonzero h, or exhibit a direct
authentic-source obstruction to a proposed improvement. Selected p=97 already falsifies
universal A≤1. **No wall has been certified; a source-specific discriminator remains missing.**
