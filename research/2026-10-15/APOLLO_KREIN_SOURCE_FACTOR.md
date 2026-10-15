# APOLLO — An authentic finite-window Krein factorization of the Suzuki kernel

**2026-10-15; branch:** research/apollo-suzuki-second-third-jet-2026-10-15.
**Source ancestry:** ONE OBJECT draft PR #106 @ 04b6d8ede12c58afe4a244b11297663c33260de1; Tate draft PR #103 @ 940f0a47ef25b8b553c2f0b45032b37e68c23b02; Phoenix II main 03db44203147a7b28d445bb9f970fa71360e78c4.
**Provenance:** genuine SUCC source original Suzuki screw via SHA-pinned source_weil_hierarchy; no nontrivial-zero inputs. No source archives changed or main merged. Classical Suzuki eq (1.3) / (2.9): https://arxiv.org/html/2606.09096v3 .
**RH PROVED: NO.**

## K1. Exact prime-hinge decomposition into two independent positive Hilbert features

Let
\[
B(x,y)=\tfrac12(|x|+|y|-|x-y|)
\]
and for every real b>0 let
\[
T_b(t)=(1-|t|/b)_+,\qquad
E_b(x,y)=T_b(x-y)-T_b(x)-T_b(y)+1.
\]
Both B and E_b are genuine positive-semidefinite Hilbert Gram kernels on arbitrary finite sets:
- B is the Gram of two-sided anchored Brownian interval indicators, with positive/negative half-lines in orthogonal L² components.
- T_b(x-y) is the autocorrelation Gram of the translated normalized interval indicator b^(-1/2) 1_[x,x+b] in L²(R). E_b is its anchored increment Gram.

**K1 theorem, all real x,y,b>0:**
\[
\boxed{
(|x-y|-b)_+-(|x|-b)_+-(|y|-b)_+
=bE_b(x,y)-2B(x,y).}
\]
Proof: (|t|-b)_+=|t|-b+bT_b(t) is a literal elementary identity. Form the anchored two-variable difference. The constant cancels; the |t| term gives -2B, and T_b yields bE_b.

For *each* genuine prime-power n=p^k, the coefficient is precisely w_n=log(p)/sqrt(p^k), b_n=log(n). A fake primitive n=6 is never admitted, as w_6=0 in the authentic von Mangoldt source. K1 does NOT say the prime-hinge kernel alone is PSD; it is a **difference** of two PSD kernels.

The code exhaustively validates an exact-Fraction matrix of rational x,y,b values and all rational principal minors on selected true Brownian/interval feature Grams. These tests calibrate (not replace) the universal algebraic/feature proofs.

## K2. Exact source-canonical plus-minus feature carrier at any finite a

Fix a>0, x,y in [-a,a]. Only the finitely many true Euler impulses
\[
P_a=\{n=p^k:\log n<2a\}
\]
have a nonzero anchored hinge. For n outside P_a the original (|t|-b_n)_+ vanishes for t∈{x-y,x,y}; **do not** sum its artificial separately divergent Brownian and triangular parts over inactive infinite primes.

Use the original one-real-place Suzuki constants
\[
C_\infty=-\psi(1/4)+\log\pi
=\gamma+\pi/2+3\log2+\log\pi>0,
\]
and for j>=0, d_j=4j+1, alpha_j=d_j/2, c_j=4/d_j². Define the centered OU covariance
\[
E_j(x,y)=e^{-\alpha_j|x-y|}-e^{-\alpha_j|x|}
-e^{-\alpha_j|y|}+1.
\]
It is a **positive Hilbert kernel**, with explicit spectral feature
\[
\phi_{j,x}(\omega)
=\sqrt{\frac{2c_j\alpha_j}{\alpha_j^2+\omega^2}}\;(e^{i\omega x}-1)
\quad\text{in }L^2(\mathbb R,d\omega/(2\pi)).
\]
The Fourier integral is e^{-alpha_j|x-y|}. Since sum_j c_j<∞, the infinite direct-sum positive Gamma feature exists and the kernel sum converges uniformly on every compact.

With s(x)=sinh(x/2), h(x)=cosh(x/2)-1, the *original polar* anchored kernel is exactly
\[
K_{\rm pole}(x,y)=8s(x)s(y)-8h(x)h(y).
\]
The contact term +C_infty |t|/2 contributes precisely -C_infty B(x,y). Applying K1 to each **true source** prime hinge yields the central identity:
\[
\boxed{
\begin{aligned}
K_g(x,y)&=K_+^{(a)}(x,y)-K_-^{(a)}(x,y),\\
K_+^{(a)}(x,y)
&=\sum_{j\ge0}c_jE_j(x,y)+8s(x)s(y)
+\sum_{n\in P_a}w_nb_nE_{b_n}(x,y),\\
K_-^{(a)}(x,y)
&=8h(x)h(y)
+\left(C_\infty+2\sum_{n\in P_a}w_n\right)B(x,y).
\end{aligned}}
\tag{K2}
\]
Each right-hand block **individually** has an a-priori, positive L² or 1D Hilbert feature. No imaginary zeta-zero locations, fitted Gram or presumed RH enters their construction. The sums over prime powers are finite on each fixed a, and the Gamma feature sum is absolutely convergent. The original half-density w_n=log(p)/sqrt(n), poles, **one** Gamma ladder and contact survive.

This is a genuine **Krein factorization** of the complete signed original Suzuki kernel on each finite interval. It is **NOT** a positive factorization of K_g. Presenting a difference of Hilbert-positive Grams as one positive Gram is a logical error.

The Python module apollo_krein_factor.py independently evaluates the original source finite-J Suzuki g using genuine prime labels, then evaluates K_+-K_- with the two sets of explicit features. This is a numerical holdout, not the universal analytic proof above. The source calculator is pinned through apollo_derivative_jets.true_third_prime_wavefronts and the SHA-authenticated source; no fake source substitute.

## K3. Mixed D² and D³ reconstruct exactly the genuine Weil distribution

For t=x-y, treat derivatives below as **distributions**:
\[
\partial_x\partial_y B(x,y)=\delta_0(t)
\]
and, since T_b''(t)=(\delta_{-b}+\delta_b-2\delta_0)/b,
\[
\partial_x\partial_y[bE_b(x,y)]
=2\delta_0(t)-\delta_b(t)-\delta_{-b}(t).
\]
Thus each K1 prime plus-minus pair yields
\[
w_n[2\delta_0-\delta_{b_n}-\delta_{-b_n}]
-2w_n\delta_0
=-w_n(\delta_{b_n}+\delta_{-b_n}),
\]
**exactly** the original negative von Mangoldt Weil source, with no spurious origin contact.

For the positive Gamma OU feature,
\[
\boxed{
\partial_x\partial_y[c_jE_j(x,y)]
=\frac4{d_j}\delta_0(t)-e^{-\alpha_j|t|}.
}
\]
The coefficients follow from the exact identities 2 c_j alpha_j=4/d_j and c_j alpha_j²=1. The pole feature contributes e^{t/2}+e^{-t/2}. The contact Brownian feature contributes -C_infty δ_0 and cancels the artificial prime contact.

Hence the finite-J K2 identity, with the **infinite-Suzuki contact C_infty** and first J authentic Gamma rungs, differentiates to its exact signed distribution. In the J→∞ distributional limit the divergent individual sum_j 4/d_j δ_0 is renormalized *with* the Gamma smooth component and cannot be independently evaluated as a measure. After taking that legitimate coupled limit, the mixed D² kernel is the completed W_zeta, and mixed D³ exposes the authentic δ' prime jets from AP-01 and AP-02. This is source-faithful calculus, not a positivity inference.

**Important finite convention:** K2 at finite J retains C_infty. The prior ONE OBJECT O1 finite-stage Weil W_J uses the *contact-matched* C_J instead. Both schemes converge to the same original infinite source, but their finite distributions differ by a genuine contact delta. Never compare their J-stage formulae as identical.

## K4. The concrete missing contraction (PROOF-EQUIVALENT, UNVERIFIED)

Let the positive and negative terms in K2 define genuine source-derived Hilbert feature maps
\[
\Phi_+^{(a)}:[-a,a]\to\mathcal H_+^{(a)},\qquad
\Phi_-^{(a)}:[-a,a]\to\mathcal H_-^{(a)}.
\]
Their direct-sum constructions and inner-product equalities are **unconditional and source-canonical**. The single remaining gate for the sign of this fixed-window K2 is:
\[
\boxed{\exists\,T_a:\overline{\operatorname{span}}\Phi_+^{(a)}([-a,a])
\to\mathcal H_-^{(a)}\text{ linear contractive},
\qquad T_a\Phi_+^{(a)}(x)=\Phi_-^{(a)}(x)\quad\forall x.}
\tag{K4}
\]
A standard finite-combination norm argument proves K4 **if and only if** K_g is PSD on all finite sets in [-a,a]. If K_g≥0, the prescribed map on the positive-feature span is well-defined because any vanishing positive combination must have zero negative combination. The norm inequality then implies its extension is a contraction. Conversely a contraction makes every difference-Gram nonnegative.

Demanding (K4) for **all a>0** is RH-equivalent through Suzuki/Weil's classical positivity criterion. We have **not proved K4**, even at a=1/2. The true-positive 2×2 source certificate from earlier ONE OBJECT covers only one selected two-point subspace. The low 30 Legendre Schur sign and the all-a theorem remain unverified.

The gamma tail K_+^(infty)-K_+^(J) is itself PSD, so genuinely proving K_+^(J)-K_-≥0 for **all point combinations in one interval** would suffice for that interval, but this is an all-test infinite-dimensional inequality—not numerical finite Gram positivity.

**Source-closure wall:** the infinite prime family must NOT be separated into Brownian and triangular feature sums outside finite a; separately these sums can diverge while their signed K1 combination is exactly zero on inactive primes. Finite-window selection is a mathematically essential SUCC source index, not an implementation optimization.

## Verdict, controls and next independent probes

- **K1, K2 and K3 — PROVED ANALYTIC** with classical feature identities and the signed original Suzuki source as stated; mathematical originality not certified. Zero positions not read.
- **Finite code — EXACT rational** for K1 and both positive feature matrix minors; **TESTED NUMERIC** for independently evaluated original genuine Weil/Suzuki finite-J K2 difference on multiple prime-active windows. Machine floating rounding is not a proof certificate.
- **Negative control:** plus PSD and minus PSD does not imply the difference PSD. For example diag(1,1)-diag(2,0) has a negative direction. The feature contraction needed in K4 is absent.
- **Cross-check:** exact mixed second derivative of each positive prime triangular kernel contains an artificial +2w δ_0, exactly cancelled by the negative Brownian term, leaving the original negative impulses. Gamma contacts are infinite-regulator-coupled.
- **Next verdict-changing task:** develop a *source-specific* operator norm/range/shorting estimate establishing K4 on a nontrivial interval, using the correct full source and the genuine scalar/pole/prime and Gamma sectors. Connect the B/Brownian negative feature to PR #107's fixed-window Neumann inverse and derivative-residual Schur bounds without claiming the unresolved low matrix sign. Extend to every a or find a source-authenticated negative witness (which would require extraordinary independent review). A candidate contraction inferred from assuming K_g≥0 is circular.

Code: observational_succ/apollo_krein_factor.py; tests/test_apollo_krein_factor.py; workflow .github/workflows/apollo-derivative-jets.yml; companion APOLLO_DERIVATIVE_SOURCE_THEOREMS.md. All original source files and other live PR branches untouched.

**RH PROVED: NO.**


## K5. True-prime source activation is a Krein-neutral extension, not independent Hilbert nesting

The interval source index P_a jumps at a=log(p^k)/2. The authentic *signed* kernel K_g, however, remains compatible under restricting a larger interval to any smaller interval. K2's decomposition into positive/negative Hilbert carriers is **not** individually canonical under this transition.

For a newly activated prime with source clock b=log(p^k), w=log(p)/sqrt(p^k), take any previous smaller interval [-a0,a0] with 2a0<b. For ALL x,y in that interval, |x|,|y|,|x-y|<b, so its genuine prime hinge is identically zero. Yet its positive and negative channel increments satisfy the EXACT identity
\[
\boxed{ w b E_b(x,y)=2w B(x,y),\quad |x|,|y|,|x-y|<b. }
\tag{K5-neutral}
\]
Neither feature is necessarily the zero Hilbert feature: for x=y=r>0 and 2r<b,
\[
wb E_b(r,r)=2wr=2w B(r,r)>0.
\]
Thus adding a genuine prime to the positive-minus-negative source factorization of the extended interval **adds an equal positive and negative pair on the older observation carrier**. A would-be source gluing functor that independently and identically embeds each old positive Hilbert feature into a new one **without accounting for this neutral pair** is not justified by equality of the signed K.

**Original n=2 numerical-free source example:** exact SHA-pinned source rational log intervals certify 1/2<log2<1, and the true half-density coefficient w2=log2/sqrt2>0 with outward rational bounds. At old half-width a0=1/4 the source n=2 is not active (2a0=1/2<log2). At new half-width a1=1/2 it is active (2a1=1>log2). On the old anchor r=1/4, the positive added n=2 feature energy is *exactly* w2/2 and the added negative Brownian feature energy is *exactly* w2/2; the signed source sum is precisely zero. This is a genuine **nontrivial neutral birth** with algebraic proof. It uses exact rationals to certify log2's wavefront ordering, no zero data, no fitted Gram.

What follows is NOT that a source-compatible family of contractions across interval widths exists. Rather, any APOLLO K4 all-a contraction proof must either use each interval's independent positive/negative carriers, or construct a lawful *paired* source extension and verify coherence across every activation. A naïve positivity inheritance at source births is UNVERIFIED. This is a precise SUCC observability / gluing issue, not proof of RH.

Implementation: neutral_prime_activation_pair and authentic_prime_two_activation_on_old_window; exact Fraction adversarial checks in tests/test_apollo_krein_factor.py. Synthetic b=3/4 is used for algebraic verification on old rational points; the all-b identity together with the SHA-certified 1/2<log2<1 transfers the result to genuine b=log2 symbolically, without pretending that log2 is rational.

**K5 PROVED LOCAL / source-authenticated original n=2.** New operator gluing existence remains UNVERIFIED. RH PROVED: NO.
