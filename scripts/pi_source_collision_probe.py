"""Deterministic exact finite receipt; never an asymptotic pi certificate."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_source_collision import (
    adversarial_complement, cell_collision, galois_collision_bounds,
    galois_collision_mean, prime_window, small_ball_pairs,
)


def receipt():
    rows = []
    for p in (17, 41, 73, 97, 113, 137, 193):
        window = prime_window(p)
        for cells in ((4, 16, 64) if p <= 97 else (16,)):
            radius = Q(1,cells)
            mean = galois_collision_mean(window, radius)
            lower, upper = galois_collision_bounds(p,radius)
            assert lower <= mean <= upper
            selected = Q(cells*small_ball_pairs(window.states,radius),window.length**2)
            rows.append({"prime":p,"period":window.period,"length":window.length,
                         "cells":cells,"mean_scaled_close_pairs":str(cells*mean),
                         "scaled_lower":str(cells*lower),"scaled_upper":str(cells*upper),
                         "selected_scaled_close_pairs":str(selected),
                         "selected_cell_collision":str(cell_collision(window.states,cells)),
                         "source_tail_upper":str(window.tail_bound),
                         "holdout":p>97})
    heldout = []
    for p in (1009,2017):
        window = prime_window(p)
        canonical_cells = 1
        while (16*canonical_cells)**5 <= p*p:  # fixed exponent c=2/5
            canonical_cells *= 16
        heldout.append({"prime":p,"period":window.period,"length":window.length,
                        "fixed_c_2_over_5_cells":canonical_cells,
                        "canonical_cell_collision":str(cell_collision(window.states,canonical_cells)),
                        "diagnostics":[{"cells":m,"cell_collision":str(cell_collision(window.states,m)),
                                        "scaled_close_pairs":str(Q(m*small_ball_pairs(window.states,Q(1,m)),window.length**2))}
                                       for m in (16,64,256,1024)]})
    w=prime_window(97)
    fake=adversarial_complement(97,64)
    phases=tuple((u+v)%1 for u,v in zip(w.local,fake))
    assert cell_collision(phases,64)==64
    assert all(v.denominator%97 for v in fake)
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
        "observational_succ/pi_source_collision.py","scripts/pi_source_collision_probe.py",
        "tests/test_pi_source_collision.py")}
    return {"schema":"SUCC-PI-SOURCE-COLLISION-1","status":"VERIFIED_FINITE",
            "arithmetic":"integers and fractions only","parent":"de005af44cb4592d7a8be73f46fa1983f627da27",
            "rows":rows,"larger_source_holdouts":heldout,
            "fake_p_free_complement":{"prime":97,"cells":64,"cell_collision":"64",
                                       "authentic_source":False,"misleading_local_only_claim_rejected":True},
            "source_sha256":hashes,"pi_normality":"OPEN",
            "selected_asymptotic_collision_bound":"UNVERIFIED",
            "independence_of_pi_normality":"NOT_ESTABLISHED",
            "note":"Small rows use diagnostic resolutions, not fitted asymptotic rates. Canonical schedule is fixed in advance."}


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    data=json.dumps(receipt(),indent=2,sort_keys=True)+"\n"
    if args.output:
        Path(args.output).write_text(data)
    else:
        print(data,end="")
