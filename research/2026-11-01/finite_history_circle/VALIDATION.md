# Validation and execution receipts — exact scope and known boundaries

## Verified local programs

- `python -m unittest discover -s /mnt/data/succ_constant_curvature_round/tests -p 'test_*.py' -v`: **55/55 new methods PASS** on final authored source after the first-step branch extension.
- A combined replay from **13 previously mounted SUCC research snapshots** plus this package in `/mnt/data/succ_circle_combo` uses the same root-discoverable test filenames, 0 conflicting source paths: `python -m unittest discover -s /mnt/data/succ_circle_combo/tests -p 'test_*.py' -q`: **539/539 PASS** in ~1.9 s. This is NOT the complete >10,000 SUCC repository suite and does not substitute for GitHub CI.
- `python symbolic_probe.py` (SymPy optional): 6 algebraically separate symbolic conditions pass, including combined original source identity, exact six-sample mutant polynomial identity, and degree checks.
- `python independent_numeric.py` (mpmath, optional): 160-decimal-digit diagnostics at **N=(3,7,16,31), h=(1,3,5)**, 12 finite combinations. Independently computes Π_k through sine rather than our outward radical interval implementation, obtains exact rational original source phases and independently evaluates the signed Weyl sums and maxima; all 12 observed errors lie within proved rational analytic budgets. These diagnostics are **not** proof certificates.
- `python -m compileall ...` completed for the modules and root test.

## Independent methods and actual checks

1. **Source arithmetic:** four original signed linear poles (independent_oracle.py) vs combined numerator/denominator with exact Horner evaluations (finite_history.py).
2. **Source recovery:** exact Fraction Gaussian eliminator vs fraction-free Bareiss determinant/Cramer's rule, using original and shifted seven-node datasets.
3. **Six-source countermodel:** exact polynomial coefficient-convolution identity in Python, separately verified by SymPy. Uniform all-x positivity is a *paper inequality* with explicit polynomial coefficient bounds, not an extrapolation from 151 finite sampled positive numbers.
4. **Future source:** direct rational convolution vs finite ordered Wilson differences plus the REQUIRED terminal source boundary term; the full infinite tail bound is proved by the positive source inequality.
5. **Geometry:** nested positive-radical certified dyadic intervals by integer isqrt vs independent arbitrary-precision sine calculation at 12 nonfitted probe coordinates. **Additional exact independent Machin/arctangent rational π interval** certificates verify Π_k<π with the geometric defect and the exact unwrapped zero-seeded phase projector against its per-time error budget for N=1,2,4,7,16,31, no float tests.
6. **Seed/history:** 16 exact inverse branches, 16^N exact N-step preimages for N≤3 (4096 actual distinct Fraction states), and 16 altered initial seeds sharing positive-time phases. These are finite tests of general exact proofs.
7. **Phase and controlled echo:** all-horizon rational analytic budgets for every nonzero integer h, and optional 12-case high-precision direct signed sum diagnostics. No numerical positive result is promoted to a selected asymptotic saving.

## Assumptions and limitations

- The `(2,4)` rational source model is a DECLARED prior justified only by the already-known original four signed BBP poles. Seven points cannot infer this model class from arbitrary data.
- To recover forcing from seven **circle phases**, both the literal zero boundary U0=0 and first forcing lift 3<r1<4 are declared; without this, eight positive-time phases instead recover r2..r8 but not the original seed.
- Source observations, rational phase labels and model coefficients are assumed EXACT; finite or noisy digit samples have no proved stable recovery radius.
- The circle reconstruction is classical and its π limit is an *inherited* mathematical theorem; BBP's equality to the same π is also an *inherited* input. The geometric/Wilson predictor gives a new quantitative finite-to-finite bridge, not an independent π=BBP proof.
- No complete checkout was available to run `scripts/verify_provenance.py`, the full repository tests, foundations or ordinal probes. No new Lean proof declarations and no external blind referee.
- π base-16 normality, RH and a physical realized quantum tunneling law remain OPEN.

The detailed paper proofs give definitions, hypotheses, all-horizon quantifiers, counterexamples, source labels and the next falsification target.
