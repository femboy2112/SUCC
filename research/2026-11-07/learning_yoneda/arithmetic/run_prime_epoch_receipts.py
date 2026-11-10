"""Exact pole/cycle/gluing and hostile signed covariance certificates."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
import hashlib
import json
from fractions import Fraction as Q
import finite_adelic as f
import prime_epochs as p
import independent_oracle

BASE=Path(__file__).resolve().parent


def main(output=BASE):
    output=Path(output)
    output.mkdir(parents=True,exist_ok=True)
    clean=[]
    for prime in (577,641,881,1201,1601):
        w,counts=p.exact_clean_check(prime)
        clean.append(dict(w,distinct_residues=len(counts),cycle_repetitions=w['L']//w['order'],
                          checked_principal_parts=w['next_pole']-w['birth'],
                          gauss_upper=str(p.gauss_rational_upper(prime))))
    selectors=[]
    for A in (37,73,137,257,521):
        prime=p.good_prime(A)
        w=p.window(prime)
        weights=sum(abs(Q(int(A<=n<2*A),A)-Q(int(w['start']<=n<w['stop']),w['L']))
                    for n in range(min(A,w['start']),max(2*A,w['stop'])))
        assert weights==p.variation(A,prime)
        selectors.append({'A':A,'p':prime,'L':w['L'],'order':w['order'],
                          'p_over_4A':str(Q(prime,4*A)),'exact_total_variation':str(weights)})
    hostile=[]
    for prime in (137,281,521):
        w=p.window(prime)
        shadow=f.construct(3,w['start'],w['L'],9,Q(1,2**20),(3,5,7,prime))
        _,_,_,lower=f.verify(shadow)
        independent_count=independent_oracle.check(shadow)
        g=p.gauss_rational_upper(prime)
        signed=lower[1]-g
        assert signed>0
        row={'p':prime,'A':w['start'],'L':w['L'],'order':w['order'],
             'principal_parts_preserved':shadow['B']+1,'independent_states':independent_count,
             'gauss_rational_upper':str(g),
             'Re_W_lower_floor_12':str(lower[1]*10**12//1)+'/1000000000000',
             'Re_covariance_lower_floor_12':str(signed*10**12//1)+'/1000000000000',
             'exact_covariance_lower_sha256':hashlib.sha256(str(signed).encode()).hexdigest(),
             'literal_zero_preserved':False,'original_denominator_support_preserved':False}
        hostile.append(row)
        print(f"p={prime}: m={w['order']}, aligned length={w['L']}, "
              f"Re Cov > {signed*10**12//1}/10^12",flush=True)
    result={'status':'CERTIFIED-FINITE','clean_epochs':clean,'good_prime_selectors':selectors,
            'hostile_covariance':hostile,
            'BK_or_PNT_asymptotic_validated_by_finite_data':False,
            'pi_normality':'OPEN','RH':'OPEN'}
    (output/'PRIME_EPOCH_RECEIPTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f"Clean principal parts: {sum(x['checked_principal_parts'] for x in clean)}; "
          f"complete-cycle epoch points: {sum(x['L'] for x in clean)}",flush=True)
    paths=['PRIME_EPOCH_THEOREM.md','PRIME_EPOCH_PREREGISTRATION.md','prime_epochs.py',
           'test_prime_epochs.py','run_prime_epoch_receipts.py','PRIME_EPOCH_RECEIPTS.json',
           'EXTERNAL_SOURCE_AUDIT.json',
           'finite_adelic.py','independent_oracle.py',
           '../../../../observational_succ/selected_orbit.py','../../../../observational_succ/duck_bbp.py']
    hashes={x:hashlib.sha256(((output if x=='PRIME_EPOCH_RECEIPTS.json' else BASE)/x).read_bytes()).hexdigest() for x in paths}
    (output/'PRIME_EPOCH_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=BASE)
    main(parser.parse_args().output)
