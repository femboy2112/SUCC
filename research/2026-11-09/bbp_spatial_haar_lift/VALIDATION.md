# Validation and provenance — BBP spatial Haar to two-digit lift

## Baseline and scope

Parent SUCC #562, ff52b3d8cfe4a94c30716596bda4ce960d054f73. Research branch created and [PREREGISTRATION.md](PREREGISTRATION.md) committed first at 2f163e155998bab2d89240a3a97ff715f63ea3a5 before the new 65,536-digit source run. Original four signed poles, U0=0, full prime carry and repository main unchanged.

## Independent mathematical checks executed locally

A more extensive isolated research bundle (separate from the compact GitHub implementation) passed 22 focused Python 3.13 tests in 0.12 seconds: source versus four original rational poles; r' versus differentiated source; all 256 second-digit spatial lifts; all 4096 third-digit lifts; 2-adic negative-time partial zero checks; temporal 16-cycle E2=15; 1/5 rational wrong-seed spatial/real separation; full CRT phase reconstruction; exact 225-mode energy; Markov/de Bruijn controls; original-source rational Green tail first 129 two-digit readouts. It contains its own raw local log and SHA manifest. This is NOT a claim those 22 tests were run against the compact GitHub module byte-for-byte. GitHub root tests are separately published under tests/test_bbp_spatial_haar_lift.py.

New 65,536 hex digits were generated from the original four-pole bulk integer BBP interval with guards 24 and 32. Both produce the identical full string. The first 40,960 digits match the earlier #561 certificate (SHA256 with newline c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527); independent Machin alternating rational bounds validate the first 128 digits. The finite 65,536 stream SHA256 including newline is e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53.

Finely scoped finite metrics:
- Genuine linear 65,535 pairs: exact E2 =18061567/4294836225; 225-mixed energy =5658763/1431612075; every pair appears, minimum 213, maximum 302.
- Artificial cyclic 65,536 pairs: exact E1=16997/134217728, E2=35323/8388608 and mixed=265587/67108864; minimum 213, maximum 303. The wrap pair is NOT a genuine last→first π transition.
- 2-adic spatial source n mod256: all 256 pairs, exactly once each, 2-digit Haar. Temporal first-nibble cycle: 16 pair types only, exact E2=15.
These finite data do not imply any asymptotic normality or source-selected signed Fourier saving.

## Exact reproducibility

From repository root:

    python -m unittest discover -s tests -p 'test_bbp_spatial_haar_lift.py' -v
    python research/2026-11-09/bbp_spatial_haar_lift/reproduce.py > /tmp/bbp_two_digit_receipt.json
    python scripts/verify_provenance.py
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py
    python -m unittest discover -s tests -p 'test_*.py'

The compact branch test checks source, all 16/256/4096 spatial lifts, temporal non-Haar and real two-digit source/tail readout. The long reproduction script generates and validates the full source holdout; it has no unverified random input.

**Not preclaimed:** all 12k+ native repository tests, exact-head CI, new Lean formalization, independent journal referee. They require actual run results; do not extrapolate from isolated 22-test bundle. The first isolated test invocation exposed a typo in the newly copied *expected* old-prefix SHA, corrected after comparing actual digits to #561. Source digits were not altered.

## Negative controls

- The same source temporal low-nibble path: exactly one-digit Haar, not two-digit Haar.
- Positive doubly stochastic mixing Markov matrix P=(3/4)I+(1/4)J/16: one-digit Haar and full support, but E2=135/16.
- Balanced periodic 16-cycle and order-2 de Bruijn period (uniform depth1/2 but not3).
- Rational s=1/5 original-source wrong seed: its 2-adic difference is divisible256 after n=2, but its real turn is 1/5.
- Changed derivative slope 3→11 is caught by exact original source congruences.
- Missing analytic source tail is rejected at a small/ambiguous depth.

All source/interpretive inference remains separate: **one-digit real π Haar and two-digit real π Haar are OPEN.**