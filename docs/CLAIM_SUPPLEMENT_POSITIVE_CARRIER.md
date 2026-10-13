# Positive carrier realization supplementary claim ledger

**Namespace:** PCR-01–PCR-41; add to historical O1–O638, Cambrian O639–O679, SWM-*, EOS-* and
CAR-01–CAR-21 WITHOUT renumbering, collision, or promoting unverified source claims.
Part I: [dossier](../research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY.md) ·
[frozen receipt](../research/2026-10-13/POSITIVE_CARRIER_RECEIPT.json) ·
[Lean core](../formal/EODCS_PositiveCarrier.lean).
Part II (audit of Part I, field of definition, ghost freedom):
[dossier II](../research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY_II.md) ·
[frozen receipt II](../research/2026-10-13/POSITIVE_CARRIER_II_RECEIPT.json) ·
[Lean core II](../formal/EODCS_PositiveCarrierII.lean).  Part II amends PCR-05, PCR-09, PCR-19 and
PCR-22 in place (marked **[amended II]**) without renumbering.

| ID | Claim | Status | Exact evidence / limitation |
|---|---|---|---|
| PCR-01 | The calibration matrix P is row-stochastic, rank 3 with r1−r2−r3+r4=0, nonnegative rank 4 | CLASSICAL / LEAN-KERNEL VERIFIED core | `calibration_fooling_bound` (nonnegative integer factorizations of the support pattern need ≥ 4 terms; rational case by clearing denominators); exact receipt `calibration` |
| PCR-02 | The one-stage rank of P equals the full sequential Hankel rank of PW₁ | PROVED LOCAL (not assumed) | Theorem 7.1: dependence ε=(1,−1,−1,1) survives the step and the silent swap; exact minimal realization dim 3 |
| PCR-03 | PW₁ (lazy path walk + observed position + silent non-commuting swap) has linear dimension 3, every positive carrier of its complete behavior has ≥ 4 states, and a 4-state carrier exists | PROVED LOCAL / TESTED | fooling set on diag(p)·P block from the single uniform source; oracle FINITE_OBSTRUCTION at 3, LAWFUL_REALIZATION at 4 with exact equivalence certificate |
| PCR-04 | PWₙ has linear dimension 3ⁿ and positive carrier dimension 4ⁿ | PROVED LOCAL / TESTED n≤2 | tensor-product span and product fooling sets; n=2 block rank 9, fooling 16 verified |
| PCR-05 | (r, d⁺)=(3,4) is the smallest possible gap pair: r ≤ 2 forces d⁺ = r over ℝ **[amended II]** | PROVED LOCAL (ℝ); over ℚ REFUTED (PCR-27) | Theorem 5.1 via the closed reachable cone in ℝ²; over ℚ the Fibonacci cat system has r = 2 and d⁺_ℚ = ∞ (II.3) |
| PCR-06 | Cone ⇒ carrier: normalized (N), source-containing (P), invariant (I), mass-conserving (M) finitely generated cone yields explicit column-stochastic B_{a,z} and convex λ_σ with the same complete behavior | CLASSICAL / PROVED LOCAL / TESTED | Theorem 4.1; `verify_cone` exact LP; pointedness, convexity, nonzero generators derived from (N); (M) derived on minimal realizations |
| PCR-07 | Carrier ⇒ cone: an m-state carrier gives an observable extension W ⊇ V_min with an m-generator invariant normalized cone; the intersection with V_min is polyhedral invariant but may need more than m generators | CLASSICAL / PROVED LOCAL | Theorem 4.2; restricted vs unrestricted distinction (Gillis–Glineur) |
| PCR-08 | Exact criterion: d⁺ < ∞ iff a polyhedral cone K with R̄ ⊆ K ⊆ P is invariant under all events (Heller's theorem, controlled source-indexed bottom-completed form) | CLASSICAL core / PROVED LOCAL specialization | Theorem 4.3; normalization automatic by Lemma 3.2 |
| PCR-09 | Existence over ℝ does not give existence over ℚ at the same size: a rational behavior with d⁺_ℝ = 6, d⁺_ℚ = 7 **[amended II: superseded by PCR-27, which is smaller (r = 2) and infinite]** | EXTERNAL THEOREM (CKMSW 2017) + PROVED LOCAL transfer (Lemma 7.4) | one-shot embedding d⁺ = rank₊ + 1; matrix not reproduced here |
| PCR-10 | For fixed m, real m-state realizability is in the existential theory of the reals; finiteness of d⁺ is only semi-decided; ℚ-decidability open | CLASSICAL / UNVERIFIED (finiteness) | Prop. 4.5(c); no termination claim for the search |
| PCR-11 | If an m-state positive carrier exists then every peripheral eigenvalue of every minimal-realization event-word operator is ρ times a root of unity of order ≤ m | PROVED LOCAL (classical ingredients: Frobenius, Fox–Rubin, ADFB 1996) | Theorem 6.1: positively reachable restriction, sub-quotient spectrum inclusion, exact mass growth, imprimitivity index |
| PCR-12 | The rational clock (cos θ = 3/5) is a valid 3-dimensional behavior with no finite positive carrier | PROVED LOCAL; LEAN-KERNEL VERIFIED number theory | Theorem 7.2; `gaussian_rotation_never_real`; 19,682 words exact-nonnegative; charpoly (x−½)(x²−(3/5)x+¼) |
| PCR-13 | Cyclotomic clock C_k: linear dimension 1+φ(k), positive dimension exactly k | PROVED LOCAL / TESTED k∈{3,4,5,6,8,10,12,30} | lower bound by PCR-11 with ½ζ_k; upper bound by exact-LP-verified k-orbit cone and equivalence certificate; k−1 generators fail |
| PCR-14 | Support certificates (fooling/Boolean rank) are blind to C_k's gap and spectral certificates are blind to PWₙ's gap | PROVED LOCAL | C₆ Hankel block strictly positive (fooling bound 1 vs truth 6); PW operators have rational spectra |
| PCR-15 | Legality is a function of the bottom-completed behavior: a available after (σ,u) iff p_σ(u a ⊥) = 0 | PROVED LOCAL | Prop. 8.1; ⊥ is a representation change, not a sensor (`BOT` declared only on total actions) |
| PCR-16 | Equal legal behavior + equal legality pattern ⇒ every public-history adaptive policy (randomized, stopping) is legal in both and has identical closed-loop joint laws and source posteriors | PROVED LOCAL; LEAN-KERNEL VERIFIED skeleton | Theorem 8.2; `closed_loop_law_transport`, `posterior_data_transport`; exact tests incl. randomized policy on PW₁ vs its cone carrier |
| PCR-17 | Positivity of the legal-word behavior suffices for lawful realization | REFUTED | Prop. 8.3 minimal square: 1-state COARSE realizes every legal probability yet promotes b; d⁺_law = 2 |
| PCR-18 | A lawful carrier with m states shows at most 2^m − 1 menus; d⁺_law ≥ log₂(#menus + 1) | PROVED LOCAL | Lemma 8.4 |
| PCR-19 | The weakest source-preserving repair of a failed availability square is CAR-4's q* with the enabledness component (quotient form) / realizing the bottom completion (realization form); d⁺_law ≤ d⁺_⊥ **[amended II]** | quotient clause PROVED LOCAL; realization clause REFUTED (PCR-31/32); d⁺_law < d⁺_⊥ RESOLVED (strict, unbounded) | Prop. 8.5 corrected in II §7: the bottom completion fixes ghost values and costs up to 4ⁿ states; the weakest repair is the coarsest lawful carrier of the operational profile |
| PCR-20 | Destructive observation never destroys original-source evidence in a complete-behavior realization: posteriors are ratios of behavior values | PROVED LOCAL | Remark 8.6 + Theorem 8.2; quotient instance CAR-13 |
| PCR-21 | Costs/budgets are a graded product with the counter; they bound dimensions by (B+1) factors and do not interact with positivity | PROVED LOCAL (elementary) | Prop. 8.7 |
| PCR-22 | The oracle's four verdicts are sound; UNRESOLVED is never upgraded to impossibility; refinement explores only reachable rays and is complete only for finitely-reachable-generated cones **[amended II]** | soundness PROVED LOCAL / TESTED; the termination claim of Prop. 4.6 was FALSE as implemented and is fixed (PCR-36) | Prop. 4.6, Prop. 10.1; clock search stalls UNRESOLVED; PW₁ and C_k found; Fibonacci creep bounded by `max_rounds` |
| PCR-23 | d⁺_res > d⁺ occurs for behaviors (via Gillis–Glineur matrices and Lemma 7.4) | EXTERNAL THEOREM + PROVED LOCAL transfer; instance not exhibited | Prop. 4.4; recurrent-process instance UNVERIFIED |
| PCR-24 | The naive boxed equivalence "behavior + normalized invariant cone + lawful structure ⟺ finite source-faithful carrier" holds only in the corrected form of Theorem 9.1; its naive readings are refuted by PCR-17, PCR-03/12/13, PCR-09 | PROVED LOCAL (corrected) / REFUTED (naive) | Theorem 9.1 (A)–(D) |

Scope booleans frozen in the Part I receipt: `empirically_authenticated_source=false`,
`rational_vs_real_positive_dimension_gap_exhibited_here=false` (Part I; Part II exhibits it),
`restricted_vs_unrestricted_cone_gap_exhibited_here=false`,
`whole_program_Lean_refinement_proved=false`,
`general_decidability_of_finite_positive_dimension_claimed=false`, `main_merge_executed=false`.

## Part II claims (PCR-25 – PCR-40)

| ID | Claim | Status | Exact evidence / limitation |
|---|---|---|---|
| PCR-25 | Rational cone theorem: for a subfield F ⊆ ℝ, d⁺_F < ∞ iff an F-rational polyhedral cone K with R̄ ⊆ K ⊆ P is invariant under all events; m F-rational generators give d⁺_F ≤ m | CLASSICAL core (Weyl–Minkowski over ordered fields, LP basic solutions) / PROVED LOCAL | II Theorem II.1 |
| PCR-26 | Irrational contact: a ray in R̄ that is an extreme ray of P is an extreme ray of every sandwiched polyhedral cone; an irrational such ray forces d⁺_ℚ = ∞ and Fld ⊇ ℚ(ray) | PROVED LOCAL | II Theorem II.2; finite ℚ(√D) certificate `two_dimensional_contact_certificate` with mutation controls |
| PCR-27 | Fibonacci cat system (A=[[2,1],[1,1]]/4 and A⁻¹/4 with resets): valid, r = 2, d⁺_ℝ = 2 with the explicit ℚ(√5) carrier ((3±√5)/8, 1/4 entries), d⁺_ℚ = ∞, Fld = ℚ(√5) | PROVED LOCAL; LEAN-KERNEL VERIFIED number-theoretic core | II Theorem II.3; `golden_carrier` exact in ℚ(√5); `golden_slope_irrational`; receipt `fibonacci_cat_system` (21,844 words nonnegative, orbit slopes = Fibonacci ratios) |
| PCR-28 | The ℚ/ℝ positive-realization gap occurs at the smallest possible linear dimension (2) and is infinite; one-shot matrices of rank ≤ 2 never separate | PROVED LOCAL | PCR-27 + rank-2 NMF rationality (extreme columns) |
| PCR-29 | Dimension-two dichotomy: r = 2 (rational data) ⇒ d⁺_ℝ = 2 and d⁺_ℚ ∈ {2, ∞}; d⁺_ℚ = 2 iff a rational invariant sandwiched sector exists | PROVED LOCAL | II Theorem II.4; positive control FINE (sector [0,2]); Fibonacci: grid UNRESOLVED, contact ⇒ ∞ |
| PCR-30 | Operational profile Π(K) (legal histories, values, menus) is the invariant of public-history policy transport; ghost values p_⊥(u a z) for unavailable a are unmeasurable | PROVED LOCAL (Part I Thm 8.2 reread) | II D-II.2 |
| PCR-31 | Ghost freedom: d⁺_law(K) = min over lawful completions p′ of Π(K) of d⁺(p′); the bottom completion is one completion | PROVED LOCAL | II Theorem II.5 (restriction/zeroing construction both ways) |
| PCR-32 | Ghost gap: PHₙ has d⁺_law = 1 and d⁺_⊥ = 4ⁿ + 1; with a legal source d⁺_law = 2, d⁺_⊥ ≥ 4ⁿ + 1; r(p_⊥(PH₁)) = 4 vs r_law = 1 | PROVED LOCAL / TESTED n ≤ 2 | II Theorem II.6; ghost blocks (1/16)P and (1/32)P⊗P with fooling 4 and 16; refusal mass ½ |
| PCR-33 | "Realize the bottom completion" is NOT the weakest source-preserving repair; the weakest is the coarsest lawful carrier of Π(K) | REFUTED (Part I clause) / PROVED LOCAL (corrected) | II §7 |
| PCR-34 | Refusal completion p̃ is a function of Π(K) and recovers it; realized by the support-uniform completion SU(K) (≤ &#124;C&#124;·2^&#124;C&#124; states); Π(K₁) = Π(K₂) iff SU(K₁) ≡ SU(K₂), decided exactly with a legal-value or menu witness | PROVED LOCAL / TESTED | II Prop. II.7; `profile_equivalence_certificate`; availability square separated at (mixed, b·ok) as a menu difference |
| PCR-35 | Public menu = intersection of per-source menus over compatible sources is the only menu a public-history controller may use (otherwise the menu is a hidden-source sensor); it is a function of Π | PROVED LOCAL | `public_menu`; CAR-07 made executable |
| PCR-36 | Part I's `reachable_cone_refinement` does not terminate on the Fibonacci system (generator count stays at 4; rounds replace outer rays by Fibonacci convergents with denominators F_k); fixed by a round bound; soundness unchanged; Part I receipt unchanged | REFUTED (Part I termination claim) / PROVED LOCAL (corrected) | II Theorem II.10; test `test_no_rational_interval_and_creeping_refinement` |
| PCR-37 | Blind spot exhibited: the diagonal contraction has r = 3, a reachable cone with infinitely many extreme rays (orbit on the parabola y = x²), hence the reachable-ray refinement never finds a carrier, yet d⁺ = 3 (triangle cone (1,1),(−2,1),(1,−2)); the grid search finds a 3-state carrier | PROVED LOCAL / TESTED | II Example II.9; receipt `blind_spot_diagonal_contraction` |
| PCR-38 | General fooling-set theorem: k positive pairwise-fooling cells in a nonnegative integer factorization with m terms ⇒ k ≤ m (any shape); pigeonhole proved from scratch | LEAN-KERNEL VERIFIED (propext, Quot.sound, Classical.choice) | `fooling_set_bound`, `fin_injective_le` |
| PCR-39 | Menus are functions of supports ⇒ ≤ 2^m distinct menus for an m-state carrier (Part I Lemma 8.4) | LEAN-KERNEL VERIFIED | `menu_count_bound`, `supportCode_injective` |
| PCR-41 | The three identities of the cone theorem (word intertwining, behavior transport under τG = 1ᵀ, column-stochasticity from mass conservation on generators) hold over any commutative semiring; instantiated at ℕ and ℤ | LEAN-KERNEL VERIFIED (`EODCS_PositiveCarrierCone.lean`) | closes Part I's Lean-ready plan; ℚ-instance not constructed (no algebra library in the no-mathlib lane); nonnegativity is a hypothesis, not an identity |
| PCR-40 | Part II oracle composition (Part I verdicts → grid search → interval search → contact certificate with `field="Q"`) is sound and never reports a ℚ-obstruction as an ℝ-obstruction | PROVED LOCAL / TESTED | `carrier_realization_oracle_ii`; five routes smoke-tested |

Scope booleans frozen in the Part II receipt: `rational_vs_real_positive_dimension_gap_exhibited_here=true`,
`rational_vs_real_gap_is_infinite_at_linear_dimension_two=true`,
`ghost_gap_d_law_strictly_below_d_bottom_exhibited_here=true`, `bottom_completion_is_weakest_repair=false`,
`reachable_ray_refinement_complete=false`, `general_decidability_of_finite_positive_dimension_claimed=false`,
`general_decidability_of_rational_positive_dimension_claimed=false`, `cone_theorem_identities_lean_formalized_over_commutative_semiring=true`, `cone_theorem_lean_formalized_over_Q=false`,
`empirically_authenticated_source=false`, `main_merge_executed=false`.
