# Random norm weaving on the genuine BBP four-pole source

Additive source-typed research on top of SUCC #648 (itself stacked on #646). This round takes the user's `sqrt(rand()) = max(rand(),rand())` identity literally and uses it to construct **three exact, typed observers**:

1. **Source-integral instrument:** a common threshold T weaves independent auxiliary variables into the original positive BBP weight Q(t), giving exact Bernoulli π/16, a nonzero third cumulant -1/45, a nested Bernoulli coupling to the source-chiral integral and a guaranteed rare positive defect click. A geometrically stopped max-norm machine reconstructs every original forcing moment and π/16 with finitely many random draws almost surely.
2. **Time-labelled interferometer:** a single random disk radius and *retained angular reference* reused at the actual original BBP time taps n,n+2 recovers the signed phase `-e(255 h z_n)` exactly after calibration. Randomizing phase independently at each tap makes the detector blind and creates false baseline norm energy.

3. **Coherent source-Gamma moment filter:** reuse the same source random row across n,n+2,...,n+2k. The signed Gram gives exact negative two-time correlations; the positive binomial collision energy has a proven `15 Γ(2k+2)/(256 n^(2k+2))` asymptotic for every fixed k. This is not an estimate for π normality.

This is a constructive stochastic **observer** for the original source, not a claim that the physical BBP digits are independent or that BBP normality has been proved. A chosen sampling representation is not unique.

## Reproduce

```sh
python -m unittest -v test_weaving_probe.py
python independent_audit.py
python make_report.py
```

See `THEOREMS.md` for domain, source/seed passport, exact proofs, conditional R0 gate, and hostile controls; `VALIDATION.md` for receipts; `NEXT.md` for the remaining signed arithmetic obligation. No existing SUCC files, main branch, frozen originals, Lean or workflows are changed.
