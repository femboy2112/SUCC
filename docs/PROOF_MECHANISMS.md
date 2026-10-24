# PROOF MECHANISMS — a transductive catalogue

> **SOURCE-PROOF AUTHORITY CORRIGENDUM (2026-10-24).**
> This is a *methodology catalogue*, not a sound theorem prover.
> String descriptions of a witness's membership do NOT authenticate
> that it satisfies the source contract. Callback/Boolean flags
> are likewise not Lean proof certificates. Finite bisection with
> exact Fraction arithmetic produces a rational BRACKET, not
> generally an exact unknown threshold. "GENERIC implication"
> is not a failure: source-specific verification of its premise
> can yield a targeted result. A property lost under a quotient
> may still control recurrent source behavior; require a
> source/action/readout commuting diagram before deriving a no-go.
> Categorical *faithfulness* (injective on hom-sets), source
> preservation, target-relative sufficiency and experimental
> failure observability are distinct. The former "BBP four-pole lane CLOSED"
> verdict is **WITHDRAWN**: see
> [the BBP source-repair dossier](../research/2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md)
> and the [corrected four-pole audit](../research/2026-10-23/CYC03_LANE_CLOSED.md)
> (the filename retains "CLOSED" for link stability; its *content* is the
> corrected, withdrawn-verdict audit, R1–R8). Concretely: `α = 1/3` does **not**
> share the authenticated BBP source (it changes the initial state `y₀`);
> `r(n)=16^{-n}` **is** a coboundary (a non-coboundary only inside the narrower
> rational-function class); and an equivalent reformulation earns **no proof
> credit** but is not therefore worthless. The current entries below have been
> corrected to match; the former claims are preserved in the historical reports
> (`CYC03_LANE_CLOSED_HISTORICAL.md`, `CYC03_BBP_FOUR_POLE_LANE.md`).


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
**Hypotheses.** (a) implication proved, not observed; (b) if Premise is equivalent
to Target the criterion earns **no proof credit** — it is a restatement, not a
step — yet an equivalent restatement can still be *useful* as a representation: it
may expose a source-specific estimate that is easier to prove, give a finite/rate
form, or make counterexamples checkable; (c) a Premise trivially stronger than
Target is vacuous.
**Ceiling.** Cannot prove Premise. Cannot, by itself, detect that Premise ≡ Target
— that needs a separate argument. Equivalence is a *no-credit* flag, not a dead end.
**Instance.** CYC-01′: normality ⟸ carry-sum → 0, where the carry sum is
observable. The value is that it *relocates* the open content to a place where one
can at least measure. The caveat learned the hard way: a criterion that holds
*generically* (for every x) does not **by itself** discriminate π — but
source-specific verification of its premise can still yield a targeted result (see
the corrigendum).

## 2. M2 — Exact countermodel as the theorem

**Form.** To refute `∀q ∈ C : Q(q)`, exhibit `q ∈ C` and prove `¬Q(q)` by exact
arithmetic, with an exact failure margin.
**Produces.** A refutation robust to any numerical dispute.
**Hypotheses.** Membership `q ∈ C` is the most-skipped step and the only
interesting one; the failure must be exact, not floating.
**Ceiling.** Never positive. Says nothing about the *size* of the failure set —
"one countermodel refutes a universal, not a generic".
**Instances (this repo).** `h = P₅(2t) − P₃(2t)`: `‖h′‖² = 36` but
`‖(Q₄h)′‖² = 60` — L² projection is *not* derivative-contractive. And a
cautionary one from the four-pole round: `α = 1/3` was offered as a countermodel
"sharing every structural feature of π". It does **not**: it keeps the forcing
`r(n)` but changes the initial state `y₀` from `0` to `1/3` (so `y₁ = 7/15`, not
the authentic `2/15`), and the authentic source carries a unique bounded backward
tail `t₀ = π/16`. So `1/3` is a *generic* `T₁₆` circle-dynamics negative control,
**not** a member of the authenticated BBP source, and cannot prove a shared
feature "irrelevant". See the corrected audit
`research/2026-10-23/CYC03_LANE_CLOSED.md` (R2).

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
**Ceiling.** **Silent on rates, and class-relative.** A nonzero weighted invariant
`Σ_j b^{−j} c_j ≠ 0` excludes a coboundary only *inside the declared class*. The
tempting false inference, now corrected: `r(n) = 16^{−n}` is **not** a counterexample
— it *is* an exact coboundary, `r(n) = 16·q(n−1) − q(n)` with `q(n) = 16^{−n}/255`;
it is a non-coboundary only within the narrower rational-function-in-`n` class.
Illustrate the genuine obstruction with `r_K(n) = K!/[n(n+1)…(n+K)]`, whose rational
pole invariant `(1−16)^K ≠ 0` while its tail decays at arbitrarily high polynomial
order — *that* is the content of "silent on rates". (See `CYC03_LANE_CLOSED.md` R4.)

## 5. M5 — Soundness by refusal

**Form.** Design a bound that provably *fails to conclude* on a known
counterexample, so its silence is trustworthy.
**Produces.** A bound whose non-conclusion is informative.
**Hypotheses.** You must exhibit the refusal on an explicit negative control
(`x = 1/3`, a generic non-BBP-source orbit — not a member of the authenticated source).
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
  bound for *most* of them. **Ceiling:** "most" does not pin a single orbit; without
  a source-specific amplifier it does not by itself reach π.
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

## 12. There IS a general theory: FieldClass, and fidelity as the organising test

**Correction to an earlier version of this document.** A first draft of this
section claimed "there is no strong general theory; it is a routing table".
That was false, and false in a diagnosable way: it inferred a claim about
*theory* from an inventory of *techniques*. Counting tricks cannot settle
whether a theory exists — the same error as proving non-normality from a finite
prefix. The repository already contains the theory. This section states it.

### 12.1 The observer category

`docs/FOUNDATIONS.md` §1 fixes five levels — physical carrier, causal record,
semantic representation, mathematical structure, global report — and asks the
governing question:

> **Which morphisms between these levels are faithful, causal, regular,
> computable and justified?**

The SUCC arrow `O_n → O_{n+1}` (append a *realized* event, §2) is the canonical
arrow. Everything in §0 is a *derived* arrow inside this category.

### 12.2 FieldClass is the theory, and it is executable

`docs/OBSERVER_PROOF_ACCESS.md` + `observational_succ/field_limit_compactness.py:
source_dependent_field_frontier` define a field label as a property of a
triple, never intrinsic to an object:

```
FieldClass(Source, Target, Tools)
```

| class | meaning | proof obligation |
|---|---|---|
| **SimpleField** | verified finite program supplies the interface | program + lawfulness |
| **IdealHardField** | provable existence, no computable witness | existence + *non-existence of a selector* |
| **FuckedField** | proved impossibility / nonidentifiable fiber | the impossibility itself |
| **Unresolved** | toolkit-relative dark | **nothing** — explicitly not a theorem |

The fourth class is the discipline that the failed draft lacked. "Cannot prove
within this toolkit" is categorically different from "impossible", and the code
enforces the distinction (`"unresolved_observer_ambiguity":
"TOOLKIT_RELATIVE_DARK_NOT_PROVED_ABSOLUTE_IMPOSSIBILITY"`).

### 12.3 The single criterion, and why the ten mechanisms are instances

> **Fidelity criterion.** A reduction is a morphism between observation
> stages. It is *faithful* iff its failure mode is observable at the target
> stage. An unobservable failure is a lossy quotient masquerading as an
> equivalence.

"Every reduction must state its own failure mode" is not an independent
principle; it is a consequence of this criterion. In the observer language each
mechanism is a specific fidelity test:

| mechanism | what it actually is |
|---|---|
| M1 conditional criterion | a map whose *fidelity* is the unproved part |
| M2 countermodel | a witness that a quotient is **non-faithful** |
| M3 noncommuting limits | proof that two **orders of observation** are non-equivalent |
| M4 cohomological obstruction | an invariant of the observer's **action algebra** |
| M5 soundness by refusal | an observer correctly reporting its **own blindness** |
| M6 orthogonal channels | factoring **information** into independent channels |
| M7/M8 | quantifying how much the **finite resolution** is short |
| M9 two instruments | two observers comparing notes |
| M10 kernel check | delegating **fidelity-checking** to a machine |

### 12.4 The transient criterion (a predictive theorem-shape — and how it was misapplied)

The following rule has predictive content, **but only once an authenticated
source/action/readout commuting diagram is in place** — and the BBP four-pole lane
is the cautionary case where it was applied *without* one:

> **Transient criterion.** If a structural feature a proof uses is annihilated by
> one application of the dynamics *in a faithful pushforward*, it lives on the
> *transient* and cannot control the *recurrent* statistics.

The former round read this as a one-line kill of the four-pole lane. That reading
is **withdrawn**. The pole residues live in the forcing *index* variable, not in
`T₁₆` state space, so the "poles die in one step" pushforward is **not faithful**:
the pole measure's pushforward is `0`, but its Stieltjes readout is `r(n) ≠ 0`, and
the source Green/Hausdorff kernel is positive with infinite Hankel rank
(`m₀ = 0`, `m₁ = 15/64`) — the residues are *not* invisible. The `α = 1/3`
"countermodel" does not repair this: it is a generic non-source orbit (see M2).
The lesson is the opposite of a success: the criterion is sound, but applying it
across a **non-faithful** quotient is exactly the fidelity error this corrigendum
warns against. See `research/2026-10-23/CYC03_LANE_CLOSED.md` (R1–R3).

The rule is still a **routing rule with predictive content** — which is what a
theory supplies — provided its faithfulness hypothesis is discharged first.

## 13. Ranked for a CYC-03-shaped problem

1. **M3 (noncommuting limits) applied to the criterion itself.** Before proving
   anything, ask: does the criterion's quantifier order match the problem's?
   CYC-03 needs uniformity over `d < R_N` at fixed `N`; the natural proofs give
   the reverse. This diagnostic costs a day and can save a campaign.
2. **M8 (threshold arithmetic) + M9 (calibration)** as a *gate*: compute the
   exact flip value and the exact available value before writing any prose. A
   large ratio (say > 100) *localises* how far short the lane is — treat it as a
   quantitative obstruction to clear, not as proof the lane is dead.
3. **Transference** (unused here): build a dense model for the *carry-cost
   functional*. Genuinely untried, and structurally different from everything
   closed so far.

## 14. Reusable artifacts proposed

1. **A routing skill** (`proof-mechanism-router`): given a problem statement,
   classify its input type, list which mechanisms can consume it, and print each
   one's ceiling. Cheap to build, and it guards against the fidelity error that
   derailed the four-pole round (applying a transient-mass rule across a
   non-faithful quotient).
2. **A mechanism-receipt test pattern**: every research module ships
   `MECHANISM`, `CEILING`, `THRESHOLD` and `FAILS_ON` fields.
3. **A conditional-criterion doc template**: `Target ⟸ Premise` with mandatory
   sections *why this is not a tautology* and *what would falsify Premise*.
4. **A three-module library** (`exact_countermodel`, `threshold_bisect`,
   `mechanism_audit`) — small, dependency-free, exact-rational.
