# Virtual gauge × cyclotomic circle × radial high-frequency chirp

**2026-11-04; research-only, add-only child of #502, pinned parent 7e91606f15dc5e4dbf4d9105f5110df3c4b7d6cd.** No modifications to the authentic four signed poles, \(U_0=0\), proof contracts, main, existing tests, formal/Lean, CI, or archives. The pre-existing angular/radial decomposition is #499/#500; #501 is sibling/read-only. This is a paper derivation, **not** a new global normality theorem or verified academic novelty. Hypotheses and early development observations are disclosed in PREREGISTRATION.md.

Conventions: \(e(x)=\exp(2\pi ix)\). \(\zeta=\exp(i\pi/4)\). For a coefficient vector \(w=(w_1,\ldots,w_8)\), define \(P_w(t)=\sum_{j=1}^8w_j t^{j-1}\), \(r_w(n)=\sum_{j=1}^8w_j/[8(n-1)+j]\), and the zero-initialized state \(U^{(w)}_0=0,\ U^{(w)}_n=16U^{(w)}_{n-1}+r_w(n)\). The analytic period is \(\mathcal L(w)=\int_0^1P_w(t)/(1-t^8/16)\,dt=\sum_{n\ge1}16^{-(n-1)}r_w(n)\). Every interchange here is absolutely convergent.

## VG-01: one eight-root carrier contains both quadratics (EXACT)

Put
\[
u=(1+i)/2,\quad a=1/\sqrt2,\quad v_k=u\zeta^k,\quad 0\le k<8.
\]
Then \(|v_k|=2^{-1/2}\), \(v_k^8=1/16\), and
\[
\prod_{k=0}^7(1-v_k t)=1-t^8/16=:D_8(t).
\]
The even \(k\) give rational-coordinate Gaussian points \(u,iu,-u,\bar u\); odd \(k\) give the four points \(\{\pm a,\pm ia\}\) with coordinates in \(\mathbb Q(\sqrt2)\). The common cyclotomic field is \(\mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2)\), a **field**, not the product algebra \(\mathbb Q(\sqrt2)\times\mathbb Q(i)\) used in an earlier separate representation. No representation equivalence to that product is asserted.

For \(|v|<1\), write \(L_v(t)=-\log(1-vt)=\sum_{m\ge1}v^m t^m/m\), principal analytic branch on \(0\le t\le1\). Each \(L_{v_k}(1)\) is an algebraic-coefficient BBP-type series with the exact radix 16:
\[
L_{v_k}(1)=\sum_{m\ge0}16^{-m}\sum_{j=1}^{8}\frac{v_k^j}{8m+j}.
\]
The eight-point discrete Fourier character projector RECOVERS each original denominator lane:
\[
\frac18\sum_{k=0}^{7}\zeta^{-kj}L_{u\zeta^k}(1)
 =u^j\sum_{m\ge0}\frac{16^{-m}}{8m+j},\qquad 1\le j\le8.
\]
Proof: expand the absolutely convergent logarithmic series and use \(\frac18\sum_k\zeta^{k(n-j)}=\mathbf1_{n\equiv j\bmod8}\). This is Fourier resolution of **Taylor coefficients**, not dynamical equidistribution of the **BBP time orbit**.

The Gaussian \(u\) yields the inherited angular source exactly:
\[
K_{\rm ang}(t)=4\,\Im\frac{u}{1-ut}
 =\frac4{(t-1)^2+1}
 =\frac{P_{\rm ang}(t)}{D_8(t)},\quad
w_{\rm ang}=(2,2,1,0,-1/2,-1/2,-1/4,0).
\]
Its period is \(\mathcal L(w_{\rm ang})=4\Im[-\log(1-u)]=\pi\). The four Gaussian quarter-turns give \(\pi,\ 4\arctan(1/3),\ -4\arctan(1/3),\ -\pi\); the other four roots give \(0,\ \pm4\arctan(1/\sqrt2),\ 0\). **They are not eight independent π formulas.** The root rotation and the prime-class \(S_a\) operator below are mathematically different actions.

## VG-02: the radial ghost is a cross-sector norm coboundary (EXACT)

Let \(a=1/\sqrt2,\ u=(1+i)/2\), and \(B(t)=(t-1)^2+1\). The two *different* quadratic norm products obey
\[
(1-a)(1+a)=(1-u)(1-\bar u)=1/2.
\]
Throughout \(0\le t\le1\), define the positive real ratio
\[
F(t)=\frac{(1-at)(1+at)}{(1-ut)(1-\bar u t)}
=\frac{2-t^2}{B(t)}.
\]
The rational analytic function is nonconstant, but \(F(0)=F(1)=1\). Its exact logarithmic differential
\[
K_{\rm rad}(t)=2\frac{d}{dt}\log F(t)
=\frac{P_{\rm rad}(t)}{D_8(t)},\quad
w_{\rm rad}=(2,-2,-1,-2,-1/2,-1/2,1/4,0)
\]
satisfies \(\int_0^1K_{\rm rad}(t)dt=0\). This is a **nonzero exact-boundary null**, not a zero finite state, quantum vacuum, energy debt, or a claim about photon/particle amplitudes. The cross-sector equality of norms is the direct cancellation mechanism.

Indeed \(L_a(1)+L_{-a}(1)=\log2=L_u(1)+L_{\bar u}(1)\); simultaneously \(4\Im L_u(1)=\pi\). Thus the Gaussian phase and the real/Gaussian norm relation are two distinct observations of the SAME eight-root analytic carrier. The general construction of BBP and null BBP formulas from complex logarithms is classical: Barsky, Muñoz & Pérez-Marco, *On the genesis of BBP formulas*, Acta Arith. **198** (2021), 401–426, DOI 10.4064/aa200619-28-9. Neither it nor this local derivation establishes π normality.

## VG-03: an affine π fiber with a **unique** accelerated-source pin (EXACT)

From #499's source-prime projection, put
\[
w_\lambda=w_{\rm ang}+\lambda w_{\rm rad},\qquad
K_\lambda=K_{\rm ang}+\lambda K_{\rm rad}.
\]
For every real \(\lambda\), \(\mathcal L(w_\lambda)=\pi\). For rational \(\lambda\) the taps define a rational BBP-type series. For \(\lambda\in\mathbb Z_{(2)}:=\{a/b\in\mathbb Q:b\text{ odd}\}\), the genuine rational zero-seeded states \(U_n^{(\lambda)}=Y_n+\lambda Z_n\) have odd reduced denominators (since inherited \(Y_n,Z_n\) do). The full original is \(w_1=P=(4,0,0,-2,-1,-1,0,0)\), while \(w_0=w_{\rm ang}\) and \(w_{-1}=P^\sharp/2\), where \(P^\sharp=(0,8,4,4,0,0,-1,0)\).

The #499 Frobenius source action on this EXACT two-dimensional module gives
\[
S_1w_\lambda=S_5w_\lambda=w_\lambda,\qquad
S_3w_\lambda=S_7w_\lambda=-w_{-\lambda}.
\]
This character mirror is **not** an assertion of independent statistical samples.

Critically, \(P_{\rm ang}(1)=15/4\) and \(P_{\rm rad}(1)=-15/4\), so
\[
P_\lambda(1)=\frac{15}{4}(1-\lambda),\qquad
r_\lambda(n)=\frac{15(1-\lambda)}{32n}+O_\lambda(n^{-2}).
\]
This follows directly by the classical endpoint Mellin estimate \(\int_0^1 t^{8(n-1)}P_\lambda(t)dt=P_\lambda(1)/(8n)+O(n^{-2})\). **Within this declared fiber, the original \(\lambda=1\) is the unique \(O(n^{-2})\)-forcing source.** In fact \(r_1(n)=15/(64n^2)+O(n^{-3})\). This source-condition pin is a genuine improvement in structural interpretation, not selection of Haar measure.

A geometric (not dynamically selected) circle follows. Define
\[
\theta_\lambda(t):=\frac14\int_0^tK_\lambda(s)ds
=\arctan(t-1)+\frac\pi4+\frac\lambda2\log F(t),
\quad 0\le t\le1.
\]
Then \(\theta_\lambda(0)=0,\ \theta_\lambda(1)=\pi/4\). Glue eight copies by \(\Theta_\lambda(k+t)=\zeta^k\exp(i\theta_\lambda(t))\) for \(k=0,\ldots,7\): this is a well-defined CONTINUOUS degree-one circle map, with endpoints at the eight roots of unity and total winding 1. The original source \(\lambda=1\) additionally has \(\theta'_1(1)=0\); the gluing is not asserted to be \(C^1\). This topological circle is explicitly CONSTRUCTED and is **not** a conjugacy between the actual BBP shift orbit and uniform circle rotation.

## VG-04: a strong observational redundancy/no-go at FIXED Weyl frequencies (EXACT)

Let \(Y=U^{(w_{\rm ang})}\) and \(Z=U^{(w_{\rm rad})}\). Inherited #497/#499 prove \(0<Z_n<1/(32n+16)\) for all \(n\ge1\) with the literal \(U_0=0\). Thus
\[
\left|\frac1N\sum_{n=1}^N e(h(Y_n+\lambda Z_n))-
\frac1N\sum_{n=1}^N e(h(Y_n+\mu Z_n))\right|
\le\frac{\pi|h||\lambda-\mu|}{16N}H_N
\]
for every fixed integer \(h\) and real \(\lambda,\mu\). Proof: \(|e(x)-e(y)|\le2\pi|x-y|\), then sum \(Z_n<1/(32n)\). Every bounded fixed-parameter π-source in the fiber has precisely the SAME limiting fixed-frequency Weyl behavior. Therefore merely adding more such π formulas does not supply an independent asymptotic signed-cancellation constraint. It is an exact **asymptotic redundancy** theorem.

## VG-05: the radial ghost becomes oscillatory at SUCC's CURRENT superquadratic frequency scale (PAPER PROOF)

This changes when the observed character frequency grows with time. Since \(\mathcal L(w_{\rm rad})=0\), the original zero-seeded finite radial state has the **exact tail representation**
\[
Z_n=-\sum_{m\ge1}16^{-m}r_{\rm rad}(n+m).
\]
For real \(x\ge1\), the same formula defines a smooth source-only extension \(z(x)\). Exact partial-fraction expansion gives
\[
r_{\rm rad}(x)=-\frac{15}{32x}-\frac{53}{256x^2}+O(x^{-3}).
\]
Because \(\sum_{m\ge1}16^{-m}=1/15\) and \(\sum_{m\ge1}m16^{-m}=16/225\), termwise expansion/differentiation (uniformly convergent on \(x\ge A>1\)) yields
\[
z(x)=\frac1{32x}-\frac5{256x^2}+O(x^{-3}),\qquad
z''(x)=\frac1{16x^3}+O(x^{-4}).
\]
Here the differentiated error is justified by the rational partial fractions and exponentially decaying \(m\)-sum; it is not inferred by differentiating an uncontrolled big-O.

Hence for all sufficiently large integer \(A\), any \(H>0\) satisfying \(cA^2\log A\le H\le CA^2\log A\) with fixed \(c,C>0\), \(f(x)=H z(x)\) has \(0<c' H/A^3\le f''(x)\le C'H/A^3\) for all \(A\le x\le2A\). The **classical van der Corput second-derivative exponential-sum estimate** therefore proves
\[
\left|\sum_{A\le n<2A}e(H Z_n)\right|
\ll A\sqrt{H/A^3}+\sqrt{A^3/H}
\ll\sqrt{A\log A}.
\]
In particular
\[
\boxed{\frac1A\sum_{A\le n<2A}e(H Z_n)=O\!\left(\sqrt{\frac{\log A}{A}}\right)}
\quad\text{when }H\asymp A^2\log A.
\]
At any fixed \(h\ne0\), however, \(\frac1A\sum_{A\le n<2A}e(hZ_n)=1+O_h(A^{-1})\). **Same genuine radial field: fixed-frequency coherence, superquadratic-frequency cancellation.** This is a precise, checkable "ephemeral support across observation scales" theorem, with no physics interpretation.

At #501's target \(H=|h|16^{\lfloor\log_{16}(A^2\log A/|h|)\rfloor}\), the hypothesis is met. But the *actual* original phase is
\[
e(HU_n)=e(HY_n)e(HZ_n).
\]
The last radial cancellation DOES NOT give cancellation of this product without a source-coupled estimate. A hostile companion \(Y_n=-Z_n\) would make the product exactly 1; this companion is not an authentic SUCC angular stream. No unconditional improvement to the original signed Weyl/current gate has been proved.

The distinguishing prospective observable is therefore the **mixed angular–radial phase correlation**
\[
\mathcal C_{A,H}(\lambda)=A^{-1}\sum_{A\le n<2A}e(HY_n)e(\lambda HZ_n).
\]
The constant-\(\lambda\) observations coalesce for fixed frequency, but separate at \(H\asymp A^2\log A\). A theorem at the **actual \(\lambda=1\)** must use the signed prime-Frobenius residue information, chronological forcing, and centered real numerators; no character or root-circle symmetry alone imposes it.

## Observations, controls, limitations

- Independent exact Fraction/polynomial tests plus numerical finite holdouts are in \`tests/test_virtual_gauge_circle.py\`. The local isolated suite: **12 tests passed**; it does NOT stand for all >11k native SUCC tests, Lean checks, blind independent review, or hosted CI.
- Before preregistration, exploratory epochs 128,256,512,1024,2048,4096 were used; they are DEVELOPMENT data. The prospectively declared holdouts 307,953,1901 met their finite 0.25 high-frequency / 0.99 fixed-frequency thresholds. These finite observations are **not** proof of the asymptotic claim, which rests on the analytic second-derivative estimate.
- Strict boundary distinctions: the logarithmic null is a **completed period** zero, not the original source's **initial state** zero; the circle of roots is a finite analytic carrier, not an observed Haar time distribution; global novelty is **UNVERIFIED**.
- Older scholarship already explains families of BBP/null formulas. The original π base-16 normality conjecture, selected fixed-h Weyl decay, #501's \(M_A(H)=o(1/\log A)\), and RH all remain **OPEN**.

**Next verdict-changing probe:** use the exact sign/orientation and chronology of the original Y-Z factor pair to bound \(\mathcal C_{A,H}(1)\) on the #501 frequency schedule. Require a falsifier separating true Gaussian angular + original radial from (a) the radial null alone, (b) altered seeds, (c) sparse nonbirth mutants, and (d) the artificial \(Y=-Z\) canceller. Do not treat source-blind high-frequency radial cancellation as mixed-source cancellation.
