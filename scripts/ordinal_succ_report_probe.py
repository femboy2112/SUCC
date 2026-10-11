#!/usr/bin/env python3
"""Reproduce finite SUCC observer second-order Weil-report controls.

Mathematical ordinal omega/omega+1 semantics are recorded as
a DESCRIPTION, not an infinite computation or an RH proof.

python scripts/ordinal_succ_report_probe.py --output /tmp/ordinal-succ.json
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.ordinal_succ_report import (
    OrdinalFiniteStage,exact_bounded_time_horizon,
    quartic_observer_report,exact_polynomial_rectangle,
    oscillator_observer_report,synthetic_ordinal_semantics,
    harmonic_half_density_observer,harmonic_dyadic_divergence_certificate,
)
from observational_succ.gamma_interferometer import individual_impulse_determinant


def run(*,dps=72,horizon=28):
    if type(dps) is not int or not 50<=dps<=130:
        raise ValueError("Precision must be in 50..130")
    if type(horizon) is not int or not 15<=horizon<=256:
        raise ValueError("Need source horizon in 15..256")
    import mpmath as mp
    a=OrdinalFiniteStage.genuine(horizon)
    mutated={n:1 for n in range(1,horizon+1)}
    mutated[6]=2
    fake=OrdinalFiniteStage.from_prefix(mutated,horizon)
    early=OrdinalFiniteStage.genuine(9)
    times=(Q(0),Q(-1),Q(1))
    with mp.workdps(dps):
        k1=early.report(times,dps=dps)["kernel"]
        k2=a.report(times,dps=dps)["kernel"]
        same=max(abs(k1[i][j]-k2[i][j]) for i in range(3) for j in range(3))
        rational_time=Q(9,5)
        true_report=a.report((Q(0),rational_time),dps=dps)
        fake_report=fake.report((Q(0),rational_time),dps=dps)
        curvature=fake.connected_pair_curvature(2,3)
        jump=fake._gamma_snapshot().slope_jump(6,dps=dps)
        det=individual_impulse_determinant(mp.log(2),
                                           mp.log(2)/mp.sqrt(2),dps=dps)
        mixed=a.rectangle_increment(Q(3,5),Q(1,5),
                                   Q(1,20),Q(1,30),dps=dps)
        oscillator=oscillator_observer_report((Q(0),Q(1),Q(2),Q(3)),dps=dps)
        quartic=quartic_observer_report()
        ordinal=synthetic_ordinal_semantics(horizon)
        semantic_true=a.restrict(6).semantic_log_partition_hessian(2,3)
        semantic_fake=fake.restrict(6).semantic_log_partition_hessian(2,3)
        half_density=harmonic_half_density_observer(256,3)
        diverges=harmonic_dyadic_divergence_certificate(8)
        answer={
            "status":"FINITE_ORDINAL_SUCC_SECOND_ORDER_WEIL_PROBE",
            "no_actual_infinite_ordinal_computed":True,
            "no_RH_or_Weil_positive_sign_assumed":True,
            "formal_ordinals":{
                "finite_successor":"n->n+1, complete source prefix",
                "limit_omega":"filtered colimit/union of coherent finite observations",
                "omega_plus_one":"mathematical retrospective Suzuki/Weil report",
                "finite_run_is_not_limit":not ordinal["omega_computation_executed"],
                "global_PSD_predicate_proved":ordinal["report_property_proved"],
            },
            "bounded_query_stabilization":{
                "rational_times":["0","-1","1"],
                "sufficient_stage":exact_bounded_time_horizon(times)[
                    "certified_source_SUCC_horizon"],
                "earlier_observer_stage":early.n,
                "later_observer_stage":a.n,
                "max_matrix_change":mp.nstr(same,25),
                "scope":"prime wavefront exact by finite stage; Gamma response separately analytic",
            },
            "connected_source_second_order":{
                "primes":[2,3],
                "composite_event":6,
                "true_connected_curvature":str(
                    a.connected_pair_curvature(2,3)["connected_second_order_residual"]),
                "fake_connected_curvature":str(curvature[
                    "connected_second_order_residual"]),
                "fake_slope_jump":mp.nstr(jump,30),
                "predicted_second_order_delta":"-log(6)/sqrt(6) at t=log(6)",
                "finite_observation_time":"9/5",
                "two_time_Weil_diagonal_fake_minus_true":mp.nstr(
                    fake_report["kernel"][1][1]-true_report["kernel"][1][1],30),
            },
            "semantic_second_derivative_information_geometry":{
                "source":"Hessian log finite positive evidence partition function",
                "genuine_Hessian":[[str(x) for x in row]
                                   for row in semantic_true["Hessian_log_Z"]],
                "fake_six_Hessian":[[str(x) for x in row]
                                    for row in semantic_fake["Hessian_log_Z"]],
                "genuine_covariance_determinant":str(
                    semantic_true["determinant"]),
                "fake_covariance_determinant":str(
                    semantic_fake["determinant"]),
                "both_information_geometries_PSD":True,
                "Weil_identification_established":False,
            },
            "two_observer_mixed_finite_difference":{
                "t":"3/5","u":"1/5","h":"1/20","k":"1/30",
                "mixed_covariance_increment":mp.nstr(mixed,30),
                "distributional_limit":"Psi''(t-u) = Weil distribution",
                "positive_definiteness_proved":False,
            },
            "hilbert_critical_line_observer_escape":{
                "stage":256,
                "finite_norm_squared":"1",
                "fixed_local_projector":"P_3",
                "local_projector_expectation":str(
                    half_density["finite_projector_expectation"]),
                "identity_expectation":str(
                    half_density["identity_expectation"]),
                "harmonic_H_256":str(diverges["exact_H_N"]),
                "H_256_lower_bound":str(diverges["provable_lower_bound"]),
                "weak_limit_zero_not_strong":True,
                "normalizable_omega_vector_exists":False,
                "source_inert_and_not_RH":True,
            },
            "positive_observations_are_not_positive_correlations":{
                "quartic_psi_nonnegative":True,
                "quartic_second_derivative_nonnegative":True,
                "quartic_kernel":[[str(z) for z in row]
                                  for row in quartic["kernel"]],
                "quartic_determinant":str(quartic["determinant"]),
                "quartic_quadratic_vector_ones":str(
                    quartic["quadratic_vector_ones"]),
                "isolated_prime_impulse_negative_determinant":mp.nstr(det,25),
                "oscillator_Hilbert_Gram_identity_error":mp.nstr(
                    oscillator["identity_error"],25),
                "oscillator_second_curvature_can_be_negative":True,
            },
            "next_theorem":"Source-defined positive-definite DISTRIBUTION Psi'' on complete test-function core; RH equivalent, NOT proved",
        }
        return answer


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dps",type=int,default=72)
    p.add_argument("--horizon",type=int,default=28)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    payload=json.dumps(run(dps=a.dps,horizon=a.horizon),sort_keys=True,indent=2)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(payload,encoding="utf-8")
    else:
        print(payload,end="")


if __name__=="__main__":
    main()
