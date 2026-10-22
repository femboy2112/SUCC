"""Deterministic exact-rational proof/model replay with Git blob identity check.

No physical observation and no Lean proof claimed. Requires SUCC base branch.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path

from observational_succ.boundary_port_geometry import (
    PortFrame, diamond, diamond_bridge_inverse, diamond_contact_response,
    hidden_contact_defect, two_contact_gain_inverse, future_safe_partition,
)

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/'research/2026-10-22/BOUNDARY_PORT_GEOMETRY_EXACT_RECEIPT.json'
FILES=('observational_succ/boundary_port_geometry.py','tests/test_boundary_port_geometry.py')
PORTS=(('L','u'),('u','v'),('v','R'),('L','R'))
WEIGHTS=(Q(1),Q(7),Q(2),Q(3))


def git_blob(path):
    data=(ROOT/path).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()


def reproduce():
    base=diamond()
    f0=PortFrame.from_network(base,PORTS)
    perm_count=0; verified_intermediate=0; reverse_count=0
    for order in permutations(range(4)):
        frame=f0; net=base; log=[]
        for i in order:
            frame=frame.update(i,WEIGHTS[i]);net=net.add(PORTS[i],WEIGHTS[i]);log.append(i)
            if frame != PortFrame.from_network(net,PORTS):
                raise AssertionError('Independent full-graph Schur mismatch')
            verified_intermediate+=1
        perm_count+=1
        for i in reversed(log):
            frame=frame.reverse_recorded_update(i,WEIGHTS[i]);reverse_count+=1
        if frame!=f0:raise AssertionError('Recorded reverse history failed')
    if f0.Lambda!=PortFrame.from_network(diamond(7),PORTS).Lambda:
        raise AssertionError('Hidden source no longer invisible')
    inversions=0
    for a,g in product((Q(1,3),Q(1),Q(2),Q(17,5)),(Q(),Q(1),Q(7),Q(23,3))):
        if diamond_bridge_inverse(a,diamond_contact_response(a,g))!=g:
            raise AssertionError('Exact parameter inversion failed')
        inversions+=1
    _,r=two_contact_gain_inverse(1,diamond_contact_response(1,7)-1,
                                 2,diamond_contact_response(2,7)-1)
    if r!=Q(9,32):raise AssertionError('Green kernel probe failed')
    hidden=hidden_contact_defect(f0,1,0,Q(7),Q(1))
    if hidden['mixed_third_derivative_at_zero'][0][0]!=Q(1,8):
        raise AssertionError('Cubic source coupling failed')
    states=('before0','before7','after0','after7')
    obs={'before0':Q(1),'before7':Q(1),'after0':Q(7,6),'after7':Q(49,41)}
    act={'contact':{'before0':'after0','before7':'after7','after0':'after0','after7':'after7'},
         'idle':{x:x for x in states}}
    refined=future_safe_partition(states,obs,act)
    if refined['rounds']!=1 or refined['minimal_observable_state_count']!=4:
        raise AssertionError('Future-safe quotient failed')
    return {
        'claim_namespace':'BPGS-01..12',
        'source_parent':'PR239@6b50a7828cb9350aa391a5469cde8454b8a0b95c',
        'source_git_blob_sha1':{p:git_blob(p) for p in FILES},
        'rational_exact':True,
        'fixed_port_permutations':perm_count,
        'source_intermediate_jet_equalities':verified_intermediate,
        'logged_reverse_source_events':reverse_count,
        'known_family_contact_inversions':inversions,
        'hidden_g7_no_contact_response':'1',
        'g0_contact_a1':'7/6',
        'g7_contact_a1':'49/41',
        'two_strength_visible_port_r7':str(r),
        'hidden_mixed_third_derivative':str(hidden['mixed_third_derivative_at_zero'][0][0]),
        'finite_observation_refinement_rounds':refined['rounds'],
        'finite_observable_classes':refined['minimal_observable_state_count'],
        'independent_physical_source_authenticated':False,
        'genuine_physical_FUCC_derived':False,
        'Cherenkov_emission_derived':False,
        'Lean_kernel_checked':False,
        'RH_proved':False,
    }


def main():
    v=reproduce()
    if '--check' in sys.argv:
        expected=json.loads(RECEIPT.read_text())
        if expected!=v:
            print('RECEIPT DRIFT:\n'+json.dumps({'expected':expected,'actual':v},indent=2,sort_keys=True))
            raise SystemExit(1)
        print('Exact Git-blob-pinned source and rational replay: PASS')
    print(json.dumps(v,indent=2,sort_keys=True))


if __name__=='__main__':main()
