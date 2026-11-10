# Operation zero-origin spectral flux — conservation without artificial anticlumping

**Research-only; 2026-11-08; π base-16 normality OPEN.** Start from literal `U0=0`, the full authentic four-pole BBP recurrence and *certified*, not imported, hexadecimal digits. Observe what happens as the mathematical path grows: each new word contributes a **constant-length vector increment** but changes the aggregate discrepancy through **signed interference**. No digit value or run is disallowed. The experiment measures whether persistent temporal spectral lines emerge, rather than forbidding legitimate local clumps.

**Strongest exact results:** `THEOREMS.md` ZOS-02 constant-step/signed-arrival identity; ZOS-03 character-orthogonal refinement flux `E_(k+1)-E_k>=0`; ZOS-04 total temporal Parseval power; ZOS-06 exact original three-channel phase product; ZOS-07 original zero-seed signed lag-energy identity (inherited). These are **finite identities valid for many nonnormal countermodels**, not source-specific decay theorems.

**Observed:** the 16,384-digit original-zero BBP sample has `(E1,E2,E3)=(0.0006529093,0.0152759552,0.2445373535)` and largest non-DC Fourier power `0.000600298`. These lie within 16 same-histogram shuffled control ranges. Balanced 16-periodic and sorted clones are sharply distinguished; repeated order-3 de Bruijn is the crucial deep/temporal false-flat control. The tiny sample-count in some signed-work amplitude bins is disclosed. The toy spectral-feedback generator is *not the π process* and did not beat the shuffled overall spectrum.

## Reproduction on an SUCC checkout

```bash
python -m unittest discover -s tests -p 'test_zero_origin_spectral_flux.py' -v
python research/2026-11-08/zero_origin_spectral_flux/experiment.py --n 8192 --depth 3 --shuffles 16 --out /tmp/succ-zos-8192
python research/2026-11-08/zero_origin_spectral_flux/experiment.py --n 16384 --depth 3 --shuffles 16 --out /tmp/succ-zos-16384
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Run from repo root. The CLI uses **standard library only**, relies on existing `observational_succ.duck_bbp` and writes the complete structured finite receipt plus `progress.csv`. For each run it checks the first 128 digits independently with exact Machin-series rational enclosures. The original source orbit is exact Fraction arithmetic at all N; the expensive three-channel Fraction histories are independently verified only for n<=1024 in the large run.

Follow `PROTOCOL.md` for the frozen extension and its limits; `CLAIM_LEDGER.md` for authorities and refuters; `NEXT.md` for the next source-specific inequality. Mathematical proofs and exact scopes are in `THEOREMS.md`; actual measured results and validation in `VALIDATION.md`. This branch neither modifies historical source contracts nor changes another agent's research branch.
