# Preregistration — Gamma × SUCC Gaussian sphere solenoids (2026-11-05)

## Provenance / immutable baseline
Additive child of draft SUCC #513 (head `727a97a006e929243e0fee1ab44cf52dc68e2c8f`), which already contains #499's authentic prime-Frobenius Gaussian primal, #500's quarter-Haar Cayley geometry, #509's tau-saddle/angular response, and #513's Fekete/Weyl gate. Historical SUCC primary four-tap BBP forcing and literal U0=0 are **not** to be edited. No main merge, release, publication, source replacement, novelty priority or physical solenoid assertion.

This document records **development derivations ALREADY found before this preregistration**. Future tests below are calibration/independent-oracle checks; do not advertise them as blind confirmations of the pre-derived identities. Distinguish continuum source parameter t, logarithmic variable log t, complex sphere coordinate z, and chronological arithmetic time n.

## Original source and proposed constructions
Source forcing `r_o(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U0=0`, `Un=16 U(n-1)+r_o(n)`. Prime-character angular/radial transfer kernels (inherited from #499):
`K_a(t)=4/((t-1)^2+1)`,
`K_r(t)=2 d/dt log F(t)`,
`F(t)=(2-t^2)/((t-1)^2+1)`, `0<=t<=1`, `F(0)=F(1)=1`.
Let `a=1+i`, `b=1-i`, `u=a/2`, `ubar=b/2`,
`theta(t)=atan(t-1)+pi/4` and `tau=2-sqrt(2)`.

Development prediction GS-01: `u/ubar=i`, `u^8=ubar^8=1/16`. The **complex radial+angular** source coordinate `W(t)=F(t)exp(2i theta(t))` satisfies
`W(t)=u+ubar exp(4i theta(t))=-i(2-t^2)/(t-b)^2`. Consequently `W([0,1])` is exactly the semicircle of center u, radius |u|=1/sqrt(2), from 1 through `1+i` at tau to i. Moreover `K_a(t)dt=sqrt(2)|dW(t)|`, yielding the **existing** BBP period pi by circumference/diameter. This is source **analytic geometry**, not the chronological selected circle orbit. A circle parametrization is not an equidistribution proof.

Development prediction GS-02: meromorphic one-forms on the Riemann sphere
`omega_a=-2i dlog[(t-a)/(t-b)]`, `omega_r=2 dlog[(2-t^2)/((t-a)(t-b))]` restrict to the two SUCC kernels. Their complex polarizations
`omega_a-i omega_r=-2i dlog W` and
`omega_a+i omega_r=2i dlog Wbar_alg`
where `Wbar_alg=i(2-t^2)/(t-a)^2`. At pole a the first is regular and the second has a pole; at b the reverse. Radial residues are +2 at +/-sqrt2 and -2 at a,b; angular residues -2i at a and +2i at b. The radial integral along [0,1] is zero but its meromorphic periods around individual punctures are nonzero. No assertion of a globally exact primitive on the punctured sphere.

Development prediction GS-03: define the SU(2) Möbius rotation `H(z)=(z-1)/(z+1)`; `L(z)=u z`; and the transverse conjugate `L_perp=H L H^-1`. The corresponding fixed-point axes are 0/infty and -1/+1 (perpendicular axes in round-sphere geometry). They preserve *conjugacy invariants* (complex multiplier u, 8-step multiplier 1/16), NOT pointwise orbit equality. The two maps do not commute; a diagnostic at z=0 should give `L(L_perp(0))-L_perp(L(0))=(u-1)^2/(u+1)=(-1-3i)/10`. An arbitrary coordinate rotation will not manufacture source-selected Weyl cancellation.

Development prediction GS-04: under t=e^v, Gamma at sigma+i omega is `int_R exp(sigma v-exp(v))exp(i omega v) dv`, an infinite logarithmic helix with nonconstant weight. Its periodization modulo log16 has Fourier coefficients `Gamma(sigma-2pi i k/log16)` (minus sign for the chosen negative Fourier convention). Normalized sigma=1 gamma coefficients for ALL nonzero k are **nonzero** (Gamma has no zeros). The Gamma helix alone is therefore NOT Haar. In the original t in [0,1] interval, the positive Gamma kernel `e^-t dt` and SUCC angular kernel `K_a(t)dt` have ratio `e^-t((t-1)^2+1)/4` decreasing from 1/2 to 1/(4e). Same geometric carrier does not mean same measure. The analytic radial+angular circle's normalized arclength is SUCC angular measure, while Gamma weighting remains nonuniform.

## Prospective validations (not yet run against this preregistered branch)
1. SymPy exact algebra for Gaussian atom, W rationalization, radius identity, W(tau), F angular half-arc symmetry, derivative and K_a= sqrt2|W'| for t in (0,1).
2. Independent symbolic residues of each meromorphic form at the two complex Gaussian poles and at +/-sqrt2, plus complex-polarization cancellation. Check branch-cut independence of differentials, not absolute logs.
3. Exact symbolic H conjugation, spherical fixed point axes, 8-step multiplier, nonzero commutator, and a negative mutant H=identity (no transverse axis).
4. 50-digit independent Mellin/Gamma Fourier quadrature for the nonzero k=1,3,4,8 coefficients, plus direct periodized density quadrature. Include k=0, wrong sign, and a uniform Haar reference as controls.
5. Exact Fraction original and one-tap mutant BBP states with same seed, fresh n=11,19,37 and finite phase contrasts. Explicit same-forcing coherent wrong seed `s*=-pi/16`: all t-kernel and sphere conclusions remain **unchanged**, though the real selected phases differ. No digit oracle.
6. Formula transfer consistency between the #499 full four-pole original BBP kernel and angular+radial decomposition; mutation of `F(t)` must destroy circle identity except trivial reparametrizations, and perturbing a Gaussian pole destroys eighth-power 1/16.

## Verdict criterion and scope
Accept a new-to-SUCC *geometric factorization* only after exact proofs and independent probes. Refute **Gamma ⇒ Haar** if any normalized Gamma nonzero Fourier coefficient survives (predicted yes). Refute **coordinate-rotation ⇒ selected π normality** with the same-forcing wrong seed (predicted yes). Only a new literal-zero-seed, original-carry, fixed-h signed arithmetic inequality would upgrade the selected Weyl/normality gate; no such claim is anticipated from geometry alone. Report failures precisely, and preserve new code/test receipts in the draft branch.
