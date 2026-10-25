# What all local observers force inside the rational-forcing class

**Date:** 2026-10-24. **Parent:** #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Status:** elementary paper consequences of polynomial congruences and
p-adic continuity. Scholarly originality is not claimed. These results
authenticate a forcing; they do not prove normality of its selected orbit.

The moving-prime controls in [the joint-primary dossier](PI_JOINT_PRIMARY_OBSERVERS.md)
are rational **sequences** at integer times. Their forcing is not one fixed
proper rational **function** of time. This distinction cannot be removed
from Bailey--Crandall Hypothesis A. Here is a positive rigidity statement
on precisely the missing class restriction.

## 1. A fixed prime detects distinct proper rational forcings with positive density

Let r,s belong to `Q(X)`, tend to zero on the positive real axis, and have
no poles at positive integers. If r is not s, then there exist a prime p,
positive integer K, positive integer a, and negative integer v such that

$$
v_p(s(n)-r(n))=v<0
\qquad\text{for every positive }n\equiv a\pmod{p^K}.
$$

Consequently their complete p-primary circle phases disagree on an
arithmetic progression of density `p^(-K)`.

**Proof.** Write the nonzero proper rational difference as `f=P/Q`, with
integer polynomials. Choose a positive integer a, beyond the finitely many
numerator zeros, with `0<|f(a)|<1`. Its rational value is nonintegral, so
some prime p satisfies

$$
A=v_p(P(a))<B=v_p(Q(a)).
$$

Take `K=1+max(A,B)`. The values `P(a),Q(a)` are nonzero integers, so A and B
are finite nonnegative integers. If `n=a mod p^K`, polynomial congruence
gives `P(n)=P(a) mod p^K` and likewise for Q. Since K exceeds both
valuations, `v_p(P(n))=A`, `v_p(Q(n))=B`; hence `v_p(f(n))=A-B<0`.

For a rational circle point, equality of p-primary components is equivalent
to the difference lying in `Z_(p)`, that is, having nonnegative p-valuation.
Thus the primary components disagree throughout this progression. QED.

**Corollary: density-zero time-aligned disagreement suffices.** Suppose for
every fixed prime p,

$$
\limsup_{N\to\infty}\frac1N
\#\{1\le n\le N:\pi_p([r(n)])\ne\pi_p([s(n)])\}=0.
$$

Then `r=s` exactly. Eventual agreement at each fixed prime is more than
enough, even if its starting threshold depends on the prime. A single
prime progression from the theorem would otherwise give positive lower
density, contradicting the hypothesis.

In fact `liminf` zero at each fixed prime suffices: the witness supplies
positive lower density. Writing `d=B-A`, its p-primary discrepancy has exact
order `p^d`, hence circle distance at least `p^(-d)` from zero. The lower
mean time-aligned primary distance is therefore at least `p^(-(K+d))`.
Thus vanishing mean primary distance at each prime also forces identity.
The valuation is constant on the stated progression; its actual primary
phase need not be constant. For example `f(n)=1/n`, a=9, p=3 and K=3 give
phases `1/9` at n=9 and `7/9` at n=36, both of valuation -2.

An unweighted average over observer primes is weaker and insufficient.
For `f(n)=1/(n+1)`, the mismatch density at prime p is `1/p`; its arithmetic
mean over primes tends to zero even though f is nonzero. The theorem needs
each fixed prime's density to vanish, or one fixed summable family of
strictly positive prime weights whose weighted mismatch tends to zero.
Positivity then retains every individual witness. An observer schedule
whose weight on each fixed prime vanishes needs an additional argument.

This concerns **time-aligned values of the forcing**, not equality of
unpaired marginal distributions, agreement of support counts, or random
observer relabelling. The properness assumption is necessary: an integer
constant difference is invisible to every primary circle observer.

An explicit calibration is `f(n)=1/((n+1)(n+2))`: at a=1, p=3,
`v_3(f(1))=-1`, and K=2 works. Every n congruent to 1 modulo 9 has
`v_3(f(n))=-1`, regardless of how small f(n) becomes in the real metric.

## 2. Full absolute agreement at one prime is still stronger

For any rational function f with no poles at positive integers, if
`f(n)->0` in `Q_p` as the ordinary integer n tends to infinity, then f is
identically zero. Properness is unnecessary here.

Fix a positive integer a. The integers `n_j=a+p^j` tend to infinity in the
ordinary ordering and tend to a p-adically. Continuity of f at a gives
`f(n_j)->f(a)` in `Q_p`; the assumed limit gives `f(n_j)->0`. Hence
`f(a)=0`. This holds for every positive a, so a polynomial numerator has
infinitely many zeros and is zero. QED.

There is a still weaker averaged version: at one fixed prime, the condition

$$
\liminf_{N\to\infty}\frac1N\sum_{n=1}^N
\min(1,|f(n)|_p)=0
$$

already implies `f=0`. Otherwise choose a positive integer a with f(a)
nonzero. Polynomial congruences on a sufficiently fine p-power progression
preserve its nonzero p-adic norm, so the displayed nonnegative average has
a fixed positive lower bound. This concerns absolute p-adic values, which
retain integral information discarded by primary circle projection.

Accordingly, the source-matching escape control's full local convergence
to the authentic forcing itself proves that its changed forcing cannot
belong to the same fixed rational-function class. There is no conflict
between the control and the rigidity theorem.

## 3. The authentic BBP source has a small exact algebraic certificate

The actual four-pole forcing simplifies to

$$
r(X)=\frac{120X^2-89X+16}
{(8X-7)(8X-3)(2X-1)(4X-1)}.
$$

Its numerator degree is two, denominator degree four, and it is proper.
Within the class `deg P<=2`, `deg Q<=4`, two rational functions which
agree at seven distinct nonsingular points agree identically: the cross
product `P_1 Q_2-P_2 Q_1` has degree at most six and seven zeros.
With this denominator fixed, three nonsingular exact values determine
the numerator of degree at most two. The degree/pole-class bound is part
of the certificate; a finite sample without that bound is insufficient.

These are polynomial identity facts, not statistical estimates. Once r
and `U_0=0` are fixed, `U_n=16U_(n-1)+r(n)` already fixes every source
state. Normality asks a further question about the time frequencies of
that unique history.

## 4. What this contributes to the research cut

All fixed local observers can, under an exact rational-function hypothesis,
force the authentic source rather than merely constrain it. This supports
the strong reading of the author's joint-observer intuition. It also
locates the remaining task accurately: source authentication is available;
real temporal cancellation is not obtained from authentication alone.

The next theorem must use the rigid rational source to bound the joint
conditional collision, trimmed carry hotspots, or gain-preservation defect.
Replacing the rational identity by all fixed real/p-adic asymptotic jets
is defeated by the source-matching control. Requiring exact authenticity
still does not justify assuming the missing statistical conclusion.
