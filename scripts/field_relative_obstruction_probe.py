#!/usr/bin/env python3
"""Deterministic machine-readable receipts. No carrier source authentication."""
from __future__ import annotations
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.field_relative_closure import (
    FiniteField, minimal_inconsistent_core, invariant_orbits,
)
from observational_succ.field_probe_repair import (
    repair,verify_repair,set_cover_field,
)
from observational_succ.field_context_descent import (
    SourceVoltageGraph, audit_descent,
)
from observational_succ.field_limit_countermodels import (
    omega_rival_at_horizon,unrealizable_limit_prefix,
)
from observational_succ.field_analytic_shadow_countermodel import (
    symmetric_jet_with_forced_offline_zero,
)


def receipt()->dict:
    bits=((0,0),(0,1),(1,0),(1,1))
    f=FiniteField("two-bit-original-source","version-1",bits,
        {"a":(0,0,1,1),"b":(0,1,0,1),"const":(0,0,0,0)},
        {"xor":(0,1,1,0)})
    fa=f.factor(("a",),"xor")
    fab=f.factor(("a","b"),"xor")
    assert not fa.proved and fab.proved
    assert f.verify(fa) and f.verify(fab)

    even=((0,0,0),(0,1,1),(1,0,1),(1,1,0))
    parity=FiniteField("even-parity-source","v1",even,
        {f"bit{i}":tuple(x[i] for x in even) for i in range(3)},
        {"target":tuple(x[0] for x in even)})
    claims=tuple((f"bit{i}",1) for i in range(3))
    real=parity.local_realizability(claims)
    core=minimal_inconsistent_core(parity,claims)
    assert real['pairwise_realizable'] and not real['fiber']
    assert len(core.minimal_records)==3

    graph=SourceVoltageGraph("winding-3",0,(0,1,2),
         ((0,1,(1,)),(1,2,(1,)),(2,0,(1,))),1)
    loop=graph.integrate()
    assert graph.verify(loop) and loop.status=="NONZERO_HOLONOMY"
    assert abs(loop.escape.translation[0])==3

    cover=set_cover_field(6,({0,1,2,3},{0,1,4},{2,3,5}))
    r=repair(cover,("pair_index",),("cover_0","cover_1","cover_2"),"original_bit")
    assert verify_repair(cover,r) and r.selected==("cover_1","cover_2")

    A=(0,1,3,2);B=(0,3,2,1)
    zeros=invariant_orbits((0,1,2,3),(A,B),(1,0,0,0))
    xor=invariant_orbits((0,1,2,3),(A,B),(0,1,1,0))
    assert zeros['claim_is_frame_invariant'] and not xor['claim_is_frame_invariant']

    original=FiniteField("original","v1",(0,1),{"r":(0,1)},{"t":(0,1)})
    destroyed=FiniteField("updated","v1",(0,1),{"r":(0,0)},{"t":(0,0)})
    desk=audit_descent(original,destroyed,(0,0),("r",),("r",),"t","t")
    assert desk.covariance and not desk.truth_square and not desk.updated_report_proves_original_claim

    analytic=symmetric_jet_with_forced_offline_zero(8)
    omega=omega_rival_at_horizon(100)
    unre=unrealizable_limit_prefix(100)
    # Computed, not asserted: a single repair probe is impossible iff NO singleton
    # candidate proves the factorization (exhaustive over the candidate menu).
    single_probe_suffices=any(
        cover.factor(("pair_index",c),"original_bit").proved
        for c in ("cover_0","cover_1","cover_2"))
    return {
        "status":"FINITE_CARRIER_RELATIVE_OBSTRUCTION_RECEIPT",
        "mathematical_status":"classical proof obligations plus exact finite source checks",
        "physical_source_authenticated":False,
        "omega_inferred_from_finite_scan":False,
        "rh_or_weil_sign_claimed":False,
        "two_bit": {"single_a_factors_xor":fa.proved,
                      "a_b_factors_xor":fab.proved,
                      "single_a_rival":str(fa.counterexample)},
        "local_realizability":{"pairwise":real['pairwise_realizable'],
             "globally_realized":bool(real['fiber']),"minimal_unsat_core":len(core.minimal_records)},
        "source_holonomy":{"status":loop.status,
            "translation":list(loop.escape.translation),
            "source_walk_verified":graph.verify(loop)},
        "repair":{"minimum_probe_count":len(r.selected),"selected":list(r.selected),
                  "lower_probe_count_1_impossible":not single_probe_suffices},
        "frame_holonomy":{"source_zero_invariant":zeros['claim_is_frame_invariant'],
              "source_xor_invariant":xor['claim_is_frame_invariant']},
        "changing_carrier":{"observation_square_commutes":desk.covariance,
              "original_target_truth_preserved":desk.truth_square,
              "original_target_decodable":desk.updated_report_proves_original_claim},
        "limit_controls":{"prefix_horizon":100,
                 "boundary_rival":omega['rival'],
                 "locally_realizable_no_global_source":not unre['infinite_report_realizable']},
        "analytic_moonshot_falsifier":{
             "reflection_symmetry":analytic["reflection_symmetric"],"matching_origin_jet_order":analytic["jet_order"],
             "offcritical_zero_real":str(analytic["zero_real"]),
             "offcritical_zero_imag":str(analytic["zero_imag"]),
             "actual_riemann_xi_modified":analytic["actual_Riemann_xi_used_or_modified"]},
        "academic_novelty_claim":False,
    }

if __name__=='__main__':
    print(json.dumps(receipt(),sort_keys=True,indent=2))
