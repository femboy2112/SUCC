# Dual slope–cofactor descent and the exterior-dimension ladder

**Research date:** October 20, 2026. **Parent:** Academic Main VII at b5f9591033db2022bda6a2f16a935c06466f9eff. **Status:** PROVED PAPER for the elementary claims below, TESTED FINITE for exact executable controls, OPEN for the proposed weighted high-divisor savings. This work claims no proof of the abc conjecture, no improvement to the \(t<2/3\) weighted moment range, no RH or signed-Weil result, no Lean verification and no established academic novelty. The components are classical linear algebra, geometry and arithmetic; their organization is new to SUCC.

## A. The actual remaining two-summand obstruction

For primitive \(a+b=c\le X\), set \(H=abc/\operatorname{rad}(abc)\). With the positive powerful-divisor coefficients \(g_t\) already established in CLOUD-ABC-01, the exact triple expansion is
\[
S_t(X)=\sum_{\substack{d,e,f\ge1\\(d,e)=(e,f)=(d,f)=1}}
g_t(d)g_t(e)g_t(f)N_X(d,e,f).
\]
Primitive rational-slope separation gives \(N_X(d,e,f)\le 1+X^2/(def)\). For all \(0\le t<1\) the entire sector \(def\le X^2\) therefore contributes at most \(2E_3(t)X^2\), where \(E_3(t)\) is a finite Euler product. The **only unsummed sector** for this method is
\[
\mathcal R_t(X)=\sum_{\substack{def>X^2\\\text{pairwise-coprime moduli}}}
g_t(d)g_t(e)g_t(f)N_X(d,e,f).
\]
Here \(N_X\le1\), but summing possible singleton contributions without estimating their **arithmetic incidence** is invalid.

A concrete OPEN target is a uniform dyadic saving
\[
\mathcal I_t(X,Q)=
\sum_{Q<def\le2Q}g_t(d)g_t(e)g_t(f)N_X(d,e,f)
\ll_t X^2\left(\frac{X^2}{Q}\right)^{\sigma_t}
\quad(Q>X^2,\ \sigma_t>0).
\]
This would sum geometrically and prove \(\mathcal R_t(X)\ll_t X^2\). It is a conjectured useful **sufficient estimate**, not a theorem. In particular, our cofactor identity below does not already imply it.

## B. Cofactor duality for any number of summands — COF-01

Fix an integer \(m\ge2\), and positive integers \(x_1,\ldots,x_m,c\) satisfying \(x_1+\cdots+x_m=c\le X\). Let \(d_i\mid x_i\) for \(i\le m\) and \(d_{m+1}\mid c\); set \(x_i=d_i u_i\) and \(c=d_{m+1}u_{m+1}\). Put
\[
D=\prod_{i=1}^{m+1}d_i,\qquad
U=\prod_{i=1}^{m+1}u_i.
\]
The dual Diophantine equation is
\[
d_1u_1+\cdots+d_mu_m=d_{m+1}u_{m+1}.
\]
AM–GM applied to the positive summands gives the **exact inequality**
\[
\boxed{DU=c\prod_{i=1}^{m}x_i
\le \frac{c^{m+1}}{m^m}
\le \frac{X^{m+1}}{m^m}.}
\]
Therefore \(D>X^m\Rightarrow U<X/m^m\). For \(m=2\), this recovers \(DU\le X^3/4\) and \(D>X^2\Rightarrow U<X/4\).

**Status: PROVED PAPER, classical.** Small complementary products do not by themselves bound how frequently the dual equation has solutions.

## C. Exterior determinant theorem — EXT-01 and EXT-02

Add the hypothesis that all \(m+1\) moduli \(d_i\) are **pairwise coprime**. Choose **any** \(m\) admissible solutions and form the integer \(m\times m\) matrix \(A\) with first \(m\) coordinates of each solution as one column.

**EXT-01 (PROVED PAPER).**
\[
\boxed{D\mid\det A,\qquad |\det A|\le X^m.}
\]

**Divisibility proof.** For \(1\le i\le m\), all entries of row \(i\) are divisible by \(d_i\), so \(\prod_{i\le m}d_i\mid\det A\). In each column the sum of all \(m\) rows equals the corresponding \(c\), a multiple of \(d_{m+1}\). Replacing one row by the row sum preserves the determinant; hence \(d_{m+1}\mid\det A\). Pairwise coprimality combines these to \(D\mid\det A\).

**Archimedean proof.** Hadamard gives \(|\det A|\le\prod_j\|A_j\|_2\). Since the summands are positive, \(\|A_j\|_2\le\|A_j\|_1=c_j\le X\), proving \(|\det A|\le X^m\).

**EXT-02 (PROVED PAPER).** If \(D>X^m\), every choice of \(m\) admissible source points has zero determinant. Therefore **all** first-\(m\) coordinate vectors span a rational subspace of dimension at most \(m-1\). The same holds for first-\(m\) **cofactor** vectors, because multiplication by \(\operatorname{diag}(d_1,\ldots,d_m)\) is invertible over \(\mathbb Q\).

For \(m=2\), rank at most one plus primitive reduced coordinates forces all admitted positive solutions to be the **same** point: this is the original singleton rule. For \(m\ge3\), rank drop is not the same as uniqueness.

## D. A strong negative control: high-D can have arbitrarily many primitive solutions in dimension 3

Fix \(K\ge3\), choose an **odd** \(n\) divisible by every odd prime at most \(K-1\), and take it sufficiently large, say \(n>12K^3\). Let
\[
(d_1,d_2,d_3,d_4)=(n,n+1,2n+1,3n+2),\qquad X=K(3n+2).
\]
These four moduli are pairwise coprime. For every \(k=2,\ldots,K\), put
\[
(a_k,b_k,z_k,c_k)=
\big((k-1)n,\ (2k-1)(n+1),\ 2n+1,\ k(3n+2)\big).
\]
Every point satisfies \(a_k+b_k+z_k=c_k\le X\), and \(d_i\) divides its corresponding coordinate. Further,
\[
\gcd(a_k,z_k)=\gcd(k-1,2n+1)=1,
\]
because each odd prime dividing \(k-1\) divides \(n\), while \(2n+1\) is odd and equals \(1\) modulo every such prime. Thus every solution is **primitive**, even in the strong sense that its first and third coordinates are coprime.

There are \(K-1\) distinct solutions. Their first three coordinate vectors have rank exactly two, since they are affine-linear in \(k\) with independent constant and slope vectors.

On the other hand,
\[
D=n(n+1)(2n+1)(3n+2)>6n^4,\qquad
X=K(3n+2)\le4Kn,
\]
so \(D>X^3\) whenever \(n>12K^3\).

**EXT-03 (REFUTED naive generalization):** The assertion \(D>X^m\Rightarrow N_X\le1\) fails spectacularly already at \(m=3\), with **unbounded multiplicity** as \(K\) increases. Only the rank drop is universally true.

Frozen exact sample: \(n=1001,K=3\), moduli \((1001,1002,2003,3005)\), \(D=6037084083030\), \(X=9015\), \(X^3=732651078375\); two admissible primitive points are \((1001,3006,2003,6010)\) and \((2002,5010,2003,9015)\). Both satisfy the same high-D conditions and are nonproportional.

This shows why a legitimate \(X^2\to X^3\to X^4\) method must introduce **successive exterior rank, lower-dimensional lattice sections, and arithmetic incidence**, not merely an exponent substitution.

## E. An all-dimensions residue simplex bound — SMP-01

Let \(m,W\ge1\) and let \(R\subseteq(\mathbb Z/W\mathbb Z)^m\) be a set of \(r\) distinct canonical residue vectors. Let
\[
N_R^{(m)}(X)=\#\{(x_1,\ldots,x_m)\in\mathbb Z_{>0}^m:
\sum x_i\le X,\ (x_i\bmod W)_i\in R\}.
\]
For one residue vector choose representatives \(\rho_i\in\{1,\ldots,W\}\), with \(0\bmod W\) represented by \(W\). Writing \(x_i=\rho_i+Wn_i\), \(n_i\ge0\), and \(n=\lfloor(X-\sum\rho_i)/W\rfloor\), the exact count is \(\binom{n+m}{m}\) for \(n\ge0\), otherwise zero.

Put \(t=X/W\ge0\). When \(n\ge0\), each of the \(m\) factors in \(m!\binom{n+m}{m}\) differs from \(t\) by at most \(m\), and lies between 0 and \(t+m\). Telescoping the product yields
\[
\boxed{\left|N_R^{(m)}(X)-\frac{r}{m!}(X/W)^m\right|
\le\frac{rm^2}{m!}(X/W+m)^{m-1}.}
\]
When \(n<0\), \(t<m\), and the same bound follows immediately from \(t^m\le m^2(t+m)^{m-1}\). Summing over disjoint residue vectors proves the general estimate for **all** \(m,W,X,R\), including sparse sets.

For \(X>0,r>0\), the relative discrepancy is bounded by
\[
\frac{m^2W}{X}\left(1+\frac{mW}{X}\right)^{m-1}
\le\frac{m^2W}{X}\exp\left(\frac{m^2W}{X}\right).
\]
Consequently **SMP-02 (PROVED PAPER):** \(m^2W/X\to0\) is a sufficient condition for uniform joint growth \(m=m(X)\to\infty\), even with sparse changing residue sets. This is not asserted necessary for structured sources. At \(m=2\) the Main VII CRT theorem has a better sharp constant; preserve it.

For \(W=1\) and all coordinates positive, **exactly**
\[
N^{(m)}(X)=\binom{\lfloor X\rfloor}{m}.
\]
For integer \(X=N\) and \(m=\lfloor c\sqrt N\rfloor\), fixed \(c>0\),
\[
\frac{\binom Nm}{N^m/m!}
=\prod_{j=0}^{m-1}(1-j/N)\longrightarrow e^{-c^2/2}\ne1.
\]
This supplies a genuine sharp-scale countercontrol to treating fixed-\(m\) volume asymptotics as uniform in \(m\). In particular, for strictly positive summands, \(m>X\) gives zero integer solutions, so a literal \(X^\infty\) simplex-volume extrapolation is not a global count.

## F. What an X-infinity carrier can actually mean

At a fixed finite budget \(X\), there is no infinite sequence of **strictly positive integers** whose sum is at most \(X\). If zeros are permitted and all coordinates have unit cost, then arbitrarily far singleton coordinates yield infinitely many labeled states even at budget \(X=1\).

A legitimate discrete infinite carrier can instead declare integer weights \(w_j\ge1\) and count finitely supported nonnegative \(u_j\) satisfying \(\sum_jw_ju_j\le X\). Such counts are finite for every finite \(X\) **if and only if** \(w_j\to\infty\). One direction: only finitely many coordinates have cost at most \(X\), and all occupations are bounded. Conversely, infinitely many \(w_j\le M\) give infinitely many distinct singleton states below cost \(M\).

With \(w_j=j\), the formal local-degree generating series is
\[
\prod_{j\ge1}(1-z^j)^{-1}=\sum_{n\ge0}p(n)z^n,
\]
so the budget-\(X\) count is \(\sum_{n\le X}p(n)\), the cumulative integer-partition function. The product exists coefficientwise because the weights escape to infinity; this is **not** an analytic-convergence assertion and not a universal identification of \(X^\infty\).

A Hilbert/operator infinite exterior completion would instead need suitable operator-ideal conditions, compatible cylinder measures or analogous genuine convergence and source-realization proofs.

## G. Global primitivity becomes generic while pairwise coprimality becomes rare

A new exact **local clock divergence** appears already at fixed genuine prime \(p\), when \(m\) grows. For independent summand residues in \((\mathbb Z/p\mathbb Z)^m\):

- Global primitivity at \(p\) means **not all \(m\) slots are divisible by \(p\)**. Probability: \(P_{\mathrm{gcd},p}(m)=1-p^{-m}\).
- Pairwise coprimality among the \(m\) summand slots means **at most one is divisible by \(p\)**. Probability:
  \[
  P_{\mathrm{pair},p}(m)=(1-1/p)^m+
  \frac m p(1-1/p)^{m-1}.
  \]

These are exact finite residue counts, not an independence assertion across different integer prime places. At \(m=2\) they coincide. At \(m=3,p=2\), the first probability is \(7/8\), while the second is \(1/2\). For fixed \(p\) and \(m\to\infty\), the first tends to **one** and the second to **zero**.

Thus the naive two-summand Euler factor, where every prime occupies at most one summand slot, gets **less** representative of globally primitive source tuples as dimension grows—not more. The total \(c=\sum_i x_i\) is an additional coordinate whose local divisibility is correlated by actual additive cancellation, requiring a separate valuation-compatibility or character constraint.

This is an exact reason to introduce prime-valuation **hypergraphs** and source-typed local cancellation gates instead of extending the two-summand pairwise-coprime support grammar to higher dimensions.

## H. Missing machinery and exact next research questions

**Priority 1 — Two-summand high-divisor incidence (the actual \(t=2/3\) frontier).** Use \(du+ev=fw\), \(D=def>X^2\), \(U=uvw<X/4\) and the genuine powerful weights \(g_t\). Derive a dyadic \(D\)-dependent incidence saving, or an improved high-\(H\) tail. Coarse cofactor cardinality alone is insufficient; treat generalized-Fermat/Pythagorean-square families as adversarial examples.

**Priority 2 — Rank-stratified \(m\)-summand incidence.** Top wedges detect rank drop, not cardinality. Use Smith normal form, lattice saturation/covolume, lower Plücker minors and successive minima to bound lower-rank sections. Record counterexamples before proposing any stronger universal density bound.

**Priority 3 — Local prime-clock compatibility.** For \(m\ge3\), a primitive gcd condition does not force pairwise coprimality of all summands: \(6,10,15\) have joint gcd 1 but nontrivial pairwise gcds. The divisor support and local Euler factors must therefore be indexed by genuine prime-valuation patterns, not the two-summand rule that one prime occupies at most one slot.

**Priority 4 — Dimension-uniform geometry.** Make \(m,W,X\) explicit variables and keep SMP-01's actual growth condition. Develop dimension-dependent simplex/Farey/Grassmannian bounds and test whether the source constraints allow better than \(m^2W/X\).

**Priority 5 — Infinite-carrier completion.** Construct an actual projectively compatible weighted source or probability law. No unweighted \(X^\infty\) count is allowed. Prove finite-cylinder identities, quantitative tightness and honest limit transport first.

**Priority 6 — Formalization.** Extend PR #211's kernel-checked primitive determinant into a row-sum determinant divisibility lemma and exterior rank-drop certificate for arbitrary fixed \(m\); encode the rank-two high-D counterfamily as a hostile control.

**Prior art, not novelty claims:** classical determinant and geometry-of-numbers methods; Per Salberger, *Counting rational points on projective varieties*, 2023, https://doi.org/10.1112/plms.12508 ; Oscar Marmon, *A generalization of the Bombieri–Pila determinant method*, 2010, https://arxiv.org/abs/0905.4443 . These investigate much stronger projective/integer point bounds than the simple elementary lemmas certified here. Do not suggest EXT-01 is academically new without independent review.

## H. Exact executable controls

The new standard-library module exterior_cofactor_ascent.py and test_exterior_cofactor_ascent.py supply deterministic integer/Fraction checks: exhaustive small stars-and-bars counts, residue-simplex errors, strict type guards, exact Bareiss determinants, m=2 singleton calibration, explicit m=3 counterfamilies with unbounded multiplicity, cofactor AM–GM checks, failure of pairwise-prime simplification in m>=3, and the locally finite partition carrier.

These are **falsification controls** supporting the complete elementary proofs above, not standalone proofs of their universal quantifiers. The high-divisor dyadic estimate remains OPEN. No existing source archive, theorem, namespace registry or main commit is modified by this research branch.
