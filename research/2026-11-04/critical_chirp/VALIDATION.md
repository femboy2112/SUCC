# Validation — Critical coherent signed chirp

Date: 2026-11-04. Parent Gamma Prybar PR #501 head `af5c7ba30ea57d725bd334310798357d50f12fce`. This branch was created from that exact SHA. PREREGISTRATION.md was committed first, at `99917115ef73da3931b4d895cf097f1c00fb394e`, before fresh holdouts were run.

## Local executable checks ACTUALLY RUN

- CPython 3.13.5: `python -m unittest -v tests/test_critical_chirp.py tests/test_critical_chirp_receipt.py` → **8/8 PASS**, no skipped/error. Finite exact source, positive tail bounds, independent original four-pole vs collapsed polynomial source, common odd-register versus original Fraction phase, critical radix schedule, and all-finite coherent arc lower certificate.
- `python research/2026-11-04/critical_chirp/receipt_probe.py --write research/2026-11-04/critical_chirp/FINITE_RECEIPT.json` followed by `--verify` → `CRITICAL_CHIRP_FRACTION_RECEIPT_VERIFIED`. Exact Fractions are hashed, not rounded floats. Holdouts n=137,509,911 each satisfied the predicted source/tail inequality. Results use the same mathematical source but different computational expressions.
- Optional `python research/2026-11-04/critical_chirp/integral_calibration.py` → `QUADRATURE_CALIBRATION_ONLY_NOT_PROOF`. Independent mpmath 60/90-digit checks: for μ=8,32,128, `μ|∫_a^2 e(-μ/u²)du|` gives 1.077839222393716, 1.216711981784593, 1.258524507025296 respectively, trending toward 4/π=1.273239544735163. Same values at both precisions. This is finite numerical support for the analytic half-turn endpoint calculation, not a proof.
- `python -m compileall -q research/2026-11-04/critical_chirp tests` → completed with exit 0.

## Honest limits / ordinary baseline

- A local exploratory `python -m unittest discover -s tests -p 'test_critical_chirp*.py'` initially reported **one missing-module import error** for the native bridge, because this isolated staging directory does not contain the actual SUCC `observational_succ` package. The 8 standalone tests and exact receipt passed. The bridge test is intentionally intended for a genuine GitHub checkout. DO NOT interpret its local import failure as a proof/mathematical failure or claim native success without running it at the actual checked-out SHA.
- Native `tests/test_critical_chirp_repo_bridge.py`, full 11k+ SUCC suite, provenance/observer/ordinal probes, exact-head hosted workflows, and Lean proof checks have NOT been executed by this local staging run. The green GitHub Actions of parent PR #501 belong to parent SHA, not this child.
- Paper CC-01..04 proofs are explicit derivations in PROOFS.md, **not** newly compiled Lean. Same-model derivation of one fact via several computer implementations is not independent scholarly corroboration.
- No use of π digits to construct the source or prove a result; irrational counterseed appears only as the known completed boundary in the mathematical proof and is not numerically approximated in the rational tests.

π base-16 normality and original selected signed Weyl/current gates remain **OPEN**.
