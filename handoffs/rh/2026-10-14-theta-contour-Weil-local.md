# RH handoff candidate: authentic Xi contour → bounded positive Weil spectral shadow

**Origin:** `femboy2112/SUCC`, child of PR #78 (`96fbc5eac5705573014c0c8bbd4fc85c63bf1fd9`), draft-only `research/xi-complex-contour-weil-residue-2026-10-14`.
**RH PROVED: NO.** This is a mathematical observation / local spectral theorem, not global completed-Weil positivity. No write to `femboy2112/FuckingRH` is made or authorized implicitly.

## Mathematical statement

The original completed integer-Gaussian theta source defines Xi without unknown nontrivial zero input. Outward rational source quadrature, explicit Gaussian integer and time tails, and rigorous Simpson fourth-derivative enclosures give at `z0=(141347/10000)i`, `r=1/500`:

`|F(z0)|<1.094e-7`, `|F'(z0)|>0.00138260`, `sup_D|F''|<0.75`, and

`|F'(z0)|r-|F(z0)|-(sup_D|F''|)r²/2>1e-6`.

Rouché then shows exactly one simple authentic Xi zero in the closed-contour interior; real/even symmetry forces that zero onto the critical line. No zero oracle is used by the proof engine. The same source gives the conjugate zero.

Under the classical Weil explicit formula, for every real `f in C_c^∞(R)` and `A_f(s)=∫f(x)e^((s-1/2)x)dx`, contour integration of `(Xi'/Xi)(s) A_f(s)A_f(1-s)` gives `|A_f(rho)|²>=0`. The conjugate pair contributes a *genuine* positive rank<=2 kernel `2cos(gamma(x-y))` on `L²(-a,a)`. A source-only midpoint gamma approximation has exact operator-norm error `<=8a²/500`, verified with rational phase/interval arithmetic for `a<=1`. Thus we have quantitative source-to-operator identification for a **local** Weil spectral summand. This says nothing about the signed high-spectrum remainder or RH.

## Hostile controls / limits

- A mathematical proposal contour from original integer theta is not a preexisting zero input; Rouché is independently verified by outward rationals.
- False phase/site, undeclared integer-theta modes, missing time/prime modes, and forged certificate flags are refused.
- A concrete even real entire curve with the same authentic first two Taylor coefficients and norm² <1/3 has zeros at `s=3/4+20i` yet is not an Euler/theta source. Finite shadow equivalence and Fock positivity alone cannot establish Weil positivity.
- The rest of Weil's spectral form may be signed. No summing finitely many positive residues establishes a nonnegative total or a Hilbert–Pólya realization.
- Non-Euler control / conductor/parity and Suzuki full-form domain identification from PRs #71/#73/#76 still required for all-source extensions.

## Reproduce

`python -m unittest discover -s tests -p 'test_theta_complex_contour.py' -v`

`python scripts/theta_complex_contour_probe.py --verify research/2026-10-14/THETA_COMPLEX_CONTOUR_RECEIPT.json`

`python scripts/theta_contour_independent_oracle.py` (independent numerical calibration **only**; mpmath required)

Exact proof, rational results, counterexamples, scope ledger: `research/2026-10-14/THETA_COMPLEX_CONTOUR_AND_WEIL_SHADOW.md`.

**Next:** source-first quantitative control of the **complementary signed Weil spectrum** on a rigorously typed Suzuki form core. The finite contour itself is not RH progress without that complementary estimate.
