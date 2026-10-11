#!/usr/bin/env python3
"""Replay finite Euler-SUCC / Poisson-Gamma seam, zero-free.

All -2m indices are the known trivial zeros, not nontrivial zero data.
No RH or Weil sign is claimed. Read the independent proof ledger in
research/2026-10-10/FINITE_SUCC_HASSE_THETA_SEAM.md.

Usage:
  python scripts/hasse_theta_seam_probe.py --output /tmp/seam.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.hasse_theta_seam import (
    SUCCDifferenceSource, gamma_pole_prime_bridge,
    gamma_subtracted_prime_current, prime_current_tail_enclosure,
    theta_xi_partial,theta_xi_tail_bound,
    raw_completed_finite_mutation, riemann_siegel_leading,
    symmetric_offline_quartet_counterexample,
    prime_source_moment_energy, prime_current_finite_differences,
)


def _strfrac(q):
    return str(q)


def run(*, dps=90, prime_cutoff=101):
    import mpmath as mp
    true=SUCCDifferenceSource.zeta(180)
    mutant={n:1 for n in range(1,181)}
    mutant[6]=2
    fake=SUCCDifferenceSource.from_prefix(mutant,180)
    zeta_neg={}
    for m in (0,1,2,3,4,6,8):
        r=true.zeta_negative_certified(m)
        zeta_neg[str(-m)]={
            "eta":str(r["eta"]),
            "zeta":str(r["zeta"]),
            "independent_hasse":str(r["hasse"]),
            "euler_succ_terms":m+1,
            "hasse_succ_terms":m+2,
        }
    with mp.workdps(dps):
        jets={}
        for m in (1,2,3):
            x=gamma_pole_prime_bridge(m,terms=120,dps=dps)
            y=gamma_subtracted_prime_current(m,terms=120,dps=dps)
            p=prime_current_tail_enclosure(m,prime_cutoff,dps=dps)
            jets[str(-2*m)]={
                "zeta_prime_from_infinite_succ_jets":mp.nstr(
                    x["zeta_derivative_from_finite_differences"],28),
                "zeta_prime_from_safe_zeta":mp.nstr(
                    x["zeta_derivative_from_safe_euler"],28),
                "positive_current_from_gamma_subtracted_jets":mp.nstr(
                    y["gamma_corrected_negative_side"],28),
                "positive_current_from_safe_euler":mp.nstr(
                    y["positive_safe_prime_current"],28),
                "finite_prime_lower":mp.nstr(p["lower"],24),
                "omitted_prime_upper_bound":mp.nstr(p["tail_upper_bound"],12),
                "SUCC_derivative_window_size":121,
                "note":"zero scalar finite; first/second SUCC spectral jets nonterminating",
            }
        s=mp.mpc("0.5","4")
        xi_from_theta=theta_xi_partial(s,max_integer=4,dps=dps)
        xi_bound=theta_xi_tail_bound(s,max_integer=4,dps=dps)
        zeta_strip=true.zeta_from_eta_analytic(s,terms=112,dps=dps)
        xi_from_hasse= s*(s-1)/2*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*zeta_strip
        s2=mp.mpc(2)
        fake_completion=raw_completed_finite_mutation(s2,n=6,delta=1,dps=dps)
        true_completion=theta_xi_partial(s2,max_integer=6,dps=dps)
        forced_symmetry=theta_xi_partial(s2,max_integer=6,dps=dps,mutations={6:2})
        early=riemann_siegel_leading(200,source=fake,dps=dps)
        later=riemann_siegel_leading(250,source=fake,dps=dps)
        off=symmetric_offline_quartet_counterexample()
        moment_true=prime_source_moment_energy(
            (1,-3,2),source_horizon=128,dps=dps)
        moment_fake=prime_source_moment_energy(
            (1,-3,2),source_horizon=128,fake_composite_six=1,dps=dps)
        moment_succ=prime_current_finite_differences(
            1,4,source_horizon=128,dps=dps)
        return {
            "status":"FINITE_SUCC_HASSE_THETA_SEAM_REPLAY",
            "provenance":"preexisting classical identities, exact arithmetic and numerical calibrations",
            "sources":{"genuine_prefix":true.horizon,"fake_at_6":2,
                       "fake_primitive_2_seam":{str(k):str(v)
                                  for k,v in fake.parity_source_defects(
                                      primitive_only=True).items()}},
            "exact_negative_zeta_values":zeta_neg,
            "trivial_zero_gamma_pole_jets":jets,
            "critical_strip_transport_comparison":{
                "sample_s":"1/2+4i, NOT selected from any zero list",
                "xi_theta_4_integer_terms":mp.nstr(xi_from_theta,35),
                "xi_from_112_eta_SUCC_differences":mp.nstr(xi_from_hasse,35),
                "absolute_gap":mp.nstr(abs(xi_from_theta-xi_from_hasse),16),
                "theta_critical_strip_analytic_tail_bound":mp.nstr(xi_bound,16),
                "eta_SUCC_numerical_error_is_NOT_interval_certified":True,
            },
            "source_seam_negative_control_at_s_2":{
                "genuine_completed_theta":mp.nstr(true_completion,35),
                "fake_actual_completed_dirichlet":mp.nstr(fake_completion,35),
                "fake_FORCED_symmetric_theta":mp.nstr(forced_symmetry,35),
                "actual_fake_minus_genuine":mp.nstr(
                    fake_completion-true_completion,25),
                "exact_fake_increment":"1/(36*pi)",
                "forced_symmetry_is_NOT_source_completion":True,
            },
            "riemann_siegel_square_root_window":{
                "spectral_t_200_fake_visibility":early["window"]>=6,
                "spectral_t_200_window":early["window"],
                "spectral_t_250_fake_visibility":later["window"]>=6,
                "spectral_t_250_window":later["window"],
                "new_source_activation_height":"t=72*pi, asymptotic main-sum only",
                "nonzero_remainder_is_required":True,
            },
            "positive_moment_source_control":{
                "true_Hankel_energy":mp.nstr(moment_true["energy"],25),
                "fake_composite_6_Hankel_energy":mp.nstr(moment_fake["energy"],25),
                "both_moment_energies_positive":bool(
                    moment_true["energy"]>0 and moment_fake["energy"]>0),
                "complete_SUCC_difference_fourth_order":mp.nstr(
                    moment_succ["positive_moment_formula"],25),
                "inertness":"generic positive composite event passes; NOT Weil",
            },
            "symmetric_fake_offline_zeros":{
                "critical_line_minimum":str(off["critical_line_positive_lower_bound"]),
                "off_line_real_parts":[str(x) for x in off["constructed_offline_zero_real_parts"]],
                "critical_line_polynomial":"(t^2 - 3/16)^2 + 1/16",
            },
            "nontrivial_zero_locations_or_ordinates_used":False,
            "missing":"full Weil pairing with independently derived source-specific positivity",
        }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dps",type=int,default=90)
    p.add_argument("--prime-cutoff",type=int,default=101)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    data=run(dps=a.dps,prime_cutoff=a.prime_cutoff)
    raw=json.dumps(data,sort_keys=True,indent=2)+"\n"
    if a.output is None:
        print(raw,end="")
    else:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(raw,encoding="utf-8")


if __name__=="__main__":
    main()
