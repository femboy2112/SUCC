# PROOF MECHANISMS — a transductive catalogue

**Date:** 2026-10-23. **Status:** methodology. Not a claim about any open problem.
Companion to `research/2026-10-23/CYC03_LANE_CLOSED.md`.

> A **proof mechanism** is a reusable *transducer*: a shape that consumes a
> specific kind of input and emits a specific kind of theorem, with a specific
> ceiling. Naming the ceiling is as important as naming the mechanism — most
> wasted effort in this repository has been applying a mechanism outside the
> class where it can produce anything.

Each entry: **form · produces · hypotheses · ceiling · instance**.

## 0. The taxonomy (input → output → ceiling)

| # | Mechanism | Consumes | Emits | Hard ceiling |
|---|---|---|---|---|
| M1 | Conditional criterion | an implication + a checkable premise | "Target ⟸ Premise" | cannot prove the premise |
| M2 | Exact countermodel | a universal claim + a member | refutation with witness | never positive |
| M3 | Noncommuting limits | a doubly-indexed family | a located defect | cannot choose the right order |
| M4 | Cohomological obstruction | a forcing + a multiplier | non-existence of a telescoping | silent on rates |
| M5 | Soundness by refusal | a bound family | a bound that cannot lie | may be too weak to decide |
| M6 | Orthogonal channel decomposition | a space + a form | exact weighted rank-one sum | needs exact Grams |
| M7 | Constant sharpening | a published envelope + source data | a strictly better constant | may not change the verdict |
| M8 | Threshold arithmetic | a free parameter + a conclusion | the exact flip value | only localises, never crosses |
| M9 | Two-instrument check | one quantity | calibrated agreement | never a proof |
| M10 | Kernel-checked finite kernel | a finite algebraic lemma | certified lemma | never an infinite analytic theorem |

## 1. M1 — Conditional criterion + gap closure

**Form.** Exhibit `Target ⟸ Premise` where Premise is a checkable property of an
explicit family; prove the implication; then declare the residual gap.
**Produces.** A theorem plus a *named* open obligation.
**Hypotheses.** (a) implication proved, not observed; (b) Premise not equivalent
to Target (else tautology); (c) Premise not trivially stronger (else vacuous).
**Ceiling.** Cannot prove Premise. Cannot detect that Premise ≡ Target without a
separate argument.
**Instance.** CYC-01′: normality ⟸ carry-sum → 0, where the carry sum is
observable. The value is that it *relocates* the open content to a place where
one can at least measure. The danger is exactly the trap this repo fell into:
a criterion that is generic (holds for every x) cannot discriminate π.

## 2. M2 — Exact countermodel as the theorem

**Form.** To refute `∀q ∈ C : Q(q)`, exhibit `q ∈ C` and prove `¬Q(q)` by exact
arithmetic, with an exact failure margin.
**Produces.** A refutation robust to any numerical dispute.
**Hypotheses.** Membership `q ∈ C` is the most-skipped step and the only
interesting one; the failure must be exact, not floating.
**Ceiling.** Never positive. Says nothing about the *size* of the failure set —
"one countermodel refutes a universal, not a generic".
**Instances (this repo).** `h = P₅(2t) − P₃(2t)`: `‖h′‖² = 36` but
`‖(Q₄h)′‖² = 60` — L² projection is *not* derivative-contractive. And the
decisive one from this round: **α = 1/3 shares the BBP forcing, poles, residues
and invariants with π, yet its carry sum diverges to 3/2.** A countermodel
sharing every structural feature of the target is the strongest kind — it
proves the feature is *irrelevant*.

## 3. M3 — Noncommuting-limits diagnostic

**Form.** For a doubly-indexed family `F_{m,N}` with a claimed limit, prove
`lim_m lim_N ≠ lim_N lim_m` and identify which order the naive argument
silently uses.
**Produces.** A located defect in a diagram — unconditional whenever both
iterated limits exist and differ.
**Hypotheses.** Both limits must genuinely exist (each is its own obligation).
**Ceiling.** Never says which order is correct. Cannot rule out that a *third*
procedure (simultaneous with a rate) succeeds.
**Instance.** POL-02: `lim_m lim_N ν_N(q_m) = δ₀` while
`lim_N lim_m ν_N(q_m) = λ`. Spatial refinement at fixed time destroys orbit
statistics. This explains *why* many natural approaches to normality fail, and
it is the single most useful diagnostic in the repository.

## 4. M4 — Cohomological obstruction

**Form.** Given forcing `r` and multiplier `b`, ask whether `r(z) = b q(z−1) − q(z)`
has a solution in a declared class. Solve exactly; the weighted invariant
`Σ_j b^{−j} c_j` per residue is complete for the rational class.
**Produces.** Exact non-existence of a telescoping witness.
**Ceiling.** **Silent on rates.** This round proved it: `r(n) = 16^{−n}` is a
non-coboundary with *geometric* decay. So "invariant ≠ 0" never implies "no
cancellation". Record this — it is the most tempting false inference in the
whole lane.

## 5. M5 — Soundness by refusal

**Form.** Design a bound that provably *fails to conclude* on a known
counterexample, so its silence is trustworthy.
**Produces.** A bound whose non-conclusion is informative.
**Hypotheses.** You must exhibit the refusal on a real counterexample (x = 1/3).
**Ceiling.** Soundness is cheap; strength is not. A bound can refuse everything.
**Instance, with correction.** CYC-01 refuses x = 1/3 — but **not** via the
mechanism the report claims. Live measurement: `η_N = max(0, 2c₁) = 0` because
`c₁ = cos(2π/3) = −1/2`; the refusal is carried by `T3 = 0.75`. The conclusion
stands; the stated arithmetic does not. **Recorded as a correction.**

## 6. M6 — Orthogonal channel decomposition

**Form.** Split the space into L²-orthogonal pieces with exact Gram matrices so a
quadratic form becomes `Σ_k w_k · (rank-one)`. Example: `φ_e = t²−¼`,
`φ_o = t(t²−¼)` with `‖φ_e‖² = 1/30`, `‖φ_o‖² = 1/840` give the weight pair
(30, 210).
**Ceiling.** Requires exact Grams and genuine orthogonality; a near-orthogonal
split silently loses a cross term (see the PDQ audit's cross-parity contamination).

## 7. M7 — Constant sharpening (and its honest failure)

**Form.** Replace a published envelope with an exact source-derived constant.
**Instance.** κ = 1/50 → κ′ = 0.0389832818322773 (1.95×), from exact endpoints
5.86231 < 47/8 plus the Ω=13 method optimum.
**Ceiling, and this is the point.** The improved constant **did not change the
verdict**: the bracket moved from −1.260 to −0.647 against a threshold of
6.0e−7. A sharpening is only progress if you also report the distance to the
threshold (→ M8).

## 8. M8 — Threshold arithmetic

**Form.** Bisect the free parameter of the *conclusion* to find the exact value
at which it would flip; compare with what is available; report the ratio.
**Instance.** Positivity needs residual cap `τ* = 363594907672565835/604462909807314587353088
= 6.0152e−7`; the present cap is `121/32 = 3.78125`; **ratio 6.29e6**.
**Why it matters.** It converts "we are stuck" into a number that any future
claim must beat. It also *falsifies* routes instantly: a 1.95× improvement
against a 6.3e6× gap is not a near miss.
**Ceiling.** Localises; never crosses. And a threshold computed under a *wrong*
bracket shape is worthless — validate the bracket first.

## 9. M9 — Two-instrument cross-check

**Form.** Implement the same quantity twice, sharing no code; report agreement
and the failure modes each can see.
**Instance.** CYC-01 instruments A and B agree to ≤7e−20; calibration 17/17.
**Ceiling.** Agreement proves the *implementation*, never the *mathematics*.
Two instruments sharing an assumption share its error. (This round: an agent's
sandbox had broken `float`/`mpmath`; the instrument caught it only because a
second path existed.)

## 10. M10 — Kernel-checked finite kernel

**Form.** Move a finite algebraic/combinatorial lemma into Lean/mathlib, certify
it, and explicitly *not* claim the ambient infinite statement.
**Instance.** The BBP identity `π = Σ rho(m)16^{−m}` is kernel-checked; global
equidistribution is explicitly not.
**Ceiling.** A finite checked certificate is not an infinite analytic theorem.
The discipline is in the *seam*: name exactly which premise remains a paper
claim.

## 11. Mechanisms not yet in the repo, worth importing

Evaluated as transducers (input → output → ceiling):

- **van der Corput / Weyl differencing** (already the spine of CYC-01) — beyond
  R=2 it buys `N^{−1/2}`-type cancellation from *smoothness of the phase*, not
  from arithmetic. **Ceiling:** needs the phase to have bounded derivatives;
  `b^j x` mod 1 is not smooth in `j`.
- **Large sieve / amplification** — consumes many frequencies at once, emits a
  bound for *most* of them. **Ceiling:** "most" is useless for one orbit; this is
  precisely why it cannot touch π.
- **Entropy compression (Moser–Tardos)** — emits existence of an object with a
  local-violation bound. **Ceiling:** pure existence; no rate, no specific orbit.
- **Polynomial method / slice rank** — consumes algebraic structure (tensors).
  **Ceiling:** π has no such structure; not applicable.
- **Compactness + finite-dimensional reduction** — consumes a uniform bound on a
  family; emits a limit object. **Ceiling:** the bound must be *uniform*, which
  is exactly what fails here (error grows as `b^N`).
- **Smoothing then un-smoothing** — consume an approximation family; emit a
  result for the limit, controlling the error. **Ceiling:** needs the error to
  vanish; POL-03 shows it grows exponentially at fixed stage.
- **Transference (Green–Tao)** — consumes a dense model of a sparse set; emits
  the sparse result. **Ceiling:** needs a pseudorandomness/linear-forms
  condition. **This is the most promising unused mechanism** if applied
  carefully: build a dense model for the carry-cost functional rather than for
  the digit set.
- **Energy increment / structure vs randomness** — consumes a discrepancy
  deficiency; emits structure. **Ceiling:** outputs structure, not cancellation.
- **Lovász Local Lemma** — satisfiability, not analytic estimates.
- **Interval arithmetic + directed rounding** — certification of finite
  statements. Already present and used correctly here.
- **Formal assistants as epistemic shift** — moves trust from prose to kernel.
  Ceiling: only for what is formalised.

## 12. Is there a general theory?

**Honest answer: not a strong one.** There is no theorem that says "mechanism X
applies to problem Y". What exists, and is worth having, is a **discipline**:

> **Every reduction must state its own failure mode.**

That single sentence subsumes M1–M10. A conditional criterion that does not name
what could make its premise false is not a criterion, it is a hope. A
countermodel that does not state its membership proof is not a refutation. A
sharpened constant that does not state the threshold distance is decoration. A
kernel check that does not name the paper gap is a liability.

The taxonomy in §0 is real: mechanisms do sort by *what they consume* and *what
they can never do*. But it is a **routing table**, not a theory.

## 13. Ranked for a CYC-03-shaped problem

1. **M3 (noncommuting limits) applied to the criterion itself.** Before proving
   anything, ask: does the criterion's quantifier order match the problem's?
   CYC-03 needs uniformity over `d < R_N` at fixed `N`; the natural proofs give
   the reverse. This diagnostic costs a day and can save a campaign.
2. **M8 (threshold arithmetic) + M9 (calibration)** as a *gate*: compute the
   exact flip value and the exact available value before writing any prose. If
   the ratio is > 100, do not write the paper; the lane needs a different shape.
3. **Transference** (unused here): build a dense model for the *carry-cost
   functional*. Genuinely untried, and structurally different from everything
   closed so far.

## 14. Reusable artifacts proposed

1. **A routing skill** (`proof-mechanism-router`): given a problem statement,
   classify its input type, list which mechanisms can consume it, and print each
   one's ceiling. Cheap to build, prevents the failure mode that cost this repo
   the four-pole lane.
2. **A mechanism-receipt test pattern**: every research module ships
   `MECHANISM`, `CEILING`, `THRESHOLD` and `FAILS_ON` fields.
3. **A conditional-criterion doc template**: `Target ⟸ Premise` with mandatory
   sections *why this is not a tautology* and *what would falsify Premise*.
4. **A three-module library** (`exact_countermodel`, `threshold_bisect`,
   `mechanism_audit`) — small, dependency-free, exact-rational.
