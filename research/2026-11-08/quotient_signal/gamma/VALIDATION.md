# Executed Gamma calibration checks

From the repository root, Python3:

```
python3 research/2026-11-08/quotient_signal/gamma/oracle.py --output research/2026-11-08/quotient_signal/gamma/RESULTS.json
python3 -m unittest discover -s research/2026-11-08/quotient_signal/gamma -p 'test_*.py' -v
```

Both commands exited0. Seven focused unit tests passed. The oracle checked
1,031 individual strict tail inequalities and independent forcing-integral
identities;185 rational kernel inequalities;192 exact shifted-seed
identities;five weighted finite-part/gamma-estimator bounds with separate
backward-recurrence endpoint identities;three mutated four-pole controls
rejected the original n^-2 tail bound. These are finite instances, not
additional unit tests or universal proof certificates.

All five cumulative observations passed their preregistered rational
bounds. The exact outward dyadic enclosures are retained in RESULTS.json;
the displayed midpoint progression is:

| N | N(C_N-C), target7/512=0.013671875 | G_N, target gamma |
|---:|---:|---:|
|64|0.0134637559756663|0.598471576321763|
|127|0.0135661065111355|0.587983969254303|
|257|0.0136193786076924|0.582551524734871|
|521|0.0136459229792472|0.579851325404248|
|1031|0.0136587467446788|0.578548428203174|

Only the last three N values were designated fresh holdouts; all cases
share the same source and instrument, so they are not independent data
families. The formulas were derived before numerical checks. This is not
a fitted gamma discovery or a fitted convergence rate.

The exact source and ordinary constants are constructed without imported
pi digits, Gamma evaluation or mpmath: Fraction forcing; positive beta
integral identities; finite geometric tail bounds; Machin alternating
arctangent intervals; rational atanh logarithm intervals; integer-square-root
bracketing. Gamma is enclosed independently with
`H_4096-log(4096)-1/8192 < gamma < H_4096-log(4096)`.
The oracle does not numerically multiply complex phases and call their
agreement a proof. The phase-product result is an exact exponent identity
plus the proved scalar remainder estimate.

Source hashes and classical identity references are in SOURCE_AUDIT.json.
Paper results are not Lean-kernel results. Required whole-repository gates
and publication are handled by the integrating parent and are not claimed
as executed by this subtask.
