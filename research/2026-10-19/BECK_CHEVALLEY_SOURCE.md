# A source-indexed Beck–Chevalley theorem for finite carriers

**Date:** 2026-10-19
**Author:** vandettalm@gmail.com (Academic Main V Thinker-Dome, Moonshot A)
**Research parent:** `origin/main` at `455600a2e013895c36238a3a97e0f470fd7ba197`
**Research branch:** `research/amv-moonshot-a-beck-chevalley-2026-10-19` (non-main; not merged, not pushed)
**Code:** `observational_succ/beck_chevalley_source.py`
**Tests:** `tests/test_beck_chevalley_source.py` (25 tests, all green)
**Lineage:** extends the existential-support / descent intuition of PR #188
(`observational_succ/meta_choice_descent.py`,
`research/2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md`) — specifically its
distinction between *formal compatibility* and *actual source realization*.

---

## 0. One-paragraph summary

The Beck–Chevalley condition for the existential-image left adjoint is a
**CLASSICAL** theorem; across every pullback (cartesian) square in a regular
category — here the category of finite sets — base change commutes with
existential quantification. This note reproves the finite case by exhaustive
predicate comparison (no new categorical theorem is claimed), exhibits the
smallest inhabited non-cartesian square on which the equality **fails**, gives an
exact worked cartesian example on SUCC clock quotients `Z/mZ → Z/nZ` with
explicit witness transport, and introduces one **new-to-project synthesis**
(not a theorem): a *source-realization* interface that separates the formal
existential (a truth value) from a certificate backed by an **actual source
element**. The firewall exhibit is a square on which the formal Beck–Chevalley
equality is **preserved** while a specific realization certificate is **broken**.
This is RH-independent; it touches no RH / Weil / Schur content.

---

## 1. Domain, definitions, quantifiers

**Domain.** Finite sets (carriers), total functions between them (exact
dict-maps), and Prop-valued predicates on carriers represented by their support
(the True-set, a subset). All data is finite and exact — no floats, no
randomness, no sampling.

**Carrier.** An ordered tuple of distinct hashable elements (a finite set with a
declared enumeration order; the order is used only to make witness selection
deterministic).

**Predicate.** For a carrier `X`, a predicate `F` is a subset `F ⊆ X`;
`F(x)` holds iff `x ∈ F`. Equality of predicates is set equality of supports.

**Existential pushforward (`exists_pushforward(q, F)`).** For `q : S → O` and
`F ⊆ S`,
> `(∃_q F)(o)  ⇔  ∃ s ∈ S.  q(s) = o ∧ F(s)`,
i.e. `∃_q F = q(F)`, the image of `F` under `q`, a subset of `O`.

**Pullback / substitution (`pullback(g, G)`).** For `g : O' → O` and `G ⊆ O`,
> `(g* G)(o') = G(g(o'))`,
i.e. `g* G = g⁻¹(G)`, a subset of `O'`.

These are the standard adjoints `∃_q ⊣ q*` (verified exhaustively in
`test_existential_pullback_adjunction`: `∃_q F ⊆ G ⟺ F ⊆ q* G` for all `F, G`).

**Square.** Four carriers and four maps
```
        S' --g'--> S
        |          |
       q'          q
        v          v
        O' --g---> O
```
with `g' : S' → S`, `q' : S' → O'`, `q : S → O`, `g : O' → O`. The square's one
law is **commutativity** `g ∘ q' = q ∘ g' : S' → O` (`is_commutative`).

**Cartesian (pullback) square (`is_cartesian`).** The square commutes **and**
the canonical comparison `φ : S' → S ×_O O', s' ↦ (g'(s'), q'(s'))` is a
bijection onto the fiber product `S ×_O O' = {(s, o') : q(s) = g(o')}`. Over
finite carriers this is decided by an exact element count plus image comparison.

---

## 2. The classical theorem (status: CLASSICAL — academic novelty NOT asserted)

**Beck–Chevalley condition (existential, pullback squares).** In a regular
category, for every pullback square as above and every predicate `F ⊆ S`,
> `g*(∃_q F)  ≅  ∃_{q'}(g'* F)`   as subobjects of `O'`,
and in the Prop-valued (subobject) setting the comparison is an **equality**.

**References.** Mac Lane & Moerdijk, *Sheaves in Geometry and Logic*, §I.9
(the Beck–Chevalley condition and its role in hyperdoctrines / the internal
logic); Jacobs, *Categorical Logic and Type Theory*, §1.9. The finite-set case
is a textbook instance; nothing here is new mathematics.

**Hypotheses (load-bearing).** (H1) the square commutes; (H2) the square is
**cartesian** (a pullback). H2 is exactly what the counterexample in §3 drops.

**Status: CLASSICAL.** Our only contribution at this layer is a *finite decision
procedure*: `beck_chevalley_holds_all(square)` compares both sides over the
**entire** powerset of `S` (complete for finite carriers), and
`test_cartesian_implies_beck_chevalley_exhaustive` verifies, over **all**
commutative squares with carriers of size ≤ 2, that cartesian ⟹ equality-for-all
-`F`, while at least one non-cartesian square genuinely fails (so the test
discriminates). This is verification, not a new theorem.

---

## 3. REQUIRED counterexample: smallest inhabited non-cartesian failure

**Found by exhaustive search** (`find_minimal_counterexample(max_elements=4,
allow_empty=False)`) over finite carriers, each of size in `[1, 4]`, ordered by
(1) ascending total element count `|S|+|S'|+|O|+|O'|`, then (2) ascending
`(|O|,|O'|,|S|,|S'|)`, then (3) the product order over maps `(q,g,g',q')`, then
(4) ascending predicate order. The first commuting, **non-cartesian**,
equality-breaking square returned is (total **5** elements):

```
        S' = {t0} --g'--> S = {s0, s1}
        |                 |
       q'                 q
        v                 v
        O' = {p0} --g---> O = {o0}

        q  : s0 ↦ o0,  s1 ↦ o0
        g  : p0 ↦ o0
        g' : t0 ↦ s0
        q' : t0 ↦ p0
        F  = {s1}
```

* Commutes: `g(q'(t0)) = g(p0) = o0 = q(s0) = q(g'(t0))`. ✓
* **Not cartesian:** fiber product `S ×_O O' = {(s0,p0), (s1,p0)}` has 2
  elements, but `S'` has 1; `φ` is not surjective. ✓
* **LHS** `g*(∃_q F)`: `∃_q{s1} = {o0}`; `g*{o0} = {p0}`.  → `{p0}`.
* **RHS** `∃_{q'}(g'* F)`: `g'*{s1} = {s' : g'(s') ∈ {s1}} = ∅` (because
  `g'(t0)=s0 ∉ F`); `∃_{q'}∅ = ∅`.  → `∅`.
* **`{p0} ≠ ∅` — Beck–Chevalley FAILS.** (`test_counterexample_exact_shape`,
  `test_counterexample_is_noncartesian_and_breaks_equality`.)

**Minimality.** Every total-4 inhabited square is all-singleton, hence
trivially cartesian, hence satisfies the equality; the search exhausts total 4
before returning at total 5 (`test_counterexample_is_minimal_total_five`). The
minimum is therefore **5 elements over inhabited carriers**.

**Degenerate smaller witness if empty carriers are admitted.** With
`allow_empty=True` the search returns a strictly smaller (total **3**) witness:
`S = {s0}, O = {o0}, O' = {p0}, S' = ∅`, `q(s0)=o0`, `g(p0)=o0`, `F = {s0}`,
giving `LHS = {p0}` but `RHS = ∅` (vacuous, because `S'` is empty)
(`test_empty_carrier_degenerate_minimum`). We report the inhabited minimum as
the **primary** counterexample under the SUCC carrier-inhabitation reading
(every declared source is inhabited); the empty case is recorded for
completeness because it is a *vacuous* RHS, not an instructive BC failure.

---

## 4. Worked cartesian example on SUCC clock quotients (status: CLASSICAL instance)

`clock_quotient_square(m, n, mp)` requires `n | m` and `n | mp` and builds the
pullback of the two canonical reductions over the shared base `Z/nZ`:
```
        S' = Z/mZ ×_{Z/nZ} Z/mpZ --g'--> S = Z/mZ
        |                                |
       q' = snd                          q = (· mod n)
        v                                v
        O' = Z/mpZ ----- g = (· mod n)-> O = Z/nZ
```
`S'` is the genuine fiber product `{(x, y) ∈ Z/mZ × Z/mpZ : x ≡ y (mod n)}`
with projections `g' = fst`, `q' = snd`; it is cartesian by construction and
`is_cartesian` re-certifies it.

**Instance `m=4, n=2, mp=4`** (`q, g = reduction mod 2`): `|S'| = 8`,
`is_cartesian = True`, and `beck_chevalley_holds_all = True`
(`test_clock_square_cartesian_and_bc_holds_all`; also checked for
`(6,3,6),(6,2,4),(4,2,2),(9,3,3),(12,6,6)`).

**Explicit witness transport.** Take `F = {1, 3} ⊆ Z/4` (the odd residues) and
the point `o' = 1 ∈ O' = Z/4`.
* LHS witness: the least `s ∈ F` with `q(s) = g(o')`. Here `g(1) = 1 (mod 2)`
  and `q(1) = 1`, so `s = 1` certifies `1 ∈ g*(∃_q F)`.
* RHS witness: transport across `φ⁻¹` to `s' = (1, 1) ∈ S'`, which satisfies
  `g'(s') = 1 = s` and `q'(s') = 1 = o'`, certifying `1 ∈ ∃_{q'}(g'* F)`.

`witness_transport(square, F, 1) = (1, (1,1))`
(`test_clock_witness_transport_explicit`). For a cartesian square the transport
never fails whenever the LHS holds (`test_transport_matches_predicate_membership`).

---

## 5. Candidate novelty: the source-realization interface (status: new-to-project SYNTHESIS — NOT a theorem)

The formal `∃` records only a **truth value** (a subobject of `O`). SUCC's
standing discipline (FOUNDATIONS.md; the NO_GHOST supplement; PR #188 §source
realization) insists on separating *formal compatibility* from *actual source
realization*. We make that separation operational for Beck–Chevalley.

**Definition (realization certificate).** A `RealizationCertificate` for
`o' ∈ ∃_{q'}(g'* F)` is an **actual element** `s' ∈ S'` with `q'(s') = o'` and
`g'(s') ∈ F` (`realize_right` returns the least-index such `s'`, a deterministic
witnessed choice — see §6).

**Definition (formal vs. source-realized fiber witnesses).** For the LHS,
`formal_fiber_witnesses(square, F)` is the set of pairs `(s, o') ∈ S ×_O O'`
with `s ∈ F` — each a legitimate formal existential witness to
`o' ∈ g*(∃_q F)`. The pair is **source-realized** iff some `s' ∈ S'` has
`φ(s') = (s, o')`. `realization_firewall_breaks` is True iff some formal witness
is **not** source-realized — a *ghost witness*.

**Firewall exhibit (`firewall_square`).**
```
        S' = {t0} --g'--> S = {s0, s1}        q : s0, s1 ↦ o0
        |                 |                   g : p0 ↦ o0
       q'                 q                   g': t0 ↦ s0
        v                 v                   q': t0 ↦ p0
        O' = {p0} --g---> O = {o0}            F = {s0, s1}
```
* **FORMAL Beck–Chevalley HOLDS at this `F`:** `LHS = RHS = {p0}`
  (`beck_chevalley_holds(square, F) = True`).
* **The realization certificate is BROKEN:** the formal fiber witnesses are
  `{(s0,p0), (s1,p0)}`, but only `(s0,p0)` is source-realized (via `t0`).
  `(s1,p0)` — a bona fide formal witness (`s1 ∈ F`, `q(s1)=o0=g(p0)`) — is a
  **ghost**: no element of the source carrier `S'` lies over `s1`.
  `realization_firewall_breaks(square, F) = True`
  (`test_formal_bc_holds_but_realization_broken`, `test_ghost_witness_identity`).

**Reading.** Preservation of the formal existential (the Prop) does **not**
entail that every formal witness is backed by a genuine source element. Only a
**cartesian** square guarantees that `φ` is a bijection, so that every
fiber-product witness is source-realized; on a cartesian clock square the
firewall never breaks (`test_cartesian_square_has_no_firewall_break`). The
realization interface is the thing that *detects the gap* when the square is not
cartesian even though the truth value happens to agree. This interface — not the
Beck–Chevalley theorem — is the only candidate novelty here, and it is labeled
**new-to-project synthesis**, not a new mathematical theorem.

---

## 6. Firewall / choice discipline (constructive, witnessed)

* **No floats, no randomness.** All carriers/maps are exact finite data; the
  module scan test (`test_source_has_no_float_random_or_rh`) asserts the source
  contains no `import random`, `random.`, `float(`, `numpy`, `math.sqrt`,
  `.seed(`, `riemann`, or `zeta(`.
* **No unrestricted choice.** Every witness selection (`realize_right`,
  `witness_transport`) is a **deterministic least-index search** over an
  explicitly ordered finite carrier — the dependent/witnessed form of choice
  (a projection out of a decidable finite Σ), which is immediate and needs no
  `Classical.choice` or excluded middle. None is used; none is required. (Pinned
  by `test_realizer_is_deterministic_least_index`.)
* **RH PROVED: NO.** No RH / Weil / Schur / zeta content; no archival or frozen
  file touched (in particular `formal/EODCS_RelationalChoice.lean` is
  untouched); no YEAN interaction.
* **Source labels are declared contracts**, not independent source
  authentication (consistent with `meta_choice_descent.py`).

---

## 7. Adversarial countermodels (crucible)

* **"Base change always commutes with ∃."** Receipt: the §3 counterexample
  (`{p0} ≠ ∅`). The claim needs H2 (cartesian); dropping it breaks the equality.
* **"If the formal BC equality holds, the witness is source-backed."** Receipt:
  the §5 firewall exhibit — equality holds, yet `(s1,p0)` is a ghost. Formal
  truth preservation ⇏ realization.
* **"The counterexample is an artifact of empty domains."** Receipt: the
  primary counterexample (§3) has **all carriers inhabited** (total 5); the
  empty-`S'` witness is reported separately and flagged as vacuous.
* **"This is a new theorem of topos theory."** Refused at the source: the
  Beck–Chevalley condition is CLASSICAL (Mac Lane–Moerdijk §I.9). Only the
  realization interface is labeled new-to-project, and only as synthesis.

---

## 8. The EXACT open obligation

The realization interface is, at present, a **detector**, not a **theorem**.

**Call a square *realization-faithful* at `F`** iff the formal Beck–Chevalley
equality `g*(∃_q F) = ∃_{q'}(g'* F)` holds **and** every formal fiber witness
`(s, o')` with `s ∈ F` is source-realized by an actual element of `S'`
(equivalently: `φ` restricts to a surjection onto `{(s,o') ∈ S ×_O O' : s ∈ F}`);
*realization-faithful* (unqualified) iff this holds for every `F`.

**(DEMONSTRATED, with receipt) The realization-faithful class is STRICTLY LARGER
than the cartesian class.** `realization_faithful_noncartesian_square()` is the
"redundant realizer" square
```
        S' = {t0, t1} --g'--> S = {s0}        q : s0 ↦ o0
        |                     |               g : p0 ↦ o0
       q'                     q               g': t0, t1 ↦ s0
        v                     v               q': t0, t1 ↦ p0
        O' = {p0} ----g-----> O = {o0}
```
whose fiber product is the single pair `{(s0, p0)}` while `S'` has **two**
elements over it. So `φ` is surjective but **not** injective — the square is
**not cartesian** — yet `beck_chevalley_holds_all = True` and
`realization_firewall_breaks(·, F) = False` for every `F`
(`test_realization_faithful_class_strictly_larger_than_cartesian`). Faithfulness
forbids **ghost** (unrealized) witnesses but tolerates **redundant**
(over-realized) ones; cartesianness forbids both. Hence the two classes are
distinct: faithful ⊋ cartesian. (Status of *this* sub-claim: **DEMONSTRATED** on
the exhibited finite square; it is an exact receipt, not a general structure
theorem.)

**(DEMONSTRATED, elementary) Characterization of realization-faithfulness.** A
finite commutative square is realization-faithful (for all `F`) **iff** its
comparison map `φ` is **surjective** onto the fiber product `P = S ×_O O'`
(`is_realization_faithful` ⟺ `comparison_is_surjective`). So faithfulness is
exactly *cartesian minus the injectivity clause*: it forbids **ghost**
witnesses but tolerates **redundant** over-realizers.

*Proof.* (⇐) Suppose `φ` is onto `P`. For any commutative square `RHS ⊆ LHS`
always holds: if `o' = q'(s')` with `g'(s') ∈ F`, then `(g'(s'), o') = φ(s') ∈ P`
and `g'(s') ∈ F`, so `o' ∈ LHS`. For `LHS ⊆ RHS`: if `o' ∈ LHS` there is
`(s, o') ∈ P` with `s ∈ F`; surjectivity gives `s' ∈ S'` with `φ(s') = (s, o')`,
so `g'(s') = s ∈ F` and `q'(s') = o'`, whence `o' ∈ RHS`. Thus formal BC holds
for every `F`; and every formal witness `(s, o') ∈ P` has a preimage, so no
ghosts — faithful. (⇒) Faithfulness at `F = S` requires every `(s, o') ∈ P`
(all of them, since `s ∈ S`) to be source-realized, i.e. in `image(φ)` — exactly
`φ` onto `P`. ∎

**Corroboration.** Exhaustively verified with **zero** mismatches over all
**72,270** commutative squares with carriers of size ≤ 3
(`test_faithfulness_equals_comparison_surjectivity_exhaustive` runs the size-≤2
sweep in the suite; the size-≤3 run is a documented one-off). Status of this
proposition: **DEMONSTRATED (elementary); academic novelty NOT asserted** — it
is the standard observation that the ∃ Beck–Chevalley condition is controlled by
surjectivity of the comparison, recast through the source-realization lens.

**The precise remaining open obligation:**

> **(OPEN) SUCC source-indexed payoff and scope.** The formal-vs-realized split
> and the surjectivity characterization are proven here only for the Prop-valued
> support in **FinSet**. Open: (a) does the realization-faithful class (strictly
> between cartesian and formal-BC) license any SUCC source-indexed *descent*
> consequence that mere formal Beck–Chevalley does not — e.g. a source-certified
> section-gluing statement that fails under redundant-but-not-ghost realizers
> are suppressed? and (b) does the characterization survive the move from
> Prop-valued support to the carrier-indexed *set*-valued fibers of
> `formal/EODCS_CarrierIndexed.lean` / PR #188, where `∃_q` is a genuine
> dependent sum rather than an image? Neither is settled here.

Status of the obligation: **OPEN / UNVERIFIED**. What is NOT open: the finite
Prop-valued characterization (DEMONSTRATED above) and the strictness of
faithful ⊋ cartesian (receipt: the redundant-realizer square).

**Next falsification opportunity.** Port `Square` / `is_realization_faithful` to
set-valued fibers and re-run the equivalence sweep: if faithfulness there no
longer coincides with comparison-surjectivity, that refutes the naive lift (a
receipt); if it does coincide, attempt the general (non-finite) proof. Then
probe (a) by constructing a source-indexed gluing instance and checking whether
a redundant-realizer square and a cartesian square give the same certified
section.
