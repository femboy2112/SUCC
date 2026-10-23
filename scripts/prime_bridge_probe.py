#!/usr/bin/env python3
"""Deterministic exact Prime Bridge receipt; numerical analysis is separate."""
from pathlib import Path
import json
import sys
from fractions import Fraction as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.arithmetic_tfd import probe as tfd_probe
from observational_succ.arithmetic_entanglement import successor_entanglement_witness
from observational_succ.interacting_arithmetic_hamiltonian import certified_linear_entropy_bound
from observational_succ.holographic_reconstruction import ArithmeticTreeCode, arithmetic_code, minimum_tree_cut
from observational_succ.padic_bulk_network import bruhat_tits_ball, reconstruct_boundary_clusters
from observational_succ.arithmetic_operator_interface import critical_state_monomial, shift_refinement_defect


def jsonable(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [jsonable(v) for v in x]
    return x


def main():
    uniform, arithmetic = ArithmeticTreeCode(radius=2), arithmetic_code(2, 1, radius=2)
    regions = [tuple(i for i in range(6) if mask & (1 << i)) for mask in range(64)]
    counts = {}
    for label, code in (("uniform", uniform), ("arithmetic_beta2", arithmetic)):
        counts[label] = sum(code.corrects_erasure(tuple(i for i in range(6) if i not in keep)) for keep in regions)
    ball = bruhat_tits_ball(2, 4)
    report = {
        "status": "EXACT_FINITE_CALIBRATION_NOT_INFINITE_PROOF",
        "arithmetic_tfd": tfd_probe(),
        "successor_entanglement": successor_entanglement_witness(),
        "unitary_linear_entropy_lower_g1_t1over128": certified_linear_entropy_bound(F(1), F(1, 128)),
        "weighted_code_probabilities": arithmetic.weights,
        "radius2_authorized_regions_out_of64": counts,
        "radius2_entropy_gap": {"region": [0, 2], "cut_edges": minimum_tree_cut(2, (0, 2)),
                                "exact_nonzero_spectrum": [F(1, 3)]*3},
        "bt2_radius4": {"vertices": len(ball.vertices), "boundary": len(ball.boundary),
                        "reconstructed_levels": [len(level) for level in reconstruct_boundary_clusters(2, 4)]},
        "critical_state": {"identity": critical_state_monomial((1, 0, 1)),
                           "prime2_range_projection": critical_state_monomial((2, 0, 2)),
                           "nontrivial_phase": critical_state_monomial((1, F(1, 3), 1))},
        "shift_refinement_defect_K2_L5": shift_refinement_defect(2, 5),
        "gravitational_duality_proved": False,
        "RH_proved": False,
    }
    print(json.dumps(jsonable(report), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
