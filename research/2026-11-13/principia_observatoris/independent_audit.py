#!/usr/bin/env python3
"""Independent exact finite audit for Principia Observatoris.

The independent oracles below use only the standard library. A separately
counted differential section imports the native module to compare its outputs.
This verifies finite specimens, not the universal manuscript proofs. Counts are
checks with shared mathematical provenance, not independent evidence votes.
"""
from fractions import Fraction as Q
from itertools import product
import json
import random


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def sub(a, b):
    return tuple(tuple(x-y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def row_dot(c, v):
    return sum(x*y for x, y in zip(c, v))


def independent_rank(columns):
    """Fraction-free recursive span dimension, independent of native RREF."""
    if not columns:
        return 0
    rows = [list(row) for row in zip(*columns)]
    rank = 0
    for j in range(len(columns)):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        p = rows[rank][j]
        for i in range(rank+1, len(rows)):
            q = rows[i][j]
            if q:
                rows[i] = [p*x-q*y for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def audit_word_horizon():
    mats = [tuple(tuple(t[2*i+j] for j in range(2)) for i in range(2))
            for t in product((-1, 0, 1), repeat=4)]
    cases = 0
    closure_cases = 0
    for a, b in product(mats, repeat=2):
        levels = [[(1, 0)]]
        for _ in range(4):
            levels.append([mv(m, v) for v in levels[-1] for m in (a, b)])
        early = levels[0]+levels[1]
        whole = [v for level in levels for v in level]
        assert independent_rank(early) == independent_rank(whole)
        for c in ((0, 1), (1, 0), (1, -1)):
            if all(row_dot(c, v) == 0 for v in early):
                assert all(row_dot(c, v) == 0 for v in whole)
                closure_cases += 1
            cases += 1
    sharp = []
    for n in range(2, 9):
        shift = tuple(tuple(int(i == j+1) for j in range(n)) for i in range(n))
        v = (1,)+(0,)*(n-1)
        values = []
        for _ in range(n+2):
            values.append(v[-1])
            v = mv(shift, v)
        assert values[:n-1] == [0]*(n-1) and values[n-1] == 1
        sharp.append({'dimension': n, 'first_nonzero_length': n-1})
    return {'matrix_pairs': len(mats)**2, 'output_cases': cases,
            'zero_prefix_closure_cases': closure_cases, 'sharp_nilpotent_chains': sharp}


def audit_defect_minimum():
    cases = comparisons = 0
    for p in product(range(-2, 3), repeat=2):
        if p == (0, 0):
            continue
        pp = sum(x*x for x in p)
        p_row = (tuple(Q(x) for x in p),)
        pinv = tuple((Q(x, pp),) for x in p)
        projection = sub(eye(2), mm(pinv, p_row))
        for flat in product((-1, 0, 1), repeat=4):
            a = (flat[:2], flat[2:])
            pa = mm(p_row, a)
            opt = mm(pa, pinv)[0][0]
            e = sub(pa, scale(opt, p_row))
            assert e == mm(pa, projection)
            assert mm(e, pinv) == ((0,),)
            lower_squared = sum(x*x for x in e[0])
            for candidate in range(-2, 3):
                diff = sub(pa, scale(candidate, p_row))
                actual_squared = sum(x*x for x in diff[0])
                assert actual_squared == lower_squared+(candidate-opt)**2*pp
                assert actual_squared >= lower_squared
                comparisons += 1
            cases += 1
    # Mutation: a nonorthogonal section gives descent when it exists but need
    # not minimize error. P=(1,0), A=[[0,1],[0,0]], S=(1,1)^T.
    p = ((1, 0),)
    a = ((0, 1), (0, 0))
    bad_section = ((1,), (1,))
    bad_b = mm(mm(p, a), bad_section)[0][0]
    bad_e = sub(mm(p, a), scale(bad_b, p))
    assert sum(x*x for x in bad_e[0]) == 2
    assert sum(x*x for x in mm(p, a)[0]) == 1
    return {'source_map_action_pairs': cases, 'candidate_model_comparisons': comparisons,
            'nonorthogonal_section_mutation_rejected': True}


def audit_word_defect():
    rng = random.Random(61820261113)
    cases = 0
    for _ in range(250):
        n, m, length = 3, 2, rng.randrange(1, 7)
        p = ((1, 0, 1), (0, 1, -1))
        aa = [tuple(tuple(rng.randrange(-2, 3) for _ in range(n)) for _ in range(n))
              for _ in range(length)]
        bb = [tuple(tuple(rng.randrange(-2, 3) for _ in range(m)) for _ in range(m))
              for _ in range(length)]
        ap, bp = eye(n), eye(m)
        for a, b in zip(aa, bb):
            ap, bp = mm(a, ap), mm(b, bp)
        direct = sub(mm(p, ap), mm(bp, p))
        rhs = tuple((Q(0),)*n for _ in range(m))
        for k in range(length):
            left, right = eye(m), eye(n)
            for b in bb[k+1:]:
                left = mm(b, left)
            for a in aa[:k]:
                right = mm(a, right)
            ek = sub(mm(p, aa[k]), mm(bb[k], p))
            rhs = add(rhs, mm(mm(left, ek), right))
        assert direct == rhs
        cases += 1
    return {'ordered_word_cases': cases, 'max_length': 6}


def audit_action_quotient():
    labels = (0, 0, 1)
    congruent = tested = 0
    for flat in product(range(3), repeat=6):
        actions = (flat[:3], flat[3:])
        good = all(labels[a[0]] == labels[a[1]] for a in actions)
        # This enumeration checks every binary word through length four from
        # every fiber pair, including the empty word.
        levels = [(0, 1)]
        all_equal = True
        for depth in range(5):
            all_equal = all_equal and all(labels[x] == labels[y] for x, y in levels)
            levels = [(a[x], a[y]) for x, y in levels for a in actions]
        assert good == all_equal
        congruent += int(good)
        tested += 1
    # Relational image invents a two-edge path by switching representatives.
    edges = {(0, 1), (2, 3)}
    label = (0, 1, 1, 2)
    image = {(label[x], label[y]) for x, y in edges}
    assert (0, 1) in image and (1, 2) in image
    assert not any(x == 0 and y == z and w == 3 for x, y in edges for z, w in edges)
    return {'two_action_three_state_models': tested, 'congruences': congruent,
            'invented_path_mutation_rejected': True}


def branch(k, rho):
    return mm(mm(k, rho), transpose(k))


def diag(rho):
    return tuple(rho[i][i] for i in range(len(rho)))


def classical_matrix(k):
    # Valid for the chosen diagonal-preserving individual Kraus maps only.
    return tuple(tuple(k[j][i]**2 for i in range(len(k))) for j in range(len(k)))


def audit_quantum_instruments():
    z0, z1 = ((1, 0), (0, 0)), ((0, 0), (0, 1))
    flip = ((0, 1), (1, 0))
    damp0, damp1 = ((1, 0), (0, Q(3, 5))), ((0, Q(4, 5)), (0, 0))
    instruments = ((z0, z1), (flip,), (damp0, damp1))
    for inst in instruments:
        total = ((0, 0), (0, 0))
        for k in inst:
            total = add(total, mm(transpose(k), k))
        assert total == eye(2)
    states = []
    for rx, rz in product((Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)), repeat=2):
        if rx*rx+rz*rz <= 1:
            states.append(((Q(1, 2)*(1+rz), rx/2), (rx/2, Q(1, 2)*(1-rz))))
    nodes = 0
    for rho in states:
        frontier = [(rho, diag(rho))]
        for _ in range(4):
            nxt = []
            for quantum, classical in frontier:
                for inst in instruments:
                    for k in inst:
                        qr, cp = branch(k, quantum), mv(classical_matrix(k), classical)
                        assert diag(qr) == cp
                        nxt.append((qr, cp))
                        nodes += 1
            frontier = nxt
    # Sum-channel diagonal closure does not imply branch closure: X measurement.
    plus = ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2)))
    minus = ((Q(1, 2), Q(-1, 2)), (Q(-1, 2), Q(1, 2)))
    assert diag(plus) == diag(minus)
    effect0 = mm(mm(plus, z0), plus)
    effect1 = mm(mm(minus, z0), minus)
    assert effect0[0][1] != 0 and add(effect0, effect1)[0][1] == 0
    assert sum(diag(branch(plus, plus))) == 1
    assert sum(diag(branch(plus, minus))) == 0
    return {'initial_density_matrices': len(states), 'subnormalized_branch_comparisons': nodes,
            'depth': 4, 'sum_only_invariance_mutation_rejected': True}



def audit_native_api():
    # Import after adding only the known repository root, never a network path.
    import sys
    from pathlib import Path
    repo = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(repo))
    from observational_succ import principia_observatoris as native

    singleton_cases = 0
    for flat in product((-1, 0, 1), repeat=9):
        a = (flat[:3], flat[3:6], flat[6:])
        v = (1, 0, 0)
        outputs = []
        for _ in range(5):
            outputs.append(v[-1])
            v = mv(a, v)
        expected = next((i for i, value in enumerate(outputs) if value), None)
        model = native.LinearModel('independent-audit', (a,), ((1,), (0,), (0,)), ((0, 0, 1),))
        result = native.linear_separator(model)
        if expected is None:
            assert result['status'] == 'ZERO_ON_ALL_WORDS'
        else:
            assert result['status'] == 'DISTINGUISHED'
            assert len(result['word']) == expected <= 2
            assert result['response'][0][0] == outputs[expected]
        singleton_cases += 1

    rng = random.Random(991618)
    switched_cases = completion_cases = 0
    for _ in range(400):
        n = rng.randrange(2, 5)
        prep = rng.randrange(1, n+1)
        out = rng.randrange(1, n+1)
        actions = tuple(tuple(tuple(rng.randrange(-1, 2) for _ in range(n)) for _ in range(n))
                        for _ in range(2))
        b = tuple(tuple(rng.randrange(-1, 2) for _ in range(prep)) for _ in range(n))
        c = tuple(tuple(rng.randrange(-1, 2) for _ in range(n)) for _ in range(out))
        model = native.LinearModel('independent-switched-audit', actions, b, c)
        result = native.linear_separator(model)
        current = [((), b)]
        first = None
        for length in range(n):
            for word, state in current:
                response = mm(c, state)
                if first is None and any(x for row in response for x in row):
                    first = length
            current = [(word+(i,), mm(a, state)) for word, state in current
                       for i, a in enumerate(actions)]
        if first is None:
            assert result['status'] == 'ZERO_ON_ALL_WORDS'
            basis = result['basis']
            r = independent_rank(basis)
            assert r == len(basis)
            assert independent_rank(list(basis)+list(zip(*b))) == r
            for a in actions:
                assert independent_rank(list(basis)+[mv(a, v) for v in basis]) == r
        else:
            assert result['status'] == 'DISTINGUISHED'
            assert len(result['word']) == first
            value = b
            for letter in result['word']:
                value = mm(actions[letter], value)
            observed = mm(c, value)
            assert result['response'] == observed
            assert any(row[result['preparation']] for row in observed)
        switched_cases += 1

        completion = native.predictive_completion(c, actions)
        frontier = list(c)
        allrows = list(c)
        for _ in range(n-1):
            frontier = [mm((row,), a)[0] for row in frontier for a in actions]
            allrows += frontier
        expected_rank = independent_rank(allrows)
        basis = completion['basis']
        assert len(basis) == expected_rank
        assert independent_rank(allrows+list(basis)) == expected_rank
        if basis:
            for a, descended in zip(actions, completion['actions']):
                assert mm(basis, a) == mm(descended, basis)
        assert completion['added_coordinates'] == expected_rank-independent_rank(c)
        assert completion['closure_depth'] <= n-independent_rank(c)
        completion_cases += 1

    difference_cases = 0
    for _ in range(150):
        n, m = rng.randrange(1, 4), rng.randrange(1, 4)
        def model_of_size(dim, label):
            actions = tuple(tuple(tuple(rng.randrange(-1, 2) for _ in range(dim))
                                  for _ in range(dim)) for _ in range(2))
            b = tuple((rng.randrange(-1, 2),) for _ in range(dim))
            c = (tuple(rng.randrange(-1, 2) for _ in range(dim)),)
            return native.LinearModel(label, actions, b, c)
        left, right = model_of_size(n, 'left'), model_of_size(m, 'right')
        difference = native.difference_model(left, right)
        result = native.linear_separator(difference)
        frontier = [((), left.initial, right.initial)]
        first = None
        for depth in range(n+m):
            for word, x, y in frontier:
                delta = sub(mm(left.readout, x), mm(right.readout, y))
                assert difference.response(word) == delta
                if first is None and any(value for row in delta for value in row):
                    first = depth
            frontier = [(w+(j,), mm(left.actions[j], x), mm(right.actions[j], y))
                        for w, x, y in frontier for j in range(2)]
        if first is None:
            assert result['status'] == 'ZERO_ON_ALL_WORDS'
        else:
            assert result['status'] == 'DISTINGUISHED' and len(result['word']) == first
        difference_cases += 1

    hankel_cases = 0
    for start in range(1, 6):
        for size in range(1, 7):
            receipt = native.bbp_hankel_ldl(start, size)
            def source(n):
                return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            independent_h = tuple(tuple(source(start+i+j) for j in range(size))
                                  for i in range(size))
            diagonal = tuple(tuple(receipt['diagonal'][i] if i == j else 0
                                   for j in range(size)) for i in range(size))
            assert receipt['matrix'] == independent_h
            assert mm(mm(receipt['lower'], diagonal), transpose(receipt['lower'])) == independent_h
            assert all(d > 0 for d in receipt['diagonal'])
            hankel_cases += 1

    malformed = [lambda: native.matrix(((0.0,),)),
                 lambda: native.matrix(((True,),)),
                 lambda: native.matrix(((1, 2), (3,))),
                 lambda: native.inverse(((1, 2), (2, 4))),
                 lambda: native.right_inverse(((1, 2), (2, 4))),
                 lambda: native.LinearModel('', (), ((1,),), ((1,),)),
                 lambda: native.LinearModel('shape', (((1, 0), (0, 1)),), ((1,),), ((1,),)),
                 lambda: native.bbp_forcing(True),
                 lambda: native.bbp_hankel_ldl(True, 1)]
    for attempt in malformed:
        try:
            attempt()
        except native.ContractError:
            pass
        else:
            raise AssertionError('Malformed native contract accepted')
    return {'all_ternary_3x3_single_action_matrices': singleton_cases,
            'switched_multi_preparation_cases': switched_cases,
            'predictive_completion_cases': completion_cases,
            'two_realization_comparisons': difference_cases,
            'source_hankel_cross_formula_cases': hankel_cases,
            'malformed_contracts_rejected': len(malformed)}


def main():
    result = {
        'scope': 'Exact finite checks; no formal assistant, physical experiment, or novelty certification',
        'word_horizon': audit_word_horizon(),
        'optimal_quotient_defect': audit_defect_minimum(),
        'word_defect': audit_word_defect(),
        'action_quotient': audit_action_quotient(),
        'quantum_instruments': audit_quantum_instruments(),
        'native_differential': audit_native_api(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
