#!/usr/bin/env python3
"""Reproducible exact-arithmetic balanced-prime-clock finite receipt.

Run from SUCC repository root. No web, π digits, outside packages or raw-file
mutation. Float phase diagnostics are explicitly non-certifying.
"""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from observational_succ.balanced_prime_clock import (
    epoch_stage_lengths, epoch_stage_weights, prime_candidates,
    epoch_histogram_from_stage, epoch_histogram_from_residues,
    direct_source_epoch_residues, epoch_phase_gram, target_gram,
    dyadic_terminal_shadow, dyadic_shadow_phase_bound,
    unbalanced_pr4A_channels_locked,
)
from observational_succ.three_channel_prime_tomography import (
    is_prime, predicted_residues, multiplicative_order_16,
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def finite_row(A):
    options=prime_candidates(A)
    if not options:
        raise AssertionError(f'no tested finite balanced clock at A={A}')
    p,m=options[0]
    lengths=epoch_stage_lengths(A,p)
    assert sum(lengths)==A
    for mode in ((1,1,1),(0,1,-1),(1,-2,0),(2,-1,3)):
        assert epoch_histogram_from_stage(A,p,1,mode)==epoch_histogram_from_residues(A,p,1,mode)
    direct=direct_source_epoch_residues(A,p)
    assert direct==[predicted_residues(p,n) for n in range(A,2*A)]
    gram=epoch_phase_gram(A,p)
    tgt=target_gram(A,p)
    max_abs_dev=max(abs(gram[i][j]-float(tgt[i][j])) for i in range(3) for j in range(3))
    return {
      'A':A, 'p':p,'order_of_16':m,'stage_lengths':list(lengths),
      'weights':[str(w) for w in epoch_stage_weights(A,p)],
      'balanced_ratio_error':str(abs(F(p,A)-F(12,5))),
      'direct_modular_recurrence':'PASS',
      'four_modes_complete_histograms':'PASS',
      'gram_error_numeric_not_certificate':max_abs_dev,
      'target_gram_45':str(tgt[1][2]),
    }


def shadow_row(A):
    p=prime_candidates(A)[0][0]
    seed, alpha_N,N,M=dyadic_terminal_shadow(A)
    assert seed.denominator%p !=0
    assert F(0)<=seed+alpha_N<=F(1,1<<M)
    bound=dyadic_shadow_phase_bound(A)
    return {'A':A,'p':p,'truncation_N':N,'dyadic_bits':M,
            'seed_sha256':hashlib.sha256(str(seed).encode()).hexdigest(),
            'phase_abs_upper_rational':str(bound),
            'phase_abs_upper_numeric_diagnostic':float(bound),
            'p_unit_seed':'PASS'}


def old_clock_row(A):
    p=next(v for v in range(4*A+7,3*A,-1) if v%8==1 and is_prime(v))
    assert unbalanced_pr4A_channels_locked(A,p)
    assert all(predicted_residues(p,n)[1]==predicted_residues(p,n)[2]
               for n in range(A,2*A))
    return {'A':A,'p':p,'C4_equals_C5_every_original_epoch_time':'PASS',
            'exact_null_direction':'(0,1,-1)'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=str,default=None)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[3]
    sourcefiles=[root/'observational_succ/three_channel_prime_tomography.py',
                 root/'observational_succ/balanced_prime_clock.py',
                 root/'tests/test_three_channel_prime_tomography.py',
                 root/'tests/test_balanced_prime_clock.py']
    rec={
      'status':'FINITE_EXACT_PROBES_ONLY',
      'pi_normality':'OPEN',
      'input_sha256':{str(p.relative_to(root)):sha(p) for p in sourcefiles},
      'balanced':[finite_row(A) for A in (100,128,256,512,1024)],
      'old_4A_null':[old_clock_row(A) for A in (100,256,512)],
      'exact_dyadic_hostile_shadow':[shadow_row(A) for A in (100,128,256)],
      'limitations':['Cochrane-Pinner and PNT/AP are classical proof imports, not finite tests',
                     'numeric phase Gram is not an interval certificate',
                     'original-zero real signed covariance decay is unproved'],
    }
    encoded=json.dumps(rec,indent=2,sort_keys=True)+'\n'
    if args.output:
        Path(args.output).write_text(encoded)
    else:
        print(encoded,end='')

if __name__=='__main__':main()
