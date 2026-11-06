# Two-clock BBP return: exact source transport, delayed phase and sharp boundary flux

**Research-only paper derivation, November 4, 2026.** Parent #504 exact SHA \`f3327bdce023fe3f68d4c5431b5a7c2b53dac2ed\`. Original four-pole BBP vector, literal U_0=0, selected Gaussian/radial prime-character split of #499/#500, unwrapped rational carries and all historical contracts are unchanged. Prior frame/covariance refs: on-main \`observational_succ/covariant_observer_frames.py\`, #393 Lorentz-clock source-Fourier noncovariance, #482 common-frame SU(2) gyroscope and false-Haar twirl, #287 conservative boundary flux; read-only sibling #505 critical chirp normal counterseeds. Source proofs here **do not establish** any Lorentz symmetry or a genuine physical dynamical law. The terms "repayment" and "observer clock" denote exact linear/arithmetic bookkeeping.

Write \`e(x)=exp(2 pi i x)\`. Let original, angular and radial zero-seeded rational states satisfy
\[
U_n=16U_{n-1}+r_o(n),\quad Y_n=16Y_{n-1}+r_a(n),\quad Z_n=16Z_{n-1}+r_r(n),\quad U_0=Y_0=Z_0=0,
\]
with \(U_n=Y_n+Z_n\) and the **actual** radial taps
\[
w_r=(2,-2,-1,-2,-1/2,-1/2,1/4,0),
\quad r_r(n)=\sum_{j=1}^8\frac{w_{r,j}}{8(n-1)+j}.
\]
#504's exact radial zero-period identity gives
\[
z(x)=-\sum_{m\ge1}16^{-m}r_r(x+m),\qquad z(n)=Z_n,\quad n\ge1,
\]
and all derivatives may be taken term by term for \(x\ge1\). Independently expanding these *rational* source terms shows
\[
r_r(x)=-\frac{15}{32x}-\frac{53}{256x^2}+O(x^{-3}),\quad
z(x)=\frac1{32x}-\frac5{256x^2}+O(x^{-3}).
\]
The error has controlled derivatives of each fixed order: for \(j\ge0\) the differentiated remainder is \(O_j(x^{-3-j})\). This follows from differentiating the finite rational partial fractions, bounding their remainder uniformly at \(x+m\ge x\), then summing the exponentially weighted m-series. No π digit oracle enters.

## OR-01: exact delayed-clock repayment identity (all n, fixed ell)

For every integer \(n\ge1\) and integer \(\ell\ge1\), iteration yields
\[
\boxed{Z_{n+\ell}=16^\ell Z_n+\sum_{j=1}^\ell16^{\ell-j}r_r(n+j).} \tag{OR1}
\]
Therefore
\[
\Delta_\ell Z_n:=Z_{n+\ell}-Z_n
=(16^\ell-1)Z_n+\sum_{j=1}^\ell16^{\ell-j}r_r(n+j).
\]
For each *fixed* \(\ell\), the first term has expansion \((16^\ell-1)/(32n)+O_\ell(n^{-2})\); the second equals \(-(16^\ell-1)/(32n)+O_\ell(n^{-2})\). Their order-\(1/n\) terms cancel **at different chronology labels**. The exact common-tail expansion sharpens this:
\[
\boxed{\Delta_\ell Z_n=-\frac{\ell}{32n^2}+O_\ell(n^{-3}),\quad
(\Delta_\ell z)'(x)=\frac{\ell}{16x^3}+O_\ell(x^{-4}).} \tag{OR2}
\]
For negative fixed \(\ell\), interpret \(n+\ell\ge1\) and the same formula holds with the signed \(\ell\).

A source-labelled *parallel transport* from n to m is
\[
W_{n,m}(H)=e(H(Z_m-Z_n)).
\]
It satisfies \(W_{n,m}W_{m,k}=W_{n,k}\), \(W_{n,n}=1\), \(W_{m,n}=W_{n,m}^{-1}\), and every closed loop has product 1. This is a flat U(1) **pure-gauge cocycle**; its trivial holonomy does NOT mean the selected BBP orbit is equidistributed or that a physical electromagnetic field vanishes. The old on-main Lorentz-frame machinery preserves causal edge ordering on a declared Minkowski carrier; the present one-dimensional discrete-clock retiming is only an **algebraic source-frame transport**, not a Lorentz boost.

## OR-02: exact same-forcing fixed-h time-frame equivalence, no new normality

For each **fixed signed** lag \(\ell\), (OR2) implies \(\sum_{n\ge\max(1,1-\ell)}|\Delta_\ell Z_n|<\infty\). Thus for any fixed integer h,
\[
\boxed{\left|\sum_{n=n_0}^Ne(hU_n)-\sum_{n=n_0}^Ne(h(Y_n+Z_{n+\ell}))\right|
\le2\pi|h|\sum_{n=n_0}^\infty|\Delta_\ell Z_n|=O_{h,\ell}(1),}
\]
where \(n_0=\max(1,1-\ell)\). In particular they have the **same normalized fixed-h Weyl limit** if one exists. This transfers the problem between frames without answering it. At growing h=H_A, however, the bound is \(O_\ell(H_A)\), and ceases to be useful at the current critical depth. This is a precise observer-resolution boundary.

## OR-03: an all-horizon delayed-observer exponential sum with a SHARP boundary term

For \(\ell\in\mathbb Z\setminus\{0\}\) fixed and \(A\) sufficiently large that all labelled indices exist, define for any positive integer H:
\[
C_{A,\ell}(H)=\frac1A\sum_{n=A}^{2A-1}e\!\left(H(Z_{n+\ell}-Z_n)\right),\qquad q:=H/A^2.
\]
By the exact source asymptotic (OR2), uniformly over \(n\in[A,2A)\),
\[
H\Delta_\ell Z_n=-\frac{\ell q}{32(n/A)^2}+O_\ell(q/A).
\]
Comparing the resulting \(C^1\) Riemann sum to its integral using a direct derivative/variation estimate of \(O_\ell(q/A)\) gives
\[
\boxed{C_{A,\ell}(H)=\int_1^2 e\!\left(-\frac{\ell q}{32x^2}\right)dx
+O_\ell\!\left(\frac{1+q}{A}\right).} \tag{OR3}
\]
This estimate holds for all \(q>0\), with a constant depending on fixed \(\ell\), although it is useful only when \(q=o(A)\).

Let \(q\to\infty\). The real phase \(\phi(x)=-\ell q/(32x^2)\) has nonvanishing derivative \(\ell q/(16x^3)\). Integrating by parts and then bounding the remainder by the same nonstationary-phase derivative argument gives
\[
\boxed{C_{A,\ell}(H)=
\frac{8}{\pi i\ell q}
\left[8e\!\left(-\frac{\ell q}{128}\right)
-e\!\left(-\frac{\ell q}{32}\right)\right]
+O_\ell\!\left(q^{-2}+\frac{1+q}{A}\right).} \tag{OR4}
\]
**Both endpoint terms are essential.** The ratio of their magnitudes is exactly 8:1, so they CANNOT cancel each other no matter their relative phases:
\[
\boxed{\frac{56}{\pi|\ell|q}-O_\ell(q^{-2}+(1+q)/A)
\ \le |C_{A,\ell}(H)|\ \le\
\frac{72}{\pi|\ell|q}+O_\ell(q^{-2}+(1+q)/A).} \tag{OR5}
\]

At #501/#503's actual frequency schedule
\[
H_A(h)=|h|16^{\lfloor\log_{16}(A^2\log A/|h|)\rfloor},\quad
q_A=H_A/A^2,\quad \frac{\log A}{16}<q_A\le\log A
\]
for every sufficiently large A and fixed \(h\ne0\). Since \(q_A^2/A\to0\), it follows rigorously:
\[
\boxed{|C_{A,\ell}(H_A(h))|=\Theta_{\ell,h}(1/\log A).} \tag{OR6}
\]
This is source-specific relative-frame **signed cancellation**, yet the sharp epoch endpoint flux is **too large to satisfy** the desired little-o(\(1/\log A\)) selected Weyl gate. Exact non-simultaneity has created an observable boundary obstruction rather than solved normality.

This result is NOT the original \(\sum e(HU_n)\) and is not a counterexample to π normality. An independent simple first-derivative/Kusmin–Landau test gives \(C=O_\ell(1/q)\) when \(q\asymp\log A\); the explicit endpoint calculation above proves matching scale and prevents mistaken o. Compare the classical Kusmin–Landau condition \(f'\) monotone and separated from integers; here \(f'=H(\Delta_\ell z)'\asymp_\ell q/A\) and lies inside (0,1/2) for sufficiently large A.

## OR-04: retiming changes *how* repayment appears; smoothing moves the debt to the boundary

Let \(w\in C_c^\infty((1,2))\) be a declared fixed observer window. The source-labelled smoothly weighted delayed response is
\[
C^w_{A,\ell}(H)=\frac1A\sum_{n\in\mathbb Z}w(n/A)e(H\Delta_\ell Z_n),
\]
with terms only where \(w(n/A)\ne0\). By (OR3) with amplitude \(w\),
\[
C^w_{A,\ell}(H)=\int_1^2w(x)e(-\ell q/(32x^2))dx+O_{w,\ell}((1+q)/A).
\]
Because \(w\) and every derivative vanish near both endpoints, integration by parts can be iterated arbitrarily without producing an endpoint term. For every **fixed** integer \(M\ge1\),
\[
\boxed{C^w_{A,\ell}(H)=O_{w,\ell,M}(q^{-M}+(1+q)/A).} \tag{OR7}
\]
On the actual \(q_A\asymp\log A\) schedule, choose \(M=2\): this is \(o(1/\log A)\). The **same radial source** has a sharp-interval \(\Theta(1/\log A)\) response and a smooth-window \(o(1/\log A)\) response. The faster cancellation is not an original source invariant: it depends on the observer window. In particular, a smooth-window estimate cannot replace the **maximal sharp-subinterval** critical-ratchet target required by #501/#503/#505.

The original selected mixed signal is
\[
e(H(Y_n+Z_{n+\ell}))=e(HU_n)\,e(H\Delta_\ell Z_n).
\]
Knowing the second factor oscillates does NOT control the product; source-correlated angular phases can defeat it. A falsifier is the explicitly **changed angular source** \(Y_n^\star=-Z_{n+\ell}\), making the coupled product identically 1. More seriously, the *authentic four-pole forcing with a nonzero real seed* \(-\pi/16\) produces the coherent completed orbit \(-T_n\) (sibling #503/#505), while preserving the same additive radial cocycle after the seed is assigned to the angular line. This demonstrates why literal original zero seed and source-selected real numerator/carry have indispensable status.

A common-frame SU(2) twirl in #482 can erase a coherent Bloch vector without changing the source's underlying purity. Our smooth-window example is analytically different but shares that **observer averaging is not a proof of source mixing**. The #393 clock-boost SUCC Fourier noncovariance check is another independent warning.

## OR-05: the next genuinely distinguishing source-coupled lamp

Use both chronologically labelled channels and the true integer/rational carries to study:
\[
\mathfrak C_{A,H}^{\ell}(I):=A^{-1}\sum_{n\in I}e(HY_n)e(HZ_{n+\ell}),\qquad
I\subseteq[A,2A)\ \text{contiguous}.
\]
The target required for original π normality at the high F4 depth is a **MAXIMAL-SUBINTERVAL** signed estimate for \(\ell=0\):
\[
\boxed{\sup_{I}\left|\mathfrak C_{A,H_A(h)}^{0}(I)\right|=o_h(1/\log A)
\quad\forall\text{ fixed }h\ne0.}
\]
No such estimate is proved here. A potentially discriminating intervention is to retain the *same authentic* angular and radial sequences and compare the lag-zero correlation with \(\ell=\pm1,\pm2\), keeping radial-only, same-forcing wrong seed, and finite-window smooth observer controls. A positive bound must survive the no-go that a phase factor with separately small sums can still have a fully coherent product with its companion. It must also pay a sharp-window endpoint/current, rather than laundering it away by smoothing.

## Provenance and validation scope

OR-01 to OR-04 are ordinary exact recurrence algebra, differentiable rational tail asymptotics, Euler–Maclaurin/Riemann-sum comparison, and classical repeated nonstationary-phase integration by parts. This is **not** a global novelty claim. The earlier radial return theorem, cyclotomic carrier, source character projector, and accelerated four-pole forcing are inherited from #499/#500/#504. The critical high-frequency and maximal-subinterval choice comes from #501/#503/#505 (read-only cross-branch, not copied ancestry).

Finite exact/numerical calibrations live in \`tests/test_observer_relative_return.py\` and \`probe.py\`, with optional receipt. The proof does not rely on finite samples. The scoped claim ledger and source map accompany this document. No new Lean proof, no independent scholarly review and no full native >11k SUCC suite claim. **π normality, original signed Weyl/current and RH remain OPEN.**
