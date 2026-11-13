# The Machin escape attempt: a quantitative two-place obstruction

**Status: PROVED PAPER in the stated family; exact finite checks.** This addresses the
unexamined multi-log suggestion at the end of Main XXV's
[restricted-exponent dossier](../frontier_rungs/RESTRICTED_EXPONENT.md), specifically
RDT-06 and RDT-08. It gives no restricted exponent for pi and no R0 saving.
The baseline is `db9fb4b84672050efa79b13377f1e73364598a14`.
No literature-priority claim is made. The calculations and proof are by one model;
root review, external review, and formal verification have separate authority.

The proposed escape was concrete: Machin's formula supplies two small complex
logarithm arguments, overcoming the single-logarithm effective-base obstruction.
We construct the standard diagonal Pade approximants, combine them with a common
rational denominator, and prove that the resulting rational approximants approach
pi in the real metric; along the degree subsequence `n=2^k`, they approach
**zero** in the 2-adic metric. The latter
forces the divisibility advantage onto the rational term, rather than the pi
coefficient. This is a demonstrated obstruction for this family, not a prohibition
on all multi-log or multipole constructions.

## 1. Exact objects and theorem

For every integer `n >= 1`, define

\[
Q_n(z)=\sum_{j=0}^n {n\choose j}{2n-j\choose n}z^j,
\qquad
P_n(z)=[Q_n(z)\log(1+z)]_{\le n}.
\]

The bracket means Taylor truncation at zero. Thus `P_n,Q_n` have rational
coefficients, `P_n(0)=0`, and `Q_n(0)=binom(2n,n)`.
For an odd integer `q >= 3`, put

\[
\alpha_q=\frac{q+i}{q-i},\qquad z_q=\alpha_q-1=\frac{2i}{q-i},
\qquad L_n(q)=\frac{P_n(z_q)}{Q_n(z_q)}\in\mathbb Q(i).
\]

The denominator is nonzero, as proved below. Define the rational number

\[
 b_n=2\left(4\operatorname{Im}L_n(5)-\operatorname{Im}L_n(239)\right).
\]

**GP-01 (real approximation, all `n >= 1`).**

\[
 |\pi-b_n|
 \le \frac{16}{(2n+1)5^{2n+1}}
      +\frac4{(2n+1)239^{2n+1}}.
\tag{1}
\]

**GP-02 (quantitative wrong-side divisibility).** For `n=2^k`, `k >= 2`,

\[
 v_2(b_n)\ge n-2k-4.
\tag{2}
\]

Equation (1) also implies `b_n>0` for every `n>=1` (its right side is
less than 1, while `pi>3`), so these valuations are finite. In particular,
for `k >= 4`, `v_2(b_n)>0`. Any rational common-denominator
normalization of `pi-b_n`, written `A_n pi-B_n`, has

\[
 v_2(A_n)-v_2(B_n)=-v_2(b_n)<0.
\tag{3}
\]

Consequently the exact gain of RDT-02(b),
`G_n=2^{max(v_2(A_n)-v_2(B_n),0)}`, is **one** on this subsequence.
No radix-restricted advantage is obtained over the unrestricted transference
bound from the same forms. This conclusion is invariant under multiplying a form
by any nonzero rational scalar; choosing a more elaborate common denominator
cannot alter it.

The growing powers of two here refer to **Pade degree**, not digit position.
No limit in one of those variables has been substituted for the other.

## 2. Proof of the Pade identity and the real estimate

For `m>n`, partial fractions give the elementary identity

\[
 \sum_{j=0}^n\frac{(-1)^j{n\choose j}{2n-j\choose n}}{m-j}
 =\frac{(m-n-1)\cdots(m-2n)}{m(m-1)\cdots(m-n)}.
\tag{4}
\]

To check it without a Pade theorem, compare the residues at each `m=j` and
the behavior at infinity. It implies that the coefficients of degrees
`n+1,...,2n` vanish in `Q_n log(1+z)-P_n`. At degree `2n+1+j` the coefficient is

\[
 (-1)^j\frac{(n+j)!^2}{j!(2n+j+1)!}
 =(-1)^j\frac{{n+j\choose j}}
 {(2n+j+1){2n+j\choose n}}.
\tag{5}
\]

Hence, initially for `|z|<1`,

\[
 R_n(z):=Q_n(z)\log(1+z)-P_n(z)
 =z^{2n+1}\int_0^1\frac{t^n(1-t)^n}{(1+zt)^{n+1}}\,dt.
\tag{6}
\]

This follows either by the beta integral or direct integration of the absolutely
convergent power series. Our `z_q` satisfy `|z_q|=2/sqrt(q^2+1)<1`.

Let `mathsf P_n` be the Legendre polynomial, given explicitly by its usual
finite factorial sum. A direct coefficient identity gives

\[
 Q_n(z)=z^n\mathsf P_n(1+2/z),\qquad 1+2/z_q=-iq.
\]

In the factorial expansion of `mathsf P_n(-iq)`, the alternating coefficient
signs cancel the signs of the even powers of `i`. Every term therefore has the
same complex argument. Keeping its leading term gives

\[
 |Q_n(z_q)|\ge
 \left(\frac q{\sqrt{q^2+1}}\right)^n {2n\choose n}>0.
\tag{7}
\]

The chord `1+t z_q` has modulus at least `q/sqrt(q^2+1)`. Using (6), (7), and
`integral_0^1 t^n(1-t)^n dt=1/((2n+1)binom(2n,n))`,

\[
 \left|\log\alpha_q-L_n(q)\right|
 \le\frac{(2/q)^{2n+1}}{(2n+1){2n\choose n}^2}
 \le\frac2{(2n+1)q^{2n+1}}.
\tag{8}
\]

Here `binom(2n,n)>=2^n` follows by multiplying `(n+j)/j >=2` for `1<=j<=n`.
The complex principal logarithm has `Im log alpha_q=2 arctan(1/q)`.
Exact Gaussian arithmetic gives

\[
 \alpha_5^4/\alpha_{239}=i.
\tag{9}
\]

Also `0<4 arctan(1/5)-arctan(1/239)<4/5<pi/2` (the lower bound follows, for
example, from `arctan(1/5)>1/5-1/(3*5^3)` and `arctan(1/239)<1/239`). Thus (9)
selects the real angle `pi/4`, rather than another branch. It proves the usual
Machin identity and `pi/2=4 Im log alpha_5-Im log alpha_239`.
Equation (1) follows from twice the triangle inequality in (8).

## 3. The second place sees a zero period

Work in `K=Q_2(i)`, with the valuation normalized by `v(2)=1`.
For odd `q`, `v(q-i)=1/2`, hence `v(z_q)=1/2`. The logarithm power series
converges on all `1+z` with `v(z)>0`, and is a homomorphism there.
These standard facts are stated in MIT's official
[18.785 Fall 2021 problem set 10, Problem 2(c,d,h)](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_pset10.pdf),
read for this derivation. Only these classical logarithm facts are imported.
In particular `i` belongs to this domain and `4 log_2(i)=log_2(1)=0`.
Equation (9) therefore gives

\[
 4\log_2\alpha_5-\log_2\alpha_{239}=0.
\tag{10}
\]

This is an exact difference of target fields: the complex period is `i*pi/2`,
whereas its 2-adic logarithmic period vanishes. It is not evidence that real pi
vanishes or that either metric can be interchanged with the other.

### 3.1 The denominator cannot hide a large 2-adic loss at power-of-two degrees

Let `n=2^k`, `k>=2`. The constant term of `Q_n` has valuation
`v_2(binom(2n,n))=1`, by the factorial valuation formula.
For `1<=j<n`,

\[
 v_2{n\choose j}=k-v_2(j),
\]

because `binom(n,j)=(n/j)binom(n-1,j-1)` and all binomial coefficients in
row `n-1` are odd (expand `(1+X)^{2^k-1}` modulo 2).
Thus the `j`th nonconstant term of `Q_n(z_q)` has valuation at least
`k-v_2(j)+j/2>1`. The last term has valuation `n/2>=2`.
The constant is the unique least-valuation term, so

\[
 v(Q_n(z_q))=1.\tag{11}
\]

This is the step that makes the normalized Pade quotient auditable. An
unnormalized small remainder alone would not suffice.

### 3.2 A uniform lower bound for the remainder valuation

For every positive integer `M`, the factorial valuation formula, or binary
carry counting, implies `v_2(binom(M,r))<=floor(log_2 M)`.
Using the second expression in (5), the coefficient of `z^{2n+1+j}` has
valuation at least `-2 log_2(2n+j+1)`. Consequently the term after evaluation
at `z_q` has valuation at least

\[
 \frac{2n+1+j}{2}-2\log_2(2n+1+j)
 \ge n+\frac12-2\log_2(2n+1).
\tag{12}
\]

For `n>=4`, the last inequality follows from monotonicity in `j>=0`:
the derivative of `j/2-2 log_2(2n+1+j)` is positive.
The terms tend 2-adically to zero. Thus their convergent sum, divided by (11),
satisfies

\[
 v(\log_2\alpha_q-L_n(q))
 \ge n-\frac12-2\log_2(2n+1).\tag{13}
\]

Complex conjugation is the nontrivial automorphism of `Q_2(i)` and preserves
its unique valuation. It commutes with this convergent logarithm series.
Furthermore

\[
 b_n=\frac{4(L_n(5)-\overline{L_n(5)})
 -(L_n(239)-\overline{L_n(239)})}{i}.
\]

Subtract (10) and its conjugate from this expression. The ultrametric triangle
inequality and (13) bound `v_2(b_n)` below by the right side of (13).
Since `2n+1<2^{k+2}` and `b_n` is rational, its integer valuation is at least
`n-2k-4`. This proves (2). Multiplication by a common denominator proves (3).

## 4. Scope extension and the surviving escape route

The same argument applies to a **fixed finite** collection of odd integers
`q_j>=3` and rational coefficients `c_j`, provided

\[
 \sum_j c_j\log\alpha_{q_j}=i\lambda\pi\quad\text{over the real principal branches},
 \qquad \sum_j c_j\log_2\alpha_{q_j}=0,
 \qquad 0\ne\lambda\in\mathbb Q.
\]

For integral `c_j`, the second condition follows when the product
`prod alpha_{q_j}^{c_j}` is a root of unity; clearing fixed denominators covers
rational coefficients. Set `b_n=lambda^{-1} sum c_j Im L_n(q_j)`.
Then `b_n -> pi` over the reals and

\[
 v_2(b_n)\ge n-O(\log n)
 \quad(n=2^k),
\]

where the constant accounts for the fixed coefficients, `lambda`, and the
factor `1/(2i)` in imaginary-part extraction. Hence the eventual gain is again
one. This is **GP-03**, a paper corollary with the declared hypotheses.

The theorem does not cover degree-dependent logarithm arguments, coefficient
families with growing negative 2-adic valuations, other Pade index schedules,
true Hermite--Pade systems that are not the stated componentwise quotients,
or multipole forms with a different local remainder geometry. It does not
prove those escape routes work. It identifies what a successful construction
must evade: simultaneous approximation of a real nonzero period and its
zero 2-adic logarithmic image, with controlled denominators.

The source-preserving bridge to the BBP problem is the classical identity of
both real values with pi; no transfer of rational BBP clock or carry statistics
is asserted. This is an arithmetic route elimination below R0, not a new
statistical estimate for the original BBP orbit.

## 5. Exact checks, retained mutations, and next falsifier

The standard-library exact arithmetic script is [gaussian_probe.py](gaussian_probe.py);
its raw JSON is [GAUSSIAN_RESULTS.json](GAUSSIAN_RESULTS.json). Reproduce with
`python research/2026-11-12/leah_gamma_twist/gaussian_probe.py`.
All displayed valuations below were computed with `fractions.Fraction`, and
Gaussian valuation was calculated as half the rational valuation of the norm.
Real error checks used a separate alternating Machin enclosure with `2n+10`
terms in each arctangent. No floating value was used as a certificate.

| Degree n | Exact v2(b_n) | Theorem lower bound n-2 log2(n)-4 |
|---:|---:|---:|
| 4 | 5 | -4 |
| 8 | 10 | -2 |
| 16 | 19 | 4 |
| 32 | 36 | 18 |
| 64 | 69 | 48 |

Completed checks: 330 exact order/coefficient identities for degrees 1 through
20; 30 denominator valuations for degrees 4,8,16,32,64 and q in
`{3,5,7,17,239,1001}`; five combined Machin valuation checks; five rational
real-error enclosures; three mutation/scope checks. The initial scratch probe used a looser integer lower bound. The packaged probe
checks exactly the stronger bound (2); it passed on the same five degrees.
When the degree-three scope control was added, its first test had the sign of
`A*pi-B` reversed and failed. The exact rational enclosure showed the error is
negative; the assertion and displayed inequality were corrected and the full
probe rerun. The failed sign assumption is retained here.

The non-power-of-two control `n=3,q=5` has `v(Q_n(z_q))=15/2`, refuting extension
of the exact denominator valuation (11) to arbitrary n. Indeed
`b_3=1072231967/341301560` has `v_2(b_3)=-3`, an actual pi-side tilt. An exact
alternating Machin enclosure gives
`1493 < 1072231967-341301560*pi < 1494`, so its primitive integer error is
greater than one and RDT-02(c) makes this particular form silent at every
radix position. This also refutes any extension of GP-02 to every degree.
Changing the Machin
coefficient 4 to 3 destroys the torsion relation (9). These controls show that
the arithmetic hypotheses perform work. After the proof and original cases were fixed,
three additional exact denominator holdouts `(n,q)=(128,31),(128,257),(256,3)`
also returned valuation one; these are recorded separately from the original counts.

**Next falsifying probe.** Audit equations (4), (7), and (12) by a separately
written symbolic/valuation derivation. One power-of-two degree and odd `q>=3`
violating (11) refutes the key normalization lemma. One exact rational `b_n`
violating (2), with the stated Pade coefficients, refutes GP-02. Agreement at
more degrees cannot replace the all-degree argument above.

**Next constructive strike.** Seek a convergent pi form with an explicitly
proved positive linear slope of `v_2(A_n)-v_2(B_n)` that is not a fixed finite
combination of locally convergent, denominator-controlled logarithm
approximants. If found, pay the real remainder rate and common-denominator
cost through RDT-01 before claiming a restricted-exponent improvement.
Even a restricted exponent below one would still leave the medium-scale
statistical implication needed for R0 open.
