"""SWM-A03: exact, bounded incidence-kernel probe; no production mutation.

The independent calculation uses rational row reduction, not the native
spanning-forest descent solver. Integer graph incidence has integral
fundamental-cycle vectors; this is asserted, never assumed numerically.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))


def periods(vertices, edges):
    """Exact integer cycle-basis periods for (tail, head, scalar weight)."""
    matrix = [[Fraction(int(v == head) - int(v == tail))
               for tail, head, _ in edges] for v in vertices]
    pivots = []
    row = 0
    for column in range(len(edges)):
        pivot = next((r for r in range(row, len(matrix))
                      if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        divisor = matrix[row][column]
        matrix[row] = [x / divisor for x in matrix[row]]
        for r in range(len(matrix)):
            if r != row:
                multiple = matrix[r][column]
                matrix[r] = [x - multiple * y
                             for x, y in zip(matrix[r], matrix[row])]
        pivots.append(column)
        row += 1
    values = []
    for column in range(len(edges)):
        if column in pivots:
            continue
        cycle = [Fraction(0)] * len(edges)
        cycle[column] = 1
        for r, pivot in enumerate(pivots):
            cycle[pivot] = -matrix[r][column]
        assert all(Fraction(x).denominator == 1 for x in cycle)
        assert all(sum(cycle[k] * (int(v == e[1]) - int(v == e[0]))
                       for k, e in enumerate(edges)) == 0 for v in vertices)
        values.append(int(sum(x * edge[2] for x, edge in zip(cycle, edges))))
    return values


def subgroup_generator(values):
    result = 0
    for value in values:
        result = gcd(result, value)
    return result


def overlap_edges(charts):
    result = []
    for i, j in combinations(range(len(charts)), 2):
        for vertex in sorted(charts[i].keys() & charts[j].keys()):
            result.append((i, j, charts[i][vertex] - charts[j][vertex]))
    return result


def independent_controls():
    count = 0
    flat = 0
    for a, b, c, d in product(range(-2, 3), repeat=4):
        source = [(0, 1, a), (1, 2, b), (2, 0, c), (0, 1, d)]
        source_values = periods(range(3), source)
        wanted = subgroup_generator(source_values)
        edge_charts = [{0: 0, 1: a}, {1: 0, 2: b},
                       {2: 0, 0: c}, {0: 0, 1: d}]
        path_charts = [{0: 0, 1: a, 2: a + b},
                       {2: 0, 0: c, 1: c + d}]
        gauged = [{v: p + 7 * (i + 1) for v, p in chart.items()}
                  for i, chart in enumerate(path_charts)]
        for charts in (edge_charts, path_charts, gauged):
            actual = subgroup_generator(periods(range(len(charts)),
                                                 overlap_edges(charts)))
            assert actual == wanted, (a, b, c, d, wanted, actual)
        for modulus in (2, 3, 5):
            assert all(value % modulus == 0 for value in source_values) == (
                wanted % modulus == 0)
        flat += wanted == 0
        count += 1
    return {"source_assignments": count, "cover_and_gauge_comparisons": count * 3,
            "modular_comparisons": count * 3, "flat_assignments": flat,
            "arithmetic": "Fraction row reduction and integer gcd; no floats",
            "largest_incidence_matrix": [4, 7], "label_box": [-2, 2]}


def native_witness():
    from observational_succ.local_global_descent import (
        Chart, Dart, DescentError, VoltageSource, assemble_charts,
        construct_chart, verify_result,
    )
    from observational_succ.constructive_gluing_tower import run_diagonal_tower

    menu = (2, 3)
    lost = lcm(*menu)
    graph = VoltageSource("SWM-A03-lcm-two-dart", (0, 1),
                          (Dart("a", 0, 1, (1,)),
                           Dart("b", 0, 1, (1 + lost,))), 1)
    charts = tuple(construct_chart(graph, key, (key,)) for key in ("a", "b"))
    result = assemble_charts(graph, charts)
    verify_result(graph, charts, result)
    assert result.status == "OBSTRUCTED"
    assert abs(result.obstruction.displacement[0]) == lost
    independent_source_periods = periods((0, 1), [(0, 1, 1), (0, 1, 1 + lost)])
    independent_overlap_periods = periods((0, 1), [(0, 1, 0), (0, 1, -lost)])
    assert subgroup_generator(independent_source_periods) == lost
    assert subgroup_generator(independent_overlap_periods) == lost
    collapsed_overlap_periods = periods((0, 1), [(0, 1, 0)])
    assert subgroup_generator(collapsed_overlap_periods) == 0
    native_checks = []
    for modulus in menu + (5,):
        quotient = VoltageSource(f"SWM-A03-projected-{modulus}", (0, 1),
                                tuple(Dart(d.key, d.tail, d.head,
                                           (d.displacement[0] % modulus,))
                                      for d in graph.darts), 1)
        local = tuple(construct_chart(quotient, key, (key,)) for key in ("a", "b"))
        projected = assemble_charts(quotient, local)
        verify_result(quotient, local, projected)
        # Here each reduced label is 1 for the blind moduli, so the native
        # INTEGER solver also passes. This is not a general modular solver.
        expected = "GLUED" if lost % modulus == 0 else "OBSTRUCTED"
        assert projected.status == expected
        native_checks.append({"modulus": modulus, "native_reduced_label_status": projected.status,
                              "true_quotient_period": lost % modulus})
    repaired = VoltageSource("SWM-A03-flat-control", (0, 1),
                             (Dart("a", 0, 1, (1,)), Dart("b", 0, 1, (1,))), 1)
    repaired_charts = tuple(construct_chart(repaired, key, (key,)) for key in ("a", "b"))
    repaired_result = assemble_charts(repaired, repaired_charts)
    verify_result(repaired, repaired_charts, repaired_result)
    assert repaired_result.status == "GLUED"

    # Removing a declared dart must be rejected, not interpreted as flatness.
    coverage_rejected = False
    try:
        assemble_charts(graph, charts[:1])
    except DescentError:
        coverage_rejected = True
    assert coverage_rejected
    # A stale source digest must be rejected even with consistent local math.
    stale = Chart(charts[0].name, repaired.digest, charts[0].vertices,
                  charts[0].dart_ids, charts[0].potentials)
    stale_rejected = False
    try:
        assemble_charts(graph, (stale, charts[1]))
    except DescentError:
        stale_rejected = True
    assert stale_rejected
    # A connected chart receives one gauge. Applying one to a disconnected
    # patch is stronger than the correct componentwise sheaf action.
    disconnected = VoltageSource("SWM-A03-disconnected-gauge", (0, 1), (), 1)
    disconnected_chart = Chart("bad-connected-declaration", disconnected.digest,
                               (0, 1), (), ((0, (0,)), (1, (1,))))
    disconnected_rejected = False
    try:
        assemble_charts(disconnected, (disconnected_chart,))
    except DescentError:
        disconnected_rejected = True
    assert disconnected_rejected

    tower = run_diagonal_tower(graph, levels=2,
                               patches=(("a", ("a",), None),
                                        ("b", ("b",), None)))
    tower_result = tower.proof_at_E()
    assert tower_result.status == "OBSTRUCTED"
    return {"source_id": graph.source_id, "source_digest": graph.digest,
            "vertices": graph.vertices,
            "darts": [[d.key, d.tail, d.head, d.displacement] for d in graph.darts],
            "local_potentials": {c.name: c.potentials for c in charts},
            "overlaps": [[o.left, o.right, o.vertex, o.delta] for o in result.overlaps],
            "native_status": result.status,
            "period_subgroup_generator": lost,
            "independent_source_basis_periods": independent_source_periods,
            "independent_overlap_basis_periods": independent_overlap_periods,
            "one_vertex_overlap_mutation_generator": subgroup_generator(collapsed_overlap_periods),
            "source_walk": result.obstruction.lifted_walk,
            "signed_period": result.obstruction.displacement,
            "overlap_cycle": result.obstruction.cycle,
            "finite_modular_menu": menu, "projected_checks": native_checks,
            "flat_control": repaired_result.status,
            "missing_dart_rejected": coverage_rejected,
            "stale_source_rejected": stale_rejected,
            "disconnected_chart_rejected": disconnected_rejected,
            "native_tower": {"levels": 2, "status": tower_result.status,
                             "epistemic_macros_at_E": tower_result.epistemic_macros_at_E,
                             "expanded_source_steps": tower_result.expanded_obstruction_steps}}


def main():
    started = time.monotonic()
    parent = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    source_files = ("observational_succ/local_global_descent.py",
                    "observational_succ/constructive_gluing_tower.py",
                    "research/2026-10-12/LOCAL_GLOBAL_YONEDA_GLUE_2026-10-12.md",
                    "provenance/IMPORT_MANIFEST.json")
    result = {"claim_id": "SWM-A03", "parent_sha_at_probe": parent,
              "command": "PYTHONDONTWRITEBYTECODE=1 python -B research/2026-10-13/SWARM_ATLAS/A03_probe.py",
              "python_version": sys.version.split()[0],
              "source_sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in source_files},
              "independent_probe": independent_controls(), "hostile_witness": native_witness(),
              "scope": "Bounded scalar exact controls plus paper theorem; no universal numerical proof"}
    result["elapsed_seconds"] = round(time.monotonic() - started, 6)
    result["exit_code"] = 0
    result["probe_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
