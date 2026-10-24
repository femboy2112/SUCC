# Academic Main IX — integration report (π Moonwalk / circle / source)

**Status: STAGED, NOT MERGED.** This integration branch is a reviewable candidate.
No push to `main`, no release, no tag was performed. Merge awaits hosted-CI green
on the pushed branch and explicit maintainer authorization.

- **Starting `main`:** `b116841f12b41aaf7600da39bbb40577f25b6295` (Academic Main VIII).
- **Candidate head:** `5bafd77` on `integrate/academic-main-ix-pi-circle-source-2026-10-23`
  (287 commits over `main`, history-preserving `--no-ff` merges).
- **Firewall preserved:** provenance `establishes_mathematical_truth: false`;
  RH, π normality, abc, signed-Weil positivity all **OPEN**. No claim promoted.

## 1. Verified PR graph (git ancestry, not PR labels)

- **Main stack (linear):** `main → #234 → #235 → #236 → #238 → #240 → #242 → #243 → #244`
  — every edge confirmed by `merge-base`. Tip **#244** (`5e2ba04`) covers all eight.
- **Independent 3-stack:** `main → #237 → #239 → #241` (tip `#241` = `bed4716`) —
  verified **not** absorbed into #244 (a #237 theorem is not a #238 hypothesis).
- **#244 children:** #245 (`d4568a9`), #246 (`074f0d2`), #247 (`5a29229`); #247 children
  **#248 (`277b3e7`) and #249 (`5e35aea`) are siblings** (neither ancestor of the other).
- **Independent π roots on main:** #232 (`bf55ab1`), #231 (`ccd702f`), #229 (`70462c2`), #233 (`13d5a40`).
- **Support PRs on main:** #220–#227 (additive; #227 doc-only). **#226 is `0c4e6982`** — one
  clean additive commit directly on `main` (an earlier report of an "off-main anomaly" was a
  coordinator SHA-transcription error, corrected here).

## 2. Admission — all 28 open PRs accounted for, 0 orphans

17 leaf tips cover the whole graph and were merged (ancestry-preserving):
`{220,221,222,223,224,225,226,227,229,231,232,233,241,245,246,248,249}`.
#244 and #247 fold in transitively through their children (no separate merge).
**Every one of the 17 tips + the covered bases #244/#247/#237/#239 is a verified
ancestor of the candidate head.**

## 3. Conflicts and their actual resolutions

| Merge | Conflict | Resolution |
|---|---|---|
| 11 additive tips (220–231, 241) + #232 | none | clean |
| #233 | `docs/CLAIM_INDEX.md` | union (both research entries kept; paragraph separation restored) |
| #245 | `CLAIM_INDEX.md`, `CLAIM_LEDGER.md`, `ROADMAP.md` | union of additive entries |
| #246 | `docs/CLAIM_NAMESPACE_REGISTRY.json` | **semantic JSON union by `fq_prefix`** — a text union would have fused the DUCK and CSO objects into one malformed node with two `"namespace"` keys; merged as JSON instead → 35 rows, 0 duplicate `fq_prefix` |
| #248, #249 | none | clean (git 3-way placed the circle doc entries without overlap) |

**Claim-namespace registry:** merged by pure semantic union (list of objects; no row
rewritten or removed). Added namespaces across the whole round: `DUCK` (#232), `RP` (#244,
inherited byte-identically by 245/246/247/248/249), `SFR` (#245), `CSO` (#246). The audited
labels `CGPD/PCG/CC/SCR/TC` were **absent** from every tip's registry.

**Completeness repair:** three claim prefixes were used in supplements but unregistered —
`CGPD` (#229, CGPD-01–14), `PCG` (#231, PCG-00–10), `PBR` (#233, PBR-01–20). Registered as
**research-status** namespace rows (explicit status strings disclaim π-normality / RH / abc /
Weil / novelty — they are **not** installed theorems). Registry now 38 namespaces; the
namespace-collision gate passes (15/15).

**Shared `ci.yml`:** only #232 modified it (one additive line calling
`scripts/verify_duck_pi_dependencies.py`, which exists and runs rc=0). Every other PR added its
own per-PR workflow file (additive). 20 new workflow files total.

## 4. Validation (local, CI-equivalent environment)

| Gate | Result |
|---|---|
| `scripts/verify_provenance.py` | **SOURCE_PROVENANCE_VERIFIED** (rc=0); 17 byte-identical research archives; `establishes_mathematical_truth: false` |
| `scripts/observer_foundations_probe.py` | rc=0 |
| `scripts/ordinal_succ_report_probe.py` | rc=0 |
| `scripts/verify_carry_safe_lean.py` | rc=0 (carry-safe Lean receipt re-verified) |
| namespace-collision gate | 15/15 OK |
| full `unittest discover` (CI-equivalent env, `PYTHONPATH`=root) | **7374 / 7374 OK** (combined 17-PR tree; 1138 s) |
| full `unittest discover` (bare, no editable install) | 7373 pass, 1 error — the environment artifact below |

**On the one local error.** A bare `unittest discover` (without an editable install) reported
`FAILED (errors=1)`: `test_eodcs_meta_choice_descent.test_exact_probe_receipt_and_independent_count`.
Proven to be an **environment artifact, not a repo defect or merge regression**:
1. No merged commit touches `tests/test_eodcs_meta_choice_descent.py` or
   `scripts/meta_choice_descent_probe.py` (empty `git log main..HEAD` on those paths).
2. The error is `ModuleNotFoundError: No module named 'observational_succ'` — the test spawns a
   subprocess whose `sys.path` lacks the repo root.
3. **Bare `main` fails it identically** (rc=1) — pre-existing, merge-independent.
4. It **passes** when the package is importable. Re-running the **entire** suite with
   `PYTHONPATH=<root>` (the CI-equivalent condition) gives **7374/7374 OK** in 1138 s. CI installs
   the package editable (`pip install -e ".[test]"`), so the hosted jobs are green — consistent with
   #244/#246 having passed their full-length CI math checks. The combined tree has **no** merge
   regression and **no** genuine failure.

**CI inversion resolved.** #244 and #247 showed a "red" math check in the rollup; the log shows
`##[error]The operation was canceled.` — a concurrency/fail-fast cancellation of a re-run at
~90 s, while tests streamed `... ok`. Their genuine full-length runs (13–19 min) **passed**.
Not a regression.

## 5. Preservation / history

- 17 research archives byte-identical (provenance gate).
- Ancestry preserved via `--no-ff` merges; no cherry-pick, no history rewrite, no squash.
- Original signed-Weil source and SHA-backed manifest untouched; no claim promotion; RH OPEN.

## 6. What remains before `main`

1. Push the integration branch; let hosted CI run on the **combined** head (the local run is
   CI-equivalent but not the hosted job — "do not claim CI passes before it does").
2. On green CI + explicit maintainer imprimatur, merge with `--no-ff` preserving ancestry.
3. Update top-level roadmap to "Academic Main IX" **only after** the merge and its CI evidence.

No step in 1–3 has been taken. The branch is a staged, reviewable candidate.
