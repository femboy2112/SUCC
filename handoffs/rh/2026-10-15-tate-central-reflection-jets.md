# RH candidate handoff — Tate's 1-s reflection, the genuine Gamma Brownian contact and prime-power jet diode

**2026-10-15.** Standalone draft research in \`femboy2112/SUCC\`, branch \`research/tate-central-reflection-prime-jet-2026-10-15\`, child of APOLLO #122 head \`bf1bb848cfc9076b954d530b7a4ce255a4d70d5f\`. Source Tate #103, completed theta #114, original signed Suzuki/APOLLO #110/#116; immutable source \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`. **Main, historical source and FuckingRH untouched. RH OPEN. No nontrivial zeta-zero input.**

## Real source identity that changed the RH architecture

With the *forward-over-dual* Tate convention and true unramified zeta place p:
\[
R_p(s)=\frac{1-p^{s-1}}{1-p^{-s}},\qquad
R_p(1/2)=1,\qquad |R_p(1/2+it)|=1,
\]
but
\[
\boxed{(\log R_p)'(1/2)
=-\frac{2\log p}{\sqrt p-1}
=-2\sum_{k\ge1}\frac{\Lambda(p^k)}{\sqrt{p^k}}.}
\]
These are **EXACTLY** the original arithmetic Suzuki/FUCC prime-power half-density source jets. This formula is a Tate/Mellin first derivative, not an assumed physical negative energy causing motion. The odd conductor-3 source changes sign at unramified p=2 because \(\chi_{-3}(2)=-1\); p=3 is genuinely ramified and never receives the unramified local rule.

The original real place is
\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\quad
C_\infty=-\psi(1/4)+\log\pi
\]
with \(\psi\) digamma and \(C_\infty\) the AUTHENTIC negative Brownian contact in the Weil/Suzuki APOLLO factorization. Tate Poisson ensures \(\Gamma_{\mathbb R}(s)\zeta(s)=\Gamma_{\mathbb R}(1-s)\zeta(1-s)\). Since \(\zeta(1/2)\ne0\) by the elementary positive alternating Dirichlet eta series, reflection differentiates to
\[
\boxed{\zeta'(1/2)/\zeta(1/2)=C_\infty/2.}
\]
Thus the original Brownian contact is the exact center 1-s reflection counter-slope: Archimedean local reflection slope -C, analytic zeta finite/global reflected slope +C. This is the exact source scalar normalization, NOT an all-test positive operator theorem.

## Mathematical diode/no-go: naive finite prime reflection does NOT globalize

For every finite prime cutoff P, \(\prod_{p\le P}R_p(1/2)=1\), but its center log derivative is a strictly negative sum tending to -∞ by classical \(\sum_p1/p=\infty\). On real 0<sigma<1,
\[
\lim_{P\to\infty}\prod_{p\le P}R_p(\sigma)
=\begin{cases}
+\infty&\sigma<1/2\\1&\sigma=1/2\\0&\sigma>1/2.
\end{cases}
\]
Multiplying the nonzero finite real Gamma ratio cannot repair this ordinary prime product. Correct global analytic zeta completion requires Tate's Poisson/function-space construction, not a naive inversion of the two incompatible Euler half-planes. This refutes a SOURCE REPRESENTATION, not computability of true completed zeta.

## Actual computable arithmetic residual, with source-local tail bound

For every genuine p, local reflection log expansion has jets
\[
\log R_p(s)=\sum_{k\ge1}\frac{p^{-ks}-p^{-k(1-s)}}k.
\]
At the CENTER, k>=3 half-density differentiated prime-power current is **absolutely convergent**; k=1 and k=2 diverge across p. On the FULL strip 1/4<=Re(s)<=3/4, remove first N>=7 local prime-power log terms and retain
\[
H_N(s)=\exp\sum_{p,k>N}\frac{p^{-ks}-p^{-k(1-s)}}k.
\]
This is a nonzero normally convergent holomorphic, source-prime-only reflection residual; it satisfies \(H_N(1-s)=H_N(s)^{-1}\), \(|H_N(1/2+it)|=1\). It has an ALL-HEIGHT exact truncation certificate
\[
\boxed{\left|\log H_N(s)-\sum_{p\le P,k>N}\frac{p^{-ks}-p^{-k(1-s)}}k\right|
\le\frac1{2P},\qquad P\ge16.}
\]
The lower k<=N jet counterterms still carry the nontrivial global regularization debt. This high-jet object is not the complete ζ ratio and not Weil-positive.

## Source-negative controls even stronger than a functional-equation mutant

The exact polynomial \(M_m(s)=1+\frac{16\,4^{2m}}3s(s-1)(s-1/2)^{2m}\) preserves \(M_m(1-s)=M_m(s)\), has \(M_m(0)=M_m(1)=M_m(1/2)=1\), preserves any chosen finite central jet orders 1..2m-1, but has zeros at s=1/4 and 3/4. Multiplying completed xi by this M retains symmetry, original principal pole residues and the same Gamma, but **destroys Euler multiplicativity**. Therefore reflection/Gamma/finite center derivatives cannot by themselves prove RH. The authentic von Mangoldt source and independently constructed positive feature domination remain mandatory.

Original theta Poisson \(\Theta(t)=t^{-1/2}\Theta(1/t)\) fixes the symmetric log-heat weight \(\exp(x/4)\Theta(e^x)\) even in x. This is the correct source reflective quarter-density chart; the Dirichlet reflection itself is centered at s=1/2 and has half-density p^{-k/2}. Those two exponents must be linked by the proper Mellin transform rather than identified by analogy.

**An additional true-source parity/Schur consequence:** The source real Gamma, contact and symmetric prime2 reflections preserve t->-t parity. For EVEN f the negative sinh-polar term vanishes; exact J256/Omega=217/20 arithmetic proves original completed Weil Q>||f||²/140 with 14 vanishing moments. For ODD f, inherited true Γ Fourier analysis proves Q>||f||²/20 with 16 moments. In Suzuki derivative coordinates a noncontiguous 15-low Legendre space P1..P14 plus P16 (7+8 reflection parity blocks) therefore has infinite-dimensional high QGQ>=K/140, K=(-Delta_N)^-1. This is a legitimate 15-dimensional lower Schur frontier but weaker than the 18-dimensional high K/16 alternative; old genuine gprime source gives only R0<847/80 I. Neither source-authentic 15-low sign nor all radii sign is proved. Details: `observational_succ/tate_reflection_parity_schur.py` and the parity section of the main dossier.

## Exactly what remains RH-hard

Tate's global functional equation, analytic continuation, source center contact and now a convergent high arithmetic jet can all be justified **without RH**. What SUCC lacks is a SOURCE-DERIVED low-jet/global reflection map that transports the true first/second prime-power current through the real Gamma/contact and complete Weil test space **while proving** \(E_+(v)\ge E_-(v)\), or the original source 18×18 zero-shift low Schur inequality, on every finite observation radius. The needed all-test positivity is not implied by finite local unitary phases, finite-inverse-limit coherence or large cutoffs.

**Artifacts:** full \`research/2026-10-15/TATE_CENTRAL_REFLECTION_DIODE.md\`; exact source code \`observational_succ/tate_central_reflection.py\`; tests \`tests/test_tate_central_reflection.py\`; frozen \`research/2026-10-15/TATE_CENTRAL_REFLECTION_RECEIPT.json\`; reproduce \`python scripts/tate_central_reflection_probe.py --verify\`; CI \`.github/workflows/tate-central-reflection.yml\`; claim supplement \`docs/CLAIM_SUPPLEMENT_TATE_REFLECTION_DIODE.md\`.

**Classical sources:** Tate's thesis (1950/1967); Stephen Kudla, Tate's Thesis, local/global functional equations; Terence Tao, Tate's proof of the functional equation; Masatoshi Suzuki, arXiv:2606.09096v3 (2026). Scholarly originality not claimed for classical identities; their exact coupling to original SUCC source/field and registered hostiles is new-to-project, peer review unperformed.

**RH PROVED: NO.**
