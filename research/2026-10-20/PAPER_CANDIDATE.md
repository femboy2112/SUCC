# DRAFT — NOT FOR PUBLICATION (no maintainer authorization)

# Exact certificates for local-to-global positivity transport, with a hostile audit of a proposed rigidity calculus

**Status of this document.** A referee-readable *candidate* assembled from the
strongest **actually proved / certified** results of Operation Rigidity Forge. It
claims **no new mathematics**: every theorem below is classical, or a refutation, or
a formal re-expression. The contribution is infrastructural and methodological. Per
the project discipline it is **not to be published, tagged, or submitted** without
explicit maintainer authorization. Novelty boundaries are stated in §6.

## Abstract
We give an exact (rational/symbolic) certificate layer for finite and shorted Schur
complements and prove a form-core positivity-transport theorem with an exact
counterexample showing `L²`-density cannot replace form-core density. We use this
layer as a *crucible* to audit a proposed "unified ascent calculus and five-fold
obstruction theory," refuting eight specific claims with exact counterexamples and
supplying minimal correct replacements. We then exhibit a formal theorem-transport
bridge discharging a SUCC Mason–Stothers certificate by mathlib4's `Polynomial.abc`,
with a full axiom audit, and derive classical polynomial Fermat. Finally we localize
the Cauchy–Schwarz `t<1/2` ceiling of an abc radical-index moment bound to a
layer-uniform `θ=1` wall, naming exactly the machinery a genuine improvement needs.

## 1. Introduction and prior work
Schur complements and the shorted operator (Anderson–Trapp), Douglas's range
factorization lemma, Haynsworth's inertia additivity, and Schoenberg's theory of
conditionally negative-definite kernels are classical. Mason–Stothers (Stothers
1981; Mason 1984) is the polynomial abc theorem; it is formalized in mathlib4
(`Polynomial.abc`, Baek–Lee 2024). The abc radical-index second-moment bound and its
exceptional-set refinements are recent (BBLT, arXiv:2410.12234). Our aim is not to
extend these but to build an **exact, hostile-tested certificate layer** in which a
proposed local-to-global rigidity theory can be checked claim-by-claim, and to carry
one classical theorem faithfully across the SUCC/mathlib boundary.

## 2. The exact rigidity certificate layer
**Definitions.** For real symmetric `M=[[A,B],[B*,D]]`, PD is tested by Sylvester
(leading principal minors `>0`), PSD by *all* principal minors `≥0` (the
leading-only test is PD-only; `[[0,0],[0,−1]]` is the standard trap). Negative
witnesses are exact rational vectors `v` with `vᵀMv<0` (numeric search, exact check).

**Theorem 2.1 (finite Schur, D≻0).** `M⪰0 ⇔ A−BD⁻¹B*⪰0`. *Proof:* square completion
`Q(x⊕y)=⟨(A−BD⁻¹B*)x,x⟩+⟨D(y+D⁻¹B*x),(y+D⁻¹B*x)⟩`, verified exactly. ∎

**Theorem 2.2 (shorted extension, D⪰0).** With `D⁺` and range inclusion
`ran(B*)⊆ran(D)`, `M⪰0 ⇔ A−BD⁺B*⪰0`; if range inclusion fails, `M` is not PSD. This
is the Douglas/shorted form.

**Theorem 2.3 (form-core positivity transport).** For a closed lower-bounded form `q`
and a form core `C`, `q≥0` on `C` implies `q≥0` on `Q(q)`. *Proof:* `q` is form-norm
continuous and `{q≥0}` is form-closed; approximate in form norm. ∎
**Counterexample 2.4 (necessity of form core).** An exact truncated unbounded
indefinite form on `ℓ²` with an `L²`-dense test space `ker φ` (`φ` discontinuous) on
which `q>0`, while `q[e₁]=−9<0`: `L²`-density does **not** certify positivity. ∎

Rigidity is reported as six independent obligations (source adequacy, range
inclusion, gap, inverse-response sign, true-Schur PSD, sufficient surrogate), never
as a single scalar — collapsing them is the failure mode §3 documents.

## 3. The crucible: eight refutations with replacements
Using §2 we audit the proposed calculus (full ledger in
`GEMINI_CRUCIBLE_DOSSIER.md`). Decisive results, all exact:
- **Restricted coercivity transfer — REFUTED.** `A=2,B=(1,0),D=[[1,9/10],[9/10,1]]`:
  the compression `⟨De₁,e₁⟩=1` yields surrogate `>0`, but the true Schur complement
  is `−62/19<0`, with explicit negative vector. span(e₁) is not `D`-invariant.
- **Sufficient-as-necessary — MISLEADING.** `A=1,D=100,B=2`: surrogate `−3<0`, true
  Schur `24/25>0`. Failure of a sufficient test is not a negative witness.
- **Memory-debt transfer — REFUTED.** Autonomy of a quotient ⇏ unique source lift
  (`2ⁿ` lifts); and `‖(I−P)E(I−P)‖<γ` under `E⪰γI` is vacuous for any proper `P`.
- **Strict data-processing contraction — REFUTED.** Merge `C(x₁,x₂,x₃)=(x₁+x₂,x₃)`:
  `TV` stays `1/2` despite a nonzero kernel component; strict contraction needs
  intra-fiber sign cancellation.
- **Primitive prime-clock law — REFUTED.** Correct law `3(p−1)/((p+1)p^k)` (factor 3
  for three slots), derived from the conditional-Haar model; `p=2` normalization `=1`.
- **Prime-weight asymptotic — MISCLASSIFIED.** `Σ Λ(n)n^{−1/2}=2eᵃ+O(a²)` ⟺
  `ψ(x)=x+O(√x log²x)`: RH-strength, not PNT.
- **Float `is_globally_rigid` — REFUTED.** Ignores `D≻0`; `A=(1),D=(−1),B=0` falsely
  "rigid."
- **Master identity + five obstructions — NOT ADOPTED.** No shared carrier; defects
  are non-additive (quadratic inverse response); a class (vanishing uniform
  coercivity `diag(1,1/2,…)`) is missing.

## 4. Formal transport: Mason–Stothers ⟶ mathlib `Polynomial.abc`
A Lean 4 bridge (`MasonStothersBridge.lean`, mathlib v4.14.0) discharges the SUCC
Mason–Stothers certificate by `Polynomial.abc`, reconciling conventions exactly
(sum `A+B=C ↦ a+b+c=0` via `c:=−C`; radical via `radical_neg`; the char hypothesis
as the fact that eliminates mathlib's derivative-zero disjunct). A proven char-2
control (`X²,1,X²+1`) shows the hypothesis is load-bearing; a `#guard_msgs`
typecheck-failure control shows coprimality is genuinely required. Classical
polynomial Fermat (char 0, `n≥3`) is **derived** (mathlib v4.14.0 lacks it). Axiom
audit: `{propext, Classical.choice, Quot.sound}` (the disclosed cost of importing
mathlib; the standalone SUCC core remains `{propext, Quot.sound}`).

## 5. An abc moment no-go, sharply localized
For primitive triples, `S_t(X)=Σ ris(abc)^t ≤ M(t)M(2t)X²` holds for `t<1/2`
(Cauchy–Schwarz; `ris=n/rad`). With the layer radical `m_j(n)=∏_{p:v_p(n)=j}p` one has
the exact anatomy `ris(n)^t=∏_{j≥2}m_j^{t(j−1)}` (ABC-DEC-01; the `ε₀=0` case of BBLT
Lemma 2.2). The per-layer Euler factor converges iff `θ<1` **independently of the
layer** (ABC-DEC-02), so bounding the exponent or deleting any single layer cannot lift
the `t<1/2` ceiling: the obstruction is a layer-uniform `θ=1` wall, and passing it
requires genuine below-diagonal cancellation (BBLT's Fourier moment bounds +
geometry-of-numbers counts), which an Euler-product toolkit structurally lacks. abc
stays open; this is a decisive no-go, not a bound.

## 6. Originality boundaries and open problems
**No new mathematics is claimed.** Theorems 2.1–2.3 are classical; §3 are refutations
(the value is decisiveness + minimal replacements + exactness); §4 is a transport of
mathlib's theorem (classical); §5 is a no-go that *names* the missing machinery rather
than supplying it. **Open and untouched:** the abc conjecture; the `S_t` bound for
`1/2≤t<1`; binary Goldbach (`R_Λ(N)∼𝔖(N)N`); the Riemann Hypothesis and the signed
`S₄=A₄−R₄` sign. No zeta-zero ordinate is used anywhere; no positive auxiliary Gram is
identified with the completed Weil form.

## References (indicative)
Stothers 1981; Mason 1984; Baek–Lee (mathlib `Polynomial.abc`) 2024; Anderson–Trapp
(shorted operator) 1975; Douglas 1966; Haynsworth 1968; Schoenberg 1938; Berg–
Christensen–Ressel 1984; Bernert–Browning–Lichtman–Teräväinen arXiv:2410.12234.
