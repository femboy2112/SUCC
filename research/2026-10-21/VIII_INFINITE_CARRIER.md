# Countable weighted modes: finite shells, Gibbs cylinders, and trace thresholds

Date: 2026-10-21. Status: **PROVED** by the paper arguments below, with
the explicitly identified classical product-measure existence theorem.
Finite computations: **TESTED EXACT**. Formal status: **NOT FORMALIZED**.
Prior art: classical countable product probability, partition functions,
and diagonal self-adjoint operators; new-to-project synthesis only.

This dossier extends the local-finiteness statement in PR #214, head
`9372c669892a2a29fb8c16f0fa20c11815f650df`. That statement explicitly
limits its infinite product to a coefficientwise formal identity. It does
not incorrectly claim the analytic conclusions proved conditionally here.

## 1. The actual carrier and its compatible finite pieces

Fix a sequence of positive **integer** costs (w_j)_{j>=1}. Modes are labeled:
equal costs do not identify different modes. Define

\[
 \Omega=\bigoplus_{j\ge1}\mathbb N_0
 =\{n=(n_j):n_j=0\text{ for all but finitely many }j\},\qquad
 E(n)=\sum_jw_jn_j.
\]

This is a specified countable set with finite sums, not a symbolic
infinite-dimensional simplex. Its finite-mode subsets Omega_J consist of
states supported in {1,...,J}, embedded by zero padding. They are nested
and their union is Omega. Its finite-energy subsets are
Omega_{<=X}={n in Omega:E(n)<=X}, for real X>=0.

**Finite-shell theorem.** Every Omega_{<=X} is finite if and only if
w_j->infinity, meaning that for each M only finitely many indices have
w_j<=M. No monotonicity of the sequence is assumed.

**Proof.** If costs escape, only finitely many modes are affordable at X,
and their occupations are bounded by floor(X/w_j). Conversely, infinitely
many modes of cost <=M give infinitely many different singleton states at
budget M. This proves both directions. For w_j=1 local finiteness fails
already at budget one. Requiring *every* occupation to be positive is a
different construction with no finite-energy states; it does not repair
this carrier.

The positive integer hypothesis makes the formal coefficient of z^e in
product_j(1-z^{w_j})^{-1} finite under escape. For each e only the finite
set of affordable modes contributes. This is a coefficientwise statement;
analytic evaluation at a real q requires the next theorem.

## 2. The analytic criterion and an honest Hilbert-space realization

Fix beta>0, put q=exp(-beta) in (0,1), and q_j=q^{w_j}. The extended
nonnegative partition sum is

\[
 Z(q)=\sum_{n\in\Omega}q^{E(n)}\in[1,\infty].
\]

**Partition/trace theorem.** For every such weight sequence,

\[
 Z(q)=\lim_{J\to\infty}\prod_{j=1}^J(1-q_j)^{-1},\qquad
 Z(q)<\infty\iff\sum_{j\ge1}q_j<\infty. \tag{1}
\]

The operator H on the explicitly chosen Hilbert space ell^2(Omega) is

\[
 (Hf)(n)=E(n)f(n),\qquad
 D(H)=\{f:\sum_nE(n)^2|f(n)|^2<\infty\}.
\]

It is densely defined, nonnegative and self-adjoint. Its finite-support
linear span is a core. It has compact resolvent exactly when w_j->infinity.
The positive bounded diagonal operator exp(-beta H) is trace class if and
only if (1) is finite, and its trace is Z(q). On this Hilbert space this is
also the bounded-operator nuclearity criterion. No assertion about
nuclearity of an unspecified locally convex space is intended.

**Proof of (1).** Sum over Omega_J first. The J finite geometric series
factor, so its sum is Z_J=product_{j<=J}(1-q_j)^{-1}. Since Omega_J
increases to Omega, the nonnegative series increases to the entire sum.
For 0<=x<=q<1, integration of 1/(1-u) gives

\[
 x\le-\log(1-x)\le x/(1-q).
\]

Thus log Z_J is bounded in J exactly when the partial sums of q_j are
bounded. This proves (1), including divergence, without interchanging
conditionally convergent expressions. The criterion implies escape, but
escape alone does not imply the criterion.

**Operator proof.** Symmetry and nonnegativity are coordinatewise. The
domain contains the finite linear span of basis vectors and is dense.
For any g in ell^2, set f(n)=g(n)/(E(n)+i) (or with -i). Then
sum E(n)^2|f(n)|^2<=||g||^2 and (H+i)f=g; the two ranges are all ell^2,
giving self-adjointness. Alternatively the coordinatewise adjoint has
exactly the displayed maximal domain. Truncating any enumeration of Omega
approximates both f and Hf in norm, proving the core assertion.

If all energy shells are finite, the diagonal (H+1)^{-1} is approximated
in operator norm by its finite-energy restrictions: the omitted diagonal
entries are at most 1/(X+1). If a shell is infinite, its orthonormal basis
vectors have resolvent images with lengths bounded below by 1/(X+1);
these have no norm-convergent subsequence. Thus compact resolvent is
equivalent to the finite-shell criterion. Finally a positive diagonal
operator is trace class exactly when the sum of its diagonal entries is
finite. Here those entries are precisely q^{E(n)}, giving (1).

This H is a declared occupation-energy operator. It is **not** an original
signed Weil form, and its positivity cannot establish arithmetic-source
positivity or RH.

## 3. Projectively consistent probability, and where its mass lives

For finite J define a probability on N_0^J by

\[
 \mu_J(n_1,\ldots,n_J)
 =\prod_{j=1}^J(1-q_j)q_j^{n_j}. \tag{2}
\]

Summing the final occupation from zero to infinity gives one, so these
probabilities are projectively consistent. The countable product-measure
theorem yields a unique probability mu on N_0^N with these cylinders.
Its hypotheses hold: each coordinate is a countable discrete measurable
space, each geometric law is a probability, and the marginals agree.
One may apply the real-coordinate version to measures supported on N_0;
the countable intersection of the coordinate support events has full mass.

**Support theorem.** This product probability is carried by Omega if and
only if sum_j q_j<infinity. In the convergent case it is exactly

\[
 \mu(\{n\})=Z(q)^{-1}q^{E(n)}\quad(n\in\Omega). \tag{3}
\]

In the divergent case mu(Omega)=0, and no normalized probability of the
form (3) exists on Omega.

**Proof.** The probability all coordinates after J vanish is
a_J=product_{j>J}(1-q_j), obtained by continuity from finite intersections.
If the sum converges, the elementary finite union bound and passage to
the limit give 1-a_J<=sum_{j>J}q_j->0. Hence the increasing union of the
events {all coordinates after J vanish}, which is Omega, has measure one.
If the sum diverges, each a_J=0, since the finite products are at most
exp(-sum q_j) and tend to zero. The same countable union then has measure
zero. In the convergent case the probability of any singleton n follows
by finite cylinder continuity and is the full product in (3); its
normalizing product is exactly (1). This supplies the special-case support
proof directly, without silently invoking a finite-to-infinite counting rule.

## 4. Quantitative convergence with the topology and observables stated

Let lambda_J be mu_J zero-padded to N_0^N. Put
S_J=sum_{j>J}q_j. Under (1), and with total variation defined as
sup_A |mu(A)-lambda_J(A)|,

\[
 \|\mu-\lambda_J\|_{\rm TV}
 =1-\prod_{j>J}(1-q_j)\le\min(1,S_J). \tag{4}
\]

**Proof.** On Omega_J, mu=a_J lambda_J; off Omega_J, lambda_J is zero
and mu has mass 1-a_J. This decomposition proves the exact equality and
the event Omega_J attains it. The inequality is the union bound.
Consequently every bounded real observable F obeys

\[
 |\mathbb E_\mu F-\mathbb E_{\lambda_J}F|
 \le(\sup F-\inf F)\min(1,S_J). \tag{5}
\]

By contrast, when sum q_j diverges, mu(Omega)=0 while lambda_J(Omega)=1,
so the total variation distance is **one for every J**. Nonetheless the
finite cylinders are eventually exact. In the product topology even weak
convergence holds: couple by drawing n from mu and zeroing coordinates
after J; these truncations converge coordinatewise to n. Bounded continuous
functions then converge by dominated convergence. Thus projective/weak
convergence does not imply convergence on the finite-support carrier or
in total variation.

When S_J<1, (4) also supplies a **rational partition enclosure** whenever
q and the known tail bound are rational:

\[
 Z_J\le Z(q)\le Z_J/(1-S_J). \tag{6}
\]

Indeed Z_J/Z(q)=a_J lies between 1-S_J and one. The hypothesis S_J<1
belongs to this particular enclosure; failure of this coarse tail test
does not refute convergence of Z.

For unbounded observables (5) is insufficient. The expected energy is
exactly, as an extended nonnegative sum,

\[
 \mathbb E_\mu E=\sum_j\frac{w_jq_j}{1-q_j}, \tag{7}
\]

by the geometric expectation and nonnegative summation. Thus finite mean
energy is equivalent to sum_j w_j q_j<infinity, a stronger condition than
(1). The omitted expected energy is the tail of (7). A finite partition
alone does not justify differentiation under an infinite partition product.

## 5. Calibration w_j=j, with explicit rational bounds

For w_j=j the finite shell coefficients are the ordinary partition numbers
p(e), independently of any analytic substitution. At every q in (0,1),

\[
 Z(q)=\prod_{j\ge1}(1-q^j)^{-1}=\sum_{e\ge0}p(e)q^e<\infty,
 \qquad S_J=\frac{q^{J+1}}{1-q}. \tag{8}
\]

The equality is licensed by nonnegative sums and (1). Equations (4)–(6)
give explicit exponentially decaying mode-truncation and trace enclosures.
For the energy tail use 1-q^j>=1-q^{J+1} when j>J and differentiate the
*finite-variable convergent geometric series*, obtaining

\[
 \mathbb E\sum_{j>J}j n_j
 \le\frac{q^{J+1}((J+1)-Jq)}{(1-q)^2(1-q^{J+1})}. \tag{9}
\]

There is also a distinct **energy-budget** approximation. For 0<q<r<1
and integer B>=0, since E is integer,

\[
 \mu_q(E>B)
 =Z(q)^{-1}\sum_{E(n)>B}(q/r)^{E(n)}r^{E(n)}
 \le(q/r)^{B+1}\frac{Z(r)}{Z(q)}. \tag{10}
\]

The API uses (6) at r for an upper bound on Z(r), and any finite partial
partition at q for a lower bound on Z(q), yielding an exact rational
bound capped at one. The mode cutoff J in that calculation is a parameter
used to enclose Z; it is not the budget B. This gives an effective
finite-energy-carrier approximation under a verified tail hypothesis.

For example p(0),...,p(10)=(1,1,2,3,5,7,11,15,22,30,42), and the
number of states at budget five is 19. The code verifies these counts by
dynamic programming, checks them against an independent divisor-sum
recurrence, and compares finite rational partitions with rigorous bounds.

## 6. Decisive counterexample: escape is not heat-trace control

Take w_j=bit_length(j) for j>=1. The block of energy k has exactly
2^{k-1} different modes, so w_j->infinity. Every energy shell is finite,
and H has compact resolvent. But

\[
 \sum_jq^{w_j}=\sum_{k\ge1}2^{k-1}q^k
 \begin{cases}
 =q/(1-2q)&0<q<1/2,\\
 =\infty&q\ge1/2.
 \end{cases} \tag{11}
\]

Therefore Z(q) is finite **exactly** for beta>log 2. At beta=log 2,
the first K complete energy blocks contribute K/2 to this sum. The
vacuum and one-particle states alone give Z>=1+K/2 for every K. This
exact rational lower bound proves divergence without numerical eigenvalues
or an approximate critical exponent. Consistent cylinders still exist,
but almost every product state has infinitely many occupied modes and
infinite energy. Finite-mode zero padding stays TV distance one away.

For q<1/2, a complete-block cutoff K has 2^K-1 modes and exact one-mode
tail

\[
 S_K^{\rm block}=\frac{q(2q)^K}{1-2q}. \tag{12}
\]

This gives certified partition and TV bounds by (4),(6). The finite
partition is product_{k<=K}(1-q^k)^{-2^{k-1}}. For budget B, only blocks
k<=B are affordable. The coefficient of z^{kn} in (1-z^k)^{-b} is
binom(b+n-1,n): it counts weak compositions of n among b labeled modes.
Convolving these finite coefficient lists computes full shell counts
without explicitly allocating the exponentially many affordable modes.

**A second boundary: trace class need not imply finite mean energy.**
Take m_k=floor(2^k/k^2) modes of cost k, omitting empty blocks, and
q=1/2. The spectrum still escapes and
sum_k m_k 2^{-k}<=sum k^{-2}<infinity, so Z is finite. However

\[
 \sum_k k m_k2^{-k}
 \ge\sum_k(1/k-k2^{-k})=\infty.
\]

Thus (7) diverges. This counterexample rules out using mere trace
convergence as an unbounded-observable or derivative-interchange license.

## 7. Implementation, reproducibility, and authority boundary

Files: `observational_succ/viii_infinite_carrier.py` and
`tests/test_viii_infinite_carrier.py`. The numeric interfaces use exact
Fraction q, rejecting bool, float, out-of-range q, noninteger costs and
noninteger cutoffs. Generic finite-list functions make finite assertions
only. Infinite-tail functions refer only to the completely specified linear
or dyadic spectra, with their proved closed tail formulas. There is no
caller-supplied `tail_certificate=True`, theorem-status string, or checker
callback that can replace the required infinite hypothesis.

Tests compare occupation enumeration with coefficient dynamic programming,
individual dyadic modes with multiplicity-block calculations, partition
numbers with the independent Euler divisor recurrence, and exact finite
probabilities with rational tail enclosures. Projective consistency is
tested with a finite geometric sum **plus its exact remaining tail**;
no finite partial sum is mislabeled a normalized infinite law. The dyadic
critical example is a permanent negative control for convergence APIs.

These computations corroborate formulas on finite inputs. The analytic
theorems are supported by the complete proofs and the cited product-measure
existence theorem, not by a finite census. No Lean proof is claimed, and
same-model internal agreement is not independent external refereeing.

Next decisive probe: formally verify the finite-cylinder marginal identity
and the elementary partition tail bound, then instantiate a genuinely
source-derived interacting carrier. A local positivity or finite-shell
assertion cannot replace a summable tail when interactions are introduced.

## 8. Primary and authoritative source map

Consulted 2026-10-21; no external PDF was copied into the repository.

- Rick Durrett, *Probability: Theory and Examples*, version January 11,
  2019, [author-hosted manuscript](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
  Appendix A.3, Theorem A.3.1 (printed p.464; PDF p.472): compatible
  real-coordinate finite-dimensional laws have a unique countable product
  extension. This is the identified external existence dependency in
  Section 3. Its countable discrete specialization satisfies every hypothesis.
  The support dichotomy is proved directly above; it also agrees with
  the Borel–Cantelli results in Section 2.3 of the same manuscript.
- NIST DLMF [27.14.2–3](https://dlmf.nist.gov/27.14): the standard Euler
  partition product and generating function, with the analytic domain
  |q|<1 explicitly stated. This is a normalization/prior-art check;
  Sections 1,2,5 independently justify the real positive specialization.
- PR #214, exact head recorded at the start: the existing finite-shell
  equivalence and formal coefficient identity are retained as valid.

No academic originality is claimed for these classical mechanisms. The
project gains a precise criterion, quantitative enclosures, and falsifying
examples that separate four previously adjacent notions: local finiteness,
projective consistency, finite-support Gibbs probability, and trace class.
