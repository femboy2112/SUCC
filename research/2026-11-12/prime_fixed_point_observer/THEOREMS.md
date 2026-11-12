# Prime fixed points, productive observers, and the additive compatibility gap

**Status.** Elementary constructions and written proofs in the declared
categories; known antecedents are identified. Exact finite implementations are
separate evidence. Same-model proof audits are not external refereeing or Lean
verification. **Binary Goldbach, pi normality, and RH remain OPEN.**

The question is whether primes can be the fixed objects of a categorical
operation, and whether a finite recursive program can travel indefinitely and
reach every one. The answer is yes. The useful distinction is between the
operation that recognizes fixed objects, the program that travels among them,
and the additive structure needed to pair them around a prescribed midpoint.

## 1. A literal category whose fixed objects are 1 and the primes

Let `Div` be the thin category with positive integers as objects and a unique
arrow `a -> b` exactly when `a` divides `b`. Composition is divisibility
transitivity. Let `tau(n)` count all positive divisors, including 1 and n.
Define

```math
F(n)=n^{\tau(n)-1},\qquad F(1)=1.
```

**PFO-01 — PROVED LOCAL (elementary construction).** `F` extends to an
endofunctor of `Div`; its fixed objects are exactly `{1} union Primes`.
There is a natural transformation `Id -> F`.

**Proof.** If `a|b`, every divisor of a is a divisor of b, so
`tau(a)<=tau(b)`. Write `u=tau(a)-1`, `v=tau(b)-1`. From `a|b` and `u<=v`
we obtain `a^u|b^v`. This supplies the required arrow; identity and composition
laws follow from thinness. For n>=2, tau(n)=2 exactly when n is prime; then
F(n)=n. A composite has tau(n)>=3, hence F(n)>=n^2>n. The unit is fixed.
Finally n divides F(n) for every n, and all naturality squares in this thin
category commute. QED.

Examples:

| Object | tau | Image |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 16 |
| 6 | 4 | 216 |
| 7 | 2 | 7 |
| 9 | 3 | 81 |

F is not idempotent: `4 -> 16 -> 65536`. This is a construction of the
requested fixed-object property, not a fast prime algorithm. Its definition
uses bounded divisor arithmetic and does not assume any additive prime theorem.

**PFO-02 — PROVED LOCAL (no retraction in this category).** There is no
endofunctor R of `Div` which fixes every prime and sends every integer to a
prime or 1.

**Proof.** The arrows `2 -> 6 <- 3` would imply both `2|R(6)` and `3|R(6)`.
Their common multiple cannot be 1 or prime. More generally any Div functor
fixing every prime satisfies `rad(n)|R(n)`. QED.

In particular, the least-prime-factor map is not a Div functor: `3|6`, but
`lpf(3)=3` does not divide `lpf(6)=2`. Also, distinct primes have no arrows
between them in Div. A traversal that visits them successively must expose an
additional computational or additive category. This is a genuine constraint
on the arrows, not an objection to an infinite algorithm.

## 2. Prime closure in a category that supports traversal

Let `Ord` be the thin category on integers >=2 with an arrow `a -> b` iff
`a<=b`, and let `PrimeOrd` be its full prime subcategory. Put

```math
C(n)=\min\{p\ge n:p\text{ prime}\},\qquad
L(n)=\max\{p\le n:p\text{ prime}\}.
```

These are actual total computable maps. For each candidate n, test divisibility
by `2,...,floor(sqrt(n))`. The maximum for L exists because 2<=n. To see that
C's forward scan terminates, any prime divisor q of `n!+1` is >n; the scan
will finish no later than reaching such q. This elementary existence bound
proves totality, not efficiency.

**PFO-03 — PROVED LOCAL.** With i the inclusion,

```math
C\dashv i\dashv L.
```

As endomaps of Ord, `iC` and `iL` are monotone idempotents whose fixed
objects are exactly the primes. In particular `iC` is a closure operator.

**Proof.** For a prime p, `C(n)<=p` iff `n<=p`; also `p<=L(n)` iff `p<=n`.
These are precisely the hom-set conditions for the two adjunctions. Monotonicity
and idempotence also follow directly from the extrema. QED.

Thus a chronological prime observer can use

```math
p_0=2,\qquad p_{k+1}=C(p_k+1).
```

It produces strictly increasing primes. Every prime q is reached: the scan
rejects no prime and never jumps over a prime in choosing the least next one.
Equivalently, induction on the finite set of primes <=q gives its finite
output index. The whole stream need not be completed for this universal
statement to be proved.

There is also a split idempotent in the category of decidable subsets of N
and total computable maps:

```math
\rho(n)=\min\{d\ge2:d\mid n\}\quad(n\ge2),\qquad
\rho^2=\rho,\qquad\operatorname{Eq}(\rho,\mathrm{id})=\mathbb P.
```

The least divisor is prime, because a proper factor of it would be a smaller
divisor of n. If `j:Primes -> N_{>=2}` is inclusion and r is rho with codomain
restricted to primes, then `r j=id` and `j r=rho`. This map is not substituted
for C or asserted to be a Div functor.

**Fixed-orbit boundary.** Once an iteration of any fixed-point map reaches p,
it stays at p. The observer needs `C` together with successor `S(n)=n+1`.
Neither `C` alone nor rho alone visits all fixed points in one orbit.

## 3. A finite program that really unfolds by beta reduction

Here a **fixed-point combinator** constructs a recursive program. An operator
**commutator** is a separate object, introduced in section 6. They share a
research role but are not interchangeable words.

Use the untyped lambda calculus, lazy pairs, natural-number literals, and
arithmetic delta rules `succ`, `mul`, `mod`, `gt`, `eq`. Boolean results are
Church booleans. No primality oracle is an instruction. With

```math
Y=\lambda f.(\lambda x.f(xx))(\lambda x.f(xx)),
```

write the finite program schematically as

```text
Trial = Y (lambda trial n d.
  if d*d > n then true
  else if n mod d == 0 then false
  else trial n (d+1))

Scan = Y (lambda scan n.
  if Trial n 2 then Pair(n, scan(n+1))
  else scan(n+1))

Primes = Scan 2
```

`Trial`'s primality interpretation has the explicit precondition n>=2.
The actual code lowers this finite syntax to SUCC's existing de Bruijn terms
and uses its capture-avoiding beta contraction. Arithmetic operations are
declared delta reductions. Calling the program pure beta reduction would omit
the arithmetic runtime; a further Church encoding of those primitives is
possible but is not the implementation being claimed.

For any functional G, with x chosen fresh for G, set

```math
W_G=(\lambda x.G(xx))(\lambda x.G(xx)).
```

Then literally `W_G ->_beta G(W_G)` and `YG ->_beta W_G`. Thus
`YG =_beta G(YG)` is beta convertibility; it should not be confused with
a claim that Curry's particular syntax always reduces directly to the
literal term `G(YG)`. The standard construction and its evaluation-strategy
qualification are covered in the [Cornell primary lecture notes][lambda].

**PFO-04 — PROVED LOCAL (productivity theorem).** Under the stated lazy
semantics, for every integer k>=0 a finite computation observes the first k
primes, each once, and for every prime p there is a finite observation that
emits p.

**Proof.** For fixed n>=2, each trial raises d by one; either it finds a divisor
or `d*d>n` ends the test. The square-root divisor lemma makes its Boolean
result correct. Every finite integer scan segment consists of finitely many
such terminating computations. Euclid's argument supplies a next prime beyond
every current bound, so every requested next stream cell appears after finite
work. Induct on k. For any fixed prime p, only the finite segment 2,...,p must
be scanned, so p appears. Lazy evaluation exposes each pair without forcing
its recursive tail. QED.

The program has finite syntax and unbounded natural registers. The theorem
does not replace this with a finite-state machine, claim bounded memory, or
assume that infinitely many steps have elapsed. Nor does it claim a runtime
advantage over a proper sieve. O'Neill's [primary analysis][sieve] distinguishes
divisibility-based prime streams from an actual Eratosthenes marking sieve.

`lambda_observer.py` is an untyped research fragment with general recursion.
It is **not** a new inhabitant of the strongly normalizing simply typed
Lambda–Haar compiler. A finite reduction budget reports `UNKNOWN` when
exhausted; the observed prefix remains an observation, not a negative theorem.

## 4. Multiplication produces a prime fixed subspace

The divisor construction has a natural coalgebraic form. On the algebraic
complex vector space with basis `e_n`, n>=1, define

```math
\Delta_\times e_n=\sum_{ab=n}e_a\otimes e_b,
\qquad \epsilon(e_n)=\mathbf1_{n=1}.
```

Both iterated coproducts enumerate ordered triples with product n, so this is
coassociative. The factor pairs `(1,n)` and `(n,1)` give the counit identities.
On the span of labels n>=2, remove those two trivial factorizations:

```math
B e_n=\sum_{\substack{ab=n\\a,b\ge2}}e_a\otimes e_b.
```

**PFO-05 — CLASSICAL STRUCTURE, proof restated.** The primitive basis elements
are exactly the prime labels. The kernel of B is the span of those elements.

**Proof.** A prime has no proper factor pair. A composite has at least one.
Distinct input labels have disjoint factor-pair supports, because each pair
determines its product. Hence no linear combination of different composite
labels can cancel those outputs. QED.

This coproduct and prime-primitive identification are already in
Fauser–Jarvis, [*The Dirichlet Hopf algebra of arithmetics*][coalgebra],
Definition 3.3 and Theorem 3.5; Appendix B records the divisor-incidence Gram
structure. No priority claim is made. In the linear space, **linear combinations
of primes** are primitive too. The unit `e_1` is group-like, not primitive.

Do not silently assert the bialgebra compatibility with ordinary multiplication:
`Delta(e_4)` has coefficient 1 at `e_2 tensor e_2`, whereas `Delta(e_2)^2`
has coefficient 2. Any corrected bialgebra is an additional declared structure.

### Hilbert domains and the exact contraction

Let `H=ell2({2,3,...})`, `K=ell2({(a,b):a,b>=2})`, with counting-measure
orthonormal bases, and put

```math
c(n)=\tau(n)-2.
```

The factor-incidence map B is unbounded: `c(2^k)=k-1`. Its closed extension
has domain `sum_n c(n)|x_n|^2<infinity`. Its positive self-adjoint Gram
operator is

```math
D=B^*B,\qquad De_n=c(n)e_n,
\qquad\operatorname{Dom}(D)=\{x:\sum_n c(n)^2|x_n|^2<\infty\}.
```

These statements follow from the disjoint supports: `||Bx||^2` is exactly
the first weighted sum; closure follows by coordinate convergence. Define the
bounded resolvent

```math
T=(I+D)^{-1},\qquad Te_n=\frac{1}{\tau(n)-1}e_n.
```

**PFO-06 — PROVED LOCAL (elementary spectral consequence).** If P is the
orthogonal prime projection, then

```math
\operatorname{Fix}(T)=\operatorname{ran}P=\ker B,
\qquad \|T^r-P\|=2^{-r}\quad(r\in\mathbb Z_{\ge0}).
```

**Proof.** At a prime the eigenvalue of T is 1. At a composite c(n)>=1, so
the eigenvalue is at most 1/2. Subtract P and take the supremum of the
diagonal eigenvalues of the rth power. Equality occurs at any prime square,
where c(p^2)=1. QED.

Thus the fixed **basis labels** are precisely primes; every square-summable
prime superposition and the zero vector are fixed as well. T is a contraction
on the composite sector, not a globally strict contraction with a unique fixed
point. Including 1 requires a separate direct-sum vacuum fixed vector; inserting
1 into `1/(tau(n)-1)` would divide by zero.

Examples: `T e_7=e_7`, `T e_9=(1/2)e_9`, `T e_12=(1/5)e_12`.
The number 12 is not reduced to a different number here: its vector coefficient
shrinks. This is a different semantics from F(12) or rho(12).

**PFO-07 — PROVED LOCAL (finite source aperture).** For an integer b>=1,
if only proper divisors 2<=d<=b are tested, prime labels are recognized exactly
throughout `2<=n<(b+1)^2`. For an integer window bound M>=2,
`b=floor(sqrt(M))` suffices.

**Proof.** A composite has a prime divisor <=sqrt(n)<b+1, hence an integer
divisor <=b. Every fixed cutoff nevertheless accepts q^2 for a prime q>b.
For instance b=5 accepts 49; b=7 rejects 49 while keeping 7. QED.

Growing b with the demanded input is a single finite algorithm. It is not
defeated by the existence of a counterexample beyond any **fixed** cutoff.

## 5. A finite fixed-sum spectral certificate

Fix an even integer N>=4. Let `H_N=span{e_k:2<=k<=N-2}` of dimension M=N-3,
and let `J_N e_k=e_(N-k)`. Restrict D to this space and put

```math
H_N^{\rm pair}=D_N+J_ND_NJ_N,
\qquad T_N=(I+H_N^{\rm pair})^{-1}.
```

The pair energy at k is the explicit nonnegative integer

```math
c(k)+c(N-k)=\tau(k)+\tau(N-k)-4.
```

It vanishes precisely when k and N-k are both prime. Accordingly, if R(N)
counts ordered prime pairs,

```math
R(N)=\dim\ker H_N^{\rm pair}.
```

**PFO-08 — PROVED LOCAL (finite certificate; Goldbach encoding).** For every
integer r>=0,

```math
R(N)\le Z_N(r):=\operatorname{Tr}(T_N^r)
\le R(N)+(N-3-R(N))2^{-r}.
```

Consequently

```math
2^r>N-3\quad\Longrightarrow\quad
R(N)=\left\lfloor\sum_{k=2}^{N-2}
\frac{1}{(\tau(k)+\tau(N-k)-3)^r}\right\rfloor.
```

**Proof.** Each zero-energy basis state contributes 1. Every other energy is
an integer >=1 and contributes at most 2^-r. There are N-3-R(N) such states.
At the stated cutoff the nonnegative error is strictly below 1, giving the
floor identity. QED.

For `N=6,r=1`, the unqualified floor rule fails: the terms are `1/2,1,1/2`,
whose sum is 2 although R(6)=1. This is why the strict resource cutoff is
part of the certificate. For N=4, M=1, R=1 and the bound still works.

Define `Q_N=T_N^single J T_N^single J`. This alternative filter has
`Tr(Q_N^r)=sum_k[(tau(k)-1)(tau(N-k)-1)]^-r`, with the same error upper bound.
Its eigenvalue-1 space is the pair-energy zero-mode space; Q_N itself is
invertible and has no zero modes. It gives the same finite floor at the stated
cutoff, but generally different finite trace values. The implementation uses the **sum-energy**
resolvent, and the receipt identifies it through its energy histogram.

The positivity of Z_N(r) is automatic, even in a model with no zero modes.
A theorem asserting Z_N(r)>=1 at a sufficient cutoff, for every even N, would
be Goldbach-equivalent. The diagonal representation has not made that lower
bound free. Computing the trace still evaluates the divisor arithmetic of
every candidate; no runtime speedup is claimed.

## 6. The actual commutator and the two-path Haar block

Let P_N be the prime diagonal projection on H_N. Write
`m_N=Tr(P_N)=pi(N-2)` and define

```math
A_N=P_NJ_NP_N.
```

**PFO-09 — PROVED LOCAL (exact reflection spectrum).**

```math
A_N^3=A_N,\qquad
\operatorname{Tr}(A_N)=\mathbf1_{\mathbb P}(N/2),\qquad
\operatorname{Tr}(A_N^2)=R(N).
```

**Proof.** On e_k, A_N has output
`1_P(k)1_P(N-k)e_(N-k)`. Applying it twice yields the diagonal indicator of
prime pairs and a third application recovers A_N. A diagonal matrix entry of
A_N can occur only at k=N/2. The square has one diagonal 1 for every ordered
pair. QED.

Each unequal unordered pair p+q=N gives a two-dimensional block. Its
orthonormal vectors are

```math
v_+=\frac{e_p+e_q}{\sqrt2},\qquad
v_-=\frac{e_p-e_q}{\sqrt2},\qquad A_Nv_\pm=\pm v_\pm.
```

This is exactly the two-point Haar transform, applied along reflection pairs
rather than necessarily adjacent integer intervals. A prime midpoint gives one
additional +1 state. Hence there are `(R(N)+1_P(N/2))/2` eigenvalues +1 and
`(R(N)-1_P(N/2))/2` eigenvalues -1. In particular

```math
R(2n)\equiv\mathbf1_{\mathbb P}(n)\pmod2.
```

For a composite midpoint the positive and negative traces cancel **even when
Goldbach pairs exist**. Positive odd powers see only the central prime; positive even powers
retain all pair states. This is a precise reason an unqualified signed-trace
positivity argument would lose the desired witnesses.

**PFO-10 — PROVED LOCAL (commutator identity).**

```math
[P_N,J_N]e_k=(\mathbf1_{\mathbb P}(N-k)-\mathbf1_{\mathbb P}(k))e_{N-k},
```

and therefore

```math
\|[P_N,J_N]\|_{\rm HS}^2=2(m_N-R(N)),\qquad
R(N)=m_N-\tfrac12\|[P_N,J_N]\|_{\rm HS}^2.
```

**Proof.** Sum the squared displayed coefficients. The two linear indicator
sums both equal m_N; the product sum is R(N). QED.

The bound `||[P_N,J_N]||_HS^2<2m_N` for every even N is exactly Goldbach,
so it is a **reformulation** until an independent source-derived estimate is
proved. Two different commutators give no information: `[P_N,J_NP_NJ_N]=0`
because both factors are diagonal; `[T_N,J_N]=0` because the pair energy is
reflection symmetric. Both identities hold even without any prime pair.

For even N>4, the even subspace contributes exactly 2 to the squared
commutator norm: 2 is prime and N-2 is an even composite. Passing to the odd
subspace subtracts this deterministic term; it does not solve the remaining
odd-prime correlation problem. N=4 is handled separately.

These are Hilbert-space constructions, not evidence that a physical photon
computes the primes, and not a demonstrated quantum speedup. Distinct beta
presentations of one pair do not create additional semantic pair states.

## 7. From Haar coefficients to sharp finite marginal bounds

For midpoint n>=2 and displacement `0<=d<=n-2`, put
`a(d)=1_P(n+d)`, `b(d)=1_P(n-d)`. Then

```math
G(n)=\sum_da(d)b(d),\qquad R(2n)=2G(n)-\mathbf1_{\mathbb P}(n).
```

After zero padding to dyadic length L, Haar Parseval gives

```math
G(n)=\frac{AB}{L}+
\sum_{I\text{ dyadic},\ |I|\ge2}\frac{\Delta_Ia\,\Delta_Ib}{|I|}.
```

Here A and B are total masses, and `Delta_Ia` is the left-half mass minus
right-half mass. Each normalized Haar coefficient is `Delta_Ia/sqrt(|I|)`;
their inner-product expansion proves the identity. Contributions have signs.
For n>2, zero the single-prime-2 endpoint while retaining the displacement
coordinates before asserting parity support;
on the remaining arrays the finest band equals G(n)/2. This includes the
unknown overlap itself and is not an independent positivity estimate.

For integer z>=2, define the jointly screened interior

```math
\mathcal D_{n,z}=\{0\le d<n-z:
\ell\nmid n^2-d^2\text{ for all primes }\ell\le z\}.
```

Choose disjoint cells I whose union exhausts the screened interior. Define
capacities D_I, positive-side prime counts A_I, and negative-side prime counts
B_I, all restricted to this same set.

**PFO-11 — PROVED LOCAL (finite observer and its sharpness boundary).** The
number of interior unordered witnesses lies between

```math
\sum_I\max(0,A_I+B_I-D_I)
\quad\text{and}\quad\sum_I\min(A_I,B_I).
```

The lower bound cannot decrease under refinement; the upper cannot increase.
For independently assignable binary masks these bounds are sharp cellwise.

**Proof.** Inclusion-exclusion gives the lower bound; overlap cannot exceed
either marginal, giving the upper. The inequality
`max(0,x+y)<=max(0,x)+max(0,y)` proves lower refinement; the inequality
`min(a1+a2,b1+b2)>=min(a1,b1)+min(a2,b2)` proves upper refinement. In a
cell of capacity D, putting one mask in the first A positions and the other
in the last B attains the lower bound; nesting attains the upper. QED.

These counts are separate marginals, **not probabilistically independent**:
the shared CRT condition already couples the two arithmetic arguments.
The upper bound controls the interior witness count, not necessarily the full
G(n), because a pair involving a small prime <=z can have been excluded.

**PFO-12 — PROVED LOCAL (shared-center correction).** If a cell contains d=0,
the two masks must have the same known center bit `c=1_P(n)`. Its sharp
lower bound for one globally coherent binary source is

```math
c+\max\{0,(A_I-c)+(B_I-c)-(D_I-1)\}.
```

The upper remains `min(A_I,B_I)`. Other cells use the previous formulas.

**Proof.** Remove the center, whose overlap is c. The remaining capacities and
marginals are `D_I-1,A_I-c,B_I-c`. Off-center positive and negative integer
labels are distinct, both within and across cells; therefore any assignments
to them form a single global binary source. Apply the sharp bound there and
restore the center. QED.

This pays a small but real source-coherence debt. At n=9,z=2,width=4, the
first cell has admissible d=0,2 and A=B=1,D=2. The relaxed lower bound is 0.
The actual shared center 9 is composite, so the coherent bound is 1: both
prime occurrences must be at d=2. The same-source condition supplies information
discarded by treating the two center slots separately.

At n=1024,z=2,width=128 the center is excluded by parity. A zero-overlap
counterfeit matches every coarse cell's two prime marginals, totaling A=137
and B=171, whereas the actual source has 25 witnesses. This control survives
the shared-center correction. It diagnoses the observer's information loss,
not a failure of the genuine primes to pair.

## 8. A categorical counterfeit isolates the additive embedding

Let f be the parity-preserving involution exchanging the following pairs and
fixing every other positive integer:

```text
(53,9), (59,15), (61,21), (67,25), (71,27),
(73,33), (79,35), (83,39), (89,45), (97,49).
```

Transport ordinary multiplication and all its factorization maps by f:

```math
a\odot b=f(f^{-1}(a)f^{-1}(b)).
```

This is an isomorphic multiplicative monoid and category. The transported
coalgebra, primitive subspace, divisor spectrum, norm bound 2^-r, and finite
enumerability all survive. The transported prime indicator agrees with the
ordinary indicator at every n>97. Observations supported entirely on that
tail agree, and finite relabeling does not change limiting densities. Weighted
prefix sums and additive correlations involving a modified small label need
not agree.

**PFO-13 — PROVED LOCAL (hostile model).** If ordinary addition is retained,
the transported primes have no pair summing to 100, although their count and
even-prime profile in [2,98] match the ordinary primes.

**Proof.** Their set in that interval is `{2} union {3,5,7,...,49}`. It has
25 members, one even. Two odd members sum to at most 98. Pairing 2 with
anything in the interval cannot give 100 because 98 is not in the set. Ordinary
primes in the interval also number 25, but the six unordered pairs are
`(3,97),(11,89),(17,83),(29,71),(41,59),(47,53)`. Thus their ordered count
is 12. QED.

The commutator squares are respectively 50 and 26, so the reflection observer
distinguishes sources which the fixed-sector dimension does not.

This transported source fails SUCC's genuine additive/multiplicative braid.
For `S(x)=x+1`, the transported multiplier by 2 is
`V'_2(x)=f(2f^{-1}(x))=2f(x)` because f fixes all even integers. Therefore

```math
V'_2S(8)=106,\qquad S^2V'_2(8)=18.
```

By contrast ordinary multiplication satisfies `V_2 S=S^2 V_2`. If addition
and successor are also transported, the old witnesses transport coherently:
the counterpart of `3+97=100` becomes `3 oplus 49=100`. There is then no
contradiction. The countermodel isolates the loss of the **authentic additive
embedding**, not a refutation of Goldbach or of categorical equivalence.

The ordinary braid is necessary source information; its presence alone is not
claimed to imply an adequate prime-pair estimate. We have identified what an
abstract prime category forgets, not proved that this one restored relation
settles every additive problem.

## 9. Earned result and next obligation

We have unconditional fixed-object constructions, a productive finite recursive
observer, a source-derived spectral filter, exact finite pair certificates,
and explicit categorical and observational countermodels. The operator
commutator and zero-mode criteria are exact **reformulations** of the remaining
Goldbach condition. The shared-center correction is a genuine finite observer
improvement with a strict witness at n=9; it is not a universal advance.

A useful next proof must control the genuine two-sided source, for every
sufficiently large composite midpoint, using independently established
estimates. For example, a predeclared sieve/cell schedule with proved marginal
bounds forcing a positive coherent lower certificate would suffice. The
schedule and marginal estimates must be obtained without consulting already
identified prime pairs. Existence of an unspecified successful schedule is
merely another restatement once singleton cells are allowed.

The classical sieve parity obstruction is relevant to this kind of inference;
[Tao's primary discussion][parity] explains why broad classes of sieve inputs
do not distinguish the needed binary correlation. It is a boundary on those
methods, not a theorem that every possible category or observer approach fails.

[coalgebra]: https://arxiv.org/abs/math-ph/0511079
[lambda]: https://courses.cs.cornell.edu/cs611/2007fa/lectures/lec03-fa07.pdf
[sieve]: https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
[parity]: https://terrytao.wordpress.com/2014/07/09/the-parity-problem-obstruction-for-the-binary-goldbach-problem-with-bounded-error/
