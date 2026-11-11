# Round III — irrational semantics, rational arithmetic

**Date:** 2026-11-10. **Scope:** ordinary classical mathematics and explicit
computable names. **Status:** CLASSICAL / PROVED LOCAL for the derivations;
TESTED MODEL (`VERIFIED_FINITE`) for the accompanying implementation checks.
This note does not promote an existing SUCC, normality, or RH claim.

The [Dedekind–Yoneda construction](DEDEKIND_YONEDA.md) recovers real order from
rational probes. The [computation graph](COMPUTATION_GRAPH.md) supplies certified
rational names for sqrt(2) and the authentic BBP source. Here we ask what actual
arithmetic can be transported through those representations. Three answers are
useful: rational witnesses implement cut arithmetic; quadratic fields become
rational linear algebra; rational expressions in pi become exact rational
functions in a formal variable.

## R1. Addition is a convolution of rational witness families

For a finite real x let C_x={q in Q:q<x}. Regard Q as the thin category with an
arrow p -> q exactly when p<=q. Its identities matter: strict < alone is not a
category. A lower set C is a presheaf with values in the two-element truth-value
poset. For lower sets define

$$
(C\boxplus D)(r)
 =\bigvee_{p,q\in\mathbb Q}
    \bigl(C(p)\wedge D(q)\wedge[r\le p+q]\bigr).
$$

In sets, this means r belongs iff there are rational witnesses p in C and q in D
with r<=p+q. This is the Boolean-enriched rational addition convolution. It is
the elementary truth-valued instance of Day's presheaf convolution; we prove
the instance used here rather than importing unspecified enrichment machinery.

**Theorem R1 (all finite x,y).** C_x boxplus C_y = C_(x+y).

If r<=p+q with p<x and q<y, then r<x+y. Conversely, if r<x+y, choose a positive
rational epsilon<(x+y-r)/2. Density gives p in (x-epsilon,x) and q in
(y-epsilon,y), so p+q>r. Both implications use the rational labels and addition
on the base. An unlabelled category of witnesses cannot supply this operation.

The operation is associative: either parenthesization asserts the existence of
p in C, q in D, s in E with r<=p+q+s. For example, given such a triple one can
take the intermediate witness p+q; conversely an intermediate witness <=p+q
can only make the resulting upper bound smaller. Associativity of rational
addition therefore gives the equality of lower sets. The ambient unit on all
lower sets is the *closed* principal lower set downarrow 0. On the subcategory
of rounded real cuts, the *open* cut C_0 also acts as a unit, by Theorem R1.
These two presheaves are different; the ambient unit must not be misidentified.

For x,y>0, multiplication is another rational witness operation:

$$
r\in C_{xy}
\iff \exists p,q\in\mathbb Q_{>0}:
 p<x,\ q<y,\ r\le pq.
$$

The forward implication follows by approaching x and y from below; the reverse
uses positivity. This formula is restricted to positive factors. Arbitrary
signed multiplication needs sign information or two-sided enclosures; the
same formula with the positivity restriction deleted is false.

**Computation boundary.** Existence of these presheaves is a semantic theorem
for all reals. An algorithm needs an effective presentation of the cuts or
located enclosures. Arbitrary real cuts are not automatically computable.

**Hostile control.** If one forgets the labels p,q, every irrational cut is a
countable dense linear order without endpoints and has the same bare order
type. Addition cannot be recovered from that common shape. The repair is the
projection of the category of elements to Q, with Q's arithmetic retained.

## R2. A quadratic irrational compiles to rational matrices

Let K=Q(sqrt(2)) with the positive real embedding selected by the cut
1<sqrt(2)<2. Define

$$
M(a,b)=\begin{pmatrix}a&2b\\b&a\end{pmatrix},\qquad a,b\in\mathbb Q.
$$

This is multiplication by a+b sqrt(2) in the basis (1,sqrt(2)). Direct matrix
multiplication gives

$$
M(a,b)M(c,d)=M(ac+2bd,ad+bc).
$$

The map is injective, preserves sums and 1, and sends sqrt(2) to
J=[[0,2],[1,0]], with J^2=2I. Inverting a nonzero element is rational arithmetic:

$$
(a+b\sqrt2)^{-1}=\frac{a-b\sqrt2}{a^2-2b^2}.
$$

The denominator cannot vanish for rational a,b unless both vanish, by
irrationality of sqrt(2). This is a field representation, not a finite-precision
approximation.

### The category equivalence, including all arrows

Define Quad_2(Q) as follows:

- An object is a finite-dimensional Q-vector space V equipped with a Q-linear
  operator J:V->V satisfying J^2=2 id_V.
- An arrow (V,J)->(W,H) is a Q-linear map F with FJ=HF.
- Identities and composition are those of Q-linear maps.

**Theorem R2.** FinVect_K is equivalent to Quad_2(Q).

Restriction of scalars takes a K-space to its underlying Q-space and lets J be
multiplication by sqrt(2). Conversely define scalar multiplication by

$$
(a+b\sqrt2)\cdot v=(aI+bJ)v.
$$

The relation J^2=2I verifies the field multiplication law above. A map is
K-linear precisely when it is Q-linear and commutes with J. These constructions
are inverse on the given structures, with the evident identity coherence maps.
Finite dimension on either side is equivalent: if dim_K V=n, then dim_Q V=2n;
in the other direction a finite Q-basis spans over K, and the field action
forces the same dimension identity. Thus no nonzero odd-dimensional Q-space
can occur as an object. This supplies a genuine equivalence carrying arbitrary
linear maps, not just a numerical encoding of objects.

In chosen bases a K-matrix (a_ij+b_ij sqrt(2)) becomes a rational block matrix
with blocks M(a_ij,b_ij). Matrix composition is preserved entry by entry. The
previous round's finite matrix/family machinery can therefore host this
quadratic extension once rational linear structure and J are included.

### Algebra does not select an order embedding

Replacing J by -J also satisfies the relation. The polynomial equation alone
does not select positive sqrt(2). The labelled Dedekind cut selects the real
embedding. Once selected, signs of a+b sqrt(2) are decided with rational
arithmetic: when a,b have opposite signs compare a^2 with 2b^2; when they have
the same sign, the answer is immediate. Equality occurs only when a=b=0.

The same construction works for K=Q[t]/(p), with p a monic irreducible rational
polynomial: finite K-spaces correspond to finite rational spaces equipped with
an operator annihilated by p. If p has real roots, a rational isolating interval
chooses a specific real embedding. A polynomial with several roots does not
choose its own cut.

**Hostile control.** Replacing [[0,2],[1,0]] by [[0,1],[1,0]] changes J^2=2I to
J^2=I. The exact probe rejects this mutation. Treating the conjugate embeddings
as order-identical would also be wrong.

## R3. Pi compiles into one rational-function variable

Here is the more perverse payoff. Transcendence obstructs a finite rational
matrix for pi, but makes rational-expression equality particularly clean.

Let Q(t) be the field of rational functions in one indeterminate, and Q(pi)
the smallest subfield of R containing Q and pi. Classical transcendence of pi
is an explicit hypothesis for the following construction.

**Theorem R3.** Evaluation is a field isomorphism

$$
\operatorname{ev}_{\pi}:\mathbb Q(t)\xrightarrow{\cong}\mathbb Q(\pi),
\qquad \frac{p(t)}{q(t)}\longmapsto\frac{p(\pi)}{q(\pi)}.
$$

Every nonzero q in Q[t] has q(pi)!=0 by transcendence, so evaluation is defined
on every rational function. If its value is zero, then p(pi)=0, hence p=0.
Thus evaluation is injective. Its image is a field containing Q and pi, and
every rational expression lies in Q(pi), so it is surjective.

Consequently

$$
\frac{p(\pi)}{q(\pi)}=\frac{r(\pi)}{s(\pi)}
\iff p(t)s(t)-r(t)q(t)=0\quad\text{in }\mathbb Q[t].
$$

Equality is decided by finite polynomial arithmetic. It never requires deciding
whether an approximate floating-point number is exactly zero. For example,
(pi^2-1)/(pi-1)=pi+1 is an exact identity.

### Matrix categories, not just a field analogy

Let Mat_K have objects n in N, including 0, and arrows n->m the m-by-n matrices
over K, with usual matrix composition. Entrywise evaluation gives an isomorphism

$$
\operatorname{Mat}_{\mathbb Q(t)}
 \cong\operatorname{Mat}_{\mathbb Q(\pi)}.
$$

It preserves each hom-set bijectively, addition, identity matrices and
composition. Choosing bases then yields the standard equivalence between the
associated finite vector-space categories. This is a second explicit category
equivalence, now for a field containing the actual source constant.

The isomorphism is of fields/categories before ordering. To represent the real
order, retain the particular cut of pi. A generic formal variable has no
automatically selected real size.

### Order becomes a terminating rational interval computation

Suppose [l_N,u_N] is a computable sequence of rational enclosures of pi with
width tending to zero, such as the certified source intervals in the companion
note. Given a nonzero polynomial p, evaluate it on the enclosure by outward
rational interval Horner arithmetic. These intervals converge to p(pi): this
follows by induction through finitely many additions and multiplications as
the input interval shrinks to one point. Since p(pi)!=0, eventually its interval
excludes zero. Its sign is then certified.

For p/q, first decide p=0 symbolically. Otherwise apply the same process to p
and q and multiply their signs. Every fixed input terminates. This is a
computable ordered-field presentation of Q(pi), not a uniform claim about all
reals, and it does not assert a useful common complexity bound for arbitrary
polynomial degrees and coefficient heights.

The input representation is part of this theorem: the algorithm receives the
rational-function expression. It does not reconstruct such an expression from
an arbitrary Cauchy approximation name, even with a promise that its value is
in Q(pi). The halting-coded values in the computation note are all rational,
hence all in Q(pi). A general decoder from those names to canonical expressions
would decide whether each value is zero, and thereby decide halting. Thus the
abstract field isomorphism is not an unrestricted computable inverse from the
usual real-number representation. Our compiler starts with the named generator
t and preserves its expression history and the selected source cut.

**Digit/floor corollary.** For f in Q(t), floor(f(pi)) is computable. If f is a
constant rational function, compute the floor exactly. If f is nonconstant,
then f(pi) is irrational: an equality f(pi)=a/b would give the nonzero polynomial
b p-a q a root at pi. Shrinking certified intervals therefore eventually fit
between two successive integers. In particular, floor(16^j pi) is computable
for each fixed j>=0. This yields the radix digit after reduction modulo 16.

**Why the symbolic zero branch is necessary.** A refinement procedure waiting
for a sign on p(pi) cannot terminate when p is identically zero. Transcendence
does not make 0 nonzero. Polynomial normalization handles this branch first.

**Why correlations are necessary.** Applying naive interval subtraction to
[1,2]-[1,2] returns [-1,1], although x-x=0 for a shared x. Formal variable
identities preserve this correlation. Treating repeated occurrences as unrelated
input choices gives sound enclosures but loses exact simplifications.

### Exact relation to the authentic SUCC source

With the pinned four-pole source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n),
$$

let pi_N=sum_{n=1}^N 16^{1-n}r(n). Then U_N=16^{N-1}pi_N is rational.
The completed coordinate is Y_N=16^{N-1}pi, for N>=1. Formally it is represented
by 16^{N-1}t, and the tail by 16^{N-1}(t-pi_N). All finite rational identities
among these expressions are available in Q(t). The cut of pi and the analytic
BBP tail theorem certify which real values those symbols denote.

This divides the obligations precisely: polynomial identities certify equality;
source-derived interval bounds certify real order and digit decisions; a
separate theorem must establish long-run Fourier cancellation. An algebraic
compiler does not supply that statistical theorem.

## R4. The finite-matrix boundary is real

**Theorem R4.** Pi cannot be an eigenvalue of a nonempty finite matrix over Q.
The characteristic polynomial of a d-by-d rational matrix is a monic rational
polynomial of degree d. An eigenvalue is a root. Pi is transcendental, so this
is impossible for d>=1.

More strongly, no unital Q-algebra map Q(t)->Mat_d(Q) exists for finite d>=1.
Its image of t would satisfy its characteristic polynomial by Cayley–Hamilton.
That polynomial is a nonzero, hence invertible, element of Q(t), whose image
could not be zero under a unital homomorphism. Contradiction.

The Q(t) representation avoids this obstruction with finite *syntax* of
unbounded polynomial degree; Q(t) is infinite-dimensional as a Q-vector space.
This boundary says nothing against finite programs computing pi to arbitrary
requested precision. The BBP and Machin implementations are such programs.

## R5. Rational metric probes retain the error budget

The order nerve tells us which rational probes lie below a real. To transport
quantitative errors, retain rational distance probes as well:

$$
D_x(q)=|x-q|,\qquad q\in\mathbb Q.
$$

For all finite x,y,

$$
\sup_{q\in\mathbb Q}|D_x(q)-D_y(q)|=|x-y|.
$$

The <= direction is the reverse triangle inequality. For >= choose any rational
q<min(x,y); the difference is exactly |x-y|. Thus the rational distance profile
is an isometric embedding into functions with finite pairwise supremum distance.
The individual profiles are unbounded. Normalize at the rational basepoint 0:

$$
\widetilde D_x(q)=|x-q|-|q|.
$$

The reverse triangle inequality gives |D-tilde_x(q)|<=|x|, and subtracting the
same function from both profiles preserves their difference. Hence this gives
an actual isometric embedding R -> l-infinity(Q), with
norm(D-tilde_x-D-tilde_y)=|x-y|. This elementary identity is the metric/Yoneda-style
companion to the fully faithful rational order nerve. No computability of an
arbitrary full infinite profile is asserted.

A certified enclosure of width epsilon therefore has a genuine quantitative
meaning. A Lipschitz observer with constant L transports that uncertainty by
at most L epsilon. Fourier characters on the circle satisfy the familiar
2*pi*|h| bound; floor and fractional-part-as-an-interval-coordinate are
discontinuous at integers and require the separate margin checks in the
computation note.

## R6. The new arrow-numbers grow coherent families again

The preceding field isomorphism is effective at the symbolic level. Normalize
a rational function p/q by polynomial gcd reduction and make q monic; normalize
zero as 0/1. Rational coefficients have unique reduced numerator/positive
denominator descriptions. Finite coefficient lists therefore have canonical
natural-number codes. For complete explicitness one may use

$$
z(a)=\begin{cases}2a&a\ge0,\\-2a-1&a<0,\end{cases}\quad
\langle u,v\rangle=\frac{(u+v)(u+v+1)}2+v,
$$

code a/b by <z(a),b-1>, and code a finite list (c_0,...,c_(k-1)) by
2^k product_(i=0)^(k-1) p_(i+2)^(c_i+1). Pair the numerator and denominator
list codes, where p_1=2,p_2=3,... is the ordered prime sequence. Valid list
and matrix codes have exactly the prescribed prime support, with no extra
prime factors. Decoding checks reduced fractions, trimmed polynomials, a monic
nonzero denominator and coprimality. The canonical scalar codes form a decidable
subset of N, on which equality, sum, product and nonzero inverse are computable.

For an m-by-n matrix A over Q(t), put

$$
\operatorname{code}(A:n\to m)
=2^n3^m\prod_{k=0}^{mn-1}p_{k+3}^{\operatorname{code}(A_k)+1}.
$$

Unique factorization and the stored dimensions recover all entries, including
zeros and empty matrices. This gives a category of natural-number-coded arrows
isomorphic to Mat_Q(t), hence to Mat_Q(pi). Composition is a terminating
decode/matrix-multiply/normalize/encode operation, not ordinary multiplication
of the numerical codes. The values of pi are not being encoded into a finite
decimal string: its named transcendental generator is retained symbolically.

Fix a universe, or a small model with chosen finite products, for the
finite-dimensional vector-space category. Let K=Q(t), and define
G_n:FinVect_K->FinVect_K by G_n(V)=V^n and
G_n(h)=h^n. An arrow matrix A:n->m produces a natural transformation

$$
\tau_A(V):V^n\longrightarrow V^m,\qquad
(v_i)_i\longmapsto\left(\sum_i A_{ji}v_i\right)_j.
$$

Every component is K-linear, and every linear map h commutes with scalar
coefficients, so naturality is immediate. Composition satisfies
tau_B composed with tau_A = tau_(BA), and identities give identity families.

**Theorem R6.** Mat_K is isomorphic to the full subcategory of the functor
category [FinVect_K,FinVect_K] on the finite-power functors G_n.

To prove fullness, let tau:G_n=>G_m be any natural transformation. The component
at the one-dimensional space K is an m-by-n matrix A. For each v in V apply
naturality to h_v:K->V, 1->v, and to each elementary input vector in K^n.
It forces tau_V to act by the coefficients A_ji on a vector supported in one
coordinate. K-linearity then forces the displayed formula on every tuple.
Thus tau=tau_A. Faithfulness follows by evaluating at K. The n=0 and m=0 cases
are covered by the zero vector space and the unique zero maps.

The Yoneda variance can be checked explicitly: V^n is Hom_K(K^n,V), and tau_A
is precomposition with A-transpose:K^m->K^n. The reversal for covariant
representables is compensated by transpose; it is not silently ignored.

Combining the constructions gives an exact answer to the original bonus:

$$
\operatorname{Mat}_{\mathbb Q(\pi)}
\cong\text{typed natural-number-coded rational-function matrices}
\cong\{G_n,\text{ natural transformations}\}.
$$

An arrow-number has become a coherent family of linear computations on every
finite vector space. The family determines the arrow again, from its component
at K. This is the same representable-observation discipline in a non-thin
category: all linear arrows are retained, not just comparisons of real values.

## R7. Feed the pi compiler back into the two broken-inverse operators

Round II's matrix-unit proof works over any field. Extend its coefficients to
K=Q(t) and set

$$
\mathcal A_K=K\langle S,T\mid TS=1\rangle,\quad
P=1-ST,\quad E_{ij}=S^iPT^j,\quad P_n=1-S^nT^n.
$$

Then P_m A_K P_n is Mat_(m-by-n)(K), by the same matrix-unit relations and
finitely supported unilateral representation. Evaluation of K at pi yields

$$
P_m\mathcal A_{\mathbb Q(t)}P_n
\cong\operatorname{Mat}_{m\times n}(\mathbb Q(\pi)).
$$

For rectangular corners this is a linear bijection compatible with typed
composition, not an assertion that every rectangular matrix space is an
algebra. Explicitly, the category with objects P_n, arrows
Hom(P_n,P_m)=P_m A_K P_n, and identity P_n is isomorphic to Mat_K.

Thus the prior two-operator boundary machine now supports every finite linear
computation with rational-function coefficients in the authentic pi constant.
The rational cut supplies order certificates for its scalar expressions.
This does not contradict R4: the ambient representation is infinite-dimensional
over Q, and the coefficients have unbounded rational-function syntax. It also
does not include arbitrary nonlinear functions or establish statistical
cancellation merely by supplying a linear language in which to ask for it.

## R8. The same Isbell move builds cuts and finite vector spaces

The preceding constructions admit one further common completion mechanism.

Regard a field K as a one-object **Ab-enriched** category: its sole hom-object
is the additive abelian group of K, and composition is field multiplication.
An enriched presheaf is a K-module, hence a K-vector space. Isbell conjugacy is
the algebraic linear dual V-star=Hom_K(V,K); double conjugacy is V-double-star.
The reflexive completion consists of those V for which the canonical evaluation
map V->V-double-star is an isomorphism. This enrichment is essential: no such
claim is made about the bare multiplicative monoid with Set-valued presheaves.

**Theorem R8 (classical, with the usual choice principle for vector-space
bases).** The Ab-enriched reflexive completion of the one-object field is
equivalent to FinVect_K. This is the field case of Avery–Leinster Example 6.12.

Here is the dimension argument. Finite-dimensional evaluation is an isomorphism
by dual bases. If V is infinite-dimensional, choose a countably infinite
dimensional direct summand W with basis e_0,e_1,... . Then W-star=K^N, while
finite-support coordinate sequences form a proper subspace K^(N) inside it.
There is a linear functional L on K^N that vanishes on every finite-support
sequence but sends the all-ones sequence to 1: define it first on the sum of
that subspace and the span of the all-ones sequence, then extend a basis.
If L were evaluation at w=sum a_n e_n, evaluation on the individual coordinate
sequences would give every a_n=0, contradicting L(1,1,...)=1. Thus W is not
reflexive. Dualization respects the two-term direct-sum splitting V=W direct-sum U,
so surjectivity of evaluation for V would imply surjectivity for W. Hence no
infinite-dimensional V is algebraically reflexive.

For the actual source field this gives the concrete completion chain

$$
\operatorname{Ref}_{\mathbf{Ab}}(\mathbf B\mathbb Q(t))
\simeq\operatorname{FinVect}_{\mathbb Q(t)}
\simeq\operatorname{FinVect}_{\mathbb Q(\pi)}.
$$

Together with R6 and R7, the same finite linear category has presentations by
reflexive modules over one object, typed number-coded matrices, finite-power
functors and natural transformations, and corners of the two-operator algebra.

This is the precise relationship to Dedekind cuts: over the rational order
category, Isbell conjugacy takes upper and lower bounds; over the enriched
one-object field, it takes linear duals. The fixed objects are respectively
MacNeille cuts and finite-dimensional vector spaces. The construction is shared;
the base, enrichment, and fixed-point conditions must be stated separately.

## Steelman — crucible — verdict

**Steelman.** Irrational computations can be rebuilt from coherent rational
families, with exact maps and useful arithmetic, while retaining source and
observer data.

**Crucible.** We test the relation J^2=2I, field identities, rational-function
normalization, certified signs and floors against a distinct Machin name. We
reject a wrong quadratic relation, a wrong factor cancellation, zero
denominators, equal finite probe profiles mistaken for equality, and loss of
correlation between repeated variables. The BBP name is shared with the
companion implementation and its hash is recorded: this is not independent
verification of the source identity or of pi's transcendence.

**Verdict.** R1–R8 are proved within the stated classical hypotheses; the finite
implementation receipt corroborates only the tested operations. The strongest
new bridge for this repository is the combination of Q(t) algebra with the
authentic source cut: symbolic equality and certified individual observations
can share one representation without pretending that either implies normality.

**Next verdict-changing probe.** Exhibit a source-preserving transform of the
completed orbit whose signed character sums admit a uniform sublinear bound,
with a transported observer and independently checked residual. Merely
computing more certified digits, or selecting a posteriori cancelling pairs,
does not meet this obligation.

## Reproduction and provenance

Run from this directory:

```sh
python -W error rational_compiler_probe.py --output rational_compiler_receipt.json
```

The script uses Python's exact integers and fractions.Fraction, and imports the
explicit pi-name functions from computation_probe.py. The receipt records both
file hashes. No floating-point comparison is a certificate. Finite checks do
not establish the universal theorems; their derivations appear above.

The category equivalences in R2 and R3 are standard algebraic consequences,
derived here for the chosen source. They are not claims of new classical
mathematics. The integration with this dossier and its audit boundaries is
the local contribution.

Primary sources for background:

- Brian Day, *On closed categories of functors*, Reports of the Midwest Category
  Seminar IV (1970), pp. 1–38, DOI
  [10.1007/BFb0060438](https://doi.org/10.1007/BFb0060438),
  [inspected primary scan](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/DayReport.pdf). R1 uses only the
  explicitly proved truth-valued specialization.
- Tom Avery and Tom Leinster, *Isbell conjugacy and the reflexive completion*,
  Theory and Applications of Categories 36 (2021), 306–347,
  [author manuscript](https://arxiv.org/abs/2102.08290). Its Example 6.10 connects
  reflexive completion of posets with Dedekind–MacNeille completion; Example
  6.12 gives the enriched ring/module dual and field/finite-vector-space cases.
- Ferdinand von Lindemann, *Ueber die Zahl pi*, Mathematische Annalen 20 (1882),
  213–225, [published paper](https://doi.org/10.1007/BF01446522). The archive PDF
  URL was unavailable to the root audit; the directly inspected modern proof
  below supplies the primary text used here for the classical theorem.
- David H. Bailey, *An elementary, self-contained proof that pi is
  transcendental* (2026), [author-hosted proof](https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf).
  R3 and R4 explicitly depend on the classical transcendence theorem; this
  dossier does not re-prove it or infer it from numerical data.
- The exact BBP source, error derivation, primary BBP paper and Machin identity
  are documented in [COMPUTATION_GRAPH.md](COMPUTATION_GRAPH.md). Branch donor
  identities are pinned in [SOURCES.md](../SOURCES.md).
