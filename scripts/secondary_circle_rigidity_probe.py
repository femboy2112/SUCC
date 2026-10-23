"""Byte-reproducible exact finite secondary-circle rigidity receipt.

Calculates finite source enclosures only. No pi-normality/RH conclusion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from scripts.secondary_circle_independent_oracle import run_oracle

from observational_succ.secondary_circle_rigidity import (
    certified_pi_cosine_intervals, interval_prime_and_chord_budget,
    amplified_fourier_bound, real_chord_rigidity, exact_rational_orbit_cosine,
    exact_uniform_polygon_cosine, circle_rotation_commutator,
)


def scaled_floor(q: Q, digits: int = 12) -> int:
    return (q.numerator*10**digits)//q.denominator


def scaled_ceil(q: Q, digits: int = 12) -> int:
    return -((-q.numerator*10**digits)//q.denominator)


def pi_case(base: int, horizon: int, cutoff: int) -> dict:
    observations=certified_pi_cosine_intervals(base,horizon,cutoff,
                                               level=18,precision=85,order=28)
    budget=interval_prime_and_chord_budget(observations)
    amp=amplified_fourier_bound(base=base,frequency=1,horizon=horizon,
                      replicas=2,cutoff=cutoff,
                      cosine_band_bound=budget.harmonic_bound)
    return {
        "base":base,"horizon":horizon,"cutoff":cutoff,
        "cos1_scaled_1e12_outer": [scaled_floor(observations[1][0]),
                                     scaled_ceil(observations[1][1])],
        "mean_chord_scaled_1e12_outer": [scaled_floor(budget.mean_chord_interval[0]),
                                           scaled_ceil(budget.mean_chord_interval[1])],
        "prime_cosine_defect_scaled_1e12_upper":scaled_ceil(budget.max_prime_cosine_defect),
        "chord_deficit_scaled_1e12_upper":scaled_ceil(budget.chord_deficit),
        "real_harmonic_bound_scaled_1e12_upper":scaled_ceil(budget.harmonic_bound),
        "Fourier_h1_bound_scaled_1e12_upper":scaled_ceil(amp.modulus_upper),
        "asymptotic_theorem_claim":False,
    }


def receipt() -> dict:
    source=ROOT/"observational_succ/secondary_circle_rigidity.py"
    tests=ROOT/"tests/test_secondary_circle_rigidity.py"
    cases=[]
    for q in (3,5,7,9):
        ms=[Q(1)]+[exact_rational_orbit_cosine(q,2,k) for k in range(1,41)]
        r=real_chord_rigidity(ms)
        cases.append({"modulus":q,"base":2,
                      "first_chord":str(r.mean_chord),
                      "prime_defect":str(r.max_prime_cosine_defect),
                      "max_harmonic":str(max(abs(c) for c in ms[1:])),
                      "certificate_bound":str(r.harmonic_bound)})
    pent=[exact_uniform_polygon_cosine(5,h) for h in range(0,7)]
    assert pent[1]==0 and pent[5]==1
    assert real_chord_rigidity(pent[:5]).max_prime_cosine_defect == 0
    assert real_chord_rigidity(pent[:6]).max_prime_cosine_defect == 1
    return {
      "claim":"research_only_finite_no_pi_normality_RH_or_Weil_proof",
      "parent_pr":247,
      "authentic_circle_pi_source":"PR247 pi_interval and _cos_enclosure",
      "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
      "test_sha256":hashlib.sha256(tests.read_bytes()).hexdigest(),
      "rational_periodic_controls":cases,
      "independent_cyclotomic_oracle":run_oracle(),
      "five_gon_all_but_five_prime_counterexample":{
          "first_chord":"2","prime_defect_at_cutoff_4":"0",
          "prime_defect_at_cutoff_5":"1",
      },
      "one_ninth_persistent_chord_defect": {
          "first_chord":"2","third_chord":"3",
          "third_harmonic_cosine":str(exact_rational_orbit_cosine(9,2,3))},
      "doubling_half_turn_rotation_commutator":str(circle_rotation_commutator(2,Q(1,2))),
      "tripling_half_turn_rotation_commutator":str(circle_rotation_commutator(3,Q(1,2))),
      "pi_cases":[pi_case(2,5,12),pi_case(16,5,20)],
      "proof_obligation":"eta_N -> 0 AND floor(log2(M_N))*epsilon_(M_N,N) -> 0 for growing subexponential M_N",
    }


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=None)
    args=parser.parse_args()
    doc=json.dumps(receipt(),indent=2,sort_keys=True)+"\n"
    if args.output is not None:
        args.output.write_text(doc,encoding="utf8")
    else:
        print(doc,end="")


if __name__=="__main__":
    main()
