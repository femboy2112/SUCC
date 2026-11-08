"""Run prospectively specified holdouts and write exact reproducible receipts."""
import hashlib
import json
from math import gcd, prod
from fractions import Fraction as Q
from pathlib import Path
import sys

# Bind the shared source to this checkout, including for direct script execution.
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import finite_adelic as primary
import independent_oracle

BASE=Path(__file__).resolve().parent
ROWS=((5,17,19,9,18),(11,37,41,17,22),(17,73,79,31,26),(23,137,139,47,30))


def fraction_record(q):
    raw=f'{q.numerator}/{q.denominator}'.encode()
    return {'numerator_bits':abs(q.numerator).bit_length(),
            'denominator_bits':q.denominator.bit_length(),
            'sha256':hashlib.sha256(raw).hexdigest()}


def main(output=BASE):
    output=Path(output)
    output.mkdir(parents=True,exist_ok=True)
    results=[]
    seeds=[]
    for J,A,L,K,E in ROWS:
        B=A+L-1
        P=primary.primes_through(8*B)
        w=primary.construct(J,A,L,K,Q(1,2**E),P)
        error,margin,residuals,lower=primary.verify(w)
        assert all(x > Q(999,1000) for x in lower.values())
        independent=independent_oracle.check(w)
        # A fixed seed has not been produced across the growing horizons.
        assert w['seed'].denominator > 1
        assert gcd(w['seed'].denominator,prod(P)) == 1
        assert w['seed'] not in seeds
        seeds.append(w['seed'])
        record={
            'J':J,'A':A,'L':L,'B':B,'K':K,'eta':f'1/{2**E}',
            'prime_count':len(P),'max_prime':max(P),'seed':fraction_record(w['seed']),
            'seed_is_exact_zero':w['seed']==0,
            'complete_original_denominator_support_preserved':False,
            'new_seed_denominator_coprime_to_all_original_epoch_support':True,
            'seed_upper_bound':str(Q(1,16**A)+Q(1,2**E*16**B)),
            'principal_part_equalities':(B+1)*len(P),
            'two_adic_equalities':B+1,'independent_state_equalities':independent,
            'prefix_floors_equal':J+1,'prefix_carry_increments_equal':J,
            'prefix_error':fraction_record(error),'prefix_margin':str(margin),
            'max_future_distance':fraction_record(max(abs(t) for t in residuals)),
            'weyl_realpart_lower_bounds':{
                str(h):{'exact':fraction_record(v),
                        'floor_12_decimals':str((v*10**12)//1)+'/1000000000000'}
                for h,v in lower.items()},
            'source_requires_no_pi_input':True,
        }
        results.append(record)
        print(f"A={A} B={B}: {record['principal_part_equalities']} principal parts, "
              f"{independent} independent states; h=5 Re(W) > "
              f"{lower[5]*10**12//1}/10^12; literal zero rejected",flush=True)
    receipts={'status':'EXACT_FINITE_CERTIFICATES','rows':results,
              'quantifier':'for each horizon a distinct rational seed; no fixed-seed nonnormality',
              'pi_normality':'OPEN','rh':'OPEN'}
    (output/'FINITE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
    # A reproducible hash ledger over proof/code/preregistration and receipts.
    paths=['THEOREMS.md','PREREGISTRATION.md','finite_adelic.py','independent_oracle.py',
           'run_receipts.py','test_finite_adelic.py','FINITE_RECEIPTS.json',
           '../../../../observational_succ/selected_orbit.py',
           '../../../../observational_succ/duck_bbp.py']
    hashes={p:hashlib.sha256(((output if p=='FINITE_RECEIPTS.json' else BASE)/p).read_bytes()).hexdigest() for p in paths}
    (output/'ARTIFACT_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=BASE)
    main(parser.parse_args().output)
