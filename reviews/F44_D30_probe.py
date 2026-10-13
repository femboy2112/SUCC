#!/usr/bin/env python3
"""Independent exact F44 review probe. No imports from F44 or project modules."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))


def outer(v):
    return tuple(tuple(x*y for y in v) for x in v)


def trace(a):
    return sum((a[j][j] for j in range(len(a))), F())


def kron(a, b):
    return tuple(tuple(a[i//len(b)][j//len(b[0])] * b[i%len(b)][j%len(b[0])]
                       for j in range(len(a[0])*len(b[0])))
                 for i in range(len(a)*len(b)))


def reduce(a, subsystem):
    if subsystem == 'Q':
        return tuple(tuple(sum((a[2*i+e][2*j+e] for e in range(2)), F())
                           for j in range(2)) for i in range(2))
    return tuple(tuple(sum((a[2*q+i][2*q+j] for q in range(2)), F())
                       for j in range(2)) for i in range(2))


def branch(rho, k):
    kk = kron(k, ID)
    return multiply(multiply(kk, rho), transpose(kk))


def encode(a):
    return [[str(x) for x in row] for row in a]


ID = matrix(((1, 0), (0, 1)))
X = matrix(((0, 1), (1, 0)))
PLUS = scale(F(1, 2), add(ID, X))
MINUS = scale(F(1, 2), add(ID, scale(-1, X)))
BELL = scale(F(1, 2), outer((1, 0, 0, 1)))
MIXTURE = matrix(((F(1, 2), 0, 0, 0), (0, 0, 0, 0),
                  (0, 0, 0, 0), (0, 0, 0, F(1, 2))))
INSTRUMENTS = (
    (matrix(((1, 0), (0, 0))), matrix(((0, 0), (0, 1)))),
    (PLUS, MINUS),
    (matrix(((1, 0), (0, F(3, 5)))), matrix(((0, F(4, 5)), (0, 0)))),
    (matrix(((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))),),
)


def local_tree(rho, tape, history=(), depth=0):
    """Adaptive common policy, persistent tape, early stop and censored boundary."""
    if depth >= 1 and history[-1][1] == 1:
        return {('halt', len(history), sum(a for a, _ in history) % 2): trace(rho)}
    if depth == 3:
        return {('censored', 3, sum(a for a, _ in history) % 2): trace(rho)}
    action = (tape + depth + sum(y for _, y in history)) % len(INSTRUMENTS)
    outputs = {}
    for y, k in enumerate(INSTRUMENTS[action]):
        for z, p in local_tree(branch(rho, k), tape, history+((action, y),), depth+1).items():
            outputs[z] = outputs.get(z, F()) + p
    return {z: p for z, p in outputs.items() if p}


def destructive_word(source, word):
    """Source is parity class; first read erases the other original bit."""
    initial = ((0, 0), (1, 1)) if source == 0 else ((0, 1), (1, 0))
    out = {}
    for original in initial:
        c = original
        record = ()
        for action in word:
            y = c[action]
            c = (y, 0) if action == 0 else (0, y)
            record += (y,)
        out[record] = out.get(record, F()) + F(1, 2)
    return out


def main():
    half = scale(F(1, 2), ID)
    assert reduce(BELL, 'Q') == reduce(MIXTURE, 'Q') == half
    assert reduce(BELL, 'E') == reduce(MIXTURE, 'E') == half
    for instrument in INSTRUMENTS:
        total = matrix(((0, 0), (0, 0)))
        for k in instrument:
            total = add(total, multiply(transpose(k), k))
            assert reduce(branch(BELL, k), 'Q') == reduce(branch(MIXTURE, k), 'Q')
        assert total == ID
    output_laws = {}
    for source, rho in (('Bell', BELL), ('mixture', MIXTURE)):
        law = {}
        for tape, weight in ((0, F(2, 5)), (1, F(3, 5))):
            for z, p in local_tree(rho, tape).items():
                law[z] = law.get(z, F()) + weight*p
        assert sum(law.values(), F()) == 1
        output_laws[source] = law
    assert output_laws['Bell'] == output_laws['mixture']

    # Independently construct the global gate as a basis permutation.
    perm = (0, 1, 3, 2)
    def cnot(rho):
        return tuple(tuple(rho[perm[i]][perm[j]] for j in range(4)) for i in range(4))
    after = {name: trace(multiply(PLUS, reduce(cnot(rho), 'Q')))
             for name, rho in (('Bell', BELL), ('mixture', MIXTURE))}
    assert after == {'Bell': F(1), 'mixture': F(1, 2)}
    xx_plus = scale(F(1, 2), add(kron(ID, ID), kron(X, X)))
    xx_minus = add(kron(ID, ID), scale(-1, xx_plus))
    probabilities = {name: (trace(multiply(xx_plus, rho)), trace(multiply(xx_minus, rho)))
                     for name, rho in (('Bell', BELL), ('mixture', MIXTURE))}
    assert probabilities == {'Bell': (F(1), F()), 'mixture': (F(1, 2), F(1, 2))}
    domination = add(MIXTURE, scale(F(-1, 2), BELL))
    assert domination == scale(F(1, 4), outer((1, 0, 0, -1)))
    # Rank-one outer factor is an exact PSD certificate, not a floating eigentest.

    # Equal one-time marginals conceal different temporal memory.
    retained = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    refreshed = {k: F(1, 4) for k in product((0, 1), repeat=2)}
    for coordinate in (0, 1):
        assert {y: sum((p for h, p in retained.items() if h[coordinate] == y), F())
                for y in (0, 1)} == {0: F(1, 2), 1: F(1, 2)}
        assert {y: sum((p for h, p in refreshed.items() if h[coordinate] == y), F())
                for y in (0, 1)} == {0: F(1, 2), 1: F(1, 2)}
    assert retained != refreshed

    # Independent ordering/control witness, and original-target reset ambiguity.
    words_checked = 0
    for n in range(5):
        for word in product((0, 1), repeat=n):
            assert destructive_word(0, word) == destructive_word(1, word)
            words_checked += 1
    original_reset_fiber = ((0, 0), (1, 0))
    assert len({c for _, c in original_reset_fiber}) == 1
    assert len({s for s, _ in original_reset_fiber}) == 2

    manuscript = Path('/home/leah/succ_lab/swm-f44/research/2026-10-13/SWARM_ATLAS/F44.md')
    print(json.dumps({
        'review': 'F44_D30', 'author_commit': 'acc1942011cb8fbc7fdcd3e2e48d169af3d74bfc',
        'author_manuscript_sha256': hashlib.sha256(manuscript.read_bytes()).hexdigest(),
        'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_probe_read_or_imported': False, 'arithmetic': 'exact rational matrices',
        'initial_Q_and_E_marginals': encode(half),
        'local_adaptive_stopping_postprocessing_law': [
            {'output': list(z), 'probability': str(p)} for z, p in sorted(output_laws['Bell'].items())],
        'stopping_boundary': 'depth-three censoring; no numerical certification of divergence',
        'CNOT_then_X_plus': {k: str(v) for k, v in after.items()},
        'joint_XX_outcomes': {k: list(map(str, v)) for k, v in probabilities.items()},
        'PSD_domination_certificate': {'matrix': encode(domination),
                                       'factor': 'outer(1,0,0,-1)/4'},
        'target_fibers_XX': {'plus': ['Bell', 'mixture'], 'minus': ['mixture']},
        'memory_control': {'retained_00_probability': '1/2', 'refreshed_00_probability': '1/4',
                           'all_single_time_bit_marginals': ['1/2', '1/2']},
        'destructive_order_words_checked': words_checked,
        'counterfactual_original_pair_targets': {'even': 0, 'odd': 1},
        'reset_current_carrier_count': 1, 'reset_original_target_count': 2,
        'scope': 'bounded exact witnesses; universal claims require the paper arguments'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
