# OPUS IV (second seat) — Hostile referee, round 2

**Operation Principia Observatoris — Second Forge.** Referee report, 2026-11-14.
**Material under review.**
- A. [`OPUS_II_CAUSAL_GEOMETER.md`](OPUS_II_CAUSAL_GEOMETER.md) (CG-1 … CG-13), with `observational_succ/observatoris_quantale_quotient.py` and `tests/test_observatoris_quantale_quotient.py`.
- B. [`OPUS_I_FINITE_OBSERVER.md`](OPUS_I_FINITE_OBSERVER.md) (FO-1 … FO-10), with `observational_succ/observatoris_finite_observer.py` and `tests/test_observatoris_finite_observer.py`.

**Executable receipts.** [`tests/test_observatoris_referee_round2.py`](../../../../tests/test_observatoris_referee_round2.py): 39 tests, about 23 s, stdlib and exact arithmetic only. The file does **not** import the reviewed modules. It has its own quantale tables, Kleene closure, quotients, partition lattice, Möbius transform, GF(2) kernel test and Z/4 and Z/6 brute force, network evaluator, carrier minimiser, and a belief game that runs without fusion pruning.

```sh
python -m unittest tests.test_observatoris_referee_round2 -v
```

The two reviewed test files were also run individually: quantale quotient 45 tests OK (46 s), finite observer 42 tests OK (30 s). The full suite was not run, per instructions. CI status is not claimed.

**Method.** METHOD.md: steelman, crucible, verdict. A refutation is given only with a receipt. Unsupported doubt is labelled UNVERIFIED with the wall named. Where a statement survived, the attack that was tried is stated. Test classes in the receipts file are named `S01_…` to `S17_…`, matching the findings below.

**Headline.** Both reports are mathematically strong. Every theorem-level statement I could test survives. The damage is at the edges:
- one false scoped observation (S-9);
- one receipt that does not witness the property it is cited for (S-3);
- one hypothesis that the lab's own instance cannot satisfy (S-7);
- one literally false headline sentence (S-13);
- several census numbers in the prose that no regression test pins (S-18);
- missing classical attributions (S-19).

---

## Findings

### S-1. CG-3 (seven-way equivalence): SURVIVES

**Attack.**
- **Paper re-derivation, every arrow.** Each step uses only infinitary QL/QR, M, U and A. None uses finiteness, commutativity, integrality or surjectivity:
  - (5)⇒(1) inducts on Qⁿ, and the off-image b contribute ⊥ by QL;
  - Lemma L ⇐ handles empty fibres by a⊗⊥ = ⊥;
  - (2)⇔(6) needs nonempty families, and off-image rows are correctly excluded.
- **Condition (5) quantifier.** Restricting to a ∈ q(X) is harmless but unnecessary: off-image rows of Q∃(R) are ⊥, so (5) holds there trivially. Restricting to the image is necessary in (6), and the report does so.
- **Executable.** I compared (1), (2), (3), (4), (5) and (6) using my own implementation.
  - The quantale is **Rel(2)**, binary relations on a 2-set under composition. It is noncommutative, non-integral (unit 1001 ≠ top 1111) and **not** of the form P(monoid), so it is outside the reviewed lab's families.
  - 14 random relations on 3 states were each crossed with 6 report maps, including the non-surjective (0,0,2) with m = 4 and (1,1,3) with m = 4.
  - (3) and (4) quantify over all closed predicates (all 16³ candidates enumerated).
  - All six conditions agree, and both verdicts occur.
  - Boolean, exhaustive for n ≤ 3, with a forced empty fibre in the middle of Y: all six agree.

**Receipt.** `S01_CG3_SevenWaySurvives` (2 tests).
**Verdict.** SURVIVES; PROVED stands.
**Wall.** Infinite X is checked on paper only. There is no finite receipt for an infinite-sup failure, and none should exist given the infinitary QL/QR proof.

### S-2. CG-7 sandwich, hierarchy and Boolean census: SURVIVES (numbers reproduced)

**Attack.**
- Independent Boolean census of all 2,594 relation/partition models (n ≤ 3, surjective q).
  - Counts reproduced exactly: may* = must* without lumpable **462**; exact without may* = must* **384**; unpointed without exact **384**; forward without backward **240**; backward without forward **240**.
  - The chain lumpable ⇒ may* = must* ⇒ exact ⇒ unpointed never fails.
- Sandwich Q∀* ≤ M ≤ ρ̂_x ≤ S ≤ Q∃*: 60 random Rel(2) models on 3–4 states, with q non-surjective into 4 reports. It never fails, including at ⊤-rows of Q∀ at empty fibres.

**Receipt.** `S02_CG7_CensusAndSandwich.test_boolean_census_2594`, `test_sandwich_rel2_nonsurjective`.
**Verdict.** SURVIVES. Note that the reviewed test only asserts that these kinds *exist*; it does not pin the counts. See S-18.

### S-3. CG-7 "every link can be strict, including **both outer links at one (x,b)**": REQUIRES REPAIR (wrong receipt)

**Target.** OPUS_II §CG-7, the statement line and "Tropical reading". The cited receipt is fibre A = {0,1,2} with 0→3 (2), 1→3 (1), giving "(∞, 2, 1)". It is tested as `test_both_inequalities_strict_at_one_start`.

**Receipt.** My own computation of the full five-term chain at that receipt is

  (Q∀*, M, ρ̂₀, S, Q∃*) = (∞, ∞, 2, 1, 1).

Both **outer** links (Q∀* ≤ M and S ≤ Q∃*) are **equalities**. Only the composite inequalities Q∀* ≤ ρ̂ ≤ Q∃* are strict. The cited receipt therefore does not witness the claim, and the reviewed test does not test it.

**Further receipt.** In Boolean V the claim is impossible: Q∀* < M ≤ S < Q∃* needs three distinct values. This is checked exhaustively on all 2,594 models, with zero occurrences.

**Repair (the claim itself is true).** A saturating-tropical(3) receipt makes **all four links strict at one (x,b)**:
- states A = {0,1,5}, C = {2,3}, B = {4};
- edges 0→4 (1), 5→4 (2), 1→5 (1), 0→2 (0), 3→4 (0);
- at x = 5, b = B: (Q∀*, M, ρ̂₅, S, Q∃*) = (∞, 3, 2, 1, 0).

Replace the receipt, and add "requires a quantale with a chain of length ≥ 3 below ⊤; impossible in Bool".

**Test.** `test_S3_cited_receipt_does_not_witness_outer_links_but_tropical_one_does`, `test_S3_boolean_can_never_have_both_outer_links_strict`.

### S-4. CG-8 (adjunctions, residual side, both Beck–Chevalley conditions): SURVIVES

**Attack.**
1. **Residual side, noncommutative case.** Closedness is φ(u)⊗R ≤ φ(v), with the predicate on the **left**. So Int_R must use the **right** residual c/b = ⋁{a : a⊗b ≤ c}, and §0 does so.
   - In Rel(2) I checked, for every φ, that Int φ is closed, Int φ ≤ φ, and ψ ≤ φ ⇔ ψ ≤ Int φ for every closed ψ.
   - Mutation: the same construction with the left residual a\c **fails** the coreflection in Rel(2). The side is load-bearing and the report has it right.
2. **L = Cl_Q∘q_! ⊣ q^*|.** Checked on Rel(2) with an empty fibre (q = (0,0,1), m = 3), 150 random closed pairs per model, with no failure.
3. **Counit.** L q^*ψ = ψ on the image and ⊥ off it, holding exactly.
4. **Right Beck–Chevalley.** q_* preserves closedness ⇔ Q∃(R) ≤ Q←(R*) ⇔ backward exactness (∀a, z: Q*(a,q(z)) = ⋁_{q(x)=a} R*(x,z)).
   - Boolean exhaustive n ≤ 3 with **every second report empty**, and Rel(2) random: the three are always equivalent, and both verdicts occur.
   - So the right BC condition really is backward exactness, i.e. CG-3(1) for (R^op, V^rev). I re-derived this on paper: B = Q←(R*) is reflexive and transitive, including at empty b (⊤⊗⊥ = ⊥).
5. **Pairing receipt.** Edge 0→2, q = (0,1,1), φ = (1,0,1): q_*φ = (1,0) is not Q∀-closed but is Q←-closed. Reproduced.

**Receipt.** `S04_CG8_RightBeckChevalley` (4 tests).
**Verdict.** SURVIVES.

### S-5. CG-10 (arbitrary-join closure, unique coarsest exact refinement): SURVIVES, but MIS-ATTRIBUTION by omission

**Attack.**
- **Paper.** The coarsening argument uses only associativity of ⋁: a coarser partition's profile is a join of finer profiles. It is valid for arbitrary index families, infinite X, any quantale, and partitions not refining ker q.
- **Executable.**
  - Rel(2) and P(left-zero), 4 states, 25 random relations each.
  - Every pair of exact partitions has an exact join, and the discrete partition is exact.
  - For **every** one of the 15 partitions q: the join of all exact refinements of q is itself above all of them, and my own profile-splitting fixpoint returns exactly that join.
- **Meet and selected-start receipts** were reproduced with my own code.
- **"4 states minimal for meet failure"** holds for **every** quantale, for a structural reason. On ≤ 3 points, two partitions are either comparable or meet to the discrete partition, which is always exact. I checked this exhaustively over set partitions.

**Receipt.** `S05_CG10_JoinClosure` (3 tests).
**Verdict.** SURVIVES.

**Attribution.** CG-3(2) says exactness = (ordinary) lumpability of R*. Hence CG-10 is the classical fact that ordinarily-lumpable / stable partitions form a join-closed family with a unique coarsest refinement, computed by partition refinement. Sources: Kemeny–Snell 1960; P. Buchholz, *Exact and ordinary lumpability in finite Markov chains*, J. Appl. Prob. 31 (1994); Paige–Tarjan, SIAM J. Comput. 16 (1987); Derisavi–Hermanns–Sanders, IPL 87 (2003).

The report's honesty block lists lumpability, but CG-10 is presented ("surprising", "Correction to the brief") without these citations. **Repair:** add them, and label CG-10 CLASSICAL in substance.

### S-6. CG-5 (change of base): SURVIVES; truncation strictness confirmed

**Attack.**
- **Strictness on the finite truncations.** I built P(Σ^{≤2}+#) independently: 8 words and 256 languages, with the full 256² tensor check.
  - min-length → saturating-tropical(3) (# ↦ 3) is **strict**.
  - saturating-tropical(3) → Bool is **strict**.
  - budget-tropical(3) → Bool is oplax only: joins hold, it is not strict and not lax (2⊗1 = ∞).
- **Extra mutation.** min-length into the **budget** quantale is **not** strict. The saturating target is essential, and the report chose it correctly.
- **Oplax ⌊a/2⌋ receipt (4).** h is oplax and not strict. q is V-exact at 0, not V-exact at the reachable state 1, and W-ghosted at 0. Reproduced.
- **Lax receipts 5a and 5b** reproduced:
  - 5a is lax **only in the unit**; its tensor is strict ({0,1}+{0,1} = {0,1}). This is harmless, because 5b covers the strict-unit case.
- **Oplax transport of all-start exactness.** 150 random 3-state budget-tropical(3) models per map, for two oplax maps, all partitions: no failure.

**Receipt.** `S06_CG5_BaseChange` (3 tests).
**Verdict.** SURVIVES.

### S-7. CG-6(2) graded theorem: REQUIRES REPAIR (hypothesis not satisfiable by the lab's own instance)

**Target.** "deg: M → (ℕ,+) a monoid homomorphism … The truncated monoid Σ^{≤L} + # used in the lab is fine because # never has degree 1."

**Typed contradiction.**
- In Σ^{≤L}+#, #·x = # for any letter x.
- A monoid homomorphism to (ℕ,+) would need deg(#) + deg(x) = deg(#), so deg(x) = 0.
- That contradicts deg(x) = 1 for letters.
- So **no ℕ-valued degree exists on the lab's monoid**, and the theorem as stated does not cover the lab's evidence.

**Repair.** Let deg take values in (ℕ ∪ {∞}, +), with deg(#) = ∞. Equivalently, require only that a product of n degree-1 elements has degree n or ∞, and that the unit has degree 0. The proof goes through verbatim.

**Survival check.** Letter-valued relations on 3–4 states, 2 random report maps each, over P(Σ^{≤2}+#) and P(Σ^{≤3}+#) built independently: all-start exactness ⇔ one-step lumpability (bisimulation of ker q) holds in every case, and both verdicts occur.

**Receipt.** `S07_CG6_GradedTheorem`.

### S-8. CG-12 (whole distance ⇔ ker q ⊆ ≅): SURVIVES

**Attack.** 60 random models each over Rel(2) (non-integral: here "≅" needs k ≤ R*(x,x′), not ⊤) and over saturating tropical, on 3–4 states with random partitions. Equivalence held throughout; both verdicts occurred.

**Receipt.** `S08_CG12_WholeDistance`.
**Attribution** (skeleton / T₀ reflection) is correct.

### S-9. CG-13(4) "none on 3 states at τ = 1": REFUTED (receipt)

**Target.** OPUS_II §CG-13(4): "A 3-state example at τ = 2 was found by exhaustive search over weights in {−1,0,1} and τ ≤ 2. The same search found none on 2 states, and **none on 3 states at τ = 1**."

**Receipt.** I used the report's own conventions: A[y][x] is the weight of x → y; the source is Σ_{q(z)=b}(A^τ)[z][x]; the fibre-mean quotient is Ā.

| receipt | edges | q | from x at τ = 1: source (A, B) | quotient Ā (A, B) | outcome |
|---|---|---|---|---|---|
| (i) | x→x (1), x′→x′ (−1), x′→z (1) | (A, A, B) | (1, 0) | (0, ½) | report A **deleted**, report B **invented** |
| (ii) loop-free | x→x′ (1), x′→x (−1), x′→z (1) | (A, A, B) | (1, 0) | (0, ½) | same |

- The exhaustive count over all 3⁹ matrices with entries in {−1,0,1}, all three 2-block partitions and every start is > 0.
- With 2 states it is impossible: only one non-trivial report.
- So the **minimal** invent-and-delete instance is 3 states at τ = 1. The 4-state headline receipt is valid but not minimal.
- The search code behind the scoped observation is in no test file, so the false claim was never regression-checked.

**Repair.** Replace the sentence with: "Invent-and-delete needs ≥ 2 reports, hence ≥ 3 states, and 3 states at τ = 1 suffice (receipt). The 4-state example is illustrative." Delete or provide the unseen "3-state τ = 2 example".

**Status of the τ = 2 sentence.** UNVERIFIED — wall: the example is not given.

**Rest of CG-13 survives.**
- Sign balance with global sign ε: 150 random switch-equivalent matrices, τ ≤ 4, support = walks.
- Resolvent lumpability ⇔ lumpability, with the column-sum convention Σ_{q(z)=b} A[z][x] (Kemeny–Snell's row condition, transposed): 400 random cases on n = 3, 4 with entries in {−2,…,2}, half forced lumpable.
- Surjectivity is used only for the rank argument. For non-surjective q one restricts to the image and nothing changes.
- The generic-faithfulness polynomial claim is correct on paper: nonnegative integer walk counts, and a countable union over τ of proper algebraic sets is still null.

**Receipt.** `S09_CG13_SignedInventDelete` (4 tests).

### S-10. CG-1(a″) backward form ("proved by symmetry only; not separately tested"): SURVIVES

**Attack.**
- Exhaustive over P(left-zero) with n = 2: all 4,096 relations, all 64 candidate ψ.
- 120 random Rel(2) relations.
- R*(x,z) = ⋀{ψ(x) : R(u,v)⊗ψ(v) ≤ ψ(u), k ≤ ψ(z)} holds in every case.

**Receipt.** `S10_CG1_BackwardForm`. The gap the report itself flagged is now closed by a test.

### S-11. FO-2 (n+m−1 bound, sharpness, 2n−1): SURVIVES

**Attack.**
- **Counts.** My own minimiser and canonical BFS numbering reproduce **48** unary cores (≤ 4 states) and **11,500** two-instrument cores (≤ 3 states, binary readouts).
- **Bound and sharpness.** Exhaustive over all these cores, with independently simulated response vectors and prefix bucketing: two distinct cores of sizes n, m always disagree within length n+m−1, and the maximum agreement is **exactly n+m−2** for every size pair.
- **Sharp family.** My own cycle/chain construction, built from the prose definition (not the lab's `sharp_pair`), gives core sizes exactly (n, m) and agreement exactly n+m−2 for 1 ≤ n, m ≤ 6.
- **Conventions.** Readout-before-transition is Mealy, which gives N−1; Moore gives N−2. The refusal sink counts as a state after totalisation. Both are stated correctly.
- **2n−1.** This follows from (a) with m ≤ n, and its sharpness follows from (b) with m = n.

**Receipt.** `S11_FO2_CoresAndSharpness` (3 tests).

**Minor attribution.** Fine–Wilf is about two periodic words (bound p+q−gcd); the extremal pair here is a cycle against an eventually constant chain. "Lineage" is loose. Prefer Moore 1956 / Gill 1962 for n+m−1 and drop or soften Fine–Wilf.

### S-12. FO-3 (reduct-core identity, 3-state pure-intervention minimality): SURVIVES

**Attack.** I re-derived the minimality proof. On |X| = 2, ∼_A forces every A-readout to be constant, so a constant-readout b can expose nothing. This is exhaustive over all 2-state, 2-instrument carriers, and the 3-state receipt is reproduced, all with my own minimiser.

**Receipt.** `S12_FO3_Exposure`.

**Scope note.** The statement is for total carriers. With an unobservable refusal (the report's own "next falsification"), "pure intervention" is not even well-typed. This is UNVERIFIED — wall: no semantics are given for unobservable refusal.

### S-13. FO-4(ii) headline sentence: OVERCLAIM (wording); the mathematics SURVIVES

**Target.** "The order-r data at c0 are consistent with **every** j-independent function only when r < h_j(c0)."

**Receipt.** Literally false for every r ≥ 0 and every f. Two different j-independent functions already differ at c0, which lies in every ball, so the data cannot be consistent with both.

**Repair.** The bullets below the sentence prove the intended statement: "…consistent with **some** j-independent function iff r < h_j(c0)."

**Survival checks.**
- Horizon = ball horizon for all f: {0,1}³ → Z/2 and {0,1}² → Z/4, every baseline and every j.
- Transport formula Δ_V f(c0) = (−1)^{|V∩C|} Σ_{V⊆S⊆V∪C} Δ_S f(b): 200 random **integer** functions with k ≤ 5, signs included.
- NAND receipt: h_3 = (1,1,1,2,1,1,1,2) reproduced, and the exhaustive count **192 of 720** reproduced.

**Receipt.** `S13_FO4_FO5_Horizons` (3 tests).

### S-14. FO-6 exact cost 2·Σ_{i<d} C(k−1,i): SURVIVES (both bounds re-derived; strongest FO claim)

**Paper re-derivation.**
- **Lower bound.** Split h = u + x_j v. If |Q₁| < dim P_{d−1}(k−1), there is a nonzero v vanishing on Q₁, and h = x_j v is a j-dependent adversary vanishing on Q. Symmetrically, (x_j − 1)v handles Q₀. Q₀ and Q₁ are disjoint slices.
  - The construction is valid over any nontrivial abelian group: use ⟨g⟩ ≅ Z/p, or a rational kernel scaled into ⟨g⟩ ≅ Z.
- **Upper bound.** With Q₀ = Q₁ = B_{d−1}, subtracting the slices kills u **without** requiring u to vanish, leaving v = 0 on a unisolvent ball. This is the real reason the pair of balls works, and the report states it correctly.
- **Adaptivity.** On a j-independent input, an adaptive run must query a certifying set, so adaptivity does not help.

**Executable.**
1. GF(2), k ≤ 4, every d, j at both ends. I used my own predicate, "kernel dimension on P_d equals kernel dimension on the j-free part", which differs in formulation from the lab's row-space test. The ball pair certifies, and **every** set of size cost−1 fails.
2. **Full brute-force minimum over non-field groups.** Z/4 with k ≤ 3 and Z/6 with k ≤ 2: enumerate every h ∈ P_d with coefficients in the group, collect the zero-sets of the j-dependent ones, and minimise |Q| over all subsets. The minimum equals 2·Σ_{i<d} C(k−1,i) in every case.
3. Ball certification iff r ≥ d also holds over Z/4 and Z/6.

**Receipt.** `S14_FO6_CertificationCost` (2 tests).
**Verdict.** SURVIVES.
**Wall.** G = ℤ is paper only.

**Attribution (minor).** The lower bound is "each slice must be an interpolation set for RM(d−1, k−1)": evaluation-injective sets for Reed–Muller codes / multilinear interpolation. Hamming-ball unisolvence is classical. Cite (e.g. MacWilliams–Sloane, ch. 13) and label the cost formula PROVED / CLASSICAL ELEMENTARY.

### S-15. FO-9 exact identifiability criterion: SURVIVES; hypothesis |V_p| ≥ 2 is load-bearing

**Attack.**
- **A different DAG** from the lab's: root r with values {0,1,2} (ternary), root s binary, u with pa\* = {r, s}, v with pa\* = {u}. That is 1,536 networks.
  - The criterion family identifies the class.
  - Each of the 8 single-deletion mutants fails both the criterion and identification.
  - Clamping each root **separately**, with the other read, fails: joint clamping is necessary.
  - Unclamped full observation fails.
  - 40 random families drawn from a 160-experiment universe: criterion ⇔ identification in every case.
- **"Unrestricted class doing all the work?"** Yes. Necessity is witnessed by all-constant networks, so the iff is specific to the unrestricted class. The report says so (O2).
- **Value sets of size 1.** If a potential parent p has |V_p| = 1, a family that never clamps p still identifies the class: p ≡ 0, so context (0, c_r) is realised whenever r is clamped. The literal "clamp **all** of pa\*(i)" condition is then not necessary.
  - The FO-9 statement does assume |V_p| ≥ 2, so this is a scope confirmation, not a refutation.
  - But summary row C6 drops the hypothesis. **Repair:** add "(all value sets of size ≥ 2)" to C6, or restate the criterion over parents with |V_p| ≥ 2 only.
- **Cyclic D.** Out of scope; networks are not even well-defined without a fixed-point semantics. The report excludes cycles.
- **Parentless nodes** are correctly exempt.

**Receipt.** `S15_FO9_IdentifiabilityOwnDAG`, `S15b_FO9_SingletonValueSetBoundary`.

### S-16. FO-8 minimality (cancellation; gating): SURVIVES

**Attack.** Own evaluator, exhaustive:
- the binary chain x→z→y with ternary y always composes;
- every monotone network with one binary hidden node and a path through z composes; there are exactly 6 monotone 2-input tables.

**Wording note.** The "two binary hidden nodes" gate of (b2) is itself a constant gate (z2 ≡ 0) on the edge z1→y. So (b1) and (b2) are one mechanism (constant gate) at two placements, and (b3) is the genuinely different range-restriction mechanism. The minimality statements are unaffected.

**Receipt.** `S16_FO8_Gating`.

### S-17. FO-10 (belief fixed point, sufficient conditions, refutations): SURVIVES; census reproduced; bound attainment answered partly

**Attack.**
- **Independent solver.** My belief game runs on **original states** (not classes) and has **no fusion pruning**: fused beliefs are simply never settled. It therefore does not presuppose the report's "fused ⇒ lost" lemma.
- **Census over all 46,916 two-instrument carriers with ≤ 3 states and S = X.** Exact agreement with the report's table:

  | property | count |
  |---|---|
  | free | 42,380 |
  | class non-disturbing | 3,596 |
  | class-injective | 6,344 |
  | free, not injective | 36,036 |
  | commuting-idempotent | 3,828 |
  | commuting-idempotent, not free | 384 |

  - Non-disturbing ⇒ free and injective ⇒ free hold throughout.
  - Lee–Yannakakis q(q−1)/2 holds, with maximum depth 3 at q = 3.
- **Termination and all horizons.** The win operator is monotone on a finite set of reachable beliefs, and a winning tree has finite depth. Depth ≤ number of beliefs. Re-derived on paper.
- **Receipts reproduced.**
  - A,B,C: commuting and idempotent, not free, and 1[C] inaccessible.
  - A,B,C,D: all 8 Boolean targets accessible, each in ≤ 1 step; the class is inaccessible.
  - reset_and_readout: free, not injective.
  - readout_swap: free, disturbing.
- **Depth bound (s−1)(q−1).** Never violated, including for **every start subset** S of every class-injective carrier with ≤ 3 states.
  - It is attained at (s,q) = (2,3), with depth 2.
  - It is **not** attained at s = q = 3: the maximum is 3, below the bound 4. This partly answers open item O3; tightness in general remains open.

**Receipt.** `S17_FO10_FreeObservability` (2 tests).
**Wall.** The complexity of the start-subset version is not checked, as the report also says.

### S-18. Test-suite audit (vacuous, circular, unpinned, sampling-dependent)

1. **Numbers in prose that no test pins.**
   - CG-7 census 462 / 384 / 384 / 240 / 240: `test_boolean_2594…` only asserts that the kinds exist.
   - FO-10 table of six counts: `test_sufficient_conditions…` asserts only `> 0` for two of them.
   - CG-13(4) search claims: no test at all, and one of them is false (S-9).

   All the census numbers are now pinned by independent code in this file.
2. **Circular predicate.** `test_certification_cost_exhaustive` checks both the upper and the lower bound with the lab's own `certifies_absence`. It is now closed by S-14's independent predicate and the Z/4 and Z/6 brute force.
3. **Vacuous.**
   - `test_naive_dimension_count_is_only_half` checks only the binomial identity 2(dim P_d − dim P_d^{j-free}) = cost. It is no evidence about certification.
   - `test_class_prior_can_lower_the_detection_order` asserts three trivial facts and does not enumerate the class.
4. **Mislabelled.**
   - `test_both_inequalities_strict_at_one_start` does not test the "outer links" claim it is cited for (S-3).
   - `test_target_not_constant_on_class_is_refused` checks "not accessible", not a refusal; the behaviour is correct.
5. **Untested claims.** FO-9(iii) degree prior (the report admits this). CG-1(a″) was untested, and is now tested (S-10).
6. **Sampling-dependent (seeded).**
   - CG: three-state weighted sample; transport sample; CG-10 weighted sample.
   - FO: reconstruction sample of 2,500; 250 random FO-9 families; random carriers in the cross-checks.

   These are acceptable as seeded regression tests, but must be read as OBSERVED (sample), not exhaustive.

### S-19. Attribution summary

| item | issue | repair |
|---|---|---|
| CG-10 | Coarsest lumpable / stable refinement is classical | Cite Buchholz 1994, Paige–Tarjan 1987, Derisavi–Hermanns–Sanders 2003; label CLASSICAL in substance (S-5) |
| CG-3(2)/(6) | "R* lumpable" is ordinary lumpability | Cite Kemeny–Snell at the statement |
| FO-6 | Interpolation / Reed–Muller lower bound | Cite (S-14) |
| FO-2(b) | Fine–Wilf lineage is loose | Use Moore / Gill (S-11) |
| CG-13(2) | Global sign ε = −1 is *antibalance* | Cite Harary 1957 next to Harary 1953 |

Citations I checked and believe correct: Lee–Yannakakis (IEEE Trans. Computers 43(3), 1994; ADS depth n(n−1)/2); Kuo–Sloan–Wasilkowski–Woźniakowski (Math. Comp. 79, 2010); Rota 1964; Kelly–Street 1974; Kemeny–Snell 1960. Bibliographic details beyond these were not verified (no network lookup).

### S-20. Items attacked with no defect found (brief list)

- **CG-1 (a)/(a′).** The left-residual side is right: my wrong-side check refutes the alternative in Rel(2).
- **CG-2.**
- **CG-4.**
- **CG-6(1).** Integral needs 3 states; P(Z/2) gives a 2-state ghost. Re-derived.
- **CG-9.** The tropical residual max(c−a, 0) is the shortcut amount. Re-derived.
- **CG-11.** Completeness needs no attainment. Re-derived.
- **FO-1(6).** Re-derived.
- **FO-7.** Classical.

None of these needed a receipt.

---

## Most damaging five (ranked)

1. **S-9.** A false "exhaustive search" observation in CG-13(4): 3 states at τ = 1 do invent-and-delete. It is a provenance-integrity defect, because the search is unpinned and its result is wrong.
2. **S-3.** CG-7's "both outer links strict at one (x,b)" is cited to a receipt in which both outer links are equalities. The claim is true but impossible in Bool, and needs the replacement receipt.
3. **S-18.** Census numbers in both reports are not regression-pinned (CG-7 counts, FO-10 table), and the CG-13 search is untested. Reproduced here, so they are now pinned.
4. **S-7.** The CG-6(2) hypothesis "deg: M → ℕ" is unsatisfiable on the lab's truncated monoid. Repair: ℕ ∪ {∞}.
5. **S-13 together with S-5/S-19.** A literally false headline sentence in FO-4(ii) ("every" → "some"), and classical results (coarsest lumpable refinement; interpolation-set lower bound) presented without the classical sources.

## Strongest statements that survived everything thrown at them

- **CG-3** seven-way equivalence: noncommutative, non-integral, non-P(M) Rel(2); non-surjective q; empty fibres; paper check for infinite X.
- **CG-8** adjunctions with the right residual; right BC ⇔ backward exactness. The left-residual mutation fails.
- **CG-10** arbitrary-join closure and the splitting fixpoint equalling the brute-force maximum over Rel(2) and left-zero.
- **FO-6** exact cost 2·Σ_{i<d} C(k−1,i): independent GF(2) predicate, and a full brute-force minimum over Z/4 and Z/6.
- **FO-2** n+m−1 / n+m−2: exhaustive over 11,500 independently minimised cores.
- **FO-10** census, with a belief game that does not assume the fusion lemma.
- **FO-9** criterion on a ternary, two-root-parent DAG.

## What this referee could not check

- Infinite-X statements (paper only).
- CG-13(7) measure-zero (paper only).
- FO-6 over G = ℤ (paper only).
- Lean formalisation (none exists).
- Exhaustive three-state models over 8- or 16-element quantales (sampled only).
- Three-instrument or ternary-readout FO-2 enumeration.
- Lee–Yannakakis complexity for start subsets.
- The unseen "3-state τ = 2" signed example.
- Bibliographic page numbers.
