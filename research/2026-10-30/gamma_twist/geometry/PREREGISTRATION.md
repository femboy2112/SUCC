# Geometry front: predictions recorded before the formal probe suite

Parent: PR400 `2b0628f52e9d88993c2e3ffa30b9748adfb781f0`.
Authentic forcing and zero seed remain unchanged. Only this directory is edited.

1. **GEO-01, positive phase-lift rigidity.** For any probability posterior and
   unit observable Z, an exact equality E Z = e(h U_n) forces Z=e(h U_n) almost
   surely. Approximate equality with error epsilon gives E|Z-e(h U_n)|^2<=2epsilon.
   PASS: exact rational 2D-vector identity for all declared finite controls and
   a paper proof. FAIL: a unit-mean/unit-vector example with positive variance.
   A Green-budget approximate lift must have finite total conditional dispersion;
   this is an obstruction to one positive averaging mechanism, not normality.
2. **GEO-02, second source jet of the finite golden root.** Recover the already
   known 1/n term, then derive the 1/n^2 term directly. The positive cubic mutant
   Q+epsilon(1-e^-x)^3 must preserve the first term and change the second. PASS:
   symbolic coefficients agree with an alternate expansion; exact finite root
   enclosures and independent quadrature converge to the predictions. Finite
   agreement is calibration only. A higher fourth-order mutant must still pass
   this second-jet identification, so source uniqueness remains false.
3. **GEO-03, interpolation ambiguity.** Positive smooth Gamma cocycles matching
   every integer value and every integer source derivative can differ at
   fractional times. PASS: explicit periodic perturbation and analytic proof.
   The continuous positive convolution-semigroup condition should uniquely fix
   its interpolation from the time-one law, because Laplace exponents are
   additive. This condition must be separately supplied, not inferred from
   the integer lattice.
4. **GEO-04, genuine order defect but seed blindness.** Two original affine
   updates at different source times have a nonzero translation commutator,
   15(r(j)-r(i)); its value is unchanged by altering the seed. Retain literal
   integer carry and all 16 Walsh masks in actual finite trajectories. A
   source-only order defect cannot distinguish the coherent counterseed.
5. **Recovered controls only.** Reconstruct real Gamma/Beta/Barnes formulas,
   three derivations of the scalar Green budget, and golden-source limit.
   Prior PR370 has the finite golden branch and 1/n correction; October27
   `PI_SELECTED_BOUNDARY_CRT_FRONTIER.md` has the exact Green constant. No
   new-identity claim for those recoveries.

Fresh evaluation choices: n=17,31,53,89; cubic epsilon=1,5; fourth-order
positive mutant epsilon=1; integer interpolation times 0..12 and fractional
quarter-times. Source rank/age mutant t=128; wrong ratio (5,-2,-1,-1);
same-ratio (4,0,-1,0). Source-family equality is not selected-phase equality.

All major finite outputs will be preserved in machine-readable receipts.
Shared-model derivation and separate implementation are not independent peer
review. No Lean or external proof authority is claimed.

Additional finite tensor probe (after the scalar/jet suite, before evaluation):
For coherent same-forcing seed−pi/16, all literal carries from time2 are15, so
its complete grade/carry Walsh matrix must have rank1. Test whether the authentic
zero-seed matrices already computed at n3,7,17 have rank>1; exact matrix rank
would be a finite source-selected distinction, with no universal density claim.
Check Parseval identity sum_mask(1-m_mask²)=16(1-sum_digit p_digit²) exactly.
