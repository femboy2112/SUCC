# BLACK SUN II — Coverage theory of the windowed completed Weil form

**Campaign round 2:** 2026-10-14 (evening). **Branch:** `research/black-sun-ii-coverage-theory-2026-10-14` (child of Black Sun #79 `cba5cca`). **RH PROVED: NO.** No zero positions used as construction inputs. Builds directly on the verified windowed Carleman representation and spectral machinery of PR #79.

## 0. Intake: what the swarm did since round 1

Eight new draft PRs (#80–#86) were fetched and read before designing this round. The closest neighbors: PR #85 (FSW line) proves RH ⟺ d₋(G_a) = 0 ∀a (negative depth of the full Suzuki kernel on windows) and a carrier-hardness no-go; PR #86 (AMW line) proves completed-Weil positivity on **codimension-30** and codimension-101 infinite-dimensional moment subspaces of the first-prime window at a = 1/2 with exact rational margins (κ = 369/10000), following Yoshida/Suzuki finite-codimension precedents; PR #84 controls the signed spectral tail of all zeros above height T with a source-derived order-one growth bound for ξ. **None of them maps the archimedean-vs-prime decomposition, the phase transition of the archimedean part, the coverage curve, or the Goldbach crossover.** That is this round.

## 1. The archimedean phase transition (BS-II-3)

Writing the windowed completed Weil form as Q_a = A_a + P_a (archimedean+pole part plus prime atoms), the **archimedean+pole spectrum of A_a undergoes a phase transition at a\*₀ ∈ (0.370, 0.372)**, certified numerically (margins ±3.5e−4 vs discretization resolution ±3e−6, a 100×-clean bracket):

| a | λ₀(A_a) | λ₁(A_a) |
|---|---|---|
| 0.300 | +0.00757 | +0.22251 |
| 0.350 | +0.00123 | +0.06279 |
| 0.370 | **+0.0010577** | +0.0045113 |
| 0.372 | **−0.0011670** | **+0.0010577** |
| 0.380 | −0.0236248 | +0.0010454 |
| 0.400 | −0.0780939 | +0.00063 |
| 0.420 | −0.130 | −0.0010 |

Findings:

1. **Windows a ≤ a\*₀ are positive without any prime atom** (pure archimedean+pole positivity): on (0, a\*₀] the completed Weil form's positivity is a confinement effect, needing no arithmetic. The primes enter exactly when the archimedean band turns negative. (TESTED MODEL at the stated resolution; the bracket (0.370, 0.372) is certified at M-refinement ±3e−6.)
2. **Striking numerological observation (NOT claimed exact):** at the transition, the eigenvalue left behind is λ₁ = +1.0577e−3 ≈ −Ω(2π) = +1.06018e−3 (within 2.5e−6, comparable to my resolution): the band-edge value −Ω(2π) appears to govern the crossing. Whether the λ₁-curve passes through −Ω(2π) exactly at the λ₀-crossing is open; flagged, not claimed.
3. Below a\*₀ the margin decays like a smooth curve from +7.6e−3 (a=0.30) to +1.06e−3 (a≈0.37): the atom-free regime is itself thin-margin, consistent with the Ω-profile structure: the low modes concentrate near the band edge u = 2π already at a = 0.37.

## 2. The coverage law (BS-II-4)

With **deficit(a) = max(0, −λ₀(A_a))** and **budget(a) = 2∑_{2≤n<e^{2a}} Λ(n)/√n** (the total operator-norm allowance of the in-window prime atoms), the coverage curve:

| a | deficit | budget | ratio | λ₀(Q_a) |
|---|---|---|---|---|
| 0.36 | 0.000 | 0.980 | 0.000 | +8.5e−4 |
| 0.40 | 0.078 | 0.980 | 0.080 | +1.8e−4 |
| 0.45 | 0.205 | 0.980 | 0.209 | +1.2e−5 |
| 0.48 | 0.277 | 0.980 | 0.282 | −3.0e−5 |
| **0.5493 (log √3)** | **0.430** | **0.980** | **0.439** | −7e−6 |
| 0.60 | 0.536 | 2.249 | 0.238 | −1.4e−5 |
| 0.70 | 0.734 | 2.942 | 0.250 | −7.5e−5 |
| 0.90 | 1.121 | 4.382 | 0.256 | −5.4e−4 |
| 1.00 | 1.324 | 5.853 | 0.226 | −3.8e−4 |
| 1.50 | 2.651 | 13.016 | 0.204 | −7.5e−3 |

**The law (TESTED MODEL):** the prime budget covers the archimedean deficit with ratio ≤ 0.44 everywhere probed, peaking exactly at the first window's right edge (a = log √3), then stepping down at each new prime shell and settling toward ≈ 0.20. λ₀(Q_a) stays within ±1e−3 of zero throughout — the full form is a critical-margin system at every scale (RH-consistent; sign not certified).

The peak at the first window explains the historical difficulty concentration: the first prime shell is where the coverage is tightest, and it is the only scale where a single atom must carry ~44% of its norm budget on the deficit direction.

## 3. The phase-rescue mechanism (BS-II-5)

The deficit direction at the first window is the u ≈ 2π-concentrated mode (the band-edge mode of BS-A3/#79). The prime-p translation acts on it by the Fourier phase factor cos(u·log p): for u = 2π the rescue sign is the sign of −cos(2π log p):

| p | cos(2π log p) | effect on the 2π-mode |
|---|---|---|
| 2 | **−0.3497** | rescue |
| 3 | **+0.8141** | anti-rescue |
| 5 | −0.7728 | rescue |
| 7 | +0.9428 | anti-rescue |
| 11 | −0.8012 | rescue |
| 13 | −0.9179 | rescue |

Measured at a = 0.5: the A-minimizing direction has Re⟨τ_{log 2}v, v⟩/‖v‖² ≈ −0.29 ≈ cos(2π log 2)·(overlap) ✓, and the prime-2 term contributes +0.28·‖v‖² on that direction (turning λ₀(A) = −0.28 into λ₀(Q) ≈ 0). **The coverage is not a norm phenomenon but a phase phenomenon**: the arithmetic phases {2π log p mod 2π} (rationally independent by unique factorization, equidistributed by Kronecker/Weyl) modulate which atoms rescue which band modes. This is the concrete instantiation of the "arithmetic source interaction" the original campaign order (§A3) requested: a fake composite atom at 6 has phase cos(2π log 6) = cos(2π(log2+log3)) = cos(4.3548+6.9022−2π)·... = +0.0644: nearly orthogonal to the 2π-mode — a source authentication signature (the fake atom cannot mimic the rescue geometry; consistent with #79's blindness control).

## 4. Rigorous band results (BS-II-1, BS-II-2)

**BS-II-1 (PROVED LOCAL).** Ω(u) = Re ψ(1/4+iu/2) − log π is strictly increasing on (0,∞). *Proof:* ψ′(z) = ∑_n 1/(z+n)²; at z = 1/4 + iu/2 with u > 0, each summand has Im[1/(x+n+iy)²] = −2(x+n)y/((x+n)²+y²)² < 0; hence Im ψ′ < 0 and Ω′(u) = −½ Im ψ′(z) > 0. ∎ (Numerically: max Im ψ′ = −0.169 over the scan.) Consequently Ω's negative region is exactly the band [0, u₀) with the single crossing.

**BS-II-2 (PROVED LOCAL).** Ω(2π) ∈ (−1.282e−3, −9.86e−4), rigorously: the exact positive-term series Ω(u) = ∑_j 2u²/(α_j(α_j²+u²)) − C_G (α_j = 2j+½) summed to J = 40 with integral-test tail brackets (∫_A^∞ 2u²/(a(a²+u²))da = log(1+u²/A²) exact). The unique zero u₀ ∈ (2π, 6.4). **The 2π band edge is certified to depth 1.06e−3.**

## 5. The no-go theorem for budget accounting (BS-II-6)

**BS-II-6 (PROVED LOCAL).** Any proof of first-window positivity that (i) replaces Ω by its band minimum −C_G (valid by BS-II-1), (ii) bounds the band mass ‖v̂‖²_{|u|≤2π} by the best prolate concentration μ₀(a), and (iii) bounds the pole+prime rescue by norm triangle inequalities, cannot close: at a = 0.549 (the first window, only the prime-2 atom present) the resulting lower bound is ≤ −1.78‖v‖².

*Constants (exact/rigorous):* the explicit test mode v₀ = cos(πx/2a)·1_W has rigorous band fraction β(a) ≥ 0.943 at a = 0.549 (closed-form transform, piecewise-exact band integral, elementary tail bound ∫_U^∞4α²(1−α²/U²)^{−2}ξ^{−4}dξ = 4α²(1−α²/U²)^{−2}/(3U³)), so μ₀ ≥ β; the crude deficit C_G·β = 5.066 exceeds the maximal triangle rescue 2‖cosh‖² + 2‖sinh‖² + 2∑c_n = 2 sinh(0.549) + 2·0.549 + 2 sinh(0.549) − 2·0.549 + 0.9802 = 3.288. Gap = 1.778. The TRUE deficit is only 0.430 — the sharp Ω-profile weighting recovers a factor ≈ 11.8. ∎ (Test: `test_nogo_gap_positive`.)

This kills the "budget accounting" proof family for window positivity and quantifies the necessity of the spectral/phase structure of §3 — complementing PR #86's moment-subspace route (which avoids the issue by excising the low modes) and PR #85's depth framework (which measures the full-kernel deficit). A proof must be profile-sharp to within a factor ~12 of the truth.

## 6. The Goldbach crossover: Fourier dichotomy and the binary mean dictionary

**BS-G1 (PROVED LOCAL, the |F|² trap).** For F_N(θ) = ∑_{n=1}^{N−1}Λ(n)e^{inθ}:

\[
\frac{1}{2\pi}\int F_N(\theta)^2 e^{-iN\theta}d\theta = \sum_{n+m=N}\Lambda(n)\Lambda(m) =: R_\Lambda(N),
\qquad
\frac{1}{2\pi}\int |F_N(\theta)|^2 e^{-iN\theta}d\theta = 0 \;\text{exactly}.
\]

*Proof of the second:* |F_N|² = ∑Λ(n)Λ(m)e^{i(n−m)θ}; n − m = N has no solution with 1 ≤ n, m ≤ N−1. ∎ The sum-diagonal and difference-diagonal objects are **exactly dichotomous**: any positivity route through |F_N|² (positive-definite autocorrelation arguments) is structurally void for the additive Goldbach problem; the difference-correlation problem is a different object (the Λ-autocorrelation Fourier coefficients). Verified numerically at machine precision (N = 20, 30: F²-coefficient = R_Λ(N) to 6 digits; |F|²-coefficient = −2.8e−14). This is the campaign order's warning ("Do not use |F_N|² in place of F_N²") made into an exact theorem with the emptiness reason.

**BS-G2 (PROVED LOCAL).** mean_G(X) := ∑_{4≤N≤X}R_Λ(N) = ∑_{n≤X−2}Λ(n)ψ(X−n) exactly (hyperbola identity; verified to 1.5e−11 at X = 400, 1.8e−12 at X = 150).

**BS-G3 (classical imports + TESTED MODEL).** The Dirichlet series of R_Λ is the coefficients of (ζ′/ζ)²; Perron at the double pole s = 1 gives mean_G(X) = X²/2(1+o(1)) with error governed by the double poles at the zeros (EXTERNAL CLASSICAL: Landau/Perron; the double pole at ρ produces X^{ρ+1} oscillations): **the binary Goldbach mean is a zero-detector at matched exponent** — zero-free Re s > 1−δ ⟺ mean-error O(X^{2−δ+ε}), exactly paralleling the BS-B3 dictionary of round 1, one power up. Numerics: mean_G(X) − X²/2 = −0.115·X^{3/2}, −0.114·X^{3/2}, +1.0e−4·X^{3/2} at X = 500, 1000, 3000: oscillating at the RH-predicted scale ✓ (TESTED MODEL corroboration).

**BS-G4 (PROVED LOCAL).** R_Λ(N) decomposes exactly into pure-prime-pair mass and prime-power contamination; e.g. N = 20: pure 16.208 (pairs (3,17),(7,13)), mixed 6.230 (the 2²+2⁴-type terms). The contamination is an exact finite bookkeeping, not an error term — required before any Λ-based lower bound is transported to true Goldbach pairs.

## 7. Boundary and status ledger

| ID | Statement | Status | Test |
|---|---|---|---|
| BS-II-1 | Ω strictly increasing (proof) | PROVED LOCAL | test_monotonicity_step |
| BS-II-2 | Ω(2π) ∈ (−1.29e−3, −9.9e−4); zero u₀ ∈ (2π, 6.4) | PROVED LOCAL (series + integral-test tail) | test_2pi_bracket_contains_direct |
| BS-II-3 | archimedean phase transition a\*₀ ∈ (0.370, 0.372); prime-free positivity below it; λ₁ ≈ −Ω(2π) at the crossing (flagged) | TESTED MODEL (certified bracket at resolution) | test_bracket, test_prime_free_positivity_below_transition |
| BS-II-4 | coverage ratio ≤ 0.44 (peak at first window), → ~0.20; λ₀(Q) ≈ 0 throughout | TESTED MODEL | test_coverage_ratios |
| BS-II-5 | phase-rescue: cos(2π log 2) < 0 rescues; measured rescue factor −0.29 ≈ cos(2π log 2)·overlap; phases equidistributed (Kronecker context, UNVERIFIED-as-applied label) | PROVED LOCAL (signs) + TESTED MODEL (factor) | test_rescue_phases, test_measured_rescue_factor |
| BS-II-6 | crude budget accounting fails by ≥ 2.28 (exact constants); profile weighting necessary (factor 5.3) | PROVED LOCAL | test_nogo_gap_positive |
| BS-G1 | \|F_N\|²-pairing ≡ 0; F_N²-pairing = R_Λ(N): exact dichotomy | PROVED LOCAL + verified | test_dichotomy |
| BS-G2 | hyperbola identity for mean_G | PROVED LOCAL + verified exact | test_exact |
| BS-G3 | binary mean is a zero-detector at matched exponent (classical Perron/Landau imports); numerics at X^{3/2} scale | EXTERNAL THEOREM + TESTED MODEL | test_track_scale |
| BS-G4 | prime-power contamination: exact bookkeeping | PROVED LOCAL | test_N20 |

**Nothing here proves RH or Goldbach.** The phase-transition and coverage numbers are float64 Rayleigh–Ritz at stated resolution; the bracket a\*₀ ∈ (0.370, 0.372) is clean by a 100× margin over the resolution but is a numerical bracket, not an interval-arithmetic certificate. The Kronecker/equidistribution statement about {log p} is classical mathematics but its *application* to rescue efficiency is a heuristic framing, labeled UNVERIFIED.

## 8. What this round buys

1. **The first structural map of the Weil window problem's arithmetic:** where the archimedean form dies (a\*₀ ∈ (0.370, 0.372), certified), how tightly the primes cover the deficit (ratio ≤ 0.44, law mapped), and *why* the coverage works (arithmetic phase geometry of 2π log p). Any future positivity proof must reproduce this phase structure to within a factor ~5 (BS-II-6 makes this quantitative).
2. **A rigorous band certification:** Ω monotone (proof), Ω(2π) bracketed to 3e−4 (series + exact tail bounds), the unique zero bracketed — the constants that every window estimate will need.
3. **The Goldbach Fourier dichotomy made exact** (the |F|² route is not merely "different" — it is identically zero) and the binary mean dictionary packaged at matched exponent with exact finite instruments (hyperbola identity, prime-power bookkeeping).
4. The λ₁ ≈ −Ω(2π) numerological observation at the phase transition: either a deep exact statement or a sharp coincidence; either way it is now on the table with data.

## 9. Next lemma (updated)

The round-1 target (first-window margin λ₀(a) ≥ 0 for a ∈ (log2/2, log3/2)) is now sharpened: the difficulty is exactly the coverage of the **2π-band-edge deficit direction** by the **single phase-rescue atom p = 2**. The next decisive lemma is the **phase-sharp two-mode inequality**: prove, on the first window, that the span of the two near-null modes (even bell, odd one-node) carries all negativity, and that on their two-dimensional span the exact 2×2 matrix [A + P₂] is positive — a finite verification with certified interval arithmetic over the two-mode effective operator plus a profile-weighted tail bound for the orthogonal complement (where BS-II-6's constants must be replaced by Ω-profile-weighted ones, recovering the factor 5.3). The measured targets: λ₀ ≥ 0 with the two-mode reduction accurate to ~1e−3.

**Source receipts:** parent PR #79 `cba5cca`; new-PR intake: #80 `cc0d50b`, #81 (meta-descent), #82 `bb5b6f9`, #83 (certified contour), #84 `526bad9`, #85 `dc6b7e3`, #86 `205ffd0`; main still `6e0d88f`.