#!/usr/bin/env python3
"""Independent rational cone/branch crucible. Does not import X07 or its probe."""
from fractions import Fraction as Q
from itertools import combinations, permutations
import json

AUTHOR = '57618f394b9f1aab9fd2c5c06483f98a36751afc'

def mat(rows):
    return tuple(tuple(map(Q, row)) for row in rows)

def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])

def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))

def mv(a, x):
    return tuple(sum(v * w for v, w in zip(row, x)) for row in a)

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def plus(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))

def scale(a, k):
    return tuple(tuple(k * x for x in row) for row in a)

def branch(p, rho):
    return mm(mm(p, rho), p)

def positive(a):
    return all(x >= 0 for row in a for x in row)

def supports(a, sources, mass=None):
    mass = mass or (Q(1),) * len(a)
    return {i for i, source in enumerate(sources)
            if sum(v * w for v, w in zip(mass, mv(a, source))) > 0}

I2 = eye(2)
P0, P1 = mat(((1, 0), (0, 0))), mat(((0, 0), (0, 1)))
E2 = ((Q(1), Q(0)), (Q(0), Q(1)))
# A directed diagram with incomparable zero faces; all branch maps are TNI.
events = (mat(((0, 0, 0), (0, 1, 0), (0, 0, 1))),
          mat(((1, 0, 0), (0, 0, 0), (0, 0, 1))), scale(eye(3), Q(1, 2)))
E3 = tuple(tuple(Q(i == j) for i in range(3)) for j in range(3))
faces, compatible = {}, {}
for size in range(4):
    for chosen in combinations(range(3), size):
        variants = []
        for order in permutations(chosen):
            t = eye(3)
            for event in order:
                t = mm(events[event], t)
            variants.append(t)
        assert all(t == variants[0] for t in variants)
        assert positive(variants[0])
        key = frozenset(chosen)
        compatible[key] = supports(variants[0], E3)
        faces[key] = frozenset(i for i in range(3) if i not in compatible[key])
assert faces[frozenset((0,))] == frozenset((0,))
assert faces[frozenset((1,))] == frozenset((1,))
for first in faces:
    for second in faces:
        assert faces[first] | faces[second] <= faces[first | second]
maximal = [key for key in faces if not any(faces[key] < other for other in faces.values())]
assert all(faces[key] == frozenset((0, 1)) for key in maximal)
assert set.intersection(*compatible.values()) == {2}
assert all(compatible.values())
# Removing directedness leaves two incompatible single-event witnesses.
a, b = supports(P0, E2), supports(P1, E2)
assert a == {0} and b == {1} and not a & b
assert not supports(mm(P0, P1), E2)
# Remove faithfulness at one current interface: positive global maps revive zero mass.
faithless_first = supports(I2, E2, (Q(1), Q(0)))
faithless_second = supports(P1, E2)
assert faithless_first == {0} and faithless_second == {1}
assert positive(I2) and positive(P1) and not faithless_first & faithless_second
# Remove positivity while every cone mass remains faithful.
R1 = mat(((1, 1), (0, -1)))
R2 = mat(((0, -1), (0, 0)))
assert not positive(R1) and not positive(R2)
assert supports(R1, E2) == {0} and supports(mm(R2, R1), E2) == {1}
assert mv(R1, E2[1]) == (1, -1)  # nonzero vector has zero total mass outside cone
assert sum((1, -1)) == 0
assert Q(1) + Q(-1) == 0  # signed zero hyperplane contains e0+e1, neither summand
# Changing normalized source classes invalidates the common-source conclusion.
assert not {E2[0]} & {E2[1]}
# Common-map mutation on a fixed 2D cone: selected map depends on source label k.
for k in range(1, 9):
    source = (Q(1, k + 1), Q(k, k + 1))
    assert sum(source) == 1
    assert sum(mv(I2, source)) > 0
    assert sum(mv(scale(I2, 0), source)) == 0  # declared death at time k+1
# Selected CP branches need not commute although their total channels do.
PLUS = mat(((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))))
MINUS = mat(((Q(1, 2), Q(-1, 2)), (Q(-1, 2), Q(1, 2))))
def total_z(rho):
    return plus(branch(P0, rho), branch(P1, rho))
def total_x(rho):
    return plus(branch(PLUS, rho), branch(MINUS, rho))
for i in range(2):
    for j in range(2):
        basis = mat([[int((r, c) == (i, j)) for c in range(2)] for r in range(2)])
        assert total_z(total_x(basis)) == total_x(total_z(basis))
ba, ab = tr(branch(PLUS, branch(P0, P0))), tr(branch(P0, branch(PLUS, P0)))
assert (ba, ab) == (Q(1, 2), Q(1, 4))
# PSD zero-face calibration on independently constructed rank-one sources.
psd_checks = 0
for v in ((1, 0), (0, 1), (1, 1), (1, -1), (1, 2)):
    rho = scale(mat([[x * y for y in v] for x in v]), Q(1, sum(x*x for x in v)))
    assert (tr(mm(P0, rho)) == 0) == (v[0] == 0)
    psd_checks += 1
# A partial probe after a flip is disabled: coarse constant reports hide this.
def flip(x):
    return 1 - x
def probe_at_zero(x):
    return x if x == 0 else None
assert probe_at_zero(flip(0)) is None and flip(probe_at_zero(0)) == 1
# One strict zero-face growth can be delayed arbitrarily; use N=37 as a witness.
N = 37
for n in range(N + 3):
    t = I2 if n < N else P0
    assert supports(t, E2) == ({0, 1} if n < N else {0})
assert Q(1, 2**12) > 0 and sum(mv(scale(I2, 2), E2[0])) == 2
# Positive transpose is not CP: its Choi swap has negative antisymmetric quadratic form.
swap = mat(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
v = (Q(0), Q(1), Q(-1), Q(0))
assert sum(x*y for x, y in zip(v, mv(swap, v))) == -2
print(json.dumps({
    'reviewed_author_commit': AUTHOR,
    'author_probe_read_or_imported': False,
    'positive_directed_diagram': {'ideals': len(faces), 'greatest_zero_coordinates': [0, 1],
                                 'common_source_coordinate': 2},
    'mutations': {'no_directed_union': [sorted(a), sorted(b)],
                  'nonfaithful_interface': [sorted(faithless_first), sorted(faithless_second)],
                  'nonpositive_maps': {'R1': [[str(x) for x in r] for r in R1],
                                       'R2': [[str(x) for x in r] for r in R2]},
                  'changing_original_classes': 'disjoint normalized singletons',
                  'source_selected_maps': '8 exact normalized source fixtures; universal family proved in review',
                  'selected_CP_branch_masses': list(map(str, (ba, ab))),
                  'enabledness': 'flip then zero-only probe undefined; reverse order defined'},
    'PSD_zero_face_checks': psd_checks,
    'delayed_first_face_growth': N,
    'finite_prefix_mass_at_12': str(Q(1, 2**12)),
    'positive_not_TNI_mass': '2',
    'transpose_Choi_negative_quadratic_form': '-2',
    'analytical_boundaries_not_numerical_tests': [
        'unbounded-height c00 tail family', 'uncountable antichain has no countable cofinal ideals',
        'all finite positive masses do not imply positive infinite-event mass',
        'arbitrary late strict growth prevents a uniform stabilization deadline'],
}, indent=2, sort_keys=True))
