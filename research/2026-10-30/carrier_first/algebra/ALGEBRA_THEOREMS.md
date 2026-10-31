# Labeled carrier arithmetic and the exact obstruction to forgetting order

**Authority:** local paper proofs of elementary category, binomial and linear
algebra statements; a separately scoped Lean4.14 kernel subset; exact finite
tests and a separately implemented oracle. No scholarly-priority claim.
Parent PR417 and sibling PR421 already contain scalar Pascal/umbral,
Grothendieck, first-jet and source-realization constructions. The addition here
is an executable typed path API, the noncommutative product/transport defects,
the reachable-state descent criterion, and its native BBP ordering instance.

## A1. Positive paths and coherent colored gluing

An object is a finite ordered list of pairwise distinct labeled slots; each
slot has an arbitrary color. A morphism from S to T is an extension
`T=S concatenated L`, equipped with one binary selection choice for each slot
of L. Identity is empty extension; composition concatenates both slot and
choice lists. The middle objects must match literally. Labels may not be
reused. Associativity and identities follow from list concatenation, so this
is a category, not merely an array of binomial numbers. Its arrow grade is
the number of selected new slots and is additive under composition.

For a fixed n-slot extension the arrows of grade k are bijective to its
k-element subsets; their number is C(n,k). Splitting before the last slot
partitions arrows according to the final bit and gives Pascal. Splitting a
fixed concatenation of blocks of lengths a,b partitions by the first block's
grade j and gives Vandermonde. The three-block bijections agree exactly,
since both retain the same three substrings. Relabeling is functorial whenever
the relabeling is injective on the finite lists involved. Disjoint union of
unlabelled cardinalities is implemented by disjoint colored concatenation;
the commutativity isomorphism swaps blocks, and must also move their histories.

The grade quotient is not faithful: `(0,1)` and `(1,0)` have the same endpoint
grade but different histories. This is a genuine forgotten arrow, not a
different count. A morphism here need not commute with a time-sensitive
source decoration after that permutation.

## A2. Signed completion and the smallest multiplication square

The commutative monoid of finite-set isomorphism classes is N. Pairs `(p,n)`
of positive counts satisfy `(p,n)~(p',n')` iff `p+n'=p'+n`. Addition and the
inverse `(n,p)` descend, giving Z by `(p,n)->p-n`. The pair product
`(p p'+n n', p n'+n p')` descends and realizes the ordinary integer product.
The API keeps positive counts/paths separate from signed representatives;
equivalence is a named method, not equality of the representatives.

For two differently colored finite blocks A,B, the grade-two decomposition is

```
two-subsets(A disjoint-union B)
       <-> two-subsets(A) disjoint-union (A x B) disjoint-union two-subsets(B).
```

The map sends a mixed pair to its ordered color components, and the inverse
forgets that order after restoring the colors. This is the smallest grade in
which both summands participate. Taking cardinality gives
`ab=C(a+b,2)-C(a,2)-C(b,2)`. Both sides are polynomials, so the identity extends
to all signed ranks a,b. The diagram retains the two inclusions and their
colors: total rank four alone cannot distinguish the cross terms 1*3 and 2*2.
Grade-two evaluation alone also confuses ranks zero and one.

For n>0, `C(-n,k)=(-1)^k C(n+k-1,k)`. This follows directly by factoring
(-1)^k from the falling product. Negative values, for example C(-1,1)=-1,
cannot be cardinalities of literal finite subset sets. Vandermonde on signed
ranks follows by polynomial extension of the positive identity (fix one
variable at a time and use infinitely many natural roots).

## A3. Noncommutative umbral transport and the overlap defect

Let R be any associative unital Q-algebra and let x be central. On R[x],
define J coefficientwise by `J(x^k/k!)=C(x,k)`. Then `Delta J=J D`, with
`Delta f(x)=f(x+1)-f(x)`: verify on each basis vector using Pascal and extend
linearly. Commutation of coefficients is unnecessary. But ordinary products
are not preserved. The full ordered product formula is

\[
 \binom xi\binom xj=\sum_{r=0}^{\min(i,j)}
 \frac{(i+j-r)!}{r!(i-r)!(j-r)!}\binom x{i+j-r}.
\]

Proof on natural x: count an ordered pair of subsets by intersection size r,
then classify its union into intersection and two exclusive parts. Polynomial
extension proves it for every x. Matrix/source coefficients multiply in their
original order `A_i B_j`. No coefficient permutation is licensed.

The transported product `f star g=J(J^-1 f J^-1 g)` retains only the r=0 term:
`C(x,i) star C(x,j)=C(i+j,i)C(x,i+j)`. Thus the ordinary-minus-star product
defect is exactly the sum of the r>=1 overlap terms. This identifies the
discarded shared-slot interactions. In particular `x*x-x star x=x`.

Delta is a derivation for star, while for ordinary multiplication
`Delta(fg)=Delta(f)g+f Delta(g)+Delta(f)Delta(g)` with displayed order.
Equivalently it is `f(x+1)Delta(g)+Delta(f)g`. The star algebra is associative
because the transported polynomial algebra is; ordinary commutativity is
not silently added to noncommutative R.

**A safe analytic extension.** In a finite-dimensional complex normed
algebra, suppose `||c_k||<=C rho^k` with `0<rho<1`. Then
`f(z)=sum c_k z^k/k!` and `Jf(z)=sum c_k C(z,k)` are entire and locally
normally convergent. For |z|<=R, R>=1,
`|C(z,k)|<=product_(j=0)^(k-1)(j+R)/(j+1)
<=exp((R-1)H_k)`, a polynomial majorant in k; the geometric coefficient
bound dominates it. The shifted coefficient sequence has the same property,
so subtracting locally normally convergent series gives `Delta Jf=J Df`.
Termwise analytic differentiation follows from local normal convergence.
This is a sufficient domain, not a theorem for arbitrary formal Newton
series. Polynomial product identities remain unconditional; using them on
two infinite series requires an absolute-convergence argument. No closure
of the entire union of these exponential classes under star is asserted.

## A4. Exact source-decorated descent: flat on which states?

At Pascal vertex (n,k), let `A_(n,k)` and `B_(n,k)` be linear maps on one
fixed vector space V assigned respectively to bits zero and one. A path's
weight W is their chronological composition, later maps acting on the left.
Define the elementary diamond

\[
 D_{n,k}=B_{n+1,k}A_{n,k}-A_{n+1,k+1}B_{n,k}.
\]

**Operator version.** Every path transport from every starting vertex depends
only on its endpoint iff every D_(n,k)=0. Necessity compares the two length-two
paths. For sufficiency, any two bit words of equal length/grade are related
by adjacent swaps 01<->10; a flat diamond preserves the transport under each
swap, with the same remaining prefix and suffix endpoints.

**Selected reachable-state version.** Fix one start and one vector v. At each
reachable vertex let R_(n,k) be the set of all transported vectors from that
start. Then every path applied to v depends only on its endpoint iff

\[
 D_{n,k}w=0\quad\hbox{for every reachable }w\in R_{n,k}.
\]

Necessity appends 01 and 10 to each reachable prefix. Sufficiency again
uses adjacent swaps; before the swapped letters the vector is reachable,
and afterwards the same suffix acts on equal vectors. This proof requires
no invertible edges. It cannot replace reachable vectors by the whole
ambient space in the necessary condition.

Exact control: A=diag(1,2), B=((1,1),(0,1)) have nonzero commutator, but both
fix v=(1,0). Every reachable vector is v, and every selected path has the same
state. Conversely the two shears A=((1,1),(0,1)), B=((1,0),(1,1)) give different
length-two states for v=(1,0). Thus operator flatness and selected adequacy
are different predicates even in the smallest matrix model.

## A5. What a nonflat diamond actually contributes

For words with a common prefix P and suffix S,

\[
 W(P01S)-W(P10S)=W(S)D_{n,k}W(P).
\]

Any adjacent-swap chain yields the exact telescoping sum of these transported
defects. The suffix starts at (n+2,k+1), common to both branches. Bare sums of
diamonds omit the actual action and are generally wrong. This is an explicit
noncentral source interaction; it need not have a useful sign after a
complex observer. For constant matrices with norms at most L, each swap
has norm at most `L^(length-2)||BA-AB||`. A bubble-sort comparison uses exactly
the word's inversion count, proving the corresponding norm bound. This is a
generic upper error estimate, not a selected Fourier saving.

## A6. Authentic BBP source-order rigidity, and its limit

For radix b>1, the affine update is the matrix
`M(r)=((b,r),(0,1))` on vectors `(u,1)`. Direct multiplication gives

\[
 M(s)M(r)-M(r)M(s)=\begin{pmatrix}0&(b-1)(r-s)\\0&0\end{pmatrix}.
\]

The authentic source, with `a=8n-7`, is exactly
`r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`. Each summand is positive and strictly
decreasing for a>0. Hence for any finite N>=2, every source-permuted affine
path has lift
`b^N s+sum_(j=1)^N b^(N-j) r(pi(j))`. Because both native sequences
`r(1)>...>r(N)` and `b^(N-1)>...>1` strictly decrease, the chronological
ordering is the unique maximizer and the reversed ordering the unique
minimizer. Proof: any inversion of the source order can be corrected by an
adjacent swap; the lift increases by exactly
`(b-1)b^(N-j-1)(r(i)-r(l))>0` when the earlier slot j receives the larger
source value r(i). Sorting reaches the native order. This is an all-N,
source-correct obstruction to forgetting the update history.

It is independent of the initial seed. The coherent seed satisfies the same
ordering theorem, so the result cannot certify zero-seed normality. It is
also an unwrapped inequality: two positive decreasing source values 2/15
and 1/15 with b=16 have a swap defect exactly one, invisible on the circle.
The lemma restricts admissible history descent; it does not separate actual
BBP phases or bound their selected pair collisions.

## Provenance and semantic roles

Pascal/Vandermonde, Grothendieck completion, binomial finite calculus,
coefficientwise umbral transport and rearrangement are classical mathematics.
The binomial path and Pascal conventions agree with the primary reference
[NIST DLMF 26.3](https://dlmf.nist.gov/26.3), checked during this round.
The explicit API and scoped descent/defect assembly are this local research
artifact. PR417 is the carrier baseline; PR421 supplies the read-only
source/first-jet realization context. Main's operational triangle supplies
the author-defined Harmonic/Golden/Euler–Mascheroni/Fibonacci and
Oily–Macaroni provenance. Harmonic accumulation and recursive transport have
literal operators here. No new occurrence of a golden/Fibonacci constant is
forced by this algebra, and no arithmetic distribution theorem is inferred
from the author-defined semantic roles.
