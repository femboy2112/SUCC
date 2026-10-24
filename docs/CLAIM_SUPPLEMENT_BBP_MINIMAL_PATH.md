# BBP Minimal Path — claim-ID crosswalk (compatibility index)

This path (`docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md`) was independently used by two draft
PRs for DIFFERENT, disjoint-meaning claim families. During the coherent-main integration
(2026-10-24) the two families were split into distinct canonical supplements, and this file
became the crosswalk mapping every original bare `MP-xx` ID (SHA-qualified by its source PR)
to its stable fully-qualified ID (FQID). Bare IDs remain valid inside their own supplement;
the FQIDs are the collision-free keys registered in `docs/CLAIM_NAMESPACE_REGISTRY.json`.

The two families are disjoint in meaning and evidence and **must never be merged**:

- **Gauge / missing-prime / spectral-bulk** — PR #260, head
  `654e9c9984ced49cee454d99cff20415072d1ffc`, parent #256
  `0683f8f166b9106ab8405a2d6538415b5ac84ba3`. Canonical supplement
  `CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH_GAUGE.md`, module
  `observational_succ/bbp_minimal_path_gauge.py`. Namespace `BBP_MINIMAL_PATH_GAUGE`,
  fq_prefix `MP.GAUGE`.
- **Odd-prime births / minimal recurrence / Galois selection** — PR #261, head
  `4b52cb87a19c2f599e5386fc12a9758bab12cba8`, stacked on #258
  `9aa55b3a6e1150d1690612c740a38e86adc081db`. Canonical supplement
  `CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH_BIRTHS.md`, module
  `observational_succ/bbp_minimal_path_births.py`. Namespace `BBP_MINIMAL_PATH_BIRTHS`,
  fq_prefix `MP.BIRTHS`.

The first-cell identifiers below are dotted FQIDs, which are deliberately **not** matched by
the supplement claim-ID scanner (`observational_succ/claim_namespaces.py`), so this crosswalk
does not itself register a third bare `MP-` supplement file.

## Gauge family (PR #260) — bare `MP-0x` lives in `...GAUGE.md`

| FQID | Original bare ID (source) | Proposition |
|---|---|---|
| MP.GAUGE-01 | MP-01 in #260 654e9c99 | Exact time-dependent Green gauge H_n(y)=y+t_n commuting with ×16; periodic counter-trajectories |
| MP.GAUGE-02 | MP-02 in #260 654e9c99 | q-power torsion coset dense on the circle, invisible to all p-primary reads at p≠q |
| MP.GAUGE-03 | MP-03 in #260 654e9c99 | Normal/nonnormal rational forced trajectories share first K forcing values and all p≠q torsion readouts |
| MP.GAUGE-04 | MP-04 in #260 654e9c99 | Exact cyclic-time Fourier decomposition; Gauss-bound sufficient criterion (no verified cross-spectral decay) |
| MP.GAUGE-05 | MP-05 in #260 654e9c99 | Complete source / signed phase coupling indispensable; bounded no-go |
| MP.GAUGE-06 | MP-06 in #260 654e9c99 | Actual-source o(1) signed nonzero-mode cross-interference implies π base-16 normality (CONDITIONAL, premise UNVERIFIED) |

## Births family (PR #261) — bare `MP-0x` lives in `...BIRTHS.md`

The #261 table reused bare `MP-05` for two distinct claims; the second occurrence and every
later ID were renumbered by +1 so each bare ID is unique within its file.

| FQID | Original bare ID (source) | Proposition |
|---|---|---|
| MP.BIRTHS-01 | MP-01 in #261 4b52cb87 | Exact odd-prime first births B(N)~6N/log N |
| MP.BIRTHS-02 | MP-02 in #261 4b52cb87 | Every p^k new full-state valuation −k; fixed-depth power law |
| MP.BIRTHS-03 | MP-03 in #261 4b52cb87 | Minimal homogeneous rational recurrence order two |
| MP.BIRTHS-04 | MP-04 in #261 4b52cb87 | Positive infinite Hankel, all-prime-birth, periodic counterfeit |
| MP.BIRTHS-05 | MP-05 (first) in #261 4b52cb87 | Authentic p-free complementary Galois trace and full twisted second moment |
| MP.BIRTHS-06 | MP-05 (second) renumbered to MP-06 in #261 4b52cb87 | Almost-all-embeddings bound p/[(p−1)·L·ε²] |
| MP.BIRTHS-07 | MP-06 renumbered to MP-07 in #261 4b52cb87 | Selected p=97 squared amplitude >1/20 and Galois RMS²<1/40 |
| MP.BIRTHS-08 | MP-07 renumbered to MP-08 in #261 4b52cb87 | Minimal p-free autonomous clock can resonate (REFUTED as generic local-to-global) |
| MP.BIRTHS-09 | MP-08 renumbered to MP-09 in #261 4b52cb87 | Selected amplification A_p=o(L_p) implies normality (CONDITIONAL, premise UNVERIFIED) |

Both families are research-only draft claims: PAPER / CONDITIONAL / EXACT-FINITE / REFUTED as
labelled, no new Lean authority, π normality and RH open.
