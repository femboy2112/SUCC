#!/usr/bin/env python3
"""Independent exact controls for X07; imports no cohort implementation.

Finite row-substochastic kernels act on original/current subprobabilities.
The probe checks null domains, likelihoods, trace exchanges and support variance.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from pathlib import Path
import argparse
import hashlib
import json


def matrix(rows):
    rows = tuple(tuple(Q(x) if type(x) in (int, Q) else _bad() for x in row)
                 for row in rows)
    if not rows or not rows[0] or len({len(row) for row in rows}) != 1:
        raise ValueError('nonempty rectangular matrix required')
    if any(x < 0 for row in rows for x in row):
        raise ValueError('negative kernel weight')
    if any(sum(row) > 1 for row in rows):
        raise ValueError('kernel row mass exceeds one')
    return rows


def _bad():
    raise ValueError('exact integer/Fraction required')


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError('carrier dimensions do not compose')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def mass(mu):
    return sum((sum(row, Q(0)) for row in mu), Q(0))


def normalize(mu):
    z = mass(mu)
    if not z:
        return None
    return tuple(tuple(x/z for x in row) for row in mu)


def originals(mu):
    return tuple(sum(row, Q(0)) for row in mu)


def current(mu):
    return tuple(sum((row[j] for row in mu), Q(0)) for j in range(len(mu[0])))


def original_support(mu):
    return frozenset(i for i, row in enumerate(mu) if any(row))


def identity(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def path_sum(mu, kernels):
    """Independent enumeration over every hidden path, without matrix products."""
    if not kernels:
        return mu
    result = [[Q(0)]*len(kernels[-1][0]) for _ in mu]
    def visit(original, state, depth, weight):
        if depth == len(kernels):
            result[original][state] += weight
            return
        for after, probability in enumerate(kernels[depth][state]):
            if probability:
                visit(original,after,depth+1,weight*probability)
    for original, row in enumerate(mu):
        for state, weight in enumerate(row):
            if weight:
                visit(original,state,0,weight)
    return tuple(tuple(row) for row in result)


def atomic_support_product(a, b):
    return tuple(tuple(any(a[i][k] > 0 and b[k][j] > 0
                           for k in range(len(b))) for j in range(len(b[0])))
                 for i in range(len(a)))


def rational_grid_checks():
    row_options = [(Q(i, 2), Q(j, 2)) for i in range(3) for j in range(3-i)]
    kernels = tuple(matrix(rows) for rows in product(row_options, repeat=2))
    laws = [tuple(tuple(Q(o == a and x == b) for x in range(2)) for o in range(2))
            for a, b in product(range(2), repeat=2)]
    laws += [((Q(1,2),Q(0)),(Q(0),Q(1,2))),
             ((Q(0),Q(1,2)),(Q(1,2),Q(0))),
             ((Q(1,4),Q(1,4)),(Q(1,4),Q(1,4)))]
    result = {'kernels':len(kernels), 'ordered_kernel_pairs':0, 'commuting_pairs':0,
              'law_composition_checks':0, 'positive_normalization_checks':0,
              'null_composition_checks':0, 'support_composition_checks':0}
    for a, b in product(kernels, repeat=2):
        ab, ba = multiply(a,b), multiply(b,a)
        result['ordered_kernel_pairs'] += 1
        result['commuting_pairs'] += ab == ba
        # Point-mass preparations force every matrix entry in the converse.
        assert (ab == ba) == all(multiply(mu,ab) == multiply(mu,ba) for mu in laws[:4])
        assert tuple(tuple(x > 0 for x in row) for row in ab) == atomic_support_product(a,b)
        result['support_composition_checks'] += 1
        for mu in laws:
            first = multiply(mu,a)
            final = multiply(first,b)
            assert final == path_sum(mu,(a,b)) == multiply(mu,ab)
            assert original_support(final) <= original_support(first) <= original_support(mu)
            result['law_composition_checks'] += 1
            once = normalize(final)
            staged = None if normalize(first) is None else normalize(multiply(normalize(first),b))
            assert once == staged
            if once is None:
                result['null_composition_checks'] += 1
            else:
                assert mass(first) > 0
                second_mass = mass(multiply(normalize(first),b))
                assert mass(final) == mass(first)*second_mass
                result['positive_normalization_checks'] += 1
    return result


def coordinate_kernel(axis, outcome, n=3):
    """Noisy local bit read and reset; row mass depends on the initial bit."""
    size = 2**n
    rows = [[Q(0)]*size for _ in range(size)]
    for x in range(size):
        bit = (x >> axis) & 1
        likelihood = Q(3,4) if bit == outcome else Q(1,4)
        rows[x][x & ~(1 << axis)] = likelihood
    return matrix(rows)


def trace_dag_checks():
    # a<c and b<d; cross-chain events commute on separate coordinates.
    event_axes = {'a':0, 'b':1, 'c':0, 'd':1}
    orders = tuple(order for order in permutations(event_axes)
                   if order.index('a') < order.index('c')
                   and order.index('b') < order.index('d'))
    prior = tuple(tuple(Q(o+1,36) if o == x else Q(0) for x in range(8))
                  for o in range(8))
    checked = 0
    for outcomes in product(range(2), repeat=4):
        events = {event:coordinate_kernel(axis,outcomes[i])
                  for i,(event,axis) in enumerate(event_axes.items())}
        canonical = None
        for order in orders:
            law = path_sum(prior,tuple(events[e] for e in order))
            if canonical is None:
                canonical = law
            assert law == canonical
            product_kernel = identity(8)
            for e in order:
                product_kernel = multiply(product_kernel,events[e])
            assert law == multiply(prior,product_kernel)
            assert normalize(law) is not None
            checked += 1
    return {'events':4,'linear_extensions':len(orders),'outcome_assignments':16,
            'joint_law_and_posterior_checks':checked,
            'note':'fixed named events; only declared a<c and b<d dependencies'}


def boundary_controls():
    read0 = matrix(((1,0),(0,0)))
    flip = matrix(((0,1),(1,0)))
    reset = matrix(((1,0),(1,0)))
    prior = ((Q(1,2),Q(0)),(Q(0),Q(1,2)))
    before = path_sum(prior,(read0,flip,reset))
    after = path_sum(prior,(flip,read0,reset))
    assert multiply(identity(2),flip) == multiply(flip,identity(2))
    assert mass(before) == mass(after) == Q(1,2)
    assert current(before) == current(after) == (Q(1,2),Q(0))
    assert originals(normalize(before)) == (Q(1),Q(0))
    assert originals(normalize(after)) == (Q(0),Q(1))
    # Positive posterior agreement is strictly weaker than likelihood agreement.
    d = matrix(((Q(1,2),0),(0,Q(1,4))))
    n = matrix(((0,1),(0,0)))
    dn, nd = multiply(d,n), multiply(n,d)
    assert dn != nd and dn == tuple(tuple(2*x for x in row) for row in nd)
    forward, backward = multiply(prior,dn),multiply(prior,nd)
    assert normalize(forward) == normalize(backward)
    assert mass(forward) == Q(1,4) and mass(backward) == Q(1,8)
    # Commuting projectors can produce an impossible event.
    a0 = matrix(tuple(tuple(int(x == y and not (x & 1)) for y in range(4)) for x in range(4)))
    b1 = matrix(tuple(tuple(int(x == y and bool(x & 2)) for y in range(4)) for x in range(4)))
    corr = ((Q(1,2),Q(0),Q(0),Q(0)),(Q(0),Q(0),Q(0),Q(1,2)))
    assert multiply(a0,b1) == multiply(b1,a0)
    null = multiply(corr,multiply(a0,b1))
    assert mass(null) == 0 and normalize(null) is None
    half = matrix(((Q(1,2),),))
    coin = ((Q(1),),)
    finite_masses = []
    for depth in range(17):
        assert mass(coin) == Q(1,2**depth) and original_support(coin) == frozenset((0,))
        finite_masses.append(mass(coin))
        coin = multiply(coin,half)
    # Deterministic instruments do not make a mixed preparation deterministic.
    read1 = matrix(((0,0),(0,1)))
    mixed = ((Q(1,2),Q(1,2)),)
    both = [sorted(original_support(multiply(mixed,k))) for k in (read0,read1)]
    assert both == [[0],[0]]
    pure_supports = []
    for bit in (0,1):
        pure = (tuple(Q(x == bit) for x in range(2)),)
        supports = [sorted(original_support(multiply(pure,k))) for k in (read0,read1)]
        assert supports != both
        pure_supports.append(supports)
    return {'weak_unobserved_commutation':True,
            'mixed_preparation_not_single_F48_preparation':
                {'mixed_outcome_supports':both,'pure_outcome_supports':pure_supports},
            'same_outcome_mass_and_current_law_different_originals':
                {'event_mass':mass(before),'current':current(normalize(before)),
                 'originals_ab':originals(normalize(before)),
                 'originals_ba':originals(normalize(after))},
            'same_normalized_joint_law_different_likelihoods':
                {'ab_mass':mass(forward),'ba_mass':mass(backward)},
            'commuting_null_event':{'mass':0,'posterior':None},
            'positive_finite_prefixes_need_not_give_positive_infinite_event':finite_masses}


def bayes_and_wealth_controls():
    checked, positive, null = 0,0,0
    for p,q in product((Q(0),Q(1,2),Q(1)),repeat=2):
        alpha,beta = (p,1-p),(q,1-q)
        for values in product((Q(0),Q(1,2),Q(1)),repeat=4):
            likelihood = (values[:2],values[2:])
            unnormalized = tuple(tuple(alpha[i]*beta[j]*likelihood[i][j]
                                       for j in range(2)) for i in range(2))
            posterior = normalize(unnormalized)
            checked += 1
            if posterior is None:
                null += 1
                continue
            positive += 1
            support_rows = [i for i in range(2) if alpha[i] > 0]
            support_cols = [j for j in range(2) if beta[j] > 0]
            restricted_rank_one = (len(support_rows) == 1 or len(support_cols) == 1 or
                                   likelihood[0][0]*likelihood[1][1] == likelihood[0][1]*likelihood[1][0])
            rows,cols = originals(posterior),current(posterior)
            ci = all(posterior[i][j] == rows[i]*cols[j] for i,j in product(range(2),repeat=2))
            assert ci == restricted_rank_one
    p_yes,q_yes = Q(1,4),Q(3,4)
    good = p_yes*(q_yes/p_yes)+(1-p_yes)*((1-q_yes)/(1-p_yes))
    bad = p_yes*(q_yes/p_yes)**2+(1-p_yes)*((1-q_yes)/(1-p_yes))**2
    assert good == 1 and bad == Q(7,3)
    assert p_yes > Q(1,9)
    return {'bayes_rank_one_cases':checked,'positive_cases':positive,'null_cases':null,
            'duplicate_lr_expectation':good,'marginal_reuse_expectation':bad,
            'false_wealth_crossing':p_yes,'purported_ville_bound':Q(1,9)}


def encode(value):
    if isinstance(value,Q):
        return str(value)
    if isinstance(value,dict):
        return {key:encode(val) for key,val in value.items()}
    if isinstance(value,(tuple,list)):
        return [encode(val) for val in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    receipt = {'assignment':'X07','base_commit':'508f16881a4b145dffa13d0d3d336d1abcbda98c',
               'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'method':'exact Fraction arithmetic; no cohort imports',
               'kernel_grid':rational_grid_checks(),'trace_dag':trace_dag_checks(),
               'counterexamples':boundary_controls(),'C18_C23_review':bayes_and_wealth_controls()}
    output = json.dumps(encode(receipt),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(output)
    print(output,end='')


if __name__ == '__main__':
    main()
