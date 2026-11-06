# Source-jet reconstruction from the zero-period radial field: an all-order BBP observer-transport theorem

**2026-11-04, research-only, additive continuation of draft #506.** This statement was derived interactively **after** the original chronological preregistration; do not reclassify it as blind. Base #504 pinned \`f3327bdce023fe3f68d4c5431b5a7c2b53dac2ed\`. Authentic four signed BBP source taps \`P=(4,0,0,-2,-1,-1,0,0)\`, literal \(U_0=0\), radial \(Z_0=0\), and all source/contracts remain unchanged. No claim of π normality or worldwide priority.

## SJ-01: the original \(n^{-2}\) forcing is the radial repayment *rate* (paper exact)

Use genuine BBP forcing \(r_o(x)\) and radial future-tail extension \(z(x)\):
\[
r_o(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2},
\quad
z(x)=-\sum_{m\ge1}16^{-m}r_r(x+m),\quad z(n)=Z_n,
\]
where \(r_r(x)=\sum_{j=1}^8w_{r,j}/[8(x-1)+j]\) with \(w_r=(2,-2,-1,-2,-1/2,-1/2,1/4,0)\).

Exact rational Laurent expansion of these *literal* source rational functions gives
\[
\begin{aligned}
r_o(x)&=\frac{15}{64x^2}+\frac{151}{512x^3}
       +\frac{1209}{4096x^4}+O(x^{-5}),\\
z(x)&=\frac1{32x}-\frac5{256x^2}+\frac{27}{2048x^3}
       -\frac{209}{16384x^4}+O(x^{-5}).
\end{aligned}
\]
All higher coefficients are rational and the expansion has controlled differentiated remainders. For each fixed signed lag \(\ell\), \(d_\ell(x)=z(x+\ell)-z(x)\) has
\[
d_1(x)=-\frac1{32x^2}+\frac9{128x^3}-\frac{265}{2048x^4}+O(x^{-5}),
\quad
d_2(x)=-\frac1{16x^2}+\frac{13}{64x^3}-\frac{577}{1024x^4}+O(x^{-5}).
\]
Hence the exact **leading source/observer-current bridge** is
\[
\boxed{r_o(n)+\frac{15}{2}(Z_{n+1}-Z_n)
       =\frac{421}{512n^3}+O(n^{-4}).} \tag{SJ1}
\]
The original accelerated four-pole forcing is asymptotically \(15/2\) times the **outflow rate** \(-d_1\) of its endogenous zero-period radial field. The coefficient \(15=16-1\) is inherited from the genuine base-16 source clock; no π digit was inserted.

## SJ-02: two delays synchronise an additional entire source jet

Seek \(a,b\in\mathbb Q\) such that \(r_o(n)+a d_1(n)+b d_2(n)\) vanishes through \(n^{-3}\). Coefficient matching gives
\[
15-2a-4b=0,\qquad 151+36a+104b=0.
\]
The unique exact solution is \(a=541/16,\ b=-421/32\), yielding
\[
\boxed{r_o(n)+\frac{541}{16}(Z_{n+1}-Z_n)
                   -\frac{421}{32}(Z_{n+2}-Z_n)
       =\frac{13653}{4096n^4}+O(n^{-5}).} \tag{SJ2}
\]
A three-lag sample recovers one further jet:
\[
(a_1,a_2,a_3)=\frac1{256}(22309,-17021,4551),\qquad
r_o(n)+\sum_{\ell=1}^3a_\ell d_\ell(n)
 =\frac{537369}{32768n^5}+O(n^{-6}).
\]
These coefficients were independently computed from exact rational original taps and the exponentially weighted radial tail; finite Fraction probes are calibration, not the source of their derivation.

## SJ-03: theorem for ANY fixed number m of delays (paper proof)

For **each fixed integer \(m\ge1\)** there is a UNIQUE vector \((a_1^{(m)},\ldots,a_m^{(m)})\in\mathbb Q^m\) such that
\[
\boxed{r_o(n)+\sum_{\ell=1}^m a_\ell^{(m)}(Z_{n+\ell}-Z_n)
=O_m(n^{-(m+2)})\qquad(n\to\infty).} \tag{SJ3}
\]
Proof: write \(z(x)\sim\sum_{k\ge1}z_kx^{-k}\), \(z_1=1/32\ne0\); and \(r_o(x)\sim\sum_{k\ge2}c_k x^{-k}\). Each \(z_k,c_k\in\mathbb Q\): the rational source's Laurent series and the moments \(\sum_{j\ge1}j^r16^{-j}\in\mathbb Q\) for every fixed r ensure this. The coefficient of \(x^{-(j+1)}\) in \(d_\ell(x)\) is a polynomial \(p_j(\ell)\) of degree \(j\) with **zero constant** and nonzero leading coefficient \((-1)^jz_1\ell^j\). The \(m\times m\) interpolation matrix \(P_{j,\ell}=p_j(\ell)\), \(j,\ell=1,\ldots,m\), is a lower-triangular polynomial-basis change from the nonzero Vandermonde matrix \([\ell^j]\), whose determinant is
\[
\det P=(-1)^{m(m+1)/2}z_1^m
 \left(\prod_{\ell=1}^{m}\ell\right)\prod_{1\le a<b\le m}(b-a)\ne0.
\]
Thus there is a unique rational solution to the m rational linear equations canceling the coefficients of \(x^{-2},\ldots,x^{-(m+1)}\); the remainder is \(O_m(x^{-(m+2)})\) by the rational-source uniform asymptotics.

**Boundary:** this theorem holds for each fixed m. The coefficients can grow rapidly with m; it does NOT grant uniform control as \(m=m(A)\to\infty\). Nor is this an exact finite-shift identity for all n; the residual is nonzero (SJ1/SJ2 prove explicit leading coefficients).

## SJ-04: uniformly negligible phase transport at SUCC's CRITICAL Fourier depth

For m fixed define the **delayed radial frame correction**
\[
B_m(n):=\sum_{\ell=1}^m a_\ell^{(m)}(Z_{n+\ell}-Z_n),\qquad
\varepsilon_m(n):=r_o(n)+B_m(n)=O_m(n^{-(m+2)}).
\]
The original zero-seeded recurrence gives an exact frequency-transport Ward identity:
\[
\boxed{e(HU_n)e(HB_m(n))
=e(16H U_{n-1})e(H\varepsilon_m(n)).} \tag{SJ4}
\]
Thus on every epoch \([A,2A)\), for every original selected integer frequency \(H\) with \(H\ll A^2\log A\), and ANY unit-bounded complex observer amplitudes \(\xi_n\),
\[
\boxed{\sup_{I\subseteq[A,2A)}
\frac1A\left|\sum_{n\in I}\xi_n
\left[e(HU_n)e(HB_m(n))-e(16H U_{n-1})\right]\right|
=O_m\left(\frac{\log A}{A^m}\right).} \tag{SJ5}
\]
Proof: use \(|e(x)-1|\le2\pi|x|\) termwise on the exact phase identity and \(|I|\le A\). The current error is far smaller than \(1/\log A\), for **m=1 already**; m≥2 improves the explicit power of A.

This is an actual source-specific, selected-pole, observer-time **near-exact signed-phase transport**. It is NOT the desired \(o(1/\log A)\) bound on either of the individual sums, because the correction \(e(HB_m(n))\) is coupled to the unknown original phase. The exact right side is merely another high-frequency BBP observation. In particular a coherent same-forcing wrong seed \(s=-\pi/16\) obeys the same forcing identities, but fails normality. Forcing jets and gauge transport alone do not distinguish that seed. The **literal zero seed** and centered signed real numerator are still load-bearing.

**Causality:** \(B_m(n)\) uses \(Z_{n+\ell}\), which is observed **later** than time n. (SJ4) is a retrospectively certified source-frame relation, or an online relation with an \(\ell\)-step reporting delay. It is NOT a zero-time oracle for future source states. This is exactly the non-simultaneous observer correction at issue.

## Verification / next honest proof route

- Exact independent SymPy rational source Laurent expansion and rational geometric moment oracle reproduce \(r_o\), \(z\), \(d_1,d_2\), the coefficients \(15/2\), \((541/16,-421/32)\), and the three-lag vector.
- Independent \`fractions.Fraction\` future-tail calculations with no π digits and horizons \(n=101,307,953,1901\) reproduce the residual leading coefficients. These finite calculations are NOT the proof of the all-m invertible-matrix theorem.
- Focused code in \`tests/test_source_jet_transport.py\` checks exact low-order coefficients and independent finite residuals.
- Potential next lamp: use #499 prime-Frobenius *signed* source characters and the literal unwrapped zero-seed integer carries to prove a **nontrivial correlation inequality** between \(e(16H U_{n-1})\) and \(e(HB_m(n))\). Without it, (SJ4) is a powerful representation of the open signed-Weyl gate, not its solution. A proposed bound must be falsified by same-forcing coherent real seeds, the radial-only nonnormal control, and altered initial branch choices.
- No physical energy accounting, borrowed quantum energy, global novelty or π-normality theorem is claimed.

**Status: source-jet spanning and signed-phase transport proved within stated classical asymptotics; original \(\pi\) fixed-character Weyl/current and critical maximal-subinterval smallness are OPEN.**
