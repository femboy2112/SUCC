# Complementary review of the moving-frequency proof

Reviewer: diophantine agent, same model and inherited context. This is a
complementary mathematical check, not blind or external proof authority.
Reviewed file: `../MOVING_FREQUENCY.md`.
SHA256: `de443a42a2e5f21423cc9525688c62a03eeaa6568dfd5ab9e04865aec5d69267`.

I reconstructed MF-01's lower and upper integrals, MF-02's unit-phase
alignment argument, both threshold constants, and MF-03b's exact finite
summation-by-parts identity. No defect was found in the stated scopes.

- MF-02 correctly uses one unit alignment zeta of the selected sum. The
  source edge q=z_next conjugate(z)^16 has target zeta^(-15). The Euclidean
  triangle factor is 17, so the squared factor is 289. The endpoint-count
  convention has M edges and M+1 vertices.
- The early/late-quarter lower phase gap is exactly 9/245; the upper gap
  is below 15/64, so the chord lower bound stays in its valid half-circle.
- In MF-03b the boundary coefficient of the last phase is `1-a_last`.
  This is essential: replacing it by a separate final term would lose the
  displayed constant. Both endpoint norms are controlled by csc(pi lambda),
  and monotonicity controls the total cotangent variation. The resulting
  bound <=1/lambda is valid for 0<lambda<=1/2.
- For BBP, lambda=15|h|/(256A^3), with the upper increment below15/32.
  At |h|>=512A^2/15, the source sum is <=A/2, hence the selected deficit
  is at least A/578 for all seeds.
- The coherent same-forcing seed proves exactly the stated limitations
  below the quadratic sum scale and cubic lag-energy scale. These estimates
  do not distinguish the authentic boundary, and no fixed-frequency
  positive-density claim follows.

This review checks paper implications. I did not duplicate the root's finite
numerical test suite or certify an infinite theorem by sampling.
