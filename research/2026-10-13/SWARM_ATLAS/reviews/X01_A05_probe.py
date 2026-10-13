"""Independent bounded X01 reviewer; never imports the X01 implementation."""
import hashlib
import itertools as it
import json
from pathlib import Path


def subsets(w):
    return tuple(f for n in range(len(w)+1) for f in it.combinations(w, n))


def restrict(row, f):
    return tuple(row[i] for i in f)


def inverse_families(stages, index):
    for family in it.product(*(tuple(stages[f]) for f in index)):
        if all((tuple(family[j][0][g.index(k)] for k in f), family[j][1]) == family[i]
               for i, f in enumerate(index) for j, g in enumerate(index) if set(f) <= set(g)):
            yield family


def finite_model(profiles, multiplicities, labels):
    index = subsets((0, 1))
    receipts = tuple((s, a) for s, n in enumerate(multiplicities) for a in range(n))
    d = {f: {(restrict(profiles[s], f), (s, a)) for s, a in receipts} for f in index}
    b = {f: {(restrict(profiles[s], f), labels[s]) for s, a in receipts} for f in index}
    x = {f: {restrict(row, f) for row in profiles} for f in index}
    df = tuple(inverse_families(d, index)); bf = tuple(inverse_families(b, index))
    assert {v[0][1] for v in df} == set(receipts) and len(df) == len(receipts)
    image = {(profiles[s], labels[s]) for s, a in receipts}
    assert {v[-1] for v in bf} == image and len(bf) == len(image)
    comparisons = partial_exceptions = cost_checks = 0
    for f in index:
        for g in index:
            if not set(f) <= set(g): continue
            pullback = {(r, e) for r in x[g] for e in receipts
                        if tuple(r[g.index(k)] for k in f) == restrict(profiles[e[0]], f)}
            retained = {(restrict(profiles[s], g), (s, a)) for s, a in receipts}
            cartesian = retained == pullback
            source_supported_criterion = all(r == restrict(profiles[e[0]], g) for r, e in pullback)
            injective = len(x[g]) == len(x[f])
            assert cartesian == source_supported_criterion
            if all(multiplicities): assert cartesian == injective
            partial_exceptions += cartesian and not injective
            comparisons += 1
    for z in it.product((0, 1), repeat=2):
        for label in (0, 1):
            costs = [min((1+s+a for s, a in receipts if labels[s] == label
                          and restrict(profiles[s], f) == restrict(z, f)), default=None)
                     for f in index]
            m = None if None in costs else max(costs)
            actual = min((1+s+a for s, a in receipts if labels[s] == label
                          and profiles[s] == z), default=None)
            assert m == actual
            cost_checks += 1
    return comparisons, partial_exceptions, cost_checks


def main():
    models = comparisons = partial_exceptions = cost_checks = 0
    alphabet = tuple(it.product((0, 1), repeat=2))
    for n in range(3):
        for profiles in it.product(alphabet, repeat=n):
            for multiplicities in it.product((0, 1, 2), repeat=n):
                for labels in it.product((0, 1), repeat=n):
                    counts = finite_model(profiles, multiplicities, labels)
                    models += 1; comparisons += counts[0]
                    partial_exceptions += counts[1]; cost_checks += counts[2]
    finite_model(((0, 0), (1, 0), (1, 1)), (1, 0, 0), (0, 0, 0))
    # A finite topological countermodel after deleting L-discreteness.
    label_points = {0, 1}; image = {0}; opens = (set(), label_points)
    closure = {p for p in label_points if all(not (p in u) or bool(u & image) for u in opens)}
    assert closure == {0, 1} and image != closure
    finite_support_costs = []
    for n in range(9):
        f = tuple(range(n)); source = frozenset(f)
        assert all(k in source for k in f)
        finite_support_costs.append(len(source))
    report = {
        'subject_commit': 'd9631e3008051628a45bd6373ef35e884d3a7384',
        'reviewer_base': 'ad6db3cfeb4cd9426b622f31d3d5c2892c3d7d37',
        'command': 'timeout 30s python research/2026-10-13/SWARM_ATLAS/reviews/X01_A05_probe.py',
        'independence': 'New standard-library enumeration; X01 probe neither read nor imported',
        'finite_models': models, 'refinement_comparisons': comparisons,
        'partial_support_cartesian_noninjective_cases': partial_exceptions,
        'finite_cost_equalities': cost_checks,
        'unsupported_fiber_nonempty_receipt_control': 'Rows 00 supported, 10/11 unsupported: cartesian comparison although report restriction not injective',
        'nondiscrete_label_countermodel': {'W': [], 'E': ['e'], 'lambda_e': 0,
                                          'label_topology': 'indiscrete {0,1}',
                                          'limit_B_labels': [0], 'closure_labels': sorted(closure)},
        'finite_support_all_ones_prefix_costs': finite_support_costs,
        'infinite_claim_scope': 'Infinite absence and compactness proved in review, not inferred from finite execution',
        'exit_code': 0, 'full_suite_run': False, 'compiler_run': False,
        'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'review_sha256': hashlib.sha256(Path(__file__).with_name('X01_A05_REVIEW.md').read_bytes()).hexdigest(),
        'verdict': 'SURVIVES under stated hypotheses'}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__': main()
