"""Frozen exact minimum geometry receipt; no pi normality claim.

All finite pi values are outward rational intervals from authenticated
Wallis/Kummer and rational Taylor, not input digits of pi.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.poisson_circle_minimal import (
    rational_greedy_circle, exact_energy, haar_origin_expected_energy,
    certified_pi_energy, ternary_periodic_counterfeit_energy,
    polygon_poisson_energy, energy_to_weyl_upper,
)
from poisson_minimal_independent_oracle import audit


def outward(lo: Q, hi: Q, places: int = 12) -> dict:
    scale=10**places
    a=lo*scale;b=hi*scale
    return {"lower":f"{a.numerator//a.denominator}/{scale}",
            "upper":f"{-((-b.numerator)//b.denominator)}/{scale}"}


def sha256(path: str) -> str:
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def receipt():
    greedy=[]
    allpoints=rational_greedy_circle(20,max_height=14)
    for N in (1,2,3,4,6,8,12,16,20):
        e=exact_energy(allpoints[:N])
        bound=haar_origin_expected_energy(N)
        assert Q(1)<=e<=bound
        greedy.append({"N":N,"energy":outward(e,e),
                       "proven_Haar_origin_mean_and_greedy_ceiling":str(bound)})
    pi=[]
    for N,steps in ((2,128),(3,128),(4,4096),(5,1024),(6,4096)):
        r=certified_pi_energy(2,N,wallis_steps=steps,
                              dyadic_bits=48,taylor_order=14)
        pi.append({"N":N,"b":2,"Wallis_Kummer_stage":steps,
                   "energy_enclosure":outward(r.energy_lower,r.energy_upper),
                   "Haar_origin_mean":str(haar_origin_expected_energy(N)),
                   "certified_strictly_above_Haar_mean":r.energy_lower>haar_origin_expected_energy(N),
                   "first_Weyl_mean_squared_upper":outward(Q(0),energy_to_weyl_upper(r.energy_upper,1)),
                   "source_transport_error_upper":outward(Q(0),r.transport_error)})
    counter=[]
    for depth in range(1,6):
        e=ternary_periodic_counterfeit_energy(depth)
        counter.append({"r":depth,"base":2,"source":f"1/3^{depth}",
                        "period":2*3**(depth-1),"limiting_energy_gap_exact":str(e-1),
                        "limiting_gap_lt_one_in_1e8": e-1<Q(1,10**8)})
    return {
        "status":"EXACT_FINITE_PLUS_PAPER_CONDITIONAL_PI_NORMALITY_UNPROVED",
        "parent_commit":"f986507851e34636f60bee657dcdf0771a934380",
        "parent_pi_prime_source_blob":"ab48ffe102657100a1c9363030aa4867981d13d0",
        "source_sha256":sha256("observational_succ/poisson_circle_minimal.py"),
        "tests_sha256":sha256("tests/test_poisson_circle_minimal.py"),
        "independent_oracle_sha256":sha256("scripts/poisson_minimal_independent_oracle.py"),
        "inherited_actual_pi_source_sha256":sha256("observational_succ/pi_prime_carry_transport.py"),
        "greedy_exact_samples":greedy,
        "genuine_pi_finite_samples":pi,
        "nonnormal_periodic_chord_shadow_families":counter,
        "uniform_polygon_energy_example_q29":str(polygon_poisson_energy(29)),
        "method_distinct_exact_oracle":audit(),
        "normality_claimed":False,"RH_claimed":False,"Lean_claimed":False,
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    encoded=json.dumps(receipt(),indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(encoded,encoding="utf-8")
    else:
        print(encoded,end="")


if __name__=="__main__":
    main()
