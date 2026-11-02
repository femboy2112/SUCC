# Operation Main XIX — validation receipt

**Date:** 2026-11-01 (New York). All runs on a compliant virtual environment
(`--system-site-packages` + `pip install -e '.[test]'`): Python 3.12, **mpmath 1.4.1**, numpy 2.5.0,
sympy 1.12, scipy 1.18.0. The suite and gates are **never** run under `python -I` (isolated mode
drops the editable `observational_succ`). The repo's own scripts are invoked with `PYTHONPATH=<repo>`
(exactly what the hosted CI's `pip install -e` provides).

## 1. Full test suite

`python -m unittest discover -s tests -p 'test_*.py'` on the integration head:

- **`Ran 11092 tests in 2089.628 s`** — **11091 native pass**, **1 pre-existing environment-only
  artifact**: `test_eodcs_meta_choice_descent.test_exact_probe_receipt_and_independent_count`.
- That test shells out to `python scripts/meta_choice_descent_probe.py`; a **bare** script invocation
  puts `scripts/` on `sys.path[0]` (not the cwd), so the probe's `import observational_succ` fails
  (`ModuleNotFoundError`), rc=1. **The identical error occurs on baseline `main` (4eb411e3)** — the
  test, the probe, and `observational_succ/` are byte-identical to `main`, so this is **not** an XIX
  regression. Under `PYTHONPATH=<repo>` (CI's editable install) the probe is rc=0 and the test is
  **OK** → **11092 OK**. Established lesson carried forward: never run the suite under `python -I`.
- This is the same artifact Main XVII recorded (10025/1); it rides on local invocation, not math.

## 2. Script gates (AGENTS.md required validation + math-memory)

| Gate | Result |
|---|---|
| `scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, `source_commit ba075348`, rc=0 |
| `scripts/observer_foundations_probe.py` | rc=0 (firewall flags unchanged; `loop_prefix_17` unresolved) |
| `scripts/ordinal_succ_report_probe.py` | rc=0 |
| `scripts/verify_math_memory_graph.py` | **PASS: 51 typed nodes, 60 typed edges**, rc=0 |
| `scripts/build_math_memory.py --write` (catalog regenerated **LAST**, after all doc edits) | rc=0 |
| `scripts/build_math_memory.py --check` | rc=0 (see §3) |

## 3. Catalog regeneration (last)

The math-memory catalog was regenerated **after** all dossier files and the three additive nav
blocks were written, then `--check` run. Warnings are the by-design unregistered research-dir
prefixes (FP/AC/CH/CSG/CRE/LCS/… mint no registry namespace) plus the pre-existing legacy
single-letter prefixes — the same classes as `main`, now with the Main XIX source-hash rows added.
No DUPLICATE and no MISSING warnings. (Exact warning delta recorded in the integration commit.)

## 4. Per-cluster probes and the central theorem (independent reproduction)

- **LCS sharpness** — principal and the cluster-C reviewer independently reproduced the exact `c_d`
  table, the sign lemma, the remainder identity (1) by two routes, and the finite-N trend toward
  the predicted limits/defect `(1−(d+1)/c)²` (per-lag profiles match the leading-coefficient model
  to 3 digits; weighted ratios consistent to ~1% at the largest reachable horizon for d=1,2). The
  committed LCS limit tests are closed-form echoes; this independent finite-N evidence plus the
  checked paper proof carry the result. **Recommended follow-up:** a committed per-lag
  "profile-shift" probe (`m(ρ)=∫_1^∞ cos(2π c_d ρ s^{d+1}) s^{−2} ds`, `ρ=16^{k−(d+1)ℓ}`).
- **Cluster probes** re-run green by the three reviewers: four-pole 30, arctan/finite-history/
  circle/holonomy 216, LCS+CRE 70 (268 subtests), categorical+arctan 260, shared trunk 327,
  `operational_yoneda_descent` 21. **0 skips** across every audited module on the genuine checkout;
  the formerly-skippable `ObservationPathCategory` / sheet-adapter / parent-pointed-source tests all
  execute and pass (they skip only under `python -I` or a broken import path).

## 5. Integrity

`observational_succ/`, `formal/`, `scripts/`, `provenance/IMPORT_MANIFEST.json`, `.github/`,
`ci.yml`, `pyproject.toml`, the frozen BBP source, `U_0=0`, and the four signed poles are
**byte-identical to `main`** (`git diff main..HEAD` touches only `research/` and `tests/`, plus the
integration commit's additive nav blocks and regenerated catalog). Lean/CI are confirmatory. The
§1 `main`-after SHA and the hosted exact-head CI result are recorded on the PR after the authorized
merge.
