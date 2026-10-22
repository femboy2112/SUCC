"""Source-bound exact boundary-response and observation-anchoring receipt.

This probe contains NO actual measured alpha, Euler gamma, or physical
calibration. It exercises synthetic competing boundary realizations only.
"""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from observational_succ.boundary_realization_selection import (
    FiniteNetwork, PredictedBranch, BoundaryObservation,
    boundary_response, boundary_glue, surviving_branches,
)


def _blob(path):
    b=path.read_bytes()
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()


def _encode(M):
    return [[str(x) for x in row] for row in M]


def main():
    root=Path(__file__).resolve().parents[1]
    edge=FiniteNetwork(2,(0,1),((0,1,Q(1,2)),))
    path=FiniteNetwork(3,(0,2),((0,1,Q(1)),(1,2,Q(1))),((1,Q(1)),))
    d0=boundary_response(edge)
    p0=boundary_response(path)
    d1=boundary_response(edge,1)
    p1=boundary_response(path,1)
    assert d0==p0
    assert d1!=p1
    total=boundary_glue(boundary_response(FiniteNetwork(2,(0,1),((0,1,Q(1,3)),))),d0)
    assert total[0][0]==Q(5,6)
    static_models=(PredictedBranch('edge','edge-topology',d0[0][0]),
                   PredictedBranch('path','path-topology',p0[0][0]),
                   PredictedBranch('third','other-topology',Q(1,3)))
    static_selection=surviving_branches(static_models,BoundaryObservation(Q(1,2),Q(1,100)))
    assert static_selection['survivors']==('edge','path')
    assert not static_selection['unique_class_within_declared_family']
    dynamic_models=(PredictedBranch('edge','edge-topology',d1[0][1]),
                    PredictedBranch('path','path-topology',p1[0][1]))
    dynamic_selection=surviving_branches(dynamic_models,BoundaryObservation(Q(-1,3),Q(1,100)))
    assert dynamic_selection['survivors']==('path',)
    assert dynamic_selection['unique_class_within_declared_family']
    print(json.dumps({
        'research':'SUCC_OBSERVATION_ANCHORED_BOUNDARY_RIGIDITY_2026_10_22',
        'scope':'exact finite graph DtN, measurement-interval selection, two-stage dynamic holdout',
        'paper_theorem':'conditional selection of measured boundary equivalence class, not physical reality by fiat',
        'source_branch':'research/total-boundary-adelic-impedance-2026-10-22',
        'single_edge_static_response':_encode(d0),
        'series_path_static_response':_encode(p0),
        'single_edge_dynamic_s1':_encode(d1),
        'series_path_dynamic_s1':_encode(p1),
        'glued_parallel_static_response':_encode(total),
        'static_indistinguishable_topologies':True,
        'static_surviving_models':static_selection['survivors'],
        'static_unique_class':False,
        'heldout_dynamic_surviving_models':dynamic_selection['survivors'],
        'heldout_dynamic_unique_class':True,
        'fine_structure_constant_predicted_from_SUCC':False,
        'Euler_Mascheroni_mathematical_value_physically_measured_here':False,
        'independent_physical_measurements_performed':False,
        'gravitational_ER_EPR_proved':False,
        'signed_Weil_positivity_proved':False,
        'RH_proved':False,
        'source_module_git_blob':_blob(root/'observational_succ/boundary_realization_selection.py'),
        'tests_module_git_blob':_blob(root/'tests/test_boundary_realization_selection.py'),
    },sort_keys=True,indent=2))


if __name__=='__main__':main()
