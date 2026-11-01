# Integration-only test oracle namespace repair (2026-10-31)

**Scope:** only tests/test_carrier_path_measure.py and tests/test_seed_superposition.py in THIS new combined draft research branch. No modification to the original PR #431 or #433 branches, their research modules, the original BBP source, formal proof contracts, production, workflows or main.

## Fault class — Python sys.modules collision, not arithmetic

The historical PR #431 test adds the carrier_path_measure research directory to sys.path and imports a helper literally named independent_oracle. The later PR #433 test adds a DIFFERENT seed_superposition directory to sys.path and imports a different helper with the **same top-level module name** inside test methods. When full root unittest discovery runs both, Python may reuse the first module cached in sys.modules for the second import, depending on test discovery order. These helpers export DIFFERENT symbols; the failure is a module-identity collision, not a counterexample to their mathematics. Our new lag test had the same potential and was separately fixed before integration.

**Status of historical CI errors:** a live GitHub check of PR #433 showed Python mathematical/epistemic jobs failed on one head (details in GitHub, but the connector did not supply job logs). The import pattern itself is an independently inspectable root cause CANDIDATE. Its causal relation to those job failures is **UNVERIFIED**, so this note does not claim the cause was established from raw logs.

## Resolution: source-file-targeted importlib, distinct names

On this combined child branch ONLY, the two historical test files now load their own original helper files using importlib.util.spec_from_file_location with unique module identities:

- _carrier_path_independent_oracle for the unchanged PR #431 carrier oracle;
- _seed_superposition_independent_oracle for the unchanged PR #433 seed oracle;
- _signed_lag_independent_oracle already used in our new tests for the unchanged new lag oracle.

This avoids any dependency on module search path ordering or cache state. All three oracle implementations themselves remain BYTE-FOR-BYTE identical to their prior Git objects. Existing mathematical assertions and fixture inputs in the old test files were not altered; only import wiring changed.

**Exact child-only test blob SHAs:**
- tests/test_carrier_path_measure.py: bf5a28115c8e2f03bd2cf8661063399802994a6d;
- tests/test_seed_superposition.py: a431dba3e88a6e6b1de64b8824498839af1016f3;
- tests/test_selected_lag_tomography.py: 75df7fdae1a790bce4e23a39620da3dd9c2f4551, locally re-executed 28/28 PASS.

This is a **configuration/integration repair**, not independent proof or new mathematical discovery. CI on the final exact combined head is required to establish the actual integration success. Do not silently rewrite the historical source branches to hide this conflict.