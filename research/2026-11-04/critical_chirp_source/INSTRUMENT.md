# Exact finite maximal signed certificate

This instrument encloses the actual finite quantity M_A(H), not only its
full-epoch coefficient. It proves no universal asymptotic. Every operation in
`signed_probe.py` uses integers or Fractions.

## Source and depth

The first evaluator iterates all four original rational poles with seed zero.
The second uses the independently collapsed quadratic numerator, one LCM and
an integer register. Their entire epoch vectors must agree exactly. These
are different implementations of one source, not independent source families.

For A=2^k, use log A=k log 2 and

    log 2 = 2 sum_(j>=0) 3^(-2j-1)/(2j+1).

After N terms the positive remainder is at most
9/[4(2N+1)3^(2N+1)]. The reported H must satisfy
H <= A² log(A)_lower <= A² log(A)_upper < 16H; otherwise the instrument
rejects the depth. This certifies the specified floor, including its radix
boundary, without a floating logarithm.

## Character budget

Machin's identity pi=16 arctan(1/5)-4 arctan(1/239), obtained by the tangent
addition formula with the angle in (0,pi/2), and alternating arctangent bounds
enclose pi. The midpoint is rounded down to the 2^-80 grid, and its distance
from both pi enclosure endpoints is checked to be below 2*2^-80.

Reduce the exact rational phase to [-1/2,1/2) before rounding to 2^-80.
The angular error is below 14*2^-80. The resulting angle has absolute value
below 4. Degree-47 sine/cosine Taylor polynomials have each remainder at most
4^48/48!, by the real Lagrange remainder. Each output component is rounded
down to the 2^-60 grid. Euclidean error is bounded by the sum of component
errors. If the original phase has enclosure radius delta, add 7 delta using
2 pi < 7. The complete sufficient budget is

    14*2^-80 + 2*4^48/48! + 2*2^-60 + 7 delta <= 2^-50.

The code checks this exact rational inequality on every call. The coherent
control's phase radius comes from the positive decreasing source tail:

    L_n = sum_(k=1)^24 16^-k r(n+k),
    L_n < T_n < L_n + r(n+25)/(15*16^24).

Forcing positivity/monotonicity is inherited from the original Mellin density;
no numerical value of pi constructs this control or the authentic orbit.

## Maximum over all intervals

Let z_n be the grid characters and P_b their integer-scaled prefix sums.
Every contiguous sum is exactly a chord P_b-P_a. Exhaustively enumerate all
A(A+1)/2 chords using integer squared norms, and let D² be the largest.
Integer square root gives floor(D) <= D < floor(D)+1. Every exact character
differs from its grid value by at most epsilon=2^-50, so every normalized
interval sum differs by at most epsilon. Therefore

    max(0, floor(D)/(A*2^60)-epsilon) <= M_A(H)
       <= min(1, (floor(D)+1)/(A*2^60)+epsilon).

This upper bound covers ALL intervals, even if the maximizing exact interval
differs from the grid witness. Multiplication by exact Lambda gives the R
enclosure. Decimal displays are rounded outward with integer division.

Checks include exact roots of unity, enormous integer phase translations,
conjugate characters, a zero full-sum/nonzero maximal-sum adversary, interior
diameter witnesses, constant periodic orbits, and deliberate underresolution.
Finite data do not adjudicate a claim about all sufficiently large epochs.
