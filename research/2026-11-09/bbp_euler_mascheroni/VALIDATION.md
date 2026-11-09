# Validation and source provenance

## Tested environment

New research is implemented in Python >=3.10, using standard-library `fractions.Fraction`, `math`, and `unittest`. A subset of tests invokes independently implemented `mpmath` high-precision quadrature and q-Gamma derivative, which is in the existing SUCC research/test dependencies (`pyproject.toml`). No source or old test file is changed. The local test harness cannot download/execute the complete SUCC repository; it carries an **explicitly marked test-only exact copy** of `duck_bbp.forcing`, checked against the original four fractions, but that copy is NOT included in the GitHub commit.

## Executed commands

From the isolated research worktree:

`PYTHONPATH=. python -m unittest discover -s tests -p test_bbp_euler_mascheroni.py -v`

Result: **19/19 PASS**, Python 3.13, including exact BBP source equality, grouped-Laplace equality, q-integer composition, independent endpoint exponential polynomial derivatives, Mellin rational prime logs, source gamma finite part, actual 3³ and31 valuation records, full reduced denominator factors, canonical q-Gamma derivative oracle, exact Lambert tail, divisor-series coefficients, two-pole hostile source and invalid inputs.

`python -m compileall -q observational_succ/bbp_euler_mascheroni.py tests/test_bbp_euler_mascheroni.py research/2026-11-09/bbp_euler_mascheroni/experiment.py`

Independent symbolic audit of jets with `sympy` and independent high-precision integral quadrature with `mpmath` are **numerical/symbolic corroboration**; the universal proof is on paper, not formalized in Lean. The primary external source for the q-Gamma product and recurrence is [NIST DLMF 5.18.4/7](https://dlmf.nist.gov/5.18); for ψ(1) and ψ(2) use [DLMF 5.4](https://dlmf.nist.gov/5.4).

## Provenance and authority boundary

- Four-pole source, zero seed and future tail: frozen imported SUCC `observational_succ/duck_bbp.py` and classical BBP identity.
- Positive source Q and free-energy cocycle: existing SUCC Oily Macaroni III and source Mellin Hilbert work (Oct 26), not newly invented.
- Gamma16 q-blocking: existing exact GM16-06 from draft #568, not newly invented.
- The blocked-clock Euler finite part, large-g π bridge, exact local Mellin correction and two-prime passport form this round's new-to-SUCC composition, unreviewed academically.
- All numerical constants are finite validation scope. No normality claim. New GitHub full-suite/CI status must be checked at the precise resulting research head and must not be borrowed from parent commits.
