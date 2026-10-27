# Operation Goldbach–Seinfeld Bin Window — exact validation receipt

**Date:** 2026-10-27. **Parent:** original-source solenoid PR #320 head `5ea12570aec86c3a8b555e927c10337804568a62`. **New research:** exact 2-adic zero boundary, no-startup conjugacy/odometer, finite source-labelled ghost zero and honest real/2-adic Fourier firewall. **π base-16 normality remains OPEN.**

## Actual local scope

- `16/16` focused exact Python 3 tests passed in `0.083 s` on the final authored source/test versions; the raw stdout/stderr is retained in `BBP_BINWINDOW_FOCUSED_TEST.log`.
- The isolated local source interface temporarily supplied *only* the original signed four-pole `succ_internal_matrix_walk.authentic_r` function via a byte-visible faithful independent Fraction implementation. **That shim is excluded from the GitHub commit**; the actual native module is imported on the repository branch. No claim of native combined-suite validation before hosted/native execution.
- Tests independently reconstruct the original signed four poles, including negative-index algebraic extension, check original recurrence, compare zero windows through early source times and hex depths 1–6, enumerate all 16/256/4096 states for odometer cycles, and verify source-seed/2-adic character mismatch.
- The original p-adic boundary is corroborated through `48` hexadecimal precisions by exact modular rational operations; the all-depth boundary is instead proved by the analytic 2-adic logarithmic primitive in the full dossier.
- The **counterfeit** from #320 has infinite-past boundary `−1`, not zero. This exact countermodel distinguishes the new original-source boundary from the older generic 2-adic time-equidistribution property.
- Independent rational algebra checks the raw generating function against the canceled quartic and the derivative-of-log expression at 25 exact rational arguments; this corroborates, not substitutes for, the `Q_2(i)` analytic proof.
- Finite ghost receipts establish that formally nonzero rational negative-time contributions vanish modulo `16^k` at every tested early index; the theorem proof supplies all indices.
- A deterministic JSON receipt is regenerated and verified byte-for-byte by `scripts/bbp_binwindow_conjugacy_probe.py --write` and `--verify` and its false `pi_base16_normality_proved=True` mutation is rejected without modifying the correct receipt.

## Native repo / proof authority boundary

**Not done in the isolated authoring session:** full native SUCC unittest discovery; frozen-source provenance verifier; observer and ordinal probes; hosted pull-request CI; any new Lean theorem. These are explicit integration gates, and nothing above asserts that a hosted job succeeded. The source rational function is quoted unchanged from the already authenticated four-pole expression and imported through `succ_internal_matrix_walk.authentic_r` for positive indices.

**Paper proof authority:** convergence of the analytic 2-adic logs on the closed unit disc of `Q_2(i)`, the vanishing logs of `−1,±i`, isometry of the four-pole rational source, exact extension `Φ(n)=U_n`, conjugacy to an adding machine, and the all-`k` finite-clock permutation. None of those infinite claims is Lean formalized here; local modular tests do not provide infinite authority.

**Remaining exact arithmetic obligation:** original selected real-circle Weyl cancellation `Σ_(n<=N)exp(2πihU_n)=o(N)` for each nonzero integer h. Finite Haar uniformity in the 2-adic source does not imply it. Do not promote the new boundary theorem or the Seinfeld ghost zero into a π normality assertion.

**Reproduction commands (run from the native repository root):**

```sh
python -m unittest tests.test_bbp_binwindow_conjugacy
python scripts/bbp_binwindow_conjugacy_probe.py --verify
python scripts/bbp_binwindow_conjugacy_probe.py --mutate-check
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```
