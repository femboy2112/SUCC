# Circle Origin Gauge — source-relative claim supplement (research only)

**Current work:** draft PR #257, stacked on signed BBP Source Genesis #253.
**Parent source context:** corrected BBP #252, circle/Kummer #247–#249,
and independent Green Rank duality #254 (sibling, not imported).
The exact proof dossiers and source files are cited in
research/2026-10-24/CIRCLE_CYCLOTOMIC_ORIGIN_GAUGE.md.

| ID | Scoped theorem/counterexample | Status | Source/falsifier |
| --- | --- | --- | --- |
| OGC-01 | T_b reorigin conjugacy has source-correct affine cocycle H_d(a)=(b^d−1)a | CLASSICAL, PAPER-PROVED / EXACT FINITE TESTED | Wrong rotation-only commutation mutants |
| OGC-02 | Only b−1 circle translations commute with unchanged T_b; 15 hexadecimal frames have identical Fourier magnitude but phase averages can cancel falsely | CLASSICAL / EXACT TESTED | Unforced x=0 remains fixed and nonnormal |
| OGC-03 | Arbitrarily small source differences can reach maximal circle separation under an expanding covering | CLASSICAL / EXACT TESTED | delta=1/(2b^n) yields half-turn at n |
| OGC-04 | Origin-averaged squared difference of two normalized orbit characters is ≤4/N exactly with its underlying chord-moment identity | CLASSICAL FOURIER / PAPER-PROVED | At a selected frame 0 versus 1/3 has squared difference 3 for all N, b=16 |
| OGC-05 | Finite grid origin history tomography requires distinct h b^j mod m; multiplicative-order criterion suffices | CLASSICAL / EXACT FINITE TESTED | m=15 collisions, m=7 period3 nonalias |
| OGC-06 | Fix(T_b^d) has b^d−1 points; cyclotomic factors and minimal-period dynamical counts are DISTINCT, related by Möbius inversion | CLASSICAL / EXACT TESTED | Phi_2(16)=17 but exact-period-two points=240 |
| OGC-07 | Full fixed-point origin grid tends to Haar while one selected orbit with exact period d tends to delta0 at exact W1 rate | CLASSICAL / PAPER-PROVED / EXACT TESTED | x_d=1/(b^d−1), full-period selected trajectory |
| OGC-08 | Independent source-certified π polygon intervals select arbitrarily deep period-d rational shadows with full phase-budget accounting | EXACT FINITE TESTED / NO PI LIMIT | Future errors expand; fake remains periodic |
| OGC-09 | The authentic BBP rational forcing is precisely the unique bounded moving-origin source connection, with finite rational residual and signed lag boundary enclosure | PAPER-PROVED / EXACT FINITE TESTED; inherited BBP source | Wrong initial y0 or shift indexing rejected |
| OGC-10 | π-selected signed cyclotomic-lag cancellation and base16 normality | **OPEN / UNVERIFIED** | All periodic shadow controls and source-matched impostors remain |
| OGC-11 | Exact Haar-origin fourth moment (2N²−N)/N⁴; Markov+Borel–Cantelli gives almost-every-origin normality; grid fourth-moment resource ≥N(N+1)/2 | CLASSICAL / PAPER-PROVED / EXACT FINITE TESTED | Selected origin a=0 may be exceptional |
| OGC-12 | Full inverse T_b preimage tree has exact Fourier cutoff and W1-to-Haar 1/(4b^k), while source pushforward by T_b^k remains delta_x | CLASSICAL / PAPER-PROVED / EXACT FINITE TESTED | Selected inverse branch is not a Haar ensemble |

No new Lean declarations in this branch. Finite rational tests and dedicated CI do
not certify the all-horizon analytical proofs or academic novelty. The
one-point compactification and R/Z are homeomorphic circles but have
different declared group/coordinate structures; there is no physical
inertial-frame covariance claim.

**Important frontier:** a source-justified quantitative lift from
circle-origin ensemble bounds to the actual BBP-selected point π.
The exact fourth-moment/Haar normality result is about almost every point,
not π. Such a source-lift must give a non-circular signed
all-horizon estimate on authentic cyclotomic lags, with full
periodic-counterfeit and rational-approximation controls.
