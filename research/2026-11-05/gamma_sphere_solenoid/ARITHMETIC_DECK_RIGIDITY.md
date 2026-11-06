# Post-prereg discovery: exact odd-cyclotomic deck rigidity of the Gaussian sphere observation

**Research-only, 2026-11-05, derived AFTER GS-01–04 preregistration.** Existing SUCC #499/#500 supplies the authentic zero-seeded BBP and the real Cayley chart; the Gaussian/Riemann-sphere circle W comes from PROOFS.md in this same research child. Arithmetic odd-root rigidity is proved here by a classical prime-to-residue-characteristic argument, but worldwide scholarly novelty/independent referee verification are **UNVERIFIED**. There is no original-source Weyl bound.

## 1. Transport from the ACTUAL source-phase circle

Let \(\zeta=e^{2\pi i x}\in S^1\). The **source phase to tangent chart** is
\[
t=\tan(\pi x)=-i(\zeta-1)/(\zeta+1)
\]
(with t=∞ at ζ=−1; all maps extend projectively). Let \(a=1+i,b=1-i,u=a/2,\bar u=b/2\), \(q(t)=(t-a)/(t-b)\), and
\[
W(t)=u-\bar u\,q(t)^2.
\]
A direct substitution gives the EXACT circle automorphism
\[
\boxed{B(\zeta)=q(t(\zeta))
=\frac{(1+2i)\zeta+1}{\zeta+1-2i}
=c\frac{\zeta-z_0}{1-\bar z_0\zeta},}\tag{DL1}
\]
with \(z_0=(-1+2i)/5,\ |z_0|^2=1/5,\ c=(-3+4i)/5,\ |c|=1\).
Hence the source-observed normalized sphere circle is
\[
\boxed{S(\zeta):=\frac{W(t(\zeta))-u}{\bar u}=-B(\zeta)^2.}\tag{DL2}
\]
It is a degree-TWO continuous map of the circle, not a global homeomorphism.

The sharp angular Jacobian of the degree-one Blaschke transport B is the Poisson kernel
\[
\frac{d\arg B(e^{i\varphi})}{d\varphi}
=\frac{1-|z_0|^2}{|e^{i\varphi}-z_0|^2}
\in\left[\frac{1-r}{1+r},\frac{1+r}{1-r}\right]
=\boxed{[\varphi_g^{-2},\varphi_g^2]},\quad
r=1/\sqrt5,\;\varphi_g=(1+\sqrt5)/2.\tag{DL3}
\]
Bounds are sharp at phases aligned/anti-aligned with z0. This is the exact SUCC Gaussian/Cayley origin of the golden-ratio squared distortion factor. It is a geometry constant, not an arithmetic equidistribution rate.

## 2. Explicit branch involution and elementary obstruction

The nontrivial deck involution of S is
\[
\boxed{
J(\zeta)=B^{-1}(-B(\zeta))
=\frac{i(3\zeta+1-2i)}{(2-i)\zeta-3i}.
}\tag{DL4}
\]
On the whole circle, \(J^2=\mathrm{id}\), \(B(J\zeta)=-B(\zeta)\), and \(S(J\zeta)=S(\zeta)\). There are two preimages under S for every point. But SUCC's source phases belong to a much smaller arithmetic set.

**Theorem (odd-torsion branch rigidity).** Let z,w be complex roots of unity of ODD order. Then
\[
\boxed{w\ne J(z).}\tag{DL5}
\]
Consequently S is **injective on the union of ALL odd-order roots of unity**, despite being two-to-one on the full circle.

**Proof (no asymptotics).** Assume w=J(z). Clearing the denominator in DL4 gives the exact Gaussian-integer identity
\[
(2-i)zw-3i(z+w)-(2+i)=0.\tag{DL6}
\]
Let K be a cyclotomic number field containing z,w and i, and choose any prime ideal of its ring of integers above the Gaussian prime \(\varpi=1+i\) (the residue characteristic is 2). Since \(i\equiv1\), \(2\equiv0\) and \(3\equiv1\) modulo \(\varpi\), DL6 becomes
\[
\boxed{(z+1)(w+1)=0\quad\text{in the residue field of characteristic 2}.}\tag{DL7}
\]
At least one of z,w reduces to 1. The reduction map on roots of unity whose order is coprime to residue characteristic is injective (prime-to-p torsion has no nontrivial elements in the kernel of reduction). Since both orders are odd, this forces z=1 OR w=1 in the characteristic-zero field K.

But J(1)=(-3+4i)/5. This element of Q(i) is NOT a Gaussian integer and therefore not an algebraic integer, while EVERY root of unity is an algebraic integer. If z=1, w=J(1) is impossible. If w=1, involutivity implies z=J(1), equally impossible. Contradiction. QED.

**Why the hypothesis matters:** J(-1)=i and J(i)=−1. Both ARE roots of unity, but orders 2 and 4 are even. A generic circle covering does not have DL5; e.g. the nontrivial circle involution z↦z^−1 preserves odd torsion. The Gaussian coefficients and ramified prime 2 are doing actual proof work.

## 3. Source consequence: the authentic BBP falls exactly inside the rigid carrier

The ORIGINAL historical four-pole rational source simplifies algebraically to
\[
\boxed{r_o(n)=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}.}\tag{DL8}
\]
Every denominator factor is odd at integer n≥1. The integer radix update \(U_n=16U_{n-1}+r_o(n)\) starting from literal \(U_0=0\) therefore gives U_n∈Q with ODD reduced denominator for every n≥0. Consequently
\[
\boxed{\zeta_n=e^{2\pi i U_n}\text{ is a root of unity of odd order for every }n.}
\]
The exact sphere observation S(ζ_n) therefore has precisely ONE lift **within the union of all odd-order cyclotomic phases**. This resolves the *finite exact sign/branch ambiguity*, without an oracle for π digits. It is an arithmetic source restriction, not a new phase statistic.

An arbitrary source tap mutation can destroy the odd-denominator contract. A separate arbitrary initial seed (e.g. irrational s*=−π/16) also fails the rational source-state condition. Therefore one must not use DL5 to infer that the correct literal zero seed has already been selected by an asymptotic observation.

## 4. Counterintuitive limitation: source-admissible exact injectivity is not a stable inverse

Let m be Haar probability on input circle S¹. B and S are holomorphic self-maps of the unit disk with unimodular boundary values. The mean-value property for their nonnegative Fourier powers gives
\[
\int_{S^1}S(\zeta)^h\,dm(\zeta)=S(0)^h,\quad
S(0)=-B(0)^2=\boxed{\eta=(3-4i)/25},\quad h\ge1.\tag{DL9}
\]
Thus even a NORMAL input circle orbit would send the sphere observables S(ζ_n) to the **NON-HAAR Poisson/harmonic measure** \(P_\eta\), with density
\[
dP_\eta(e^{i\alpha})
=\frac{1-|\eta|^2}{|e^{i\alpha}-\eta|^2}\frac{d\alpha}{2\pi},
\quad|\eta|=1/5.
\]
**Demanding Haar of the W-circle is a WRONG target for π normality.** The correct input-Haar transported target is P_eta.

Conversely, S_*m=S_*(J_*m) since S∘J=S, yet \(J_*m\ne m\). Indeed J extends holomorphically to the open disk and
\[
\int_{S^1}\zeta\,d(J_*m)(\zeta)=J(0)=(-1+2i)/3\ne0.\tag{DL10}
\]
This is a **full-support non-Haar** countermodel with EXACTLY the same S-observation distribution as Haar, not just a finite near miss.

Restricting to the odd-torsion arithmetic subset does NOT restore a stable inverse at the level of weak convergence. The odd-order roots are dense in S¹. For each complete Nth root grid with N odd, approximate each of its J-images by a root of unity of an odd order M_N→∞ with mesh o(1). Both arrays now consist *only* of odd-order roots; their S-observations have the same asymptotic P_eta target, but their input distributions approach m and J_*m respectively. No contradiction with DL5: no exact individual branch equality is asserted between the two odd-order arrays, only arbitrarily close values.

**Hence:** arithmetic exact source admissibility makes individual branch selection unique; it does not by itself yield a continuous/quantitatively stable observation inverse, and it supplies no bound for \(\sum_{n\le N}e(hU_n)\).

## 5. Falsifiers, provenance, and next arithmetic lamp

Independent tests should check: (a) exact DL1–DL8 with SymPy; (b) odd conductor 1,3,5,7,9 versus ALL ordered odd pairs via cyclotomic resultants; (c) even-order counterexample −1→i; (d) root grids N=53,97 against the non-Haar Poisson Fourier target; (e) branch-flipped grids identical under S but not equidistributed in original ζ; (f) approximate odd-order grid lift with explicit quantitative mesh error and failure of inverse stability. These finite tests validate implementation, not the universal DL5, which has the separate prime-reduction proof above.

**New-to-SUCC frontier:** Can SOURCE-TIME recurrence, prime-Frobenius residues and carry constraints upgrade the exact odd-torsion lift into any quantitative **signed** temporal estimate? That is a genuinely further probe. Galois/cyclotomic membership alone is not enough: root grids can be arranged nonuniformly and both converge after branch-approximated sphere observation.

**Claim status:** DL1–DL10 paper-proved within declared classical algebraic/analytic facts; validation finite observed; global novelty UNVERIFIED; no externally verified original Weyl saving, no π normality, no RH result.
