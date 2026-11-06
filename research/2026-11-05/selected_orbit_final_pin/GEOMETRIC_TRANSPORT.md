# Finite-delay charge obstruction and audited geometric interfaces

**Paper theorem, exact finite calibration; no original signed estimate.** The original four signed poles and unwrapped U_0=0 remain the source. This is a D obstruction for seed-annihilating observers and a B representation otherwise, not a claim of literature novelty.

## GT1: exhaustive integer-character charge for finite delays

Let r be any deterministic forcing and U_(n+1)(s)=16U_n(s)+r(n+1), U_0(s)=s. For offsets d_j>=0 and integer coefficients c_j, define

    R_d(n)=sum_(k=1)^d 16^(d-k) r(n+k),
    M=sum_j c_j16^d_j,  A_c(n)=sum_j c_j R_d_j(n).

Finite recurrence iteration, without discarding any integer part, proves

    sum_j c_j U_(n+d_j)(s)=M U_n(s)+A_c(n),
    product_j e(c_j U_(n+d_j)(s))=e(A_c(n))e(M U_n(s)).     (GT1)

Changing the seed multiplies this by e(M16^n s). Therefore M=0 if and only if the monomial is invariant under EVERY real seed change. The reverse implication follows because a nonzero integer M gives a nonconstant character of s at every fixed n. At M=0 the observable is exactly a forcing-only function, so every coherent same-forcing completion passes every inequality about this observable that the selected zero seed passes. This is an explicit countermodel to using such observations alone to select Haar.

For a finite trigonometric polynomial in the delayed circle states, apply GT1 term by term and group by M: it becomes sum_M a_M(n)e(MU_n(s)), with explicitly known forcing-dependent coefficients. An inequality about the nonzero-charge part must still control selected weighted Weyl sums. This identity does not prove that no clever nonlinear estimate exists; it identifies the arithmetic quantity any such estimate must bound. It does not cover arbitrary non-character integer-lift predicates, growing delay families without paid constants, or all imaginable source-labelled categories.

Examples: (16,-1) at delays (0,1) and (256,-1) at (0,2) have M=0 and retain only exact source forcing. The ordinary lag difference (-1,1) at (0,d) has M=16^d-1 and retains the original selected phase. The bispectrum observer in #508 has a nonzero angular charge and an explicitly small radial defect; its preserved phase is exactly the missing signed quantity, as that branch already states.

## GT2: rational wrong seeds must not be forced to fail

For the same forcing and s=1/5, 16^n s=s modulo1. Thus every fixed-h sharp interval sum is multiplied by the constant e(h/5), and its magnitude is EXACTLY unchanged. In GT1 the multiplier is e(M/5), independent of n. This is true also at every integer high frequency H_A. A proposed magnitude diagnostic which rejects 1/5 while accepting zero is invalid. Coherent seed s=-alpha and nearby periodic completions remain the relevant nonnormal controls; rational seeds are a different control class.

## EPSILON/ZETA audit and boundary

Read-only #515–#517 are pinned in LIVE_PINS.json and are not ancestors of #518. In #515 the Blaschke Jacobian bounds are valid, the odd-torsion deck injectivity has a residue-characteristic proof, and the same paper constructs odd-root arrays whose limiting sphere observations agree while input limits differ. Exact injectivity does not provide uniform inverse conditioning. In #516, pulling back Fubini--Study by Xi z^d cancels Xi exactly; source phase survives only in anchored section coefficients Xi^j=e(jU_n). The topology and this curvature therefore cannot distinguish the coherent completion. These are inherited obstructions, not new discoveries.

#507–#509's delayed radial bounds, nonzero angular response and cubic phase restoration do not establish the signed trilinear mean. #511/#512/#518's reconstruction retains the phase and its source labels but adds no occupancy estimate. Full integer lifts and literal zero specify the object; their inclusion in an observation does not turn reconstruction into a distribution inequality.

No new stable selected-embedding height inequality, gauge-covariant quantitative plaquette constraint, or source-selected nonlinear bound was obtained in this round. No operator intertwiner from the BBP Gaussian prime classes to the completed zeta Weil form is supplied. The new RH boundary estimate remains on its own branch.

## Next falsifier

For any candidate finite-delay nonlinear inequality, first compute M. If M=0, the coherent completion is an exact falsifier of any claimed mixing consequence. If M!=0, retain a_M(n), all sharp endpoints and source carries; the required new estimate is the actual signed sum of a_M(n)e(MU_n), not the known coefficient norm. A source-only multiplier estimate cannot control that sum without a separate argument.
