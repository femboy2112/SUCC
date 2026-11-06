# Operation PRIME-JET × GAUSSIAN SOURCE GAUGE: signed energy bands, critical line and arithmetic fiber

**2026-11-05.** Research-only additive descendant of SUCC draft #516 (pinned parent 56747eb11cd56de7a6f75dfbbab3cb94721d0427), which contains #515 Gamma/sphere and #499 prime-character primal. Original SUCC BBP forcing, literal U_0=0, archived proofs, Lean, production, workflows and main are untouched. These are classical identities and a new-to-SUCC composition, NOT a claim of worldwide novelty, physical negative energy, Hilbert–Pólya operator, RH, or π normality.

**Chronology:** PJ-01–04 and the nonextension argument were development deductions BEFORE PREREGISTRATION.md; the prime-log16 resonance, two-sheeted fiber repair and sharp smooth boundary estimate were refined AFTER preregistration. Finite tests validate implementations, not universal theorems; all universal statements below have separate derivations.

## 1. Typed source map: not all “prime jets” are identical

There are THREE distinct sources/operators:
- Zeta Euler-product prime power p^k with logarithmic displacement a=k log p and exact weight w=(log p)p^(-k/2), entering the classical Guinand–Weil explicit formula;
- SUCC original, zero-seeded rational BBP forcing r_o(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U_n=16U_(n-1)+r_o(n), whose Gaussian primal from #499 carries a χ_{-4} prime-class character in a rational eight-tap source module;
- Dirichlet-character-twisted prime powers, corresponding to *another* L-function (e.g. Dirichlet beta for χ_{-4}), with different gamma completion. Comparing their source actions is permitted. Equating these three operators without an intertwiner is NOT.

Let I=(-L,L), D=2L and H_L=L²(I,dx). For a>0 define the ZERO-EXTENDED partial translation S_a on H_L:
\[
(S_af)(x)=\mathbf1_I(x-a)\,f(x-a),\quad x\in I.
\]
Its adjoint is (S_a^*f)(x)=\mathbf1_I(x+a)f(x+a).

## 2. PJ-01: a prime power really contributes a SIGNED self-adjoint form

For each p prime and k>=1, put
\[
a_{p,k}=k\log p,\quad w_{p,k}=(\log p)/p^{k/2}>0,\qquad
\boxed{J_{p,k,L}=-w_{p,k}(S_{a_{p,k}}+S_{a_{p,k}}^*).}
\]
This is bounded self-adjoint. For f∈C_c∞(I), define g=f*\widetilde f, with \widetilde f(x)=\overline{f(-x)}. A direct change of variables gives
\[
g(a)=\int f(x)\overline{f(x-a)}dx,\quad
\boxed{\langle f,J_{p,k,L}f\rangle=-2w_{p,k}\operatorname{Re}g(a).}\tag{PJ1}
\]
This is EXACTLY the arithmetic p^k term in the Guinand–Weil explicit formula in the Fourier convention below. The prime term vanishes for a>=2L, so for any fixed compact support there are only finitely many contributing prime powers.

It is NOT negative semidefinite: choose two equal-shaped disjoint packets f0,f1=f0(.-a), with matching phases. On their span, the compression of J is the 2×2 Hermitian matrix [[0,-w],[-w,0]] with eigenvalues ±w. The normalized symmetric vector has expectation -w, and the antisymmetric vector +w. A constant-mode spectral “negative energy reservoir” therefore exists only as a signed interaction, not as a universal physical energy stored in each prime.

## 3. PJ-02: exact finite-window quantized bands and infinite-clock limit

Use the translation x↦x+L to replace I by (0,D). Disintegrate L²(0,D) along residue r mod a:
\[
x=r+j a,\quad 0\le r<a,\quad
m(r)=\#\{j\ge0:r+ja<D\}.
\]
Up to null sets this is a unitary direct integral of finite-dimensional chains \(\mathbb C^{m(r)}\). The operator S_a+S_a* on each fiber is the adjacency matrix of a path on m(r) vertices. The standard sine eigenvectors yield exactly
\[
\boxed{\operatorname{spec}(J|_{\text{fiber }m})
=\left\{-2w\cos\frac{\pi j}{m+1}:j=1,\ldots,m\right\}.}\tag{PJ2}
\]
For a>=D, J=0. For 0<a<D, if D/a is an integer q, almost all fibers have m=q; otherwise fibers of lengths floor(D/a) and ceil(D/a) occur on positive-measure sets (ignore a length-zero fiber). Each level has infinite Hilbert-space multiplicity due to the residue continuum; “quantization” refers to the finite SET of level values, not a finite Hilbert-space dimension.

The **sharp operator norm** for 0<a<D is
\[
\boxed{\|J_{p,k,L}\|=
2w_{p,k}\cos\left(\frac{\pi}{\lceil 2L/a_{p,k}\rceil+1}\right).}\tag{PJ3}
\]
The bound is attained in arbitrarily accurate norm by fields supported on longest fibers. At the onset a=D, J=0, while for any D>a arbitrarily close to a, \(\|J\|=w\): the operator norm has a jump across the support threshold. This is real, not a numerical artifact.

On H=L²(R), the uncompressed bilateral shift has Fourier multiplier
\[
\widehat J(\xi)=-2w\cos(a\xi),\qquad
\operatorname{spec}(J)=[-2w,2w].
\]
As L→∞, the finite path eigenvalues become dense in that interval. This gives a **precise finite-window discrete levels → continuous band** mechanism, independently of SUCC #516's different, chosen solenoid operator \(q\mapsto\kappa q^2\) or its sphere-monopole levels. NO intertwining theorem between those Hilbert spaces has been established.

### Smooth observation cost at the threshold

The norm jump does not produce an O(w) effect for fixed-regularity smooth probes. If D=a+δ with 0<δ<a, and \(f\in H^1_0((0,D))\), then
\[
g(a)=\int_0^\delta f(x+a)\overline{f(x)}dx.
\]
Each boundary restriction satisfies \(\|f\|_{L^2(0,\delta)}\le\delta\|f'\|_2\) and \(\|f\|_{L^2(D-\delta,D)}\le\delta\|f'\|_2\), by the fundamental theorem of calculus and Cauchy–Schwarz. Thus
\[
\boxed{|\langle f,Jf\rangle|
\le 2w\,\delta^2\|f'\|_2^2.}\tag{PJ4}
\]
Consequently saturating the new negative jet at arbitrarily narrow δ forces derivative/observer cost to grow at least on order 1/δ for normalized packets. This **boundary-layer conditioning** connects to SUCC's general observation-cost theme, NOT to a physical Casimir energy.

## 4. PJ-03: the critical zeros appear in the FULL completed balance

For \(f\in C_c^\infty((-L,L))\), let \(F(z)=\int_\mathbb R f(x)e^{izx}dx\) and \(h(z)=F(z)\overline{F(\bar z)}\). Put
\[
\Omega(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi,\qquad\psi=\Gamma'/\Gamma.
\]
The classical Guinand–Weil explicit formula, with zeros counted with multiplicity and proper symmetric summation, gives
\[
\boxed{\sum_\rho h((\rho-\tfrac12)/i)
=h(i/2)+h(-i/2)
+\frac1{2\pi}\int_\mathbb R |F(t)|^2\Omega(t)\,dt
+\sum_{p^k<e^{2L}}\langle f,J_{p,k,L}f\rangle .}\tag{PJ5}
\]
The pole terms are absent when F(±i/2)=0. Under RH, every nontrivial zero is \(\rho=1/2+i\gamma\), so the left side is \(\sum_\gamma|F(\gamma)|^2\ge0\). The established Weil positivity criterion is an equivalence with RH when asserted for the ENTIRE appropriate admissible test class, not for a few finite levels. The Gamma and pole terms, different prime powers and sign-sensitive correlations are mandatory. Negativity of ONE J neither contradicts nor proves RH.

Classical independent anchors: E. Bombieri, “Remarks on Weil’s quadratic functional in the theory of prime numbers,” 2000, https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0 ; P. Garrett, “Guinand’s explicit formula,” https://www-users.cse.umn.edu/~garrett/m/complex/notes_2020-21/12g_guinand_explicit_fml.pdf ; Connes–Consani, “Weil positivity and Trace formula, the archimedean place,” https://arxiv.org/abs/2006.13771 ; A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” https://arxiv.org/abs/math/9811068 . Connes's absorption-spectrum interpretation is a serious existing program, not an achieved identification of the J eigenvalues with critical zeros.

## 5. PJ-04: the prime log clock aligns EXACTLY with SUCC's base-16 sphere scale

Let \(\Lambda=\log16\), and take the quotient real logarithmic circle R/ΛZ that already appears in SUCC #515's Gamma solenoid. A prime shift advances this circle by \(a_p=\log p\).

- p=2 gives \(\log2/\Lambda=1/4\), a finite cyclic four-step rotation.
- For any odd p, \(\log p/\Lambda\) is irrational, because a rational relation would give \(p^a=2^{4b}\) for nonzero integers a,b, contradicting unique factorization.
- More strongly, for distinct odd primes p1,…,pr, the list \(1,\log p_1/\Lambda,\ldots,\log p_r/\Lambda\) is Q-linearly independent: exponentiating any cleared integer relation yields \(16^{a_0}\prod_i p_i^{a_i}=1\), forcing all a_i=0. By Kronecker–Weyl, their **auxiliary common-iterate** orbit \(n(\log p_1/\Lambda,\ldots,\log p_r/\Lambda)\mod1\) is equidistributed on the r-torus.

This is a genuine arithmetic distinction between the base-16 2-primary clock and odd-prime clocks. It is NOT the chronological BBP orbit \(e(U_n)\), not a zeta-zero distribution, and it does not by itself produce Weil positivity.

## 6. PJ-05: χ_-4 prime-class “gauge coding” is not absorbable in a real phase

SUCC #499 proves a genuine rational source action S_a on all eight-tap sources with angular eigensource \(\chi_{-4}(a)\) and radial trivial eigensource. On the SEPARATE test Dirichlet-character model \(\chi=\chi_{-4}\), twist the odd-p prime jet by
\[
J_{p,k}^{\chi}=-w_{p,k}\left(\chi(p)^k S_a+\overline{\chi(p)^k}S_a^*\right).
\]
Each SINGLE odd-prime jet is unitarily equivalent to its untwisted version, and hence has the same set of levels (multiply the jth residue-chain coordinate by χ(p)^{-kj} or conjugate as convention requires). But ALL these arithmetic twists cannot be removed by a SINGLE continuous ARCHIMEDEAN gauge.

**Sharp no-extension theorem.** Let \(G=\{\log(m/n):m,n\text{ positive odd integers}\}\subset\mathbb R\), and define the well-defined multiplicative-sign character \(\chi_G(\log(m/n))=\chi_{-4}(m)\chi_{-4}(n)\). This is a homomorphism \(G\to\{\pm1\}\). Set
\[
\delta_j=\log\frac{4j+3}{4j+1}\to0,\qquad
\chi_G(\delta_j)=-1\quad(j\ge1).
\]
Therefore \(\chi_G\) is discontinuous at zero in the relative real topology, hence has **no continuous extension** \(G\to\mathbb R\to S^1\). In particular no \(e^{itx}\) can realize these signs at all log-prime generators.

Stronger: no nonzero measurable \(u:\mathbb R\to S^1\) can satisfy
\(u(x+g)=\chi_G(g)u(x)\) a.e. for EVERY \(g\in G\). Applying this to δ_j forces \(u(x+\delta_j)=-u(x)\) a.e.; strong continuity of translations in \(L^2_{\rm loc}(\mathbb R)\) contradicts |u|=1. This is an exact arithmetic/archimedean **source-map obstruction**, not nonzero gauge curvature. The G-action is abelian and its prime shifts commute.

**Constructive minimal repair:** append a **two-sheeted arithmetic fiber** \(\varepsilon\in\{\pm1\}\) to the Γ log16 circle \(v\in\mathbb R/\Lambda\mathbb Z\), and for every positive odd integer m set
\[
\boxed{T_m(v,\varepsilon)=(v+\log m\bmod\Lambda,\ \chi_{-4}(m)\varepsilon).}\tag{PJ6}
\]
Then \(T_m T_n=T_{mn}=T_nT_m\), and χ is the continuous projection \(\varepsilon\mapsto\varepsilon\) on this augmented compact space. This is the minimal explicit *finite-fiber* cure for the failed real-only gauge. The prime p=2 is EXCEPTIONAL: χ(2)=0, so it has its own 2-primary channel instead of an invertible map on this two-sheeted χ fiber. A completed adelic/Frobenius object, if constructed later, must retain rather than suppress this distinction.

The augmentation is an exact mathematical model, not a unique canonical SUCC field, physical gauge theory or source-selected normality theorem. Twisted Dirichlet beta L has its OWN Γ factor and zero spectrum; it is not the Riemann ζ function.

## 7. Exact critical boundary and failure controls

- The prime-power shift data and Γ term reconstruct the **classical Weil form**; this does not identify SUCC's BBP signed source \(r_o(n)\) with the primes of ζ. SUCC prime-class χ projection and the log-clock Dirichlet character share the same arithmetic character but belong to DIFFERENT typed operators.
- The degree-\(16^n\) Riemann sphere curvature of #516 and chosen monopole levels remain source/seed-blind. The present prime-power jets are source-specific to ζ but do not solve selected SUCC π Weyl decay.
- A nonzero negative eigenvalue of a jet cannot be promoted to an actual zeta zero, physical vacuum state, or proof of critical-line localization.
- Global 2-direction curvature requires an actual noncommuting, independently supplied transverse map with paid transformations. T_m are COMMUTING; the χ fiber is nontrivial in extension topology/continuity, NOT curvature.
- To reach RH, derive a NEW non-tautological lower bound for the entire Gamma+pole+all-primes Weil form for a nontrivial infinite test family, then deal with all test functions. To reach π normality, additionally build a genuine source/carry intertwiner to the literal U0=0 BBP orbit. Neither gate is closed.

**Verdicts:** PJ1–PJ6 and boundary norm estimates are paper-derived within explicitly declared elementary/classical models. Finite evaluations are OBSERVED once within recorded scope. Source-completion/rate/originality is UNVERIFIED. RH and base-16 normality of π remain OPEN.
