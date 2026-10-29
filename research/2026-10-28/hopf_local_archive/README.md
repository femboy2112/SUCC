# SUCC Quaternionic Hopf — local mathematical research package

**READ THIS FIRST.** This is research held **locally only**, pending Claude's Main XII integration. No GitHub state was modified. The original four signed BBP poles, chiral rank-two source and the zero-seeded real BBP recurrence remain immutable input definitions.

**Key result:** The PR #333 real source successor `T` is scaled orientation-reversing, which obstructs a fixed right-Hopf S4 one-step map. However it **exchanges right/left quaternionic Hopf observer gauges**, and its square descends to an exact quarter-turn on S4. A separate source-anchored Hopf chart retains all four signed source poles and the source state, but its orbit is not sphere-normal.

## Artifacts

- [`HOPF_SOURCE_DOSSIER.md`](HOPF_SOURCE_DOSSIER.md) — rigorous source passport, proofs, handedness-transport diagrams, candidate lifts, no-go examples, ledger, next discriminators.
- [`hopf_source_exact.py`](hopf_source_exact.py) — standalone pure-`Fraction` rational Hamilton/SUCC source/Hopf implementation; no repo import or runtime dependency.
- [`test_hopf_source.py`](test_hopf_source.py) — deterministic exact tests, including adversarial seed, sign, gauge and chirality controls.
- [`oracle_sympy.py`](oracle_sympy.py) — independent symbolic derivation from the PR #333 original complex-sector update; a separate calculation route, not a blind independent witness.
- [`validation_unittest.log`](validation_unittest.log), [`validation_oracle.log`](validation_oracle.log), [`validation_receipt.log`](validation_receipt.log) and [`oracle_sympy_results.json`](oracle_sympy_results.json) — actual local outputs.
- [`SOURCE_RECEIPT.json`](SOURCE_RECEIPT.json) — compact exact observation examples, provenance and test scope.
- [`CLAIM_LEDGER.json`](CLAIM_LEDGER.json) — typed, source-pinned claims, explicit refutations, scope and next discriminating probe.
- [`CLAUDE_HANDOFF_AFTER_MAIN_XII.md`](CLAUDE_HANDOFF_AFTER_MAIN_XII.md) — **do not run until approved** post-integration instructions, safe non-main integration.
- [`SHA256SUMS.txt`](SHA256SUMS.txt) — reproducibility manifest of local textual files.

## Commands

Run inside this directory:

```bash
python -m unittest -v test_hopf_source.py
python oracle_sympy.py      # requires SymPy
python make_receipt.py
sha256sum -c SHA256SUMS.txt
```

Only the focused tests and independent oracle have been run; **not** SUCC's full native CI, Lean, or hosted checks.

## Pinned context (refresh later)

- SUCC main inspected: `6dd80730c3575d91f746546a25da5aedbd2e2737` (Main XI).
- Primary research PR #333 source: `a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5`.
- Pending Main XII draft PR #342 observed: `ce7df73431e85a4eb2a290445da8e09d4f924b3e`.
- Related Oily/gamma PRs #310 and #340 contain complementary source moments; **they do not establish an independent joint chiral/Hopf construction**.

**Status:** mathematical candidate + verified algebraic counterexamples; *π normality remains open*.
