# Local prime gaps, global analytic continuation, and the Archimedean zeta transport

**Date:** 2026-10-11. **Origin:** the maintainer argues that analytic continuation gives a coherent value for a divergent path, and specifically notices the Euler factor \((1-p)^{-1}\) at \(s=-1\). **Status:** classical zeta mathematics plus exact source-mutant and finite-cutoff tests. **Not** a theorem about RH nontrivial zeros or gravitational holography.

**Primary sources:** [NIST DLMF 25.2](https://dlmf.nist.gov/25.2) (series, Euler product, continuation), [25.4](https://dlmf.nist.gov/25.4) (functional equation, completed \(\xi\)), [25.6](https://dlmf.nist.gov/25.6) (special values and Bernoulli numbers), and [27.4](https://dlmf.nist.gov/27.4) (Euler product requires absolute convergence). These theorems are independent source inputs, not claims proved by the tests.

## 1. What can be continued, and in what order?

For \(\Re(s)>1\),
\[
\zeta(s)=\sum_{n=1}^{\infty}n^{-s}
=\prod_p E_p(s), \quad E_p(s)=(1-p^{-s})^{-1}.
\]
At \(s=-1\), the original partial sums \(1+\cdots+N=N(N+1)/2\) diverge to \(+\infty\). The *globally analytically continued function* nevertheless satisfies \(\zeta(-1)=-1/12\). This is a valid zeta-regularized assignment, not the ordinary sum.

Each individual local Euler factor can also be analytically continued, with
\[
E_p(-1)=\frac1{1-p}=-\frac1{p-1}.
\]
The denominator is precisely the maintainer's first FUCC prime-jet/SUCC-carrier return gap \(\tau_{p,0}=p-1\), more generally \(\tau_{p,k}=(p-1)p^k\). It is also Euler's \(\varphi(p)\), the number of units of \(\mathbb F_p\). These are exact local arithmetic identifications, NOT independently an Archimedean completion.

**CRUCIAL NONCOMMUTATION (elementary theorem):** For cutoff X,
\[
Q_X=\prod_{p\le X}E_p(-1)
=\frac{(-1)^{\pi(X)}}{\prod_{p\le X}(p-1)}
\longrightarrow0,
\]
as infinitely many primes at least 3 contribute factors of modulus at most 1/2. Thus
\[
\boxed{\operatorname{AC}\big(\prod_p E_p\big)(-1)=-1/12
\quad\ne\quad
\lim_{X\to\infty}\prod_{p\le X}\operatorname{AC}(E_p)(-1)=0.}
\]
The second expression means only the finite-prime-cutoff limit, not a nonzero-convergent Euler product. **Global continuation and infinite assembly cannot be swapped outside the original domain.** This is an exact negative control for careless SUCC transport across local and global frames.

### 1b. The stronger SUCC/FUCC relation: an existing ax+b semigroup

This local \((1-p)\) factor has an even more precise **operator-algebraic** connection to the maintainer's SUCC/FUCC operators. Acting on integer addresses, let
\[
S(n)=n+1,\quad V_p(n)=pn.
\]
Then
\[
S V_p(n)=pn+1,\quad V_p S(n)=pn+p,
\]
so the **address difference** is
\[
\boxed{S V_p(n)-V_p S(n)=1-p.}
\]
At the Hilbert-space level the true relation on the canonical orthonormal basis is
\[
\boxed{V_p S=S^p V_p.}
\]
The two sides map \(|n\rangle\) to the **same** ket \(|pn+p\rangle\). The genuine operator commutator is \([S,V_p]|n\rangle=|pn+1\rangle-|pn+p\rangle\), **not** the scalar \((1-p)|n\rangle\). The \(p-1\) extra SUCC steps are the exact cost of moving a prime dilation past a unit shift.

**Falsification/source control:** For **every composite** integer \(q\ge2\), the same ax+b relation \(V_q S=S^q V_q\) and address defect \(1-q\) hold. In particular, 6 yields defect -5 but 6 is *not* an independent Euler prime factor. Therefore the affine commutation law ALONE does not recover primality, an Euler product, the Gamma completion, or RH. Unique factorization and authentic prime-supported Euler data remain additional premises.

**Strong independently established connection:** Joachim Cuntz, *C*-algebras associated with the ax+b-semigroup over N*, 2006, [arXiv:math/0611541](https://arxiv.org/abs/math/0611541), explicitly develops the shift/dilation semigroup on \(\ell^2(\mathbb N)\), connects its \(C^*\)-algebra to the Bost–Connes number-theoretic construction, and realizes a related stabilized \(C^*\)-algebra through crossed products of **finite-adèle functions** and, separately, functions on the **real Archimedean completion**. Cuntz's original construction uses additional quotient/analytic relations; the raw SUCC/FUCC isometries alone do NOT automatically prove an isomorphism of those completed algebras.

This is an **actual published mathematical finite↔Archimedean relation in the same ax+b family**. It raises a serious future path: identify the precise operator algebra, quotient/representation, regularity, dynamics and source-specific zeta partition function, then see whether its legitimate analytic completion carries the relevant Weil-form structure. No such bridge is proved by the present prime-gap arithmetic tests, and there is no claim of academic priority.

## 2. The lawful global transport uses the Gamma/Archimedean completion

The classical functional equation is
\[
\zeta(s)=2(2\pi)^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\]
At \(s=-1\) this gives the source-specific bridge
\[
\boxed{\zeta(-1)=-\frac{\zeta(2)}{2\pi^2}
=-\frac1{2\pi^2}\prod_p(1-p^{-2})^{-1}=-\frac1{12}.}
\]
Here the prime Euler product at \(2\) **really converges**. The Archimedean factor is enforced by the functional equation, not guessed by formally multiplying \((1-p)^{-1}\).

The completed object \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) satisfies \(\Lambda(s)=\Lambda(1-s)\); in particular,
\[
\Lambda(-1)=\Lambda(2)=\pi/6.
\]
The Riemann \(\xi\)-function additionally includes \(s(s-1)/2\); \(\Lambda\) itself has poles at 0 and 1.

**Classical family, not an isolated coincidence:**
\[
\zeta(1-2m)=
\frac{2(-1)^m(2m-1)!}{(2\pi)^{2m}}\zeta(2m)
=-\frac{B_{2m}}{2m}.
\]
For \(m=1,2,3\), this yields \(-1/12,1/120,-1/252\). The exact code checks six Bernoulli values. No nontrivial zeros are accessed.

## 3. Quantitative finite-prime transport with a proved bound

Let \(P_X=\prod_{p\le X}(1-p^{-2})^{-1}\) for integer cutoff \(X\ge2\). The missing prime factors are a subset of all integers greater than X, so
\[
1\le\zeta(2)/P_X
=\prod_{p>X}(1-p^{-2})^{-1}
\le\prod_{n=X+1}^{\infty}(1-n^{-2})^{-1}
=(X+1)/X.
\]
The all-integer product telescopes exactly:
\[
\prod_{n=X+1}^{M}\frac{n^2}{(n-1)(n+1)}
=\frac{M(X+1)}{X(M+1)}.
\]
Define the finite source-derived transported approximation \(V_X=-P_X/(2\pi^2)\). The functional equation and \(\zeta(2)=\pi^2/6\) now imply the RIGOROUS estimate
\[
\boxed{0<V_X-\zeta(-1)\le1/(12X).}
\]
The implemented prime products \(P_X\) and error coefficient are exact Fractions. Floating results are display-only. This **does not** compute a physically infinite process; it applies a known global theorem to a finite source-specific product with an explicit tail bound.

The locally continued product instead starts \(-1,+1/2,-1/8,+1/48,-1/480\) for prime cutoffs 2,3,5,7,11 and heads toward zero.

## 4. Independent Abel transport and arithmetic source mutations

Let \(\eta(s)=(1-2^{1-s})\zeta(s)\), initially an identity in the Dirichlet convergence domain, then valid by analytic continuation. At s=-1 the Abel-regularized alternating walk satisfies
\[
R(r)=\sum_{n\ge1}(-1)^{n-1}nr^n=\frac{r}{(1+r)^2},
\quad0\le r<1,
\]
with **exact** error
\[
1/4-R(r)=\frac{(1-r)^2}{4(1+r)^2}.
\]
Hence \(\eta(-1)=1/4\) and \(\zeta(-1)=\eta(-1)/(1-4)=-1/12\). This is another lawful continuation protocol—not the ordinary sum.

**Hostile p=2 deletion:** Set \(F(s)=(1-2^{-s})\zeta(s)\), a genuine Euler-source mutation. Then
\[
F(-1)=(1-2)(-1/12)=+1/12,
\quad F(2)=(3/4)\zeta(2).
\]
If one incorrectly applies the **unmodified zeta** Gamma/reflection coefficient to F, it predicts
\[
-F(2)/(2\pi^2)=-1/16\ne+1/12.
\]
So the global transport is not a universal correction that can be pasted onto arbitrary prime products. Its arithmetic source identity and functional-equation hypotheses are load-bearing. Inserting a fake composite “p=6 Euler factor” similarly changes the source product and is rejected as an authentic prime.

## 5. Claims, limits and next decisive questions

- **O128 CLASSICAL / TESTED MODEL:** \(E_p(-1)=-1/(p-1)\), the negative inverse first prime-jet SUCC return gap.
- **O136 CLASSICAL / PROVED LOCAL / TESTED MODEL:** the exact ax+b relation `V_p S=S^p V_p` and address-level discrepancy `SV_p(n)-V_pS(n)=1-p` connect the local Euler denominator to shift–dilation noncommutation. The same relation holds for composite q, so it is not a prime-selection/Euler-source theorem.
- **O129 PROVED LOCAL:** locally continued prime-factor cutoff product tends to zero and is not global \(\zeta(-1)\).
- **O130 CLASSICAL:** completed zeta/functional equation relates the continued \(-1\) to the convergent Euler product at \(2\).
- **O131 PROVED LOCAL conditional on the classical global theorems:** finite prime cutoff yields \(V_X\) with absolute error ≤1/(12X).
- **O132 CLASSICAL / TESTED MODEL:** Abel eta at -1 yields 1/4 with exact quadratic deficit, transporting to -1/12.
- **O133 CLASSICAL / TESTED MODEL:** the functional equation transports the entire negative odd-integer family to positive even values; six exact Bernoulli values checked.
- **O134 REFUTED:** a source-mutated Euler function necessarily inherits unmodified zeta's Archimedean reflection coefficient; p=2 removal is a precise counterexample.
- **O135 UNVERIFIED:** this special-value transport proves a source-derived full Weil-positive form, RH, a physical holographic boundary or intrinsic proof inability.

**Next tests:** Construct a source-derived operator-valued finite-Euler/Gamma transport on valid test-function domains, with genuine/mutated Euler sources and a strict *no nontrivial-zero-reading* rule. Ask whether the required *global* commutation is provable on a nontrivial source category, rather than merely on isolated special values. Develop a controlled connection to SUCC/FUCC prime clocks; do not infer all-zero critical-line constraints from \(\zeta(-1)\) alone.

**Verdict:** A divergent path can have a uniquely and coherently associated analytically continued value. The formal \((1-p)^{-1}\) factors make the first prime SUCC gap visible but their naive product **fails**. The global Gamma/reflection relationship is the actual mathematical bridge between the authentic convergent prime product and \(-1/12\). This is a defensible, classical calibration of the maintainer's local-versus-global mathematical transport intuition.
