# Validation and authority — 2026-11-15

## Exact execution provenance

The original-main BBP forcing formula and four-pole identity were recovered from `observational_succ/duck_bbp.py`, `docs/PI_NORMALITY_FRONTIER.md`, and the existing #646 exact source contract. This additive research module independently implements that fixed rational function and does not edit the parent source.

Executed in isolated model container, Python standard library `unittest` plus separate `sympy` audit, on files in this dossier:

- `python -m unittest discover -s . -p 'test_*.py' -v`: **26/26 PASS**, raw log included.
- `python audit_algebra.py`: all **four source polynomial derivative residues** checked coefficientwise modulo 16, plus exact `4,-2,-1,-1` pole identity; **PASS**, raw output included.
- `python -m compileall -q .`: **PASS**.
- `python make_report.py > FINITE_REPORT.json`: **PASS**, with exact source tail bounds and two certified loop pulses.
- The q=16 and q=256 π real-circle return-pulse certificates retain exact rational lower bounds and future-tail interval widths. Real-circle numeric decimals are annotations only; no uncited floating-point interval replaces a rational inequality.

## Failure-before-repair chronology

The first local suite returned FAIL in 2/20 tests. A comparison erroneously read `U_n mod2^k` from `U_n mod1`, silently deleting the integer winding; this is precisely the potential source-coordinate error the project forbids. It was repaired by introducing a separate **unreduced** lifted rational state for the 2-adic computation; the signed circle states remain reduced only in the real-circle observer. The other failure incorrectly assumed that a mutated four-pole coefficient must preserve the original loop; mutant closure failed and the test was repaired to assert that discrepancy directly. The later exact run passed 20/20, and after strengthening odd-prime passport/phase controls, **26/26** passed. The initial failure is disclosed; it is not claimed as a success.

## Explicit limits

- The mathematical inequalities with `forall k exists n` are paper proofs, not machine-certified universal theorems. The 2020 pi irrationality measure is an imported external theorem; the additive `C_a` in the onset bound is not calculated.
- The native SUCC full ~13k tests, `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`, and Lean were **not run** in the disconnected standalone container. Hosted CI for this new PR head must be inspected separately; do not infer a pass from tests on another branch.
- This does not implement a physical Higgs measurement or quantum apparatus, nor show a phase density lower bound for π or full normality.

The theorem-domain hostile check also excludes terminating circle displacements (example 1/16): the escape lemma applies to nonterminating orbits, including all irrational sources, not arbitrary nonzero phases. This amendment was made before final validation.
