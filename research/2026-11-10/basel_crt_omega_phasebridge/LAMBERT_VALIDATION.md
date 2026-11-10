# Lambert-W signed Basel gate — local validation record

**Scope:** isolated additive continuation of draft #585 on 2026-11-10, in an environment with Python 3.13, mpmath 1.3.0 and the standard library. The prior Main XXIII candidate #584 remains separately under review. No repository-wide native tests, hosted CI, Lean or external referee was run for this change.

Command:

```sh
python -W error -m unittest discover -s research/2026-11-10/basel_crt_omega_phasebridge -p 'test_lambert_basel_gate.py' -v
```

Actual observed result: **12 tests, 0 failures, 0 errors, 0.039s** (local system). Key controls: exact four-pole rational prefix, BBP tail bound at five horizons, principal W inversion, real negative W branch, proof-level rational threshold / minimality, three-log asymptotic calibration, actual finite original-seed phase difference below the analytical rational budget, exact integer winding, coherent and periodic wrong seed, irrational sparse digits and universal bounded tail. mpmath phase calculations are *noncertifying cross-checks*; the pass/fail certificate core uses exact rational comparisons.

Local SHA-256 of finalized new files:

```text
LAMBERT_W_SIGNED_BASEL_GATE.md 39d5f9ce9a917dcc7941525285a4d8501bcb28ae8683955064165fe3c2cb015c
test_lambert_basel_gate.py cd0c1e7ee13fc737b3faa9da52691a3eaa0c646d8032e983090dd2df0dd0c776
```

Example rational threshold results:

```text
A=11, R=3, M=33, h=8, L=30, phase bound 0.03869204 < 1/3
A=32, R=4, M=128, h=8, L=123, phase bound 0.113572 < 1/4
A=64, R=5, M=320, h=8, L=314, phase bound 0.08916941 < 1/5
A=100, R=6, M=600, h=1, L=593, phase bound 0.02221919 < 1/6
A=200, R=7, M=1400, h=1, L=1392, phase bound 0.02369737 < 1/7
```

The displayed decimal bounds are *rounded presentations of exact Fraction computations*. No asymptotic sign estimate or theorem about π's normality is inferred from the sample points. Tests share model/researcher provenance, not independent blind review.
