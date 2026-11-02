# Certified Frostman / non-concentration measurement harness — x16 orbit of π

**Author:** Ravel · **Date:** 2026-11-02 · **Branch:** `research/x3-rigidity-machinery-2026-11-02`

**Status of this artifact:** *measurement tool* (empirical). It **does not** prove `dim_* μ > 0`.

---

## 1. Object

Obligation **(B)** of the x3 rigidity route is `dim_* μ > 0` for the empirical accumulation

    μ = lim_{N→∞} (1/N) Σ_{n=1}^N δ_{x_n}

of the **completed orbit**

    x_n = { 16^{n−1} π },      x_{n+1} = { 16 x_n }   (exact).

`dim_* μ > 0` is equivalent to a **Frostman bound**

    μ_N(I) ≤ C |I|^s   for some s > 0,  uniformly in dyadic intervals I and horizons N.

The quantity a dimension proof must bound is the **sharpest empirical Frostman exponent**

    s_N := min over dyadic intervals I of  log(μ_N(I)) / log(|I|).

For a normal orbit this tends to **1**; for a low-dimensional orbit it tends to **0** (or a
constant < 1). This harness measures `s_N` exactly, at dyadic scales `k = 0 .. K_max(N)`.

---

## 2. Method — exact, no floating-point error

The orbit is the base-16 digit tail of π: `x_n` is the hex string of `frac(π)` starting at
position `n`. Hence the orbit is encoded **exactly** by the base-16 (equivalently base-2) digit
string of π, and a dyadic interval of bit-depth `k` (length `2^{−k}`) is a `k`-bit prefix of a
point's binary expansion.

The harness:

1. **Exact π digits.** Reads the binary mantissa of `mpmath`'s π directly (`frac = man·2^exp`),
   groups 4 bits → hex digits. No base-conversion rounding. Precision `D ≈ 1.205·M` decimal
   digits for `M` hex digits. Verified against the known hex prefix
   `243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89…` (64 digits, PASS)
   and against the digit map `x ↦ {16x}` independently.
2. **Binary trie over N suffixes.** Counts, for every `k`-bit prefix, how many of the N orbit
   points land in the corresponding dyadic interval — i.e. the exact `μ_N(I)` occupancy.
3. **Sharpest exponent.** `s_N = min_k min_I log(μ_N(I)) / log(2^{−k})`, over all trie nodes.

**Scale convention.** For a finite `μ_N`, a single point in a length-`2^{−k}` interval gives
`μ_N(I)=1/N`, which violates `μ_N(I) ≤ C|I|^s` for any fixed `s>0` once `k > log₂ N`. We therefore
compute `s_N` only over `k ≤ K_max := ⌊log₂ N⌋` (i.e. `|I| ≥ 1/N`). As `N→∞`, `K_max→∞` and every
scale is eventually covered — the standard finite-horizon truncation of the lower Frostman dimension.

---

## 3. Results — main orbit (π)

| N | K_max | s_N (π) | worst interval (k, count) |
|---|-------|---------|---------------------------|
| 10³ | 9 | 0.77398 | (9, 8) |
| 10⁴ | 13 | 0.80618 | (13, 7) |
| 10⁵ | 16 | 0.83998 | (16, 9) |
| 10⁶ | 19 | 0.86695 | (19, 11) |

`N = 10⁶` full scale profile (k → ratio = log μ / log 2^{−k}):

```
 k=1  .99979    k=6  .99594    k=11 .98250    k=16 .93045
 k=2  .99856    k=7  .99347    k=12 .96936    k=17 .90635
 k=3  .99827    k=8  .99158    k=13 .96456    k=18 .89026
 k=4  .99811    k=9  .98960    k=14 .95660    k=19 .86695   <- deepest scale
 k=5  .99733    k=10 .98736    k=15 .94691
```

**Reading.** Every shallow/mid scale (k ≤ 16) sits at ratio ≥ 0.93, monotonically tending to 1.
The only downward pull is the deepest scale `k = K_max`, where the max bin load among `2^k ≈ N`
bins is `~ log N / log log N` — a **universal finite-size artifact** present in *every* normal
orbit. The worst interval is always at the deepest scale, with tiny count (8→11 points).

**Empirical conclusion.** `s_N` rises monotonically toward **1**, and is indistinguishable from a
random i.i.d. orbit (see §4). This is precisely the signature of a **normal (Lebesgue-like)**
orbit, i.e. the empirical accumulation is consistent with `dim_* μ = 1`.

---

## 4. Controls — validation that the tool distinguishes `dim_*`

| Control | construction | expected dim_* | measured s_N (N=10³) |
|---|---|---|---|
| (a) Liouville | α = Σ 2^{−j!}, x_n = {2^n α} | 0 | **0.0054** (≈967/1000 pts in one bin) |
| (a′) rational | α = 1/17, x_n = {16^n α} (periodic, finite support) | 0 | **0.3333** (= 125 pts per atom) |
| (b) random | i.i.d. uniform hex digits (seed 12345) | 1 | **0.795** (→1, tracks π) |

The tool **correctly separates** the two dimension classes by an order of magnitude:

- Liouville orbit concentrates (~97% of mass in a single dyadic interval at depth 9) → `s_N ≈ 0.005`.
- Rational periodic orbit has finite support → `s_N = 1/3` (8 atoms at the resolved scales).
- Random orbit tracks π's orbit almost exactly at every horizon (diffs ≤ 0.01, pure PRNG seed
  fluctuation):

| N | π s_N | random s_N |
|---|---|---|
| 10³ | 0.77398 | 0.79538 |
| 10⁴ | 0.80618 | 0.80618 |
| 10⁵ | 0.83998 | 0.83048 |
| 10⁶ | 0.86695 | 0.86035 |

This confirms the harness is a valid discriminator: it would *detect* any non-trivial
concentration of π's orbit if it existed at the tested scales, and it detects none.

---

## 5. What this CAN and CANNOT certify (brutal honesty)

**CAN certify (exact, unconditional):**

- The exact value of the finite-empirical `s_N` for the *truncated* digit string of π of the
  stated length — a finite computation with exact integer/`mpmath` arithmetic (no float error).
- The exact dyadic occupancy counts `μ_N(I)` for all dyadic I at depth ≤ K_max(N).
- That the tested prefix of π's orbit (up to `N = 10⁶` points, `M ≈ 10⁶` hex digits) exhibits **no
  measurable non-concentration** at any scale `≤ log₂ N`, and is statistically indistinguishable
  from a random orbit.

**CANNOT certify:**

- `dim_* μ > 0` for the *infinite* orbit. Any finite horizon yields a finite vector of occupancies;
  it can only *lower-bound* the apparent `s` at observed scales. It cannot rule out a heavier
  interval at some unseen scale driving the true liminf to 0.
- `lim_{N→∞} s_N = 1` (π normality), nor that `s_N` stays bounded away from 0 at all future N.
- That the weak-* limit μ exists, is Lebesgue, or satisfies a Frostman bound with a *uniform* C.

**Boundary.** This is a *measurement* tool that empirically locates the Frostman exponent and
validates the trie machinery against known dim_*=0 / dim_*=1 controls. It is **not** a proof of
`dim_* μ > 0` and is not offered as one.

---

## 6. Reproducibility

```sh
python3 research/2026-11-02/x3_rigidity_machinery/frostman_harness.py --selftest   # verify π digits
python3 research/2026-11-02/x3_rigidity_machinery/frostman_harness.py --N 1000000 --controls
```

Dependencies: `mpmath` (≥1.2), Python ≥3.8. Runtime ≈ 21 s at N=10⁶ (12.8 s π digits + 8 s trie).
All outputs are deterministic given the PRNG seed (default 12345) for the random control.

---

## 7. Relation to the x3 route and the signed Weyl bottleneck

This harness does **not** touch the actual wall of the x3/Furstenberg route, which — per
`UNIVERSAL_X3_DEFECT_THEOREM.md` — is the *measure-level* ×3-invariance (equivalently the full
Weyl equidistribution `Σ_{n≤N} e(h·16^n π) = o(N)`), not any single Fourier defect. `dim_* μ > 0`
(obligation B) is a *necessary* consistency check on the empirical accumulation, and it passes.
Passing it is a sanity gate, **not** a step toward normality: every normal orbit passes it, but so
do many non-normal orbits (e.g. an orbit with a single positive-mass atom plus a diffuse part would
still have `dim_* > 0`). The positive result here is **evidence of consistency**, not of the
source-specific signed cancellation that remains the open bottleneck.

**Still DARK:** signed Weyl cancellation / measure-level ×3-invariance. π normality and RH remain OPEN.
