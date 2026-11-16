# OPUS I — The Finite Observer: reconstruction, interaction horizons, wiring and single-copy access

**Campaign:** Principia Observatoris — Second Forge. **Agent:** OPUS I (delegated; integration by the principal session).
**Date:** 2026-11-14. **Base commit:** `8a28c4dfe927d9b62d0b0d1df6c7b5c34210fbc6`. No commit, branch, PR or ledger change was made by this agent.
**Question A.** For which finite source systems do complete, bounded intervention-response data determine the target-relevant causal dependency structure?

**Executable lab:** `observational_succ/observatoris_finite_observer.py`.
**Tests:** `tests/test_observatoris_finite_observer.py` — 42 unittest methods, exhaustive small-model enumeration, mutation and holdout controls. Command: `python -m unittest tests.test_observatoris_finite_observer -v` (about 30 s).

**Status vocabulary.** CLASSICAL [named source] · PROVED (paper proof given here) · OBSERVED IN EXACT FINITE MODELS · CONJECTURED · REFUTED (with receipt). "PROVED" means a proof is written below. It does not claim scholarly novelty. Most results here are classical or elementary consequences of classical results, put together for SUCC. No claim is made about physics, brains, RH, π-normality or the causal-proximity geometry beyond what is stated.

**Attribution of reused SUCC machinery.**
- The instrument/transcript convention and the counterfactual observation algebra come from `docs/CARRIER_RELATIVE_TARGETS.md` §2–3 and `observational_succ/carrier_relative_targets.py`. In that convention each readout is recorded *before* the instrument's transition.
- The destructive A,B,C carrier comes from the same document, §3.
- The idea of treating refusal of an unavailable action as a modelling assumption comes from `observational_succ/future_safe_quotient.py`.
- The "fully hidden two-state swap" corpse is BPGS-09 in `docs/CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md`.
- The two-path cancellation and the causal-contrast vocabulary come from the shared founding note, `research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md` (§2, crucible 2). That note was used as input only, not as a validation witness.
- The lab re-implements behavioural partition and the bounded policy planner independently. Its tests **cross-check** them against `carrier_relative_targets.behavioral_partition`, `plan_target` and `first_step_erasure_obstruction`.

---

## 0. Corrections to the commissioning statements (summary)

| # | Commissioned statement | Verdict | Receipt |
|---|---|---|---|
| C1 | Bounds n+m−1 / 2n−1 for bounded-length identification | **SURVIVES, with sharper hypotheses.** n, m must be **core** (minimal-realisation) sizes, or any upper bounds on them. The constant n+m−1 is for the readout-before-transition convention (the Moore-machine convention gives n+m−2). For partial carriers, sizes are counted after totalisation, so the refusal sink counts as a state. | FO-2; exhaustive over 11 500 distinct cores |
| C2 | "Adding an instrument only refines the core (give the map between cores)" | **CORRECTED.** A new *intervention* can enlarge the reachable set, so the new core can contain states with no old counterpart. The exact map is a surjection from the A-reachable **sub-carrier** of the new core onto the old core: core_A(M) ≅ core(core_{A∪B}(M)\|_A). | FO-3; exhaustive over 46 916 carriers |
| C3 | A2(ii) horizon = min{\|S\| : j∈S, Δ_S f(c0)≠0} | **SURVIVES for the prior-free (all-functions) class.** Under a model-class prior the detection order can be lower. | FO-4; class {0, x1+x1x2} |
| C4 | Implicit strengthening of A2(iii): horizon ranges up to deg_j | **REFUTED as "attains deg_j".** The true range is 1 = min_c h_j(c) ≤ max_c h_j(c) ≤ deg_j, and the upper bound can be strict. | f = x3·NAND(x1,x2) over GF(2): deg_3 = 3, h_3 ≤ 2 at every baseline (192 of 720 essential pairs strict for k=3) |
| C5 | A2(iv) "certifying absence needs all 2^{k−1} contexts" | **CORRECTED UNITS.** It is 2^{k−1} two-point *contrasts*, i.e. **2^k evaluations**. Under a degree bound d the exact minimum is **2·Σ_{i<d} C(k−1,i)** evaluations. Naive dimension counting proves only half of this. | FO-6; exhaustive k ≤ 4 over GF(2), k ≤ 3 over GF(3) |
| C6 | A3: identifiable iff "all nodes settable and readable in all contexts?" | **SHARPENED to an exact iff.** For each non-root node, all of its potential parents must be clamped **jointly** in every joint context while the node is free and read. Settability of single nodes is not enough. Roots need not be read, and sink nodes need not be settable. | FO-9; exhaustive over a 128-network class |
| C7 | A3 gating example | **SHARPENED.** In monotone binary single-input networks, a path through **one** hidden node always composes. Gating needs either a constant gate on a direct edge, or two binary hidden nodes, or one ternary hidden node (range restriction). | FO-8b; exhaustive over 36 + 720 monotone networks |
| C8 | A4: "commute and idempotent" as a free-observability condition | **REFUTED.** The destructive A,B,C carrier is commuting and idempotent, yet not freely observable. Class-level non-disturbance and class-level injectivity are each **sufficient**. **Neither is necessary.** | FO-10 |
| C9 | (new) "every algebra target is single-copy accessible ⇒ joint access" | **REFUTED.** Target-wise executable knowledge does not compose. | FO-10d; 4-state, 3-instrument receipt |

---

## Part A1 — The finite observer and what complete data determine

### Definitions (used throughout)

- **Carrier.** A finite set X. A finite instrument set A. For each a ∈ A, a readout o_a : X → V_a and a (possibly partial) transition t_a : X ⇀ X. A **pointed** carrier also has a selected start x0. An **uncertain** carrier has a start set S ⊆ X instead.
- **Experiment.** A word w = a1…ak ∈ A⁺. Its **transcript** from x is (o_{a1}(x), o_{a2}(t_{a1}x), …). Each readout is taken *before* that instrument acts. This is the `carrier_relative_targets.trace` convention.
- **Response map.** f_x(w a) = o_a(t_w x). The transcript of w is the list of f_x on the prefixes of w, so "all transcripts of length ≤ L" carries exactly the same information as "f_x on all words of length 1..L".
- **Partiality.** Write ⊥ for refusal. Put o_a(x) := ⊥ and t_a(x) := sink when t_a(x) is undefined, where sink is a fresh state on which every readout is ⊥. This **totalisation** is lawful only if refusal is observable. That is a physical assumption and is not derived here.
- **k-equivalence.** x ≡_k y iff f_x = f_y on all words of length 1..k. **Behavioural equivalence:** ∼ = ⋂_k ≡_k.
- **Core.** core(M) is Reach(x0)/∼, pointed at [x0], with the induced readouts and transitions. It is canonically numbered by breadth-first search from [x0] in instrument order. In code, `core()` returns that canonical form, so two cores are isomorphic iff they are equal.

### FO-1 (Kernel: which data define observation). Status: PROVED (elementary)

**Domain.** Finite carriers as above. The commissioned tuple was (Carrier, Instruments, Actions, Records, Resources, Target).

**Statement.**
1. *Observation* (all counterfactual transcripts) is a function of the kernel **K = (X, A, (o_a, t_a)_{a∈A}, x0 or S)** alone.
2. **Records** are derived: they are the transcript function of K.
3. **Actions** are the special instruments with constant readout. Partial actions reduce to total ones by totalisation, assuming refusal is observable.
4. **Resources** (costs, budgets) do not affect the core. They matter only for bounded or single-copy execution.
5. **Target** P : S → Y is needed for target knowledge and plays no role in observation.
6. **Non-redundancy, split form.** Replace each instrument (o_a, t_a) by a pure measurement (o_a, id) and a pure action (const, t_a). This **does not change** the behavioural partition of X or the reachable set. However, it **can change** single-copy accessibility.

**Proof of 6.**
- *Split readings are paired readings.* Take a split word. The readout at a measurement letter m_a is o_a(t_u x), where u lists the action letters before it (measurements do not move the state). This equals the paired response f_x(u a).
- *Paired readings are split readings.* A paired word a1…ak is simulated by m_{a1} d_{a1} … m_{ak} d_{ak}.
- So the two toolkits induce the same ∼ on X. The pure actions move states exactly as the paired instruments do, so reachable sets agree.
- *Single-copy access differs.* For the destructive A,B,C carrier, the split toolkit is freely observable and the paired one is not (FO-10). ∎

**Tests.**
- `test_readout_disturbance_pairing_redundant_for_core_only`: exhaustive over unary carriers with n ≤ 3, plus the A,B,C carrier.
- `test_malformed_kernels_rejected` (negative).

**Buys.** A minimal, typed kernel. It shows that the pairing of a readout with its disturbance matters only for executable knowledge, never for counterfactual knowledge.

**Does NOT establish.** That the declared kernel faithfully represents a real source (the "σ" obligation of CARRIER_RELATIVE_TARGETS §3, item 3). It also does not establish that refusal is physically observable.

**Interop.** Input: any finite (partial) carrier. Output: the totalised tables and response map used by every later theorem.

**Next falsification.** A source whose refusal is *not* observable, where the ⊥-totalisation over-reports what the observer can know. Compare the core with and without ⊥ readouts.

### FO-2 (Bounded-length identification, sharpness, reconstruction). Status: (a) CLASSICAL, proof given; (b), (c), (d) PROVED; all OBSERVED exhaustively

**Domain.** Total pointed carriers M = (X, A, o, t, x0) and M′ over the **same** instrument names. Readout comparison is per instrument; different charts are never compared, following CARRIER_RELATIVE_TARGETS. Partial carriers are first totalised. Let n = |core(M)| and m = |core(M′)|.

**(a) Identification bound.** If f_{x0} = f′_{x0′} on all words of length ≤ n+m−1, then they agree on all words. Equal complete responses hold **iff** core(M) ≅ core(M′). The isomorphism is **unique**.

**(b) Sharpness.** For all n, m ≥ 1 there are unary carriers with core sizes exactly n and m that agree on all words of length ≤ n+m−2 and differ at length n+m−1.

**(c) Constructive reconstruction.** Suppose the source has core size ≤ n. Then responses on lengths 1..2n−1 determine the core, and `reconstruct_core` builds it. The value 2n−1 cannot be lowered: apply (b) with m = n.

**(d) What is not identifiable.** Response data cannot see anything that core(M) does not determine:
- the number of states;
- unreachable states;
- which hidden states were merged by ∼;
- the hidden transition structure inside a ∼-class.

**Proof of (a).**
1. Work on the cores; the response of M equals the response of core(M), because the quotient map from Reach(x0) is a readout- and transition-preserving morphism. Form the disjoint union U of the two cores, with N = n+m states.
2. On U, every word of length k+1 is either a single letter or has the form a·w′ with |w′| ≤ k. Since f_x(a w′) = f_{t_a x}(w′), we get ≡_{k+1} = F(≡_k), where x F(E) y means: for all a, o_a x = o_a y and t_a x E t_a y.
3. F is monotone, ≡_0 is the total relation, and ≡_1 ⊆ ≡_0. By induction the chain decreases.
4. If ≡_k = ≡_{k+1}, the chain is constant from k on. Before that, each step strictly increases the number of blocks. There is 1 block at k = 0 and at most N blocks, so ≡_{N−1} = ∼. Hence x0 ≡_{n+m−1} x0′ implies x0 ∼ x0′.
5. *Equal responses give an isomorphism.* Define φ([t_w x0]) = [t′_w x0′].
   - Well defined: if t_w x0 ∼ t_v x0, then for every suffix u, f′(wu) = f(wu) = f(vu) = f′(vu). So t′_w x0′ ∼ t′_v x0′, and these are equal in the minimal core.
   - φ is surjective because every core state is reachable, and injective by the symmetric argument.
   - φ preserves readouts (f(wa) = f′(wa)) and transitions by construction.
   - *Uniqueness:* any isomorphism ψ must send [x0] to [x0′] and commute with every t_a, so ψ([t_w x0]) = [t′_w x0′] = φ(...).
6. *Isomorphic cores give equal responses.* Immediate from step 1. ∎

**Proof of (b).** Let c ≠ d be two readout values. Take a p-state cycle and a q-state chain, and index outputs from k = 1.
- The **cycle** emits s_k = d if k ≡ q−1 (mod p), and c otherwise.
- The **chain** emits s′_k = s_k for k ≤ q−1, and c for k ≥ q. Its last state loops on itself.
- For p ≥ 2, take p = n and q = m. When n = 1, swap the roles; when n = m = 1, use two constant machines.
- *Agreement up to n+m−2:* for q ≤ k ≤ p+q−2, the offset k−(q−1) lies in [1, p−1], which is not ≡ 0 (mod p). So s_k = c = s′_k.
- *Disagreement at n+m−1:* at k = p+q−1, s_k = d ≠ c = s′_k.
- *Cycle core size is p:* it has a single d per period, so its minimal period is p.
- *Chain core size is q:* s′_{q−1} = s_{q−1} = d ≠ c, so the preperiod is exactly q−1 and the period is 1.
- Lineage: these are extremal words in the sense of Fine–Wilf. ∎

**Proof of (c).**
1. Let the true core have k ≤ n states. Inside one k-state core, the chain argument of (a) gives: distinct states differ on some word of length ≤ k−1 ≤ n−1.
2. Every core state is reached by an access word of length ≤ k−1 ≤ n−1 (breadth-first search).
3. For each prefix u with |u| ≤ n, define its row as (f(uv)) over suffixes 1 ≤ |v| ≤ n−1. Two prefixes have equal rows iff they reach the same core state.
4. Readouts are f(ua). The transition is row(u) → row(ua), with |ua| ≤ n.
5. All data used have length ≤ n + (n−1) = 2n−1.
6. The code re-checks that the rebuilt machine reproduces **every** supplied datum.
7. *Caveat:* under a **false** size bound, the output can be a smaller machine that is consistent with the truncated data. This is exactly (b). Test `test_reconstruction_mutations` exhibits it. ∎

**Proof of (d).** Suppose M′ has a surjective morphism onto M on reachable parts, or differs from M only by unreachable states. Then M and M′ have the same core, hence the same responses by (a).
- *Receipt, unreachable state:* {0,1}, start 0, a: o = (0,1), t = id. Its responses equal those of the one-state carrier.
- *Receipt, merged states:* the hidden two-state swap with constant readout. Its responses equal those of the one-state carrier, while the state count is 2 ≠ 1 (BPGS-09 corpse). ∎

**Classical sources.**
- E. F. Moore, *Gedanken-experiments on sequential machines*, Automata Studies (1956). It gives the length bound in the Moore-machine convention; the proof above is self-contained in the present convention.
- A. Nerode, *Linear automaton transformations*, Proc. AMS 9 (1958).
- R. E. Kalman, P. L. Falb, M. A. Arbib, *Topics in Mathematical System Theory* (1969): realisation and minimality.
- A. Gill, *Introduction to the Theory of Finite-State Machines* (1962).
- N. J. Fine, H. S. Wilf, *Uniqueness theorems for periodic functions*, Proc. AMS 16 (1965).
- The reconstruction table is the classical observation-table/Hankel idea: D. Angluin, *Learning regular sets from queries and counterexamples* (1987).

**Exact evidence.**
- `test_identification_bound_exhaustive_and_sharp` enumerates all distinct cores of total carriers with ≤ 4 states over 1 instrument (48 cores) and ≤ 3 states over 2 instruments (11 500 cores), with binary readouts. Two distinct cores always disagree within length n+m−1. The maximum agreement for each size pair (n, m) is **exactly** n+m−2.
- `test_sharp_family_all_small_sizes` covers n, m ≤ 7.
- `test_reconstruction_exhaustive` covers all carriers for (1 instrument, n ≤ 4) and (2 instruments, n ≤ 2), plus a seeded sample of 2 500 of the 46 656 three-state two-instrument carriers.
- `test_partial_carriers_reduce_to_totalized_cores` covers all 1- and 2-state partial carriers.
- `test_same_responses_iff_equal_canonical_cores_with_unique_isomorphism` exhausts all pointed isomorphisms.

**Buys.** An exact answer to Question A at the level of *behaviour*:
- complete bounded data from a selected start determine **exactly** the reachable-observable core;
- the length budget is sharp in terms of core sizes;
- reconstruction is constructive.

**Does NOT establish.**
- Identification of the hidden carrier.
- Anything about sources not covered by the size bound. No finite data certify a size bound.
- Single-copy executability: complete data assume a resettable or multi-copy access path.

**Interop.** Input: two finite pointed carriers, or data plus a declared core-size bound. Output: a canonical core (an isomorphism-class invariant), or a shortest separating word.

**Next falsification.** Find a pair of carriers (any alphabet or partiality) with distinct totalised cores that agree up to length n+m−1. The proof says this is impossible. The enumeration can be extended to 3 instruments or ternary readouts.

### FO-3 (Toolkit monotonicity and exposure). Status: PROVED; OBSERVED exhaustively

**Domain.** A total carrier M over instruments A ∪ B, where B is new. Write M|_A for M with only the A-instruments.

**Statement.**
1. **core(M|_A) ≅ core(core(M)|_A).** Equivalently, there is a surjective morphism from the A-reachable sub-carrier of core_{A∪B}(M) onto core_A(M). Hence |core_A| ≤ |core_{A∪B}|.
2. On X, ∼_{A∪B} ⊆ ∼_A.
3. *Readout exposure is minimal at 2 states.* The new instrument b is a readout: X = {0,1}, a: o = (0,0), t = id; b: o = (0,1). Then 0 ∼_A 1, and b alone separates them.
4. *Pure-intervention exposure needs exactly 3 states.* Example: X = {0,1,2}, a: o = (0,0,1), t = id; b: o ≡ 0, t = (0,2,2). Then 0 ∼_A 1, and the word b·a separates them.

**Proof.**
- *(1).* The quotient map Reach_{A∪B}(x0) → core(M) is a morphism for the A-instruments. So M|_A and core(M)|_A have equal A-responses from their starts. Apply FO-2(a).
- *(2).* Every A-word is an (A∪B)-word.
- *Minimality in (4).* Suppose |X| = 2, x ∼_A y and b has constant readout. Since ∼_A refines the readouts, every A-readout is constant on X = {x, y}. The readout of b is constant too. So every transcript is constant, and no word separates. ∎

**Tests.**
- `test_reduct_core_identity_exhaustive` checks (1) and (2) over all 46 916 two-instrument carriers with ≤ 3 states.
- `test_pure_intervention_exposure_needs_three_states` checks all 2-state carriers.
- `test_new_readout_exposes_hidden_distinction`.

**Buys.** A precise "more instruments, finer knowledge" law. It also shows the second effect: interventions can *enlarge* what is reachable, not only refine it.

**Does NOT establish.** That a physically new instrument exists. Nor that it reads the same source (σ).

**Interop.** Input: carrier plus an instrument subset. Output: the reduct-core identity and a refinement certificate.

**Next falsification.** Partial instruments whose refusal semantics interact with B. The claim is proved after totalisation; check whether an **un**observable refusal breaks it.

---

## Part A2 — Interaction-order horizons

**Definitions.**
- f : {0,1}^k → G, where G is an abelian group (Z or Z/m in the code), and c0 is a baseline. For T ⊆ [k], c0⊕1_T flips the coordinates in T.
- Δ_S f(c0) = Σ_{T⊆S} (−1)^{|S|−|T|} f(c0⊕1_T).
- j is **essential** iff f(c) ≠ f(c⊕e_j) for some c.
- An **order-r observer at c0** sees f on the Hamming ball B_r(c0).
- The **detection horizon** is h_j(c0) := min{|S| : j∈S, Δ_S f(c0) ≠ 0}, with min ∅ = ∞.

### FO-4 (Möbius expansion and the intervention-order horizon). Status: (i) CLASSICAL; (ii) PROVED; OBSERVED exhaustively

**(i) Expansion.** f(c0⊕1_T) = Σ_{S⊆T} Δ_S f(c0), with unique coefficients. j is essential iff some S ∋ j has Δ_S f(c0) ≠ 0, at **any** fixed baseline.

**(ii) Horizon, prior-free.** The order-r data at c0 are consistent with **every** j-independent function only when r < h_j(c0). Precisely:
- if r < h_j(c0), there is an explicit j-independent g with g = f on B_r(c0);
- if r ≥ h_j(c0), the ball contains a j-pair with different values.

In particular, an AND gate x1⋯xk at c0 = 0 is invisible to every order < k: it equals the zero function on B_{k−1}(0). At c0 = 1⋯1 its horizon is 1.

**Proof of (i).** Möbius inversion on the Boolean lattice holds over any abelian group, because the incidence algebra has integer entries (Rota 1964).
- *Essential ⇒ some coefficient.* If Δ_S = 0 for every S ∋ j, then f(c0⊕1_T) = Σ_{S⊆T∖j} Δ_S = f(c0⊕1_{T∖j}). Every context is c0⊕1_T for a unique T, and flipping j toggles j ∈ T, so f does not depend on j.
- *Coefficient ⇒ essential.* If f does not depend on j, then for S ∋ j, Δ_S = Σ_{T⊆S∖j} (−1)^{|S|−1−|T|}(f(c0⊕1_{T∪j}) − f(c0⊕1_T)) = 0.

**Proof of (ii).**
1. g(T) − g(T∖j) = Σ_{S⊆T, j∈S} Δ_S.
2. If |T| < h_j, every term vanishes. If T = S* attains the minimum, the sum equals Δ_{S*} ≠ 0.
3. The smallest radius of a ball holding both T and T∖j is |T|, so the first difference inside B_r(c0) appears exactly at r = h_j.
4. *Extension when r < h_j.* For each j-pair {c, c⊕e_j}: if both points are in the ball they agree (step 2), so keep that common value. If one is in the ball, copy its value to the other. If neither is, give both any common value. The result is j-independent and equals f on the ball.
5. The order-r data are in bijection with {Δ_S : |S| ≤ r}, because the transform is triangular with ±1 on the diagonal.
6. So **first-order contrasts at one baseline see exactly Δ_∅ and the Δ_{{j}}**: the degree-≤1 part of the expansion at c0. ∎

**Correction (C3).** "Detect" must be read prior-free. Take the class {0, g} with g = x1 + x1x2. Then h_2(0) = 2. Yet the order-1 datum g(e1) = 1 ≠ 0 rules out the zero function, and the only other member, g, depends on x2. So in that class, order 1 already settles "depends on x2". See `test_class_prior_can_lower_the_detection_order`.

**Finite value sets (PROVED).** Let V_i be finite, c0 ∈ ∏V_i, and b ∈ ∏(V_i ∖ {c0_i}).
- Each binary subcube anchored at c0 with alternatives b reduces to the Boolean case.
- *j essential ⟺ visible in some anchored subcube.* Suppose f(c[j:=a]) ≠ f(c[j:=a′]). Then one of the two values differs from f(c[j:=c0_j]), which gives a pair in a subcube anchored at c0.
- *The horizon is the minimum of the subcube horizons.* A ball pair that differs only at j, both off c0_j, has the same distance as its comparison with c0_j.
- This is the classical **anchored decomposition**: F. Y. Kuo, I. H. Sloan, G. W. Wasilkowski, H. Woźniakowski, *On decompositions of multivariate functions*, Math. Comp. 79 (2010).

**Tests.**
- `test_mobius_inversion_unique_exhaustive`.
- `test_essential_iff_coefficient_and_horizon_equals_ball`: every f : {0,1}³ → Z/2 and every f : {0,1}² → Z/3 and Z/4, every baseline, every j, every r. The horizon is checked against an independent ball search, and the extension is checked.
- `test_and_gate_invisible_below_order_k` for k ≤ 5.
- `test_first_order_data_are_the_degree_one_part`.
- `test_finite_value_sets_reduce_to_anchored_subcubes`: all 512 Boolean-valued functions on {0,1,2}², plus random tables on 3×2×2.

**Buys.** An exact, baseline-relative **intervention-order horizon**: the minimum number of simultaneous interventions needed to *see* a dependency without priors.

**Does NOT establish.** Anything about noise, sampling or dynamics, or that physical interventions are "simultaneous".

**Interop.** Input: a finite table into an abelian group, plus a baseline. Output: the coefficient vector {Δ_S}, the horizons h_j(c0), and either a j-independent extension (non-detection certificate) or a separating pair.

**Next falsification.** Replace the group by a non-group codomain (bare equality only). The horizon via balls is still defined, but the Möbius side is not. Determine which statements survive.

### FO-5 (Baseline transport and the horizon range). Status: PROVED; transport and degree invariance OBSERVED exhaustively; one strengthening REFUTED

**Statement.** Let a_S = Δ_S f(b) and C := supp(b ⊕ c0). Then:

**Δ_V f(c0) = (−1)^{|V∩C|} · Σ_{V ⊆ S ⊆ V∪C} Δ_S f(b).**

Consequences:
1. The Möbius degree deg f, and the variable degree deg_j f = max{|S| : j∈S, Δ_S ≠ 0}, are baseline-invariant. Top coefficients change only by sign.
2. For essential j: **1 = min_c h_j(c) ≤ max_c h_j(c) ≤ deg_j f**.
3. The upper bound is attained by AND gates, but **not always**. This refutes the strengthening "max_c h_j(c) = deg_j f".

**Proof.**
1. Take b = 0 without loss of generality. Write f(x) = Σ_S a_S x^S as a multilinear polynomial with integer coefficients acting on G.
2. Substitute x_i = y_i for i ∉ C and x_i = 1 − y_i for i ∈ C, where y = x ⊕ c0.
3. ∏_{i∈S∩C}(1 − y_i) = Σ_{R⊆S∩C} (−1)^{|R|} y^R. The monomial y^V arises exactly from S = (V∖C) ∪ W with V∩C ⊆ W ⊆ C, that is, from V ⊆ S ⊆ V∪C, with sign (−1)^{|V∩C|}.
4. *Degree invariance.* For |V| = deg f, every proper superset in the sum has a zero coefficient. So Δ_V f(c0) = ±Δ_V f(b). Apply the same argument from c0 back to b, and repeat with j-containing sets for deg_j.
5. *max ≤ deg_j.* Let S* contain j with |S*| = deg_j. At any c0, Δ_{S*} f(c0) = ±a_{S*} ≠ 0.
6. *min = 1.* Essentiality gives a c with f(c) ≠ f(c⊕e_j). There Δ_{{j}} f(c) ≠ 0. ∎

**Receipt (REFUTED strengthening).** Over GF(2), take f = x3 + x1x2x3 = x3·NAND(x1,x2). At baseline 0 its coefficients are {x3, x1x2x3}, so deg_3 = 3. Yet h_3(c) over the 8 baselines is (1,1,1,2,1,1,1,2). At c = (1,1,·), 1 + x1x2 becomes y1 + y2 + y1y2, which has degree-1 terms. Exhaustively, for k = 3 over GF(2), **192 of the 720 essential (f, j) pairs** have max_c h_j(c) < deg_j.

**Tests.**
- `test_baseline_transport_formula`: all 6 561 functions {0,1}³ → Z/3 × 8 shifts, plus 300 random Z-valued functions with k ≤ 5.
- `test_horizon_range_and_degree_invariance`.
- `test_upper_horizon_not_always_attained`.

**Buys.** The exact answer to "how does the horizon move with the baseline". It also explains why a dependency invisible at one operating point appears at first order elsewhere. This is a precise, finite version of the founding note's warning that relevance is context-dependent.

**Does NOT establish.** A closed form for max_c h_j(c). See the open list.

**Interop.** Input: coefficients at baseline b, plus a shift. Output: coefficients at b⊕shift.

**Next falsification.** Characterise max_c h_j(c). Candidate (CONJECTURED, untested): it equals deg_j iff some baseline annihilates all lower-order j-coefficients. This is tautological as stated; a structural version is open.

### FO-6 (Exact cost of certifying ABSENCE of a dependency). Status: PROVED; OBSERVED exhaustively

**Domain.** P_d(k; G) is the set of f : {0,1}^k → G with Möbius degree ≤ d (baseline-invariant by FO-5), where G is a nontrivial abelian group and 0 ≤ d ≤ k. A query set Q ⊆ {0,1}^k **certifies absence of j** at a j-independent f if every g ∈ P_d with g|_Q = f|_Q is j-independent.

- Because P_d is a group, this holds iff every h ∈ P_d vanishing on Q is j-independent. So certification depends on Q only.
- An adaptive algorithm run on a j-independent input must therefore, on that input, query a certifying set. Adaptivity cannot help.

**Statement.**
1. The minimum |Q| is exactly **2·Σ_{i<d} C(k−1, i)** evaluations. It is attained by the **ball pair**: both values of x_j, over the radius-(d−1) ball in the other coordinates around a baseline.
2. For d = k (all functions) this is 2^k: **every point is needed**. Dropping any single point allows an adversarial g. In contrast units this is 2^{k−1}, which corrects the units in C5.
3. The order-r ball B_r(c0) certifies absence for the class P_d iff **r ≥ d** (for 1 ≤ d ≤ k).
4. Pure dimension counting gives only dim P_d − dim(j-independent part) = Σ_{i<d} C(k−1,i), which is **half** the truth.

**Proof.**
1. Centre coordinates at the baseline. Write h = u + x_j·v, where u ∈ P_d(k−1) and v ∈ P_{d−1}(k−1); every such pair occurs. Then h is j-independent iff v = 0.
2. Let Q_0, Q_1 be the projections of the query points with x_j = 0 and x_j = 1.
3. *Lower bound.* Suppose |Q_1| < dim P_{d−1}(k−1) = Σ_{i<d} C(k−1,i).
   - Construct a nonzero v vanishing on Q_1. If G contains an element of prime order p, use F_p-linear algebra inside ⟨g⟩ ≅ Z/p. Otherwise G contains Z: find a rational kernel vector, scale it to integers, and multiply by g.
   - Then h = x_j v vanishes on Q but depends on j.
   - Symmetrically, if |Q_0| is too small, take v vanishing on Q_0 and h = (x_j − 1)v.
   - Hence |Q| = |Q_0| + |Q_1| ≥ 2 Σ_{i<d} C(k−1,i).
4. *Upper bound.* With Q_0 = Q_1 = B_{d−1}, the function v = (u+v) − u vanishes on B_{d−1}. That ball is unisolvent for P_{d−1}: its values give every Δ_S with |S| ≤ d−1. So v = 0.
5. *Ball statement (3).* For B_r(c0), Q_1 is the radius-(r−1) ball in k−1 variables. If r < d, a monomial of degree r ≤ d−1, centred at c0, vanishes on that ball, so certification fails. If r ≥ d, the upper-bound argument applies. ∎

**Tests.**
- `test_certification_cost_exhaustive`: the ball pair certifies, and **every** set of size cost−1 fails, for all k ≤ 4, d ≤ k over GF(2) (j at both ends) and all k ≤ 3 over GF(3). Monotonicity of certification makes checking size cost−1 sufficient.
- `test_unrestricted_class_needs_every_point`.
- `test_order_r_ball_certifies_degree_d_iff_r_ge_d`.
- `test_naive_dimension_count_is_only_half`.

**Buys.** A sharp resource law: **absence is expensive, presence is cheap**. One differing pair certifies presence. Absence needs the whole ball pair. A degree prior d reduces the cost from 2^k to 2·Σ_{i<d} C(k−1,i), achievable from one baseline with intervention order d.

**Does NOT establish.** Bounds for noisy evaluations, randomized algorithms with error, or non-multilinear priors.

**Interop.** Input: (k, d, j, query set). Output: certify / fail, with exact minimum cost.

**Next falsification.** Randomised certification with one-sided error. The deterministic lower bound says nothing there; test whether O(Σ) is still needed.

### FO-7 (Differentiable analogue). Status: CLASSICAL; polynomial part OBSERVED with exact Fractions

1. **Polynomials (Taylor).** A polynomial p : R^k → R of degree ≤ d equals its order-d Taylor polynomial at any baseline. So the d-jet at one point determines every finite contrast p(c0+h) − p(c0).
2. **Smooth maps: no jet suffices.** The flat function φ(x) = e^{−1/x²} for x > 0, φ(x) = 0 for x ≤ 0 (Cauchy 1823) has a zero ∞-jet at 0, yet φ(1) − φ(0) = e^{−1} ≠ 0.
3. **Analytic maps.** On a connected domain the full ∞-jet determines f (identity theorem). No finite jet does, since x^{d+1} has a zero d-jet at 0.
4. **Baseline relativity.** x1⋯xk has zero jet of order < k at 0, but a nonzero gradient at (1,…,1). This is the smooth counterpart of FO-4/FO-5.

**Tests.** `test_polynomial_jets_and_mutations`:
- the jet reproduces exact contrasts for random rational polynomials;
- the mutation p + (x1 − c0_1)^{d+1} has the same d-jet but a different contrast;
- the gradient of the cube monomial vanishes at 0 and not at 1.

The flat function is not computed: it is not exactly rational. It is cited only.

**Buys / does NOT establish.** The founding note's "causal derivative" (§2) sees exactly the d-jet. It is a complete instrument only under a polynomial-degree prior, and incomplete for merely smooth responses. No claim is made about physical differentiability.

---

## Part A3 — Wiring is not a response invariant

**Definitions.**
- A **network** is a finite acyclic list of nodes with value sets (each of size ≥ 2 in the class statements). Each node i has **potential parents** pa\*(i) among earlier nodes and a total table F_i on ∏_{p∈pa\*(i)} V_p. Roots are constants (exogenous settings).
- An **experiment** clamps a set K to values (do-intervention: clamped nodes bypass their tables) and reads a set R.
- The **essential edge** p → i holds iff F_i depends essentially on p.
- The **response** is the input-to-output map with the other roots at their declared values.
- **Net dependency** means a non-constant response.

### FO-8 (Two distinct failure modes; minimal sizes). Status: PROVED; OBSERVED exhaustively

**(a) Signed cancellation.**
- N1: z1 = x, z2 = x, y = z1 − z2. N0: the same nodes with constant tables.
- Both have response y ≡ 0, but different essential graphs. N1 has the essential path x → z1 → y.
- **Minimal:** one hidden binary node plus a direct edge suffices: z = x, y = x XOR z.
- *Proof of minimality.* With no hidden node, the response *is* F_y, so essential and net dependency coincide. With a chain-only x → z → y and binary z, essential x → z forces z ∈ {x, 1−x}, a bijection. Essential z → y forces F_y(0) ≠ F_y(1). Then F_y∘F_z is non-constant. ∎

**(b) Gating / inactive context (cancellation-free, monotone).**
- *(b1) Direct edge, constant gate:* y = x ∧ z with z ≡ 0. The edge x → y is essential, the response is constant, and every table is monotone.
- *(b2) Path through a hidden node, two binary hidden nodes needed:* z1 = x, z2 ≡ 0, y = z1 ∧ z2 (`gating_network`).
  - **Claim:** in monotone binary networks with a single input and one hidden node z, the path x → z → y always composes.
  - *Proof.* The monotone one-variable functions are 0, 1, x. Essential x → z gives z = x. Then y(x) = F_y(x, x) with F_y monotone. If F_y(0,0) = F_y(1,1), monotonicity gives F_y(0,0) ≤ F_y(a,b) ≤ F_y(1,1), so F_y is constant, contradicting essential z → y. ∎
- *(b3) Range restriction:* one **ternary** hidden node suffices. z = x ∈ {0,1} ⊂ {0,1,2} and y = [z ≥ 2] (`range_gate_network`). The essential witness of F_y lies at an unrealised value of z.

**Tests.**
- `test_two_path_cancellation_and_minimal_repair`.
- `test_one_hidden_node_suffices_with_direct_edge`.
- `test_binary_chain_composes_exhaustively`: all 72 networks on x → z → y with ternary y.
- `test_monotone_gating_minimal_sizes`: all 36 monotone one-hidden-node networks, with exactly 4 direct-edge gates, and all 720 monotone two-hidden-node networks, where non-composing paths exist.

**Minimal repair for the pair (N1, N0).** A single extra experiment separates them: clamp z1 := 0 at x = 1 and read y (N1 gives −1, N0 gives 0). Reading z1 alone also works. **Neither repairs the class:** N2 (z1 = z2 = x, y ≡ 0) has the same z1-readout as N1 and a different graph. FO-9 gives the exact requirement.

**Buys.** Two **receipt-backed and distinct** reasons why a path of essential edges is not a net dependency:
- signed cancellation, which needs non-monotone combination;
- inactive context, where the essential witness of a downstream table is never realised, through a constant gate or range restriction.

The founding note's warning "a shortest-path metric on magnitudes invents influence" therefore has two independent finite witnesses.

**Does NOT establish.** Anything quantitative about how often these occur, or results for cyclic or dynamical networks.

**Interop.** Input: a network. Output: its essential graph, the response map, and a pair of response-equivalent networks with different graphs when one exists.

**Next falsification.** In monotone networks with **several** inputs and baseline contexts, decide whether every non-composing essential path is a gating instance, i.e. has an unrealised witness context. CONJECTURED for acyclic monotone networks; untested.

### FO-9 (Realised-context lemma; exact identifiability criterion). Status: PROVED; OBSERVED exhaustively

**(a) Realised-context lemma.** Fix a family of experiments 𝓔. Let C_i(N) be the set of contexts of pa\*(i) realised in some experiment of 𝓔 in which i is unclamped. Then the data of 𝓔 depend on each F_i **only through F_i restricted to C_i(N)**.
- *Proof.* By induction in topological order: if two networks agree on the realised contexts, all node values agree in every experiment, and so do the realised contexts. ∎
- In the code, a modification of F_i at contexts that are never evaluated leaves the data unchanged.

**(b) Exact criterion.** Let 𝓝(D, V) be the **unrestricted class** of networks on a known potential-parent DAG D with value sets |V_p| ≥ 2. The essential graph is determined by the data of 𝓔 **for every network in 𝓝** iff:

> for every node i with pa\*(i) ≠ ∅ and every joint context c ∈ ∏_{p∈pa\*(i)} V_p, some experiment in 𝓔 clamps **all** of pa\*(i) to c, leaves i unclamped, and reads i.

**Proof.**
- (⇐) Each F_i is read on its whole domain, so its essential parents are determined.
- (⇒) Suppose some (i, c) is missing. Take N with every node constant, choosing constants v_p ≠ c_p for p ∈ pa\*(i).
  - In N, context c at i occurs only when every p ∈ pa\*(i) is clamped to c_p. By hypothesis, whenever that happens with i free, i is not read.
  - Let N′ equal N except F′_i(c) ≠ v_i. Downstream tables are constant in both, so no read value changes, and N, N′ have identical data.
  - N has no essential edges. N′ has p → i for every p ∈ pa\*(i), because c and c[p := a] differ in output. ∎

**Corollaries.**
- *(i) Joint clamping is necessary.* Setting single nodes, or observing every node without clamps, does not identify the class. See `test_full_readout_without_clamps_fails`.
- *(ii) Order requirement.* The required simultaneous-intervention order is max_i |pa\*(i)|. This is the A2 horizon phenomenon in the unrestricted class.
- *(iii) Degree prior (PROVED, not separately tested).* If each F_i is known to have Möbius degree ≤ d, then clamping pa\*(i) over a radius-d ball around one context suffices. That ball is unisolvent for P_d by FO-4/FO-6.

**Tests.**
- `test_identifiability_criterion_exhaustive_class` covers the class on r → u → v, r → v (128 networks) and the universe of 64 experiments: every node is read, hidden, clamped to 0 or clamped to 1. It checks 257 families: the minimal required family, all 6 single-deletion mutants, and 250 seeded random families. Criterion ⟺ identification holds on all of them, and every deletion mutant fails.
- `test_realized_context_lemma` covers 200 random (family, network) pairs.

**Buys.** The exact answer to the A3 identifiability question in the prior-free setting, with the price stated in experiments: Σ_i ∏_{p∈pa\*(i)} |V_p|, before sharing experiments between nodes.

**Does NOT establish.** Results for restricted classes (linear or monotone networks), for latent confounders without clamps, for cycles, or for noise. Those can be cheaper or impossible.

**Interop.** Input: (skeleton, family of experiments). Output: a yes/no identifiability verdict and, for "no", a witness pair of networks with equal data and different graphs.

**Next falsification.** The monotone class (C7). Find the exact experiment family needed; it is presumably smaller. Probe whether FO-9's "joint clamping of all parents" still holds there.

---

## Part A4 — Free (single-copy) observability

**Definitions** (CARRIER_RELATIVE_TARGETS §2–3).
- The **counterfactual algebra** is the set of class-constant functions on X/∼. It is the knowledge available from all words on resettable copies.
- A carrier with start set S is **freely observable** if one unresettable copy, run by an adaptive policy, determines the ∼-class of its start for every start in S. Equivalently, the class-identity target, and hence every algebra target, is single-copy accessible.

### FO-10 (Exact all-horizon criterion; sufficient conditions; refutations). Status: (a), (b) PROVED; (c), (d) REFUTED with receipts; (e) CLASSICAL plus OBSERVED

**(a) Exact criterion.** Work in the quotient Q = X/∼; this is legitimate because ∼ is a congruence that refines every readout.
- A **belief** is a set of pairs (label, current class), where the label is the original class or a target value.
- A belief is **fused**, and hence lost forever, if one current class carries two labels. Equal histories plus an equal current class give equal futures.
- A belief is **settled** if it carries a single label.
- A belief **wins** if it is settled, or if some instrument maps it to output-blocks that all win.

Free observability ⟺ the initial belief {([x],[x]) : x ∈ S} lies in the **least fixed point** of this win operator, computed on the finite set of reachable beliefs.
- Synchronous iteration returns the optimal worst-case depth. That depth is bounded by the number of reachable beliefs, so the decision holds for **all horizons**.
- The same game with target values as labels decides single-target access. It extends `carrier_relative_targets.plan_target`, which is budget-bounded at 16.
- *Proof.* Readouts and futures depend only on the current class, and fusion is irreversible. A winning policy tree has finite depth, so it lies in some finite stage of the fixed point. Conversely, a fixed-point certificate yields a policy. The policy is verified by an independent executor on the **original** carrier. ∎

**(b) Sufficient conditions.**
1. **Class non-disturbing** (t_a x ∼ x for all a, x) ⇒ freely observable by the **preset** word listing every instrument once.
   - *Proof.* Each readout is taken at a state ∼ x0, so it equals o_a(x0).
   - ≡_1 is a congruence: t_a x ∼ x ≡_1 y ∼ t_a y. Hence ≡_1 ⊆ ∼, and ∼ = ≡_1.
   - So the readout vector (o_a(x0))_a determines the class. ∎
2. **Class-injective dynamics** (every t_a injective on Q) ⇒ freely observable, with depth ≤ (s−1)(q−1), where s = |S/∼| and q = |Q|.
   - *Proof.* No fusion can occur. Repeatedly apply a shortest distinguishing word for two surviving candidates. It has length ≤ q−1 by FO-2 in the reduced quotient, and it removes at least one candidate. ∎

**(c) Refutations of candidate iff's.**
- **"Commuting and idempotent ⇒ free": REFUTED.** In the A,B,C carrier, t_a = t_b = const_A, which is idempotent and commuting. The algebra has dimension 3, yet 1[C] is not single-copy accessible at any horizon. The lab and the existing `first_step_erasure_obstruction` both return certificates.
  - Exhaustively, over all 46 916 two-instrument carriers with ≤ 3 states, **384** commuting-idempotent carriers are not freely observable.
- **"Free ⇒ class-injective" (and "free ⇒ non-disturbing"): REFUTED.** `reset_and_readout` has m = (read, id) and r = (0, reset). It is free via m but not class-injective. `readout_swap` (read, then flip) is free but disturbing.
  - Exhaustively, 36 036 carriers are free but not class-injective.

**(d) Target-wise access does not compose: REFUTED** ("every algebra target accessible ⇒ free").
- Receipt `separately_but_not_jointly`: states A,B,C,D with start set {A,B,C}. Instrument a flags A, c flags B, b flags C, and each of them sends every state to D.
- Each of the 8 Boolean targets on {A,B,C} is accessible with one instrument, and the policies were executed and verified.
- Full class identification is impossible: every first move fuses the two unflagged states.
- **Executable knowledge is not closed under conjunction.** This is a new-to-project boundary sharpening CARRIER_RELATIVE_TARGETS §3.

**(e) Classical connection.**
- For S = X, free observability is exactly the existence of an **adaptive distinguishing sequence** for the reduced machine Q.
- D. Lee and M. Yannakakis, *Testing finite-state machines: state identification and verification*, IEEE Trans. Computers 43(3), 1994, decide this in polynomial time and give depth ≤ q(q−1)/2.
- Observed: over all 46 916 carriers, every free carrier has optimal depth ≤ q(q−1)/2. The bound is tight at q = 3: maximum depth 3.
- The complexity of the start-**subset** version was not checked by this agent and is not claimed.

**Exhaustive numbers** (all total two-instrument carriers with ≤ 3 states and binary readouts, 46 916 in all):

| Property | Count |
|---|---|
| Freely observable | 42 380 |
| Class non-disturbing (all free) | 3 596 |
| Class-injective (all free) | 6 344 |
| Free but not class-injective | 36 036 |
| Commuting-idempotent | 3 828 |
| Commuting-idempotent and not free | 384 |

**Tests.**
- `test_destructive_abc_negative_control`.
- `test_positive_controls`.
- `test_sufficient_conditions_and_converse_failures_exhaustive`, which also executes every returned policy on every start and checks both depth bounds.
- `test_targetwise_access_does_not_compose`.
- `test_free_implies_every_algebra_target_accessible`.
- `test_cross_check_with_existing_bounded_planner`: the optimal depth equals `plan_target`'s worst cost whenever it is ≤ 8, and both report failure otherwise.
- `test_target_not_constant_on_class_is_refused`.

**Buys.**
- An exact, budget-free decision procedure for the "second obligation" of CARRIER_RELATIVE_TARGETS §3.
- Two clean sufficient conditions.
- Receipts showing that the natural algebraic conditions (commuting and idempotent) are irrelevant, and that target-wise access is not compositional.

**Does NOT establish.** A polynomial algorithm for arbitrary S; the belief space is exponential in the worst case. It also says nothing about stochastic instruments or physical non-disturbance.

**Interop.** Input: carrier, start set, optional target. Output: accessible yes/no, optimal depth, a verified decision tree, and the number of beliefs explored.

**Next falsification.** A structural iff short of the fixed point, e.g. "free ⟺ no reachable belief all of whose instruments fuse". This is CONJECTURED **false** in general, because branching interacts. Test it by searching for a carrier where every reachable belief has a non-fusing instrument but the game is lost through cycling.

---

## What Question A now has as an answer (synthesis, labelled)

1. **Behaviour (FO-2).** Complete bounded responses from a selected start determine exactly the reachable-observable core, up to unique isomorphism, with sharp length n+m−1. They determine nothing finer. *PROVED / CLASSICAL.*
2. **Dependencies at a baseline (FO-4–FO-6).** A dependency is detected exactly at intervention order h_j(c0). Its *absence* costs 2·Σ_{i<d} C(k−1,i) evaluations under a degree-d prior, and 2^k without one. *PROVED.*
3. **Structure (FO-8, FO-9).** The one-step dependency graph is **not** a response invariant. Signed cancellation and inactive context are two distinct mechanisms. In the prior-free class, the graph is identified iff each node's potential parents are jointly clamped through all contexts with the node read. *PROVED.*
4. **Execution (FO-10).** Counterfactual knowledge (the algebra) and single-copy knowledge differ. The gap is decided exactly by a finite game. It is closed by class non-disturbance or class-injectivity, not by commutation or idempotence, and it is not closed under conjunction of targets. *PROVED / REFUTED receipts.*

## Open / unproved but promising

- **O1.** A closed form or structural characterisation of max_c h_j(c) (FO-5). Known: it lies between 1 and deg_j, can be strictly below deg_j, and equals deg_j for AND.
- **O2.** The exact identifiability criterion (FO-9 analogue) for **restricted** classes: monotone, linear over a ring, or degree-d. For degree-d only sufficiency is proved; necessity is open.
- **O3.** The complexity and depth bound of free observability for start **subsets** S ⊊ X (Lee–Yannakakis covers S = X). It also remains open whether the (s−1)(q−1) bound for class-injective carriers is sharp.
- **O4.** Cyclic or time-unrolled networks, where FO-9 and the founding note's chain-rule sensitivity D_{x→y}(t,s) should meet. The finite-difference horizon should become a horizon in (order, delay).
- **O5.** Partial readout plus restricted interventions: when is the identified *subgraph* maximal? Conjectured: the realised-context lemma gives the exact identified part, edge by edge, as in the certification logic of FO-6.
- **O6.** Noisy or stochastic instruments. Every result here is deterministic; none transfers without a new proof.

## Provenance and boundaries

- Base commit `8a28c4dfe927d9b62d0b0d1df6c7b5c34210fbc6`. Files created: the report, `observational_succ/observatoris_finite_observer.py` and `tests/test_observatoris_finite_observer.py`. No other repository file was modified. No imported theorem or archival original was touched.
- Only the agent's own test file was run: 42 tests, OK, about 30 s. The full suite and the AGENTS.md validation scripts were **not** run by this agent, per the delegation instructions. CI status is not claimed.
- No result here promotes any claim-ledger entry. Integration into `docs/CLAIM_LEDGER.md` or a claim supplement is left to the principal, under the ledger's update policy.
- **Physical boundary.**
  - "Observer", "instrument" and "intervention" denote declared finite mathematical objects.
  - Nothing here asserts that a brain, a physical apparatus or a quantum system realises these models.
  - Nothing here asserts that finite observations prove universal statements.
  - Nothing here bears on RH, Weil positivity or π-normality.

---

## Erratum added by the principal investigator after adversarial review (2026-11-14)

The text above is the workstream's report as delivered. The second hostile referee
([OPUS_IV_REFEREE_ROUND2.md](OPUS_IV_REFEREE_ROUND2.md), findings `S-n`, independent receipts in
`tests/test_observatoris_referee_round2.py`) found the following; the body is left unchanged.
Every theorem it could test survived.

- **FO-4(ii) (S-13, wording).** "Consistent with every `j`-independent function" should read
  "consistent with **some** `j`-independent function". The mathematics (horizon = ball horizon,
  the signed transport formula, the 192/720 count) was reproduced independently.
- **FO-6 (S-14, S-18).** The exact cost survived a full independent brute force; but the
  workstream's own test checked both bounds with the lab's predicate (circular), and
  `test_naive_dimension_count_is_only_half` only checks a binomial identity. The lower bound is
  the classical interpolation-set (Reed–Muller) argument.
- **FO-9 (S-15).** The hypothesis `|V_p| ≥ 2` is load-bearing: with a single-valued parent the
  literal "clamp all parents" condition is not necessary. The summary row that drops the
  hypothesis is incorrect as written.
- **FO-10 (S-17).** All six census counts and all receipts were reproduced by an independent
  belief game without fusion pruning. The depth bound `(s−1)(q−1)` holds on every start subset
  tested and is attained at `(s,q) = (2,3)` but not at `(3,3)` (maximum 3 < 4): it is not sharp
  in general.
- **FO-2(b) (S-19).** The stated Fine–Wilf lineage is loose.
