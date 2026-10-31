# Complementary review of SG-02 through SG-04

Reviewer: the `gamma_gauss` sibling, same model family and shared campaign
context. This is a complementary derivation audit, not blind external proof
authority. Reviewed file hashes and an independent symbolic leading-term
calculation are in [signed_review_receipt.json](signed_review_receipt.json).

**Verdict: no blocking mathematical issue found in the reviewed versions.**

- **SG-02:** the full complex recurrence gives the stated chord inequality.
  The two truncated Euclidean norms are each bounded by the full energy
  norm, giving 17 before squaring and 289 afterwards. No independence or
  primary-only bound is substituted. The result permits every real seed.
- **SG-03, existence and all minimizers:** the initial lag phase is a
  surjective affine function of the real seed with nonzero coefficient
  `15 h 16^A`. All later phases are continuous integer-power functions of
  this circle coordinate; compactness supplies a minimum. Its energy is
  at most the coherent-seed M. Every centered minimizing lift therefore
  has absolute value at most sqrt(M/8). The strict first condition gives
  `17 sqrt(M/8)<1/2`; the strict source condition supplies the other
  `<1/2`. The integer unwrapping defect is strictly less than one in
  absolute value and must vanish at every adjacent pair of every
  minimizer. Equality cases at one are correctly excluded.
- The exact Green difference obeys the same inhomogeneous recurrence,
  so the entire minimizing vector differs by one homogeneous mode
  `a_j tau`. Orthogonal projection gives Q exactly. The centered Taylor
  lower bound has the stated factor `1-pi^2 M/24`. For the upper bound
  the quadratic-minimizing lifts need not be centered: every real tau
  still gives a valid seed, and the global inequality
  `1-cos(2*pi*u)<=2*pi^2*u^2` remains valid. Thus this is an all-minimizer
  result, not an assumption that a convenient local stationary point is
  globally minimal.
- **SG-04:** independent rational expansion gives leading source
  `15/(64n^2)` and decrement `15/(32n^3)`. Multiplication by the geometric
  resolvent mass `1/15` gives `D_n~1/(32n^3)`, hence the constant
  `pi^2 h^2/512` in the mean-square floor. For L→infinity, L<=CA,
  the projection removes at most a constant multiple of D_A^2, while
  the full square norm is at least L D_(A+L-1)^2. Their ratio tends
  to zero uniformly in that stated regime. The fixed coherent seed
  attains the same asymptotic, so this is a sharp source-only obstruction.

The exact zero seed has not been shown to stay above this floor by a
constant amount. SG-04 must not be reported as progress on SC-06's
selected positive-constant lower bound. The dossier currently preserves
that distinction. The order bound `(p-1)/4` in its SC-06 paragraph uses
the inherited SC-06 restriction `p=1 mod4`; other prime classes have
different but still comparable window scales.
