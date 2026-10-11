#!/usr/bin/env python3
"""Reproduce zero-blind balanced theta SUCC and finite Li coefficient bounds.

Run from repo root:
  python scripts/balanced_theta_li_probe.py --output /tmp/balanced-theta-li.json

No nontrivial zeta zeros enter source construction. A finite-model double
zero is computed independently as a hostile diagnostic, not as a proof
ingredient. All analytic inequalities are theorems for ideal integrals;
mpmath printing is not certified directed rounding.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.balanced_theta_li import (
    theta_defect, matched_theta_cutoff, one_prime_fake_defect,
    finite_gamma_succ_defect, finite_li_coefficients,
    li_all_degree_bound, finite_double_zero, li_coevolving_diagonal,
)
from observational_succ.hasse_theta_seam import SUCCDifferenceSource


def run(*, dps=85, u="2", tolerance="1e-10", degree=12):
    import mpmath as mp
    if not 2<=degree<=24 or not 60<=dps<=150:
        raise ValueError("Require 2<=degree<=24, 60<=dps<=150")
    with mp.workdps(dps):
        cert=matched_theta_cutoff(u,tolerance,dps=dps)
        n=cert["horizon"]
        if n>256:
            raise ValueError("Source test needs <=256 integrated events")
        Nsrc=max(64,n)
        true=SUCCDifferenceSource.zeta(Nsrc)
        altered={k:1 for k in range(1,Nsrc+1)}
        altered[6]=2
        fake=SUCCDifferenceSource.from_prefix(altered,Nsrc)
        d_true=theta_defect(u,n,source=true,dps=dps)
        d_fake=theta_defect(u,n,source=fake,dps=dps)
        predicted=one_prime_fake_defect(u,6,1,dps=dps)
        if abs((d_fake-d_true)-predicted)>mp.mpf("1e-60"):
            raise ArithmeticError("Fake-six theta source anomaly not reproduced")
        if abs(d_true)>cert["analytic_tail_bound"]+mp.mpf("1e-55"):
            raise ArithmeticError("Theta reflection defect violated analytic tail bound")

        truncated=finite_li_coefficients(3,"1.2",degree,dps=dps)
        reference=finite_li_coefficients(4,"2",degree,dps=dps)
        li_bound=li_all_degree_bound(3,"1.2",degree,dps=dps)
        measured=abs(truncated[-1]-reference[-1])
        if measured>li_bound["li_coefficient_error_bound"]+mp.mpf("1e-60"):
            raise ArithmeticError("Li fixed-degree analytic error envelope violated")
        spurious=finite_li_coefficients(4,"0.325",degree,dps=dps)
        collision=finite_double_zero(4,dps=45)
        diagonal=li_coevolving_diagonal(
            degree,match_reflection=True,dps=dps)
        target=mp.power(2,-degree)
        gamma=finite_gamma_succ_defect(mp.mpc("1.1","0.7"),"-2.5","0.5",dps=dps)
        return {
            "status":"ZERO_BLIND_BALANCED_THETA_AND_LI_PROBE",
            "full_theta_asymptotic":"for fixed N, D_N(u)/exp(u/2) -> 1 as u->inf",
            "matched_horizon":{
                "logarithmic_u":mp.nstr(cert["u"],20),
                "source_event_N":n,
                "requested_error":mp.nstr(cert["requested_tolerance"],20),
                "theoretical_reflection_bound":mp.nstr(cert["analytic_tail_bound"],25),
                "observed_true_reflection_defect":mp.nstr(d_true,25),
                "observed_fake_six_defect":mp.nstr(d_fake,25),
                "fake_minus_true":mp.nstr(predicted,25),
                "fake_at_mirror_fixed_u_0":str(theta_defect(0,n,source=fake,dps=dps)),
            },
            "finite_gamma_shift_triangle_residual":mp.nstr(abs(gamma["residual"]),20),
            "finite_Li":{
                "degree":degree,
                "candidate_theta_N":3,"candidate_arch_window_T":"1.2",
                "reference_theta_N":4,"reference_arch_window_T":"2",
                "candidate":mp.nstr(truncated[-1],30),
                "reference":mp.nstr(reference[-1],30),
                "observed_gap":mp.nstr(measured,20),
                "analytic_fixed_degree_gap_bound":mp.nstr(
                    li_bound["li_coefficient_error_bound"],20),
                "zero_free_disk_radius":"1/2",
                "all_degree_uniform_positivity":False,
            },
            "degree_coevolution":{
                "Li_index":degree,
                "arithmetic_horizon":diagonal["arithmetic_horizon"],
                "archimedean_T":mp.nstr(
                    diagonal["archimedean_window_T"],25),
                "Li_index_absolute_accuracy_goal":mp.nstr(target,20),
                "Li_index_accuracy_bound":mp.nstr(
                    diagonal["Li_fixed_degree_error_bound"],20),
                "simultaneous_poisson_accuracy_bound":mp.nstr(
                    diagonal["reflection"]["theta_reflection_error_bound"],20),
                "both_errors_below_2_to_minus_index":bool(
                    diagonal["Li_fixed_degree_error_bound"]<target and
                    diagonal["reflection"]["theta_reflection_error_bound"]<target),
                "RH_sign_proved":False,
            },
            "finite_collision":{
                "N":4,
                "T_threshold":mp.nstr(collision["T_star"],25),
                "spectral_t_threshold":mp.nstr(collision["t_star"],25),
                "square_root_split_coefficient":mp.nstr(
                    collision["off_line_splitting_coefficient"],20),
                "finite_N_4_T_0_325_positive_Li_first_degree_count":
                    sum(1 for x in spurious if x>0),
                "first_Li":mp.nstr(spurious[0],20),
                "last_Li":mp.nstr(spurious[-1],20),
                "off_line_roots_are_FINITE_model_only":True,
            },
            "epistemic_limit":"Fixed-index Li convergence; NO uniform all-index sign and NO RH proof",
            "nontrivial_zeta_zeros_used_as_source":False,
        }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dps",type=int,default=85)
    p.add_argument("--u",default="2")
    p.add_argument("--tolerance",default="1e-10")
    p.add_argument("--degree",type=int,default=12)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    data=run(dps=a.dps,u=a.u,tolerance=a.tolerance,degree=a.degree)
    blob=json.dumps(data,sort_keys=True,indent=2)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(blob,encoding="utf-8")
    else:
        print(blob,end="")


if __name__=="__main__":
    main()
