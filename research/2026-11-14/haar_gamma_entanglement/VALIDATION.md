# Validation and epistemic authority — quantum/Haar/Gamma causal volume

**2026-11-14.** This package was built as a standalone local overlay on a declared two-qubit mathematical source. It contains no external physical data and does not attest any original BBP physical Hilbert carrier, actual wormhole, Bell test or source-cost meter.

## Commands actually executed

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python research/2026-11-14/haar_gamma_entanglement/independent_symbolic.py
python -m compileall -q observational_succ tests research/2026-11-14/haar_gamma_entanglement/independent_symbolic.py
```

- **22/22 focused standard-library unit tests PASS**, exact rational + Gaussian rational matrix entries (see `receipts/FOCUSED_TESTS.log`).
- **129 independently implemented SymPy symbolic assertions PASS**, including nine Gamma dephasing depths 0..8, marginal/conditional non-signalling for three local basis choices, source Bell/quadrature contrasts, partial transpose, CHSH spectrum, six direct Gamma Fourier integrals and one 16-child propensity control (see `receipts/INDEPENDENT_SYMPY.log`).
- **compileall PASS** (see `receipts/COMPILE.log`).
- The independent SymPy oracle **does not import the new module** and constructs its own density matrices, partial traces, Pauli matrices and probability checks. Both implementations share the same mathematical declared source, not independent empirical provenance. The Horodecki theorem and source quantum mechanical axioms are classical imports, not newly formalized.
- **NO full repository SUCC suite, provenance gate, ordinal probe, new Lean kernel check, Bell/steering laboratory observation, or physical gravity calculation performed here.** Hosted CI at this PR head is a separate evidence source and must be checked before integration.

## Controls and exact receipts

| Control | Expected and confirmed within declared source | Meaning |
| --- | --- | --- |
| Bell `γ=1` vs classical `γ=0` | identical every diagonal readout, `ZZ=1` | ordinary digit Haar incomplete for entanglement |
| Gamma depth 2, omega 1 | `γ=-i/2`, `XX=0`, `XY=1/2`, `CHSH²=5`, `PPT minor=-1/16` | complementary phase readout needed; still quantum entangled |
| Nonselective A probe X/Y/Z | B marginal `I/2` for every γ tested | no-signalling |
| Selective X measurement | Bell conditional B pure ±X vs separable B `I/2` | conditional steering, no remote channel |
| Joint Z dephasing | `ρ_1` becomes `ρ_0` while B remains `I/2` | genuine joint backaction, not A-to-B signaling |
| Co-moving compensated frame | entire Bell sector unchanged | frame covariance vs actual unrecorded one-side dephasing |
| 16-child radix Haar | zero average, unit L² norm with each prefix depth | lawful one-mode multiresolution normalization |
| Nonuniform policy | uniform contrast `1/4`, raw report `1/2`, propensity corrected `1/4` | observer attention changes sampling, not automatically source truth |
| Adaptive policy with missing children | input rejected | unsupported source-target identification |
| Fresh independent XY repeated `+` | posterior `81/97` after four copies; repeated Z leaves `1/2` | evidence is probe-dependent; duplicates not independent |

All exact results apply only to a **chosen** joint source representation. The observer's physical apparatus must be separately calibrated. No source authentication of quantum nature follows from software algebra.

**Git audit:** additive-only files are hashed in `FILE_HASHES.json`. Git blob hashes must match locally authored bytes when pushed. No commit or hosted CI should be claimed before actual remote readback.
