"""Replay the four prospectively fixed cases; no floating-point certificates."""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

ts=load('covforge_terminal_receipt',HERE/'terminal_support.py')
oracle=load('covforge_terminal_oracle_receipt',HERE/'independent_oracle.py')

def exact_hex(x):
    return f'{x.numerator:x}/{x.denominator:x}'

def digest_rows(rows):
    return hashlib.sha256(('\n'.join(exact_hex(x) for x in rows)+'\n').encode()).hexdigest()

def rational_lower(x,denominator=10**12):
    result=Q((x*denominator)//1,denominator)
    assert result<=x<result+Q(1,denominator)
    return str(result)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'RECEIPTS.json',
                        help='output JSON path; defaults to the retained local receipt')
    args=parser.parse_args(argv)
    rows=[]
    for J,A in ((5,37),(11,73),(17,137),(23,257)):
        p=ts.selected_prime(A)
        w=ts.construct(J,A,A,2*A-1,Q(1,8),(3,5,7,p))
        verified=ts.verify(w)
        independently=oracle.check(w)
        m=ts.order16(p)
        Lp=(p-1)//4
        overlap=max(0,min(2*A,2*Lp+1)-max(A,Lp+1))
        root=isqrt(p)
        sqrt_upper=root if root*root==p else root+1
        local_upper=min(Q(1),Q(sqrt_upper,m)+2*(1-Q(overlap,A)))
        covariance={h:verified['signed_lower'][h]-local_upper for h in (1,2,3,5)}
        assert all(bound>0 for bound in covariance.values())
        row={
            'J':J,'A':A,'B':w['B'],'K':w['K'],'eta':'1/8',
            'selected_prime':p,'selected_order':m,'observed_primes':w['observed_primes'],
            'q_prime_count':w['t'],'q_hex':format(w['q'],'x'),
            'q_bits':w['q'].bit_length(),'capacity_Kmax':w['precision_capacity'],
            'seed_hex_fraction':exact_hex(w['seed']),
            'selected_candidate_offset':w['skipped_candidates'],
            'original_terminal_denominator_bits':w['original'][-1].denominator.bit_length(),
            'exact_terminal_denominator_preserved':True,
            'all_denominators_divide_original_cumulative_D_B':True,
            'literal_zero_preserved':False,'chronological_support_preserved':False,
            'observed_principal_part_equalities':(w['B']+1)*len(w['observed_primes']),
            'two_adic_equalities':w['B']+1,'prefix_carry_equalities':J,
            'earliest_original_seed_prime_birth':verified['earliest_original_seed_prime_birth'],
            'latest_original_seed_prime_birth':verified['latest_original_seed_prime_birth'],
            'original_history_sha256':digest_rows(w['original']),
            'shadow_history_sha256':digest_rows(w['shadow']),
            'exact_mean_square_sha256':digest_rows([verified['mean_square']]),
            'signed_W_lower':{str(h):rational_lower(v) for h,v in verified['signed_lower'].items()},
            'local_clock_mean_abs_upper':str(local_upper),
            'signed_covariance_lower':{str(h):rational_lower(v) for h,v in covariance.items()},
            'independent_oracle':independently,
        }
        rows.append(row)
        print(f'A={A}, p={p}, K={w["K"]}, capacity={w["precision_capacity"]}, '
              f'W1>={row["signed_W_lower"]["1"]}, '
              f'Cov1>={row["signed_covariance_lower"]["1"]}',flush=True)
    result={'scope':'finite exact hostile controls; positive horizon-dependent seeds; pi normality OPEN',
            'rational_certificate_rounding':'downward to denominator 10^12',
            'fraction_encoding':'signed hexadecimal numerator / positive hexadecimal denominator',
            'rows':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
