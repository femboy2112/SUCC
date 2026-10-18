#!/usr/bin/env python3
"""Reproducible source-aware exact rational SUCC bidirectional cut probe.

No nontrivial zeros, RH conclusion, or nonzero unperformed source measurement.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from observational_succ.bidirectional_cut import (
    bernoulli_clock_covariance, square_root_tail_energy,
    clock_period_integral,clock_tail_optimum,certified_cut_residual,
    SourcePassport)
from observational_succ.bidirectional_hilbert import (
    orthogonal_innovations,hidden_target_counterexample)


def serialize(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serialize(v) for v in x]
    return x


def outward(x, side, decimals=12):
    grid=10**decimals
    q=x*grid
    if side=='lower':return F(q.numerator//q.denominator, grid)
    if side=='upper':return F(-((-q.numerator)//q.denominator), grid)
    raise ValueError('side required')


def build():
    independent_cases=[]
    for N in range(1,9):
        solution=clock_tail_optimum(N)
        if N<=7:
            direct=clock_period_integral(solution['coefficients'])
            assert direct['mean_square']==solution['minimum']
        independent_cases.append({
            'N':N,
            'mean_square_minimum':str(solution['minimum']),
            'S_N':str(solution['S']),
            'b_cut_obstruction':str((6*solution['minimum'])**2),
            'full_minimum_not_implied':True,
        })
    nontrivial=clock_tail_optimum(1)
    witness=certified_cut_residual(nontrivial['coefficients'],R=28,terms=14)
    assert witness['lower']>1 and nontrivial['minimum']==F(1,4)
    assert certified_cut_residual((F(0),),R=28,terms=14)['upper']==1
    sample=certified_cut_residual((F(1),F(-1),F(1)),R=48,terms=14)
    witness3=hidden_target_counterexample()
    assert witness3['surviving']==1
    src=SourcePassport('declared-positive-clocks',0,tuple(range(1,9)))
    assert src.require_prefix(8)
    return serialize({
        'domain':'exact rational clock source + classical Hilbert assertions',
        'new_math':'Jordan J2 square root of periodic backward modular clock tail',
        'Basel_in_source_mean':'1/12 = (1/(2*pi^2))*zeta(2); independent carry proof also exists',
        'pair_correlation_2_3':bernoulli_clock_covariance(2,3),
        'tail_optimal_1_to_8':independent_cases,
        'tail_only_counterexample':{
            'N':1,'coefficient':nontrivial['coefficients'][0],
            'periodic_optimum':nontrivial['minimum'],
            'true_L2_residual_lower':outward(witness['lower'],'lower'),
            'true_L2_residual_upper':outward(witness['upper'],'upper'),
            'zero_coefficient_true_L2_upper':F(1),
            'verdict':'refutes tail optimum => full Hilbert optimum',
        },
        'mixed_signed_trial_1_minus_1_plus_1':{
            'periodic_Haar_energy':sample['tail_Haar_alpha'],
            'full_L2_lower':outward(sample['lower'],'lower'),
            'full_L2_upper':outward(sample['upper'],'upper'),
            'L2_tail_upper':sample['tail_upper'],
        },
        'finite_orthogonal_ghost':{
            'target_norm_sq':witness3['norm_sq'],
            'all_forward_readings_zero':not any(witness3['innovation_energies']),
            'surviving_residual_sq':witness3['surviving'],
        },
        'source_passport':'mathematical declaration, not external attestation',
        'unverified':'uniform global L2 Nyman--Beurling residual convergence',
        'RH_proved':False,
    })


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    result=build()
    path=Path(__file__).resolve().parents[1]/'research/2026-10-18/BIDIRECTIONAL_CUT_RECEIPT.json'
    if args.verify:
        expected=json.loads(path.read_text(encoding='utf-8'))
        if expected!=result:
            raise SystemExit('SOURCE_RECEIPT_MISMATCH: recomputed exact data differ from frozen receipt')
        print('BIDIRECTIONAL_CUT_RECEIPT_VERIFIED; RH_proved:false')
    else:
        print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
