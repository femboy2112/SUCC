"""Classical Shallit folding calibrated against independent Euclidean division.
Primary source: J. Shallit, JNT 11 (1979), 209-217, Theorem 1.
No claim of new discovery or finite proof of bounded infinite partial quotients.
"""
from fractions import Fraction as Q
import json


def fold(u,v):
    if u<3 or v<1: raise ValueError('u>=3, v>=1')
    a=[0,u-1,u+1]
    for _ in range(1,v):
        a=a[:-1]+[a[-1]+1,a[-1]-1]+a[-2:0:-1]
    return a


def euclidean(p,q):
    out=[]
    while q:
        a,r=divmod(p,q)
        out.append(a);p,q=q,r
    return out


def run():
    rows=[]
    for u in (3,5,16,19):
        for v in range(2,11):
            value=sum((Q(1,u**(2**j)) for j in range(v+1)),Q(0))
            f=fold(u,v);e=euclidean(value.numerator,value.denominator)
            assert f==e
            assert set(f[1:])<={u-2,u-1,u,u+2}
            assert len(f)==2**v+1
            rows.append(dict(u=u,v=v,length=len(f),max_partial_quotient=max(f),
                             exact_fold_equals_euclidean=True))
    windows=[]
    for j in (5,8,11):
        a=2**j+1;b=2**(j+1)-2
        bound=Q(1,256)+Q(16,(8*a+1)**3)
        assert bound<Q(1,20)
        windows.append(dict(A=a,B=b,length=b-a+1,
                            all_index_distance_upper=str(bound)))
    return dict(classical_reference='https://cs.uwaterloo.ca/~shallit/Papers/scf.pdf',
                fold_rows=rows,whole_windows=windows,
                scope='Exact finite recovery of a published theorem; infinite result uses its proof.')

if __name__=='__main__': print(json.dumps(run(),indent=2))
