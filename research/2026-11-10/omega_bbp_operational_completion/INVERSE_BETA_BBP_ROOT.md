# Reverse-beta folding of the authentic BBP tree: two roots and a faithful Mellin witness

**2026-11-10 · Research continuation of #579 · Corrects the earlier misinterpretation of the user's Omega proposal.**

## 0. The actual question

Do **not** begin with raw head-unsolvable \(\Omega_3\) and label its steps with arbitrary BBP arithmetic. First expand the **source's own** infinite computation, observe its repeated index-shifted contexts, and *inverse-beta fold / higher-order anti-unify* those contexts into a finite parameterized recursive root. In an untyped lambda calculus the root can be presented as an application of two identical self-referential terms. A fixed-point equation is a finite **cyclic description**, not a finite full beta normal form. The infinite arithmetic value is determined by a declared semantic boundary condition, not by beta-reduction alone.

This note constructs two source-faithful roots, proves an exact injective intertwining between them, and exhibits the remaining inverse-observer instability. It does **not** prove digit equidistribution.

## 1. Direct inverse-beta fold of the full four-pole source

Define
\[
R(n)=\frac4{8n+1}-\frac2{8n+4}-\frac1{8n+5}-\frac1{8n+6},
\quad
\pi=\sum_{n\ge0}16^{-n}R(n).
\]
This matches the frozen source \(r(j)=R(j-1)\). Its *computational* unfolding is
\[
R(0)+16^{-1}\big(R(1)+16^{-1}(R(2)+\cdots)\big).
\]
The invariant context is **not** equality of the numeric leaf labels \(R(n)\); it is equality *after the successor transport* \(n\mapsto n+1\).

Set
\[
F(g)=\lambda n.\big(R(n)+16^{-1}g(n+1)\big),\qquad
w_F=\lambda z.F(zz),\qquad W_F=w_Fw_F.
\]
One ordinary beta contraction yields the exact operational equality
\[
W_F\to_\beta F(W_F).
\]
By unfolding at index 0, \(W_F(0)\) presents the full BBP tree. Reading the tree backward, abstract the recurrent subtree into \(g\), abstract the clock into \(n\), and introduce \(w_Fw_F\) at the root. **This is the intended reverse-folding mechanism.** In a lazy or guarded implementation, each finite approximation is productive; an eager evaluation of raw \(W_F\) can diverge. \(\beta\)-conversion neither proves arithmetic convergence nor selects a real-valued solution.

For clarity, this is the self-application skeleton of the classical Curry \(Y\) construction, with the *source-dependent context \(F\)* acting as the guard; it is not SUCC's independent \(\Omega_3\) length-growth experiment.

On the Banach space \(\ell^\infty(\mathbb N_0)\),
\[
\|F(g)-F(h)\|_\infty\le\frac1{16}\|g-h\|_\infty.
\]
There is a unique **bounded** real-valued solution
\[
B(n)=\sum_{j\ge0}16^{-j}R(n+j),\qquad B(0)=\pi.
\]
Outside the bounded class there is an exact family of counterfeit roots
\[
B_C(n)=B(n)+C16^n.
\]
All solve \(B_C(n)=R(n)+B_C(n+1)/16\). The boundedness or equivalent boundary condition \(\lim_{n\to\infty}16^{-n}B_C(n)=0\) pays the homogeneous-mode selection. A syntactic reverse fold alone cannot select \(C=0\).

## 2. A deeper source-specific root: integrate the four poles *before* folding

Use \(\int_0^1 x^{8n+a-1}\,dx=1/(8n+a)\) to show
\[
R(n)=\int_0^1x^{8n}P(x)\,dx,\qquad
P(x)=4-2x^3-x^4-x^5.
\]

**Exact source factorization:**
\[
\boxed{P(x)=(1-x)(x^2+2)(x^2+2x+2).}
\]
This includes *all four* signed poles. In particular \(P(1)=0\), the first denominator-asymptotic moment cancels, and
\[
R(n)\sim\frac{15}{64n^2}\quad(n\to\infty).
\]
Both quadratic factors are positive on the integration interval. The Gaussian norm \((x+1)^2+1\) occurs in the final factor; \(x^2+2\) belongs to a different imaginary-quadratic norm pattern. Do not misidentify them as identical Gaussian factors.

Now expand the infinite BBP tree inside the integral:
\[
\pi=\int_0^1 P(x)\Big(1+\frac{x^8}{16}
+\Big(\frac{x^8}{16}\Big)^2+\cdots\Big)\,dx.
\]
Define the new computational operator on \(C([0,1])\):
\[
(Gf)(x)=P(x)+\frac{x^8}{16}f(x).
\]
It is a \(1/16\)-contraction, hence has the unique fixed point
\[
\boxed{K(x)=\operatorname{Fix}(G)(x)=
\frac{(1-x)(x^2+2)(x^2+2x+2)}{1-x^8/16}.}
\]
The equivalent omega-shaped self-application is \(w_G=\lambda z.G(zz)\), \(W_G=w_Gw_G\to_\beta G(W_G)\). This is a *nontrivial* reverse fold: the unbounded index \(n\) has disappeared into the multiplicative geometric operator \(x^8/16\), and the full four-pole source is preserved in \(P(x)\).

The standard BBP identity then gives \(\int_0^1K(x)\,dx=\pi\). The integral identity is not the result of beta-reduction alone; termwise integration is justified by uniform convergence of \(\sum_j(x^8/16)^j\).

## 3. Exact arithmetic–analytic intertwiner (the proof-relevant arrow)

Define the sampled Mellin/Hausdorff moment observer
\[
(\mathcal M f)(n)=\int_0^1x^{8n}f(x)\,dx.
\]
Then **for every continuous \(f\) and every \(n\ge0\)**,
\[
\begin{aligned}
(\mathcal M\,Gf)(n)
&=R(n)+\frac1{16}\int_0^1x^{8(n+1)}f(x)\,dx\\
&=(F\,\mathcal M f)(n).
\end{aligned}
\]
Thus
\[
\boxed{\mathcal M\circ G=F\circ\mathcal M,\qquad
\mathcal M(K)=B.}
\]
This is an **exact, source-labelled, computational commuting square** between two genuinely different roots of the same unfolded BBP tree. It was derived from the four poles and the index shift, rather than decorating a generic \(\Omega\) clock.

**Faithfulness theorem:** \(\mathcal M:C([0,1])\to\ell^\infty(\mathbb N_0)\) is injective. Indeed, \(x\mapsto x^8\) is a homeomorphism of \([0,1]\); polynomials in \(x^8\) are uniformly dense in \(C([0,1])\) by Weierstrass. If all moments of a continuous \(f\) vanish, then \(\int f\,g=0\) for every continuous \(g\); choosing \(g=\overline f\) gives \(\int|f|^2=0\), so \(f=0\).

The original completed BBP tail is **exactly** the moment of this folded rational root:
\[
\boxed{T_n=\sum_{j\ge1}16^{-j}r(n+j)
=\frac1{16}B(n)=\frac1{16}(\mathcal M K)(n).}
\]
Hence for the authentic zero-seed prefix \(U_0=0,\ U_{n+1}=16U_n+r(n+1)\),
\[
\boxed{U_n+\frac1{16}(\mathcal M K)(n)=16^{n-1}\pi.}
\]
This is a precise equality between a terminating *finite rational computation* and a *source-derived analytic fixed-point computation*, with a nontrivial faithful moment observer. It is the proposed computational-arithmetic weld, now at the level of an actual source-specific square.

**Not an equivalence:** \(\mathcal M\) is injective but not onto all bounded sequences, and the inverse on its image is not bounded in the natural sup norms.

## 4. Exact instability of the inverse pinbed

Set \(f_k(x)=\sin(2\pi kx)\) for positive integers \(k\). Then
\(\|f_k\|_\infty=1\). By integration by parts, uniformly over \(n\ge1\),
\[
\left|\int_0^1x^{8n}\sin(2\pi kx)\,dx\right|
\le\frac{1}{\pi k};
\]
for \(n=0\) the moment is zero. Consequently
\[
\boxed{\|\mathcal M f_k\|_{\ell^\infty}\le1/(\pi k)\to0
\quad\text{while}\quad\|f_k\|_\infty=1.}
\]
**The all-index observer separates continuous functions but does not admit a uniformly stable inverse on its full image.** This is a precise reason why equality after completion does not permit finite-slice or frequency-window identification without explicit precision payment. It does not rule out better-conditioned inverse results on the much narrower BBP source-generated class.

## 5. Real proof gap: syntax folding is solved; source-selected phase remains open

The constructive achievements here are source-specific \(R\to P\), two contraction roots, an injective indexed-Mellin intertwiner, a literal four-pole factorization, and the exact prefix–moment tail equality. They are **not** merely a count-only \(\Omega_3\) simulation.

Still unverified:
- a *faithful typed lambda compiler* whose actual reduction addresses and cost/clock trace preserve the source terms and the integer carry observer (a paper-level equation is not yet such a compiler);
- a source-specific estimate on the signed digit orbit \(e(h16^{n-1}\pi)\) or on the corresponding complete carry/parity cocycle, rejecting wrong seeds; the contraction and analytic moments do not imply statistical cancellation;
- any claim of uniqueness of the *syntactic* inverse-beta root: it is semantically unique only after the function space and boundary conditions are fixed.

The immediate discriminating experiment is to build the AST of the exact four-pole prefix recurrence, anti-unify the shifted subtrees into \(F\), and independently anti-unify the integrated expansion into \(G\). Verify step-by-step \(\mathcal M\circ G=F\circ\mathcal M\) and finite arithmetic moment identities, then test a source mutation. A zero-forcing \(\Omega\) tree also contracts, but it does not have the source factorization \(P=(1-x)(x^2+2)(x^2+2x+2)\).

**Claim ledger:** source polynomial factorization, fixed-point equations, moment intertwiner, injectivity, inverse-instability counterexample, and tail identity: **PROVED PAPER** (with finite exact checks below); faithful concrete AST/lambda compiler: **UNVERIFIED**; zero-seed parity balance and full hexadecimal normality of \(\pi\): **OPEN**.

**References:** [original BBP formula](https://mathworld.wolfram.com/BBP-TypeFormula.html); [Curry fixed-point combinator derivation (UPenn)](https://www.seas.upenn.edu/~cis5110/notes/cis511-c-sl4.pdf); [SUCC current frontier](../../../docs/PI_NORMALITY_FRONTIER.md). This construction is not claimed to be novel relative to all classical BBP integral manipulations; its role is to correct SUCC's operational modeling.