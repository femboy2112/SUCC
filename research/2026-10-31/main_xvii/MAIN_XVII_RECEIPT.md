# Operation Main XVII — validation and integration receipt

**Date:** 2026-10-31 (New York). **Status:** faithful integration of 35 open research PRs
(#390–#424) into a typed carrier architecture, with a firewall audit, a selected-arithmetic attack,
and full local validation, delivered through a reviewed PR for an authorized merge to `main`. No
publish, tag, release, force-push, archive rewrite, frozen-source change, or workflow change. **No
mathematical status promoted. π base-16/base-3 normality, the signed Weyl gate `T_N(h)=o(N)`
(`Sbar_N(h)=o(1)`), RH, Weil positivity, general Collatz, and shifted Lonely Runner n=18..94 remain
OPEN.**

## 1. Before / after

| | SHA |
|---|---|
| `main` before | `e18ba565ca540adb7edf3292f5593929e76d91c5` (Operation Main XVI) |
| Integration branch | `integration/succ-main-xvii-carrier-selected-frontier-2026-10-31` (from `origin/main`) |
| `main` after merge | _recorded on the PR after the authorized merge_ |

## 2. What was integrated

13 ancestry-minimal leaves (`#391 #394 #395 #396 #410 #413 #415 #418 #419 #420 #421 #423 #424`),
ancestry-preserving `--no-ff`, **zero conflicts**, subsuming all 35 open PRs. Overall diff vs `main`:
**1312 files, +175843 / −3** (the 3 deletions are #396's catalog regeneration). All content is
additive under `research/2026-10-30/…` and the new `research/2026-10-31/main_xvii/`, except:
- #396's inherited additive canonical touch (`docs/CLAIM_INDEX.md` block, `docs/CLAIM_SUPPLEMENT_
  HUMAN_T_ACTION_SNAPSHOT.md`, regenerated `docs/math_memory/CLAIM_CATALOG.json`,
  `tests/test_human_t_action_snapshot.py`);
- additive Main XVII nav blocks in `docs/CLAIM_INDEX.md`, `docs/ROADMAP.md`,
  `docs/math_memory/INDEX.md`;
- the new `tests/test_main_xvii_primary_saving.py` and the regenerated catalog.

**No change** to `observational_succ/`, `formal/`, `scripts/`, `provenance/`, `.github/`, `ci.yml`,
the frozen BBP source, `provenance/IMPORT_MANIFEST.json`, `U_0=0`, or the four signed poles.

## 3. Audit verdict

Three independent read-only reviewers (carrier/universal-N; universal ℕ/ℤ + carrier-first;
Pisot-Lagrangian + dyadic-ζ) re-derived the load-bearing algebra and re-ran the committed probes; the
principal audited the BBP arithmetic spine, the finite-band/cylinder certificates, and the small
triangle/Lorentz/frame-reset clusters directly. **Firewall intact across all 35 PRs; every package
INTEGRATE or INTEGRATE-SCOPED; no DEFER.** The Basel all-order `N^{-2k}Tr(G^k)→2ζ(2k)/(2π)^{2k}` is
PROVED for k=1, **CONJECTURED** for weighted k≥2 — integrated as a candidate. Full registry +
countermodel ledger: `MAIN_XVII_CLAIM_REGISTRY.md`. Hygiene caveats (internal claim-ID drift, README
"PROVED" vs CLAIMS `DISCLOSED` label drift, two uncommitted-script provenance receipts, three
agent-prompt files not to be indexed, the `A_n` notation collision) are recorded there and are
confined to quarantined `research/2026-10-30/` docs; none changes repo-wide status.

## 4. Selected-arithmetic attack (directive §V)

Primary target (dyadic-block saving) and secondary (finite-band certificate) **not reached**. Honest
value delivered — see `MAIN_XVII_SELECTED_ARITHMETIC.md`:
- **NET-XVII-1 (new, rigorous):** primary-only per-window saving `Ẽ_p(h) ≥ 1 − (√p+2)/(L−1)` via the
  subgroup/Gauss bound `|Σ_{g∈⟨16⟩}e_p(αg)| ≤ √p`; isolates the whole proof debt into the cofiber
  cross-term. Does not bound the full sum, dyadic blocks, or `o(N)`.
- **Sharpened obstruction:** my TV-erosion conjecture refuted by data — cofiber ≈ uniform-random
  circle steps (second moment ≈ 1/12); the gap is a source-derived second-moment / non-conspiracy
  bound (NET-XVII-2), which AT-07/SC-05 show cannot follow from primary/zero-seed/conductor-depth
  alone.
- **Certified finite bound:** SC-06 `E_p(h)≥1/4` re-certified on 425 fresh windows × h∈{1,2,3,5}
  (min 0.8366), calibrated instrument + independent second method (≤1e-50); subgroup bound 0/493
  violations, NET-XVII-1 0/922 violations.

## 5. Validation (local, on the integration head)

| Gate | Result |
|---|---|
| `tests/test_main_xvii_primary_saving.py` (new; subgroup bound, NET-XVII-1, SC-06, window correctness, SC-05 + AT-07 controls) | **7 passed** |
| `tests/test_human_t_action_snapshot.py` (from #396) | **10 passed** |
| `verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, source_commit `ba075348`, 72 items, rc=0 |
| `observer_foundations_probe.py` / `ordinal_succ_report_probe.py` | rc=0 (firewall flags unchanged) |
| `verify_math_memory_graph.py` | PASS, 51 nodes / 60 edges, rc=0 |
| `build_math_memory.py --check` | rc=0 (catalog regenerated **last**, after all doc edits) |
| Full root suite `unittest discover -s tests -p 'test_*.py'` (normal env) | **Ran 10025 tests; 1 error** = the pre-existing environment-only artifact `test_eodcs_meta_choice_descent.test_exact_probe_receipt_and_independent_count` (its subprocess `python scripts/meta_choice_descent_probe.py` puts `scripts/` on `sys.path[0]` → `ModuleNotFoundError: observational_succ`); **both files unchanged by this PR**, bare-subprocess failure reproduced (rc=1), and `PYTHONPATH=<repo>` (CI's `pip install -e`) → probe rc=0. **10024 native pass.** Do NOT run the suite under `python -I`. |
| `formal/`, `.github/`, `ci.yml`, frozen BBP source vs `main` | byte-identical; Lean + CI workflows confirmatory |
| Per-PR research probes (`research/2026-10-30/…`) | re-run green by the three reviewers; outside main-suite discovery by design (established SUCC pattern); promoted result carried by the new `tests/` file |

_(The §1 `main`-after SHA and the hosted exact-head CI result are filled from the authorized merge
and the PR head run.)_

## 6. Mathematical status (unchanged; no promotion)

NET-XVII-1 is a rigorous classical sub-result about the *primary* component of a per-prime window;
SC-06 is an OPEN uniform statement (numerically certified, not proved); the Basel weighted all-order
limit is CONJECTURED (k≥2). The 35 integrated packages are research-status, with their own labels
(`DISCLOSED`/`CLASSICAL`/`PROVED LOCAL`/`CONDITIONAL`/`OBSERVED`/`CONJECTURED`/`UNVERIFIED`/`OPEN`/
`DARK`/`REFUTED`). π base-16/base-3 normality, the signed Weyl gate, RH, Weil positivity, general
Collatz, and shifted Lonely Runner n=18..94 all remain **OPEN**. Main XVII promotes no mathematical
status and supplies no signed cancellation.
