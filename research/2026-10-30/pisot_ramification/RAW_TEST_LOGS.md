# Raw local execution receipt — Operation Pisot Ramification

Date: 2026-10-30. Independent oracle executed locally:

    python /mnt/data/succ_pisot_ramification_20261030/independent_oracle.py

Actual final output:

    Exact polynomial, discriminant, basis-index, matrix-inverse and positive-Pisot grammar: PASS
    A3 characteristic: x**3 - x**2 - 3 nonPisot dominant root: 1.8637065278191891
    B3 characteristic: t**3 - 8*t**2 + 5*t - 1 Pisot unit root: 7.3371085496550469
    Conjugate moduli: 0.369179457962 0.369179457962
    Ramified prime candidates (indeed ramified; disc squarefree): {3: 1, 5: 1, 17: 1}

Independent local Jupyter controls also checked:
- A2=[[1,3],[1,0]], B2=A2+I have characteristic polynomials x^2-x-3 and x^2-3x-1.
- A3/B3 characteristic polynomials, integer inverse and B3 determinant 1.
- Polynomial basis change C=[[1,2,13],[0,1,7],[0,1,8]] has determinant 1.
- B3^{-1}=2I-A3=B3^2-8B3+5I exact.
- Positive combinatorial refinements length2 and length3 hold coefficientwise through degree22/24.
- Quadratic shift theorem checked on grid 1≤a,b≤29 using double precision as secondary calibration only; theorem is exact algebra in main dossier.
- Positive matrix [[2,1],[1,3]] has real conjugate 1.381966>1 and A-I=[[1,1],[1,2]] has Pisot unit x²-3x+1.

Disclosed initial failure: first SymPy implementation directly expanded high powers of 1/(1-z-z^ell) and timed out. Replaced with finite coefficient convolution. Final executed independent source is byte-equal to committed independent_oracle.py Git blob a98d20b3b6b180b16804f124d7261176bdf347ad. A vacuous conditional assertion in the first source revision was removed.

Prepared but not actually run from the exact committed file: 14-method standard-library pisot_ramification_probe.py. It has source blob SHA 7a8f240b065925a25dcb2178a0e132a3a8d21f71, verified by GitHub fetch. This report does not pretend it was executed.

NOT RUN: complete SUCC AGENTS root suite, hosted exact-head CI, Lean and independent referee. π normality and RH remain OPEN.
