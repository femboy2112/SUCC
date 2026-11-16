# Main XXVI foundations and observer-interface audit

Audit date: 2026-11-16. Scope: exact active heads #618–#644 and #655, with focused examination of the source/authentication/observer/Gamma/detector contracts. This is an independent same-model mathematical/code review, not external peer review. No imported classical theorem receives new formal authority here.

## Source and ancestry

The audit read `AGENTS.md` and `docs/METHOD.md`, then actual proof and implementation files through immutable Git heads. The isolated worktrees are `foundations_review` at #644 `bbe8b815754edf08c69e613d40ef8062f0edfa91` and `foundations_alt` at #643 `8097d9e802da1d83a615d8812e74279820f5ae7e`. No shared integration checkout was edited.

- #618→#619; independently developed #620; #622 has #618/#619/#620 in its ancestry. Integrating #622 imports all three once. #621 is an independent main-based arithmetic observer application.
- #623→#624→#625→#626→#627→#628→#629→#630→#631→#632 is a common stack. Its two descendants fork into #633→#635→#637→#639→#641→#643 and #634→#636→#638→#640→#642→#644. The two maximal heads retain all ancestors; corresponding inherited statements are not independent proofs.
- #655 is an independent main-based, two-file compiled-probe note and exact finite control.

## Proof-bearing findings

1. **Source and observer remain different types.** `research/2026-11-14/probe_budget/THEOREMS.md` PB-01–08 distinguishes static nondestructive target identification, adaptive single-copy identification, and equivariant point/stochastic sections. PB-03's fiber constancy criterion is the deterministic action-descent theorem already in the foundations. PB-05's no-lift/stochastic-only/point ladder is consistent; PB-06 correctly demonstrates that refinement can abolish a backward section without destroying stored information. No section is silently promoted to actual source identification.
2. **Lawful posterior rather than invented observation likelihood.** `recursive_observer_fixed_point/THEOREMS.md` RFO-01–07 uses the full joint outcome/next-state kernel, retains original/current coordinates, rejects zero-likelihood conditioning, and prices action costs separately. RFO-05's contraction constant is explicitly conservative and requires a fixed action and valid likelihood factorization. RFO-06's alternating outcome two-cycle decisively rejects the unrestricted fixed-point claim. RFO-07's ascending predictive span stabilizes by n−1 and distinguishes model-relative operational equivalence from physical source identity.
3. **Gauge reduction is target-relative.** `gauge_anchored_source/THEOREMS.md` GA-01–03 correctly requires source-law covariance, an equivariant anchor, an invariant joint readout, and report-fiber compatibility beyond mere gauge equivariance. The posterior quotient identity needs positive evidence probability and no invariant-prior assumption. `seed_source_rank/POINTED_ZERO_THEOREM.md` PZ-01's pointed-orbit induction is valid only for the same fixed successor. The paired source-representation gauge in `SEED_ADMISSIBILITY_THEOREMS.md` remains a different object. The latter note correctly retains both the coherent wrong seed as a control for overbroad hypotheses and finite rational shadow controls against seed-uniform finite onset.
4. **Physical analogies are scoped.** `observational_gr/DERIVATION.md` and `operational_gr_source_action/RESEARCH.md` explicitly require Lorentz, scale, matter/action, and thermodynamic premises; observer agreement is not promoted to physical Einstein dynamics. Their finite tensor tomography and nine-null-direction rigidity are elementary conditional algebra. `haar_gamma_entanglement/THEOREMS.md` explicitly distinguishes conditional steering, joint-state disturbance, unconditioned no-signalling, and an actual additional coupling. The original arithmetic carrier is not assigned a quantum state by analogy.
5. **Nonlinear observation order remains paid.** The two Gamma branches retain signed/complex phases, positive Oily source laws, and conditional source coordinates as different objects. `gamma_volume/THEOREMS.md` GV-06 gives the exact shared-source composition defect `Π Sα (I−JΠ) Sβ J`; independently redrawn coordinates have a different joint law. GV-09–11's descent/alias assertions do not claim that a Gamma averaged expectation reconstructs the next event. The order-six cycle is a genuine scope guard.
6. **Detectors are equivalent instruments.** `interferometer_atlas/THEOREMS.md` ATLAS-01 and ATLAS-03 have valid full-support/dominated-convergence proofs of equivalence to normality. ATLAS-02 pays the full infinite frequency mixture with finite first moment 8/3 and the authentic Green-tail bound, giving `|Cπ_B−CU_B|≤7/(12B²)`. This transports an estimate if supplied; it does not supply decay. The claims table explicitly records R0, source-selected signed decay, π normality and RH OPEN. The physical phase-oracle readout is declared rather than assumed to be an available arithmetic instrument.
7. **Compiled knowledge is conditional accounting.** #655 CKP-01–04 preserves discovery/compilation/storage/application and source-validity costs. Its `2^n−1` equality-oracle lower bound is a standard exact adversary argument; cached bit-model equality remains O(n). Conditional probe entropy zero is correctly distinguished from independence or zero execution cost. No P=NP promotion is made.
8. **Independent arithmetic extension.** #621 `RESEARCH.md` separates the Bagchi/Nyman–Beurling classical input, finite-prefix interpolation, a genuinely open norm-bound criterion, and exact rational infinite-tail certificates. Its Möbius prefix proof and bounded-prefix-to-density argument are internally consistent. Neither archive nor source coefficients should be rewritten. The external Bagchi theorem was not independently reverified against primary literature in this bounded audit.

## Required repairs and authority limits

No new mathematical contradiction was found in the examined foundations contracts. This is a bounded audit, not certification of every line in all inherited research notes. Preserve the independently developed #619/#620 manuscripts, their errata, and #622's cross-examination; do not unify similarly named observer types by name alone. Merge catalog additions by claim identity, preserve separate source/operator types, and regenerate the canonical catalog/relation graph on the final combined tree. Historical receipt success applies only to its recorded head. These focused replays do not validate the final integration tree.

The #632 source-gauge caveat is load-bearing: pointed fixed-source rigidity must never be used to infer rigidity under an explicitly compensated source change. The #648/#651 gauge conflict belongs to the separate source audit; this report does not discharge it.

## New composite deduction: a quantitative observer/Gamma transport interface

**Status:** PROVED PAPER by the derivation below; a classical composite deduction from inherited signed defect telescoping and GV-04/GV-05. No academic-priority or π-frontier estimate claim.

Let V,W be complex Banach spaces, K:V→V and B:W→W bounded contractions, and P:V→W bounded. Put D=PK−BP. For every real α≥0 define Fα(A)=(2I−A)^−α through the norm-convergent positive Gamma/negative-binomial series of GV-04. Then

`||P Fα(K) − Fα(B) P|| ≤ α ||D||`.

For α=0 this is zero. For α>0, at each integer n,

`P K^n − B^n P = Σ_{j=0}^{n−1} B^(n−1−j) D K^j`.

This is an exact signed identity proved by telescoping; hence its norm is at most n||D||. GV-04's coefficients w_n^(α) are nonnegative with total mass one and mean α (differentiate `(2−z)^−α` at z=1). Norm convergence and summation give the bound. This proof neither replaces D by a positive source marginal nor discards the phase of an individual term.

For the authentic retained two-loop law of GV-05, `u=x−x²/2`, `v=x²/2`, `a=(1−u)(1−v)`, and `Qx,α(A)=a^α(I−uA)^−α(I−vA)^−α`, the same argument gives

`||P Qx,α(K) − Qx,α(B)P|| ≤ α[u/(1−u)+v/(1−v)] ||D|| ≤ 2α||D||`.

Both factors and the source coordinate are retained. At x=1 the operator is F_(2α), so the factor two is necessary. The universal coefficients α and 2α are optimal: use scalar K=1, B=1−ε, P=1, ε↓0, where `[1−(1+ε)^−α]/ε→α`, respectively replace α by 2α. This is ordinary differentiation of a declared scalar function, independent of numerical tests.

**Hostile boundaries.** Contraction cannot be dropped: α=1, K=19/10, B=9/5, P=1 gives left side 5 versus proposed ||D||=1/10. Retained x cannot be integrated out before composing without paying GV-06's defect. This is an upper error bound, not an anti-lock lower bound, not a statement that small averaged Gamma defect implies small one-step defect, and not a proof of any decay for the actual BBP winding. The order-six alias already refutes the naive converse. Any eventual application to a physical observer must separately authenticate K,B,P and costs.

## Executed focused replays

- At immutable #644: fourteen focused unittest files, **306 tests passed**, exit 0 for each; raw commands/output in `foundations_tests.json`.
- At immutable #643: fourteen focused unittest files, **258 tests passed**, exit 0 for each; raw commands/output in `foundations_alt_tests.json`.
- #621 extracted exact subtree: `python -m unittest discover -p 'test_*.py'`, **14 tests passed**, exit 0, recorded in `foundations_extract_tests.json`.
- #655 extracted exact subtree: `python exact_probe.py`, exit 0: 510 finite sources; 87,380 cached queries; 8 unresolved rival pairs; 510 stale-source mismatches; worst 8-bit discovery count 255. These are finite controls, not asymptotic complexity measurements.
- Fresh exact Fraction checks of the composite Gamma bound: 648 scalar contraction instances for integer shapes 1–8, 21 original source coordinates (669 total checks), twelve exact endpoint sharpness ratios, and the noncontraction mutant. Receipt `foundations_gamma_transport_checks.json`. The universal theorem rests on the proof, not these checks.

The full combined mandatory gates, generated artifact checks, Lean authority and hosted CI remain the integration owner's final-tree obligations. No earlier receipt or this audit substitutes for them.
