"""Postregistration dual audit of all unit-disk tables in a fixed carry menu.

This is a certificate of a method's finite approximation floor. It is not a
new predictor, a holdout retune, or an upper bound on the true signed mean.
"""
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import json
from math import isqrt
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from carry_model import (Box, Interval, SCALE, TABLE_SCALE, phase, packed,
                         unpacked, clock, source_xi, magnitude_bounds,
                         fraction_record, feature, key_text, toward_zero)


def radial_witness(box):
    re=(box.re.lo+box.re.hi)//2
    im=(box.im.lo+box.im.hi)//2
    norm2=re*re+im*im
    if not norm2:
        return Box()
    upper=isqrt(norm2)
    if upper*upper<norm2:upper+=1
    a=toward_zero(re*TABLE_SCALE,upper)
    b=toward_zero(im*TABLE_SCALE,upper)
    assert a*a+b*b<=TABLE_SCALE*TABLE_SCALE
    return Box(Interval.ratio(a,TABLE_SCALE),Interval.ratio(b,TABLE_SCALE))


def dual_certificate(target, row_features, witness):
    """One proof-valid lower bound, with all table features charged.

    row_features[r] lists the q replica categories at r; repetitions remain.
    Target and witness boxes enclose |target_r|<=1 and |witness_r|<=1. The
    latter is an explicit caller obligation: `radial_witness` enforces it.
    """
    m=len(target)
    if not m or len(row_features)!=m or len(witness)!=m:
        raise ValueError('matching nonempty arrays required')
    q=len(row_features[0])
    if not q or any(len(row)!=q for row in row_features):
        raise ValueError('same positive replica count required')
    alignment=Interval(0,0)
    totals=defaultdict(Box)
    for f,categories,v in zip(target,row_features,witness):
        alignment=alignment+(v.conjugate()*f).re
        for category in categories:
            totals[category]=totals[category]+v.conjugate()
    alignment=alignment.divide(m)
    cost=Q(0)
    moments={}
    for category,value in sorted(totals.items()):
        moment=value.divide(m*q)
        cost+=magnitude_bounds(moment)[1]
        moments[category]=packed(moment)
    lower=max(Q(0),Q(alignment.lo,SCALE)-cost)
    return {'lower_bound':fraction_record(lower),
            'alignment_box':alignment.as_list(),
            'table_support_function_upper':fraction_record(cost),
            'feature_moments':moments,'feature_count':len(moments),
            'witness_boxes_sha256':sha256(json.dumps([packed(v) for v in witness],separators=(',',':')).encode()).hexdigest()}


def audit(data):
    p,m,q,n0=data['p'],data['m'],data['q'],data['n0']
    carries=data['source']['carries']
    xs=clock(p,source_xi(p))
    out={'A':data['A'],'p':p,'m':m,'q':q,'rows':[],
         'scope':'Postregistration dual audit of every unit-disk table in each frozen feature menu; finite only.'}
    for row in data['folded_source']:
        h=row['h']
        target=[phase(h*x,p)*unpacked(b) for x,b in zip(xs,row['B'])]
        radial=[radial_witness(f) for f in target]
        for menu in ('one','two'):
            categories=[]
            for r in range(m):
                cats=[]
                for j in range(q):
                    n=n0+r+j*m
                    cats.append(key_text(feature(carries[n-2],carries[n-1],menu)))
                categories.append(cats)
            for name,witness in (('target',target),('radial_dyadic',radial)):
                cert=dual_certificate(target,categories,witness)
                cert.update({'h':h,'menu':menu,'witness':name})
                out['rows'].append(cert)
    out['pi_normality']=out['RH']='OPEN'
    return out


def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    raw=args.source.read_bytes()
    payload=gzip.decompress(raw) if args.source.suffix=='.gz' else raw
    result=audit(json.loads(payload))
    result['source_sha256']=sha256(raw).hexdigest()
    result['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    for row in result['rows']:
        print(row['h'],row['menu'],row['witness'],row['lower_bound']['decimal_diagnostic'],flush=True)


if __name__=='__main__':main()
