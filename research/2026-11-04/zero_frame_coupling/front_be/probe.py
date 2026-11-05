"""Exact rational observer-norm and source-symbol checks; no asymptotic inference."""
from fractions import Fraction as Q
from math import comb, factorial, prod
import argparse
import hashlib
import json
from pathlib import Path

ORIGINAL = tuple(map(Q, (4, 0, 0, -2, -1, -1, 0, 0)))
RADIAL = (Q(2), Q(-2), Q(-1), Q(-2), Q(-1, 2), Q(-1, 2), Q(1, 4), Q(0))
ANGULAR = tuple(a-b for a, b in zip(ORIGINAL, RADIAL))


def source(n, taps):
    return sum((c/Q(8*n-8+j) for j, c in enumerate(taps, 1)), Q(0))


def original_polynomial(n):
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def radial_coefficients(order):
    """Independent formal recurrence z(x+1)-16z(x)=r_rad(x+1).

    This does not use geometric moments of the future tail.
    """
    z = [Q(0)]
    for k in range(1, order+1):
        shifted_forcing = sum((c*Q((-j)**(k-1), 8**k)
                               for j, c in enumerate(RADIAL, 1)), Q(0))
        lower = sum((z[d]*(-1)**(k-d)*comb(k-1, k-d)
                     for d in range(1, k)), Q(0))
        z.append((lower-shifted_forcing)/15)
    return tuple(z)


def lag_coefficient(z, order, lag):
    return sum((z[d]*(-1)**(order-d)*comb(order-1, order-d)*lag**(order-d)
                for d in range(1, order)), Q(0))


def determinant(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    value = Q(1)
    for c in range(len(rows)):
        pivot = next((j for j in range(c, len(rows)) if rows[j][c]), None)
        if pivot is None:
            return Q(0)
        if pivot != c:
            rows[c], rows[pivot] = rows[pivot], rows[c]
            value = -value
        scale = rows[c][c]
        value *= scale
        for j in range(c+1, len(rows)):
            factor = rows[j][c]/scale
            rows[j] = [x-factor*y for x, y in zip(rows[j], rows[c])]
    return value


def maximal_squared(points):
    """Exact square of A-normalized maximal complex subinterval sum."""
    A = len(points)
    if A < 1:
        raise ValueError("nonempty points required")
    prefixes = [(Q(0), Q(0))]
    for x, y in points:
        u, v = prefixes[-1]
        prefixes.append((u+x, v+y))
    return max((prefixes[b][0]-prefixes[a][0])**2+
               (prefixes[b][1]-prefixes[a][1])**2
               for b in range(1, A+1) for a in range(b))/A**2


def observer_case(A):
    points = [(Q((n*n+3*n+1) % 11-5, 7), Q((2*n*n+n) % 13-6, 9))
              for n in range(A, 2*A)]
    weights = [Q(8*A**3, 3*n**3) for n in range(A, 2*A)]
    weighted = [(w*x, w*y) for w, (x, y) in zip(weights, points)]
    plain, observed = maximal_squared(points), maximal_squared(weighted)
    inverse = Q(3*(2*A-1)**3, 8*A**3)
    assert observed <= Q(64, 9)*plain
    assert plain <= inverse**2*observed
    return {"A": A, "plain_max_squared": str(plain),
            "weighted_max_squared": str(observed),
            "exact_inverse_bound": str(inverse), "both_transfer_bounds": True}


def source_rows():
    U = Y = Z = Q(0)
    result = []
    for n in range(1, 114):
        assert source(n, ORIGINAL) == original_polynomial(n)
        U = 16*U + original_polynomial(n)
        Y = 16*Y + source(n, ANGULAR)
        Z = 16*Z + source(n, RADIAL)
        assert U == Y+Z
        if n in (23, 61, 113):
            raw = "|".join(map(str, (U, Y, Z)))
            result.append({"n": n, "unwrapped_source_gluing": True,
                           "exact_state_sha256": hashlib.sha256(raw.encode()).hexdigest()})
    return result


def polynomial_remainder(p, divisor):
    p = list(map(Q, p))
    divisor = list(map(Q, divisor))
    while len(p) >= len(divisor):
        c = p[-1]/divisor[-1]
        offset = len(p)-len(divisor)
        for j, d in enumerate(divisor):
            p[offset+j] -= c*d
        while p and not p[-1]:
            p.pop()
    return tuple(p)


def receipt():
    z = radial_coefficients(8)
    determinants = []
    for m in (5, 6):
        matrix = [[lag_coefficient(z, j+1, ell) for ell in range(1, m+1)]
                  for j in range(1, m+1)]
        actual = determinant(matrix)
        predicted = (-1)**(m*(m+1)//2)*z[1]**m*factorial(m)*prod(
            b-a for a in range(1, m+1) for b in range(a+1, m+1))
        assert actual == predicted
        determinants.append({"m": m, "determinant": str(actual), "predicted_equal": True})
    assert polynomial_remainder(RADIAL[:-1], (2, -4, 1)) == ()
    assert polynomial_remainder(ORIGINAL[:-1], (2, -4, 1)) != ()
    return {"parent": "bc2d7b01b6b0a37cb79994e180758e98681aa68e",
            "status": "exact finite algebra only; selected cancellation OPEN",
            "radial_coefficients": [str(x) for x in z[1:]],
            "determinants": determinants,
            "observer_rows": [observer_case(A) for A in (7, 13, 29)],
            "source_rows": source_rows(),
            "radial_interior_zero_not_shared_by_original": True}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = json.dumps(receipt(), indent=2, sort_keys=True)+"\n"
    if args.write:
        args.write.write_text(result)
    else:
        assert args.verify.read_text() == result, "observer receipt mismatch"
        print("OBSERVER_INVERSION_SYMBOL_RECEIPT_VERIFIED")
