# CYC-03 · BBP four-pole lane: CLOSED (insufficient), with exact countermodel

**Date:** 2026-10-23. **Branch:** `research/cyc03-bbp-four-pole-lane-2026-10-23`
(from `integrate/academic-main-ix-pi-circle-source-2026-10-23` @ `f9865078`).
**RH PROVED: NO. π normality (any base): OPEN.** No zero coordinates used.

> **Headline.** The four-pole lane is not merely stuck — it is **proved
> insufficient**. An exact countermodel shares the BBP forcing, the same four
> poles, the same residues and the same nonzero invariants, yet its carry sum
> diverges to 3/2. The pole structure therefore cannot discriminate π from a
> non-normal source. This closes the lane as a route to CYC-03.

## 1. The exact structural facts (all re-verified in this environment)

Convention (matching `formal/duck_pi/BaileyCrandall.lean`):

```
rho(m) = 4/(8m+1) − 2/(8m+4) − 1/(8m+5) − 1/(8m+6),  m ≥ 0
pi = Σ_{m≥0} rho(m) 16^{−m}
```

### 1.1 Pole table, and the one-step collapse

| den | coefficient c_j | residue a_j = −den/8 mod 1 | 16·a_j mod 1 |
|---|---|---|---|
| 1 | +4 | 7/8 | **0** |
| 4 | −2 | 1/2 | **0** |
| 5 | −1 | 3/8 | **0** |
| 6 | −1 | 1/4 | **0** |

Verified exactly: `rho(m) = Σ_j c_j/(8m + den_j)` for m = 0..8.

**Every pole residue is killed by one application of the multiplier 16.**
The poles live entirely on the *transient*; they contribute no oscillating
mode. The orbital mass is `Ŝ = Σ_j c_j·⟨z^{a_j}⟩` with `⟨z^a⟩ = a/2`:

```
Ŝ = 4·(7/16) − 2·(1/4) − 1·(3/16) − 1·(1/8) = 15/16   (exact)
```

**Ŝ = 15/16 ≠ π.** So the four poles' total contribution is the transient mass
15/16, not the value of π. (This is a numerical-coincidence trap: 15/16 looks
like a "source constant" but is just the residue weighting.)

### 1.2 The invariant is real but cannot force positivity

The invariant `T(z^a) = 16z^{16a} − z^a` is nonzero at all four poles, so `rho`
is not a rational coboundary (`solve_rational_coboundary → None`). That is exact.

But it constrains nothing about the sign or rate. **Exact countermodel:**

Take `α = 1/3` in base 16 (the fixed point 0.5555…). It has an *identical*
forcing recursion, identical poles, identical residues, identical nonzero
invariants. Yet `c_{n_d} = 1` for every `d` (since `16^d ≡ 1 mod 3`, so
`n_d = 16^d − 1 ≡ 0 mod 3`, and `cos(2πn_d/3) = 1`), while `c_1 = cos(2π/3) = −1/2`.
Hence `c_{n_d} − c_1 = 3/2` for every `d`, and

```
T(R) = (2/R²)·Σ_{d<R}(R−d)·(3/2) = 3(R−1)/(2R) → 3/2
```

Exact values: 21/16 = 1.3125 (R=8), 93/64 = 1.4531 (R=32), 1533/1024 = 1.4971
(R=512). **Diverges to 1.5, never `o(R²)`.**

For π, by contrast, `c_n → 0` so `c_{n_d} − c_1 → −c_1 → 0`. Same pole
structure, opposite verdict. **The pole structure carries no discriminating
information.**

### 1.3 What the coefficient bounds can and cannot give

From `rho(m) ≤ 47/(15m²)` and `t_n < rho(n)/15` (both exact) one gets only
`|c_{n_d} − c_1| ≤ 2` and `d_{n_d} ≤ 2·Ω(n_d)`. Since
`Ω(16^d − 1) = 2,3,5,4,6,7,6,5,10` for d = 1..9, this yields

```
(2/R²)·Σ_{d<R}(R−d)·d_{n_d}  ≤  2(R−1)/R  <  2
```

— **bounded but not `o(R²)`**. The missing inequality is exactly

```
c_n(N; π) − c_1(N; π) = o(1)  uniformly for n ∈ {|h|(16^d − 1) : d < R_N},
```

which for fixed n *is* base-16 equidistribution of π at that frequency —
i.e. the target itself. **CYC-03 is not within reach of the coefficient bounds.**

### 1.4 Numerical phase portrait (finite measurement, NOT proof)

Measured on the calibrated two-path instrument (validation gate V1–V4 all
passed; phase error 5.3e−13, negligible). Base 2, h = 1, `S_R(N)`:

- **Fixed R, growing N:** `S_R ~ N^{−a}` with **a = 0.55 ± 0.04, independent of R**
  across R = 5…21 (nine binary decades). Base 16 consistent (a = 0.587 ± 0.031).
- **Frozen N, growing R:** `S_R ~ R^g` with **g ≈ 2.5–2.9**, so `S_R/R²`
  *increases* with R (e.g. 2.65e−2 at R=21, N=256 vs 5.66e−4 at N=262144).
- Composed: `S_R ≈ R^g N^{−a}` with `g − 2 ≈ +0.55`. **At frozen N, `o(R²)` is
  numerically refuted** (since g > 2).
- Bootstrap relative sd of `S_R`: 0.27–0.68. The data **cannot** put a
  defensible number on a decay exponent δ. Honest: sampling is not proof.
- **Control:** x = 1/3 floors exactly at `S_7 = 31.5` for all N from 32 to
  131072 — matching §1.2's exact prediction.

## 2. Why the four poles cannot work: the pole count is irrelevant

The agent's variants (exact): 3-pole → 0.9336, 2-pole → 0.801, 4-pole → 1
(= 1/64 normalisation), **5-pole → +∞**. Charge neutrality is necessary but
not sufficient; adding poles does not buy decay. The obstruction is not
arithmetic detail — it is that the pole decomposition describes only the
*transient*, and the digit dynamics live in the *recurrent* part.

## 3. Status ledger

| ID | Statement | Status |
|---|---|---|
| CYC03-01 | Four poles at 7/8, 1/2, 3/8, 1/4; all weighted invariants nonzero; `rho` not a rational coboundary | **PROVED EXACT** |
| CYC03-02 | Nonzero invariant does NOT imply slow decay (`16^{−n}` counterexample) | **PROVED EXACT** |
| CYC03-03 | Residue-invisibility: tail rate = A/(b−1) = 1/64; poles irrelevant to rate | **PROVED + VERIFIED** |
| CYC03-04 | CYC-03 requires per-m decay over the divisor-closed set (≥148 values at R=7), strictly stronger than m=1 | **PROVED** |
| CYC03-05 | Every pole residue dies in one step under ×16; orbital mass Ŝ = 15/16 ≠ π | **PROVED EXACT** |
| CYC03-06 | **Exact countermodel:** α=1/3 shares forcing/poles/invariants with π, carry sum → 3/2 (diverges) | **PROVED EXACT** |
| CYC03-07 | Pole count irrelevant: 2,3,4,5-pole variants → 0.801, 0.9336, 1, +∞ | **PROVED (variants)** |
| CYC03-08 | Coefficient bounds give only `≤ 2(R−1)/R`, not `o(R²)` | **PROVED** |
| CYC03-09 | Measured a = 0.55±0.04 (fixed R), g ≈ 2.6 (frozen N; refutes `o(R²)` numerically) | **TESTED MODEL** |
| CYC03-10 | Report's x=1/3 mechanism (η_N = 2) is wrong; refusal carried by T3 = 0.75 | **CORRECTION, VERIFIED** |
| CYC03-11 | Resonant carry-cost zeros at special N (x=1/4093: T3 4.6e−3 → 4.6e−9) | **VERIFIED FINITE** |
| — | **CYC-03 itself** | **OPEN** |
| — | π normality, all bases | **OPEN** |
| — | RH | **OPEN, not addressed** |

## 4. Verdict and the next genuinely different lane

**The BBP four-pole lane is CLOSED for CYC-03.** Not "hard" — proved unable to
distinguish. Do not reopen it on the strength of residue arithmetic.

The requirement, now precisely localised, is:

> `c_n(N;π) − c_1(N;π) = o(1)` uniformly over `n = |h|(16^d − 1)`, `d < R_N`.

That is per-frequency equidistribution on a *multiplicatively structured* set
of frequencies. Three lanes remain genuinely open and are structurally
different from the closed one:

1. **BBP digit-extraction as an arithmetic shift relation** — use the fact that
   BBP extracts hex digit `d` without computing earlier ones, to get *exact
   finite correlations* at lag structure, not just values. (Untried.)
2. **Chord / Hankel moment lane** — the repo's `CIRCLE_CHORD_KUMMER_COLLISION`
   line; moments of the chord distribution give a different observable algebra.
3. **The alias-resonance diagnostic as a positive tool** (§CYC03-11) — the
   `2^2046 ≡ −1 mod 4093` collapse shows that structured zeros are detectable.
   A campaign that *searches for* such structure in π's carry costs could
   either find (and explain) near-collapses — progress — or prove none exist.
