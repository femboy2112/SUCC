# Fibonacci constants in the extruded harmonic/Oily readout

**PROVED LOCAL assembly of classical identities; not a normality estimate.**
Leah/femboy2112 authored the Harmonic / Golden / Euler–Mascheroni triangle
and Oily–Macaroni. The inherited Pascal construction fixes
lambda=(sqrt5-1)/2, p=lambda², and

    A_m=E H_(Binomial(m,p))=H_m-sum_(j=1)^m lambda^j/j,
    Omega_m=lambda-A_m+log(mp),  Omega=lambda-gamma.

Those formulas, Fibonacci diagonals and the one-snapshot harmonic finite
part gamma-log5/2 already exist in the repository. We do not claim them as
discoveries. Here we calculate the **accumulated** readout along the declared
Fibonacci extrusion, with a finite all-time error budget. This clock is an
observer choice; no theorem identifies it with the selected BBP clock.

## FCK01: the total Oily calibration loss

Let F0=0,F1=F2=1, phi=1/lambda, q=-lambda². For m>=1 put

    h_m=H_m-log m-gamma,
    b_m=Omega-Omega_m=h_m+sum_(j>m)lambda^j/j.

The inherited elementary harmonic bound gives 0<h_m<1/(2m).
Since F_(n+2)>=2F_n, both series below converge absolutely:

    Z_F(s)=sum_(n>=2) F_n^(-s), s>0,
    B_F=sum_(n>=2) b_(F_n)>0.

The conventional reciprocal Fibonacci constant is C_F=1+Z_F(1), including
both F1=F2=1. It already controls the exact source fluctuation budget in
[FIC03](../composition/FIBONACCI_COMPOSITION.md). Here it also controls the
harmonic part of the accumulated Oily loss:

    Z_F(1)/2-Z_F(2)/12 < sum_(n>=2)h_(F_n) < Z_F(1)/2.

The sharper lower bound follows from the positive Binet integral for the
digamma function: expand its denominator once, or use the first two
enclosing positive-real asymptotic truncations. No asymptotic infinite
series is substituted as a convergent series.

For every N>=2 the uncomputed Oily budget satisfies

    0 < B_F-sum_(n=2)^N b_(F_n)
      <= 1/F_(N+1)+1/F_(N+2)
         +lambda^(F_(N+1)+1)/[(F_(N+1)+1)(1-lambda)^2].       (1)

For the harmonic part, split the Fibonacci tail into even and odd indices
and sum geometric bounds. For the golden part, the remaining F_n are
distinct integers at least F_(N+1); replace them by all such integers,
bound each denominator below by F_(N+1)+1, and sum twice geometrically.
This proves (1) for all horizons, without a fitted error coefficient.
Consequently

    sum_(n=2)^N Omega_(F_n)=(N-1)Omega-B_F+o(1).             (2)

Thus Oily–Macaroni is the linear slope of this accumulated, specified
readout, while B_F is a finite total calibration loss. It is not a new
physical action or a source-selected signed phase.

## FCK02: the fibonorial constant supplies the finite offset

Binet's formula, checked from the Fibonacci recurrence and two initial
values, is F_n=phi^n(1-q^n)/sqrt5. Therefore exactly

    product_(n=1)^N F_n=phi^[N(N+1)/2] 5^(-N/2) (q;q)_N,
    (q;q)_N=product_(n=1)^N(1-q^n).

The positive limit C_prod=(q;q)_infinity is the classical Fibonacci factorial
constant. Its negative base q retains the alternating conjugate root;
replacing q by +lambda² changes even F1 and the product. The log tail obeys

    |log C_prod-log(q;q)_N|
      <= |q|^(N+1)/[(1-|q|)(1-|q|^(N+1))].                 (3)

Indeed |log(1-u)|<=|u|/(1-|u|), then sum a geometric upper bound.
Combine the exact product with A_m=log(mp)+gamma+b_m and p=phi^-2:

    sum_(n=2)^N A_(F_n)
      = (N-1)(N-2)/2 * log phi
        +(N-1)(gamma-log5/2)
        +log[(q;q)_N/(1-q)] + sum_(n=2)^N b_(F_n).          (4)

In particular the finite part after subtracting the first two terms is

    K_F=log[C_prod/(1+lambda²)]+B_F.                       (5)

The triangular coefficient in (4) is an actual summation count. The golden
growth, Euler finite part, Fibonacci product and Oily loss all occur in
different algebraic roles in one exact transport identity. This supplies a
precise interpretation of the **extruded** triangle, without conflating its
positive auxiliary realization with arithmetic time. Equations(1),(3)
give a rigorous effective remainder for (5).

## FCK03: exact certificates and falsifiers

The executable certificate uses integer Fibonacci recurrence, rational
square-root brackets, positive atanh logarithm series, and the positive-real
digamma remainder through B12/B14 after shifting small arguments to64.
The shift is exact:

    h_m=h_j+log(j/m)-sum_(k=m+1)^j 1/k, j>=m.

Every final decimal endpoint is rounded **outward** from rational endpoints.
The certificate uses120 Fibonacci ranks,180 golden powers and80 product
factors, including analytic bounds for every omitted tail. It does not use
precomputed digits of gamma, pi or the reciprocal Fibonacci constant.
See [raw certificate](../receipts/clock-exact.log).

For orientation only, certified values round to

    C_F = 3.359885666243...
    log C_prod = 0.204361883409...
    K_F = 1.544905887502...

The separate100-digit oracle uses digamma, a geometric-tail integral,
q-Pochhammer evaluation, and direct binomial expectations for three finite
aggregates. These are numerical cross-checks, not a second interval proof
or an external referee. Exact tests also check transported log identities,
harmonic and golden-tail differences, wrong conjugate sign and wrong mark.

**Refuted shortcut:** these constants distinguish extrusion conventions,
but cannot alone certify the authentic selected phase. All positive-source
clock identities remain valid after changing the arithmetic seed to the
coherent same-forcing seed. Conversely the fresh versus retained-memory
variance budgets differ despite the same first source law. Thus neither
the constants nor the starting snapshot determine an untyped internal arrow.

## Primary inputs and prior provenance

The only imported analytic remainder is the classical positive-real
digamma bound, documented in [NIST DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii).
Its integral origin is [DLMF5.9.15](https://dlmf.nist.gov/5.9.E15).
The product convention is [DLMF17.2.4](https://dlmf.nist.gov/17.2.E4).
All Fibonacci product algebra and tail estimates above are displayed here.
No irrationality or transcendence assertion about these constants is needed.

Inherited source:
`research/2026-10-29/oily_triangle_sheet/PASCAL_GOLDEN_HARMONIC.md`
at parent PR408. The prior Fibonacci information-clock branch is separately
pinned by the composition/arithmetic fronts. Scholarly priority is not claimed.
