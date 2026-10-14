# Gaussian SUCC observers, prime-sphere chirality, and a signed Weil certificate frontier

**Research date:** 2026-10-14. **Branch:** \`research/gaussian-weil-conditional-certificates-2026-10-14\`. **Pinned parent:** \`9405013730d8b11d016e42736146243a77ff3d5e\` (draft PR #73, source-interaction). **Sibling source:** prime-sphere PR #68 at \`17f1c8da3948ddce719cde301423cb3e31bf6716\`; no merge from that branch is claimed. **Source-critical antecedent:** completed-Weil PR #71 at \`55307fec354be0c671562233ca744907cf716ca5\`. Do not edit \`main\`.

**Firewall:** RH is open. No Gaussian-prior positivity is equated to the genuine Weil sign. No unknown zero is a construction input. No physical sensor, full adelic SUCC functor, scholarly priority, or uniform nonnegative Weil-form lower bound is claimed.

## Source and literature

Primary: Masatoshi Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v3, 23 September 2026), equations (1.3)–(1.8), especially the signed continuous screw kernel \(g\) and equality \(Q_W(v)=\langle G_a(i v'), i v'\rangle\) for compact tests. https://arxiv.org/html/2606.09096v3. Weil's classical criterion states \(Q_W(v)\ge0\) for every \(v\in C_c^\infty(\mathbb R)\) if and only if RH. Rasmussen & Williams, *Gaussian Processes for Machine Learning*, chapter 2, https://gaussianprocess.org/gpml/chapters/RW2.pdf, is the classical source for conditional Gaussian covariance formulae. Existing SUCC source-specific normalizations and the distinction between genuine and auxiliary Gamma modes are from draft PRs #68, #71, #73, not independent blinded external proofs.

### Three inequivalent Gaussians (GWC-0, definitions)

(A) The *authentic real-place* test \(\exp(-\pi tx^2)\), yielding Gamma, theta and Poisson under explicitly imported analytic theorems. (B) A freely chosen *epistemic* Gaussian covariance over the prime-sphere finite toy. (C) A putative Gaussian random linear functional with **exact** covariance \(Q_W\). (B) exists trivially; (C) exists if and only if RH. Do not identify any of them without a proven map.

## I. Exact six-point Gaussian prime sphere (GWC-1, PROVED LOCAL)

Embed the prime-sphere double-cone vertices as \(N=(0,0,1),S=(0,0,-1),E_j=(\cos(j\pi/2),\sin(j\pi/2),0)\) for \(j=0,1,2,3\). This is a geometric realization of **the finite six-vertex sphere only**, not an adelic sphere. Define the covariance
\[
  K_{uv}=\exp[-(\log 2)\|u-v\|^2/2]=2^{-\|u-v\|^2/2}.
\]
In the order \(N,S,E_0,E_1,E_2,E_3\), its full rational matrix is
\[
 \begin{pmatrix}
1&1/4&1/2&1/2&1/2&1/2\\
1/4&1&1/2&1/2&1/2&1/2\\
1/2&1/2&1&1/2&1/4&1/2\\
1/2&1/2&1/2&1&1/2&1/4\\
1/2&1/2&1/4&1/2&1&1/2\\
1/2&1/2&1/2&1/4&1/2&1\\
 \end{pmatrix}.
\]
An independent explicit eigenbasis yields spectrum \(13/4,(3/4)^3,(1/4)^2\), determinant \(351/4096\); no-pivot LDL positive pivots are \(1,15/16,3/5,7/12,15/28,39/80\). Thus K is strictly PSD by exact rational arithmetic. More generally the Gaussian kernel is PSD via \(e^{-c\|x-y\|^2}=e^{-c\|x\|^2-c\|y\|^2}\sum_{m\ge0}(2c)^m(x\cdot y)^m/m!\).

For **true odd primes** \(p\), define \(T_p(E_j)=E_{pj\bmod4}\), fixing poles. These actions all preserve K. Yet the *oriented* area \(\det(E_0,E_1)\) is multiplied by the arithmetic character \(\chi_4(p)=+1\) for \(p\equiv1\bmod4\) and \(-1\) for \(p\equiv3\bmod4\). The prime-3 versus prime-5 action is therefore geometrically indistinguishable to distance-only K but distinguishable by signed source-labelled orientation. The dyadic action (and fake composite 6) collapses equatorial vertices, whereas composite 9 acts isometrically but **must be rejected** by primality authentication. This supplies a precise observer-language gap, not RH positivity.

## II. Borehole posterior as finite source-relative uncertainty (GWC-2, CLASSICAL + PROVED LOCAL)

Under an *assumed*, independently labelled Gaussian source law, noisy observations \(y\) on sites O with variance \(\eta^2\ge0\) yield
\[
 \mu_{x|O}=K_{xO}(K_{OO}+\eta^2I)^{-1}y,\quad
 \operatorname{Var}(X_x|O)=K_{xx}-K_{xO}(K_{OO}+\eta^2I)^{-1}K_{Ox}.
\]
For noise-free equator observations O successively \((E_0)\), \((E_0,E_1)\), \((E_0,E_1,E_2)\), and all four equator sites, the **exact** unobserved north-pole variances are \(3/4,2/3,7/12,5/9\). Thus four measurements contract Gaussian-model uncertainty while leaving substantial unseen uncertainty. The Gaussian choice and its noise law are assumptions: finite data alone do not certify the true arithmetic source.

## III. Observer sign blindness (GWC-3, PROVED LOCAL)

For arbitrary infinite-dimensional real Hilbert space H and finite observed span E, take a unit \(e\in E^\perp\). \(A_+=I\) and \(A_-=I-2|e\rangle\langle e|\) have identical observed compression \(P_EA_\pm P_E\), but \(\langle e,A_-e\rangle=-1\). Every finite set of continuous linear probes has an unprobed orthogonal direction. This produces *candidate-model* sign nonidentifiability, **not** a source-preserving mutation of zeta. It ceases to be an obstruction once one obtains source-derived **uniform operator-tail bounds** over every direction.

## IV. Gaussian-windowed probes dense in the full compact test domain (GWC-4, PROVED LOCAL)

For \(a,\sigma>0\), define \(b_a(x)=\exp[-1/(a^2-x^2)]\) when \(|x|<a\), zero otherwise, and \(v_n(x)=b_a(x)e^{-x^2/(2\sigma^2)}x^n\). The span of the \(v_n\) is dense in \(H_0^1(-a,a)\). Indeed for \(f\in C_c^\infty(-a,a)\), the quotient \(f/(b_a e^{-x^2/(2\sigma^2)})\) is \(C^\infty\) on the closure and zero near its endpoints. Polynomial approximation in C¹ follows from uniform polynomial approximation of the derivative, integration, and an adjusted constant. Multiplying by the fixed smooth weight transfers convergence in C¹ and hence H¹. Density of \(C_c^\infty\) gives the result.

The Weil form is continuous on \(H_0^1(-a,a)\) by Suzuki's bounded-interval continuous screw-kernel representation. Therefore verifying every finite Gram of all these windows for every a is **equivalent** to Weil positivity/RH. Finite truncations remain only finite tests.

## V. The signed authentic Weil kernel: uniform finite step approximation (GWC-5, PROVED LOCAL conditional on Suzuki's classical identification)

Let \(g:\mathbb R\to\mathbb R\) be the *actual* even continuous screw potential in Suzuki's Eq. (1.3), with the exact full prime-power tape and one real Gamma factor. For \(r=|t|\),
\[
g(t)=-4(e^{r/2}+e^{-r/2}-2)+\sum_{p^k\le e^r}{\log p\over p^{k/2}}(r-k\log p)
- {r\over2}(\psi(1/4)-\log\pi)
-4\sum_{j\ge0}{1-e^{-(4j+1)r/2}\over(4j+1)^2}.
\]
Let \(g_J\) retain exactly the first J Gamma rungs, and leave **all other terms unmodified**. This is a signed source representation, not a positive GP covariance. Positivity of the source coefficients or Gamma summands alone gives no Weil sign.

**Uniform tail:** for every t, the missing rungs are nonnegative and
\[
  \|g-g_J\|_{L^\infty(\mathbb R)}
 \le \tau_J:= {1\over4J+1}+{4\over(4J+1)^2}.
\tag{1}
\]
Proof: \(4\sum_{j=J}^\infty (4j+1)^{-2}\le 4[(4J+1)^{-2}+\int_J^\infty(4x+1)^{-2}dx]\).

**Lipschitz:** for each \(a>0\), on \([-2a,2a]\), \(g_J\) has Lipschitz constant at most
\[
L_J(a)=2(e^a-e^{-a})+\tfrac12|\psi(1/4)-\log\pi|
 +\sum_{p^k\le e^{2a}}{\log p\over p^{k/2}}
 +2\sum_{j=0}^{J-1}{1\over4j+1}.
\tag{2}
\]
Use \(r\mapsto(r-b)_+\) 1-Lipschitz and \(1-e^{-\alpha r}\) derivative bounded by \(\alpha\), plus the pole derivative bound. At fixed a, \(L_J(a)=O_a(\log J)\). Both bounds are analytic; **numerical transcendental evaluation is not automatically a validated interval**.

Let \(H_a=L_0^2(-a,a)\) be the mean-zero closed subspace and \(P_a\) its orthogonal projection. On H_a, let \(G_a=P_aT_gP_a\), where \(T_gf(x)=\int_{-a}^a g(x-y)f(y)dy\). Split \((-a,a)\) into N equal intervals, width \(h=2a/N\), centers \(c_i\), and let \(G_{a,J,N}\) be \(P_a\) times the finite block kernel \(g_J(c_i-c_j)\) times \(P_a\). Every point in block i,j satisfies \(|(x-y)-(c_i-c_j)|\le h\). Consequently Schur's bound on an interval of length \(2a\) gives
\[
 \boxed{ \|G_a-G_{a,J,N}\|_{H_a\to H_a}
 \le \varepsilon_{a,J,N}:=2a(\tau_J+{2a\over N}L_J(a)). }
\tag{3}
\]
This holds **simultaneously for every compact test**: it is not a claim from inspected finite Gram spectra. Choosing \(N=J^2\) yields \(\varepsilon_{a,J,J^2}=O_a(1/J)\). Fixed a, not a uniform all-a bound.

The step operator on its finite cellwise constant mean-zero subspace is represented by \(M_{ij}=h\,g_J(c_i-c_j)\), restricted to \(\sum_i z_i=0\). It annihilates the infinite-dimensional complement. If a rigorous **lower certificate** proves \(M|_{\mathbf 1^\perp}\succeq-\delta I\) for \(\delta\ge0\), then Suzuki's \(Q_W(v)=\langle G_a(i v'),i v'\rangle\) yields the **true source-domain bound**
\[
 \boxed{Q_W(v,v)\ge-(\delta+\varepsilon_{a,J,N})\|v'\|_{L^2}^2
  \quad(v\in H_0^1(-a,a)).}
\tag{4}
\]
If for every positive integer a one constructs from genuine source laws sequences with \(\delta+\varepsilon\to0\), then Weil positivity and RH follow. **No such source-derived lower-bound sequence is proved here.** If RH fails, a compact negative witness eventually forces a negative certified finite matrix once errors become small. This is an exact, falsifiable reduction with explicit errors, not a proof of the missing sign.

**Contact calibrator:** the signed finite source potential \(\Psi_J\) of existing PR #71 and Suzuki's \(g_J\) satisfy exactly
\[
 \Psi_J(R)+g_J(R)
 =R\left({\pi\over4}+{\log2\over2}
 -\sum_{j=0}^{J-1}\left({2\over4j+1}-{1\over2j+1}\right)\right).
\tag{5}
\]
The limit \(\Psi=-g\) follows by digamma identities. The finite truncations are **not identical** until this linear Gamma contact correction is retained. Independently checked at nine numerical sample pairs, not asserted as a machine proof of the distribution identity.

**Compactness trap:** the genuine continuous bounded-interval G_a is compact. Therefore its quadratic form cannot enjoy a strict uniform positive gap \(Q_W(v)\ge c\|v'\|^2\) for fixed \(c>0\) on the infinite-dimensional H0¹ space. Seek error-controlled vanishing negative parts, never an impossible global coercivity constant.

## VI. Gaussian existence for exactly the Weil covariance (GWC-6, CLASSICAL EQUIVALENCE)

On the real test space \(D=C_c^\infty(\mathbb R;\mathbb R)\), define \(C_W(f,h)=W(f*\widetilde h)\). There exists a consistently jointly Gaussian centered family \(X(f)\), linear in L² of probability and satisfying \(\mathbb E[X(f)X(h)]=C_W(f,h)\) **if and only if RH**. Necessity: covariance matrices are PSD, hence Weil positivity. Sufficiency: assuming Weil positivity, each finite covariance matrix is PSD, so centered multivariate normal laws are consistent and realize the family via Gaussian Hilbert space/Kolmogorov extension. This is not a constructive source-first proof; nor does it assert a tempered generalized stochastic field or sample-path regularity. The authentic Weil W is not interchangeable with the independently positive toy K.

## VII. Global-curve uniqueness versus finite observer model classes

With only finitely many sample values and functional equation symmetry, infinitely many reflected analytic candidates can match samples while acquiring extra off-critical zeros, e.g. by multiplying \(\xi(s)\) by \(1+c\,s(s-1)\prod_i(s-s_i)(s-(1-s_i))\) with reality-reflection partners included. Such candidates fail to share the *authentic Euler germ* on an open \(\Re s>1\) domain. By the identity theorem the full genuine completed zeta's analytic continuation is unique. Thus the desired “number of allowed global curves” should be formalized as a *finite-history admissible model class given an explicit probe language*, not as freedom to choose another zeta completion despite all source laws.

## VIII. Claim summary and remaining verdict-changing experiment

| Claim | Status | Independent discriminator / limitation |
|---|---|---|
| GWC-1 | PROVED LOCAL | Exact rational K eigenbasis/LDL; signed character is unseen by radial K |
| GWC-2 | CLASSICAL + PROVED LOCAL | Rational GP Schur complements; law is chosen, not measured |
| GWC-3 | PROVED LOCAL | Rank-one invisible negative model; not Euler/source lawful |
| GWC-4 | PROVED LOCAL | Weighted polynomial C¹ density; all finite test matrices required |
| GWC-5 | PROVED LOCAL + CLASSICAL IMPORT | Uniform signed operator error (1)-(4); true matrix sign **UNVERIFIED** |
| GWC-6 | CLASSICAL EQUIVALENCE | Gaussian Weil covariance exists iff RH; existence NOT constructed |
| RH positivity | UNVERIFIED | Needs \(\delta\to0\) with genuine source full-test control |

**Priorities:** (1) implement genuinely validated rational/interval enclosures for prime-log, digamma and exp in \(M_{ij}\) and \(L_J(a)\); independent certified spectral lower-bound decomposition in mean-zero coordinates; (2) test alternative Hermite/heat Galerkin discretizations, compare the lower eigenvectors and scaling N,J; (3) matched non-Euler and fake-composite source mutations, preserving conductor/functional-equation tests; (4) derive or falsify a positive source-defined factorization of the **authentic** Q_W, without smuggling in its square root. Negative finite certificates are allowed and decisive; finite positive certificates with a nonzero residual are never silently universal.

**Research classification:** finite Gaussian GP = SimpleField under declared prior; source-transmitting signed Weil operator = IdealHard candidate; globally source-derived positivity may be an unsolved IdealHard pathway or, if an off-line zero is established, a true mathematical boundary. Neither “FuckedSpace” nor RH truth follows from the analogy.
