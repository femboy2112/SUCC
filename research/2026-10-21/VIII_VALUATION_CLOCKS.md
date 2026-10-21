# Finite valuation compatibility, sum phases, and quantitative CRT transport

Date: 2026-10-21. Status: **PROVED** by the complete paper proofs below;
finite implementations **TESTED EXACT**; not formally kernel checked.
Prior art: classical finite Fourier analysis, valuation arithmetic, CRT, and
elementary sieve tails. This is a new-to-project synthesis, not a novelty claim.
No implication for integer abc, RH, or Goldbach is asserted.

## 1. Audit of the incoming claim and the precise extension

Reviewed PR #214 head `9372c669892a2a29fb8c16f0fa20c11815f650df`, in
`research/2026-10-20/DUAL_SLOPE_EXTERIOR_ASCENT.md`, Sections E–I, and
`observational_succ/exterior_cofactor_ascent.py`. Its local pairwise factor
concerns summands only. Its text explicitly excludes the total coordinate.
That qualification is correct and load-bearing. Its weighted infinite carrier
asserts local finiteness, not convergence of an analytic partition function.
Neither scoped claim is refuted here.

The finite construction here consists of actual residues at genuine primes,
with an exact linear sum map. A compatibility cell is a subset of a finite
residue space, not a metaphorical hypergraph. The new calculation determines
the cardinality of every truncated valuation cell of that map, including the
canceling leading-unit phases. It also gives the pairwise factor when the
total coordinate really is included.

## 2. Exact finite theorem, with two derivations of the phase count

Let p be prime, k>=1, m>=1, and define
nu_k(x)=min(v_p(x),k) on Z/p^k Z, where nu_k(0)=k. A depth k therefore
means **at least k**, not exact valuation k. Fix e=(e_1,...,e_m) in
{0,...,k}^m and take the x_i independently and uniformly in nu_k(x_i)=e_i.
The size of that product cell is

\[
 A(e)=\prod_i a(e_i),\qquad
 a(j)=(p-1)p^{k-j-1}\ (j<k),\quad a(k)=1.
\]

For r>=0 let U_r(t) be the number of r unit residues modulo p with sum t.
Then, with the empty sum allowed,

\[
 U_r(0)=\frac{(p-1)^r+(p-1)(-1)^r}{p},\qquad
 U_r(t)=\frac{(p-1)^r-(-1)^r}{p}\quad(t\ne0).
 \tag{1}
\]

**Character proof.** Put zeta=exp(2 pi i/p). The geometric sum gives
p^{-1} sum_{a mod p} zeta^{a(s-t)}=1_{s=t}. Summing over all r-tuples of
units gives

\[
 U_r(t)=p^{-1}\sum_{a\bmod p}\zeta^{-at}
      \left(\sum_{u\ne0}\zeta^{au}\right)^r.
\]

The inner sum is p-1 at a=0 and -1 otherwise. The remaining nonzero-a sum
is p-1 if t=0 and -1 otherwise, proving (1). This is finite orthogonality;
no infinite Fourier limit or approximate root of unity enters the code.

**Independent recurrence proof.** Multiplication by any nonzero scalar
identifies every nonzero-target fiber, so let A_r=U_r(0), B_r=U_r(1).
Appending a nonzero final coordinate gives
A_{r+1}=(p-1)B_r and
B_{r+1}=A_r+(p-2)B_r. Initial values are A_0=1,B_0=0.
Substitution verifies that (1) satisfies this recurrence and initial values.
This route uses no characters.

**Full valuation law.** If all e_i=k then nu_k(sum x_i)=k with probability
one. Otherwise put h=min e_i<k, r=#{i:e_i=h}, and
rho=U_r(0)/(p-1)^r. For j in {0,...,k}, the exact probabilities are

\[
 \pi_e(j)=
 \begin{cases}
 0&j<h,\\
 1-\rho&j=h,\\
 \rho(p-1)p^{-(j-h)}&h<j<k,\\
 \rho p^{-(k-h-1)}&j=k.
 \end{cases} \tag{2}
\]

Consequently the number of vectors with the given summand depths and total
depth j is exactly A(e) pi_e(j). In particular this displayed rational number
is an integer, including every zero cell.

**Proof.** Divide the sum by p^h and reduce modulo p. Exactly the r coordinates
of minimal depth contribute nonzero leading digits; these digits are uniform
independent units. The others contribute zero. Equation (1) gives the
cancellation probability rho. To justify all higher depths, condition on
every leading digit and on all coordinates except one of minimal depth.
Its remaining k-h-1 digits are unrestricted and uniform: that summand can be
written p^h(u+p y), with y uniform modulo p^{k-h-1}. Once the leading sum is
zero, division of the total by p^{h+1} is a translate of this uniform y.
The successive exact-zero/nonzero digit counts give (2). When k=h+1 the
remaining group is trivial and the last line is simply rho. This treats the
boundary case without a nonexistent free digit.

Prescribing the leading units themselves makes the first cancellation
deterministic: their sum must be zero modulo p; after that, the same uniform
higher-digit argument applies. Thus depth alone is not the entire local
constraint: the leading phase sum is the missing datum.

For an exact target residue c mod p^k, the fiber size is

\[
 \#\{x:\nu_k(x_i)=e_i,\ \sum x_i=c\}
 =\frac{A(e)\pi_e(\nu_k(c))}{a(\nu_k(c))}. \tag{3}
\]

Indeed common multiplication by a unit preserves the summand classes and
acts transitively on target residues of any given depth. This proves (3)
independently of floating-point Fourier evaluation.

**Hostile cases.** A unique minimal depth has rho=0, so no cancellation is
possible. At p=2, r odd has rho=0 while r even has rho=1. For two odd
summands mod 16 the total-depth probabilities are (0,1/2,1/4,1/8,1/8),
not the unconditional geometric law. For three odd summands the total is
always odd. Replacing the genuine prime by a composite invalidates the
field-unit count; the implementation rejects composite, bool, float, and
rational prime arguments.

## 3. Joint primitivity versus pairwise coprimality, including the total

Let m>=2, x uniform in F_p^m, and c=sum x_i. Local joint primitivity of
(x_1,...,x_m,c) has probability

\[
 d_{m,p}^{\rm prim}=1-p^{-m}. \tag{4}
\]

Adding c does not change the gcd: all summands vanish if and only if all
selected coordinates vanish. Pairwise coprimality instead means that at
most one selected coordinate vanishes. For summands alone its probability is

\[
 d_{m,p}^{\rm pair,sum}
 =p^{-m}\big((p-1)^m+m(p-1)^{m-1}\big). \tag{5}
\]

Including c changes the answer to

\[
 d_{m,p}^{\rm pair,total}
 =p^{-m}\big((p-1)^m+
       m((p-1)^{m-1}-U_{m-1}(0))\big). \tag{6}
\]

**Proof.** If no summand is zero, any value of c is allowed: c can be the
sole zero. This contributes (p-1)^m. If one summand is zero, choose it in m
ways; the other m-1 summands are units, and c must now be nonzero. Remove
exactly U_{m-1}(0) choices. Two zero summands are forbidden. This proves (6).

For m=2 all three notions agree, because U_1(0)=0 and (5)=1-p^{-2}.
For m=3,p=2 they are respectively 7/8, 1/2, and **1/8**. This is an exact
counterexample to extending a summand-only factor to the augmented tuple.
It is not a counterexample to the explicitly scoped statement of PR #214.

## 4. Finite CRT composition and a moving-box theorem

Choose finitely many **distinct genuine primes** p, with precision k_p and
one local valuation cell R_p subset (Z/p^{k_p} Z)^m as above. Put
W=product p^{k_p}. Coordinatewise CRT is a bijection and commutes with the
sum, so the combined residue set R has exactly

\[
 |R|=\prod_p |R_p|,\qquad |R|/W^m=\prod_p |R_p|/p^{mk_p}. \tag{7}
\]

The assertion is finite: repeated-prime constraints cannot be multiplied
as though independent. Arbitrary disjoint unions of cells may be counted
by summing their exact cardinalities before applying CRT.

For **every** integer X>=0, and **any** residue set R modulo W, let N_R(X)
count positive x_i<=X with x mod W in R. Each coordinate residue occurs
floor(X/W) or ceil(X/W) times, whence

\[
 |R|\lfloor X/W\rfloor^m\le N_R(X)
 \le |R|\lceil X/W\rceil^m. \tag{8}
\]

The module returns these integer bounds, the main term |R|(X/W)^m, and
the maximum distance from that main term to the two bounds. The bounds
are exact when W divides X. For X>0 and R nonempty they imply

\[
 \left|\frac{N_R(X)}{|R|(X/W)^m}-1\right|
 \le (1+W/X)^m-1\le e^{mW/X}-1. \tag{9}
\]

For the lower side, (z+1)^m-z^m >= z^m-(max(0,z-1))^m follows from
monotonicity of increments of t^m on t>=0, so the same upper expression
controls both sides. Thus m=m(X), W=W(X), R=R(X) may all move, including
sparse R, under the declared sufficient regime **mW/X -> 0**. No fixed-m
constant is hidden. At W=X+1 the single zero residue has no positive box
point while its main term (X/(X+1))^m tends to one for fixed m. Therefore
arbitrary moving-modulus relative asymptotics are false.

This theorem concerns boxes. The separately reviewed simplex theorem in
PR #214 has its own dimension-dependent boundary estimate and the stronger
sufficient restriction m^2 W/X -> 0. The two regions and growth conditions
must not be interchanged.

## 5. A genuine infinite-prime tail, not finite-prime primitivity

Fix m>=2, integer X>=0 and integer P>=1. Test **all genuine primes <=P**
for the relevant local coprimality rule, optionally imposing additional
residue conditions. If an accepted box tuple is not globally primitive,
some prime q>P divides all summands. Since the summands are positive,
q<=X, and there are at most floor(X/q)^m such tuples. Thus

\[
 0\le N_{\le P}^{\rm prim}(X)-N^{\rm prim}(X)
 \le \frac{X^m}{(m-1)P^{m-1}}. \tag{10}
\]

Here sum_{q>P}q^{-m} <= sum_{n>P}n^{-m} <= integral_P^infinity u^{-m}du.
Additional restrictions only decrease the possible error.

For pairwise coprimality among summands, a bad pair i,j at q contributes
at most X^m/q^2. For a bad pair (x_i,c), first choose x_i a multiple of q,
choose m-2 other summands, and solve for the last summand modulo q. This
gives at most floor(X/q) ceil(X/q) X^{m-2} <= 2X^m/q^2, since q<=X.
The case m=2 uses X^0=1 and the same argument. Consequently

\[
 0\le N_{\le P}^{\rm pair}(X)-N^{\rm pair}(X)
 \le \left[\binom m2+2m\,1_{\text{total included}}\right]\frac{X^m}{P}.
 \tag{11}
\]

When P>=X both errors are exactly zero. These are absolute error bounds,
not relative errors in an arbitrarily sparse family. Relative use requires
the displayed error to be small compared with that family's main term.

Equations (7)–(11) prove the passage to global densities for fixed m. For
example, let d_p be (6), W_P=product_{p<=P}p and d_P=product_{p<=P}d_p.
The local failure probability is at most binom(m+1,2)/p^2: each pair of
the distinct linear coordinates x_i and c is a rank-two linear condition
(m>=2), and the union bound applies, even where events coincide. Every
d_p is positive. To see positivity even at small p, choose m-1 units and
choose the remaining unit freely if all units can sum arbitrarily; more
simply (6) includes the strictly positive (p-1)^m term. Therefore
the infinite product d_infinity is positive and

\[
 0\le d_P-d_\infty\le \binom{m+1}{2}/P. \tag{12}
\]

One proof of positivity uses -log(1-u)<=2u once u<=1/2 and handles the
finitely many initial factors separately. The tail difference follows from
1-product(1-u_p)<=sum u_p and the same integral estimate. Combining the
box estimate and tails gives, with C_m=binom(m,2)+2m,

\[
 \left|N^{\rm pair,total}(X)/X^m-d_\infty\right|
 \le (1+W_P/X)^m-1+
       \big(C_m+\binom{m+1}{2}\big)/P. \tag{13}
\]

For fixed m, choosing any P(X)->infinity with W_{P(X)}/X->0 proves the
global asymptotic. For a completely elementary available choice, take the
largest positive integer P with P^P<=sqrt(X); then W_P<=P^P<=sqrt(X)
and P->infinity. No prime number theorem is used. For moving m, (13)
remains valid; a sufficient **absolute normalized error** regime is
mW_P/X->0 and m^2/P->0. It does not promise relative error if d_infinity
also tends to zero. Joint primitivity follows analogously from (4),(10),
with Euler product product_p(1-p^{-m}); the Euler-product identification
with 1/zeta(m) is classical and is not needed for these bounds.

## 6. Implementation, independent checks, and limitations

Files: `observational_succ/viii_valuation_clocks.py` and
`tests/test_viii_valuation_clocks.py`. All output arithmetic is integer or
Fraction; exact inputs reject booleans/floats where not part of the domain.
The finite cell is frozen and copies nested depths to a tuple. Its type
contains no theorem-status field, checker callback, or authority registration.

The code computes the closed formulas. The tests independently enumerate
residue vectors and count valuations by divisibility by successive powers,
rather than duplicating the repeated-division implementation. They cover all
cells in several complete small spaces, exact sum residues, the p=2 phase
obstruction, CRT at coprime prime powers, sparse moving-modulus failure,
total-inclusive pairwise counts, and actual global gcd tail census.
These are independent finite mathematical mechanisms; they are **not**
independent-model or formal-kernel endorsements of the universal proof.

Next falsifier: enumerate cells with heterogeneous deep prime powers and
separately formalize the higher-digit translation bijection; audit whether a
consumer mistakenly treats depth k as exact valuation k or assumes the
infinite-prime tail is relative in a sparse family.

## 7. Sources and provenance

No source archive was modified, and no large paper was copied. The proofs
above are independently written elementary derivations.

- NIST DLMF, [27.10, equations 27.10.2–5](https://dlmf.nist.gov/27.10):
  standard finite Fourier inversion and Ramanujan sums. Consulted 2026-10-21
  as an official reference for terminology and normalizations. Our recurrence
  proof and direct character proof supply the complete special case used here.
- [PR #214](https://github.com/femboy2112/SUCC/pull/214), exact head stated in
  Section 1: source of the explicitly summand-only local factor being audited.
  That prior project statement is preserved; equation (6) is its additional
  total-inclusive calculation.

Formal verification: **NOT FORMALIZED**. Academic novelty: **UNVERIFIED**;
all mechanisms are classical and no priority claim is made.
