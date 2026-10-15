#!/usr/bin/env python3
"""Recompute an exact wild/Alexander SUCC source-theorem receipt.

No horn geometry is generated, nor physical sensors or completed Weil positivity.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.wild_ambient_succ import (
    SourceFrame, SquareDisk, RectangularThread, certified_linking,
    intrinsic_vs_ambient_observer, alexander_imported_complement,
    commutator_tower_receipt, a5_commutator_witnesses,
    a5_tower_assignment, a5_conjugacy_invariant_observer,
    alexander_a5_finite_quotient,
    abelian_character_of_expanded_root, covering_monodromy,
    solenoid_cohomology_class, compressed_flat_operator_control,
    a5_holonomy_energy_sign_control, reflection_positive_no_go,
)


def jsonable(value):
    if isinstance(value,Fraction):
        return f'{value.numerator}/{value.denominator}'
    if isinstance(value,dict):
        return {str(k):jsonable(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [jsonable(x) for x in value]
    if isinstance(value,bool) or value is None or type(value) in (int,str):
        return value
    raise TypeError('No floating/unknown source may enter the receipt')


def receipt():
    src=SourceFrame('wild_ambient_exact_PL_source',0,'xyz_integer_common_orientation',1)
    disk=SquareDisk(Fraction(2),1,src)
    linked=RectangularThread(Fraction(1),Fraction(3),Fraction(1),1,src)
    unlink=RectangularThread(Fraction(3),Fraction(5),Fraction(1),1,src)
    root_tower=a5_tower_assignment(6)
    return jsonable({
        'status':'WILD_AMBIENT_SUCC_EXACT_SOURCE_MODEL',
        'frozen_parent':'205ffd020dd2a320eeac70a91a2a2700c969c048',
        'RH_proved':False,
        'nontrivial_zeta_zero_coordinates_input':False,
        'physical_horn_geometry_constructed':False,
        'physical_A5_instrument_executed':False,
        'alexander_theorem_dependency':alexander_imported_complement(),
        'intrinsic_vs_ambient':intrinsic_vs_ambient_observer(),
        'exact_PL_linking':{
            'hopf':certified_linking(disk,linked),
            'unlinked':certified_linking(disk,unlink),
            'orientation_reversed':certified_linking(disk,RectangularThread(1,3,1,-1,src)),
        },
        'commutator_tower':{
            'finite_stages':[commutator_tower_receipt(i) for i in range(1,7)],
            'direct_limit_perfect_group_proof':'free_product_injection_and_commutator_generation',
            'actual_topology_identification':'IMPORTED_HATCHER_P171_172',
            'scalar_windings_mod_7':[abelian_character_of_expanded_root(n,7) for n in range(1,7)],
        },
        'nonabelian_A5':{
            'group_order':60,
            'commutator_candidate_pairs':60*60,
            'commutator_image_size':len(a5_commutator_witnesses()),
            'finite_nesting':root_tower,
            'conjugacy_invariant':a5_conjugacy_invariant_observer(),
            'finite_surjective_quotient':alexander_a5_finite_quotient(),
            'source_to_arithmetic_Weil_map_constructed':False,
        },
        'other_inverse_system':{
            'dyadic_cohomology_representatives':[solenoid_cohomology_class(1,i,2) for i in range(6)],
            'monodromy_degree_2_winding_1':covering_monodromy(2,1),
            'monodromy_degree_2_winding_2':covering_monodromy(2,2),
            'actual_horned_sphere_is_solenoid':False,
        },
        'no_go_controls':{
            'compressed_flat_matrices':compressed_flat_operator_control(),
            'A5_source_signed_energy':a5_holonomy_energy_sign_control(),
            'reflection_symmetry_indefinite':reflection_positive_no_go(),
        },
        'claim_boundaries':{
            'topological_exterior_source_provenance':'Alexander_1924_and_Hatcher_2B_imported',
            'abstract_group_direct_limit_proved_from_declared_rules':True,
            'new_finite_nonabelian_source_diagnostic':True,
            'original_weil_Q_identified_with_A5_connection':False,
            'completed_weil_all_test_positive':False,
            'general_wildness_decider_claimed':False,
        }
    })


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    obj=receipt()
    raw=json.dumps(obj,sort_keys=True,indent=2)+'\n'
    if args.verify:
        stored=json.loads(args.verify.read_text(encoding='utf-8'))
        if stored!=obj:
            raise SystemExit('WILD_AMBIENT_RECEIPT_MISMATCH')
        print('WILD_AMBIENT_SUCC_RECEIPT_VERIFIED')
    elif args.output:
        args.output.write_text(raw,encoding='utf-8')
        print('WILD_AMBIENT_SUCC_RECEIPT_WRITTEN')
    else:
        print(raw,end='')

if __name__=='__main__':main()
