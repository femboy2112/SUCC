# Sharp periodic-tail enclosure for the zero-centered residue-clock L² error

**Date:** 2026-10-13 (America/New_York). **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`, stacked on bootstrap `research/property-proof-graph-bootstrap-2026-10-13` @ `11781889a3822d8f2602716fdc12f80755f1b399` (which descends from `main` `6e0d88f1b235b85188393bbcd64ac0436cb71a70`). **RH PROVED: no.** No zeta zero, completed Gamma, pole, conductor or Weil kernel is read, constructed or guessed.

**Claim status:** PROVED LOCAL (elementary exact periodicity + telescoping, explicitly realized in exact rational arithmetic). This is a *sharpening of an existing finite certificate*, not a new priority theorem and not a global L² convergence result.

## Theorem PTE-01 — exact periodic two-sided enclosure

Let `S` be a finite set of moduli `n >= 2`, let `(a_n)_{n in S}` be exact rational coefficients, and set `F(k) = sum_n a_n r_n(k)` with `r_n(k) = (k mod n)/n`. Let `L = lcm(S)`. The squared global `L²(w)` error with `w_k = 1/(k(k+1))` is

  `E = sum_{k>=1} |1 - F(k)|² / (k(k+1))`.

Then, for every horizon `K >= 1`:

  `P_K + m/(K+1)  <=  E  <=  P_K + M/(K+1)`,

where `P_K = sum_{k=1..K} |1 - F(k)|²/(k(k+1))` is exact, and

  `m = min_{1<=k<=L} |1-F(k)|²`,  `M = max_{1<=k<=L} |1-F(k)|²`.

Both `m` and `M` are exact rationals obtained by sampling the single period `1..L`.

**Proof.**
1. `r_n` is `n`-periodic because `(k+n) mod n = k mod n`. Since `L` is divisible by every `n in S`, `F(k+L) = F(k)`; hence `|1-F(k)|²` is `L`-periodic, and its global min/max over all `k>=1` equal its min/max over `1..L`.
2. Every tail weight `1/(k(k+1)) > 0`, so `m·Σ_{k>K} 1/(k(k+1)) <= tail <= M·Σ_{k>K} 1/(k(k+1))`.
3. Telescoping: `Σ_{k>K} 1/(k(k+1)) = Σ_{k>K}(1/k - 1/(k+1)) = 1/(K+1)`.
4. Combining, `E = P_K + tail` gives the stated enclosure. ∎

**Sharpness.** The prior enclosure (ZCR-07) is `P_K <= E <= P_K + (1+Σ|a_n|)²/(K+1)`. We have `|1-F(k)| <= 1 + Σ|a_n|·|r_n(k)| <= 1 + Σ|a_n|`, with `|r_n(k)| <= (n-1)/n < 1` for every `n >= 2`, so `M < (1+Σ|a_n|)²` **strictly** for every nonempty family. The new upper bound is therefore strictly sharper in every case, and it additionally supplies a lower bound `m/(K+1)` the prior enclosure could not (nonzero generically). Example: the ZCR-04 perfect-interpolant family `{2:1, 3:1, 4:0, 5:5/6}` has `L=60`, old coefficient `529/36 ≈ 14.69`, new coefficient `M=1` — a **~15×** tightening; the single clock `a_2=2` tightens from `9` to `1` (4×).

## Verified receipt

Implementation `observational_succ/periodic_tail_enclosure.py` (exact `Fraction` arithmetic, no floats). Tests `tests/test_periodic_tail_enclosure.py` (8 assertions) verify, exactly:
- `r_n` is `n`-periodic and `F` is `L`-periodic;
- the sampled-period extremes cover every defect;
- the enclosure is ordered with strictly positive lower bound in the generic case;
- `strictly_sharper_upper` with exact coefficients `M < (1+Σ|a_n|)²`;
- the known closed form `||1 - 2g_2||² = 1 - ln 2 ≈ 0.3068528194` is **bracketed** by the exact enclosure at `K=256` (independent analytic route: `Σ_{j>=1} 1/((2j)(2j+1)) = 1/2 - 1/3 + 1/4 - ... = 1 - ln 2`).

Run:
```sh
python3 -m unittest tests.test_periodic_tail_enclosure -v
```

## Boundary (what this does NOT establish)

This is a finite certified-enclosure improvement. It does **not** provide:
- a global L² approximation bound that tends to zero (node N05);
- the completed Gamma/pole/conductor or Weil-form identification (P03/P07);
- any spectral or positivity conclusion;
- any statement about zeta-zero locations.

As `K` grows with `L` fixed, the enclosure width `(M-m)/(K+1) -> 0`, so it is a *convergent* finite certificate — but `L` itself grows with the coefficient family, and no uniform (in the family) positive lower bound is claimed; the LCM blackout bound `1/L² -> 0` (ZCR-06) shows why a uniform lower bound is unavailable. This enclosure is therefore a sharper instrument for the **same** finite problem, not a bridge to the global one.

## Next verdict-changing probes

1. Combine the sharp enclosure with the ZCR-06 LCM structure to separate the tail into the synchronized `jL` cells (exactly computable) and the residual, refining the lower bound toward `1/L²` plus a residual term.
2. For the optimal Báez-Duarte coefficient family `a_n = -mu(n)/n`, derive an explicit `L`-asymptotic for `M` and `m` and test whether the enclosure width remains useful as `K` grows.
3. Attempt the same periodicity argument on the **matched Euler vs non-Euler (Davenport–Heilbronn)** mutation to confirm the enclosure is source-faithful (it must be, since it uses only `r_n` periodicity — verify it detects no source, i.e. it is a pure instrument).

## Lean kernel check (node Q05)

The load-bearing periodicity step is formalized in `formal/PeriodicResidue.lean`
(standalone Lean 4.14.0, no mathlib) and checks with exit 0:

- `residue_periodic`: `(k + L) % n = k % n` whenever `n > 0` and `n ∣ L` (depends only on `propext`);
- `clock_periodic`: `(k + n) % n = k % n` (`propext` only);
- `sum_periodic`: pointwise addition preserves period `L` (**axiom-free**).

Run: `lean formal/PeriodicResidue.lean`. Together the first and third give, by structural induction over a modulus family, `F(k + L) = F(k)` for the integer shadow of the clock combination — the exact hypothesis that makes the periodic-tail enclosure valid.
