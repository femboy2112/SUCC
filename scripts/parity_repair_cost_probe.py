#!/usr/bin/env python3
"""Reproduce the exact minimum-cost parity-repair evidence as stable JSON.

No observation is performed; this verifies a declared finite graph model with
exact integer / Fraction arithmetic (no floats, no randomness).  Running with
``--write-certificates`` regenerates the frozen optimality-certificate table
``research/2026-10-19/PARITY_REPAIR_CERTIFICATES.json`` bit-for-bit.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.parity_repair_cost import (  # noqa: E402
    all_flip_targets,
    connected_graph_certificates,
    greedy_sequential_repair,
    illegal_source_law_alteration,
    ising_couplings,
    ising_ground_state_bruteforce,
    ising_ground_state_energy,
    lawful_model_repair,
    min_repair_cost,
    probe_reveal_obstruction,
    repair_graph,
    single_flip_local_certificate,
    unit_weights,
    verify_maxcut_identity,
)

CERTIFICATE_PATH = (Path(__file__).resolve().parents[1]
                    / "research" / "2026-10-19"
                    / "PARITY_REPAIR_CERTIFICATES.json")


def certificates_text() -> str:
    """Canonical serialization of the <=5-vertex certificate family."""
    return json.dumps(connected_graph_certificates(5),
                      indent=2, sort_keys=True) + "\n"


def receipt() -> dict:
    triangle = repair_graph(("A", "B", "C"),
                            [("A", "B"), ("B", "C"), ("C", "A")])
    square = repair_graph(("a", "b", "c", "d"),
                          [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")])
    k4_minus_edge = repair_graph(
        ("p", "q", "r", "s"),
        [("p", "q"), ("p", "r"), ("q", "r"), ("q", "s"), ("r", "s")])

    # ALL-FLIP UNIT identity C_* = |E| - MaxCut on a sample (triangle).
    identity = verify_maxcut_identity(triangle)

    # Sweep: identity holds on every connected graph on <= 5 vertices.
    certificates = connected_graph_certificates(5)
    per_n = {}
    for cert in certificates:
        per_n[cert["n_vertices"]] = per_n.get(cert["n_vertices"], 0) + 1

    # Ising ground-state mapping cross-check (fractional weights allowed).
    t_ising = (1, 0, 1)
    w_ising = (1, 1, 1)
    couplings = ising_couplings(t_ising, w_ising)
    ground = ising_ground_state_bruteforce(triangle, couplings)
    mapped = ising_ground_state_energy(triangle, t_ising, w_ising)

    # Greedy-suboptimal negative control (all-flip unit on K4 minus an edge).
    greedy = greedy_sequential_repair(
        k4_minus_edge, all_flip_targets(k4_minus_edge),
        unit_weights(k4_minus_edge))
    exact = min_repair_cost(
        k4_minus_edge, all_flip_targets(k4_minus_edge),
        unit_weights(k4_minus_edge))

    # Single-flip strict local optimum on C4 (cost 2 vs global 0).
    bad = {"a": 0, "b": 0, "c": 1, "d": 1}
    local_cert = single_flip_local_certificate(
        square, all_flip_targets(square), unit_weights(square), bad)

    # Probe vs. model-repair vs. illegal source-law alteration (odd triangle).
    odd = (1, 1, 1)
    probe = probe_reveal_obstruction(triangle, odd)
    lawful = lawful_model_repair(triangle, odd, unit_weights(triangle))
    illegal = illegal_source_law_alteration(triangle, odd, (0,))

    return {
        "status": "EXACT_FINITE_CLASSICAL_OPTIMIZATION_NOT_GLOBAL_THEOREM",
        "domain": "finite undirected (multi)graph with F2 edge targets, weights >= 0",
        "sample_all_flip_unit_identity": {
            "graph": "triangle C3",
            "num_edges": identity.num_edges,
            "max_cut": identity.max_cut,
            "repair_cost_star": identity.repair_cost_star,
            "C_star_equals_E_minus_MaxCut": identity.holds,
        },
        "connected_graph_family_size": len(certificates),
        "connected_graphs_per_n": per_n,
        "all_maxcut_identities_hold": all(
            c["maxcut_identity_holds"] for c in certificates),
        "ising_ground_state_bruteforce_energy": str(ground.energy),
        "ising_ground_state_mapping_energy": str(mapped),
        "ising_mapping_agrees": ground.energy == mapped,
        "greedy_sequential_cost": str(greedy.cost),
        "exact_min_cost": str(exact.cost),
        "greedy_strictly_suboptimal": greedy.cost > exact.cost,
        "c4_local_optimum_cost": str(local_cert.local_cost),
        "c4_global_cost": str(local_cert.global_cost),
        "c4_is_strict_local_optimum": local_cert.is_strict_local_optimum,
        "c4_strictly_suboptimal": local_cert.strictly_suboptimal,
        "probe_repair_cost_paid": probe.repair_cost_paid,
        "probe_alters_source": probe.source_targets_altered,
        "probe_makes_globally_representable": probe.makes_globally_representable,
        "probe_reveals_obstruction": probe.reveals_obstruction,
        "lawful_repair_cost": str(lawful.cost),
        "lawful_repair_alters_source": lawful.source_targets_altered,
        "lawful_repair_is_lawful": lawful.lawful_succ_repair,
        "illegal_alteration_apparent_cost": str(illegal.apparent_repair_cost),
        "illegal_alteration_alters_source": illegal.source_targets_altered,
        "illegal_alteration_is_lawful_succ_repair": illegal.lawful_succ_repair,
        "NP_hardness_is_noncomputability": False,
        "field_class_of_C_star": "SimpleField (finite program returns exact value)",
        "physically_realized_observation": False,
        "source_provenance_authenticated": False,
        "LEM_proved": False,
        "RH_proved": False,
    }


def main(argv: list[str]) -> int:
    if "--write-certificates" in argv:
        CERTIFICATE_PATH.write_text(certificates_text())
        print(f"wrote {CERTIFICATE_PATH}", file=sys.stderr)
        return 0
    print(json.dumps(receipt(), sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
