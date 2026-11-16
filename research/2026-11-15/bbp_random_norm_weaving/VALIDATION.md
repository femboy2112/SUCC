# Executed validation — source-attached random norm weaving

**Date 2026-11-15.** All source and statistic statements are scoped; none proves π-normality, R0 or physical quantum measurements. The new research is additive and source files were not modified.

## Executed commands on the isolated research package

```sh
python -m unittest -v test_weaving_probe.py     # 35/35 PASS
python independent_audit.py                    # exact SymPy source/Jacobian/cumulant PASS
python make_report.py                         # high-precision finite smoke and exact source jets PASS
python -m compileall -q weaving_probe.py test_weaving_probe.py independent_audit.py make_report.py # PASS
```

Full output in `TEST_LOG.txt`, `ALGEBRA_AUDIT.txt`, `REPORT_LOG.txt` and `FINITE_REPORT.json`. All `Fraction` congruences, source sums, source-moment formulas and conditional-probability kernels are exact arithmetic. `independent_audit.py` does not import `weaving_probe.py`; it independently recomputes Q and 29 source moments, the pair moments, κ3 = -1/45, rational kernel difference and the square-to-disk Jacobian. Monte Carlo outcomes and mpmath π phases are **uncertified numeric smoke**, not interval certificates. π/16 numerical equality is backed by the imported BBP identity, not by the mpmath result.

## Reproducible finite sample

- Original source jet modulo 16 is calculated from **unreduced exact rational U_n**, directly for q=16, n=5..12, and q=256, n=5..10. Expected `7+4(-1)^floor(n/2)` passes. This does not depend on assuming BC-0 infinite logarithm proof.
- Four finite source π-phase observations at preselected n and h are high-precision numeric smoke. They check the inherited two-time phase relation (not an all-B limit) and the two click quadratures.
- 24,000 deterministic seeded Monte Carlo rows were used for the original/chiral source Bernoulli program. They generated **zero** rare defect hits, expected ~0.510. The probability of observing zero under the exact model is about 0.6005. This is deliberately retained as a hostile reminder that finite negative detection does not contradict a proven small positive probability.
- A separate 62,000-row stochastic geometric stopping simulation approximated π/16 and passed a deliberately loose finite statistical tolerance. The theoretical equality comes from exact geometric weights and source moments.
- The normalized random disk reference was tested with 35,000 and 60,000 draws for radius, ordering and inverse-map consistency; sample-based tolerances are not a mathematical proof. The Jacobian derivation supplies the proof.
- Coherent wrong-seed reference control at z=0 gives zero calibrated shared energy. Independent fresh random angular references destroy the signed phase even for a fully coherent orbit. The zero-anchor mutant from #648 kills the source commutator; this round checks the predicted altered period via exact modular formulas.

## Not run / not claimed

- Full root repository test discovery, required root provenance/foundations/ordinal probes, hosted CI on this branch, new Lean kernel checks or an independent blinded mathematical referee.
- Physical randomized source, genuine Higgs, quantum field energy, physically isolated trials, π normality, unconditional all-shell R0 or fixed-frequency Weyl decay.
- Source phase access costs and analytic error guarantees for a real experimental π phase oracle. The added Monte Carlo components alone cannot create such access.

**Claim authority:** source identities and Jacobian/moment/cumulant formulas paper-proved with exact independent symbolic checks; stochastic program Monte Carlo finite tested; long-time arithmetic claims explicitly OPEN. All original BBP source/seed, provenance, main and current drafts preserved.

## Additional signed temporal-Gamma checks

The final focused suite includes six additional tests of exact time-paired signed original-source Gram entries, strict Cauchy–Schwarz 2×2 determinants, k=0..5 exact positive finite-difference energies, and the fixed-k=0..3 asymptotic coefficient numerically at n=16,384 using exact `Fraction` arithmetic (finite numerical convergence check only). The full asymptotic is proved by positivity and the original endpoint polynomial expansion, not by the finite tests. The coherent source amplitudes are a selected stochastic observer, not a claim about physical negative energy or Weyl saving.

### Test-development corrections retained in this scope note

An early test mistakenly required exact floating-point equality for a coherent zero-phase probability; it was replaced by an explicit numerical tolerance and independently tested exact formula. An initial finite-n Gamma convergence tolerance at n=4096 was too tight for k=3; the test was repaired to n=16384, and its finite-n approximation is not treated as a proof. Both were test design errors, not counterexamples to the stated paper identities.
