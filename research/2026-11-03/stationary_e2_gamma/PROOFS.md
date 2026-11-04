# OPERATION STATIONARY E² — exact original BBP receiver, Gamma cohomology and its invariant-measure boundary

**2026-11-03 · RESEARCH-ONLY PAPER DERIVATIONS.** Exact parent draft PR #478 at SHA 16e4d36369822e669f214b455481c25a93ba294c. Historical, already-main E-tower source: research/2026-10-27/BBP_RANK_TWO_CHIRAL_E_TOWERS.md and observational_succ/rank_two_chiral_towers.py (rank-two Gaussian), as well as original A/B-to-E receipt and descent PRs #26, #27, #28, and no-ghost #61. Ancestors of #478 include #477 Möbius, #475 mesoscopic and #474 line/sheet Gamma. PR #479 is a READ-ONLY sibling, not secretly imported. All ORIGINAL four signed poles and literal U₀=0 preserved; π base-16 normality remains OPEN.

## SE-01. A four-rational-dimensional source engine already exists, and its gain IS the one-step Gamma Fourier gain

The original E² carrier is K²=Q(i)⊕Q(i), rational dimension four, with chiral involution J and Q-linear source-successor T. In rational even/odd bases,

G=(1/2)[[1,-1],[1,1]], H=[[0,1],[1/2,0]], T=diag(G,H), J=diag(I₂,-I₂).

For the fixed input b=(1,0,1,0) and readout l=(4,0,0,-4),

\[
\boxed{T^4=-J/4,\quad T^8=I/16,\quad c_m=l(T^m b).}
\]

The first eight c_m are (4,0,0,−2,−1,−1,0,0), followed by c_{8k+j}=16^{-k}c_j. This is inherited E² source math, not a newly invented source or independent proof.

The rotating even block multiplies by g=(1+i)/2. The normalized Gamma(shape=1,rate=1) characteristic function at angular frequency ω=1 is, CLASSICALLY,

\[
\boxed{\mathbb E(e^{iX})=\int_0^\infty e^{-t}e^{it}dt
=\frac1{1-i}=\frac{1+i}{2}=g.}\tag{SE-01}
\]

Thus the E² 45° gain is IDENTICALLY the one-step Gamma Fourier multiplier. Eight steps rotate through 2π and contract by 1/16: g^8=1/16. The odd chiral sector is the conjugation-twisted map H(z)=g \bar z and H²=1/2; it shares the eighth return but not the same internal history. This exact scalar match does not imply the Gamma distribution is the deterministic law of π's digits.

## SE-02. Exact Mellin/Beta coupling of both E² lanes to the IMMUTABLE four poles

Split the original first-shell taps into

c⁺=(4,2,0,−1,−1,−1/2,0,1/4),
c⁻=(0,−2,0,−1,0,−1/2,0,−1/4).

Define their time-INDEPENDENT rational field readouts on the FIXED compact clock q∈[0,1]:

\[
\mathcal R_\pm(q)=\sum_{j=0}^7c_j^\pm\frac{q}{8+(j-7)q},\quad
\mathcal R(q)=\mathcal R_+(q)+\mathcal R_-(q).
\tag{SE-02}
\]

Because the original total shell is (4,0,0,−2,−1,−1,0,0),

\[
\boxed{\mathcal R(q)=\frac{4q}{8-7q}-\frac{2q}{8-4q}
-\frac{q}{8-3q}-\frac{q}{8-2q}.}\tag{SE-03}
\]

For the exact clock q_n=1/(n+1), \(\mathcal R(q_n)=r(n+1)\), where

r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2), U₀=0, U_{n+1}=16U_n+r(n+1).

No π digit stream or changed source enters this identity. The Mellin weight
\(1/(m+1)=\int_0^1t^m dt=B(m+1,1)=\Gamma(m+1)\Gamma(1)/\Gamma(m+2)\)
is exactly the Gamma-to-factorial finite/continuum interface proposed by the user.

The old E² complete first-shell generating function is
\[
F(t)=l(I-tT)^{-1}b=\frac{P(t)}{1-t^8/16}
=\frac{4(1-t)}{(1-t+t^2/2)(1-t^2/2)},\quad
P(t)=4-2t^3-t^4-t^5.
\]

For every B≥0 the ORIGINAL zero-seed BBP rational completion has a STRICTLY STATIC fixed-matrix integral representation

\[
\boxed{
\alpha_B=\sum_{n=1}^B16^{-n}r(n)
=\frac1{16}\sum_{m=0}^{8B-1}\frac{lT^m b}{m+1}
=\frac1{16}\int_0^1 l(I-(tT)^{8B})(I-tT)^{-1}b\,dt.
}\tag{SE-04}
\]

Here \((tT)^{8B}=16^{-B}t^{8B}I\). For B→∞, inherited classical BBP exact source integration yields \(\alpha=\pi/16\). Equation SE-04 supplies a finite rational static E² receiver for each B, with no moving external operator. It does NOT imply π normality.

## SE-03. Both E² channels are necessary: opposite first-order updates cancel source-specifically

By the exact first-shell mass and moment constraints
\[
\sum_j c_j^+=15/4,\quad \sum_j c_j^-=-15/4,\quad
\sum_j c_j=0,\quad \sum_j j c_j=-15,
\]
expanding the rational readouts at q=0 gives

\[
\boxed{
\mathcal R_+(q)=\frac{15}{32}q+\frac12q^2+O(q^3),\quad
\mathcal R_-(q)=-\frac{15}{32}q-\frac{17}{64}q^2+O(q^3),
}
\]
\[
\boxed{\mathcal R(q)=\frac{15}{64}q^2+\frac{151}{512}q^3+O(q^4).}
\tag{SE-05}
\]

These are exact Taylor coefficients for the original rational source, not fitted numerics. The paired source is positive and quadratic at the zero boundary. Indeed P(t)=(1-t)(t²+2)(t²+2t+2)>0 on 0<t<1, and P(t)≤15(1-t). For any 0<q≤1, set s=1/q. The original Mellin identity gives
\[
\mathcal R(q)=\int_0^1 t^{8/q-8}P(t)\,dt,
\quad
0<\mathcal R(q)\le\frac{15q^2}{(8-7q)(8-6q)}
\le\frac{15}{2}q^2.
\tag{SE-06}
\]

Removing the odd source lane changes the update to O(q), destroys the exact four-pole passport, and violates the zero-boundary cancellation.

## SE-04. The requested time-HOMOGENEOUS stationary E receiver is an exact rational finite model

Encode the clock internally rather than storing an externally advancing n:

\[
\boxed{g(q)=\frac{q}{1+q},\quad g^n(q)=\frac{q}{1+nq},\quad q_0=1.}\tag{SE-07}
\]

E holds one fixed tuple (q,p,a⁺,a⁻) of rational registers, initialized to (1,1,0,0). The two common-source chiral lanes deliver verified receipts \(\mathcal R_\pm(q)\). In ONE epistemic macro-update E applies the TIME-INDEPENDENT map

\[
\boxed{
q'=g(q),\qquad p'=p/16,\qquad
(a^\pm)'=a^\pm+\frac{p}{16}\mathcal R_\pm(q).
}\tag{SE-08}
\]

By induction, after n updates,
\[
q_n=1/(n+1),\ p_n=16^{-n},\
a_n^++a_n^-=\alpha_n=\sum_{j=1}^n16^{-j}r(j),\
U_n=\alpha_n/p_n.
\]

This is a fixed DIMENSION receiver and its internal formula never depends explicitly on the index n. It is NOT constant-bit memory: exact rational denominator heights and output precision increase unboundedly as n increases. The two lanes have a genuine COMMON source; accepting each lane alone cannot invent a joint state (historical SUCC #28/#61). The accompanying code checks labels, exact clock alignment and both values; labels are mathematical provenance tags, not cryptographic attestation.

## SE-05. Intrinsic Gamma future gives a UNIQUE, bounded source-correcting stationary field

Define for q∈[0,1] the genuine source-completed Gamma corrector

\[
\boxed{\tau(q)=\sum_{j=1}^\infty16^{-j}\mathcal R(g^{j-1}(q)),
\qquad\tau_B(q)=\sum_{j=1}^{B}16^{-j}\mathcal R(g^{j-1}(q)).}\tag{SE-09}
\]

By SE-06 the series converges uniformly, 0≤τ(q)≤q²/2, and τ(0)=0. It satisfies the EXACT cohomological/coboundary law

\[
\boxed{16\tau(q)-\tau(g(q))=\mathcal R(q).}\tag{SE-10}
\]

It is the UNIQUE BOUNDED solution of this equation: if δ is the difference of two bounded solutions, δ(g^nq)=16^nδ(q), and boundedness forces δ(q)=0.

The two chiral correctors obey the same equation individually, with leading terms

\[
\boxed{\tau_+(q)=q/32+O(q^2),\quad
\tau_-(q)=-q/32+O(q^2),\quad
\tau(q)=q^2/64+O(q^3).}\tag{SE-11}
\]

Thus the original E² even/odd cancellation eliminates the entire O(q) stationary field. Along q_n=1/(n+1), τ(q_n) is EXACTLY the original positive BBP Gamma Green tail T_n, not a fitted approximation.

For every finite B and rational q,

\[
\boxed{\tau(q)-\tau_B(q)=16^{-B}\tau(g^Bq),\quad
0\le\tau(q)-\tau_B(q)
\le\frac{q^2}{2(1+Bq)^2\,16^B}.}\tag{SE-12}
\]

The finite corrected moving equation has the exact, source-selected defect

\[
\boxed{\mathcal R(q)+\tau_B(gq)-16\tau_B(q)
=16^{-B}\mathcal R(g^Bq).}\tag{SE-13}
\]

Every finite receiver calculation remains rational and its residual is explicitly controlled. For integer n≤B this recovers the inherited #468 finite seam \(U_n+\tau_{B-n}(q_n)=16^n\alpha_B\).

## SE-06. Conjugacy: the moving forced BBP system IS a static Koopman carrier, but this does NOT select Haar

Define on \(X=\mathbb T\times[0,1]\) the TIME-HOMOGENEOUS skew product

\[
S(x,q)=(16x+\mathcal R(q)\bmod1,g(q)),\quad
S_0(y,q)=(16y\bmod1,g(q)).
\]

For the exact field section define \(H(x,q)=(x+\tau(q)\bmod1,q)\). This is a continuous invertible fiber rotation with inverse (y−τ(q),q). The source coboundary yields the EXACT COMMUTING SQUARE

\[
\boxed{H\circ S=S_0\circ H.}\tag{SE-14}
\]

Original \(S^n(0,1)\) has first coordinate \(\{U_n\}\); the completed coordinate is \(\{16^n\alpha\}\), α=τ(1)=π/16. This is a rigorous realization of a stationary observer retaining finite field updates while the selected physical phase keeps moving. No new source/seed is inserted.

Let K be the time-independent Koopman operator on continuous circle/clock observables, Kf=f∘S. For the selected source character χ_h(x,q)=e(hx), \(e(t)=\exp(2πit)\),

\[
\boxed{K\chi_h(x,q)=e(h\mathcal R(q))\,\chi_{16h}(x,q).}\tag{SE-15}
\]

The moving index has been absorbed into a fixed operator and its exact source multiplier. In the completed Gamma frame Ψ_h(x,q)=e(h(x+τ(q))), the multiplier trivializes:

\[
\boxed{K\Psi_h=\Psi_{16h}.}\tag{SE-16}
\]

THIS IS NOT FOURIER DECAY. The frequency still shifts internally by ×16, and |Ψ_h|=1; no norm contraction or selected Weyl estimate follows. The original source target remains the marked-state Cesàro average
\[
\frac1N\sum_{n=0}^{N-1}(K^n\chi_h)(0,1)
=\frac1N\sum_{n=0}^{N-1}e(hU_n)\stackrel{?}{\longrightarrow}0.
\tag{OPEN-SELECTED-WEYL}
\]

**Complete invariant-measure theorem.** Every S-invariant Borel probability measure is supported on q=0: invariance implies
\[
0=\int(q-g(q))d\mu=\int\frac{q^2}{1+q}d\mu
\quad\Longrightarrow\quad\mu(q=0)=1.
\]
On that boundary \(\mathcal R(0)=0\), and S reduces to ×16, so

\[
\boxed{\operatorname{InvProb}(S)
=\{\nu\otimes\delta_0: \nu\in\operatorname{InvProb}(x\mapsto16x\bmod1)\}.}\tag{SE-17}
\]

This is an exact classification of stationary FIELD states, NOT a classification of which subsequential limit is selected from the marked (0,1) orbit. Non-Haar examples are δ₀ and δ_{1/5}, because 16/5≡1/5 mod1. The source's Gamma corrector uniquely chooses the OBSERVATION GAUGE, not the limiting PHASE MEASURE. A same-four-pole coherent changed initial seed x₀=1/5−α has precisely that non-Haar completed trajectory, while satisfying all SE-01–16 source formulas.

## SE-07. Auxiliary Gamma tangent can be stationarized exactly in Q(i), but its Fourier modulus DOES NOT vanish

The source Mellin transformation is

\[
r(n)=\int_0^\infty e^{-nu}K_{\rm BBP}(u)\,du,\quad
K_{\rm BBP}(u)=\tfrac18e^{7u/8}P(e^{-u/8})>0.
\]

Near u=0, \(K_{\rm BBP}(u)=15u/64+O(u^2)\). Thus the normalized positive **AUXILIARY** probability density
\[
p_n(u)=e^{-nu}K_{\rm BBP}(u)/r(n)
\]
has a Gamma(shape 2,rate n) tangent model. Its exact Fourier multiplier for any real ω is
\[
m_n(\omega)=r(n-i\omega)/r(n),\quad
g_n(\omega)=(1-i\omega/n)^{-2},\quad
\boxed{c_n(\omega)=m_n(\omega)/g_n(\omega).}
\tag{SE-18}
\]

The genuine rational source Laurent expansion \(r(z)=15/(64z^2)+151/(512z^3)+O(z^{-4})\) implies \(c_n(\omega)=1+O_\omega(n^{-2})\). Since r(z) has numerator roots \((89\pm\sqrt{241})/240<1\) and all denominator poles <1, no \(c_n(\omega)\) is zero for n≥1 and real ω. Therefore the SOURCE-SPECIFIC stationary corrected field product

\[
\boxed{Z_N(\omega)=\prod_{n=1}^{N}c_n(\omega)
\longrightarrow Z_\infty(\omega)\ne0.}\tag{SE-19}
\]

The FINITE update is exactly Gaussian-rational when ω∈Q, and can be written as one time-independent observer on (q,z):
\(q'=q/(1+q),\ z'=z\,\big[r(1/q-i\omega)/r(1/q)\big](1-i\omega q)^2\).

This is the requested mathematically coherent *stationary field receiver*. But multiplying back the Gamma(shape2,rate n) tangent factors yields
\[
\boxed{
\lim_{N\to\infty}\left|\prod_{n=1}^{N}m_n(\omega)\right|
=|Z_\infty(\omega)|\,
\frac{\pi|\omega|}{\sinh(\pi|\omega|)}>0
}\tag{SE-20}
\]
(with ratio 1 at ω=0), by the classical Euler sinh product. So the source-derived positive Gamma increments do not select Haar through repeated convolution. THIS PRODUCT IS NOT the chronological π Weyl product or sum; it is an auxiliary positive Mellin observer. The signed selected BBP phase remains the missing test.

An alternative exact Gamma quotient for the N-factor source product is obtained from the roots \(a_\pm=(89\pm\sqrt{241})/240\) and poles \(b\in\{1/2,1/4,7/8,3/8\}\):
\[
\prod_{n=1}^{N}m_n(\omega)
=N^{2i\omega}(C(\omega)+O_\omega(N^{-1})),\quad
C(\omega)=
\prod_{a=a_\pm}\frac{\Gamma(1-a)}{\Gamma(1-a-i\omega)}
\prod_b\frac{\Gamma(1-b-i\omega)}{\Gamma(1-b)}\ne0.
\tag{SE-21}
\]
This recovery is a classical Gamma product specialized to the ORIGINAL numerator and four signed poles; no claim of new special-function priority.

## Verdict and next genuinely distinguishing instrument

**PAPER PROVED in stated mathematical domains:** exact rank-two E²/Gamma frequency-1 gain identification; autonomous compact q observer; immutable zero-seeded finite α_B and four-pole recovery; E² opposite chiral cancellation to quadratic field; unique bounded Gamma source section and rational finite error; exact source-to-product dynamical conjugacy and full invariant-probability classification; auxiliary rational-Gaussian Gamma tangent limit with nonzero magnitude.

**OBSERVED (finite):** pure Fraction local standard-library tests check all E² taps, zero-seed matching, 0/8 return, rational finite seams, receipt mutations and Gaussian field products; independently executed symbolic source Taylor identities and mpmath finite convergence checks.

**REFUTED:** (i) stationarity of the receiver or existence of a unique Gamma section implies Haar; δ_{1/5} on the compact boundary is a decisive coherent non-Haar witness. (ii) positive normalized Gamma source convolution alone forces nonzero Fourier modes to vanish; SE-20 provides the opposing exact nonzero limit.

**UNVERIFIED:** any NEW source-selected signed original Weyl or mesoscopic real collision inequality. The exact conjugacy transports rather than proves that estimate. Base-16 normality of π and RH remain OPEN. A source-successful next probe must distinguish the literal x₀=0 orbit from the same-four-pole coherent x₀=1/5−α orbit, preferably by proving an unbounded sequence of real BBP chiral-sector signed losses in the marked Koopman receiver. If it just restates the selected Weyl sum as K-powers, it is a pathway repair, not a new cancellation result.

Relevant classical antecedents: NIST DLMF §5.2 Euler Gamma integral, §5.9 Gamma/Beta integral, §5.11 Gamma ratio asymptotics; classical compact skew products and invariant measures; old SUCC E² dossier and #26/#27 E-source receipt methodology. No formal Lean certificate or external independent mathematics referee claimed.
