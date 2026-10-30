# Complementary review of same-period positive source fibers

Reviewed `../period_preserving/PERIOD_FIBERS.md`, SHA256
`a167fc98484ac2f7e07ed67b0c5d55f4c71425710c56ee13ac0fc8a2f327f688`.
Reviewer is the constants-front agent, sharing the parent model and repository;
this is not external independent refereeing.

**Verdict:** PF01–PF03 survive the stated paper review. No substantive defect
was found. The restricted completeness statement is correctly limited to
D=(16−z^8)P, not all possible BBP null relations.

- The period telescopes because R(0)=R(1)=0; the chronological forcing
  coboundary has the correct sign, and the orbit difference is −epsilon I_n.
- The orthogonal weight z^8(1−z)^(m+1) makes the first N moments vanish with
  the stated n−1 indexing. The first surviving moment is the positive monic
  polynomial squared norm, not an empirical sign fit.
- Q=(1−z)(4+4z+4z²+2z³+z^4) gives the global4B relative bound; epsilon=1/(8B)
  ensures positivity without a sampled grid.
- The Beta tail bound has exactly m+1 powers after multiplying by8n. Its
  summability justifies bounded fixed-frequency Weyl differences, rather than
  a claim that the changed source must fail normality.

A separate small closed-form probe does not import the producer: N=0,m=13
and N=1,m=11 use the explicit Beta mean for p_1. It verifies32 exact orbit
identities, prefix zeros, the first positive unmatched orbit, and the proposed
tail bound. `period_review_receipt.json` and `receipts/period-review.*` preserve
the raw result and command metadata. This finite check supplements the proof;
it does not prove PF02 for arbitrary N by itself.

The controls keep the same selected pi period. Calling them nonnormal would
be false: their normality is exactly the same open question as the original.
The dossier states this boundary correctly.
