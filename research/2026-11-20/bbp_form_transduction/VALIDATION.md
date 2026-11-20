# Validation receipts — 20 November 2026

Scope: one new isolated research directory. The baseline published Main XXVI is not locally cloned in the execution container; network git clone was attempted and failed with `Could not resolve host: github.com`. GitHub connector was used to read `AGENTS.md`, `docs/METHOD.md`, the untouched `observational_succ/duck_bbp.py`, parent #672, sibling #670 and main frontier. Parent source and root repository suite are **not** silently assumed to have been executed here.

## Commands actually run

```sh
cd /mnt/data/bbp_form_transduction
python -m unittest discover -v -p 'test_*.py'
# 20 tests passed, 0 failures/errors, ~0.05 seconds
python independent_sympy_audit.py
# PASS; original/mutant symbolic source and jets; 60 finite p-square prime/modulus cases
```

The stdlib tests include: four-pole and zero-seed recurrence; exact rational finite terminal; finite locked counterseed; original vs matched-jet prime residue; p=11 denominator; p-square real/adic scaling; product formula; CRT prime factorization/reassembly; complex cofactor/gauge invariance; correctly transported Gaussian widths; positive phase-independent form-order defect; Poisson small-width asymptotic; mandatory signed interference; original finite shell locked control; short-support sparsity; physical-feedback positive/negative toy controls; invalid inputs.

The separately constructed SymPy audit returns:

```json
{
  "Qfactor_and_first_jet": "PASS",
  "source_matrix_original_det": 55,
  "source_matrix_mutant_det": 81,
  "independent_native_source_formula": "PASS",
  "p_square_jet_original": "15*z**4 - 59*z**6 + O(z**7)",
  "p_square_jet_mutant": "15*z**4 - 57*z**6 + O(z**7)",
  "heldout_p_square_residue_cases": 60,
  "verdict": "PASS"
}
```

Algebraic formulas and limit claims are justified by paper derivations in THEOREMS.md. Numerical finite checks do not certify universal quantifiers; the p-square asymptotic is proved by rational Laurent expansion, not extrapolation from finite primes. The limit of the *Gaussian norm* uses standard uniform convergence of the Fourier series and Taylor expansion.

## Explicit not-run scope

- The mandatory full root source/provenance verifier `python scripts/verify_provenance.py` was **not run**, since a complete local checkout could not be obtained.
- The inherited `python -m unittest discover -s tests -p 'test_*.py'` (14k+ tests) was **not run** in this container.
- The required `python scripts/observer_foundations_probe.py` and `python scripts/ordinal_succ_report_probe.py` were **not run** in this container.
- No source-wide CI outcome is claimed unless independently checked on the exact new commit. Lean, external refereeing and independent real-physics experiments are not claimed.
- No asymptotic pi-shell signed correlation, R0, pi normality, RH, energy-transfer experiment, or physical feedback measurement was performed or proved.

## Expected post-upload verification

Read back each GitHub blob against its tested local source snapshot, compare the branch against #672 head, and verify only added research files; open a **draft** stacked PR, do not merge. Run `python -m compileall`, focused tests, docs-link check, JSON parsing if applicable, and `git diff --check` when a checkout becomes available.
