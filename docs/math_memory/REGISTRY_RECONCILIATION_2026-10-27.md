# Claim-namespace registry reconciliation — Main XII (2026-10-27)

**Scope:** additive registration of pre-existing-main claim supplements into `docs/CLAIM_NAMESPACE_REGISTRY.json` so the FQID resolver recognizes orphaned rows. **No historical theorem ID renamed; no proof status promoted; no supplement byte modified.** Every added entry carries an explicit reconciliation `status` string and `code: []`; per-row proof status stays `UNCLASSIFIED_RAW` (parsing a table row never certifies it). This is a discovery-layer hygiene pass, not a mathematical result.

## Result

| metric | before | after |
|---|---|---|
| registered namespaces | 60 | **184** |
| registered claim rows (builder-parseable) | 804 / 1876 | **1876 / 1876** |
| catalog warnings | 1200 | **9** |

Gates after the pass: `tests.test_claim_namespace_collisions` 15/15 OK; memory tests OK; `scripts/verify_provenance.py` → SOURCE_PROVENANCE_VERIFIED.

## Method (three verified tranches, 124 entries)

1. **91 single-prefix safe** — files with one unregistered prefix, derived from the builder-parsed catalog (`claims[].registered == false`), zero collisions against the 60 existing. Each → one additive entry, `supplement_files=[file]`, `id_count` = parsed row count.
2. **8 multi-prefix** — four files each hosting two claim families (`OBSERVER_SCHUR`: OD+OS; `PERIODIC_TAIL`: MS+PTE; `PRIME_JET_GENESIS`: PIG+PJG; `TATE_CARRIER_WEIL`: CR+TF). Registered both prefixes per file. This closed the parseable-row gap to **1876/1876**.
3. **25 alternate-ID-scheme file-level** — supplements whose ID format (`O1`, `CH1`, `NG-D`, `K1`, `S1`, …) the builder's `PREFIX-123` regex does not parse. Detected prefixes were **verified against each file's actual dominant claim-row prefix** before registration. A heuristic detector initially mis-registered two (`BLACK_SUN`→`ALEX`, a stray non-ID token; `EFFECTIVE_TATE_GATES`→`EF` which is real but its file's `TF` family collides) — both caught by the verify pass and **reverted**. The builder regex was deliberately **not** broadened (it is #341-authored tracked code; changing it risks the 1876 count and the 14-test gate).

## The 9 documented residual warnings (human-review items — intentionally NOT auto-resolved)

Auto-merging any of these could collapse distinct claim families under one prefix — a correctness defect, not a cleanup. Left flagged on purpose:

- **Prefix collisions across distinct files** (resolve by provenance: shared namespace vs. relabel):
  - `EMPIRICAL_CARRIER.md` — prefix `EC` already → `EDGE_CARRIER_RECONSTRUCTION`.
  - `SUZUKI_FIRST_PRIME.md` — prefix `S` already → `APOLLO_PRIME_DOMAIN`.
  - `ZERO_CENTERED_ARCH.md`, `ZERO_CENTERED_FUCC.md`, `ZERO_CENTERED_PURITY.md` — three files share prefix `ZCR`.
  - `EFFECTIVE_TATE_GATES.md` — real family `EF`, but its `TF` family collides with `TATE_CARRIER_WEIL`.
- **FQID crosswalk (already registered under a dotted namespace):**
  - `BBP_MINIMAL_PATH.md` — rows use `MP.GAUGE-*` (registered); add the file to `MP.GAUGE`'s `supplement_files`.
- **Table-less / prose supplements (indexed as source_documents; no claim namespace):**
  - `META_CONTOUR.md`, `YEAN_PROOF_OPERATORS.md`.

All 185 supplements remain indexed in `CLAIM_CATALOG.json` `source_documents`; nothing is lost, and the residual is characterized rather than hidden. The remaining warnings reflect honest, pending provenance decisions — not missing coverage.
