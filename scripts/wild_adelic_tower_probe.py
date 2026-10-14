"""Deterministic original-source WILD ADELIC SUCC exact receipt generator."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ.wild_adelic_tower import (
    TowerLaw, ExteriorEmbeddingContract, CohomologyWindingCertificate,
    finite_arithmetic_no_free_tail, source_qualified_folner_energy,
    pinched_tame_arc_inverse_lipschitz_bound,
)


def receipt():
    common = {'source_id':'Z-source:0', 'epoch':14, 'basis':'common-real-profinite-phase'}
    factorial = TowerLaw(**common, kind='factorial')
    dyadic = TowerLaw(**common, kind='constant', constant=2)
    distinct = TowerLaw(**common, kind='distinct_primes')
    ex = ExteriorEmbeddingContract(factorial,'CONDITIONAL-unknotted-cables',
                                   factorial.source_id,factorial.epoch,'unknotted_torus')
    internal = CohomologyWindingCertificate(factorial)
    m=6
    level=3
    deep=factorial.inverse_level(level,m)
    target=factorial.real_flow_phases(F(7,11),deep)
    inverse=factorial.inverse_coordinate(level,m,target)
    delta_stage = 1
    while factorial.D(delta_stage)%m:
        delta_stage += 1
    steps=[(F(1,2),F(1)),(F(-2,3),F(2)),(F(4,5),F(1,7))]
    return {
        'schema':'succ-wild-adelic-1', 'campaign_date':'2026-10-14',
        'source':common,
        'source_domains':{
            'factorial_degrees_1_to_7':[factorial.degree(i) for i in range(1,8)],
            'factorial_D_0_to_6':[factorial.D(i) for i in range(7)],
            'dyadic_D_0_to_6':[dyadic.D(i) for i in range(7)],
            'distinct_primes_1_to_6':[distinct.degree(i) for i in range(1,7)],
        },
        'dual_localization':{
            'factorial_group':'Q', 'dyadic_group':'Z[1/2]',
            'distinct_primes_group':'squarefree-denominator subgroup of Q',
            'factorial_intrinsic_cech_value':str(internal.transport(0,6,5)[1]),
            'factorial_unknotted_exterior_value':str(ex.exterior_group_value(6,5*factorial.D(6))),
            'extrinsic_embedding_stipulated_not_geometrically_verified':True,
            'unknown_ambient_embedding_may_have_different_pi1':True,
        },
        'globalization':{
            'm2_dyadic_automorphism':dyadic.scale_automorphism(2),
            'm3_dyadic_automorphism':dyadic.scale_automorphism(3),
            'm6_dyadic_kernel':dyadic.dual_kernel_order(6),
            'm6_factorial_automorphism':factorial.scale_automorphism(6),
            'm6_factorial_kernel':factorial.dual_kernel_order(6),
            'm2_distinct_primes_automorphism':distinct.scale_automorphism(2),
            'm2_distinct_primes_kernel':distinct.dual_kernel_order(2),
            'inversion_requested_level':level, 'inversion_m':m,
            'inversion_deep_level':deep,
            'inverted_real_coordinate':str(inverse),
            'original_target_coordinate':str(target[level]),
            'm_times_inverse_is_target':(m*inverse)%1==target[level],
            'snake_delta_6_root_5':factorial.delta_circle_root(6,5,delta_stage),
            'snake_delta_6_root_5_expected':5,
            'finite_circle_m6_kernel':6,
        },
        'tail_obstruction':finite_arithmetic_no_free_tail((2,3,5,7),2,3),
        'exact_gram_gap_control':{
            'steps':[(str(s),str(w)) for s,w in steps],
            'folner_N_100':str(source_qualified_folner_energy(factorial,steps,100)),
            'folner_N_1000':str(source_qualified_folner_energy(factorial,steps,1000)),
            'no_uniform_gap_for_these_shifts':True,
            'not_the_Weil_quadratic_form':True,
        },
        'ambient_conditioning_toy':{
            'resolution_2_inverse_lipschitz_lower':str(pinched_tame_arc_inverse_lipschitz_bound(2)),
            'resolution_12_inverse_lipschitz_lower':str(pinched_tame_arc_inverse_lipschitz_bound(12)),
            'toy_is_not_an_Alexander_horned_sphere':True,
        },
        'claim_status':{
            'WA-01_to_WA-04':'CLASSICAL / SOURCE-SPECIALIZED PAPER PROOFS',
            'WA-05_to_WA-13':'CLASSICAL TOPOLOGICAL INPUTS + EXACT ARITHMETIC CERTIFICATES',
            'WA-14_to_WA-15':'PAPER PROOF VIA ARZELA-ASCOLI, NO PRIORITY CLAIM',
            'WA-16_to_WA-17':'CLASSICAL COMPACTNESS + EXACT FINITE FOLNER',
            'explicit_geometric_Alexander_embedding_built':False,
            'real_physical_source_authenticated':False,
            'Lean_topology_kernel_claimed':False,
            'additive_adele_class_identified_with_multiplicative_idele_class':False,
            'Weil_form_identified_with_solenoid_gram':False,
            'original_nontrivial_zeta_zero_positions_used':False,
            'RH_PROVED':False,
        },
    }


def encoded():
    return json.dumps(receipt(),indent=2,sort_keys=True,ensure_ascii=False)+'\n'


def main():
    ap=argparse.ArgumentParser()
    g=ap.add_mutually_exclusive_group()
    g.add_argument('--verify',type=Path)
    g.add_argument('--write',type=Path)
    args=ap.parse_args()
    s=encoded()
    if args.verify:
        expected=args.verify.read_text(encoding='utf-8')
        if expected!=s:
            raise SystemExit('SOURCE RECEIPT MISMATCH: '+str(args.verify))
        print('WILD_ADELIC_SOURCE_RECEIPT_VERIFIED')
    elif args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(s,encoding='utf-8')
        print('WILD_ADELIC_SOURCE_RECEIPT_WRITTEN',args.write)
    else:
        print(s,end='')


if __name__ == '__main__':
    main()
