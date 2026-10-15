"""Deterministic zero-free exact arithmetic receipt for Suzuki prime onset."""
import json
import sys
from pathlib import Path
from fractions import Fraction as Q

# Make direct `python scripts/suzuki_first_prime_probe.py` work from repo root,
# as well as module invocation, without an editable package installation.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_first_prime import (
    first_prime_wavefront, genuine_prime_weight_interval, hs_squared,
    prime_differential_form, l2_piecewise, neumann_quadratic,
    onset_archimedean_certificate,
)


def receipt():
    a=Q(2,5)
    sample=((Q(-2,5),0),(Q(-3,8),1),(Q(-7,20),0),
            (Q(3,10),0),(Q(13,40),1),(Q(7,20),0),(Q(2,5),0))
    b=Q(9,13);c=Q(7,10)
    norm=l2_piecewise(sample)
    shifted=prime_differential_form(sample,c,b)
    if shifted != -b*norm:
        raise ArithmeticError("two-edge phase calibration failed")
    steps=((-a,Q(0),Q(1)),(Q(0),a,Q(-1)))
    K,K2=neumann_quadratic(steps,a)
    if K!=K2:
        raise ArithmeticError("Neumann carrier mismatch")
    return {
        "research":"Suzuki first genuine prime wavefront",
        "primary":"https://arxiv.org/html/2606.09096v3",
        "arithmetic_wavefront":first_prime_wavefront(a),
        "exact_synthetic_control":{
            "synthetic_phase_c":"7/10 (NOT log2)",
            "synthetic_weight_b":"9/13 (NOT log2/sqrt2)",
            "kernel_HS_squared":str(hs_squared(a,c,b)),
            "translated_pair_form":str(shifted),
            "translated_pair_norm_squared":str(norm),
            "translated_pair_Rayleigh":str(shifted/norm),
        },
        "authentic_prime_2_weight_bracket":{
            "lower":str(genuine_prime_weight_interval(2)[0]),
            "upper":str(genuine_prime_weight_interval(2)[1]),
        },
        "neumann_K_q":str(K),
        "neumann_primitive_norm_squared":str(K2),
        "full_archimedean_boundary_certification":onset_archimedean_certificate(),
        "all_interval_Weil_positivity_proved":False,
        "Suzuki_global_limit_proved":False,
        "original_nontrivial_zero_locations_used":False,
        "physical_source_authenticated":False,
        "RH_proved":False,
    }


def main():
    print(json.dumps(receipt(),indent=2,sort_keys=True))


if __name__=="__main__":main()
