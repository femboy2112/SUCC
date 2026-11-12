# Separate audit of the damped integer-grade filters

**2026-11-12.** This is a bounded, separately tasked same-model audit of the
root's construction. It is not external peer review. The arithmetic replay
uses a smallest-prime-factor sieve, independent Lagrange weights and direct
product evaluation rather than the production trial-factor and polynomial
expansion paths.

## Verdict and repaired finding

The all-grade leakage theorem, coefficient amplification bound, signed
interval formula, integer rounding and two-sided monotone ratchet are sound
under the stated hypotheses. Every one of the **18 frozen arithmetic
certificates** was independently reproduced, with **zero differing fields**
in the mathematical outputs checked. The replay confirms 14 positive lower
bounds, four negative lower responses, and eleven exact count recoveries.

A real helper-domain bug was found and reported before finalization. The
initial `histogram_certificate` accepted rational masses but unconditionally
asserted the integer-count promise. The executed input

```python
histogram_certificate((Fraction(1, 2), 0, 4), 2)
```

returned `count_recovered=True`, integer count zero, despite actual zero-grade
mass `1/2`. Its real interval `[0,1/2]` was sound; attaching the integer
interpretation was unsound for that admitted input.

**Repair observed:** the wrapper now requires nonnegative exact integer
histogram entries, while general nonnegative rational masses remain usable
through `response` and `certificate` without an integer promise. The audit
replayed the reported input after repair and observed a `ValueError`.
The root added the explicit regression and a valid real-mass control.
All frozen arithmetic inputs were integers, so the repaired issue changes
none of their recorded results.

## 1. Domain and all-grade leakage

The argument requires nonnegative mass on **integer** grades, finite total
mass, even degree `d>=2` for the public lower filter, and `0<t<=1/2` for
the displayed leakage envelope. There is no unstated maximum grade.

The polynomial has unit value at grade zero and roots at grades
`1,...,d-1`. At every integer `h>=d`, the `d-1` negative factors give the
negative sign. The magnitude is

\[
g_d(h)=\frac{t^{h+d(d-1)/2}
 \prod_{j=1}^{d-1}(1-t^{h-j})}
 {\prod_{j=1}^{d-1}(1-t^j)}.
\]

At `h=d` the products cancel exactly, leaving
`t^[d(d+1)/2]`. Cancelling the product terms between successive grades gives

\[
\frac{g_d(h+1)}{g_d(h)}
=t\frac{1-t^h}{1-t^{h-d+1}}
\le\frac{t}{1-t}\le1.
\]

This proves the claimed envelope for every higher integer grade. It is
not based on the finite high-grade test. Summing the signed pointwise bound
against nonnegative finite mass gives

\[
(1+\epsilon)c_0-\epsilon M\le B\le c_0.
\]

For the arithmetic specialization, both endpoints `n-a,n+a` are at least
two. Thus each `Omega` is at least one, the grade is a nonnegative integer,
and grade zero means both endpoints are prime. The range `0<=a<=n-2`
counts each unordered pair once, including the equal-prime pair at `a=0`.
The total mass is exactly `n-1`.

## 2. Uniform conditioning

Positive roots and a zero constant term force alternating nonzero
coefficients. Their absolute sum therefore equals

\[
\prod_{j=1}^{d-1}\frac{1+t^j}{1-t^j}.
\]

Each factor increases with `t`, so it is enough to bound the infinite
product at `1/2`. The first four factors multiply to `51/7`. For `j>=5`,
`x=2^-j<=1/32` and

\[
\log\frac{1+x}{1-x}\le\frac{2x}{1-x}\le\frac{64}{31}x.
\]

Since `sum_(j>=5) 2^-j=1/16`, the tail logarithm is at most `4/31`.
The inequality `exp(4/31)<31/27` gives the stated strict bound
`(51/7)(31/27)=527/63<9`. No missing tail factor or dependence on degree
was found. The bound controls propagation of absolute response errors;
it does not make acquiring source-authenticated responses free.

## 3. Interval signs, upper mass budgets and integer rounding

For positive coefficients the code takes the lower response endpoint to
minimize a term; for negative coefficients it takes the upper endpoint.
The upper filtered endpoint uses the opposite selections. These choices
are correct for asymmetric intervals.

Solving the lower inequality in section 1 gives

\[
c_0\le\frac{B+\epsilon M}{1+\epsilon}.
\]

Replacing B by its upper enclosure is safe. An upper bound `M_budget` on
the actual total mass is also safe: replacing the actual mass by a larger
number only weakens this upper bound. Clipping to `[0,M_budget]` is valid.
The resulting feasible interval does not by itself certify that every input
response packet has a nonnegative histogram realization; source/model
authenticity remains an explicit hypothesis.

One executed endpoint control used the genuine histogram `(2,1,4)`, for
which `F(1/2)=7/2`, `F(1/4)=5/2`, and actual mass seven. Supplying asymmetric
enclosures `[3,5]` and `[2,3]` with the deliberately larger mass budget ten
gave filtered interval `[-1,3]` and target interval `[0,34/9]`, which contains
the true zero mass two. Both the signed endpoints and the budget relaxation
were checked exactly.

The integer lower expression is the exact ceiling of the nonnegative real
lower endpoint; the upper expression is its exact floor. If
`epsilon*M<1`, the exact response lies in `(c_0-1,c_0]`, so its ceiling is
the correct integer count. With uncertainty, the width estimate and the
condition `epsilon*M+18 max eta<1` are sufficient. A genuine integral packet
must contain an integer; an empty integer interval is properly rejected.

## 4. Monotone lower/upper ratchet

The added mathematical extension to odd degree is valid. Its higher-grade
tail has the same absolute magnitude formula and the opposite sign; hence
odd degrees give upper bounds. For `h>=d+2`, the ratio between degrees
`d+2` and `d` is

\[
\frac{(t^d-t^h)(t^{d+1}-t^h)}{(1-t^d)(1-t^{d+1})}.
\]

It is nonnegative and at most
`t^(2d+1)/[(1-t^d)(1-t^(d+1))]`. This majorant increases with t and decreases
with d, so its maximum in the declared domain is `1/3` at `d=1,t=1/2`.
At the two newly cancelled grades the newer response is zero. These facts
prove the stated pointwise monotonicities. Summing against nonnegative
mass preserves them, and the common absolute leakage envelope tends to zero.
The public code correctly continues to reject odd degree as a **lower**
filter; the separate mathematical upper ladder is not mislabeled by the API.

## 5. Independent complete arithmetic replay

The audit built the smallest prime factor of every integer through **8198**
with a sieve. It then computed
`Omega(k)=1+Omega(k/spf(k))`, generated each midpoint histogram, and counted
unordered prime pairs separately using the sieve's prime indicator.

For each frozen degree, the weights were independently generated as the
Lagrange weights at nodes `t,t^2,...,t^d`, rather than by expanding the
production polynomial. The filtered value was evaluated in two ways:

- Sum the direct product `Q(t^h)` against the sieve histogram.
- Sum the independent Lagrange weights against the generating responses.

Those two independent expressions agree exactly. The audit then recomputed
the mass budget, coefficient norm, leakage, clipped interval, integer
endpoints, positivity and recovery flags. All these fields matched every
published certificate. The separate prime count matched grade-zero mass.

| Midpoint n | Direct unordered count | Recovered at d=2 | Recovered at d=4 | Recovered at d=6 |
|---:|---:|:---:|:---:|:---:|
| 10 | 2 | yes | yes | yes |
| 257 | 14 | no | yes | yes |
| 509 | 20 | no | yes | yes |
| 1021 | 30 | no | yes | yes |
| 2053 | 53 | no | no | yes |
| 4099 | 84 | no | no | yes |

**Observed:** 18 certificates, zero mismatched mathematical fields,
14 positive lower bounds, four negative responses, eleven exact recoveries.
All 18 nine-decimal displays in `DAMPED_FILTERS.md` were also verified to
their stated rounding precision.

The independent computational core was:

```python
from fractions import Fraction as F
from math import ceil, floor

limit = 8198
spf = [0] * (limit + 1)
for p in range(2, limit + 1):
    if spf[p] == 0:
        for k in range(p, limit + 1, p):
            if spf[k] == 0:
                spf[k] = p
omega = [0] * (limit + 1)
for k in range(2, limit + 1):
    omega[k] = 1 + omega[k // spf[k]]

def independent_packet(n, degree, t=F(1, 2)):
    hist = {}
    for a in range(n - 1):
        h = omega[n+a] + omega[n-a] - 2
        hist[h] = hist.get(h, 0) + 1
    nodes = [t**r for r in range(1, degree + 1)]
    weights = []
    for j, x in enumerate(nodes):
        value = F(1)
        for k, y in enumerate(nodes):
            if k != j:
                value *= -y / (x-y)
        weights.append(value)
    def product_filter(h):
        z = t**h
        value = z
        for j in range(1, degree):
            value *= (z-t**j) / (1-t**j)
        return value
    B = sum((c * product_filter(h) for h, c in hist.items()), F(0))
    responses = [sum((c*x**h for h, c in hist.items()), F(0))
                 for x in nodes]
    assert B == sum((a*f for a, f in zip(weights, responses)), F(0))
    eps = -product_filter(degree)
    assert eps == t**(degree*(degree+1)//2)
    M = sum(hist.values())
    lower = max(F(0), B)
    upper = min(F(M), (B+eps*M)/(1+eps))
    direct = sum(spf[p] == p and spf[2*n-p] == 2*n-p
                 for p in range(2, n+1))
    assert hist.get(0, 0) == direct
    return B, lower, upper, ceil(lower), floor(upper), direct
```

The record comparison was against every entry of `DAMPED_RESULTS.json`.
No production module was imported for that replay. The later single
fractional-count regression and asymmetric-endpoint checks deliberately
called the production API to validate the repair and interface behavior.

## 6. Final inspected hashes and limits

After the initial audit, the report added the exact response vector
`F_n((1/2)^r), r=1,...,d` to each frozen row. A further independent SPF
replay computed each response directly as
`sum_(a=0)^(n-2) (1/2)^[r*(Omega(n+a)+Omega(n-a)-2)]`, without importing
the production module. **All 18 added vectors, comprising 72 exact rational
coordinates, matched with zero differences.** The report addition exposes
the inputs to the already-audited filtered combinations.

The earlier inspected `damped_filters.py` hash was
`24271ccc8d17650e62e1f36fbee65c8e7f64d461d032dd11ea678b55e75bd069`, and
the earlier results hash was
`641c7ce6a5921cae7d1bf7c31d79b4b866f849145fbd6bd920206dc1c0352f58`.
They are retained here as provenance for the original full-certificate
replay. The final inspected hashes, including the added response vectors,
are:

| File | SHA-256 |
|---|---|
| `damped_filters.py` | `b379b3fdf194661d46d5842f1f2e68f03a42ef9cc8c9703cb89e09e4638b6700` |
| `test_damped_filters.py` | `b8c1476a30cf68c524eea8f63c66cb36ffc8d6213c7f77779c5f9b3efd9a357a` |
| `DAMPED_FILTERS.md` | `4966a88aa52a9e671596d2ec5c7870bb8556012e3bc450f943cb5528b2e7310e` |
| `DAMPED_RESULTS.json` | `7bbd2b25d0309bfe83c073733b05564cc2ed47cbd5a176660a5991b5be9009a7` |

The audit did not run a new broad test campaign or the native repository
suite. It used the frozen arithmetic cases, the proofs, and the targeted
counterexample/repair controls above. The finite results do not furnish an
analytic all-midpoint estimate for the coupled responses and do not prove
Goldbach. The known integer grade spectrum, nonnegative finite mass, source
authentication and paid response uncertainty remain load-bearing.
