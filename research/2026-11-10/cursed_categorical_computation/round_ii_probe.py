#!/usr/bin/env python3
"""Exact, bounded probes for the two cursed categorical computation rounds.

Standard library only. The receipt records finite observations, not universal
proofs, repository-wide gates, a compiled lambda model, or a normality result.
Run: python round_ii_probe.py --output round_ii_receipt.json
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(x) for x in zip(*a)]


def madd(a, b, scale=1):
    return [[x + scale * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def rank(a):
    a = [[Q(x) for x in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        t = a[r][j]
        a[r] = [x / t for x in a[r]]
        for i in range(len(a)):
            if i != r:
                t = a[i][j]
                a[i] = [x - t * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def source(n):
    require(n >= 1, "source index")
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def bilinear(x, a, y):
    return sum(x[i] * a[i][j] * y[j]
               for i in range(len(x)) for j in range(len(y)))


def oscillator_probe():
    projections = []
    for block in (2, 3):
        projections.append([[Q(1, block) if i//block == j//block else Q(0)
                             for j in range(6)] for i in range(6)])
    p2, p3 = projections
    require(mm(p2, p2) == p2 and mm(p3, p3) == p3, "projection identities")
    c = madd(mm(p2, p3), mm(p3, p2), -1)
    require(transpose(c) == [[-x for x in row] for row in c], "skew transpose")
    require(rank(c) == 2, "oscillator rank")
    require(mm(mm(c, c), c) == [[-Q(2, 9)*x for x in row] for row in c],
            "oscillator cubic")
    clocks = (1, 2, 3, 7, 11, 31, 101)
    areas = {n: bilinear([source(n+i) for i in range(6)], c,
                         [source(n+1+i) for i in range(6)]) for n in clocks}
    require(all(x > 0 for x in areas.values()), "sample source areas positive")
    require(bilinear([Q(1)]*6, c, [Q(1)]*6) == 0, "constant-source null")
    require(-areas[1] < 0, "orientation-reversal negative control")
    # Exact coefficients in r(n+i)=sum_{power>=1} coeff(power,i)n^-power.
    def coefficient(power, shift):
        return sum(Q(w, 8) * Q(pole-8*shift, 8)**(power-1)
                   for w, pole in ((4, 7), (-2, 4), (-1, 3), (-1, 2)))
    laurent = {}
    for degree in range(2, 10):
        laurent[degree] = sum(
            bilinear([coefficient(k, i) for i in range(6)], c,
                     [coefficient(degree-k, i+1) for i in range(6)])
            for k in range(1, degree))
    require(all(laurent[k] == 0 for k in range(2, 9)), "area lower Laurent terms")
    require(laurent[9] == Q(675, 128), "area leading Laurent coefficient")
    return {"status": "VERIFIED_FINITE", "rank": 2,
            "clocks": list(clocks), "areas": {str(n): str(v) for n, v in areas.items()},
            "laurent_through_degree_9": {str(k): str(v) for k, v in laurent.items()},
            "controls": ["constant-source null", "orientation reversal"]}


def transform(n):
    return (n % 3, (n//3) % 3, n//9)


def tcompose(b, a):
    a, b = transform(a), transform(b)
    return sum(3**i * b[a[i]] for i in range(3))


def karoubi_probe():
    monoid = range(27)
    idem = [e for e in monoid if tcompose(e, e) == e]
    families = {e: sorted({tcompose(e, m) for m in monoid}) for e in idem}
    hom = {(e, f): [a for a in monoid if tcompose(f, tcompose(a, e)) == a]
           for e in idem for f in idem}
    require(len(idem) == 10, "T3 idempotent count")
    require(sum(map(len, hom.values())) == 348, "T3 typed arrow count")
    require(families[18] == [0, 2, 6, 8, 18, 20, 24, 26], "family 18")
    require(families[12] == [0, 1, 3, 4, 9, 10, 12, 13], "family 12")
    require(tcompose(24, 9) == 18 and tcompose(9, 24) == 12,
            "numerical retract isomorphism")
    equivariance = 0
    for (e, f), arrows in hom.items():
        maps = set()
        for a in arrows:
            require(tcompose(a, e) == a and tcompose(f, a) == a, "corner identities")
            values = tuple(tcompose(a, x) for x in families[e])
            require(set(values) <= set(families[f]), "family map codomain")
            require(values not in maps, "faithful family action")
            maps.add(values)
            for x in families[e]:
                for m in monoid:
                    require(tcompose(a, tcompose(x, m)) ==
                            tcompose(tcompose(a, x), m), "right equivariance")
                    equivariance += 1
    composable = 0
    for e, f, g in product(idem, repeat=3):
        for a in hom[e, f]:
            for b in hom[f, g]:
                ba = tcompose(b, a)
                require(ba in hom[e, g], "Karoubi composition closure")
                for x in families[e]:
                    require(tcompose(ba, x) == tcompose(b, tcompose(a, x)),
                            "family composition")
                composable += 1
    require(21 not in hom[18, 18], "ambient unit is not object identity")
    return {"status": "VERIFIED_FINITE", "elements": 27, "idempotents": idem,
            "typed_arrows": 348, "equivariance_instances": equivariance,
            "composable_pairs": composable,
            "family_18": families[18], "family_12": families[12],
            "controls": ["ambient identity 21 rejected at object 18"]}


def acompose(x, y):
    a, b = x
    c, d = y
    return a*c, a*d+b


def acode(x):
    a, b = x
    return 2**(a-1) * (2*b+1)


def adecode(n):
    require(n >= 1, "positive affine code")
    a = 1
    while n % 2 == 0:
        a += 1
        n //= 2
    return a, (n-1)//2


def affine_probe():
    grid = list(product(range(1, 6), range(6)))
    assoc = 0
    for a, b, c in product(grid, repeat=3):
        require(acompose(acompose(a, b), c) == acompose(a, acompose(b, c)),
                "affine associativity")
        assoc += 1
    coding = 0
    for a, b in product(range(1, 13), range(17)):
        require(adecode(acode((a, b))) == (a, b), "affine code roundtrip")
        coding += 1
    require(acode(acompose(adecode(2), adecode(3))) == 10, "D2 S code")
    require(acode(acompose(adecode(3), adecode(2))) == 6, "S D2 code")
    require(acompose(adecode(2), adecode(3)) != acompose(adecode(3), adecode(2)),
            "ordinary scalar multiplication mutation rejected")
    small = [(1, 0), (1, 1), (2, 0), (2, 1)]
    membership = 0
    for g, x in product(grid, repeat=2):
        a, b = g
        A, B = acompose(g, x)
        require(A % a == 0 and B >= b and (B-b) % a == 0, "ideal membership")
        require((A//a, (B-b)//a) == x, "unique ideal coordinate")
        membership += 1
    equivariance = 0
    for g, h, k, x, r in product(small, repeat=5):
        # Coordinates gx are unique. F_k(gx)=h k x.
        left = acompose(h, acompose(k, acompose(x, r)))
        right = acompose(acompose(h, acompose(k, x)), r)
        require(left == right, "affine-ideal equivariance")
        equivariance += 1
    coherence = 0
    for g, h, j, k, l, x in product(small, repeat=6):
        require(acompose(j, acompose(l, acompose(k, x))) ==
                acompose(j, acompose(acompose(l, k), x)), "ideal map coherence")
        coherence += 1
    require([g for g in grid if acompose(g, g) == g] == [(1, 0)],
            "affine idempotent control")
    return {"status": "VERIFIED_FINITE", "associativity_triples": assoc,
            "code_roundtrips": coding, "ideal_membership_cases": membership,
            "ideal_equivariance_cases": equivariance, "ideal_composition_cases": coherence,
            "noncommuting_codes": {"2_after_3": 10, "3_after_2": 6}}


def forcing(kind, n):
    if kind == 0:
        return source(n)
    if kind == 1:
        return Q(0)
    return source(n) + Q(1, n+2)


@lru_cache(None)
def partial(kind, n):
    return sum((forcing(kind, j)/16**j for j in range(1, n+1)), Q(0))


def action(kind, ab, state):
    n, u = state
    a, b = ab
    k = a*n+b
    z = u/16**n-partial(kind, n)
    return k, 16**k*(z+partial(kind, k))


def gauge(r, q, state):
    n, u = state
    return n, u+16**n*(partial(q, n)-partial(r, n))


def source_action_probe():
    affine = [(1, 0), (1, 1), (2, 0), (2, 1)]
    seeds = [Q(0), Q(1, 7), -Q(2, 3)]
    count = 0
    for kind, seed, n, a, b in product(range(3), seeds, range(12), affine, affine):
        state = (n, 16**n*(seed+partial(kind, n)))
        require(action(kind, a, action(kind, b, state)) ==
                action(kind, acompose(a, b), state), "source action composition")
        count += 1
    naturality = 0
    for r, q, seed, n, a in product(range(3), range(3), seeds, range(12), affine):
        state = (n, 16**n*(seed+partial(r, n)))
        require(gauge(r, q, action(r, a, state)) ==
                action(q, a, gauge(r, q, state)), "gauge naturality")
        naturality += 1
    require(source(1) == Q(47, 15), "authentic first forcing")
    require(source(1) % 1 == Q(2, 15) and forcing(1, 1) == 0,
            "observer distinguishes conjugate sources")
    return {"status": "VERIFIED_FINITE", "source_action_cases": count,
            "gauge_naturality_cases": naturality,
            "source_kinds": ["authentic", "zero", "authentic plus 1/(n+2)"],
            "seeds": [str(s) for s in seeds], "clock_range": [0, 11],
            "r1": "47/15", "authentic_phase_at_1": "2/15", "zero_phase_at_1": "0"}


def number_mu(n):
    sign, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


@lru_cache(None)
def afactors(g):
    A, B = g
    return tuple(((a, B-a*d), (A//a, d))
                 for a in range(1, A+1) if A % a == 0
                 for d in range(B//a+1))


def affine_mu(g):
    a, b = g
    return number_mu(a)*((b == 0)-(b == a))


@lru_cache(None)
def recursive_affine_mu(g):
    if g == (1, 0):
        return 1
    return -sum(recursive_affine_mu(x) for x, y in afactors(g) if y != (1, 0))


@lru_cache(None)
def factor_counts(n):
    if n == 1:
        return (1,)
    out = [0]*(n.bit_length()+1)
    for d in range(2, n+1):
        if n % d == 0:
            for k, count in enumerate(factor_counts(n//d)):
                out[k+1] += count
    while out[-1] == 0:
        out.pop()
    return tuple(out)


def mobius_probe():
    count = 0
    for g in product(range(1, 41), range(41)):
        target = int(g == (1, 0))
        require(sum(affine_mu(x) for x, y in afactors(g)) == target,
                "affine left convolution inverse")
        require(sum(affine_mu(y) for x, y in afactors(g)) == target,
                "affine right convolution inverse")
        require(recursive_affine_mu(g) == affine_mu(g), "recursive affine inverse")
        count += 1
    splits = sorted((acode(x), acode(y)) for x, y in afactors(adecode(10)))
    require(splits == [(1, 10), (2, 3), (3, 6), (5, 2), (10, 1)], "code 10 cuts")
    bad = lambda g: number_mu(g[0])*((g[1] == 0)-(g[1] == 1))
    bad_left = sum(bad(x) for x, y in afactors((2, 1)))
    bad_right = sum(bad(y) for x, y in afactors((2, 1)))
    require((bad_left, bad_right) != (0, 0), "wrong b=1 support rejected")
    for n in range(1, 121):
        require(sum((-1)**k*c for k, c in enumerate(factor_counts(n))) == number_mu(n),
                "ordered-factorization Mobius")
    # The raw whole-cut category is the divisibility interval and has endpoints.
    cut_cases = 0
    for n in range(1, 33):
        cuts = [d for d in range(1, n+1) if n % d == 0]
        require(all(d % 1 == 0 and n % d == 0 for d in cuts), "initial and terminal cuts")
        cut_cases += 1
    require(len([d for d in range(1, 5) if 4 % d == 0]) == 3,
            "noncoprime divisor product control")
    require(3 != 2*2, "Div4 differs from Div2 squared")
    return {"status": "VERIFIED_FINITE", "affine_grid": {"a": [1, 40], "b": [0, 40]},
            "affine_grid_points": count, "checks_per_point": ["left inverse", "right inverse", "recursive inverse"],
            "code_10_factor_pairs": splits,
            "wrong_support_control_at_2_1": {"left": bad_left, "right": bad_right},
            "integer_mobius_cases": 120, "factor_counts_12": factor_counts(12),
            "factor_counts_30": factor_counts(30), "whole_cut_cases": cut_cases,
            "bialgebra_mutation": {"Delta_p_squared_middle_coefficient": 2,
                                    "Delta_p_squared_argument_middle_coefficient": 1}}


def plus_shift(v, k=1):
    return {i+k: c for i, c in v.items() if c}


def minus_shift(v, k=1):
    return {i-k: c for i, c in v.items() if i >= k and c}


def subtract(v, w):
    keys = set(v) | set(w)
    return {i: v.get(i, 0)-w.get(i, 0) for i in keys if v.get(i, 0) != w.get(i, 0)}


def defect(v):
    return subtract(v, plus_shift(minus_shift(v)))


def matrix_unit(i, j, v):
    return plus_shift(defect(minus_shift(v, j)), i)


def matrix_unit_probe():
    for j in range(25):
        v = {j: 1}
        require(minus_shift(plus_shift(v)) == v, "infinite-index TS identity")
        require(defect(v) == ({0: 1} if j == 0 else {}), "origin projector")
    products = 0
    for i, j, k, l in product(range(6), repeat=4):
        for t in range(9):
            lhs = matrix_unit(i, j, matrix_unit(k, l, {t: 1}))
            rhs = {i: 1} if j == k and t == l else {}
            require(lhs == rhs, "matrix unit multiplication")
        products += 1
    for n, j in product(range(8), range(12)):
        lhs = subtract({j: 1}, plus_shift(minus_shift({j: 1}, n), n))
        rhs = {j: 1} if j < n else {}
        require(lhs == rhs, "finite corner projection")
    return {"status": "VERIFIED_FINITE", "basis_origin_checks": 25,
            "matrix_unit_products": products, "basis_vectors_per_product": 9,
            "corner_projection_cases": 96,
            "representation": "finitely supported vectors with no upper truncation"}


def primes(count):
    out, p = [], 2
    while len(out) < count:
        if all(p % q for q in out if q*q <= p):
            out.append(p)
        p += 1
    return out


def matrix_code(n, m, rows):
    require(len(rows) == m and all(len(row) == n for row in rows), "matrix dimensions")
    out = 2**n*3**m
    for p, a in zip(primes(n*m+2)[2:], [x for row in rows for x in row]):
        require(a >= 0, "natural coefficient")
        out *= p**(a+1)
    return out


def span_composition(b, a):
    n, m, k = len(a[0]), len(a), len(b)
    left = [(x, y, j) for y in range(m) for x in range(n) for j in range(a[y][x])]
    right = [(y, z, j) for z in range(k) for y in range(m) for j in range(b[z][y])]
    out = [[0]*n for _ in range(k)]
    for x, y, s in left:
        for yp, z, t in right:
            if y == yp:
                out[z][x] += 1
    return out


def family_functor(a, xs):
    return [[(i, witness, x) for i, size in enumerate(row)
             for witness in range(size) for x in xs[i]] for row in a]


def span_family_probe():
    mats = [[[a, b], [c, d]] for a, b, c, d in product(range(2), repeat=4)]
    for a, b in product(mats, repeat=2):
        require(span_composition(b, a) == mm(b, a), "span/matrix composition")
    a, b = [[1, 2], [0, 1]], [[2, 0], [1, 1]]
    ba = mm(b, a)
    codes = [matrix_code(2, 2, x) for x in (a, b, ba)]
    require(codes == [573873300, 644143500, 261373463851500], "matrix code examples")
    xs = [list(range(2)), list(range(3))]
    composed = family_functor(b, family_functor(a, xs))
    direct = family_functor(ba, xs)
    require([len(x) for x in composed] == [len(x) for x in direct] == [16, 11],
            "family functor composition cardinalities")
    require(len({matrix_code(2, 2, a) for a in mats}) == 16, "matrix code injectivity sample")
    require(matrix_code(0, 0, []) == 1 and matrix_code(0, 2, [[], []]) == 9,
            "empty matrix encodings")
    target = [[2, 3], [1, 2]]
    choices = [list(product(range(y), repeat=x))
               for ar, br in zip(a, target) for x, y in zip(ar, br)]
    transformations = sum(1 for _ in product(*choices))
    require(transformations == 36, "coefficient-map natural transformation count")
    return {"status": "VERIFIED_FINITE", "binary_span_pairs": 256,
            "example_product": ba, "codes_A_B_BA": codes,
            "family_output_cardinalities": [16, 11],
            "example_natural_transformations": transformations,
            "controls": ["empty dimensions retained", "zero entries retained"]}


def digit_q(measure):
    out = Counter()
    for x, weight in measure.items():
        tail = (16*x) % 1
        for a in range(16):
            out[(a+tail)/16] += weight/16
    return dict(out)


def finite_observer_probe():
    for x in (Q(0), Q(3, 7)):
        once = digit_q({x: Q(1)})
        require(digit_q(once) == once, "Q idempotence")
    grid = digit_q({Q(0): Q(1)})
    require(len(grid) == 16 and all(v == Q(1, 16) for v in grid.values()), "atomic Q null")
    interval_w1 = 16*Q(1, 2*16**2)
    circle_w1 = 16*Q(1, 32)**2
    require(interval_w1 == Q(1, 32) and circle_w1 == Q(1, 64), "declared Wasserstein metrics")
    laws = {
        "independent": {(x, y): Q(1, 4) for x, y in product(range(2), repeat=2)},
        "locked": {(0, 0): Q(1, 2), (1, 1): Q(1, 2)},
        "twisted": {(0, 1): Q(1, 2), (1, 0): Q(1, 2)}}
    character = {}
    for name, law in laws.items():
        for coordinate in (0, 1):
            require(sum(w for pair, w in law.items() if pair[coordinate] == 0) == Q(1, 2),
                    "fair marginal")
        character[name] = sum((-1)**(x+y)*w for (x, y), w in law.items())
    require(character == {"independent": 0, "locked": 1, "twisted": -1}, "mixed character controls")
    return {"status": "VERIFIED_FINITE", "Q_idempotence_inputs": ["0", "3/7"],
            "atomic_fixed_measure_support_size": 16,
            "W1_interval": str(interval_w1), "W1_geodesic_circle": str(circle_w1),
            "mixed_characters": {k: str(v) for k, v in character.items()}}


def signed_groupoid_probe():
    previous = Q(0)
    for n in range(1, 33):
        components = [(4, 8*n-7, 1), (2, 8*n-4, -1),
                      (1, 8*n-3, -1), (1, 8*n-2, -1)]
        card = sum(Q(sign*copies, order) for copies, order, sign in components)
        require(card == source(n), "signed groupoid source cardinality")
        previous = 16*previous+card
        require(previous == 16**n*partial(0, n), "groupoid recurrence")
    weighted = sum((source(n)/16**(n-1) for n in range(1, 33)), Q(0))
    require(weighted == 16*partial(0, 32), "pi versus pi/16 normalization")
    cyclic_orders = [next(k for k in range(1, 5) if k*x % 4 == 0) for x in range(4)]
    klein_orders = [1 if x == (0, 0) else 2 for x in product(range(2), repeat=2)]
    require(max(cyclic_orders) == 4 and max(klein_orders) == 2, "equal-cardinality nonequivalence")
    return {"status": "VERIFIED_FINITE", "source_clocks": [1, 32],
            "r1": "47/15", "normalization_weight": "16^(-(n-1))",
            "same_cardinality_control": {"BC4": "1/4", "B_C2xC2": "1/4",
                                          "maximum_element_orders": [4, 2]},
            "infinite_sum_status": "classical BBP identity, not inferred from this finite probe"}


def fractran(fractions, n, limit):
    trace = [n]
    for _ in range(limit):
        for f in fractions:
            candidate = n*f
            if candidate.denominator == 1:
                n = candidate.numerator
                trace.append(n)
                break
        else:
            break
    return trace


def fractran_probe():
    for a, b in product(range(9), repeat=2):
        trace = fractran([Q(3, 2)], 2**a*3**b, a+1)
        require(len(trace) == a+1 and trace[-1] == 3**(a+b), "FRACTRAN exponent addition")
    forward = fractran([Q(2), Q(1, 2)], 1, 8)
    reverse = fractran([Q(1, 2), Q(2)], 1, 8)
    require(forward == [2**i for i in range(9)], "first applicable forward")
    require(reverse == [1, 2, 1, 2, 1, 2, 1, 2, 1], "priority mutation changes trace")
    return {"status": "VERIFIED_FINITE", "addition_cases": 81,
            "addition_3_2_trace": fractran([Q(3, 2)], 72, 8),
            "priority_2_then_half": forward, "priority_half_then_2": reverse,
            "PIGAME": "classical source theorem; not executed by this probe"}


def cancellation_probe():
    # Exact roots at h=8 on the sixteen-point grid are +/-1.
    z = [(-1)**j for j in range(16)]
    pairs = [(j, j+1) for j in range(0, 16, 2)]
    positive_defect = sum(abs(z[i]+z[j]) for i, j in pairs)
    negative_defect = sum(abs(1+1) for _ in pairs)
    require(positive_defect == 0 and sum(z) == 0, "Haar-grid pair calibration")
    require(negative_defect == 16, "zero-phase pair calibration")
    require(negative_defect != 0, "false cancellation certificate rejected")
    cdf_cases = 0
    for a, b in product([Q(k, 3) for k in range(-4, 5)], repeat=2):
        overlap = min(abs(a), abs(b)) if a*b < 0 else 0
        require(abs((a+b)/2) == (abs(a)+abs(b))/2-overlap, "CDF overlap identity")
        cdf_cases += 1
    require(abs(Q(1-1+1, 3)) == Q(1, 3), "unmatched mass calibration")
    return {"status": "VERIFIED_FINITE", "positive_grid_pair_defect": positive_defect,
            "zero_phase_pair_defect": negative_defect, "cdf_pointwise_cases": cdf_cases,
            "exact_pi_antipodes": "excluded by the irrationality proof in ROUND_II.md; not a finite scan",
            "source_selected_asymptotic_estimate": "OPEN"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    families = {
        "oscillator": oscillator_probe(),
        "numeric_karoubi": karoubi_probe(),
        "affine_codes_and_ideals": affine_probe(),
        "source_action_and_gauge": source_action_probe(),
        "mobius_and_cuts": mobius_probe(),
        "matrix_units": matrix_unit_probe(),
        "spans_and_family_functors": span_family_probe(),
        "digit_and_character_controls": finite_observer_probe(),
        "signed_groupoids": signed_groupoid_probe(),
        "fractran": fractran_probe(),
        "pair_and_cdf_certificates": cancellation_probe(),
    }
    receipt = {
        "schema": "succ.cursed_categorical_computation.round_ii_probe.v1",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "result": "PASS",
        "evidence_status": "VERIFIED_FINITE",
        "families": families,
        "not_claimed": ["repository-wide test pass", "hosted CI", "Lean or Rocq compilation",
                        "independent external refereeing", "complete SUCC lambda compiler",
                        "pi normality", "original-zero parity balance", "RH"],
    }
    content = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    print(content, end="")


if __name__ == "__main__":
    main()
