# Operation Kepler — coherent Gamma arithmetic tiling and the BBP normal form

**2026-10-29; research-only draft, stacked on SUCC #373 at 262ed838b30b7ec50f4d05a4ec8fa1c977970dec.** Inherited original signed four-pole source and U_0=0 are unmodified. Research ancestors #367/#373; totient/Pascal sibling #372 at 44912760eca39069ef5b980a492a1feabc9f6149 is consulted, not silently merged. Base-16 normality of pi and RH remain OPEN.

## Why Kepler rather than epicycles

An exact mathematical representation need not reveal the mechanism governing the selected trajectory. The author asks whether harmonic/golden/Euler, totient/cototient, Gamma and Gaussian 45-degree twists glue into a plane and whether the result can constrain genuine BBP cancellation. The answer is a coherent **layered** construction plus exact obstructions; a single canonical plane preserving all these structures has not been derived.

## The Gamma triangle plane — proved local construction

Let Z_0 have Gamma(2,1) distribution and let (A_i) and (B_j) be independent families of Gamma(1,1) strip increments. For i,j≥0 set

V_(i,j)=Z_0+sum_(k<i) A_k+sum_(l<j) B_l.

Then V_(i,j) has Gamma(i+j+2,1) distribution. Every unit square has

V_(i+1,j)-V_(i,j)=A_i = V_(i+1,j+1)-V_(i,j+1),

V_(i,j+1)-V_(i,j)=B_j = V_(i+1,j+1)-V_(i+1,j).

Triangulate each square along the same diagonal. The two triangles use exactly the same underlying edge variables, and the sum around each square is zero **pathwise**. Independent Gamma(r,1) and Gamma(s,1) add to Gamma(r+s,1); the fraction X/(X+Y) has Beta(r,s) law, independent of X+Y. This supplies lawful arbitrary subdivision and recombination. Shared strips imply neighboring cells are correlated, not independent.

Take independent positive increments along every horizontal/vertical strip indexed by all integers and use oriented two-sided sums: this makes a well-defined additive potential on the complete Z² plane, with vanishing square defect. On negative coordinates these potentials may be signed and should NOT be called Gamma variables. Conditional increment independence also cannot be asserted on the negative side of a pinned reference without further information. **Whole-plane geometric gluing is exact; an everywhere-positive Gamma rank is not part of the theorem.**

For a source-faithful rank analogue, the positive convolution roots μ_(a,t) constructed in #367 can replace Gamma strip increments at each fixed source parameter a>0. Their convolution and exponential tilting commute; this still does NOT identify the stochastic sheet with deterministic pi digits.

## Determinant-one Fibonacci integer tiling — proved all Z²

Let B be the integer matrix [[1,1],[1,2]], with det B=1. Define u_m=B^m(1,0)^T for all integers m, and T_(m,n)=u_m dot u_n. Every adjacent cell satisfies

T_(m,n)T_(m+1,n+1)-T_(m,n+1)T_(m+1,n)=1.

Proof: the 2x2 cell is the product of the adjacent column pair matrices and their transpose. det[u_m,u_(m+1)]=det(B)^m det[(1,0),(1,1)]=1, and similarly in n. This is universal, not a finite-grid extrapolation. Its positive-index vectors are (1,0),(1,1),(2,3),(5,8),... and align asymptotically with golden/Fibonacci directions. No asserted pathwise functor identifies this integer array with the Gamma field or the selected BBP orbit.

## Harmonic / golden / Euler–Mascheroni rank readout

Choose λ=(sqrt(5)-1)/2, with λ²=1-λ and 1+λ=λ^(-1), via the original **two-stage Oily** fixed-point convention. For Y_r~Gamma(r,1) and Re(s)>-r,

K_r(q,s)=E[Y_r^s exp(-qY_r)]=Gamma(r+s)/(Gamma(r)(1+q)^(r+s)).

Then E log Y_r=ψ(r) and E exp(-λY_r)=λ^r. Define D(r)=ψ(r)-λ^r. For positive integer rank,

D(r)=H_(r-1)-γ-λ^r,
D(r+1)-D(r)=1/r+λ^(r+2)>0,
D(2)=1-γ-λ²=λ-γ.

The Gamma function supplies continuous-rank interpolation, harmonic numbers give its exact integer logarithmic moments, and the golden Laplace probe uses the declared two-stage source. γ alone does not select λ; wrong-observer and one-channel controls remain valid.

## The exact Gaussian 45° / 90° twist

Use the **specified Fourier sign** exp(+itY), unit Gamma rate and frequency t=1. Then

Φ_r(t)=E exp(itY_r)=(1-it)^(-r),
Φ_1(1)=(1+i)/2 (angle +45°, amplitude 1/sqrt(2)),
Φ_2(1)=i/2 (angle +90°, amplitude 1/2),
Φ_(r+s)(1)=Φ_r(1)Φ_s(1).

This is an exact Gaussian rational phasor composition, with amplitude contraction. It is not a unitary physical quarter-turn, and the angle becomes r arctan(t) at other frequencies. The separate complex-argument Euler Gamma integral becomes a Fourier transform in u=log x:
Gamma(σ+it)=∫_R exp(σu-exp(u)) exp(itu)du.
These are related analytic transforms, not the assertion that Gamma(s) literally rotates a physical carrier.

## NEW exact original-source finite phasor theorem (GT-6)

Retain the authentic BBP source

R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
Q(x)=4-2exp(-3x)-exp(-4x)-exp(-5x)>0,
μ_a(dx)=exp(-ax)Q(x)dx/R(a), a>0.

At the natural source scale define Φ_a=E_μa exp(iaX)=R(a(1-i))/R(a).

**For every real a>0: Re Φ_a>0, Im Φ_a>0 and |Φ_a|>1/2.** It approaches the Gamma rank-two response by the explicit asymptotic

Φ_a=i/2 + 59(1+i)/(60a)+O(a^(-2)).

Certificate: put

D=(a²+4a+8)(2a²+6a+9)(2a²+10a+25)(15a²+121a+240).

Then Re Φ_a=(a+3)(a+4)(a+5) P4/(2D), Im Φ_a=(a+3)(a+4)(a+5) P5/(2D), where

P4=118a⁴+930a³+3707a²+7260a+7200,
P5=60a⁵+602a⁴+2904a³+7667a²+11280a+7200.

Also 4D(15a²+121a+240)(|Φ_a|²-1/4)=P9, where

P9=3540a⁹+91318a⁸+1059000a⁷+7300703a⁶+33156378a⁵+
103207249a⁴+220620060a³+312831000a²+266976000a+103680000.

Every displayed denominator and every polynomial coefficient is positive for a>0. Thus the source response is in quadrant I with radius strictly above 1/2, approaching exactly 90 degrees. The attached exact SymPy probe independently reconstructs and checks the algebra and first correction. The simpler positive **mutant** Q_mut(x)=15x has the same Gamma(2) endpoint but Φ_mut=i/2 at every finite a. This provides a genuine finite source fingerprint, not signed selected-path cancellation.

## Totient/cototient arithmetic glue

Keep a full register j mod q, with successor j↦j+1 mod q. Define χ_q(j)=1 if gcd(j,q)=1, 0 otherwise. Its Möbius expansion is χ_q(j)=sum_(d|gcd(j,q)) μ_Mobius(d); the uniform counts are φ(q)=sum_(j mod q)χ_q(j) and cototient(q)=q-φ(q). For coprime q,s, CRT glues residue registers exactly. Projecting first to the primitive/nonprimitive bit is NOT dynamically sufficient: at modulus 6, 0 and 2 are both nonprimitive, but successors 1 and 3 have different primitive flags.

Oily weights w_j=(j+1)/2^(j+2) yield **weighted** primitive masses m_2=m_16=4/9, m_3=29/49, m_6=416/1323, not the uniform fractions φ(q)/q. The jointly conditioned Gamma ranks j+2 described in sibling #372 belong to a declared Pascal observation model; the older Oily packet model sharing the same grade marginal has a different joint law. Keep their source passports separate.

## Global symmetry obstruction

A 45° rotation cannot preserve a rank-two Euclidean lattice as a global symmetry: in a lattice basis its matrix would have integer entries, but its trace is 2cos(π/4)=sqrt(2), not an integer. A diagonal of a square may point at 45°; that is not the same as full rotational lattice invariance. The hyperbolic Farey tessellation with unimodular rational neighbors is likewise a different chart and is not globally preserved by multiplication by exp(iπ/4). This does not prohibit local twist transport, nonperiodic tilings or source-dependent chart changes.

## Operation Kepler: O(1) uniform normalization of the **selected** orbit

With original signed r(n)=R(8n-7), U_0=0, U_n=16U_(n-1)+r(n), put T_n=sum_(j>=1)16^(-j)r(n+j). The inherited BBP identity gives T_0=π/16, U_n+T_n=16^(n-1)π and T_(n+1)=16T_n-r(n+1). Hence X_n=U_n+T_n satisfies **exactly** X_(n+1)=16X_n.

Since Q(x)=2(1-e^(-3x))+(1-e^(-4x))+(1-e^(-5x))≤15x, the positive source obeys r(k)≤15/(8k-7)². Monotonicity of r and the geometric sum imply 0<T_n≤r(n+1)/15≤1/(8n+1)². Therefore for every integer h and N≥1,

|sum_(n≤N)e^(2πih U_n) - sum_(n≤N)e^(2πih16^(n-1)π)|
 ≤2π|h|sum_(n≥1)T_n
 ≤2π|h|*(π²/384)=π³|h|/192.

This is **O(1) for the UNnormalized sums**, hence O_h(1/N) for the normalized averages. It is a source-faithful strong comparison but does not bound the remaining pure pi orbit sum. The coherent counterseed U_0=-π/16 still gives V_n=-T_n→0, with Weyl average→1. The zero seed must remain authenticated.

## Claim status and next discriminatory experiment

**PROVED LOCAL / CLASSICAL:** Gamma/Beta gluing; Fibonacci SL2 tiling; Gamma 45/90 phasors; the strict finite original-source phasor polynomial theorem; CRT residue preservation; the square-lattice 45° symmetry no-go; and the O(1) BBP normal-form bound. **UNVERIFIED:** exact functor from those layers to the selected digit history, and physical Gamma/rotation interpretation. **OPEN:** pi base-16 normality and RH.

The next target is a genuinely noncentral, signed, original-source and zero-seed-sensitive estimate on the complete literal-carry/Pascal/primitive tensor, including source labels and residue state mod 2,3,5,6,10,15,30. Require controls: coherent same-forcing seed (-π/16); wrong fourpole source; positive mutant Q=15x; wrong Pascal/Gamma joint; two-color projection; incorrect 45° global symmetry; and generic coherent phase sequences. An invertible positive weighting, or this O(1) normal form, is not a new cancellation estimate.

**Reproduction:** run the adjacent kepler_exact_probe.py (SymPy). The full additional standalone exact-rational implementation, 10 test methods and independent oracle are preserved as a downloadable research bundle in the conversation. The full SUCC suite, Lean and hosted exact-head CI have NOT been run on this new branch; regenerate its catalog and run the required AGENTS.md gates before merging. No historical source, conjecture status, or default is changed.

**Source context:** NIST DLMF Gamma integral https://dlmf.nist.gov/5.2 and digamma https://dlmf.nist.gov/5.4 ; Bailey–Crandall (2001) https://doi.org/10.1080/10586458.2001.10504441 ; source repo SUCC draft PRs #367, #372, #373.
