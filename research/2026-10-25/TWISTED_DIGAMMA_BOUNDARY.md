# Sign-twisted successor, Gamma inversion, and the Euler-defect source

Date: 2026-10-25. Parent: `eca4462ee4d62642b15c4af672136aa5bcacd00b`.
Status: **CLASSICAL / PROVED LOCAL** identities and exact finite certificates.
Academic priority is UNVERIFIED. This note preserves a source while changing
its declared readout; it does not establish BBP orbit cancellation, pi
normality, RH, or a physical fermion interpretation.

## 1. Hole contract and novelty boundary

The user's proposal is that a reciprocal/sign twist should meet the Gamma
function and Euler--Mascheroni near the same boundary. The strongest faithful
test is an explicit intertwining of successor, reciprocal transport, and an
authenticated source observable. An analogy between two pictures is not the
test. The inherited Euler cell is

$$
\delta(x)=\frac1x-\log\left(1+\frac1x\right),\qquad x>0.
$$

[The existing zero/one bridge](GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md) already
proves that its untwisted sum at the unit origin is gamma and connects its
positive density to the original BBP four-pole density. Those are inherited
results. The added interface here is the reciprocal Gamma successor, its
sign-twisted Euler readout, and a dyadic reconstruction of the untwisted
constant from the twisted readouts, with a retained finite remainder.

The weakest local target is an exact source-preserving identity with a
provable tail bound. It is substantially weaker than any digit-normality
claim: it can hold for source observables that are independent of the
initial state of the BBP recurrence. The cheapest falsifiers are omitted
finite boundary terms, wrong parity, treating two twists as identity, and
confusing an alternating source sum with a character sum of orbit states.

## 2. Gamma has a literal reciprocal successor

For real a>0 define

$$
Q(a)=\frac{\Gamma((a+1)/2)}{\Gamma(a/2)},\qquad
F(a)=\frac{d}{da}\log Q(a).
$$

The classical Gamma recurrence immediately gives

$$
\boxed{Q(a+1)=\frac{a}{2Q(a)},\qquad
Q(a+2)=\frac{a+1}{a}Q(a).}
\tag{TDG-1}
$$

The first step is genuinely reciprocal. Two steps retain the multiplier
(a+1)/a; a pair of twists is not an identity return. Differentiation gives

$$
F(a)=\tfrac12[\psi((a+1)/2)-\psi(a/2)],\qquad
\boxed{F(a)+F(a+1)=1/a.}
\tag{TDG-2}
$$

By the classical digamma series, or by an integral and geometric summation,

$$
F(a)=\sum_{n\ge0}\frac{(-1)^n}{a+n}
=\int_0^1\frac{t^{a-1}}{1+t}\,dt.
\tag{TDG-3}
$$

The series is conditionally convergent. Pairing adjacent terms is legitimate;
arbitrary rearrangements are not used. For its N-term prefix the exact
successor identity is

$$
F_N(a)+F_N(a+1)=\frac1a+\frac{(-1)^{N-1}}{a+N}.
\tag{TDG-4}
$$

The boundary term is executable and nonzero. The condition F(a)->0 at
infinity uniquely selects TDG-3 among solutions of TDG-2: differences are
antiperiodic, so their absolute values are unchanged by integer shifts.

Likewise TDG-1 by itself does not uniquely select Gamma. For any real c,
Q(a) exp(c sin(pi a)) obeys the same reciprocal successor. The classical
normalization Q(a)/sqrt(a/2)->1 removes this antiperiodic gauge. Thus the
Gamma connection is exact, while boundary selection remains load-bearing.

For 0<a<1, Gamma reflection additionally gives

$$
\frac{Q(a)}{Q(1-a)}=\tan(\pi a/2),\qquad
F(a)+F(1-a)=\frac{\pi}{\sin(\pi a)}.
\tag{TDG-5}
$$

This is a reciprocal/reflective identity in a translated-source coordinate,
not a theorem identifying an affine BBP orbit with a Mobius strip.

### Exact finite certificate for the infinite alternating harmonic source

Use 1/(1+t)=sum_(k>=0)(1-t)^k/2^(k+1). With

$$
B(a,k+1)=\frac{k!}{a(a+1)\cdots(a+k)},\qquad
P_K(a)=\sum_{k<K}\frac{B(a,k+1)}{2^{k+1}},
$$

the exact residual integral gives

$$
\boxed{
\frac{B(a,K+1)}{2^{K+1}}
\le F(a)-P_K(a)\le
\frac{B(a,K+1)}{2^K}.}
\tag{TDG-6}
$$

Indeed the residual is integral t^(a-1)(1-t)^K/[2^K(1+t)] dt, and
1/2<=1/(1+t)<=1. Every endpoint is rational for rational a. This is a
certificate, whereas a decimal digamma evaluation is an independent
numerical diagnostic only.

## 3. The same Euler cells give gamma or log(4/pi)

The original unit-source sum is absolutely convergent:

$$
\sum_{n\ge1}\delta(n)=\gamma.
$$

Apply alternating signs to those same cells, without changing their values:

$$
\boxed{\sum_{n\ge1}(-1)^{n-1}\delta(n)=\log(4/\pi).}
\tag{TDG-7}
$$

Here is a proof which records the Gamma source. More generally, define

$$
D_-(a)=\sum_{n\ge0}(-1)^n\delta(a+n),\quad a>0.
$$

Pairing the logarithmic increments gives the convergent product

$$
\prod_{k\ge0}\frac{(a+2k+1)^2}{(a+2k)(a+2k+2)}
=\frac{\Gamma(a/2)\Gamma((a+2)/2)}{\Gamma((a+1)/2)^2}
=\frac{a}{2Q(a)^2}.
$$

This follows first at a finite product via Gamma recurrence and then by
the Gamma-ratio asymptotic. Therefore

$$
D_-(a)=F(a)-\log\frac{a}{2Q(a)^2}.
\tag{TDG-8}
$$

At a=1, F(1)=log 2 and Q(1)=1/sqrt(pi), proving TDG-7. In particular the
odd and even positive subseries are, respectively,

$$
\sum_{k\ge0}\delta(2k+1)=\frac{\gamma+\log(4/\pi)}2,
\qquad
\sum_{k\ge1}\delta(2k)=\frac{\gamma-\log(4/\pi)}2.
$$

Euler gamma is retained in the symmetric sector; the alternating contrast
has the different value log(4/pi). In the digamma difference TDG-2 the
common additive -gamma cancels exactly. Neither statement says gamma is
zero or that the constants are interchangeable.

## 4. A source-preserving dyadic Gamma decomposition of gamma

For any real d>0 set

$$
S(d)=\sum_{n\ge1}\delta(dn),\qquad
A(d)=\sum_{n\ge1}(-1)^{n-1}\delta(dn).
$$

The source is unchanged; d selects its sampled lattice. The same Gamma
product argument with b=1/d proves

$$
\boxed{
A(d)=\frac{\log2}{d}
-\log\left[
\frac{\sqrt\pi\,\Gamma(1+1/(2d))}
{\Gamma(1/2+1/(2d))}\right].}
\tag{TDG-9}
$$

For detail, the logarithmic part has paired product

$$
\prod_{k\ge0}
\frac{(2k+1+b)(2k+2)}{(2k+1)(2k+2+b)}
=\frac{\sqrt\pi\,\Gamma(1+b/2)}{\Gamma((1+b)/2)}.
$$

Absolute summability of the delta source allows even/odd separation:
A(d)=S(d)-2S(2d). Telescoping gives the exact finite-level identity

$$
\boxed{
\gamma=\sum_{j=0}^{J-1}2^jA(2^j)+2^JS(2^J),\qquad J\ge0.}
\tag{TDG-10}
$$

Because delta(x)=integral_0^(1/x) t/(1+t) dt, we have
0<delta(x)<1/(2x^2). Consequently

$$
0<2^JS(2^J)<\frac{\zeta(2)}{2\,2^J}<\frac5{6\,2^J}.
\tag{TDG-11}
$$

The last rational constant requires no numerical pi value:
zeta(2)<sum_(n=1)^5 1/n^2+integral_5^infinity x^-2 dx
=5989/3600<5/3. Letting J increase proves

$$
\boxed{\gamma=\sum_{j\ge0}2^j A(2^j),\qquad A(1)=\log(4/\pi).}
\tag{TDG-12}
$$

Every term A(d) is strictly positive. One proof is alternating monotonicity;
another uses the inherited positive Euler density W(t):
A(d)=integral_0^1 W(t)t^(d-1)/(1+t^d) dt.

The leading scale is also certified, not fitted:

$$
\left|A(d)-\frac{\pi^2}{24d^2}\right|
\le\frac{\zeta(3)}{3d^3}.
\tag{TDG-13}
$$

Indeed |delta(x)-1/(2x^2)|<=1/(3x^3) follows by integrating
t/(1+t)=t-t^2/(1+t). Sum absolute errors and use
sum_(-1)^(n-1)/n^2=(1-2^(1-2))zeta(2)=pi^2/12.

### Why the finite certificates cannot erase the boundary

For N=2^J M, define A_N(d) and S_N(d) with n<=N. The finite exact identity is

$$
S_{2^JM}(1)=\sum_{j<J}2^j A_{2^{J-j}M}(2^j)+2^J S_M(2^J).
\tag{TDG-14}
$$

The code verifies that every original delta(n) has coefficient exactly one.
Removing the final term changes those coefficients. Alternating-series
remainders and rational logarithm intervals independently enclose each
A(d). Combining them with TDG-11 yields a rational gamma interval without
using gamma, pi, or Gamma values as certificate inputs.

## 5. Normalization shifts are declared coordinate changes

For a fixed real c,

$$
H_N-\log(e^cN)=(H_N-\log N)-c\longrightarrow\gamma-c.
$$

Thus a reference scaled by e^gamma makes this particular finite part zero,
but does not prove gamma=0; choosing that scale already specifies gamma.
Two changes c and d compose additively. The implemented rational-offset
certificate translates both rational interval endpoints by -c, preserving
this cocycle exactly. Logarithm bases and reference scales are different
choices; this statement changes the latter with the natural logarithm fixed.

## 6. BBP transport and the operator boundary

The source-preserving alternating four-ray readout is

$$
\mathcal B_-:=\sum_{n\ge1}(-1)^{n-1}r(n)
=\frac18\sum_{j=1}^4 c_jF(a_j),
$$

where c=(4,-2,-1,-1) and a=(1/8,1/2,5/8,3/4). This follows by finite
source splitting and the convergent alternating limit. Exact instruments
enclose it by two different decompositions: direct rational r(n) with its
alternating tail, and the four TDG-6 Beta intervals. It is not the BBP
value pi, which uses weights 16^(-(n-1)), nor a Fourier statistic of U_n.

For a source sequence f and finite depth N define

$$
T_{b,N}(f)=\sum_{k=0}^{N-1}b^{-k-1}f_k,\quad b\ne0.
$$

The exact resolvent identity, with the same depth on both source shifts, is

$$
bT_{b,N}(f)-T_{b,N}(Ef)-f_0=-b^{-N}f_N.
\tag{TDG-15}
$$

The BBP backward tail uses b=16 and f_k=r(n+k+1). The alternating Gamma
resolvent uses b=-1 and f_k=1/(a+k), with T=-F. Their formal placement in
one family does not identify their operators. Nor is a sign at every source
step the same as a single orientation-reversing seam at a finite endpoint.
The source schedule and the authentic initial value must be checked again
for any proposed transfer to orbit statistics.

## 7. Validation, provenance, and next discriminant

The module is [twisted_digamma_boundary.py](../../observational_succ/twisted_digamma_boundary.py).
The [13 focused tests](../../tests/test_twisted_digamma_boundary.py) passed
locally. They include independent binomial integration of Beta coefficients;
digamma/Gamma numerical holdouts; source-word exact identities; rejection of
the dropped-boundary and two-twists-equal-identity mutations; finite dyadic
source-weight reconstruction; two independent BBP readouts; the wrong
resolvent multiplier; and rational-offset normalization covariance. Numerical
oracles corroborate the formulas but do not create their interval authority.

Primary classical sources, read for this round:

- [NIST DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1): Gamma successor.
- [NIST DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3): Gamma reflection.
- [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6): digamma series and its common -gamma.
- [NIST DLMF 5.11](https://dlmf.nist.gov/5.11): Gamma-ratio asymptotics.
- [NIST DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1): Euler Beta integral.
- [NIST DLMF 5.4](https://dlmf.nist.gov/5.4): unit and half-unit Gamma values.

The exact identities are classical consequences, newly instrumented here;
no claim of discovering a new special-function identity is made. The local
frame dominates a bare visual analogy because its source weights, boundary
terms, and normalization defects can be checked. It does not dominate the
existing authentic-source normality program: all the source-only identities
survive changing the BBP initial state. The next discriminant is an explicit
source-faithful map to the actual selected Fourier cocycle which distinguishes
U0=0 from the same-forcing tuned controls. No such map is asserted here.
