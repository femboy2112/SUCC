# ABC clock-energy families, exact local laws, and the Green--Tao transference barrier

**Date:** 2026-10-19. **Track:** independent SUCC arithmetic; separate from the completed-Weil/RH signed-Schur program.
**Branch:** `research/abc-clock-green-tao-2026-10-19`, based on SUCC `main` at `4de865766d53ea448555386d98f3e88e3ec605b6`.
**Status:** elementary statements **PROVED LOCAL** by explicit proofs; Green--Tao **EXTERNAL THEOREM**; bounded census **TESTED MODEL**; publication priority **UNVERIFIED**; ABC and RH **OPEN**.

## 0. Objects, sources, and the acceptance boundary

A primitive positive triple `T=(a,b,c)` satisfies `a+b=c` and `gcd(a,b)=1`. These imply pairwise coprimality. Set

\[
R(T)=\operatorname{rad}(abc),\quad H(T)=\frac{abc}{R(T)}=\operatorname{ris}(abc),
\quad X(T)=\log R(T),\quad Y(T)=\log(c/R(T))=\log(H(T)/(ab)).
\]

For rational \(\varepsilon=u/v\ge0\), code computes exactly
\(Q_\varepsilon(T)^v=c^v/R(T)^{u+v}\), where \(Q_\varepsilon(T)=c/R(T)^{1+\varepsilon}\).
**Only values at a fixed epsilon are directly comparable without taking roots.**
All integer computations use sourced actual prime factors, not fake prime impulses. SUCC does not derive the ordinary integers from this construction.

## 1. The primitive prime-clock Haar law (PROVED LOCAL)

Fix a genuine prime \(p\), Haar-uniform \((a,b)\in\mathbb Z_p^2\) conditioned on not both being divisible by \(p\), and \(c=a+b\). At most one slot among \(a,b,c\) is divisible by \(p\). Among the \(p^2-1\) primitive pairs modulo \(p\),

* \((p-1)(p-2)\) have no occupied slot;
* \(p-1\) occupy the \(a\)-slot only, and similarly for the \(b\)- and \(c\)-slots.

Consequently,

\[
\Pr(\text{none})=\frac{p-2}{p+1},\qquad
\Pr(\text{given slot occupied})=\frac{1}{p+1}.
\]

For any fixed slot \(s\in\{a,b,c\}\) and integer \(k\ge1\),

\[
\boxed{\Pr(v_p(s)\ge k)=\frac{p^{1-k}}{p+1},\qquad
\Pr(v_p(s)=k)=\frac{p-1}{(p+1)p^k}.}
\]

**Proof.** For \(s=a\), the Haar probability that \(p^k\mid a\) and \(p\nmid b\) is \(p^{-k}(1-p^{-1})\). Divide by \(1-p^{-2}\), the primitive conditional normalizer. Difference of depths \(k\) and \(k+1\) gives exact depth. Exchange \(a,b\) for the second slot; the integral determinant-one transformation \((a,b)\mapsto(a,a+b)\) proves the third. The modulo-\(p\) counts prove the zero-depth statement. QED.

**Scope of independence.** For a **fixed finite set** of primes, these conditioned \(p\)-adic random variables are independent in the normalized profinite product. Integer pair densities in expanding squares converge to the product of these local laws. Indeed, fix \(M\) containing the relevant prime powers, then use Möbius inversion to count primitive integer pairs in each locally allowed residue cell. Each cell has main term proportional to
\[
\frac{X^2}{M^2}\sum_{\substack{d\ge1\\(d,M)=1}}\frac{\mu(d)}{d^2}
=\frac{X^2}{M^2\zeta(2)}\prod_{p\mid M}(1-p^{-2})^{-1}
\]
with error \(O_M(X\log X)\). **Neither growing \(M\) nor arbitrarily deep simultaneous prime clocks follows from fixed-\(M\) CRT.**

The exact Fourier clock projector is
\[
\mathbf1_{p^k\mid a+b}=\frac1{p^k}\sum_{j=0}^{p^k-1}
e^{2\pi i j(a+b)/p^k},\quad
\mathbf1_{v_p(a+b)=k}=\mathbf1_{p^k\mid a+b}-\mathbf1_{p^{k+1}\mid a+b}.
\]
This is mathematical phase-locking, not quantum phase or stochastic independence along one observed triple.

## 2. An unconditional ABC high-energy sparsity bound (PROVED LOCAL)

**Lemma (ris moment).** For each \(0<\theta<1\) there is \(C_\theta<\infty\) such that
\[
\boxed{\sum_{n\le X}\left(n/\operatorname{rad}(n)\right)^\theta
\le C_\theta X,\quad X\ge1.}
\]

**Proof.** Write \(f_\theta(n)=\operatorname{ris}(n)^\theta\) and \(g_\theta=\mu*f_\theta\) in Dirichlet convolution. This is nonnegative multiplicative: \(g_\theta(p)=0\) and
\[
g_\theta(p^k)=p^{\theta(k-2)}(p^\theta-1)\ge0\quad(k\ge2).
\]
Consequently,
\[
\sum_{d\ge1}\frac{g_\theta(d)}{d}
=\prod_p\left(1+\frac{p^\theta-1}
{p^2(1-p^{\theta-1})}\right)<\infty.
\]
The local correction is \(O_\theta(p^{\theta-2})\), summable over primes for \(\theta<1\). Since \(f_\theta=1*g_\theta\), summing divisors gives \(\sum_{n\le X}f_\theta(n)\le X\sum_{d\ge1}g_\theta(d)/d\). QED.

**Theorem (uniform global subquadratic exceptional-triple count).** For all fixed \(\varepsilon\ge0\), \(\eta>0\), let \(N_\varepsilon(X)\) count primitive triples with \(a\le b\), \(X<c\le2X\), and \(c>\operatorname{rad}(abc)^{1+\varepsilon}\). Then
\[
\boxed{
N_\varepsilon(X)=O_{\varepsilon,\eta}
\left(X^{8/5-\frac{\varepsilon}{5(1+\varepsilon)}+\eta}\right),\quad X\ge2.
}
\]

**Proof.** Put \(\beta=\varepsilon/(1+\varepsilon)\in[0,1)\) and choose \(0<t<1/3\). Pairwise coprimality implies
\(H(T)=\operatorname{ris}(a)\operatorname{ris}(b)\operatorname{ris}(c)\).
Apply Hölder with exponent three to all \(1\le a,b\le2X\) satisfying \(a+b\le2X\), restricted to primitive pairs. For each \(n=a,b,c\), the sum of \(\operatorname{ris}(n)^{3t}\) over these pairs is \(O_t(X^2)\), because each \(n\) occurs at most \(2X\) times and the lemma holds for \(3t<1\). Hence
\[
\sum_{\substack{a,b\ge1,\;a+b\le2X\\(a,b)=1}} H(T)^t=O_t(X^2).
\]

Fix \(0<\alpha<1\) and split at \(\min(a,b)=X^{1-\alpha}\).
Unbalanced triples contribute at most \(O(X^{2-\alpha})\) by elementary counting. On the balanced part, \(ab\ge X^{2-2\alpha}\). The exceptional condition gives \(R<c^{1/(1+\varepsilon)}\), hence
\[
H(T)=abc/R>ab\,c^\beta\ge X^{2-2\alpha+\beta}.
\]
The moment bound and Markov yield \(O_t(X^{2-t(2-2\alpha+\beta)})\) balanced triples. Take
\[
\alpha=\frac{t(2+\beta)}{1+2t}
\]
to equalize exponents and obtain
\[
N_\varepsilon(X)\ll_{\varepsilon,t}
X^{2-\frac{t(2+\beta)}{1+2t}}.
\]
For any \(\eta>0\) fix \(t<1/3\) sufficiently close to \(1/3\). The limiting exponent is \(2-(2+\beta)/5=8/5-\beta/5\); absorb the remaining exponent gap into \(\eta\). QED.

**Firewall:** this is a quantitative density-zero result among \(O(X^2)\) ordinary pair candidates, **not** ABC finiteness or a bound on the global optimal \(K_\varepsilon\). No novelty or optimality claim in the outside literature is made.

## 3. Green--Tao square-completion and the transference no-go (PROVED LOCAL; external infinitude)

Green and Tao prove arbitrarily long progressions of primes; in particular infinitely many distinct three-term prime progressions. Let \(u=p-d,p,v=p+d\) be distinct **odd primes**, \(d>0\). Two primitive triples follow:
\[
T_0=(u,v,2p),\qquad T_\square=(uv,d^2,p^2),
\qquad uv+d^2=p^2.
\]
The first has \(\operatorname{ris}(abc)=1\), because \(2,u,p,v\) are distinct primes, and \(c/R=1/(uv)\).
For the second, \(\gcd(d,upv)=1\), so
\[
\operatorname{rad}(uv\,d^2p^2)=upv\operatorname{rad}(d),\qquad
\operatorname{ris}(uv\,d^2p^2)=p\,d^2/\operatorname{rad}(d).
\]
It follows that
\[
\boxed{\frac{p^2}{\operatorname{rad}(uv\,d^2p^2)}
=\frac{p}{uv\,\operatorname{rad}(d)}<\frac13.}
\]
The strict inequality follows from \(u\ge3\), \(v>p\), \(\operatorname{rad}(d)\ge1\). Since \(R\ge1\), for **every** \(\varepsilon\ge0\), \(c/R^{1+\varepsilon}<1/3\) throughout the family. But \(\operatorname{ris}(abc)\ge p\to\infty\) along Green--Tao's infinite 3-progressions.

**Interpretation:** even infinite repeated-prime depth does not force positive ABC excess. Additive progressions of primes are **not** automatically the high-quality ABC families. Prime authenticity matters: the *composite* AP \(7,8,9\) gives \((63,1,64)\) with \(R=42\) and \(c/R=32/21>1\). This supplies a hostile mutation of the prime constraint.

Original paper: Green--Tao, *The primes contain arbitrarily long arithmetic progressions*, Annals of Mathematics 167 (2008) 481–547, https://annals.math.princeton.edu/2008/167-2/p03 . Tao's primary lecture on transference, the \(W\)-trick, and linear-form complexity: https://terrytao.wordpress.com/2010/06/05/254b-lecture-notes-7-the-transference-principle-and-linear-equations-in-primes/ .

## 4. The exact finite convex envelope and the unresolved global bound

For all primitive triples define
\[
K_*(\varepsilon)=\sup_T\frac{c}{R(T)^{1+\varepsilon}},\quad
\log K_*(\varepsilon)=\sup_T\{Y(T)-\varepsilon X(T)\}.
\]
It is an extended-real convex function, a supremum of affine functions. For a partition into families \(\mathcal F\),
\(\log K_*=\sup_{\mathcal F}\sup_{T\in\mathcal F}(Y_T-\varepsilon X_T)\) is **tautological**, not a uniform estimate.
\(K_*(\varepsilon)<\infty\) for all \(\varepsilon>0\) is precisely ABC's constant-bound formulation.

**Conditional proposition.** If ABC holds, then \(\log K_*\) is locally a maximum of finitely many affine functions and hence locally piecewise linear for \(\varepsilon>0\). Proof: fix \(\varepsilon_0>0\), apply ABC at \(\delta=\varepsilon_0/4\). For \(\varepsilon\ge\varepsilon_0/2\),
\[
Y_T-\varepsilon X_T\le\log K_*(\delta)-(\varepsilon_0/4)X_T.
\]
So large radical implies a uniformly losing branch. Finitely many bounded radicals imply finitely many triples *under ABC at \(\delta\)*, because \(c\le K_*(\delta)R^{1+\delta}\). Therefore only finitely many local active branches remain. Without ABC, finite data cannot establish this conclusion.

Source-family key presently used: \((\omega(abc),\Omega(abc)-\omega(abc),\omega(a),\omega(b),\omega(c))\). It deliberately discards detailed prime labels only for exploratory grouping; the full signature keeps every actual prime and occupied slot. Additional probes should include \(\min(a,b)/c\) and precise \(p\)-adic clock orders. Uniform constants **across unseen families** remain the decisive debt.

### Exact integer experiment, explicitly held out

Run `python scripts/abc_clock_green_tao_probe.py --limit 1200`. Unordered primitive triples \(a\le b\):

| c range | primitive triples | epsilon-0 ABC hits |
| --- | ---: | ---: |
| 3..600 training | 54,749 | 21 |
| 601..1200 holdout | 164,143 | 12 |

At epsilon 0, training maximum \(c/R=9/2\) occurs at \((1,512,513)\); holdout maximum \(49/10\) occurs at \((5,1024,1029)\), **strictly exceeding training**. At \(\varepsilon=1/10\) and \(1/2\), holdout maxima do not exceed training maxima; neither comparison is a universal bound. The held-out range contains 111 family-key values absent from training.

The probe performs exact integer/Fraction comparisons. Tests independently recompute radicals, exhaust small bounded envelopes, enumerate prime-power residue cells, reject counterfeit prime labels, and check \(7,8,9\) as a hostile counterfamily. Finite counts are never promoted to an all-integer theorem.

## 5. Tao's tools: a proposed bridge with a sharp missing obligation

The actual Green--Tao ingredients are (1) pseudorandom majorants for primes or almost primes, (2) a dense-model transference principle, (3) the small-prime \(W\)-trick, and (4) Gowers/Fourier controls for the linear patterns under study. The local Haar clock law provides exact prime-place weights, but **not** a uniform majorant for high-\(\operatorname{ris}\) tails, density relative to that majorant, or moving-modulus linear-forms estimates.

**Next genuinely discriminating theorem attempt:** for some \(t\in[1/3,1)\), prove or refute a uniform \(O_t(X^2)\) bound on the dyadic primitive joint moment \(\sum_{a+b=c}\operatorname{ris}(abc)^t\) using a second, arithmetic-divisor-lattice or sieve route. The current Hölder proof stops at \(t<1/3\). A stronger moment would improve the explicit sparsity exponent, but still would not prove ABC without a new family-uniform extremal bridge. Calibrate against seeded artificial composites, moving CRT moduli, and extremely unbalanced triples.

Formalization debt: YEAN's additive/multiplicative normalizers might certify the finite factor identities, but Lean has not been run for this work. No standard-library Python pass supplies a Lean proof. RH's signed Weil form is an independent, unresolved obstruction.

## 6. Repository cross-checks and scholarly caveats

* SUCC `observational_succ/prime_clock_yoneda.py` supplies an existing actual \(\mathbb Z/p^r\) source-authentication pattern; no imported source dossier was edited.
* YEAN's checked additive–multiplicative transport suggests future verified normal forms; it is **not** an analytic ABC theorem.
* FuckingRH's prime-wavefront and multiplicativity experiments provide rigorous negative controls about source erasure, not a transport from these positive moment bounds to Weil positivity.
* The separate `femboy2112/abc` README makes an unconditional proof claim; no result from it has been assumed or authenticated as a theorem in this branch.
* Related unrefereed 2026 preprint for comparison: R. Laniewski, *Radical defects, Wieferich primes, and the abc conjecture*, https://arxiv.org/abs/2609.00039. No exhaustive scholarly priority audit has been completed.

**Next verdict-changing lamp:** moving-prime-support correlation control with an explicit, uniform high-depth tail. **ABC OPEN. RH OPEN.**


## 7. Primary-literature correction: our moment bound is a baseline, not a record

**External theorem (2026):** C. Bernert, T. Browning, J. D. Lichtman and J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, https://arxiv.org/html/2410.12234 (v2; current 2026 paper). For \(N_\lambda(X)\) counting primitive \(a+b=c\) with \(c\le X\) and \(\operatorname{rad}(abc)<c^\lambda\), Theorem 1.3 establishes
\[
N_\lambda(X)\ll_{\lambda,\delta} X^{3/5+\delta}\quad (0<\lambda<1).
\]
Theorem 1.2 also gives \(X^{(23\lambda+3)/40+\delta}\) for \(0<\lambda\le2\); de Bruijn's classical bound gives \(X^{2\lambda/3+\delta}\), sometimes better than 3/5 for small \(\lambda\). Our epsilon>0 exceptional condition corresponds to \(\lambda=1/(1+\varepsilon)<1\), so their 3/5 bound vastly outperforms section 2. At epsilon=0 (lambda=1), Theorem 1.2 gives exponent 13/20, not 3/5. We make **no novelty or best-known bound claim** for section 2.

Their section 2 already implements a powerful prime-power *anatomic decomposition*: \(n=n_0\prod_{j\le d}n_j^j\), with quantified residual and radical control (Lemma 2.2 and Proposition 2.1). Sections 3 and 4 then apply Fourier and geometry-of-numbers estimates. Thus this work's energy stratification overlaps known, deeper theory. The source-indexed output of ABCTriple.exponent_layers(), which canonically retains all prime labels and slots, satisfies the exact identities
\[
(a,b,c)=\left(\prod_k a_k^k,\prod_k b_k^k,\prod_k c_k^k\right),
\qquad R(abc)=\prod_k a_kb_kc_k.
\]
It lacks their **bounded-d truncation and uniform analytic savings**, which are the essential next comparison. Our next probe should reproduce one quantitative Fourier or geometric estimate on a fully specified prime-layer family, against the published sharp bound. Tao/Green--Tao transference alone does not supply these estimates.

## 8. Exact profinite Gibbs energy threshold (PROVED LOCAL in a declared probability model)

Construct the normalized *profinite primitive Haar* model: independently at each genuine prime p choose Haar-uniform \((a_p,b_p)\in\mathbb Z_p^2\) conditioned on not both being divisible by p; set \(c_p=a_p+b_p\). Define \(V_p=v_p(a_pb_pc_p)\) and \(H_p=p^{(V_p-1)_+}\). The infinite product \(H_{\mathrm{loc}}=\prod_p H_p\) is a random variable of the **profinite model**, not the ris of an ordinary randomly chosen integer triple.

**Theorem ABC-CLK-09.** The product is almost surely finite, and for each integer \(k\ge1\)
\[
\boxed{\Pr(H_p\ge p^k)=\frac{3}{(p+1)p^k}}.
\]
For \(0\le s<1\) its moment factor equals
\[
\boxed{Z_p(s)=\mathbb E H_p^s=
\frac{p-2}{p+1}+\frac{3(p-1)}{p(p+1)(1-p^{s-1})}}.
\]
The global moment \(\mathbb E H_{\mathrm{loc}}^s=\prod_pZ_p(s)\) is finite for \(0\le s<1\), and infinite for \(s\ge1\).

**Proof.** Section 1 yields \(\Pr(V_p=0)=(p-2)/(p+1)\) and \(\Pr(V_p=j)=3(p-1)/((p+1)p^j)\) for \(j\ge1\). Sum the geometric series defining \(Z_p(s)\); at each fixed p it diverges for \(s\ge1\). For \(s<1\), \(Z_p(s)-1=O_s(p^{s-2})\); the sum of these positive increments over primes converges as \(s-2<-1\). Hence the infinite product is finite. Also \(\sum_p\Pr(H_p>1)=\sum_p3/[p(p+1)]<\infty\), so Borel--Cantelli gives finitely many active \(H_p\) almost surely. Independence for fixed sets of p and monotone convergence establish the global product identity. QED.

**Source firewall.** The almost-sure finiteness of this abstract source-indexed product does **not** give a uniform moment bound for \(H(abc)\) on growing integer boxes. That transfer is a separate, still UNVERIFIED local-to-global problem. The threshold is a moment singularity in a p-adic probability model, not a physical energy, an RH sign or quantum evidence.

## 9. Exact Green--Tao shadow fan in an L-term progression

Given an odd-prime AP \(p_0,\ldots,p_{L-1}\) with step d, every \(j=1,\ldots,L-2\) and every \(k=1,\ldots,\min(j,L-1-j)\) supplies a three-prime subprogression and the primitive ABC triple
\[
(p_{j-k}p_{j+k})+(kd)^2=p_j^2.
\]
The number of **distinct square lifts** is exactly
\[
\sum_{j=1}^{L-2}\min(j,L-1-j)
=\left\lfloor\frac{(L-1)^2}{4}\right\rfloor.
\]
For all lifts \(c/\operatorname{rad}(abc)<1/3\), regardless of their repeated-prime energy. Green--Tao gives arbitrarily long prime progressions as an **external theorem**, hence unbounded quadratic fans of individually benign lifts. This sharply falsifies any inference from *many* synchronized prime subprogressions to high ABC quality. The exact code prime_ap_shadow_fan authenticates primes and the original progression; its five-prime example (5,11,17,23,29) yields four distinct lifts, including one with spacing twice the base AP step. No proof of Green--Tao is claimed here.

**Updated local validation:** 14 isolated standard-library unit tests passed under Python 3.13. Full existing SUCC test suite and hosted CI are UNVERIFIED pending an actual complete-checkout run.
