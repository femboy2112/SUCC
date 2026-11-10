# Validation receipt, scope, and exact replay

**Environment:** Python 3.13.5; standard-library only in the four new probes. No external π oracle. No full SUCC checkout validation, Lean theorem kernel-check, hosted PR CI or independent external reviewer is claimed here.

**Code files and commands (from the repository root, with the scripts in this folder):**

```sh
python research/2026-11-10/gaussian_circle_long_lag/gaussian_circle_probe.py
python research/2026-11-10/gaussian_circle_long_lag/viete_three_way_probe.py
python research/2026-11-10/gaussian_circle_long_lag/source_pair_probe.py
python research/2026-11-10/gaussian_circle_long_lag/long_lag_holdout.py
```

**Actual local executions (exit 0 each):**

- Full lattice disk/angle/BBP script: 50 exact tests including rational angular mode h=4,8, Gauss count, BBP independent enclosure and rational source-shadow calculations; six independent primitive disk/octant Mobius controls; eight independent Jacobi `χ₋₄` divisor-vs-disk controls.
- Viète: 10 stages of exact rational radical intervals for the inscribed/circumscribed polygon, each overlapping Gauss disk rational area enclosure and authentic four-pole BBP rational interval.
- Source pair: 96 exact rational checks including pair-vs-lag energy and 48 two-index source/Green-completed squares; coherent period-two nonnormal controls.
- Fixed rounded-grid holdouts: `A=257,509`, `q=8` with exact original-zero and `s_A=-P_(2A+12)` recurrence. Every input state is an exact Fraction. The floor grid denominator is `D=10^22`; every pair's threshold classification has a safety margin `>2q` integer grid units, hence its inclusion/exclusion is **exact**. The triangular energy differs from the exact fractional energy by **strictly less than `2q²/D=128/10^22=1/78,125,000,000,000,000,000`**. The displayed decimal J values are rounded. The completed π transport costs at most `8q²/[15(A+1)²]` separately.

| A | q | source type | rounded `J^U` | exact counted short pairs | medium pairs | long pairs | long-lag weighted contribution |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 257 | 8 | original zero | 1.027737438 | 235 | 764 | 7198 | 0.873599163 |
| 257 | 8 | same-forcing rational shadow | 7.999996555 | 1018 | 2958 | 28920 | 7.005704483 |
| 509 | 8 | original zero | 1.009999096 | 492 | 2194 | 29573 | 0.911828682 |
| 509 | 8 | same-forcing rational shadow | 7.999999122 | 2026 | 8919 | 118341 | 7.308354429 |

The short lag cutoff is `floor(log2 A/2)=4`; the medium cutoff is `floor(sqrt A)`, which is 16 and 22. Epochs and schedules were selected in this local session after exploratory A=16,32,64,128. They were not independently blinded and were not remotely preregistered; do **not** classify them as fresh external holdouts or evidence of all-A uniformity.

**Proven inequalities versus tests:** The all-R GC-01 sector theorem, GC-02 Fourier estimate, GC-03 primitive asymptotic, GC-05 scalar-phase transfer, GC-06 conditional pullback, source-shadow all-A energy inequality and source two-index cocycle are analytic/paper derivations. Finite tests are only consistency checks, not universal proof certificates.

**Negative controls:** (1) sparse axis-only points on a Gaussian disk concentrate exactly at angle 0 and have `J=q`, despite full disk's `J≤16`; (2) for each finite Gauss-area rational approximant `π_(16^M)` the full hexadecimal orbit eventually becomes zero; (3) the same-source rational shadow yields energy ~q, so source forcing alone does not guarantee bounded energy; (4) finite polygon or finite source prefixes cannot certify all-epoch normality.

**Next code validation:** independently rederive the convex-sector counting proof, control prime/CRT-inherited source numerators, and preregister much larger source epochs on a separate repository branch before viewing data. Do not merge into current Main XXIII candidate while its own gates are in flight.