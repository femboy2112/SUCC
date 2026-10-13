#!/usr/bin/env python3
"""Exact classical Lorentz, causal E receipts and proof descent diagnostics."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.covariant_observer_frames import (
    physical_frame_demo,epistemic_flux_demo,LorentzFrame)
from observational_succ.covariant_proof_descent import (
    covariant_proof_demo,bit_shears,OriginalSourceSquare)
from observational_succ.asynchronous_e_tower import asynchronous_e_demo
from fractions import Fraction as F


def probe():
    physical=physical_frame_demo()
    semantic=covariant_proof_demo()
    relay=asynchronous_e_demo()
    boost=LorentzFrame.boost('x',F(1,3)).then(LorentzFrame.boost('y',F(1,3)))
    pure,rotation=boost.decompose_boost_then_rotation()
    shear=bit_shears()
    destructive=OriginalSourceSquare('original-pair',(0,0),(0,1),(0,0),(0,1),((0,0),(1,0)))
    rep={
        'scope':'classical 2+1 Lorentz, finite source-category and causal receipts',
        'proof_assistant_formalization':False,
        'physical_cognitive_lorentz_hypothesis_proved':False,
        'source_authentication':False,
        'all_theorems_mathematically_global':False,
        'lorentz':physical,
        'wigner_rotation':[[str(a) for a in row] for row in rotation.matrix],
        'wigner_rotation_nontrivial':rotation!=LorentzFrame.identity(),
        'net_boost':[[str(a) for a in row] for row in pure.matrix],
        'epistemic_flux':epistemic_flux_demo(),
        'proof_transport':semantic,
        'destructive_observation_square_commutes':destructive.observation_square()['commutes'],
        'destructive_original_claim_preserved':destructive.original_claim_square()['preserved'],
        'destructive_original_claim_decodable':destructive.decoder()['factors'],
        'asynchronous_tower':relay,
    }
    assert rep['lorentz']['mismatch_only_spacelike'] is True
    assert rep['wigner_rotation'][1][1]=='40/41'
    assert rep['wigner_rotation'][1][2]=='-9/41'
    assert rep['wigner_rotation'][2][1]=='9/41'
    assert rep['asynchronous_tower']['late_status']=='PROVED'
    assert rep['destructive_original_claim_decodable'] is False
    return rep

if __name__=='__main__':
    print(json.dumps(probe(),indent=2,sort_keys=True))
