# SUCC Academic Main II — Research Dependency Graph (2026-10-16)

Machine-readable companion: [`SUCC_ACADEMIC_MAIN_II_MERGE_COVERAGE.json`](SUCC_ACADEMIC_MAIN_II_MERGE_COVERAGE.json).
Prior layer: [`SUCC_RESEARCH_DEPENDENCY_DAG.md`](SUCC_RESEARCH_DEPENDENCY_DAG.md) (Academic Main, 2026-10-15).

This graph is reconstructed from **actual Git ancestry** (`git merge-base --is-ancestor`), not PR base
labels or titles. Pre-merge `main` anchor: `02fc9f4` (Academic Main I). Integration head: `325309b`.

**RH PROVED: NO.** The Riemann hypothesis remains open. Nothing below constructs the signed completed
Weil form or certifies the sign of the first-window Schur complement `S_4 = A_4 - R_4`.

## Three families, four terminal tips

The 15 open PRs #133–#147 are three strictly-stacked Git chains. Four terminal tips cover all 15
(each listed PR head is a verified ancestor of `325309b`):

### Family A — proof machinery & arithmetic Schur  (tips #138, #137)

```text
#133 YEAN proof kernels (0f86ba2)
  └─ #134 proof-producing carrier bridges (5d6d717)
       └─ #135 Observer Schur (24d0f18a)          ← merge-base(#137,#138)
            ├─ #136 unit/prime SUCC (53c53e9)
            │    └─ #138 canonical Tate log clocks (7705897) ── TIP
            └─ #137 arithmetic resonance / Schur (95dbf40) ──── TIP
```

`#137` and `#138` **diverge** at `#135` and neither contains the other; both tips are required. The
integration merges `#138` first, then `#137` (its additive doc changes auto-merged).

### Family B — source-indexed observer computation  (tip #144)

```text
#139 SUCC-λ observation calculus (f4f3d83)
  └─ #140 E-ladder consensus (940f089)            ← historical red: KeyError 'kind'
       └─ #143 collective observers (f7cc849)      ← repairs #140, adds regression
            └─ #144 cofinal Schur telescope (dc497bc) ── TIP
```

### Family C — Gamma / factorial / FUCC / signed Weil  (tip #147)

```text
#141 Dirac-comb Gamma continuum (849b241)
  └─ #142 band-uniform Gamma de-aliasing (6623fd1)
       └─ #145 factorial-Gamma SUCC×FUCC (b8e147d)
            └─ #146 prime-FUCC Tate–Mellin transport (d7545a1)
                 └─ #147 certified signed Weil splines (8bfc4a7) ── TIP
```

## Source-proof dependencies (what each family imports, and from where)

| Family | Imports (dependency) | Status of the import | Repository anchor |
|---|---|---|---|
| A | Finite-Haar → profinite-Hilbert completion chain | PROVED LOCAL (density + uniform bound premises explicit) | `CLAIM_SUPPLEMENT_PROOF_TEETH.md`, `test_profinite_hilbert.py` |
| A | WB4 four-low positivity `A_4 > 0` at `a=1/2`, `D_4 ⪰ (1/50)Q_4 K Q_4` | PROVED LOCAL (Academic Main I, parent WB4) | `source_weil_hierarchy.py`, weighted-Bessel-four supplement |
| A | YEAN Lean kernels (affine two-point, rational cyclic retract) | EXTERNAL CLAIM (recorded kernel receipts; **not** rebuilt as RH proof) | `research/2026-10-16/observer_schur_receipts/` |
| A (#137) | Inherited high coercivity `D ⪰ κ K` and derivative tail | CONDITIONAL import (premise, not re-proved) | `CLAIM_SUPPLEMENT_ARITHMETIC_RESONANCE.md` |
| A (#138) | Tate/Poisson all-test theorem; completed-ζ pole residues `(−1, +1)` | CLASSICAL / EXTERNAL THEOREM | `unit_prime_tate_bridge.py`, `tate_idelic_zeta.py` |
| B (#144) | Conditional cofinal effective-approximation theorem | CONDITIONAL (oracle **not** implemented; **not** an RH decision procedure) | `cofinal_schur_telescope.py`, `COFINAL_SCHUR_TELESCOPE.md` |
| B (#143) | Dual-port receipt schema (repairs #140) | PROVED LOCAL / TESTED MODEL + regression | `consensus_lambda.py` |
| C (#141/#142) | `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` via Dirac-comb sampling + de-aliasing | VERIFIED EXACT MODEL (finite-source error budget) | `gamma_dirac_continuum_probe.py`, `gamma_band_dealias` |
| C (#145) | Positive factorial moments → Gamma source reconstruction | VERIFIED EXACT MODEL | `factorial_gamma_fucc`, `CLAIM_SUPPLEMENT_FACTORIAL_GAMMA_FUCC.md` |
| C (#146/#147) | True `Λ(p^k)=log p`, half-density `n^{−1/2}`, prime-active signed spline | VERIFIED EXACT MODEL + hostile controls | `prime_active_weil_spline`, `tate_mellin_prime_transport` |

## Cross-family shared assumptions (NOT independent bearings)

Per the Aletheia common-provenance rule, the following are **shared source** and must not be counted
as independent corroborations:

- All three families ride **one** canonical arithmetic source (Suzuki `arXiv:2606.09096v3`, `Q(ζ)`
  prime powers). Family A, B, and C computations of overlapping quantities are the **same source**
  seen through different decompositions — not independent witnesses.
- The Beta-coordinate and exponential order-statistic Gamma models (#145) are **two descriptions of
  one probability law**, not two sources.
- `#137`'s high-response bounds and `#144`'s telescope both inherit the **inverse-Neumann metric `K`**;
  neither supplies a spectral gap `κ I`.

## The RH-hard object (unchanged, OPEN)

```text
S_4 = A_4 − R_4            (first-window four-mode Schur complement)
```

Available within stated source hypotheses: positive original `A_4`; high-sector coercivity relative to
`K`; two-sided brackets `A_4 − L_U − 50 T_{r_U} ⪯ S_4 ⪯ A_4 − L_U`. **Missing:** an authenticated
high-response approximation whose certified error is strong enough to **determine the sign** of `S_4`.
See [`SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md`](SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md) and the
next-campaign plan `research/2026-10-16/SUCC_FUCC_TATE_WEIL_NEXT_CAMPAIGN.md`.
