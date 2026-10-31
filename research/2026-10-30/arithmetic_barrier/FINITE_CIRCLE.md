# Certified finite selected-circle calibration

**Status: finite exact certificate; no unbounded-horizon theorem.**
The original four-pole zero-seed recurrence has
`U_n=16^(n-1)pi-T_n`, where `0<T_n<(8n+1)^(-2)`. The implementation keeps
`U_n mod 1` as an exact Fraction and refines the future by eight terms:

```
L_n = {U_n} + sum_(j=1)^8 16^(-j) r(n+j)
L_n < lifted pure phase < L_n + 16^(-8)/(8(n+8)+1)^2.
```

The interval is reduced on the circle only at observation. It can cross an
integer or bin boundary; such cases are retained as ambiguous rather than
silently rounded. All 1024 positions were unambiguous on grids 16, 64 and 256
under this refinement. The parent 256-position hexadecimal counts were
independently recovered.

## Character certificate

For each rational interval midpoint, `finite_circle.py` encloses both parts
of `exp(2 pi i h x)` by outward integer arithmetic on scale `2^96`. Pi itself
is enclosed through Machin's identity and alternating arctangent series,
not supplied digits. With angle reduced to `[-pi,pi]`, degree-50 cosine and
degree-51 sine polynomials have rigorous Taylor--Lagrange errors at most
`(22/7)^51/51!` and `(22/7)^52/52!`. Each operation rounds outward. The
remaining phase uncertainty is paid with the Lipschitz constant `2 pi |h|`.
Rational rectangle bounds and integer square roots bound the modulus.

The predeclared 64 cases are `h=1,...,16` on blocks `[1,256]`, `[257,512]`,
`[513,1024]` and `[1,1024]`. Every normalized modulus is strictly below 1/4;
the largest certified upper bound is **0.102382**, at `h=2`, `[1,256]`.
Raw real/imaginary integer rectangles, scale, counts and rounded outward
modulus bounds are in `receipts/finite-circle.log` (JSON content).

`independent_circle_oracle.py` imports no certificate implementation. It
uses mpmath pi at 1400 decimal digits to extract the 1024 reference phases,
then evaluates characters at 100 digits. All 64 numerical sums lie inside
the certified rectangles, and all three bin tables agree. This numerical
oracle checks implementation; it is not the mathematical authority.

## Controls and claim limits

Known exact quadrant phases calibrate signs, negative interval arithmetic
is tested, tail refinement must nest, and the coherent pure orbit and zero
frequency must not pass cancellation. Eventual dyadic aliases and constant
15-torsion twists retain their exact algebra; rational `1/7` is not a circle
alias, but is not required to fail asymptotic normality.

The successful finite threshold is not an estimate for all N, all h, all
intervals, or all prime windows. Neither these counts nor the positive
Green-tail bridge supply the source-selected signed interaction theorem.
The latter is separately attacked in `signed_crt/` and remains open.
