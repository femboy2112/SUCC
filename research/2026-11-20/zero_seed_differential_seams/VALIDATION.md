# Validation and exact evidence scope

**Research-only local execution, 2026-11-20.** All checks below were executed on the newly authored isolated research files in the container. GitHub connector publication, blob SHA verification and branch comparison are documented in the draft PR separately and must be checked before claiming remote equality. This receipt does not imply full SUCC validation, an external referee, or Lean kernel checking.

## Commands and exact outcomes

1. `python -m unittest discover -s . -p 'test_*.py' -v` — **26 tests, OK**, no skips and no failures. Raw stdout/stderr: [`focused_unittest.log`](focused_unittest.log).
2. `python independent_audit.py` — **737 independent-implementation checks, PASS**, using SymPy rational Mellin integrals, exact Taylor/moment identities, signed quarter-current Fourier characters, new high-precision 110-digit late clocks `71,317,997,3007`, and exact original-source controls for prime-square `p=7,79,131`. Raw output: [`independent_audit.log`](independent_audit.log), structured [`independent_audit_receipt.json`](independent_audit_receipt.json). This second implementation was independently coded but shares source theory and is **not** a blind mathematical referee.
3. `python -m compileall -q seam_differentials.py test_seam_differentials.py independent_audit.py` — pass (exit 0).
4. Relative Markdown links: checked after all files existed, pass.
5. `sha256sum -c SHA256SUMS.txt` — all 13 declared source/evidence files pass; the manifest does not hash itself.

## Precise numerical and model receipts

- Exact outward rational source-lag enclosures distinguish source `Q` and matched-jet mutant `Q+(1−t)^2` at clocks `n=0,19,99,999` with terminal depth 43; all comparisons are exact `Fraction`, not floating guesses.
- The analytic original lag mean is strictly increasing in the actual chronological clock and strictly less than `1/15`; `∂_τ μ_n` is negative at every checked clock and each τ sample. Proof gives all-clock scope; finite tests are only implementation calibration.
- The high-precision oracle independently confirmed the signed second-order split `lim_(m→∞) m² (μ_(m−1)(1)−μ_(m−1)(0))=−4/3375`; the proof is an independent algebraic expansion.
- Original four-pole rational intervals with independent code determine quarter-head source-order signed contrasts: `p=7→0`, `p=79→+1`, `p=131→−1`. All clocks and root/carry labels are retained. These are different-source counterfactuals; the unmodified original phase is not claimed to satisfy a new asymptotic lower bound.
- The sharp current formula `||Dq_n||TV=2·16^n` and Fourier coefficients are proved for all `n`; finite tests check a collection of frequencies and clocks. Fixed λ Gaussian attenuation is an analytic theorem, not a measured physical heat process.
- The original zero-seeded four-pole source rational tail verifies the known first 12 digits `3243F6A8885A` only to check source-first quarter parity, not to claim discovery of π's digits.

## Explicitly not run / not claimed

- **Not run:** native full >14k SUCC unittest suite, root `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`, hosted GitHub CI, formal Lean proof, physical observation.
- **Not claimed:** source-selected all-B positive π phase displacement, π base-16 normality, all-positive-integer Collatz, RH, quantum speedup, physical zero-point energy or an unconditional real-phase mixing theorem.
- **Boundaries:** the τ-derivative compares declared source-family members, the s-distributional derivative compares seed perturbations, and the p-swap compares two ordered sources. Only `μ_(n+1)(0)-μ_n(0)>0` is the native **unchanged-source temporal differential**; it remains a source-lag statement, not a selected π orbital-density statement.
