# Coupled Wilson claim ledger

All statements have the hypotheses in their linked proof. Paper derivations,
exact finite executions, and external assessed theorems have distinct authority.
No worldwide novelty or independent-model verification is claimed.

| ID | Statement / quantifiers | Status and authority | Hostile boundary / next probe |
|---|---|---|---|
| CW-01 | Every fixed finite SU(2) graph, closed word list, nonnegative rational coupling list, rational polynomial and positive rational tolerance admits the terminating exact expectation certificate | PROVED LOCAL, [construction](CONSTRUCTION.md); classical ingredients; executable rational adapter | Large expansions may be expensive; no uniform cutoff estimate. Test against an independent character contraction |
| CW-02 | Every nonnegative coupling and finite even degree gives a strictly positive, character-positive plaquette factor | PROVED LOCAL, [character proof](CONSTRUCTION.md); exact coefficient controls | Negative coupling or odd degree does not receive both certificates |
| RO-01 | Every nonconstant nonnegative polynomial Q(x+y) on two reflected SU(2) scalar holonomies fails RP on the full half-polynomial algebra | PROVED LOCAL negative result, [orthogonality proof](REFLECTION_ORDER.md) | The moving test has increasing norm; fixed-test convergence is not refuted |
| RO-02 | The factorwise normalized approximation has error at most 2M 3^ceil(2S) sum beta_p^(Kp+1)/(Kp+1)! | PROVED LOCAL, [telescoping proof](REFLECTION_ORDER.md) | Preserve shared edges and bound the actual observable; volume and norm growth remain |
| RO-03 | The explicitly stated independent-half/fixed-boundary reflected factorization is RP, including shared half-links | PROVED LOCAL specialization of classical character positivity | A new lattice must exhibit the split; gauge or CP invariance alone is insufficient |
| RO-04 | Under that split the OS Hilbert quotient has dimension at most product_p sum_(j<=Kp)(j+1)^2 | PROVED LOCAL, finite feature map and null-space identification | Moving continuous boundary or unproved time-translation maps cannot inherit this finite-rank/dynamics claim |
| TO-01 | For every finite tuple of SU(2) holonomies, equality of single/pair/ordered-triple traces is equivalent to common conjugacy | CLASSICAL, [elementary proof and primary attribution](TRACE_OBSERVER.md); exact new adapter | Configuration completeness requires the full joint pushforward law to reconstruct a source measure |
| TO-02 | Pair traces cannot distinguish (i,j,k) from (i,j,-k); triple traces do | PROVED LOCAL counterexample | This necessity occurs at rank three, not every tuple |
| TO-04 | If epsilon<=s²/18 and 13epsilon<abs(det A), a common gauge aligns all tuple entries within (1+8/s+22/s²)epsilon | DERIVED PAPER BOUND, [full proof](TRACE_OBSERVER.md), second same-family analytic check | Degenerate anchors prevent this Lipschitz estimate; probe source-realized conditioning across cutoffs |
| RP-GAUGE | Positive probability + gauge invariance + reflection invariance implies RP | REFUTED by exact SU(2) and Z2 controls | Retain reflected-square source structure |
| RP-CP | Reflection-equivariant CP coarse maps preserve RP without a support condition | REFUTED by a four-point deterministic map | Positive-half localization is load-bearing |
| LAW-MEAN | Means of a configuration-complete trace bank determine the law | REFUTED by the one-holonomy first/second-moment control | Observe the joint law or the required higher moments |
| FORMAL-LOCAL | The pinned upstream proof-transport generator and the new finite rational negative Gram certificate replay in Lean 4.32 | OBSERVED bounded execution, [receipts and scope](FORMAL_REPLAY.md) | Full upstream endpoint/Comparator replay not performed; analytic Haar identification remains paper-level |
| YM-EXISTENCE | The October 28 release constructs a 4D Wightman theory from Wilson lattice gauge theory in its specified limit sense | EXTERNAL ASSESSED RESULT, [primary scope audit](UPSTREAM_SCOPE.md) | Not an independently reproduced SUCC continuum theorem; preserve common witnesses and domains |
| YM-GAP / PI | This work proves the Yang–Mills mass gap or source-selected BBP cancellation | NOT ESTABLISHED; no such implication claimed | Requires a new uniform spectral / arithmetic signed inequality |

Execution counts and final-commit validation belong in [VALIDATION.md](VALIDATION.md)
and the draft PR's final validation record. Finite passing cases do not prove
the all-input theorems; their displayed derivations do the mathematical work.
