#!/usr/bin/env python3
"""Reproduce bounded exact SUCC choice/descent evidence as stable JSON.

No observation is performed; this verifies a declared finite graph model.
"""
from __future__ import annotations

import json
from itertools import combinations, product

from observational_succ.meta_choice_descent import (
    FiniteTransportGraph, ParityEdge, brute_force_sections,
    local_edge_witnesses, solve_parity_descent, triangle, verify_loop,
)


def receipt() -> dict:
    odd = triangle((1, 1, 1))
    even = triangle((1, 1, 0))
    odd_result = solve_parity_descent(odd)
    even_result = solve_parity_descent(even)
    vertices = ("a", "b", "c", "d")
    pairs = tuple(combinations(vertices, 2))
    cases = 0
    obstructed = 0
    flat = 0
    for states in product((0, 1, 2), repeat=6):
        edges = tuple(ParityEdge(u, v, value - 1, "original", "GF2")
                      for (u, v), value in zip(pairs, states) if value)
        graph = FiniteTransportGraph("original", "GF2", vertices, edges)
        verdict = solve_parity_descent(graph)
        solutions = brute_force_sections(graph)
        assert verdict.section_exists == bool(solutions)
        assert verdict.number_of_sections == len(solutions)
        if verdict.section_exists:
            flat += 1
        else:
            obstructed += 1
            assert verdict.obstruction is not None
            assert verify_loop(graph, verdict.obstruction)
        cases += 1
    # Independent 4-vertex parity-fiber count: sum_H 2**(4-c(H)) = 393.
    assert cases == 729 and flat == 393 and obstructed == 336
    assert not odd_result.section_exists and odd_result.number_of_sections == 0
    assert verify_loop(odd, odd_result.obstruction)
    assert even_result.number_of_sections == 2
    return {
        "status": "EXACT_FINITE_SOURCE_CONTRACT_NOT_GLOBAL_THEOREM",
        "domain": "finite undirected multigraph with F2 edge transports",
        "choice_is_local_and_available": all(local_edge_witnesses(e) for e in odd.edges),
        "odd_triangle_global_sections": len(brute_force_sections(odd)),
        "odd_triangle_obstruction_verified": True,
        "even_triangle_global_sections": len(brute_force_sections(even)),
        "all_four_vertex_simple_labeled_graphs": cases,
        "flat_graphs": flat,
        "obstructed_graphs": obstructed,
        "independent_exhaustive_oracle_agrees": True,
        "physically_realized_observation": False,
        "source_provenance_authenticated": False,
        "full_sheaf_or_topos_semantics_formalized": False,
        "LEM_proved": False,
        "RH_proved": False,
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), sort_keys=True, indent=2))
