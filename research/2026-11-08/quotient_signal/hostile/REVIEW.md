# Independent crucible review

Baseline `a974db527c19708006b9f6d7f0ca01d08d1e0524`. This is another agent's
paper audit and independent finite/numerical implementation, not an external
referee report. All agents share model and repository provenance.

## Surviving claims, ranked by what they establish

1. **GQ2--4: genuine source-derived gamma calibration.** Reviewed
   `gamma/THEOREMS.md`, SHA256
   `f9993d356f27aaf4fed00f9ac28d7a15560c3b252c8e713321262c6c429de6b2`.
   Independently checked the Green kernel exponent, polynomial coefficients,
   derivative cap22, denominator cap15 and `1-f<=2(1-x)`. The two beta
   integrals give the stated lower/upper tail bounds and strict `7/(512n^3)`
   error. Independently summing the geometric weights gives
   `sum_(n=1)^(m-1)n16^(n-m)=(15m-16+16^(1-m))/225`, recovering
   `C=B/15-16R/225+pi/225`. Every displayed coefficient in C's simplification
   checks. The harmonic error is less than `1/(2N)` by convex trapezoids,
   producing `11/(8N)` and the phase error `11pi|h|/(256N)`. The leading
   expansion also independently gives `T_n=1/(64n²)-7/(512n³)+O(n^-4)`.
   The inherited closed forms for R and B are explicitly attributed rather
   than claimed as a new finding. No correction identified.
2. **QS2: exact observer conditioning constant.** Reviewed
   `quotient/THEOREMS.md`, SHA256
   `b98caac430166c8f4399628b7e4238e4ad749381471ecd03518872736c52bfee`.
   On each occupied cell, the two rank-one projections have squared angle
   sine `1-|E_Ca|²`; their squared difference is that scalar times identity
   on their two-dimensional span. Constant input1 on a maximizing cell
   attains the norm. Orthogonal direct sum across positive-weight cells
   proves the exact maximum and weighted application. The rotated-cell
   lift preserves the phase Lipschitz bound. No correction identified.
3. **QS4: signed scale accounting.** The exact covariance telescope correctly
   keeps every bilinear increment. Earlier increments are measurable at a
   later level, so mixed means vanish. Monotone reconstruction energy is
   separated from the signed, potentially nonmonotone covariance. QC2 gives
   an independent four-point unit-phase failure of sign monotonicity.
4. **Root source probe: finite source comparison.** Reviewed
   `source_probe.py`, SHA256
   `2c9f0d674f425c3aadf39011d369d14641d622d026906a076ac3616dde6cc0bf`.
   Rational labels, rotated nested partitions, shadow residues and exact
   source product factorization respect the stated domains. `M>=p` is a
   sufficient exact local-measurability condition even with rotated cells,
   because distinct p-grid points are at least1/p apart. Repeated local
   values can still carry different complements, so this does not imply
   complement reconstruction. Norm bounds in assertions test consistency
   of enclosing intervals; the universal inequalities are established by
   the paper proofs, not those weak interval-overlap assertions.

## Independent executed evidence

`oracle.py` exhausts every pair of four-point fourth-root-of-unity arrays.
It checks **327,680** exact conditional identities/refinement equations,
plus explicit gauge and signed-increment controls. These are finite instances,
not327,680 unit tests. Its four unittest cases pass. The separate rational
Machin/Taylor instrument encloses **24** coherent/alias continuum calibration
rows, retaining rational endpoints and analytic finite error caps. These
calibrations use no inherited interval engine and no special-function oracle.

`verify_source.py` independently evaluates every scalar reported for all
**120** source/seed/complement/phase/depth/origin cases at A=137 and2203:
**2,760 scalar containment checks pass**, with100 decimal digits and a declared
1e-80 rounding tolerance. It uses exact rational complementary phases and a
separate cell-grouping implementation. This is a numerical cross-check of
the rigorous outward rectangles, not a second rigorous interval proof.
The source history builder and the actual data are shared. Six additional
exact direct modular four-ray checks at fresh source indices pass. Input
hashes, execution script hash, method and dependence are in SOURCE_REVIEW.json.

## Retained failures and limits

- First continuum-oracle serialization exceeded Python's4300-digit integer
  string limit. The fix rounds rational sinc endpoints outward to denominator
  10^50 before reporting; it does not change the theorem or disable a global
  Python limit. Four tests and the full oracle were rerun successfully.
- First standalone source-review invocation lacked the repository import
  path, so `observational_succ` was not found. Added an explicit script-local
  repository path; no dependency/environment installation. The corrected
  source review was rerun successfully.
- A generic universal gamma coefficient for the discarded covariance is
  refuted by QC3/QC4 under their explicit model hypotheses. This is not a
  refutation of the authentic GQ gamma calibration or an unspecified further
  original-zero identity.
- The completion-relative phase q_n is exactly the same at the coherent
  wrong seed. The fixed-zero **unwrapped** reference does authenticate zero,
  while its phase-only version has aliases. This distinction in GQ4 is
  correct and necessary. No inference from the gamma calibration to local
  prime/complement covariance is supplied or accepted.

The strongest next test is an explicit map from the authentic signed
conditional term to the calibrated cumulative Green observable with a
uniform error. It must account for origin-dependent finite parts, distinguish
an epoch average from a cumulative product, and retain the literal zero
boundary. At present that bridge is **OPEN**.

**Pi base-16 normality: OPEN. RH: OPEN.**
