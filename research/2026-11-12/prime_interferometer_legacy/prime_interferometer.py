#!/usr/bin/env python3
"""Exact, source-transparent finite probes for the SUCC/Goldbach Haar proposal.

Scope: finite integer intervals only; never treats a computation as a Goldbach proof.
No external dependencies. Python >=3.10.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path


def sieve(limit: int) -> list[bool]:
    arr = bytearray(b'\x01') * (limit + 1)
    arr[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if arr[p]:
            arr[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    return [bool(v) for v in arr]


def integer_haar_correlation(a: list[int], b: list[int]):
    """Parseval overlap by scale. All outputs Fraction-exact."""
    N = len(a)
    assert N == len(b) and N > 0 and N & (N-1) == 0
    pre_a = [0]
    pre_b = [0]
    for x, y in zip(a, b):
        pre_a.append(pre_a[-1] + x)
        pre_b.append(pre_b[-1] + y)
    def sm(pre, lo, hi):
        return pre[hi]-pre[lo]
    lowpass = Fraction(pre_a[-1] * pre_b[-1], N)
    by_width = {}
    width = 2
    while width <= N:
        total = Fraction(0)
        for lo in range(0, N, width):
            mid = lo + width//2
            hi = lo + width
            da = sm(pre_a,lo,mid)-sm(pre_a,mid,hi)
            db = sm(pre_b,lo,mid)-sm(pre_b,mid,hi)
            total += Fraction(da*db, width)
        by_width[width] = total
        width *= 2
    direct = sum(x*y for x,y in zip(a,b))
    assert lowpass + sum(by_width.values(), Fraction(0)) == direct
    return lowpass, by_width, direct


def goldbach_haar(n: int, prime: list[bool]):
    assert n >= 2 and len(prime) > 2*n
    width = 1 << (n-2).bit_length()
    a, b = [0]*width, [0]*width
    for d in range(n-1): # 0 <= d <= n-2, both summands >= 2
        eligible = (n == 2 or ((n+d)&1)==1)
        if eligible:
            a[d] = int(prime[n+d])
            b[d] = int(prime[n-d])
    lowpass, detail, G = integer_haar_correlation(a,b)
    # Quotient the deterministic parity sublattice before using Haar as a probe.
    if n > 2:
        assert width % 2 == 0
        parity_index = (1-n) % 2
        aq,bq = a[parity_index::2], b[parity_index::2]
        qlow,qdetail,qG=integer_haar_correlation(aq,bq)
        assert qG==G and detail[2]==Fraction(G,2), 'parity echo failed'
    else:
        qlow,qdetail,qG=lowpass,detail,G
    ordered_direct = sum(int(prime[p] and prime[2*n-p]) for p in range(2,2*n-1))
    assert ordered_direct == 2*G-int(prime[n])
    return {'midpoint_n':n,'n_is_prime':bool(prime[n]),
            'goldbach_witnesses_unordered':G,'ordered_pairs':ordered_direct,
            'half_interval_size':n-1,'padded_haar_size':width,
            'plus_primes':sum(a),'minus_primes':sum(b),
            'lowpass':str(lowpass),
            'details_by_width':{str(k):str(v) for k,v in detail.items()},
            'signed_detail_sum':str(sum(detail.values(), Fraction(0))),
            'exact_parseval':True,'finest_scale_parity_echo': (n==2 or detail[2]==Fraction(G,2)),
            'parity_quotient_lowpass':str(qlow),
            'parity_quotient_detail_sum':str(sum(qdetail.values(),Fraction(0))),
            'parity_quotient_details_by_width':{str(k):str(v) for k,v in qdetail.items()}}


def countermodel():
    L=32
    a=[int((i%4)==1) for i in range(L)]
    b=[int((i%4)==3) for i in range(L)]
    low,detail,overlap=integer_haar_correlation(a,b)
    _,dpos,pos=integer_haar_correlation(a,a)
    assert overlap==0 and pos==8
    assert all(v==0 for k,v in detail.items() if k>=8)
    assert all(v==0 for k,v in dpos.items() if k>=8)
    # Every aligned dyadic interval length >=4 sees identical counts A and B.
    for width in [4,8,16,32]:
        for i in range(0,L,width):
            assert sum(a[i:i+width])==sum(b[i:i+width])
    return {'length':L,'allowed_parity':'odd','a_support':[i for i,v in enumerate(a) if v],
            'b_support':[i for i,v in enumerate(b) if v],
            'same_marginal_counts_each_dyadic_block_width_at_least_4':True,
            'no_witness_overlap':overlap,'positive_control_overlap':pos,
            'lowpass':str(low),'negative_control_details':{str(k):str(v) for k,v in detail.items()},
            'positive_control_details':{str(k):str(v) for k,v in dpos.items()}}


def crt_local(n: int, ell: int):
    assert ell>=2
    good=sum((n*n-d*d)%ell != 0 for d in range(ell))
    expected=ell-(1 if n%ell==0 or ell==2 else 2)
    assert good==expected
    return {'ell':ell,'admissible_residues':good,'forbidden_residues':ell-good}


def sieve_probe(n:int, prime:list[bool], bounds=(3,5,7,11)):
    # Compare local CRT survival with exact primality only in source-safe interior.
    result=[]
    for bound in bounds:
        small=[p for p in range(2,bound+1) if prime[p]]
        dmax=max(-1,n-bound-1) # both endpoints strictly > cutoff
        ds=[d for d in range(max(0,dmax+1)) if ((n+d)&1)==1]
        survivors=[d for d in ds if all((n*n-d*d)%p for p in small)]
        genuine=[d for d in survivors if prime[n+d] and prime[n-d]]
        result.append({'cutoff':bound,'interior_candidates':len(ds),
                       'crt_survivors':len(survivors),'true_pairs':len(genuine),
                       'false_survivors':len(survivors)-len(genuine)})
    return {'n':n,'by_cutoff':result}


def crt_haar_certificate(n: int, z: int, block: int, prime: list[bool]):
    """Certified inclusion-exclusion via same CRT channel occupancy.

    Only paths n-d>z are included; small prime endpoints are excluded.
    A_z,B_z are SINGLE-SIDE prime indicators, but both are restricted to
    channels in which neither endpoint has a prime factor <=z.
    """
    assert n>=3 and z>=2 and block>=1 and block & (block-1)==0
    small_primes=[ell for ell in range(2,z+1) if prime[ell]]
    groups={}
    D=[]
    for d in range(n-z): # n-d >= z+1
        if all((n*n-d*d)%ell for ell in small_primes):
            D.append(d)
            if d//block not in groups:groups[d//block]=[0,0,0]
            g=groups[d//block];g[0]+=1
            g[1]+=int(prime[n+d]);g[2]+=int(prime[n-d])
    bound=sum(max(0,A+B-Dcnt) for Dcnt,A,B in groups.values())
    ceiling=sum(min(A,B) for Dcnt,A,B in groups.values())
    actual=sum(int(prime[n+d] and prime[n-d]) for d in D)
    assert 0<=bound<=actual<=ceiling
    return {'n':n,'cutoff':z,'block_size':block,'crt_survivors':len(D),
            'prime_plus':sum(g[1] for g in groups.values()),
            'prime_minus':sum(g[2] for g in groups.values()),
            'certified_lower_bound':bound,'certified_upper_bound':ceiling,'actual_interior_witnesses':actual,
            'source_safe_interior':f'n-d>{z}','checked_inequality':True}


def matched_coarse_zero_overlap_countermodel(n:int, z:int, block:int, prime:list[bool]):
    """Construct fake prime source with exact marginal block counts and 0 pairs.

    If the CRT channel has enough spare positions per block, fill disjoint
    spots on the plus/minus side. This is a direct adversarial witness to
    non-identifiability from those block statistics.
    """
    small_primes=[ell for ell in range(2,z+1) if prime[ell]]
    groups={}
    for d in range(n-z):
        if all((n*n-d*d)%ell for ell in small_primes):
            groups.setdefault(d//block, []).append(d)
    afake,bfake=set(),set()
    for I,ds in groups.items():
        count_a=sum(prime[n+d] for d in ds)
        count_b=sum(prime[n-d] for d in ds)
        assert count_a+count_b<=len(ds), 'block forces a Goldbach witness: no counterfeit possible'
        afake.update(ds[:count_a]);bfake.update(ds[count_a:count_a+count_b])
        assert not (afake&bfake)
        assert sum(d in afake for d in ds)==count_a
        assert sum(d in bfake for d in ds)==count_b
    # Prime source is a single integer predicate f: plus and minus sides do not intersect for d>0.
    assert 0 not in afake and 0 not in bfake
    return {'n':n,'cutoff':z,'block_size':block,
            'coarse_margin_counts_identical_to_actual_source':True,
            'crt_admissible_positions_only':True,
            'fake_plus_count':len(afake),'fake_minus_count':len(bfake),
            'fake_goldbach_witnesses':len(afake&bfake),
            'actual_goldbach_witnesses':sum(prime[n+d] and prime[n-d] for ds in groups.values() for d in ds)}

def main():
    prime=sieve(20002)
    test_midpoints=[2,5,10,11,50,100,101,256,257,512,1024,2048,4096]
    gold=[goldbach_haar(n,prime) for n in test_midpoints]
    assert all(x['ordered_pairs']>0 for x in gold) # finite sample only
    assert all(x['ordered_pairs']%2==int(x['n_is_prime']) for x in gold)
    for z in [2,3,5,7]:
        hierarchy = [crt_haar_certificate(1024,z,w,prime) for w in [128,64,32,16,8,4,2,1]]
        assert all(a['certified_lower_bound']<=b['certified_lower_bound']
                   and a['certified_upper_bound']>=b['certified_upper_bound']
                   for a,b in zip(hierarchy,hierarchy[1:]))
        assert hierarchy[-1]['certified_lower_bound']==hierarchy[-1]['certified_upper_bound']
    for n in [5,10,100,256]:
        for ell in [2,3,5,7,11,13]:
            assert crt_local(n,ell)['admissible_residues']>=1
    out={'protocol':'exact finite Haar + independent prime-pair count + CRT ablations',
         'scope':'finite sample; no universal Goldbach inference',
         'midpoints':gold,'countermodel':countermodel(),
         'crt_example_n100':[crt_local(100,p) for p in [2,3,5,7,11,13]],
         'sieve_ablations':[sieve_probe(n,prime) for n in [100,256,1024]],
         'crt_haar_certificates': [crt_haar_certificate(1024,z,block,prime)
                                    for z,block in [(2,128),(3,128),(3,64),(3,32),(3,16),(3,8),(5,128),(5,64),(7,128)]],
         'matched_coarse_hostile_source':matched_coarse_zero_overlap_countermodel(1024,2,128,prime),
         'observer_hierarchy_z3_n1024':[crt_haar_certificate(1024,3,w,prime)
                                        for w in [1024,512,256,128,64,32,16,8,4,2,1]],
         'checks_passed':['Haar identity exact Fraction','ordered count direct independent loop',
                          'exchange parity','CRT local residue counts','countermodel coarse matching',
                          'CRT-Haar lower AND upper bounds', 'monotone observer refinement',
                          'matched-marginal CRT hostile source']}
    output=str(Path(__file__).with_name('results.json'))
    with open(output,'w') as f: json.dump(out,f,indent=2)
    print('Validated finite experiment; saved',output)
    print('n  R(2n)  unord G   lowpass   detail-sum')
    for r in gold:
        print(f"{r['midpoint_n']:>5} {r['ordered_pairs']:>7} {r['goldbach_witnesses_unordered']:>8} {float(Fraction(r['lowpass'])):>9.3f} {float(Fraction(r['signed_detail_sum'])):>11.3f}")
    c=out['countermodel']
    print('Countermodel overlap',c['no_witness_overlap'],'positive control',c['positive_control_overlap'], 'lowpass',c['lowpass'])
    print('CRT n=100',out['crt_example_n100'])
    print('CRT Haar certificates:', [(v['cutoff'],v['block_size'],v['certified_lower_bound']) for v in out['crt_haar_certificates']])
    print('Matched-source counterfeit:', out['matched_coarse_hostile_source'])
    for r in out['sieve_ablations']:
        print('sieve n',r['n'],[(s['cutoff'],s['crt_survivors'],s['true_pairs']) for s in r['by_cutoff']])

if __name__ == '__main__':main()
