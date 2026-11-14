# Causal geometry: what "closer = more causally relevant" actually supports

**Second Forge, 2026-11-14.** Status labels follow [docs/METHOD.md](../../../docs/METHOD.md).
Every statement is about a *declared mathematical model*. Nothing here is a claim about
physical spacetime, quantum gravity, RH, or π-normality, and no scholarly novelty is claimed:
the ingredients are classical and are named where used. What is new to this project is the
assembly, the exact hypotheses, and the receipts.

The founding note ([PR #618](https://github.com/femboy2112/SUCC/pull/618), shared input) proposes
that proximity be an *output* of causal coupling. This document asks which geometric object the
mathematics forces. The answer is that **there are two objects, not one**, and they live over
different algebra:

| | structural dependency ("can influence") | net response ("does influence") |
|---|---|---|
| value algebra | an idempotent one: a quantale (truth values, costs, best-path weights, path languages) | a ring (signed reals); no idempotence |
| composition | joins of path weights never cancel | sums of path weights can cancel |
| geometry | the closure `R*` is a directed (Lawvere-type) distance: its triangle inequality is transitivity of closure | no triangle inequality once a response can cancel |
| under an observation quotient | can only get *closer* (QG-2); exactness has a four-way criterion (QG-3) | can be invented **and** deleted |
| bridge | `supp` is a homomorphism on nonnegative weights and only *lax* on signed ones (RG-1) | |

Sections 1–2 are the structural side (quotient geometry over a quantale). Sections 3–5 are the
response side (positivity, balance, gauge). Section 6 puts both to work on the "unseen causal
horizon". Section 7 lists what failed.

Executable evidence: `tests/test_observatoris_quantale_quotient.py`,
`tests/test_observatoris_response_geometry.py`; kernel evidence:
`formal/ObservatorisQuantale.lean` (see [THEOREM_FORGE.md](THEOREM_FORGE.md) for receipts).

**This is the text as repaired after adversarial review.** A hostile referee refuted or forced
repair of several statements of the first version (HQ-2(b), HQ-3, the HQ-4 chain, parts of RG-3,
RG-4's criterion, the scope of RG-1(c), QG-3 item 5 off the image, and the ghost/quasar
asymmetry). The refuted versions are kept as corpses in [COUNTERMODELS.md](COUNTERMODELS.md) §5,
with the referee's receipts in `tests/test_observatoris_referee_receipts.py`; each repaired
statement below says what changed.

---

## 1. Weighted ancestral reachability (QG-1 … QG-4)

**Inherited starting point.** SUCC's Principia-ancestral supplement
([PAP-01…PAP-05](../../../docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md)) treats Boolean
reachability: reachability from a selected start equals satisfaction of every hereditary
predicate; projection to an observation quotient is sound; and all-start endpoint exactness is
equivalent to saturation preserving hereditary predicates. Everything in this section
*generalises* those results; the Boolean case is recovered exactly.

**Definitions.** A *value structure* is a set `V` with a preorder `≤`, arbitrary suprema `⋁`, a
multiplication `⊗` and a unit `k` satisfying the inequalities of a unital quantale (monotone
`⊗`, distribution of `⊗` over `⋁` on both sides, associativity, unit laws). Commutativity is
**not** assumed. Instances:

- `𝔹 = ({0,1}, ≤, ∧, 1)`: reachability;
- `([0,∞], ≥, +, 0)`: cost / elapsed steps (`⋁` is `inf`);
- `([0,1], ≤, ·, 1)` and `(max, min)`: best-path relevance, bottleneck;
- `𝒫(M)` for a monoid `M` (e.g. words of actions): path languages — trace-level information.

For a set `X`, a `V`-relation is `R : X×X → V`. Its closure is
`R*(x,z) = ⋁ {weight of p : p a finite path x → z}` (the empty path has weight `k`). A
`V`-valued **hereditary predicate** (a *potential*) is `φ : X → V` with
`φ(u) ⊗ R(u,v) ≤ φ(v)` for all `u,v`. For an observation `q : X → Y`:

```
Q∃(a,b) = ⋁ { R(u,v) : q(u)=a, q(v)=b }          (may-quotient; SUCC's existential relation)
Q∀(a,b) = ⋀_{q(u)=a} ⋁_{q(v)=b} R(u,v)            (must-quotient)
(q_!φ)(b) = ⋁ { φ(u) : q(u)=b }                    (direct image of a potential)
```

**QG-1 (weighted PAP-01).** `R*(x,·)` is a potential with `k ≤ R*(x,x)`, and it is the least
such: for every potential `φ` with `k ≤ φ(x)`, `R*(x,z) ≤ φ(z)` for all `z`.
*Status: PROVED; Lean `star_closed`, `one_le_star`, `star_le_of_closed`. Classical in content
(enriched closure / shortest-path duality with feasible potentials).*

*Proof.* Closedness: `R*(x,u) ⊗ R(u,v) = ⋁_p (w(p) ⊗ R(u,v))` by right distribution, and each
term is the weight of a path to `v`. Minimality: by induction along a path, `w(p) ≤ φ(z)`: the
empty path gives `k ≤ φ(x)`; extending by an edge gives `w ⊗ R(y,z) ≤ φ(y) ⊗ R(y,z) ≤ φ(z)`. ∎

In the cost instance this is the classical statement that the shortest-path distance is the
largest feasible potential difference.

**QG-2 (weighted PAP-02: the quotient never under-reports).** For all `x,z`:
`R*(x,z) ≤ Q∃*(q(x), q(z))`. *Status: PROVED; Lean `star_le_quot_star`.*

*Proof.* `z ↦ Q∃*(q(x),q(z))` is an `R`-potential, because `R(u,v) ≤ Q∃(q(u),q(v))` and
`Q∃*(q(x),·)` is a `Q∃`-potential; apply QG-1. ∎

Read in the cost instance: **`d_Q(q(x),q(z)) ≤ d_source(x,z)`**. An observer who collapses
states can only see things as *closer* than they are. Coarse-graining invents shortcuts; it
never hides a route.

**QG-3 (weighted PAP-03: the exactness criterion).** The following are equivalent.

1. *Endpoint exactness at every start:* `Q∃*(q(x),b) ≤ (q_! R*(x,·))(b)` for all `x ∈ X`,
   `b ∈ Y` (the reverse inequality always holds by QG-2).
2. *Fibre constancy:* `q(x) = q(x')` implies `q_! R*(x,·) = q_! R*(x',·)`.
3. `q_!` maps `R`-potentials to `Q∃`-potentials.
4. `q^* q_!` (saturation) maps `R`-potentials to `R`-potentials.
5. *One-step may is below closure must:* every source edge `u → v` is realised, up to its weight,
   by the closure from **every** representative of `q(u)`:
   `R(u,v) ≤ (q_! R*(x',·))(q(v))` whenever `q(x') = q(u)`; equivalently `Q∃(R) ≤ Q∀(R*)`.
   (Found by the delegated workstream. The equality form "may = must for the closure" holds
   **on the image of `q`** only: on an empty fibre the must-value is the empty meet `⊤`.)

*Status: PROVED twice by different authors and routes — the PI's paper proof formalised in Lean
(`exact_iff_fibreConstant`, `exact_iff_pushClosed`, `exact_iff_satClosed`,
`exact_iff_edgeRealised`, axiom-free) and the Causal Geometer's independent paper proof with
exhaustive finite models over six value structures, one of them noncommutative. New-to-project
synthesis of classical ingredients.*

*Proof.* (1⇒2) Both sides equal `Q∃*(q(x),·)`. (2⇒4) Let `φ` be a potential and `s,t ∈ X`.
By right distribution it suffices to bound `φ(u) ⊗ R(s,t)` for each `u` with `q(u)=q(s)`. Now
`R(s,t) ≤ R*(s,t) ≤ (q_!R*(s,·))(q(t)) = (q_!R*(u,·))(q(t))` by (2), so by left distribution
`φ(u) ⊗ R(s,t) ≤ ⋁_{q(v)=q(t)} φ(u) ⊗ R*(u,v) ≤ ⋁_{q(v)=q(t)} φ(v) = (q_!φ)(q(t))`,
using that a potential propagates along the whole closure (left distribution and associativity).
(4⇒3) `(q_!φ)(a) ⊗ Q∃(a,b) = ⋁_{q(u)=a,q(v)=b} (q_!φ)(q(u)) ⊗ R(u,v) ≤ (q_!φ)(b)`.
(3⇒1) `q_!R*(x,·)` is then a `Q∃`-potential with unit at `q(x)`; apply QG-1 to `Q∃`. ∎

**Selected-start form.** For one chosen `x`:
`[∀b: Q∃*(q(x),b) ≤ (q_!R*(x,·))(b)]  ⟺  q^*q_!R*(x,·) is an R-potential.`
*PROVED; Lean `exactAt_iff_saturated_star_closed`.* As in the Boolean case, failure at another
start does not refute exactness at the selected one.

**QG-4 (may/must sandwich).** For every actual start `x` and report `b`:

```
Q∀*(q(x), b)  ≤  (q_! R*(x,·))(b)  ≤  Q∃*(q(x), b).
```

*Status: PROVED; Lean `quotAll_star_le_push_star`, `push_star_le_quot_star`. The must/may idea
is classical (modal transition systems; abstract interpretation); the weighted statement is an
elementary transposition.*

*Proof of the left inequality.* `q_!R*(x,·)` is a `Q∀`-potential: for `q(u)=a`,
`R*(x,u) ⊗ Q∀(a,b) ≤ R*(x,u) ⊗ ⋁_{q(v)=b} R(u,v) = ⋁_{q(v)=b} R*(x,u) ⊗ R(u,v) ≤ (q_!R*(x,·))(b)`.
Apply QG-1 to `Q∀`. ∎

In the cost instance: **`d_∃ ≤ d_source(x, fibre of b) ≤ d_∀`.** From quotient data alone the
observer gets a certified two-sided bracket: the may-distance is a time before which nothing can
arrive; the must-distance is a time by which a route is guaranteed from *every* representative.
Both inequalities are strict in general, and `Q∀* = Q∃*` is sufficient but not necessary for
exactness (see [COUNTERMODELS.md](COUNTERMODELS.md), and the agent report for the receipts).

### 1b. Results of the delegated quotient-geometry workstream

Full statements, proofs and receipts are in
[agents/OPUS_II_CAUSAL_GEOMETER.md](agents/OPUS_II_CAUSAL_GEOMETER.md). That report numbers its
theorems `CG-1 … CG-13`; they are cited here as "Geometer CG-n" and are distinct from the `QG-n`
identifiers of this document. The PI checked three of them by a separate brute force
(condition 5 above, join-closure, and the meet-failure receipt on four states).

- **A strict four-step hierarchy (Geometer CG-7, PROVED, each step strict by receipt).**
  one-step lumpable (`Q∀ = Q∃`) ⇒ `Q∀* = Q∃*` ⇒ **exact** ⇒ unpointed closure commutation.
  In particular `Q∀* = Q∃*` does **not** characterise exactness (the PI's question; REFUTED by
  SUCC's own PAP-04 chain), and the source value is **not** a function of the four quotient
  closures: two models share all of them and differ in what the start can reach.
- **A canonical repair (Geometer CG-10, PROVED).** All-start exact partitions are closed under
  arbitrary joins, so every observation has a **unique coarsest exact refinement** `q̂`, computed
  by profile splitting, and the true source values are recovered through it. Meets of exact
  partitions can fail (four states are needed), and for *selected-start* exactness there is no
  canonical coarsest refinement. The PI's worry that joins might fail was wrong.
- **Change of value structure (Geometer CG-5).** Strict homomorphisms transport selected-start
  exactness (also Lean `exactAt_map`). *Oplax* maps transport all-start exactness only; *lax*
  maps transport nothing, even with strict unit and joins (receipts). Converses fail at every
  link of language → cost → truth.
- **Time reversal (Geometer CG-8).** `q^*` has a left adjoint `Cl_Q∘q_!` and a right adjoint
  `Int_Q∘q_*` on potentials. Invertibility of the left Beck–Chevalley mate is forward exactness;
  of the right mate, **backward** exactness (the same theorem for the reversed relation). The
  universal image `q_*` pairs with the *backward* must-quotient, not the forward one.
- **Whole-distance preservation (Geometer CG-12, CLASSICAL).** `R*(x,z) = Q*(q(x),q(z))` for all
  pairs iff `q` merges only states at mutual unit distance.
- **Minimal ghosts (Geometer CG-6).** Three states are minimal only for *integral* value
  structures; two suffice otherwise.

**What this buys.** One theorem now covers reachability, cost, elapsed time, best-path relevance
and trace languages; SUCC's strict hierarchy *endpoint < cost < trace* (PAP-04) becomes a chain
of changes of value structure. Identifying SUCC's `future_safe_quotient` trace contract with
language-level exactness is **not established** (that contract also tracks costs, source tags
and rejection behaviour). **What it does not establish:** anything about signed weights
(Section 3), probabilities, frequencies, or the authenticity of a declared source table.

---

## 2. Ghosts and quasars: the two one-sided errors of an observer's geometry

Let the source be a network with dependency digraph `G_C` and structural distance `d_C`, and let
`G` be any value relation on the report set `Y` — the observer's geometry, however obtained.

- A **ghost** is a route the geometry asserts that the selected source state lacks
  (`G*(q x, b)` exceeds what `x` can do).
- A **quasar** is a source dependency the geometry does not account for
  (`R*(x,y) ≰ G*(q x, q y)`): an unseen ancestor.

**QG-5 (the quasar-free geometries; universal property).** For any `G`, in every value
structure, the following are equivalent:

1. no unseen ancestors at any horizon: `R*(x,y) ≤ G*(q x, q y)` for all `x, y`;
2. every source edge is covered: `R(u,v) ≤ G*(q u, q v)`;
3. `Q∃ ≤ G*`.

Hence **`Q∃*` is the least geometry without quasars, and a quasar is exactly an uncovered source
edge.** *PROVED* (the proof of QG-2 with `G*` in place of `Q∃*`); *CLASSICAL* in content: this is
soundness of existential abstraction (simulation preserves reachability). The first version of
this document stated only the special case `G = Q∃`, which the referee correctly called a
near-tautology; the equivalence above is the referee's strengthening (its R-1, exhaustively
tested on 4 928 cases).

**The symmetric picture.** The two quotient constructions of §1 are the two one-sided-error
geometries:

| geometry | ghosts (invented routes) | quasars (unseen ancestors) |
|---|---|---|
| may-quotient `Q∃` | possible | **impossible** (QG-5) |
| must-quotient `Q∀` | **impossible** (QG-4) | possible |
| exact observation (QG-3) | none | none |
| a model omitting a source edge | possible | possible |

*Receipt that a must-quotient hides an ancestor (referee R-3):* `q = (0,0,1)` with the single
edge `1 → 2`: `Q∀` is empty, so `d_∀ = ∞`, while `d_C(1,2) = 1`.

**Who can detect what (repaired; the first version overclaimed an asymmetry).**
With the source table in hand, both errors are decidable by computation: a ghost by a potential /
hereditary invariant containing the start (QG-1, SUCC's PAP-05), a quasar by the uncovered-edge
test above. With only quotient or model data, **neither** is decidable without an experiment:
two sources can share `Q∃`, `Q∀` and both closures while one has a ghost at the start and the
other does not (receipt: edges `{1→2, 1→0}` versus `{0→1, 1→2}`, `q = (0,0,1)`), and a quasar
shows only through a cone violation (HQ-3). So the asymmetry between "found by an invariant" and
"found by a contrast" is a difference between *data regimes*, not between failure types.
For value structures that are not totally ordered (path languages) one pair of nodes can be a
ghost and a quasar at once.

What survives of "the observer's effective light cone and the source dependency cone fail to
coincide": the failure has exactly these two directions, each geometry construction errs in one
of them only, and an omitted edge — a wrong model rather than a coarse one — is the only way a
*may*-type geometry acquires a quasar.

---

## 3. From structure to response: the support map (RG-1, RG-2)

Now weights are signed. A finite linear carrier is `z_{t+1} = A z_t` with `A` a square matrix
over an ordered field; `A_{vu}` is the weight of the structural edge `u → v`. The lag-`τ`
response of `y` to an impulse at `x` is `ρ_τ(x→y) = (A^τ)_{yx}` — the note's `C A^{t−s−1} B`
with coordinate input and readout. *(The chain-rule identity itself is CLASSICAL.)*

**RG-1 (support is lax; exact on the nonnegative cone).** *PROVED.*

(a) For every `A`: `ρ_τ(x→y) ≠ 0` implies a structural walk of length exactly `τ` from `x` to
`y`. *No response without ancestry.*
(b) If `A ≥ 0` entrywise, the converse holds: response support **equals** structural walks, at
every lag.
(c) The converse fails for signed `A`. For **distinct** nodes `x ≠ z` the smallest all-lag
failure has four nodes.

*Proof.* `(A^τ)_{yx}` is the sum over walks `x=w_0→…→w_τ=y` of the products of edge weights;
non-walks contribute zero, which gives (a). If `A ≥ 0`, each walk contributes a strictly positive
term, giving (b). Algebraically: `supp(ab) = supp(a)∧supp(b)` in a field, while
`supp(a+b) ≤ supp(a)∨supp(b)` with equality on the nonnegative cone; so `supp` is a semiring
homomorphism from nonnegative weights to `𝔹` and commutes with matrix powers, but is only lax on
signed weights. (c) *Receipt:* the signed diamond `x→y (1)`, `x→y' (1)`, `y→z (1)`, `y'→z (−1)`
has `(A²)_{zx} = 1 − 1 = 0` and no other walk from `x` to `z`, so `z` never responds to `x`
although every edge is live. *Minimality:* with three nodes `{x,w,z}`, a zero lag-1 response
forces `A_{zx}=0`, and then `(A²)_{zx} = A_{zw}A_{wx} + A_{zz}A_{zx} + A_{zx}A_{xx} = A_{zw}A_{wx}`,
which is nonzero whenever the only possible route `x→w→z` exists. ∎

(A cancellation at a *single* lag already occurs with two nodes: `A = [[1,0],[1,−1]]` has
`(A²)_{21} = 0` and `(A)_{21} = 1`. *Scope repaired after review:* for self-return (`x = z`,
positive lags) three nodes suffice — `x→w (+1), x→z' (−1), w→x, z'→x` has `(A^τ)_{xx} = 0` for
all `τ ≥ 1` — and two nodes never do; referee R-12.)

**RG-2 (finite decision of "never responds").** For an `n`-node linear carrier,
`ρ_τ(x→y) = 0` for `τ = 0,…,n−1` implies `ρ_τ(x→y) = 0` for all `τ`; and `n−1` zeros do not
suffice. *PROVED from Cayley–Hamilton (CLASSICAL); sharpness by the length-`n−1` chain.* The
bound uses the declared dimension; it is not a black-box guarantee
([FINITE_HORIZONS.md](FINITE_HORIZONS.md)).

**The restoring instrument.** In the signed diamond, the intervention `do(z_{y'} = c)` deletes
the edge into `y'` and the response of `z` to `x` reappears at lag 2. *Missing interventions
restore distinguishability*: the dependency was structurally present and behaviourally void for
every experiment that only touches `x` and reads `z`.

---

**RG-6 (signed quotients; resolvent lumpability — Geometer CG-13, PROVED there).** For signed
weights the quotient can both *invent* and *delete* a response at the same start (receipt in the
report), in contrast with QG-2 where deletion is impossible. The correct signed quotient notion
is Kemeny–Snell lumpability (CLASSICAL). With `I − A` invertible and `q` surjective,
**`(I−A)^{-1}` is lumpable iff `A` is lumpable**. For idempotent values the analogous statement
is false: closure-exactness (QG-3) is strictly weaker than one-step lumpability. The gap exists
because `R ↦ R*` is not injective while `A ↦ (I−A)^{-1}` is. *Generic faithfulness (CLASSICAL in
spirit):* as a polynomial in indeterminate edge weights, `(A^τ)_{yx}` has nonnegative integer
coefficients and is nonzero iff a walk exists, so exact cancellation is a proper algebraic
condition requiring mixed signs.

## 4. When the response supports a geometry: balance (RG-3, RG-4)

**RG-3 (nonnegative carriers: a graded supermultiplicative relevance).** Let `A ≥ 0`, `γ > 0`,
and `R_T(x,y) = max_{0≤τ≤T} γ^τ ρ_τ(x→y)`. Then

```
R_{S+T}(x,z) ≥ R_S(x,y) · R_T(y,z),     R_T(x,x) ≥ 1,     R_T(x,y) > 0 ⟺ d_C(x,y) ≤ T.
```

*PROVED.* `(A^{s+t})_{zx} = Σ_y (A^t)_{zy}(A^s)_{yx}` and every term is nonnegative; take the
maximising lags.

**What this is and is not (repaired after review; three overclaims withdrawn).**

- The family `D_T = −log R_T` is **graded**: `D_{S+T}(x,z) ≤ D_S(x,y) + D_T(y,z)`. At a fixed
  horizon it is *not* a metric (chain `x→y→z` at `T=1`), it can be negative (`A = [[2]]`), and
  the order it induces depends on the discount `γ`, which is chosen, not derived.
- A genuine `[0,∞]`-valued directed (Lawvere) quasi-metric is obtained by taking all lags and
  clamping: `D(x,y) = max(0, −log sup_{τ≥0} γ^τ ρ_τ(x→y))`. Then `D(x,x) = 0` and the triangle
  inequality holds because the supremum over all lags is supermultiplicative. It still depends
  on `γ`.
- The triangle inequality does **not** single out `−log`: every decreasing `φ` with
  `φ(ab) ≤ φ(a) + φ(b)` works, including the founding note's own `log(1 + 1/R)` (since
  `1 + 1/(ab) ≤ (1+1/a)(1+1/b)`). What is special about `−log` is only that, up to scale, it is
  the monotone transform turning products into sums *exactly*. So the note's edge-length
  transform remains a choice; what the theorem adds is that for balanced carriers the **response
  itself** (not only a path construction built from single edges) obeys the triangle inequality
  under any such transform.
- What defeats every transform is **cancellation, not imbalance**: if some structurally reachable
  pair has zero response at every lag, then for any `φ` with `φ(0) = ∞` and `φ(r) < ∞` for
  `r > 0` the graded inequality fails (signed diamond: `R(x,y)·R(y,z) = 1 > 0 = R(x,z)`).
  A carrier that is not balanced up to sign but never cancels (the negative directed 4-cycle)
  satisfies it.

**RG-4 (balance excludes cancellation).** Call `A` *balanced up to sign* if there are
`σ ∈ {±1}^N` and `ε ∈ {±1}` with `ε·σ_v A_{vu} σ_u ≥ 0` for all `u,v`. Then for all `τ,x,y`:
`(A^τ)_{yx} = ε^τ σ_y σ_x (|A|^τ)_{yx}`. Consequently response support equals structural walks,
`|ρ|` satisfies RG-3, and **any hidden (cancelled) dependency requires that neither `A` nor `−A`
is balanced.** *PROVED.*

*Proof.* With `S = diag(σ)`, `S A S = ε|A|`, so `A^τ = ε^τ S |A|^τ S`. ∎

*Criterion (repaired after review).* `A` is balanced up to sign iff for some `ε` every closed
walk `W` of the underlying undirected signed multigraph has sign product `ε^{|W|}`. For `ε = 1`
this is Harary's balance theorem (CLASSICAL, 1953); the identity above is signature similarity
from qualitative matrix theory (CLASSICAL). The first version quoted the `ε = 1` criterion for
the `ε`-notion, which is wrong for `A = [[−1]]`. The referee checked the repaired criterion on
all 19 683 sign tables of size three.

*CORROBORATED:* the PI proved the case `ε = 1`; the Causal Geometer independently proved the
statement with the global sign (its CG-13(2)). The module's `switching_function` tests `ε = 1`;
`is_balanced_up_to_sign` tests both.

*The converse fails:* a directed 4-cycle with one negative edge is not balanced up to sign, yet
it has at most one walk of each length between two nodes, so nothing can cancel. (The negative
directed 3-cycle, used in the first version, is unbalanced for `ε = 1` but balanced for
`ε = −1`.) Imbalance is necessary for hidden dependency, not sufficient. An exact criterion for
*possible* cancellation at a given `(x,y,τ)` in terms of the sign pattern is open; it is
semi-algebraic in the magnitudes.

---

## 5. Gauge: which magnitudes are physical and which are units (RG-5)

The founding note insists that "relatively relevant" needs calibrated units. The following makes
the unit freedom exact.

**RG-5 (unit changes are potentials; the invariant content is holonomy).** *PROVED;* part (b) is
the CLASSICAL diagonal-similarity theorem, reproved here (attributed from memory to
Engel–Schneider and Fiedler–Pták; the exact statements were not checked against the sources);
(c) is the dimension of the cycle space (Kirchhoff); the "holonomy" language is switching of
gain graphs (Zaslavsky). The weakening of strong connectivity in (b) is the referee's (R-14).

(a) A change of node units `z' = Dz` (`D` positive diagonal) gives `A' = DAD^{-1}` and
`ρ'_τ(x→y) = (d_y/d_x)·ρ_τ(x→y)`. In log form every directed distance shifts by a potential:
`D'(x,y) = D(x,y) + φ(x) − φ(y)`.

(b) Let `A, B` have the same zero pattern and entry signs, with ratios `r(u→v) = B_{vu}/A_{vu}`.
Then `B = DAD^{-1}` for some positive diagonal `D` **iff** the product of `r^{±1}` around every
closed walk of the underlying undirected multigraph is `1` (exponent `−1` when an edge is
traversed backwards). If every edge lies on a directed cycle (in particular if the digraph is
strongly connected) it suffices that all *directed* cycle products of `A` and `B` agree.

(c) The space of positive weightings of a fixed pattern modulo unit changes has dimension
`b₁ = |E| − |V| + c` (first Betti number; `c` = number of weak components).

*Proof.* (a) is a direct computation. (b, ⇒) each ratio is `d_v/d_u`, which telescopes around a
closed walk. (b, ⇐) on each weak component fix a root with `d = 1` and define `d_v` as the
product of ratios along any undirected walk from the root; the hypothesis makes this
well defined, and then `d_v = d_u · r(u→v)` on every edge. For the strongly connected case,
replace each backward traversal of an edge `u→v` by a directed path `P` from `v` to `u`; the
directed cycle `u→v∘P` has ratio product `1`, so `P` carries `r(u→v)^{-1}` and the product is
unchanged; the resulting directed closed walk splits into directed cycles, each with product `1`.
(c) In logarithms the unit action is the coboundary `δφ(u→v) = φ_v − φ_u`, whose kernel is the
locally constant functions (dimension `c`); its cokernel has dimension `|E| − (|V| − c)`. ∎

**Corollaries (each with an executable receipt).**

- *One-way comparisons are not unit-free.* "Source `x` is more relevant to `y` than source `z`
  is" can be reversed by a unit change at `x` (receipt: weights `2,1` into a common target,
  rescale the first source by `4`). The note's requirement of *transported calibration* is
  therefore necessary, not cautious.
- *Unit-free quantities:* round-trip products `ρ_s(x→y)·ρ_t(y→x)`, lag ratios
  `ρ_τ(x→y)/ρ_σ(x→y)`, ratios of parallel paths, loop gains.
- *Forest carriers have no unit-free magnitudes.* If the structure graph has no undirected cycle
  (`b₁ = 0`), every positive weighting is unit-equivalent to all ones. On a tree, relevance
  magnitudes are pure convention; only the *graph* is physical.
- *Cycle products are not enough without strong connectivity.* The acyclic diamond has no
  directed cycle, but its two parallel paths carry one unit-free ratio (`b₁ = 1`).

**The unifying remark (repaired).** Allowing signed unit changes `D ∈ diag(ℝ^×)`, `A` is
balanced up to sign exactly when `A` or `−A` is unit-equivalent to a nonnegative carrier. The
unit-free content of a carrier is a holonomy class on the cycle space of its structure graph: a
positive part (unit-free magnitudes) and a sign part (frustration). **Both the
calibration-independent magnitudes and the possibility of cancelled, hidden dependencies live in
the same place — the loops and parallel paths of the carrier.** A tree-shaped carrier has
neither.

---

## 6. The unseen causal horizon (HQ-1 … HQ-4)

**Setting.** A finite network: nodes `N`, value sets, **synchronous** updates
`z_{t+1,v} = f_v(z_t|_{pa(v)})`, dependency digraph `G` with an edge `u → v` for each declared
parent. An observer reads sensor nodes `S ⊆ N` at every step, *before* the update, and may
override actuator nodes; the override applied at time `t+1` is a function of the sensor record
through time `t` (a *lawful record-driven policy*, possibly with memory). `d` is directed
distance in `G`; `d(H,·) = min_{h∈H} d(h,·)`. Comparing two runs means two preparations of the
carrier (resettable or independent copies); on a single unresettable copy the comparison is
counterfactual.

**HQ-1 (cone lemma with an acting observer).** Let two initial states differ only on `H ⊆ N`,
and run the same deterministic policy on both. Then the two sensor records through time `t` are
identical for every `t < d(H,S)`, and the two states agree at every node `v` with `d(H,v) > t`
for every `t ≤ d(H,S)`. *PROVED; finite propagation is CLASSICAL, the care is in the acting
observer.* The referee attacked it with 300 random nonlinear networks, memoryful policies,
sensors that are actuators and `H` meeting `S`; it survived, and the range `t ≤ d(H,S)` for
states is the referee's sharpening (R-5).

*Proof.* Induction on `t`. At `t=0` the states differ only on `H`. If the claim holds at `t` and
`t < d(H,S)`: the records through `t` agree, so the policy applies the same overrides in both
runs; a node `v` with `d(H,v) > t+1` has all parents at distance `> t`, hence equal inputs, hence
equal values (or the same override). ∎

*Boundaries (each is a hypothesis, not a defect).* After detection the observer itself is a
causal channel from sensors to actuators, which is not an edge of `G`; with sequential
(Gauss–Seidel) updates the chain `h→v→s` is detected one step early; randomised policies need
shared coins, otherwise the conclusion holds only in law.

**HQ-2 (effect versus detection: the warning margin).** Define the structural lead time
`m = d(H,y) − d(H,S)` for a target node `y`.

(a) *No-go.* For every carrier on `G` and every lawful policy, no record depends on the cause
before time `d(H,S)`. If `m ≤ 0`, on a carrier that realises its structural distances evidence
can never strictly precede the first effect on the target. Relative to the toolkit and to `G`.

(b) *Sharpness (repaired after review).* Let the carrier be linear and balanced up to sign with
switching signs `σ`, let the observer be **passive**, and let the two initial states differ by a
perturbation `δ₀` **aligned with the sign pattern** (`σ_h δ₀(h) ≥ 0` for all `h`). Then, for
every common initial state, the first effect at `y` occurs exactly at `d(supp δ₀, y)` and the
first sensor difference exactly at `d(supp δ₀, S)`. *PROVED:* `A^τ δ₀ = ε^τ S|A|^τ(Sδ₀)` with
`Sδ₀ ≥ 0`, so component `y` is nonzero iff a walk of length `τ` from the support reaches `y`.

*Refuted first version:* "on every nonnegative linear carrier effect and detection times equal
the structural distances". Receipts (referee R-6, replayed in
`test_mixed_sign_cause_refutes_the_unrepaired_sharpness_claim`): with `h₁→y`, `h₂→y` and
perturbation `(+1, −1)` the target never moves although `d(H,y) = 1`; and an open-loop policy
clamping an actuator on the only route blocks the effect for good.

(c) *Signed carriers.* For a passive observer, effect and detection times are never earlier than
the structural distances and can be strictly later, or never (RG-1c).

This is the exact form of "it matters before the observer has evidence that it matters": it is
a statement about **which sensor is structurally closer to the cause than the target is**, valid
as a lower bound for every policy and attained under the hypotheses of (b).

**HQ-3 (a model-cone violation is a finite witness of a hidden wire — repaired).** Let the
observer's model have dependency graph `G_M` on the same nodes, with the same synchronous time
convention. Suppose two preparations differ **exactly** on `{x}`, and `y` differs between them
at some lag `τ` with

```
τ < d_M(x,y)      and      ( τ ≤ d_M(x,S)   or   the policy is passive / open-loop ).
```

Then the source has a dependency edge absent from `G_M`. *PROVED* by HQ-1 applied to the model,
contrapositive.

*Refuted first version:* the same statement without the second condition. Receipt (referee R-7,
replayed in `test_an_acting_observer_can_fake_a_cone_violation`): model = source with edges
`x→s`, `a→y`; a policy copying the sensor `s` into the actuator `a` makes `y` respond at lag 3
although `d_M(x,y) = ∞` and there is no hidden edge. The apparent hidden wire is the observer.
Two further ways the witness can be fake, each excluded by a stated hypothesis: a preparation
that also perturbs another declared node, and a time-convention slip (sensors read after the
update). The converse fails as before: a hidden wire can cancel, be gated off, or lie beyond
every available intervention; then it is `UNVERIFIED`, not absent.

**HQ-4 (the chain — repaired).** For an observation `q`, source nodes `x,y`, and a carrier on
`G_C`:

```
d_Q∃(q x, q y)  ≤  d_C(x, q⁻¹(q y))  ≤  d_C(x,y)  ≤  T_eff(x→y)   (passive or open-loop observer),
d_C(x, q⁻¹(b))  ≤  d_Q∀(q x, b).
```

The first inequality is QG-2 and is an equality **for all reports `b` iff the observation is
exact at `x`** (QG-3): exactness concerns the distance to a *fibre*, not to a chosen
representative. *Refuted first version:* "`d_Q∃(q x,q y) = d_C(x,y)` iff cost-exact"; receipt
(referee R-4): single edge `0→2`, labels `(0,1,1)`: exact at every start, yet
`d_Q∃(q0,q1) = 1 < ∞ = d_C(0,1)`. The third inequality is HQ-1 and needs a passive or open-loop
observer (or `τ ≤ d(x,S)`), by the receipt under HQ-3; it is an equality under the hypotheses of
HQ-2(b). The last line is QG-4.

**Boundary.** These are statements about declared finite networks with synchronous updates. No
superluminal influence, measurement postulate or physical horizon is modelled. Quantum
correlations without signalling are *not* edges of `G`: a carrier whose marginal statistics do
not respond to a remote intervention has no response edge there, whatever its joint statistics
(the founding note's adversary 3 stands).

---

## 7. What failed (receipts in [COUNTERMODELS.md](COUNTERMODELS.md))

| Conjecture | Verdict | Receipt |
|---|---|---|
| Net response always generates a directed path geometry | REFUTED | signed diamond: `R(x,y)R(y,z)=1`, `R(x,z)=0` |
| A live structural path implies a response at some lag | REFUTED for signed carriers; PROVED for carriers balanced up to sign | signed diamond; RG-4 |
| Imbalance implies some cancellation | REFUTED | negative directed 4-cycle |
| Equal directed cycle products imply unit-equivalence | REFUTED when some edge lies on no directed cycle | acyclic diamond with parallel-path ratio 2 |
| "x is closer to y than z is" is observer-independent | REFUTED without transported calibration | unit change reverses the order |
| Coarse-graining can hide a causal ancestor | REFUTED for may-quotients (QG-5); **TRUE for must-quotients** | `q=(0,0,1)`, edge `1→2` |
| A may-quotient path lifts from the selected start | REFUTED (inherited: SUCC three-state ghost) | PAP-04 |
| *First-version claims refuted by the referee* | see COUNTERMODELS §5 | `tests/test_observatoris_referee_receipts.py` |

**Next falsification opportunities.** (i) Nonlinear carriers: find the right replacement for
balance (monotone systems are cancellation-free but can still *gate*; see the finite-observer
report). (ii) Stochastic carriers: is there a must/may sandwich for hitting probabilities, where
the value algebra is not idempotent? (iii) An exact sign-pattern criterion for possible
cancellation at a given lag. (iv) An intercept theorem: when can the observer act in time, given
that acting makes it a causal channel?
