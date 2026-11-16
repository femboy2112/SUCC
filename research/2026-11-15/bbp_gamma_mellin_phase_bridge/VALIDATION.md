# Validation and authority (2026-11-15)

This is a paper-derivation plus executable finite-check research branch. Run:

```bash
python -m unittest -v test_gamma_phase.py
python independent_audit.py
python -m compileall -q gamma_phase.py test_gamma_phase.py independent_audit.py
```

- Focused original-source `Fraction` and complex `mpmath` tests: **30/30 PASS** in the isolated bundle.
- Independent no-primary-import `SymPy` rational/Taylor and separately implemented t-integral oracle: **35/35 checks PASS**.
- Algebra checked: original four-pole rational source, factorized Q/R, K's first three boundary coefficients, arbitrary complex-beta two-axis expansion coefficients, source successor, source Green inequalities.
- Numerical checks: direct t-integral complex Gamma windows against first-, second- and third-term asymptotics; fixed lag q=4, proportional lag q=n, saturated lag q=n², complex Gamma(3+i omega) response; source-conditioned full two-frequency phase responses and explicit TV envelope. Numerical checks **do not establish the infinite limit**.
- Hostile controls: coherent wrong seed does not change source-only windows, positive endpoint mutant changes total constant despite same Gamma leading endpoint jets, noncommuting Fourier/expectation order, wrong scale and reverse orientation.
- Full source chronology, exact integer winding, original odd-denominator CRT and original π real phases are not artificially randomized or presumed equidistributed.

**NOT RUN OR NOT CLAIMED:** Full SUCC repository native unit suite, mandatory provenance/foundations/ordinal probes on the exact new stacked head, Lean verification, hosted CI, external referee, physical quantum experiments, π R0, π base-16 normality, RH. Original π equality is an imported classical result. This is a same-model numerical/symbolic double-check, not independent third-party proof review.
