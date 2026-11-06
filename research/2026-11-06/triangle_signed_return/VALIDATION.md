# Validation, provenance, and executed scope — 2026-11-06

## Exact live base

Connected GitHub source: femboy2112/SUCC, research child branch research/triangle-silver-return-spectrum-2026-11-06, stacked on PR #528 exact base SHA **45c5d41435fdf94998d81901b0e58b9fa7775106**. Root AGENTS.md inspected and followed: strictly additive research, no modification to original four poles, U0, frozen source, production, formal/Lean, docs contracts, workflows, main, release or license.

Preregistrations were committed on the connected repository **before new finite tests**:
- Initial prereg at b59df1d6f7faa3d77b050cef86f79d2f4ed5747e;
- Carry-borrow prereg at ab50d7f49eb96c611b86e15504dce51898c8d696;
- Dyadic-shell prereg at db6d9f0c0cb05399dcb4c7710eae287a6b8252ce.

Exploratory **already-seen** silver formula and determinant-two computations were explicitly disclosed in the first prereg; no claim that they were blind discoveries.

## Reproducible commands

From this directory, Python standard library:

    python -m compileall -q experiment.py test_experiment.py symbolic_audit.py
    python -m unittest -v test_experiment.py
    python experiment.py > FINITE_RESULTS.generated.json

Optional independent symbolic package (SymPy):

    python symbolic_audit.py

Executable script **experiment.py** and regression file **test_experiment.py** were tested locally. GitHub remote blobs after push were compared against local git hash-object:
- experiment.py: cb0990c27c6c50747e033fdd152c5a2aa4d54bde — MATCH
- test_experiment.py: 6783e65967dbe47cf8bb58ef6d7a37679e4db9c2 — MATCH
- symbolic_audit.py: 4989aa08688b30fc10f811213ac5eb1e0b61db32 — MATCH

The human-friendly FINITE_RESULTS.json contains semantically identical finite checkpoints in compact formatting, and is NOT claimed to be byte-identical to the pretty-printed Python stdout; regenerate the raw output with the command above. Both the quantitative experimental values and reproduction code are preserved.

## Executed result

- **10/10 focused unittest methods PASS**, 0 errors/failures, as recorded in TEST_STDERR.txt; stdlib compileall PASS.
- Optional SymPy algebra oracle PASS: full four-pole numerator/denominator decomposition; exact digamma rational-argument reduction; exact ratio (2+sqrt2)/(2−sqrt2)=(1+sqrt2)^2. Saved in SYMBOLIC_AUDIT_LOG.txt.
- Entire small triangle images modulo 2,4,8 enumerated exactly (image index 2, kernel cardinality 2); all-coordinate Q/2 spoof and source-plane inversion checked through k=12; missing-bit spoof correctly **succeeds** against the naive closure test.
- 21 independently recomputed source-clone modular controls for **non-dyadic** lags q=3,5,6,10,12,24,40 at n=0,7,43 PASS.
- Genuine original four-pole Fraction trajectory with literal zero seed, n up to 544. Original four partial fractions independently match combined rational source for n=1..256; 2-adic past graph independently matches original unwrapped state for fixed n/k samples.
- Exactly 4×384=1536 source-specific carry-borrow checks, n=128..511 and k=2,3,4,5, PASS. Strata are recorded without post-hoc threshold fitting.
- Original return-fiber samples at **N=512, h=1**:
  - Q=4,M=128: R≈0.003211346734, diagonal 0.0078125;
  - Q=8,M=64: R≈0.018183323497, diagonal 0.015625;
  - Q=16,M=32: R≈0.024190033738, diagonal 0.03125.
  Same \(|W|^2≈0.002210146797\), and low-state relabeling leaves R unchanged to printed float precision. Both negative and positive offdiagonal signed shells are preserved; no monotone saving is inferred.
- Nonnormal isometric shadow H(n)=n/(2n−1)^4: R≈0.99995 on the same three N=512 regimes. Exact theorem TS8 proves R_shadow→1 for any N→∞ irrespective of the factorization Q×M.
- Finite source mass partial sums N=128,512 were computed as rational fractions, but comparison to the closed form was done in FLOAT; the rigorous bound for the infinite tail comes instead from the analytic polynomial proof in TS5. Floating source/shell results are **not certified intervals**.

## Failed tests retained

See FAILED_SCRATCH_LOG.md. Two failures surfaced and were not suppressed: (a) assumed wrong carry always violates modulo-Q triangle closure (FALSE; half-modulus spoof), and (b) accidentally applied BBP-specific V-label assertions to the H-shadow (incorrect test helper, then corrected). The first produced the actual certificate-defect theorem.

## Boundaries, obligations, and CI

The local theorem arguments are not Lean-kernel proofs, externally blind peer review, or a world-novelty assertion. We did **NOT** execute the full SUCC native 12k+ suite, root scripts/verify_provenance.py, observer_foundations_probe.py or ordinal_succ_report_probe.py, full Lean or hosted exact-head CI in this local environment. A credential-less local clone could not resolve github.com; all writes were made through the authorized GitHub connector. Hosted CI is to be inspected after the draft PR exists, not reported as passing here.

Source-map σ is authenticated for original tests; false transport and shadow controls are explicitly marked separate. Probe μ covers finite exact controls and independent CAS algebra but NOT the all-horizon source-selected real signed inequality. Pathway φ to π normality remains **OPEN**.


## Follow-up execution: certified finite return signs + source Gamma moment

After preregistration files PREREGISTRATION_INTERVAL.md and PREREGISTRATION_GAMMA_MOMENT.md landed on the branch, the following were *locally executed* on the actual committed Python source bytes:

    python -m compileall -q experiment.py test_experiment.py certified_finite.py test_certified_finite.py first_moment.py test_first_moment.py
    python -m unittest -v test_experiment test_certified_finite test_first_moment
    python certified_finite.py > CERTIFIED_FINITE_RESULTS.generated.json
    python first_moment.py > FIRST_MOMENT_RESULTS.generated.json
    python symbolic_first_moment_audit.py  # optional SymPy

**18/18 total focused unit tests PASS**, 0 failures/errors. The new finite Fourier certificate uses rational Machin π enclosure and exact Taylor remainder errors, |R−Rhat|<1/2400; see CERTIFIED_FINITE_THEOREM.md. Five finite signs are rigorously decided, one fresh sample at N=768,h=2,Q=4 is AMBIGUOUS. First-moment constant B has exact algebraic/analytic proof and 0<E_N<241/(288N); displayed 75-digit Decimal values are **diagnostics**, not independent proof. All first-moment program behavior uses standard-library fractions/decimal; SymPy audit is optional.

Preserved symbolics: the first optional CAS audit initially FAILED solely because SymPy did not simplify two equal real logarithms in the same normal form; we replaced that brittle expectation with explicit positive algebraic ratio verification, retained the exact digamma equality, and reran the audit successfully. This is not a counterexample to the theorem. The source and error proofs do not depend on CAS.

Current research additional docs: CERTIFIED_FINITE_THEOREM.md, CERTIFIED_FINITE_RESULTS.json, FIRST_MOMENT_THEOREM.md, FIRST_MOMENT_RESULTS.json and corresponding scripts/tests; no original/frozen source changes. Full native suite, formal Lean, independent academic review and hosted exact-head CI are separate gates.
