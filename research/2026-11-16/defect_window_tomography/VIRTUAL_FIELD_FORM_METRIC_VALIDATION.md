# Virtual-Field Form Metric — exact implementation and high-precision source audit

**Date:** 2026-11-16. **Scope:** finite exact rational BBP source claims, the phase-norm comparison and the terminal-backward representation in [VIRTUAL_FIELD_FORM_METRIC.md](VIRTUAL_FIELD_FORM_METRIC.md). This document does **not** claim a proved all-late-shell bound, π normality, a physical norm, a thermodynamic temperature or a source-independent observation law.

## 1. Executed exact source test

The local exact standard-library file at /mnt/data/test_virtual_form_metric.py was executed as:

~~~sh
python -m unittest -v /mnt/data/test_virtual_form_metric.py
~~~

Result: **10 tests PASS, zero failures, zero errors**. The code is committed byte-for-byte as [tests/test_virtual_form_metric.py](../../../tests/test_virtual_form_metric.py); both its independently computed local Git blob hash and GitHub's fetched blob SHA are

~~~text
a8a3bc54d9ab4073ecb3339ea6078c0e1cac42ea
~~~

The code uses exact Python Fraction for **every source-side comparison**, not floating estimates of π. It checks: original four-pole zero-seeded U_m vs direct rational BBP partial sum; the reversal of the full B-shell from one endpoint U_2B; the inherited strict rational source-tail envelope; the exactly summed squared orbit-amplification coefficient (1−16^(−2B))/(255B); five strict finite rational source lower certificates; one-endpoint central-digit counts/inequality; periodic word+zero shadows sharing a prescribed prefix; delayed shell pseudometric aliasing; zero and rational nonunit fixed-point controls; and an actual changed-seed affine recurrence (not an empty self-comparison).

## 2. Fully rational finite certificates

Write R_B=(1/B)sum_{k=1}^B ||U_2B/16^k||_circle² and rho_B=8r(2B+1)/(225B). Both are exactly rational. The proven source inequality is

\[
1-\Re W_B(\pi/16)\ge8R_B-\rho_B.
\]

The table entries are **readable decimal renderings of exact Fractions**, and all strict >3/5 comparisons were evaluated in full exact arithmetic.

| B | R_B (rational) | 8R_B−rho_B (rational) | middle 4..11 digits among B trailing digits |
|---:|---:|---:|---:|
| 16 | 0.075084310973 | 0.600673990707 | 6 |
| 32 | 0.079825201617 | 0.638601550083 | 14 |
| 64 | 0.088161132374 | 0.705289051089 | 33 |
| 128 | 0.089051047282 | 0.712408377266 | 66 |
| 256 | 0.089039450341 | 0.712315602606 | 142 |

The finite records are **in-sample** relative to the much longer existing Main XXVI horizon. Do not claim they predict arbitrary future shells.

## 3. Independently implemented 800-digit completed π-phase audit

A separate Python/mpmath implementation at **800 decimal working digits** directly evaluated the completed x=π/16 circle phases and, independently, the rational shadow \(P_{2B}=U_{2B}/16^{2B}\), comparing both with the exact-rational source inequality and the dynamic phase-norm estimate.

| B | Completed A_B=1−Re W_B (numerical) | Rational shadow A_B(P_2B) (numerical) | \(\sqrt{B^{-1}\sum|z_n(x)-z_n(P_{2B})|^2}\) |
|---:|---:|---:|---:|
| 16 | 0.90099444766680814217 | 0.90099406315390110567 | 1.46113e-6 |
| 32 | 0.93797282253741399887 | 0.93797283570033586992 | 2.617621e-7 |
| 64 | 1.0554633216582933208 | 1.0554633186258441174 | 4.658687e-8 |
| 128 | 1.0220058404212315568 | 1.0220058400648545457 | 8.263492e-9 |
| 256 | 1.0692061935464905526 | 1.0692061935924068617 | 1.463284e-9 |

All five independently evaluated A_B fall inside the two-sided rational/π-bound sandwich and exceed the source-rational lower certificate. Every evaluated phase-norm difference was at or below the analytic bound using the actual tail \(T_{2B}\) (the sine Lipschitz estimate is nearly saturated because these phase discrepancies are tiny). These are **numerical diagnostics, not certified interval proofs**; the universal inequalities have separate elementary paper derivations.

## 4. Hostile controls and asymptotic boundary

- **Source-label alias:** x and y=x+1/16^B are different real-source initial states, but their phases agree at every sampled n>=B; d_B is a pseudometric, not a metric on authenticated source identities.
- **Finite periodic shadow:** repeating any finite prefix + 0 gives a purely periodic rational computational form; the period/horizon budget can grow with B. Approximate matching on finite windows is not evidence for asymptotic π normality.
- **Source terminal rational P_m:** its radix expansion is eventually periodic, but its period may be huge; it is an endpoint rational approximation and **not** the same original historical forcing/seed if promoted to a new autonomous infinite source.
- **Changed seed:** U_n(s)=U_n(0)+16^n s has the *same forcing* but another original state; source-only Gamma observations can be blind to this label. A coherent s=−x makes the complete circle locked while the original zero seed is the authenticated task.
- **Rational fixed nonunit phase:** x=1/15 is periodic, has R0, and can have zero relative speed. Avoid claiming nonperiodicity is necessary for R0.
- **Sparsely supported irrational:** the inherited x_star has infinitely many nonzero digits but late shells with R0-energy approaching zero. Being irrational and knowing a finite norm does not prove an eventual positive lower bound.
- **No universal norm:** the Hilbert probe seminorm is a norm only on the quotient by the toolkit kernel. Its weights, observation cost, real/complex phase basis and source maps are part of the declaration.

## 5. Claim ledger

- **PROVED PAPER (classical):** weighted probe semimetric, cylinder ultrametric, shell pseudometric kernel, periodic finite-prefix shadow construction, source terminal-backward identity, exact phase Lipschitz norm bound, rational torus-squared comparison, quantitative source tail correction, and R0 iff liminf R_B>0.
- **OBSERVED EXACT FINITE:** five source-rational lower bounds >3/5; five central-digit counts and ten focused tests; not independent arithmetic-source witnesses.
- **OBSERVED NUMERICAL:** five independent 800-digit completed-phase checks; not interval certified.
- **UNVERIFIED/OPEN:** an all-large-shell lower bound on the exact terminal rational energy for the literal zero-seeded original four-pole source. Also open: base-16 π normality and all nonzero-mode Weyl saving.

The exact next discriminating probe is to derive a source/cofactor/restricted-exponent mechanism that prevents \(U_{2B}/16^k\) from lying near integers for almost every \(k\in[1,B]\) along arbitrarily late shells. Freeze the relevant digit/cofactor/CRT budget and attack it with shifted seeds and rational periodic shadows **before** asserting any universal theorem. The known right answer for finite B is not a substitute for the missing asymptotic arithmetic estimate.
