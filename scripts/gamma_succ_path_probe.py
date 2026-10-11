#!/usr/bin/env python3
"""Exact SUCC/Gamma boundary and analytic prime-moment displacement probe.

No zeta zero input, no regularized divergent series, no global sign claim.
Use from repo root: python scripts/gamma_succ_path_probe.py --prime-bound 53 --gamma-steps 64
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.gamma_succ_path import (
    FactorialSuccPath, MomentChannel, PrimeMomentPath,
)


def run(prime_bound=53,gamma_steps=64,dps=55):
    if prime_bound < 2 or gamma_steps < 2:
        raise ValueError("Finite cutoffs must be >=2")
    P=PrimeMomentPath.genuine(prime_bound)
    G=FactorialSuccPath(gamma_steps)
    G.verify_bridge()
    import mpmath as mp
    with mp.workdps(dps):
        jet=P.first_jet(dps=dps)
        parts=P.reflected_log_jet_one(G,dps=dps)
        piP=mp.sqrt(6*(mp.mpf(P.zeta_two_rational().numerator)/
                           P.zeta_two_rational().denominator))
        at_one=P.at_u_one(G,dps=dps)
        true_jet=(2*mp.diff(mp.zeta,2)/mp.zeta(2)
                  -mp.log(mp.zeta(2)))
        control=PrimeMomentPath(
            6,(MomentChannel(2),MomentChannel(3),MomentChannel(6)))
        return {
            "status":"FINITE_PATH_PROBE",
            "input_zeros":False,
            "prime_bound":prime_bound,
            "gamma_succ_steps":gamma_steps,
            "gamma_factorial_exact_prime_bridge":True,
            "gamma_factorial_value_decimal_digits":len(str(G.endpoint())),
            "gamma_succ_ratio_at_z_2":str(G.gamma_succ_ratio(2)),
            "gamma_succ_boundary_defect_at_z_2":str(G.gamma_boundary_defect(2)),
            "zeta_two_prime_fraction":str(P.zeta_two_rational()),
            "finite_pi_squared_proxy":str(P.pi_squared_proxy()),
            "finite_pi_proxy":mp.nstr(piP,30),
            "pi_squared_gap_bound":str(P.genuine_pi_squared_tail_bound()),
            "m_equals_one_scalar_ratio":str(P.scalar_ratio_at_one()),
            "prime_first_log_jet":mp.nstr(jet,30),
            "prime_second_log_jet":mp.nstr(P.second_jet(dps=dps),30),
            "prime_first_jet_tail_bound":mp.nstr(P.genuine_first_jet_tail_bound(dps=dps),15),
            "missing_first_jet_observed":mp.nstr(abs(true_jet-jet),15),
            "finite_reflected_value_at_u_1":mp.nstr(at_one,30),
            "classical_limit_negative_one":str("-1/12"),
            "finite_reflected_first_log_jet":mp.nstr(parts["total"],30),
            "finite_reflected_decomposition":{
                k:mp.nstr(parts[k],30)
                for k in ("gamma_succ","powers","sine_rotation","finite_prime_jet")
            },
            "counterfeit_composite_6_scalar_ratio":str(control.scalar_ratio_at_one()),
            "counterfeit_composite_6_is_true_zeta_source":control.is_genuine_prefix(),
            "counterfeit_composite_6_first_log_jet":mp.nstr(control.first_jet(dps=dps),30),
            "scope":"path and germ algebra / Euler-Gamma limit, NOT Weil positivity or RH"
        }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prime-bound",type=int,default=53)
    p.add_argument("--gamma-steps",type=int,default=64)
    p.add_argument("--dps",type=int,default=55)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    result=run(args.prime_bound,args.gamma_steps,args.dps)
    blob=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(blob)
    else:
        print(blob,end="")


if __name__=="__main__":
    main()
