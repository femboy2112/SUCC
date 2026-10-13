"""Bounded exact witnesses for A07; no universal theorem inferred from tests."""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.noncommuting_proof_transport import (
    EventRecord, FiniteCarrier, Instrument, factor_original_claim, finite_separator,
)
from observational_succ.quantum_records import (
    INITIAL_ZERO, QuantumObserver, causal_noncommutativity_probe,
    measure_x, measure_z,
)


@dataclass
class Span:
    X: tuple
    Y: tuple
    E: dict  # token -> (input, output, record word, exact weight)

    def validate(self):
        assert len(set(self.X)) == len(self.X) and self.X
        assert len(set(self.Y)) == len(self.Y) and self.Y
        for x, y, h, w in self.E.values():
            assert x in self.X and y in self.Y and isinstance(h, tuple)
            assert isinstance(w, Q) and w >= 0
        for x in self.X:
            assert sum((w for a, _, _, w in self.E.values() if a == x), Q()) == 1
        return self


def compose(P, R):
    assert P.Y == R.X
    return Span(P.X, R.Y, {
        (e, f): (x, z, h + k, w * v)
        for e, (x, y, h, w) in P.E.items()
        for f, (yy, z, k, v) in R.E.items() if y == yy
    }).validate()


def identity(X):
    return Span(X, X, {x: (x, x, (), Q(1)) for x in X}).validate()


def cell(P, R, a):
    assert P.X == R.X and P.Y == R.Y and set(a) == set(P.E)
    mass = defaultdict(Q)
    for e, ep in a.items():
        assert ep in R.E and P.E[e][:3] == R.E[ep][:3]
        mass[ep] += P.E[e][3]
    assert all(mass[ep] == row[3] for ep, row in R.E.items())
    return a


def vertical(a, b):
    return {e: b[ep] for e, ep in a.items()}


def horizontal(P, R, a, b):
    return {(e, f): (a[e], b[f]) for e, f in compose(P, R).E}


def kernel(P):
    out = defaultdict(Q)
    for x, y, h, w in P.E.values():
        out[x, y, h] += w
    return dict(out)


def kernel_compose(A, B):
    out = defaultdict(Q)
    for (x, y, h), w in A.items():
        for (yy, z, k), v in B.items():
            if y == yy:
                out[x, z, h + k] += w * v
    return dict(out)


def level(n, name):
    return Span((0, 1), (0, 1), {
        (x, i): (x, 1-x, (name + ':0',), Q(1, n))
        for x in (0, 1) for i in range(n)
    }).validate()


def assoc(t):
    (a, b), c = t
    return a, (b, c)


def rejects(P, R, a):
    try:
        cell(P, R, a)
    except AssertionError:
        return True
    raise AssertionError('Hostile 2-cell accepted')


def quantum_span(X, I, epoch):
    rows = {}
    for i, rho in enumerate(X):
        for outcome, prob in I.probabilities(rho).items():
            if prob:
                p, post = I.event(rho, outcome)
                assert p == prob
                rows[i, outcome] = (rho, post, (f'{epoch}:{I.name}:{outcome}',), p)
    Y = tuple(dict.fromkeys(row[1] for row in rows.values()))
    return Span(X, Y, rows).validate()


def deterministic_span(field, name, epoch):
    I = field.action(name)
    X = tuple(range(field.count))
    assert all(I.enabled)
    return Span(X, X, {x: (x, I.transitions[x],
                (EventRecord(name, I.outputs[x], epoch, field.source_id, field.basis_id),), Q(1))
                for x in X}).validate()


def main():
    levels = {name: [level(n, name) for n in (4, 2, 1)] for name in 'ABCD'}
    P, R, S, T = (levels[name][0] for name in 'ABCD')
    p, r = levels['A'][1], levels['B'][1]
    pp, rr = levels['A'][2], levels['B'][2]
    a = cell(P, p, {(x, i): (x, i % 2) for x, i in P.E})
    aa = cell(p, pp, {(x, i): (x, 0) for x, i in p.E})
    b = cell(R, r, {(x, i): (x, i % 2) for x, i in R.E})
    bb = cell(r, rr, {(x, i): (x, 0) for x, i in r.E})
    ab = cell(compose(P, R), compose(p, r), horizontal(P, R, a, b))
    aabb = cell(compose(p, r), compose(pp, rr), horizontal(p, r, aa, bb))
    interchange = vertical(ab, aabb)
    assert interchange == horizontal(P, R, vertical(a, aa), vertical(b, bb))
    cell(compose(P, R), compose(pp, rr), interchange)
    L, U = compose(compose(P, R), S), compose(P, compose(R, S))
    cell(L, U, {e: assoc(e) for e in L.E})
    cell(U, L, {(a, (b, c)): ((a, b), c) for a, (b, c) in U.E})
    lower = compose(compose(pp, rr), levels['C'][2])
    c = cell(S, levels['C'][2], {(x, i): (x, 0) for x, i in S.E})
    maps = {((e, f), g): ((vertical(a, aa)[e], vertical(b, bb)[f]), c[g])
            for (e, f), g in L.E}
    cell(L, lower, maps)
    upper = compose(pp, compose(rr, levels['C'][2]))
    right_maps = cell(U, upper, {(e, (f, g)): (vertical(a, aa)[e],
                       (vertical(b, bb)[f], c[g])) for e, (f, g) in U.E})
    assert vertical(maps, {t: assoc(t) for t in lower.E}) == vertical(
        {t: assoc(t) for t in L.E}, right_maps)
    four = compose(compose(compose(P, R), S), T)
    final = compose(P, compose(R, compose(S, T)))
    pentagon = {}
    for (((a0, b0), c0), d0) in four.E:
        start = (((a0, b0), c0), d0)
        short = assoc(assoc(start))
        stage = assoc((assoc(start[0]), start[1]))
        long = stage[0], assoc(stage[1])
        assert short == long
        pentagon[(((a0, b0), c0), d0)] = short
    cell(four, final, pentagon)
    unit = identity(P.Y)
    tri = compose(compose(P, unit), R)
    triangle = {((e, y), f): (e, f) for (e, y), f in tri.E}
    assert all((assoc(t)[0], assoc(t)[1][1]) == (t[0][0], t[1]) == triangle[t] for t in tri.E)
    cell(tri, compose(P, R), triangle)
    for Z in (P, R, identity(P.X)):
        l, u = compose(identity(Z.X), Z), compose(Z, identity(Z.Y))
        cell(l, Z, {(x, e): e for x, e in l.E})
        cell(u, Z, {(e, y): e for e, y in u.E})
    assert kernel(compose(P, R)) == kernel_compose(kernel(P), kernel(R))
    skew = Span(p.X, p.Y, {e: row[:3] + (Q(1, 3) if e[1] == 0 else Q(2, 3),)
                         for e, row in p.E.items()}).validate()
    assert rejects(P, skew, a)  # Equal endpoint/record law, incompatible apex masses.
    wrong_label = Span(p.X, p.Y, {e: row[:2] + (('forged',), row[3])
                                for e, row in p.E.items()}).validate()
    assert rejects(P, wrong_label, a)
    law1 = Span((0,), (0, 1), {i: (0, i, ('r',), Q(1, 2)) for i in (0, 1)}).validate()
    law2 = Span((0,), (0, 1), {i: (0, i, ('r',), Q(i+1, 3)) for i in (0, 1)}).validate()
    assert set(kernel(law1)) == set(kernel(law2)) and kernel(law1) != kernel(law2)
    assert rejects(law1, law2, {0: 0, 1: 1})
    field = FiniteCarrier(2, (Instrument('Blind', (0, 0), (1, 0), (True, True)),
                             Instrument('Read', (0, 1), (0, 1), (True, True))),
                          'A07-declared-source', 'bit-v1')
    h0, h1 = (field.run(x, ('Blind',)) for x in (0, 1))
    assert h0.public_signature == h1.public_signature
    assert (h0.initial_source, h1.initial_source) == (0, 1)
    assert (h0.terminal_state, h1.terminal_state) == (1, 0)
    futures = [field.run(x, ('Blind', 'Read')).observed_values for x in (0, 1)]
    assert futures == [(0, 1), (0, 0)] and finite_separator(field, 0, 1) == ('Read',)
    assert not factor_original_claim(field, (0, 1), ('0', '1'), ('Blind',),
                                     target_id='original-bit').valid
    assert factor_original_claim(field, (0, 1), ('0', '1'), ('Blind', 'Read'),
                                 target_id='original-bit').valid
    native_span = compose(deterministic_span(field, 'Blind', 1), deterministic_span(field, 'Read', 2))
    for x in (0, 1):
        trace = field.run(x, ('Blind', 'Read'))
        row = native_span.E[x, 1-x]
        assert row == (x, trace.terminal_state, trace.records, Q(1))
    X = quantum_span((INITIAL_ZERO,), measure_x(), 1)
    XZ = compose(X, quantum_span(X.Y, measure_z(), 2))
    Z = quantum_span((INITIAL_ZERO,), measure_z(), 1)
    ZX = compose(Z, quantum_span(Z.Y, measure_x(), 2))
    assert [w for _, _, h, w in XZ.E.values() if h == ('1:X:plus', '2:Z:zero')] == [Q(1, 4)]
    assert [w for _, _, h, w in ZX.E.values() if h == ('1:Z:zero', '2:X:plus')] == [Q(1, 2)]
    direct = QuantumObserver.initial_state().advance(measure_x(), 'plus')
    longer = QuantumObserver.initial_state().advance(measure_z(), 'zero').advance(measure_x(), 'plus')
    assert direct.state == longer.state and direct.records != longer.records
    assert direct.verify({'X': measure_x(), 'Z': measure_z()})
    assert longer.verify({'X': measure_x(), 'Z': measure_z()})
    paths = ['observational_succ/noncommuting_proof_transport.py', 'observational_succ/quantum_records.py',
             'observational_succ/yoneda.py', 'observational_succ/causal_nerode_succ.py',
             'provenance/IMPORT_MANIFEST.json', str(Path(__file__).relative_to(ROOT))]
    receipt = {'claim_id': 'SWM-A07', 'parent_sha': '5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
               'command': 'python research/2026-10-13/SWARM_ATLAS/A07_probe.py',
               'command_exit': 0,
               'status': 'TESTED MODEL; universal statements have separate paper proofs',
               'interchange_points': len(interchange), 'pentagon_points': len(pentagon),
               'triangle_points': len(triangle), 'hostile_cells_rejected': 3,
               'counterexample': {'originals': [0, 1], 'currents': [1, 0], 'common_report': [['Blind', 0, 1]],
                                  'extended_outcomes': futures, 'minimal_states': 2},
               'quantum_order': causal_noncommutativity_probe(),
               'quantum_span_order_weights': ['1/4', '1/2'],
               'native_deterministic_embedding': 'exact EventRecord and endpoint replay for both inputs',
               'actual_hardware_observations': False, 'unperformed_paths_actualized': False,
               'bounds': {'maximum_apex': len(four.E), 'states': 2, 'maximum_depth': 4},
               'sha256': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}}
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
