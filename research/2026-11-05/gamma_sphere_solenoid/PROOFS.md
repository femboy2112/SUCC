# Operation Gamma × Riemann sphere: intrinsic Gaussian solenoids and exact angular–radial circle

**Research-only SUCC note, 2026-11-05.** Additive child of #513, whose ancestry contains original prime-Frobenius primal #499, Cayley source #500, radial tau saddle #509 and Fekete gate #513. All prior statements are inherited, not independently rediscovered. This note constructs a *new-to-this-branch explicit factorization* and subjects its interpretation to countermodels. Classical arctangent, Möbius, beta–Gamma and Fourier facts are not claimed as original mathematical discoveries. **Base-16 π normality remains OPEN.**

**Chronology:** GS-01–04 and the semicircle identity were derived *before* the preregistration; the rational beta-coordinate discovery was made *after* the preregistration. All reported finite tests are validation, not blind invention of the theorem.

## 0. Types and exact original source

The original source is the historical unmodified four-tap BBP:
\[
P_o(t)=4-2t^3-t^4-t^5,\quad
r_o(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r_o(n).
\]
The genuine prime-character decomposition from #499 is
\[
D_8(t)=1-t^8/16,\qquad
K_a(t)=\frac{P_a(t)}{D_8(t)}=\frac4{(t-1)^2+1},
\quad
K_r(t)=\frac{P_r(t)}{D_8(t)}=2\frac{d}{dt}\log F(t),
\]
\[
F(t)=\frac{2-t^2}{(t-1)^2+1},\qquad
K_a+K_r=P_o/D_8,\qquad F(0)=F(1)=1.
\]
Here **t∈[0,1] is the analytic source parameter**, not chronological BBP time n or a sampled fractional digit phase. Arithmetic Y_n/Z_n are the zero-seeded recurrences of angular/radial taps, U_n=Y_n+Z_n, with inherited positive Z_n bound 0<Z_n<1/(32n+16). Do not identify analytic angular measure with source-orbit empirical distribution.

Let a=1+i, b=1-i, u=a/2 and \bar u=b/2. Then
\[
a b=2,\quad u/\bar u=i,\quad u^4=-1/4,\quad u^8=\bar u^8=1/16.
\]
This is the authentic Gaussian primal atom #499, not a freely fitted base-16 ratio.

## 1. GS-01: a source-intrinsic semicircle on the Riemann sphere

Define the monotonically increasing angle
\[
\theta(t)=\arctan(t-1)+\pi/4,\quad \theta(0)=0,\quad\theta(1)=\pi/4,\quad
\theta'(t)=1/[(t-1)^2+1].
\]
The radial potential and the angular phase combine as
\[
W(t)=F(t)e^{2i\theta(t)}.
\]
With q(t)=(t-a)/(t-b), direct algebra gives e^{2i\theta}=-i q(t) on real t. Therefore
\[
\boxed{W(t)=u-\bar u\,q(t)^2
=u+\bar u e^{4i\theta(t)}
=-i\frac{2-t^2}{(t-b)^2}.}\tag{GS1}
\]
The identity is rational and extends to a degree-two map \(\widehat{\mathbb C}\to\widehat{\mathbb C}\), ramified at a and b. The restriction to real t∈[0,1] satisfies
\[
|W(t)-u|=|\bar u|=1/\sqrt2.
\]
It traverses exactly HALF this Euclidean circle as 4θ runs from 0 to π:
\[
W(0)=1,\quad
W(2-\sqrt2)=1+i,\quad W(1)=i.
\]
This circle lives in the affine chart of the **Riemann sphere**; it need not be a round-sphere great circle. Its *Euclidean* radius is |u|, center u. Differentiating GS1 gives
\[
|dW|=4|\bar u|\,d\theta=2\sqrt2\,d\theta,\quad
\boxed{K_a(t)\,dt=4\,d\theta=\sqrt2\,|dW|.}\tag{GS2}
\]
The half-circle has Euclidean length π/√2, diameter √2, and
\[
\int_0^1K_a(t)\,dt
=\sqrt2\,{\rm Length}(W([0,1]))
=\frac{2\,{\rm Length(semicircle)}}{\rm Diameter}=\pi.
\]
**Interpretation:** a source-faithful *representation of the known π-period* as circumference/diameter. The universal Euclidean circumference ratio is not deduced from a new axiom, and the π constant was already present in classical arctangent geometry.

### GS-01b: exact radial saddle symmetry

Write v=t−1=tan(θ−π/4). Then
\[
F(t)=\frac{1-2v-v^2}{1+v^2}
=\cos(2\theta-\pi/2)-\sin(2\theta-\pi/2)
=\sqrt2\cos(2\theta-\pi/4).
\]
(The intermediate cosine/sine expression is understood with v=tan(θ−π/4); equivalently it is \(\cos(2(\theta-\pi/4))-\sin(2(\theta-\pi/4))\).)
Consequently
\[
G(\theta):=2\log F
=\log 2+2\log\cos(2\theta-\pi/4),
\quad G(\theta)=G(\pi/4-\theta).
\]
Its unique maximum is \(\log2\) at \(\theta=\pi/8\), corresponding to \(\tau=2-\sqrt2\), and the circle point \(W(\tau)=1+i\). This recovers #509's source radial saddle and angular half-arc in a SINGLE intrinsic circle, without using its chronological BBP orbit.

## 2. GS-02: transverse meromorphic solenoids have different monodromy

On the punctured Riemann sphere define genuine meromorphic differentials
\[
\omega_a=-2i\,d\log\frac{t-a}{t-b},\qquad
\omega_r=2\,d\log\frac{2-t^2}{(t-a)(t-b)}.
\]
Their restrictions to [0,1] are \(K_a(t)dt,K_r(t)dt\). These are **dlog differentials**, independent of a choice of local logarithm branch. The angular and radial sources are two real components of the SAME complex logarithmic connection:
\[
\boxed{\omega_a-i\omega_r=-2i\,d\log W(t),}\qquad
\boxed{\omega_a+i\omega_r=2i\,d\log W^*(t),}\tag{GS3}
\]
with \(W^*(t)=i(2-t^2)/(t-a)^2\), equal to complex conjugate W for real t.

The residue table is exact:
| Puncture | res ω_a | res ω_r | res (ω_a−iω_r) | res (ω_a+iω_r) |
|---|---:|---:|---:|---:|
| a=1+i | −2i | −2 | 0 | −4i |
| b=1−i | +2i | −2 | +4i | 0 |
| +√2 | 0 | +2 | −2i | +2i |
| −√2 | 0 | +2 | −2i | +2i |

Total residues of each meromorphic differential equal zero on \(\widehat{\mathbb C}\). At a complex pole the angular loop is real-valued ±4π, while radial loop is imaginary-valued −4πi; these are operationally 90-degree different **complex periods** in a declared dlog basis. They are not electromagnetic fields or physical spacetime directions.

The radial period on the original interval remains ZERO:
\[
\int_0^1 \omega_r=2\log F(1)-2\log F(0)=0.
\]
But around individual complex punctures \(\oint\omega_r=2\pi i\operatorname{res}(\omega_r)\ne0\).
**This is the rigorous meaning of a globally nontrivial support differential whose particular observed boundary integral vanishes.** An interval exact form need not have a single-valued primitive on the punctured sphere. None of these integrals varies with the choice of U0; source selection remains unproved.

## 3. GS-03: two sideways sphere axes and honest transport cost

Let \(H(z)=(z-1)/(z+1)\), a Möbius transformation represented by the SU(2) matrix \(2^{-1/2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\). It rotates the *round sphere* and takes the 0/∞ axis to the antipodal −1/+1 axis. Define
\[
L(z)=uz,\qquad L_\perp=H\circ L\circ H^{-1},
\quad L_\perp(z)=\frac{(u+1)z+u-1}{(u-1)z+u+1}.
\]
The axes are perpendicular in the usual round-sphere geometry; the two loxodromic maps are conjugate and share their intrinsic multiplier u and eight-step multiplier 1/16 in their OWN axis charts:
\[
L^8(z)=z/16,\quad L_\perp^8=H\circ L^8\circ H^{-1}.
\]
They do NOT commute. An exact nonzero transport defect is
\[
(L\circ L_\perp)(0)-(L_\perp\circ L)(0)=\frac{(u-1)^2}{u+1}=\frac{-1-3i}{10}.\tag{GS4}
\]
It is a **map composition defect**, NOT a nontrivial source-selected digit current, and the affine difference here is well-defined only because these particular points are finite.

Some intermediate \(L_\perp\)-orbits hit ∞: starting at \(z=3/5\), the fourth iterate is ∞, so ALL iterations and verifications must be in homogeneous \(\mathbb{CP}^1\) coordinates, not affine division. This was identified by a failing early local test and repaired before validation.

The round-sphere line element is \(ds_{S^2}=2|dz|/(1+|z|^2)\). For an SU(2) map H this line element is invariant; however Euclidean lengths in the complex chart are NOT invariant:
\[
|H'(z)|=\frac2{|z+1|^2},\quad
K_a\,dt=\frac{1+|W|^2}{\sqrt2}\,ds_{S^2}.
\]
A sideways observer must transport this weight with the sphere rotation, not silently use \((1+|H(W)|^2)\) or assume Euclidean arc length preservation. With the correct transported density the original analytic π integral agrees **tautologically by change of variables**, not because of an independent arithmetic constraint.

## 4. GS-04: two Gamma solenoids are NOT automatically Haar

Let T have the Exp(1) density \(e^{-t}dt\) for t>0 and V=log T. Euler's integral gives for Re(s)>0
\[
\Gamma(s)=\int_{\mathbb R}\exp(sv-e^v)\,dv.
\]
For L=log16, periodize \(p_L(v)=\sum_{j\in\mathbb Z}\exp(v+jL-e^{v+jL})\) onto [0,L). The normalized density has exact coefficients
\[
\widehat p_L(k)
=\int_0^Lp_L(v)e^{-2\pi i k v/L}dv
=\boxed{\Gamma(1-2\pi i k/L)}.\tag{GS5}
\]
Gamma has no zeros; thus all nonzero coefficients remain nonzero. **The canonical Gamma-weighted infinite logarithmic helix does NOT produce Haar**, even though it occupies the full circular carrier.

The opposite chirality has coefficient \(\overline{\Gamma(1-2\pi i k/L)}\). The convolution of the two has the exact positive non-Haar multiplier
\[
\boxed{|\Gamma(1+2\pi i k/L)|^2
=\frac{\pi\omega_k}{\sinh(\pi\omega_k)},\quad\omega_k=2\pi |k|/L,\quad k\ne0,}\tag{GS6}
\]
with value 1 at k=0. Equivalently a double Gamma smoothing of ANY source phase empirical measure attenuates its Fourier coefficients by this multiplier without extinguishing them; for every fixed k, smoothed Weyl decay is equivalent to the original **OPEN** Weyl decay. Reversing the attenuation at large |k| has exponential conditioning cost. A fourfold rotation average removes k not divisible by 4 but leaves coefficient \(\Gamma(1-8\pi i/L)\ne0\) at k=4. Neither a perpendicular rotation nor averaging two conjugate carriers establishes Haar.

On the *source interval* [0,1], the Gamma density \(e^{-t}dt\) and original angular source density \(K_a(t)dt\) satisfy
\[
\frac{e^{-t}}{K_a(t)}
=\frac{e^{-t}((t-1)^2+1)}4,\qquad
\frac{d}{dt}\frac{e^{-t}}{K_a(t)}
=-\frac{e^{-t}(t-2)^2}{4}<0\quad(0<t<1).
\]
The ratio decreases strictly from 1/2 to 1/(4e). Their measures have the same support and equivalent finite densities, **not the same angular distribution**.

## 5. GS-05: explicit exact SUCC → Beta → Gamma factorization (post-prereg discovery)

The original angular phase has rational sine and cosine:
\[
\sin(2\theta(t))=\frac{t(2-t)}{D(t)},\qquad
\cos(2\theta(t))=\frac{2(1-t)}{D(t)}.
\]
Define the monotone rational projective coordinate on 0≤t≤1:
\[
\boxed{X(t)=\left[\frac{t(2-t)}{D(t)}\right]^2,\quad X(0)=0,\quad X(1)=1.}
\]
Because \(X=\sin^2(2\theta)\) and both sine/cosine are nonnegative on the original quarter arc,
\[
\boxed{\frac{dX}{\sqrt{X(1-X)}}=4\,d\theta=K_a(t)\,dt \quad(0<t<1).}\tag{GS7}
\]
The endpoint singularities in X are integrable, and hence
\[
\boxed{\pi=\int_0^1K_a(t)dt
=B(1/2,1/2)=\frac{\Gamma(1/2)\Gamma(1/2)}{\Gamma(1)}.}\tag{GS8}
\]
This is an **explicit rational source-coordinate identity**, not merely matching two numeric values of π. It can be recovered from two perpendicular *positive coordinate axes* in the first quadrant:
\[
\Gamma(1/2)^2=\int_{p,q>0}e^{-(p+q)}(pq)^{-1/2}\,dp\,dq.
\]
Take \(R=p+q,\ X=p/(p+q)\). The Jacobian \(dp\,dq=R\,dR\,dX\) exactly cancels the \(R^{-1}\) from \((pq)^{-1/2}\), leaving \(e^{-R}dR\,dX/\sqrt{X(1-X)}\). The R integral is Γ(1)=1. **This is a precise two-axis Gamma/projective quotient description of the same source angular measure.** It does not mean Gamma physically causes Euclidean π or implies an individual BBP orbit distributes uniformly.

## 6. Failure-mode proof: same forcing, wrong seed

For the unchanged original forcing choose the coherent seed \(s_*=-\pi/16\) (the analytic completion of the BBP source). Then the exact chronological state is \(-T_n\), where
\[
T_n=\sum_{j\ge1}16^{-j}r_o(n+j)>0,\qquad T_n\to0.
\]
This gives a real-circle trajectory tending to one point, not a normal orbit. Yet every formula GS1–GS8, all meromorphic periods, all sphere-rotation conjugacies and all Gamma measures are identical between the authentic U0=0 system and this wrong-seed system. Thus **no argument from these analytic/kinematic identities alone can deduce the original selected Weyl property**. What remains is a literally zero-seeded, integer-carry-aware signed estimate on the authentic chronological sequence.

## 7. Verdict and next falsifier

**Paper-derived within stated classical hypotheses:** GS1–GS8, meromorphic residues, beta source-coordinate identity, exact sphere transport, Gamma non-Haar obstruction. **Numerically / symbolically observed:** the specific finite sanity checks in VALIDATION.md; the tests are not universal proof certificates or an independent external referee. **Refuted:** bare Gamma-carrier/Haar identification, bare sideways rotation/independent π selection. **UNVERIFIED:** new signed arithmetic inequality beyond SUCC #513's Fekete/multiscale gate; selected Weyl decay; base-16 normality of π; priority in literature.

**Next verdict-changing probe:** derive an original-carry-conditioned asymptotic inequality for the *original* selected angular×radial chiral holonomy over sharp temporal blocks. Demand explicit predictions different for U0=0 and s*=-π/16, source taps unmodified, with no substitute Haar averaging. The composed SU(2) sphere lens must be paid for with a transport Jacobian and must not merely rename c_N(h).

## Classical references (not novelty claims)

- NIST DLMF [§5.2 Euler’s Gamma integral](https://dlmf.nist.gov/5.2), [§1.14 Mellin transforms](https://dlmf.nist.gov/1.14), [§5.5 functional/reflection identities](https://dlmf.nist.gov/5.5).
- Cambridge [Riemann sphere and Möbius transformations](https://www.dpmms.cam.ac.uk/~tkc10/complex_2007/Chapter3.pdf); Möbius conjugacy and cross ratios are classical.
- SUCC inherited: draft [#499](https://github.com/femboy2112/SUCC/pull/499), [#509](https://github.com/femboy2112/SUCC/pull/509), [#513](https://github.com/femboy2112/SUCC/pull/513).
