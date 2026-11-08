# Fresh independently dated source-character holdout addendum — 2026-11-06

**Status: registered before evaluating the cases below.** The earlier `PREREGISTRATION.md` was committed before the official `holdout_probe.py` run, but the `(A,h)=(223,1),(223,2),(457,1),(457,2)` signed values had been *explored in an informal scratch calculation before that preregistration*. Thus those four must be reported as **pre-seen finite calibration** and NEVER represented as blind independent holdouts. The old preregistration remains frozen and byte-identical; this amendment makes the chronology explicit. The former values remain rigorously certified finite enclosures, but they are not fresh holdouts.

## New fixed untouched cases (not yet calculated)

- Authentic signed BBP original source `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, literal `U_0=0`.
- Unexamined new epochs: `A=239` and `A=503`, **one new frequency** `h=3` per epoch. Evaluate each genuine completed orbit on `[A,2A)`.
- Use **unaltered** `signed_certificate.py`, `source_completed_samples(A,depth=12)`, `certified_weyl(samples,3)`, and 12-decimal outward-rational bounds, with no revised phase width, Taylor degree or threshold if inconvenient. Certify signed character magnitude via the existing exact rational Taylor/Machin method; no floating-point proof.
- Positive control: exact uniform 16-root grid at `h=3` has rigorously bounded magnitude < 1e-6. Negative control: coherent constant completed `beta=1/5` repeated `239` states at `h=3` must have rigorous magnitude > 0.99.
- Accept exact certificate for whatever finite value occurs (including >1 bound); **do not** use finite differences or favorable values to infer any infinite decay, normality, or a new analytic signed saving.
- Record local exact test log, new JSON `FRESH_HOLDOUT_RAW.json`, and corresponding hashes in the receipt. Distinguish these two commit-first cases from the four pre-seen calibration cases forever.

The resulting conjecture status is **UNVERIFIED** until a source-specific infinite signed bound is independently derived. This addendum uses the same model/reasoner, so no external blinding or academic priority is claimed.
