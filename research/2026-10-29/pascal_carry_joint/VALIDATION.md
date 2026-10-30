# Validation receipts and authority limits

**Research date:** 2026-10-29. Draft child intended from PR #370 at `4d4d49b575b476cc33f762d2b6a7fd6d1b924655`, itself stacked on #369/#367. Original four-pole source and `U0=0` unchanged. Source-independent theory and source-selected signed claims are explicitly separated.

## What ran locally

- The full *staged, isolated package* tests from predecessor PR #368 (25 tests) together with the new exact-rational suite (32 tests): **57/57 PASS**; see [stdlib_tests.log](stdlib_tests.log). Python 3.13.5. Includes exact posterior/diamond conservation, q/Green rational marginals, all depth-D labels, source-zero literal carries, torsion shift, 12 separate exact finite TV comparisons to asymptotic composite kernel, 26 Haar covariance checks, rank-inverse coefficients and altered-source negative controls.
- `python research/2026-10-29/pascal_carry_joint/joint_carry_probe.py` -> `SOURCE_PASCAL_CARRY_JOINT_EXACT_PASS n=1..9`.
- `python research/2026-10-29/pascal_carry_joint/independent_oracle.py` -> `RATIONAL_POLYNOMIAL_AND_COMPOSITION PASS`, `COMPOSITE_NORM 1 MEAN 46/15 HAAR_0_LAG 8845/49011`, `COMPOSITE_HAAR_CORRELATION PASS lags0..11`, four independent 65-dps source integrals, `INDEPENDENT_SOURCE_INTEGRALS PASS`, `INDEPENDENT_COMPLEX_SPECTRAL_ORACLE PASS`. See [independent_oracle.log](independent_oracle.log). Independent formula decomposition and direct integral methods; **not** independent human peer review.
- `python -m compileall -q research/2026-10-29/pascal_carry_joint tests/test_pascal_carry_joint.py`: exit 0.
- A preliminary generic SymPy infinite-sum oracle timed out before emitting results. It was replaced by exact *geometric derivative* formulas and an independent bounded-degree recurrence; the revised script passed as above. The original timeout is a tooling/performance failure, not a refutation of the mathematical identity.
- Exact signed phase coefficients are represented as rational residues and rational weights. No finite floating-point agreement is cited as an infinite mathematical proof.

## Technical evidence boundaries

- The 25 inherited PR #368 tests are present as a historical locally uploaded research backup. Their success **is not** the full SUCC native test suite.
- Root SUCC was **not cloned** (container Git HTTPS DNS failure: cannot resolve github.com). Thus root `scripts/verify_provenance.py`, native full unittest discovery, source/observer/ordinal probes, Lean, CIs on newly posted head and independent original-source audits are **NOT RUN locally**. GitHub remote hosted run status must be inspected after committing; do not claim success before completed.
- The universal TV theorem uses an inherited #370 bound `TV(q_t,w)<=22/t` and an inherited #367 positive-source moment estimate `E_mu_a Z<2/a` for `a>0`; each premise is stated explicitly in the paper and should be independently re-audited when integrating.
- Changed seed `s=-pi/16` is a *symbolic original-forcing* counterexample; its all-15 carries follow exactly from `U_t=-T_t`, not from a fabricated finite-precision π simulation.
- No proof of exact source-to-physical selection, source-unique conditional observation, π normality, RH, or scholarly priority is claimed.

## Git remote identity and side effects

The new branch and PR must be checked with GitHub's exact commit/tree/blob SHAs. All added files are under `research/2026-10-29/pascal_carry_joint/` and `tests/test_pascal_carry_joint.py`. The source-manifest, historical imports, original four-pole kernel, production modules and workflows are untouched. No merging, tagging, release or archival rewrite is authorized.
