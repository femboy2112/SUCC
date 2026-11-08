# Reproducibility and limited truth-status receipts

**2026-11-08.** Isolated stdlib/fraction source module and tests, Python 3.13 (mpmath 1.3 used for explicitly noncertifying Gamma/zeta checks). Intended source baseline SUCC `main@43a607818907120d4cdab73d240f5b4d7700b63f`. No existing source, provenance, formal or frozen file modified.

## Executed commands (local, not full SUCC checkout)

```sh
cd xi_cayley_round
PYTHONPATH=. python -m unittest discover -s tests -p 'test_xi_cayley_prime_pinbed.py' -v
python -m compileall -q observational_succ tests
```

**Observed:** 12/12 focused tests pass, zero failures/errors; compileall exits 0. Relevant local Python source and test Git blob SHAs are included in the PR's exact-head readback receipt after push.

- Exact Fraction Cayley images of rational-height critical line, Euler and half-density convergence horodisks, inverse-reflection symmetry, synthetic offcritical and critical entire polynomial controls.
- Exact independent rational formal-log polynomial oracle for synthetic Li coefficients at n=1..9 and several offcritical `a`; exact toy Jensen zero count for disks that exclude/include the prescribed fake zero.
- Numerical Jensen angular integral check of the fake polynomial on r=1/5 and r=1/2 versus its *independently exact* Jensen log; numerical circle phase-winding of fake and on-line controls. These are NUMERICAL DIAGNOSTICS; no rigorous interval enclosure for actual xi was run.
- Exact sieve/fraction finite prime Mertens products for P=2,3,5,7 and larger finite samples; fake-composite-six rejected and original vs half-density local Cayley zeros distinguished.
- Numerical full original `xi(s)` comparisons in Re(s)=2 and 3 against **unshifted true-prime finite Euler products**, *including* the exact pole, Gamma and pi completion. The independently paper-derived absolute prime-log remainder encloses observed finite discrepancies; code evaluation is standard floating/mpmath, not an interval certificate.

### Mertens boundary finite diagnostics (not a proof of the asymptotic)

| Prime cutoff P | log(P)*prod_(p<=P)(1-1/p) |
|---:|---:|
| 50 | 0.5426136013384832 |
| 100 | 0.5540815989540405 |
| 1000 | 0.5592882264035702 |
| 10000 | 0.5607687409613624 |
| 100000 | 0.5612887094185551 |

The known classical limit is `e^-gamma ≈0.561459483566885` (Mertens). The agreement is a calibration, not an independent proof.

## Explicit missing gates

- Full SUCC project-native `python scripts/verify_provenance.py` and full `python -m unittest discover -s tests -p 'test_*.py'`: NOT RUN locally on this isolated directory.
- `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`, Lean proof kernel, exact-head hosted CI, independent scholar review: NOT RUN at authoring time.
- Actual arithmetic bound `exp J_xi(r)` rigorous enough to exclude a genuinely new zero-free disk: NONE. The source-log continuation and all-radius vanishing conditions remain RH-EQUIVALENT / OPEN.
- Finite numerical contour winding is not a mathematical zero detector without a validated error bound on F'/F between observations.
- Mertens theorem and Li criterion are classical externally sourced theorems, not discoveries in this work.

**The original zeta Euler source was never modified.** The half-density factor is deliberately tagged CHANGED-SOURCE and must not be fed to the source-authority evaluator as a proof of RH.
