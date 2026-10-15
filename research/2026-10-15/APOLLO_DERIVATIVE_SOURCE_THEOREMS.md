# OPERATION APOLLO — Second/third Weil–Suzuki jets, prime-source tomography, and the one-scalar feature gate

**Research date:** 2026-10-15. **Branch:** research/apollo-suzuki-second-third-jet-2026-10-15.
**Pinned parent:** research/one-object-tate-weil-suzuki-connes-2026-10-15 at 04b6d8ede12c58afe4a244b11297663c33260de1 (draft PR #106), transitively on Tate source PR #103 at 940f0a47ef25b8b553c2f0b45032b37e68c23b02 and Phoenix II main 03db44203147a7b28d445bb9f970fa71360e78c4.
**No main changes, no cross-repo push, no prior source rewrites, no zero reading. RH PROVED: NO.**

## 0. Intake, actual pre-existing frontier, and the choice of probe

The user proposed that **second and third derivatives are load bearing** in the SUCC/Tate/Weil/Suzuki/Connes interface. We took this as a *precise testable conjecture* about distribution-valued differentiation, source detection, gauge ambiguity, positivity and domain losses.

Suzuki's 2026 primary-source formulas (arXiv:2606.09096v3, September 23 2026), (1.3), (2.2), (2.9)–(2.11), §7.7, establish that for the **authentic even continuous screw** g:
- W=-D²g on compact test functions, D=d/dt as distributions;
- the original signed Weil form Q_W(v) equals the signed compact integral with kernel g(x-y) acting on v';
- under RH, one can produce a positive feature representation, while its unconditional source-kernel equality is **NOT** proved (Suzuki §7.7).
Source: https://arxiv.org/html/2606.09096v3 .

Parallel **draft** PR #107 (https://github.com/femboy2112/SUCC/pull/107) claims a useful **fixed-window** genuine high-sector Douglas-range theorem at a=1/2, assuming inherited AMW-06B high coercivity, but does NOT prove the original low Schur sign or all-a theorem. We do not duplicate or import its unmerged files. APOLLO attacks the *orthogonal derivative identification* problem on its own branch.

External mathematical imports: the distributional primitive/kernel identity (Suzuki); elementary characterization of distributions annihilated by D^m; Fourier/Mellin basic identities; Krein–Langer/Weil conditional-positivity characterization. Project-local source enclosures are inherited from exact Git-SHA-pinned observational_succ/source_weil_hierarchy.py. Scholarly novelty of the particular synthesis unverified.

## AP-01: Three distributional jet layers with exact original arithmetic (CLASSICAL / PROVED DERIVATION)

Fix J>=0. Use the **original signed finite real-Gamma Weil distribution** W_J and **contact-matched even** Suzuki primitive g_J from ONE OBJECT O1:
\[
W_J(h)=\int h(t)(e^{t/2}+e^{-t/2})dt
-\sum_{n=p^k\ge2}\frac{\log p}{\sqrt n}[h(b_n)+h(-b_n)]
-C_0h(0)
-\sum_{j=0}^{J-1}\int_0^\infty e^{-\alpha_jt}[h(t)+h(-t)-2e^{-t/2}h(0)]dt,
\]
with b_n=log n, alpha_j=(4j+1)/2, C_0=EulerGamma+log(4pi), and the nontrivial zeros **never** used as construction inputs. The original prime sum is locally finite on h in Cc-infinity.

For d_j=4j+1, let
\[
C_J=C_0+\sum_{j<J}\bigl(4/d_j-2/(2j+1)\bigr)
\]
and
\[
g_J(t)=-4(e^{|t|/2}+e^{-|t|/2}-2)
+\frac12C_J|t|
+\sum_{n=p^k}\frac{\log p}{\sqrt n}(|t|-b_n)_+
-\sum_{j<J}\frac4{d_j^2}(1-e^{-d_j|t|/2}).
\]
For every smooth compact test h:
\[
\boxed{W_J(h)=-\langle D^2g_J,h\rangle,\qquad
\langle D^3g_J,h\rangle = W_J(h')=-\int_\mathbb R g_J(t)h'''(t)dt.}
\tag{AP1}
\]

**Proof:** O1 established the first equality by independent distributional derivatives of the pole, prime ramps, contact cusp and exponential Gamma rungs. Distributional derivative is defined by <DT,h>=-<T,h'>. Hence <D³g,h>=-<-W,h'>=W(h'), proving the second formula *without pointwise third differentiation across the origin or prime wavefront*. Compact h of class Cc³ suffices for the finite-stage integrals, whereas the full tempered-distribution statement holds on Cc-infinity. No sign assumption.

The full **finite-J third derivative** is
\[
\boxed{
D^3 g_J=
-\sinh(t/2)
-\sum_{j<J}\alpha_j\,\operatorname{sgn}(t)e^{-\alpha_j|t|}
+\sum_{n=p^k}w_n(\delta'_{b_n}+\delta'_{-b_n})
+\left(C_0-2\sum_{j<J}\frac1{2j+1}\right)\delta'_0.}
\tag{AP1-3}
\]
Distribution test pairings are locally finite. All notation δ'_b means derivative in *the distribution variable t*, acting by <δ'_b,h>=-h'(b). Exact polynomial/rational symbolic tests verify the **rational offset** of δ'_0. Critically, the separated δ'_0 coefficient diverges as J→infinity; the smooth Gamma sum diverges oppositely in the distribution topology. **Do not take their limits separately.** This is why third derivatives require a stronger source-renormalization protocol than evaluating an ordinary pointwise third derivative.

The independent numeric oracle uses the odd compact Cc³ test h(t)=t(1-(t/R)^2)^4 on |t|<R and zero outside (R rational), calculates original W_J(h') from the Euler/real-Gamma/pole/contact source and -∫g_Jh''' independently, splitting integrals at true prime wavefronts. Nine genuine-source cases and deliberately wrong contact mutation are **NUMERICAL CALIBRATIONS**, not the analytic proof.

## AP-02: Exact prime-power tomography with second/third singular jets (PROVED LOCAL)

For b_n=log(p^k)>0 and w_n=log(p)/sqrt(p^k), every genuine source impulse contributes
\[
D^2g\big|_{\text{prime }n}=w_n(\delta_{b_n}+\delta_{-b_n}),
\quad
D^3g\big|_{\text{prime }n}=w_n(\delta'_{b_n}+\delta'_{-b_n}).
\tag{AP2}
\]
The arch and pole terms are smooth in a neighborhood of each b_n>0; the set {b_n} is discrete on compact windows. Thus the first radial derivative has the exact source jump
\[
\boxed{g'(b_n+)-g'(b_n-)=\frac{\log p}{\sqrt{p^k}}.}
\tag{AP2-jump}
\]
This distinguishes n=p^k from fake composite-6: Λ(6)=0, so there is **no** original log 6 jump. It is an exact mathematical/source identity; a physical sensor or finite mathematical observer has not been shown to sample an irrational clock with infinite exactness.

Implementation genuine_prime_third_jet(n) imports the *pinned original* source, authenticates n=p^k, and returns exact outward rational enclosures for log n and w_n using source.log_iv(p), source.sqrt_inverse(n). true_third_prime_wavefronts(R) uses rational log enclosures for **every** inclusion/exclusion decision on R<=4, and raises on a possible boundary collision. It does not silently infer from a floating threshold or from zeros of xi. Cases R=1/2,1,2 give respectively (), (2), and (2,3,4,5,7). Mutant n=6,10,12... is rejected. These are **finite source signatures**; infinite all-test positivity is untouched.

## AP-03: The *third derivative's exact quadratic gauge* (CLASSICAL / PROVED LOCAL NO-GO)

Let g,h be even continuous functions, anchored at 0, with equal third distributional derivatives D³g=D³h. A standard distribution theorem says D³(h-g)=0 iff h-g is a polynomial of degree <=2. Evenness kills the linear term; anchoring kills the constant. Thus
\[
\boxed{h(t)=g(t)+ct^2\quad(c\in\mathbb R).}
\tag{AP3-gauge}
\]
This remaining quadratic gauge is invisible to D³ but not to D². It changes the signed source as
\[
W_h=W_g-2c\,dt
\]
in distributions, where $dt$ is **constant Lebesgue-density distribution**, and changes the anchored (Krein–Langer) kernel by
\[
\boxed{K_h(x,y)=K_g(x,y)-2cxy.}
\tag{AP3-Gram}
\]
The correction is rank one and can have either sign. For the SHA-pinned original zeta K_g at x=1/4, the exact rational source enclosure strictly certifies K_g(x,x)>0 (inherited from PR #106). The mutant with c=64 has a rigorously **strictly negative** K_h(x,x) yet exactly the **same third derivative**. This is explicitly **NOT** a counterexample to RH: $h$ is NOT a lawful completed zeta source because it adds the constant density -128 dt to W_g.

**Minimal gauge repair:** If D³h=D³g as above AND W_h(eta)=W_g(eta) for *one* compact smooth eta of nonzero total mass m=∫eta dt ≠0, then
0=(W_h-W_g)(eta)=-2cm implies c=0. Equivalently one source-identifiable nonzero kernel value fixes c in the anchored symmetric 2D setting. The one scalar pairing must come from the authentic **Tate/pole/Arch source**, not from a fitted positivity assertion.

**Do not conflate two origin defects:** A contact mutation cδ_0 in W corresponds to a |t|-cusp in g, and its **derivative δ'_0 is visible to D³** (our wrong-contact bump tests detect it). The D³-invisible gauge is a *constant W density* coming from t², not an origin delta. They are distinct distributions with distinct test signatures. Identifying them as one vague “boundary term” is an invalid source map.

## AP-04: Why a raw third-derivative kernel cannot be positive (CLASSICAL / PROVED LOCAL)

Since genuine g is even, D³g is **odd**, hence its translation kernel T(x-y)=D³g(x-y) is antisymmetric under exchanging x,y. Pairing any *real* smooth v against it symmetrically gives
\[
\iint_{\mathbb R^2} v(x)D^3g(x-y)v(y)dx\,dy=0,
\]
interpreted by distributional duality. A real antisymmetric bilinear form has no nontrivial positive quadratic content. Multiplying by i produces a formally self-adjoint Fourier multiplier but no source-derived sign.

Pairing a derivative in **both** arguments instead yields an even operator:
\[
\partial_x\partial_y K_g(x,y)=W(x-y);
\quad
\partial_x^2\partial_yK_g(x,y)=\partial_xW(x-y);
\quad
\partial_x^2\partial_y^2K_g(x,y)=-W''(x-y).
\tag{AP4-mixed}
\]
If W is positive definite then -W'' is positive definite too (Fourier multiplier ξ²), **but the converse is false**. Counterexample: W=-1 (constant density, hence W(v*tilde v)=-|∫v|²<0 on nonzero-mass tests), yet -W''=0 is positive semidefinite. More differentiation can *hide* the very low mode needed for the global sign.

## AP-05: The exact derivative/moment loss theorem (CLASSICAL / PROVED LOCAL)

For each integer m>=1, write D^m Cc-infinity(R) for the set of all m-th derivatives of compact smooth functions. Then
\[
\boxed{
D^m C_c^\infty(\mathbb R)
=\{v\in C_c^\infty(\mathbb R):
 \int_{\mathbb R}x^k v(x)\,dx=0,\quad 0\le k<m\}.
}
\tag{AP5}
\]
**Proof of necessity:** integration by parts m times, boundary terms vanish, derivative D^m x^k=0 for k<m.

**Proof of sufficiency:** for v with all m vanishing moments define
\[
\phi(x)=\int_{-\infty}^{x}\frac{(x-t)^{m-1}}{(m-1)!}v(t)dt.
\]
Then D^mφ=v. Left of supp(v) the integral vanishes. Right of supp(v), expand $(x-t)^{m-1}$; each coefficient is an assumed zero moment, so φ=0. Therefore φ∈Cc-infinity, proving equality. The m moment functionals are linearly independent (test bumps near m distinct points), giving exact codimension m.

**Meaning for APOLLO:** A test strategy that uses only D²-generated sources automatically excludes TWO polynomial moments; only D³-generated sources excludes THREE. Their extra smoothness cannot certify Weil positivity on the complementary low subspace. This is structurally the low-sector sign debt already explicit in Suzuki's 30-Legendre Schur program, but is not a new proof of the low matrix sign.

Calibration: phi(t)=t^b(1-t)^b on [0,1], zero outside; b>=7, m=1,2,3. It is only finitely smooth at endpoints (not Cc-infinity), but all exact polynomial moment identities and the compact m-fold primitive are checked using Fraction. The universal smooth theorem is the analytic proof above; finite polynomials do not pose as a complete proof oracle.

## AP-06: A minimal mixed-third verification theorem for a candidate positive feature (PROVED GENERAL REDUCTION, RH-HARD PREMISE)

Let $K_g(x,y)=g(x-y)-g(x)-g(-y)+g(0)$, with authentic real even continuous g. Let $F(x,y)$ be **any continuous real symmetric anchored** kernel ($F(0,y)=F(x,0)=0$), e.g. a genuine Hilbert Gram from independently constructed features. Assume the pullback of W=-D²g along x-y is well-defined as a distribution on R².

**Claim A:** If
\[
\partial_x\partial_yF(x,y)=W(x-y)
\quad\text{as distributions on }\mathbb R^2,
\tag{AP6-second}
\]
then **F=K_g everywhere**.

*Proof:* $\partial_x\partial_y(F-K_g)=0$. Every continuous solution is $a(x)+b(y)$ in distributions. The two anchored boundary conditions force $a+b=0$ identically.

**Claim B:** If instead only the mixed *third* source derivative is matched,
\[
\partial_x^2\partial_yF(x,y)=\partial_xW(x-y)
\quad\text{as distributions,}
\tag{AP6-third}
\]
then
\[
\boxed{F(x,y)=K_g(x,y)+cxy}
\]
for some *real* c. Indeed, for H=F-K_g, H_{xxy}=0 gives H(x,y)=xB(y) by integrating and using anchored boundary values; real symmetry then gives xB(y)=yB(x), forcing B(y)=cy. A **single** exact source pairing F(x0,y0)=K_g(x0,y0) with x0*y0≠0 fixes c=0.

Either (AP6-second) with anchor conditions, or (AP6-third) with the one scalar, would imply RH **IF F is independently Hilbert-positive and the identity holds for ALL admissible source tests**. These are PROOF-EQUIVALENT-strength identification targets, NOT established for Suzuki's unconditionally defined $\mathfrak S_x$ feature family. No hidden circular assumption is allowed. The “one-scalar” observation does **not** reduce the all-test identity itself to a single sample.

This is a practical probe-selection result: instead of fitting K_g values at sampled pairs, test a *distributional mixed derivative* of an independently positive candidate F against the genuine prime-power δ', full Gamma singular kernel, pole, half-density and two renormalization contacts; check one nonzero canonical normalization. Numeric coincidences at finite pairs are not a substitute.

## AP-07: Authentic small-r differentiability and a quantified source-bound (PROVED ANALYTIC, TESTED NUMERIC)

For $r>0$ away from true prime wavefronts, let $q=e^{-r/2}$, $C_\infty=\gamma+\pi/2+3\log2+\log\pi$. The Gamma derivative identity
\[
 2\sum_{j\ge0}\frac{q^{4j+1}}{4j+1}
 =\operatorname{artanh}q+\arctan q
\]
implies the **source-derived radial first derivative**
\[
g'(r)=
-4\sinh(r/2)+\frac{C_\infty}{2}
-\operatorname{artanh}(q)-\arctan(q)
+\sum_{n=p^k:\log n<r}\frac{\log p}{\sqrt n}.
\tag{AP7-g1}
\]
No zeros are read. For $0<r\le1/4<\log2$, the prime sum is exactly zero. Differentiate away from r=0:
\[
g''(r)=-2\cosh(r/2)+\frac{q}{1-q^4},
\quad
g'''(r)=-\sinh(r/2)-\frac{q}{2(1-q^4)}
-\frac{2q^5}{(1-q^4)^2}.
\tag{AP7-g2g3}
\]
They are **ordinary derivatives only on the strictly positive source-prime-free interval**. At r=0 the gamma singularity requires the previously specified distribution/Pf/contact interpretation.

**Quantified theorem:** with C=(EulerGamma+log(2pi))/2,
\[
\boxed{\left|g'(r)-\frac12\log r-C\right|\le3r,
 \qquad 0<r\le1/4.}
\tag{AP7-bound}
\]
*Proof:* write z=r/4. Then
$\operatorname{artanh}(e^{-r/2})=\frac12\log(\coth z)$ and
$0\le\frac12\log(z\coth z)\le z/2=r/8$,
because $z/(1+z)\le\tanh z\le z$ (the lower inequality follows from $e^{2z}\ge1+2z$). By differentiating arctan(e^{-r/2}) and AM-GM, its deviation from π/4 is at most r/4. Finally $4\sinh(r/2)\le2r e^{r/2}\le16r/7$ when $r\le1/4$, using $e^{1/8}\le8/7$. The constant terms in (AP7-g1) cancel to C, and the error is <=$(16/7+1/4+1/8)r=149r/56<3r$. All inequalities are elementary uniform estimates, not fitted constants.

It follows analytically that
\[
\lim_{r\downarrow0}r\,g''(r)=\tfrac12,\quad
\lim_{r\downarrow0}r^2 g'''(r)=-\tfrac12,
\]
giving the exact *strength* of the second and third ordinary singularities. This is consistent with Suzuki (2.2) $g(r)=\frac12r\log r+A r+O(r^2)$. Thus naive pointwise third-derivative squaring or evaluating $g'''(0)$ is **not** a legal Hilbert feature construction.

The code tests the analytic formulas with independent high-precision values at rational radii. Those floating comparisons are **calibration**, not certificates of their own rounding. The uniform estimate above is the proved analytical content.

## Claim ledger and current RH dependency

| ID | Claim status | Evidence | Wall |
|---|---|---|---|
| AP-01 | CLASSICAL / PROVED DERIVATION | distributional differentiation of exact source-matched finite Weil/Suzuki identity | not Weil positivity |
| AP-02 | PROVED LOCAL | exact original prime-power labels, signed $\delta'$ source enclosures, no fake6, rational cutoff checks | infinite observer sample execution not claimed |
| AP-03 | CLASSICAL / PROVED LOCAL + mutant counterexample | kernel D³ of even anchored distributions is quadratic; strict negative original-plus-fake gauge | mutant violates genuine W normalization |
| AP-04 | CLASSICAL / PROVED NO-GO | odd/antisymmetric D³, constant-W negative example hidden by -D²W | raw higher derivatives cannot sign a form |
| AP-05 | CLASSICAL / PROVED LOCAL | exact moment-annihilator characterization for $D^mC_c^\infty$ | derivative-only probes leave m low moments |
| AP-06 | CLASSICAL / PROVED CONDITIONAL IDENTIFICATION | mixed derivative distribution uniqueness with anchor and symmetry | independent positive F ↔ original W mixed jet still unproved |
| AP-07 | PROVED ANALYTIC + TESTED NUMERIC | exact Gamma derivative summation; uniform rational-linear g' error; asymptotic g'',g''' | no full signed positivity |
| RH | UNVERIFIED | unconditionally constructed positive feature with exactly authentic mixed jet for ALL tests, or full Suzuki low Schur/all-a sign | RH OPEN |

## Next Apollo phase: falsification plan (do not promote sampled correlations)

1. Obtain Suzuki's unconditional source-defined feature $\mathfrak S_x$ precisely from primary §7.7 and its earlier construction; fix real Fourier orientation, Gamma/conductor, analytic boundary values and test domain. Compute **$\partial_x^2\partial_y\langle \mathfrak S_x,\mathfrak S_y\rangle$** distributionally by a new route not using $W_\zeta$ or assumed RH.
2. Prove/refute equality of its prime δ' wavefront amplitudes with the genuine p^k log-weights and its gamma/Pf/contact distribution at origin; challenge it with χ_-3 parity/conductor and non-Euler fake6. Equality only at finitely many points is NOT enough.
3. Use a single exact source-normalized anchor value to fix any residual cxy gauge, but ONLY after all-test derivative equality. If equal and feature Gram is independently positive, the Weil–Suzuki theorem would give RH.
4. Independently attack the fixed-window shorting sign from PR #107. AP-05 predicts that derivative-based tests can miss low moments; certify the authentic 30×30 low matrix, do not infer positivity from moment-null high-sector evidence. Any genuine negative witness must be verified at exact original-source error and independently audited.
5. Connes alternative: match his principal-value normalization and ALL prime places before comparing its trace-derived mixed derivative to $W_\zeta$; off-identity local clock traces and their derivatives cannot fix the identity-contact distribution. Do not identify the D³-invisible constant mode with the δ_0 contact.

**Developer/repro:** 
- observational_succ/apollo_derivative_jets.py, tests/test_apollo_derivative_jets.py,
- scripts/apollo_derivative_probe.py,
- .github/workflows/apollo-derivative-jets.yml with Python 3.10/3.13, source-provenance gates;
- inherited SHA-pinned Suzuki exact intervals and originals remain unchanged.

The objective is source-correct **identification and discriminating probes**, not the assertion of an unproved RH breakthrough.

**RH PROVED: NO.**


## APOLLO source factorization phase — companion theorem

The follow-on [APOLLO_KREIN_SOURCE_FACTOR.md](APOLLO_KREIN_SOURCE_FACTOR.md) supplies an **exact true-source** positive-minus-positive factorization of the original signed continuous Suzuki anchored kernel on every finite window. Its Gamma OU, real polar, genuine Euler prime-interval and Brownian contact channels reproduce the full signed Weil mixed D² and prime δ' mixed D³. Each channel is a separately genuine positive Hilbert feature, but their **difference** is not proven nonnegative. The resulting full-source Hilbert contraction K4 is RH-equivalent and UNVERIFIED.

A new source-gluing obstruction K5 shows that genuine newly activated prime factors appear as a nontrivial equal positive/negative feature pair on previously observed intervals, although the signed kernel restriction is unchanged. Any coherent transport of contractions across all a must account for such Krein-neutral births; equality of signed kernels alone cannot justify literal inclusion of both positive and negative feature representations.
