# VALIDATION - Front B carry-transport probe (Daniel Bernoulli)

All paths relative to this directory (`research/2026-11-05/main_xx_forge/front_b/numerics/`; the run was made in a scratch copy, then relocated).
Python: scratchpad venv (3.12.3, mpmath 1.3.0 pure-python backend, numpy 2.5.4, sympy 1.14.0). Never `python -I`. No git. Every mpmath use is inside `mp.workdps(...)`.
Status labels: **Observed** = one deterministic run of the stated command; **Cross-checked** = reproduced by an independent second route in the same run. Nothing here is Demonstrated.

## Exact commands (cwd = front_b/, PY = venv/bin/python)
```
$PY carry_transport_probe.py --stage calibrate     # 15 s
$PY carry_transport_probe.py --stage cb1 --procs 7 # 443 s wall (A=4096 Fraction oracle dominates: ~400 s)
$PY carry_transport_probe.py --stage edge          # 159 s
$PY carry_transport_probe.py --stage cb1g          # 55 s
$PY carry_transport_probe.py --stage trueseed --procs 3   # 26 s
$PY carry_transport_probe.py --stage third         # 10 s  (reads the reference checkout; our oracles never import it)
$PY carry_transport_probe.py --stage cb3 --procs 6 # 63 s wall, A up to 2^17
$PY carry_transport_probe.py --stage j2 --procs 6  # 73 s wall
$PY carry_transport_probe.py --stage receipt       # merges data/*.json + summary + sha256 of scripts -> FINITE_RECEIPT.json
$PY test_carry_transport.py                        # 13 tests, 2.1 s, OK
```
(`--stage all` runs every stage in order. `--quick` shrinks the epochs.) CB-3 compute (cb3 + j2) = 136 s total, within the 15-minute bound; largest A reached = 131072 = 2^17.

## 1. Calibration record (instrument first, evidence second)
Observed, data/calibrate.json:
- r(1) = 47/15 exactly (Fraction) and 188/60 via the big-integer path.
- r(n) > 0 for all n <= 100000 (integer sign test; plus the analytic argument 4/(8n-7) > 4/(8n-4) and 1/(8n-3), 1/(8n-2) < 1/(8n-4)).
- Series: sum_{n<200} 16^-n r(n) - pi/16 = -9.4261e-247 (mp, 260 dps).
- Gauge identity U_n + T_n = 16^(n-1) pi: residual inside the rigorous bracket at n = 1,2,5,10,20,50,100,500,1000,2000,4096,8192 (residual <= 1.4e-121 vs bracket width 3.9e-121..7.7e-121; `within_bracket` True in all 12). T_n is computed from rationals only (fixed point 2^400, outward rounding, start bracket [0,1/10] at N0=nmax+120). pi is used only as the external reference.
- 64 n^2 T_n: 0.5286 (n=1), 0.9865 (64), 0.99913 (1000), 0.9999967 (2^18); n*(64n^2 T_n - 1) -> -0.875 = -7/8 (so T_n = (1-7/(8n)+...)/(64 n^2)). Largest-n value is the rigorous lower bracket.
- 16 T_n - T_(n+1) = r(n+1): bracket-consistent for all 262144 n; max bracket width 34 units of 2^-400 (2^-394.9).
- pi hex digits: own integer Chudnovsky vs mpmath, 262544 digits requested, first 262542 compared, all agree; known prefix 243f6a8885a308d313198a2e03707344 OK; third route BBP digit extraction (float) agrees at positions 1, 10, 100, 1000, 3990, 5000, 19990, 100000, 262000 (6 hex digits each).
- Hand case (plain loops, no oracle classes) A=64: (m,k)=(2,2): sum b = 8, J = +2.829987504499269e-4; (1,3): 8, J = -1.553461819714475e-4; (3,1): 7, J = -8.165110005489983e-3. Oracle A and oracle B reproduce all three exactly (also asserted in test_carry_transport.py).
- Detector control: forcing NEGATED (M4) gives 50524 mismatches at A=1024 in both oracles - the comparison can fail.
- Third cross-check (data/third.json): observational_succ/selected_orbit.py (`carry_by_definition`, `carry_by_window`, `critical_depths`) imported read-only (no bytecode). For A = 64, 173, 347, 691 and seeds 0 and 1/5: exact Fraction J agrees with our oracle B for BOTH of its methods on all 82 (cell, triple) comparisons (0 disagreements), and its `critical_depths` maximum equals our dmax in all 8 cells. Our oracles were written before and without it.
- CB-3 instrument self-check: uniform-law joint-CDF algebra vs closed-form Haar counting, max diff 6.9e-17; joint-CDF algebra vs Monte Carlo (2e6 samples, strongly non-uniform law, effect size up to 0.0247): max |z| = 1.62.

## 2. CB-1 (rational form) - data/cb1.json, cb1_summary.json
Oracle A = Fractions, repo definitions; oracle B = pure big-integer common-denominator arithmetic. Every n in [A,2A), every (m,k), m,k>=1, d up to dcap = floor(log16(64A^2)) + 2.
- Source, seeds {0, 1/5, 1/3, 3/7, 5/17}, epochs {64,173,347,691,1024,4096}: oracle B ran on 30 cells, oracle A on 27 cells (seeds 1/3, 3/7, 5/17 at A=4096 were B only). Cases with S_d(n) < 1: **591,175 (n,m,k,seed) cases; mismatches in claimed b or claimed delta: 0 in oracle B, 0 in oracle A; cross-oracle disagreements (sum b, sum delta as exact Fraction, bit-digest of b by definition, bit-digest of b by claim, admissibility count, minimum margin): 0.**
- dmax (largest fully admissible depth): A=64:4, 173:5, 347:5, 691:6, 1024:6, 4096:7. One partially admissible depth: A=347, d=6 (S_6(n)<1 for part of the window); the identity held on the admissible n there too (included in 591,175).
- Smallest 1 - S_d among the preregistered fully admissible triples: 0.4517 (A=691, (1,5), n=691). So the preregistered epochs do not probe the edge; see Section 2b.
- Boundary control (first inadmissible depth d=dmax+1, S_d >= 1 everywhere in the window), seed 0: A=64: 256 cases, 130 b-mismatches, 252 delta-mismatches; A=173: 865, 385, 865; A=347: 825, 448, 808; A=691: 4146, 1860, 4146; A=1024: 6144, 3441, 6075; A=4096: 28672, 15967, 28395. The identity FAILS there (roughly half the b bits differ), as expected outside the hypothesis; it is therefore not a vacuous identity.

### 2b. Edge: S_d just below 1 (data/edge.json, oracle B and, for A<=2048, oracle A)
Smallest admissible epoch per depth is exactly A = 4^d/8 (64A^2 = 16^d): d=3: A=8, 4: 32, 5: 128, 6: 512, 7: 2048, 8: 8192 (A-1 inadmissible in each). Tightest 1 - S_d: 0.0979, 0.02655, 0.006785, 0.001706, 4.270e-4, 1.068e-4 (d=3..8). Cases 16, 96, 512, 2560, 12288, 57344; mismatches 0 (oracle B all; oracle A d<=7 all, cross-oracle OK). One level deeper (d+1, inadmissible) b-mismatches: 4/24, 45/128, 320/640, 1427/3072, 6916/14336, 31625/65536.

### 2c. Mutants (A in {64,173,347,691,1024}, seed 0, both oracles agree in every cell)
| forcing | admissible-case mismatches (A=1024) | note |
|---|---|---|
| M1: 4->5 on first pole | 0 (cases 6144, dmax 4) | positive forcing: CB-1 holds |
| M2: constant r = 1/1000 | 0 (3072, dmax 3) | positive forcing |
| M3: unforced r = 0 | 0 (10240; interval empty, b = 0) | degenerate |
| M4: r -> -r | 50524 (b: 21852, delta: 28672) | every mismatch has S_m<0 and S_d<0 and S_m>S_d |
| M5: (-1)^n r(n) | 25108 (b: 10743, delta: 14365) | mismatches classified by S_m<0 / S_d<0 / S_m>S_d (counts in data) |
Same pattern at all five epochs (see cb1_summary.json). M4/M5 "dmax" is the cap dcap, not a true bound.

## 3. CB-1g (gauge form) - data/cb1g.json
Seed 0, alpha = pi/16, thresholds from the rigorous T_n bracket, z_(n+d) two ways: (i) pi hex digits (100 hex digits = 400 bits), (ii) x_(n+d) + T_(n+d) mod 1 from the oracle-B exact x. Epochs and admissible cases: 64: 384, 173: 1730, 347: 4380, 691: 10365, 1024: 15360, 4096: 86016 = **118,235 cases; membership mismatches vs exact b: 0 (route i), 0 (route ii); ambiguous (bracket-straddling) cases 0; delta containment violations 0; max |z(i) - z(ii)| = 1 unit of 2^-400.** Minimum endpoint margin over all cases: 1.07e-5 (A=347); per epoch 4.0e-3, 3.6e-4, 1.07e-5, 4.2e-4, 1.67e-5, 3.85e-5. Wrap exposure (S_d<1 but 16^d T_n >= 1): **0 cases**. Inadmissible depths: both routes reproduce the same (wrong) b as the rational form (e.g. A=4096 d=8: 15967 mismatches in each route). Instrument-vs-instrument: the vectorised float gauge `b_vector` reproduces the oracle-B repo-definition bit-digest for every admissible triple at every epoch (6+10+10+15+15+21 = 77/77); gauge dmax equals oracle dmax at all six epochs.

## 4. Exact J values - data/trueseed.json
(m,k) listed as in HS-08 (k=1,2). J printed as computed (exact Fraction -> float; sign exact).
| s | A | (m,k) | sum b | avg delta | J |
|---|---|---|---|---|---|
| 0 | 173 | (4,1) | 38 | 0.256894046428 | -3.72408672369403740e-02 |
| 0 | 173 | (3,2) | 42 | 0.272811559611 | -3.00369931373419413e-02 |
| 0 | 347 | (4,1) | 21 | 0.063818181446 | -3.29944945710047106e-03 |
| 0 | 347 | (3,2) | 21 | 0.067789628337 | -7.27089634869130565e-03 |
| 0 | 691 | (5,1) | 179 | 0.257422672659 | +1.62218985873500716e-03 |
| 0 | 691 | (4,2) | 194 | 0.273476717872 | +7.27581468932677299e-03 |
| 0 | 4096 | (6,1) | 471 | 0.117193042710 | -2.20280833484286535e-03 |
| 0 | 4096 | (5,2) | 506 | 0.124514926237 | -9.79769986711569131e-04 |
| 1/5 | 173 | (4,1) | 42 | same | -1.41194799537033774e-02 |
| 1/5 | 173 | (3,2) | 44 | same | -1.84762994957234430e-02 |
| 1/5 | 347 | (4,1) | 17 | same | -1.48268269787143036e-02 |
| 1/5 | 347 | (3,2) | 18 | same | -1.59164294899016810e-02 |
| 1/5 | 691 | (5,1) | 181 | same | +4.51654586452371939e-03 |
| 1/5 | 691 | (4,2) | 189 | same | +3.99246748549932778e-05 |
| 1/5 | 4096 | (6,1) | 522 | same | +1.02483635401571342e-02 |
| 1/5 | 4096 | (5,2) | 556 | same | +1.12272612632884315e-02 |
Full tables (all admissible triples, all six epochs, both seeds) in data/trueseed.json. J(1/5) != J(0) in general (as anticipated). The sign of J(0) changes with A (negative at 173, 347, 1024(1,1..3), positive at 691): the sequence of J(0) over this epoch list is not monotone.
Coherent seed s* = -pi/16: gauge route (rigorous T) b = 0 in all 77 admissible (A,m,k) triples, J = -avg delta (e.g. A=64 (1,1): -4.59141054708945260e-4; A=173 (4,1): -0.256894...; A=691 (5,1): -0.2574227). Repo-definition route (mp, dps = 1.21*nlast+150, A in {64,173,347,691}): b = 0 in all 41 admissible triples there, J agrees with the gauge value to float precision (max diff 0.0 at float64); in INADMISSIBLE triples the coherent b is NOT zero (A=64: (4,1) 9/64, (5,1) 26/64; A=173: (5,1) 43/173, (6,1) 82/173), i.e. "b==0" is an admissible-regime statement.
Also noted: for (m,k)=(1,1) J(0) equals J(coherent) at A=64, 173, 691 (b = 0 in both).

## 5. CB-3 - data/cb3.json (and summary.json)
Construction as specified: tau_j = 16^floor(log16 64j^2)/(64 j^2); p = uniform off tau in (0.3,0.7); inside u + 0.02*phi(tau)*w_perp + c*g (phi = exp(1-1/(1-x^2)), x=(tau-1/2)/(1/5); w = e1-e2 with the gradient component projected out in {dp_0=0, sum dp=0}; c by Newton so F_p(tau)=tau).
- Grid (mp 80 dps, 1001 nodes tau = i/2000, i=500..1500): max |F_p(tau) - tau| = 9.02e-60 (L=70 hex digits, independent of the L=50 used to solve); p_0 = 1/16 exactly (error 0.0); sum error 4.2e-81; min p = 0.04236; max |p_a - 1/16| = 0.02014; non-uniform at 783/1001 nodes; max adjacent-step L-inf 1.12e-4 per h=5e-4 (0.224 per unit tau): continuous.
- Production laws (float64 vectorised Newton) for j <= 262544: 110189 positions in the bump (42.0%); max |F-tau| = 5.6e-16; p_0 == 1/16 exactly; float vs mp on 30 random actual tau_j: max |dp| = 2.8e-17, mp residual <= 1.9e-60.
- Digits: numpy default_rng(seed).random inverse-CDF; preregistered seeds 20261105, 1, 2; supplementary 3..12 (13 CB-3 sequences); null: iid uniform digits seeds 101..112; comparator: true pi digits (gauge form, relies on CB-1g verified only for A<=4096).
- Epochs: A = 2^10..2^17 AND (supplementary) round(2^(e+1/2)), e=10..16 (15 epochs). Admissible triples: 15 (dmax 6), 21 (7), 28 (8), 36 (9), 45 (10 at A=131072). All b by the float gauge test with exact 100-digit fallback: exact fallbacks 0, unresolved 0, minimum endpoint margin 3.6e-9 (A=131072) >> 1e-13 float threshold, so every comparison is certain.
- J (mean over 13 CB-3 seeds of max over admissible triples of |J|): 1.21e-2 (A=1024) ... 1.30e-3 (A=131072); iid-uniform null (12 seeds): 1.31e-2 ... 9.7e-4; pi: 1.08e-2 ... 1.46e-3. Preregistered seeds at A=131072: 2.46e-3, 4.29e-3, 3.28e-4.
- Log-log slopes (15 epochs): CB-3 mean-over-13-seeds max|J|: **-0.504**; rms over triples: -0.549; pow2-only: -0.463 / -0.510; half-only: -0.566 / -0.609. Preregistered single seeds: 20261105: -0.305, 1: -0.297, 2: -0.620. iid null: max|J| -0.421, rms -0.472. pi (one sequence): -0.483. (Single-sequence slopes are noisy; the 13-seed pooled fit is the stable one.)
- EXACT expectation of J under the CB-3 measure (digit-product measure, no sampling): max over triples of |E J| is 2.7e-7 over all 15 epochs (e.g. 3.2e-8 at A=1448, 2.7e-7 at 2896, 1.6e-9 at 131072) and ~1e-22 (zero to float) for windows whose tau-range avoids the bump (A = 1024, 4096, 16384, 65536 - there CB-3 is exactly Haar iid). Per-n bias is up to 9e-4 but positive and negative parts cancel to ~1e-8 (cancellation is the calibration F(tau)=tau telescoping). A log-log slope of this bias is NOT meaningful (window-phase dependent, spans 22 orders); the fitted values in cb3.json (+0.59) should be ignored.
- Witnesses (prefix [1,N), N=2A): exact expectation f(1)-f(2) is between 0.00393 and 0.01109 for every N in [1024, 262144] (600 log-spaced N), and max_a |E f(a) - 1/16| between 0.00197 and 0.00555 - never near 0. Empirical, 13 CB-3 sequences mean vs 12 uniform sequences mean: A=131072 (N=262144): f1-f2 = 0.0098 (sd 0.0007) vs 0.0002 (sd 0.0005); max_a|f-1/16|: 0.0052 vs 0.0010; pi: f1-f2 = 0.0001, max dev 0.0016. At A=1024 a single sequence is inside noise (sd ~0.007). Adjacent-equal-pair witness: expected sum_a f(aa)-1/16 = 0.77e-4..1.83e-4 but sampling sd 5e-4 (N=262144) so it is NOT detectable empirically (empirical mean over 13 sequences within noise); f1-f2 and max-dev are the usable witnesses.
Expectation from the brief ("J ~ A^-1/2 while the witness stays bounded away from 0"): the slope matches the iid-null slope; the same sd decay holds for uniform digits, so the decay is a property of the statistic's sampling noise and not of CB-3.

## 6. J2 - data/j2.json, data/summary.json
Triples per A: k_large (1,dmax-1), k=1 (dmax-1,1), balanced; l = 1,2,3; Leb(I_n cap T^-l I_(n+l)) by the exact counting function; E[b_n b_(n+l)] by joint CDF inclusion-exclusion (validated vs Monte Carlo above).
- Exact expectation under CB-3 (E J2): max over all 45 (A,rep) rows: l=1: 1.509e-5; l=2: 9.40e-7; l=3: 1.99e-7. Under the uniform control with the same code: <= 1.1e-18, 1.9e-18, 1.2e-18. For comparison max |E J| = 2.7e-7.
- Scale invariance: balanced triple, l=1, A = 2048, 8192, 32768, 131072: E J2 = 1.4396e-5, 1.4349e-5, 1.4384e-5, 1.4390e-5 (not decaying); l=2: 9.40e-7, 8.67e-7, 8.98e-7, 9.03e-7; same tau-window (A -> 4A) at A = 2896, 11585, 46341: 5.32e-6, 5.58e-6, 5.66e-6. E J at the same A: -2.2e-8, -3.7e-8, -5.9e-9, -1.6e-9 (first-order bias small and not constant).
- Sampling noise (12 iid-uniform sequences): sd of J2 (l=1, balanced) 8.7e-3 (A=2048), 3.7e-3 (32768), 1.3e-3 (131072); decay slope of null sd -0.43 (J2) and -0.45 (J). Ratio E J2 / null sd: max 0.011 (l=1), 6.1e-4 (l=2), 4.3e-5 (l=3); for first order max |E J|/sd = 5.4e-5. CB-3 empirical J2 mean over 13 sequences (l=1, balanced): +2.3e-3 +- 7.1e-3 (A=2048) ... -2.7e-4 +- 1.8e-3 (A=131072): consistent with 0 and with 1.4e-5. pi J2 values lie inside the null spread (0 of 135 (A,rep,l) entries beyond 3 null sd); the 13-sequence CB-3 mean J2 is within 3 standard errors of the exact expectation in all 135 entries.
- Reading of the data (observation, not theorem): at the exact-expectation level a second-order selected statistic distinguishes CB-3 from Haar (1.4e-5 constant along A -> 4A vs 0 for Haar, versus first-order 1e-9..1e-7 ~ 0). At A <= 2^17 a single sequence cannot resolve it (z <= 0.011). Heuristic extrapolation of the null sd (sd ~ 0.47/sqrt(A) at A=2^17): resolution of 1.44e-5 would need A of order 10^9 - beyond this instrument. This is arithmetic on the measured sd, labelled extrapolation.

## 7. What was NOT tested / boundary
- CB-1 / CB-1g were verified exactly only for A <= 4096 (six epochs) and rational/pi seeds; no claim for larger A beyond the gauge-form J sweeps, which assume CB-1g.
- Irrational seeds other than s*=-pi/16 and s=0 were not run through the repo-definition route.
- The Fraction oracle A was not run for seeds 1/3, 3/7, 5/17 at A=4096 (oracle B only); mutants only up to A=1024.
- CB-3 is a finite sweep (A <= 2^17, sd-limited). No proof that J -> 0 along all A, no statement about pi normality. The CB-3 sequence is a random model: results are about the product measure (exact expectations) and 13 sampled sequences. numpy RNG streams are numpy-version dependent (2.5.4 recorded).
- Admissibility S_d(n) < 1 is as in the brief. The reference module `selected_orbit.admissible` uses the different (stronger-looking) test 16^d T_n <= 1; they gave identical critical depths in all 8 compared cells, and no S_d<1 <= 16^d T_n wrap case occurred anywhere in 118,235 gauge cases, but the two conditions are not the same condition.
- J2 was computed for three representative triples per A, l <= 3, not for all triples.
- Float64 is used for sums in the CB-3 sweeps (thresholds exact to ~1e-16 relative; sums of delta are exact big-integer prefix sums); decisions on b are certified by margins >= 3.6e-9 vs float error ~1e-16.
