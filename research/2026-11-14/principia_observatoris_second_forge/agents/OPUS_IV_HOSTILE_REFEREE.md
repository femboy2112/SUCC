# OPUS IV — Hostile referee report on the Second Forge

**Operation Principia Observatoris — Second Forge.** Date 2026-11-14. This is an adversarial review for the principal investigator (PI). Nothing here is merged or promoted in the ledger. Method: steelman, then crucible, then verdict ([docs/METHOD.md](../../../../docs/METHOD.md)).

- **Receipts:** `tests/test_observatoris_referee_receipts.py`. It has 29 tests, exact `Fraction` arithmetic and stdlib only. Two of the tests compile Lean scratch files against the pinned Lean 4.14.0 and skip themselves if that compiler is missing.
- **Command:** `python -m unittest tests.test_observatoris_referee_receipts -v`.
- **Result on this machine:** 29 tests, OK, about 7.5 s.
- **Test names:**
  - `R*_refutes_*` passes when the defect is present.
  - `R*_survives_*` passes when the attacked statement, or my repaired statement, held on every model tried.
  - `R*_vacuous_*` shows that an existing test cannot fail.
- **Files under review that still pass:** `tests/test_observatoris_response_geometry.py`, `tests/test_observatoris_classical_appearance.py` and `tests/test_observatoris_finite_horizons.py` (88 tests, OK). I did not run the full suite.

**Identifiers.** The package was edited while I reviewed it (commits `993066fa`, `99f5f198` and later working-tree changes).

- I use the *current* identifiers. `QG-n` in CAUSAL_GEOMETRY.md was called `CG-n` when I started.
- Line numbers refer to CAUSAL_GEOMETRY.md as it stood at the end of the review.
- "Geometer CG-n" (OPUS_II) was outside my brief. I did not review it, except RG-6, which the PI imported into CAUSAL_GEOMETRY.md.

**Independence.** I did not look for or use the external "Astra" campaign.

---

## Findings

### R-1. QG-5 "an honest coarse-graining has no unseen ancestors" (CG.md:179–187)

**Verdict: SURVIVES. It is a near-tautology, so I give its strongest correct form.**

- **Steelman.** QG-5 is a corollary of QG-2. It is "PROVED" only because the observer's geometry is *defined* as the may-quotient of the very source the observer cannot see. The content that is not a tautology is a universal property.
- **Repaired statement (true in every `LaxQuantale`).** Let `G` be any value relation on the report set `Y`. The following are equivalent:
  - (i) no unseen ancestors at any horizon: `R*(x,y) ≤ G*(q x, q y)` for all `x, y`;
  - (ii) every source edge is covered: `R(u,v) ≤ G*(q u, q v)`;
  - (iii) `Q∃ ≤ G*` pointwise.
- **Proof.** (i)⇒(ii) because edges are bounded by the closure. (ii)⇔(iii) by the definition of the supremum. (iii)⇒(i) because `z ↦ G*(q x, q z)` is an `R`-potential; apply QG-1. This is the QG-2 proof with `G*` in place of `Q∃*`.
- **What it buys.** `Q∃*` is the *least* geometry without quasars, and a quasar is exactly an uncovered source edge.
- **Receipt.** `test_R01_survives_strongest_qg5_quasar_free_iff_every_edge_covered` is exhaustive over all loop-free 3-node sources, every labelling and every observer graph (4 928 cases). It also exhibits geometries without quasars that are strictly coarser than `Q∃`.
- **Classical.** This is the universal property of existential abstraction (simulation preserves reachability).

### R-2. §2 "Ghosts … no experiment is needed; quasars … no invariant of the model can reveal it" (CG.md:189–202)

**Verdict: OVERCLAIM. The asymmetry is between data regimes, not between failure types.**

- The ghost detector (a closed set) is a *source-level* object.
- **Receipt** (`test_R02_*`, the same models as the PI's C-9): `R_a = {1→2, 1→0}` and `R_b = {0→1, 1→2}` with `q = (0,0,1)`. They have identical `Q∃` and `Q∀`, hence identical closures. Start 0 is a ghost under `R_a` and exact under `R_b`. So an observer who holds only the quotient data cannot detect a ghost without an experiment.
- Conversely, anyone who holds the source table detects a quasar without an experiment, by the uncovered-edge test of R-1.
- **Repair.** "With the source table, both failures are decidable by computation. With only model or quotient data, neither is: ghosts need a contrast, and quasars need a cone violation."
- **Minor.** "Exactly two ways" holds for totally ordered value structures. Over path languages the values can be incomparable, so one pair can be a ghost and a quasar at once.

### R-3. C-6 / CG.md:432 "Coarse-graining can hide a causal ancestor — REFUTED … receipt: —"

**Verdict: MIS-LABELLED REFUTATION. It breaks the receipt rule, and the conjecture is true for the package's own must-quotient.**

- **Receipt** (`test_R03_*`): `q = (0,0,1)` with the single edge `1→2`. Then `Q∀(a,b) = ⊥`, so `d_∀ = ∞`, while `d_C(1,2) = 1`. The must-quotient of QG-4 is a coarse-graining built from the source alone, and it hides a one-step ancestor.
- The sentence at CG.md:196, "cannot arise from coarse-graining alone", is false for must-coarse-graining.
- **Repair.** Mark C-6 "REFUTED for may-quotients (receipt: QG-5); TRUE for must-quotients (receipt R-3)".

### R-4. HQ-4 "first inequality … equality iff cost-exactness, QG-3" (CG.md:410)

**Verdict: REFUTED.**

- **Receipt** (`test_R04_*`): the single edge `0→2` with labels `(0,1,1)`. The quotient is exact at every start, yet `d_Q∃(q0, q1) = 1 < ∞ = d_C(0,1)`.
- Exactness equates `d_Q∃(q x, b)` with the distance to the *fibre* `d_C(x, q⁻¹b)`, not with the distance to a chosen representative.
- **Repair** (checked in the same test): `d_Q∃(q x, b) = d_C(x, q⁻¹ b)` for all `b` iff `ExactAt x`. For a given `y`, only `d_Q∃ ≤ d_C(x, q⁻¹ q y) ≤ d_C(x,y)` holds.

### R-5. HQ-1, the cone lemma with an acting observer (CG.md:362–374)

**Verdict: SURVIVES within its declared setting, and it can be sharpened.**

- **What I tried** (`test_R05_*`): 300 random *nonlinear* networks on 2–6 nodes, with values 0–2 and self-loops allowed. Sensors were also actuators, `H` could meet `S` or the actuators, and policies had memory (they depended on the whole record).
- Records always agreed for `t < d(H,S)`.
- **Sharpening.** States agree off the cone for every `t ≤ d(H,S)`, one step further than stated. The inductive step at `t+1` only uses records through `t`.
- **Outside the setting (boundary, not a defect):**
  - With sequential (Gauss–Seidel) updates, the chain `h→v→s` is detected at `t = 1 < 2` (`test_R05b_*`).
  - Randomised policies need shared coins (a coupling); otherwise the conclusion holds only in law.
- **Test gap.** The existing `test_records_cannot_depend_on_the_cause_before_the_bound` runs no policy at all. It does not test the acting observer, which is where HQ-1 says "the care" lies.

### R-6. HQ-2(b) "on every nonnegative (or balanced) linear carrier … effect and earliest detection times equal the structural distances exactly" (CG.md:384)

**Verdict: REFUTED as stated. It holds only for impulses, or perturbations aligned with the sign pattern, under a passive observer.**

- **Receipt 1** (`test_R06_*`): `A ≥ 0` with `h1→y` and `h2→y` (weight 1 each) and `H = {h1, h2}`. The perturbation `(+1, −1)` never reaches `y`, although `d(H,y) = 1`. The sensor still detects at `d(H,S) = 1`.
- **Receipt 2** (`test_R06b_*`): a lawful open-loop policy clamps the actuator `a` on the only route `h→a→y`. There is never an effect, although `d(h,y) = 2`.
- **Repair.** On a balanced linear carrier (`ε σ_v A_vu σ_u ≥ 0`) with a passive observer, take a perturbation `δ₀` with `σ_h δ₀(h) ≥ 0` for all `h`. Then:
  - the effect time at `y` is `d(supp δ₀, y)`;
  - the detection time is `d(supp δ₀, S)`;
  - for every initial state (the dynamics is linear).

### R-7. HQ-3 "a model-cone violation is a finite witness of a hidden wire" (CG.md:397–402), and the HQ-4 middle inequality `d_C(x,y) ≤ T_eff`

**Verdict: REFUTED as stated. This is the observer-mediated channel that HQ-1 itself warns about.**

- **Receipt** (`test_R07_*`):
  - The model equals the source: `x→s`, `a→y`, with persistence.
  - The record-driven policy copies the sensor `s` into the actuator `a`.
  - `y` first differs at lag 3, while `d_M(x,y) = ∞`. There is no hidden edge.
- The same receipt breaks `d_C ≤ T_eff` in HQ-4 when `T_eff` is measured with an acting observer.
- **Repaired HQ-3.** Assume `G_M` contains every source dependency, and two preparations differ *exactly* on `{x}`. If `y` differs at some `τ` with `τ < d_M(x,y)` and `τ ≤ d_M(x,S)`, then a hidden edge exists. The second condition is not needed for open-loop or passive policies. The proof is the sharpened HQ-1 (R-5).
- **Two further ways the claimed witness can be fake** (paper-level; each is a single extra hypothesis to state):
  - *Fat-hand preparation:* the preparation also perturbs a declared node `h` with `d_M(h,y) < τ`.
  - *Time-convention slip:* sensors are read after the update, which makes every apparent lag one step short.
- On a single unresettable copy the two-preparation contrast is counterfactual (CARRIER_RELATIVE_TARGETS §3). HQ-3 must say that it assumes resettable or independent preparations.

### R-8. QG-3 item 5: "equivalently `Q∃(R) ≤ Q∀(R*)` … equivalently 'may = must for the closure'" (CG.md:91–94)

**Verdict: REQUIRES REPAIR (off-image points).**

- The inequality form is true.
- The equality form fails whenever `q` is not surjective. On an empty fibre the must-value is the empty meet `⊤`, while the may-value is `⊥`.
- **Receipt** (`test_R08_*`): exhaustive over all Boolean relations on 3 states and all 27 maps into 3 reports.
  - Exactness ⇔ `Q∃(R) ≤ Q∀(R*)`.
  - Exactness ⇔ may = must for `R*` on the rows of the *image*.
  - When `q` is not onto, every exact case fails equality everywhere.
- **Repair.** Write "may = must for the closure **on the image of q**".

### R-9. RG-3 "For unbalanced carriers no transform of `|ρ|` can work" (CG.md:277)

**Verdict: REFUTED by the package's own example.**

- **Receipt** (`test_R09_*`): the negative directed 3-cycle is unbalanced (C-3), yet it satisfies the graded multiplicative triangle inequality for all `s, t ≤ 5` and all `γ ∈ {1, 1/2, 2}`.
- What fails the inequality is *cancellation*, not imbalance. One counterexample (the diamond) cannot carry a claim quantified over all unbalanced carriers.
- **Repair.** Take any carrier with an all-lag cancellation and any transform `φ` with `φ(0) = ∞` and `φ(r) < ∞` for `r > 0`. Then the graded triangle inequality fails for `φ(|ρ|)`.

### R-10. RG-3 "`−log` of the response is DERIVED rather than chosen … the founding note's `ℓ = log(1+1/R)` was a choice" (CG.md:273–276)

**Verdict: OVERCLAIM.**

- Supermultiplicativity of `R_T` gives the graded triangle inequality for every decreasing `φ` with `φ(ab) ≤ φ(a) + φ(b)`. That includes the founding note's own `log(1 + 1/R)`, because `1 + 1/(ab) ≤ (1 + 1/a)(1 + 1/b)`. It also includes the clamp `max(0, −log R)`.
- **Receipt** (`test_R10_*`): over 1 000 exact triples on random nonnegative carriers, three discounts and all horizon pairs.
- **Repair.** "`−log` is, up to a positive scale, the unique monotone transform that turns products into sums *exactly* (Cauchy's functional equation). The triangle inequality alone does not single it out."

### R-11. RG-3 and the summary table "Lawvere-type distance; triangle inequality is a theorem" (CG.md:18, 261–271)

**Verdict: OVERCLAIM. The family `D_T` is graded; for a fixed `T` it is not a Lawvere metric.**

- **Receipts** (`test_R11_*`):
  - Chain `x→y→z` at `T = 1`: `D_1(x,z) = ∞ > 0 = D_1(x,y) + D_1(y,z)`.
  - `A = [[2]]` gives `D(x,x) = −log 2 < 0`, and `5·e_{10}` gives `D(x,y) < 0`.
  - The chosen discount `γ` reverses which of two sources is "closer" (`γ = 1/20` versus `γ = 1`).
- **Repair.** `D(x,y) := max(0, −log sup_{τ≥0} γ^τ ρ_τ(x→y))` is a genuine `[0,∞]`-valued Lawvere quasi-metric:
  - `D(x,x) = 0`;
  - the triangle inequality follows because the supremum over all lags is supermultiplicative;
  - it still depends on `γ`, which is chosen, not derived.

### R-12. RG-1(c) "the smallest all-lag failure has four nodes" (CG.md:219)

**Verdict: REQUIRES REPAIR (scope).**

- The proof assumes `x ≠ z`.
- **Receipt** (`test_R12_*`): for self-influence at positive lags, the three-node carrier `x→w (+1)`, `x→z (−1)`, `w→x`, `z→x` has closed walks of every even length, and `(A^τ)_{xx} = 0` for all `τ ≥ 1`. Two nodes never do this (all 2×2 tables over `{−2,…,2}`).
- For `x ≠ z` the four-node claim SURVIVES. I re-checked the paper proof for all real weights, including self-loops.

### R-13. RG-4 after the `ε` update (CG.md:281–291, 345–346)

**Verdict: REQUIRES REPAIR. The statement is now internally inconsistent.**

- With the global sign `ε`, `A = [[−1]]` counts as balanced, yet:
  - (a) its only closed walk is *negative*, so the quoted "Harary 1953: every closed walk positive" no longer characterises the defined notion;
  - (b) `D A D⁻¹ = A` for every nonzero diagonal `D`, so §5's "balance is exactly unit-equivalence to a nonnegative carrier" is false when `ε = −1`.
- **Receipt** (`test_R13_*`). It also checks the repaired criterion independently on all 19 683 3×3 sign tables: `A` is balanced up to sign ⇔ for some `ε`, every closed walk `W` has sign `ε^{|W|}`.
- **Repair.** State that criterion, and write "`A` or `−A` is unit-equivalent to a nonnegative carrier".

### R-14. RG-5(b) diagonal similarity

**Verdict: SURVIVES, and can be strengthened.**

- Strong connectivity is not needed. It is enough that every edge lies on a directed cycle, equivalently that every weak component is strongly connected.
- The proof is unchanged: replace each backward traversal inside its strongly connected component.
- **Receipt** (`test_R14_*`): 150 carriers made of two disjoint strongly connected blocks.
- **Attribution.** Engel–Schneider and Fiedler–Pták are plausible, but I could not verify the exact statements from memory (UNVERIFIED — wall: no library access).

### R-15. RG-5(c) `b₁ = |E| − |V| + c`

**Verdict: SURVIVES.**

- **Receipt** (`test_R15_*`): `|E| − rank(incidence matrix)` matches on 300 random patterns, including self-loops (zero rows) and two-cycles.
- **Attribution.** The cycle-space dimension is Kirchhoff's (CLASSICAL). The "holonomy class" is classical gain-graph switching (Zaslavsky 1989). Please cite it.

### R-16. RG-6 resolvent lumpability

**Verdict: SURVIVES.**

- **Paper proof.** If `AP = PÂ`, then `(I−A)P = P(I−Â)`. Since `P` is injective, `I−Â` is invertible, and the converse follows the same way.
- **Receipt** (`test_R16_*`): 100 exact rational cases each way.
- The `(I−A)⁻¹` statement is the classical intertwining of functional calculus. The "invent and delete" receipt lives in OPUS_II, which I did not check.

### R-17. CA-6, the four-state machine matches every transcript over {X, H, Z}

**Verdict: SURVIVES for ALL words, with a complete finite certificate.**

- **Certificate** (`test_R17_*`): twelve exact identities in `ℚ^{2×2}` show that `s ↦ ρ_s` intertwines `X`, `H` and the `Z` instrument. Since the update is linear, induction on the word gives equality of transcript laws for every length.
- **Cross-check.** Three independent implementations agree on all words of length ≤ 7.
- **Attribution.** This is the one-qubit stabiliser fragment, so cite Gottesman–Knill and Spekkens' toy theory. THEOREM_FORGE now gives a state-vector proof, which this corroborates independently.

### R-18. CA-4 "ambiguity exactly `2^{min(r,t)}`" (THEOREM_FORGE.md:105)

**Verdict: REFUTED.**

- The register is *cyclic*, so prediction recovers.
- **Receipts** (`test_R18_*`):
  - `(n,r,t) = (4,2,3)` gives 2, not 4;
  - `(4,2,4)` gives 1;
  - `(4,3,2)` gives 2, not 4, and here `t ≤ r`.
- The existing test samples only `t ≤ n − r`.
- **Repair** (exhaustive for every register the module allows): the ambiguity is `2^{min(s, n−s, r, n−r)}` with `s = t mod n`.
- **Consequence.** Every finite deterministic carrier has eventually periodic ambiguity, and an invertible one returns to 1. So row 1's "✗ at long horizon" must read "✗ at some horizons".

### R-19. CA-3 "pairwise independent diagnostics … computed by tests" (THEOREM_FORGE.md:104, 123–132)

**Verdict: OVERCLAIM. The table does not exhibit pairwise independence.**

- **Receipts** (`test_R19_*`):
  - (i) The module's own `is_free_observation(window_carrier(4,2))` is **False**, because `step` counts as an instrument. The ✓ in row 1 is not computed.
  - (ii) Even granting every cell, *no* pair of diagnostics realises all four pass/fail combinations; every pair misses one.
  - (iii) "free ⇒ deterministic core" is never separated.
  - (iv) If row 2's predictive cell is read as ✗, then "predictive ⇒ aligned" is not separated either.
- **Repair.** Separate readout instruments from dynamics in the predicate. Then either add rows that realise each missing combination, or claim only "no implication except free ⇒ deterministic core, which is open".

### R-20. FH-7 autonomous horizon `n+m−1`, sharp

**Verdict: SURVIVES.**

- **Receipt** (`test_R20_*`): my own enumeration of machines (not of ρ-words), binary outputs, `n ≤ m ≤ 4`, `n+m ≤ 7`. Distinctness is certified by the length `max(n,m) + nm`.
- **Mis-attribution.** (a)+(b) are exactly Moore's `N−2` bound (FH-8) specialised to a one-letter input alphabet. The constant is CLASSICAL, not "PROVED here".

### R-21. FH-3 `n+m`, exact over GF(2)

**Verdict: SURVIVES.**

- **Receipt** (`test_R21_*`): independent enumeration with pigeonhole length `2^{n+m} + n + m`, for `n, m ≤ 3`.
- **Attribution.** `ker p + ker q = ker lcm` (FH-3d) is classical linear-recurrence theory (Lidl–Niederreiter, ch. 8). I cite this from memory.

### R-22. FH-6 "Equivalently, the surviving members are those whose deviation comes at or before index `n−1`" (OPUS_III:334)

**Verdict: REFUTED at `n = 1`, `H = 0`.**

- **Receipt** (`test_R22_*`): `b₀ ∈ LR₁` (BM order 1), but it first deviates at index `1 > 0`.
- The preceding iff survives when checked through Berlekamp–Massey (BM), not through the hard-coded formula.
- **Repair.** Add "or `H = 0`".

### R-23. Vacuous or circular existing tests

**Verdict: VACUOUS (`test_R23_*`).**

- **`test_no_learner_is_right_on_both_extremal_sequences_at_2d_minus_1`.** It asserts `not (g == a and g == b)`. That holds for every `g` because `a ≠ b`, so it cannot fail, and it tests one learner while the claim is about all learners.
- **`test_declared_dimension_admits_b_H_iff_H_le_n_minus_2`.** It compares the hard-coded `founding_b_order = H+2` with `H ≤ n−2`, which is pure arithmetic.
- **Weak, but not vacuous:**
  - `test_prediction_fails_exactly_at_the_resolution` samples only the range where the false formula holds (R-18).
  - `test_window_shift_is_free_…` asserts that the carrier is *not* free.
  - `test_quotient_distance_never_exceeds_source_distance` says "all 4-node patterns" but samples 600 at random.
  - `test_warning_margin_and_detection_bound` tests only single-node impulses, which is narrower than HQ-2(b).
  - `test_adversary_forces_any_number_of_mind_changes` tests one learner only.

### R-24. FH-9 receipts and constants

**Verdict: SURVIVES.**

- **Receipt** (`test_R24_*`): independent evaluation of the Rabin pair (first difference at `xx`, 15/64 versus 9/64) and the HMM pair (`k₀ = 3`).
- One-letter generative HMMs are all identical, so the sharpness families must use at least two letters; they do.
- My paper re-check of the `n+m−2` Rabin argument holds.
- **UNVERIFIED — wall:** whether Paz or Tzeng state `n₁+n₂−1` or `n₁+n₂−2`.

### R-25. FH-8 Moore `N−2`, Mealy `N−1`

**Verdict: SURVIVES.**

- **Receipt** (`test_R25_*`): exhaustive over all 3-state, 2-letter, binary machines. Equivalence is certified independently by pair reachability.

### R-26. Lean encoding: `LaxQuantale`, `ExactAt`, `propQ`, empty `X`, off-image `Y`

**Verdict: SURVIVES.**

- **Field-by-field check.** Every field is an inequality that a unital quantale satisfies. Omitting `one_mul_le`, antisymmetry and commutativity only weakens the hypotheses. `quotAll` is a sup of lower bounds, which is a legitimate meet. `ExactAt` is exactly prose item (1). `propQ` is the frame of propositions.
- **Receipt** (`test_R26_*`; it needs Lean): core Lean accepts two instances:
  - the reversed-order cost quantale, presented as sets of achievable costs (`le` = "min b ≤ min a", `sSup` = union, so infimum of cost);
  - the noncommutative path-language quantale.
- `exact_iff_fibreConstant` specialises with `X = Empty`.
- The theorems quantify over arbitrary `q`, so off-image points are covered.
- No result was forced by a definition.
- **Minor.** The header's `([0,∞], ≤, ·)` needs the convention `0·∞ = 0`.

### R-27. `scripts/check_observatoris_lean.py`, the "must-is-not-may" negative control

**Verdict: REFUTED as a falsity control.**

- The harness counts any exit 1 with a type error as "rejected".
- **Receipt** (`test_R27_*`): the TRUE statement `⊥ ≤ push(...)` is rejected in exactly that way under the same proof term, and it is then proved in one line.
- The control therefore certifies that a proof term does not fit, not that the mutated statement is false.
- **Repair.** Make a control prove `¬` of the mutation in an instance, as the propQ ghost does.

### R-28. Paper re-derivations without new code

**Verdict: SURVIVES.**

- FH-1, including the pointer-class refutation.
- FH-2 (the coupling).
- FH-5(b)–(f): the uniqueness lemma at `t ≥ 2d`, and the adversaries.
- FH-6(a)–(d): I re-derived `δ₁ = 1/12` and `δ₂ = 1/180` by hand, and the asymptotic `(π/2)·16⁻ⁿ`.
- FH-10(a)–(d).
- FH-11: I checked the `P₃` reduction (`y → 0` iff every row is eventually 0), Π⁰₃-hardness, and that Π⁰₃-complete sets are not in `Σ⁰₂ ∪ Π⁰₂`.
- FH-12.
- FH-14. Note: the explicit witness `g = f + t(t−1)⋯(t−d+1)` needs `char K = 0` or `char K > d`; sharpness over any field with at least `d+1` elements follows by interpolation instead.
- QG-1 to QG-4 (Lean-checked).
- RG-1(a,b) and RG-2.

### R-29. Novelty and attribution

**Verdict: MIS-ATTRIBUTION RISK. Each item below is presented as PROVED or new-to-project but is a named classical result.**

- **QG-2.** This is soundness of existential abstraction (Clarke–Grumberg–Long 1994; Cousot–Cousot 1977).
- **QG-3(3)/(4) and Lean `satClosed_iff_sat_closure_idempotent`.** These are likely the completeness conditions of abstract interpretation (Giacobazzi–Ranzato–Scozzari 2000). UNVERIFIED — wall: the exact correspondence needs the paper.
- **RG-1(a,b).** Classical combinatorial matrix theory (Brualdi–Ryser).
- **RG-4 identity.** Signature similarity, from qualitative matrix theory (Brualdi–Shader).
- **RG-5.** Holonomy is gain-graph switching (Zaslavsky).
- **CA-6.** Gottesman–Knill / stabiliser fragment.
- **FH-7.** Moore 1956, unary case.
- **FH-5(c).** Uniqueness of the minimal LFSR when the length is at least 2L (Massey 1969).

---

## Most damaging five (ranked)

1. **R-7 (HQ-3, HQ-4).** The headline "finite witness of a hidden wire" is faked by the acting observer that HQ-1 was built to handle. The repair needs `τ ≤ d_M(x,S)` and exact preparations.
2. **R-6 (HQ-2(b)).** The sharpness claim is false for multi-node causes and for clamping policies.
3. **R-9 + R-10 + R-11 (RG-3).** These three break the answer the package gives to the founding note:
   - "no transform works for unbalanced carriers" is refuted by the package's own 3-cycle;
   - "−log is derived" is undercut, because the founding note's `log(1+1/R)` works equally well;
   - `D_T` is a graded family, with negative values and dependence on `γ`, not a Lawvere metric.
4. **R-4 (HQ-4).** "Equality iff cost-exactness" is false; exactness concerns fibres, not representatives.
5. **R-2 + R-3 (§2, C-6).** The ghost/quasar asymmetry is an artefact of who holds the source. The must-quotient hides ancestors. C-6 is a "REFUTED" verdict without a receipt.

Next in severity: R-18 (CA-4 refuted), R-19 (CA-3 not exhibited), R-13 (RG-4 inconsistent after the `ε` update).

## Strongest survivors

- The Lean core, QG-1 to QG-4: genuinely general, including the reversed-order cost quantale, noncommutative languages, empty `X` and off-image `Y` (R-26).
- QG-5 in its universal-property form (R-1).
- The HQ-1 cone lemma, with acting observers that have memory and with overlapping sensors, actuators and `H`; it is sharpened to `t ≤ d(H,S)` (R-5).
- RG-1(a,b) and RG-2; the four-node minimality for `x ≠ z`.
- RG-5(a)–(c), including the strengthening (R-14, R-15).
- RG-6 (R-16).
- CA-6, now with a complete certificate (R-17).
- FH-3, FH-7, FH-8 and FH-9: every constant re-derived and brute-forced independently.
- FH-6(d) closed form; FH-11.

## Walls (what I could not check)

- **Exact statements of the cited classics:**
  - Engel–Schneider and Fiedler–Pták;
  - Paz and Tzeng (`n+m−1` or `n+m−2`);
  - Giacobazzi–Ranzato–Scozzari;
  - Kechris §23.A (I recall `P₃` as stated).
- **Out of scope:** the OPUS_II report, including RG-6's "invent and delete" receipt and Geometer CG-6/7/10.
- **Moving target:** the documents changed during the review. My findings are against the final state I read.
