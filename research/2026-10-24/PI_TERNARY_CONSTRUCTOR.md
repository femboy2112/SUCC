# Ternary Pascal filters: a dyadic quarter filter and an isometric base-81 source

**Date:** 2026-10-24. **Inherited source:** draft #272 at
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
**Authority:** paper proofs below; finite checks are explicitly scoped.
**Status:** exact new source constructions and sharp denominator obstructions.
Real same-law transport, real central-carry retention, and pi normality remain OPEN.
No scholarly priority is claimed.

## 1. Objects and the precise research cut

Use the authentic rational BBP source

\[
U_0=0,\qquad U_{n+1}=16U_n+r(n+1),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Write \(\alpha=\pi/16\), \(U_n=16^n\alpha-T_n\), and
\(T_n=\int_0^1t^n\,d\rho(t)\), using the fixed positive measure from
[the inherited real-kernel dossier](PI_PASCAL_REAL_KERNEL.md):

\[
d\rho(t)=w(t)\,dt,\qquad
w(t)=\frac{g(t^{1/8})}{8t^{7/8}(16-t)},\qquad
g(x)=4-2x^3-x^4-x^5.
\]

Its endpoint densities are
\(w(t)\sim t^{-7/8}/32\) at zero and
\(w(t)\sim(1-t)/64\) at one. Its support is the entire interval.
Let \(E\) shift the original index and \(\Delta=E-1\).
The inherited dyadic source interpolation \(F\) obeys, uniformly on
\(\mathbb Z_2\),

\[
v_2(\Delta^jF(t))=\nu(j):=2j-s_2(j)-1\quad(j\ge1),
\qquad F(0)=0,\quad F(n)=U_n.
\]

The starting classical identity is
\(\sum_{j=0}^k\binom kj2^j=3^k\). The present cut asks whether a
Pascal operator can produce an authentic rational ternary source with
a controlled **absolute** error and less carry information than the
previous \((E-1)/5\) construction. Equality of empirical laws is a
separate obligation.

For every fixed polynomial \(P\), finite linearity gives

\[
P(E)^kU_n=P(16)^k16^n\alpha
-\int_0^1t^nP(t)^k\,d\rho(t).
\tag{1}
\]

For nonconstant real \(P\), its remainder at \(n=0\) tends to zero
if and only if \(\lVert P\rVert_{[0,1]}\le1\). Sufficiency follows
by dominated convergence, since the equality set is finite; necessity
uses positive even powers on an interval where \(|P|>1\).

## 2. A base-three filter with a purely dyadic cover

**Proved.** The polynomial

\[
P_3(t)=\frac{t-4}{4},\qquad P_3(16)=3,
\qquad -1\le P_3(t)\le-3/4\quad(0\le t\le1)
\]

gives the exact rational sequence

\[
H_k=(E-4)^kU_0
=\sum_{j=0}^k\binom kj(-4)^{k-j}U_j,
\qquad X_k=H_k/4^k,
\]

\[
\boxed{X_k=3^k\alpha-(-1)^kL_k},\qquad
L_k=\int_0^1(1-t/4)^k\,d\rho(t)>0.
\tag{2}
\]

Here \(L_k\to0\), and endpoint rescaling gives

\[
L_k\sim\frac{\Gamma(1/8)}{32}(4/k)^{1/8}.
\tag{3}
\]

For a proof, put \(t=4u/k\) near zero, where the density has the
displayed asymptotic and \((1-u/k)^k\to e^{-u}\). A fixed interval
away from zero has an exponentially small contribution. Bounds by a
constant times \(u^{-7/8}e^{-u}\) justify dominated convergence after
restricting to a sufficiently small fixed neighborhood of zero.

The rational recurrence and its forcing are

\[
H_{k+1}=12H_k+(E-4)^kr(1),
\]

\[
X_{k+1}=3X_k+\frac{(-1)^k}{4}J_k,
\qquad
J_k=\int_0^1(1-t/4)^k(16-t)\,d\rho(t)>0.
\tag{4}
\]

Thus the forcing is alternating and tends to zero; it is not the
original four-pole forcing. In fact \(J_k=12L_k+4L_{k+1}\).

### Exact positive remainder oracle

For \(a,k\ge0\), define the rational quantity

\[
J_{a,k}=\sum_{j=0}^k\binom kj(-1/4)^j r(a+j+1)
=\int_0^1t^a(1-t/4)^k(16-t)\,d\rho(t)>0.
\]

The positive denominator expansion gives, for every integer \(M\ge1\),

\[
\sum_{a=0}^{M-1}\frac{J_{a,k}}{16^{a+1}}
<L_k<
\sum_{a=0}^{M-1}\frac{J_{a,k}}{16^{a+1}}
+\frac{J_{M,k}}{15\,16^M}.
\tag{5}
\]

The inequalities follow from \(J_{a,k}\) decreasing in \(a\).
They are exact rational enclosures and require no cancellation model.

### Sharp minimum denominator and its rate tradeoff

**Proved, scoped to fixed rational polynomial filters.** Write
\(P=R/c\), \(R\in\mathbb Z[t]\), where \(c\ge1\) is the least
positive common denominator. Suppose \(P(16)=3\) and its absolute
moment remainder tends to zero. Then \(|R(0)|\le c\), while

\[
R(0)\equiv R(16)=3c\pmod {16}.
\]

For \(c=1,2,3\), the smallest possible absolute representatives of
\(3c\) modulo 16 are respectively \(3,6,7\), all greater than \(c\).
Therefore \(c\ge4\). The displayed linear \(P_3\) attains four.
It is also the unique admissible linear filter with common denominator
four: its integer numerator must be \(t-4\).

Every admissible denominator-four polynomial has \(R(0)=-4\), hence
\(P(0)=-1\). Consequently none has an exponentially decaying absolute
remainder along even orders. Indeed polynomial regularity gives
\(|P(t)|\ge1-Ct\) near zero. Integrating \(P(t)^{2k}\) over a small
interval \([0,c_0/k]\), where this power is bounded below, gives a
positive constant times \(k^{-1/8}\). The linear filter attains this
fastest possible power scale within the denominator-four class.
This statement does not classify growing-degree filter families or
arguments using cancellation modulo one.

The older \((E-1)/5\) filter has a faster absolute error
\(\asymp5^{-k}k^{-1/8}\), with a different cover. The new construction
trades that exponential accuracy for a smaller and purely dyadic cover;
it is not a uniform improvement in every metric.

## 3. Exact dyadic behavior of the quarter filter

Put \(A_j=\Delta^jU_0\). The Mahler coefficients of the sequence
\(H_k\), with differences now in \(k\), are

\[
B_j=\Delta_k^jH_0=(E-5)^jU_0=(\Delta-4)^jU_0
=\sum_{i=1}^j\binom ji(-4)^{j-i}A_i.
\]

For \(1\le i\le j\), the inherited profile and the factorial
valuation formula give

\[
v_2\!\left(\binom ji(-4)^{j-i}A_i\right)
=\nu(j)+s_2(j-i).
\tag{6}
\]

The unique least valuation is the term \(i=j\). Thus
\(v_2B_j=\nu(j)\), and \(v_2(B_j-A_j)\ge\nu(j)+1\) when the
difference is nonzero. The latter difference vanishes for \(j=1\).
The series \(\mathcal H(t)=\sum B_j\binom tj\) converges uniformly
on \(\mathbb Z_2\), agrees with \(H_k\) on nonnegative integers,
and has the same full uniform difference profile.

For completeness, Vandermonde's identity gives

\[
v_2\left(\binom{x+h}{j}-\binom xj\right)
\ge v_2(h)-\lfloor\log_2j\rfloor\quad(x,h\in\mathbb Z_2).
\tag{7}
\]

Indeed use \(\binom h\ell=(h/\ell)\binom{h-1}{\ell-1}\) in
the difference identity. Since
\(\nu(j)+1-\lfloor\log_2j\rfloor\ge2\) for \(j\ge2\),
\(\mathcal H-F\) is at most \(1/4\)-Lipschitz. The isometry of
\(F\) therefore proves that \(\mathcal H\) is an isometry too.
Its reductions modulo each \(2^b\) are permutations, so compactness
also proves surjectivity.

In particular,

\[
\boxed{v_2(H_k)=v_2(k),\qquad
v_2(X_k)=v_2(k)-2k\quad(k\ge1).}
\tag{8}
\]

The normalized ternary source has an actual growing dyadic denominator:
its reduced denominator contains exactly \(2^{2k-v_2(k)}\). The
construction has not made that information disappear.

For real circle readout, write \(H_k=C_k+x_k\), with integer \(C_k\)
and \(0\le x_k<1\). Then

\[
\{X_k\}=\left\{\frac{x_k+(C_k\bmod4^k)}{4^k}\right\}.
\tag{9}
\]

The modulus \(4^k\) is necessary and sufficient for universal readout
over unrestricted integer lifts of the same fractional part. Equation
(8) does not assert that all those lifts occur on the authentic source,
or that the real floor residues have any uniform conditional law.

## 4. A stronger ternary-power construction retaining the dyadic isometry

The exact polynomial

\[
P_{81}(t)=\frac{t^2-t+3}{3}
=1-\frac{t(1-t)}3
\]

satisfies

\[
P_{81}(16)=81=3^4,\qquad 11/12\le P_{81}(t)\le1
\quad(0\le t\le1).
\]

Consequently

\[
\boxed{Z_k=P_{81}(E)^kU_0=81^k\alpha-M_k},\qquad
M_k=\int_0^1P_{81}(t)^k\,d\rho(t)>0,
\tag{10}
\]

where \(M_k\to0\) and

\[
M_k\sim\frac{\Gamma(1/8)}{32}(3/k)^{1/8}.
\tag{11}
\]

The zero endpoint gives this term by the same rescaling as in (3).
The endpoint at one contributes \(O(k^{-2})\), and a fixed interior
interval contributes exponentially less. Both endpoints must be kept
in this argument, even though only one supplies the leading term.

The denominator three is the least possible among all fixed rational
polynomial filters with value 81 at 16 and vanishing absolute remainder.
If the common denominator is \(c\), then
\(|R(1)|\le c\) and \(R(1)\equiv81c\pmod {15}\). At \(c=1\)
the least absolute residue is 6; at \(c=2\) it is 3. Both are too
large. The displayed polynomial attains \(c=3\). No linear polynomial
with denominator three can work; at degree two the endpoint conditions
force \(R(0)=R(1)=3\), whence \(R(t)=a t(t-1)+3\), and evaluation
at 16 forces \(a=1\). Thus it is the unique minimum-degree example
at the minimum denominator.

### Positive rational forcing and exact diagonal beta moments

There is a useful factorization at the actual source multiplier:

\[
P_{81}(E)-81=(E-16)(E+15)/3.
\]

Consequently the derived source has a positive rational recurrence

\[
Z_{k+1}=81Z_k+b_k,\qquad
b_k=\frac13\left[P_{81}(E)^k(r(n+2)+15r(n+1))\right]_{n=0}
=\int_0^1(81-P_{81}(t))P_{81}(t)^k\,d\rho(t)>0.
\]

This is a Hausdorff-moment sequence with moment variable
\(P_{81}(t)\in[11/12,1]\). In particular every finite difference
has the completely monotone sign. Using the inherited positive forcing
moments \(D_{a,j}=\int t^a(1-t)^j(16-t)\,d\rho(t)\), its exact
Newton coefficients are

\[
\boxed{(-1)^j\Delta^jb_0
=3^{-j-1}\left(15D_{j,j}+D_{j+1,j}\right)>0.}
\]

This follows from \(1-P_{81}(t)=t(1-t)/3\) and
\(81-P_{81}(t)=(16-t)(t+15)/3\). The available rational beta
oracle evaluates both terms without an approximation to pi. A simple
all-order bound is

\[
0<(-1)^j\Delta^jb_0
<\frac{16r(1)}3\,12^{-j}.
\]

Here \(t(1-t)\le1/4\) and \(t+15<16\) on the interval interior.
Also \(b_k=81M_k-M_{k+1}\sim80M_k\), and the exact convergent
positive series is \(\alpha=\sum_{k\ge0}b_k/81^{k+1}\).
These are source and moment theorems, not digit-frequency estimates.

### Full dyadic profile, now for the normalized source itself

The decisive algebraic identity is

\[
P_{81}(E)-1=\frac{E\Delta}{3}.
\]

Thus this is literally a weighted Pascal transform of the diagonal of
the original difference table:

\[
Z_k=\sum_{j=0}^k\binom kj3^{-j}\Delta^jU_j.
\]

On the exponential signal, \(\Delta^j16^j=240^j\), so the row
sum becomes \(\sum_j\binom kj80^j=81^k\). On the moment kernel,
the same diagonal operator acts as \(-t(1-t)\); its new Pascal
factor is precisely \(1-t(1-t)/3\). This accounts for the different
behavior on the growing signal and on its real error.

Therefore the Mahler coefficients of \(Z_k\) are exactly

\[
\boxed{C_j=\Delta_k^jZ_0=3^{-j}\Delta^jU_j.}
\tag{12}
\]

The uniform inherited theorem gives \(v_2C_j=\nu(j)\). The
interpolation \(G(t)=\sum_{j\ge0}C_j\binom tj\) hence satisfies

\[
G(0)=0,\quad G(k)=Z_k,\quad
v_2(\Delta^jG(t))=\nu(j)
\quad(t\in\mathbb Z_2,j\ge1).
\tag{13}
\]

To prove the last equality, use
\(\Delta^jG(t)=\sum_{i\ge j}C_i\binom t{i-j}\).
The first term has strictly smallest valuation because \(\nu\)
strictly increases. Also \(C_1\) is odd and, for \(j\ge2\),
\(\nu(j)-\lfloor\log_2j\rfloor\ge1\). Equation (7) shows that
\(G(t)-C_1t\) is strictly contracting. Thus \(G\) is a bijective
isometry of \(\mathbb Z_2\), and

\[
\boxed{v_2(Z_k)=v_2(k)\quad(k\ge1).}
\tag{14}
\]

This is an exact dyadic chart for a ternary-power source. In particular
\(G\circ F^{-1}\) is a dyadic isometry relating the two source charts.
No real continuity or same-law circle transport is inferred for that map.

### A reusable preservation lemma

The preceding argument generalizes. Let
\(P\in\mathbb Q[t]\cap\mathbb Z_2[t]\) satisfy
\(P(1)=1\) and \(P'(1)\in\mathbb Z_2^\times\).
Then \(P(1+\Delta)-1=a\Delta+\Delta^2S(\Delta)\), with \(a\)
odd and all coefficients dyadically integral. For
\(V_k=P(E)^kU_0\), its \(j\)-th Newton coefficient is
\((P(E)-1)^jU_0\). The unique smallest-valuation term in its
expansion in \(A_i\) is \(a^jA_j\). Hence it has valuation
\(\nu(j)\), and the entire normalized interpolation is again a
bijective isometry with full profile (13). A real orbit shadow follows
only when the separate condition \(\lVert P\rVert_{[0,1]}\le1\)
holds. The lemma proves both bridges for \(P_{81}\).

### Arithmetic and window costs

Put \(K_k=(E^2-E+3)^kU_0\), so \(Z_k=K_k/3^k\). Its readout
from \(\{K_k\}\) needs \(\lfloor K_k\rfloor\bmod3^k\) for
unrestricted compatible integer lifts. The construction reads \(2k+1\)
original source values, and the coefficient norm of \(P_{81}^k\)
is exactly \((5/3)^k\): coefficients alternate by degree, so evaluate
the absolute coefficient sum at \(t=-1\).

At the same ternary depth \(4k\), iterating the quarter filter needs
\(4k+1\) inputs, cover \(4^{4k}\), and coefficient norm
\((5/4)^{4k}\). The base-81 filter uses half as many shifts and
cover \(3^k\), while its asymptotic absolute error is larger only by
the factor \(3^{1/8}\). The covers contain different prime information;
this comparison does not assert any source carry is uniformly distributed.

For a translated source index, a fixed two-shift transport obeys

\[
\frac{U_{n+2}-U_{n+1}+3U_n}{3}
=81U_n+5r(n+1)+r(n+2)/3.
\tag{15}
\]

Its discrepancy from multiplication by 81 is \(O(n^{-2})\).
The analogous one-shift quarter-filter identity is

\[
\frac{U_{n+1}-4U_n}{4}=3U_n+r(n+1)/4.
\tag{16}
\]

These prove approximations to the **pushforward** of an input empirical
law. They do not prove that this pushforward equals the input law.

## 5. Positive Pascal filters for every prime, with an exact dyadic differential

There is also a direct family that answers the bounded-differential
question precisely. Fix an integer \(q\ge2\), and choose an **odd**
integer \(d\ge1\) with \(q\le16^d\). Set

\[
a=\frac{q-1}{16^d-1},\qquad
P_{q,d}^{+}(t)=1+a(t^d-1),\qquad
Y_k=(P_{q,d}^{+}(E))^kU_0.
\]

Here \(0<a\le1\), \(P_{q,d}^{+}(16)=q\), and
\(0\le P_{q,d}^{+}(t)\le1\) on the unit interval. Thus

\[
Y_k=q^k\alpha-N_k,\qquad
N_k=\int_0^1(1-a+at^d)^k\,d\rho(t)>0,
\]

\[
N_k\sim\frac1{64a^2d^2k^2}.
\tag{19}
\]

For the asymptotic, the only maximum of the kernel is at \(t=1\),
where \(P(t)=1-ad(1-t)+O((1-t)^2)\) and
\(w(t)\sim(1-t)/64\). The same endpoint rescaling as above proves
the statement. This includes \(a=1\), whose moment is \(T_{dk}\).

The whole transform is a positive, normalized Pascal row:

\[
Y_k=\sum_{j=0}^k\binom kj a^j(1-a)^{k-j}U_{dj}.
\tag{20}
\]

Its coefficient norm is exactly one, at every order. It does not
amplify an a priori uniform error in compatible real input lifts.
Taking the fractional part after this rational average still requires
the compatible lift information; averaging raw values is distinct
from averaging their empirical laws.

### The all-parameter dyadic theorem

Write \(\delta=v_2(q-1)\). The odd denominator of \(a\) gives
\(v_2(a)=\delta\). The Newton coefficients of \(Y_k\) are

\[
C_j^{q,d}=a^j(E^d-1)^jU_0.
\]

Because \(d\) is odd,
\(E^d-1=d\Delta+\Delta^2S(\Delta)\) has an odd leading
coefficient and all other coefficients dyadically integral. The
unique minimum-valuation term in \((E^d-1)^jU_0\) is \(d^jA_j\).
Consequently

\[
\boxed{v_2(C_j^{q,d})=\nu(j)+j\delta.}
\tag{21}
\]

Let \(\mathcal Y_{q,d}(z)=\sum C_j^{q,d}\binom zj\).
This defines an analytic interpolation on \(\mathbb Z_2\), agrees
with \(Y_k\) at every nonnegative integer, and has the exact global
distance law

\[
\boxed{v_2(\mathcal Y_{q,d}(x)-\mathcal Y_{q,d}(y))
=v_2(x-y)+\delta\quad(x\ne y\in\mathbb Z_2).}
\tag{22}
\]

For the proof, \(2^{-\delta}C_1^{q,d}\) is odd, and the higher
coefficients, divided by \(2^\delta\), satisfy the strict
Lipschitz bound following (7). Thus \(2^{-\delta}\mathcal Y_{q,d}\)
is a bijective isometry of \(\mathbb Z_2\). In particular the
image of \(\mathcal Y_{q,d}\) is exactly \(2^\delta\mathbb Z_2\).

There is a literal differential statement as well:

\[
\boxed{v_2(\mathcal Y_{q,d}'(z))=\delta
\quad\text{for every }z\in\mathbb Z_2.}
\tag{23}
\]

Indeed
\(v_2(C_j^{q,d}/j!)=(\delta+1)j-1\).
Writing each binomial polynomial in falling-factorial form shows
uniform convergence of its differentiated series. The \(j=1\)
derivative has valuation \(\delta\); every \(j\ge2\)
contribution has valuation at least \(1+2\delta\), so it cannot
cancel the first one. The same coefficient estimate also supplies
analytic convergence on a dyadic ball of radius strictly larger than
one. These are exact metric and derivative statements, not a claim
that the original real and dyadic topologies are interchangeable.

### Base three and the primes below sixteen

For \(q=3,d=1\),

\[
P_{3,1}^{+}(t)=\frac{2t+13}{15},\qquad
Y_k=\sum_{j=0}^k\binom kj(2/15)^j(13/15)^{k-j}U_j,
\]

\[
Y_k=3^k\alpha-N_k,\qquad N_k\sim\frac{225}{256k^2},
\qquad v_2(Y_k)=v_2(k)+1.
\]

Thus \(\mathcal Y_{3,1}/2\) is a dyadic isometry, and the
unnormalized derivative has dyadic absolute value exactly \(1/2\)
everywhere. This avoids the divergent dyadic denominators of the
quarter filter. The price is a denominator-15 filter, whose compatible
integer-lift cover grows as \(15^k\).

More generally, when \(d=1\) its reduced denominator is
\(15/\gcd(q-1,15)\). All primes below sixteen have the following
exact data:

| Prime \(q\) | \(\delta=v_2(q-1)\) | Dyadic distance factor | Filter denominator |
| --- | --- | --- | --- |
| 2 | 0 | 1 | 15 |
| 3 | 1 | \(1/2\) | 15 |
| 5 | 2 | \(1/4\) | 15 |
| 7 | 1 | \(1/2\) | 5 |
| 11 | 1 | \(1/2\) | 3 |
| 13 | 2 | \(1/4\) | 5 |

The finite prime list therefore has a uniform distortion bound of four
within this construction. Arbitrarily large primes are reached by an
odd \(d\); the distortion \(2^{v_2(q-1)}\) is explicit but is
not asserted uniformly bounded over all primes.

For \(d=1\) the derived forcing is particularly simple:

\[
Y_{k+1}=qY_k+b_k,\qquad b_k=aP_{q,1}^{+}(E)^kr(1)>0,
\qquad (-1)^j\Delta^jb_0=a^{j+1}D_{0,j}>0.
\]

For general odd \(d\), positivity follows from
\(q-P_{q,d}^{+}(t)=a(16^d-t^d)>0\), and the forcing is again
a rational Hausdorff-moment sequence. The full construction applies
to every positive-kernel source with the inherited dyadic profile,
including the prescribed-constant countermodels. Hence the proved
bounded differential alone cannot imply a digit-frequency theorem.

The affine filters are not asserted to form a multiplicatively coherent
family in \(q\): generally \(P_p^+P_q^+\ne P_{pq}^+\). Their
commuting products do yield source shadows for the product bases, but
the precise differential formula (21)--(23) was proved for each
designated affine filter, not automatically for every product. Likewise
the diagonal base-81 construction is a different source from four
iterations of an affine base-three filter.

## 6. Why naive binary deblocking does not give a free integer filter

There is an authentic rational binary deblocking

\[
B_{4n+s}=2^sU_n\quad(0\le s<4),\qquad
B_m=2^m\alpha-\tau_m,\qquad
\tau_{4n+s}=2^sT_n.
\]

It is tempting to apply \((E+1)^k\) to get \(3^k\), or apply
\((2E-1)^k\) because the scalar polynomial \(2t-1\) is bounded
on \([0,1]\). But the deblocked tail is not a scalar positive
Hausdorff-moment tail in the binary index.

Here is the exact failure mechanism. At a fixed \(t\in(0,1]\), put
\(x=t^{1/4}\). The kernel sequence \(a_{4n+s}(t)=2^st^n\) has
four eigenbranches \(\lambda=\zeta x\), \(\zeta^4=1\), with

\[
a_m(t)=\sum_{\zeta^4=1}c_\zeta(x)(\zeta x)^m,
\qquad
c_\zeta(x)=\frac14\sum_{s=0}^3(2/x)^s\zeta^{-s}.
\]

At \(t=1\), the positive branch has coefficient \(15/4\), and
the negative branch has coefficient \(-5/4\). Applying the two
filters and using the density at \(t=1\) gives

\[
3^k\alpha-(E+1)^kB_0
\sim\frac{15}{4}\frac{2^k}{k^2},
\tag{17}
\]

\[
3^k\alpha-(2E-1)^kB_0
\sim-\frac{45}{64}\frac{(-3)^k}{k^2}.
\tag{18}
\]

For (17), the positive branch has
\(1+t^{1/4}=2-(1-t)/4+O((1-t)^2)\). For (18), the dominant
negative branch has
\(-1-2t^{1/4}=-3+(1-t)/2+O((1-t)^2)\). The elementary
endpoint integral \(\int_0^\infty u e^{-au}\,du=a^{-2}\)
gives the constants above. All other branches have strictly smaller
exponential modulus at this endpoint.

The apparent singularities of \(c_\zeta(x)\) at zero are not
integrated separately there. On \(0\le t\le\varepsilon\), use
the original kernel bound
\(a_j(t)\le8\varepsilon^{-3/4}\varepsilon^{j/4}\).
The absolute Pascal sums are then bounded by a constant times
\((1+\varepsilon^{1/4})^k\), respectively
\((1+2\varepsilon^{1/4})^k\). Each is exponentially smaller
than its claimed dominant branch for fixed \(\varepsilon<1\).

Both remainders grow in absolute value. This refutes the proposed
vanishing-absolute-error arguments. It makes no claim about the
fractional parts of those growing remainders.

## 7. Controls, verification, and the remaining statistical obligation

The filter algebra remains valid for any positive Hausdorff tail,
including the prior rational source
\(T_n^*=2C/[(n+1)(n+2)]\),
\(U_n^*=16^nC-T_n^*\), with \(C>0\) rational. For \(C=1/15\),
the original circle law tends to \(\delta_{1/15}\), whereas the
base-81 filter law tends to \(\delta_{2/5}\). Thus positive kernels,
exact ternary filters, and small absolute errors do not supply
same-law invariance. The stronger inherited prescribed-constant
countermodels can preserve the full dyadic profile as well; the
preservation lemma then applies to those alternative sources.

Read-only exact rational calculations in this lane checked
\(v_2(H_k)=v_2(k)\) through order 80, and both the base-81 valuations
and its Newton coefficients on smaller ranges. A separate exact replay
checked its forcing-difference identity at orders 0 through 18, its
strict positive bound at those orders, and its source Newton identity
at orders 1 through 19. The affine prime-family replay used
\(q=2,3,5,7,11,13,17,31,257,65537\), with the smallest allowed odd
\(d\). It checked 120 literal Newton identities, 120 exact Newton
valuations, and 1,710 exact distance identities among indices 0 through
18. These finite checks
calibrate the formulas; the infinite claims rest on the proofs above.
Exploratory high-precision checks of (17) and (18), at
\(k=20,40,80,120,200,300\), approach constants \(15/4\) and
\(-45/64\). Those decimal observations are not proof certificates.
No full-suite or hosted-CI result is asserted by this lane.

The diagonal construction (10)--(14) supplies an explicit
rational base-81 shadow of the actual constant, with a positive
absolute-error kernel, minimum denominator three, and the entire
authentic dyadic isometry profile. Its low-degree formula gives a
concrete real transport to test in (15). If the same selected window
laws became invariant under 81, the inherited positive-collision-
dimension rigidity route could use the coprime pair 16 and 81.
The affine family (19)--(23) supplies a complementary exact result:
positive normalized Pascal filters in every prime base, with explicit
global dyadic distance distortion and literal derivative valuation.
Neither identifies its real empirical law with the original one.
That invariance and the all-scale real collision estimate remain
separate, unproved requirements. The construction is a genuine
source theorem and an improved instrument; it is not a normality proof.
