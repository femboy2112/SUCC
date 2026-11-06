# AV: authentic BBP lag alias valve, source flux and finite escape

**Date:** 2026-11-04. **Status:** rigorous paper derivations with exact-rational focused tests; no new Lean declaration, no claim of independent human refereeing. **Base:** merged main a673ec95dfac4ef6a61c60222be8b615fd08535d. **Immutable original source:**

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},\quad
U_0=0,\ U_n=16U_{n-1}+r(n).
\]

All asserted recurrences for changed seeds are identified as countermodels, not the original selected phase. Set \(x_n=\{U_n\}\), \( \|z\|=\min_{k\in\mathbb Z}|z-k|\) and \(k_q(z)=(1-q\|z\|)_+\), \(q\ge2\) an integer. No claims about real fluid mechanics, physical quantum amplitudes, RH, or base-16 normality are made.

## AV-01: source-oriented lag shear (proved)

The source has the exact positive Mellin density
\[
r(n)=\int_0^1t^{8n-8}P(t)\,dt,\qquad
P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2).
\]
For \(n,d\ge1\) and the unwrapped source lag \(D_{n,d}=U_{n+d}-U_n\), subtract the same recurrence at times \(n+d+1\) and \(n+1\):
\[
D_{n+1,d}=16D_{n,d}-\sigma_{n,d},\quad
\sigma_{n,d}=r(n+1)-r(n+d+1)
=\int_0^1t^{8n}(1-t^{8d})P(t)\,dt.
\]
The same equality holds on \(\mathbb R/\mathbb Z\) for \(\delta_{n,d}=\{D_{n,d}\}\). Since \(0<P(t)\le15(1-t)\) for \(0<t<1\) and \(0<1-t^{8d}\le8d(1-t)\),
\[
\boxed{0<\sigma_{n,d}<
120d\int_0^1t^{8n}(1-t)^2dt
=\frac{240d}{(8n+1)(8n+2)(8n+3)}.}\tag{AV-1}
\]
For fixed \(d\), the upper bound is \(O(dn^{-3})\). This sign is an actual source property; the induced *net* collision flux has no predetermined sign.

## AV-02: the 16-pocket alias partition (exact, source-independent)

Define central outward leakage and lateral reinjection:
\[
L_q(z)=k_q(z)-k_{16q}(z)\ge0,\qquad
I_q(z)=\sum_{j=1}^{15}k_{16q}(z-j/16)\ge0.
\]
The preimages of the radius-\(1/q\) tent under multiplication by sixteen form sixteen disjoint narrow tents. Consequently, pointwise for every real \(z\),
\[
\boxed{k_q(16z)=k_{16q}(z)+I_q(z),\qquad
k_q(16z)-k_q(z)=I_q(z)-L_q(z).}\tag{AV-2}
\]
The support-boundary cases hold because \(q\ge2\) and the tent is zero at its endpoints. This is algebra of the circle map, not dissipative dynamics.

## AV-03: exact signed chronological valve and quantitative source bound (proved)

Fix integer \(A\ge2\). For lag \(1\le d<A\), put \(b_d=2A-d-1\), and take transitions \(n=A,\ldots,b_d-1\); all points \(n,n+d,n+1,n+d+1\) are within the original epoch \([A,2A)\). Define
\[
F_{n,d,q}=k_q(16\delta_{n,d}-\sigma_{n,d})-k_q(16\delta_{n,d}),\qquad
|F_{n,d,q}|\le q\sigma_{n,d}.
\]
The Lipschitz bound holds globally on the circle, including tent endpoints. Inserting AV-1/2 into the chronological identity and telescoping,
\[
\boxed{\sum_{n=A}^{b_d-1}(L_q-I_q)(\delta_{n,d})
=k_q(\delta_{A,d})-k_q(\delta_{b_d,d})
+\sum_{n=A}^{b_d-1}F_{n,d,q}.}\tag{AV-3}
\]

The true source is strictly decreasing. Thus the positive shear telescopes:
\[
0\le \sum_{n=A}^{b_d-1}\sigma_{n,d}
=\sum_{j=1}^{d}r(A+j)-\sum_{j=1}^{d}r(b_d+j)
\le\sum_{j=1}^d r(A+j)
<\frac{15d}{(8A+1)(8A+2)}.
\]
The last inequality is from the original \(r(j)<15/((8j-7)(8j-6))\). Summing lags gives the useful finite original-source estimate
\[
\boxed{\sum_{d=1}^{A-1}\sum_{n=A}^{b_d-1}\sigma_{n,d}
<\frac{15A(A-1)}{2(8A+1)(8A+2)}.}\tag{AV-4}
\]
The \(A-1\) boundary differences in AV-3 each have absolute value at most one. Therefore
\[
\boxed{\left|\frac q{A^2}\sum_{d=1}^{A-1}\sum_{n=A}^{b_d-1}
(L_q-I_q)(\delta_{n,d})\right|
\le \frac{q(A-1)}{A^2}
+\frac{15q^2(A-1)}{2A(8A+1)(8A+2)}.}\tag{AV-5}
\]
For \(q=O(\log A)\), this is \(O(q/A+q^2/A^2)=o(1)\). The bound holds for the original zero seed and for **every changed seed with the same forcing**. It proves that the *net* nonnegative outflow and lateral reinjection almost balance after normalization. It does **not** bound either large positive flow separately, and cannot imply \(J_{A,q}=o(K_A)\). Exact source flux can have either sign; the finite receipts show both.

The signed source term is not thrown away:
\[
F_{n,d,q}
=q\int_0^{\sigma_{n,d}}
\left(\mathbf1_{(0,1/q)}(\{16\delta_{n,d}-t\})-
\mathbf1_{(1-1/q,1)}(\{16\delta_{n,d}-t\})\right)dt.
\]
Thus the prospective sign-sensitive discriminator is the **actual relative occupancy of the two oriented boundary arcs**, together with the cofactor/seed information, not merely positive shear.

## AV-04: every *distinct rational pair* eventually escapes, with a finite exact residue (proved)

For every real \(z\) and integer \(L\ge0\),
\[
\boxed{k_q(z)=\sum_{j=0}^{L-1}L_{16^jq}(z)+k_{16^Lq}(z).}\tag{AV-6}
\]
This is the exact finite first-passage/release decomposition; every summand is nonnegative. If \(z\in\mathbb Q/\mathbb Z\) has denominator dividing \(D\), then for nonzero \(z\) its circle distance is at least \(1/D\). Hence \(k_{16^Lq}(z)=0\) when \(16^Lq\ge D\). For \(z=0\) it remains 1 at every depth.

Every genuine original \(U_n\) is rational with **odd** denominator, because the original collapsed forcing denominator is odd and the recurrence multiplies by 16. Let \(D_A\) be the least common multiple of denominators of the genuine phases \(x_n\), \(A\le n<2A\), let \(R_A=\#\{(n,t):x_n=x_t\}\), and choose the finite depth \(L_A=\min\{L:16^Lq\ge D_A\}\). Then
\[
\boxed{J_{A,q}=\frac q{A^2}\sum_{n,t=A}^{2A-1}
\sum_{j=0}^{L_A-1}L_{16^jq}(x_n-x_t)
+\frac{qR_A}{A^2}.}\tag{AV-7}
\]
This is exact for each finite epoch, with no π digits or limit assumptions. It says the *nonidentical* pairs eventually leave the nested zero pocket at some realizable finite resolution. It does **not** establish a useful bound on the distribution of their escape depths: the necessary \(L_A\) may be of order \(A\) or greater, whereas the normality route examines \(K_A\asymp\log\log A\). Neither rationality nor finite evacuation establishes any \(o(K_A)\) bound on \(J_{A,q_A}\).

This is a literal mathematical version of “eventually releases in finite chunks,” and an exact statement of why the word **eventually** alone is insufficient.

## AV-05: same forcing + odd denominators + finite coherent wrong seed (proved countermodel)

For every integer \(A\ge2\), take \(M=2A\), \(\alpha_M=\sum_{j=1}^{M}16^{-j}r(j)\), and choose the odd integer
\[
Q_A=512A^2 16^M+1,\qquad
s_A=\frac{\operatorname{nearest\_integer}(-Q_A\alpha_M)}{Q_A}.
\]
Then \(|s_A+\alpha_M|\le1/(2Q_A)\). The trajectory
\(V_0=s_A,\ V_n=16V_{n-1}+r(n)\)
has **the same four-pole source** and every state has odd reduced denominator, yet \(s_A\ne0\) and this seed depends on \(A\).

For \(A\le n<2A\), let \(R_{n,M}=\sum_{j=n+1}^{M}16^{n-j}r(j)\). Exact unwrapped algebra gives
\[
V_n=16^n(s_A+\alpha_M)-R_{n,M}.
\]
The positive source bound and the geometric weights imply
\(0<R_{n,M}<1/[(8n+1)(8n+2)]<1/(64A^2)\).
The seed approximation contributes less than \(1/(1024A^2)\). Thus the entire selected epoch lies on one short real arc, with width
\[
\boxed{\operatorname{width}\{V_n:A\le n<2A\}<\frac9{512A^2}.}\tag{AV-8}
\]
For \(2\le q\le512A^2/9\), every ordered pair satisfies a lower tent bound, giving
\[
\boxed{J_{A,q}(V)\ge q\left(1-\frac{9q}{512A^2}\right).}\tag{AV-9}
\]
For the logarithmic target \(q_A\asymp\log A\), this wrong-seed family has \(J_{A,q_A}\sim q_A\), **not** \(o(K_A)\), even though AV-1..AV-5 and odd-denominator arithmetic all hold. This is an epoch-dependent family, NOT a fixed wrong seed and NOT a counterexample to π-normality.

The previously documented fixed real counterseed \(s_*=-\pi/16\) instead gives \(V_n=-T_n\), so its completed orbit is the nonnormal fixed point zero and its epoch energies are similarly maximal. That comparison uses the genuine Green-tail theorem; the executable finite family above uses rational arithmetic only. Both identify the literal \(U_0=0\) anchor as indispensable.

## AV-06: what a useful valve theorem must now prove (OPEN)

For the target \(K_A=\lfloor\log_{16}\log A\rfloor\), \(m_A=16^{K_A}\), \(q_A=m_A/2\) on sufficiently large dyadic \(A\), inherited SUCC proves that \(J_{A,q_A}=o(K_A)\) would imply base-16 normality.

AV-2/3 show **incoming pocket mass almost balances outgoing leakage**, not a net dissipative spectral gap. AV-7 shows **finite release**, not early release or bounded total mass. The missing source-selected estimate is an upper bound on the sum of releases **and** the unresolved residual at a usable scale, equivalently some genuine new control on the original real near-pair concentration. Local prime clocks, the original odd cofactor, integer carries and \(U_0=0\) must determine the missing escape-depth distribution. No such theorem is proved here.

**Claim classification:** AV-01..05 are paper-proved elementary/source-scoped identities and an exact rational hostile family; the project’s arithmetic lag-dispersion saving is UNVERIFIED. Base-16 π normality and RH remain OPEN. No originality priority or new Lean-kernel authority is claimed.
