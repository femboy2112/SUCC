# The authentic BBP source has a Gamma primitive and a normalization constant

Date: 2026-10-25 (America/New_York). Parent: PR #297 at
`eca4462ee4d62642b15c4af672136aa5bcacd00b`.

**Status:** classical special-function identities with source-specific paper
proofs and exact finite certificates. The new implementation uses the original
signed BBP forcing. It does not establish its signed orbit cancellation,
normality of pi, RH, or an arithmetic independence claim about Euler's constant.
Academic priority is unverified. These are a new-to-this-branch interface and
normalization audit, not a claim to have discovered Gamma theory.

## 1. Hole contract and inherited facts

The question is whether the proposed boundary twist has an exact Gamma
realization, and where Euler--Mascheroni survives when the source is kept
faithful. The source is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad n\ge1.
$$

Set

$$
a=(1/8,1/2,5/8,3/4),\qquad w=(4,-2,-1,-1).
$$

The inherited [BBP regulator dossier](../2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md)
already proves

$$
B(s)=8^{-s}\sum_i w_i\zeta(s,a_i),\qquad B(0)=15/8,
$$

and the disappearance of the common Euler constant from the balanced digamma
readout at s=1. The [source repair](../2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md)
already proves the four-pole moments and the discounted Green tail. Those
claims are inherited, not rediscovered here.

The new exact interface is a multiplicative primitive whose successor ratio
retains all four shifts, with two finite certificate routes for its boundary
normalization. The cheapest falsifiers are: a changed pole weight; a dropped
Gamma normalization; a missing factor of 8; or the false claim that a rational
successor ratio fixes its initial multiplicative value.

## 2. Gamma lift of the complete four-pole source

For real x>=0 define, using the standard positive Gamma function,

$$
G(x)=\frac{\Gamma(x+1/8)^4}
{\Gamma(x+1/2)^2\Gamma(x+5/8)\Gamma(x+3/4)}.
\tag{GB-1}
$$

The Gamma recurrence gives the exact positive rational quotient

$$
q(x):=\frac{G(x+1)}{G(x)}
=\frac{(x+1/8)^4}{(x+1/2)^2(x+5/8)(x+3/4)}.
\tag{GB-2}
$$

Taking its logarithmic derivative yields

$$
\frac18\frac{d}{dx}\log q(x)
=\frac18\sum_i\frac{w_i}{x+a_i}=r(x+1).
\tag{GB-3}
$$

Here r is extended by its displayed rational formula to real x+1>=1.
The shifts a_i are source-index parameters, not orbit states on the digit
circle. The exponent 1/8 is essential: deleting it multiplies the forcing
by eight. The formula is a source-preserving identity, not a source average.

For finite N>=0,

$$
\frac{G(x+N)}{G(x)}
=\prod_{j=0}^{N-1}q(x+j)
=\prod_i (x+a_i)_N^{w_i}.
\tag{GB-4}
$$

At rational x this is an exact rational certificate. Both its direct product
and its independently arranged rising-factorial product are tested.

The classical Gamma ratio asymptotic and
sum w_i=0, sum w_i a_i=-15/8 give

$$
\lim_{x\to\infty}x^{15/8}G(x)=1.
\tag{GB-5}
$$

This normalization is load-bearing. If another positive function F on [0,infinity)
has F(x+1)=q(x)F(x), then F/G is 1-periodic. If in addition
x^(15/8)F(x)->1, then for each fixed x, F(x)/G(x)=F(x+N)/G(x+N)->1.
Thus F=G. Without the boundary normalization, every positive 1-periodic
multiple is a solution; even multiplying by the constant 7 preserves every
successor ratio. The latter is an exact hostile control in the tests.

## 3. The ordinary Green tail is a balanced digamma readout

Define

$$
H(x)=-\frac18\frac{d}{dx}\log G(x)
=-\frac18\sum_iw_i\psi(x+a_i).
$$

The classical partial-fraction expansion

$$
\psi(z)=-\gamma+\sum_{k=0}^{\infty}
\left(\frac1{k+1}-\frac1{k+z}\right)
$$

and sum w_i=0 cancel both common terms. Hence

$$
\boxed{H(x)=\sum_{k=0}^{\infty}r(x+k+1)>0,\quad
H(x)-H(x+1)=r(x+1).}
\tag{GB-6}
$$

Convergence follows from r(x+k+1)=O(k^-2). In particular H(x)->0,
H(x)~15/(64x), and H is the unique solution to this successor difference
law with the stated zero boundary at infinity. The same periodic-difference
argument proves uniqueness.

This is the **ordinary** tail. It is not the base-16 tail
T_n=sum_(j>=1)16^(-j)r(n+j) used to authenticate pi. The latter obeys
16T_n-T_(n+1)=r(n+1) and has size 1/(64n^2). A Gamma/digamma identity for H
does not allow replacing T by H in the selected BBP recurrence.

For finite N>=1, the exact prefix of GB-6 has omitted tail bracket

$$
\frac{15}{8(8(x+N)+6)}
<H(x)-\sum_{j=0}^{N-1}r(x+j+1)
<\frac{15}{8(8(x+N)-7)}.
\tag{GB-7}
$$

Proof: write r(y+1) as the sum of three positive reciprocal differences
with total interval length 15. Thus
15/(8y+6)^2<r(y+1)<15/(8y+1)^2. Integrate the decreasing lower comparison
from N to infinity, and the upper comparison from N-1 to infinity.
Every denominator in GB-7 is positive on the declared domain.

## 4. Euler--Mascheroni survives one primitive higher

Set

$$
M_k=\sum_iw_i(1-a_i)^k
=4(7/8)^k-2(1/2)^k-(3/8)^k-(1/4)^k.
$$

Then M_0=0, M_1=15/8 and M_k>0 for every integer k>=1. Positivity
follows by grouping the expression as
2[(7/8)^k-(1/2)^k]+[(7/8)^k-(3/8)^k]+[(7/8)^k-(1/4)^k].
These are eight times the inherited signed forcing-pole moments.

The convergent Taylor expansion of log Gamma(1-z), |z|<1, now gives

$$
\boxed{\log G(0)=\frac{15}{8}\gamma+
\sum_{k=2}^{\infty}\frac{M_k\zeta(k)}k.}
\tag{GB-8}
$$

Thus Euler's constant cancels from the balanced derivative in GB-6 while
appearing in the canonical primitive normalization in GB-8. This is an
explicit identity in a declared expansion; it does not prove that gamma is
algebraically indispensable in every expression for G(0).

Every summand after the gamma term is positive. For K>=1, M_k<4(7/8)^k
and zeta(k)<2 for k>=2 imply

$$
0<\sum_{k>K}\frac{M_k\zeta(k)}k
<\frac{64}{K+1}(7/8)^{K+1}.
\tag{GB-9}
$$

The code combines this with inherited exact gamma bounds and rational
Dirichlet-sum/integral bounds for each integer zeta value. No numerical
Gamma or zeta value generates a certificate endpoint.

An independently arranged Euler-product proof gives

$$
\log G(0)=M_1\gamma+
\sum_{n=1}^{\infty}\left[-\log q(n-1)-\frac{M_1}{n}\right].
\tag{GB-10}
$$

Indeed -log q(n-1)=sum_(k>=1)M_k/(k n^k); its first term is exactly
M_1/n. The compensated summands are positive. Setting A=7/8, the tail
after n=N is at most

$$
\sum_{n>N}\frac{2A^2}{n^2(1-A/n)}
\le\frac{2A^2}{N(1-A/(N+1))}.
\tag{GB-11}
$$

The finite sum in GB-10 equals -log(product_(j<N)q(j))-M_1 H_N;
its logarithm is enclosed by the inherited rational atanh-series routine.
The two interval routes overlap on the declared finite holdouts. Removing
the M_1 gamma compensator makes them disjoint, giving an exact mutation
receipt rather than a floating-point disagreement.

## 5. The source zeta derivative fixes the same multiplicative boundary

The inherited B(s) is entire after the four Hurwitz residues cancel. The
classical identity zeta'(0,a)=log Gamma(a)-log(2 pi)/2 gives

$$
\boxed{B'(0)=\log G(0)-\frac{15}{8}\log8.}
\tag{GB-12}
$$

The log(2 pi) constants cancel because sum w_i=0; the log8 term survives
because B(0)=15/8. The code encloses this derivative by GB-8 and exact
log8 bounds. Omitting the factor 8^(-s) in the source yields the wrong
derivative and is detected by disjoint intervals.

If desired, exp(-B'(0))=8^(15/8)/G(0) is a **signed source zeta-product
normalization**. The weights w_i include negative entries, so this must not
be relabelled the determinant of an asserted positive operator. No
nontrivial zeta-zero positions appear as inputs.

## 6. The user's zero-reference change and its conversion term

For a real offset c define

$$
\Gamma_c(z)=e^{c(z-1)}\Gamma(z),\qquad \psi_c(z)=\psi(z)+c.
$$

Then Gamma_c(1)=1, psi_c(1)=c-gamma, and
Gamma_c(z+1)=e^c z Gamma_c(z). At c=gamma the derivative at the unit
origin vanishes, but the ordinary Gamma successor normalization has changed.

The BBP quotient sees this transformation particularly cleanly:

$$
G_c(x):=\prod_i\Gamma_c(x+a_i)^{w_i}
=e^{-15c/8}G(x).
\tag{GB-13}
$$

Its rational successor ratio q and its balanced derivative H remain
**exactly invariant**. However its boundary normalization changes:
x^(15/8)G_c(x)->e^(-15c/8). The canonical condition GB-5 selects c=0
within this real exponential gauge family.

At c=gamma, GB-8 becomes log G_gamma(0)=sum_(k>=2)M_k zeta(k)/k.
This is the precise sense in which the explicit Euler constant can be zero
in a different normalization while the local authenticated BBP source stays
unchanged. The conversion constant has not disappeared. Because B(s)
retains its original Hurwitz normalization, its derivative must be written

$$
B'(0)=\log G_c(0)+\frac{15c}{8}-\frac{15}{8}\log8.
\tag{GB-14}
$$

Changing only log G(0) in GB-12 and omitting this compensation is invalid.
Likewise choosing c=gamma uses that constant to specify the new reference;
it is not an independent derivation of gamma.

## 7. What is and is not gained

| Claim | Status and boundary |
|---|---|
| Four-pole source equals the logarithmic derivative of a Gamma successor quotient | PROVED PAPER, exact rational finite checks |
| Gamma primitive is unique after its multiplicative infinity normalization | PROVED PAPER; ratio alone permits periodic gauges |
| Common gamma disappears from the balanced digamma readout | CLASSICAL, inherited; exactly source-balanced |
| Canonical log G(0) has the convergent gamma/zeta expansion GB-8 | PROVED PAPER; explicit rational remainder certificate |
| B'(0) is the same normalization with the source scale correction | CLASSICAL Hurwitz identity, source-specific application |
| Setting the Gamma unit derivative to zero preserves q and H | PROVED PAPER; the primitive normalization shifts |
| These identities establish selected pi-orbit cancellation | OPEN; no such estimate is obtained |

The next useful bridge must retain the selected c=0 BBP trajectory or its
signed Fourier correlations. Local Gamma source identities and normalization
changes alone cannot supply those statistics. A comparison theorem that
controls the signed Fourier sum while preserving all four poles and the
initial selector would be a genuine new proof step; merely writing that sum
in Gamma notation would be a reformulation.

## 8. Reproduction and primary sources

Implementation: [bbp_gamma_boundary.py](../../observational_succ/bbp_gamma_boundary.py).
Tests: [test_bbp_gamma_boundary.py](../../tests/test_bbp_gamma_boundary.py).
Command: `python -m unittest tests.test_bbp_gamma_boundary -v`.

Observed focused validation: **13 tests passed**. Exact checks cover source
recovery, product composition and rising-factorial enumeration, moment
balance, source-tail certificates, independent boundary enclosures, and
missing-gamma/missing-scale/mutated-weight controls. One mpmath log-Gamma
readout calibrates both rational intervals; it is explicitly numerical and
supplies no proof authority. No new Lean theorem is claimed.

Classical primary reference entries:

- [DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1), Gamma recurrence;
  [5.5.2](https://dlmf.nist.gov/5.5.E2), digamma recurrence.
- [DLMF 5.7](https://dlmf.nist.gov/5.7), log-Gamma Taylor and digamma
  partial-fraction expansions. GB-8 is the ordinary |z|<1 form obtained
  by expanding the extra logarithm in 5.7.3.
- [DLMF 5.8.2](https://dlmf.nist.gov/5.8.E2), Euler's Gamma product and
  its normalization by gamma.
- [DLMF 5.11](https://dlmf.nist.gov/5.11), Gamma ratio asymptotics.
- [DLMF 25.11.18](https://dlmf.nist.gov/25.11.E18), the Hurwitz derivative
  at zero used in GB-12.

The proof, exact code and numerical calibration share mathematical source
data; they are complementary checks, not independent external refereeing.
