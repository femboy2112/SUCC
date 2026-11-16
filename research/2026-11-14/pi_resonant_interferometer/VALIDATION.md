# Validation and proof authority — original BBP phase-collision detector

**Executed isolated Python 3.13 environment on 2026-11-14.** All mathematical claims in THEOREMS.md include their own hypotheses. No physical Higgs/quantum experiment has been run, no direct evidence for π normality, no RH theorem, no newly verified completed Weil positivity.

### Executed commands

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python research/2026-11-14/pi_resonant_interferometer/independent_oracle.py
PYTHONPATH=. python research/2026-11-14/pi_resonant_interferometer/probe.py
python -m compileall -q observational_succ/pi_resonant_interferometer.py \
  tests/test_pi_resonant_interferometer.py \
  research/2026-11-14/pi_resonant_interferometer/{independent_oracle,probe}.py
```

- **29/29 focused stdlib/SymPy/mpmath tests PASSED**, including independent checks of Machin/Taylor click enclosures for the actual completed and rational BBP sources at eleven indices each.
- **Independent symbolic oracle PASS:** both positive coefficient polynomials in `m-2`, 984 different exact rational source-innovation comparisons (82 clock starts times 12 lags), 7 independently encoded pair-collision energies, independent Gamma(2) phase integral at 85-digit working precision, periodic `1/15` false-normality control. Numerical quadrature is diagnostic for a known analytic identity, not a theorem certificate.
- **Rational finite shells** B=4,8,16,32 certified by upper/lower rational Machin/Taylor plus original BBP Green-tail error. Exact finite output in `receipts/FINITE_SHELLS.json`.
- **Python compileall PASS.** Exact raw logs in `receipts/FOCUSED_TESTS.log` and `receipts/INDEPENDENT_ORACLE.log`.
- **Historical source:** original `observational_succ/duck_bbp.py` and `docs/PI_NORMALITY_FRONTIER.md`, and the already-established IAD lag no-go and Gamma source. No modifications to any of them.

### What is and is not proved

HD1/HD2 come from displayed positive-polynomial and geometric-series derivations and are exact for the stated original forcing/clock. HD3/HD6 are finite algebraic identities. Click-probability intervals are **rigorous for the stated finite indices**, relying on classical Machin identity and elementary Taylor/geometric upper bounds. A *hypothetical* randomized Hadamard phase oracle produces the displayed Bernoulli law; no actual qubit gate attached to π is available. All asymptotic R0, π normality and RH obligations remain open.

### Hostile controls

- The relative phase **without** compensating the harmonic preserves source history but admits rational aliases; a special 1/17 seed is phase-aliased at lag 2. The fully compensated lag is source-independent and cannot authenticate the selected origin.
- The nonnormal `x=1/15` has positive click probability on every epoch and pair energy 1. This defeats any claim that near-certain eventual clicks imply normality.
- One-sided unrecorded Gamma(2) phase rotation makes the perfectly coherent zero-phase input click with probability 1/2; a co-moving compensated phase does not. This refutes uncalibrated smoothing as arithmetic cancellation.
- Selection-weighted Haar/click averages have bias; conditional unbiasedness needs positive, known propensities and an authentic source likelihood.
- A single resonant lag signal, an all-positive Gamma factor or a finite shell certificate does not imply the all-lag signed Fejér bound.

**Not executed:** full-root SUCC suite, required root provenance/observer/ordinal probes at this branch head, new Lean kernel check, blind independent research review, an actual high-energy Higgs experiment, or π normality proof. GitHub CI status is separate and must be checked on the exact new commit.
