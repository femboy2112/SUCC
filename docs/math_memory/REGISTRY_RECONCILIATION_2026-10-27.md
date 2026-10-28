# Claim-namespace registry reconciliation — Main XII (2026-10-27)

**Scope:** additive registration of pre-existing-main claim supplements into `docs/CLAIM_NAMESPACE_REGISTRY.json` so the FQID resolver recognizes orphaned rows. **No historical theorem ID renamed; no proof status promoted; no supplement byte modified.** Every added entry carries an explicit reconciliation `status` string and `code: []`; per-row proof status stays `UNCLASSIFIED_RAW` (parsing a table row never certifies it). Discovery-layer hygiene, not a mathematical result.

## Result

| metric | before | after |
|---|---|---|
| registered namespaces | 60 | **176** |
| registered claim rows (builder-parseable + fqid-conformant) | 804 / 1876 | **1863 / 1876** |
| catalog warnings | 1200 | **30** |

Gates after the pass (all exit 0): `scripts/academic_main_vii_gate.py`, `academic_main_viii_gate.py`, `verify_duck_pi_dependencies.py`, `main_vii_hostile_replay.py --require-fixed`; `tests.test_claim_namespace_collisions`; memory + Farey tests; `scripts/verify_provenance.py` → SOURCE_PROVENANCE_VERIFIED. Graph lint PASS.

## Method (116 fqid-conformant entries added)

1. **91 single-prefix safe** — files with one unregistered prefix from the builder-parsed catalog (`claims[].registered == false`), zero collisions. **Minus 2** reverted below.
2. **8 multi-prefix** — four files hosting two claim families each (OD+OS, MS+PTE, PIG+PJG, CR+TF); both prefixes registered.
3. **25 → 19 alternate-ID-scheme file-level** — supplements whose ID format (`O1`, `CH1`, `NG-D`, …) the builder regex does not parse; detected prefix verified against the file's dominant claim-row prefix (2 heuristic mis-registrations caught and reverted at generation). **Minus 6** reverted below.

## The fqid-conformance correction (why 8 entries were reverted)

The canonical authority parser `observational_succ/claim_namespaces.py:fqid` enforces `_BARE_PREFIX = [A-Z]{2,6}[0-9]*(?:-…)` — **a prefix must be 2–6 uppercase letters** (optionally digit/hyphen-segmented) — and an authority check that the bare ID occurs as its **own** Markdown cell `| ID |`. The catalog builder's regex is more lenient (it accepts a single-letter prefix like `C-01`), so 8 of my candidate entries parsed for the catalog yet are **rejected by `fqid`**, which breaks `scripts/academic_main_vii_gate.py` (a hosted-CI gate). They were reverted:

| namespace | prefix | why non-conformant |
|---|---|---|
| GAMMA_COMPLETION | `C` | single letter |
| TATE_BESSEL_SEVEN_SCHUR | `B7` | one letter + digit |
| APOLLO (K-family) | `K` | single letter |
| APOLLO_PRIME_DOMAIN | `S` | single letter |
| FULL_PRIME_RESOLVENT | `R` | single letter |
| OBSERVER_TATE_ATOM | `A` | single letter |
| ONE_OBJECT | `O` | single letter |
| TATE_SOURCE_CONDUCTOR | `T` | single letter |

These supplements use single-letter / digit ID schemes that **cannot be registered under the fqid authority model**; they stay indexed in `CLAIM_CATALOG.json` `source_documents` and are documented here as a known residual rather than forced in. (This is why the hosted-CI `mathematical and epistemic checks` gate is load-bearing: it caught an over-eager registration the local unittest suite does not exercise.)

## Residual warnings (human-review items — intentionally NOT auto-resolved)

The 30 warnings (regenerated on the final HEAD; they match `CLAIM_CATALOG.json` → `coverage` exactly) are precisely **17 unregistered supplement files + 13 unregistered claim rows**, preserved as explicit legacy residual — indexed as `source_documents`, deliberately **not** forced through the canonical FQID authority parser:

**(a) Legacy single-letter / letter+digit prefixes — fqid-non-conformant, preserved NOT registered (8 files):** `CLAIM_SUPPLEMENT_GAMMA_COMPLETION.md` (`C`; rows C-01…C-06), `CLAIM_SUPPLEMENT_TATE_BESSEL_SEVEN_SCHUR.md` (`B7`; rows B7-01, B7-08…B7-13), `CLAIM_SUPPLEMENT_APOLLO.md` (`K`), `CLAIM_SUPPLEMENT_APOLLO_PRIME_DOMAIN.md` (`S`), `CLAIM_SUPPLEMENT_FULL_PRIME_RESOLVENT.md` (`R`), `CLAIM_SUPPLEMENT_OBSERVER_TATE_ATOM.md` (`A`), `CLAIM_SUPPLEMENT_ONE_OBJECT.md` (`O`), `CLAIM_SUPPLEMENT_TATE_SOURCE_CONDUCTOR.md` (`T`). The **13** row-level `NO EXACT NAMESPACE` warnings are exactly the C-* (6) and B7-* (7) rows of the first two files.

**(b) Other residual — indexed, not namespace-registered (9 files):** `CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md` (rows already registered under the dotted `MP.GAUGE-*` crosswalk), `CLAIM_SUPPLEMENT_EFFECTIVE_TATE_GATES.md` (EF/TF prefix collision), `CLAIM_SUPPLEMENT_EMPIRICAL_CARRIER.md`, `CLAIM_SUPPLEMENT_SUZUKI_FIRST_PRIME.md`, `CLAIM_SUPPLEMENT_ZERO_CENTERED_ARCH.md`, `CLAIM_SUPPLEMENT_ZERO_CENTERED_FUCC.md`, `CLAIM_SUPPLEMENT_ZERO_CENTERED_PURITY.md` (shared `ZCR` family across three files), and the table-less prose supplements `CLAIM_SUPPLEMENT_META_CONTOUR.md` and `CLAIM_SUPPLEMENT_YEAN_PROOF_OPERATORS.md`.

Auto-registering any single-letter prefix would break the canonical `fqid` parser (the hosted-CI `academic_main_vii_gate.py` gate); collapsing a shared/collision prefix would merge distinct claim families; forcing a prose supplement would mint rows with no table. All **185** supplements remain indexed as `source_documents`; nothing is lost, and the residual is enumerated here rather than hidden. Reducing it further is a separately-reviewed registration batch, not a merge-blocking cleanup.
