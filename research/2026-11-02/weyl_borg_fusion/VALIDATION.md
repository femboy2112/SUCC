# Validation and boundary report

**Staged local research directory, not full SUCC clone** (container git DNS resolution failed). Original base SHA verified via connected GitHub API: 81045770234a114247e43eb08ae5c6d446e9514a.

- python -m unittest discover -s tests -p 'test_weyl_borg_fusion.py' -v: **12/12 PASS, 0 skips** in the staged local directory.
- python -m compileall -q of staged directory: **PASS**.
- Exact four-pole signed-vs-combined independent Fraction evaluation n=1..256: PASS, r(1)=47/15.
- Exact zero-seed recurrence, first 80 states: PASS.
- Complete rational phase exponents and aliases M=16,256,4096, positive/negative frequencies, first 64 authentic states: PASS.
- Source 2-adic modular carry with r(1) mod256=225: PASS.
- Exact finite positive Green-tail enclosures and rational 2nd/3rd source bounds at selected n: PASS.
- Source-sign mutation rejected, uniform-cell high-alias coherent controls h=M: PASS.

The universal all-n statements in PROOFS are elementary paper derivations, not inferred from finite data. Different formulas share the same original mathematical source and are not external/independent verification.

NOT RUN / NOT CLAIMED: full >10k original SUCC test suite, scripts/verify_provenance.py, complete observer foundations and ordinal scripts, Lean compilation of these new theorems, external peer review, full baseline source/proof CI and hosted exact-head CI. All remain UNVERIFIED until independently executed. Neither π-normality nor source-specific signed cancellation is claimed.
