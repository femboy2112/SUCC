"""Separate interval-arithmetic/direct-sum check of held-out maxima.

This shares the root's source boxes but uses no FFT or Taylor phase evaluator.
It is arithmetic/algorithm diversity, not independent source provenance.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
from mpmath.ctx_iv import MPIntervalContext

HERE=Path(__file__).resolve().parent


def rational(mpf_tuple):
    sign,man,exponent,_=mpf_tuple
    value=Q((-1 if sign else 1)*man)
    return value*2**exponent if exponent>=0 else value/Q(2**(-exponent))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--A',type=int,default=22003)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    sp=HERE/f'results/source_{args.A}.json'
    bp=HERE/f'results/budget_{args.A}.json'
    source=json.loads(sp.read_text());budget=json.loads(bp.read_text())
    p,m=source['p'],source['m']
    L=(p-1)//4
    xi=4*pow(16,L+1-(p+7)//8,p)%p
    xs=[xi]
    for _ in range(1,m):xs.append(xs[-1]*16%p)
    assert len(set(xs))==m and xs[-1]*16%p==xi
    iv=MPIntervalContext();iv.dps=70
    scale=1<<80
    rows=[]
    for source_row,budget_row in zip(source['rows'],budget['rows']):
        assert source_row['h']==budget_row['h']
        B=[iv.mpc(iv.mpf([a,b])/scale,iv.mpf([c,d])/scale)
           for a,b,c,d in source_row['B']]
        for measured in budget_row['maxima']:
            degree=measured['degree'];t=measured['maximizing_upper_bound_slope']
            total=iv.mpc(0)
            for x,b in zip(xs,B):
                angle=-2*iv.pi*((t*pow(x,degree,p))%p)/p
                total+=b*iv.mpc(iv.cos(angle),iv.sin(angle))
            magnitude=abs(total/m)
            lo,hi=[rational(tup) for tup in magnitude._mpi_]
            stored=measured['max_correlation_upper']
            upper=Q(stored['numerator'],stored['denominator'])
            rad=measured['normalized_L1_radius']
            radius=Q(rad['numerator'],rad['denominator'])
            assert hi<=upper
            assert upper-lo<=2*radius+Q(10000,scale)
            rows.append({'h':source_row['h'],'degree':degree,'slope':t,
                         'direct_abs_interval':[str(lo),str(hi)],
                         'inside_fft_upper':True,'gap_within_radius':True})
    out={'A':args.A,'direct_terms':len(rows)*m,'checks':rows,
         'source_sha256':sha256(sp.read_bytes()).hexdigest(),
         'budget_sha256':sha256(bp.read_bytes()).hexdigest(),
         'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Independent MPIntervalContext direct sums of shared source boxes; all selected maxima, no FFT; no asymptotic claim.'}
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(args.A,len(rows),'maxima;',len(rows)*m,'direct interval terms PASS')


if __name__=='__main__':main()
