# The twisted seam coefficient, q-Gamma, and the Euler finite part

**Status:** PROVED PAPER for the identities and bounds below; VERIFIED FINITE
for the listed exact checks. Classical q-product identities applied to the
seam coefficient. Scholarly novelty is unverified. No authentic BBP signed
cancellation, pi normality, or RH claim follows.

**Baseline:** `eca4462ee4d62642b15c4af672136aa5bcacd00b`, PR #297.
The underlying recurrence and its initial state are not modified by this note.

## 1. A literal q-product occurs in the twisted boundary problem

Consider a real affine recurrence with multiplier b>1 and any forcing:

$$
X_n=bX_{n-1}+r(n),\qquad X_0=c.
$$

If U is its zero-initial solution, then X_N=b^N c+U_N. The boundary condition
X_N=lambda X_0+beta therefore has scalar coefficient b^N-lambda:

$$
(b^N-\lambda)c=\beta-U_N.
$$

Set q=1/b. Its normalized coefficient is d_N(lambda)=1-lambda q^N.
For every positive integer M,

$$
\prod_{N=1}^{M}d_N(\lambda)=(\lambda q;q)_M.
\tag{QG-1}
$$

Here (a;q)_M means the finite product of (1-aq^j), 0<=j<M. In the
antiperiodic case lambda=-1, this gives

$$
P_{q,M}:=\prod_{N=1}^{M}(1+q^N)
=\frac{(q^2;q^2)_M}{(q;q)_M}.
\tag{QG-2}
$$

**Proof:** factor 1-q^(2N)=(1-q^N)(1+q^N) separately at each N. All
denominators are nonzero for 0<q<1. This is an exact finite identity.

The product over different horizons is an explicitly chosen aggregation of
scalar seam coefficients. It is not asserted to be the determinant of a
single source-authenticated infinite BBP operator. The BBP multiplier gives
q=1/16 exactly.

## 2. Convergence and an exact rational certificate

For 0<q<1, the infinite positive product

$$
P_q:=\prod_{N=1}^{\infty}(1+q^N)
=(-q;q)_\infty
=\frac{(q^2;q^2)_\infty}{(q;q)_\infty}
\tag{QG-3}
$$

converges because 0<log(1+q^N)<=q^N and the geometric series converges.
Its logarithmic tail obeys

$$
0<\log P_q-\log P_{q,M}
\le\frac{q^{M+1}}{1-q}.
$$

Let S=q^(M+1)/(1-q)<1. Then a completely rational enclosure is

$$
P_{q,M}(1+S)<P_q<\frac{P_{q,M}}{1-S}.
\tag{QG-4}
$$

**Proof:** expand the tail product. Its constant and linear terms are 1+S,
and its higher terms are strictly positive. Its degree-k elementary
symmetric sum is at most S^k/k!, hence the product is at most exp(S), which
is strictly smaller than 1/(1-S). For rational q the displayed endpoints
are rational. At q=1/16 the condition S<1 holds already at M=0.

## 3. The sign twist is an exact q-Gamma quotient

For a>0 define the shifted positive product

$$
P_q(a)=\prod_{n=0}^{\infty}(1+q^{n+a}).
$$

In particular P_q(1)=P_q. Factor each plus term into a ratio of minus
terms and apply the defining product of q-Gamma to obtain

$$
\boxed{
\frac{P_q(a)}{P_q(1)}
=(1+q)^{1-a}\frac{\Gamma_q(a)}{\Gamma_{q^2}(a)}.
}
\tag{QG-5}
$$

**Derivation:**

$$
P_q(a)=\frac{(q^{2a};q^2)_\infty}{(q^a;q)_\infty},\qquad
\Gamma_q(a)=\frac{(q;q)_\infty(1-q)^{1-a}}{(q^a;q)_\infty}.
$$

Substitution gives QG-5, using (1-q^2)/(1-q)=1+q. The sign twist therefore
has an actual Gamma-family expression, with no appeal to visual similarity.
These q-product and q-Gamma definitions are classical; see
[DLMF 5.18.1--4](https://dlmf.nist.gov/5.18).

The ordinary Gamma limit gives, for each fixed a>0,

$$
\lim_{q\uparrow1}\frac{P_q(a)}{P_q(1)}=2^{1-a}.
\tag{QG-6}
$$

Both q-Gamma factors approach the same Gamma(a), so their common limit
cancels. The invoked Gamma limit is [DLMF 5.18.10](https://dlmf.nist.gov/5.18.E10).
Changing q toward 1 changes b toward 1. It is a deformation of the
recurrence family, not a limit that the fixed BBP multiplier 16 undergoes.

## 4. Euler--Mascheroni appears in the untwisted logarithmic derivative

Define psi_q(a)=d log Gamma_q(a)/da, a>0, and gamma_q=-psi_q(1).
Differentiating the normally convergent product on compact a-intervals gives

$$
\psi_q(a)=-\log(1-q)
+(\log q)\sum_{n=0}^{\infty}\frac{q^{n+a}}{1-q^{n+a}},
$$

$$
\boxed{
\gamma_q=\log(1-q)-\log q\sum_{N=1}^{\infty}
\frac{q^N}{1-q^N}\longrightarrow\gamma\quad(q\uparrow1).
}
\tag{QG-7}
$$

The limit is justified without interchanging an unbounded Lambert series
and a singular limit. Let f_q=log Gamma_q. These functions are convex on
(0,infinity), and converge pointwise to log Gamma by DLMF 5.18. For every
0<h<1, convexity bounds f_q'(1) between the left and right difference
quotients at 1 with spacing h. First take q upward to 1 in those two finite
quotients, then h downward to zero. The bounds converge to
psi(1)=-gamma, as recorded in [DLMF 5.4.12](https://dlmf.nist.gov/5.4.E12).
This proves QG-7.

However, the normalized *antiperiodic* product has derivative

$$
\left.\frac{d}{da}\log\frac{P_q(a)}{P_q(1)}\right|_{a=1}
=-\log(1+q)-\gamma_q+\gamma_{q^2}
\longrightarrow-\log2.
\tag{QG-8}
$$

Thus Euler--Mascheroni occurs in the two untwisted q-Gamma derivatives and
cancels from their limiting sign-twisted difference. The two finite-q
gamma quantities need not be equal. A claim that the twist's limiting
normalization is gamma rather than log 2 would fail QG-8.

### A shifted reference gives an explicit shifted finite part

Write t=-log q. QG-7 compares the two singular terms

$$
\gamma_q=\log(1-q)+t\sum_{N\ge1}\frac1{e^{Nt}-1}.
$$

As q tends to1 the first term tends to minus infinity; the second tends
to plus infinity because their sum has the proved finite limit gamma.
This is a specified, compensated limit, never arithmetic on unsigned
infinity symbols. If a positive reference scale ell replaces (1-q) by
ell(1-q) in the subtraction prescription, then exactly

$$
\gamma_q^{[\ell]}=\gamma_q+\log\ell,
\qquad\gamma_q^{[\ell]}\longrightarrow\gamma+\log\ell.
$$

The named Euler constant corresponds to ell=1. Thus a changed reference
can genuinely shift the finite part, but its value must travel with its
reference prescription. The normalization is part of the object being
compared; it cannot be changed silently in a source-identification proof.

## 5. There is also an exact small/large-parameter duality

Put q=exp(-t), t>0, and qhat=exp(-4*pi^2/t). The classical modular product
identity [DLMF 17.2.6_2](https://dlmf.nist.gov/17.2.E6_2) says

$$
P_{e^{-t}}=\frac1{\sqrt2}
\exp\left(\frac{\pi^2}{12t}+\frac{t}{24}\right)
(\widehat q^{1/2};\widehat q)_\infty.
\tag{QG-9}
$$

This is a genuine transformation exchanging the small t regime with the
large 1/t regime. In particular,

$$
\log P_{e^{-t}}-\frac{\pi^2}{12t}-\frac{t}{24}
\longrightarrow-\frac12\log2\qquad(t\downarrow0).
\tag{QG-10}
$$

For an explicit error certificate put a=exp(-2*pi^2/t), so qhat=a^2.
The absolute error in QG-10 relative to its limiting constant is at most

$$
\frac{a}{(1-a)(1-a^2)}.
$$

Indeed the error is log of the product of (1-a^(2n+1)); use
-log(1-u)<=u/(1-u) and sum a geometric bound. This is the classical
modular identity's consequence, not a newly discovered duality and not an
identification of a Möbius strip with a modular transformation.

## 6. Adversarial source test and proof boundary

Every QG-1--10 expression above is independent of the forcing r and initial
value c. Replace the entire BBP forcing by zero while keeping multiplier16:
all seam coefficients and q-products remain identical. With c=0, the
resulting orbit is constantly zero and has Fourier mean1 for every integer
frequency. Therefore these identities alone cannot imply authentic-source
equidistribution. They describe the homogeneous seam normalization, not the
missing source-specific numerator beta-U_N.

The useful interface is the exact separation

$$
\text{boundary response}
=\frac{\beta-U_N}{16^N-\lambda}.
$$

The Gamma expressions govern a declared aggregation of denominators.
A prospective proof must retain and estimate the authenticated numerators
and their cross-time phases. Restoring that coupling, rather than replacing
the numerator by an average, is the next open bridge.

## Verification and provenance

Reusable finite instruments are in
[qgamma_seam.py](../../observational_succ/qgamma_seam.py), with seven tests in
[test_qgamma_seam.py](../../tests/test_qgamma_seam.py). They certify finite
seam products, rational infinite-product/Lambert tails, integer q-Gamma
ratios, and gamma_q intervals through inherited rational logarithm bounds.
The source-erasure and wrong-twist controls are explicit. The focused test
command `python -m unittest tests.test_qgamma_seam -v` passed seven tests.

- Exact Fraction computation checked QG-2 for q=1/16,1/2,2/3 and
  M=1,2,7,16: twelve cases passed. The proof is the termwise factorization,
  not the finite check.
- An independent 70-decimal mpmath evaluation checked QG-5 at
  q=1/16,1/2 and a=1/2,1,7/4; largest reported absolute discrepancy was
  9.056e-72. This is a floating-point consistency observation, not an interval
  certificate or proof of the infinite identity.
- The same precision checked QG-9 at t=log16,1,0.2; largest reported absolute
  discrepancy was 3.228e-69. DLMF is the source for the modular theorem.
- No claim is made that q-Gamma's uniqueness theorem supplies uniqueness of
  the authentic BBP circle statistics. Those are different mathematical
  objects and the r=0 control separates them.

**Verdict:** a concrete Gamma-family connection to the proposed seam exists;
its source-independent component is completely explicit. Euler--Mascheroni
is present in a neighboring renormalized derivative, and cancels from the
limiting antiperiodic ratio. Authentic signed cancellation remains OPEN.
