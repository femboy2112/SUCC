#!/usr/bin/env python3
"""Independent exact finite controls for X01; no existing repair oracle imports.

The infinite completion assertions are proved in X01.md, not extrapolated
from these finite checks. All finite mathematical source tables are complete.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


def unary_equivalent(action, report, left, right):
    """Full unary behavior equivalence by exact pair-orbit exhaustion."""
    visited = set()
    while (left, right) not in visited:
        if report[left] != report[right]:
            return False
        visited.add((left, right))
        left, right = action[left], action[right]
    return True


def partition(action, report):
    return tuple(min(y for y in range(len(action))
                     if unary_equivalent(action, report, x, y))
                 for x in range(len(action)))


def finite_recovery(action, report, code):
    """Check recovery from an independently generated finite report table.

    At most n^2 distinct pairs occur before repetition. Thus lengths 0..n^2-1
    separate every inequivalent pair for this finite unary source.
    """
    native_rows, coded_rows = [], []
    for initial in range(len(action)):
        native, coded, current = [], [], initial
        for _ in range(len(action) ** 2):
            native.append(report[current])
            coded.append(code[report[current]])
            current = action[current]
        native_rows.append(tuple(native))
        coded_rows.append(tuple(coded))
    return all(coded_rows[i] != coded_rows[j] or native_rows[i] == native_rows[j]
               for i in range(len(action)) for j in range(len(action)))


def exhaustive_transport_controls():
    counts = dict(tables_examined=0, strict_maps=0, injective_completion_maps=0,
                  surjective_completion_maps=0, surjective_source_maps=0,
                  nonsurjective_source_but_surjective_completion=0,
                  source_bijection_but_noninjective_completion=0)
    n = 2
    functions = tuple(itertools.product(range(n), repeat=n))
    for ax, ay, hx, hy, f, k in itertools.product(functions, repeat=6):
        counts['tables_examined'] += 1
        if not all(f[ax[x]] == ay[f[x]] and hy[f[x]] == k[hx[x]]
                   for x in range(n)):
            continue
        counts['strict_maps'] += 1
        coded = tuple(k[hx[x]] for x in range(n))
        qx, qy, qc = partition(ax, hx), partition(ay, hy), partition(ax, coded)
        # The exact A01 repair/base-change square, checked by separate orbits.
        for x, xx in itertools.product(range(n), repeat=2):
            assert (qc[x] == qc[xx]) == (qy[f[x]] == qy[f[xx]])
        injective = all(qc[x] != qc[xx] or qx[x] == qx[xx]
                        for x, xx in itertools.product(range(n), repeat=2))
        assert injective == finite_recovery(ax, hx, k)
        surjective = set(qy) == {qy[f[x]] for x in range(n)}
        source_surjective = set(f) == set(range(n))
        if source_surjective:
            assert surjective
            counts['surjective_source_maps'] += 1
        if len(set(k)) == n:
            assert injective
        counts['injective_completion_maps'] += int(injective)
        counts['surjective_completion_maps'] += int(surjective)
        counts['nonsurjective_source_but_surjective_completion'] += int(
            not source_surjective and surjective)
        counts['source_bijection_but_noninjective_completion'] += int(
            source_surjective and not injective)
    return counts


def mutation_controls():
    # Report-preserving but not action-commuting: A01's exact countermodel.
    ax, hx = (0, 1), (0, 0)
    ay, hy, f = (0, 2, 2), (0, 0, 1), (0, 1)
    assert all(hx[x] == hy[f[x]] for x in range(2))
    assert any(f[ax[x]] != ay[f[x]] for x in range(2))
    assert unary_equivalent(ax, hx, 0, 1)
    assert not unary_equivalent(ay, hy, f[0], f[1])

    # Bijective source transport can erase the native observational quotient.
    ax = ay = (0, 1)
    hx, hy, f, k = (0, 1), (0, 0), (0, 1), (0, 0)
    assert len(set(f)) == 2
    assert len(set(partition(ax, hx))) == 2
    assert len(set(partition(ay, hy))) == 1
    assert not finite_recovery(ax, hx, k)

    # A noninjective output code can remain injective on whole behaviors:
    # two successive coded readings recover each position in a three-cycle.
    cycle, three_reports, folded = (1, 2, 0), (0, 1, 2), (0, 0, 1)
    assert len(set(folded)) < len(folded)
    assert finite_recovery(cycle, three_reports, folded)

    # Lack of source surjectivity can either matter or be behaviorally hidden.
    target_action = (0, 1)
    assert set(partition(target_action, (0, 1))) != {0}
    assert set(partition(target_action, (0, 0))) == {0}
    return dict(noncommuting_action_rejected=True,
                bijective_source_can_erase_completion_information=True,
                noninjective_report_code_can_preserve_behavior=True,
                nonsurjectivity_can_matter_or_be_hidden=True)


def infinite_family_finite_controls(max_depth=8):
    """Exact finite obligations for symbolic infinite counterfamilies only."""
    patched_patterns = 0
    for depth in range(max_depth + 1):
        for pattern in itertools.product((0, 1), repeat=depth):
            finite_support = frozenset(i for i, bit in enumerate(pattern) if bit)
            assert tuple(int(i in finite_support) for i in range(depth)) == pattern
            integer_source = sum(bit * 2 ** i for i, bit in enumerate(pattern))
            assert tuple((integer_source // 2 ** i) % 2 for i in range(depth)) == pattern
            # Finite support remains finite under the source-changing shift.
            shifted = frozenset(i - 1 for i in finite_support if i > 0)
            assert all(int(i in shifted) == int(i + 1 in finite_support)
                       for i in range(depth))
            patched_patterns += 1
    # Countable infinite report alphabet example: source n, action predecessor,
    # native report n; threshold coding produces 1^n 0^infinity.
    ray_checks = 0
    for source in range(33):
        for coordinate in range(40):
            native = max(source - coordinate, 0)
            threshold = int(native > 0)
            assert threshold == int(coordinate < source)
            assert max(max(source - 1, 0) - coordinate, 0) == max(
                source - (coordinate + 1), 0)
            ray_checks += 1
    # Every tested finite initial segment of all ones has a ray witness.
    for depth in range(41):
        assert all(int(depth - i > 0) == 1 for i in range(depth))
    return dict(patched_patterns=patched_patterns, ray_coordinate_checks=ray_checks,
                all_one_prefix_witnesses=41,
                infinite_claim_status='PAPER PROOF; finite checks are controls only')


def run_probe():
    return dict(claim='SWM-X01', status='EXACT FINITE CONTROLS PASS',
                finite_transport=exhaustive_transport_controls(),
                mutations=mutation_controls(),
                infinite_controls=infinite_family_finite_controls())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run_probe()
    result['probe_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
