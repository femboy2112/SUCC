# Operation ONE OBJECT — Tate / Weil / Suzuki / Connes source gluing, contact defect and the honest last gate

2026-10-15. **Research branch:** research/one-object-tate-weil-suzuki-connes-2026-10-15.
**Pinned parent:** Tate draft PR #103, head 940f0a47ef25b8b553c2f0b45032b37e68c23b02; its base main 03db44203147a7b28d445bb9f970fa71360e78c4 (Phoenix II). No main changes, no independent RH-repo changes, no historic provenance rewrites. **RH PROVED: NO.** Classical Weil–Suzuki and Tate/Connes results are *imports*, not new priority claims.

## Exact objective, without a shortcut

There are **two distinct mathematical obligations**. First, source-faithfully identify the Weil functional, Suzuki's continuous screw, and any proposed Connes trace *including the identity/contact distributions and exact test domains*. Second, manufacture a **positive factorization of that very same signed object** without assuming the positivity of the target. Merely showing the first does not settle the second. A Hilbert feature map obtained by assuming the desired Gram matrices positive is circular.

Suzuki's primary source, *Weil's quadratic form via the screw function* (arXiv:2606.09096v3, Sep 2026), Eq. (1.3), §7.7, §§8.1–8.2, is the main boundary:
https://arxiv.org/pdf/2606.09096 .
Suzuki explicitly states the conditionally sufficient but **unproved** equality of an auxiliary Gram kernel with the anchored source-defined $g$ kernel (§7.7). This is our exact “last gate,” not an available theorem.

Connes' primary trace-formula source *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (arXiv:math/9811068), Theorem 3 and local trace discussion, has the local factor $|1-u|_v^{-1}$ and a prescribed **principal-value distribution** at $u=1$:
https://arxiv.org/pdf/math/9811068 .
That normalization must not be reconstructed from off-identity data by decree.

### Source architecture

    Tate local self-dual Haar, genuine p and characters
       |   (earlier PR #103 conductor/parity/phase source locks)
       v
    authentic original prime powers + one real Gamma + poles
       |
       v  W_J [signed distribution, correctly renormalized]
          ==== exact W_J(h) = -<g_J,h''>  for ALL Cc² h ====
       |
       v  even, anchored continuous Suzuki g_J ---> g (locally uniform)
          |                                          |
          +-- K_g(x,y)=g(x-y)-g(x)-g(-y)+g(0)        |
          |                                          |
          +--- exact Hilbert factor for all x,y?  [RH-hard, UNVERIFIED]
    
    independent Connes local finite p-clock / Fourier-dual trace
          -> stabilized |1-u|_p^-1 off identity [PROVED LOCAL]
          -> globally normalized principal value [UNVERIFIED]
          -> original same W as above [UNVERIFIED]
          -> noncircular positive object [UNVERIFIED]

No nontrivial zero positions are used anywhere in the construction code. The Connes clock is a declared finite **mathematical model**, not an authenticated physical measurement or a proof of a global trace formula.

## O1. Source-finite distribution/continuous-screw commuting square (CLASSICAL relation, new-to-project exact finite truncation)

Let $\mathcal D=C_c^2(\mathbb R)$ and $h\in\mathcal D$, with $h(0)=h_0$. The actual zeta source has $\Lambda(n)=\log p$ for $n=p^k$, zero otherwise. Write $b_n=\log n$, $w_n=\Lambda(n)/\sqrt n$, $\alpha_j=2j+1/2$, and $C_0=\gamma+\log(4\pi)$. For integer $J\ge0$, define the **signed finite-Gamma Weil distribution**

\[
\begin{split}
W_J(h)={}&\int_\mathbb R h(t)(e^{t/2}+e^{-t/2})\,dt\\
 &-\sum_{n=p^k\ge2}w_n[h(b_n)+h(-b_n)]-C_0 h_0\\
 &-\sum_{j=0}^{J-1}\int_0^\infty e^{-\alpha_jt}
 [h(t)+h(-t)-2e^{-t/2}h_0]\,dt .
\end{split}
\tag{O1-W}
\]
For compact $h$ the prime sum is **locally finite**. The entire omitted $t>\sup|\operatorname{supp}h|$ part of the contact subtraction is retained in each arch integral; dropping it invalidates the identity.

Set
\[
C_J=C_0+\sum_{j=0}^{J-1}\left(\frac4{4j+1}-\frac2{2j+1}\right),\qquad
r=|t|.
\]
Define the finite-source even continuous primitive
\[
\begin{split}
g_J(t)={}&-4(e^{r/2}+e^{-r/2}-2)+\frac12 C_Jr\\
 &+\sum_{n=p^k\ge2}w_n(r-b_n)_+
 -\sum_{j=0}^{J-1}\frac4{(4j+1)^2}
  (1-e^{-(4j+1)r/2}).
\end{split}\tag{O1-g}
\]
The exact **distributional** theorem is
\[
\boxed{\quad W_J(h)=-\int_\mathbb R g_J(t)h''(t)\,dt\quad
 \text{for every }h\in C_c^2(\mathbb R),\text{ every }J\ge0.\quad}
\tag{O1}
\]
This holds for *all admissible h* analytically, not just the finite numerical calibration tests.

**Direct proof:** $D^2[-4(e^{r/2}+e^{-r/2}-2)]=-(e^{t/2}+e^{-t/2})$ with no origin delta. For $b>0$, $D^2(r-b)_+=\delta_{b}+\delta_{-b}$. $D^2(C_Jr/2)=C_J\delta_0$. For $d=4j+1$, distributionally
\[
D^2\Big[-\frac4{d^2}(1-e^{-dr/2})\Big]
 = e^{-dr/2}-\frac4d\,\delta_0.
\]
Thus $-D^2g_J$ has the correct pole/prime/Gamma terms and its *total* contact coefficient is $-C_J+\sum_{j<J}4/(4j+1)$. The last coefficient equals
\[
-C_0+2\sum_{j<J}\frac1{2j+1},
\]
exactly the contact from the untruncated all-$t$ integral in (O1-W). This proves equality of distributions on $\mathcal D$. No zero-side input; no positivity presumed.

**Source uniqueness within this representation:** An even continuous distributional primitive with $g(0)=0$ and $-g''=W$ is unique. Indeed, the difference of two primitives has distributional second derivative zero, hence is affine; evenness eliminates its slope and anchoring eliminates its constant. This is representation uniqueness for a *given W*, not unique recovery of arithmetic from finitely many probes.

## O2. Canonical limit, exact rational contact and gamma-tail budget (PROVED LOCAL using classical digamma identity)

The classical digamma identity $\psi(1/2)-\psi(1/4)=\pi/2+\log2$ yields
\[
\lim_{J\to\infty}(C_J-C_0)=\frac\pi2+\log2,\quad
C_\infty=\gamma+\frac\pi2+3\log2+\log\pi
=-\psi(1/4)+\log\pi.
\]
This **exactly** matches the scalar in Suzuki Eq. (1.3). For $J\ge1$,
\[
0<C_\infty-C_J=
\sum_{j\ge J}\frac{1/4}{(j+1/4)(j+1/2)}
\le B_J:=\frac14\left[\frac1{J+1/4}+\frac1{(J+1/4)^2}\right].
\tag{O2-a}
\]
Proof: bound each summand above by $(1/4)(j+1/4)^{-2}$ and use first-term + monotone integral. The *omitted gamma potential* satisfies
\[
0\le \sum_{j\ge J}\frac4{(4j+1)^2}(1-e^{-\alpha_j|t|})\le B_J.
\]
Consequently, **uniformly on $|t|\le R$**,
\[
|g(t)-g_J(t)|\le (1+R/2)B_J,\qquad
|\langle g-g_J,h''\rangle|
\le(1+R/2)B_J\|h''\|_{L^1} .
\tag{O2-b}
\]
On each fixed compact, $g_J\to g$ uniformly; $W_J\to W$ on $C_c^2$ by the source formula with the regularized gamma kernel. Passing to the limit in (O1) gives $W=-g''$ distributionally. This is the existing classical Weil–Suzuki identification with a *new explicit finite contact matched approximation*, not a newly proved RH-relevant sign.

**Important distinction:** Original source_weil_hierarchy.py instead truncates the Gamma sum while retaining **infinite** contact $C_\infty$. That approximation is valid with its own one-sided error bounds but does **not** give (O1) exactly for finite $J$. The two finite schemes must not be silently conflated.

## O3. Source-observation and Hilbert sign are independent (EXACT COUNTERMODEL)

Let a non-Euler mutant signed distribution be $W_{\mathrm{mut}}=-w(\delta_b+\delta_{-b})$ for rational $b,w>0$. Its even anchored primitive is $g_{\mathrm{mut}}(t)=w(|t|-b)_+$. It obeys **exactly** the same distributional commuting square $W_{\mathrm{mut}}=-g_{\mathrm{mut}}''$.

But for every rational $t>b$ the anchored Gram diagonal is
\[
K_{\mathrm{mut}}(t,t)
=g_{\mathrm{mut}}(0)-2g_{\mathrm{mut}}(t)+g_{\mathrm{mut}}(0)
=-2w(t-b)<0.
\]
Hence it cannot be a Hilbert Gram kernel. **Commutation plus real/prime-looking impulses does NOT prove positivity**. This is a decisive toy mutant, not a negative witness against actual zeta. A correctly sourced W is necessary; even that does not automatically yield positive Hilbert features.

For arbitrary $g$ the necessary 2-point determinant test is
\[
K_g(x,x)K_g(y,y)-K_g(x,y)^2\ge0.
\]
The exact rational positive control $g(t)=-t^2$ has $K_g(x,y)=2xy$, rank one and PSD. Its sign-reversed twin $g(t)=+t^2$ has negative diagonals. These controls establish that the finite Gram test can distinguish positivity from source compatibility; they do **not** certify the authentic global K.

## O4. Tate/Connes local finite fixed-point trace (CLASSICAL/PROVED LOCAL)

Let $p$ be genuine, $r\ge1$, $G_r=\mathbb Z/p^r\mathbb Z$, and $u\in\mathbb Z$ with $p\nmid u$. On complex functions of $G_r$, let $(T_uf)(x)=f(u^{-1}x)$. This is a permutation with
\[
\operatorname{Tr}T_u=\#\{x:(u-1)x\equiv0\bmod p^r\}
=\gcd(u-1,p^r)=p^{\min(v_p(u-1),r)}.
\tag{O4-a}
\]
**Proof:** The endomorphism $x\mapsto(u-1)x$ on $\mathbb Z/p^r$ has kernel of size $\gcd(u-1,p^r)$ (elementary cyclic-group theorem). Its normalized finite additive Fourier $\mathcal F_r$ intertwines $T_u$ with $T_{u^{-1}}$ on the dual group: $\widehat{T_u f}(k)=\widehat f(uk)$ by variable substitution. Thus its character-basis trace equals the configuration-basis trace **without introducing a fitted spectral model**.

For $u\ne1$, $v=v_p(u-1)<\infty$ and
\[
\operatorname{Tr}T_u=p^v
=\frac1{|1-u|_p}\quad\text{for every }r>v.
\tag{O4-b}
\]
This is a lawful finite-clock *local* fixed-point coefficient matching the off-identity Connes denominator. For $u=1$, $\operatorname{Tr}T_1=p^r\to\infty$: **no ordinary limiting trace exists**.

The exact tests count fixed points independently, try prime/composite and nonunit mutants, examine $p=3,u=10$ with traces $3,9,9,9,\ldots$, and calibrate the Fourier intertwiner numerically. These finite clocks do **not** construct the Schwartz–Bruhat global adelic trace, its cutoff projections, root-number data, or the Weil positivity mechanism.

## O5. Contact-at-identity ambiguity: an obstruction shared by Weil and Connes (PROVED LOCAL / classical distributions)

Knowing a local trace kernel $|1-u|_p^{-1}$ only for $u\ne1$ does not determine a global distribution. If $T$ is any extension to test functions around $u=1$, then $T+c\delta_1$ has **identical off-identity restrictions** for every scalar $c$ but changes test values by $c h(1)$. Without an order assumption, even derivatives of $\delta_1$ may enter.

Under the chart $u=e^t$ at the positive real place, the identity $u=1$ is $t=0$, so this is the same *type* of contact ambiguity that O1 resolves through the Weil Gamma normalization. Connes' primary Theorem 3 fixes a particular principal value by requiring a Fourier-transform normalization and treating the singularity explicitly; **off-identity fixed-point counts alone do not supply it**. Do not equate an arbitrary finite trace extension with that canonical Connes distribution.

The implemented wrong-contact mutant shifts the Suzuki contact by rational $c$ and yields exactly $W_J-(-g_{J,\mathrm{mut}}'')=c\delta_0$, producing a visible $c h(0)$ defect on compact tests. This is a calibrated source-map probe; local codimension-one ambiguity is not a proof that every global Connes extension remains free.

## O6. The literal Hilbert factorization gate (CONDITIONAL; proof-equivalent strength)

The *authentic* even Suzuki $g$ determines
\[
K_g(x,y)=g(x-y)-g(x)-g(-y)+g(0)
\tag{O6-K}
\]
for all real $x,y$. If an observer/source-construction provides **a Hilbert space** $\mathcal H$ and maps $\Phi:\mathbb R\to\mathcal H$ with **exact** inner products
\[
K_g(x,y)=\langle\Phi(x),\Phi(y)\rangle_{\mathcal H}
\qquad \forall x,y\in\mathbb R,
\tag{O6-feature}
\]
then every finite anchored Gram matrix is positive semidefinite; by the classical Suzuki/Weil criterion, **RH follows**.

Conversely, under RH the authentic $K_g$ is PSD and the Moore–Aronszajn construction gives an abstract Hilbert feature map. Thus (O6-feature), without any extra source-construction restriction, is an **RH-equivalent condition**. Its exact source-derived, unconditional construction is **UNVERIFIED**. In particular, specifying a positive Hilbert inner product *by assuming $K_g\succeq0$* simply restates RH and pays no truth debt. A genuine source-faithful positive Gram factorization that survives fake-composite, wrong-Gamma, wrong-pole, conductor/parity, and non-Euler controls would be decisive.

Suzuki §7.7 formulates an even more specific sufficient identity involving an independently defined analytic family $S_x$ and its integral Gram; see the primary source. We have **not** identified our Connes local clock with Suzuki's $S_x$ nor computed this kernel identity.

### Honest dependency graph / verdict

- **Disclosed (within stated analytic domains):** O1 exact finite-stage source distribution/screw transport, O2 rational tail majorant, O3 exact non-Euler Gram obstruction, O4 finite fixed-point trace and Fourier intertwining, O5 local delta-contact ambiguity. Classical imports are separately acknowledged.
- **Observed once / TESTED NUMERICAL:** nine independent compact bump quadrature comparisons at 60-digit working precision; wrong contact mutation gives 1/3 defect. They are not directed-rounding certificates; the proof of O1 is analytic.
- **UNVERIFIED:** source-indexed global Tate Schwartz–Bruhat ↔ Connes principal-value trace equality, full source-certified Connes factorization, original infinite signed Suzuki low/30-high cross-resolvent range, uniform all-a Weil sign, Suzuki §7.7 equality, RH.
- **REFUTED shortcut:** a commuting signed distribution/screw square alone gives positive Hilbert Gram (O3); off-identity local trace fixes the contact distribution (O5).

### Verdict-changing probes and acceptance criteria

1. **Cross-normalization:** show the full Connes semilocal principal value, with its Haar, Fourier renormalization, identity/contact and all primes, equals the ORIGINAL W on a dense Schwartz–Bruhat test algebra. *Pass:* exact distribution identity and error topology. *Fail:* explicit $c h(0)$ or prime-weight discrepancy. *Ambiguous:* only finitely many values match.
2. **Positive-feature kernel:** propose $\Phi$ built without source zeros; compute its *a priori* positive Gram and prove equality with actual $K_g$ for all reals, including pole/contact and true prime jumps. *Pass:* analytic identity with all quantifiers. *Fail:* one certified negative model or one nonzero kernel residual; for genuine zeta negative K would refute RH and needs extraordinary independent audit. *Ambiguous:* finite precision PSD.
3. **Suzuki alternative:** for canonical $a=1/2$ source $G_a$ (existing PRs #85/#96), certify the 30-low original matrix and cross-resolvent range $\operatorname{Ran}B^*\subset\operatorname{Ran}D^{1/2}$ and limiting Schur $A-BD^\dagger B^*\succeq0$, **then repeat uniformly/all $a$**. *Pass* only with all necessary limits. *Fail* explicit certified original-source Rayleigh witness. *Ambiguous* fixed positive shifts.
4. **Hostile source transfer:** chi(-3) conductor, odd Gamma and missing Euler p=3, plus non-Euler Davenport–Heilbronn matched controls must reject source-blind “positivity” arguments. Finite Connes trace alone contains neither epsilon/conductor nor Weilian prime weights, so cannot pass this gate by design.

The strongest next theorem would identify **a source-constructed positive Gram factor** with the already source-identified signed $K_g$ without relying on a pre-assumed positive global $K_g$. That is the actual moonshot, with significant unpaid truth debt.

**Reproduce:**
- python -m unittest discover -s tests -p 'test_one_object_transport.py' -v
- python scripts/one_object_transport_probe.py
- python scripts/verify_provenance.py
- full repository unittest plus foundation/ordinal probes as required by AGENTS.md.
The exact code performs only authenticated source prime-power enumeration; no nontrivial zero positions enter. All numerical output is explicitly labeled calibration rather than theorem certificates.

**RH PROVED: NO.**
