"""Exact finite controls for the proposed terminal-tail norm calibration.

This uses rational surrogate tails to test the generic metric comparison,
plus original BBP forcing for tail bounds. It does not approximate pi or
certify infinite quantifiers. The paper proof is separate.
"""
from fractions import Fraction as Q
from math import prod, isqrt
import json


def r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def distance(t):
    f = t % 1
    return min(f, 1-f)


def norm2(y, B):
    return sum((distance(y / 16**k)**2 for k in range(1, B+1)), Q(0))/B


def root_triangle(E, R, H):
    """Exactly decide |sqrt(E)-sqrt(R)| <= sqrt(H)."""
    if E+R <= H:
        return True
    return (E+R-H)**2 <= 4*E*R


count = 0
mutations_rejected = 0
for B in (1, 2, 3, 7, 16, 31, 64):
    G = Q(1-Q(1,16**(2*B)), 255*B)
    assert G == sum((Q(1,16**(2*k)) for k in range(1,B+1)),Q(0))/B
    for t in (Q(1,1024), Q(1,7), Q(1,2), Q(9,10)):
        H = t*t*G
        for y in (Q(0), Q(1,3), Q(-3,5), Q(8), Q(16**B-1), Q(16**B,2), Q(12345,67)):
            E = norm2(y, B)
            R = norm2(y-t, B)
            assert root_triangle(E,R,H), (B,t,y)
            count += 1
        assert norm2(-t,B)==H
        assert not root_triangle(Q(0), norm2(-t,B), Q(0))
        mutations_rejected += 1

tail_rows = []
for B in (1,2,3,16,31,64,128,512):
    n=2*B
    beta = r(n+1)/15
    D = (16*B+1)*(16*B+2)
    assert beta < Q(1,D) < Q(1,256*B*B)
    gap=Q(1,256*B*B)-Q(1,D)
    assert gap >= Q(1,1632*B**3)
    E_lower=gap*gap/(255*B)
    assert E_lower >= Q(1,679173120*B**7)
    # A finite partial tail lies below the true tail; the full upper bound
    # also confines the coherent raw norm below the critical coefficient.
    partial = sum((r(n+j)/16**j for j in range(1,25)),Q(0))
    G=Q(1-Q(1,16**(2*B)),255*B)
    assert partial*partial*G < Q(1,16711680*B**5)
    assert beta*beta*G < Q(1,16711680*B**5)
    tail_rows.append({'B': B, 'scaled_coherent_partial': float(B**5*partial*partial*G),
                      'critical_constant': float(Q(1,16711680))})

for n in range(1,129):
    assert r(n) == Q(120*n*n-89*n+16, prod((2*n-1,4*n-1,8*n-7,8*n-3)))

square_count = 0
for B in range(9, 10000):
    marker = (isqrt(B)+1)**2
    assert B < marker <= 2*B
    assert Q(1,1024*B) >= Q(1,16711680*B**5)
    square_count += 1

print(json.dumps({'square_marker_location_checks':square_count,
                  'generic_norm_controls':count,
                  'zero_error_mutations_rejected':mutations_rejected,
                  'source_bound_shells':len(tail_rows),
                  'source_polynomial_checks':128,
                  'coherent_partial_diagnostics':tail_rows,
                  'scope':'exact finite calibration; not a pi statistical theorem'},indent=2))
