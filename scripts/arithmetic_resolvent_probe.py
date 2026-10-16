#!/usr/bin/env python3
"""Bounded serial source replay and deterministic principal integration packet."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import platform
import resource
import shlex
import subprocess
import sys
from time import monotonic
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ import arithmetic_resolvent as A
from observational_succ import one_object_relative_residual as R
from observational_succ.four_low_schur_proof_teeth import source_snapshot, certified_scalar_improvement

OWN=('observational_succ/arithmetic_resolvent.py','tests/test_arithmetic_resolvent.py',
     'scripts/arithmetic_resolvent_probe.py','research/2026-10-16/AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md')
DOSSIERS=('research/2026-10-16/COMPACT_SOURCE_GALERKIN.md',
          'research/2026-10-16/OBSERVER_SCHUR_SOURCE.md',
          'research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md',
          'reviews/2026-10-16_OBSERVER_SCHUR_HOSTILE_AUDIT.md')

def hashes(paths):
    return {p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}

def write(path,obj):
    path.write_text(json.dumps(A.serial(obj),sort_keys=True,indent=2)+'\n')

def git(*args):
    p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,text=True,check=True)
    return p.stdout.strip()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--lower-grid',type=int,choices=(512,1024),default=512)
    args=p.parse_args()
    output=args.output.resolve()
    output.parent.mkdir(parents=True,exist_ok=True)
    start=monotonic(); source=source_snapshot(); own=hashes(OWN)
    A.verify_runtime_source()
    print('Replaying inherited source coercivity and full derivative bound',flush=True)
    inherited=certified_scalar_improvement()
    # EVERY response is saved before any final certificate intervals are requested.
    candidates=[A.freeze_candidate(n,64) for n in (12,16,20)]
    candidates.append(A.freeze_candidate(16,64,F(1,100)))
    candidate_path=output.with_name(output.stem+'-candidates.json')
    write(candidate_path,candidates)
    candidate_bytes=sha256(candidate_path.read_bytes()).hexdigest()
    print('Candidates frozen; certifying full-source upper forms',flush=True)
    uppers=[A.certify_upper(c,512) for c in candidates]
    shifted=[A.shifted_certificate(candidates[-1],shift,512,20)
             for shift in (F(1,100),F(1,1000))]
    for result in shifted:
        result['response_error_operator_caps']=A.sector_caps(result['response_error_upper'])
    print('Certifying U=0 derivative lower bound, grid',args.lower_grid,flush=True)
    lower=A.certified_zero_trial_lower(20,args.lower_grid)
    print('Preserving finite-family obstruction attempts',flush=True)
    failed=[A.finite_family_obstruction(n,20,512) for n in (12,16)]
    # Full source A >= truncated A >= its exact interval lower majorant.
    lowentries=tuple(tuple(A.truncated_entry(i,j,512) for j in range(1,5)) for i in range(1,5))
    alower,_,_=A.interval_majorants(lowentries)
    cs={p:s['R0_operator_upper_cap'] for p,s in lower['sectors'].items()}
    correction=tuple(tuple(cs['odd' if i%2==0 else 'even']/F(2*i+3) if i==j else F()
                           for j in range(4)) for i in range(4))
    slo=R.add(alower,correction,-1); best=uppers[2]
    oldcaps={'odd':F(1939731,4294967296),'even':F(3654297,2147483648)}
    improvements={name:{'old_upper_cap':oldcaps[name],
                        'new_upper_cap':best['parity_caps'][name]['operator_upper_cap'],
                        'strictly_improved':best['parity_caps'][name]['operator_upper_cap']<oldcaps[name],
                        'new_R0_cap':cs[name],
                        'old_R0_cap':F(75625,20699),
                        'lower_correction_strictly_improved':cs[name]<F(75625,20699)}
                  for name in oldcaps}
    packet={'schema':'AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE_V1',
            'sourceidentity':{'git_blob':source['source_git_blob'],
                              'source_commit':'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc',
                              'source_sha256':source['sha256'],
                              'runtime_verified_against_pinned_code':True,
                              'channels':['both signed poles','contact','true prime-2 half density','one real Gamma tower'],
                              'zero_coordinates_used':False},
            'radius':F(1,2),'Wmetric':A.metric((1,2,3,4)),
            'basis':'unnormalized P1(2t), P2(2t), P3(2t), P4(2t)',
            'exactlower':slo,'exactupper':best['S0_upper_form'],
            'certified_order':'exactlower <= S0 <= exactupper in W form coordinates',
            'upper_degree':20,'candidate':candidates[2],
            'two_sector_operator_upper_caps':best['parity_caps'],
            'lower_response_caps':lower['sectors'],'A_lower_form':alower,
            'source_bounds':{'kappa':inherited['kappa'],'gprime_L1_strict_upper':F(11,40)},
            'separatederrorbudgets':{
                'upper_finite_Gamma_entry_intervals':best['truncated_H_intervals'],
                'upper_interval_radius_by_parity':best['entry_radii_by_sector'],
                'upper_whole_Gamma_operator_tail':best['whole_Gamma_tail_norm_upper'],
                'upper_whole_Gamma_form_tail':R.scale(best['whole_Gamma_tail_norm_upper'],best['V_Gram']),
                'upper_spatial_integration_error':F(),
                'upper_matrix_solve_error':'exact midpoint solves; rounded candidate frozen and fully reevaluated',
                'lower_BV_Lipschitz':lower['BV_Lipschitz'],
                'lower_cell_errors':[{'mode':c['mode'],
                    'linear':c['between_cell_linear_error'],'quadratic':c['between_cell_quadratic_error']}
                    for c in lower['columns']],
                'lower_finite_Gamma_column_energies':[
                    {'mode':c['mode'],'midpoint_energy':c['midpoint_absolute_energy_upper'],
                     'whole_cell_energy_upper':c['finite_J_whole_interval_energy_upper']}
                    for c in lower['columns']],
                'lower_whole_Gamma_derivative_operator_tail':lower['sectors']['odd']['whole_Gamma_derivative_operator_tail'],
                'positive_shift_residual_certificates':shifted},
            'incompletegap':{'zero_shift_sign':'OPEN',
                'shift_to_zero_regularization_gap':'NO VANISHING RATE ESTABLISHED',
                'coarse_regularization_gap_order':'0 <= S_lambda-S0 <= R0 <= direct_sum(c_odd I_odd,c_even I_even)',
                'coarse_regularization_gap_sector_caps':cs,
                'lower_bound_trial':'U=0; entire derivative tail closed for this conservative bound',
                'higher_degree_response_relative_residual':'NOT CERTIFIED',
                'actual_adjoint_range_or_fractional_identification':'OUTSIDE_THIS_LANE'},
            'analyticdebt':['inherited whole-high coercivity and square-root range paper theorems',
                'source identification of PR85 completed Suzuki kernel',
                'paper Legendre/BV/Young/Douglas arguments; no Lean proof in this lane',
                'new positive lower sign or negative upper direction not established'],
            'status':'CONDITIONAL_PAPER_THEOREMS_WITH_EXACT_AUTHENTIC_SOURCE_INTERVAL_EXECUTION',
            'proof_authority':'not a formal kernel proof','RH_PROVED':False,
            'improvements':improvements,'producer_sha256':own,'dossier_sha256':hashes(DOSSIERS)}
    print('Running focused hostile and algebraic controls',flush=True)
    stream=io.StringIO(); tests=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_arithmetic_resolvent.py')
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(tests)
    packet_path=output.with_name(output.stem+'-packet.json')
    stable=source==source_snapshot() and own==hashes(OWN)
    A.verify_runtime_source()
    success=result.wasSuccessful() and stable and all(v['strictly_improved'] and v['lower_correction_strictly_improved'] for v in improvements.values())
    packet['execution_checks_passed']=success
    write(packet_path,packet)
    receipt={'command':shlex.join([sys.executable,*sys.argv]),'utc':datetime.now(timezone.utc).isoformat(),
        'schema':'ARITHMETIC_RESOLVENT_EXECUTION_V1',
        'status':'PASS' if success else 'FAIL', 'source_git_blob':source['source_git_blob'],
        'evidence':{'deterministic_packet':packet_path.name,'frozen_candidates':candidate_path.name,
                    'proof_authority':'conditional paper proof plus exact interval execution'},
        'python':platform.python_version(),'cwd':str(ROOT),'git_head':git('rev-parse','HEAD'),
        'git_branch':git('branch','--show-current'),'source_before':source,'source_after':source_snapshot(),
        'own_sha256_before':own,'own_sha256_after':hashes(OWN),'stable_bytes':stable,
        'candidate_file':candidate_path.name,'candidate_file_sha256':candidate_bytes,
        'packet_file':packet_path.name,'packet_sha256':sha256(packet_path.read_bytes()).hexdigest(),
        'inherited_source_bound_replay':inherited,'upper_certificates':uppers,
        'positive_shift_certificates':shifted,'zero_trial_lower':lower,
        'finite_family_no_go_attempts':failed,
        'regularization_controls':[A.regularization_counterexample(n) for n in (10,100,1000)],
        'tests':{'run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
                 'skipped':len(result.skipped),'successful':result.wasSuccessful(),'output':stream.getvalue()},
        'elapsed_seconds':monotonic()-start,'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'environment':{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','PYTHONDONTWRITEBYTECODE')},
        'full_suite_run':False,'git_mutations_performed':False,'success':success,'RH_PROVED':False}
    write(output,receipt)
    print(stream.getvalue(),end='')
    print('Source bracket:',A.serial(improvements))
    print('Packet:',packet_path,'sha256',receipt['packet_sha256'])
    print('PASS' if success else 'FAIL','elapsed',receipt['elapsed_seconds'],'RSS KiB',receipt['peak_RSS_KiB'])
    return int(not success)

if __name__=='__main__':
    raise SystemExit(main())
