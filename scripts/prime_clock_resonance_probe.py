#!/usr/bin/env python3
"""Reproducible exact source receipts; no empirical extrapolation or pi input."""
import argparse
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.prime_clock_resonance import (
    source_passport, projection_certificate, forced_coherence_gap,
    uniform_coherence_gap_floor, project_period, pairing,
)
from observational_succ.succ_internal_matrix_walk import PhasePoly
from observational_succ.cyclotomic_selected_source import character_mean
from observational_succ.bbp_resonance_controls import (
    same_forcing_odd_control, inverse_arc_membership,
)
from observational_succ.bbp_resonance_collision import (
    conductor_supported_counterfeit, collision_ladder_budget,
)
from observational_succ.bbp_resonant_lags import prime_filter_passport

DEST = ROOT/'research/2026-10-25/PRIME_RESONANCE_RECEIPT.json'
SOURCES = (
    'observational_succ/prime_clock_resonance.py',
    'observational_succ/bbp_resonance_controls.py',
    'observational_succ/bbp_resonance_collision.py',
    'observational_succ/bbp_resonant_lags.py',
    'observational_succ/bbp_source_memory.py',
    'observational_succ/bbp_cyclotomic_birth.py',
    'observational_succ/succ_internal_matrix_walk.py',
    'observational_succ/pi_source_genesis.py',
    'formal/PrimeClockProjection.lean',
)


def digest(values):
    return sha256('\n'.join(str(v) for v in values).encode()).hexdigest()


def rational_json(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


def run():
    rows=[]
    for p in (17,41,73,97,113,193,257,337):
        x=source_passport(p)
        control=same_forcing_odd_control(p)
        counterfeit=conductor_supported_counterfeit(p)
        row={'p':p,'m':x.m,'n0':x.n0,'delta':x.delta,'L':x.order,
             'good_order':x.order**3>p,'h':x.h,'source':x.source,
             'passport_verified':x.validate(),
             'unwrapped_prefix_sha256':digest(x.prefix),
             'complement_sha256':digest(x.complement),
             'forcing_modulus_gap_lower':forced_coherence_gap(p),
             'changed_initial_control':{
                 'source_authentication_failures':control['authentic_failures'],
                 'initial_sha256':digest([control['initial']]),
                 'denominator_bits':control['denominator'].bit_length(),
                 'modulus_deficit_upper':control['modulus_deficit_upper'],
                 'authentic_source':False},
             'allowed_conductor_counterfeit':{
                 'minimum_grid_denominator_bits':counterfeit.minimum_denominator.bit_length(),
                 'sum_distance_from_one_upper':counterfeit.normalized_sum_distance_from_one_upper(),
                 'all_in_first_16_cell':all(0<s<Q(1,16) for s in counterfeit.selected),
                 'authentic_source':False}}
        if x.m>=11:
            floor=uniform_coherence_gap_floor(p)
            assert row['forcing_modulus_gap_lower']>=floor
            row['explicit_modulus_gap_floor']=floor
        if p in (41,73,97,193):
            a=Q(1,100)
            actual=inverse_arc_membership(p,x.states[0],a)
            tuned=inverse_arc_membership(p,control['states'][0],a)
            assert control['modulus_deficit_upper']<tuned['deficit_threshold']
            assert not actual['inside'] and tuned['inside']
            row['inverse_seed_arcs']={'angular_radius':a,
                                     'authentic':actual,'changed_initial':tuned,
                                     'all_prime_avoidance_proved':False}
        if p<=113:
            box=character_mean(s % 1 for s in x.states).outward(48)
            row['authentic_normalized_sum_box']=asdict(box)
            row['authentic_modulus_squared_upper']=box.modulus_squared_upper()
        if p in (17,41,113):
            periods=(1,3) if p in (17,113) else (1,5)
            certs=[]
            for d in periods:
                c=projection_certificate(x,d)
                certs.append({'d':d,'retained_period':c['period'],
                              'low_period_gcd':c['low_period'],
                              'coset_period':c['coset_period'],
                              'repeated_copies':c['repeats'],
                              'signed_recomposition_exact':c['full']==c['low']+c['interaction'],
                              'energy_sum_exact':sum(c['energies'],PhasePoly.zero())==PhasePoly.one(),
                              'formal_full_sha256':digest(c['full'].terms),
                              'formal_J_sha256':digest(c['interaction'].terms)})
            row['projection_certificates']=certs
        rows.append(row)
    # Deterministic finite grid control, NOT an independently sampled source.
    # Sum e(0)+e(1/4)+e(1/2)+e(3/4)=0 only in complex evaluation,
    # not in the free group algebra. A certified interval is the authority.
    haar_grid=character_mean([Q(j,4) for j in range(4)]).outward(48)
    assert haar_grid.real_low<=0<=haar_grid.real_high
    assert haar_grid.imag_low<=0<=haar_grid.imag_high
    assert haar_grid.modulus_squared_upper()<Q(1,10**20)
    # Exact high-period anti-phase survives canonical compression.
    x=source_passport(41)
    u=tuple(PhasePoly.monomial(a) for a in x.primary)
    anti=tuple(v.star() for v in u)
    assert pairing(u,project_period(anti,x.order))==PhasePoly.one()
    old=prime_filter_passport(17,4,(2,))
    fresh=prime_filter_passport(41,4,(2,))
    assert old['residue']==0 and fresh['residue']==4
    ladder=collision_ladder_budget(256,1,1,1)
    assert ladder.squared_upper==Q(18869,50176)
    return {'schema':'SUCC.prime-resonance.v1',
            'baseline_commit':'461942c0bf616518e668d236d1c6b1596665a7dd',
            'authority':'exact rational identities and certified finite intervals; paper asymptotics separate',
            'pi_normality_proved':False,
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in SOURCES},
            'prime_windows':rows,'synthetic_grid_box':asdict(haar_grid),
            'resonant_lag_receipt':{'start':4,'lag':2,'killed_prime':17,'fresh_prime':41,
                                   'old_residue':0,'fresh_residue':4,
                                   'circle_phase':fresh['filtered_phase']},
            'finite_collision_certificate':{**asdict(ladder),'squared_upper':ladder.squared_upper}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--write',action='store_true')
    group.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    data=json.dumps(run(),default=rational_json,sort_keys=True,indent=2)+'\n'
    if args.write:
        DEST.write_text(data)
        print('WROTE',DEST.relative_to(ROOT))
    elif args.verify:
        if not DEST.exists() or DEST.read_text()!=data:
            raise SystemExit('receipt differs from source replay')
        print('VERIFIED',DEST.relative_to(ROOT),sha256(data.encode()).hexdigest())
    else:
        print(data,end='')


if __name__=='__main__':
    main()
