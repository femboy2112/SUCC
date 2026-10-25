# Pascal filters for base 3, a base-81 source, and sharp denominator costs

**Date:** 2026-10-24. **Inherited head:**
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3` (draft #272).
**Status:** paper proofs and exact finite calibration. Real carry retention,
same-law multiplication-by-81 invariance, and pi normality remain **OPEN**.
No scholarly priority or new formal-checker authority is asserted.

## 1. Contract, notation, and the actual advance

The question is whether the elementary weighted Pascal identity

\[
\sum_{j=0}^k\binom{k}{j}2^j=3^k
\]

can improve a source construction, rather than merely rename an unknown
distribution theorem. The precise subproblem here is to minimize the
division needed by a fixed rational polynomial filter of the authentic
BBP source while retaining a vanishing **absolute real** error. A second
subproblem asks whether a power of 3 admits a filter preserving the full
dyadic source geometry.

Use the inherited objects and proofs in
[the real-kernel dossier](PI_PASCAL_REAL_KERNEL.md) and
[the dyadic dossier](PI_PASCAL_MAHLER_SOURCE.md):

\[
\alpha=\pi/16,\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1),
\quad U_n=16^n\alpha-T_n,
\]

\[
T_n=\int_0^1t^n\,d\rho(t),\qquad
w(t)=\frac{d\rho}{dt}
\sim\frac1{32}t^{-7/8}\ (t\downarrow0),\quad
w(t)\sim\frac{1-t}{64}\ (t\uparrow1).
\]

The positive finite measure has full support and no atoms. Its mass is
\(\alpha\). With \(E\) the shift in the authentic source index,

\[
P(E)^kU_n=P(16)^k16^n\alpha-
\int_0^1t^nP(t)^k\,d\rho(t).
\tag{1}
\]

For a fixed nonconstant real polynomial, the last integral at \(n=0\)
tends to zero exactly when \(\|P\|_{[0,1]}\leq1\). Necessity uses the
nonnegative even moments; sufficiency is dominated convergence.

The authentic dyadic interpolation \(F\) has \(F(n)=U_n\) and, for
every \(j\geq1\) and \(z\in\mathbb Z_2\),

\[
v_2(\Delta^jF(z))=\nu(j):=j-1+v_2(j!)=2j-s_2(j)-1.
\tag{2}
\]

The additions proved below are:

- Denominator 4 is the smallest for a fixed filter reaching base 3;
  denominator 5 is the smallest allowing exponential absolute decay,
  and the earlier denominator-5 filter is rate-optimal at that denominator.
- Allowing the fourth power of 3 lowers the denominator to 3, which is
  globally minimal over **all positive powers of 3** in this mechanism.
- The resulting degree-two filter reaches base 81 and preserves (2),
  including a bijective dyadic isometry, at its zero initial condition.
- Translating the authentic source by two entries and resetting its
  initial value restores quadratic real decay without losing that
  dyadic source profile.
- The finite-window statistical target can use multiplication by 81,
  a strictly weaker invariance than tripling, with a three-sheet local
  readout. The required statistical equality is not proved.

This is a construction and a sharp arithmetic tradeoff, not a proved
improvement in a real collision exponent. The adversarial boundary in
Section 8 is part of the result.

## 2. Sharp denominator and rate tradeoff for base 3

Write \(P=A/b\), where \(A\in\mathbb Z[t]\), \(b\geq1\), and \(b\)
is the least positive integer clearing all coefficients. Suppose
\(P(16)=3\) and \(\|P\|_{[0,1]}\leq1\). Then

\[
A(0)\equiv3b\pmod {16},\qquad |A(0)|\leq b.
\tag{3}
\]

For \(b=1,2,3\), the distance from \(3b\) to \(16\mathbb Z\) is
respectively 3, 6, 7, greater than \(b\). Hence \(b\geq4\), in every
polynomial degree. Equality is attained by

\[
P_4(t)=\frac{t-4}{4},\qquad
X_k=P_4(E)^kU_0
=3^k\alpha-(-1)^k\int_0^1(1-t/4)^k\,d\rho(t).
\tag{4}
\]

Its absolute error tends to zero, with

\[
|X_k-3^k\alpha|
\sim\frac{\Gamma(1/8)}{32}\left(\frac4k\right)^{1/8}.
\tag{5}
\]

This improves the universal division label from \(5^k\) to \(4^k\),
but sacrifices the earlier exponential error rate. There is a sharp reason.
At denominator 4, (3) forces \(P(0)=-1\). For every such fixed polynomial,
\(|P(t)+1|\leq Lt\) near zero for a fixed \(L>0\). On a sufficiently
short interval of length \(c/k\), \(|P(t)|^{2k}\) is bounded below by a
positive constant. Since \(w(t)\gg t^{-7/8}\),

\[
\int_0^1P(t)^{2k}\,d\rho(t)\gg_P k^{-1/8}.
\tag{6}
\]

Therefore no fixed denominator-4 filter has exponentially decaying
absolute error. If the first nonzero term of \(P(t)+1\) has degree \(m\),
the endpoint itself contributes a positive multiple of
\(k^{-1/(8m)}\); a flatter endpoint makes that part slower.

For denominator 5, (3) instead forces \(P(0)=-1/5\), so
\(\|P\|_{[0,1]}\geq1/5\). For every continuous real \(P\) on the full
support of \(\rho\),

\[
\limsup_{k\to\infty}
\left|\int P(t)^k\,d\rho(t)\right|^{1/k}
=\|P\|_{[0,1]}.
\tag{7}
\]

The upper bound is immediate. For the lower bound, use even powers and
a positive-mass neighborhood where \(|P|\) is close to its maximum.
The previous filter \(P_5(t)=(t-1)/5\) attains \(\|P_5\|=1/5\).
Thus denominator 5 is the smallest that permits exponential decay, and
its exponential rate \(1/5\) is optimal over **all fixed polynomial
degrees at that denominator**. This does not assert a unique optimizer.

There is also an exact dyadic cost to (4). Put
\(H_k=(E-4)^kU_0\). Then, for every integer \(k\geq1\),

\[
v_2(H_k)=v_2(k),\qquad v_2(X_k)=v_2(k)-2k.
\tag{8}
\]

Indeed expand \((\Delta-3)^kF(0)\). The term with one difference has
valuation \(v_2(k)\). For \(j\geq2\),
\(v_2\binom{k}{j}\geq v_2(k)-v_2(j)\), while
\(\nu(j)-v_2(j)\geq1\). The one-difference term is the unique minimum.
The zero-difference term vanishes because \(F(0)=0\).

All minimality claims in this section concern a fixed scalar polynomial
filter and a vanishing absolute real moment error. Degree-varying filters,
matrix filters, source-specific recovery of carries, and cancellation
modulo 1 are outside the lower bounds.

## 3. A degree-two Pascal filter for \(81=3^4\)

The better block construction is

\[
\boxed{P(t)=1+\frac{t(t-1)}3,\qquad P(16)=81.}
\tag{9}
\]

On \([0,1]\),
\(11/12\leq P(t)\leq1\), with equality 1 only at the endpoints.
Consequently the rational zero-initial source

\[
\boxed{Z_k=P(E)^kU_0=81^k\alpha-M_{0,k},\qquad
M_{n,k}=\int_0^1t^nP(t)^k\,d\rho(t)>0}
\tag{10}
\]

has \(M_{0,k}\to0\). The Pascal expansion is explicit:

\[
Z_k=\sum_{j=0}^k\binom{k}{j}3^{-j}\Delta^jU_j.
\tag{11}
\]

It reads \(2k+1\) authentic source entries. The integral numerator
operator is \(E^2-E+3\), so a universal phase readout of its \(k\)-th
power divided by \(3^k\) retains an integer lift modulo \(3^k\).
This assertion is about unrestricted lifts; it does not say every label
occurs along the actual source.

### Denominator 3 is globally minimal among powers of 3

Suppose a fixed admissible \(A/b\) has \(P(16)=3^m\), with \(m\geq1\).
Then

\[
A(1)\equiv b3^m\pmod {15},\qquad |A(1)|\leq b.
\tag{12}
\]

For \(b=1\) or 2, the residue is divisible by 3 and nonzero modulo 5.
No integer of magnitude at most 2 has those two properties. Thus no
positive power of 3 is possible at denominator 1 or 2. Equation (9)
attains denominator 3, proving the global minimum in this mechanism.

At denominator 3, the two endpoint conditions together force
\(m\equiv0\pmod4\). The condition modulo 15 first forces \(m\) even;
when \(m\equiv2\pmod4\), the residue \(3^{m+1}\equiv11\pmod {16}\)
has no representative in \([-3,3]\). For \(m\equiv0\pmod4\), both
endpoints are forced to equal 3 for \(A\), hence 1 for \(P\).
This proves a necessary condition; it does not assert that every such
power is attained with denominator 3. The first possible exponent,
\(m=4\), is attained by (9).

### An explicit error bound using existing rational oracles

For \(0\leq t\leq1/2\),

\[
P(t)^8\leq1-t.
\tag{13}
\]

To prove this, differentiate \(\log(P(t)^8/(1-t))\). Its derivative
has the sign of \(-15t^2+23t-5\), which increases strictly on this
interval and changes sign once. Thus the quotient's maximum is at an
endpoint. Its endpoint values are 1 and \(2(11/12)^8<1\). Symmetry
gives \(P(t)^8\leq t\) on the other half. The integer exponent 8 is
smallest for this particular inequality: it fails at \(t=1/2\) for
every exponent at most 7.

For \(a=\lfloor k/8\rfloor\), splitting the integral at \(1/2\) gives

\[
0<M_{n,k}<R_{n,a}+T_{n+a}
<\frac{D_{n,a}}{15}
+\frac1{(8(n+a)+1)(8(n+a)+2)}.
\tag{14}
\]

Here \(D_{n,a}\) and \(R_{n,a}\) are the inherited positive beta and
tail-difference moments, with exact rational enclosures. The estimate
holds for every integer \(n,k\geq0\); it requires no asymptotic guess.

For fixed \(n\), endpoint rescaling gives the sharper leading behavior

\[
M_{n,k}\sim
\begin{cases}
\displaystyle\frac{\Gamma(n+1/8)}{32}
\left(\frac3k\right)^{n+1/8},&n=0,1,\\[6pt]
\displaystyle\frac9{64k^2},&n\geq2.
\end{cases}
\tag{15}
\]

At zero, \(P(t)=1-t/3+O(t^2)\) and
\(t^nw(t)\sim t^{n-7/8}/32\). At one, writing \(s=1-t\),
\(P(t)=1-s/3+O(s^2)\) and \(t^nw(t)\sim s/64\).
Separate small endpoint neighborhoods from a compact interior interval,
where \(P\leq1-\epsilon\), and use these expansions with dominated
Laplace rescaling. The first endpoint dominates for \(n=0,1\); the
second dominates for \(n\geq2\). No jointly growing \(n,k\) asymptotic
is asserted.

## 4. The base-81 source preserves the complete dyadic source profile

This is more than equality of a few residues. From (11), its Newton
coefficients are exactly

\[
B_j=\Delta_k^jZ_0=3^{-j}\Delta^jU_j,\qquad
v_2(B_j)=\nu(j)\quad(j\geq1),\qquad B_0=0.
\tag{16}
\]

Therefore

\[
G(z)=\sum_{j\geq0}B_j\binom zj
\tag{17}
\]

converges uniformly on \(\mathbb Z_2\), interpolates every \(Z_k\),
and satisfies

\[
\boxed{v_2(\Delta^jG(z))=\nu(j)
\quad(j\geq1,\ z\in\mathbb Z_2).}
\tag{18}
\]

Indeed
\(\Delta^jG(z)=\sum_{\ell\geq0}B_{j+\ell}\binom z\ell\).
The \(\ell=0\) term has valuation \(\nu(j)\); every later term has
strictly greater valuation. The coefficients of the falling-factorial
series have valuation \(v_2(B_j/j!)=j-1\), so the series is also analytic
on the open dyadic disk \(|z|_2<2\).

The interpolation is a **bijective isometry** of \(\mathbb Z_2\).
For \(h\ne0\), the translated Newton identity gives

\[
G(z+h)-G(z)=\sum_{j\geq1}\binom hj\Delta^jG(z).
\]

The first term has valuation \(v_2(h)\). For \(j\geq2\),
\(v_2\binom hj\geq v_2(h)-v_2(j)\) and
\(\nu(j)-v_2(j)\geq1\), so all other terms have strictly larger
valuation. Thus \(v_2(G(z+h)-G(z))=v_2(h)\). Each induced finite
residue map is injective and hence bijective; compactness gives
surjectivity on \(\mathbb Z_2\).

### General filter criterion behind this preservation

The same argument works for any
\(P\in\mathbb Z_{(2)}[t]\) such that

\[
P(1)=1,\qquad P'(1)\in\mathbb Z_2^\times.
\tag{19}
\]

Write \(P(t)-1=(t-1)Q(t)\). Then \(Q(1)\) is odd, and

\[
\Delta_k^j[P(E)^kF(0)]_{k=0}
=\Delta^jQ(E)^jF(0).
\]

Expanding \(Q(E)^j\) around \(E=1\), its constant term is odd and all
other coefficients are dyadically integral. Equation (2) supplies a
unique term of valuation \(\nu(j)\). Equations (17)-(18) then apply.
The real requirements \(P(16)=q\) and \(|P|\leq1\) are independent
additional conditions. Our base-81 filter meets all of them.

**Scope:** (18) preserves the dyadic **source** profile. It does not
assert that the new forcing has the original forcing profile. If
\(s(k)=G(k)-81G(k-1)\), then

\[
\Delta^js(k)=\Delta^{j+1}G(k-1)-80\Delta^jG(k-1),
\]

whose two valuations can compete. Its real decay at the untranslated
origin is \(k^{-1/8}\), not the original quadratic rate.

## 5. Two authentic source shifts restore quadratic forcing decay

For a fixed integer \(n\geq0\), define a zero-initial rational source

\[
S_k^{(n)}=P(E)^kU_n-81^kU_n
=81^kT_n-M_{n,k},\qquad S_0^{(n)}=0.
\tag{20}
\]

Its forcing is

\[
S_{k+1}^{(n)}-81S_k^{(n)}
=\int_0^1t^n(81-P(t))P(t)^k\,d\rho(t)>0.
\tag{21}
\]

Every signed finite difference of the right side is positive, since
\(0<P(t)\leq1\). Its extension to real \(k\geq0\) is completely
monotone, by differentiation under this compactly supported Laplace
integral. For each fixed \(n\geq2\), (15) gives

\[
M_{n,k}\sim\frac9{64k^2},\qquad
S_{k+1}^{(n)}-81S_k^{(n)}\sim\frac{45}{4k^2}.
\tag{22}
\]

The full dyadic source profile survives the reset. Its Newton coefficients
for \(j\geq1\) are

\[
3^{-j}\Delta^jU_{n+j}-80^jU_n.
\tag{23}
\]

The first term has valuation \(\nu(j)\); the second has valuation at
least \(4j>\nu(j)\), because \(U_n\in\mathbb Z_2\). Thus (17)-(18)
and the bijective isometry proof apply to (20) as well.

For \(n=2\), the represented constant is explicitly

\[
T_2=16\pi-\frac{205826}{4095}.
\tag{24}
\]

It has the same base-81 normality status as pi: rational addition and
nonzero rational multiplication preserve normality in a fixed base,
and the inverse affine map is rational too. A primary proof is
Doty--Lutz--Nandakumar, *Finite-State Dimension and Real Arithmetic*,
[Theorem 4.3 and Corollary 4.4](https://web.cs.ucdavis.edu/~doty/papers/fsdra.pdf).
That theorem does **not** identify the selected empirical laws of the
two rational-affine related constants. Base 81 and base 3 normality are
equivalent by the usual power-of-base theorem.

## 6. A smaller local cover and a weaker symmetry target

For every integer \(n\geq0\), the original recurrence gives

\[
\boxed{
\frac{U_{n+2}-U_{n+1}+3U_n}{3}
=81U_n+5r(n+1)+\frac{r(n+2)}3.}
\tag{25}
\]

This reads three consecutive source states, spanning two source shifts.
Let \(\mu_I\) be the original phase law on a window beginning at \(A\),
and let \(\nu_I\) be the empirical law of the left side modulo 1.
The exact coupling and monotonicity of the forcing imply

\[
W_1(\nu_I,(T_{81})_*\mu_I)
\leq5r(A+1)+\frac{r(A+2)}3=O(A^{-2}).
\tag{26}
\]

The two additional source entries at the window end must be supplied,
or the shortened-window endpoint cost retained.

The local numerator \(H=U_{n+2}-U_{n+1}+3U_n=C+x\), where
\(C\in\mathbb Z\) and \(0\leq x<1\), has readout

\[
\{H/3\}=\frac{x+(C\bmod3)}3.
\tag{27}
\]

Thus a local symmetry test needs a fixed three-sheet label. Repeated
filtering still needs the \(3^k\) label described above. At \(n=0\),
\(Z_1=38599/2457\); dropping the numerator carry gives \(106/2457\).
Their circle discrepancy is \(1/3\) (their canonical phases differ
by \(2/3\)). The exact carry is essential to a universal readout.

The missing target is

\[
W_1(\nu_I,\mu_I)\longrightarrow0
\tag{28}
\]

on the same selected authentic windows. By (26), this is the new
\(T_{81}\)-invariance condition. It is not established by the filter.

It is a strictly weaker invariance than \(T_3\)-invariance, even among
\(T_{16}\)-invariant measures: \(\delta_{1/5}\) is fixed by both 16
and 81, but multiplication by 3 sends it to \(\delta_{3/5}\).
Since 16 and 81 are coprime, the inherited positive-all-scale-collision
rigidity route can use 81 directly. No inference from \(T_{81}\)
invariance alone to \(T_3\) invariance is made. The precise nonergodic
Rudolph--Johnson input is stated as Theorem 1.3 in
[Bourgain--Lindenstrauss--Michel--Venkatesh](https://www.math.ias.edu/~akshay/research/blmv.pdf);
positive entropy alone gives a Haar component, so the inherited
all-scale condition and residual argument must still be retained.

## 7. Two structural extensions with sharply limited meanings

### 7.1 The positive filter is a quadratic norm linking 3 and 16

Let \(\omega=(1+i\sqrt{11})/2\). Then
\(\omega+\overline\omega=1\),
\(\omega\overline\omega=3\), and
\(\omega^2=\omega-3\). Repeated multiplication gives
\(\omega^5=15+\omega\), hence
\(16-\omega=\overline\omega^{\,5}\). Therefore

\[
P(t)=\frac{(t-\omega)(t-\overline\omega)}3,
\qquad
P(16)=\frac{3^5}{3}=3^4.
\tag{29}
\]

The conjugate commuting linear filters
\((E-\omega)/\overline\omega\) and
\((E-\overline\omega)/\omega\) multiply to \(P(E)\).
Their multipliers at 16 are \(\overline\omega^4\) and \(\omega^4\),
each of complex modulus 9. This explains the real positivity and the
power-of-three value algebraically. It supplies no equidistribution,
independence, or irrational-rotation theorem for the selected source.

### 7.2 An integer base-31 filter can preserve the source profile too

For comparison, the following degree-six integer polynomial passes both
the real and dyadic tests:

\[
P_{31}(t)=2t-1-t^4(t-1)(t-16),
\quad P_{31}(16)=31,\quad P_{31}(1)=1,\quad P'_{31}(1)=17.
\tag{30}
\]

On \([0,1]\), the subtracted term is nonnegative, so \(P_{31}\leq1\).
Also

\[
P_{31}(t)+1=t\,[2-t^3(1-t)(16-t)]\geq\frac5{16}t\geq0,
\]

using \(t^3(1-t)\leq27/256\). Hence \(|P_{31}|\leq1\), and
the general criterion (19) gives a base-31 source with the complete
dyadic source profile and no division-cover label. It uses six source
shifts per iterate. The earlier degree-one filter \(2E-1\) already
reached base 31, but its Newton coefficient valuations are
\(\nu(j)+j\), not \(\nu(j)\). The new fact here is compatibility of
the real filter and the unchanged dyadic profile, not a new base-31
normality result or an improved local transport estimate.

## 8. Adversarial boundary and next useful experiment

The prescribed-constant construction in
[the inherited countermodel dossier](PI_PASCAL_PRESCRIBED_CONSTANT.md)
can use \(C=1/5\), while retaining the dyadic source profile and a
positive real moment tail. Its original base-16 phases converge to
\(\delta_{1/5}\). Applying (9) gives phases converging to the same
atom, because \(81^kC\bmod1=C\) and the transformed moment tends to
zero. The general criterion (19) preserves the dyadic profile here too.

Thus even the combination of this filter, a preserved dyadic isometry,
a positive moment kernel, and limiting multiplication-by-81 invariance
does not imply normality without a real anti-clustering hypothesis.
This control changes the original BBP forcing; it does not refute the
authentic source target (28).

The highest-leverage remaining experiment is an exact, carry-retaining
comparison of the actual three-sheet output in (25) with the **same**
original selected window law, accompanied by a positive all-scale real
collision estimate. The algebraic transport error is already bounded by
(26); the unknown part is the statistical agreement. Another iteration
of the polynomial identities alone cannot establish that agreement.

## 9. Exact finite calibration and authority

An independent scratch implementation, using only integers and
`Fraction`, executed **5,523 assertions** successfully. It computed
authentic states directly from the original four-pole recurrence and
polynomial powers by literal coefficient convolution. The checks cover:

- Endpoint obstructions through powers \(3^{160}\), including the
  denominator-3 exponent condition.
- The denominator-4 valuation identity for every \(1\leq k\leq80\).
- Base-81 Newton coefficients through order 32 and translated difference
  valuations for starts 0 through 16 and orders 1 through 16.
- Reset sources at original starts 2, 3, 7, including their Newton
  identities, full tested valuation grids, and 507 strict complete-
  monotonicity sign checks for the rational forcing.
- The degree-six base-31 profile on starts 0 through 8 and orders
  1 through 8; the local base-81 transport identity through start 64.
- Exact rational kernel samples at all \(t=j/1000\), the sharp integer
  exponent-8 endpoint test, and the nontripling invariant atomic control.
- Twenty-eight independent Machin-arctangent rational enclosures of
  the actual remainder, at original starts 0, 1, 2, 7 and transform
  orders 1, 2, 7, 8, 16, 31, 40, checked against the rational bound (14).

These finite ranges calibrate the formulas. The universal claims,
minimalities, dyadic extensions, and asymptotics rest on the proofs
above, not the sample grid. No production code or existing test was
modified by this translator lane. The root integration must report its
own repository gates separately.
