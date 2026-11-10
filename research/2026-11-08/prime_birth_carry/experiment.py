"""Fresh A=2048 source-time holdout; protocol committed before source analysis.

PYTHONPATH repo_root python research/2026-11-08/prime_birth_carry/experiment.py --output /tmp/prime-birth-carry.json
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
from observational_succ.prime_birth_carry import (
    balanced_boundaries,prime_check,replay_epoch,stage_events,
    digit_word_counts,digit_tv_uniform,signed_carry_covariance,
    shadow_seed,shadow_negative_certificate,positive_parts,
    weighted_junction_law,junction_law_exact,STAGE_RATIONAL_SLOPES,
    pulse_formula,conditional_prime_digit_bound)


def multiplicative_order_16(p: int) -> int:
    v=16%p;d=1
    while v!=1:
        v=v*16%p;d+=1
        if d>p:raise ArithmeticError('invalid prime order')
    return d


def select_clock(A: int):
    center=Fraction(12*A,5)
    lo=(9*A+3)//4
    hi=(5*A)//2
    candidates=[]
    for p in range(lo+(1-lo)%8,hi+1,8):
        if not prime_check(p):continue
        try:balanced_boundaries(A,p)
        except ValueError:continue
        m=multiplicative_order_16(p)
        if m**3<=p or m**2*p.bit_length()**4<=p:continue
        candidates.append((abs(Fraction(p)-center),p,m))
    if not candidates:raise RuntimeError('no valid prime at this finite epoch')
    _,p,m=min(candidates)
    return p,m


def fraction_json(q):
    q=Fraction(q)
    return {'numerator':q.numerator,'denominator':q.denominator}


def complex_json(z):
    return {'real':round(z.real,12),'imag':round(z.imag,12),
            'abs':round(abs(z),12)}


def distribution(records):
    cnt=Counter(x.junction for x in records)
    n=len(records)
    return {'total':n,'counts':[cnt.get(i,0) for i in range(3)],
            'rates':[fraction_json(Fraction(cnt.get(i,0),n)) for i in range(3)],
            'parity_numerator':cnt.get(0,0)-cnt.get(1,0)+cnt.get(2,0),
            'parity_rate':fraction_json(Fraction(cnt.get(0,0)-cnt.get(1,0)+cnt.get(2,0),n))}


def run(A=2048):
    p,m=select_clock(A)
    rows=replay_epoch(A,p)
    bounds=balanced_boundaries(A,p)
    events=stage_events(rows)
    if tuple((n,j) for n,j,z,real in events)!=pulse_formula(p):
        raise AssertionError('wrong source birth line')
    stage=[]
    for j,(l,r) in enumerate(zip(bounds,bounds[1:])):
        sub=[v for v in rows if l<=v.n<r]
        stats=distribution(sub)
        limit=junction_law_exact(STAGE_RATIONAL_SLOPES[j])
        stats.update({'stage':j+1,'interval':[l,r],
                      'exact_junction_reference':[fraction_json(t) for t in limit],
                      'real_prime_carry_matches':sum(v.real_carry==v.prime_carry for v in sub),
                      'birth_indexes':[v.n for v in sub if v.injection]})
        stage.append(stats)
    prime_count=Counter(r.prime_carry%16 for r in rows)
    real_count=Counter(r.real_carry%16 for r in rows)
    scans=[]
    for d in (1,2,3):
        pc=digit_word_counts(rows,d,prime=True)
        rc=digit_word_counts(rows,d,prime=False)
        scans.append({'depth':d,'starts':A-d+1,
                      'prime_distinct':len(pc),'real_distinct':len(rc),
                      'prime_tv':fraction_json(digit_tv_uniform(pc,d)),
                      'real_tv':fraction_json(digit_tv_uniform(rc,d))})
    cov={str(h):{name:complex_json(z) if isinstance(z,complex) else z
                 for name,z in signed_carry_covariance(rows,h).items()}
         for h in (1,3,8)}
    # Matched controls are exact arithmetic and preserve source/prime passport.
    shadow=shadow_seed(A)
    cert=shadow_negative_certificate(A,shadow)
    if not cert:raise AssertionError('dyadic coherent seed not certified negative')
    wrong=replay_epoch(A,p,shadow)
    if not all(r.real_carry==15 for r in wrong):raise AssertionError('coherent carry failed')
    if not all(r.prime_carry==t.prime_carry and r.junction==t.junction
               for r,t in zip(rows,wrong)):
        raise AssertionError('prime-channel mutation under p-integral seed')
    alt=replay_epoch(A,p,Fraction(1,5))
    if not all(r.prime_carry==t.prime_carry for r,t in zip(rows,alt)):
        raise AssertionError('p-integral seed changed prime clock')
    exact_prime_pairs=sum(1 for r in rows if r.real_carry==r.prime_carry)
    pi_finger=weighted_junction_law()
    sha=hashlib.sha256((str(A)+'|'+str(p)+'|'+','.join(str(r.real_carry) for r in rows)+'|'+
                      ','.join(str(r.prime_carry) for r in rows)).encode()).hexdigest()
    return {'schema':'PBC-JUNCTION-A2048-v1',
            'scope':'finite original four-pole rational source; no pi normality theorem',
            'A':A,'p':p,'order_m':m,'stage_boundaries':bounds,
            'source_events':[{'n':n,'prime_injection':j,'prime_carry':z,'real_carry':real}
                             for n,j,z,real in events],
            'source_positive_rational_passport':all(sum(positive_parts(n))>0 for n in (A,)+tuple(v[0] for v in events)),
            'stage_junction':stage,'whole_junction':distribution(rows),
            'whole_junction_limit':[fraction_json(x) for x in pi_finger],
            'local_real_exact_carry_matches':exact_prime_pairs,
            'prime_carry_counts':[prime_count.get(i,0) for i in range(16)],
            'real_carry_counts':[real_count.get(i,0) for i in range(16)],
            'word_scans':scans,'signed_slip_character':cov,
            'hostile':{'dyadic_seed_sha256':hashlib.sha256((format(shadow.numerator,'x')+'/'+format(shadow.denominator,'x')).encode()).hexdigest(),
                       'dyadic_seed_denominator_power2':(shadow.denominator.bit_length()-1),
                       'all_wrong_real_carries_15':True,
                       'same_prime_channels_as_original':True,
                       'seed_one_fifth_changes_real_carries':any(r.real_carry!=t.real_carry for r,t in zip(rows,alt)),
                       'seed_one_fifth_same_prime_clock':True},
            'complete_exact_source_tape_sha256':sha,
            'analytical_status':'existing BEC04/CP imported for asymptotic; finite statistics descriptive'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    result=run()
    target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('source epoch',result['A'],'selected p',result['p'],'ord',result['order_m'])
    print('source-birth lines',result['source_events'])
    for s in result['stage_junction']:
        print('stage',s['stage'],'length',s['total'],'tau histogram',s['counts'],'parity',s['parity_rate'])
    print('observed real/prime carry matches',result['local_real_exact_carry_matches'])
    print('coherent wrong-seed all carries 15:',result['hostile']['all_wrong_real_carries_15'])
    print('receipt',str(target))

if __name__=='__main__':main()
