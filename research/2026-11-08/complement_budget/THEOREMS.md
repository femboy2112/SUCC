# A finite dual test of the original complement's arithmetic budget

Status: **PROVED PAPER** for the stated finite inequalities. Source-specific
finite applications are separately certified; no asymptotic decay is asserted.
Underlying convex duality, orthogonal projection and FFT identities are classical.

## CB1. An unrestricted-resonance dual lower bound

On the authenticated clean clock S=xi<16>, use normalized inner product
<u,v>=mean conjugate(u)v. Put a(x)=e(hx/p), r=conjugate(a), |B|<=1,
W=<r,B>, E=mean |B|². A declared finite menu of nonresonant polynomial atoms
phi_j=e(P_j(x)/p) has PR8 costs w_j=min(1,D_j sqrt(p)/m)>0,
where D_j is the NONCONSTANT reduced degree of hX+P_j modulo X^m-xi^m.
Thus |<r,phi_j>|<=w_j. Define

    M = max_j |<phi_j,B>|/w_j,       M=0 for an empty menu.

For EVERY complex R and all finite complex coefficients c_j, with
V=Rr+sum c_j phi_j, rho=mean |B-V| and K=sum |c_j|w_j,

    rho + K >= (E-|W|²)/(max(1,M)+|W|).                 (CB1)

The retained resonance R is completely free in this inequality. In particular,
small W does not by itself ensure a small PR8 certificate in a given dictionary.
This is a lower bound on a sufficient METHOD's cost, not a lower bound on W.

Proof. Set u=B-Wr. Then <r,u>=0 and <u,B>=E-|W|²>=0.
Pointwise |u|<=1+|W|. For each atom,
|<u,phi_j>|<=|<B,phi_j>|+|W| |<r,phi_j>|<=(M+|W|)w_j.
Writing B=(B-V)+Rr+sum c_j phi_j, take the real part of <u,B> and bound:

    E-|W|² <= (1+|W|)rho + (M+|W|)K
              <= (max(1,M)+|W|)(rho+K).

The denominator is positive. No independence, learning generalization, or
selection-before-observation assumption was used. Coefficients may depend on
the complete authenticated history. QED.

Consequently if E>=e0>0, W->0 and M stays bounded along a sequence, then the
menu's best rho+K stays bounded away from zero. This CONDITIONAL obstruction
can coexist with normality. No such asymptotic M bound for the actual source
is proved here. Enlarging the menu changes M; a certificate for monomial atoms
does not cover every mixed polynomial in the same degree range.

## CB2. Fully finite outward certificate

Given rational E_lower<=E, W_upper>=|W| and M_upper>=M, a rigorous lower bound is

    max(0,E_lower-W_upper²)/(max(1,M_upper)+W_upper).

For a monomial menu phi_(d,t)=e(t*x^d/p), scatter B's values onto y=x^d modp.
Its complete length-p DFT divided by m gives ALL correlations
<phi_(d,t),B>. This includes every coefficient t, with no spectral subsampling.
Omit t=-h from d=1 (the resonance); omit duplicate t=0 from d>1. With d<m,
t!=0 and d>=2, the reduced degree is d. At t=0 in d=1 it is one.

This remains a restricted menu. No quantitative assertion about its unmeasured
mixed-coefficient polynomial extensions is licensed by this calculation.

## CB-FFT. Integer-radius Bluestein certification

Centers are Gaussian integers divided by S=2^80. A shared integer radius R
means complex L1 error at most R/S for each entry. The inherited `phase`
routine supplies outward rational sine/cosine rectangles by Taylor expansion
and a Machin pi enclosure. Their midpoint and summed coordinate half-widths
give a center and L1 radius with no floating input.

Multiplication of two centers rounds each coordinate downward, costing <2/S
in L1. For a butterfly a +/- w b, exact w is a unit phase, hence |w|_1<=2.
If input radii are R, twiddle radius T, and center norms |b_center|_1<=C/S,
the new error in units 1/S is bounded by

    3R + ceil(T C/S) + 2.

This follows by decomposing w b - w_center b_center as
w(b-b_center)+(w-w_center)b_center. Bit reversal is exact; induction proves
the bound for every unnormalized radix-two FFT stage. The implementation uses
the maximum actual center L1 norm each stage, without interpreting it as an
upper bound on the true input norm.

For two transformed arrays with radii R_A,R_B and maximum center norms
C_A/S,C_B/S, pointwise multiplication has radius

    ceil((R_A C_B + R_B C_A + R_A R_B)/S)+2.

Inverse FFT uses the same butterfly bound. Division by positive integer N
adds at most two integer radius units after rounding and divides the old
radius upward. Chirp multiplications use the first product bound.

The Bluestein identity is exact:

    exp(-2 pi i j k/p)
      = e(-j²/(2p)) e(-k²/(2p)) e((k-j)²/(2p)).

Zero padding N>=2p-1 makes the circular convolution reproduce every required
difference k-j. Thus the integer implementation encloses the complete DFT,
including composite lengths in tests. It does not rely on floating FFT error
heuristics. Independent direct rational-phase summation tests sign, scaling,
padding and error containment. Formal kernel verification is not claimed.

## Boundary and next theorem

All these tests concern a declared model class. They can refute a cheap-fit
shortcut or demonstrate a finite budget obstruction; they cannot establish
normality's negation. The original-zero task is still to find and prove a
usable all-epoch model estimate, or bypass this stronger sufficient model
condition with a direct signed covariance estimate.

Pi base-16 normality: OPEN. RH: OPEN.
