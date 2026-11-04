# OPERATION PISOT–GAMMA: the two-conjugate seam and unimodular phase descent

**2026-11-02 · RESEARCH ONLY · PAPER PROOFS + EXACT FINITE REPLAY.** This branch is an additive child of Gamma Seam draft #468 at exact parent \`7c7f26ea3ebb530744d695cf485b0e35d0997143\` (through #465/#461 to Main XIX). Retain the original signed four-pole BBP forcing, literal \`U_0=0\`, archives, formal kernel, production and history without modification. **NO new base-16 π-normality theorem.** Our use of the silver ratio/Pisot unit is *specialized to the original Gamma seam*; the Pell and Pisot properties themselves are classical.

## PG-01. An exact 2D Pell carrier; a unit hidden in the decaying conjugate

Let λ=1+√2, λ'=1−√2=−λ^(−1). For each k≥0 define integers P_k,Q_k by
\[
\lambda^k=P_k+Q_k\sqrt2,\qquad
(\lambda')^k=P_k-Q_k\sqrt2.
\]
The integral carrier map \(M=\left(\begin{smallmatrix}1&2\\1&1\end{smallmatrix}\right)\) has det −1 and
\[
M^k=\begin{pmatrix}P_k&2Q_k\\Q_k&P_k\end{pmatrix},\quad
P_k^2-2Q_k^2=(-1)^k,\quad
P_{k+2}=2P_{k+1}+P_k.
\]
Take \(\mathcal P_k=\left(\begin{smallmatrix}P_k&P_{k+1}\\Q_k&Q_{k+1}\end{smallmatrix}\right)\); det \(\mathcal P_k=(-1)^k\). Thus the **exact canonical Bézout pair**
\[
u_k=(-1)^kQ_{k+1},\qquad v_k=-(-1)^kQ_k
\]
satisfies simultaneously
\[
\boxed{
u_k P_k+v_k P_{k+1}=1,\quad
u_kQ_k+v_kQ_{k+1}=0,
}
\]
\[
\boxed{
u_k\lambda^k+v_k\lambda^{k+1}=1,\quad
u_k(\lambda')^k+v_k(\lambda')^{k+1}=1.
}\tag{PG-01}
\]
This last equality is the key finite/infinite phenomenon: \((\lambda')^k\to0\) exponentially, but the **coupled** integer coefficients \(u_k,v_k\) grow exponentially and transport the decaying conjugate to one *exact unit* at EVERY k. Consequently **dropping the stable conjugate before Bézout reconstruction discards exactly one unit**, not an asymptotically negligible phase. This is a mathematically rigorous description of the user's "infinite tails dance together" intuition, but it is universal algebra, not yet an original-source temporal mixing statement.

Define the Lucas/Pell integer trace \(\mathcal L_k=\lambda^k+(\lambda')^k=2P_k\). Then
\[
\boxed{u_k\mathcal L_k+v_k\mathcal L_{k+1}=2.}
\]
For ANY declared real lift \(y\in\mathbb R\), and integer h, put \(F^\pm_{k,h}(y)=e(h(\lambda_\pm)^ky)\) where \(e(t)=\exp(2\pi it)\). Exact multiplicativity of the phases gives
\[
\boxed{
(F^+_{k,h})^{u_k}(F^+_{k+1,h})^{v_k}
=(F^-_{k,h})^{u_k}(F^-_{k+1,h})^{v_k}
=e(hy),
}\tag{PG-02}
\]
whereas using the INTEGER trace alone gives \(e(2hy)\). Using the primitive integer P_k frequencies directly gives
\[
\boxed{e(hP_ky)^{u_k}e(hP_{k+1}y)^{v_k}=e(hy).}\tag{PG-03}
\]
The noninteger single-sheet characters depend on the chosen real lift, but their **reconstructed final product** e(hy) is a legitimate circle character and is invariant under y→y+m for m∈Z. The 2D integral carrier is unimodular; no physical Planck constant or quantum claim follows.

## PG-02. Original Γ source and finite measured-seam chart

Keep EXACTLY the BBP rational source
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
For b≥n≥0 write
\[
\alpha_b=\sum_{j=1}^b16^{-j}r(j),\qquad
R_{n,b}=\sum_{j=n+1}^b16^{n-j}r(j).
\]
These are original, exact rationals. They satisfy
\[
U_n=16^n\alpha_b-R_{n,b},\quad
R_{n,b}=R_{n,m}+16^{n-m}R_{m,b}.
\]
Set \(x_n=\{U_n\}\in[0,1)\), and **retain the original integer carry**
\(c_n=\lfloor U_n\rfloor\). The proper finite analytic/Gamma real lift is
\[
\boxed{Y_{n,b}=x_n+R_{n,b}=16^n\alpha_b-c_n\in\mathbb Q.}\tag{PG-04}
\]
This equality makes the chosen branch and boundary explicit: \(Y_{n,b}\) need NOT belong to [0,1), and reducing it modulo one *before* applying a noninteger Pisot frequency would silently change the result. The original positive Beta/Gamma kernel
\(P(u)=4-2u^3-u^4-u^5=(1-u)(u^2+2)(u^2+2u+2)\)
proves
\[
0\le R_{n,b}\le T_n
=\int_0^1\frac{u^{8n}P(u)}{16-u^8}\,du
\le\frac1{(8n+1)(8n+2)}\le\frac1{64n^2}
\quad(n\ge1).
\]

## PG-03. The exact mixed Γ–Pisot phase transport, independent of k

Define the analytic expanding and contracting phase sheets for any k≥0:
\[
\mathcal F^\pm_{n,b,k}(h)
=e(h(\lambda_\pm)^kY_{n,b}).
\]
Their signed Bézout product from PG-02 equals \(e(hY_{n,b})\) **exactly** for each sheet:
\[
\boxed{
\mathcal F^\pm_{n,b,k}(h)^{u_k}
\mathcal F^\pm_{n,b,k+1}(h)^{v_k}
=e(hY_{n,b})=e(hU_n)e(hR_{n,b}).}\tag{PG-05}
\]
The same finite rational source chart works for every Pell order. The reconstructed character differs from the literal zero-selected circle phase by
\[
\boxed{
|e(hY_{n,b})-e(hU_n)|
\le2\pi|h|R_{n,b}
\le\frac{2\pi|h|}{(8n+1)(8n+2)}.}\tag{PG-06}
\]
For any late source window \(a+1\le n\le b,\ a\ge1\), the TOTAL complex phase error of the whole joint Γ–Pisot reconstruction satisfies
\[
\boxed{\sum_{n=a+1}^b|e(hY_{n,b})-e(hU_n)|
\le\frac{\pi|h|}{32a},}\tag{PG-07}
\]
and its mean error is ≤π|h|/[32a(b−a)]. This is a rigorous finite-to-infinite boundary-control theorem—not a signed cancellation theorem. It is the previous Gamma seam transport realized in a **new two-conjugate Pell frame**.

For every dyadic block scale j within a length-N late window, normalize Haar block energy \(C_j=E_j/(N2^j)\) and signed loss \(\omega_j=W_j/(N2^{j+1})\). With the two phase fields \(z_n=e(hU_n)\) and \(w_n=e(hY_{n,b})\), classical parallelogram inequalities and the common ℓ¹ error give simultaneously at ALL j
\[
\boxed{|C_j(z)-C_j(w)|,\ |\omega_j(z)-\omega_j(w)|
\le\frac{\pi|h|}{16aN}.}\tag{PG-08}
\]
Thus even highly unstable individual Pisot sheets have a uniformly stable **joint signed Haar cascade** once the exact inverse is applied first. This does not lower-bound any \(\omega_j\).

## PG-04. Gluing two independently truncated adjacent windows

For any \(0\le n\le b_1<b_2\),
\[
Y_{n,b_2}-Y_{n,b_1}
=16^{n-b_1}R_{b_1,b_2}
\]
with the SAME integer carry \(c_n\). When an earlier window \(a+1\le n\le b_1\) is transferred from its own cutoff \(b_1\) to the later cutoff \(b_2\), the *joint reconstructed* complex phase obeys
\[
\boxed{
\sum_{n=a+1}^{b_1}|e(hY_{n,b_2})-e(hY_{n,b_1})|
\le\frac{32\pi|h|}{15}R_{b_1,b_2}
\le\frac{32\pi|h|}{15(8b_1+1)(8b_1+2)}.}\tag{PG-09}
\]
This bound is independent of either window length and of the selected Pell index k. If the expanding/contracting sheets are bounded independently AFTER raising them to |u_k|,|v_k|, they pay artificial exponential amplification. The exact signed joint identity avoids this cost. **Two windows can be coherently glued with a k-independent Gamma boundary expense.**

## PG-05. Regulator-matched growing-frequency probe (different from fixed-h Weyl!)

Compare the TRUE circle character at the integer Pisot TRACE harmonic \(\mathcal L_k=2P_k\), to the expanding analytic sheet of the SAME measured-seam lift:
\[
e(h\mathcal L_k x_n)\quad\text{versus}\quad e(h\lambda^k Y_{n,b}).
\]
Since \(\mathcal L_k-\lambda^k=(\lambda')^k\), the exact exponent mismatch is
\[
\boxed{\delta_{n,b,k}=(\lambda')^kx_n-\lambda^kR_{n,b}.}\tag{PG-10}
\]
For n≥a+1,
\[
|\delta_{n,b,k}|\le\lambda^{-k}+\frac{\lambda^k}{64a^2}.
\]
Set the unit **regulator** \(\mathcal R=\log\lambda>0\). Choose the nearest nonnegative integer \(k(a)\) to \(\log(8a)/\mathcal R\). Then
\[
\lambda^{k(a)}\in[8a/\sqrt\lambda,\,8a\sqrt\lambda],
\]
and with \(\sqrt\lambda+1/\sqrt\lambda=\sqrt{2\lambda}\),
\[
\boxed{|\delta_{n,b,k(a)}|
\le\frac{\sqrt{2\lambda}}{8a},\qquad
|e(h\mathcal L_{k(a)}x_n)-e(h\lambda^{k(a)}Y_{n,b})|
\le\frac{\pi|h|\sqrt{2\lambda}}{4a}.}\tag{PG-11}
\]
All these bounds hold for all b>a, all n∈(a,b] and every h. The mean and each normalized signed Haar energy/loss comparison are O_h(a^(-1)) uniformly over block scales. The choice k(a) can be computed with **exact algebraic comparison in Q(√2)** without approximate logarithms.

**Crucial quantifier boundary:** the INTEGER Weyl frequency \(\mathcal L_{k(a)}\asymp a\) MOVES with a. This transport **does not** assert cancellation for any fixed harmonic, and cannot discharge normality or Gate A alone. Neither sheet is a circle character until recombination or integer-trace projection.

**PARITY-SENSITIVE SEAM:** because \((\lambda')^k=(-1)^k\lambda^{-k}\), for odd k the two terms of δ have the same sign (both nonpositive); for even k they can genuinely cancel at exactly \(x_n=\lambda^{2k}R_{n,b}\). This is a well-typed, falsifiable *source-selected finite* phase-locking condition, not an asserted frequency law.

## PG-06. An elementary 16/Pisot arithmetic separation (not temporal decorrelation)

The Pell integers P_k are odd for ALL k≥0: \(P_0=P_1=1\) and \(P_{k+2}\equiv P_k\bmod2\). Thus \(\mathcal L_k=2P_k\equiv2\bmod4\). For any k,m≥1, \(16^m\equiv0\bmod4\); hence
\[
\boxed{|\mathcal L_k-16^m|\ge2,\quad
|\lambda^k-16^m|\ge2-\lambda^{-k}>2-\lambda^{-1}>1.}
\]
The field norm provides the complementary exact algebraic obstruction \(N(\lambda)=-1\) versus \(N(16)=256\). Clock identities \(\lambda^k=16^m\) cannot occur. This is additive ABSOLUTE frequency separation, NOT a selected real-circle correlation estimate. The unit action \(M\in GL_2(\mathbb Z)\) and base-16 dilation on local finite carriers are different types and cannot be identified by a naive circle/sphere rotation.

## PG-07. The silver regulator really occurs in the source—but only as a scalar boundary period

Existing Gamma Seam #468 proves for the exact same original forcing:
\[
\boxed{\sum_{n\ge1}r(n)
=\frac{(4+5\sqrt2)\pi}{16}
+\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2).}
\]
We independently checked the exact rational partial-fraction identity
\[
\frac{P(u)}{1-u^8}
=\frac{u+3}{4(1+u^2)}-\frac{u^3}{1+u^4}
+\frac{u}{2(1+u^4)}+\frac5{2(1+u^4)}+\frac3{4(1+u)}.
\]
The \(1+u^4\) branch produces the silver-unit logarithm, while all **finite original source increments r(n)** remain rational. In \(\partial_t\log[G(t+1)/G(t)]\), Euler–Mascheroni \(-\gamma\) cancels since \(\sum c_i=0\). The regulator \(\log\lambda\) therefore supplies a mathematically natural logarithmic resolution scale, but scalar source-mass identities do not control the SIGNED temporal window covariance.

## PG-08. Sharp no-go and the missing theorem

The same EXACT Gamma forcing with a different real seed \(s=1/5-\alpha\), \(\alpha=\pi/16\), yields a completed orbit \(16^n/5\bmod1=1/5\): all its Fourier amplitudes are coherent. Every Pell determinant, both analytic conjugate reconstructions, the exact Gamma window sewing, the silver mass and the regulator-matched transport also hold on that coherent counterseed. Therefore NONE of those source/representation identities by itself proves the original \(U_0=0\) asymptotic signed loss.

Even on a generic circle measure with density \(1+\cos(2\pi x)\), \(\widehat\mu(1)=1/2\) but the marginal means \(\widehat\mu(P_k)=\widehat\mu(P_{k+1})=0\) for k≥2. Thus apparent high-frequency mixing in **each channel** does not force mixing of their signed Bézout product. Preserve the JOINT phases and original integer carries, not only marginals or independent Haar controls. This generic countermodel is not an invariant measure of the original BBP recurrence.

**Remaining novel arithmetic estimate (OPEN):** derive a genuinely original-four-pole, original-zero-seed bound on the **signed joint** Pisot/Gamma cross-block reinforcement, or equivalently produce an unbounded aggregate Haar loss budget over the intermediate scales of Gamma Seam GS-04. The finite Pell/gluing identities specify an information-preserving probe but do not supply the source-specific bound. An all-horizon proof must still resolve the original Weyl gate for EVERY fixed nonzero integer h. Inherited SUCC positive coherent differential shadow from #463 is mandatory additional hostile source control.

### Proof boundaries and prior work

Exact Pell algebra, Gamma recurrence (DLMF §5.5), SUCC's previous Gamma tail and Haar energy identities are reused and attributed. New to this branch is their **typed two-conjugate phase sewing, exact amplification accounting, uniform regulator-matched error and parity-sensitive zero-locus**. External prior art warns that Pisot numbers may generate persistent Fourier nondecay: Erdős's Pisot Bernoulli convolution theorem (see Solomyak's Bernoulli convolution notes). Schmidt's 1980 periodic-expansion theorem and Dubickas's 2023 Pisot quotient theorem are arithmetic background; neither asserts a π normality result. No scholarly priority claim is made. Independent implementations of the same formulas are not blind mathematical witnesses. No merger, tag, release, publication or claim-status promotion is authorized.
