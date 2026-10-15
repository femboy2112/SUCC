# SUZUKI 30 — Original mixed Legendre moments with completed real Gamma tail

**Research date:** 2026-10-15. **Branch:** research/suzuki-mixed30-gamma-tail-2026-10-15. **Pinned parent:** recovered Suzuki Neumann draft PR #123 at d2a85cd1fdc66bc353f2d9897666a48abcfc8ae8, ultimately Phoenix-II main. Pinned source PR85 original blob 0cc8510b71d178fc79e8d410a86d8b6014cf9178. No original source files, main, concurrent PRs or external RH repository modified. No nontrivial zero positions read. **RH PROVED: NO.**

## 1. The authentic signed operator, not a fitted covariance

At the true first-prime window \(a=\tfrac12\), take the original mean-zero Legendre modes
\[
u_i(x)=P_i(2x),\qquad i=1,\dots,30,\qquad x\in(-a,a).
\]
The original finite-J signed Suzuki operator \(G_J\) has the entire genuine von Mangoldt p=2 source (with log2/sqrt2), both poles, completed infinite-contact normalization, and the first J real Gamma factors. The prior unreviewed but now recovered source code constructs exactly
\[
M^{(J)}_{k,i}=\langle u_k',(G_Ju_i)'\rangle_{L^2(-a,a)}
\]
in SHA-pinned outward-rational intervals. It is **not** the pure Gram \(T_{i,l}=\langle (Gu_i)',(Gu_l)'\rangle\), not the actual high zero-shift resolvent response and not a Weil PSD certificate.

We now enclose the *infinite* original Gamma limit \(M^{(\infty)}_{k,i}\) using an independently derived source-specific rational tail.

## 2. Source-correct Gamma potential and cancellation

The original signed even Suzuki potential includes the one real Gamma ladder
\[
-\sum_{j\ge0} c_j(1-e^{-\alpha_j|t|}),
\qquad
c_j=\frac4{(4j+1)^2},\quad
\alpha_j=\frac{4j+1}2.
\]
For the already-completed contact convention, the missing \(j\ge J\) potential is
\[
g_\infty-g_J=-\sum_{j\ge J}c_j(1-e^{-\alpha_j|t|}).
\]
Because each u_i has integral ZERO, the source constant \(-\sum c_j\) disappears after applying the convolution to u_i and differentiating. Thus the actual source difference in the derivative channel is
\[
\partial_x[(G_\infty-G_J)u_i](x)
=\sum_{j\ge J}c_j\,\partial_x
    \int_{-a}^{a}e^{-\alpha_j|x-y|}u_i(y)\,dy.
\tag{GM30-1}
\]
This is a **source-derived analytic identity**, not an assumption that the original negative arithmetic source has become positive.

## 3. The actual missing-tail bound is O(J^-2)

For \(E_\alpha(x-y)=e^{-\alpha|x-y|}\), ordinary integration by parts in y gives
\[
\partial_x E_\alpha u_i(x)=
  \int_{-a}^{a}E_\alpha(x-y)u_i'(y)\,dy
  +E_\alpha(x+a)u_i(-a)
  -E_\alpha(x-a)u_i(a).
\tag{GM30-2}
\]
The operator with kernel \(E_\alpha(x-y)\) on the actual finite support has \(L^2\)-norm at most \(2/\alpha\) by Schur. The two boundary exponentials each have integral at most \(1/\alpha\). Consequently,
\[
\big|\langle u'_k,\partial_x(E_\alpha u_i)\rangle\big|
\le\frac1\alpha\left(
  2\|u'_k\|_\infty+2\|u'_k\|_2\|u'_i\|_2
\right).
\tag{GM30-3}
\]
For the ORIGINAL unnormalized Legendre functions on a=1/2,
\[
\|u'_k\|_\infty\le k(k+1),\qquad
\|u'_k\|_2^2=2k(k+1),\qquad
|u_i(\pm a)|=1.
\]
The derivative supremum is the classical Legendre endpoint bound; the L2 identity agrees exactly with the recovered source-authentic Neumann dual derivative metric. AM–GM gives
\[
\|u'_k\|_2\|u'_i\|_2
=2\sqrt{k(k+1)i(i+1)}
\le k(k+1)+i(i+1).
\]
Inserting the true Gamma values \(c_j/\alpha_j=8/(4j+1)^3\) yields
\[
|M^\infty_{k,i}-M^J_{k,i}|
\le [2i(i+1)+4k(k+1)]\sum_{j\ge J}\frac8{(4j+1)^3}.
\]
By decreasing-integral comparison for J>=1,
\[
\sum_{j\ge J}\frac8{(4j+1)^3}
\le\frac8{(4J+1)^3}
+\int_J^\infty\frac8{(4x+1)^3}\,dx
=\frac1{(4J+1)^2}+\frac8{(4J+1)^3}.
\]
Therefore the explicitly SOURCE-TYPED infinite completion certificate is
\[
\boxed{
\left|M^\infty_{k,i}-M^J_{k,i}\right|
\le [2i(i+1)+4k(k+1)]
\left[\frac1{(4J+1)^2}+\frac8{(4J+1)^3}\right].
}
\tag{GM30-4}
\]
Every bound is an exact rational number, no numerical eigenvalue fit. It is O(J^-2) at fixed i,k and has the correct true original Gamma parity. For k+i odd, the integral is EXACTLY zero by reflection symmetry of the even source kernel and odd parity of the derivative product, independently of J.

## 4. Same-source finite-to-infinite reconstruction

For each valid original finite-J source interval \([a_{k,i}^J,b_{k,i}^J]\), the actual infinite moment belongs to
\[
M^\infty_{k,i}\in[a_{k,i}^J-E_{k,i}(J),
                  b_{k,i}^J+E_{k,i}(J)].
\]
For any two distinct original stages J1<J2, their intervals enclose the SAME infinite mixed moment, so intersection is source-lawful and MUST be nonempty. A disjoint pair is a true mathematical/provenance failure, not a favorable sign. The executable certificate tests the source J1/J2 overlap and exactly preserves odd-parity zeros.

This is a partial solution to the source-domain completion problem: it carries **actual finite Legendre mixed derivative observations to a rigorously enclosed infinite real-Gamma source object**, rather than simply naming an omega-stage. The bound is valid for all mathematical J>=1; this software inherits the original finite mixed moment engine's J<=64 implementation budget. It cannot claim a 30×30 pure derivative tensor or an infinite proof execution.

## 5. What it does and does not yield for Suzuki's low 30 Schur

The authentic Neumann dual geometry supplies a positive rank-30 derivative Gram H with an exact parity tridiagonal inverse. The genuine source mixed moment M is a necessary ingredient in projecting the source derivative response against the low Legendre derivatives.

However the projection residual has the structure
\[
T-M^*H^{-1}M,
\qquad
T_{i,l}=\langle (G u_i)',(G u_l)'\rangle.
\]
**We have not bounded or fully computed T**, nor its original infinite high resolvent cross. A rigorous interval for M cannot be silently treated as a certificate for T or the signed zero-shift Schur. Even positivity of a source-derived derivative norm does NOT imply the completed Weil sign.

The next real RH-hard gate remains the ORIGINAL low Schur complement and source feature dominance at a=1/2 and all larger intervals, with original Gamma/contact/pole/prime energies and valid functional-analytic domains. These remain open.

## Execution, hostile controls and proof status

- **Analytical original-source theorem GM30-1–4:** proved using cancellation from mean-zero source, exact boundary integration by parts, Schur norm and Legendre derivative geometry. No nontrivial zeros or positivity assumption.
- **Exact finite mathematical probes:** gamma_mixed_spectral_tail, true_mixed_legendre_tail_bound, authentic_infinite_gamma_mixed_rows and completed_mixed_gamma_two_stage_intersection in observational_succ/suzuki_mixed30_gamma_tail.py.
- **Tests:** tests/test_suzuki_mixed30_gamma_tail.py checks the exact rational sum/integral bound, two original J-stage intersection, preservation of true parity zeros, source constraints, mode range guards and rank30 first original low column.
- **Receipt:** scripts/suzuki_mixed30_gamma_tail_probe.py emits true finite/complete mixed intervals, the 30-mode rational Gamma error and explicit unresolved sign.
- **CI:** .github/workflows/suzuki-mixed30-completed-gamma.yml on Python 3.10/3.13, including inherited original true mixed, Neumann dual and source provenance regressions.
- **Source mutation controls:** false Euler primitive n=6 refused by pinned original prime tape; corrupted SHA cannot pass the inherited _pinned_source; wrong parity/malformed source modes rejected.

**Verdict:** genuine source finite→infinite real Gamma **mixed-derivative** transport now has an analytic O(J^-2) rational bound. Original global low 30 signed Schur and RH: **UNVERIFIED / OPEN**.


## 6. A sign-separated ORIGINAL infinite-Gamma mixed first moment from two source derivations

There is an unusually useful strictly signed **mixed derivative** quantity that can be certified without guessing a Weil eigenvalue.

The first mean-zero Legendre mode is u1(x)=2x on [-1/2,1/2], with u1'(x)=2. Let F1(x)=(G∞u1)(x) for the **same** original signed, completed source. Because g∞ is even and u1 is odd, F1 is odd. Therefore, using the exact source interval length one,

\[
M^\infty_{1,1}
=\int_{-1/2}^{1/2}2 F_1'(x)\,dx
=2[F_1(1/2)-F_1(-1/2)]
=4F_1(1/2).
\]

The existing **independently implemented** original source Neumann-flux adapter computes
\[
\mu_\infty=2\int_0^1(1-2t)g_\infty(t)\,dt
=2F_1(1/2),
\]
so the two derivations must agree on the exact identity

\[
\boxed{M^\infty_{1,1}=2\mu_\infty.}
\tag{GM30-5}
\]

There are two error mechanisms that fail differently:
- our finite-J true original signed mixed derivative source \(\bigl[M^J_{1,1}\bigr]\), expanded by the separately derived O(J^-2) derivative-channel Gamma tail;
- the prior original signed source flux \(\mu_\infty\), derived from weighted pole/contact/prime2/real-Gamma integrals and its independently bounded **positive** omitted Gamma tail.

Both must enclose the SAME original M∞11; their intersection is used as a **hostile original-source consistency check**. An empty intersection raises ArithmeticError, never an invented value. A strict upper bound below zero from BOTH sources, after accounting for every authentic Gamma tail, would certify the TRUE signed mixed derivative M∞11<0. The new function original_completed_first_mixed_negative_source(J=64) performs this exact source-verified intersection, requiring strict negativity from each input, with explicit source provenance and no zero-reading.

**Essential scope:** a negative mixed derivative \(\langle u'_1,(G u_1)'\rangle\) is NOT the original Weil quadratic \(\langle u_1,G u_1\rangle\), not a negative eigenvalue, and not the low Schur complement. It cannot refute RH. It is a valuable exact original signed source response for the eventual 30-low/source-high coupling.

**No full 30-mode pure derivative Gram or RH sign is established.**
