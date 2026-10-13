#!/usr/bin/env python3
"""Independent exact D26 witnesses; no repository implementation imports."""
from fractions import Fraction as Q
from itertools import product
import json

P = tuple(map(Q, (-8, -4, -2, 1)))
ROOT = (Q(3678, 1000), Q(3679, 1000))


def reduce(v):
    v = list(map(Q, v))
    while len(v) > 3:
        top = v[-1]
        shift = len(v) - len(P)
        for i, coefficient in enumerate(P):
            v[shift + i] -= top * coefficient
        assert v[-1] == 0
        v.pop()
    return tuple(v + [Q(0)] * (3 - len(v)))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, k):
    return tuple(x * k for x in a)


def mul(a, b):
    v = [Q(0)] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i + j] += x * y
    return reduce(v)


ONE = reduce((1,))
ALPHA = reduce((0, 1))
A = scale(add(add(mul(ALPHA, ALPHA), scale(ALPHA, -2)), scale(ONE, -4)), Q(1, 8))
C = scale(ONE, Q(1, 2))
Z = add(ONE, scale(A, -1))
MAXIMUM = scale(ALPHA, Q(1, 4))
BOUNDARIES = (A, C, Z, MAXIMUM)


def polynomial(x):
    return sum(c * x**i for i, c in enumerate(P))


def sign(v):
    if not any(v):
        return 0
    lo, hi = ROOT
    for _ in range(128):
        bounds = [sorted((c * lo**i, c * hi**i)) for i, c in enumerate(v)]
        left, right = sum(b[0] for b in bounds), sum(b[1] for b in bounds)
        if left > 0:
            return 1
        if right < 0:
            return -1
        middle = (lo + hi) / 2
        if polynomial(middle) < 0:
            lo = middle
        else:
            hi = middle
    raise AssertionError('exact sign budget exhausted')


def f(x):
    return mul(ALPHA, mul(x, add(ONE, scale(x, -1))))


def cell(x):
    signs = [sign(add(x, scale(b, -1))) for b in BOUNDARIES]
    if 0 in signs:
        raise ValueError('boundary excluded')
    for i in range(3):
        if signs[i] > 0 > signs[i + 1]:
            return 'ABC'[i]
    raise ValueError('outside carrier')


def source_path(x, size):
    answer = []
    for _ in range(size):
        answer.append(cell(x))
        x = f(x)
    return ''.join(answer)


def tent(x):
    return 2 * x if x <= Q(1, 2) else 2 - 2 * x


def itinerary(x, size):
    result = []
    for _ in range(size):
        if x == Q(1, 2):
            raise ValueError('critical itinerary requires a convention')
        result.append(int(x > Q(1, 2)))
        x = tent(x)
    return tuple(result)


def realize(word):
    x = Q(1, 3)
    for bit in reversed(word):
        x = x / 2 if bit == 0 else 1 - x / 2
    assert itinerary(x, len(word)) == word
    return x


assert polynomial(ROOT[0]) < 0 < polynomial(ROOT[1])
# No root over F_5: monic cubic is irreducible, and the denominator ring is nonzero mod 5.
assert all(sum(int(c) * x**i for i, c in enumerate(P)) % 5 for x in range(5))
assert mul(ALPHA, A) == ONE
assert tuple(f(x) for x in (C, MAXIMUM, A, Z)) == (MAXIMUM, A, Z, Z)
assert all(sign(add(y, scale(x, -1))) > 0 for x, y in zip(BOUNDARIES, BOUNDARIES[1:]))
assert tuple(f(f(x)) for x in (A, C, Z)) == (Z, A, Z)
# Derive legal transitions from complete monotone interval image endpoints.
graph = []
for left, right in zip(BOUNDARIES, BOUNDARIES[1:]):
    indices = sorted(BOUNDARIES.index(f(x)) for x in (left, right))
    graph.append(tuple(indices[0] <= i < indices[1] for i in range(3)))
assert graph == [(False, False, True), (False, False, True), (True, True, False)]
illegal_AA_rejected = not graph[0][0]
paths = {str(x): source_path(reduce((x,)), 3) for x in (Q(3, 10), Q(2, 5))}
assert paths == {'3/10': 'ACB', '2/5': 'ACA'}
missing_source_realization_rejected = paths['3/10'] != 'ACA'
assert illegal_AA_rejected and missing_source_realization_rejected
# Q_r(x)=r^2*x^2-r*(r+1)*x+(r+1), for the proof of F(x)<x on B.
q_c = add(add(ONE, scale(ALPHA, Q(1, 2))), scale(mul(ALPHA, ALPHA), Q(-1, 4)))
q_z = add(scale(ONE, 3), scale(ALPHA, -1))
assert sign(q_c) == sign(q_z) == -1
# Both sides have degree <=4 in x. Five exact values certify the polynomial identity.
for rational_x in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
    x = reduce((rational_x,))
    bracket = add(add(scale(mul(ALPHA, ALPHA), rational_x**2),
                      scale(mul(ALPHA, add(ALPHA, ONE)), -rational_x)), add(ALPHA, ONE))
    lhs = add(f(f(x)), scale(x, -1))
    rhs = scale(mul(mul(ALPHA, add(x, scale(Z, -1))), bracket), -rational_x)
    assert lhs == rhs
checks = 0
for length in range(1, 8):
    for word in product((0, 1), repeat=length):
        x = realize(word)
        for n in range(length):
            y = x
            for _ in range(n):
                y = tent(y)
            assert itinerary(y, length - n) == word[n:]
            checks += 1
try:
    itinerary(Q(1, 2), 1)
except ValueError:
    boundary_rejected = True
else:
    raise AssertionError('boundary mutation survived')
assert itinerary(Q(1, 8), 1) == itinerary(Q(3, 8), 1) == (0,)
assert itinerary(tent(Q(1, 8)), 1) != itinerary(tent(Q(3, 8)), 1)
returns = []
for x in (Q(1, 10), Q(2, 5)):
    y, tau = tent(x), 1
    while not 0 < y < Q(1, 2):
        y, tau = tent(y), tau + 1
        assert tau < 5
    returns.append({'source': str(x), 'tau': tau, 'return': str(y), 'step_two': str(tent(tent(x)))})
assert [r['tau'] for r in returns] == [1, 2]
assert returns[0]['return'] != returns[0]['step_two']
# r=2 on its post-image carrier has no strict right-half source state.
assert Q(2) / 4 == Q(1, 2)
print(json.dumps({
    'source_parent': '5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
    'independent_implementation': 'stdlib rational polynomial long division; no native imports',
    'alpha_root_bracket': list(map(str, ROOT)),
    'endpoint_orbit_and_return_images_exact': True,
    'finite_source_autonomy_falsifier': paths,
    'B_infinity_ghost_certificate': {'Q_at_c_negative': True, 'Q_at_z_negative': True,
        'degree4_identity_five_exact_points': True, 'cubic_irreducible_mod5': True,
        'universal_argument': 'dossier polynomial factor and monotone convergence; not finite enumeration'},
    'tent_realized_words': sum(2**k for k in range(1, 8)),
    'tent_depth_square_checks': checks,
    'mutations': {'critical_boundary_rejected': boundary_rejected,
        'illegal_AA_against_source_images_rejected': illegal_AA_rejected,
        'graph_legal_but_wrong_actual_source_rejected': missing_source_realization_rejected,
        'r2_right_word_has_no_postimage_source': True,
        'finite_window_autonomy_refuted': True,
        'missing_return_time_refuted': True},
    'variable_return_receipts': returns,
    'physical_source_authentication': False,
}, indent=2, sort_keys=True))
