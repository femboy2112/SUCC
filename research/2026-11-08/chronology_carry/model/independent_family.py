"""Independent scalar-integer audit of CCM4, from individual source phases.

No import from carry_model, family_audit, Box, Fourier, or root-phase tools.
The source phase enclosures are shared; their fold and dual arithmetic are not.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import argparse
import gzip
import json

S=1<<80
Q=1<<24


def ceil_sqrt(n):
    a=isqrt(n)
    return a+(a*a<n)


def inward(n,d):
    return n//d if n>=0 else -((-n)//d)


def rational(value):
    return {'numerator':value.numerator,'denominator':value.denominator,
            'decimal_diagnostic':float(value)}


def verify(data,primary):
    m,q,n0=data['m'],data['q'],data['n0']
    carries=data['source']['carries']
    results=[]
    primary_rows={(r['h'],r['menu']):r for r in primary['rows'] if r['witness']=='radial_dyadic'}
    for source in data['per_time_phases']:
        h=source['h']
        if source['start']!=n0 or len(source['boxes'])!=m*q:
            raise ValueError('declared source chronology required')
        center_dot=0
        total_radius=0
        feature_sums={'one':defaultdict(lambda:[0,0]),'two':defaultdict(lambda:[0,0])}
        for r in range(m):
            re=im=radius=0
            for j in range(q):
                a,b,c,d=source['boxes'][r+j*m]
                x=(a+b)//2;y=(c+d)//2
                re+=x;im+=y
                radius+=max(x-a,b-x)+max(y-c,d-y)
            norm=ceil_sqrt(re*re+im*im)
            vx=inward(re*Q,norm) if norm else 0
            vy=inward(im*Q,norm) if norm else 0
            assert vx*vx+vy*vy<=Q*Q
            center_dot+=vx*re+vy*im
            total_radius+=radius
            for j in range(q):
                index=n0-1+r+j*m
                current,previous=carries[index],carries[index-1]
                for menu,key in (('one',str(current)),('two',f'{previous},{current}')):
                    feature_sums[menu][key][0]+=vx
                    feature_sums[menu][key][1]-=vy
        alignment_lower=Fraction(center_dot,Q*q*S*m)-Fraction(total_radius,q*S*m)
        for menu,sums in feature_sums.items():
            cost=Fraction(sum(ceil_sqrt((x*x+y*y)*S*S) for x,y in sums.values()),S*m*q*Q)
            lower=max(Fraction(0),alignment_lower-cost)
            claimed=primary_rows[h,menu]['lower_bound']
            main=Fraction(claimed['numerator'],claimed['denominator'])
            # Distinct outward arithmetic may round in either order. Agreement
            # is checked at2^-60, while each rational bound is proved separately.
            gap=abs(main-lower)
            assert gap<Fraction(1,1<<60)
            results.append({'h':h,'menu':menu,'lower_bound':rational(lower),
                            'alignment_lower':rational(alignment_lower),
                            'support_function_upper':rational(cost),
                            'difference_from_primary':rational(gap),
                            'features':len(sums),'radial_witnesses_checked':m})
    return {'rows':results,'source_phase_boxes_shared':True,
            'different_basis':'Individual e(hU_n) boxes folded directly; no principal/complement reconstruction.',
            'different_arithmetic':'Python Gaussian integers and Fraction; no primary Box or phase arithmetic.',
            'scope':'Independent arithmetic replay of finite family floors, not independent source construction.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--primary',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    source_raw=args.source.read_bytes();primary_raw=args.primary.read_bytes()
    data=json.loads(gzip.decompress(source_raw))
    output=verify(data,json.loads(primary_raw))
    output['source_sha256']=sha256(source_raw).hexdigest()
    output['primary_receipt_sha256']=sha256(primary_raw).hexdigest()
    output['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    for row in output['rows']:
        print(row['h'],row['menu'],row['lower_bound']['decimal_diagnostic'],
              row['difference_from_primary']['decimal_diagnostic'],flush=True)


if __name__=='__main__':main()
