"""Exact source-hashed finite receipts for Witt-carry SUCC limit observer.

PYTHONPATH=. python scripts/witt_carry_learning_probe.py
No physical measurements; universal results require independent paper proofs.
"""
from __future__ import annotations
import hashlib
from itertools import product
from pathlib import Path
from fractions import Fraction as F
import json
from observational_succ.witt_carry_learning import (
 carry_cocycle, cocycle_square, digit_map_preserves_distance,
 full_ring_tables,first_carry_witness,learning_signature,
 update_version_space,delayed_tower_counterfeit,calibrated_ring_table_budget,
 sparse_factorial_prefix,full_ring_homogeneous_projection,geometric_bt_ball_profile,
 p_step_unipotent_probe,lifted_succ_loop,
 factorial_stage_modulus,factorial_prime_precision,factorial_cofinal_witness,
 factorial_counterfeit_characteristics,
)


def git_blob(path):
    data=path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    cocycles=0
    for p in (2,3,5,7):
        for a,b,c in product(range(p),repeat=3):
            x,y=cocycle_square(a,b,c,p)
            assert x==y
            cocycles+=1
    metrics=0
    for p,k in ((2,5),(3,4),(5,3)):
        for a,b in product(range(p**k),repeat=2):
            assert digit_map_preserves_distance(p,k,a,b)
            metrics+=1
    operations=0
    for p,k in ((2,3),(3,2),(5,2)):
        mm=full_ring_tables(p,k,'mixed')
        ee=full_ring_tables(p,k,'equal')
        assert mm['size']==ee['size'] and mm['add']!=ee['add']
        operations+=2*p**(2*k)
        assert full_ring_homogeneous_projection(p,k,'mixed')==2*p**(2*k)
        assert full_ring_homogeneous_projection(p,k,'equal')==2*p**(2*k)
    delayed=0
    for p in (2,3,5):
        for K in range(1,10):
            data=delayed_tower_counterfeit(p,K)
            assert data['honest'][:K]==data['counterfeit'][:K]
            assert data['honest'][K]!=data['counterfeit'][K]
            delayed+=1
    budgets={}
    for k in range(1,5):
        d=calibrated_ring_table_budget(2,k,F(1,4),F(1,8))
        assert d['total_level_error_bound']<=d['allocated_level_error']
        budgets[str(k)]={'all_table_cells':d['table_queries'],
                         'exact_repetitions_per_cell':d['repetitions_per_query'],
                         'actual_error_upper_bound':str(d['total_level_error_bound']),
                         'allocated_error':str(d['allocated_level_error'])}
    first={}
    for p in (2,3,5,7):
        first[str(p)]={'carry_diagnostic':first_carry_witness(p)['mixed_sum'],
                       'mixed_S_to_p_stage2':p_step_unipotent_probe(p,2,'mixed'),
                       'equal_S_to_p_stage2':p_step_unipotent_probe(p,2,'equal'),
                       'model_after_full_geometry':update_version_space(p,
                          tuple((k,learning_signature(p,k,'mixed','geometry')) for k in range(1,7)),
                          'geometry')['survivors'],
                       'model_after_marked_second_level':update_version_space(p,
                          tuple((k,learning_signature(p,k,'mixed','marked_addition')) for k in (1,2)),
                          'marked_addition')['survivors'],
                       'unlabelled_BT_ball_radius3':geometric_bt_ball_profile(p,3)['total']}
    graded_holonomy=0
    for p,k in ((2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(5,2),(5,3)):
        m=lifted_succ_loop(p,k,'mixed')
        e=lifted_succ_loop(p,k,'equal')
        assert m['coarse_return'] and e['coarse_return']
        assert m['fine_value']==p**(k-1) and e['fine_value']==0
        graded_holonomy+=2
    cofinal=0
    for modulus in range(1,201):
        witness=factorial_cofinal_witness(modulus)
        assert factorial_stage_modulus(witness['stage'])%modulus==0
        cofinal+=1
    factorial_precision_cases=0
    for k in range(1,16):
        pdepth=factorial_prime_precision(k)
        assert factorial_stage_modulus(k)==__import__('math').prod(p**v for p,v in pdepth.items())
        factorial_precision_cases+=1
    fake=factorial_counterfeit_characteristics(4)
    assert fake['cardinality_of_both']==24
    assert fake['mixed_ring_characteristic']==24
    assert fake['equal_local_product_characteristic']==6
    report={
        'research':'SUCC_WITT_CARRY_OBSERVER_LIMIT_2026_10_22',
        'status':'CLASSICAL_PAPER_THEOREMS_EXACT_FINITE_CHECKS_NOT_LEAN_CERTIFIED',
        'actual_physical_source_readings':False,
        'empirical_error_rate_calibrated':False,
        'whole_infinite_observation_program_executed':False,
        'geometry_physically_identified':False,
        'gravitational_ER_EPR_proved':False,
        'signed_completed_Weil_positivity_proved':False,
        'RH_proved':False,
        'carry_cocycle_exact_instances':cocycles,
        'graded_lifted_succ_holonomy_tests':graded_holonomy,
        'factorial_cofinal_modulus_cases':cofinal,
        'factorial_valuation_level_cases':factorial_precision_cases,
        'global_equalchar_factorial_counterfeit_at_4':fake,
        'whole_tree_digit_isometry_exact_instances':metrics,
        'independent_finite_ring_operation_cells':operations,
        'delayed_counterfeit_tower_tests':delayed,
        'source_rigidity_second_level_fingerprints':first,
        'noisy_full_table_calibration_p2':budgets,
        'geometry_only_all_levels_cannot_identify_characteristic':True,
        'marked_source_addition_distinguishes_second_level':True,
        'sparse_factorial_Zp_completion_without_original_Z_realizer':True,
        'full_finite_table_and_compatible_parent_maps_required_for_global_geometry':True,
        'source_module_git_blob':git_blob(root/'observational_succ/witt_carry_learning.py'),
        'primary_tests_git_blob':git_blob(root/'tests/test_witt_carry_learning.py'),
        'extended_tests_git_blob':git_blob(root/'tests/test_witt_carry_extended.py'),
        'probe_git_blob':git_blob(root/'scripts/witt_carry_learning_probe.py'),
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':main()
