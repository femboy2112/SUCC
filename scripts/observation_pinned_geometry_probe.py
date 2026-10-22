"""Deterministic exact source/probe receipt. No actual physical measurements supplied."""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from hashlib import sha1
from pathlib import Path
import json

from observational_succ.observation_pinned_geometry import (
 qphase,src_affine_phase,phase_affine,multiplier_image_count,
 first_shell_cycle_fingerprint,projective_first_shell,
 axis_vertex,axis_distance,dilation_root_displacement,
 equal_first_shell_distinct_ring_witness,
 oriented_cycle_probe,counterfeit_extension_orders,hidden_four_state_alias,
)


def git_blob_hash(path):
    data=path.read_bytes()
    return sha1(f"blob {len(data)}\0".encode()+data).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    naturality=0
    for p in (2,3,5):
        for k in range(1,4):
            for n in range(-15,26):
                for a,b in ((1,1),(2,0),(3,0),(2,3)):
                    assert src_affine_phase(n,a,b,p,k)==phase_affine(qphase(n,p,k),a,b,p,k)
                    naturality+=1
    images=0
    for p in (2,3,5):
        for k in range(1,4):
            for q in (2,3,5,6,8):
                modulus=p**k
                assert multiplier_image_count(q,p,k)==len({q*x%modulus for x in range(modulus)})
                images+=1
    shell={}
    for p in (2,3,5,7):
        f=first_shell_cycle_fingerprint(p)
        assert f['root_degree']==len(projective_first_shell(p))==p+1
        assert len(f['nonfixed_cycle'])==p
        assert axis_distance(p,-2,3)==5
        assert dilation_root_displacement(p,p)==1
        shell[str(p)]={'degree':f['root_degree'],'succ_nonfixed_cycle':p,
                       'succ_fixed_point_count':1,'Vp_root_displacement':1}
    ring={}
    for p in (2,3,5):
        x=equal_first_shell_distinct_ring_witness(p)
        assert x['integer_ring_p_times_one']!=x['equal_characteristic_ring_p_times_one']
        ring[str(p)]={'first_shell_equivalent':True,
                      'second_level_multiplier_image_counts':[
                          x['integer_ring_mul_p_image_count'],x['equal_characteristic_ring_mul_p_image_count']]}
    fakes=0
    for p in (2,3,5):
        for depth in range(1,5):
            true,fake=counterfeit_extension_orders(p,depth)
            assert true[:depth]==fake[:depth] and true[depth]!=fake[depth]
            fakes+=1
    dry=[]
    for p in (2,3,5,7):
        observations=tuple(str(i%p) for i in range(2*p+1))
        found=oriented_cycle_probe(observations,(2,3,5,7),'SYNTHETIC_NOT_PHYSICAL','SIMULATED_CLOCK')
        assert found['selected_p']==p
        assert not found['full_infinite_tower_empirically_verified']
        dry.append(p)
    hidden=hidden_four_state_alias()
    assert hidden['reported_period']==2 and hidden['true_period']==4
    report={
        'research':'OPIG_OBSERVATION_PINNED_GEOMETRY_2026_10_22',
        'status':'CLASSICAL_PAPER_THEOREMS_EXACT_FINITE_CONTROLS_NOT_LEAN',
        'actual_physical_experiment_performed':False,
        'physical_spacetime_identified':False,
        'gravitational_ER_EPR_proved':False,
        'signed_Weil_positivity_proved':False,
        'RH_proved':False,
        'assumptions':'faithful oriented source; full compatible cyclic ring p-power quotient tower; rank-two projective lift for BT geometry',
        'finite_source_affine_naturality_cases':naturality,
        'independent_multiplier_image_tests':images,
        'first_shell_fingerprints':shell,
        'distinct_complete_sources_same_first_shell':ring,
        'finite_horizon_tower_counterexamples':fakes,
        'synthetic_cycle_candidate_selections':dry,
        'hidden_state_alias_counterexample':True,
        'geometry_forced_conditionally':'Zp coset tree and PGL2(Qp) lattice tree (rank two supplied) with source-equivariant affine action',
        'physical_global_truth_from_one_finite_observation':False,
        'source_module_git_blob':git_blob_hash(root/'observational_succ/observation_pinned_geometry.py'),
        'exact_tests_git_blob':git_blob_hash(root/'tests/test_observation_pinned_geometry.py'),
    }
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=='__main__':main()
