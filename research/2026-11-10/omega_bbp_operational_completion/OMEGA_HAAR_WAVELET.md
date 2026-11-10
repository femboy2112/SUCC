# Ω₄ × Ω₅ × Haar: the source clock, inverse-branch Möbius packet, and oriented defect

**10 November 2026.** Source-first continuation of [INVERSE_BETA_BBP_ROOT](INVERSE_BETA_BBP_ROOT.md) and draft PR #579. **Source contracts unchanged; no main merge, proof of π normality, or inference from CI.**

## 0. Outcome and precise scope

**Proved (paper and finite checks):** (1) 2- and 3-step BBP foldings share a six-step diamond; (2) chronological *lossy* 2/3 Haar coarse-grainings fail to commute by a rank-two skew operator with a canonical oscillator plane; (3) the genuine four-pole source drives this plane with a strictly positive oriented adjacent-window pairing and exact power-law asymptotics; (4) the sixteen inverse circle branches admit a unitary character/Walsh-Haar filter bank whose parity component is an antiperiodic Möbius section, with an exact source-orbit twisted-Fourier identity; (5) both inverse defects have explicit adversarial boundaries.

**OPEN:** no source-selected signed decay, no parity balance, no full hexadecimal normality; no complete type-preserving beta AST compiler. The Möbius twist belongs to the **inverse observer's parity bundle**, not to the physical topology of π. The Ω₄ and Ω₅ raw lambda terms are NOT beta-convertible merely because both clock counters reach six source steps. The noncommuting projections are *inserted* lossy observers; the exact source foldings commute.

## 1. Source-first omega clocks

Let

\[
R(n)=\frac4{8n+1}-\frac2{8n+4}-\frac1{8n+5}-\frac1{8n+6},\quad q=16^{-1},\quad
F(g)(n)=R(n)+qg(n+1).
\]

For all integers \(d\ge1\), the exact iteration is

\[
F^d(g)(n)=b_d(n)+q^d g(n+d),\quad
b_d(n)=\sum_{j=0}^{d-1}q^jR(n+j).
\]

SUCC's syntax \(\omega_k=\lambda x.x^k\) (left-associated) and \(E_k(m)\) obeys \(E_k(m)\to_\beta E_k(m+k-2)\). Reading only the arithmetic clock increment, \(\Omega_4\) naturally indexes *pairs* of primitive BBP steps, and \(\Omega_5\) indexes *triples*. They meet after **three \(\Omega_4\) contractions / two \(\Omega_5\) contractions**, each representing six primitive source transitions:

\[
\boxed{(F^2)^3=(F^3)^2=F^6.}
\]

The raw lambda terms differ in arity and internal redex positions; this is an explicit **clock-indexed semantic assignment**, NOT yet a faithful compiler. An independent \(\Omega_3\) length-growth stream without source data cannot calculate \(R(n)\).

## 2. Exact inverse defects: averaging does not commute

A full six-entry chronological window \(v=(R(n),\ldots,R(n+5))\) is available to the forward source evaluator. A coarse six-step output \(b_6(n)=\sum_jq^jv_j\) is one scalar: the linear map \(\ell:\mathbb R^6\to\mathbb R\), \(\ell(v)=w\cdot v\) with \(w_j=q^j\), has a **five-dimensional kernel**. The minimum-norm inverse is \(\ell^+(a)=(a/\|w\|^2)w\) and the exact lost vector is \((I-\ell^+\ell)v\). This is a *chosen* inverse estimator, not the inverse of the full index-and-state BBP recurrence (which is invertible when its clock and forcing are retained).

Define orthogonal projections onto **chronological adjacent group means**:

- \(P_2\): average \((0,1),(2,3),(4,5)\) independently;
- \(P_3\): average \((0,1,2),(3,4,5)\) independently.

Their defect (apply \(P_3\) then \(P_2\), versus the reverse) is

\[
C=P_2P_3-P_3P_2,\qquad
Cv=(a,a,b,-b,-a,-a),
\]

\[
\boxed{a=(v_2-v_3)/6,\quad b=(v_4+v_5-v_0-v_1)/6.}
\]

Direct multiplication yields

\[
C^*=-C,\qquad \operatorname{rank}C=2,\qquad C^3=-\tfrac29 C.
\]

With the orthonormal basis

\[
u=(1,1,0,0,-1,-1)/2,\qquad
z=(0,0,-1,1,0,0)/\sqrt2,
\]

\[
\boxed{Cu=(\sqrt2/3)z,\qquad Cz=-(\sqrt2/3)u.}
\]

Thus the nonzero part of the **inverse coarse-graining disagreement** is exactly one real **oscillator plane**, with singular value \(\sqrt2/3\) and eigenvalues \(\pm i\sqrt2/3\). The order of coarse-graining fixes a sign convention: swapping projection order sends \(C\mapsto-C\), leaving \(\|Cv\|\) unchanged.

**Caution:** the CRT grid \(j\mapsto(j\bmod2,j\bmod3)\) supplies different, independent 2/3 axes; its row and column conditional expectations commute. Noncommutation here is tied specifically to **overlapping consecutive-time partitions**, not a formal identity of omega arities or a universal curvature.

## 3. A source-driven orientation theorem (new arithmetic payoff)

The four-pole source has the positive Hausdorff-moment representation

\[
R(n)=\int_0^1x^{8n}P(x)\,dx,\qquad
P(x)=(1-x)(x^2+2)(x^2+2x+2)>0\quad(0<x<1).
\]

Consequently \(R(n)>R(n+1)>0\). The chronological wavelet defect \(Cr^{(n)}\), for \(r^{(n)}=(R(n+j))_{j=0}^5\), is never zero. More sharply, define the *oriented adjacent-window area*

\[
\boxed{\mathscr A_n=\langle r^{(n)},C r^{(n+1)}\rangle.}
\]

**Theorem.** For every integer \(n\ge0\),

\[
\boxed{\mathscr A_n>0,\qquad
\mathscr A_n\sim\frac{675}{128}\,n^{-9}.}
\]

**Proof of strict positivity (no numeric fitting).** Put

\[
A_n=R(n)+R(n+1)-R(n+4)-R(n+5)>0,\quad
B_n=R(n+3)-R(n+2)<0.
\]

The explicit commutator gives

\[
\mathscr A_n=\frac{B_n A_{n+1}-A_n B_{n+1}}6
=\frac{A_nA_{n+1}}6\left(\frac{B_n}{A_n}-\frac{B_{n+1}}{A_{n+1}}\right).
\]

Let \(t=x^8\). From the moment representation,

\[
A_n=\int_0^1x^{8n}P(x)(1+t)(1-t^4)\,dx,
\quad -B_n=\int_0^1x^{8n}P(x)t^2(1-t)\,dx.
\]

Hence \(-B_n/A_n=\mathbb E_{\mu_n}[g(t)]\) for the strictly positive probability density \(\mu_n\propto x^{8n}P(x)(1+t)(1-t^4)dx\), with

\[
g(t)=\frac{t^2}{(1+t)^2(1+t^2)},\qquad
\frac{g'(t)}{g(t)}=\frac{2(1-t^3)}{t(1+t)(1+t^2)}>0
\quad(0<t<1).
\]

The next measure \(\mu_{n+1}\) is the increasing-\(t\) tilt of \(\mu_n\); therefore

\[
\mathbb E_{\mu_{n+1}}g-\mathbb E_{\mu_n}g
=\frac{\operatorname{Cov}_{\mu_n}(t,g(t))}{\mathbb E_{\mu_n}t}>0.
\]

The strict covariance inequality follows from \(\frac12\iint(t-s)(g(t)-g(s))d\mu_nd\mu_n>0\). Thus \(B_n/A_n>B_{n+1}/A_{n+1}\) and \(\mathscr A_n>0\). ∎

**Proof of asymptotic constant.** Rational expansions at infinity give

\[
A_n=\frac{15}{4n^3}-\frac{2067}{64n^4}+\frac{28365}{128n^5}+O(n^{-6}),
\]

\[
B_n=-\frac{15}{32n^3}+\frac{2067}{512n^4}-\frac{24045}{1024n^5}+O(n^{-6}).
\]

Therefore \(B_n/A_n=-1/8+9/(8n^2)+O(n^{-3})\), and the displayed determinant yields \(\mathscr A_n\sim675/(128n^9)\). This is a rational-asymptotic derivation, independently calibrated with exact fractions. ∎

The earlier, unoriented norm also satisfies

\[
\|Cr^{(n)}\|\sim\frac{15}{64}\sqrt{\frac{44}{3}}n^{-3}.
\]

**Mutation discriminator:** deleting just the last negative pole changes \(P(1)=0\) to \(P_{\rm mutant}(1)=1\), turns \(R(n)\sim15/(64n^2)\) into \(R_{\rm mutant}(n)\sim1/(8n)\), and moves the wavelet norm's decay from \(n^{-3}\) to \(n^{-2}\). Specifically \(n^2\|Cr^{(n)}_{\rm mutant}\|\to\sqrt{33}/24\). This detects the four-pole **source cancellation**, not the π orbit seed; other positive densities can share the same orientation sign.

## 4. Sixteen inverse branches: the precise Möbius-Haar packet

Let \(T(s)=16s\pmod1\) on \(\mathbb T=\mathbb R/\mathbb Z\). The exact inverse branch locations over a lifted destination \(t\in\mathbb R\) are

\[
s_k(t)=\frac{t+k}{16}\pmod1,\quad k=0,\ldots,15.
\]

For any continuous 1-periodic function \(f\), its full inverse-fiber data \(v_k(t)=f(s_k(t))\) has the **unitary 16-channel Fourier/Walsh-Haar packet**

\[
\boxed{H_mf(t)=\frac1{16}\sum_{k=0}^{15}
\exp(-2\pi i mk/16)\,f((t+k)/16)},\qquad m=0,\ldots,15.
\]

The low-pass \(H_0\) averages the sixteen candidates; the other fifteen channels are the *exact* lost details:

\[
\boxed{v_k(t)=\sum_{m=0}^{15}e^{2\pi i mk/16}H_m f(t),\quad
\frac1{16}\sum_k|v_k-H_0f|^2=\sum_{m=1}^{15}|H_m f|^2.}
\]

This is a discrete Fourier filter bank on each **inverse fiber**; the parity character \(H_8\) is also a Walsh-Haar **packet**, not a single scalar Haar basis atom. It equals the average of the eight adjacent pair differences \((v_{2j}-v_{2j+1})/16\). No new arithmetic distribution is inferred from this exact linear algebra.

**Monodromy theorem.** Since \(s_k(t+1)=s_{k+1}(t)\),

\[
\boxed{H_m f(t+1)=e^{2\pi i m/16}H_m f(t).}
\]

In particular,

\[
\boxed{H_8 f(t+1)=-H_8 f(t).}
\]

For real-valued continuous \(f\), this is a real **antiperiodic** section of the associated real line bundle \((\mathbb R\times\mathbb R)/((t,a)\sim(t+1,-a))\), precisely the **Möbius line bundle**. It must have a zero somewhere over every period; the discontinuous digit parity chart can avoid that only by paying a seam jump. The full sixteen-sheet covering \(T\) itself is orientation preserving and *not* a Möbius surface. The twist arises under the **chosen parity representation** of the cyclic monodromy. This is independent of whether the base point came from π.

Fourier selection is equally exact:

\[
\boxed{H_m[e^{2\pi i hs}](t)=
\begin{cases}e^{2\pi i h t/16},&h\equiv m\pmod{16},\\0,&\text{otherwise.}\end{cases}}
\]

Thus the parity sector is **exactly** the source's previously identified real Fourier frequencies \(h\equiv8\pmod{16}\). The associated half-angle oscillator is intrinsically twisted, not an ordinary periodic function on the destination circle. The \(m=8\) sign is unchanged under reversing generator \(+1\leftrightarrow-1\): parity **cannot detect an orientation reversal**. The complex characters \(m\notin\{0,8\}\) have distinct forward/inverse phases and can register direction when a transport convention is fixed.

## 5. Direct weld to the actual selected π orbit

For the original completed BBP zero seed let

\[
\theta_n=\{16^{n-1}\pi\},\qquad t_n=\theta_{n+1},\quad
 d_n=\lfloor16\theta_n\rfloor.
\]

The inverse branch and twisted parity identity are **pointwise exact**:

\[
16\theta_n=d_n+t_n,\qquad
\boxed{e^{2\pi i\,8(2j+1)\theta_n}
=(-1)^{d_n}\,e^{\pi i(2j+1)t_n}}
\quad(j\in\mathbb Z).
\]

The factor \(e^{\pi i(2j+1)t}\) is antiperiodic: the parity label flips when the lift of \(t\) changes by one; the **product is gauge-invariant**. This is an explicit computation-level realization of the Möbius bundle, requiring no claim that π's digit sequence is balanced.

The source-oriented amplitude \(a_n=n^9\mathscr A_n\to675/128>0\) yields a canonical **source-weighted Ω–Haar parity packet**:

\[
W_n^{(j)}=a_n(-1)^{d_n}e^{\pi i(2j+1)t_n}
=a_n e^{2\pi i\,8(2j+1)\theta_n}.
\]

For every fixed \(j\), on growing epochs \(A\le n<2A\),

\[
\frac1A\sum_{n=A}^{2A-1}W_n^{(j)}
-\frac{675}{128}\frac1A\sum_{n=A}^{2A-1}e^{2\pi i\,8(2j+1)\theta_n}
\longrightarrow0.
\]

**Status:** this is an exact reformulation with a source-derived asymptotically constant amplitude, **not an improved cancellation estimate**. The old odd-8 Weyl targets remain OPEN. The coherent wrong seed \(s=-\pi/16\) makes the completed orbit constant zero, hence the weighted packet tends to \(675/128\), despite identical forcing. In finite rational form, choosing \(s=-P_L\) makes every common-horizon completion \(16^n(s+P_L)=0\). This is the necessary negative control.

## 6. Which information is genuinely irreversible?

The exact **indexed rational** BBP action \((n,U_n)\mapsto(n+1,16U_n+R(n))\) is invertible onto its image when clock and forcing are retained. On the **completed circle quotient**, all sixteen distinct predecessors coalesce after one forward application: \(T(s_k(t))=t\). No future circle trajectory alone can recover the prior digit. The inverse phase section must therefore carry a branch/seed/carry witness. This is a real noninjectivity at the declared observation boundary, not a failure of arithmetic reversibility.

Similarly, \(P_2P_3-P_3P_2\ne0\) only because **different noninjective observations** are taken along overlapping time partitions; the exact source operators satisfy \(F_2^3=F_3^2\). One may reverse the projection order and obtain the opposite signed curvature, with the same defect energy. A source orientation comes from the original positive four-pole moment data plus the declared chronological order, not from declaring all possible observer directions physically identical.

A **figure-eight** is not forced by these operations. The rigorously identified objects are (a) a 2D skew/oscillator defect plane and (b) a nontrivial real Möbius **line bundle** over the inverse-observation circle. Drawing the two observer routes as lobes is a visualization choice, not an intrinsic topological identification.

## 7. Next discriminating problem

The hard question is now exceptionally explicit: can the source clock, actual integer carry history, and parity Möbius packet force the **twisted signed Weyl averages** of the original zero seed to vanish, while excluding coherent wrong seeds and near-matched pole mutants? A useful stronger probe would bound a signed conditional branch character against *future-dependent* test sections on all large epochs, or find a source identity that obstructs non-Haar invariant path measures. The universal fiber filter-bank and positive source area do not provide that estimate. Test the *signed* quantity, not its pointwise absolute value.

**Claim ledger:** exact six-step diamond, rank-two commutator, skew oscillator, source orientation and asymptotic, sixteen-channel Parseval, branch monodromy/Möbius, and pointwise twisted orbit identity: **PROVED PAPER, FINITELY CALIBRATED**. Fixed-point/BPP lambda AST source compiler: **UNVERIFIED**. The original-zero signed cancellation: **OPEN**. π base-16 normality: **OPEN**. All tests in this research round are fast standalone tests; the repository-wide ~13k test suite and hosted CI are **NOT RERUN**.

**Provenance:** BBP input from SUCC's authenticated source \(r(j)=R(j-1)\); previous inverse-fold paper at [INVERSE_BETA_BBP_ROOT](INVERSE_BETA_BBP_ROOT.md); the \(\Omega_k\) copy-growth theorem from [OMEGA_INTERPRETER](../../2026-11-09/scott_omega_causal_weld/OMEGA_INTERPRETER.md). For the classical topology, compare [M. Tehrani, *Manifolds and Vector Bundles*, Example 15.11](https://homepage.divms.uiowa.edu/~mftehrani/Manifolds%20and%20VB.pdf), and for covering monodromy [Grava, *Riemann Surfaces and Integrable Systems*, Example 1.3.22](https://people.sissa.it/~grava/RS2021.pdf). These standard constructions are not claimed as novel SUCC discoveries.
