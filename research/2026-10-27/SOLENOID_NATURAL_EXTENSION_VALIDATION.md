# Solenoid natural-extension validation boundary (2026-10-27)

**Repository parent:** #328 at 68c00f5eee86c215dd09271b35b0647a5b56f16e; research only.

**Local execution:** Python 3.13 isolated file copy, standard library Fraction. Focused test command: python -m unittest discover -s tests -p test_solenoid_digit_bridge.py -v. 11 discovered; 10 passed, 1 deliberately skipped since the complete upstream SUCC package was unavailable locally. Exact hostile grid: python scripts/solenoid_digit_bridge_probe.py, **30,704 exact rational transport/character checks passed**; original four-pole canceled and signed expressions checked on n=1..99. The initial invocation from a wrong package path failed with an import error; corrected by executing tests from the working root and adding root discovery to the probe. These were environment faults rather than mathematical test failures. Syntax compilation passed.

The script prints whether it could import and compare the native original source. In the isolated run native_repo_source_checked was false; it should be true in a complete checkout.

The new test corpus includes an *ultimately periodic rational* de Bruijn control with exactly uniform finite two-digit windows (not normal), a clock uniform with real digits all zero, a 32/3 versus 0 counterexample with the same modulo-16 2-adic state and different winding, and precision-loss verification of finite-chart inversion.

**Not run:** the full native SUCC test suite, provenance verification, foundation/ordinal probes, hosted GitHub Actions CI, and Lean. Direct git cloning from this container failed DNS; repository state and source files were inspected through the authorized GitHub connector. An exact paper proof is not the same thing as a local finite test or as a Lean theorem.

**Hash-checked Git blobs of the tested local Python sources:** module 7a3bb5c970d65a3133f052125c8d2fc427e3ac36, tests 34cd7781238d4e6a8ac4911664142dd0a992bd4a, exact grid probe bca4ae5735f9c7c875a917fbb5edcd62e2247569.

No π-normality assertion or merge authorization is implied.
