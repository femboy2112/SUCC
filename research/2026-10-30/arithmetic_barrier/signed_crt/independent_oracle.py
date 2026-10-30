"""Independent integer common-denominator source oracle + mpmath cross-check.

Does NOT import signed_crt. Integer LCM reconstruction verifies source hashes.
mpmath checks the rational enclosures but is not their proof authority.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import lcm
from pathlib import Path
import hashlib
import json
import mpmath as mp


@lru_cache(None)
def independent_source_phase(n):
    poles=((7,4),(4,-2),(3,-1),(2,-1))
    denominator=lcm(*(8*j-off for j in range(1,n+1) for off,_ in poles))
    numerator=sum(c*16**(n-j)*(denominator//(8*j-off))
                  for j in range(1,n+1) for off,c in poles)
    return F(numerator%denominator,denominator)


def mpf(q):
    q=F(q)
    return mp.mpf(q.numerator)/q.denominator


def contains(interval,value):
    return mpf(interval[0])<=value<=mpf(interval[1])


def main():
    path=Path(__file__).with_name('probe_receipt.json')
    data=json.loads(path.read_text())
    mp.mp.dps=90
    checks=0
    for row in data['rows']:
        p,h,b,L=(row[k] for k in ('p','h','birth','length'))
        phases=[independent_source_phase(n) for n in range(b,b+L)]
        assert hashlib.sha256('\n'.join(str(q) for q in phases).encode()).hexdigest()==row['source_phase_sha256']
        split=[]
        for u in phases:
            # Independent CRT: multiply numerator by inverse of cofactor.
            assert u.denominator%p==0 and u.denominator%(p*p)
            cofactor=u.denominator//p
            a=u.numerator*pow(cofactor,-1,p)%p
            complement=F((u.numerator*pow(p,-1,cofactor))%cofactor,cofactor)
            assert (u-F(a,p)-complement).denominator==1
            split.append((F(a,p),complement))
        e=lambda q:mp.exp(2j*mp.pi*mpf(q%1))
        full=abs(sum(e(h*u) for u in phases))
        primary=abs(sum(e(h*a) for a,_ in split))
        variation=sum(abs(e(h*split[j+1][1])-e(h*split[j][1])) for j in range(L-1))
        interaction=sum(1-mp.re(e(h*(phases[j+1]-phases[j]))) for j in range(L-1))/(L-1)
        for key,value in [('full_modulus',full),('primary_modulus',primary),('cofiber_variation',variation),('interaction_E',interaction)]:
            assert contains(row[key],value),(p,h,key,mp.nstr(value,35),row[key])
            checks+=1
    print(json.dumps({'status':'PASS','source_authority':'independent integer LCM reconstruction',
        'source_phases_checked':independent_source_phase.cache_info().currsize,
        'interval_cross_checks':checks,'mpmath_decimal_digits':90,
        'boundary':'mpmath is numerical cross-check; rational Machin/Taylor bounds supply certification'},indent=2))

if __name__=='__main__':main()
