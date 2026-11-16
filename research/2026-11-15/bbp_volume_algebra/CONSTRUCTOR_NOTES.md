# Constructor audit: finite volume grades and the phase closure boundary

**Date:** 2026-11-15. **Source baseline:** SUCC commit
e14d46c17a65e1e5f231c619657b9332caa181c0. **Status:** exact mathematical
derivations for root review; finite audit reported separately below.

## 1. Hole contract and source passport

The intended reusable algebra must retain the original signed source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
\]

Write \(e(t)=\exp(2\pi i t)\). The selected phase sequence at a fixed
integer frequency \(h\ne0\) is \(z_n=e(hU_n)\).

The exact question here is whether the finite polynomial/causal-volume
closure can also supply a finite rational-function linear closure for
this selected phase. The answer is a proved separation:

* Each fixed polynomial grade has a finite triangular linear system over
  \(\mathbb Q(n)\).
* The selected phase has no nonzero eventual homogeneous linear
  recurrence even over \(\mathbb C(n)\).

The first assertion supplies a lawful finite construction. The second
forbids a particular proposed closure; it does not bound computation,
approximation, cancellation, discrepancy, or digit statistics.

**Novelty tax.** The finite polynomial lift is classical symmetric-power
algebra, specialized to the authentic affine source. The rational version
of the phase obstruction is an immediate corollary of inherited
[PG-09](../../2026-11-02/pisot_gamma_gluing/PRIME_BIRTH_STRICTNESS.md).
The fixed-number-field argument and algebraic coefficient descent below
extend that inherited mechanism to \(\mathbb C(n)\). No new prime-birth
mechanism or independent academic priority is asserted.

**Cheapest falsifiers.** A recurrence at a certified first-prime endpoint
would contradict an explicit local cyclotomic automorphism. Removing the
first pole, taking \(h=0\), or taking \(p\mid h\) must destroy that local
separation test. A changed seed with denominator divisible by \(p\) must
fail the first-birth hypotheses. These controls test the instrument and
are not countermodels of the fixed original source.

## 2. The finite source volume and its graded lift

Set

\[
P(x)=4-2x^3-x^4-x^5
 =(1-x)(x^2+2)(x^2+2x+2),\qquad
R(x)=\frac{P(x)}{16-x^8}.
\]

These are the inherited four-pole source objects in
[FOUR_POLE_ATOMIC_SUBSTRATE](../../2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md).
For \(n\ge1\), define the finite polynomial

\[
f_n(x)=P(x)\sum_{j=1}^{n}16^{n-j}x^{8(j-1)}
      =(16^n-x^{8n})R(x),
\qquad f_0(x)=0.
\]

For all \(n\ge0\), \(f_n\ge0\) on \([0,1]\), and termwise integration of
the finite polynomial gives

\[
\int_0^1 f_n(x)\,dx
 =\sum_{j=1}^n16^{n-j}
   \left(\frac4{8j-7}-\frac2{8j-4}
                      -\frac1{8j-3}-\frac1{8j-2}\right)
 =U_n. \tag{CN-01}
\]

Thus the source lift changes neither the pole weights nor the seed.
For an integer \(k\ge1\), symmetry of the integrand and the
measure-zero collision diagonals give

\[
V_{n,k}:=\frac{U_n^k}{k!}
 =\int_{0<x_1<\cdots<x_k<1}
       \prod_{\ell=1}^k f_n(x_\ell)\,dx_1\cdots dx_k.
\]

Set \(V_{n,0}=1\), including at \(n=0\). This is a literal ordered
volume formula. The denominator is \(\Gamma(k+1)=k!\).

### CN-02: finite grade closure and scalar recurrence bound

For every integer \(d\ge0\), the vector
\(V_n=(V_{n,0},\ldots,V_{n,d})^{\mathsf T}\) satisfies

\[
V_{n+1,j}
 =\sum_{k=0}^{j}
    16^k\frac{r(n+1)^{j-k}}{(j-k)!}V_{n,k},
\qquad 0\le j\le d. \tag{CN-02}
\]

The matrix is lower triangular over \(\mathbb Q(n)\), with diagonal
\(1,16,\ldots,16^d\), hence determinant
\(16^{d(d+1)/2}\).

**Proof.** Expand \((16U_n+r(n+1))^j/j!\) by the binomial theorem.
The coefficient of \(U_n^k/k!\) is exactly the displayed coefficient.
The degree bound closes because an affine substitution preserves
polynomial degree. No limiting interchange is involved.

More generally, let \(F\) be any field containing \(\mathbb Q\), and let

\[
Y_n=\sum_{k=0}^d b_k(n)V_{n,k},\qquad b_k(n)\in F(n).
\]

Then \(Y_n\) satisfies a nonzero homogeneous linear recurrence over
\(F(n)\) of order at most \(d+1\), valid for all sufficiently large \(n\).
This is an upper bound, not a claim of minimal order.

To prove the assertion, write the update matrix as \(A(n)\), and let
\(A^{[0]}(n)=I\) and
\(A^{[j]}(n)=A(n+j-1)\cdots A(n)\) for \(j\ge1\).
For each \(j\), \(Y_{n+j}\) is the row
\(b(n+j)A^{[j]}(n)\in F(n)^{d+1}\) applied to \(V_n\).
The \(d+2\) rows for \(0\le j\le d+1\) are linearly dependent over
\(F(n)\). A nonzero dependence gives the claimed recurrence.
Its finitely many coefficient poles are avoided by taking \(n\)
sufficiently large.

For example, \(U_n\) has the explicit order-at-most-two recurrence

\[
U_{n+2}
 -\left(16+\frac{r(n+2)}{r(n+1)}\right)U_{n+1}
 +16\frac{r(n+2)}{r(n+1)}U_n=0. \tag{CN-03}
\]

The ratio is legitimate for all nonnegative integer \(n\): the
four-pole density gives \(r(n+1)>0\).

The full formal series, which is not a fixed finite grade, satisfies

\[
\mathcal S_n(t)=\sum_{k=0}^{\infty}V_{n,k}t^k=e^{tU_n},
\qquad
\mathcal S_{n+1}(t)=e^{t r(n+1)}\mathcal S_n(16t).
\tag{CN-04}
\]

Both the formal identity and the entire-function identity are valid.
At \(t=2\pi i h\), the latter is the actual selected phase.

## 3. Fresh-prime separation, with its inherited provenance

Let \(p\equiv1\pmod8\) be prime and \(b=(p+7)/8\).
Such a prime is at least 17. At every earlier time \(0\le i<b\), the
reduced denominator of \(U_i\) is prime to \(p\): every earlier source
denominator is at most \(p-3\). At the first occurrence,

\[
U_b=\frac4p+B_b,\qquad
B_b=16U_{b-1}-\frac2{p+3}-\frac1{p+4}-\frac1{p+5},
\qquad p\nmid\operatorname{den}(B_b). \tag{CN-05}
\]

This is precisely the arithmetic premise of inherited PG-09.
In particular \(v_p(U_b)=-1\).

Assume \(p\nmid h\), and let \(M\) be the least common multiple of the reduced
denominators of \(hB_b\) and all \(hU_i\), \(i<b\). Then \(p\nmid M\).
The field \(E=\mathbb Q(\zeta_M)\) contains the earlier phases and
\(e(hB_b)\), while

\[
z_b=e(hB_b)\zeta_p^{4h}.
\]

Because \(4h\) is nonzero modulo \(p\), this last factor is a primitive
\(p\)-th root. The classical cyclotomic degree formula gives

\[
[E(\zeta_p):E]
 =\frac{\varphi(Mp)}{\varphi(M)}=p-1. \tag{CN-06}
\]

Here the compositum is \(\mathbb Q(\zeta_{Mp})\), since \((M,p)=1\).
For a primary reference for cyclotomic irreducibility and the degree
formula, see Romyar Sharifi, *Algebraic Number Theory*, Proposition
[3.1.14](https://math.ucla.edu/~sharifi/notes/algnum-ch03.html).

For rational coefficients, a relation ending with a nonzero multiple of
\(z_b\) would put \(\zeta_p\) in \(E\), contradicting (CN-06). This is
the inherited PG-09 conclusion, not a new result here.

### CN-07: extension to any fixed number field

Let \(K\subset\mathbb C\) be a number field. If also
\(p-1>[K:\mathbb Q]\), then

\[
\sum_{i=0}^{b}c_i z_i\ne0
\quad\hbox{for all }c_i\in K\hbox{ with }c_b\ne0. \tag{CN-07}
\]

**Proof.** A zero sum would put
\(\zeta_p^{4h}\), hence \(\zeta_p\), in the compositum \(KE\). But then

\[
p-1=[E(\zeta_p):E]\le[KE:E]\le[K:\mathbb Q],
\]

a contradiction. The last inequality follows by taking a
\(\mathbb Q\)-basis of \(K\): its \(E\)-span is a finite-dimensional
\(E\)-algebra without zero divisors, hence a field. It is therefore
the compositum \(KE\), of degree at most \([K:\mathbb Q]\).
No hypothesis that \(K\) is Galois is needed.

### Infinitely many usable endpoints, without a prime-density theorem

There are infinitely many primes \(p\equiv1\pmod8\).
Indeed, for any finite list \(p_1,\ldots,p_s\) of them, take
\(A=2\prod_i p_i\). Any prime divisor \(q\) of \(A^4+1\) is odd,
does not divide \(A\), and satisfies \(A^4\equiv-1\pmod q\).
The multiplicative order of \(A\bmod q\) is therefore exactly 8,
so \(8\mid q-1\). Also \(q\) is absent from the list. This proves
infinitude. Removing the finitely many primes dividing \(h\), and
requiring \(p-1>[K:\mathbb Q]\), still leaves infinitely many.

## 4. No eventual rational-function linear recurrence for the phase

### CN-08: number-field coefficient version

For every fixed integer \(h\ne0\), every number field \(K\), every
integer \(d\ge0\), and every tuple
\(a_0,\ldots,a_d\in K(n)\) not all zero, the identity

\[
\sum_{j=0}^{d}a_j(n)z_{n+j}=0 \tag{CN-08}
\]

cannot hold for all sufficiently large integers \(n\).

**Proof.** Replace \(d\) by the largest index with
\(a_d\not\equiv0\); this includes \(d=0\).
Only finitely many integer arguments are coefficient poles, and
the nonzero rational function \(a_d\) has only finitely many zeros.
Choose a usable fresh prime \(p\) so large that
\(b=(p+7)/8\) and \(n=b-d\) avoid all these exceptions and lie in
the alleged eventual recurrence range. Evaluating (CN-08) yields
a \(K\)-linear relation involving only times \(b-d,\ldots,b\),
with nonzero coefficient on the last term. Set unused earlier
coefficients to zero in (CN-07). This contradicts (CN-07).

### CN-09: algebraic coefficient descent

Let \(s_n\in\overline{\mathbb Q}\) for all \(n\ge0\).
If \(s_n\) satisfies a nonzero eventual recurrence over
\(\mathbb C(n)\), then it satisfies one over \(K(n)\) for some
fixed number field \(K\).

**Proof.** Clear the finitely many rational-function denominators.
There are integers \(d,D,n_0\ge0\) and coefficients
\(c_{j,k}\in\mathbb C\), not all zero, such that

\[
\sum_{j=0}^d\sum_{k=0}^D c_{j,k}n^k s_{n+j}=0
\qquad(n\ge n_0). \tag{CN-09}
\]

For each \(n\ge n_0\), form the row
\(w_n=(n^k s_{n+j})_{0\le j\le d,\ 0\le k\le D}\).
Its entries lie in \(\overline{\mathbb Q}\). These rows have
width \(L=(d+1)(D+1)\), so their span over
\(\overline{\mathbb Q}\) has a finite basis consisting of at most
\(L\) of the rows. Their rank over \(\mathbb C\) is the same:
a finite minor is nonzero over one field exactly when it is nonzero
over the other. The given nonzero complex kernel vector implies
that this rank is strictly smaller than \(L\).

Gaussian elimination on a finite row basis, performed over
\(\overline{\mathbb Q}\), therefore produces a nonzero
kernel vector \((\widetilde c_{j,k})\) with algebraic entries.
Every omitted row is an algebraic linear combination of the basis
rows, so this vector annihilates every row, not merely a finite
test sample. Its finitely many entries generate one number field
\(K=\mathbb Q(\widetilde c_{j,k})\). The resulting nonzero
polynomials \(\widetilde a_j(n)=\sum_k\widetilde c_{j,k}n^k\)
give the asserted eventual recurrence over \(K(n)\).

**Reusable consequence.** Every algebraic-valued sequence that is
P-recursive over \(\mathbb C(n)\) has all of its values in a single
number field. After CN-09, choose a starting index beyond every zero
of the maximum-shift coefficient and every coefficient pole.
Adjoin to \(K\) all the finitely many values through that starting
index plus the recurrence order. Solving the recurrence forward
keeps every later value in this same finite extension. In order zero,
the eventual sequence is zero and the conclusion is immediate.
Thus unbounded algebraic degrees are a sufficient obstruction.
This is a necessary condition for such linear closure, not a
sufficient condition.

### CN-10: the selected phase is not P-recursive over \(\mathbb C\)

For each fixed integer \(h\ne0\), the original zero-selected sequence
\(z_n=e(hU_n)\) satisfies no nonzero eventual finite-order
homogeneous recurrence over \(\mathbb C(n)\). Equivalently,
clearing denominators, it satisfies no such recurrence with complex
polynomial coefficients.

**Proof.** Every \(U_n\) is rational, so every \(z_n\) is a root of
unity and belongs to \(\overline{\mathbb Q}\).
A complex-coefficient recurrence would descend by CN-09 to a
fixed number field, contradicting CN-08.

In particular there is no finite dimension \(D\), eventual state
sequence \(y_n\in\mathbb C^D\), matrix \(A(n)\in
\operatorname{Mat}_D(\mathbb C(n))\), and row
\(c(n)\in\mathbb C(n)^{1\times D}\) satisfying

\[
y_{n+1}=A(n)y_n,\qquad z_n=c(n)y_n
\]

for all sufficiently large \(n\). The \(D+1\) shifted output rows,
expressed against \(y_n\), are dependent over \(\mathbb C(n)\)
and would give a recurrence of order at most \(D\).
Affine systems over this field are also excluded after adding a
constant coordinate.

This conclusion applies to a fixed finite-grade Taylor/volume
representation with rational-function linear evolution and
rational-function linear readout. It does not exclude a different
representation using nonlinear updates or coefficient functions
outside \(\mathbb C(n)\).

## 5. Phase and carry remain exact nonlinear images

The original phase has the explicit finite nonlinear evolution

\[
z_{n+1}=e(h r(n+1))\,z_n^{16}. \tag{CN-11}
\]

Writing \(x_n=\{U_n\}\) and \(I_n=\lfloor U_n\rfloor\), the literal
integer carry is

\[
\kappa_{n+1}=I_{n+1}-16I_n
 =\lfloor16x_n+r(n+1)\rfloor,
\quad
x_{n+1}=16x_n+r(n+1)-\kappa_{n+1}. \tag{CN-12}
\]

For a formal parameter \(t\),

\[
e^{t x_{n+1}}
 =e^{t(r(n+1)-\kappa_{n+1})}e^{16t x_n}.
\]

At \(t=2\pi i h\), \(h\in\mathbb Z\), the integer-carry factor is one.
This is an exact character identity. It does not mean that the carry
can be deleted from a state representation that is meant to retain
the integer lift or the actual digit/carry history.

The role of time in CN-10 is the integer recurrence time \(n\).
It is not the coefficient index of the inherited four-dimensional
source atom, the difference-order variable of the inherited
Pascal holonomic source, or the fractional Oily depth parameter.
Their established finite closures are compatible with CN-10.

## 6. A sharp control for the remaining cancellation debt

Non-P-recursiveness does not imply cancellation, even qualitatively.
Let \(p_n\) be the increasing sequence of primes and set
\(\eta_n=e(1/p_n)\). The same fresh-prime field-degree argument,
followed by CN-09, proves that \(\eta_n\) is not P-recursive over
\(\mathbb C\). At the last time of any alleged recurrence, the
new prime \(p_n\) is absent from all previous phase denominators.
For any fixed coefficient field, eventually
\(p_n-1>[K:\mathbb Q]\), so the same contradiction applies.

But \(p_n\to\infty\), hence \(\eta_n\to1\), and consequently

\[
\frac1N\sum_{n=1}^N\eta_n\longrightarrow1.
\]

This is a different-source control for the inference from linear
nonclosure to cancellation. It is not a shifted-seed refutation of
the authentic BBP orbit. Even the strengthened phase obstruction
does not provide a lower bound on a signed BBP sum, a power saving,
an equidistribution theorem, or normality.

The still-open analytic target must retain the actual complex
character after source integration and must control signed sums
along the selected orbit. Finite source closure and fresh-prime
nonvanishing identify lawful constructions and forbidden shortcuts;
they do not discharge that target.

## 7. Executable audit and claim boundary

[prime_birth_audit.py](prime_birth_audit.py) is a standard-library-only
audit with no production imports. It compares the direct four-pole
recurrence against an independently combined rational source and
finite convolution. For each tested fresh prime it constructs an
explicit CRT exponent \(a\) with \(a\equiv1\pmod M\) and
\(a\equiv2\pmod p\). The associated cyclotomic automorphism fixes
every earlier phase and the \(p\)-free cofactor, and moves the last
phase by the exact argument \(4h/p\bmod1\).

The controls include \(h=0\), \(p\mid h\), deletion and sign mutation
of the first pole, a composite candidate, and a changed seed.
The last control is explicitly outside the source passport.
The audit also checks the positive unwrapped recurrence CN-03.

**Run status:** PASS on 2026-11-15.

| Run | Fresh primes | Cross-checked source times | Separating frequency/prime pairs | Null pairs | Degree-one recurrence centers |
| --- | ---: | ---: | ---: | ---: | ---: |
| Default prime budget 1024 | 38 | 127 | 188 | 2 | 126 |
| Extended prime budget 4096 | 133 | 510 | 663 | 2 | 509 |

The extended run reaches \(p=4073\), \(b=510\), with a 4407-bit
prior conductor and exact newborn argument shift \(4/4073\).
All listed controls passed. An additional runtime mutation changing
the first-pole weight from 4 to 5 was rejected at source time 1 by
the independent combined rational formula. Invalid budgets
True, 17.0, 16, and 4097 were rejected. The inherited PG-09 probe
was rerun successfully at its ten listed primes.

Reproduce the standalone runs with:

~~~sh
python research/2026-11-15/bbp_volume_algebra/prime_birth_audit.py
python research/2026-11-15/bbp_volume_algebra/prime_birth_audit.py --max-prime 4096
python research/2026-11-02/pisot_gamma_gluing/prime_birth_probe.py
~~~

The finite script verifies arithmetic premises and exact local
certificates. The universal recurrence exclusion rests on the
proofs CN-07 through CN-10, not on enumerating finitely many primes.

**Ledger for root review.**

| Claim | Earned kind | Dependency and boundary |
| --- | --- | --- |
| Finite ordered source volume CN-01 | Exact reformulation | Inherited four-pole source; finite sum and symmetry |
| Finite grade system CN-02 and recurrence bound | Classical proof step, source specialization | Affine dynamics, fixed degree, rational-function coefficients |
| Rational fresh-prime nonvanishing | Inherited PG-09 | Exact zero seed and source; no size lower bound |
| Fixed-number-field separation CN-07 | Proof extension | Field-degree bound at sufficiently large new primes |
| No eventual complex recurrence CN-10 | Proof step, pending root audit | Algebraic-valued phases and finite-row descent |
| Actual phase/carry dynamics CN-11 and CN-12 | Exact transport identities | Integer frequency; carry retained when observing its history |
| Selected BBP signed cancellation | OPEN | Needs a quantitative theorem at the actual embedding |

## 8. Review receipt for the assembled algebra

The constructor separately reviewed the assembled theorem, implementation,
and tests. This is an internal proof/code review, not an external or
formally checked certificate.

The reviewed implementation snapshot has SHA-256
3a292ea2bed9012730a3821f57041ee496ef925733ebc7c428d34e3751f74453
for observational_succ/bbp_volume_algebra.py. The reviewed test snapshot
has SHA-256
cdce7f7ba8601b80e8449f86e83477ead9696bea0f2c70d71eded4d06985d8f6
for tests/test_bbp_volume_algebra.py.

No arithmetic, clock, exact-type, or declared-budget defect was found
in those code snapshots. An independent three-word ordered-partition
enumeration matched both binary product parenthesizations: 409 collected
words for lengths (2,2,2), and 101 for lengths (2,1,2), including
fractional radices and unit source monomials. This supplements the
existing tests with a different combinatorial implementation; it is
still finite evidence, not the universal associativity proof.

The theorem review verified the full convolution square, all-order
endpoint cancellation, normalized Gamma bound, inclusive discrete
collision sign, seeded boundary term, formal active-head associativity,
polynomial grade closure, complex-coefficient descent, carry signs,
Gamma threshold (including alpha below one at the threshold), and
Mellin boundary sign. The root incorporated the requested restrictions
to k>=1 in the causal power hierarchy, finite fundamental-phase
observations in the lift-modulus theorem, and explicit integration
domains. One remaining wording repair was requested on theorem
snapshot a63f14f33fd9d96b991bef29522a39a0ba391a7d5301ba0222519fbb4dd7b1ff:
choose the conductor M as the least common multiple, rather than an
arbitrary common multiple, to imply p does not divide M.

### Closing receipt — 2026-11-15

**LCM wording correction resolved.** The current VA-06 explicitly
chooses M as the least common multiple of the denominators of B_b
and the earlier U_i. This supplies the required p-free conductor.
The corrected THEOREMS.md snapshot has SHA-256
8dfd1d921041d3599834f8d8b130144dcf0649e98a163e3d286b8c7bdaf3f5e2.
The preceding request is retained as review history; it is no longer
an outstanding correction. No further tests or production edits
were performed for this closing verification.
