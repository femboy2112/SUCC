# OPERATION MÖBIUS MIRROR — projective reciprocal, authentic source rigidity, exact Gamma mirror cocycle

**2026-11-02 · RESEARCH-ONLY PAPER THEOREMS · π normality OPEN.**
Rooted on [PR #475](https://github.com/femboy2112/SUCC/pull/475) at exact parent SHA \`20acb35a42b6ae5fb9260c041ed3a1aa47429484\`, ancestor #474 line/sheet Γ, #473 first-pole/collision, #471 global Fejér, #468 source tail and Main XIX. No existing source, formal kernel, proof contract, workflow, CI or main modified. The question is whether Möbius reciprocal inversion can preserve the ORIGINAL zero-seeded four-pole BBP orbit and force conjugate-pair cancellation.

## MM-01. YES: reciprocal is phase conjugation in a correctly typed projective circle chart

Let \(x\in\mathbb T=\mathbb R/\mathbb Z\). Define the projective stereographic coordinate

\[
\boxed{t(x)=\tan(\pi x-\pi/4)\in\mathbb {RP}^1,\qquad z=e^{2\pi ix}.}
\]

It is well-defined on \(\mathbb T\) because tan has period π; 0 and ∞ are genuine projective endpoints. Elementary trig gives the **exact global involution**

\[
\boxed{t(-x)=1/t(x),\qquad z(-x)=1/z(x)=\overline{z(x)}.}\tag{MM-01}
\]

This is not the ill-typed raw operation \(x\mapsto1/x\bmod1\) on a chosen real representative: for instance \(x=1/2\equiv3/2\pmod1\) but their reciprocals are 0 versus 2/3 mod1. Proper reciprocal lives in the periodized stereographic t carrier, not directly in \(\mathbb R/\mathbb Z\).

A holomorphic Möbius map \(z\mapsto1/z\) of the RIEMANN SPHERE restricts to conjugation on the unit circle; it exchanges the inside/outside of the disk and is **not** a holomorphic disk self-automorphism. Boundary orientation reversal is essential; no type switch is concealed.

Define \(P_{16}(t)=\Im(1+it)^{16}\), \(Q_{16}(t)=\Re(1+it)^{16}\); these are integer polynomials (odd/even binomial terms). Since \(x\mapsto16x\) sends the angular coordinate \(\theta=\pi x-\pi/4\) to \(16\theta-\pi/4\bmod\pi\), its exact real rational projective realization is

\[
\boxed{\mathcal D_{16}(t)=\frac{P_{16}(t)-Q_{16}(t)}{P_{16}(t)+Q_{16}(t)},\qquad
\mathcal D_{16}(1/t)=1/\mathcal D_{16}(t).}\tag{MM-02}
\]

Interpret numerator/denominator zero projectively. This is a degree-16 rational map, NOT a Möbius map itself. Each source addition \(x\mapsto x+u\) is represented by a REAL Möbius transformation

\[
\mathcal R_u(t)=\frac{t+\tan(\pi u)}{1-t\tan(\pi u)},\quad
I(t)=1/t,\quad I\circ\mathcal R_u=\mathcal R_{-u}\circ I.
\]

Thus BBP forcing appears as an exact time-dependent Möbius ROTATION after the degree-16 map, with no invented phase or changed poles.

## MM-02. Complete autonomous sphere-Möbius centralizer and NO selected-orbit conjugate pairs

Let \(D(z)=z^{16}\) on \(\widehat{\mathbb C}\). If a Möbius automorphism \(M\) commutes with D, then M permutes the two critical points \(\{0,\infty\}\). It must therefore be \(az\) or \(a/z\); direct substitution forces \(a^{15}=1\). Therefore

\[
\boxed{\operatorname{Cent}_{\mathrm{PGL}_2(\mathbb C)}(D)
=\{z\mapsto\zeta z,\ z\mapsto\zeta/z:\zeta^{15}=1\}\cong D_{15}}
\tag{MM-03}
\]

of order 30. This is a classical elementary centralizer calculation specialized to radix 16.

For the COMPLETED true π orbit \(z_n=e(16^n\alpha),\ \alpha=\pi/16\), a nontrivial centralizer image cannot equal any selected orbit point: \(\zeta z_n=z_m\) would require \((16^m-16^n)\alpha\equiv a/15\pmod1\), impossible for irrational α except identity at m=n. And \(\zeta/z_n=z_m\) would require \((16^m+16^n)\alpha\equiv a/15\pmod1\), impossible for all n,m. Thus **even the unforced carrier's genuine inversion sends the selected π orbit to a different orbit**. This uses only the classical irrationality of π, not π normality.

The finite group is too weak to force Haar: the uniform measure on 15th roots of unity is invariant under every displayed centralizer map, yet Fourier harmonic h=15 equals 1. Also exact phase NEGATION \(z\mapsto-z\), which would pair opposite phases, fails to commute with \(z^{16}\) because −1 is not a 15th root. Conjugate phases alone sum to \(2\cos\theta\), not zero.

## MM-03. Stronger original-source no-go: no nontrivial Möbius symmetry of the four-pole differential

For the AUTHENTIC rational forcing

\[
r(w)=\frac4{8w-7}-\frac2{8w-4}-\frac1{8w-3}-\frac1{8w-2}
\]

consider the meromorphic differential \(\omega=r(w)\,dw\) on the Riemann sphere. It has exactly four simple poles, at \(7/8,1/2,3/8,1/4\), with residues \(1/2,-1/4,-1/8,-1/8\) respectively. It is regular at ∞ because \(r(w)=O(w^{-2})\).

Suppose Möbius g obeys \(g^*\omega=\omega\). Residue invariance forces it to fix the unique +1/2 pole \(a=7/8\) and unique −1/4 pole \(b=1/2\), possibly interchanging the two equal-residue poles. In the cross-ratio coordinate \(v=(w-a)/(w-b)\), any g fixing a,b acts as \(v\mapsto\lambda v\). The remaining poles have \(v(3/8)=4\), \(v(1/4)=5/2\). To exchange them requires simultaneously \(\lambda=5/8\) and \(\lambda=8/5\), impossible. It therefore fixes all four poles and is the identity:

\[
\boxed{\operatorname{Aut}_{\mathrm{M\ddot ob}}(r(w)\,dw)=\{1\}.}\tag{MM-04}
\]

In particular raw index inversion w→1/w sends original poles to \(\{8/7,2,8/3,4\}\), and cannot preserve the BBP source differential. This theorem is about the **index/source sphere**, not the separate phase-circle projective reciprocal, and does not prohibit nontrivial source–observer transformations carrying additional data.

## MM-04. Forced BBP reflection has an exact source-dependent anomaly

Preserve literally \(U_0=0,\ U_{n+1}=16U_n+r(n+1)\), with original r. Let \(F_n(x)=16x+r(n+1)\pmod1\) and \(J_a(x)=a-x\pmod1\). A direct exact phase computation gives

\[
\boxed{J_aF_n(x)-F_nJ_a(x)\equiv-15a-2r(n+1)\pmod1.}\tag{MM-05}
\]

A fixed J_a commutes with EVERY time step only if \(15a+2r(n+1)\in\mathbb Z\) for all n. Since r(n)→0, this would force 15a integer and then 2r(n) integer for all late n, contradicted by 0<r(n)<1/2 for n≥2 (from source positivity and \(r(n)<4/(8n-7)\)). In unit-circle terms, \(\omega_n=e(r(n+1))\), \(F_n(z)=\omega_n z^{16}\), and inversion sends it to the **negative-forcing** map \(F^-_n(z)=\omega_n^{-1}z^{16}\); it is not an automorphism of the fixed positive-source system.

The instant defect \(|e(2r(n+1))-1|\) is summable because \(r(n)=O(n^{-2})\). Summable source anomalies do NOT imply temporal cancellation: radix growth magnifies errors unless the correct future boundary is restored.

## MM-05. YES, with an exact TIME-DEPENDENT Möbius/Gamma mirror — a two-orbit SUCC morphism

Use the genuine positive original Gamma Green tail \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\), with \(T_{n+1}=16T_n-r(n+1)\) and \(0<T_n\le[(8n+1)(8n+2)]^{-1}\) for n≥1. Set

\[
\boxed{J_n(x)=-x-2T_n\pmod1.}\tag{MM-06}
\]

Then the original source gives the **EXACT** intertwining square

\[
\boxed{J_{n+1}\circ F_n=F_n\circ J_n}\tag{MM-07}
\]

for every n≥0. Each J_n is an orientation-reversing circle Möbius boundary map, or \(t\mapsto\mathcal R_{-2T_n}(1/t)\) in the exact stereographic carrier. Moreover \(\lim_{n\to\infty}J_n(x)=-x\) uniformly on the circle (with circle distance at most 2T_n): the authentic Gamma tail exactly pays the mirror defect.

On the ORIGINAL selected trajectory \(U_n=16^n\alpha-T_n,\ \alpha=\pi/16\),

\[
J_n(U_n)=-16^n\alpha-T_n=U_n+16^n(-2\alpha).
\]

The image is therefore the same original FOUR-POLE FORCING but the changed REAL INITIAL SEED \(-2\alpha=-\pi/8\), not the selected zero seed. The reflect phase differs from its conjugate by \(e(-2hT_n)\). For all fixed h and every late window \(A\le n<B,\ A\ge2\),

\[
\boxed{\sum_{n=A}^{B-1}|e(hJ_n(U_n))-\overline{e(hU_n)}|
\le4\pi|h|\sum_{n\ge A}T_n
\le\frac{\pi|h|}{16(A-1)}.}\tag{MM-08}
\]

Thus the mirrored orbit's chronological Weyl sums are conjugates of original sums up to an absolutely summable source correction, but this DOES NOT prove either sum vanishes.

### Fully FINITE rational mirror with no π digits

For every cutoff B let

\[
\alpha_B=\sum_{j=1}^B16^{-j}r(j)\in\mathbb Q,\quad
R_{n,B}=\sum_{j=n+1}^B16^{n-j}r(j)\in\mathbb Q,\quad
\boxed{J_{n,B}(x)=-x-2R_{n,B}.}
\]

Because \(R_{n+1,B}=16R_{n,B}-r(n+1)\), these are EXACT rational Möbius circle involutions and \(J_{n+1,B}F_n=F_nJ_{n,B}\) for every \(0\le n<B\). They map the selected \(U_n\) to a SAME ORIGINAL FORCING rational-counterseed orbit with \(s_B=-2\alpha_B\), and retain the original integer carry rather than reducing before source gluing.

The inherited Gamma seam \(T_n-R_{n,B}=16^{n-B}T_B\) supplies, for all integer h,

\[
\boxed{\sum_{n=0}^{B}|e(hJ_n(U_n))-e(hJ_{n,B}(U_n))|
\le\frac{64\pi|h|}{15}T_B
\le\frac{64\pi|h|}{15(8B+1)(8B+2)}.}\tag{MM-09}
\]

That is an **all-window O_h(B^-2)** finite/global mirror transport theorem, completely source-exact and rationally computable at finite B. It is not a bound on a Weyl mean.

There is also a UNIQUE zero-initial-seed-preserving moving reflection, \(J_n^{(0)}(x)=2U_n-x\). It fixes EVERY original selected U_n individually, so it is a tautological gauge, NOT an inter-time pairing. This pins precisely where the boundary/seed selection enters.

## MM-06. Two independent mirror axes would force Haar — but GOLDEN second mirror is not source-fixed

For a probability measure μ on the ordinary phase circle, let \(c_h=\int e(hx)\,d\mu(x)\) and \(J_a(x)=a-x\). Its Fourier reflection defect is

\[
\Delta_a(h)=c_h-e(ha)\overline{c_h}.
\]

Two axes a,b satisfy the exact **reconstruction** identity

\[
\boxed{\Delta_a(h)-\Delta_b(h)
=(e(hb)-e(ha))\,\overline{c_h}.}\tag{MM-10}
\]

If \(b-a=\eta=\varphi^{-1}\) is irrational, the denominator is nonzero for every nonzero fixed h. For the golden η, its quadratic algebraic norm gives the explicit badly-approximable bound \(\|h\eta\|\ge1/(3|h|)\): for nearest integer m, \((m-h\eta)(m+h\varphi)=m^2+mh-h^2\in\mathbb Z\setminus\{0\}\) and \(|m+h\varphi|\le3|h|\). Thus

\[
\boxed{|c_h|\le\frac{3|h|}{4}(|\Delta_0(h)|+|\Delta_\eta(h)|),\quad h\ne0.}\tag{MM-11}
\]

This yields a **conditional** Weyl criterion from BOTH mirror discrepancies vanishing. But it is simply an invertible Fourier measurement: deriving the two small defects from BBP is still the unknown signed estimate.

The golden axis also has exact rational FINITE realizations \(\eta_k=F_{k-1}/F_k\). The Fibonacci identity \(|\eta-\eta_k|=\eta^k/F_k<1/F_k^2\) proves for any finite band \(1\le|h|\le H\), if \(F_k\ge3H\), then \(|1-e(h\eta_k)|\ge2/(3|h|)\), an explicitly conditioned finite two-mirror observer.

**Rigorous obstruction:** both FIXED axis reflections commuting with the autonomous radix 16 must have 15a,15b integers; their relative axis is rational, so they cannot generate the required irrational golden rotation. For forced BBP, NO fixed reflection even commutes with all steps (MM-05). One may use moving golden \(J_n^\eta(x)=16^n\eta-x-2T_n\), which EXACTLY intertwines the source, but its axis MOVES each n and it takes the selected orbit to a different real initial seed. Its statistical near-invariance is NOT supplied by Gamma positivity or Fibonacci geometry.

## MM-07. Why infinitely many virtual Möbius sheets can be perfectly Haar but the selected seed still fail

For any odd integer q with \(\gcd(q,16)=1\), consider the source-faithful skew-product carrier \(\mathbb T\times\mathbb Z/q\mathbb Z\) with

\[
\widehat F_n(x,k)=(16x+r(n+1),\,16k\bmod q)
\]

and q original-forcing counterseed orbits \(U_n^{(k)}=U_n+16^n k/q\). The q-fold seed average obeys

\[
\boxed{\frac1q\sum_{k=0}^{q-1}e(hU_n^{(k)})=0\quad\text{whenever }q\nmid h,}
\]

for EVERY time n and EVERY forcing (since 16 is invertible mod q). If q is prime, q∤h and \(\operatorname{ord}_q(16)\ge N\), then for ANY unit-phase sequence \(z_n=e(hU_n)\),

\[
\boxed{\frac1q\sum_{k=0}^{q-1}\left|
\sum_{n=0}^{N-1}z_n e(h16^n k/q)\right|^2=N.}\tag{MM-12}
\]

Proof: average the squared sum over k. Exact finite-character orthogonality kills every off-diagonal term because q∤h(16^n−16^m) for 0≤n<m<N. A suitable prime q always exists for each finite N by choosing it outside the finite set of prime divisors of \(\prod_{j=1}^{N-1}(16^j-1)\).

This gives perfect seed-averaged square-root cancellation at any finite horizon, even when the **selected k=0 Weyl sum is N** (choose z_n=1, a coherent nonnormal control). Therefore more Möbius/rotational sheets, group averaging or exact orbital pairing CANNOT substitute for a source-selected bound. This independently validates the warning in #469/#472 and the current #475 mesoscopic source-specific collision obligation.

## Verdict and discriminating next test

- **DISLOSED/PAPER PROVED** within domains: MM-01–03 circle/projective reciprocity, centralizer, original π orbit disjointness; MM-04 four-pole source differential rigidity; MM-05 exact Γ moving mirror, finite rational sewing and O(B⁻²) phase transport; MM-06 classical two-golden-mirror Fourier reconstruction and noncommuting-axis firewall; MM-07 q-sheet character ensemble no-go.
- **NEGATIVE CONTROLS:** uniform measure on 15th roots is D15-invariant yet non-Haar; same original forcing and completed coherent zero point (\(s=-\alpha\)) is mirror-symmetric about 0 but nonnormal, while its golden second mirror fails; q-sheet ensemble has exact Haar with coherently selected k=0; source differential has no Möbius index reflection.
- **UNVERIFIED:** selected original BBP source has asymptotically small golden second-mirror discrepancy, or the mesoscopic collision bound \(E_{A,\beta}=o(\log A)\) from #475. No existing theorem implies either premise. Base-16 π normality, RH, or a physical conformal causality claim remain OPEN.

**Next source-selected lamp:** use the finite rational mirror charts to transport exact signed cross-terms into #475's mesoscopic two-sided Fejér energy. Predict a discrepancy that must DIFFER between original zero-seed and both coherent and q-sheet-averaged controls; if it reduces to a renamed \(S_N(h)\), record it as gate-equivalent rather than claiming cancellation.
