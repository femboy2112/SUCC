# Unconditional Mellin-functional lower bound (MS-01)

**Date:** 2026-10-13. **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`. **RH PROVED: no.** No zeta-zero location, Gamma, pole, conductor or Weil kernel used.

**Claim status:** PROVED LOCAL (classical bounded-functional Cauchy–Schwarz, rederived with rigorous rational interval enclosures). Complements — does not replace — the combinatorial periodicity/blackout enclosures (PTE-01, TS-01) and the *conditional* zero-based obstruction (ZCR-03).

## Theorem MS-01 — unconditional analytic lower bound

The cell Mellin functional `L_s(f) = ∫_0^1 f(x) x^{s-1} dx` is bounded on `ℓ²(w)`, `w_k=1/(k(k+1))`, precisely for `Re(s) > 1/2` (classical; the norm-squared summands behave like `k^{-2Re(s)}`). For **integer `s ≥ 2`** it is therefore bounded, and Cauchy–Schwarz gives, for `e = 1 − Σ_n a_n r_n`:

  `‖e‖ ≥ |L_s(e)| / ‖L_s‖`,

with the exact values
  `L_s(1) = 1/s`,   `L_s(r_n) = (ζ(s)/s)(1/n − n^{−s})`  (ZCR-02),
and  `‖L_s‖² = (1/s²) Σ_{k≥1} (k^{−s} − (k+1)^{−s})² k(k+1)`  (a *rational* series).

**Why this is new relative to the existing work:** ZCR-03 obtains a lower bound only from an actual nontrivial zero `ρ` (hence conditional on RH being false); the periodicity/blackout bounds (PTE-01/TS-01) are purely combinatorial. MS-01 is the **unconditional analytic** mechanism: it needs no zero, no RH, no prime data beyond `ζ(s)` at an integer `s ≥ 2`. It is weaker than the exact computation (a single functional sees one direction only) — which is the point: it is a rigorous, zero-independent certificate, not a fit.

## Rigorous computation

`observational_succ/mellin_lower_bound.py` computes everything by exact rational interval arithmetic:
- `ζ(s) = Σ k^{−s}` enclosed by truncation + integral tail bound `1/((s−1)N^{s−1})`.
- `‖L_s‖²` enclosed by truncation + tail bound `2s²/((2s−1)N^{2s−1})`.
- `|L_s(e)|` lower-bounded exactly via linear-in-`ζ(s)` monotonicity on the enclosure.
- The ratio is lower-bounded by an integer square-root refinement, so the final bound is a **valid rational lower bound**, never an overestimate.

Verified (`tests/test_mellin_lower_bound.py`, 6 assertions): `ζ(s)` enclosures bracket true `ζ(2), ζ(3), ζ(4)`; `‖L_2‖²` enclosure brackets an independent 10⁵-term sum to width < 10⁻³; the bound is positive and ≤ the true `‖e‖ = √(1−ln 2)` for `a_2 = 2`; monotone in `N`.

Example: `a_2 = 2`, `s = 2` → lower bound `0.156314…` (true `‖e‖ = 0.553943…`).

```sh
python3 -m unittest tests.test_mellin_lower_bound -v
```

## Boundary

- A single-functional lower bound is **not** a global `L²` convergence certificate (N05); it bounds the error from below, not above.
- `s` is restricted to integers `≥ 2` here; the boundedness threshold `Re(s) > 1/2` is classical and is *not* re-derived (cited, not proved).
- The bound is source-blind: it uses only `ζ(s)` at an integer, so it cannot distinguish Euler from non-Euler sources (consistent with PTE-03).

## Next probe

Maximize the bound over a family of functionals `{L_s}` (several integer `s`) — a finite set of bounded linear functionals spans a larger "seen" subspace, giving a strictly better unconditional lower bound; and combine with the per-residue TS-01 structure to get a lower bound that uses *both* the analytic and the combinatorial mechanisms at once.
