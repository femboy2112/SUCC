# Transfer validation and authority

- `python -m unittest discover -s research/2026-10-30/arithmetic_barrier/transfer -p 'test_*.py' -v`: **19 tests PASS**; raw output `focused_tests.log`.
- `python research/2026-10-30/arithmetic_barrier/transfer/transfer_probe.py`: **PASS**; exact witness numerators/denominators, prime products and Stoneham controls in `exact_receipt.json`.
- `python research/2026-10-30/arithmetic_barrier/transfer/independent_oracle.py`: integer LCM reconstruction independent of Fraction/recurrence implementation; raw output `independent_oracle_receipt.json`.
- Timestamped commands, actual exit codes and stdout hashes are in `validation_commands.json`; source byte hashes and exact referenced heads are in `SOURCE_MANIFEST.json`.
- The added Champernowne control first failed because its 21-character expected
  string was compared with a 20-character slice. The integer-division/text
  reconstruction already agreed. Corrected only the fixture slice to21;
  retained the failed raw output as `control_fixture_failure.log`.
- `transfer_probe.py --approximate`: exhaustive finite q/all-translation search
  for four-state windows n=97,127,211,257,383; receipts retain exact minimum
  radii. These finite exclusions do not prove a general approximate-grid barrier.

The source used Python 3.12.3, standard library only. Probes are small and serial.
Fresh exact BBP holdouts include n=97,127,211,257,383; Stoneham holdout stages
include c=3,j=5 and c=5,j=4. Source coefficient mutation, rational aliases,
known p73 cancellation, nonnormal conductor2, periodic de Bruijn, and sparse
Kempner controls are retained. No mpmath decimal value is used as proof input.

The asymptotic exponential conductor bound relies on the classical PNT in fixed
arithmetic progressions; finite computations do not prove that theorem or an
effective threshold. The paper proofs establish TR-01--06 in their stated
domains. No Lean theorem, selected signed BBP cancellation, pi normality, RH,
or scholarly originality is claimed. The top-level campaign owns full-suite,
provenance/foundations/ordinal gates, final commit and hosted CI status; this
subdirectory does not claim those checks passed merely because its tests did.
