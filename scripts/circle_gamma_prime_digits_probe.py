"""Emit a small deterministic exact receipt for circle/Gamma/primes/digits.

The source-derived pi Mellin bracket is checked in the isolated test suite;
this frozen finite receipt deliberately records no asymptotic claim.
Run: python scripts/circle_gamma_prime_digits_probe.py --output /tmp/bridge.json
"""
import argparse
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.circle_gamma_prime_digits import (
    mode_laplacian_polynomial, eval_polynomial, ordered_succ_gamma_weight,
    genuine_prime_smooth_coefficients, factorized_phase_with_mixed_terms,
    rational_digits, cyclic_debruijn_edge_flow, pi_heat_mellin_mode_bounds,
    prime_euler_pi_bracket
)
from observational_succ.pi_polygon_normality import polygon_pi_bracket

PARENT="b116841f12b41aaf7600da39bbb40577f25b6295"


def receipt():
    box=genuine_prime_smooth_coefficients((2,3),1,2)
    n,direct,individual,mixed=factorized_phase_with_mixed_terms((2,3),Q(1,7))
    cycle_a=(1,2,4)
    cycle_b=(3,6,5)
    edges={f"{a}{b}":0 for a in range(2) for b in range(2)}
    for cycle in (cycle_a,cycle_b):
        word=tuple(2*r//7 for r in cycle)
        flow,_,_=cyclic_debruijn_edge_flow(word,2,2)
        for block,count in flow.items():
            edges["".join(map(str,block))]+=count
    alternate,_,_=cyclic_debruijn_edge_flow((0,1)*50,2,2)
    alternate={f"{a}{b}":alternate.get((a,b),0)
               for a in range(2) for b in range(2)}
    low,high=pi_heat_mellin_mode_bounds(2,3,12,256)
    prime3=prime_euler_pi_bracket(3,256)
    prime5=prime_euler_pi_bracket(5,256)
    poly=polygon_pi_bracket(12,256)
    forged_euler=Q(25,18)
    forced_upper=forged_euler+Q(1,5)
    independent_prefix=sum((Q(1,n*n) for n in range(1,31)),Q())
    assert independent_prefix>forced_upper
    assert prime3.euler_partial==Q(3,2)
    assert prime5.euler_partial==Q(25,16)
    assert max(prime5.lower_pi,poly.lower)<min(prime5.upper_pi,poly.upper)
    assert low<high
    assert (n,direct,individual,mixed)==(6,Q(5,7),Q(3,7),Q(2,7))
    assert edges=={"00":1,"01":2,"10":2,"11":1}
    return {
        "title":"CIRCLE_GAMMA_ALL_PRIMES_DIGIT_BRIDGE_FINITE_RECEIPT",
        "source_main":PARENT,
        "circle_modes":{
            "mode_2_poly":list(map(str,mode_laplacian_polynomial(2))),
            "mode_3_poly":list(map(str,mode_laplacian_polynomial(3))),
            "mode_4_poly":list(map(str,mode_laplacian_polynomial(4))),
            "square_modes":[str(eval_polynomial(mode_laplacian_polynomial(n),Q(2))) for n in range(5)],
            "hexagon_modes":[str(eval_polynomial(mode_laplacian_polynomial(n),Q(1))) for n in range(7)],
        },
        "ordered_gamma_coefficients_rate_3_over_2":[
            str(ordered_succ_gamma_weight(Q(3,2),n)) for n in range(5)],
        "prime_box":{
            "primes":[2,3],"max_power":1,"sigma":2,
            "integers":list(map(str,sorted(box))),
            "sum":str(sum(box.values(),Q())),
        },
        "phase_cocycle":{
            "phase":"1/7","factors":[2,3],"integer_mode":n,
            "factor_angle":str(individual),"mixed_angle":str(mixed),
            "direct_angle":str(direct),"naive_prime_only_fails":direct!=individual,
        },
        "hierarchy":{
            "prime7_base2_cycles":[list(cycle_a),list(cycle_b)],
            "digit_words":["".join(map(str,rational_digits(Q(a,7),2,3))) for a in (1,3)],
            "single_digit_balanced": sum(edges[key] for key in ("00","01"))==
                                     sum(edges[key] for key in ("10","11")),
            "two_digit_edges":edges,
            "periodic_binary_third_two_digit_edge_count":alternate,
        },
        "prime_to_circle":{
            "cutoff3":{"euler_partial":str(prime3.euler_partial),
                       "squared_pi_lower":str(6*prime3.euler_partial),
                       "squared_pi_upper":str(6*(prime3.euler_partial+prime3.missing_zeta_upper))},
            "cutoff5":{"euler_partial":str(prime5.euler_partial),
                       "squared_pi_lower":str(6*prime5.euler_partial),
                       "squared_pi_upper":str(6*(prime5.euler_partial+prime5.missing_zeta_upper))},
            "sourced_pi_bounds_overlap_polygon": True,
            "missing_prime3_invalidated_by_rational_harmonic_prefix": True,
            "rh_used":False,
        },
        "proof_boundaries":{
            "pi_normality_proved":False,
            "RH_proved":False,
            "RH_to_pi_phase_transference_proved":False,
            "circle_to_gamma_analytic_identity_formalized":False,
            "source_pi_gamma_bracket_finite":low<high,
            "phase_mixed_terms_required":direct!=individual,
        },
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt(),sort_keys=True,indent=2)+"\n")
    print("Exact finite circle/Gamma/primes/digits receipt generated.")


if __name__=="__main__":
    main()
