# Scope and validation — Multiplace BBP Difference Resolvent (2026-10-31)

**Baseline:** Draft PR #429 exact head 33d53f576fe2c2e847e51c24ccf7a94aa6ec6f10, ultimately Main XVII e8598cfa5d32fd1de8e94a3e458a366a0850d59e. New additive research branch only. Original four signed poles, U0=0, production, historical archive, all prior formal proof contracts, workflows, and main remain unchanged.

**Independent exact rational scratch checks actually run locally (before GitHub push):**
- Symbolic factorization of P(t)=4−2t³−t⁴−t⁵ into (1−t)(t²+2)(t²+2t+2); full original BBP r(n) combined polynomial and its derivative checked with SymPy.
- v3(r'(y))=−2d(y) checked with Fraction arithmetic for EVERY integer y from −1000 to1000 (no failures).
- Exact v3(r(y−6^m)−r(y))=m−2d(y) checked for y from −60 to60 and every m=1..9 satisfying m>d(y) (no failures).
- Source moment C_j(y) positive and fixed-J real prefix bounded by 15(J−1)(J+2)/(2(8·6^m+1)²) for tested m=2..8, J=1,2,4,7 (all checks passed).
- Exact polynomial fraction for Δ_m, its reduced-denominator factor5 and the v2/v3 profiles checked for m=2..8. One initial test for improved combined-denominator bounds mistakenly included y=16, which has only one 3-adic pole; it was corrected to the actual colliding-pole class {2,5,8,11,14} in the committed root regression. This is retained as a finite-scope calibration correction, not a theorem failure.
- Fixed-J real prefix for J=7 decays rapidly as m grows (m=2: ~0.0045872; m=8: ~2.24×10^−12), while the FULL source difference grows toward 47/15. These numerical displays corroborate the proven exact inequality; they are not extrapolated.

**Committed execution artifacts:** 22 discoverable root unittest methods in tests/test_multiplace_bbp_difference.py, and independent stdlib-only exact rational source/CRT/pole-resolvent evaluator under research/2026-10-31/multiplace_bbp_difference/multiplace_difference.py. The complete new file was NOT executed locally against a full checkout: only mathematical scratch controls were run. Hosted exact-head GitHub CI is the integration check, to be observed after opening the draft PR. Do NOT report root-suite or Lean authority without its actual result.

**Reproduce:**
- python -m unittest discover -s tests -p test_multiplace_bbp_difference.py -v
- python scripts/verify_provenance.py
- python scripts/observer_foundations_probe.py
- python scripts/ordinal_succ_report_probe.py
- python -m unittest discover -s tests -p test_*.py

**Status:** TD01–TD07B paper proofs with declared scopes; mathematical original-source synthesis, not a scholarly priority claim; all pi-normality/RH bridges remain OPEN.