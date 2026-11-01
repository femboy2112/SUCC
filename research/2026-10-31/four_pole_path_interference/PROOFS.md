# Operation FOUR-POLE PATH INTERFERENCE

**31 October 2026 · additive research child of Main XVIII 4eb411e3730a9e7b95480369a438b89d9a433a4b.** The original source, historical proofs, production and the literal zero selector are untouched. These are paper-proved classical/source-specialized statements, not Lean-certified mathematical priority claims. Base-16 π normality, NET-XVII-2 and RH remain OPEN.

## FP-01 — the original signed poles resolve into three overlapping positive edges

The unchanged four-pole source and recurrence are
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
For \(a=8n-7>0\), exactly
\[
\boxed{r(n)=2\left(\frac1a-\frac1{a+3}\right)+
\left(\frac1a-\frac1{a+4}\right)+
\left(\frac1a-\frac1{a+5}\right).}\tag{FP1}
\]
For \(m=3,4,5\), each edge \(f_m(n)=1/a-1/(a+m)\) has the positive representations
\[
f_m(n)=\frac{m}{a(a+m)}
=\int_0^m\frac{ds}{(a+s)^2}
=\int_0^\infty e^{-au}(1-e^{-mu})du>0.
\]
With \(W(s)=2{\bf1}_{[0,3]}(s)+{\bf1}_{[0,4]}(s)+{\bf1}_{[0,5]}(s)\), the overlap weights are 4 on (0,3), 2 on (3,4), and 1 on (4,5). Therefore
\[
\boxed{r(n)=\int_0^5\frac{W(s)}{(8n-7+s)^2}ds,\quad
\int_0^5W(s)ds=2\cdot3+4+5=15=16-1.}\tag{FP2}
\]
Define zero-seeded channel states \(V_{m,0}=0,\ V_{m,n}=16V_{m,n-1}+f_m(n)\). The UNIQUE authentic state for this declared four-pole forcing is
\[
\boxed{U_n=2V_{3,n}+V_{4,n}+V_{5,n},\quad n\ge0.}\tag{FP3}
\]
The rational states are summed BEFORE exponentiation; there is no independently randomized path hypothesis.

## FP-02 — absolute Laurent paths and exact finite Prony source fingerprint

Let shifts \(c=(7,4,3,2)\), signed weights \(w=(4,-2,-1,-1)\), and pole moments \(m_j=\sum_iw_ic_i^j\). Then
\[
(m_0,\ldots,m_7)=(0,15,151,1209,8995,64905,461611,3259089).
\]
The four original atoms have zero total signed mass \(m_0=0\). For every \(j\ge1\), \(m_j>0\), because \(4\cdot7^j>2\cdot4^j+3^j+2^j\). Thus for every integer \(n\ge1\), writing \(x=8n\),
\[
\boxed{r(n)=\sum_{j=1}^{\infty}\frac{m_j}{x^{j+1}}.}\tag{FP4}
\]
The series converges absolutely because \(7/x<1\), and for \(J\ge1\) its strictly POSITIVE remainder is bounded by
\[
0<r(n)-\sum_{j=1}^Jm_j/x^{j+1}
<\frac{4\cdot7^{J+1}}{x^{J+2}(1-7/x)}.
\]
The edge-path moments realize the SAME signed Laurent data:
\[
\boxed{(j+1)\int_0^5W(s)(7-s)^jds=m_{j+1}.}\tag{FP5}
\]
The finite pole polynomial and rational generating function are
\[
\boxed{Q(X)=\prod_{c_i}(X-c_i)=X^4-16X^3+89X^2-206X+168,}\tag{FP6}
\]
\[
\boxed{\sum_{j\ge0}m_jz^j=
\frac{z(15-89z+128z^2)}{1-16z+89z^2-206z^3+168z^4}.}\tag{FP7}
\]
For \(x=8n\), \(r(n)=[15x^2-89x+128]/Q(x)\). The shifts sum to 16, their pairwise products sum to 89, and their Vandermonde difference product is 120. These are EXACT source arithmetic fingerprints; their visual alignments are NOT evidence that selected phase cancellation follows.

## FP-03 — the sign of the Hankel form depends on the SOURCE MAP

The signed four-atom moment Hankel matrix \(H^{\mathrm{atom}}=(m_{i+j})_{0\le i,j<4}\) factors as
\[
H^{\mathrm{atom}}=V\operatorname{diag}(4,-2,-1,-1)V^\mathsf{T},
\quad V_{ij}=c_j^i,\quad\det V=120.
\]
Consequently
\[
\boxed{\det H^{\mathrm{atom}}=-115200,\quad
\operatorname{inertia}(H^{\mathrm{atom}})=(1+,3-).}\tag{FP8}
\]
Since this Hankel matrix is invertible, Prony reconstruction from the first eight moments \(m_0,\ldots,m_7\) uniquely returns Q and then all four weights by a Vandermonde solve, **among sources known in advance to have at most FOUR distinct atomic poles**.

In contrast, the same four-pole source has the previously established positive Euler/Gamma integral
\[
\boxed{r(n)=\int_0^1t^{8n-8}P(t)dt,\quad
P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2)>0
\quad(0<t<1).}\tag{FP9}
\]
Thus \( (-1)^k\Delta^kr(n)=\int_0^1t^{8n-8}(1-t^8)^kP(t)dt>0\) for all n≥1,k≥0. Every finite time-index Hankel \((r(n+i+j))_{0\le i,j<d}\) is positive definite, and in fact this positive-measure kernel is strictly totally positive (generalized Vandermonde/Andréief formula; support is an interval).

FP8 and FP9 refer to **DIFFERENT Hankel constructions**, the signed pole-shift coordinate and the positive time-moment coordinate. No positivity contradiction occurs; the choice of transport/observable changes what is measured. Neither result provides a positive Weil form or selected real-circle Fourier cancellation.

## FP-04 — eight-pole-moment SPOOF with literal zero boundary

Define for every integer n≥1 the positive nine-term Beta/Gamma finite difference
\[
\boxed{b_n=\sum_{j=0}^8(-1)^j{8\choose j}\frac1{8n+j}
=\int_0^1t^{8n-1}(1-t)^8dt
=B(8n,9)=\frac{8!}{(8n)(8n+1)\cdots(8n+8)}>0.}\tag{FP10}
\]
The signed Laurent moments of these nine additional atoms vanish through order seven:
\[
\boxed{\sum_{j=0}^8(-1)^j{8\choose j}(-j)^k=0\ (0\le k<8),
\quad =8!\ (k=8).}\tag{FP11}
\]
Therefore for any rational ε>0 the fake forcing \(r_\epsilon(n)=r(n)+\epsilon b_n\) has the SAME first eight signed Laurent moments as the original, remains positive, and retains the literal U0=0, but is NOT the authentic four-pole source. This does not refute four-atom Prony uniqueness, whose source-class hypothesis the mutation violates.

The completed BBP-style zero-seed constant is nevertheless shifted:
\[
\boxed{\alpha_\epsilon-\alpha_0
=\epsilon\sum_{n\ge1}16^{-n}b_n
=\epsilon\int_0^1\frac{t^7(1-t)^8}{16-t^8}dt>0,\quad
\alpha_0=\pi/16.}\tag{FP12}
\]
Let \(B_K=\sum_{n=1}^K16^{-n}b_n\). Because \(b_n\) decreases,
\(0<\sum_{n>K}16^{-n}b_n<16^{-K}b_{K+1}/15\).
The exact mutant state differs by \(U^\epsilon_n-U_n=
\epsilon\sum_{j=1}^n16^{n-j}b_j\), an expanding radix-memory amplification. Eight matching finite moments and exact zero initial condition cannot authenticate the ENTIRE original source.

## FP-05 — one/two-path Haar does NOT rule out triple phase conspiracy

For the actual states in FP3, define the empirical three-torus measure \(\mu_N=N^{-1}\sum_{n=1}^N\delta_{(\{V_{3,n}\},\{V_{4,n}\},\{V_{5,n}\})}\). The authentic zero-selected Weyl average is the joint character
\[
\boxed{N^{-1}\sum_{n=1}^Ne(hU_n)=\widehat\mu_N(2h,h,h).}\tag{FP13}
\]
No marginal factorization or independent-path average is justified by FP3.

For a decisive HOSTILE control, let A,B be independent Haar-circle variables and let \(X=A,Y=B,Z=-2A-B\pmod1\). Each one-dimensional marginal is Haar, and each TWO-dimensional pair projection is Haar, since the corresponding integer torus maps are surjective. Yet
\[
\boxed{e(2X+Y+Z)\equiv1.}\tag{FP14}
\]
Finite exact versions over odd moduli p enumerate every (a,b) mod p, set z=-2a-b, obtain each of the three pair histograms with p² cells of count one, and still lock the weighted triple phase to one.

For \(\zeta_3=e(2hV_3)\), \(\zeta_4=e(hV_4)\), \(\zeta_5=e(hV_5)\), ordinary cumulant algebra gives
\[
E_N[\zeta_3\zeta_4\zeta_5]
=\prod_iE_N[\zeta_i]
+\sum_{i<j}\mathrm{Cov}_N(\zeta_i,\zeta_j)E_N[\zeta_k]
+E_N\prod_i(\zeta_i-E_N\zeta_i).
\tag{FP15}
\]
Even complete one/two-path Haar does not bound the FINAL genuine triple-order term. This counterfeit does NOT satisfy the actual four-pole recurrence. It refutes marginal/pairwise-statistics-only normality arguments, not normality of π. The right source-selected signed triple character FP13 remains OPEN.

## FP-06 — the continuous-time original source cancels, but integer sampling can RESTORE coherence

The exact original positive future tail has the inherited analytic extension
\[
T(x)=\sum_{j\ge1}16^{-j}r(x+j)
=\int_0^1\frac{t^{8x}P(t)}{16-t^8}dt,\qquad x\ge0.
\]
For any real completed-carrier parameter \(q\ge3/16\) put
\[
\boxed{U_q(x)=16^xq-T(x).}\tag{FP16}
\]
At each positive integer n this is the SAME original four-pole recurrence, with seed \(s=q-\pi/16\). The actual selected zero seed is q=π/16>3/16. Using \(P(t)/(16-t^8)\le1-t\), differentiation gives \(T'<0,\ T''>0,\ T''(x)\le384/(8x+1)^4\).
For x≥3/4, q≥3/16, and log16>2, the leading term in \(U_q''\) is ≥6 while \(T''≤384/2401<1\). Hence
\[
\boxed{U_q'(x)>q(\log16)16^x>0,\qquad U_q''(x)>0.}\tag{FP17}
\]
Integration by parts, using increasing phase derivative, proves for all integer h≠0 and N≥1
\[
\boxed{\left|\int_1^Ne(hU_q(x))dx\right|
\le1/(\pi|h|U_q'(1))<1/(6\pi|h|).}\tag{FP18}
\]
The improper continuous integral converges as N→∞; the selected q=π/16 enjoys this O(1) smooth-time bound. This does NOT bound its sampled Weyl sum.

Define the explicit C-infinity nonnegative smooth bump
\(\psi(u)=\exp(1-1/(1-16u^2))\) for |u|<1/4, zero otherwise. Its height is one, total variation two, and its translates about integers are disjoint. Put \(w_N(x)=\sum_{n=1}^N\psi(x-n)\). Classical Poisson summation gives the EXACT finite-horizon identity
\[
\boxed{\sum_{n=1}^N e(hU_q(n))
=\sum_{\ell\in\mathbb Z}I_{N,\ell}(q,h),\quad
I_{N,\ell}=\int_{\mathbb R}w_N(x)e(hU_q(x)-\ell x)dx.}\tag{FP19}
\]
The alias series converges absolutely at each N because the integrand is smooth compactly supported. On each bump, integration by parts with FP17 and \(\int|\psi'|=2\) gives \(|I_{n,0}|\le3/(2\pi|h|U_q'(n-1/4))\). Sum the geometric lower bound \(U_q'(x)>q\log16\,16^x\):
\[
\boxed{|I_{N,0}(q,h)|\le1/(5\pi q\log16|h|)
<1/(30q|h|).}\tag{FP20}
\]

**Coherent same-forcing changed-seed control.** At q=1/5, the seed is \(1/5-\pi/16\), an irrational NONZERO value. Since \(16^n\equiv1\pmod5\), every integer time satisfies \(e(hU_{1/5}(n))=e(h/5)e(-hT_n)\). The authentic positive tail has \(\sum_{n\ge1}T_n<1/32\), hence
\[
\left|\sum_{n=1}^Ne(hU_{1/5}(n))-Ne(h/5)\right|
<\pi|h|/16<11|h|/56.
\]
Combining this and FP20 with the EXACT Poisson decomposition FP19 yields
\[
\boxed{\left|\sum_{\ell\ne0}I_{N,\ell}(1/5,h)\right|
>N-\frac{11|h|}{56}-\frac1{6|h|}.}\tag{FP21}
\]
The smooth zero-alias path shows O(1) cancellation while **the sum of nonzero sampling aliases restores nearly N-scale coherence**. This is proved for a NONSELECTED altered seed, not for π. The original q=π/16 also has FP18–20, but its nonzero alias sum is the still-OPEN signed Weyl gate in a new exact representation.

## Claims and proof barrier

**PROVED LOCAL / classical:** FP01–FP12 (positive edges, strict Hausdorff moment kernel, indefinite signed atomic Hankel, four-pole Prony under a stated source-class prior, Beta/Gamma jet-matching fake), FP13 (exact joint 3-channel character identity), FP14 (pairwise-Haar triple-lock counterexample), FP16–FP21 (smooth-time cancellation and exact nonzero Fourier alias restoration at q=1/5). No source-local or positive-moment claim is promoted to a selected real-circle result.

**OPEN / UNVERIFIED:** nontrivial all-horizon source-selected \(\widehat\mu_N(2h,h,h)=o(1)\), nonzero Poisson-alias cancellation at q=π/16, Main XVII NET-XVII-2 joint primary×cofiber L² non-conspiracy, π normality, RH. FP13/FP19 are identities/criteria, not signed savings.

**Next decisive falsifier:** use the EXACT original four-pole and U0=0 source labels to derive a quantitative bound on the genuinely joint three-channel character (or its same-basis cofiber/lag representation). Calibrate source-preserving changed seed q=1/5, nearzero irrational shadows, the first-eight-moment-matched Beta fake, pairwise-Haar triple-lock, and AT-07 seven-pole null. A proposition depending only on the signed moments through j7, positive Hausdorff Gram, one/two-path Haar or smooth-time cancellation must FAIL on at least one explicit control. A candidate passing all of them still owes fresh infinite signed source-specific proof.

**Classical provenance:** Prony exponential decomposition (Potts–Tasche); moment Hankel positivity and Andréief (Khare); Poisson sampling of smooth compact support (UPenn Advanced Analysis). Repo precedents: Main XVIII signed-lag and Main XVII NET-XVII-2; original three-place Gamma resolvent already contains P(t), positivity and source tail (not rediscovered here).