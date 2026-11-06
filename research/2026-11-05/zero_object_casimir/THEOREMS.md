# ZERO OBJECT × CASIMIR PRESSURE: source-conditioned field and selected-orbit obstruction

**Research-only mathematical dossier, 2026-11-05.** Strict add-only descendant of SUCC draft #513, pinned at \`727a97a006e929243e0fee1ab44cf52dc68e2c8f\`. Original four signed BBP poles, literal \(U_0=0\), source contracts, archive, Lean, workflow, production and main unchanged. No physical Casimir-force claim, quantum vacuum claim, π-normality claim, or worldwide novelty priority.

The user proposes that a **categorical zero object** is more primal than a particular scalar zero, and that source-selected finite forms break a symmetric baseline through their causal/history constraints. We give THREE typed realizations with an explicit non-transfer theorem: pointed-set category, Gaussian boundary conditioning, and an exact original-radix BBP Fekete seed pressure.

## CZ-01 — a zero object that really is an additive-like zero AND multiplicative-like unit (but not numerical 0=1)

In the category \(\mathbf{Set}_*\) of pointed sets and basepoint-preserving maps, the singleton \(*\) is both initial and terminal (a **zero object**). Its two universal unit laws are
\[
\boxed{X\vee *\cong X,\qquad X\times *\cong X.}\tag{CZ1}
\]
Here \(\vee\) is the categorical coproduct (wedge) and \(\times\) is Cartesian product. The **same object** is a coproduct-zero and Cartesian-product-one. This does NOT identify ordinary numerical \(0\) and \(1\) in a nontrivial ring; it does NOT make \(\times\) distribute over \(\vee\), and \(*\) is NOT the tensor unit for the **smash product** (which is the two-point pointed set \(S^0\)). The zero object has a unique self-endomorphism. It carries no nontrivial internal dynamics without richer objects and source arrows.

A scalar zero can conceal many **presentations**: in additive modules, \(\delta:A\oplus A\to A\), \(\delta(a,b)=a-b\), has kernel the entire diagonal \((a,a)\). But that short exact sequence SPLITS; a nontrivial source/gluing law must be separately specified. In SUCC #511 the forcing, rational-time cohomology and literal carries are those extra structures.

**Operational interpretation:** the baseline is a category of pointed/source-compatible constructions with explicit arrows, not the empty scalar. A probability law over its constructions is EXTRA DATA; no universal "likelihood of realizable mathematical forms" is induced by the categorical zero object.

## CZ-02 — finite mathematical 'plates' actually deform a Gaussian virtual covariance

Take a standard stationary centered real Gaussian Markov field \((X_i)_{i\in\mathbb Z}\) with
\[
\mathbb E X_i=0,\quad \mathrm{Cov}(X_i,X_j)=\rho^{|i-j|},\quad 0<\rho<1.
\]
For instance \(X_{n+1}=\rho X_n+\sqrt{1-\rho^2}\,\xi_{n+1}\) with stationary initial law and independent standard-Gaussian innovations. This is an explicit MATHEMATICAL probability model, not a physical vacuum.

Place two boundary constraints at sites \(0,d\) by using the regular conditional law \(X_0=X_d=0\). The boundary covariance is
\[
M_d=\begin{pmatrix}1&\rho^d\\ \rho^d&1\end{pmatrix},\qquad
\det M_d=1-\rho^{2d}.
\]
The Gaussian conditional Schur complement gives for every integer \(0<k<d\)
\[
\boxed{
\mathrm{Var}(X_k\mid X_0=X_d=0)
=\frac{(1-\rho^{2k})(1-\rho^{2(d-k)})}{1-\rho^{2d}}
<1-\rho^{2k}=\mathrm{Var}(X_k\mid X_0=0).
}\tag{CZ2}
\]
Thus adding the second mathematical 'plate' suppresses intermediate fluctuations. Outside the interval on the left, the stationary Markov property makes the additional future boundary condition irrelevant once \(X_0\) is fixed:
\(\mathrm{Var}(X_{-j}|X_0=X_d=0)=1-\rho^{2j}\), \(j>0\).

The joint zero boundary **density ratio**, as opposed to the nonexistent positive probability of two exact real equalities, is
\[
\frac{p_{(X_0,X_d)}(0,0)}{p_{X_0}(0)p_{X_d}(0)}
=(1-\rho^{2d})^{-1/2}.
\]
Define the relative *free-energy-like interaction* from this explicit density ratio:
\[
\boxed{F_{\rm int}(d)=\tfrac12\log(1-\rho^{2d})<0,\qquad
F_{\rm int}(d)\to0\quad(d\to\infty).}\tag{CZ3}
\]
For real separation d, \(-\frac d{dd}F_{\rm int}=-(-\log\rho)\rho^{2d}/(1-\rho^{2d})<0\) (attractive orientation under this declared convention). This provides a rigorous, source-free analogue of a Casimir pressure: the two constraints change a latent Gaussian covariance and their joint partition/density relative to the separate constraints. It is NOT the electromagnetic Casimir effect and is not a universal probability law on mathematics.

**Crucial falsifier:** the unforced stationary Gaussian process is TIME-REVERSAL invariant because its mean is zero and covariance \(\rho^{|i-j|}\) is reflection invariant, despite its forward Markov generation. A causal construction **alone** does NOT necessarily break the symmetry. A source forcing \(f_n\) can change the mean and conditioned response, but for an ADDITIVE deterministic forcing with the same noise it does not change this covariance Schur complement. Hence this baseline pressure alone is source-blind and cannot prove the selected original BBP orbit mixes.

## CZ-03 — exact source-ensemble 'Fekete pressure' and Bernoulli resonance covariance

This result directly uses SUCC #513's selected antisymmetric Vandermonde energy.

For ANY fixed real forcing sequence \(r_n\) (the authentic four-pole r_o is a special case), let
\(U_0(s)=s,\ U_{n+1}(s)=16U_n(s)+r_{n+1}\), and \(u_n=U_n(0)\).
Then
\[
\boxed{U_n(s)=u_n+16^n s.}\tag{CZ4}
\]
For integer A>=2 and ordered epoch \(\mathcal I_A=\{A,\ldots,2A-1\}\), put
\[
\mathcal E_A(s)=\frac1{A^2}
\sum_{A\le i<j<2A}
g(q_{ij}s+\alpha_{ij}),\quad
g(t)=\log|1-e(t)|^2,\quad
q_{ij}=16^j-16^i,\quad
\alpha_{ij}=u_j-u_i.
\tag{CZ5}
\]
This is exactly \(A^{-2}\log|\Delta_A(s)|^2\) of the selected orbit phase Vandermonde, with \(-\infty\) at a collision seed. These singularities form a finite set modulo1 per finite A and hence do not affect Haar expectations.

The integrable one-periodic kernel has \(\widehat g(0)=0\) and \(\widehat g(h)=-1/|h|\) for h!=0; this is proved using the Abel-regularized \(\log|1-r e(t)|^2\) and convergence in L². Since every q_ij is a nonzero integer, the Lebesgue-uniform seed ensemble obeys
\[
\boxed{\int_0^1\mathcal E_A(s)ds=0\quad\text{for every }A\ge2.}\tag{CZ6}
\]
This is a symmetric *seed ensemble* baseline, not a statement that the canonically pointed seed zero is typical.

For two labelled epoch pairs \(p=(i,j)\), \(q=(k,l)\), let \(Q_p=16^j-16^i>0\), \(Q_q=16^l-16^k>0\), \(\alpha_p=u_j-u_i\), \(\alpha_q=u_l-u_k\), and \(d_{pq}=\gcd(Q_p,Q_q)\). Define \(B_2(x)=\{x\}^2-\{x\}+1/6\). Fourier-mode matching \(aQ_p+bQ_q=0\) requires \(a=(Q_q/d_{pq})m,b=-(Q_p/d_{pq})m\), hence the exact signed covariance:
\[
\boxed{
\int_0^1g(Q_p s+\alpha_p)g(Q_q s+\alpha_q)\,ds
=\frac{2\pi^2d_{pq}^2}{Q_pQ_q}
B_2\!\left(\frac{Q_q}{d_{pq}}\alpha_p-\frac{Q_p}{d_{pq}}\alpha_q\right).}\tag{CZ7}
\]
The equality uses \(\sum_{m\ge1}\cos(2\pi mx)/m^2=\pi^2 B_2(x)\). Thus
\[
\boxed{
\mathrm{Var}_s\mathcal E_A(s)=
\frac{2\pi^2}{A^4}\sum_{p,q}
\frac{d_{pq}^2}{Q_pQ_q}
B_2\!\left(\frac{Q_q}{d_{pq}}\alpha_p-\frac{Q_p}{d_{pq}}\alpha_q\right).
}\tag{CZ8}
\]
For the **actual original zero-seeded rational BBP source** every \(\alpha_p\in\mathbb Q\), so the entire variance divided by \(\pi^2\) is a computable **exact rational**. The covariances can have both signs; dropping them before verifying the match would be mathematically invalid.

## CZ-04 — source-independent O(A^-2) bound; the unforced baseline maximizes variance

Because \(B_2(x)\le1/6\) for every real x, all positive prefactors in CZ8 give the source-independent comparison
\[
\boxed{
0\le\mathrm{Var}_{r}\mathcal E_A(s)
\le\mathrm{Var}_{r\equiv0}\mathcal E_A(s)
=\frac{\pi^2}{3A^4}\sum_{p,q}\frac{d_{pq}^2}{Q_pQ_q}.}\tag{CZ9}
\]
The *unforced source* has \(\alpha_p=0\), saturating every individual B2 upper bound. In this precise VARIANCE metric, deterministic forcing can only reduce the seed-ensemble fluctuation. It is not an energy-conservation or likelihood theorem.

The radix gcd factorization is EXACT:
\[
d_{pq}=
16^{\min(i,k)}
\big(16^{\gcd(j-i,l-k)}-1\big).
\]
Consequently, with \(a=j-i,\ b=l-k\) and \(g=\gcd(a,b)\),
\[
\frac{d_{pq}^2}{Q_pQ_q}
=16^{-|i-k|}\frac{(16^g-1)^2}{(16^a-1)(16^b-1)}
\le\left(\frac{16}{15}\right)^2
16^{-|i-k|-|a-b|}.
\]
The two geometric row-sum estimates
\(\sum_{i,k\in\mathcal I_A}16^{-|i-k|}\le(17/15)A\) and
\(\sum_{a,b=1}^{A-1}16^{-|a-b|}\le(17/15)(A-1)\) yield
\[
\boxed{
\mathrm{Var}_s\mathcal E_A(s)
\le\frac{\pi^2}{3}
\left(\frac{16}{15}\frac{17}{15}\right)^2
\frac{A-1}{A^3}
<\frac{4.808}{A^2}.}\tag{CZ10}
\]
This holds for **EVERY** deterministic forcing, including the authentic BBP source, without a mixing or probabilistic independence assumption.

Chebyshev and FIRST Borel–Cantelli (no independence needed) imply for each \(\epsilon>0\), \(\sum_A\mathbb P(|\mathcal E_A|>\epsilon)<\infty\). Intersect over \(\epsilon=1/m\) to obtain
\[
\boxed{\mathcal E_A(s)\to0\quad\text{for Lebesgue-a.e. }s\in[0,1).}\tag{CZ11}
\]
By inherited #513 Fekete→Weyl, almost every seed completion has equidistributed circle phases. This is a genuine deterministic-lacunary **ensemble theorem**, not the selected BBP \(s=0\) normality theorem. Its source-independence is a limitation for source selection.

## CZ-05 — a finite approximation to zero has HAAR future marginals but exact causal multi-time gluing

Let \(\mu_K\) be uniform measure on the zero cylinder \(C_K=[0,16^{-K})\), \(K\ge0\). This models a seed whose first K hexadecimal digits are zero but whose remaining digits are *not yet specified*. It is a stated probability model, not an automatic categorical vacuum. For all n>=K and nonzero integer h,
\[
\boxed{
\int e(hU_n(s))\,d\mu_K(s)=0.}\tag{CZ12}
\]
Indeed \(U_n(s)=u_n+16^ns\), and integration over C_K runs through exactly \(16^{n-K}\) integer periods. Thus **each** future circle marginal is Haar-uniform.

But these future marginals are NOT independent. For any finite integers \(h_j\) and times \(n_j\ge K\), set \(Q=\sum_j h_j16^{n_j}\) and \(\alpha=\sum_jh_j u_{n_j}\). Because Q is divisible by \(16^K\), exact character orthogonality gives
\[
\boxed{
\int e\!\left(\sum_jh_jU_{n_j}(s)\right)d\mu_K(s)
=\begin{cases}
e(\alpha),&Q=0,\\0,&Q\ne0.
\end{cases}}\tag{CZ13}
\]
The most important source-labelled two-time resonance is \(h_n=16,\ h_{n+1}=-1\):
\[
\boxed{
\mathbb E_{\mu_K}e(16U_n-U_{n+1})=e(-r_{n+1})
\qquad(n\ge K).}\tag{CZ14}
\]
The one-time future marginals are exactly Haar while their joint time correlation **remembers the full original forcing**. This is a rigorous realization of "symmetric baseline with source-conditioned causal gluing", not an analogy that assumes independent phases.

The forward circle transition \(x\mapsto16x+r_{n+1}\pmod1\) has ONE output for each input but exactly 16 inverse images \((y-r_{n+1}+j)/16\), \(j=0,\dots,15\), for each output y. Under Haar future marginals the regular conditional distribution over those 16 inverse branches gives each weight 1/16. Thus coarse circle projection forgets \(\log16\) nats of *backward-branch information per step* in this declared model, while the unwrapped recurrence and literal carries preserve its actual selected route.

The epochs' Fekete energy has a further exact finite seed-aliasing symmetry:
\[
\boxed{\mathcal E_A(s+16^{-A})=\mathcal E_A(s).}\tag{CZ15}
\]
Indeed every indexed future phase \(e(U_n(s))\), n>=A, itself has that period in s. Thus for any K<=A, C_K contains an integer number of full periods and
\[
\boxed{\operatorname{Law}_{s\sim\mu_K}(\mathcal E_A(s))
=\operatorname{Law}_{s\sim\mathrm{Haar}}(\mathcal E_A(s)).}\tag{CZ16}
\]
In particular the exact mean0 and variance CZ8/CZ10 hold **unchanged** even after arbitrarily many BUT FINITELY MANY initial zero digits have been selected, once observation time A is later than K.

## CZ-05b — the two-scale boundary: full ensemble transparency vs exact selected reconstruction

The seed-cylinder theorem is stronger than equal future marginals: it identifies the **entire joint law** of every finite source-time window beginning after the finite zero-prefix has expired.

Fix integer \(A\ge1\) and let \(X_A(s)=(U_A(s)\bmod1,\ldots,U_{2A-1}(s)\bmod1)\). For all \(n\ge A\),
\[
U_n(s)\bmod1=(u_n+16^{n-A}t)\bmod1,\qquad t=16^As\bmod1.
\]
Under \(\mu_K=\mathrm{Uniform}[0,16^{-K})\), if K<=A, the variable \(t\) is **EXACTLY Haar uniform** on the circle, because the interval winds \(16^{A-K}\) full periods. It is also Haar under a full-uniform seed s. Consequently, for EVERY bounded measurable function F on the A-dimensional torus,
\[
\boxed{
\mathbb E_{\mu_K}F(X_A(s))
=\mathbb E_{s\sim\mathrm{Haar}}F(X_A(s)),
\quad K\le A.}\tag{CZ16a}
\]
The whole future epoch's JOINT distribution, not merely its marginals or Fekete energy, is unchanged by any finite number of selected leading zero digits K that is no greater than its first observation time A. This is an exact strong "virtual baseline support" statement under the declared seed ensemble. It does **not** imply the individual \(U_n(s)\) are mutually independent; their graph law retains source resonance CZ14.

At the other end, an approximation to the actual pointed zero seed becomes **uniformly** accurate on the epoch once K exceeds its LAST observation time. For every s in C_K and \(A\le n<2A\),
\[
|U_n(s)-u_n|=16^n s\le16^{2A-1-K}
\]
(with ordinary unwrapped representatives; the comparison is modulo1 after applying the exponential). Therefore, for any integer harmonic H and ANY consecutive sharp subinterval \(I\subseteq[A,2A)\),
\[
\boxed{
\frac1A\left|\sum_{n\in I}
[e(HU_n(s))-e(Hu_n)]\right|
\le2\pi|H|\,16^{2A-1-K}.}\tag{CZ16b}
\]
This is a source-independent, exact Lipschitz transport bound; no distribution hypothesis.

For the authentic #501/#503 high-depth schedule \(H_A(h)\le A^2\log A\) for fixed nonzero h, choose
\[
K_A=2A+\lceil 3\log_{16}A\rceil.
\]
Then CZ16b is \(O(\log A/A)=o(1/\log A)\) uniformly in the selected cylinder and in ALL sharp subintervals. Thus the **selected critical Weyl statistic** is reproduced at the needed precision by a cylinder with roughly 2A **plus logarithmically many** zero hexadecimal digits.

The two exact regimes are:

1. \(K\le A\): the entire epoch is statistically identical to the full symmetric Haar seed ensemble, in every bounded measurable finite-time observation.
2. \(K\ge2A+O(\log A)\): the original zero-seeded critical signed Weyl statistic is uniformly reconstructible, with error negligible at the #501 sufficient scale.

The intermediate \(A<K<2A+O(\log A)\) is an **unresolved boundary/selection layer**; the exact statements above alone place NO nontrivial signed constraint across it. The unforced seed-zero countermodel shows the missing bridge cannot be universal. An original source-specific inequality must pay both this selection-resolution information and its true carry arithmetic.

This is a rigorous form of the "Haar at low resolution / exact carrier at high resolution" distinction. It is not a physical plate separation or a proof that increasing K breaks quantum symmetry spontaneously.

## CZ-06 — the zero-point pressure / limit-exchange obstruction is decisive

\(\mu_K\) tends weakly to \(\delta_0\), the truly **pointed zero seed**; its relative information cost is
\[
D_{\mathrm{KL}}(\mu_K\|\mathrm{Haar})=K\log16\to\infty.
\]
For a fixed finite time n, every continuous phase observation tends to its exact value at s=0 as K→∞. For each finite K, however, every time n≥K has exactly Haar marginals.

This is not an abstract concern. Under **zero forcing** \(r_n\equiv0\) consider \(f_{A,h}(s)=A^{-1}\sum_{n=A}^{2A-1}e(h16^ns)\), integer h≠0. The cylinder identities give
\[
\boxed{
\lim_{K\to\infty}\lim_{A\to\infty}\int f_{A,h}\,d\mu_K=0,\qquad
\lim_{A\to\infty}\lim_{K\to\infty}\int f_{A,h}\,d\mu_K=1.
}\tag{CZ17}
\]
Both conclusions follow from the exact finite operations. The first is the **ensemble limit**; the second is the exact fixed zero orbit under x→16x. A finite approximation to the zero boundary is NOT interchangeable with an exactly selected zero seed at infinite source time.

The same four-pole BBP forcing with wrong homogeneous seed \(s_*=-\pi/16\) is a source-compatible nonuniform orbit: its tail \(U_n(s_*)=-T_n\to0\), and inherited #513 shows \(\mathcal E_A(s_*)\to-\infty\). Consequently a strong all-seed-ensemble Fekete law does NOT yield even a weak source-selected determinant lower bound at s=0.

Away from finitely many seed-collision points, the exact source-seed 'pressure' derivative is
\[
\boxed{
\mathcal E_A'(s)=\frac{2\pi}{A^2}
\sum_{A\le i<j<2A}
(16^j-16^i)\cot\!\big(\pi(U_j(s)-U_i(s))\big).
}\tag{CZ18}
\]
The exponentials \(16^j\), singular cotangents and nonuniform seed resolution show why one cannot infer the value at a single seed from a small L² ensemble variance without an INDEPENDENT arithmetic regularity estimate. This derivative is a SOURCE-PRESERVING exact identity; no uniform bound is claimed.

**Where the next proof must live:** bound \(\mathcal E_A(0)\ge-o(1)\) (the inherited Fekete sufficient gate), or directly bound authentic original fixed-h signed Weyl sums. New needed input: an arithmetic inequality on the SOURCE-SELECTED centered numerator/carries that pays the singular point evaluation or the multiscale pair-collision excess. Baseline categorical units, Gaussian plate interactions, and excellent ensemble concentration do not supply it by themselves.

## Validation and academic authority

- NEW prospectively declared exact-source variance holds A=9,11 evaluated using independent Fraction BBP source and the full Bernoulli pair–pair covariance (actual \(\mathrm{Var}\approx0.020382252392099,0.013976187474423\)); all pair-clock gcd assertions PASS.
- Independently checked Gaussian conditional Schur complements for \((\rho,d,k)=(2/5,4,1),(3/7,7,3),(1/2,5,2)\).
- A second tiny-radix independent numerical midpoint integration of CZ7 gave \(\approx0.15967177\) versus analytic \(\approx0.15964439\), absolute error \(\approx2.74\times10^{-5}\); finite calibration only, not independent mathematical proof.
- 11 local exact/finite test methods pass; source bytes, test source and exact local results should be retained with scope. Neither this research PR nor a parent's prior suite certifies new paper theorems in a Lean kernel.
- Standard categorical point: pointed sets, e.g. J. Rotman, category-theory initial/terminal examples, https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/rotman.pdf . Normality source: Bailey–Crandall (2001), https://doi.org/10.1080/10586458.2001.10504441 .
- No physical Casimir effect/energy claim, no physical quantum vacuum of mathematics, no empirical field-probability statement, no external priority or normality proof.

**Verdict:** the new source/causal field model has exact ensemble neutrality, strong radix-resonance concentration and multi-time source gluing, plus a sharp finite-zero vs exact-zero limit obstruction. \(\pi\) base-16 normality, selected \(s=0\) Fekete lower bound, signed Weyl decay, critical maximal-subinterval gate and RH remain OPEN.
