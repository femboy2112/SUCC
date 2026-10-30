# Inertial Contact — validation receipt

Date: 2026-10-30. Draft PR #397 only; Main XVI original base e18ba565ca540adb7edf3292f5593929e76d91c5. All modifications additive in research/2026-10-30/fibonacci_epicycle_demon/.

## Exact source execution

Executed in isolated local Python 3 (stdlib only):

    python /mnt/data/succ_inertial_contact/inertial_contact_probe.py

Recorded test names:
- test_exact_external_record_repairs_collision: ok
- test_exact_s_one_memory_horizon: ok
- test_grade_zero_has_no_chronology_overhead: ok
- test_no_bounded_state_can_encode_all_independent_histories: ok
- test_radix_observer_cannot_extrapolate_finite_prefix: ok
- test_rest_can_receive_dynamic_information: ok
- test_static_and_active_frozen_carrier: ok

    Ran 7 tests in 0.001s
    OK

Locally executed Git blob hash: 831a9b5df9460269eb5d960bfa05d4f76d4cef31.
The remote newly committed inertial_contact_probe.py was fetched by exact branch/path and GitHub returned the same **Git blob SHA-1**, confirming byte-identity of the executable. The demonstration of stationary time-varying data uses a separate *time-indexed field* even though the toy count enumerator reuses the same indexed-word implementation as the spatial-path case; it does not claim the stationary spatial carrier is dynamically varying.

The proof in INERTIAL_CONTACT_FIELD.md is a standard injective-cardinality argument for a **specified admissible-history family**. Its exact conditional Oily grade s=1 result follows from binom(2n,1)=2n and inherited source-exchangeability; these tests are finite controls, not a universal proof validator.

## Status boundary

Verified finite witnesses: tests 7/7 PASS, remote exact source bytes matched, mathematical dossier committed. Not run: whole repository tests, provenance checker, ordinal/observer probes, Lean, hosted CI, external referee. No inference to selected π normality, no physically realized eternal information channel or infinite-time supertask, no gravitational horizon. 

Follow-up: operationally define the source/observer interaction and grade-split/carry information transport, test whether selected zero-seeded signed history breaks observational null directions, while rejecting same-forcing coherent counterseed and high-jet source mutants.
