"""Deterministic exact-rational research receipt; no zeta-zero inputs."""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
from observational_succ.carrier_locked_rigidity import (
    shifted_noise_kernel, sharp_chain_noise, affine_stability_certificate,
    cyclic_uniform_control, gaussian_mix_control,
)
from observational_succ.dual_shell_observer import (
    decompose_shells, noncommuting_boundary_witness,
    meeting_certificate, late_hidden_source,
)


def receipt():
    noise, B = sharp_chain_noise(2, 3, Q(3, 4))
    affine = affine_stability_certificate(shifted_noise_kernel(noise, 2), 2, B, 2)
    f = {1: Q(1, 2), 2: Q(-1, 3), 5: Q(3, 7), 9: Q(1, 11)}
    shells = decompose_shells(f, 2)
    boundary = meeting_certificate(f, 2, 2)
    hidden = meeting_certificate(late_hidden_source(2, 4), 2, 4)
    return {
        "source_theory": "carrier_locked_affine_dual_shell",
        "affine_stability_sharp_control": affine,
        "exact_affine_identity_control": affine_stability_certificate(
            shifted_noise_kernel({0: Q(1)}, 2), 2, 4, 2),
        "finite_cyclic_negative_control": cyclic_uniform_control(5, 2),
        "selfdual_gaussian_state_mutation": gaussian_mix_control(),
        "dual_tower": {
            "depth": shells["depth"],
            "squared_norms": [str(x) for x in shells["squared_norms"]],
            "source_squared_norm": str(shells["source_squared_norm"]),
            "reconstruction_exact": shells["reconstruction_exact"],
            "orthogonal": shells["orthogonal"],
            "Parseval_exact": shells["Parseval_exact"],
        },
        "finite_boundary": {
            "level": 2,
            "resolved_squared_norm": str(boundary["resolved_squared_norm"]),
            "tail_squared_norm": str(boundary["tail_squared_norm"]),
            "source_squared_norm": str(boundary["source_squared_norm"]),
            "glues": boundary["boundary_glued_exactly"],
        },
        "deep_hidden_source": {
            "depth": 4,
            "first_four_shells_zero": not hidden["resolved"],
            "positive_unresolved_energy": hidden["tail_squared_norm"] > 0,
            "unresolved_energy": str(hidden["tail_squared_norm"]),
        },
        "additive_boundary_counterexample": noncommuting_boundary_witness(),
        "mathematical_theorems_independently_formalized_in_Lean": False,
        "physical_source_authenticated": False,
        "completed_Weil_form_constructed": False,
        "nontrivial_zero_locations_used": False,
        "RH_proved": False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    args = ap.parse_args()
    txt = json.dumps(receipt(), sort_keys=True, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(txt, encoding="utf-8")
    else:
        print(txt, end="")


if __name__ == "__main__":
    main()
