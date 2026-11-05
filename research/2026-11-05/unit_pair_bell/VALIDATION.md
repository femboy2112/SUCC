# Validation and computational scope — Unit-Pair Bell Gluing

**Parent:** SUCC #509 exact SHA \`16b0809b1f1426e77dad52381c3ac3fbeb187e3f\`. Additive child; historical original signed four-pole source U0=0, source contracts and production remain untouched.

## Exact independent finite checks actually executed

An independent stdlib Python unittest script \`/tmp/unitpair_independent.py\` (not committed to this research PR) ran **14 tests, 0 failures/errors, 0.029 seconds**. It checked:

- authentic r_original(1)=47/15 and positivity on indices 1..64;
- paired unit history (a+b=2·16^n, a−b=U_n) through 80 rational states;
- normalized source budget \(U_n/16^n<1/5\) through 80 states;
- exact Bell dark+bright coefficients;
- exact negativity >99/202 and bright probability <1/101 through 80 states;
- dephased pure-state local equality and joint bright probability 1/2;
- separable product zero-overlap counterexample;
- weighted residue matrix \(\begin{pmatrix}1/2&1/4\\0&-1/4\end{pmatrix}\);
- exact rational time-coboundary residue invariance on an independent finite-pole specimen;
- \(G(\tau)=\log2\), loop endpoints and Bell peak;
- 1/5 wrong-seed constant phase difference modulo1;
- zero-forcing/entangled-Bell nonnormal control.

A **separate independent Fraction/SymPy run** iterated 64 original exact states and checked full pair recurrence, negativity bound and the two original/radial pole residues. At n=64, the normalized source ratio was approximately \`0.19634954084936207\`, negativity \`0.49045372418429234\`, and bright projection probability \`0.009546275815707654\`. Analytic loop peak \`sin²((log2)/2)≈0.11538054931801395\`.

A further independent Fraction check for n=0..29 verified \(p_{\rm bright}+\mathcal N=1/2\) exactly.

The committed root \`tests/test_unit_pair_bell_coupling.py\` contains a standalone related 14-method suite. **Its exact committed bytes have NOT been executed in a full SUCC checkout in this session.** Do not claim exact-blob local suite execution, complete native test pass, hosted CI success, Lean formalization or external mathematical referee certification on this child.

All-horizon claims are paper proofs in THEOREMS.md; finite checks calibrate implementation and small counterexamples, never certify π normality.

## Next validation

From a checkout of the exact child SHA, run:
\`\`\`sh
python -m unittest discover -s tests -p 'test_unit_pair_bell_coupling.py' -v
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
\`\`\`
Run the expensive full \`test_*.py\` suite only once when the research integration gate is stable.

**Original fixed-h Weyl, critical signed-maximal rate, π normality and RH remain OPEN.**