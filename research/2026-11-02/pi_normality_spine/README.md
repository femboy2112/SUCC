# π-Normality Reduction Spine — a tractability package

**Branch:** `research/pi-normality-framework-spine-2026-11-02`.

This package consolidates the base-16 π-normality reduction into a single, verified,
dependency-explicit spine. Its purpose is **tractability**: instead of another frontal
assault on the gate, it builds the scaffolding that lets any future proof-front know
(a) exactly what is proved, (b) exactly what the single remaining lemma is, and (c) exactly
what a proof of it would consume and yield.

## Contents

| File | Role |
|---|---|
| [`REDUCTION_SPINE.md`](REDUCTION_SPINE.md) | The equivalence chain (A)⟺(B)⟺(C)⟺(D), every link proved and pinned, the single open lemma (RL) named with full quantifiers, and the firewalls that keep the reduction exact. |
| [`arithmetic_core.py`](arithmetic_core.py) | Single source of truth for the exact arithmetic primitives (`r`, `U_n`, `T_n`, `W_{p,j}`, `a_{p,j}`, `κ`, `Q_{m,N}`, `ord_p(16)`). Pure `Fraction`, no float. |
| [`test_arithmetic_core.py`](test_arithmetic_core.py) | 19 exhaustive cross-check tests, each primitive verified against an independent representation (BBP identity, carry recurrence, Midy, de Bruijn, sampling floor). |
| [`ReductionSpine.lean`](ReductionSpine.lean) | Lean 4 kernel core (no Mathlib, **0 sorry/admit/axiom**) for the finite combinatorial facts: collision-energy nonnegativity and the de Bruijn balanced-witness firewall shape. |
| [`dependency_graph.json`](dependency_graph.json) | The tractability map: every proved π-claim (CTC/SPP/CG/PCN/PWI/…), its status, and its edges, with the single sink = the open lemma (RL). |

## The single remaining lemma (the summit)

> **(RL)** For `U_0=0, U_{n+1}=16U_n+r(n+1)`, prove `|Σ_{n≤N} e^{2πi h U_n}| = O(N^θ)`, `θ<1`,
> for every fixed `h≠0` — equivalently `sup_{1≤|h|≤16^{m-1}} |S_N^U(h)|=O(N^θ)`, `m=⌊log₁₆N/3⌋`.

**Proving (RL) ⇒ base-16 normality of π. Refuting (RL) ⇒ π base-16 non-normal.** The spine is
exhaustive; there is no third outcome.

## How to use this package (for a future proof-front)

1. **Import, don't re-derive.** `from arithmetic_core import r, U, T, W_pj, a_pj, kappa, Q_mN`.
   Every primitive is exact and cross-checked; do not re-verify the four-pole source.
2. **Read the firewalls first** (REDUCTION_SPINE.md §2). They list the proved negative results
   (counterseed, Galois trace, Stoneham, prime-window universality, Parseval bookkeeping) so you
   do not waste a round re-attacking a closed door.
3. **Target (RL) only.** The dependency graph shows the single sink. Any new bound must be a
   *signed* estimate on `Σ e(hU_n)` using the proved arithmetic (conductor `exp(6n)`, prime-birth
   clock, carry, cyclotomic law, `μ(π)<15/2`), and must kill the coherent counterseed `s=−π/16`.

## Verification

```bash
# arithmetic core self-check
python research/2026-11-02/pi_normality_spine/arithmetic_core.py
# exhaustive cross-check (19 tests; run from the spine dir)
cd research/2026-11-02/pi_normality_spine && python -m unittest test_arithmetic_core -v
# Lean kernel core (0 sorry, no Mathlib)
lean research/2026-11-02/pi_normality_spine/ReductionSpine.lean
```

## Status

The spine is **complete and exact**. The analytic links (Weyl criterion, Green-tail ℓ¹ transport
`ΣT_t ≤ 17/648`, PNT-in-AP) are paper-proved with sources pinned; the finite combinatorial links
are Lean-checked; the arithmetic core is exhaustively cross-checked. **π base-16 normality and
RH remain OPEN.**
