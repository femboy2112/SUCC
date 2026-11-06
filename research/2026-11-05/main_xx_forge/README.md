# Operation Main XX — history-first π proof forge (2026-11-05)

**Research only. π base-16 normality: OPEN. Selected signed Weyl gate `S_N(h)=o(N)`: OPEN. RH: OPEN.**

This round is an additive descendant of PR #522 (`cd672158`, which includes the #521 precision repair). The original four signed poles, the literal `U_0=0`, every frozen contract, and every `formal/` Lean file are untouched.

Three proof fronts attacked the bridge that #522's NEXT.md asked for: from source- and history-faithful identities to a signed estimate for the **one** realized orbit.

**Main finding.** All three fronts converge on the same thing. Every source, carry, prime-Frobenius, mixed angular–radial or Clausen observable tried here is exactly a functional of the completed ×16 orbit of the single number `α=s+π/16`. The deterministic, seed-independent Green tail `T_n` enters only as smooth endpoints. So the realized-orbit problem *is* the `{16^jπ}` problem.

**What a source route can and cannot supply.** The carry gate becomes a normality certificate exactly when paired with a **stationarity** input. Without such an input it provably fails on a non-normal seed with the same forcing.

## Fronts

| Front | Dossier | Strongest rigorous result | Decisive failure (with receipt) |
|---|---|---|---|
| **B: critical carry, shell information, transport** | [front_b/](front_b/PROOFS.md) | **CB-1:** `b_{n,m,k}=1[S_m(n+k)≤x_{n+d}<S_d(n)]` exactly. **CB-2/2′:** frequency existence (or log-scale stationarity) plus lattice smallness of `J` ⟹ Haar, by Mellin periodicity and a monotone squeeze. **CB-0:** admissible ⟺ `A≥2^{2d−3}`, certified for `d≤200`. | **CB-3:** a non-normal seed with the same forcing has `sup|J|→0` on every admissible triple. "J-family ⟹ normality" is refuted as an unconditional transport. |
| **A: Clausen energy / source arithmetic** | [front_a/](front_a/PROOFS.md) | **FA-1:** `P_{A,2A,r}=-Q_r(μ_A)+O(1/A)` exactly, so #520's open finite-cut inequality *is* fixed-h Weyl (FA-2). **FA-3:** a ×b-invariant measure that dominates Lebesgue on any open arc is Haar. **FA-5:** a seed-uniform compactness factorization. | **FL:** "Clausen energy ≤ C·carries" is refuted by CB-3. **FL-1:** the one-sided shell variant is refuted by stochastically-smaller Bernoulli digits. |
| **C: angular/radial, prime-Frobenius, collisions** | [front_c/](front_c/PROOFS.md) | **Partial-summation duality:** `sup_{V(a)≤1}|Σa_ne(hU_n)|=\max_L|S_L|` exactly. **Character–period dictionary:** the χ₋₄ source component lives in `⟨π,\arctan(1/2)⟩`; the period-map kernel is the one classical zero relation. **Pair budgets:** a mesoscopic budget ⟺ normality. | Mixed angular–radial saving, χ₋₄ orientation as a normality lever, and "microscopic exclusion ⟹ normality" are each refuted with a receipt. One preregistered observational band failed (0.11095 > 0.11) and is reported, not refit. |

The shared infrastructure for future rounds is [`observational_succ/selected_orbit.py`](../../../observational_succ/selected_orbit.py). It provides exact states for rational seeds, `S_k`, Lean-backed `T_n` enclosures, the definition and CB-1 forms of the carry bit, `J`, `c_A(h)` at locally scoped precision, admissibility, and a status-checked receipt writer.

## Hostile crucible

- Front B's proofs went to two blind same-model reviewers ([front_b/hostile_review/REVIEW.md](front_b/hostile_review/REVIEW.md)).
  - The rigor audit (BLOCK-narrow) found gaps; all are repaired.
  - The refuter could not break CB-1 (3.76M adversarial exact checks), CB-2, CB-3 or CB-4. It killed two secondary statements: an extension claim for CT-03 and a defective witness. Both corrections are recorded.
- Fronts A and C each audited CB-1 to CB-4 independently and found no error.
  - Front A notes CB-2 needs only `k=1` and `c∈(0,c_*)`, by invariance plus FA-3.
- Front C re-verified CB-1 on 39,680 cases.
- Front B's numerics re-verified CB-1 on 591,175 cases and CB-1g on 118,235 cases with two independent oracles.
- These are same-model reviews. **They are not independent scholarly referees.**

## The precise next falsifiable inequality

CB-4/FA-5 factor the gate into two strictly weaker conjuncts, and each control fails exactly one of them:

| | log-scale stationarity (LS) | lattice uniformity (H2\*) |
|---|---|---|
| zero seed | **OPEN** | **OPEN** |
| coherent `s_*=−π/16` | holds | fails |
| CB-3 calibrated seed | fails | holds |
| non-uniform Bernoulli generic point | holds | fails |
| Haar-seed ensemble | holds a.e. | holds a.e. |

**Next inequality (LS for the zero seed):**

\[
Λ_A=\sup_{1\le a<b\le8,\ b-a\ge1/4}\sup_t|μ_{[aA,bA)}([0,t))-μ_{[A,2A)}([0,t))|\to0.
\]

Every proof must fail on CB-3 seeds, which share the forcing. So it must use a seed-selective input, such as exact zero-seed rationality, beyond forcing.

## Next moonshot: three experiments, ranked by how sharply they separate genuine zero-seed cancellation from coherent wrong-seed and virtual-ensemble effects

1. **Two-factor gate probe** (Front B NEXT §1, Front A NEXT §1). Measure `Λ_A` and `\sup|J|` jointly on the zero seed (exact rationals), the coherent seed, CB-3 seeds, non-uniform Bernoulli points and Haar seeds, for `A` up to `2^{16}`. Preregister the epochs.
   - **Why it ranks first:** it is a complete 2×2 factorial in which every control's cell is known in advance. A virtual-ensemble effect cannot fake it, because the ensemble satisfies both factors and is not the selected seed.
2. **Second-order calibration test** (Front B NEXT §2, CB-5/CB-6). Build the `q=2` Markov lattice-calibrated countermodel. Then decide whether second-order selected carry statistics `J2` can be silenced without stationarity, as the hierarchy conjecture predicts, or whether there is an obstruction.
   - **Why it ranks second:** CB-5 already shows `J2` separates CB-3 in exact expectation at `≈1.44e-5`. That is the first carry-family signal that first-order calibration cannot hide.
3. **Lag-resolved Poisson-scale pair budget** `Π_A(s)≤Cs` (Front C NEXT).
   - **Why it ranks third:** it is an exact equivalent of normality with a rate. Coherent and short-period completions fail it grossly, but a 15-symbol non-normal orbit fails only like `(A/s)^{0.023}`. It discriminates sharply against coherent effects and weakly against low-entropy-defect alternatives.

## Not done, and not claimed

- No unconditional source-selected estimate was proved.
- No status was promoted.
- No Lean authority is asserted for anything new.
- Finite receipts are OBSERVED-FINITE or CERTIFIED-FINITE only.
