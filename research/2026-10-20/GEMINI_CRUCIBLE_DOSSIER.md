# Operation Gemini Crucible — hostile claim ledger (Deliverable A)

**Date:** 2026-10-20. **Branch:** `research/rigidity-forge-2026-10-20`.
**Subject:** the supplied Gemini manuscript *"From Local Structural Constraints to
Global Quantitative Rigidity in Observational SUCC: A Unified Ascent Calculus and
Five-Fold Obstruction Theory."*

**Source-availability note (honest).** The manuscript file (`math.md` /
`docs/LOCAL_TO_GLOBAL_RIGIDITY_THEORY.md`) was **not present** anywhere in the
research workspace (verified by an exhaustive filesystem search; the only hits were
the Gemini CLI config dir and SUCC's own pre-existing `*_rigidity.py` modules). Per
the operation's explicit instruction, this audit therefore works from the exact
claim descriptions and countermodels supplied in the brief (claims 1.1–1.8) and does
**not** pretend to have inspected the manuscript. Every verdict below is an **exact**
rational computation reproduced in `tests/test_gemini_crucible.py`
(`observational_succ/gemini_crucible.py`); no floating point enters any verdict.

**Governing outcome.** No synthetic universal theorem is promoted. The false
restricted-coercivity result (3.5) is **REFUTED**. The master identity (3.6) is
**NOT ADOPTED**. Salvageable ingredients are triaged with minimal correct
replacements.

---

## Verdict table

| id | object | status | one-line mechanism |
|----|--------|--------|--------------------|
| 1.1 | restricted Douglas–Schur transfer (Thm 3.5) | **REFUTED** | span(e₁) not D-invariant; true Schur = −62/19 < 0 |
| 1.2 | scalar Schur obstruction as negative witness | **MISLEADING** | failure of a *sufficient* test ≠ nonpositivity (24/25 > 0) |
| 1.3 | observer memory-debt transfer (Thm 3.2) | **REFUTED** | autonomy ⇏ unique lift; leakage hypothesis vacuous |
| 1.4 | strict TV contraction from kernel component | **REFUTED** | merge channel: TV 1/2 → 1/2 with nonzero ker component |
| 1.5 | primitive prime-clock probability | **REFUTED** | missing factor 3 (three slots); fails p=2 normalization |
| 1.6 | Σ Λ(n)n^{−1/2} = 2eᵃ+O(a²) "by PNT" | **MISCLASSIFIED** | equivalent to ψ(x)=x+O(√x log²x): RH-strength |
| 1.7 | float `is_globally_rigid` diagnostic | **REFUTED** | ignores D-positivity; A=(1),D=(−1),B=0 → false "rigid" |
| 1.8 | master identity + five obstructions (Thm 3.6) | **NOT ADOPTED** | no shared carrier; defects non-additive; a class missing |

---

## 1.1 Restricted Douglas–Schur transfer — **REFUTED**

**Gemini statement.** Coercivity restricted to the coupling subspace gives
`κ = ⟨D e₁, e₁⟩ = 1`, certifying `A − κ⁻¹ B B* = 1 > 0`, hence an inverse-response
positivity bound.

**Exact counterexample.** `A = (2)`, `B = (1, 0)`, `D = [[1, 9/10],[9/10, 1]]`.
- Gemini surrogate: `A − κ⁻¹ B B* = 2 − 1 = 1 > 0`.
- True Schur complement: `A − B D⁻¹ B* = 2 − 100/19 = −62/19 < 0`.
- Explicit negative vector of the full form: `v = (1; −D⁻¹Bᵀ·1) = (1; −100/19, 90/19)`,
  giving `vᵀ M v = −62/19 < 0`.

**Mechanism.** `span(e₁)` is **not invariant** under `D`, so the compression
`⟨D e₁, e₁⟩` is not a lower bound for the inverse response. The observed compression
of `D` is not a justified bound on `D⁻¹`.

**Minimal replacement.** Use the TRUE inverse response `A − B D⁻¹ B*` (exact); a
reducing subspace genuinely invariant under `D`; a direct inverse-response estimate
on `ran(B*)`; or the gapless Douglas factorization with its stated range/domain
(Part III §2.1–§2.2). **SUCC dependency:** `quantitative_rigidity.finite_schur_certificate`,
`coupling_negative_vector`. **Certificate:** `claim_1_1_restricted_coercivity`.

## 1.2 Sufficient certificate read as a necessary one — **MISLEADING**

`A=1, D=100, B=2, κ=1`: surrogate `A − κ⁻¹BB* = −3 < 0`, yet true Schur
`A − BD⁻¹B* = 1 − 4/100 = 24/25 > 0`. The surrogate is only a **sufficient** lower
certificate (valid when `D ⪰ κI`); its failure is **not** a negative witness.
**Replacement:** a negative witness is a vector `v` with `vᵀMv < 0`, equivalently the
TRUE Schur complement being non-PSD.

## 1.3 Observer memory-debt — **REFUTED** (two independent failures)

(a) **Lift non-uniqueness.** Two-state source `{s₀,s₁}` both observed as `o`, with
identical report/actions/costs/quotient-successor. The quotient transition is
autonomous, yet an observed history `o,o,o` has `2³ = 8` source lifts. Autonomy of
the quotient does **not** yield a unique source lift. Five notions must be kept
distinct: (i) existence of a quotient transition, (ii) autonomy on the quotient,
(iii) existence of a source lift, (iv) uniqueness of a source lift, (v) original-source
realization.

(b) **Vacuous leakage hypothesis.** For `E ⪰ γI` and any proper orthogonal
projection `P`, a unit vector `u ∈ ran(I−P)` gives `‖(I−P)E(I−P)‖ ≥ ⟨Eu,u⟩ ≥ γ`.
So `‖(I−P)E(I−P)‖ < γ` is unsatisfiable — vacuous for every nontrivial observer.
**Replacement:** preserve as a NO-GO, or require genuine leakage strictly inside a
gapped subspace (which a proper observer projection does not provide).

## 1.4 Data-processing strict contraction — **REFUTED**

Deterministic merge `C(x₁,x₂,x₃) = (x₁+x₂, x₃)`. `p = (2/5, 1/10, 1/2)`,
`q = (0,0,1)`: `TV(p,q) = TV(Cp,Cq) = 1/2`, although `p−q` has component `3/10`
along `ker C = span((1,−1,0))`. **Correct criterion.**
`TV(Cp, Cq) = Σ_y |Σ_{x ∈ fiber(y)} (p−q)(x)|`; strict contraction holds **iff** some
output fiber carries both signs of `p−q` (sign cancellation within that fiber).
Classical stochastic channels vs. quantum CPTP maps must be separated (this is the
classical fiber-cancellation statement). A positive control where the fiber *does*
cancel (`p=(3/4,0,1/4)`, `q=(0,3/4,1/4)` → `TV` 3/4 → 0) is in the tests.

## 1.5 Primitive prime-clock probability — **REFUTED** (missing factor 3)

**Corrected law (derived, not assumed):**
`Pr(v_p(abc) = k | primitive a+b=c) = 3(p−1)/((p+1) p^k)`, `k ≥ 1`.

**Derivation (conditional-Haar model).** Under independent Haar `a, b ∈ ℤ_p`
(`c = a+b`), primitivity `E` = not `p | gcd(a,b,c)`. If `v_p(a), v_p(b) ≥ 1` then
`v_p(c) ≥ 1`, violating `E`; so under `E` at most one slot has positive valuation.
Hence `v_p(abc) = k ≥ 1` means exactly one of `a,b,c` has `v_p = k` and the others
`0`; by the `a+b−c=0` symmetry there are **three** such slots:
`Pr(·) = 3 · [(p−1)/p^{k+1}]·[(p−1)/p] ÷ (1 − 1/p²) = 3(p−1)/((p+1)p^k)`.
**Normalization check.** `Σ_{k≥1} = 3/(p+1)`, which at `p = 2` equals `1` — matching
"every primitive triple has exactly one even entry among `a,b,c`." Gemini's version
omits the factor 3, sums to `1/(p+1)` (`1/3` at `p=2`), and fails this check.
**Firewall note.** This is a LOCAL per-triple law; it must **not** be transported
into a one-variable integer average or a bounded-box joint law without a separate
argument. The existing `ABC-CLK-02` Dirichlet-convolution derivation is preserved.
The local `ris` moment `E[∏ p^{t(v−1)} | E]` converges iff `t < 1` (exact,
`ris_local_moment`).

## 1.6 Prime-weight asymptotic — **MISCLASSIFIED** (RH-strength, not PNT)

`Σ_{n ≤ e^{2a}} Λ(n) n^{−1/2} = 2eᵃ + O(a²)`. With `x = e^{2a}` the error is
`O(log² x)`. By Abel summation this is equivalent to `ψ(x) = x + O(√x · log² x)`, an
**RH-strength** error term. PNT only yields `ψ(x) = x + o(x)`, hence the weighted sum
`2√x + o(√x)` — never `O(log² x)`. The claim is therefore RH-level
(CONJECTURED/open), not a classical PNT consequence. Distinguish: arithmetic weight
sums, operator-norm upper bounds, operator-norm asymptotics, and signed cancellation
in the Weil form. Also: the window threshold `2a = log n` is a measure-zero
support-intersection point for `L²` zero-extension shifts.

## 1.7 Float `is_globally_rigid` — **REFUTED**

On `A=(1), D=(−1), B=0` a diagnostic that checks only the pseudo-Schur complement
`A − B D⁺ B* = 1 > 0` declares global rigidity, but `M = diag(1,−1)` has a negative
high direction `e₂`. The missing check is **D-positivity** (`D > 0`, or `D ⪰ 0` with
`ran(B*) ⊆ ran(D)`). No float tolerance turns "no finite counterexample found" into a
global certificate. **Replacement:** `quantitative_rigidity.finite_schur_certificate`
checks the high block AND the TRUE complement, exactly.

## 1.8 Master identity + five obstruction classes — **NOT ADOPTED**

No shared quadratic form / common carrier is derived, so the memory-debt, cocycle,
and arithmetic-cumulant terms are not known to share units, functional type, sign, or
a source-derived map; and the inverse response is **quadratic** in the coupling, so
defects are **not additive** once sources interact (exact example:
coupled true defect ≠ naive sum of one-at-a-time defects). Independence and
exhaustiveness of the five classes are unproven, and at least one class is missing:
**vanishing uniform coercivity** `D = diag(1, 1/2, 1/3, …)` — every finite principal
block is strictly coercive, yet no uniform gap `κI` survives.

**Per-term test a legitimate defect must pass** (none is assumed): common carrier;
correct units; correct functional type; a source-derived map into the target form; a
valid sign; a justified decomposition; no duplicated contribution; a convergence
theorem when infinite. **Replacement:** keep the five classes as a *diagnostic
taxonomy only*, and use the per-term transport theorems of Part III (finite Schur,
shorted complement, form-core transport) in place of the master identity.

---

## Validation certificate

`PYTHONPATH=. python -m unittest tests.test_gemini_crucible` → **13 tests OK**. Every
witness above is recomputed in exact rational / symbolic arithmetic. The refutations
share the exact Schur machinery of `observational_succ/quantitative_rigidity.py`
(Part III), so the negative audit and the positive theory are one code path.
