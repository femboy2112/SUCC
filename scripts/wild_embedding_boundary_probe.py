"""Frozen *finite* wild-observer and boundary-defect research receipt.

The original Alexander horned sphere and Alexander duality are classical
theorems imported in the dossier, NOT generated or verified by this script.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from observational_succ import wild_embedding_probes as w
from observational_succ import wild_boundary_compression as b


def receipt():
    sphere=w.intrinsic_double_cone()
    assert (sphere["vertices"],sphere["edges"],sphere["faces"])==(6,12,8)
    assert sphere["Betti_Q"]==(1,0,1)
    ladder=[]
    for k in range(1,6):
        r=w.deep_commutator_receipt(k)
        assert r["up_to_level"]==()
        assert r["leading_X_power_Y_coefficient"]==1
        ladder.append({"level":k,"reduced_length":r["word_length"],
                       "abelianization":list(r["abelianization"]),
                       "vanishes_up_to_magnus_degree":k,
                       "detected_at_degree":r["first_visible_degree"],
                       "leading_X_power_Y_coefficient":1})
    s3=w.permutation_commutator_spectrum(3)
    a5=w.permutation_commutator_spectrum(5,even_only=True)
    assert (s3["group_order"],s3["distinct_commutators"])==(6,3)
    assert (a5["group_order"],a5["distinct_commutators"])==(60,60)
    boundary=b.finite_boundary_certificate()
    assert boundary.full_commutator==b.zero(5,5)
    assert boundary.norm_square_frobenius==2
    assert boundary.leakage_difference_matches and boundary.triple_coherence_zero
    inv=b.unitary_sign_invariance_control()
    assert inv["original_negative_rayleigh"]==inv["transported_negative_rayleigh"]==-1
    return {
        "source_parent":"dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc",
        "schema":"SUCC_WILD_EMBEDDING_PROBE_V1",
        "intrinsic_s2":{"V":sphere["vertices"],"E":sphere["edges"],
                        "F":sphere["faces"],"Euler":sphere["Euler"],
                        "Betti_Q":list(sphere["Betti_Q"])},
        "toy_magnus_invisible_until_depth":ladder,
        "finite_group_calibration":{"S3_order":s3["group_order"],
                                    "S3_distinct_commutators":s3["distinct_commutators"],
                                    "A5_order":a5["group_order"],
                                    "A5_distinct_commutators":a5["distinct_commutators"]},
        "finite_boundary_toy":{"source_id":boundary.source_id,
                               "full_T_C_commute":True,
                               "compressed_commutator":
                                [[str(x) for x in r] for r in boundary.compressed_commutator],
                               "commutator_squared_frobenius":str(boundary.norm_square_frobenius),
                               "leakage_difference_identity":boundary.leakage_difference_matches,
                               "three_model_associativity_identity":boundary.triple_coherence_zero,
                               "real_arithmetic_source_identified":boundary.gamma_source_identified},
        "orthogonal_transport":{"negative_rayleigh_before":str(inv["original_negative_rayleigh"]),
                                "negative_rayleigh_after":str(inv["transported_negative_rayleigh"]),
                                "actual_weil_intertwiner_constructed":inv["actual_wild_to_weil_intertwiner"]},
        "actual_horned_sphere_fundamental_group_computed":False,
        "actual_3d_wild_embedding_constructed":False,
        "completed_weil_positivity_proved":False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    args=parser.parse_args()
    value=receipt()
    if args.verify:
        expected=json.loads(args.verify.read_text(encoding="utf-8"))
        if expected!=value:
            raise AssertionError("WILD_BOUNDARY_RECEIPT_MISMATCH")
        print("WILD_BOUNDARY_FINITE_RECEIPT_VERIFIED")
    else:
        print(json.dumps(value,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
