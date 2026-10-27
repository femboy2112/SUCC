# π₃ exact-source validation and authority boundary (2026-10-27)

**Status:** Local standalone **12/12** exact-focused tests PASS; production and test files have been uploaded as literal Git blobs matching byte-for-byte their locally tested versions. Full native repository, provenance/observer/ordinal and hosted CI for this exact head must be checked separately. No Lean normality proof, no random-access spigot claim, π base3 and base16 normality both OPEN.

## Verified tested code blob IDs

| Authored file | Git blob SHA |
|---|---|
| `observational_succ/pi_ternary_handle.py` | `afb154ac22e0fcd7611f2c5ee17fc970d8f72782` |
| `scripts/pi_ternary_digits.py` | `6b840051439529e408d0e6041aa41b2b58e9def7` |
| `scripts/verify_pi_ternary_certificate.py` | `3314073860b5ada1eb5540fa658a08fcc8e7f2ee` |
| `tests/test_pi_ternary_handle.py` | `f20096930ac1eebbe3e8073f909fcea4c73e0f49` |

These IDs were compared against the independently computed local `git hash-object` values before the tree was assembled; no code is silently reconstructed from test output.

## Reproduced local commands and results

- `PYTHONPATH=/mnt/data/pi3_research python -m unittest discover -s /mnt/data/pi3_research/tests -p test_pi_ternary_handle.py -v` ⇒ 12 tests, 0 errors or failures.
- `python scripts/pi_ternary_digits.py --start 1 --count 108 --certificate ternary_108_witness.json --pole-depth 6` ⇒ 108 digits, all 4 exact sources agree; sources use **19,19,55,55** terms respectively.
- `python scripts/verify_pi_ternary_certificate.py ternary_108_witness.json` ⇒ `EXACT TERNARY PI CERTIFICATE VERIFIED`.
- `python scripts/pi_ternary_digits.py --start 501 --count 32 --certificate ternary_window_501_532.json` ⇒ `11110221222121012002221022121220`; independently replayed and verified.
- `python scripts/pi_ternary_digits.py --start 999 --count 2 --source ternary-pi2` ⇒ `10` at positions 999–1000; **1000th trit=0**.
- Source mutation: π² first tap `243→244` rejected by disjoint exact source intervals. Original BBP last pole `−1→+1` rejected by disjoint exact intervals. Digit, endpoint, term count and certified-flag mutations rejected by replay verifier.
- Independent integer-square-root inequalities tested at 5 denominators × 7 numerators × 4 scale factors. 3-adic pole-depth histogram compared to full enumeration for every depth L=1..6. Source tag retains original signed forcing and no claimed normality proof.

The full source snapshot, SHA-256 manifest, 108-digit and 501–532 rational JSON witnesses, separate replay logs, and executable scripts are available in the originating research conversation's `SUCC_pi_base3_certified_handle_2026-10-27.zip`. This GitHub research PR deliberately commits the production interface, tests, proof dossier and handoff, **not** a fabricated CI-green/native authority statement.

## Exact mathematical proof contracts

1. Primary identities: David Bailey 2023 section 9 formulas (69) π√3 and (76) π², checked visually against the published PDF. These are published inputs, not newly proved identities.
2. Entire signed tail `|R_K| ≤ |c| b^(1-K)/(b−1) Σ_j |a_j|/(ℓK+j)^s`, proved by absolute values and geometric comparison.
3. Algebraic reconstruction: exact `isqrt(floor(3^(2n)*q))` from positive rational squared carriers.
4. Accepted prefix iff exact lower/upper integer floors agree, *not* iff decimal approximations agree.
5. All four routes agree on actual finite outputs; they share π as a mathematical constant, so agreement is cross-method corroboration, not four independent physical observations.
6. Sixth-slot pole depth `v3(2k+1)` grows arbitrarily; real coefficient weights suppress high-depth resonances rather than amplifying them.
7. Missing: authenticated base-3 selected signed Weyl cancellation, and the separate original base-16 selected signed Weyl bound. Finite computed trits imply neither.
