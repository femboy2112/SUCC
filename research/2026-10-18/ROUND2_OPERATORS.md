# Forward disjointness of atomic and profinite dilation representations

Date: 2026-10-18. Base: `e42096ec0186228dd0f748767599e470f2ca2e1d`.
Stream A of Round II; follows [the atomic/Haar paper](INSTITUTE_ATOMIC_HAAR.md).

**Result.** For any set of primes S, the atomic and additive-Haar dilation
representations admit a nonzero bounded intertwiner, in either forward
direction, exactly when the reciprocal sum over S converges. No adjoint
intertwining hypothesis is needed for the obstruction. This strengthens the
project's earlier classification of intertwiners that preserve adjoints.
The proof uses a finite-group harmonic-mass transfer, Fourier coefficients,
and the common kernels of the adjoints. It covers every atomic wandering
component. The normalized GCD Gram is positive definite at every finite
size, while its synthesis norms diverge; finite positivity cannot supply a
bounded infinite transport.

The complete operator statements below have status **PROVED, PAPER**.
Three elementary residue-transfer lemmas have separate **LEAN KERNEL**
certificates. Exact finite calculations check their implementations and
give spectral enclosures; they do not prove the infinite statements.
The academic novelty of the exact operator theorem is **UNKNOWN**. Its
ingredients and the GCD-matrix theory are classical.

## 1. Definitions and claim ledger

All Hilbert spaces are complex. Inner products are linear in their first
argument. Put

\[
 H_d=\ell^2(\mathbb N_{>0}),\quad V_n e_m=e_{nm},\qquad
 H_c=L^2(\widehat{\mathbb Z},\mu),\quad
 (U_n f)(x)=\sqrt n\,1_{n\widehat{\mathbb Z}}(x)f(x/n),
\]

where mu is normalized additive Haar measure. Division by n is the inverse
of the continuous injection y maps to ny onto its image. Haar scaling is
mu(nA)=mu(A)/n. Hence U_n and V_n are isometries, and U_m U_n=U_mn and
V_m V_n=V_mn. The adjoint formula is

\[
 (U_n^*f)(y)=n^{-1/2}f(ny),\qquad
 \ker U_n^*=L^2(\widehat{\mathbb Z}\setminus n\widehat{\mathbb Z}). \tag{1}
\]

For S a set of primes, let M_S be the positive integers whose prime factors
belong to S (including 1), and let R_S be the S-free positive integers.
Every positive integer has a unique factorization km with k in M_S and m
in R_S. No density or effective enumeration assumption on S is imposed.

| ID | Quantified statement | Status and boundary |
|---|---|---|
| FWD01 | If bounded T:H_d to H_c satisfies TV_p=U_pT for every prime p, then T=0. | PROVED, PAPER; Section 3. No adjoint hypothesis. |
| FWD02 | If bounded T:H_c to H_d satisfies TU_p=V_pT for every prime p, then T=0. | PROVED, PAPER; Section 4. |
| FWD03 | For every prime subset S, a nonzero bounded forward intertwiner exists in each direction iff sum over S of 1/p is finite. | PROVED, PAPER; Sections 2–5. Existence is equivalent in both directions. |
| COST03 | The finite Gram is gcd(m,n)/sqrt(mn); the exact spectral lower/upper bounds in Section 6 hold. | PROVED, PAPER; bounded exact enclosures additionally executed. No sharp asymptotic for its largest eigenvalue asserted. |
| RESIDUE-CORE | A positive inverse residue multiplier transfers one class injectively into the identity class, preserves a multiplicative monoid, and scales a prefix by at most C. | LEAN KERNEL for precisely the explicit hypotheses in Section 8. |

These are representation-theoretic statements. They do not authenticate a
physical carrier, identify an observed covariance with a Weil form, or
establish RH. Common provenance is retained: the derivations and tests here
share one model lineage; alternative decompositions are checks, not
independent model votes.

## 2. Harmonic divergence in the identity residue class

**Lemma 2.1 (finite-group transfer).** Let M be a multiplicative submonoid
of positive integers, all coprime to q, where q is a positive integer. If
the sum of 1/n over M diverges, then

\[
 \sum_{\substack{n\in M\\n\equiv1\pmod q}}\frac1n=\infty. \tag{2}
\]

**Proof.** The image H of M in the finite group of units modulo q is a
subgroup: for every a in the image, the positive power a^(ord(a)-1) is its
inverse and remains in the image. For each a in H choose once and for all
t_a in M having residue a^(-1), and put h=|H| and C=max t_a. Every n in
M with residue a maps to t_a n in the identity class. Within that class
the map is injective. Across all classes an image has at most h preimages.
For every positive integer N, therefore,

\[
 \begin{split}
 h\!\sum_{\substack{k\in M,\ k\equiv1\ (q)\\k\le CN}}\frac1k
 &\ge \sum_{\substack{n\in M\\n\le N}}\frac1{t_{[n]}n}
 \ge C^{-1}\sum_{\substack{n\in M\\n\le N}}\frac1n .
 \end{split} \tag{3}
\]

The finite constants h,C are independent of N, proving (2). For q=1,
H is the trivial group and t=1 works. This argument does not require that
any generator itself lie in residue 1, equidistribution of primes, or
Dirichlet's theorem. QED.

**Corollary 2.2.** If sum over p in S of 1/p diverges, then for every q,

\[
 \sum_{\substack{n\in M_S\\ n\equiv1\pmod q}}\frac1n=\infty. \tag{4}
\]

**Proof.** Remove the finitely many primes dividing q to obtain S'. Its
reciprocal-prime sum still diverges. Unique factorization and monotone
limits of finite products give

\[
 \sum_{n\in M_{S'}}\frac1n
 =\sup_{F\subset S',\ F\text{ finite}}\prod_{p\in F}(1-p^{-1})^{-1}
 =\infty,
\]

since minus log(1-1/p) is at least 1/p. Apply Lemma 2.1 to M_S', a submonoid
of M_S. The identity residues in M_S and M_S' in fact coincide, but only
inclusion is needed. QED.

The same Euler-product calculation shows convergence of the monoid
harmonic sum when the reciprocal-prime sum converges: for p at least 2,
minus log(1-1/p) is at most 2/p.

## 3. Atomic-to-Haar forward disjointness

**Theorem 3.1.** If sum over p in S of 1/p diverges, every bounded linear
T:H_d to H_c satisfying TV_p=U_pT for every p in S is zero.

**Proof.** For r in Q/Z let chi_r be the additive character of the
profinite integers, and write ghat(r)=inner product of g and chi_r.
Changing variables x=ny with Haar scaling gives, for every g in H_c,

\[
 \langle U_n g,\chi_r\rangle
 =n^{-1/2}\widehat g(nr). \tag{5}
\]

This formula is well-defined for L² classes, by Haar scaling and
Cauchy–Schwarz. It does not assume pointwise evaluation of g at integers.

Fix **any** S-free integer m and set g_m=T e_m. Iterating the given
forward intertwining relation yields T e_nm=U_n g_m for every n in M_S.
If r has additive order q and n is 1 modulo q, then nr=r. The input
vectors e_nm are distinct orthonormal vectors. Boundedness of T, applied
to T*chi_r, gives

\[
 \|T\|^2\ \ge
 \sum_{n\in M_S}|\langle Te_{nm},\chi_r\rangle|^2
 \ \ge |\widehat g_m(r)|^2
 \sum_{\substack{n\in M_S\\ n\equiv1\ (q)}}\frac1n. \tag{6}
\]

The sums can first be taken over finite subsets, so no divergent-series
manipulation is implicit. Corollary 2.2 forces ghat_m(r)=0. Additive
characters are total in H_c: on each finite quotient the characters form
a Fourier basis, and finite-cylinder functions are dense in L² of the
inverse limit. Hence g_m=0 for every S-free m. Unique factorization and
T e_nm=U_n g_m then kill every atomic basis vector; boundedness extends
this to all of H_d. QED.

FWD01 is the case S equal to all primes, whose reciprocal sum diverges.
The proof uses orthonormal **input** vectors; it never asserts that their
images under T are orthogonal. Checking g_1 alone would miss other
components for a proper S, such as m=5 when S={2,3}. The quantifier over m
is essential to the component-based proof.

## 4. Haar-to-atomic forward disjointness

**Theorem 4.1.** If sum over p in S of 1/p diverges, every bounded linear
T:H_c to H_d satisfying TU_p=V_pT for p in S is zero.

**Proof.** Taking adjoints of the actual given equation yields
U_p* T*=T* V_p*. Fix any positive integer m. Whenever p in S does not
divide m, V_p* e_m=0; thus T*e_m lies in the common kernel of U_p* for
all such p. By (1) it is supported on

\[
 E_{S,m}=\bigcap_{\substack{p\in S\\p\nmid m}}
 (\widehat{\mathbb Z}\setminus p\widehat{\mathbb Z}).
\]

Chinese remaindering gives the measure of each finite intersection as
the product of 1-1/p. Continuity of probability for decreasing sets
therefore gives

\[
 \mu(E_{S,m})=\prod_{\substack{p\in S\\p\nmid m}}(1-p^{-1})=0,
\]

since removing the finitely many divisors of m preserves reciprocal-sum
divergence. Thus T*e_m=0 for every m, so T*=0 and T=0. QED.

FWD02 follows. This argument does not assume the additional forward
equation for T*; it uses only the adjoint of the stated equation for T.

## 5. Convergence gives a unitary intertwiner

Suppose now that sum over p in S of 1/p is finite, and put

\[
 E_S=\bigcap_{p\in S}(\widehat{\mathbb Z}\setminus p\widehat{\mathbb Z}),
 \qquad \alpha=\mu(E_S)=\prod_{p\in S}(1-p^{-1})>0.
\]

Define W_d as the closed span of e_m for m in R_S, and W_c=L²(E_S,mu),
regarded as a subspace of H_c by extension by zero. Distinct sets kE_S,
k in M_S, are disjoint: their selected prime valuations distinguish
them. Their measures are alpha/k. The convergent Euler product gives
alpha times sum over M_S of 1/k equal to 1. They therefore cover a set
of full Haar measure, and

\[
 H_d=\bigoplus_{k\in M_S}V_k W_d,\qquad
 H_c=\bigoplus_{k\in M_S}U_k W_c. \tag{7}
\]

Both wandering spaces have countably infinite Hilbert dimension. The
complement of S contains infinitely many primes because the full
reciprocal-prime sum diverges; hence R_S is infinite. Haar measure is
nonatomic, its restriction to E_S has positive measure, and the
profinite space is metrizable with a countable cylinder base, so W_c is
separable and infinite-dimensional.

Choose any unitary B:W_d to W_c. Define on the orthogonal sums

\[
 A(V_k w)=U_k B w. \tag{8}
\]

This extends to a unitary A:H_d to H_c. Since multiplication by p shifts
the shell index k to pk, AV_p=U_pA for every p in S. Its inverse
intertwines in the opposite direction. It also intertwines adjoints,
although no adjoint assumption was needed in Sections 3–4. Equations
(7)–(8) include S empty, where the intertwining conditions are vacuous.
Together these arguments prove FWD03.

This is an existence construction, not a classification of every
forward-only intertwiner. In particular the classification of all
adjoint-preserving intertwiners in the earlier paper must not silently
be extended to all forward-only intertwiners.

## 6. COST03: finite GCD Grams and exact spectral bounds

Define T_N:C^N to H_c by T_N e_n=U_n 1, for 1≤n≤N. Since the intersection
of the m- and n-divisibility cylinders has measure 1/lcm(m,n),

\[
 K_N(m,n)=\langle U_m1,U_n1\rangle
 =\frac{\sqrt{mn}}{\operatorname{lcm}(m,n)}
 =\frac{\gcd(m,n)}{\sqrt{mn}},\qquad
 \|T_N\|^2=\lambda_{\max}(K_N). \tag{9}
\]

**Strict positivity and determinant.** Let B_N(m,n)=gcd(m,n), let D be
diag(1,...,N), and let E(m,d)=1 if d divides m and 0 otherwise. The
divisor identity sum_{d|k} phi(d)=k gives

\[
 B_N=E\operatorname{diag}(\varphi(1),\ldots,\varphi(N))E^t,
 \quad K_N=D^{-1/2}B_ND^{-1/2},\quad
 \det K_N=\prod_{n=1}^N\frac{\varphi(n)}n>0. \tag{10}
\]

Here E is lower triangular with diagonal 1, proving the factorization
is strictly positive. This is the classical Smith determinant mechanism,
not a new positivity theorem.

**Harmonic and divisor lower bounds.** Since T_N*1 has coordinates
1/sqrt(n), we have ||T_N||²≥H_N, where H_N=sum_{n≤N}1/n. The Rayleigh
quotient at v_n=1/sqrt(n) improves this to

\[
 \lambda_{\max}(K_N)\ge R_N:=
 \frac{\displaystyle\sum_{d\le N}\frac{\varphi(d)}{d^2}
                         H_{\lfloor N/d\rfloor}^{\,2}}{H_N}
 \ge H_N. \tag{11}
\]

To derive the numerator, expand gcd(m,n) as
sum_{d|m,n} phi(d), write m=da,n=db, and sum 1/(ab). For the last
inequality, put g=T_N v. Then inner product of g and 1 is H_N and
||1||=1, so ||g||²≥H_N². Dividing by ||v||²=H_N proves it.

For completeness the **Rayleigh test value**, not necessarily the
largest eigenvalue, satisfies

\[
 R_N=\frac{1}{3\zeta(2)}(\log N)^2+O(\log N)
     =\frac{2}{\pi^2}(\log N)^2+O(\log N). \tag{12}
\]

Here is an elementary derivation rather than a numerical fit. Möbius
inversion gives

\[
 A(x):=\sum_{d\le x}\frac{\varphi(d)}{d^2}
 =\sum_{k\le x}\frac{\mu(k)}{k^2}H_{\lfloor x/k\rfloor}
 =\zeta(2)^{-1}\log x+O(1).
\]

The last equality follows from H_floor(x/k)=log(x/k)+O(1), absolute
convergence of sum (log k)/k², and the tail estimate
log x times sum_{k>x}1/k²=O(log x/x). Partial summation now gives

\[
 \sum_{d\le N}\frac{\varphi(d)}{d^2}(\log(N/d))^2
 =2\int_1^N A(t)\frac{\log(N/t)}t\,dt
 =\frac{(\log N)^3}{3\zeta(2)}+O((\log N)^2).
\]

Replacing log(N/d) by H_floor(N/d) changes the sum by O(log² N): the
pointwise square difference is O(1+log(N/d)), and another partial
summation bounds its weighted sum. Division by H_N=log N+O(1) proves
(12). In particular ||T_N|| is at least (sqrt(2)/pi+o(1))log N. No
matching upper asymptotic is asserted.

**Squarefree tensor refinement.** Let F be a finite prime set with
P=product of p in F at most N. On the principal submatrix indexed by
the squarefree divisors of P, prime valuations factor (9) as

\[
 \bigotimes_{p\in F}
 \begin{pmatrix}1&p^{-1/2}\\p^{-1/2}&1\end{pmatrix}.
\]

Its eigenvalues are precisely product over p in F of (1±p^(-1/2)), with
independent signs. The largest gives another exact lower bound

\[
 \lambda_{\max}(K_N)\ge\prod_{p\in F}(1+p^{-1/2}). \tag{13}
\]

The least tensor eigenvalue is the corresponding all-minus product,
giving an upper bound for the least eigenvalue of the full K_N by the
Rayleigh principle. These bounds expose conditioning and can improve
on (11); (12) is only the behavior of one test vector. The finite
tensor construction is a classical multiplicative-matrix mechanism.

**Rational upper certificates.** Set L(i,j)=gcd(i,j)/j. This is similar
to K_N by L=D^(1/2) K_N D^(-1/2). For every vector x with strictly
positive rational coordinates, v_i=x_i/sqrt(i) yields the exact bounds

\[
 \frac{\sum_i x_i(Lx)_i/i}{\sum_i x_i^2/i}
 \le\lambda_{\max}(K_N)
 \le\max_i\frac{(Lx)_i}{x_i}. \tag{14}
\]

The lower bound is Rayleigh's principle. To prove the upper bound U,
use 2|z_i z_j|≤|z_i|²v_j/v_i+|z_j|²v_i/v_j in the symmetric,
entrywise nonnegative quadratic form of K_N. Summing bounds it by
sum_i |z_i|²(K_N v)_i/v_i≤U||z||². At x=1 this gives

\[
 \lambda_{\max}(K_N)
 \le\max_{m\le N}\sum_{d\mid m}\frac{\varphi(d)}d H_{\lfloor N/d\rfloor}
 \le N. \tag{15}
\]

The last inequality follows also from gcd(m,j)/j≤1. Iterating x maps
to Lx and rescaling keeps all quantities rational. Any finite number
of iterations already certifies (14); convergence of the iteration is
not needed. Taking the best lower and upper values seen is valid.

Equations (9)–(15) prove COST03. As H_N diverges, the compatible maps
T_N cannot be restrictions of a bounded synthesis map on ell²(N+).
This canonical g=1 obstruction is weaker in scope than Theorem 3.1,
which rules out every bounded forward intertwiner for divergent S.

## 7. Primary prior art and novelty boundaries

The primary sources below were consulted on 2026-10-18. A primary
publisher record is distinguished from a full paper; none is counted
as a separate empirical validation of this implementation.

* Henry J. Stephen Smith, *On the Value of a Certain Arithmetical
  Determinant*, Proc. London Math. Soc. s1-7 (1875), starting p.208:
  [original publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s1-7.1.208).
  The record was consulted; a full transcription of the original was
  not audited. Equation (10) is independently derived here. Attribution
  of the GCD determinant to Smith is classical, not a novelty claim.
* Andriy Bondarenko and Kristian Seip, *GCD sums and complete sets of
  square-free numbers*, [primary author manuscript, arXiv:1402.0249](https://arxiv.org/pdf/1402.0249),
  especially Sections 2–3 and Section 7, equations (18)–(19). Their
  spectral quantity takes the supremum over all N distinct integer
  indices and all coefficient vectors. At exponent 1/2 their bound is
  O(exp(A sqrt(log N log_3 N / log_2 N))) for an absolute A<7 and
  sufficiently large N. It therefore upper-bounds our first-N matrix,
  but is not stated here as a sharp first-N asymptotic. Their
  prime-multi-index formulation also places the tensor calculation
  above squarely in established GCD-matrix theory. This 2014 result
  is a verified comparison, not a claim about the latest optimal
  bound in the literature.
* Christoph Aistleitner, István Berkes, Kristian Seip and Michel Weber,
  *Convergence of series of dilated functions and spectral norms of
  GCD matrices*, [primary author manuscript, arXiv:1407.5403](https://arxiv.org/pdf/1407.5403),
  Section 3. Their distinction between first-N integer matrices and
  arbitrary integer selections matters here. Results quoted there for
  1/2<alpha<1 cannot be extended to our critical alpha=1/2 by simply
  substituting the endpoint. Dilated-function theory is adjacent;
  its source space and its dilation convention must be transported
  explicitly before it can replace the present proof.
* Titus Hilberdink, *“Quasi”-norm of an arithmetical convolution operator
  and the order of the Riemann zeta function*,
  [primary author PDF](https://www.reading.ac.uk/maths-and-stats/-/media/project/uor-main/schools-departments/maths/maths-and-stats---staff-profiles/documents/twh_m2normpaper.pdf?hash=BAEB4C8A0DD16D150128301A7AAA3BDE&la=en),
  Appendix, Proposition A1. Divergence of sum over primes of |f(p)|²
  forces the Dirichlet-convolution output of every nonzero ell² input
  outside ell². The case f(p)=p^(-1/2) is a closely related classical
  reciprocal-prime obstruction. This operator is not identified with
  an arbitrary profinite-Haar intertwiner here, so the result is
  relevant prior art, not a claimed direct citation for FWD03.
* Hui Dan and Kunyu Guo, *Dilation theory and analytic model theory for
  doubly commuting sequences of C_.0-contractions*,
  [primary manuscript, arXiv:1907.05815](https://arxiv.org/abs/1907.05815).
  Countable doubly commuting dilation/model theory supplies the
  surrounding established framework; failure of naive countable
  wandering-space intuition is not a new phenomenon claimed here.

**Verdict on contribution.** FWD03 is a new-to-project strengthening
from adjoint-preserving transport to forward-only bounded transport,
with an explicit proof for arbitrary prime subsets and all atomic
components. The exact residue mass inequality (3) makes its analytic
input transparent and independently testable. No literature search
performed here establishes academic priority for this exact theorem.
COST03 is a project application of classical normalized GCD matrices,
with exact rational certificate code. Equations (11)–(15) are not
presented as record spectral estimates or new GCD theorems.

## 8. Executed controls and kernel boundary

Implementation: `observational_succ/round2_operators.py`.
Tests: `tests/test_round2_operators.py`.
Bounded runner: `scripts/round2_operators_probe.py`.
Exact receipt: [round2/operators_exact_receipt.json](round2/operators_exact_receipt.json).

The run uses only exact integer/Fraction calculations for decisions.
Spectral matrices are capped at N=64 and eight refinement iterations;
the saved run uses four. Residue moduli are capped at 64 and integer
prefixes at 20,000; the saved run uses prefix 500. The printed decimal
numbers are display values, never the proof objects.

| N | Certified lower for ||T_N||², shown rounded down | Certified upper, shown rounded up |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 1.7071067 | 1.7073171 |
| 4 | 2.6180323 | 2.6201889 |
| 8 | 3.7613963 | 3.7674106 |
| 16 | 5.2754345 | 5.2859508 |
| 32 | 7.0855745 | 7.1015005 |
| 64 | 9.2963384 | 9.3273208 |

Twelve focused tests passed. They compare factor-removal monoid
enumeration with independent product closure; transfer every generated
residue class with exact overlap counts; test the Fourier change of
variables in a rational group algebra; count Haar-cylinder overlaps
directly; check the totient factorization and Smith determinant by
Gaussian elimination; and check upper certificates by an independent
exact positive-semidefinite elimination. Negative controls include
composite generators, wrong Fourier phase, missing S-free components,
a false spectral upper bound, singular matrices, and resource caps.
Finite prime sets always have convergent reciprocal sums; these
experiments cannot by themselves test the infinite divergence premise.

The Lean source [ResidueTransfer.lean](../../formal/round2/ResidueTransfer.lean)
contains exactly three audited declarations:

| Declaration | Kernel statement | Axioms |
|---|---|---|
| `residue_transfer` | If n and r agree modulo q and tr agrees with 1 modulo q, then tn agrees with 1 modulo q. | `propext` |
| `transfer_injective` | Multiplication by positive t is injective on Nat. | none |
| `controlled_monoid_transfer` | For a multiplication-closed predicate M, inverse residue transfer preserves M and sends n≤N, t≤C to tn≤CN. | `propext` |

The pinned verifier `scripts/verify_round2_operators_lean.py` checked
Lean 4.14.0, the exact manifest declaration set, allowed axioms,
forbidden proof tokens, and rejection of a proposed proof of False.
It used a 1 GiB address-space cap and 60 CPU-second cap. See
[operators_lean_receipt.json](round2/operators_lean_receipt.json) and
[operators_axioms.json](round2/operators_axioms.json).
The residue inverse is an **explicit hypothesis** of the kernel
lemma. Its existence in a finite image, harmonic mass summation,
Euler products, Fourier totality and the Hilbert-space theorems were
not formalized. The Lean result does not upgrade FWD01–03 to kernel
proofs.

Reproduction from the repository root:

```sh
python -m unittest discover -s tests -p test_round2_operators.py
python scripts/round2_operators_probe.py --output research/2026-10-18/round2/operators_exact_receipt.json
python scripts/verify_round2_operators_lean.py --output research/2026-10-18/round2/operators_lean_receipt.json
```

**Next falsification opportunities.** Audit (5) under a changed Haar
normalization; remove boundedness and seek algebraic intertwiners;
replace additive Haar by an atomic or singular measure; test whether
an alleged converse classifies all forward maps rather than merely
constructing one. Each changes a genuine hypothesis. For COST03,
independently check saved rational brackets and compare sharper
published first-N estimates at the actual endpoint alpha=1/2.
No proof or finite receipt here transports a covariance into a
source-authenticated arithmetic positivity theorem.
