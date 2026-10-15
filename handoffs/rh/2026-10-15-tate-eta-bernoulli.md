# RH handoff candidate — the true 1/24 and a two-prime-source Tate/eta transducer

**Date:** 2026-10-15. **Branch:** \`research/tate-eta-bernoulli-transducer-2026-10-15\`; parent DYSPON-SPHERE I draft #112 @ \`82b9f6730833074a778ba88c71bdef2546cc6409\`, transitively original APOLLO signed Weil source #110. **Draft only, no main change and no export to a second repository. RH PROVED: NO.**

## Decision: the tempting equality is NOT a Weil spectral theorem

The earlier restricted original Weil inequality \(\langle f,W_\zeta f\rangle>\|f\|^2/24\) was obtained by weakening the exact authentic source budget
\[
M=\frac{18140507408283703}{386282620694770800}\approx0.0469617488.
\]
Exactly the SAME proof establishes \(M>1/22>1/24\). Thus 1/24 is not the intrinsic original Weil lower margin. And it is **minus** one half zeta(-1): \(1/24=-\zeta(-1)/2\), because \(\zeta(-1)=-1/12\).

## Positive result: canonical modular regulator and exact prime-jet source split

Dedekind eta has \(q^{1/24}\prod_{n\ge1}(1-q^n)\). For \(\mathcal E_\alpha(t)=e^{-\alpha t}\prod(1-e^{-nt})\), classical \(\eta\) modular inversion gives the exact S defect
\[
\frac{\mathcal E_\alpha(t)}{\sqrt{2\pi/t}\mathcal E_\alpha(4\pi^2/t)}
=e^{-(\alpha-1/24)(t-4\pi^2/t)}.
\]
Requiring the full S transport law for ALL t forces \(\alpha=1/24\). At t=2π any alpha passes the one-point test — a literal SUCC probe-gap; T-phase alone fixes alpha modulo an integer. Rational clock tests \(t/\pi\in\mathbb Q_{>0}\) discriminate wrong alpha without evaluating an infinite q-product.

**A stronger local source probe:** The selfdual eta S value at t=2π cannot distinguish exponents, but the derivative of the logarithmic S defect is exactly `−2(alpha−1/24)`; therefore one source-typed first jet fixes the canonical exponent. Equivalently alpha = F(2π)+1/(8π) = 1/24 for the true Lambert divisor current. Wrong alpha=1/22 has exact derivative error -1/132 despite passing the S fixed-point value. This is a genuine minimal-observer repair, not an RH sign theorem.

The nonconstant logarithmic derivative is the divisor current:
\[
q\,d\log\eta/dq=1/24-\sum_{n\ge1}\sigma_1(n)q^n,\qquad
\int_0^\infty\Bigl(\sum_{n\ge1}\sigma_1(n)e^{-nt}\Bigr)t^{s-1}dt
=\Gamma(s)\zeta(s)\zeta(s-1),\quad\Re s>2.
\]
Define \(D(s)=\zeta(s)\zeta(s-1)\). A genuine Euler-product differentiation produces two TRUE prime-power clock currents:
\[
-\frac{D'}D(s)=\sum_{p,k\ge1}(1+p^k)\log(p)\,p^{-ks},\quad
-\frac{\zeta'(s-1)}{\zeta(s-1)}
=\sum_{p,k\ge1}p^k\log(p)\,p^{-ks}.
\]
**Subtract the declared shifted current**: this exactly reproduces the original \(-\zeta'/\zeta(s)\) prime tape. No zeros are read; the output has vanishing coefficients at every non-prime-power n, including 6.

An independent exact integer/Dirichlet-inverse oracle reconstructs every coefficient of both log derivatives in the formal prime-log basis, verifying \((1+n)-n=1\) for true \(n=p^k\). A mutant \(\sigma_1(6)+1\) yields a detectable wrong \(\log2+\log3\) at composite 6. The original source and wrong Euler mutant cannot be confused.

The modular \(\eta\) log-derivative also gives an exact reciprocal Lambert-series identity
\[
F(t)=\frac1{24}-\frac1{2t}+\frac{\pi^2}{6t^2}
-\frac{4\pi^2}{t^2}F(4\pi^2/t),\qquad
F(t)=\sum_{n\ge1}\sigma_1(n)e^{-nt},
\]
which yields \(F(2\pi)=1/24-1/(8\pi)\). All are classical identities; new-to-SUCC integration and adversarial tests are not claims of academic priority.

**Second structural obstruction (exact, no zero lookup):** Eta's 24th power is the cusp discriminant `Delta=q-24q²+252q³-...` with Ramanujan tau coefficients, whereas the *logarithmic derivative* is Eisenstein E2 with sigma1 coefficients. These are distinct L-series and cannot be identified. Furthermore `X(s)=xi(s)xi(s-1)` obeys `X(2-s)=X(s)`, but each abstract xi zero rho contributes two shifted families rho and 1+rho; even assuming RH these are tracks Re=1/2 and 3/2, not the symmetry center 1. Any putative RH-positive single-track form must first lawfully remove the shifted arithmetic channel.

## What is STILL RH-hard

The completed zeta real Gamma \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\), half-density, two completed poles, contact \(C_\infty=-\psi(1/4)+\log\pi\), and fully signed Weil distribution **do not arise automatically** from eta's \(\Gamma(s)\zeta(s)\zeta(s-1)\). The current Euler series is initially valid only on Re(s)>2; setting \(s=1/2+it\) termwise is invalid. In particular, the prime-2 negative two-bump family from DYS-07 remains a genuine signed-kernel adversarial control.

A modular/current identity is **not** an independently justified positive Hilbert contraction. Nothing in this handoff proves all-test original Weil positivity, the Suzuki global limit, or RH.

## Next mathematical experiment

Build one test-domain-preserving Tate Schwartz–Bruhat map \(\mathcal E\) from the two-current divisor source through its exact Archimedean factor/conductor data to the **original full signed zeta Weil form** (both poles, contact and half-density). Independently construct either a source-positive comparison or PR #109's genuine 30×30 zero-shift residual Schur certificate for the first-prime interval, and force a wrong eta exponent, wrong Gamma, fake 6, non-Euler twisted source, and true negative prime-2 bump to discriminate the construction. If the desired sign is used to build the object, reject as circular.

**Artifacts:** full theorem \`research/2026-10-15/TATE_ETA_BERNOULLI_TRANSDUCER.md\`; code \`observational_succ/tate_eta_bernoulli.py\`; tests \`tests/test_tate_eta_bernoulli.py\`; deterministic receipt \`scripts/tate_eta_bernoulli_probe.py --verify\`; source checks \`.github/workflows/tate-eta-bernoulli.yml\` and \`docs/CLAIM_SUPPLEMENT_TATE_ETA_BERNOULLI.md\`.

**Primary references:** NIST DLMF §§25.6, 27.14, 23.17, 23.18; Suzuki arXiv:2606.09096v3. New mathematical ideas/academic originality unverified. **RH PROVED: NO.**
