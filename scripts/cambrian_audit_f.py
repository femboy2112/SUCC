#!/usr/bin/env python3
"""Independent analytic firewall audit. No tested arithmetic code is an oracle.

Independent objects: Ω-graded Dirichlet-log recurrence, telescoping log
enclosures, binary rational reciprocal-square-root bisection, tuple intervals.
The subject algorithm is called only as an explicitly identified SUT.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import platform
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
Interval=tuple[Q,Q]


def add(a:Interval,b:Interval)->Interval: return a[0]+b[0],a[1]+b[1]
def neg(a:Interval)->Interval: return -a[1],-a[0]
def sub(a:Interval,b:Interval)->Interval: return add(a,neg(b))
def mul(a:Interval,b:Interval)->Interval:
    products=[x*y for x in a for y in b]
    return min(products),max(products)
def scale(a:Interval,c:Q)->Interval: return mul(a,(c,c))
def divide(a:Interval,b:Interval)->Interval:
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def contains(a:Interval,x:Q)->bool: return a[0]<=x<=a[1]


def omega(n:int)->int:
    count=0
    d=2
    while d*d<=n:
        while n%d==0:
            n//=d
            count+=1
        d+=1
    return count+int(n>1)


def divisors(n:int)->list[int]: return [d for d in range(2,n+1) if n%d==0]


def connected(a:list[Q])->list[Q]:
    """DΩ a = a * DΩ b; solve triangularly, independent of exp/log powers."""
    assert a[1]==1
    b=[Q(0)]*len(a)
    for n in range(2,len(a)):
        b[n]=(omega(n)*a[n]-sum((omega(d)*b[d]*a[n//d]
                            for d in divisors(n) if d<n),Q(0)))/omega(n)
    return b


def reconstruct(b:list[Q])->list[Q]:
    a=[Q(0)]*len(b)
    a[1]=Q(1)
    for n in range(2,len(a)):
        a[n]=sum((omega(d)*b[d]*a[n//d] for d in divisors(n)),Q(0))/omega(n)
    return a


@lru_cache(None)
def log_bound(n:int)->Interval:
    """ln n=sum_(j=1)^(n-1) ln(1+1/j), each independently integrated series.

    ln((j+1)/j)=2*sum_(h>=0) (1/(2j+1))^(2h+1)/(2h+1).
    The positive tail is bounded by geometric comparison; 20 terms.
    This is different argument reduction/code from the audited binary reducer.
    """
    ans=(Q(0),Q(0))
    for j in range(1,n):
        t=Q(1,2*j+1)
        low=2*sum((t**(2*h+1)/(2*h+1) for h in range(20)),Q(0))
        tail=2*t**41/(41*(1-t*t))
        ans=add(ans,(low,low+tail))
    return ans


@lru_cache(None)
def reciprocal_sqrt(n:int)->Interval:
    lo,hi=Q(0),Q(1)
    for _ in range(75):
        mid=(lo+hi)/2
        if n*mid*mid<=1: lo=mid
        else: hi=mid
    assert n*lo*lo<=1<=n*hi*hi
    return lo,hi


def ramp(b:list[Q],t:Q,phase_mutant:dict[int,int]|None=None,
         density_power_one:bool=False,error:Q=Q(0))->Interval:
    ans=(Q(0),Q(0))
    for n in range(2,len(b)):
        if not b[n]: continue
        phase=log_bound((phase_mutant or {}).get(n,n))
        active=max(Q(0),t-phase[1]),max(Q(0),t-phase[0])
        density=(Q(1,n),Q(1,n)) if density_power_one else reciprocal_sqrt(n)
        weight=mul(log_bound(n),density)
        ans=add(ans,scale(mul(weight,active),-b[n]))
    return add(ans,(-error,error))


def clock(n:int)->tuple[Q,Q]:
    lo,hi=log_bound(n)[1],log_bound(n+1)[0]
    assert lo<hi
    return (2*lo+hi)/3,(lo+2*hi)/3


def invert(n:int,oracle)->Interval:
    before,after=clock(n-1),clock(n)
    ds=[scale(sub(oracle(pair[1]),oracle(pair[0])),1/(pair[1]-pair[0]))
        for pair in (before,after)]
    return divide(neg(sub(ds[1],ds[0])),mul(log_bound(n),reciprocal_sqrt(n)))


def slim_interval(a:Interval)->dict:
    """Sound outward rounding to rational decimal endpoints for readable receipts."""
    factor=10**15
    low=(a[0]*factor).__floor__()
    high=(a[1]*factor).__ceil__()
    return {"lower":str(Q(low,factor)),"upper":str(Q(high,factor)),
            "rounding":"outward exact rational, denominator divides 10^15"}


def rational_multiplier(scale:Q,weight:Q,s:int)->Q:
    return (weight+scale**(-s)+scale**(s-1))/(weight+1+1/scale)


def gaussian_prime_direct(real:int,imag:int)->bool:
    def isprime(n:int)->bool:
        return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
    if real==0 or imag==0:
        n=abs(real or imag)
        return isprime(n) and n%4==3
    return isprime(real*real+imag*imag)


def report()->dict:
    # Differential boundary only: these imports are the SUBJECT, never oracle.
    from observational_succ.cambrian_e_arithmetic_transport import (
        connected_from_four_queries,dirichlet_exp_prefix,selfdual_offline_family,
    )
    from observational_succ.observer_reflection import RationalInterval as SUTInterval
    records=[]
    genuine=[Q(0)]+[Q(1)]*40
    fake=genuine[:];fake[6]=Q(2)
    nonunit=[Q(0)]+[Q(2)**sum(1 for k in range(1,7) if n%(1<<k)==0)
                            for n in range(1,41)]
    for label,a in [('genuine',genuine),('fake_six',fake),('nonunit_at_2',nonunit)]:
        b=connected(a)
        assert reconstruct(b)==a
        assert dirichlet_exp_prefix(dict(enumerate(b)),40)==tuple(a)
        if label=='genuine':
            for n in range(2,41):
                # Independently recognize a genuine prime power by its factorization.
                prime_div=[p for p in range(2,n+1) if n%p==0
                           and all(p%d for d in range(2,isqrt(p)+1))]
                expected=Q(1,omega(n)) if len(prime_div)==1 else Q(0)
                assert b[n]==expected
        for n in (2,4,6,8,9,12,16,25,32):
            oracle=lambda t:ramp(b,t)
            independent=invert(n,oracle)
            actual=connected_from_four_queries(n,lambda t:SUTInterval(*oracle(t)))['coefficient_interval']
            sut=(actual.lower,actual.upper)
            assert contains(independent,b[n]) and contains(sut,b[n])
            records.append({'source':label,'event':n,'exact_b':str(b[n]),
                            'independent':slim_interval(independent),'subject':slim_interval(sut)})
    b=connected(genuine)
    endpoint_b=b[:];endpoint_b[40]+=Q(1)
    endpoint_queries=(Q(0),log_bound(40)[0]/3,2*log_bound(40)[0]/3,log_bound(40)[0])
    for t in endpoint_queries:
        assert ramp(b,t)==ramp(endpoint_b,t)
    assert reconstruct(endpoint_b)[40]!=genuine[40]
    controls=[]
    for label,kwargs in [('moved_log2',{'phase_mutant':{2:3}}),
                         ('wrong_density',{'density_power_one':True}),
                         ('large_sound_noise',{'error':Q(1,10)})]:
        oracle=lambda t:ramp(b,t,**kwargs)
        got=invert(2,oracle)
        controls.append({'mutation':label,'event':2,'coefficient_interval':slim_interval(got),
                         'declared_genuine_b1_enclosed':contains(got,Q(1)),
                         'denominator100_unique_sufficient':got[1]-got[0]<Q(1,10000)})
        if label in ('moved_log2','wrong_density'): assert not contains(got,Q(1))
        if label=='large_sound_noise': assert contains(got,Q(1)) and got[1]-got[0]>Q(1,10000)
    # Independent exact completion and sharp-boundary checks.
    scale,w=Q(9),Q(4,5)
    coeff=Q(3)*w;discriminant=coeff*coeff-4
    assert coeff==Q(12,5) and discriminant==Q(44,25)
    assert 2<coeff<Q(10,3)
    assert rational_multiplier(scale,w,0)==rational_multiplier(scale,w,1)==1
    assert rational_multiplier(scale,w,2)==rational_multiplier(scale,w,-1)
    subject=selfdual_offline_family(3,w)
    assert rational_multiplier(scale,w,2)==subject['source_multiplier_at_2']
    assert rational_multiplier(Q(2),Q(0),2)==Q(3,2)  # DZ8 alive
    assert rational_multiplier(Q(4),Q(11,10),2)==Q(413,188)  # DZ9 alive
    clocks=[{'p':p,'level':r,'child_mass':str(Q(1,p**(r+1))),
              'parent_mass':str(Q(1,p**r)),'norm_lower_bound':p**r}
             for p in (2,3,5) for r in (1,2,4,8)]
    for x in clocks: assert x['p']*Q(x['child_mass'])==Q(x['parent_mass'])
    assert 901==17*53 and all(901%p for p in (2,5,13))
    assert not gaussian_prime_direct(1,30)
    assert (4*2-1*7,4*7+1*2)==(1,30)  # explicit nonunit Gaussian factors
    # Small-width support is an exact source-domain falsifier to universal indefiniteness.
    assert 2*Q(1,4)<log_bound(2)[0]
    paths=['observational_succ/cambrian_e_arithmetic_transport.py',
           'scripts/cambrian_e_arithmetic_probe.py','tests/test_cambrian_e_arithmetic_transport.py',
           'research/2026-10-13/CAMBRIAN_E_ARITHMETIC.md']
    return {'audit':'F','audited_commit':'c2c18c3ed638478448497fb6892a747f67ee6f9b',
        'audit_base':'fb3499dfb6da9bd491bf89d01abe9de716b5d7b5',
        'python':platform.python_version(),
        'source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'auditor_script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'independent_representation':'Omega grading, telescoping integer logs, rational reciprocal-root bisection, tuple intervals',
        'tomography':records,'mutation_controls':controls,'clock_coherence_controls':clocks,
        'fresh_completion_control':{'scale':str(scale),'w':str(w),'quadratic':[1,str(coeff),1],
            'discriminant':str(discriminant),'R':'(6+sqrt(11))/5',
            'exact_R_bounds':'1<R<3, since 0<sqrt(11)<9 and sqrt(11)>0',
            'strict_strip_condition':'2<12/5<10/3','C0':1,'C1':1,
            'C2':str(rational_multiplier(scale,w,2)),
            'roots':'1/2 +/- log(R)/log(9) + (2j+1)pi*i/log(9)',
            'unknown_zeta_zero_inputs':False,'actual_zeta_zeros_asserted':False},
        'sharp_multiplier_boundary_controls':{
            'k_w_equals_2':{'quadratic':[1,2,1],'roots':[-1,-1],'real_part':str(Q(1,2))},
            'k_w_equals_k_plus_inverse_k':{'quadratic':[1,str(Q(10,3)),1],
                'roots':['-3','-1/3'],'real_parts':[0,1]}},
        'DZ8_recovered_C2':'3/2','DZ9_recovered_C2':'413/188',
        'sieve_control':{'point':[1,30],'norm':901,'factors':[17,53],
            'gaussian_factorization':[[4,1],[2,7]],'not_gaussian_prime':True},
        'revision_required':{'claim':'prime-only indefinite-form construction',
            'missing_assumption':'a>log(2)/2','countermodel_a':'1/4',
            'two_a_below_log2_certified':True,'prime_operator_in_countermodel':'zero'},
        'endpoint_T_equals_log_N':{'paper_verdict':'Last ramp atom has identically zero response on entire measured interval; exact symbolic proof',
            'four_rational_queries_below_boundary_agree':True,
            'source_coefficient_at_40_changes':True},
        'full_Weil_positivity':'UNVERIFIED, not tested or inferred',
        'Laplace_sign':'L[F_b](z)=-z^-2 sum b(n)log(n)n^-(z+1/2); for genuine full source equals +zeta_prime/zeta / z^2 only Re(z)>1/2'}


if __name__=='__main__':
    output=report()
    dest=ROOT/'research/2026-10-13/CAMBRIAN_AUDIT_F_RESULT.json'
    dest.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'audit':'F','tomography_cases':len(output['tomography']),
        'source_mutations':len(output['mutation_controls']),'revision_required':True,
        'actual_zeta_zeros_used':False,'results_file':str(dest)}))
