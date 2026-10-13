# Positive carrier realization supplementary claim ledger

**Namespace:** PCR-01–PCR-24; add to historical O1–O638, Cambrian O639–O679, SWM-*, EOS-* and
CAR-01–CAR-21 WITHOUT renumbering, collision, or promoting unverified source claims.
[Dossier](../research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY.md) ·
[frozen receipt](../research/2026-10-13/POSITIVE_CARRIER_RECEIPT.json) ·
[Lean core](../formal/EODCS_PositiveCarrier.lean).

| ID | Claim | Status | Exact evidence / limitation |
|---|---|---|---|
| PCR-01 | The calibration matrix P is row-stochastic, rank 3 with r1−r2−r3+r4=0, nonnegative rank 4 | CLASSICAL / LEAN-KERNEL VERIFIED core | `calibration_fooling_bound` (nonnegative integer factorizations of the support pattern need ≥ 4 terms; rational case by clearing denominators); exact receipt `calibration` |
| PCR-02 | The one-stage rank of P equals the full sequential Hankel rank of PW₁ | PROVED LOCAL (not assumed) | Theorem 7.1: dependence ε=(1,−1,−1,1) survives the step and the silent swap; exact minimal realization dim 3 |
| PCR-03 | PW₁ (lazy path walk + observed position + silent non-commuting swap) has linear dimension 3, every positive carrier of its complete behavior has ≥ 4 states, and a 4-state carrier exists | PROVED LOCAL / TESTED | fooling set on diag(p)·P block from the single uniform source; oracle FINITE_OBSTRUCTION at 3, LAWFUL_REALIZATION at 4 with exact equivalence certificate |
| PCR-04 | PWₙ has linear dimension 3ⁿ and positive carrier dimension 4ⁿ | PROVED LOCAL / TESTED n≤2 | tensor-product span and product fooling sets; n=2 block rank 9, fooling 16 verified |
| PCR-05 | (r, d⁺)=(3,4) is the smallest possible gap pair: r ≤ 2 forces d⁺ = r over ℝ | PROVED LOCAL (ℝ); ℚ UNVERIFIED | Theorem 5.1 via the closed reachable cone in ℝ²; Remark 5.2 names the ℚ risk |
| PCR-06 | Cone ⇒ carrier: normalized (N), source-containing (P), invariant (I), mass-conserving (M) finitely generated cone yields explicit column-stochastic B_{a,z} and convex λ_σ with the same complete behavior | CLASSICAL / PROVED LOCAL / TESTED | Theorem 4.1; `verify_cone` exact LP; pointedness, convexity, nonzero generators derived from (N); (M) derived on minimal realizations |
| PCR-07 | Carrier ⇒ cone: an m-state carrier gives an observable extension W ⊇ V_min with an m-generator invariant normalized cone; the intersection with V_min is polyhedral invariant but may need more than m generators | CLASSICAL / PROVED LOCAL | Theorem 4.2; restricted vs unrestricted distinction (Gillis–Glineur) |
| PCR-08 | Exact criterion: d⁺ < ∞ iff a polyhedral cone K with R̄ ⊆ K ⊆ P is invariant under all events (Heller's theorem, controlled source-indexed bottom-completed form) | CLASSICAL core / PROVED LOCAL specialization | Theorem 4.3; normalization automatic by Lemma 3.2 |
| PCR-09 | Existence over ℝ does not give existence over ℚ at the same size: a rational behavior with d⁺_ℝ = 6, d⁺_ℚ = 7 | EXTERNAL THEOREM (CKMSW 2017) + PROVED LOCAL transfer (Lemma 7.4) | one-shot embedding d⁺ = rank₊ + 1; matrix not reproduced here |
| PCR-10 | For fixed m, real m-state realizability is in the existential theory of the reals; finiteness of d⁺ is only semi-decided; ℚ-decidability open | CLASSICAL / UNVERIFIED (finiteness) | Prop. 4.5(c); no termination claim for the search |
| PCR-11 | If an m-state positive carrier exists then every peripheral eigenvalue of every minimal-realization event-word operator is ρ times a root of unity of order ≤ m | PROVED LOCAL (classical ingredients: Frobenius, Fox–Rubin, ADFB 1996) | Theorem 6.1: positively reachable restriction, sub-quotient spectrum inclusion, exact mass growth, imprimitivity index |
| PCR-12 | The rational clock (cos θ = 3/5) is a valid 3-dimensional behavior with no finite positive carrier | PROVED LOCAL; LEAN-KERNEL VERIFIED number theory | Theorem 7.2; `gaussian_rotation_never_real`; 19,682 words exact-nonnegative; charpoly (x−½)(x²−(3/5)x+¼) |
| PCR-13 | Cyclotomic clock C_k: linear dimension 1+φ(k), positive dimension exactly k | PROVED LOCAL / TESTED k∈{3,4,5,6,8,10,12,30} | lower bound by PCR-11 with ½ζ_k; upper bound by exact-LP-verified k-orbit cone and equivalence certificate; k−1 generators fail |
| PCR-14 | Support certificates (fooling/Boolean rank) are blind to C_k's gap and spectral certificates are blind to PWₙ's gap | PROVED LOCAL | C₆ Hankel block strictly positive (fooling bound 1 vs truth 6); PW operators have rational spectra |
| PCR-15 | Legality is a function of the bottom-completed behavior: a available after (σ,u) iff p_σ(u a ⊥) = 0 | PROVED LOCAL | Prop. 8.1; ⊥ is a representation change, not a sensor (`BOT` declared only on total actions) |
| PCR-16 | Equal legal behavior + equal legality pattern ⇒ every public-history adaptive policy (randomized, stopping) is legal in both and has identical closed-loop joint laws and source posteriors | PROVED LOCAL; LEAN-KERNEL VERIFIED skeleton | Theorem 8.2; `closed_loop_law_transport`, `posterior_data_transport`; exact tests incl. randomized policy on PW₁ vs its cone carrier |
| PCR-17 | Positivity of the legal-word behavior suffices for lawful realization | REFUTED | Prop. 8.3 minimal square: 1-state COARSE realizes every legal probability yet promotes b; d⁺_law = 2 |
| PCR-18 | A lawful carrier with m states shows at most 2^m − 1 menus; d⁺_law ≥ log₂(#menus + 1) | PROVED LOCAL | Lemma 8.4 |
| PCR-19 | The weakest source-preserving repair of a failed availability square is CAR-4's q* with the enabledness component (quotient form) / realizing the bottom completion (realization form); d⁺_law ≤ d⁺_⊥ | PROVED LOCAL; strictness UNVERIFIED | Prop. 8.5 |
| PCR-20 | Destructive observation never destroys original-source evidence in a complete-behavior realization: posteriors are ratios of behavior values | PROVED LOCAL | Remark 8.6 + Theorem 8.2; quotient instance CAR-13 |
| PCR-21 | Costs/budgets are a graded product with the counter; they bound dimensions by (B+1) factors and do not interact with positivity | PROVED LOCAL (elementary) | Prop. 8.7 |
| PCR-22 | The oracle's four verdicts are sound; UNRESOLVED is never upgraded to impossibility; refinement explores only reachable rays and is complete only for finitely-reachable-generated cones | PROVED LOCAL / TESTED | Prop. 4.6, Prop. 10.1; clock search stalls UNRESOLVED; PW₁ and C_k found |
| PCR-23 | d⁺_res > d⁺ occurs for behaviors (via Gillis–Glineur matrices and Lemma 7.4) | EXTERNAL THEOREM + PROVED LOCAL transfer; instance not exhibited | Prop. 4.4; recurrent-process instance UNVERIFIED |
| PCR-24 | The naive boxed equivalence "behavior + normalized invariant cone + lawful structure ⟺ finite source-faithful carrier" holds only in the corrected form of Theorem 9.1; its naive readings are refuted by PCR-17, PCR-03/12/13, PCR-09 | PROVED LOCAL (corrected) / REFUTED (naive) | Theorem 9.1 (A)–(D) |

Scope booleans frozen in the receipt: `empirically_authenticated_source=false`,
`rational_vs_real_positive_dimension_gap_exhibited_here=false`,
`restricted_vs_unrestricted_cone_gap_exhibited_here=false`,
`whole_program_Lean_refinement_proved=false`,
`general_decidability_of_finite_positive_dimension_claimed=false`, `main_merge_executed=false`.
