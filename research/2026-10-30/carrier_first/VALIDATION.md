# Execution and authority receipt

## Completed local checks

| Check | Result | Raw receipt |
|---|---|---|
| Parent current carrier suite | 57 tests PASS | receipts/baseline57.log |
| Five parent separate oracles | All PASS | receipts/parent-oracle-1.log through parent-oracle-5.log |
| New algebra | 14 tests PASS | algebra/receipts/focused.log |
| New analytic transport | 13 tests PASS | analytic/receipts/focused.log |
| New selected frames | 13 tests PASS | selected/receipts/focused-initial.log |
| New observer | 10 final tests PASS | receipts/observer-tests-final.log |
| Pinned hostile-control replay | 19 tests PASS | selected/receipts/inherited-hostile-controls.log |
| Full repository unittest discovery | **10008 tests PASS**,953.149s test time | receipts/native-suite.log |
| Original import provenance | PASS,72 imported files | receipts/provenance.log |
| Observer foundations | PASS | receipts/foundations.log |
| Ordinal report | PASS | receipts/ordinal.log |
| Source/ancestry/package audit | PASS | receipts/source-audit.log |
| Algebra Lean4.14 | Seven scoped declarations PASS | algebra/receipts/lean-final.log |
| Deliberately false Lean statement | REJECTED as intended, process exit1 | algebra/receipts/lean-negative-control.log |
| Final artifact/source/receipt audit | See final-audit receipt | receipts/final-audit.log |

The50 new focused tests are not counted as part of the native10008: their
research directories have explicit discovery commands. The19 replayed tests
and57 parent tests are inherited, not new independent evidence. Native-suite
warnings and negative-fixture messages remain in its raw log; its final exit
code is0 and unittest verdict is OK. No baseline failure was waived.

Additional independent implementation paths passed:

* Actual subsets, SymPy finite differences and fresh reachable diamonds.
* Gaussian resolvent via Hankel solve versus Gram--Schmidt/Jacobi continued
  fraction;54 finite theta derivative calibrations; five reflected germ
  derivatives; exact positive prime-weight fakes.
* Signed frame reconstruction via integer outward logarithms versus separate
  SymPy weights and high-precision direct source; five exact rational decodes.
* Eight full CRT products, with direct interval-phase agreement and separate
  real pi/Green-tail numerical reconstruction. No primary-only replacement.
*1028 selected hexadecimal digits independently enclosed by integer Machin
  arithmetic;18 exact count/coupling/lasso cases. The largest finite h1 bound
  is80707/286720 at N1024, using pi<22/7 and the proved source tail budget.
*768 independent CDF-W1 cases and2046 brute finite lasso words; repeated after
  the observer API correction. Repeats are not new independent authorities.
* Two rational Markov identities, three authentic resolvent degrees,90
  prime-germ moment cases and180 Hermite monomials in the cross-review.
* Five degrees of the finite-band countermodel integration check, each with
  40 further exact rational source terms; see band-countermodel-repaired.

The theta and separate high-precision phase oracles are numerical calibration,
not rigorous rounding certificates. The rational source and outward integer
interval implementations provide the finite certified statements. General
theorems rely on the written proofs. The seven Lean declarations cover only
the elementary listed algebraic statements, not the analytic dossiers.

## Failures preserved and repaired

1. **Lean normalization.** The first proof script failed because omega treated
   differently bracketed nonlinear products as different atoms. Explicit
   associativity rewrites fixed it. Original source and raw error are saved.
2. **Signed-probe domain.** Preregistered6013 is composite7*859. The probe
   stopped before phase measurement. The declared next eligible-prime rule
   produced6029; all frequencies, windows and thresholds stayed fixed.
3. **Large rational serialization.** The first final countermodel probe
   exceeded Python's4300-decimal-digit conversion limit when printing an
   exact partial tail. Calculation code was unchanged; output now records
   numerator/denominator bit lengths and a hash of their exact hex encoding.
   The failed source snapshot and receipt remain.
4. **Negative Lean control.** Its rejection is intentional and remains a
   nonzero exit. It is excluded from the positive compilation target set.

Read-only inspection also encountered guessed nonexistent paths and a
transient GitHub API disconnect. Those were resolved by inspecting actual
trees and retrying; no mathematical counterexample is inferred from them.

## Environment and reproduction

Existing environment, no installation performed:
Python3.13.13 at
`/media/leah/SPANKBANK/SUCCYBOI/SUCC-zero-dispersion/.venv/bin/python`,
mpmath1.3.0, SymPy1.14.0, NumPy2.5.4, SciPy1.18.1. System Python3.12.3
ran standard-library probes and the receipt wrapper. Each receipt records
its actual interpreter, cwd, argv, launch head, UTC times, exit code, timeout,
raw log hash and size. Commands had a1GiB memory cap and one BLAS/OpenMP
thread. The complete native suite took960.603s including wrapper overhead.

From the repository root, with the existing dependencies available:

```bash
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s research/2026-10-30/universal_nz_carrier -p 'test_*.py'
python -m unittest discover -s research/2026-10-30/carrier_first/algebra -p 'test_*.py'
python -m unittest discover -s research/2026-10-30/carrier_first/analytic -p 'test_*.py'
python -m unittest discover -s research/2026-10-30/carrier_first/selected -p 'test_*.py'
python -m unittest discover -s research/2026-10-30/carrier_first -p 'test_observer.py'
python research/2026-10-30/carrier_first/band_countermodel_probe.py
python research/2026-10-30/carrier_first/artifact_audit.py
```

Each front's validation file lists its separate oracle commands. Saved
probe programs that write data refuse to overwrite earlier receipts. Use a
fresh checkout or a fresh output name when rerunning those generators;
preserve the committed original receipts. `run_receipt.py --name NAME --
COMMAND...` likewise refuses to overwrite an existing name.

Launch HEADs remain the parent because tests ran on the additive uncommitted
research tree. Final source hashes bind those files; native production code
was unchanged. The manifest excludes itself and the final audit's own outputs
to avoid circular hashes. No failed gate is rewritten as a pass.

Hosted CI is separate: the child PR body records the exact pushed commit and
its live workflow states. Parent/sibling successes in the JSON snapshots are
not credited to this child. No external referee or new dependency/kernel
certificate is claimed beyond the stated Lean scope.
