# Isolated exact validation and independent-provenance limits

**Parent:** SUCC PR #487 pinned `5f69d87d8bddde4f7136229289bc9ebde430c5f0`. A separate preregistration was committed to `research/circle-path-electric-natural-extension-2026-11-03` before executing fresh original source probes: commit `2772bf00fef7b5a43df302560766d0547beee6a1`.

New code and tests are strictly additive, use the four original signed BBP Mellin terms and literal zero seed, and do not introduce π digits.

Actual executions recorded in `TEST_LOG.txt`:

- `python -m unittest discover -s .../tests -p 'test_circle_path_electric.py' -v`: **12/12 tests pass**, no skips. Earlier local first draft had an ordinary Python `.get` missing-default `None` in the independent current test; fixed before final 12/12 run. The failing attempt was not mathematically significant and is recorded in this document.
- `python .../probe.py --write` then `--verify`: exact original source heldout A=96,192,384 and n=97,193,385,769 **PASS**. Exact source Fraction phase and a separate integer-only common-odd-denominator modular recurrence agree for all n<=769. The independent 16-child expansion of squared imbalances matches the compact histogram norm difference exactly. Full 16-sector DFT group-ring character sums replay as exact integer coefficient vectors, no floating-point geometry.
- Python source/test compilation and receipt SHA-256 integrity validation **PASS**. All original-source phase hashes and exact rational energy values archived.

Not executed: full >11k SUCC native suite, provenance/observer/ordinal root probes, new Lean kernel, external independent human referee; historical source and parent tests are not falsely marked as new passes. GitHub hosted exact-head workflow statuses must be checked separately and may be pending.

**Paper theorem authority:** CE-01..04 have elementary general proofs within the typed domain; the independent integer and Fraction oracles verify only finite instances. The solenoid and electrical facts are classical imported mathematics. The source-selected all-horizon current dissipation saving and π base16 normality remain OPEN.
