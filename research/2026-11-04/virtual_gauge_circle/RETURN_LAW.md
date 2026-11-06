# Exact BBP virtual creation–repayment law

**Research date:** 2026-11-04. **Status:** paper-exact algebra and analysis within the authentic #499 angular/radial source, supplemented by six exact finite calibration tests. This result was derived interactively **before** commit and is not claimed to be a blind preregistered discovery or a worldwide-first theorem. It is additive to draft [#504](https://github.com/femboy2112/SUCC/pull/504). Zero-initialized original source and all historical contracts remain untouched.

## Theorem VR-01: one exact signed bump, completely returned

Let
\[
D(t)=1-t^8/16,\quad B(t)=(t-1)^2+1,\quad
F(t)=\frac{2-t^2}{B(t)},\quad G(t)=2\log F(t),\quad 0\le t\le1.
\]
The **authentic** eight-tap radial vector is
\[
w_{\rm rad}=(2,-2,-1,-2,-1/2,-1/2,1/4,0),
\qquad \frac{P_{\rm rad}(t)}{D(t)}=G'(t).
\]
The last identity was derived and tested in #499/#504. Note the exact rational numerator comparison
\[
(2-t^2)-B(t)=2t(1-t).
\]
Thus \(F(t)>1\), hence \(G(t)>0\), for \(0<t<1\), and \(G(0)=G(1)=0\).

Direct differentiation produces
\[
F'(t)=\frac{2(t^2-4t+2)}{B(t)^2}.
\]
Its unique zero on \((0,1)\) is \(t_*=2-\sqrt2\); \(G'\) is positive before \(t_*\) and negative afterward. Evaluation gives
\[
F(t_*)=\sqrt2,\qquad G(t_*)=\log 2.
\]
Consequently the *exact* signed flux satisfies
\[
\boxed{\int_0^{t_*}K_{\rm rad}(t)\,dt=+\log2,\quad
\int_{t_*}^1K_{\rm rad}(t)\,dt=-\log2,\quad
\int_0^1K_{\rm rad}(t)\,dt=0.}
\]
This is a nontrivial signed coboundary with equal boundary values, not a physical loan of energy or any violation of conservation laws.

The corresponding #499 Gaussian angular phase is
\[
\theta_0(t)=\arctan(t-1)+\pi/4,\qquad
\theta_0(t_*)=\pi/8
\]
because \(t_*-1=-(\sqrt2-1)=-\tan(\pi/8)\). Hence the radial signed-budget maximum lies exactly at the **angular half-arc** of the Gaussian \(\pi/4\) source. At this point the \(\lambda\)-family source deforms the angular phase by \(\frac\lambda4\log2\), while fixing both arc endpoints.

## Theorem VR-02: one positive original-source injection; every later injection strictly negative

For each \(n\ge1\), put \(m=8(n-1)\) and
\[
r_{\rm rad}(n)=\sum_{j=1}^8\frac{w_{{\rm rad},j}}{8(n-1)+j}
=\int_0^1t^m D(t)G'(t)\,dt.
\]
Because \(G(0)=G(1)=0\), integration by parts gives the exact signed moment identity
\[
\boxed{r_{\rm rad}(n)=-\int_0^1[t^mD(t)]'\,G(t)\,dt.}
\]
For \(n=1\), \(m=0\) and \([t^mD]'=D'=-t^7/2<0\), so \(r_{\rm rad}(1)>0\). Indeed the independent finite rational tap evaluation gives
\[
\boxed{r_{\rm rad}(1)=2/105.}
\]
For \(n\ge2\), \(m=8(n-1)\ge8\), and
\[
[t^mD]'=t^{m-1}\left[m-\frac{m+8}{16}t^8\right],\qquad
m-\frac{m+8}{16}t^8\ge\frac{15m-8}{16}>0
\]
throughout \(0<t<1\). Since \(G(t)>0\) there, we have an **all-\(n\) rigorous sign theorem**:
\[
\boxed{r_{\rm rad}(1)=2/105>0,\quad r_{\rm rad}(n)<0\ \forall n\ge2.}
\]
This is stronger than merely observing a signed integral with total zero.

Because \(D^{-1}(t)=\sum_{k\ge0}(t^8/16)^k\), absolute convergence gives
\[
\mathcal L(w_{\rm rad})=
\sum_{n=1}^\infty 16^{-(n-1)}r_{\rm rad}(n)
=\int_0^1G'(t)\,dt=0.
\]
In particular the one initial positive source injection is exactly repaid by all later negative injections:
\[
\boxed{\frac2{105}+\sum_{n=2}^\infty16^{-(n-1)}r_{\rm rad}(n)=0.}
\]

## Theorem VR-03: every finite horizon has an exact outstanding balance

Let \(Z_0=0,\ Z_n=16Z_{n-1}+r_{\rm rad}(n)\) be the genuine source's radial state. Expanding its recurrence, and using the zero total period, gives for **every** integer \(N\ge1\)
\[
\boxed{
\sum_{n=1}^N16^{-(n-1)}r_{\rm rad}(n)
=16^{-(N-1)}Z_N
=-\sum_{n>N}16^{-(n-1)}r_{\rm rad}(n)>0.
}
\]
The strict sign follows from VR-02. Equivalently,
\[
Z_N=-\sum_{j\ge1}16^{-j}r_{\rm rad}(N+j)>0.
\]
Since \(r_{\rm rad}(n)=O(1/n)\), this formula gives \(Z_N=O(1/N)\) and \(Z_N\to0\). The sharper inherited \(\frac1{32N}+O(N^{-2})\) and strict bound \(Z_N<1/(32N+16)\) remain as in #497/#499/#500.

Thus the finite signed balance, the future repayment, and the literal zero seed are tied by an **exact source-derived identity**, not by a probabilistic or assumed cancellation axiom.

## Theorem VR-04: the Ward test that stops a false π-normality proof

For **any continuously differentiable complex test function** \(\psi\colon[0,1]\to\mathbb C\), the exact boundary condition gives
\[
\boxed{\int_0^1\psi(t)K_{\rm rad}(t)\,dt
=-\int_0^1\psi'(t)G(t)\,dt.}
\]
For the CONSTANT probe \(\psi=1\), the right side vanishes. But for the nonconstant probe \(\psi(t)=t\), it is **strictly negative**:
\[
\int_0^1 tK_{\rm rad}(t)\,dt
=-\int_0^1G(t)\,dt
=-\Big[4\sqrt2\log(1+\sqrt2)-2\log2-\pi\Big] <0.
\]
The square bracket is \(\approx0.4579149064\). Its positivity is already guaranteed by \(G>0\); the closed form follows by elementary integration.

**Critical distinction:** boundary-null under a CONSTANT observation does not imply cancellation under a **phase-sensitive** (nonconstant) probe. In particular, the exact source-level budget above does NOT establish
\(\sum_{A\le n<2A}e(H(Y_n+Z_n))=o(A/\log A)\), nor any fixed-frequency Weyl decay for the actual original \(\pi\) orbit. The authentic angular source can be correlated with the radial factor. Proving an oscillatory *coupled* Ward/coboundary identity whose remainder is quantitatively controlled is the remaining task.

This is what the "virtual support" metaphor accurately captures: **a strictly nonzero transient signed resource with a precisely enforced return**, not signlessness of the zero element itself. The zero has no preferred sign, but the decomposition terms acquire rigorous signs from the original source geometry.

## Existing-source integration, tests, and claim scope

At the actual source endpoint \(t=1\),
\(K_{\rm ang}(1)=4,\ K_{\rm rad}(1)=-4\), so \(K_{\rm original}(1)=0\), equivalently the leading \(1/n\) Mellin forcing cancels **for the selected \(\lambda=1\)**. This is a second exact source cancellation distinct from the radial period integral. In fact, \(r_{\rm ang}(n)=15/(32n)+O(n^{-2})\) and \(r_{\rm rad}(n)=-15/(32n)+O(n^{-2})\), while their authentic sum is \(r_{\rm original}(n)=15/(64n^2)+O(n^{-3})\). This acceleration does not provide distributional Haar mixing.

Six exact independent regression checks in \`tests/test_virtual_return_law.py\` passed locally (Fraction ledger at finite \(n\), source tap signs, rational polynomial identities, source preservation and moment derivative positivity). These finite checks are calibration; the all-\(n\) statements above are supported by the displayed analytical proofs. No full native suite, hosted child CI, Lean formalization, external referee review or global scholarly priority claimed.

**Verdict:** source-level creation/return and finite-time balance DISCLOSED by exact algebra and real analysis under the pinned original source. A signed original angular–radial Weyl estimate remains **UNVERIFIED**. A tempting implication "zero signed period ⇒ zero weighted oscillatory correlations" is decisively **REFUTED** by \(\psi(t)=t\).
