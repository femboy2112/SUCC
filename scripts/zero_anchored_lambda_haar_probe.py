#!/usr/bin/env python3
"""Replay the fixed zero-source compiler and signed-defect finite protocol.

Default output is JSON on stdout. --output writes the complete exact receipt
and prints a compact human-readable finite table. Decimal table values are
display only; every verdict uses rational interval endpoints.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess

from observational_succ.zero_anchored_lambda import (
    SOURCE_DIGEST, CompilerError, certify_state, compile_state, compile_term,
    complete_state, guarded_tail_term, run, verify_completion_certificate,
    verify_source_certificate,
)
from observational_succ.zero_anchored_haar import (
    certified_haar_defect, certified_pascal_characters, certified_phase_grid,
    contraction_error_floor, contraction_residual, finite_verdict,
    grid_haar_defect, orbit_defect_floor, pascal_haar_upper, signed_block_overlap,
    verify_phase_grid,
)
from observational_succ.recursive_haar_pinbed import (
    canonical_law, digit_averaging_law, interval_w1,
    periodic_orbit_law,
)


ROOT = Path(__file__).resolve().parents[1]
BASE = '50481e49592af00d87c602f671a28f3503709de0'
LENGTHS = (64,128,256,512,1024,2048,4096)
THETAS = (F(1,16),F(1,2),F(3,4))


def exact_json(value):
    if isinstance(value,F):
        return str(value)
    raise TypeError(type(value).__name__)


def digest(path):
    return sha256((ROOT/path).read_bytes()).hexdigest()


def compiler_receipt():
    rows = []
    for seed in (F(),F(1,16),F(2,7)):
        for clock in (0,1,2,4,8):
            program = compile_state(clock,seed)
            normal = run(program,strategy='normal')
            applicative = run(program,strategy='applicative')
            assert normal.status == applicative.status == 'FINITE_REDUCTION_VERIFIED'
            assert normal.value == applicative.value
            cert = certify_state(normal.value,require_zero=False)
            assert verify_source_certificate(cert)
            completion = complete_state(normal.value,clock+12)
            assert verify_completion_certificate(completion)
            try:
                certify_state(normal.value)
                accepted_zero = True
            except CompilerError:
                accepted_zero = False
            assert accepted_zero == (seed == 0)
            rows.append({'clock':clock,'seed':seed,'state':asdict(normal.value),
                         'source_certificate':asdict(cert),
                         'completed_interval':[completion.lower,completion.upper],
                         'original_zero_accepted':accepted_zero,
                         'beta_steps':normal.beta_steps,'delta_steps':normal.delta_steps,
                         'evaluation_strategies_agree':True})
    tail_program = compile_term(guarded_tail_term(8,12))
    tail_normal, tail_applicative = run(tail_program), run(tail_program,strategy='applicative')
    assert tail_normal.value == tail_applicative.value
    state = run(compile_state(8)).value
    assert complete_state(state,20).finite_tail == tail_normal.value
    exhausted = run(compile_state(8),max_steps=1)
    assert exhausted.status == 'UNRESOLVED_BUDGET'
    return {'finite_state_cases':len(rows),'rows':rows,
            'guarded_tail':{'clock':8,'depth':12,'value':tail_normal.value,
                            'beta_steps':tail_normal.beta_steps,'delta_steps':tail_normal.delta_steps},
            'budget_control_status':exhausted.status}


def run_probe(lengths, depth, guard):
    maximum = max(lengths)
    phases = certified_phase_grid(0,2*maximum+1,depth=depth,guard=guard)
    assert verify_phase_grid(phases)
    rows = []
    for m in lengths:
        early = certified_haar_defect(phases,0,m)
        late = certified_haar_defect(phases,m,m)
        combined = certified_haar_defect(phases,0,2*m)
        overlap = signed_block_overlap(phases.points[:m],phases.points[m:2*m],phases.denominator)
        assert (early.approximation,late.approximation,combined.approximation) == (
            overlap.early,overlap.late,overlap.combined)
        assert combined.lower >= orbit_defect_floor(2*m)
        residuals = {str(t):contraction_residual(combined,early,t) for t in THETAS}
        strong = contraction_residual(combined,early,F(1,16),F(1,15*m))
        rows.append({'M':m,'cohort':'calibration' if m<=256 else 'holdout_for_this_instrument',
                     'D_M':asdict(early),'D_late':asdict(late),'D_2M':asdict(combined),
                     'grid_signed_overlap':asdict(overlap),
                     'true_overlap_interval':[max(F(),overlap.overlap-4*phases.point_error),
                                              overlap.overlap+4*phases.point_error],
                     'residuals_without_assumed_error':residuals,
                     'strong_extrapolation_residual':strong,
                     'strong_extrapolation_verdict':finite_verdict(strong)})
    pascal_source = certified_phase_grid(0,258,depth=depth,guard=guard)
    pascal = []
    for m in (0,1,4):
        chars = certified_pascal_characters(pascal_source,m)
        pascal.append({'degree':m,'N':257,'characters':[asdict(c) for c in chars],
                       'haar_upper':pascal_haar_upper(pascal_source,m) if m else None})
    periodic = periodic_orbit_law(tuple(range(16)))
    control = {
        'constant_zero_defect':grid_haar_defect((0,)*64,16),
        'constant_zero_overlap':signed_block_overlap((0,)*32,(0,)*32,16).overlap,
        'uniform_grid_defect':grid_haar_defect(tuple(range(16)),16),
        'periodic_balanced_digit_defect':interval_w1(periodic,digit_averaging_law(periodic)),
        'four_pole_telescoping_limit_defect':interval_w1(
            canonical_law((F(2,3),)),digit_averaging_law(canonical_law((F(2,3),)))),
        'universal_necessary_error_coefficient_at_theta_1_16':contraction_error_floor(F(1,16)),
        'strong_extrapolation_error_coefficient':F(2,15),
    }
    assert control['constant_zero_defect'] == F(15,32)
    assert control['constant_zero_overlap'] == control['uniform_grid_defect'] == 0
    assert control['four_pole_telescoping_limit_defect'] == F(35,128)
    paths = [
        'observational_succ/zero_anchored_lambda.py',
        'observational_succ/zero_anchored_haar.py',
        'observational_succ/duck_bbp.py',
        'observational_succ/c_monoid_succ_embedding.py',
        'observational_succ/recursive_haar_pinbed.py',
        'scripts/zero_anchored_lambda_haar_probe.py',
        'research/2026-11-10/zero_anchored_lambda_haar/HOLE_CONTRACT.md',
    ]
    return {
        'status':'FINITE_SOURCE_COMPILER_AND_HAAR_CERTIFICATES_VERIFIED',
        'base_commit':BASE,
        'local_head_at_run':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'source_digest':SOURCE_DIGEST,'python':platform.python_version(),
        'code_sha256':{p:digest(p) for p in paths},
        'protocol':{'lengths':lengths,'phase_depth':depth,'guard':guard,
                    'thetas':THETAS,'phase_origin':'alpha=pi/16; clock0 digit is 3',
                    'previously_unseen_pi_data_claimed':False},
        'source_certificate':{
            'start':phases.start,'count':phases.count,'depth':depth,'guard':guard,
            'horizon':phases.horizon,'integer_lower_hex':format(phases.integer_lower,'x'),
            'integer_upper_hex':format(phases.integer_upper,'x'),
            'phase_grid_denominator':phases.denominator,'points':phases.points,
            'per_point_error':phases.point_error,'defect_error':2*phases.point_error},
        'compiler':compiler_receipt(),'blocks':rows,'pascal_levels':pascal,'controls':control,
        'statistical_contraction_proved':False,'pi_normality_proved':False,
        'rh_proved':False,'infinite_quantifiers_tested':False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--lengths',type=int,nargs='+',default=LENGTHS)
    parser.add_argument('--phase-depth',type=int,default=10)
    parser.add_argument('--guard',type=int,default=16)
    args = parser.parse_args()
    if any(n<1 for n in args.lengths):
        parser.error('positive block lengths required')
    report = run_probe(tuple(args.lengths),args.phase_depth,args.guard)
    payload = json.dumps(report,default=exact_json,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload)
        print('M D_M D_late D_2M overlap strong_extrapolation')
        for row in report['blocks']:
            o = row['grid_signed_overlap']
            print(row['M'], *(f'{float(o[key]):.10f}' for key in ('early','late','combined','overlap')),
                  row['strong_extrapolation_verdict'])
        print('Exact receipt:',args.output)
        print('Pi normality OPEN; sample-length contraction OPEN.')
    else:
        print(payload,end='')


if __name__ == '__main__':
    main()
