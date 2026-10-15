# Tail-split enclosure: exact synchronized-cell separation (TS-01)

**Date:** 2026-10-13. **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13` (continues PTE-01). **RH PROVED: no.** No zeta zero, Gamma, pole, conductor or Weil kernel read or constructed.

**Claim status:** PROVED LOCAL (elementary exact periodicity + telescoping + residue-class split, realized in exact rational arithmetic). Finite-certificate sharpening; not a global L² bound.

## Theorem TS-01 — exact blackout-cell separation

With `F(k)=Σa_n (k mod n)/n`, `L=lcm(moduli)`, defect `c_r=|1-F(r)|²` on the period `r=1..L`. The residue `r=L` is **exact**: `F(L)=Σa_n·0=0`, so `c_L=1`. Let `m'=min_{r<L} c_r`, `M'=max_{r<L} c_r`, and `B=Σ_{j: jL>K} 1/(jL(jL+1))` (the exact synchronized-cell tail). Then the global squared error `E` satisfies

  `P_K + B + m'·(1/(K+1) − B)  ≤  E  ≤  P_K + B + M'·(1/(K+1) − B)`,

because the non-blackout cells carry total weight `1/(K+1) − B` and defect in `[m',M']`, while the blackout cells contribute exactly `B`.

**Sharpness vs PTE-01 (which folded `c_L=1` into the global min/max):**
- **Lower bound: strictly sharper always.** `TS_lower − PTE_lower = B(1−m') ≥ 0`, strict when `m'<1`.
- **Upper bound: strictly sharper whenever `M'≠1`.** If `M'>1`, `TS_upper = PTE_upper − B(M'−1) < PTE_upper`; if `M'<1`, `TS_upper = PTE_upper − (1−M')(1/(K+1)−B) < PTE_upper`; equality only when `M'=1` exactly. The truncation remainder `1/(J L²) → 0` as `J→∞`, so the gain is recovered exactly in the limit.
- **Blackout-dominated regime:** when the synchronized cells are the dominant contributor (exactly where the ZCR-06 LCM obstruction bites), the upper bound collapses to the exact blackout tail. Example `a_2=2`: enclosure width **5.9e-5** vs PTE-01's **3.9e-3** (a 65× tightening), bracketing `E=1−ln 2`.

This makes the ZCR-06 LCM obstruction *two-sided and certified*: not merely `E ≥ 1/L²` asymptotically, but an exact-rational `[lower, upper]` that isolates the synchronized cells' contribution from the residual.

## Verified receipt

`observational_succ/tail_split_enclosure.py` (exact `Fraction`), `tests/test_tail_split_enclosure.py` (9 assertions). Verified: `c_L=1` exactly; `B` interval `[B_low, B_low+1/(JL²)]` brackets an independent high-precision partial sum; enclosure brackets `1−ln 2` and an independent 4000-cell direct sum for an arbitrary family; lower bound `≥` PTE-01 lower in every tested family; remainder `→0` in `J`.

```sh
python3 -m unittest tests.test_tail_split_enclosure -v
python3 -m unittest tests.test_periodic_tail_enclosure -v
```

## Boundary

Still a **finite** certificate. `B → 0` as `K` grows and `L` grows with the family, so no uniform positive lower bound exists (consistent with ZCR-06). This is a sharper instrument on the same finite Nyman problem, not the global L² bound (N05). The enclosure is source-blind (uses only `r_n` periodicity).

## Next probe

Use the exact per-residue defect vector `(c_r)` — now fully separated — to lower-bound `E` by a weighted `ℓ¹` combination of *all* nonzero residue classes, not just the blackout residue, tightening the lower bound from `B + m'(1/(K+1)−B)` toward the true `Σ_r c_r S_r` with per-class weight enclosures.
