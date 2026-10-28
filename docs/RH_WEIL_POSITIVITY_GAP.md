# RH Weil positivity gap — the identification that is actually missing

**Branch:** `research/ravel-rh-weil-gap-2026-10-28` (created from `main` @ `b763ba8ef375fbac221e29e4396989a635a6ef36`). **RH PROVED: no.**

**Purpose.** This document names the *real* blocker of the RH program's
Weil/Suzuki route. The blocker is **not** "prove positivity of the completed
kernel" (that is RH itself, and re-proving it is the goal, not the obstacle).
The blocker is the **identification gap** between two different notions of
positivity that the SUCC framework generates, and which are currently being
conflated:

- **A** — *positive physical/semantic covariance* of observations, and
- **B** — *positive-definite completed Weil form* on the RH side.

Neither of these is "positive" in the same sense as the other, and no theorem
in the repository currently bridges them. Until the missing identifications in
§2 are proved, any claim that a positive covariance yields Weil positivity is a
**positivity-firewall violation** (METHOD.md Stage 2; FOUNDATIONS.md §3–4) and
must be treated as `UNVERIFIED`/`REFUTED` rather than assumed.

This is a framework-robustness artifact. It does **not** attempt an RH proof,
does **not** read nontrivial zero locations during construction, and does **not**
assert any new Weil positivity.

---

## 1. The two positivity notions, stated exactly

### 1.1 "Positive covariance" (physical/semantic) — object A

Fix a finite or finitely-indexed observation stage. Let `v:Ω→R^d` be a
vector of real-valued observable statistics indexed by the declared source,
and let `μ` be a nonnegative measure (a physical outcome law or a semantic
evidence distribution) over the parameter/source index.

- **Physical covariance.** For an outcome law `μ`, the covariance matrix
  `Σ_μ = E_μ[v v^⊤] − E_μ[v] E_μ[v]^⊤` is positive **semidefinite** by
  construction: `x^⊤ Σ_μ x = Var_μ(x·v) ≥ 0` for every `x∈R^d`. This is a
  theorem about second moments, holding for *every* probability measure `μ`,
  with **no arithmetic content whatsoever**.

- **Semantic covariance.** For an exponential-family normalizer
  `Z(θ) = Σ_n a(n) e^{θ·v(n)}` over nonnegative weights `a(n)≥0`, the Hessian
  `∇² log Z = Cov_θ(v,v)` is positive semidefinite, again by construction
  (FOUNDATIONS.md §4). The `a(n)` here are arbitrary nonnegative weights;
  the identity `∇² log Z ⪰ 0` holds whether or not `a` is the genuine
  Dirichlet/arithmetic coefficient sequence.

**Key fact (the firewall's first horn).** In *both* cases the positivity is
automatic and source-blind. Fake arithmetic sources — e.g. the deliberate
counterfeit `a(6)=2` (versus genuine `a(6)=1` with `b(6)=0`) — produce equally
positive covariance matrices. Therefore **A carries no source-identification
information**: it is a property of the probability/semantic layer, not of the
arithmetic source. Quantifiers: *for all* `μ`, *for all* nonnegative `a`, the
matrix is PSD. This is `PROVED LOCAL`/trivial, and it is *independent* of RH.

### 1.2 "Positive-definite completed Weil form" (RH setting) — object B

On the RH side the target is a **specific** kernel. In Suzuki's even screw
realization (FOUNDATIONS.md §3), with a continuously indexed two-time kernel,

    K_Ψ(t,u) = Ψ(t) + Ψ(u) − Ψ(t−u),
    ∂_t ∂_u K_Ψ = Ψ''(t−u) = W_Weil(t−u)   (as a distribution),

where `Ψ` is built from the **completed** (Gamma × pole × conductor-corrected)
ξ-type object with the *genuine* von Mangoldt / prime source, placed at the
critical **half-density**, with the correct conductor and root-number phase.

"Positive-definite" for B means:

- **global** positive definiteness of the completed kernel on the *entire*
  test space (all compactly supported smooth tests, or all of `H₀¹(−a,a)` /
  the relevant Hilbert carrier): `Σ_{i,j} c_i c̄_j K(t_i,t_j) ≥ 0` for all
  finite collections and all coefficient vectors `c`, **with the genuine
  arithmetic source fixed** and no truncation to a finite prime or spectral
  prefix.

- Equivalently, a **positive factorization** of the completed Weil form, or a
  strictly positive coercivity gap on the full carrier (not a compact/finite-rank
  shadow, not a bounded high-spectral tail).

This is the statement that is **RH-equivalent** (classical Weil/Suzuki). It is
`UNVERIFIED`, and — per CW-20 and ST-07 in the existing supplements — no finite
simulation or finite truncation establishes it.

### 1.3 The gap in one sentence

A is PSD *for every source, trivially, with no arithmetic input*; B is PSD
*for exactly one source, and that fact is RH*. Nothing in the repository makes
the specific A (whose `a(n)` is the genuine coefficient sequence) coincide
with the specific B. The two notions live on different layers of
ARCHITECTURE.md and the arrow between them is exactly what is unproven.

---

## 2. The exact missing identifications

Each row is an "if this were established, the Weil-positive conclusion would
follow" statement. Status is one of `PROVED` / `OPEN` / `REFUTED` /
`HYPOTHESIS`. A `REFUTED` row must carry a receipt (counterexample, cited
theorem, or typed contradiction); otherwise it is `OPEN` with the precise wall
named.

| # | Identification (steelmanned) | Status | Receipt / wall |
|---|---|---|---|
| G-01 | **Pointwise positivity ⇒ global positive-definiteness.** `Ψ'' ≥ 0` pointwise (or `Ψ ≥ 0` pointwise) implies the two-time kernel `K_Ψ` is positive-definite. | **REFUTED** | `Ψ(t)=t⁴`: `Ψ ≥ 0`, `Ψ'' ≥ 0` everywhere, yet the Gram at `t=±1` is `[[2,−14],[−14,2]]`, determinant `−192 < 0`. Receipt: ledger **O12** / FOUNDATIONS.md §3. |
| G-02 | **Positive physical covariance ⇒ Weil positivity.** A PSD physical covariance `Σ_μ ⪰ 0` of observations implies the completed Weil form `Q_ζ` is nonnegative. | **REFUTED** | `Σ_μ ⪰ 0` holds for *every* measure `μ`, including measures attached to fake sources. If it implied Weil positivity it would imply RH for free; since fake sources cannot satisfy the Weil functional equation/order-one growth, the implication is a typed-boundary crossing (covariance layer → proof layer). Receipt: FOUNDATIONS.md §4, ARCHITECTURE.md positivity warning. |
| G-03 | **Positive semantic covariance ⇒ Weil positivity.** `∇² log Z ⪰ 0` for an exponential-family with nonnegative weights `a(n)` implies the completed Weil form is nonnegative. | **REFUTED** | Same as G-02: `∇² log Z ⪰ 0` holds for *arbitrary* nonnegative `a(n)`, including the counterfeit `a(6)=2`. Fake arithmetic sources reproduce the cheap positivity. Receipt: FOUNDATIONS.md §4. |
| G-04 | **The genuine source is identified by positivity alone.** Nonnegative `a(n)` whose covariance is PSD *uniquely selects* the genuine Dirichlet coefficient sequence. | **REFUTED** | The fake-six control: `a(6)=2` (with `b(6)=1`) is a distinct nonnegative sequence with a PSD covariance, indistinguishable by positivity. Receipt: FOUNDATIONS.md §2; CW-17. |
| G-05 | **The screw-kernel second derivative equals the completed Weil kernel as a positive form.** `∂_t∂_u K_Ψ = W_Weil` as a *distribution* upgrades to global positive-definiteness of `K_Ψ`. | **OPEN** | The equality `∂_t∂_u K_Ψ = Ψ'' = W_Weil` is classical (distributional), but it is an identity of distributions, not a positivity statement. The step from "the mixed second derivative is the Weil distribution" to "the kernel is globally positive-definite" is exactly the missing Suzuki global limit. Wall: CW-20, ST-07. |
| G-06 | **Finite/truncated positivity ⇒ global positivity.** PSD on every finite prime or spectral truncation implies global positive-definiteness. | **REFUTED** | ST-06: a toy signed finite Hilbert form with a positive first coordinate and zero high tail can have opposite global sign; a finite prefix cannot certify the infinite tail. Receipt: ST-06. |
| G-07 | **Compactness of the Weil operator ⇒ positivity.** The compact (finite-rank-shadow) nature of the signed Weil H¹ operator (ST-09) implies nonnegativity. | **REFUTED** | A compact self-adjoint operator can still have a negative eigenvalue; an arbitrarily small negative infinite-tail eigenvalue remains possible at finite resolution. Receipt: ST-09's own boundary statement. |
| G-08 | **Half-density + conductor + Gamma + pole placement ⇒ positivity.** Correct completion data (proper Gamma, conductor `q`, pole, half-density, genuine primes) alone force global positive-definiteness. | **OPEN** | Correct completion is *necessary* for the Weil identity but not *sufficient* for positivity: the source must also satisfy the functional equation and order-one growth. The non-Euler Davenport–Heilbronn control (a genuine completed L-function-like object with a functional equation, yet a zero off the critical line) shows completion data alone does not force the critical-strip property. Wall: OBSERVER_TATE_NEXT_PROOF_GATES.md. |
| G-09 | **Source-exclusive Weil positivity.** The completed Weil form built from the *genuine* prime/von-Mangoldt source is nonnegative on all compact tests (global). | **HYPOTHESIS** | This *is* RH (CW-20, ST-07). Not a bridge; it is the destination. Listed for completeness so the bridge list does not silently smuggle the conclusion in. |
| G-10 | **A ⇒ B via a shared positive state.** There exists a bona fide positive functional/state on the correct observable algebra whose GNS/Gram is exactly the completed Weil kernel. | **OPEN** | The residual constraint from the productive failure of O12 (METHOD.md Stage 3): positivity must be derived from a positive state on the *correct* observable algebra, not from pointwise or covariance positivity. No such state has been constructed for the genuine Weil form. |

**Distribution:** `REFUTED` = 5 (G-01, G-02, G-03, G-04, G-06, G-07 — counting six), `OPEN` = 3 (G-05, G-08, G-10), `HYPOTHESIS` = 1 (G-09).

> **Corrected count note.** There are **10 distinct identifications**. By
> status: **6 REFUTED** (G-01, G-02, G-03, G-04, G-06, G-07), **3 OPEN**
> (G-05, G-08, G-10), **1 HYPOTHESIS** (G-09). No row is `PROVED`: the
> genuinely *established* facts (classical Weil identity, finite tail bounds,
> source-certified first pair) are **not** identifications — they are inputs
> that *feed* the gap, and they are already recorded in
> CLAIM_SUPPLEMENT_COMPLETED_WEIL.md (CW-*) and
> CLAIM_SUPPLEMENT_SIGNED_WEIL_H1_TAIL.md (ST-*). The gap is precisely the
> absence of any `PROVED` row here.

---

## 3. Known counterexamples / obstructions (explicit receipts)

These are the concrete objects that block the *naive* identification, each with
a receipt per METHOD.md's hard constraint.

1. **The `t⁴` pointwise-positive-but-not-PD Gram.** `Ψ(t)=t⁴` has `Ψ ≥ 0` and
   `Ψ'' ≥ 0` everywhere, yet the two-time Gram `[[2,−14],[−14,2]]` has
   determinant `−192 < 0`. Blocks G-01. Receipt: ledger **O12**, FOUNDATIONS.md §3.

2. **The `1−cos t` reverse counterexample.** `Ψ(t)=1−cos t` yields a positive
   Hilbert Gram with *sign-changing* pointwise curvature, showing the two
   notions do not even co-vary monotonically. Blocks the converse direction of
   G-01. Receipt: FOUNDATIONS.md §3.

3. **The fake-composite-at-6 control.** Deliberate `a(6)=2` (⇒ `b(6)=1`)
   versus genuine `a(6)=1` (⇒ `b(6)=0`). Both give nonnegative sequences with
   PSD covariances; positivity cannot distinguish them. Blocks G-03/G-04.
   Receipt: FOUNDATIONS.md §2, CW-17.

4. **The fake-six positive impulse changing `Ψ`.** CW-17: a fake-6 positive
   connected impulse changes `Ψ` by `−δ log6/√6 (R−log6)_+`, breaking Euler
   multiplicativity while preserving a positive-looking source. Blocks the
   "positive source ⇒ Weil source" reading. Receipt: CW-17.

5. **Positive coefficients with a negative completed kernel.** CW-18: positive
   Dirichlet coefficients can still yield `Ψ_fake(2) < 17−δ/30`, and at
   `δ=1000`, `K_fake(2,2) < 0`. The altered completion lacks the functional
   equation and order-one growth. Blocks G-08. Receipt: CW-18.

6. **The signed finite countermodel (positive first coordinate, negative
   total).** ST-06: a toy signed finite Hilbert form with a positive first
   coordinate and a zero high tail can have opposite global sign. Blocks G-06.
   Receipt: ST-06.

7. **The compact-operator-with-negative-eigenvalue obstruction.** ST-09: the
   signed Weil H¹ operator is compact (finite-rank shadow), but compactness
   does not exclude a negative eigenvalue; a negative infinite-tail eigenvalue
   survives finite resolution. Blocks G-07. Receipt: ST-09.

8. **The non-Euler Davenport–Heilbronn control.** A completed L-function-like
   object with a genuine functional equation but a zero off the critical line
   (`σ = 1/2` fails), showing that correct completion data + functional
   equation do *not* force the half-line property. This is the standing
   negative control for G-08. Status: **not yet fully analyzed in SUCC** —
   "No genuine completed non-Euler Davenport–Heilbronn source analyzed yet;
   source-specific negative control remains open." Receipt:
   CLAIM_SUPPLEMENT_SOURCE_MODEL_INTERACTION.md:34,
   OBSERVER_TATE_NEXT_PROOF_GATES.md:25.

---

## 4. What remains (missing theorem), in RH_HANDOFF format

The single missing theorem whose proof would actually close the gap and be
RH-strength, plus the required controls and a zero-independent reproduction
note.

### 4.1 The missing theorem (one precise statement)

> **Missing theorem (G-10 / G-05 closed).** There exists a positive
> functional (state) `φ` on the correct observable algebra — built from the
> **genuine** completed ξ-type object with proper Gamma factor, conductor `q`,
> pole, half-density, and root-number phase, in the Suzuki even-screw
> realization — such that the two-time kernel
> `K_Ψ(t,u) = Ψ(t) + Ψ(u) − Ψ(t−u)` is the Gram (GNS) kernel of `φ` on the
> **full** test space. Equivalently: the completed Weil form `Q_ζ` admits a
> **global** positive factorization (not a compact/finite-rank shadow, not a
> bounded high-tail) with a strictly positive coercivity gap on the full
> carrier `H₀¹(−a,a)` for every `a > 0`.

This is **not** a reformulation of "prove RH" that hides the difficulty; it is
the exact statement that the *source* (arithmetic) must be carried into the
*state* (positivity) by an arrow that currently does not exist in the
repository. Proving it is RH-strength by design; the point of this document is
that *this* is where RH effort should be spent, not on re-deriving the
automatic covariance positivity of §1.1.

### 4.2 Required controls (each must be shown to *fail* the missing theorem)

- **Fake composite at 6:** `a(6)=2` (⇒ `b(6)=1`) must *not* admit the positive
  factorization. (It currently cannot be excluded by covariance positivity
  alone — that is the gap.)
- **Changed prime weight / log phase:** perturbing `a(p)` or the log phase
  must break the positive factorization (CW-18's `K_fake(2,2)<0` is the model).
- **Wrong half-density:** placing the object off the critical half-density
  must destroy global positive-definiteness.
- **Matched Euler / Hecke:** a genuine Euler product with Hecke properties
  must *be required* for the factorization; a merely matched Euler object is
  not sufficient.
- **Non-Euler Davenport–Heilbronn:** the DH control (functional equation but a
  zero off `σ=1/2`) must fail the positive factorization, certifying that the
  half-line conclusion is not forced by completion data alone. This control is
  currently **unbuilt** in SUCC and is itself a prerequisite receipt.

### 4.3 Zero-independent reproduction note

The missing theorem must be checkable **without reading any nontrivial zero
location**. The factorization/coercivity claim must be stated in terms of the
source (prime/Gamma/pole/conductor/half-density data) and the test space only.
Any certificate must be a rigorous interval enclosure or a formal (Lean) proof
of the sign/factorization, not an mpmath float agreement, and not an evaluation
of a finite zero list. This mirrors the existing CW/ST discipline
("no numerical zeta-zero inputs").

---

## 5. Ranked cheapest next RH steps (falsifiable, not an RH proof)

Ordered by (cost × information-yield), each concrete and small, each
falsifiable, none an RH proof attempt.

1. **Build the non-Euler Davenport–Heilbronn completed control and run the
   Weil-form probe on it.** Currently the DH negative control is unbuilt
   (CLAIM_SUPPLEMENT_SOURCE_MODEL_INTERACTION.md:34). Constructing a genuine
   completed DH-type object with a functional equation and a known off-line
   zero, then confirming that its Weil form *fails* global positive-definiteness,
   converts G-08 from "OPEN by absence of a receipt" to "REFUTED with a
   receipt" — the single highest-value, lowest-cost falsification available.

2. **Sharpen CW-18's positive-coefficients-negative-kernel receipt into a
   formal counterexample to "completion data ⇒ positivity."** Enumerate the
   exact functional-equation/order-one-growth failure that the altered
   completion exhibits, producing a typed contradiction (METHOD.md receipt)
   that permanently quarantines G-08's naive reading.

3. **Formalize the `t⁴` Gram and the fake-six covariance in a Lean kernel
   snippet.** A two-line Lean proof that `[[2,−14],[−14,2]]` is indefinite and
   that `a(6)=2` yields a PSD-but-source-blind covariance gives G-01/G-03/G-04
   a *formal* receipt, upgrading them from ledger claims to machine-checked
   REFUTED entries (closes the "formal Lean kernel verification not supplied"
   gap flagged in CW's evidence separation).

4. **State the observable-algebra positive-state problem (G-10) precisely and
   attempt the *cheapest* candidate state.** Write down the correct observable
   algebra on which the Weil kernel should be a GNS Gram, and test the
   lowest-cost candidate state (e.g. a Gaussian/exponential family anchored to
   the genuine source) for whether its Gram coincides with `K_Ψ`. This is
   falsifiable: almost certainly the first candidate fails, and the *precise
   way* it fails names the next, harder wall (a productive failure per
   METHOD.md).

5. **Audit the existing CW/ST chain for any place that silently assumes a
   `PROVED`-labeled identification from §2.** A grep-and-annotate pass over
   CLAIM_SUPPLEMENT_COMPLETED_WEIL.md and CLAIM_SUPPLEMENT_SIGNED_WEIL_H1_TAIL.md
   to tag every downstream claim that (implicitly) depends on G-01…G-10, so the
   positivity firewall's transitive quarantine is explicit and no downstream
   result inherits an unproven identification.

---

## Boundary and status

- **RH PROVED: no.** This document proves nothing about RH; it *locates* the
  gap.
- No nontrivial zero locations were read during construction; no new Weil
  positivity is claimed.
- The genuinely established Weil-side facts (classical Weil identity CW-05,
  finite prime/Gamma tail bounds CW-03/CW-09/CW-11, spectral tail ST-03,
  compact shadow ST-09) remain **inputs** and are unchanged; they feed the gap
  rather than close it.
- All `REFUTED` rows carry a receipt; all `OPEN` rows name their exact wall
  (per METHOD.md Stage 2 hard constraint).
