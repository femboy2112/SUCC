# CYC-03 · BBP four-pole lane · and the correction of two published claims

> **CORRIGENDUM 2026-10-24 — SOURCE TYPING.** The following historical
> report incorrectly concluded that the BBP four-pole approach was
> mathematically closed. The original poles live in the forcing INDEX
> variable, not as states under x→16x mod1. The actual forcing-index
> signed first pole moment is 15/64 and the resulting Green tail has
> positive continuous Hausdorff measure and infinite Hankel rank.
> The unforced orbit x=1/3 does not satisfy the complete BBP
> initial condition. A rational high-order forcing family replaces
> the invalid exponential non-coboundary example, and the earlier
> universal absolute prime-path cost ceiling has an exact counterexample.
> **DO NOT cite the old closure verdict.** See
> [corrected audit](CYC03_LANE_CLOSED.md) and
> [new source proof](../2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md).
> Historical calculations below are retained for provenance; their
> overbroad dynamical conclusions are superseded.


**Date:** 2026-10-23. **Branch:** `research/cyc03-bbp-four-pole-lane-2026-10-23`
(from `integrate/academic-main-ix-pi-circle-source-2026-10-23` @ `f9865078`).
**RH PROVED: NO. π normality (any base): OPEN.** No zero coordinates used.

## 1. What this round established

### 1.1 The obstruction witness is exact, and it is weaker than it looks

The BBP forcing `r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)` has four
simple poles in base 16:

| residue | coefficient | weighted orbit invariant |
|---|---|---|
| 7/8 | +1/2 | **+1/2** |
| 1/2 | −1/4 | **−1/4** |
| 3/8 | −1/8 | **−1/8** |
| 1/4 | −1/8 | **−1/8** |

All four invariants are nonzero, so `solve_rational_coboundary` returns `None`:
**r is not a rational coboundary** `r(z) = 16q(z−1) − q(z)`. The clean
telescoping route to cancellation is closed. (Exact, `cyc03_pole_obstruction.py`.)

### 1.2 But a non-coboundary can decay geometrically (counterexample)

`r(n) = 16^{−n}` is not a coboundary in that class — `16·c·16^{−(n−1)} − c·16^{−n}
= c·16^{−n}(16²−1) ≠ 16^{−n}` — yet its tail `t_n = 16^{−n}/255` decays
geometrically. **Therefore: a nonzero pole invariant obstructs the finite
rational coboundary, NOT cancellation.** Any argument of the form "the
invariant is nonzero, hence CYC-03 fails" is refuted by this one-line
counterexample. Recorded so it cannot be made.

### 1.3 RESIDUE-INVISIBILITY THEOREM (the decisive structural finding)

Expanding the collapsed rational function (exact sympy):

```
r(x) = 15/(64x²) + 151/(512x³) + 1209/(4096x⁴) + 8995/(32768x⁵) + O(x⁻⁶)
```

The tail rate is fixed by the collapsed asymptotics alone:

```
t_n = Σ_{k≥1} 16^{−k} r(n+k),   leading term  A/(b−1)·(1/n²)  with A = 15/64
    ⇒ A/(b−1) = (15/64)/15 = 1/64.
```

Verified numerically to high precision (`n²t_n → 1/64` from below:
0.014376, 0.015357, 0.015557, 0.015611, 0.015622 at n = 10, 50, 200, 1000, 5000).

**The four pole residues never enter the tail rate.** They control digit-shift
*geometry*; the rate is controlled by the rational function's asymptotics.
This is a negative structural result for the four-pole lane: **attacking
through the residue structure cannot by itself move CYC-03.**

Also confirmed live: `π = 16·t₀` to 20 digits from rigorous rational enclosures
(width 2.4e−78 at 60 terms).

### 1.4 Where CYC-03 actually bites (the strength of the required statement)

CYC-03 needs `Σ_{d<R}(R−d)·d_{n_d}(N) = o(R²)`. The trivial bound
`d_m ≤ Ω(m)·max|c|` gives `Σ(R−d)·Ω(16^d−1) ≈ R²logR/2` — **no** `o(R²)`.
So CYC-03 requires genuine decay of `c_m` for *every* m in the divisor-closed
set (148 values already at R=7), not merely `|A_{1,N}| → 0` for m = 1.
**CYC-03 is strictly stronger than single-frequency cancellation.**

## 2. Two corrections to the published CYC-01 report

These were found by independent audit and verified by me live.

### 2.1 The x=1/3 refusal is driven by T3, not by η_N

`docs/PI_MOONWALK_CYC01_REPORT.md` §3 states that at x=1/3, b=16, the RHS stays
"≈1.118 at R=2 → 1.208 at R=12". Reproducing this live:

```
x=1/3, b=16, N=4096, R=2:  eta=0.000000  T1=0.500  T2=0.000  T3=0.750
                            RHS=1.118278  GAP=0.118278
```

`η_N = max(0, 2c₁) = 0`, **not 2**. Because 1/3 in base 16 is 0.5555…, the
orbit is the fixed point, `c₁ = cos(2π/3) = −1/2`, so `2c₁ = −1` and the
positive-part clamp zeroes it. The refusal is correct but is carried by
**T3 = 0.75**, not by the `R^{−1/2}` floor. The report's arithmetic mechanism
description is wrong even though its conclusion (soundness by refusal) stands.

### 2.2 Carry costs resonate — finite-prefix zeros are structural, not decay

At x = 1/4093 (prime, 2 has order 4092), b = 2:

| N | \|A_{1,N}\| | T3 (R=4) |
|---|---|---|
| 1023 | 1.66e−02 | 4.61e−03 |
| 2047 | 5.85e−03 | **4.60e−09** |
| 4095 | 4.88e−04 | 4.83e−08 |

T3 collapses by **six orders of magnitude** at N=2047 because
`2^2046 ≡ −1 (mod 4093)`, so `x_{j+2046} = 1 − x_j` and
`cos(n·2π(1−x)) = cos(n·2πx)` — a symmetry-induced cancellation, not decay.
**Consequence for any CYC-03 numerics:** a vanishing carry cost at isolated N
is not evidence of the needed `o(R²)`; the campaign must distinguish resonant
zeros from genuine decay. This is a calibration requirement, now recorded.

## 3. Status ledger

| ID | Statement | Status |
|---|---|---|
| CYC03-01 | BBP forcing has four poles, all weighted invariants nonzero ⇒ not a rational coboundary | **PROVED EXACT** |
| CYC03-02 | Nonzero invariant does NOT imply slow decay (`16^{−n}` counterexample) | **PROVED EXACT** |
| CYC03-03 | Residue-invisibility: tail rate = A/(b−1), poles irrelevant | **PROVED (asymptotics) + VERIFIED** |
| CYC03-04 | CYC-03 requires per-m decay over the divisor-closed set, strictly stronger than m=1 cancellation | **PROVED (bound argument)** |
| CYC03-05 | π = 16·t₀ to 20 digits via rational enclosures | **VERIFIED FINITE** |
| CYC03-06 | Report's x=1/3 mechanism (η_N=2) is wrong; refusal carried by T3=0.75 | **CORRECTION, VERIFIED** |
| CYC03-07 | Resonant carry-cost zeros at special N (1/4093 example) | **VERIFIED FINITE** |
| — | CYC-03 itself (the `o(R²)` convergence) | **OPEN** |
| — | π normality, all bases | **OPEN** |
| — | RH | **OPEN, not addressed** |

## 4. The precise missing lemma (unchanged by this round, better localised)

> **CYC-03.** For x = π, b = 16, every fixed h ≠ 0, and admissible R_N → ∞:
> `Σ_{d<R_N}(R_N−d)·d_{|h|(16^d−1)}(N; π) = o(R_N²)`.

What this round adds: the route **cannot** be the pole-residue structure (§1.3),
**cannot** be a coboundary telescoping (§1.1), and is **not** discharged by
any single-frequency estimate (§1.4). It requires genuine per-m cancellation
across the divisor-closed cyclotomic set — i.e. a Diophantine statement about
π's orbit correlations, of the same species as bounds on the irrationality
measure of π. Nothing in the current stack supplies it.
