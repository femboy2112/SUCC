"""Exact controls for protected-path bounds and finite causal reach.

This is a mathematical probe. It has no device, collapse, or infinite-proof
interpretation. It reuses Gaussian rational arithmetic, but implements path
execution and the comparison oracles separately from the new channel model.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
from random import Random

from twin_correlation_probe import (
    Q, Z, ONE, IM, scalar, matrix, eye, adjoint, multiply, tensor, scaled,
    add, density, trace, diag, apply, inner, norm2, channel,
)


def rotation(t):
    t = F(t)
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    return matrix(((c, -s), (s, c))), c, s


def fresh_step(state, unitary, c, s):
    """Literal basis execution on observer, reference, and private records."""
    result = {}
    for (b, ref, record), amplitude in state.items():
        marks = ((0, ONE),) if b == 0 else ((0, scalar(c)), (1, scalar(s)))
        for flag, weight in marks:
            for out in range(2):
                key = (out, ref, record+(flag,))
                result[key] = result.get(key, Z) + unitary[out][b]*weight*amplitude
    return {key: value for key, value in result.items() if value != Z}


def joint_density(state):
    """Direct partial trace; the input twin used by the probe has norm sqrt2."""
    result = [[Z for _ in range(4)] for _ in range(4)]
    for (b, r, h), x in state.items():
        for (c, s, k), y in state.items():
            if h == k:
                result[2*b+r][2*c+s] += x*y.conj()/2
    return matrix(result)


def partial_b(rho):
    return matrix([[sum((rho[2*a+i][2*a+j] for a in range(2)), Z)
                    for j in range(2)] for i in range(2)])


def basis_gate(n, change):
    result = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for source in range(2**n):
        bits = tuple((source >> (n-1-i)) & 1 for i in range(n))
        target_bits = change(bits)
        target = sum(bit << (n-1-i) for i, bit in enumerate(target_bits))
        result[target][source] = 1
    return matrix(result)


def cnot(n, control, target):
    def change(bits):
        result = list(bits)
        result[target] ^= bits[control]
        return result
    return basis_gate(n, change)


def run():
    counts = Counter()

    def check(group, condition):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group]))

    # The rational bounds come from ||(c-1)I+sJ||<=|c-1|+|s|.
    # Complex branch phases and mixing rotations exercise different channels.
    for length in range(1, 7):
        for denominator in (7, 11, 17, 29):
            state = {(0, 0, ()): ONE, (1, 1, ()): ONE}
            ideal_u = eye(2)
            budget = F(0)
            for step in range(length):
                u, _, _ = rotation(F((-1)**step, 5+step))
                if step % 2:
                    u = multiply(u, diag((ONE, IM)))
                _, c, s = rotation(F(1, denominator+2*step))
                state = fresh_step(state, u, c, s)
                ideal_u = multiply(u, ideal_u)
                budget += abs(1-c)+abs(s)
                check('global_isometry', sum(a.abs2() for a in state.values()) == 2)
            ideal = {(b, r, (0,)*length): ideal_u[b][r]
                     for b in range(2) for r in range(2)}
            keys = set(state) | set(ideal)
            gap = sum((state.get(k, Z)-ideal.get(k, Z)).abs2() for k in keys)/2
            check('path_budget', gap <= budget*budget)
            rho = joint_density(state)
            ideal_v = tuple(ideal_u[b][r] for b in range(2) for r in range(2))
            fidelity = inner(ideal_v, apply(rho, ideal_v))/2
            check('present_probability_bound', fidelity.im == 0)
            check('present_probability_bound', F(0) <= fidelity.re <= 1)
            check('present_probability_bound', 1-fidelity.re <= budget*budget)
            check('present_probability_bound', trace(rho) == ONE)

    # Independent environment-overlap oracle versus literal branch sum.
    overlaps = []
    for t in (F(0), F(1, 2), F(2, 3), F(3, 7)):
        _, c, s = rotation(t)
        overlaps.append((Q(c), Q(s)))
    overlaps += [(IM, Z), (-IM, Z), (Q(F(3, 5), F(4, 5)), Z)]
    product_examples = []
    for length in range(1, 7):
        state = {(0, 0, ()): ONE, (1, 1, ()): ONE}
        gamma = ONE
        previous_modulus = F(1)
        for j in range(length):
            c, s = overlaps[(j+length) % len(overlaps)]
            # Here record_0=|0>, record_1=c|0>+s|1>, so g=conj(c).
            state = fresh_step(state, eye(2), c, s)
            gamma *= c.conj()
            rho = joint_density(state)
            check('fresh_record_product', rho[0][3] == gamma/2)
            check('fresh_record_product', rho[3][0] == gamma.conj()/2)
            check('fresh_record_monotonicity', gamma.abs2() <= previous_modulus)
            previous_modulus = gamma.abs2()
            purity = trace(multiply(rho, rho))
            check('fresh_record_purity', purity == Q((1+gamma.abs2())/2))
        product_examples.append({'length':length, 'gamma_re':str(gamma.re),
                                 'gamma_im':str(gamma.im)})

    # A reversible phase excursion and a reused record both revive coherence.
    state = {(0, 0, ()): ONE, (1, 1, ()): ONE}
    state = fresh_step(state, eye(2), IM, Z)
    check('phase_excursion', joint_density(state)[0][3] == -IM/2)
    state = fresh_step(state, eye(2), -IM, Z)
    check('phase_excursion', joint_density(state)[0][3] == ONE/2)
    cx = cnot(2, 0, 1)
    check('record_reuse', multiply(cx, cx) == eye(4))
    before = (ONE, Z, ONE, Z)
    marked = apply(cx, before)
    check('record_reuse', marked == (ONE, Z, Z, ONE))
    check('record_reuse', apply(cx, marked) == before)

    # Exact causal support identity, valid for all input density matrices.
    x = matrix(((0, 1), (1, 0)))
    z = diag((1, -1))
    x0 = tensor(tensor(x, eye(2)), eye(2))
    final_z = tensor(eye(4), z)
    g12, g01 = cnot(3, 1, 2), cnot(3, 0, 1)
    back_disjoint = multiply(multiply(adjoint(g12), final_z), g12)
    check('causal_cone', multiply(multiply(adjoint(x0), back_disjoint), x0) == back_disjoint)
    coupled = multiply(g12, g01)
    back_coupled = multiply(multiply(adjoint(coupled), final_z), coupled)
    check('causal_cone', multiply(multiply(adjoint(x0), back_coupled), x0) != back_coupled)
    initial = (ONE,) + (Z,)*7
    check('causal_cone', inner(initial, apply(back_coupled, initial)) == ONE)
    changed = apply(x0, initial)
    check('causal_cone', inner(changed, apply(back_coupled, changed)) == -ONE)

    # No-signalling tested with nonunitary CPTP maps, not just local unitaries.
    damp0 = diag((1, F(3, 5)))
    damp1 = matrix(((0, F(4, 5)), (0, 0)))
    p0, p1 = diag((1, 0)), diag((0, 1))
    banks = [(damp0, damp1), (p0, p1), (x,), (diag((ONE, IM)),)]
    rng = Random(2026111216)
    states = [density(tuple(Q(F(rng.randrange(-7, 8), 11),
                              F(rng.randrange(-5, 6), 13)) for _ in range(4)))
              for _ in range(19)]
    states += [density((ONE, Z, Z, ONE)), scaled(eye(4), F(1, 4))]
    for bank in banks:
        check('kraus_calibration',
              sum_matrices([multiply(adjoint(k), k) for k in bank]) == eye(2))
        for rho in states:
            updated = sum_matrices([channel(tensor(k, eye(2)), rho) for k in bank])
            check('no_signalling', partial_b(updated) == partial_b(rho))
            check('no_signalling', trace(updated) == trace(rho))

    # Independently replay the constructive arithmetic superposition code.
    # Literal map k -> (2k/3,0) if 3|k, otherwise (k,1).
    code = [{3:F(3,5),2:F(4,5)}, {6:F(3,5),4:F(4,5)}]
    for logical, vector in enumerate(code, 1):
        actual = {}
        for k, value in vector.items():
            output = (2*(k//3), 0) if k % 3 == 0 else (k, 1)
            actual[output] = actual.get(output, F(0))+value
        check('arithmetic_encoding', actual == {(2*logical, 0):F(3,5),
                                                 (2*logical, 1):F(4,5)})
    check('arithmetic_encoding', sum(v*v for v in code[0].values()) == 1)
    check('arithmetic_encoding', sum(v*v for v in code[1].values()) == 1)
    check('arithmetic_encoding', not (set(code[0]) & set(code[1])))
    return {'schema':'succ.coherent-path-transport.v1', 'status':'PASS',
            'checks':sum(counts.values()), 'checks_by_group':dict(sorted(counts.items())),
            'product_examples':product_examples,
            'scope':'Exact finite calibrations of proved finite-path identities; no physical quantum experiment, objective collapse, infinite meeting, or arithmetic distribution theorem.',
            'interface':'Present joint output after declared frame calibration; private records are traced and no cross-observer history is read.'}


def sum_matrices(items):
    items = tuple(items)
    result = scaled(items[0], 0)
    for item in items:
        result = add(result, item)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = run()
    rendered = json.dumps(report, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end='')
