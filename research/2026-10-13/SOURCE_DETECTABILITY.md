# Source-defect detectability horizon and open-world non-identifiability

**Date:** 2026-10-13. **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`. **RH PROVED: no.** No zeta zero, completed Gamma, pole, conductor or Weil kernel is read, constructed or guessed.

**Claim status:** PROVED LOCAL (elementary exact Möbius inversion + a floor-counting identity, realized in exact rational arithmetic). This fleshes out graph nodes C08 ("original-source calibration") and C12 ("rigidity") of the zero-centered residue observer. It is a finite-horizon certificate, **not** a global source-identification theorem.

---

## Theorem SD-01 — single-source-defect detectability horizon

**Domain.** Positions `d >= 2`; cells `k >= 1`; horizon `K >= 1`; a nonzero exact rational `delta`. Let `mu` be the Möbius function and let the *source* be a coefficient map `b: N -> Q`. The finite interpolant at horizon `K` is

```
F_K(k) = sum_{n<=K} b(n) floor(k/n) = sum_{m<=k} sum_{d|m} b(d).
```

The two forms agree termwise: `floor(k/n) = #{m <= k : n | m}`, so
`sum_n b(n) floor(k/n) = sum_{m<=k} sum_{n | m} b(n)`.

**Hypotheses.** The true source is `b(n) = mu(n)`. The *defect* changes a single position: `b'(d) = mu(d) + delta`, and `b'(n) = mu(n)` for all `n != d`.

**Statement.** For every such defect at position `d` with `delta != 0`:

1. **(horizon)** a finite observer at horizon `K` detects the defect (some cell `k <= K` has `F_K(k) != 1`) **iff** `K >= d`;
2. **(first cell)** the *first* cell at which the deviation is visible is exactly `k = d`;
3. **(exact value)** at that cell, `F_K(d) = 1 + delta` exactly.

**Proof.** Write `F'_K(k)` for the defective interpolant. Using the `sum_{m<=k} sum_{d|m}` form, the single mutation contributes `delta * 1_{d | m}` inside the inner sum, so

```
F'_K(k) = sum_{m<=k} sum_{e|m} mu(e)  +  delta * #{m <= k : d | m}
        = 1                                 +  delta * floor(k/d),
```

because `sum_{e|m} mu(e) = 1_{m=1}` (Möbius inversion) and the count of `m <= k` divisible by `d` is `floor(k/d)`. Hence:

- `floor(k/d) = 0` for `k < d`, so `F'_K(k) = 1` for all `k < d` — the defect is invisible below `d`, whatever the horizon `K`.
- `floor(d/d) = 1`, so `F'_K(d) = 1 + delta != 1` — the first visible cell is `d`, with the exact deviation `delta`.

Consequently the observer detects the defect iff some `k <= K` satisfies `k >= d`, i.e. iff `K >= d`. ∎

The `n = 6` fake-composite case (ZCR-08) is the instance `d = 6`, `mu(6) = +1`, `b(6) = -1`, i.e. `delta = -2`: the value `F_6(6) = 1 - 2 = -1` is reproduced exactly.

---

## Corollary SD-02 — open-world non-identifiability

**Statement.** For **every** finite horizon `K`, there exist **infinitely many** pairwise-distinct sources that coincide with `mu` on `1..K` (hence produce identical finite observations on every cell `k <= K`) yet differ from `mu` — and from each other — at infinitely many `n > K`. A finite observer can therefore never rule out open-world source differences: the finite data `{F_K(k) : k <= K}` determines the source only up to an infinite ambiguity beyond the horizon.

**Proof.** For any `n > K` and any nonzero exact rational `delta`, define `b^{(n,delta)}` to equal `mu` everywhere except `b^{(n,delta)}(n) = mu(n) + delta`. Because `floor(k/n) = 0` for all `k <= K < n`, the mutation at `n` contributes nothing to `F_K(k)` for `k <= K`; hence `b^{(n,delta)}` and `mu` agree on every cell `k <= K`. Varying `n` over the infinite set `{K+1, K+2, ...}` (and `delta` over nonzero rationals) yields infinitely many pairwise-distinct sources with identical finite observations. ∎

---

## Verified receipt

Implementation `observational_succ/source_detectability.py` (exact `Fraction` arithmetic, no floats; imports `mobius` from `zero_centered_residue.py`). Tests `tests/test_source_detectability.py` (12 assertions) verify, exactly:

- the true source interpolates `1` on every cell, and the two interpolant forms (`floor` form vs `sum_{m<=k} sum_{d|m}` form) coincide termwise;
- **IFF** `detected_at(d, delta, K) == (K >= d)` for `d in {2,3,4,5,6,7,9,12}` and a sweep of `K`;
- the first visible cell is `d` with exact value `1 + delta` for several `d` and `delta` (including the rational `3/2`);
- the `n=6` fake composite (`delta = -2`) gives `detectability_horizon(6,-2)` with `verified_value = -1`;
- `nonidentifiable_pair(K)` returns two sources agreeing on `1..K`, differing exactly at `K+1`, with identical observations on `1..K`;
- `open_world_family(K)` yields pairwise-distinct sources agreeing with `mu` on `1..K`;
- float `delta`, zero `delta`, empty source, out-of-range positions/horizons, and float source coefficients are all rejected.

Run:
```sh
python3 -m unittest tests.test_source_detectability -v
```

Both this suite and the neighbor `tests.test_zero_centered_residue -v` pass (12 + 7 tests).

---

## Boundary (what this does NOT establish)

This is a **finite-horizon** statement about a *single* position defect and about the *impossibility of global identification from finite data*. It does **not** provide:

- a global L² approximation bound that tends to zero (node N05);
- a source-identification theorem — SD-02 shows the opposite: finite observers are *structurally* unable to close the open world;
- any claim about a defect at *infinitely many* positions, or about defects that change the *Euler* structure versus a non-Euler (Davenport–Heilbronn) source;
- the completed Gamma/pole/conductor or Weil-form identification (P03/P07);
- any spectral or positivity conclusion, or any statement about zeta-zero locations.

The detectability result is sharp *at the single-defect level* precisely because the interpolant is a partial Möbius inversion: a defect at `d` enters the `k`-cell only through `floor(k/d)`, so the horizon `d` is the exact threshold. The non-identifiability corollary is the companion negative result — sharp detection of a *known* defect does not restore identifiability of the *unknown* open-world source.

## Next verdict-changing probes

1. Extend to a **finite set** of defect positions `D`: the deviation becomes `sum_{d in D} delta_d floor(k/d)`, and the first visible cell is `min D` — verify the horizon is still the minimum defective position and the value is `1 + sum_{d in D, d | k} delta_d` at `k = min D`.
2. Test the same detectability structure on the **matched Euler vs non-Euler** mutation to confirm it is source-faithful (it must be, since it uses only the `floor(k/d)` divisibility shadow).
3. Combine with ZCR-06 (LCM blackout) and the periodic-tail enclosure (PTE-01) to bound how the *defect signal* `|delta floor(k/d)|² / (k(k+1))` decays in the global L²(w) norm as the defect position `d` grows — i.e., whether distant defects are not merely late-detected but also *norm-small*.
