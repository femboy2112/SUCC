#!/usr/bin/env python3
"""Finite, zero-free arithmetic Lambert W on Dirichlet-convolution source.

Reproduce:
  python scripts/dirichlet_lambert_probe.py --horizon 64 --sigma 4

The readout is NOT RH positivity. Its safe analytic Lambert W identity
factors through a Dirichlet transform, without analytic continuation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.dirichlet_lambert import DirichletLambertSnapshot


def run(horizon=64,sigma=4,dps=70):
    if type(horizon) is not int or not 8<=horizon<=256:
        raise ValueError("Horizon must be 8..256")
    source={n:1 for n in range(1,horizon+1)}
    fake=dict(source)
    fake[6]=2
    true=DirichletLambertSnapshot.from_prefix(source,horizon)
    bad=DirichletLambertSnapshot.from_prefix(fake,horizon)
    if not true.verify_inverse_identity() or not bad.verify_inverse_identity():
        raise ArithmeticError("Formal inverse identity did not hold")
    numeric=true.analytic_mellin_probe(sigma,dps=dps)
    import mpmath as mp
    with mp.workdps(dps):
        result={
            "status":"EXACT_ARITHMETIC_LAMBERT_PREFIX",
            "horizon":horizon,
            "independent_factorizations_of_six":true.witnesses(6),
            "true_source":true.composite_six(),
            "fake_source":bad.composite_six(),
            "true_inverse_identity":True,
            "fake_inverse_identity":True,
            "true_w_at_eight":str(true.w[8]),
            "true_connected_at_eight":str(true.connected[8]),
            "safe_mellin": {
                "sigma":sigma,
                "input_mellin":mp.nstr(numeric["input"],30),
                "analytic_w_of_mellin":mp.nstr(numeric["analytic_lambert"],30),
                "finite_dirichlet_w_mellin":mp.nstr(numeric["finite_star_sum"],30),
                "absolute_difference":mp.nstr(numeric["absolute_error"],20),
                "coefficient_tail_bound":mp.nstr(numeric["truncation_bound"],20),
                "mass_of_input":mp.nstr(numeric["abs_input_mass"],25),
                "condition":"sum |h(n)|n^-sigma < 1/e",
            },
            "epistemic_scope":"finite exact Dirichlet algebra and safe Mellin transform, not RH sign",
            "zeros_read":False,
        }
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--horizon",type=int,default=64)
    p.add_argument("--sigma",type=int,default=4)
    p.add_argument("--dps",type=int,default=70)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    s=json.dumps(run(args.horizon,args.sigma,args.dps),indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(s)
    else:
        print(s,end="")


if __name__=="__main__":
    main()
