# Independent derivation audit: damped grade filters

Date: 2026-11-12. Auditor: the boundary-translation research agent, distinct
from the root constructor but in the same model family and research session.
This is a separate derivation and computational bearing, not an external
referee, a formal proof, or independent-source corroboration.

## Scope and verdict

The audited input was the root agent's proposed product filter and its
claimed sign, tail, coefficient and error bounds. The proof checks and
the independent rational calculations below were performed before this
audit file was written. They do not attest to arbitrary later versions
of the root implementation.

**Verdict: the construction survives on nonnegative integer grades with
0<t≤1/2.** It is classical geometric polynomial extrapolation with a
useful uniform one-sided error bound and a bounded coefficient norm.
It supplies a stable target certificate, not a new all-midpoint
Goldbach estimate. No upper support ceiling is needed; integrality,
nonnegative mass, source authenticity and response accuracy remain
load-bearing.

## 1. Sign and sharp tail bound

For an integer d≥1 and 0<t<1, put

$$
Q_{d,t}(z)=
\frac{z\prod_{j=1}^{d-1}(z-t^j)}
{\prod_{j=1}^{d-1}(1-t^j)},
\qquad q_d(h)=Q_{d,t}(t^h).
$$

The denominator is positive. Substitution gives q_d(0)=1 and
q_d(h)=0 at every integer 1≤h<d. At an integer h≥d, all d−1 factors
are negative. Even d therefore gives a nonpositive tail and odd d a
nonnegative tail.

Let g_d(h)=|q_d(h)|. Direct cancellation gives

$$
g_d(d)=t^{d(d+1)/2},\qquad
\frac{g_d(h+1)}{g_d(h)}
=t\frac{1-t^h}{1-t^{h-d+1}}.
$$

This ratio is largest at h=d: writing x=t^{h-d+1}, it is
t(1−t^{d-1}x)/(1−x), which increases with x. Hence the tail is
nonincreasing precisely when

$$
t+t^2+\cdots+t^d\le1.
$$

The uniform hypothesis t≤1/2 suffices. In that range, with
T_d=d(d+1)/2, even d gives

$$
-t^{T_d}\le q_d(h)\le0\quad(h\ge d),
$$

and odd d gives 0≤q_d(h)≤t^{T_d}. The bound is attained at h=d.
For d=1 the empty product gives q_1(h)=t^h, an upper filter.

### Mutations and exclusions

- For d=2,t=3/4, the claimed tail cap fails:
  q_2(2)=−27/64 but q_2(3)=−567/1024<−27/64.
  The even-order sign remains correct on integer grades for 0<t<1;
  it is the uniform sharp tail estimate that has failed.
- An arbitrary continuous nonnegative spectrum is outside the theorem.
  At d=2,t=1/2, every real 0<h<1 has q_2(h)>0, contradicting the
  desired lower-projector sign.
- Nonnegative histogram coefficients are required when integrating
  a pointwise bound. A signed histogram does not inherit it.
- The parameter t is exact and fixed. Uncertainty in t itself needs
  a separate propagated error bound.

## 2. Trace, normalized law, and integer recovery

For a finite-mass nonnegative histogram on integer h≥0, let
M=∑c_h, F(s)=∑c_hs^h, and expand Q(z)=∑_{r=1}^d a_r z^r.
Finite linearity gives

$$
B_d=\sum_{r=1}^d a_r F(t^r)=\sum_h c_h q_d(h).
$$

The same identity holds for a countably supported histogram of finite
mass by absolute convergence. At even d, with ε=t^{T_d},

$$
(1+\epsilon)c_0-\epsilon M\le B_d\le c_0,
$$

so the sharpened certified interval is

$$
\boxed{
B_d\le c_0\le\frac{B_d+\epsilon M}{1+\epsilon}.
}
$$

For M>0, normalized responses b_d=B_d/M and p_0=c_0/M satisfy
b_d≤p_0≤(b_d+ε)/(1+ε). The case M=0 is trivial and must not be
normalized by division.

If c_0 is integral and εM<1, then c_0−1<B_d≤c_0, hence
c_0=ceil(B_d). For positivity alone, if c_0≥1, then
B_d≥1−ε(M−1). Thus ε(M−1)<1 makes exact B_d positive exactly when
c_0>0. This is an equivalence within the count model, not a proof that
the authentic arithmetic response has that sign.

At t=1/2, an even d of order sqrt(log M) can make εM<1. This counts
response samples and filtering leakage; it does not count the work or
precision needed to obtain the responses.

## 3. Monotone filter-order brackets

The construction has a true monotonicity in filter order:

$$
B_2\le B_4\le B_6\le\cdots\le c_0,\qquad
B_1\ge B_3\ge B_5\ge\cdots\ge c_0.
$$

For h≥d+2,

$$
\frac{q_{d+2}(h)}{q_d(h)}
=
\frac{(t^d-t^h)(t^{d+1}-t^h)}
{(1-t^d)(1-t^{d+1})}
\in[0,1/3]
$$

when t≤1/2. The upper bound follows from numerator≤t^{2d+1}≤1/8
and denominator≥(1−t)(1−t²)≥3/8. The newly reached grades d,d+1
are annihilated; previous zero grades remain zero; grade zero remains
one. Applying these pointwise facts and integrating against c_h≥0
proves the brackets. Their limits equal c_0 by the tail bound.

This is a ratchet in the order of a mathematical filter. It is distinct
from a physical ratchet, a source-time trajectory, or a source-selected
growth theorem.

## 4. Classical extrapolation and uniform coefficient norm

The coefficients are the Lagrange weights for evaluation at zero from
the geometric nodes t,t²,...,t^d:

$$
a_r=\prod_{s\ne r}\frac{-t^s}{t^r-t^s}
=
\frac{(-1)^{d-r}t^{(d-r)(d-r+1)/2}}
{(t;t)_{r-1}(t;t)_{d-r}}.
$$

This was derived directly by splitting the product into s<r and s>r.
It agrees with expansion of Q by the finite q-binomial identity.
The two formulas provide different exact computational routes.

The coefficients alternate in sign, so

$$
\sum_r|a_r|
=\prod_{j=1}^{d-1}\frac{1+t^j}{1-t^j}
<\frac{527}{63}<9.
$$

For the bound it suffices to extend the product to infinity at t=1/2.
The first four factors multiply to 51/7. For j≥5,

$$
\log\frac{1+2^{-j}}{1-2^{-j}}
\le \frac{2\,2^{-j}}{1-2^{-j}}
\le\frac{64}{31}2^{-j}.
$$

Their sum is at most 4/31. Finally
exp(4/31)<1/(1−4/31)=31/27, so the full product is less than
(51/7)(31/27)=527/63. This proof handles all finite orders uniformly.

Primary provenance checked during the audit:

- [NIST DLMF 17.2.35](https://dlmf.nist.gov/17.2.E35) states the finite
  q-binomial product identity; 17.2.1 defines the shifted factorial.
- Avram Sidi, [A Complete Convergence and Stability Theory for a
  Generalized Richardson Extrapolation Process](https://epubs.siam.org/doi/10.1137/S0036142994278589),
  SIAM J. Numer. Anal. 34(5), 1997, explicitly treats geometric nodes
  and stability. Its accessible abstract establishes prior-art context;
  no unread full-paper theorem is load-bearing here.

The algebra is classical. The local contribution must be described as
its explicit certificate, conditioning, and arithmetic-access contract,
not a new extrapolation theorem.

## 5. Rational response errors: one E versus two E

Suppose |Fhat_r−F(t^r)|≤δ_r and define
E=∑|a_r|δ_r. Then |Bhat_d−B_d|≤E, so

$$
c_0\ge\widehat B_d-E.
$$

For a common absolute error δ, E<9δ. This is the correct error
payment for one observed certificate.

A different question asks for guaranteed success for **every** allowed
noise realization whenever c_0≥1. The report may first be depressed
by E, after which the certificate subtracts E. A sufficient condition is

$$
\epsilon(M-1)+2E<1.
$$

Dropping the second E from that worst-case guarantee is unjustified.
For noisy integer recovery, use

$$
\left[\widehat B_d-E,
\frac{\widehat B_d+E+\epsilon M}{1+\epsilon}\right]
$$

and conclude only if it contains a unique integer. Directly rounding
ceil(Bhat_d) can fail for arbitrarily small noise when B_d is itself
an integer. Normalized measurements require absolute accuracy of
order 1/M to resolve a single count; the coefficient bound does not
remove this requirement.

## 6. Overlap with the existing Borwein donor

I inspected donor #601 at
774191e7679cd63c56bdb105541ce21c8ee27448, specifically
research/2026-11-12/prime_fixed_point_observer/BORWEIN_RATCHET.md,
its BRT-06 readout, and the associated derivation audit.

That donor already gives T=P_1+P_2/2 and
T^r=P_1+2^{-r}P_2. Its declared spectral model even yields the
exact polynomial identity P_1=2T²−T. The damped construction must
therefore not be promoted as the first finite prime projector or as
automatically superior to the supplied Borwein functional calculus.

The changed access model is specific: a finite bank of damped
generating-function responses, no grade ceiling, bounded coefficient
amplification, and certified one-sided leakage. The prior Borwein
readout assumes a different functional-calculus observation.
Neither model creates primality information that its source never supplied.

For Goldbach, F_n(s)=∑_{d=0}^{n-2}s^{Ω(n+d)+Ω(n-d)-2} is a shifted
multiplicative-Ω convolution. Obtaining its responses accurately enough,
or deriving all-midpoint bounds on their signed combination, remains
the source-selected arithmetic obligation.

## 7. Executed exact check and reproduction

Before writing this file, I executed the following independent code in
memory. It computes weights from Lagrange interpolation, then compares
them with the product filter; it does not import the root implementation.
The recorded run completed with **4,716 exact assertions and zero
failures**, including grades 97 and 1000. The mutation outside the
uniform t range returned the two fractions recorded above.

~~~python
from fractions import Fraction as Q
from math import prod

def weights(d, t):
    nodes = [t**r for r in range(1, d+1)]
    return [
        prod((-nodes[s]) / (nodes[r] - nodes[s])
             for s in range(d) if s != r)
        for r in range(d)
    ]

def product_eval(d, t, h):
    z = t**h
    return z * prod((z - t**j) / (1 - t**j)
                    for j in range(1, d))

checks = 0
for t in (Q(1, 2), Q(1, 3), Q(2, 5)):
    for d in range(1, 13):
        a = weights(d, t)
        assert sum(a) == 1
        assert sum(abs(x) for x in a) == prod(
            (1+t**j)/(1-t**j) for j in range(1, d)) < 9
        checks += 2
        for h in list(range(41)) + [97, 1000]:
            q = product_eval(d, t, h)
            assert q == sum(a[r-1] * t**(r*h)
                            for r in range(1, d+1))
            if h == 0:
                assert q == 1
            elif h < d:
                assert q == 0
            elif d % 2 == 0:
                assert -t**(d*(d+1)//2) <= q <= 0
            else:
                assert 0 <= q <= t**(d*(d+1)//2)
            q_next = product_eval(d+2, t, h)
            if d % 2 == 0:
                assert q <= q_next <= int(h == 0)
            else:
                assert q >= q_next >= int(h == 0)
            checks += 3
assert checks == 4716
assert product_eval(2, Q(3, 4), 2) == -Q(27, 64)
assert product_eval(2, Q(3, 4), 3) == -Q(567, 1024)
print(checks)
~~~

The displayed final assertions expose the mutation and check the counter
itself; they are additional to the 4,716 assertions counted in the
recorded loop. The universal statements are supported by the derivations,
not extrapolated from these finite cases. No full repository suite,
hosted CI, asymptotic prime estimate, or external referee result is claimed.

After writing this audit, I extracted and replayed the displayed Python
block verbatim. It printed `4716` and exited successfully. That replay
checks reproducibility of the recorded artifact; it is not another
independent mathematical bearing.
