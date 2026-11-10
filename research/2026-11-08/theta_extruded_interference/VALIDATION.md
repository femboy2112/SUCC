# Validation receipt — theta dual extruded interference, 2026-11-08

**Target:** standalone addition to SUCC, branch `research/theta-gamma-extruded-triangle-dual-interference-2026-11-08` from `main@43a607818907120d4cdab73d240f5b4d7700b63f`. The branch and draft PR must remain research-only. The exact GitHub commit SHA and CI outcome are separate checks after upload.

## Commands actually run (local container)

```sh
cd /mnt/data/succ_theta_triangle_round
python -m compileall -q observational_succ/theta_extruded_interference.py tests/test_theta_extruded_interference.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
```

**Result:** 26/26 focused tests PASSED, Python 3.13.5, mpmath 1.3.0, SymPy 1.14.0 installed (not a runtime requirement). Elapsed approximately 4.6 seconds. See accompanying `LOCAL_TEST_LOG.txt` captured from this command.

## What tests actually calibrate

- Exact Fraction Laguerre/Pascal coefficients, forward difference/inverse, and signed formal-Li recurrence; independent rational symbolic identities for λ1..4.
- Numerical original Jacobi-theta and upper-incomplete-Gamma representations against an independent completed `Gamma(s/2)*zeta(s)` evaluation at nonzero real/complex probes, without using nontrivial ζ zeros as a constructor.
- `lambda_1` exact Euler–Mascheroni formula; `lambda_2` calibrated against the independent Stieltjes/Gamma expression; source-only elementary moment envelope tests.
- Exact finite controls of a non-RH positive atom with reflection and endpoint normalization, wrong-Gamma completion, and composite-six mutation of the all-integer Gaussian source.
- The unmodified theta channel orientation reversal at `Im u=1/2`; the positive completed Fourier kernel; a finite-source two-time kernel identity and log-clock derivative current on selected upper-half-plane points.
- Independent SciPy integration and 55-digit mpmath on the half-Fourier sign failure at `u=17+0.25i`. This sign is a *finite observed probe*, not a rigorously enclosed interval inequality.
- Formulas for omitted theta integer modes and t-tail are analytically proven absolute upper bounds in `PROOFS.md` and implemented. These **do not make numerical quadrature itself certified**.

## Source / size / SHA256 (local exact bytes)

```text
5f3064d87982c988b12f90c2bd3da8baa1e20fde47f3e72fe019995c9ab10264  observational_succ/theta_extruded_interference.py
9b994b8f5564682f958868acc28ad76277b677f35cd79268255d225cc4b3d977  tests/test_theta_extruded_interference.py
9a00495cd15384983e7680b9ec1cc9c99b53d60bfec23344ffc88e3564108c08  research/2026-11-08/theta_extruded_interference/CLAIM_LEDGER.md
1c339dd638e8f97c752e2b638d2fb113169bed62539a56e2a9a062a67889d0ca  research/2026-11-08/theta_extruded_interference/NEXT.md
d87bb1d7109c62e7dff8480794d5e2fe35fd5d0a9a6662360ecb6ffe46fa5a52  research/2026-11-08/theta_extruded_interference/PROOFS.md
b27ef765fb99a2e8f7fb775e7b18c9d17da7cf4e647f4828bf9865efcc4b4989  research/2026-11-08/theta_extruded_interference/README.md
75905780a7094cde805f65ed216ddbc438104444eab0ba052926df1f6a3e9e5b  handoffs/rh/2026-11-08-theta-extruded-li-interference.md
```

## NOT run / NOT claimed

Full main SUCC 12k+ tests, `scripts/verify_provenance.py`, foundations/ordinal probes, Lean kernel formalization, new GitHub branch hosted CI and external scholarly referee audit. The standalone environment did not have a checkout of all 36 MB SUCC data; public Git network resolution is unavailable. Original frozen sources and root framework files are unchanged. Local finite numerical observations are not interval certificates. **RH PROVED: NO.** π normality: OPEN.
