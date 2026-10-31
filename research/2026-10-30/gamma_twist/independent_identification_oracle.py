"""Independent symbolic numerator and determinantal-divisor oracle.

Imports neither the implementation nor its tests. Finite checks support the
paper proof, not a claimed formal kernel certificate.
"""
import json
from itertools import combinations
from functools import reduce
from math import gcd
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

n = s.symbols("n")
den = (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
polys = [s.cancel(4*den/(8*n-8+d)) for d in (1, 4, 5, 6)]
C = s.Matrix([[sum((-1)**(j-i)*s.binomial(j, i)*p.subs(n, 1+i)
                   for i in range(j+1)) for p in polys] for j in range(4)])
divisors, counts = [], []
for size in range(1, 5):
    minors = [int(C.extract(rows, cols).det())
              for rows in combinations(range(4), size)
              for cols in combinations(range(4), size)]
    divisors.append(reduce(gcd, minors))
    counts.append(len(minors))
assert divisors == [1, 4, 768, 23592960]
snf = smith_normal_form(C, domain=s.ZZ)
assert list(snf.diagonal()) == [1, 4, 192, 30720]
assert C*s.Matrix([-51, 3200, -6825, 3696]) == s.Matrix([0, 0, 0, 30720])
for p, column in zip(polys, range(4)):
    expanded = sum(C[j, column]*s.prod(n-1-i for i in range(j))/s.factorial(j)
                   for j in range(4))
    assert s.expand(p-expanded) == 0

# Independently derive the all-Z2 divided difference classification.
A, Cc, D, z, x, y = s.symbols("A C D z x y", integer=True)
B = 4*z-2*D
num = s.expand(sum(a*p/4 for a, p in zip((A, B, Cc, D), polys)))
assert all(v.is_integer is not False for v in s.Poly(num, n).all_coeffs())
cross = s.cancel((num.subs(n, x)*den.subs(n, y)
                -num.subs(n, y)*den.subs(n, x))/(x-y))
# Every coefficient of cross-D is even as a polynomial in all variables.
assert all(int(v) % 2 == 0 for v in s.Poly(s.expand(cross-D), x, y, A, Cc, D, z).coeffs())

print(json.dumps({"status": "PASS", "symbolic_polynomials": list(map(str, polys)),
    "newton_matrix": [list(map(int, C.row(i))) for i in range(4)],
    "minor_counts": counts, "determinantal_divisors": divisors,
    "smith_diagonal": list(map(int, snf.diagonal())),
    "inverse_matrix": [[str(C.inv()[i,j]) for j in range(4)] for i in range(4)],
    "all_Z2_divided_difference_parity": "D modulo 2",
    "authority": "exact symbolic calibration, paper proof separate"}, indent=2))
