# Main XXI integration-time receipts (2026-11-07)

These receipts were written **during integration**. They pay the receipt debts that the
audit of the incoming research PRs found. They do not edit the original dossiers, which
stay byte-identical. Each one is cross-referenced from
[`docs/CLAIM_SUPPLEMENT_MAIN_XXI.md`](../../../docs/CLAIM_SUPPLEMENT_MAIN_XXI.md) and from
[`docs/SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md`](../../../docs/SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md).

**π base-16 normality: OPEN. Selected Weyl gate `S_N(h)=o(N)`: OPEN. RH: OPEN.**

## R1 — #540 GA-09 countermodel (`ga09_countermodel.py`)

**Why it is here.** #540 `CLAIM_LEDGER.md` labels GA-09 as **REFUTED**. GA-09 is the
claim that "finite K=3 anti-clustering directly makes the golden aperture energy
`E_a→0`". The evidence listed for the label only shows that integrating the K-bound
directly fails. That is a failed proof route, not a refutation. Under
[`docs/METHOD.md`](../../../docs/METHOD.md) §receipt rule, a REFUTED label needs a
demonstrated counterexample.

**Countermodel.** Take `A` equally spaced points `jL/A` (`j<A`) filling an arc of
length `L=2/3`. This is a general point configuration, **not** the BBP source.

| Statement | Status | Route |
|---|---|---|
| `B_A(t) ≤ A+3A²t` for every `t∈[0,1/2]` and every `A≥1`. This covers #538 ET4-OPEN's range `[1/(A+1),1/2]` and #540 GA-03's range `[0,b]`. | PROVED LOCAL (elementary) | For `t<1/3` no pair wraps around the circle, so `B_A(t)=A+2DA−D(D+1)` with `D=⌊tA/L⌋`, and `3A²t≥3ADL=2AD`. For `t≥1/3`, `B_A≤A²`. |
| `max_t (B_A(t)−A)/(A²t) = 3−3/A` | CERTIFIED FINITE (exact) for `A∈{2,3,7,50,200,800}` | Exact jump-point enumeration at those `A`, plus a brute-force rational radius grid at `A=40`. For all other `A`, the bound `K≤3` is carried by the proof in the row above. |
| `E_a(μ_A)→E_a(ν_{2/3}) = √5/9 − 1/6 ≈ 0.0817853308 > 0` | PROVED LOCAL | `μ_A⇒ν_L` weakly and `k_gold` is continuous (#540 GA-02). The closed form comes from integrating against the triangular difference density. It matches exact `ℚ(√5)` pair sums at `A=50,200,800` (0.081981, 0.081798, 0.081786). |

**Conclusion.** A K-anticlustering bound, with no source structure, does not force Haar.
Any normality consequence of the #536/#538 finite `K≤3` certificates therefore has to use
the ×16 frequency-ray rigidity, exactly as #540 GA-03 states. The GA-09 label stands,
**with this receipt**. π normality stays OPEN.

- **Run:** `python research/2026-11-07/main_xxi_receipts/ga09_countermodel.py` (exits 0;
  JSON on stdout).
- **Test:** `tests/test_main_xxi_ga09_receipt.py`. It includes a Haar-like full-circle
  control, whose energy is `<10⁻³`, so the functional is not trivially bounded below.
- **Independence:** the receipt uses only `fractions` and `sympy`. It does not import
  #540 code.
