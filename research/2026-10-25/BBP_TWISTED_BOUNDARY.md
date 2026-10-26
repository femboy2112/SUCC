# Exact BBP endpoint seams, reversible charts, and their source boundary

Date: 2026-10-25. Parent: PR #297 at
`eca4462ee4d62642b15c4af672136aa5bcacd00b`.

**Status:** PROVED PAPER for the statements below; exact rational tests for
the finite implementation. No new Lean verification or academic priority is
claimed. Authentic BBP cancellation and pi normality remain OPEN.

The user's proposed identification of initial zero with zero at infinity is
made concrete here as an endpoint condition. This is a strong, testable
interpretation of a twist. A seam and a projective inversion are useful
mathematical constructions, but they have different effects on the source.

## 1. Source, provenance, and the seam contract

Throughout,

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

The inherited source tail and BBP evaluation are

$$
T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad
\alpha=T_0=\frac\pi{16},\quad U_n=16^n\alpha-T_n.
$$

These identities, their exact interval implementations, and the Green
conjugacy predate this round: see
[source memory](../../observational_succ/bbp_source_memory.py),
[the inherited gauge dossier](../2026-10-24/BBP_MINIMAL_PATH_GAUGE_AND_MISSING_PRIME.md),
and [the prior resonance controls](BBP_RESONANCE_OBSTRUCTIONS.md).
The rational tests evaluate no supplied digits of pi.

Every real solution with initial value c is

$$X_n=U_n+16^nc=16^n(c+\alpha)-T_n.$$

Consequently c=-alpha selects the unique bounded real solution X_n=-T_n.
Authentic c=0 selects a different solution. Exponential growth of its real
lift alone says nothing about its fractional-part distribution.

**Hole contract:** determine exactly what is preserved by an endpoint seam,
which initial state it selects, and whether it is a symmetry or a quotient
of the authenticated recurrence. Success here is an exact classification or
counterexample. A new statistical-cancellation theorem is a separate target.

## 2. TB-01: classification of every affine endpoint seam

Fix an integer N>=1 and real lambda,beta. Impose only

$$X_N=\lambda X_0+\beta.$$

Substitution of X_N=U_N+16^Nc gives

$$
(16^N-\lambda)c=\beta-U_N.
$$

Therefore:

| Hypothesis | Complete solution set |
|---|---|
| lambda differs from 16^N | Unique c=(beta-U_N)/(16^N-lambda) |
| lambda=16^N and beta=U_N | Every real initial state c |
| lambda=16^N and beta differs from U_N | No solution |

The authentic state c=0 is compatible **if and only if beta=U_N**,
including the singular case. In particular, the unshifted sign seam
lambda=-1,beta=0 changes the selected initial state. A seam with beta=U_N
can preserve the authentic source, but beta then already contains its entire
finite endpoint response. No cancellation follows from that identity.

The implementation accepts exact rational inputs. Its `kind` distinguishes
unique, all, and none; `initial=None` in the all case does not select zero.
Tests cover singular cases, authentic offsets, and a changed seam offset.

## 3. TB-02: the sign seam has two different limiting regimes

For lambda=-1,beta=0,

$$
c_N=-\frac{U_N}{16^N+1}
=-\alpha+\frac{\alpha+T_N}{16^N+1},
$$
$$
X_n^{(N)}=-T_n+\frac{16^n(\alpha+T_N)}{16^N+1},\qquad0\le n\le N.
\tag{1}
$$

In particular c_N approaches -alpha, and for each **fixed** n,
X_n^(N) approaches -T_n. The finite error is positive and exactly

$$X_n^{(N)}+T_n=\frac{16^n(\alpha+T_N)}{16^N+1}.$$

If A and B_N are upper bounds for alpha and T_N, respectively, then

$$0<X_n^{(N)}+T_n<16^{n-N}(A+B_N).$$

This also controls an interior region n<=N-K by 16^(-K)(A+B_N).
The condition that the interior recede from the moving endpoint matters.
For a fixed nonnegative integer j, equation (1) instead gives

$$X_{N-j}^{(N)}\longrightarrow\alpha16^{-j}.$$

Indeed, with B_n>T_n,

$$
\left|X_{N-j}^{(N)}-\alpha16^{-j}\right|
<B_{N-j}+16^{-j}(B_N+A16^{-N}).
\tag{2}
$$

At the endpoint, X_N=-c_N approaches alpha, while the bounded solution
-T_N approaches zero. The convergence to the bounded solution is therefore
not uniform over the expanding interval. `twisted_boundary_certificate`
returns strict rational enclosures and the bound (2). For an exponentially
small sign such as X_N-alpha<0, the tests refine the source interval with N;
a fixed precision enclosure is not silently treated as a sign certificate.

For fixed general lambda,beta and all sufficiently large N, put
b=beta-lambda alpha. Then

$$X_n=-T_n+\frac{16^n(b+T_N)}{16^N-\lambda}.$$

Its endpoint profile is b16^(-j). This source-and-seam numerator must remain
visible; the denominator alone does not determine the selected trajectory.

### Relation to the inherited order-m^-4 coherence result

The exact coefficient 3 pi^2 h^2/131072 for the separately tuned rational
controls is inherited from
[BBP_RESONANCE_OBSTRUCTIONS.md, section 3](BBP_RESONANCE_OBSTRUCTIONS.md).
Those controls suppress the terminal layer on their selected window.
Equation (1) does not do that. The new proof in
[the round report, S-3 and S-4](MOBIUS_GAMMA_BOUNDARY_REPORT.md)
shows that the simple sign seam instead has order-m^-1 modulus loss on
n=m+1,...,4m. Identical fixed-index limits do not identify the asymptotics
of a moving-window observable. This is not a new derivation of the old
order-m^-4 claim and is not a statement about authentic c=0 cancellation.

## 4. TB-03: an endpoint seam is not a cyclic forcing law

Suppose one tries to continue the finite seam as
X_(N+n)=lambda X_n+beta for every n>=0. Subtract the two recurrence equations.
The necessary forcing relation is

$$r(N+n)=\lambda r(n)-15\beta,\qquad n\ge1.$$

The exact failure at the first new step, assuming the preceding seam holds,
is

$$r(N+1)-\lambda r(1)+15\beta.$$

For the sign seam this is r(N+1)+r(1)>0. For an unshifted periodic seam
it is r(N+1)-r(1)<0. These are explicit counterexamples to propagating an
endpoint relation through the original forcing.

In fact there is **no fixed real affine seam** with N>=1 that propagates
globally. The source has
r(n)=15/(64n^2)+O(n^-3), so first n->infinity forces beta=0, and then
r(N+n)/r(n)->1 forces lambda=1. Strict decrease of r contradicts
r(N+n)=r(n). Positivity and strict decrease follow directly from

$$r(n)=\int_0^1 t^{8(n-1)}(4-2t^3-t^4-t^5)\,dt,$$

whose polynomial factor is positive on (0,1). This does not rule out
other constructions with explicit time-dependent transition data; it
rules out this exact fixed affine cyclic extension. Repeating or reversing
the forcing by hand constructs a different global source.

### A prime-primary source mutation that must not be hidden

The sign seam also differs from the prior carefully chosen p-free controls.
Take p=8m+1 prime and N=4m. Since 16^m=1 modulo p, 16^N+1=2 modulo p.
The p-primary part of c_N=-U_N/(16^N+1) is nonzero: the seam imports a
p-primary component before its authentic birth. On the first-birth window
its phase numerator is

$$2\,16^t\pmod p,\qquad0\le t<3m,$$

where the authentic numerator is 4 times 16^t. To verify this, subtract
16^n U_N/(16^N+1) from U_n and use the authentic first-birth formula.
The same forcing is retained, but neither zero initialization nor this
prime-primary birth clock is preserved. Exact tests check this at four
eligible primes. The formula, not those finite instances, supplies the
all-prime statement within the declared first-birth regime.

## 5. TB-04: the generating pole records the discarded initial selector

Let R(z)=sum_(n>=1)r(n)z^n, analytic on |z|<1, and let
G_c(z)=sum_(n>=0)X_n z^n in its initial convergence disk. Summing the
recurrence gives

$$G_c(z)=\frac{c+R(z)}{1-16z},\qquad R(1/16)=\alpha.$$

Its meromorphic continuation to |z|<1 has residue

$$\mathop{\rm Res}_{z=1/16}G_c(z)=-\frac{c+\alpha}{16}.$$

The pole is removable exactly for c=-alpha, the bounded solution. For
authentic c=0 its residue is -pi/256. A finite sign seam has
c_N+alpha=(alpha+T_N)/(16^N+1)>0, so its pole is small but not removed.
For any rational c the residue is nonzero, by the inherited classical
irrationality of pi. These are analytic descriptions of different selected
solutions; a pole is not a digit-equidistribution certificate.

The finite identity used in the implementation is valid for every rational
z, including z=1/16:

$$
(1-16z)\sum_{n=0}^{N}X_nz^n
=c+\sum_{n=1}^{N}r(n)z^n-16X_Nz^{N+1}.
$$

The last term is indispensable. Tests explicitly reject dropping it;
there is no exchange of a divergent infinite series with a finite identity.
Residue intervals use rational source-tail bounds, not numerical pi input.

## 6. TB-05: reciprocal reversal survives; two quotient claims fail

In the time-dependent real chart y_n=X_n+T_n the recurrence is
F(y)=16y. The projective map J(y)=1/y satisfies

$$JFJ(y)=y/16=F^{-1}(y).$$

This holds on nonzero finite points and extends to the projective line by
swapping zero and infinity. It is a reversal symmetry. A Mobius strip is a
different construction: its sign-flip fiber gluing preserves fiber zero.
Neither construction silently identifies initial zero with a selected
boundary condition at infinity.

The map F does **not** descend to the equivalence y~1/y. The related pair
2 and 1/2 maps to 32 and 8, whereas the reciprocal class of 32 is
{32,1/32}. This exact receipt defeats the claimed quotient map.

Also J is not well-defined on the real circle: 2 and 3 have the same
class modulo one, but 1/2 and 1/3 do not. Finally y_n=16^n has reciprocal
16^(-n) tending to zero while every character e(h y_n) equals one for
integer h. Reciprocal contraction therefore does not imply character
cancellation. All three finite algebraic controls are executable tests.

## 7. TB-06: source-preserving affine maps cannot move the authentic orbit

Let H_n(x)=a_n x+b_n satisfy
H_(n+1)(16x+r(n+1))=16H_n(x)+r(n+1) for every real x.
Comparing coefficients gives a_n=a constant and

$$b_n=(1-a)U_n+16^n b_0.$$

Conversely those coefficients satisfy the commutation equation exactly.
If H_0(0)=0, then b_0=0 and H_n(U_n)=U_n for every n. The anchored
reflection is H_n(x)=2U_n-x; it is involutive but fixes the authentic
trajectory pointwise. The zero-slope case is an affine map, not an invertible
conjugacy. The [hostile audit](MOBIUS_GAMMA_HOSTILE_AUDIT.md) gives the
full classification and its implications. The implementation tests both
the commutation identity and source-fixing reflections.

This obstruction is restricted to time-preserving affine maps. It does not
preclude an operator mixing distinct times, a nonlinear transform, or a
source-sensitive signed estimate outside this class.

## 8. Validation, verdict, and the next falsifier

Owned implementation:
[bbp_twisted_boundary.py](../../observational_succ/bbp_twisted_boundary.py).
Owned exact tests:
[test_bbp_twisted_boundary.py](../../tests/test_bbp_twisted_boundary.py).

The focused command `python -m unittest tests.test_bbp_twisted_boundary`
passes 14 tests in the available repository environment. They compare
forward recurrence with an independent closed convolution; cover singular
seams, authentic offsets, altered offsets, rational interval certificates,
nonuniform limits, first-prime-clock mutation, generating-function truncation,
reversal/non-descent, and affine source symmetries. One intermediate test
could not certify an exponentially small endpoint sign with a fixed-depth
tail interval; increasing its declared depth with N resolved the precision
failure without changing any mathematical claim. Full-round results belong
to [the validation record](MOBIUS_GAMMA_VALIDATION.md).

**Verdict: productive failure of the proposed automatic circle closure.**
Exact seam selection, reversible projective coordinates, and the boundary
layer survive. The automatic propagation of the seam through authentic
forcing and the reciprocal quotient are refuted by explicit receipts.
The new distinctions are useful for choosing valid observables; they do not
establish the remaining cancellation estimate.

The next falsification opportunity is a proposed source-preserving transform
outside the time-preserving affine class. It must act nontrivially on the
authentic signed observable, retain U_0=0 and the original forcing, and
reject periodic or changed-seed controls for an explicit reason. Merely
making a generating pole removable changes the initial selector and does
not meet that contract.
