# Phoenix II — validation evidence (2026-10-14)

All commands run on the integration head `8d77c73c789b` unless noted. **Local environment: Python 3.12.3, numpy 2.5.0, mpmath.** The 3.10/3.13 matrix is a GitHub Actions fact, not a local one — see the boundary note at the end.

## Baseline (pre-integration, `main` `6e0d88f`)

```
python -m unittest discover -s tests -p 'test_*.py'
→ Ran 2132 tests  OK   (185.2s)
```
Rollback anchor confirmed green before any merge.

## Structural gates (integration head)

| Gate | Command | Result |
|---|---|---|
| Conflict markers | `git grep -nE '^(<<<<<<<\|>>>>>>>\|=======)$'` | none (clean) |
| Compile | `python -m compileall -q observational_succ tests scripts` | exit 0 |
| Provenance | `python scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, `establishes_mathematical_truth: false` |
| Observer foundations | `python scripts/observer_foundations_probe.py` | `finite_survival_claims_are_universal_proofs: false`; counterexample at 19 |
| Ordinal report | `python scripts/ordinal_succ_report_probe.py` | `positive_definiteness_proved: false` |
| Overclaim scan | tree-wide grep for RH/Weil "proved" | **none**; pervasive `RH PROVED: NO` |
| Hazard A | `git rev-parse HEAD:tests/test_zero_centered_purity.py` | `b3c500c0…` (fixed blob) |

## Full integrated suite (integration head)

```
python -m unittest discover -s tests -p 'test_*.py'
→ Ran 3350 tests  OK   (370.3s)   exit 0
```
Up from 2132 on `main`: **+1218 tests** from the 43 PRs, all green. No failures, no errors.

Wave checkpoints:
- Wave 1 (#57–65): full suite **OK** (exit 0).
- Final (#57–99): full suite **OK** (exit 0), 3350 tests.

## Integration shape

```
249 commits ahead of main; 385 files changed; +60,073 / −2
```

## Boundary (stated, not hidden)

- **Python 3.10 and 3.13 CI is NOT asserted green here.** This box is Python 3.12; the 3.10/3.13 matrix (including numpy per-interpreter resolution 2.2.x / 2.5.x) only runs on GitHub Actions after the integration branch is pushed. That push is an outward action pending explicit maintainer go. The merge-to-main gate in the campaign brief ("comprehensive 3.10/3.13 CI") is therefore **not yet satisfied** and must not be claimed until Actions reports it.
- **Lean packages** (4.14 ×2, 4.19) and the per-feature dedicated workflows were not run locally; their exact-head status is a push-time CI fact. The authoritative Python coverage is the main `ci.yml` lane (`pip install -e ".[test]"` + `unittest discover -p 'test_*.py'`), which auto-discovers every integrated `test_*.py`.
- This validation covers **integration integrity** (merges clean, tree compiles, suite green locally, firewall intact), **not** new mathematical certification of any claim.
