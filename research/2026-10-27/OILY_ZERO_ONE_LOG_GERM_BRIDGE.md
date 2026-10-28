# Operation Oily × Zero–One: the BBP logarithmic germ remembers Oily's primitive characters

**2026-10-27. Research-only additive child of PR #338**, drawing on read-only PRs #309–#310 (Oily–Macaroni) and #335 (logarithmic sampling). The signed original four-pole forcing, zero seed, historical proofs, and main are untouched. **π base-16 normality remains OPEN.**

## OZO-1. One exact source, two source coordinates (PROVED)

The authentic source has the generating function

$$
G(Q)=\sum_{n\ge1}r(n)Q^{n-1}
=\int_0^1\frac{P(x)}{1-Qx^8}\,dx,\qquad
P(x)=4-2x^3-x^4-x^5,\qquad
G(1/16)=\pi.
$$

Avoid confusing the BBP source parameter **Q**, the auxiliary grade character **z**, and an integer primitive modulus **m**.

The inherited Oily positive kernel is

$$
R(x)=\frac{P(x)}{16-x^8}
=\frac{1-x}{4(1-u(x))(1-v(x))},
\quad u=x-\frac{x^2}{2},\quad v=\frac{x^2}{2}.
$$

It decomposes as a positive packet sum

$$
R(x)=\sum_{j\ge0}p_j(x),\qquad
p_j(x)=\frac{1-x}{4}\sum_{k=0}^ju(x)^kv(x)^{j-k}.
$$

Consequently

$$
\boxed{G(Q)=16\sum_{j\ge0}\int_0^1
p_j(x)\frac{1-x^8/16}{1-Qx^8}\,dx.}
$$

This follows exactly from P=(16−x⁸)R. It is a faithful analytic graded interpolation, not a new BBP formula or an asserted p-adic isomorphism.

## OZO-2. Oily gives an Euler inverse-central-binomial decomposition of π (PROVED; classical identity)

Define the **integrated packet mass** \(\pi_j=16\int_0^1p_j(x)\,dx\). Since u−v=x(1−x),

$$
p_j(x)=\frac{u(x)^{j+1}-v(x)^{j+1}}{4x}
$$

for 0<x≤1, extending continuously at x=0. Substitute x=2t and use

$$
\int_0^{1/2}t^j(1-t)^{j+1}\,dt
=\frac14 B(j+1,j+1)+\frac1{2^{2j+3}(j+1)}.
$$

The second term cancels exactly against the subtracted integral of v^(j+1)/x. Therefore

$$
\boxed{\pi_j=2^{j+1}B(j+1,j+1)
=\frac{2^{j+1}}{(2j+1)\binom{2j}{j}}.}
$$

At Q=1/16, \(\sum_j\pi_j=G(1/16)=\pi\), so

$$
\boxed{\pi=2+\frac23+\frac4{15}+\frac4{35}
+\frac{16}{315}+\cdots
=\sum_{j\ge0}\frac{2^{j+1}}{(2j+1)\binom{2j}{j}}.}
$$

**Classical provenance:** this inverse-central-binomial π series goes back to Euler; see OEIS A000796, lines 349–354, https://oeis.org/A000796. The new-to-SUCC observation is the exact identification of the *specific authenticated Oily packet masses* with its Euler summands. Do not assert priority for Euler's identity.

Crucially \(\pi_j\) are **not** the Oily endpoint weights \(w_j=(j+1)/2^{j+2}\). The former are integrals, the latter boundary coefficients as x→1.

## OZO-3. Oily's primitive character is literally the FIRST 1-germ logarithmic coefficient (PROVED)

For fixed positive integer m and |z|≤1, define the primitive packet field

$$
R_{m,z}(x)=\sum_{\substack{j\ge0\\\gcd(j,m)=1}}z^jp_j(x).
$$

Include grade j=0 only at m=1, following the usual gcd convention. Let

$$
\boxed{\mathcal G_{m,z}(Q)=
\int_0^1\frac{16-x^8}{1-Qx^8}\,R_{m,z}(x)\,dx.}
$$

For m=1,z=1, it is exactly the original G(Q). At Q=1/16, it is 16∫R_{m,z}, a source-graded interior observation.

The inherited Oily primitive character and its response are

$$
C_m(z)=\sum_{\gcd(j,m)=1}w_jz^j,\qquad
H_m(z)=2C_m(z)-zC'_m(z).
$$

From PR #310's conditional packet theorem, as δ=1−x→0,

$$
R(x)=\delta-2\delta^2+O(\delta^3),\quad
\mathbb E_x[z^J\mathbf1_{\gcd(J,m)=1}]
=C_m(z)+\delta H_m(z)+O(\delta^2).
$$

Multiplying by \(16-x^8=15+8\delta+O(\delta^2)\) gives the exact endpoint jet

$$
\boxed{(16-x^8)R_{m,z}(x)
=15C_m(z)\delta+[15H_m(z)-22C_m(z)]\delta^2+O(\delta^3).}
$$

Set \(\rho_{m,z}(n)=\int_0^1 x^{8(n-1)}(16-x^8)R_{m,z}(x)\,dx\). Its moments are exactly

$$
I_1(n)=\frac1{(8n-7)(8n-6)}
=\frac1{64n^2}+\frac{13}{512n^3}+O(n^{-4}),
$$

$$
I_2(n)=\frac2{(8n-7)(8n-6)(8n-5)}
=\frac1{256n^3}+O(n^{-4}).
$$

Therefore

$$
\boxed{\rho_{m,z}(n)
=\frac{15C_m(z)}{64n^2}
+\frac{151C_m(z)+30H_m(z)}{512n^3}
+O(n^{-4}).}
$$

In particular, Oily's primitive character is exactly the coefficient controlling the leading \(n^{-2}\) source moment. There is no statistical independence hypothesis.

## OZO-4. The SECOND logarithmic coefficient recovers Oily's connected response (PROVED)

Define \(\alpha=15C_m(z)/64\) and \(\beta=[151C_m(z)+30H_m(z)]/512\). Since the residual moment coefficients after subtraction of \(\alpha/n^2+\beta/n^3\) are O(n^(−4)), their generating function is C² up to Q=1.

Thus

$$
\mathcal G_{m,z}(Q)
=\alpha\frac{\operatorname{Li}_2(Q)}{Q}
+\beta\frac{\operatorname{Li}_3(Q)}{Q}
+J_{m,z}(Q)
$$

with \(J_{m,z}\) twice continuously differentiable at Q=1. Put s=1−Q. The only logarithms up to order s² are

$$
\frac{\operatorname{Li}_2(1-s)}{1-s}
=\cdots+s\log s+\frac32s^2\log s+O(s^2),
$$

$$
\frac{\operatorname{Li}_3(1-s)}{1-s}
=\cdots-\frac12s^2\log s+O(s^2).
$$

This yields the **source-graded 1-germ theorem**

$$
\boxed{\mathcal G_{m,z}(1-s)
=A_{m,z}-\frac{15}{64}C_m(z)s\log(1/s)
-d_{m,z}s
-\frac{209C_m(z)-30H_m(z)}{1024}s^2\log(1/s)
+O(s^2).}
$$

Here \(A_{m,z}=\mathcal G_{m,z}(1)\) and \(d_{m,z}\) is a well-defined finite source-dependent regular slope; no assertion that it equals the ungraded slope d in PR #338. The logarithmic coefficient **pair** determines both Oily source-grade observables:

$$
C_m(z)=\frac{64}{15}c_1,\qquad
H_m(z)=\frac{209C_m(z)-1024c_2}{30},
$$

where \(c_1,c_2\) are the positive-sign multipliers of \(-s\log(1/s)\) and \(-s^2\log(1/s)\). This is a nontrivial exact relationship between Oily's Möbius primitive packet algebra and the new formal/analytic 1-boundary.

**Concrete dyadic check.** At m=2, z=1, inherited \(C_2(1)=4/9\) and \(H_2(1)=-4/27\), giving

$$
\boxed{c_1=\frac5{48},\qquad c_2=\frac{73}{768}.}
$$

Ungraded m=1,z=1 gives \(C=1,H=0,c_1=15/64,c_2=209/1024\). The independent exact rational kernel expansion for dyadic odd grades is
\((16-x^8)R_{\rm odd}(x)=\frac{20}{3}\delta-12\delta^2+O(\delta^3)\),
matching the formulas.

## OZO-5. The Gamma(2) explanation and its limits

The Oily measure at time n is proportional to \(x^{8n}R(x)\,dx\). Since R(x)~(1−x), the rescaled endpoint variable \(Y_n=8n(1-X)\) converges to the Gamma(2,1) law. The same simple source zero creates the \(n^{-2}\) coefficient and consequently the \(s\log s\) singularity of the 1-germ. These are different views of **one endpoint geometry**, not independent evidence.

The Euler–Mascheroni constant \(\gamma\) appears in the logarithmic moments via \(\psi(2)=1-\gamma\). PR #310 gives the *declared golden-centered grade* correlation
\(-8/27(\varphi^{-1}-\gamma)\); changing the center changes this coefficient. The ungraded PR #338 finite slope cancels the explicit digamma gamma terms. Neither is an intrinsic π-normality selector.

## OZO-6. Negative controls and open proof obligation

This graded enrichment is an explicitly chosen Oily packet grammar. Different source-compatible regradings can change C and H without changing the ungraded original BBP G. The complete authentic source's all-time real selection still matters.

More decisively, changing the **initial real selector** to the source-preserving future-boundary solution U_n=−T_n leaves all packet polynomials, integrated Euler masses, 0/1 source germs, and graded C,H unchanged, but the real Fourier means tend to 1 for every fixed nonzero integer frequency. Thus the new boundary theorem cannot establish π normality by itself.

The actual next mathematical route is to construct a **non-factorizing joint observer** coupling the moving real Weyl phases e(hU_n), Oily grade J, and the \(q\to1\) log-jet response. It must produce a signed saving on the original zero-selected four-pole orbit, not only O(log N/N) scalar decoration; test the unchanged-forcing changed selector and PR #320 nonnormal source mutant.

**Status:** exact source/packet bridge and the first two logarithmic coefficients PROVED LOCALLY with complete derivation; Euler π series CLASSICAL; finite arithmetic and symbolic checks CORROBORATE; selected π Fourier cancellation OPEN.
