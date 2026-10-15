"""Finite zero-lookup-free Zeno/adelic/Suzuki dyadic proof receipt."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from observational_succ import zeno_limit_transport as z
from observational_succ import adelic_zeno as a
from observational_succ import zeno_weil_dyadic as w


def receipt():
    real=z.GeometricSUCC("ORIGINAL_RATIONAL_ZENO",0,"real",0,1,Q(1,2))
    achilles=z.AchillesSUCC(Q(9,10),1,Q(1,10))
    a2=a.two_adic_inverse_limit_residue(4,8)
    blind=a.finite_place_blindspot((2,3,5))
    c=w.dyadic_stage(Q(1,2),7)
    assert real.state(4)==Q(15,16)
    assert real.modulus(Q(1,100))==7
    assert achilles.finite_checkpoint(2)["time"]==Q(99,100)
    assert achilles.finite_checkpoint(2)["remaining_gap"]==Q(9,1000)
    assert a2["observed_residue"]==a2["limit_residue"]==85
    assert blind["hidden_prime"]==7 and blind["rational_multiplier"]==Q(1,7)
    assert c["structural_norm_error"]<Q(1,1000)
    return {
      "schema":"ZENOSUCC_SOURCE_TYPED_LIMIT_V1",
      "source_parent":"dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc",
      "dichotomy":{"stage_4":"15/16","remaining":"1/16",
                   "modulus_at_1_over_100":7,
                   "physical_omega_action_done":False},
      "achilles":{"second_checkpoint_time":"99/100",
                 "second_remaining_gap":"9/1000","global_catch_time":"1"},
      "arrow":{"static_position_determines_velocity":False},
      "stadium":{"relative_speed":"2","independent_clocks_authenticated":False},
      "adic":{"two_adic_integer_stage4":"85","precision8_target_residue":85,
              "two_adic_limit":"-1/3","real_convergence_of_same_4_geometric_series":False},
      "finite_places":{"observed":[2,3,5],"hidden_denominator_prime":7,
                       "arch_multiplier":"1/7","hidden_p_expansion_norm":"7",
                       "rational_norm_product":"1"},
      "global_continuation_without_growth_bound_stable":False,
      "genuine_weil_dyadic":{"level":7,"gamma_modes":128,"spatial_cells":16384,
                "structural_error_below_1_over_1000":True,
                "all_node_intervals_authenticated":False,
                "all_test_weil_nonnegative_proved":False},
      "nontrivial_zero_coordinates_used":False,
      "physical_infinite_computation_executed":False
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--verify",type=Path)
    args=ap.parse_args()
    out=receipt()
    if args.verify:
        if json.loads(args.verify.read_text(encoding="utf-8")) != out:
            raise AssertionError("ZENOSUCC_RECEIPT_MISMATCH")
        print("ZENOSUCC_EXACT_SOURCE_RECEIPT_VERIFIED")
    else:
        print(json.dumps(out,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
