# Validation scope

Completed in the isolated research worktree, same non-main research branch:

- `PYTHONPATH=. python research/2026-11-08/covariance_forge/crucible/hostile_exact.py`
  exited 0: **4,268 exact finite checks**, preserved in `EXACT_RECEIPTS.json`.
- `PYTHONPATH=. python -m unittest discover -s research/2026-11-08/covariance_forge/crucible -p 'test_*.py' -v`
  exited 0: **4 tests passed**; raw stdout/stderr retained.
- `PYTHONPATH=. python research/2026-11-08/covariance_forge/crucible/instrument_audit.py`
  exited 0: **238 phase containment checks on 119 inputs, plus 212 source and
  unreduced-principal checks**. The last replay includes final audited root-file
  hashes and the sparse-probe hash in `INSTRUMENT_AUDIT.json`.

The two oracle modules expose `run()` returning complete JSON without writing
receipts. Root can import under unique names and save fresh replays separately.
Only each script's `__main__` block writes the committed receipt destination.

Paper review of PE9/PE14, CFS-7 and its controlled growing-degree corollary is
separate from finite execution. No new Lean or native-wide run was performed by
this child. The root owns repository-wide gates and publication. No commits or
pushes were made by this child; all additions are under this namespace.

Exact source selection is not inferred from finite agreement. The growing-memory
shadows change the seed, and the periodic finite-support controls change the
forcing. The original zero-source covariance remains unproved. π normality and
RH remain OPEN.
