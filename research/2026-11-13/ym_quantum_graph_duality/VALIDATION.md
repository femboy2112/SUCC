# Validation and replay — YM quantum graph duality

**Pinned base:** SUCC draft PR #614, `0faa85a798de5b0b9af4d62295f405165b408eb7`, stacked on Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`. Source and external paper metadata in `SOURCE_MANIFEST.json`.

## Local executed tests (truthful scope)

- Runtime: Python 3.13.5, stdlib only for new checker, no GPU and no Lean compiler installed.
- Isolated new code and inherited PR #614 `yang_mills_gauge_oracle.py` / test copied **byte for byte** into a minimal local mirror; no full repository checkout.
- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v`: **44/44 PASS** (25 new plus 19 inherited) in the minimal mirror. `FOCUSED_TEST_LOG.txt` is the exact raw terminal output.
- `python -m compileall -q observational_succ/ym_quantum_graph_duality.py tests/test_ym_quantum_graph_duality.py scripts/ym_quantum_graph_duality_probe.py scripts/ym_quantum_graph_independent_audit.py`: **PASS**.
- `python scripts/ym_quantum_graph_independent_audit.py`: **PASS**, import-free independent algorithms; exact outputs in `INDEPENDENT_RECEIPT.json`. No claim of external blind verification.
- `python scripts/ym_quantum_graph_duality_probe.py`: exact rational JSON reproduced byte-for-byte; committed as `FINITE_RECEIPT.json`. SHA-256 hashes in receipt refer to the new published module and new tests; verify them on the pushed commit.
- No floating-point tests are treated as proof. `S3` exhaustive 36 basis/6 local gauge controls and joint orbit Burnside checks are exact. All finite results carry their proven domain.

## Recorded repairs; never reclassify a failed attempt as passed

- First Poincaré schedule test asserted strict `2a<1/2` for `a=1/4`; the exact **equality** `2a=1/2` falsified the strict test. Repaired the test to `<=` on the declared `0<a<=1/4` domain; unchanged formula and no theorem strengthening.
- Running the JSON probe as `python scripts/...` initially failed due to an uninstalled minimal shadow package. Added a safe path insertion for the actual checkout root; reran and reproduced the JSON exactly. This was an environment/import-path failure, not an arithmetic result.

## Not executed here

- **NOT RUN** full SUCC tests, provenance verification, observer foundations probe or ordinal probe on the complete repository. The minimal local shadow cannot substitute for the full AGENTS.md gates.
- **NOT RUN** Yang–Mills OpenAI Lean 4.32.0 + Mathlib + Comparator replay; review's recorded build footprint is very large. No Wightman/OS source theorem was locally checked with the Lean kernel.
- **NOT CLAIMED** independent external review of these SUCC additions, worldwide novelty, a four-dimensional interacting field solution, RH, Goldbach, Collatz, pi-normality, confinement, or mass-gap closure.

## Before integration

Check the exact published Git blob hashes against the original local tested file hashes, run the four AGENTS.md gates on the branch head, review CI by commit SHA, independently scrutinize the source-mapped assumptions and proofs, and keep this PR **draft**. Base PR #614 is itself draft/unmerged; do not merge a stacked child independently of its parent.
