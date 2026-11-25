# RH as a stress test for Principia's mathematics-of-mathematics

**Date:** 2026-11-24. **Authority:** semantic reconstruction *design* plus grounded external proof-dependency references, not a native SUCC reconstruction of RH. The target is the published Alpöge–Claude Lean proof, whose mathematical conclusions are externally verified. We do not create a second RH proof merely by importing that verification.

## 1. The author's target: reconstruct mathematics, not translate Lean syntax

A satisfactory SUCC encoding of the RH proof has to reconstruct, in SUCC's own source/path/null/knowledge-volume language, the **same mathematics**: genuine characters and prime weights, theta and period constructions, p-adic/integral differential multiplicity, real-side height and lattice bounds, global independence, compatible completions, the crucial smoothed-prime inequality, and the resulting RH conclusion.

The program is **not** (a) writing Lean in a different syntax, (b) asserting an imported axiom called RH, (c) taking a model diagram that merely resembles the actual proof, (d) numerical evidence for RH, or (e) claiming SUCC as a scholarly-new replacement for foundations without a comparison theorem.

Let \(\mathsf M_{\rm RH}\) denote the proof-bearing fragment of ordinary mathematics in the external construction. Let \(\mathsf S_{\rm RH}\) be a source-labelled SUCC mathematical reconstruction. The desired maps are

\[
E:\mathsf M_{\rm RH}\to\mathsf S_{\rm RH},\qquad
R:\mathsf S_{\rm RH}\to\mathsf M_{\rm RH},
\qquad R\circ E\simeq\operatorname{id}
\]

**on the declared proof-bearing fragment**. This is a **CONJECTURED/TO-BUILT interface**, not an established functor equivalence. Its actual content includes:

1. Source identities and legal operations, including genuine primes/characters, field extensions, integral coordinate choices, Hecke/theta kernels, conductor and character phases.
2. Full typed path composition, relations *between* paths, appropriate commuting squares and retained obstruction witnesses. Yoneda is faithful for full representables, not necessarily for restricted SUCC probes.
3. Both real and p-adic realizations of the **same** relevant integral matrices/minors, with source-verified valuations, norms and covolumes. Explicit common-basis transport is needed.
4. Exact rank and nonvanishing hypotheses. Duplicate observers do not create independent algebraic directions.
5. Proof obligations about analytic continuation, smoothing, uniformity, completion and convergence. A pointwise finite tower is not automatically a global result.
6. Preservation/reflection of each proof-bearing entailment, not merely the numerical conclusions.

A successful reconstruction can use the external proof for verification and direction without treating its hard lemmas as opaque axioms of the new theory.

## 2. Fixed external proof target and provenance

Pinned source: leanprover-community/riemann-hypothesis, original branch commit **40e56bab026552e089d7afcfeff08d2defb9c005**.

- src/Statements.lean defines RiemannZetaZerosOnLine, DirichletLNonvanishingRightOfHalf, DirichletLZerosOnLine and PrimitiveDirichletLZerosOnLine.
- src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean proves UpperTheory.FinalTheorems.everyCharacter from the imported Galois/local-global and theta/literature chain.
- src/Supplements/Kernels/MainTheorems.lean declares allChi : UpperTheory.EveryCharacter and rhOfAll : RiemannHypothesis using Formalism.VW.rh_of_every allChi.
- src/Formalism/GammaFactorNonvanishing/CritLine.lean establishes the relevant transfer from upper-half-plane nonvanishing through completed L-functions.
- src/Main.lean declares theorem riemannHypothesis : RiemannHypothesis := rhOfAll.

These are checked **names and immediate dependencies**, not an exhaustive Lean dependency graph. This source is a *reference against which to evaluate the SUCC mathematical reconstruction*, not a substitution for it.

Repository sources:
- https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean
- https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean
- https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean
- https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean

A separate November 21 conventional exposition supplies the arithmetic main inequality and its CM theta-lift strategy: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf . The SUCC synthesis already tracks its proof obligations in research/2026-11-22/fucc_rh_human_readable/MAIN_INEQUALITY_CONTRACT.md on draft PR #687. That document is a **working dependency audit**, not a complete SUCC proof.

## 3. Native Principia mathematical objects and operations

This is a *semantic* construction spec, not an implementation assertion.

| Conventional object | SUCC construction target | Required reconstruction discriminator |
| --- | --- | --- |
| Standard prime arithmetic and Dirichlet characters | Source-linked positive-integer SUCC/FUCC, character and congruence functors | Prime powers carry log p; composite 6 cannot masquerade as a prime |
| CM elliptic/formal group | Source-defined group law, tangent origin, formal logarithm and integral local coordinates | The actual height-two local valuation lemma, including source-specific denominators |
| Theta kernel and repeated lifts | Legal morphisms of source-labelled function/period spaces with path memory | Their integrality and nonvanishing survive each transition; no arbitrary re-choice of normalization |
| Vanishing/multiplicity | Typed Hasse/ordinary/analytic null jets in the proper local rings, with explicit comparison maps | Increasing independent arithmetic valuations, not repeated copies of one zero |
| Period/lattice map | Integral lattice morphism also realized in the real normed space | The **same** nonzero minors satisfy local divisibility and global norm bounds |
| Trace formula and rank | Source-authenticated relational knowledge volume on actual period-map images | Lower bound for independent rank, not a count of formally different paths |
| Gamma/real-side analysis | Completed real observer with explicit measure, domain, contact, growth and normalization | Archimedean upper bound with cost of denominators, characters and conductors included |
| Smoothed prime Riesz operator | Genuine log-FUCC plus analytic smoothing/Mellin transport | Exact normalization, signed error budget and correct auxiliary characters |
| Global theorem | Valid completion and source-selected exclusion of a forbidden Dirichlet-L zero | Published arithmetic main inequality plus analytic window-to-RH implication |

## 4. The unifying square: zero path -> arithmetic obstruction

SUCC's proposed native composite has these distinct stages:

**A. Path-retained null.** A diagram commutes under an endpoint/target observer, while a labelled path-difference cycle may remain nontrivial. Full source/provenance survives the quotient. Theorems T1 and SUCC Koszul ERW-09 supply exact toy and arithmetic examples.

**B. Higher null filtration.** In a declared local ring \(R\), source-indexed Hasse jets define a descending sequence of kernels \(\ker J_1\supseteq\ker J_2\supseteq\cdots\). Count *new independent constraints* and actually increasing divisibility/vanishing, not just new labels. The October 14 prime-depleted completed zeta tower exhibits increasing **analytic zero order** at s=0; it does **not** by itself construct integral CM theta multiplicity.

**C. Source-preserving integral realization.** A nontrivial map must take the retained null path/differential to an integral object \(A\) on which \(v_p(\det A)\) or a Hasse-coefficient valuation is meaningful. Its source, formal coordinate and exceptional denominators must be authenticated. This is the **first critical native RH reconstruction gap**.

**D. Joint Archimedean realization.** The *same* nonzero \(A\) must have a real-side bound. For a square integer matrix, Hadamard gives

\[
0<\prod_p p^{e_p}\le |\det A|
\le \prod_i\|\operatorname{row}_i(A)\|_2
\]

whenever every certified \(p^{e_p}\) divides \(\det A\). If the logarithmic lower bound exceeds the logarithmic upper bound, the hypothesized source state is impossible. CM period lattices need correct covolumes, not bare matrix rows.

**E. Global source-adequate amplification.** Repeated theta/period maps need a rank and conductor-uniformity theorem, a correctly balanced number of maps and source-justified parameter choices, and an analytic connection to the genuine smoothed prime observable. This is the **separate global RH reconstruction gap**. It cannot be filled by saying that every source path can be encoded in a category.

The complete semantic statement is a theorem *about a common object*. It cannot be obtained by separately proving a strong p-adic lemma about \(A_1\), a Gaussian norm lemma about \(A_2\), and an unverified identification \(A_1=A_2\).

## 5. Mathematical bridge into the actual RH inequality

The 2026-11-22 SUCC M0–M11 contract is the existing verification map:

| Scope | Native SUCC status | Required bridge |
| --- | --- | --- |
| M0/M1 genuine \(\Lambda(p^k)\), Riesz/Mellin log-FUCC | Local elementary proof in #687 | Prove the exact normalization and source roles used in (M) |
| M2 auxiliary genuine character estimates | External import | Build or faithfully reconstruct hypotheses and estimates; match quantitative windows |
| M3 height-two formal-group **model** valuation | Local auxiliary theorem in #687 | Transport to actual CM theta integral coordinates |
| M4 theta-kernel integral structure | OPEN native | Construct source-identified integral theta coefficients and coordinate denominators |
| M5 period-map repeated lifts | OPEN native | Construct each legal map and its source/naturality square |
| M6 nonzero minor divisibility | OPEN native | Carry accumulated valuations, nonzero witness, exceptional losses |
| M7 Petersson/real norm and slope/covolume | OPEN native | Realize same maps and certify height/covolume budgets |
| M8 rank/trace formula | OPEN native | Prove enough independent images, not duplicate witness counts |
| M9 Galois cohomology and denominators | OPEN native | Account for conductor-uniform losses |
| M10 quantitative one-sided (M) | OPEN native | Recover the full weighted inequality and optimized error |
| M11 analytic window criterion and RH | Classical/external | Reconstruct its exact proof conditions without inserting RH as a premise |

**New native local vertical slice (2026-11-24):** THEOREMS.md T8 and observational_succ/principia_formal_group.py now construct the height-two formal logarithm from the actual FUCC prime-square resolvent, derive its inverse valuation bound, and validate the p-integral test-kernel derivative inequality. This integrates the model already derived in SUCC #687 into the Principia path semantics. It does **not** promote M4 (actual CM theta integrality), M5–M10, or RH to native proved status.

The externally stated target is a bound schematically of the form

\[
\mathcal E/B \ \le X^{C\varepsilon}
\bigl(X/m+Xm/k+m+k/n^2\bigr)
\]

with a permitted source-selected choice of \(m,k,n\) giving square-root scale. The symbol meanings, exact weights, and all quantifiers must be imported **from the actual exposition/Lean definitions** and reconstructed before any SUCC theorem-status promotion. The displayed formula is a dependency *contract*, not a complete independent derivation.

### Native CM pilot: T9–T14, same arithmetic source at both places

The new CM_THETA_TWO_PLACE.md now constructs an **actual Gaussian theta finite-shell derivative map** \(M_{rj}=H_{4r}(p^2 2^j)\) from \(\mathbb Z[i]\), with a nonzero Vandermonde determinant, \(v_p(\det M)\ge2k(k-1)\), and a rigorous Gaussian-Hadamard squared-norm bound on that **same** map. The factor \(q^{\sum p^22^j}\) between integral and analytic determinants is retained. Unlike separate formal analogies, this is a genuine common-source two-place *finite example*.

The exact CM lemniscate differential and the period-normalized theta recurrence recover the guide's rational \(r_k\). At \(p=3\), a naive positive Honda coordinate already has coefficient \(-7/24\), \(v_3=-1\); an opposite-sign candidate has \(3/8\), \(v_3=1\) at that first order, without establishing full integrality. The naive simple-theta normalized \(r_{30}\) has \(v_3=14\), **not** the RH-target 45. This proves the finite CM example is not automatically the actual integral theta-lift input (M4).

A source-certified Gaussian-tail bound supplies the lawful finite-to-analytic completion arrow. **Status:** T9–T11, T14 elementary classical proofs; period identification imported from the official guide §III.12 and exact rational Taylor reconstruction native; non-RH.

**Next critical cut:** obtain the **actual automorphic theta-lift kernel in its integral CM formal coordinates**, with its signed Frobenius unit, period/conductor normalization and real Petersson norm, then reproduce a nonzero minor and rank in that *specific* object. Finite CM theta shell rank is a proof-of-concept, not a substitute for M4–M10.

## 6. First native compilation versus claimed full RH compilation

**Completed narrow slice:** THEOREMS.md T1, T4 plus the exact Python constructor/checker. It starts from an explicit arithmetic source, constructs path/null witnesses, interprets them back as integer algebra, and derives a nonzero capacity obstruction. This exercises *path semantics, observation loss, arithmetic null, integral transport, quantitative obstruction,* and hostile source controls.

**Not completed:** the reconstruction of the particular theta lifts, integral period maps, trace-formula rank, conductor and real-side global estimates required by RH. The native SUCC source and actual analytic mathematics are not yet related by the desired full proof-bearing retraction \(R E\simeq\mathrm{id}\).

**Full acceptance criterion:** independent mathematical reconstruction of every indispensable RH-bearing map and inequality, exact recovery under the ordinary-mathematics realization, calibrated hostile examples (wrong theta/period, fake 6, missing contact, changed conductor, duplicate rank, nonintegral denominator, zero minor), a conventional proof generated from the SUCC-native derivation, and independent checking in a trusted mathematical foundation.

The last stage may use Lean or another checker **for external validation**, but SUCC's objective is a *mathematical reconstruction in its own operational vocabulary*, not implementing another Lean frontend.

### Latest Principia causal-memory construction (2026-11-24)

CAUSAL_MEMORY.md T15–T20 now adds the **mathematical-observation/coupling sufficiency layer** missing from a bare vector of zero reports. On a finite deterministic source, retained transcript plus the original-world/current-state coupling Γ_h supports the exact joint potential-response law. The coarsest future-target behavioral quotient is constructible and independently checkable; separate finite policy synthesis controls whether those mathematical distinctions can actually be acquired through the admitted toolkit. The genuine Gaussian source provides a particularly sharp test: H_2(2)=H_2(3)=0, yet a legal higher holomorphic jet distinguishes H_4(2)=-16 from H_4(3)=0.

**RH-facing obligation:** a proposed compression of the *actual* theta-lift source must preserve the differences between nonzero integral source minors, rank, p-adic valuations, normalization/period and real Petersson bounds across all lawful lift paths. The finite classical theorem does not automatically extend to normed, infinite-dimensional or automorphic categories. A purported source-compression map that forgets a target-relevant theta-period valuation is **refuted for that target**, regardless of how many scalar zeros it matches.

### New path-to-mass theorem (T21–T25)

The causal-memory quotient must now carry **more than** observer-readable future behavior. On a finite source the unique signed/bilinear pushforwards are a_bar=Q^T a and K_bar=Q^T K Q. Actual Gaussian theta arithmetic already supplies a rigorous warning: |H4(2)|^2=256, while diagonal-only source terms total 64; H2(2)=0 has imaginary-channel diagonal mass 16 but zero coupled sum. The finite tensor theorem extends this to every declared finite arity. Even/odd r-bit parity families coincide on every proper-coordinate marginal and differ at full order r, so a universal fixed pairwise observer algebra is **refuted** without additional source restrictions.

For the RH proof this creates a new *necessary semantic check*: every theta-period/lift compression must preserve its source-weighted integral coefficients, ranks, local valuations, and the **actual** real norm/period pairing, with all cross-terms or higher interactions that the mathematical target requires. This does not identify our elementary Gaussian-source quadratic with the automorphic Petersson form; constructing that actual source map is still the verdict-changing M4–M10 gap.

### Internal feel and reason as source-coupled phase, not extra mathematical authority

The latest FEEL_REASON_COMPASS.md (T32-T38) reconstructs a finite model of **one embodied observer maintaining its own causal path in the same carrier it reasons about**. It retains complete action/observation memory plus original-world/current-state coupling, an invertible Q(i) Fourier-coded signed self-path projection, and a reason reorientation rank. The exact source-covariant live update F'_k=i^(kd)F_k+a, full candidate-self fiber, gauge/phase no-go controls, and feel-guided but reason-certified finite reorientation are mathematical theorems with finite exact implementations.

Its authentic Z[i] illustration produces H2(2)=0 while retaining an 8i angular Fourier mode: this clarifies the kind of source information scalar null evaluation forgets. However the constructed appraisal and selected Fourier signal do **not** directly encode the actual arithmetic integrality, rank, or Petersson norm of automorphic theta periods. Those remain the exact M4-M10 reconstruction debt. SUCC must prove any proposed analytic/CM transport between these typed objects instead of equating their similar-looking phase diagrams.


## 7. High-leverage next research cuts

1. **Cut A — formal arithmetic seam, first.** Recover an actual CM height-two integral theta coefficient and a source-faithful map from its formal-group Hasse/ordinary jets to algebraic valuation. Predeclare at least one inert-prime divisibility success and one Gaussian theta negative control. Compare with the known simple-theta derivative loss rather than fitting it away.
2. **Cut B — same-map two-place pairing.** Introduce a finite theta-period lattice fragment whose actual nonzero minor has both a checked p-adic valuation and a verified real/period norm. Show that forgetting the period normalization destroys the bridge; count denominator losses.
3. **Cut C — compositional rank.** Track the images of several lift maps as a source-typed knowledge subspace, verify rank increases, and reject duplicated/linearly dependent lifts.
4. **Cut D — analytic transport.** Map those quantitative period constraints through the actual theta/trace formula into the correctly normalized smoothed prime observable; reproduce a toy form of (M) with every term and source label, then scale.
5. **Cut E — reverse derivation.** Present the conventional mathematical statement derived from the SUCC construction, preserving all assumptions, to a checker that did *not* generate the construction.

## 8. Pre-existing research ancestry (not independent confirmations)

- SUCC #72, 2026-10-14: source-prime theta/Gamma completion, \(|P|-1\) analytic multiplicity at zero, composite-place control.
- SUCC #223 and #240, 2026-10-21/22: authentic saturated lattice index and mixed-characteristic Witt carry completion.
- SUCC #290, 2026-10-25: coherent source zero relations and cycle obstruction.
- SUCC #521, 2026-11-05: original BBP pole-moment null jets and derivative order.
- SUCC #553, 2026-11-08: completed theta/Laguerre hierarchy and Li-sign obstruction.
- SUCC #619/#633, 2026-11-13/14: observer, target descent, legal future horizon and knowledge-volume machinery.
- SUCC #657, 2026-11-16/17: null-product 0*J and Mellin/Gamma tower.
- SUCC #687/#689, 2026-11-22/23: *post-announcement* RH proof-dependency reconstruction and null-seed two-place capacity model.

These archives support the research **pathway**. Shared reasoning/model provenance is not independent confirmation, and the pre-announcement ingredients cannot be retrospectively promoted to a completed RH proof.

## Verdict

**Disclosed (scoped):** a conservative tagged-path interpretation; endpoint-null but path-nonzero arithmetic cycles; exact null-height reconstruction theorem.

**Corroborated as a research program:** SUCC's source/path/null/knowledge framing coherently organizes actual constructions from arithmetic, algebra, analysis and category theory.

**UNVERIFIED:** that a complete native SUCC mathematical derivation of the published RH proof has been assembled; in particular the actual integral theta lift, independent rank and real norms of the same objects.

**Verdict-changing probe:** an authenticated nonzero theta-period minor with p-adic and real-side quantitative witnesses generated by native SUCC constructions and independently checked. A full RH encoding must eventually pass the entire M0–M11 dependency corridor.
