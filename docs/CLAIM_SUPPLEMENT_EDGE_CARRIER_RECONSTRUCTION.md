# Claim supplement: source-indexed categorical edge/carrier equivalence ladder

**Date:** 2026-10-15. **Branch:** research/edge-carrier-reconstruction-2026-10-15, stacked on research/rh-carrier-tate-functor-2026-10-15@e1cfae4fba4632e1e936d57943263e470467d27b.
**Dossier:** [EDGE_CARRIER_RECONSTRUCTION_LAB.md](../research/2026-10-15/EDGE_CARRIER_RECONSTRUCTION_LAB.md).
**RH PROVED: NO.** Classical reconstructions have named mathematical provenance; finite tests certify only their exact coded examples.

| ID | Result / required maps | Status | Verification and negative boundary |
| --- | --- | --- | --- |
| EC-01 | Invert one generator in the free one-object successor-loop category B(N) to obtain B(Z), with Aut(*)~Z and universal extension to group targets | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | IntegerLoop raw equivalence, group law and torsor, finite cyclic universal map; a **ray** groupoid has trivial based isotropy, and B(N) itself is not equivalent to B(Z) |
| EC-02 | Ring localization of the completed Z at all nonzero integers yields Q, preserving +,* and inverse laws; finite S localization yields Z[S^-1] | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | RationalSpan vs independent Fraction oracle, forbidden denominators; localization of Z/6 at 2 kills nonzero 3 |
| EC-03 | Ring presentation Z[X]/(X²+1) ~ Z[i] with exact norm, conjugation; fraction field Q(i) | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | GaussianInteger/GaussianRational ring laws, wrong coordinatewise multiplication and noncanonical representatives rejected; Q(i) is not all C |
| EC-04 | Completion of dense Q(i) in ordinary complex norm is C; exact Cauchy name for sqrt(2)+i*r has modulus 10^-n | CLASSICAL / PROVED PAPER + EXACT SPECIMEN | GaussianCauchyRoot2 rational enclosure, parity irrationality proof; no claim every C point has finite computable name |
| EC-05 | The complete compatible modular residue system lim_(n|m) Z/nZ is Zhat; CRT gives Zhat~prod_p Zp as topological rings | CLASSICAL / PROVED PAPER + FINITE EXACT CRT | All finite idempotent e_p, orthogonal partition of unity, source-compatible quotient ring laws; source Z embeds densely but PROPERLY (nontrivial idempotent) |
| EC-06 | Finite adele ring Af(Q)~Zhat[(Z\\{0})^-1]~Q tensor_Z Zhat; complete adeles A_Q=R x Af(Q) | CLASSICAL / PROVED PAPER / FINITE-RATIONAL/PROFINITE PRESENTATIONS TESTED | FiniteAdeleSpan and local scaled p-adic residues; diagonal Q proper, nontrivial idempotent zero divisors; rational real chart is not full R |
| EC-07 | Yoneda full faithfulness identifies a category's arrows with natural transformations of representables; in B(Z/m), exactly m equivariant self-maps | CLASSICAL / FINITE COMPLETE EXHAUSTION | All m^m endomaps enumerated for m<=6; arbitrary map x↦2x rejected for m=5 |
| EC-08 | Full actual SUCC source histories to reconstructed carriers retain every original physical event and source law | UNVERIFIED GENERALIZATION | Models record DECLARED source/epoch; no physical attestation, no universal proof of arbitrary event functors |
| EC-09 | Full Weil functional is transported by those carrier-equivalent interfaces to a source-derived PSD realization and RH | UNVERIFIED RH-HARD | No completed signed Weil sign theorem; categorical equivalences do not create positivity |
| EC-10 | Merely matching cardinality, finite sample outcomes, or a directed ray's path count gives an isomorphism to a larger carrier | REFUTED AS GENERAL INFERENCE | Explicit ray, noncancellative, non-domain, finite-clock and missing-topology countermodels |

## Typed status

- **Algebraic isomorphism:** B(N)[s^-1] ~ B(Z); localization Z[(Z\\0)^-1] ~ Q; Z[X]/(X²+1) ~ Z[i].
- **Complete topological isomorphism:** completion(Q(i)) ~ C; lim Z/n ~ Zhat ~ product Zp; localization(Zhat) ~ Af.
- **Proper embeddings (NOT isomorphisms of the uncompleted sources):** N→Z; Z→Q; Z→Zhat; Q→Af; Q(i)→C.
- **Only finite executable source fragments:** exact loop words, rationals, Gaussian rationals, rational Cauchy names, finite-recipe profinite and finite-adele points.
- **Source-map/physical authorization:** DECLARED MATHEMATICAL MODEL only, not empirical certification.

## Reproduction

    python -m unittest discover -s tests -p 'test_edge_carrier_reconstruction.py' -v
    python -m unittest discover -s tests -p 'test_finite_adele_localization.py' -v
    python -m unittest discover -s tests -p 'test_complex_cauchy_edge.py' -v
    python scripts/edge_carrier_reconstruction_probe.py
    python scripts/verify_provenance.py

Reference provenance and next known solved-problem tests are in the main dossier. No claim of a new RH proof or of original academic priority.
