#!/usr/bin/env python3
"""Independent exact controls for sharp uniform approximation by rank-d rivals.

No native code, floating point, or fit is used. Cofactors use signed subset
expansion, the attaining recurrence uses Cramer's rule, and Sturm's algorithm
checks the roots of the corrected kernel polynomial on the open unit interval.
These finite cases check the algebra/implementation, not the universal proof.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import factorial
import json


def forcing(n):
    if type(n) is not int or n < 1:
        raise ValueError('Positive integer source index required')
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def det(matrix):
    """Signed subset expansion, including det(empty)=1."""
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    @lru_cache(maxsize=None)
    def subdet(i, columns):
        if not columns:
            return Q(1)
        value = Q(0)
        for j, col in enumerate(columns):
            value += (-1)**j*matrix[i][col]*subdet(i+1, columns[:j]+columns[j+1:])
        return value
    return subdet(0, tuple(range(n)))


def principal(matrix, indices):
    return tuple(tuple(matrix[i][j] for j in indices) for i in indices)


def without(matrix, row, col):
    return tuple(tuple(value for j, value in enumerate(line) if j != col)
                 for i, line in enumerate(matrix) if i != row)


def mv(matrix, vector):
    return tuple(sum((x*y for x, y in zip(row, vector)), Q(0)) for row in matrix)


def inverse_by_cofactors(matrix):
    n = len(matrix)
    base = det(matrix)
    if not base:
        raise ValueError('Singular inverse requested')
    return tuple(tuple((-1)**(i+j)*det(without(matrix, j, i))/base for j in range(n))
                 for i in range(n))


def cramer(matrix, rhs):
    base = det(matrix)
    if not base:
        raise ValueError('No unique recurrence coefficients')
    n = len(matrix)
    return tuple(det(tuple(tuple(rhs[i] if k == j else matrix[i][k]
                                 for k in range(n)) for i in range(n)))/base
                 for j in range(n))


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def remainder(p, q):
    p, q = list(trim(p)), trim(q)
    if not q:
        raise ValueError('Zero polynomial divisor')
    while len(p) >= len(q):
        degree = len(p)-len(q)
        coefficient = p[-1]/q[-1]
        for i, value in enumerate(q):
            p[degree+i] -= coefficient*value
        p = list(trim(p))
    return tuple(p)


def sturm_open_unit_count(poly):
    poly = trim(poly)
    if not poly or not poly[0] or sum(poly) == 0:
        raise ValueError('Require nonzero polynomial without endpoint roots')
    chain = [poly, tuple(i*c for i, c in enumerate(poly) if i)]
    while chain[-1]:
        rem = tuple(-c for c in remainder(chain[-2], chain[-1]))
        if not rem:
            break
        chain.append(rem)
    def variations(values):
        signs = [(v > 0)-(v < 0) for v in values if v]
        return sum(a != b for a, b in zip(signs, signs[1:]))
    return variations([p[0] for p in chain])-variations([sum(p) for p in chain])


def shifted(matrix, t, alternating=True):
    return tuple(tuple(value-t*((-1)**(i+j) if alternating else 1)
                       for j, value in enumerate(row)) for i, row in enumerate(matrix))


def check_case(start, d):
    if type(d) is not int or d < 1 or type(start) is not int or start < 1:
        raise ValueError('Require positive integer start and dimension')
    m = tuple(forcing(start+k) for k in range(2*d+1))
    h = tuple(tuple(m[i+j] for j in range(d+1)) for i in range(d+1))
    assert det(h) > 0
    inv = inverse_by_cofactors(h)
    v = tuple((-1)**i for i in range(d+1))
    assert all(inv[i][j]*v[i]*v[j] > 0 for i in range(d+1) for j in range(d+1))
    q = mv(inv, v)
    assert mv(h, q) == v
    t = 1/sum(v[i]*q[i] for i in range(d+1))
    assert t > 0 and 1/t == sum(abs(x) for row in inv for x in row)
    corrected = shifted(h, t)
    assert all(value == 0 for value in mv(corrected, q))
    assert q[-1] != 0
    minor_count = 0
    for size in range(1, d+2):
        for idx in combinations(range(d+1), size):
            minor = det(principal(corrected, idx))
            assert minor >= 0
            if size == d+1:
                assert minor == 0
            minor_count += 1
    g = principal(corrected, tuple(range(d)))
    assert det(g) > 0
    # Actual stationary recurrence built solely from the corrected prefix.
    target = tuple(m[i]-t*(-1)**i for i in range(2*d+1))
    coeff = cramer(g, target[d:2*d])
    out = list(target[:d])
    for k in range(d+1):
        out.append(sum(coeff[j]*out[k+j] for j in range(d)))
    assert tuple(out) == target
    assert max(abs(x-y) for x, y in zip(m, out)) == t
    assert all(m[k]-out[k] == (-1)**k*t for k in range(2*d+1))
    # q is orthogonal to lower degrees for (1+u)dnu; corrected kernel
    # polynomial's real roots in (0,1) are independently checked by Sturm.
    assert all(sum(q[i]*(m[i+j]+m[i+j+1]) for i in range(d+1)) == 0
               for j in range(d))
    assert sturm_open_unit_count(q) == d
    # Three wrong alternatives are full rank, so cannot be rank-d rivals.
    assert det(shifted(h, t/2)) > 0
    assert det(shifted(h, -t)) > 0
    assert det(shifted(h, t, alternating=False)) > 0
    # The exact-prefix compulsory residual is larger than this uniform error.
    residual = det(h)/det(principal(h, tuple(range(d))))
    assert Q(3, 4**(d+1)-1)*residual <= t < residual
    return t, minor_count


def main():
    samples = [(n, d) for n in (1, 2, 7, 19, 61) for d in range(1, 6)]
    samples += [(123, 6), (1000, 3), (10000, 1)]
    samples += [(100000, d) for d in range(1, 5)]
    minors = 0
    controls = {}
    large = {}
    for n, d in samples:
        t, count = check_case(n, d)
        minors += count
        if (n, d) in ((1, 1), (2, 2)):
            controls[f'N{n}_d{d}'] = str(t)
        if n == 100000:
            leading = Q(15*factorial(d)*factorial(d+1), 64*4**d)
            ratio = t*n**(2*d+2)/leading
            # Only a finite check of this particular large-N control.
            assert Q(99, 100) < ratio < Q(101, 100)
            large[f'd{d}'] = True
    malformed = 0
    for n, d in ((True, 1), (1, False), (0, 1), (1, 0)):
        try:
            check_case(n, d)
        except ValueError:
            malformed += 1
        else:
            raise AssertionError('Malformed index accepted')
    # Source ablation: a single atom lacks the positive invertible Hankel input.
    try:
        inverse_by_cofactors(((Q(1), Q(1, 2)), (Q(1, 2), Q(1, 4))))
    except ValueError:
        singular_mutant_rejected = True
    else:
        raise AssertionError('Singular source accepted')
    print(json.dumps({'status': 'PASS', 'scope': 'finite rational controls only',
                      'source_dimension_cases': len(samples),
                      'corrected_principal_minors': minors,
                      'attaining_companion_recurrences': len(samples),
                      'sturm_open_interval_root_certificates': len(samples),
                      'wrong_perturbations_rejected': 3*len(samples),
                      'malformed_indices_rejected': malformed,
                      'singular_source_mutant_rejected': singular_mutant_rejected,
                      'small_exact_uniform_errors': controls,
                      'N100000_scaled_error_within_one_percent': large},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
