"""SWM-A05: bounded exact finite Kan witnesses; no production Kan implementation."""
from __future__ import annotations

import hashlib
import itertools as it
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.relational_model_genetics import Capsule, Port, pullback, GeneticsError
from observational_succ.categorical_model_bridges import ModelCapsule, thermal_correspondence
from observational_succ.dynamic_boundary_inverse import star

P = (('declared-a05', 0, 'binary-v1'),)


def functions(a, b):
    """Enumerate all source-preserving maps, including empty-domain maps."""
    for image in it.product(b, repeat=len(a)):
        if all(x[0] == y[0] for x, y in zip(a, image)):
            yield dict(zip(a, image))


def construct(objects, arrows, side, provenance=P):
    """Limit by compatible tuples; colimit by undirected component closure."""
    names = tuple(objects)
    if side == 'right':
        values = tuple((p, row) for p in provenance
                       for row in it.product(*(tuple(x for x in objects[n] if x[0] == p)
                                               for n in names))
                       if all(f[row[names.index(a)]] == row[names.index(b)]
                              for a, b, f in arrows))
        legs = {n: {v: v[1][i] for v in values} for i, n in enumerate(names)}
    else:
        tagged = [(n, x) for n in names for x in objects[n]]
        graph = {v: {v} for v in tagged}
        for a, b, f in arrows:
            for x in objects[a]:
                assert x[0] == f[x][0], 'unlicensed source-changing arrow'
                graph[(a, x)].add((b, f[x])); graph[(b, f[x])].add((a, x))
        components = []; unseen = set(tagged)
        while unseen:
            frontier = [min(unseen)]; component = set()
            while frontier:
                v = frontier.pop()
                if v not in component:
                    component.add(v); frontier.extend(graph[v] - component)
            unseen -= component
            components.append((next(iter(component))[1][0], tuple(sorted(component))))
        values = tuple(sorted(components))
        legs = {n: {x: next(v for v in values if (n, x) in v[1])
                    for x in objects[n]} for n in names}
    return values, legs


def universal_oracle(objects, arrows, side, values, legs, provenance=P):
    """Independent brute factorization: every small (co)cone has one mediator."""
    for a, b, f in arrows:
        if side == 'right':
            if any(f[legs[a][v]] != legs[b][v] for v in values): return False
        elif any(legs[b][f[x]] != legs[a][x] for x in objects[a]): return False
    for n in range(3):
        w = tuple((p, i) for p in provenance for i in range(n))
        choices = [tuple(functions(w, x) if side == 'right' else functions(x, w))
                   for x in objects.values()]
        for family in it.product(*choices):
            cone = dict(zip(objects, family))
            compatible = all(
                all(f[cone[a][x]] == cone[b][x] for x in w) if side == 'right'
                else all(cone[b][f[x]] == cone[a][x] for x in objects[a])
                for a, b, f in arrows)
            if not compatible: continue
            count = 0
            for h in functions(w, values) if side == 'right' else functions(values, w):
                count += all(
                    all(legs[k][h[x]] == cone[k][x] for x in w) if side == 'right'
                    else all(h[legs[k][x]] == cone[k][x] for x in objects[k])
                    for k in objects)
            if count != 1: return False
    return True


def check_pointwise(compatible):
    p = P[0]; a, b, y = (p, 'a'), (p, 'b'), ((p, '0'), (p, '1'))
    F = {'a': (a,), 'b': (b,), 'y': y}
    maps = [('a', 'y', {a: y[0]}), ('b', 'y', {b: y[0 if compatible else 1]})]
    order = {(x, x) for x in ('a', 'b', 'y', 'd', 'u')}
    order |= {('a', 'y'), ('b', 'y'), ('d', 'a'), ('d', 'b'), ('d', 'y')}
    assert all((x, z) in order for x, y0 in order for y1, z in order if y0 == y1)
    result = {}
    for d in ('a', 'b', 'y', 'd', 'u'):
        for side in ('left', 'right'):
            chosen = {c: F[c] for c in F if ((c, d) if side == 'left' else (d, c)) in order}
            arrows = [(a0, b0, f) for a0, b0, f in maps if a0 in chosen and b0 in chosen]
            values, legs = construct(chosen, arrows, side)
            assert universal_oracle(chosen, arrows, side, values, legs)
            result[d + ':' + side] = len(values)
            if d in F: assert len(values) == len(F[d])
    return result


def main():
    positive, hostile = check_pointwise(True), check_pointwise(False)
    assert positive['d:right'] == 1 and hostile['d:right'] == 0
    assert hostile['u:left'] == 0 and hostile['u:right'] == 1
    fake = ((P[0], 'forged-event'),)
    assert not universal_oracle({}, [], 'left', fake, {})
    p = P[0]; a, b, y0, y1 = (p, 'a'), (p, 'b'), (p, '0'), (p, '1')
    conflicting = {'a': (a,), 'b': (b,), 'y': (y0, y1)}
    bad_legs = {'a': {fake[0]: a}, 'b': {fake[0]: b}, 'y': {fake[0]: y0}}
    assert not universal_oracle(conflicting, [('a', 'y', {a: y0}), ('b', 'y', {b: y1})],
                                'right', fake, bad_legs)
    doubled = ((P[0], 'x'), (P[0], 'y'))
    assert not universal_oracle({}, [], 'right', doubled, {})
    p2 = P + (('different-source', 0, 'binary-v1'),)
    terminal, legs = construct({}, [], 'right', p2)
    assert len(terminal) == 2 and universal_oracle({}, [], 'right', terminal, legs, p2)
    assert not tuple(functions(((p2[0], 'same'),), ((p2[1], 'same'),)))
    alias = {'old0': ((P[0], 'a'),), 'old1': ((P[0], 'b'), (P[0], 'c'))}
    alias_sizes = {}
    for side in ('left', 'right'):
        values, legs = construct(alias, [], side)
        assert universal_oracle(alias, [], side, values, legs)
        alias_sizes[side] = len(values)
    assert alias_sizes == {'left': 3, 'right': 2}
    port = (Port('x', ('0', '1')),)
    left = Capsule('A', 'a', P[0][0], 0, 'binary-v1', port, (('0',),))
    right = Capsule('B', 'b', P[0][0], 0, 'binary-v1', port, (('1',),))
    assert pullback(left, right).merged is None
    try:
        Capsule('empty', 'd', P[0][0], 0, 'binary-v1', port, ())
    except GeneticsError: pass
    else: raise AssertionError('empty realization accepted')
    capsule = ModelCapsule(star(), 'electrical_RC', P[0][0], 0, 'binary-v1')
    analogy = thermal_correspondence(capsule, new_source_id='thermal-a05')
    assert not capsule.public_contract()['physical_origin_authenticated']
    assert analogy['target'].source_id != capsule.source_id
    paths = [Path(__file__), ROOT/'observational_succ/categorical_model_bridges.py',
             ROOT/'observational_succ/relational_model_genetics.py',
             ROOT/'provenance/IMPORT_MANIFEST.json', Path(__file__).parent/'A05.md',
             ROOT/'provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md']
    print(json.dumps({'claim_id': 'SWM-A05', 'status': 'TESTED MODEL',
        'parent_sha': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'command': 'python research/2026-10-13/SWARM_ATLAS/A05_probe.py',
        'exit_code': 0, 'positive_pointwise_sizes': positive,
        'contradictory_pointwise_sizes': hostile,
        'two_source_empty_right_size': len(terminal),
        'non_fully_faithful_fold_sizes': alias_sizes,
        'mutations_rejected': ['forged-empty-left-singleton', 'forged-contradictory-right-singleton',
                               'doubled-empty-right', 'source-changing-map'],
        'production_empty_pullback_refused': True, 'production_empty_capsule_refused': True,
        'physical_origin_authenticated': False,
        'oracle_scope': 'All source-preserving mediators for each supplied cone/cocone and apex 0,1,2 rows per source; 20 pointwise cases plus empty controls',
        'full_suite_run': False, 'kernel_proof_run': False,
        'sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}},
        indent=2, sort_keys=True))


if __name__ == '__main__': main()
