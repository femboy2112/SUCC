# abc moment frontier — correlation estimate + ABC-DEC-02 repair (Proof Forge III, Part V)

> **Academic Main VII status update:** this is a historical method dossier.
> CLOUD-ABC-01/05 now prove the primitive moment bound and full mean for
> 0≤t<2/3; see [the independent reconstruction](ACADEMIC_VII_ABC_REVIEW.md).
> The diagonal t<1/2 ceiling below remains a limitation of that method.
> The endpoint t=2/3 and integer abc remain open. Historical receipts are unchanged.

**Date:** 2026-10-20. **Lane:** Lane E (number theory). **Branch:** `research/pf3-lane-abc-2026-10-20`
(worktree `/home/leah/SUCC-pf3-abc`, off `79ef776`). **Status:** DRAFT, not merged.
**Modules:** `observational_succ/abc_decomposition.py` (Part V section), builds on
`observational_succ/residue_box_counting.py` (Part IV) and `abc_triple_moment.py` (ABC-TMB-01).
**Tests:** `tests/test_abc_decomposition.py` — **32 pass, 0 fail** (15 pre-existing + 17 new);
`tests/test_residue_box_counting.py` — 22 pass (no regression). `compileall` clean.
**Firewall:** exact `Fraction`/`int` or certified two-sided rational enclosures everywhere; floats
only in `*_evidence` functions, never as certificates (AGENTS.md item 8).

**ABC: OPEN. integer-abc: OPEN. t ≥ 1/2 moment bound: OPEN** (main term reaches `t<1`; the error
term is uncontrolled). No RH, no new theorem on abc, no census upgraded to a theorem.

This dossier does three things the campaign asked for: (1) **qualifies ABC-DEC-02** precisely (it was
over-broad for the `E=1` squarefree class); (2) **separates four failure modes** and marks only the two
that are actually established; (3) runs the **Part IV residue-box theorem** as a genuine additive-
correlation attempt on the inner sum, delivering one partial theorem, one quantified obstruction, and one
newly-isolated missing estimate.

Throughout, `ris(n) = n/rad(n)` (the powerful/radical-index part; `ris(n)=1` iff `n` squarefree). The
inner correlation is `I_t(c) = Σ_{a+b=c,(a,b)=1} ris(a)^t ris(b)^t`, and
`J_t(X) = Σ_{c≤X} I_t(c) = Σ_{a+b≤X,(a,b)=1} ris(a)^t ris(b)^t`.

---

## 1. ABC-DEC-02 qualified — the E=1 vs E≥2 dichotomy (Task 1)

**The defect.** The old consequence **(b)** read: *restricting to a bounded-exponent class
`{max_p v_p ≤ E}` truncates the layers but does NOT move the threshold `θ<1`.* This is **false for
`E=1`**. If every allowed integer is squarefree (`E=1`), then `ris(n)=1` identically, so the moment
`Σ ris(n)^θ` is the squarefree count for **every** `θ` (including `θ≥1`) — there is **no `θ=1` wall at
all** in that layer. The unqualified statement silently assumed `E≥2`.

### 1.1 Statement (ABC-DEC-02q)

Let the bounded-exponent class be `C_E = {n : max_p v_p(n) ≤ E}` and let the `p`-adic Haar local factor
truncated to layers `j ≤ E` be
```
E_p^{(E)}(θ) = (p−1)/p · ( 1 + Σ_{j=1}^{E} p^{(j−1)θ − j} ),
```
with class mean `M_E(θ) = Π_p E_p^{(E)}(θ)`. Then:

> **(E = 1, squarefree class).** `ris ≡ 1`, and the only surviving local factor is
> `E_p^{(1)}(θ) = (p−1)/p·(1 + 1/p) = 1 − 1/p²`, **independent of θ**. Hence
> `M_1(θ) = Π_p (1 − 1/p²) = 6/π²` for **every** `θ`. **The θ = 1 wall is ABSENT.** Equivalently, for
> every `θ` and every `X`, `Σ_{n≤X, n squarefree} ris(n)^θ = #{squarefree n ≤ X} ≤ X` — exactly, with no
> θ-dependence. *(But this layer is **vacuous for abc**: squarefree `a,b,c` give `ris(abc)=1`.)*
>
> **(E ≥ 2).** The exponent-two layer **alone** carries the term `(1−1/p)·p^{θ−2}`, whose Euler product
> `Σ_p p^{θ−2}` converges **iff `θ < 1`**. So the wall **persists**, the threshold is `θ < 1`, and
> `M_E(θ) ≤ M(θ)` (truncation only drops non-negative higher-layer terms).

**Status:** **PROVED LOCAL.** The `E=1` half is an **exact algebraic identity** (`E_p^{(1)}=1−1/p²`
is returned as an exact rational, lo==hi, for every tested `θ`; the squarefree-count identity is exact).
The `E≥2` half is PROVED LOCAL **conditional on ABC-CLK-02** for the *quantitative* constant, but the
layer exponent `θ−2` and the convergence dichotomy are unconditional exact arithmetic.

### 1.2 Proof

*E = 1.* `C_1` is exactly the squarefree integers. For squarefree `n`, `rad(n)=n`, so `ris(n)=n/rad(n)=1`
and `ris(n)^θ = 1` for all `θ`. Therefore `Σ_{n≤X squarefree} ris(n)^θ = #{squarefree ≤ X}`, independent
of `θ`, and `≤ X`. In the Haar model, truncating at `E=1` keeps only `j=1`: the local factor is
`(p−1)/p·(1 + p^{(1−1)θ−1}) = (p−1)/p·(1 + 1/p) = (p²−1)/p² = 1 − 1/p²`, which has **no θ** (the `j=1`
exponent `(j−1)θ−j = −1` is θ-free). `Σ_p 1/p²` converges, so `M_1 = Π_p(1−1/p²) = 1/ζ(2) = 6/π²` for all
`θ`. ∎

*E ≥ 2.* The `j=2` term in `E_p^{(E)}` is `(p−1)/p·p^{θ−2} = (1−1/p)p^{θ−2}`, with leading exponent
`(2−1)θ − 2 = θ − 2` (this is `layer_mean_leading_exponent(2,θ)`). `Σ_p p^{θ−2}` converges iff
`θ−2 < −1` iff `θ < 1`; at `θ=1` it is `Σ_p p^{−1}`, which **diverges**. Since every term in
`E_p^{(E)}−1` is non-negative for `θ≥0`, the presence of this one divergent-at-`θ=1` term forces the
wall for every `E≥2`. Dropping layers `j>E` only removes non-negative terms, so `M_E(θ) ≤ M(θ)`. ∎

### 1.3 Receipts (exact)
- `squarefree_class_moment(X)` → moment `=` squarefree count, `theta_independent=True`,
  `wall_present=False` (checked `X=50,200,1000`; every such `n` has `ris(n)=1`).
- `bounded_exponent_local_factor_enclosure(p,1,θ)` `= (1−1/p², 1−1/p²)` **exactly** for
  `p∈{2,3,5,7,11,13}`, `θ∈{0, 3/7, 1/2, 9/10, 1}` (lo==hi, θ-independent).
- `bounded_exponent_threshold(E)` `= None` for `E≤1`, `= 1` for `E≥2`;
  `bounded_exponent_mean_converges(1,θ)=True` ∀θ, `(E≥2, θ)` iff `θ<1`.
- Code/doc repair: module docstring consequence **(b)** rewritten with the dichotomy and labelled
  **[ABC-DEC-02q]**; `cauchy_schwarz_ceiling()` gains `bounded_exponent_helps_for_E_ge_2=False` and
  `E1_squarefree_is_vacuous=True` (old keys preserved, so the pre-existing test stays green — no
  previously-true assertion was contradicted; the E=1 case was simply **absent** before).

---

## 2. Four failure modes — honest status (Task 2)

When the elementary bound stalls at `t=1/2`, four distinct things could be "failing". They are **not**
interchangeable, and conflating a method no-go with a mathematics no-go is exactly the over-claim
AGENTS.md items 4–5 forbid. Encoded as `failure_mode_ledger()` (a `FailureMode` dataclass with a
`FailureStatus` enum) and guarded by `failure_mode_overclaim_guard()`.

| tag | failure of… | status | receipt / why |
|---|---|---|---|
| **(a)** | the **diagonal / Cauchy–Schwarz strategy** | **ESTABLISHED** | the diagonal bound `I(c) ≤ Σ_{n<c} ris(n)^{2t}` needs `2t<1`; `cauchy_schwarz_ceiling()`, ABC-DEC-02(c), ABC-TMB-01 |
| **(b)** | a **particular local Euler-product majorant** | **ESTABLISHED** | the specific `M(t)M(2t)` majorant uses `M(θ)=Π_p E_p(θ)`, which **diverges at θ=1** (the `j=2` term `p^{θ−2}`), so it blows up at inner `θ=2t=1`; `local_ris_mean_factor_enclosure`, `layer_euler_product_converges(2,1)=False` |
| **(c)** | an **entire proof CLASS** | **NOT ESTABLISHED** | no proof of class-wide impossibility exists here; in fact the residue-box main term (§3) already reaches `t<1`, so the elementary/multiplicative class is **not** excluded |
| **(d)** | the **desired THEOREM itself** | **NOT ESTABLISHED** | the OPPOSITE is expected — the circle-method heuristic predicts an `X²` average bound up to `t<1`, and abc is believed TRUE; ABC-TMB-03 only rules out a uniform **pointwise** bound (mass is `o(X²)`) |

**This is a correctness repair.** The repo establishes (a) and (b) only. Nothing here licenses "the
theorem is false" or "no elementary proof can exist". `failure_mode_overclaim_guard()` asserts
`established = (a,b)` and `not_established = (c,d)`; a regression that flips (c) or (d) is a detectable
over-claim.

---

## 3. Residue-box additive-correlation attempt (Task 3)

**Goal.** Use the Part IV residue-box theorem
`N_R(X) = (|R|/W²)(X²/2) + E_R(X)`, `|E_R| ≤ 5|R|(X/W+1)` (informative only for `W < X/10`) to bound the
additive correlation `J_t(X)` by encoding joint prime-power occupation of `(a,b)` as residue constraints
mod `W`, **without assuming the expected `t<1` bound**.

### 3.1 The encoding and the exact majorant

`ris` depends only on the **powerful part** `P(n) = Π_{p:v_p(n)≥2} p^{v_p(n)}` (`ris(n)=ris(P(n))`, and
`P(n)` is powerful; verified `ris(n)=ris(powerful_part(n))` on `[1,2000)`). The key exact inequality
(`ris_powerful_majorant_terms`, exact for integer `t`, certified enclosure otherwise):

> **ris(a)^t ≤ Σ_{d | a, d powerful} ris(d)^t**   (all `t ≥ 0`),

because at each prime `p^v ∥ a` the powerful divisors are `{1}∪{p²,…,p^v}` and
`1 + Σ_{i=2}^{v} p^{(i−1)t} ≥ p^{(v−1)t} = ris(p^v)^t`. Hence, dropping coprimality upward,

```
J_t(X) ≤ Σ_{d,d' powerful} ris(d)^t ris(d')^t · #{(a,b): a+b≤X, d|a, d'|b}.
```

Each count `#{a+b≤X: d|a, d'|b}` is **exactly** a residue-box count mod `W=lcm(d,d')`
(`joint_divisibility_count`, which calls `residues_from_predicate` + `residue_box_count`); verified
`== brute force` on `(d,d',X) ∈ {(4,9,60),(8,27,100),(4,4,50),(9,25,120)}`, and
`N = X²/(2dd') + O(X+dd')` with the proved error bound holding exactly.

### 3.2 What Part IV **did** buy — the main term reaches t<1 (ABC-COR-01)

The residue-box **main term** is
```
(X²/2) · Σ_{d,d' powerful} ris(d)^t ris(d')^t/(dd')  =  (X²/2) · G(t)²,
G(t) = Σ_{d powerful} ris(d)^t/d = Π_p ( 1 + p^{t−2}/(1 − p^{t−1}) ).
```
The dominant per-prime deviation is the `p²`-layer term `p^{t−2}` (leading exponent `t−2`,
`powerful_main_term_leading_exponent(t)=t−2`), so

> **G(t) < ∞  ⟺  t < 1**   (`powerful_main_term_converges`; Euler product confirmed numerically:
> `G(0.4)≈3.65`, `G(0.5)≈4.95`, `G(0.7)≈15.4`, finite but blowing up as `t→1`, e.g. `G(0.99)≈7.5·10¹⁵`;
> per-prime factor is `+∞` for `t≥1`).

This is the central positive finding: the residue-box decomposition handles the two variables **jointly**
(a product of local densities), so its main-term threshold is **`t < 1`**, *strictly past* the diagonal
Cauchy–Schwarz ceiling **`t < 1/2`** (which came from diagonalising to `ris^{2t}`). The factor-of-two gain
is real **at the level of the main term**, and it is consistent with the circle-method heuristic
`I_t(c) ≍ G(t)²·c`. **Status: HEURISTIC main term, PROVED convergent (exact Euler product) — NOT a
rigorous bound** (see §3.4).

### 3.3 Genuine partial theorem — the bounded-powerful-part bound (ABC-COR-02)

For a **fixed** cutoff `Q`, let
`J_t^{(Q)}(X) = Σ_{a+b≤X,(a,b)=1, P(a)≤Q, P(b)≤Q} ris(a)^t ris(b)^t`. Using the §3.1 majorant and
`#{a+b≤X: d|a,d'|b} ≤ X²/(2dd') + 5(X+dd')`:

> **Theorem (PROVED LOCAL, explicit constants, EVERY t ≥ 0).**
> ```
> J_t^{(Q)}(X)  ≤  (X²/2)·G_Q(t)²  +  5X·A_Q(t)²  +  5·B_Q(t)²,
> ```
> `G_Q=Σ_{d pow≤Q} ris(d)^t/d`, `A_Q=Σ ris(d)^t`, `B_Q=Σ ris(d)^t·d` — all finite (Q fixed), so this is
> an `X²` bound with explicit constant `G_Q(t)²` **for all `t`, including `t≥1/2`**. The main term
> dominates the residue-box error once `X > 10·A_Q(t)²/G_Q(t)²` — the direct inheritor of Part IV's
> `X > 10W` boundary.

`bounded_powerful_part_bound(X,Q,t)` returns the certified upper constants and the dominance threshold;
`bounded_powerful_part_census(X,Q,t)` is the exact oracle. Verified `J_t^{(Q)}(X) ≤ bound` on
`(X,Q,t) ∈ {(60,8,1),(80,16,1),(100,9,1),(60,8,2),(50,25,1),(60,4,3)}` — e.g. `(80,16,1)`: census
`3427 ≤ bound 347369`. This genuinely bounds the **bounded-powerful-part** part of the correlation for
every `t`; it does **not** reach the full `J_t` (the tail `P(a)>Q` is the open part).

### 3.4 The quantified obstruction + the isolated missing estimate (ABC-COR-03)

**What Part IV did NOT buy.** The residue-box error bound `5(X+dd')` per pair, summed over the full
majorant, is dominated by the `B`-term `5·B_X(t)²` with `B_X(t)=Σ_{d pow≤X} ris(d)^t·d ≍ X^{(t+3)/2}`,
giving an error `≳ X^{t+2}` (in fact `~X^{t+3}`), which **overwhelms the `X²` main term for every
`t ≥ 0`**. EVIDENCE (`residue_box_error_growth_evidence`, floats, `t=1`): the full-majorant error-bound /
`X²` is `5.7·10³, 3.1·10⁴, 1.5·10⁵, 1.1·10⁶` at `X=50,100,200,400` — monotonically growing. So:

> **The residue-box method yields NO rigorous `X²` bound on `J_t(X)` for any `t ≥ 0`** — it does not even
> reprove the diagonal `t<1/2` result. It trades a **better main term** (`t<1`) for a **worse error**.

**Why — structural.** Residue-box counting is a **non-negative lattice-point count**: it reproduces the
main term (the product of local densities) **exactly** and provides **zero cancellation below it**. The
two arithmetic constraints behave as follows (both checked exactly):
- **Coprimality** `gcd(a,b)=1` kills only the **same-prime** joint occupation: `p|a ∧ p|b` is empty
  (`coprimality_joint_occupation(2,120)`: coprime same-prime count `=0`), because it would force
  `p|gcd(a,b)`. It does **not** restrict **different-prime** occupation `p^k|a, q^l|b` (`p≠q`), which is
  exactly what carries the moment (coprime different-prime count `=248` at `p=2,q=3,X=100`).
- **`a+b=c`** only **couples** residues by CRT: `p^k|a ⟹ b≡c (mod p^k)` — two independent congruences,
  density product `1/(p^k q^l)`, **no saving**. A positive count sees the density product and nothing
  below it.

The cancellation the problem actually needs is **Fourier** (sign-changing oscillation of `e(·)` over the
minor arcs), which is **structurally invisible** to a non-negative count.

**THE NEWLY-ISOLATED MISSING ESTIMATE (the Part V deliverable).**

> A count `#{(a,b): a+b ≤ X, a ≡ α, b ≡ β (mod q)} = (X²/2q²)·(#classes) + o(X²/q)` with a **power/log
> saving**, **uniform for moduli `q` up to `q ≍ X`**. Residue-box gives only absolute error
> `O(X+q)` = `O(1)` **relative** at `q ≍ X` — vacuous precisely at the **large-powerful-part tail**
> `q ≍ X^{1/2}…X` that carries the `t ≥ 1/2` difficulty. Supplying this saving is BBLT's input, not
> SUCC's.

**Status: NO-GO for the residue-box method (gap stated); the missing estimate is the result.** This is a
no-go for *one method*, **not** for the underlying mathematics (abc / integer-abc stay OPEN, the `t<1`
bound is expected true).

---

## 4. Honest comparison with BBLT (arXiv:2410.12234)

| capability | SUCC (this lane) | BBLT |
|---|---|---|
| exact `ris` layer anatomy, main-term local densities | **yes** (ABC-DEC-01, ABC-COR-01, exact) | yes (Lemma 2.2 anatomy, with `n^{ε₀}` slack) |
| joint main-term threshold | `t<1` **as a (convergent) main term**, error uncontrolled | `t<1`-type ranges made **rigorous** |
| AP / integer-point count with saving, uniform to `q≍X` | **absent** — residue-box error `O(X+q)`, no saving | **Prop. 4.1** Heath-Brown geometry-of-numbers / determinant method |
| cancellation from `a+b=c` (Fourier) | **absent** — non-negative count only | **Prop. 3.1** Fourier 2nd/4th-moment exponential-sum bounds |
| headline object | `ris^t` **second-moment average** over all primitive triples | **exceptional-set** counts (Thm 1.2 `X^{(23λ+3)/40+ε}`, Thm 1.3 `X^{3/5+ε}`) |

The objects differ (a moment average vs. an exceptional-set count), so **no exponent comparison is made**.
What this lane adds over the prior ABC-DEC-03 statement is the **quantification**: the residue-box route
makes precise *where* the elementary toolkit stops — the main term is fine to `t<1`, and the entire gap is
a **single missing estimate** (the uniform-to-`q≍X` AP count with saving), which is exactly the
Prop. 3.1 + Prop. 4.1 pair. SUCC's toolkit is structurally diagonal / non-negative; it cannot manufacture
the sign cancellation or the determinant-method saving.

---

## 5. Ledger (AGENTS.md labels)

| ID | statement | status | conditional on |
|---|---|---|---|
| ABC-DEC-02q | E=1 squarefree class: `ris≡1`, mean `6/π²` ∀θ, **no wall** (vacuous for abc); E≥2: wall at θ=1 via the `j=2` layer alone | PROVED LOCAL (E=1 exact identity; E≥2 cond. ABC-CLK-02 constant) | ABC-CLK-02 (quantitative only) |
| ABC-FM | four-failure-mode ledger; only (a) diagonal/CS and (b) a particular Euler majorant ESTABLISHED; (c) proof class, (d) theorem NOT | CORRECTNESS REPAIR (anti-overclaim guard) | — |
| ABC-COR-01 | residue-box joint main term `(X²/2)G(t)²`, `G(t)<∞ ⟺ t<1` (past diagonal `t<1/2`) | PROVED convergent main term (exact Euler product); HEURISTIC as a bound | — |
| ABC-COR-02 | bounded-powerful-part bound `J_t^{(Q)}(X) ≤ (X²/2)G_Q²+5X A_Q²+5B_Q²`, explicit constants, **all t** | PROVED LOCAL (exact, residue-box) | — |
| ABC-COR-03 | residue-box gives no rigorous `X²` bound (error `≳X^{t+2}`); non-negative count ⇒ no cancellation; missing estimate = saving-AP-count uniform to `q≍X` | NO-GO for the method; missing estimate isolated | — |

**Next falsification opportunity.** (i) Audit ABC-CLK-02 (the one lemma the `E≥2` quantitative constant
leans on). (ii) Attempt the isolated missing estimate — a power/log-saving AP integer-point count uniform
to `q≍X` — which requires importing a Fourier/large-sieve or determinant-method input currently outside
SUCC's toolkit; any such import must come with its own provenance and error bounds (AGENTS.md items 2, 8).

**ABC: OPEN. integer-abc: OPEN. t ≥ 1/2 moment bound: OPEN** (residue-box main term reaches `t<1`, but the
error term is uncontrolled; the gap is a single, explicitly-stated missing estimate).
