#!/usr/bin/env python3
"""Exact source-indexed prime genesis crucible. Stdlib-only, no RH claim.

Replays two independent constructions (convolution exponential and prime words),
a third inversion (convolution logarithm), finite braid and Archimedean gates,
plus a deterministic alternative-source holdout matrix.
"""
import argparse
import json
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.prime_jet_genesis import (  # noqa: E402
    JetSource, SourceError, affine_braid_defects, convolution_log,
    counting_measure, direct_word_oracle, expected_prime_power_measure,
    first_archimedean_cell, fucc_path_receipt, rediscover_generators,
)

RECEIPT = ROOT / 'research/2026-10-17/PRIME_JET_GENESIS_RECEIPT.json'


def make_source(values, H):
    return JetSource(tuple((f'g_{j}', q) for j, q in enumerate(values)), F(H))


def compare_all(source):
    measured = counting_measure(source)
    assert measured == direct_word_oracle(source), 'independent words != exp jets'
    assert convolution_log(measured) == expected_prime_power_measure(source), (
        'log inverse != direct local jets')
    assert tuple(sorted(rediscover_generators(measured))) == tuple(sorted(q for q in source.sizes if q<=source.H)), (
        'greedy generator rediscovery != original species')
    return measured


def run():
    P = (2,3,5,7,11,13,17,19,23,29)
    true = make_source(P,30)
    atoms = compare_all(true)
    assert atoms == {F(i): F(1) for i in range(1,31)}
    tested, bad = affine_braid_defects(true,atoms)
    assert tested == 33 and not bad

    mutant=make_source((2,F(3,2),5,7,11,13,17,19,23,29),30)
    alternative=compare_all(mutant)
    n_bad, defects=affine_braid_defects(mutant,alternative)
    assert len(alternative)==59 and all(c==1 for c in alternative.values())
    assert defects and defects[0]['x']=='1' and defects[0]['defect']==-1

    calibrated_mutant=make_source((2,F(9,2),5,7,11,13,17,19,23,29),40)
    calibrated_measure=compare_all(calibrated_mutant)
    n_cal,bad_cal=affine_braid_defects(calibrated_mutant,calibrated_measure)
    assert all(m==1 for m in calibrated_measure.values())
    assert first_archimedean_cell(calibrated_measure)==1 and bad_cal

    squared=make_source(tuple(p*p for p in P),900)
    mass2=compare_all(squared)
    n_scale, bad_scale=affine_braid_defects(squared,mass2)
    assert not bad_scale and first_archimedean_cell(mass2)==3

    fake=make_source(P+(6,),30)
    fake_atoms=compare_all(fake)
    assert fake_atoms[F(6)]==2

    missing=make_source(tuple(p for p in P if p!=5),30)
    missing_atoms=compare_all(missing)
    assert F(5) not in missing_atoms

    invisible=make_source(P+(101,),30)
    assert compare_all(invisible)==atoms
    beyond=compare_all(make_source(P+(101,),101))
    baseline=compare_all(make_source(P,101))
    assert beyond[F(101)]==1 and F(101) not in baseline

    wrong = counting_measure(true,jet_scale=2)
    assert wrong[F(2)]==2 and wrong != atoms

    # Mutant systems with independent source passports: some collide and some
    # do not; all must preserve exact exp/log/direct-generator agreement.
    choices=(F(3,2),F(2),F(5,2),F(3),F(4),F(6))
    matrix=0
    collisions=0
    for generators in combinations_with_replacement(choices,3):
        src=make_source(generators,18)
        a=compare_all(src)
        if any(c>1 for c in a.values()):
            collisions += 1
        matrix += 1

    costs=fucc_path_receipt(true, (0,0,0,1)+(0,)*6,(3,)+(0,)*9)
    assert costs['minimum_fucc_edges']==4 and costs['ratio']=='8/7'

    return {
        'scope':'exact finite rational source chart; no universal completeness claim',
        'construction':'Pi=J/t; mu=exp_*(Pi); Pi=log_*(mu)',
        'genuine_horizon_30':{
            'atoms':len(atoms),'unit_atom_masses':True,
            'interior_braid_rectangles':tested,'defects':0,
            'first_arch_cell_mass':str(first_archimedean_cell(atoms)),
            'rediscovered_primitive_sizes':[str(x) for x in rediscover_generators(atoms)],
        },
        'collision_free_countermodel':{
            'replaced_generator':'3 -> 3/2',
            'atoms':len(alternative),'all_atom_masses_one':True,
            'interior_rectangles':n_bad,'braid_defects':len(defects),
            'first_braid_failure':defects[0],
            'first_arch_cell_mass':str(first_archimedean_cell(alternative)),
        },
        'calibration_only_countermodel':{
            'replaced_generator':'3 -> 9/2',
            'unique_atoms':True,
            'first_arch_cell_mass':str(first_archimedean_cell(calibrated_measure)),
            'interior_rectangles':n_cal,
            'braid_defects':len(bad_cal),
            'first_braid_failure':bad_cal[0],
        },
        'scale_countermodel':{
            'generator_scale':'q_j -> q_j^2',
            'atoms':len(mass2),'interior_rectangles':n_scale,
            'braid_defects':len(bad_scale),
            'first_arch_cell_mass':str(first_archimedean_cell(mass2)),
        },
        'fake_six':{'composite_atom_mass':str(fake_atoms[F(6)]),
                    'source_detects_ghost':True},
        'missing_five':{'atoms':len(missing_atoms),'observed_five':False},
        'unseen_future_source':{'horizon_30_indistinguishable':True,
                                'horizon_101_discriminator':True},
        'mutated_jet_scale_2':{'at_two_mass':str(wrong[F(2)]),'rejected':True},
        'systematic_holdout':{'generator_triples':matrix,
                              'systems_with_mass_collisions':collisions,
                              'exp_log_direct_replay':True},
        'endpoint_example':costs,
        'global_braid_proved_by_enumeration':False,
        'source_law_forcing_braid_discovered':False,
        'signed_completed_Weil_positivity_proved':False,
        'RH_proved':False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true',
                        help='compare exact replay to checked-in finite receipt')
    parser.add_argument('--write-receipt',action='store_true',
                        help='write deterministic checked-in research receipt')
    args=parser.parse_args()
    outcome=run()
    encoded=json.dumps(outcome,indent=2,sort_keys=True)+'\n'
    if args.write_receipt:
        RECEIPT.parent.mkdir(parents=True,exist_ok=True)
        RECEIPT.write_text(encoded,encoding='utf-8')
    if args.verify:
        if not RECEIPT.exists() or RECEIPT.read_text(encoding='utf-8') != encoded:
            raise SystemExit('source receipt absent/stale: FAIL CLOSED')
    print(encoded,end='')
    print('SOURCE_FINITE_RECEIPT_VERIFIED' if args.verify else 'SOURCE_FINITE_PROBE_COMPLETE',
          file=sys.stderr)

if __name__=='__main__':
    main()
