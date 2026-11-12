# Final targeted audit: coherent center and hostile-source scope

Date: 2026-11-12. Read-only, same-model audit. No repository edits. This closes the two remaining focused observations from the previous runtime audit; no broad test suite was repeated.

## Verdict: PASS within the declared finite source class

The final runtime patch implements the known shared-center bit correctly. THEOREMS.md §7 PFO-11/PFO-12 accurately separates independently assignable two-sided masks from a coherent single integer indicator. The countermodel is not claimed to satisfy authentic multiplication/primality. §8's transported-multiplication example and repaired scope are correct.

## Runtime verification

`crt_haar_certificate` now marks whether displacement zero belongs to a cell, retains its actual bit c=1_P(n), and computes

`coherent_lower = c + max(0, A+B-2c-(D-center_present))`.

When the center is absent, center_present=0 and c=0, recovering the old bound. When present, this is exactly the proposed one-source correction. The total is the sum of cell bounds.

`minimum_overlap_model(..., preserve_center=True)` restores c in the first slot of the center-containing cell and assigns the remaining A-c and B-c bits in opposite orders across D-1 positions. This preserves both marginals, the shared center, and attains the corrected lower bound. Admissible displacements are listed increasingly, so when present the center is indeed the first slot.

For positive displacement, plus-side labels are strictly above n and minus-side labels strictly below n; each side is injective, and disjoint cells have disjoint displacements. Thus there are no additional shared-integer constraints. Arbitrary off-center assignments extend to one global binary indicator. No assertion that this indicator arises from ordinary prime factorization follows.

## Targeted executions

Executed three relevant test methods:

- `test_shared_center_strengthens_the_relaxed_bound`;
- `test_crt_bounds_refinement_and_sharp_counterfeit`;
- `test_prior_coarse_observer_counterfeit`.

All passed.

Independently enumerated every feasible pair of masks for one center-containing cell of capacities D=1,…,5, both c=0 and c=1, and every feasible pair of marginals. **110 center-cell configurations passed**. For each configuration, brute-force minimum equals the corrected lower bound; brute-force maximum equals min(A,B); the runtime's constructed model preserves the exact center and both marginals and attains the minimum.

The n=9,z=2,width=4 correction is verified; the n=1024,z=2,width=128 zero-overlap hostile control remains valid because its center is excluded.

## Theorem audit

PFO-11: the ordinary Fréchet bounds, monotonicity under refinement, and sharpness for independently assignable masks are correct. The text explicitly restricts the upper bound to the screened interior and disclaims probabilistic independence.

PFO-12: removal/restoration of the known center proves the displayed lower bound. The unchanged upper bound follows from `c+min(A-c,B-c)=min(A,B)`. Both bounds are sharp in the declared single-indicator class.

PFO-13: the finite involution's transported prime set in [2,98] is exactly `{2} ∪ {3,5,…,49}`. It has no ordinary-addition pair summing to100, although the true prime set has12 ordered witnesses. The displayed braid failure `V'_2 S(8)=106` versus `S² V'_2(8)=18` and restoration under transported addition are correct.

## Final wording correction verified

The earlier statement that finite relabeling preserves 'every eventual statistic' was overbroad. A concrete falsifier is the weighted prime-prefix sum: swapping the ten listed primes for the ten composites changes that sum by **−434 for every cutoff at least97**.

Root replaced the passage with the precise statement that prime indicators agree for every n>97, tail-supported observations agree, limiting densities are unchanged, and weighted prefixes/additive correlations involving changed small labels need not agree. I reopened the updated passage and verified the repair.

## Boundary

This is an elementary proof audit with finite execution checks, not external peer review or a formal kernel run. The evidence supports the specified constructions and finite certificate repair; it supplies no universal Goldbach estimate.
