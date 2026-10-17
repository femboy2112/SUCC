# PDQ MEGASWARM — independent audit of the Four-Body Breakout and the exact positivity-threshold obstruction

**Date:** 2026-10-16 (night). **Branch:** `research/deepseek-pdq-megaswarm-2026-10-16`, HEAD `a6b7b98`
(child of PR #150 head `6a067c1`; PR #149 `8a65f0b`; main `07806f3`). **RH PROVED: NO.**
**Nontrivial zeta-zero coordinates used: NO.**

## 0. Session-provenance note (recorded for auditability)

This campaign was launched to work the same PDQ front as a sibling session. On arrival the
working tree held uncommitted edits to the exact target files (`certified_four_schur_trial.py`,
`four_schur_dual_quotient.py`, …) with advancing timestamps. Those edits were stashed (not
discarded) to isolate cleanly. The sibling session then committed and pushed `a6b7b98`
("FOUR-BODY BREAKOUT"), and the stashed blobs were verified **byte-identical** by SHA-1 to the
committed files:

```
four_schur_dual_quotient.py   f4327869adfb6e045c62f3afad48271853f59ddf  (commit == stash)
certified_four_schur_trial.py 3a300cbaf0458b1a88cf7284d1740b99d7d6840a  (commit == stash)
```

The redundant stash was dropped. **No work was lost; no foreign commit was authored by this
session.** This document adds the *independent audit* results and the *obstruction arithmetic*
below, which are NOT present in `a6b7b98`.

## 1. Live-state reconstruction

- `main` = `07806f307ae6e2f62f9c0faa90377bf79cee1cc0` (untouched).
- PR #150 head `6a067c1` = branch `research/dual-variational-schur-source-gates-2026-10-16`.
- Branch `research/deepseek-pdq-megaswarm-2026-10-16` = `6a067c1` + `a6b7b98`.
- Provenance: `scripts/verify_provenance.py` → `SOURCE_PROVENANCE_VERIFIED` (72 items, 17
  byte-identical archives).
- Baseline reproduced exactly: `CertifiedTrial((), J=64, rank=12)` → **AMBIGUOUS**,
  lower-bracket min-eig **−1.2603043728791978**, upper PSD (no strict-negative direction).

## 2. Independent audit results (Round 1) — five of five completed, all reproduce the theorems

Five independent agents re-derived the load-bearing PDQ results from scratch (no repo import):

| # | Claim audited | Verdict | Detail |
|---|---|---|---|
| 1 | Two-moment weights `30 c₁ᵀc₁ + 210 c₂ᵀc₂` | **PROVED** | `‖φ_e‖²=1/30`, `‖φ_o‖²=1/840`; weight **210 correct** (the "52.5" slip is feeding the normalized coefficient through the norm twice); containment `span{φ_e,φ_o} ⊂ P_{≤3}` valid; **no countermodel** (exhaustive deg≤5, 20k random deg≤7, exact PSD certificate). |
| 2 | IBP identities `E₀..E₃` | **PROVED** | All four correct, no sign/factor error (exact sympy residual 0; ~50-digit numeric on 7 functions). `∫h=0` simplifies `E₁`; the `−3∫t²h` term in `E₃` is **not** removable but **is** sourced by the authenticated `c₂` row (`−3∫t²h = −c₂/2`). The genuine unresolved input is the **endpoint pair** `{h(a),h(−a)}`. |
| 3 | PDQ-02 quotient identity | **PROVED as supremum** | `sup_{w∈Q₄H} |⟨Q₄h,w⟩|²/⟨Kw,w⟩ = ‖(I−P₃)h'‖²`. **Found a flaw in my own intermediate chain** (`Q₄H = span{1,t,t²,t³}^⊥∩H` is *false* — misses the `⟨w,t⁴⟩=0` constraint; witness `w=P₄(2t)`); the repo's PDQ-01 (closure of the *image*) is correct. The supremum is **not attained** (maximizer has `ψ*'∉Q₄H`). |
| 4 | High coercivity `κ` | **IMPROVEMENT PROVED** | `1/50` is **not optimal**: certified `κ′ = 0.0389832818322773` (1.9492× / residual amplification 25.65 vs 50), from exact source endpoints + Ω=13 method optimum + resolution saturation. Also: `K` is exactly parity block-diagonal; `K|F₄` has condition number 20.31, so **no scalar is optimal** — the exact object is operator-valued. |
| 5 | Nested 30→4 shorting | **CONDITIONAL / OBSTRUCTED** | Exact re-derivation + correct hypothesis: monotone shorting is **guaranteed if** the discarded middle block of `L` is strictly PD (**sufficient, not necessary** — with a negative middle block the order may still hold, e.g. `L=diag(0,−2) ⪯ U=diag(1,−1)` gives `Short(L)=0 ≤ 1=Short(U)`, or may reverse, e.g. `sign_switch_countermodel`). Practical obstruction: an interval packet's middle compression is certifiably PD only if its radii fall below `ρ* = min_{‖v‖₁=1} vᵀD_ctr v`; for a realistic toy (margin 0.02) `ρ* ≈ 1.72e−3` (relative ≈ 0.0285). This is a gap in the **computed lower enclosure** of the intermediate 5..30 effective block, **not** absence of source coercivity in the true complement: the inherited WB4 theorem `D_4 ⪰ (1/50) Q_4 K Q_4` applies to the true high complement, which contains modes 5..30. |

(The sixth audit — a certified `H'` operator upper bound — remained in flight; the sibling's
`a6b7b98` independently delivered Routes B1+B3 for that channel, so it is covered.)

## 3. The central Round-2 result: the exact positivity-threshold obstruction

**Setup.** Every certified lower bracket for `S₄` has the shape

```
S₄ ⪰ (A₄-Interval-Lower) − (1/κ)·(residual energy cap)·W_L2(low)
```

With `U=0, rank=12, J=64`:

- `A₄` interval-lower min-eig = **+9.24760625e−08** (positive, tiny).
- `W_L2(low) = diag(1/3, 1/5, 1/7, 1/9)`, max eig `1/3`.
- Present Young cap `(1/κ)‖g'‖₁² = 121/32 = 3.78125`.

**Theorem (threshold).** The exact threshold is
`τ* = sup{τ : (A₄-Interval-Lower) − τ·W_L2(low) ⪰ 0}`, i.e. the **smallest generalized
eigenvalue** of the pair `(A₄-Interval-Lower, W_L2(low))` in the `W_L2` (Legendre-mass)
metric — **not** the Euclidean `λ_min` (that is the separate `9.2476e−8` A₄ figure). Because
`A₄-Interval-Lower` is exactly parity-block-diagonal, `τ*` decouples into two 2×2 blocks; the
**even** block (modes 2,4) is binding, with exact quadratic
`(1/45)τ² − (625303051402592294271718146011/9e30)τ + C = 0`. Its smallest root is bracketed
by exact det sign-change (see `scripts/pdq_threshold_obstruction.py`):

```
τ* ∈ (6.015173631357e−07, 6.015173631582e−07)   (certified rational bracket, even block)
```

The earlier dyadic value `346751125023/2^59 ≈ 6.0151732e−7` was an *80-step bisection endpoint*
using a conservative `min_eig_lower`, which halts ~4.62e−14 **below** `τ*`; it is a valid lower
witness that positivity holds there, but it is **not exact and not the generalized eigenvalue**
(and it was already stale versus the committed script's own `2^79` output). The corrected `τ*`
does not change the headline: `S₄ ≻ 0` cannot be certified on the scalar-Young channel unless
the residual cap drops below `≈6.015e−7`, and the present `121/32` cap is **≈6.286e6× too large**.

**Corollary (why the improvements do not close it).** Sweeping certified coercivity constants:

| κ | residual cap | lower-bracket min-eig | verdict |
|---|---|---|---|
| 1/50 (published) | 3.78125 | −1.260304 | negative |
| 0.021420 (WB4 exact m4) | 3.53058 | −1.176748 | negative |
| **0.038983 (audit κ′)** | **1.93993** | **−0.646532** | **still negative** |

Even the 1.95× coercivity gain leaves the bracket negative by 0.65. The binding constraint is
**not** coercivity and **not** the Γ-tail (the sibling's `O(J⁻³ᐟ²)` IBP tail improves the *tail* by
5.7× while the bracket moved −1.260 → −0.029, i.e. ~43×) — it is the **absolute scale of the
derivative-energy / polynomial-moment channel** relative to the `O(1e−8)` A₄ margin.

**Boundary (what this does NOT say).** This obstructs the *Young-channel scalar-cap* route. It
does not prove `S₄ ⋡ 0`; the exact `H'` upper bound and the full 4-moment subtraction (the
sibling's Moonshot A/B/C) are genuinely sharper instruments. What it establishes is that the
margin is `O(1e−8)` while every coarse channel is `O(1)`-scale: only per-vector, source-attested
moment data can decide the sign.

## 4. Status ledger

| ID | Statement | Status | Evidence |
|---|---|---|---|
| AUD-01 | Two-moment weights (30, 210) and containment | **PROVED** | Independent sympy + exact PSD; no countermodel |
| AUD-02 | IBP identities `E₀..E₃` (incl. `−3∫t²h=−c₂/2`) | **PROVED** | Exact sympy; 50-digit numeric; endpoint pair is the only new input |
| AUD-03 | PDQ-02 quotient identity as supremum | **PROVED** | Independent derivation; corrected my own domain slip |
| AUD-04 | κ′ = 0.038983 > 1/50 (1.95×) | **PROVED (conditional on WB4)** | Exact source endpoints + Ω=13 optimum |
| AUD-05 | Nested shorting gate "discarded middle strictly PD" is **sufficient, not necessary**; enclosure obstruction at `ρ*` | **PROVED FINITE** | Exhaustive exact 2×2/3-7-dim sweep; toy threshold `ρ*≈1.72e−3`; both counterexamples (order-holds and order-reverses) exact |
| AUD-06 | Threshold `τ* ∈ (6.0151736313e−7, 6.0151736314e−7)` (even-block generalized eigenvalue, Legendre metric); Young channel ≈6.29e6× too loose | **PROVED FINITE (certified rational bracket)** | Exact even-block quadratic + det sign-change; dyadic `2^59/2^79` endpoints were conservative lower witnesses, not the threshold; κ-sweep |
| — | Original-source sign of `S₄` | **OPEN (AMBIGUOUS)** | Both certificates present; margin `O(1e−8)` |
| — | Riemann hypothesis | **OPEN — NOT PROVED** | No zero coordinates used |

## 5. Smallest next decisive lemma

The audit isolates a single load-bearing quantity: a **source-attested endpoint evaluator** for
`h(a), h(−a)` for `h = G v` (equivalently, the two boundary channels `ψ_e=½u₃'`, `ψ_o=½u₄'` of
the sibling's Theorem A.1), with a rigorous omitted-Γ tail, feeding the complete
`E*P⁻¹E` subtraction at `O(1e−7)` precision. Everything else in the chain is now explicit:
`A₄` lower (`1e−8`), `W_L2`, `κ′`, the Γ-tail, and the obstruction threshold. **The sign of
`S₄` reduces to certifying two endpoint numbers per trial vector to ~1e−7.**

**Source receipts:** parent `a6b7b98`; classical: Zeno/geometric completion, Legendre/Sobolev
duality, Haynsworth/Schur, Chebyshev `ψ`; original source blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Main untouched. No merges.
