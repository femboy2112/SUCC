"""Exact rational finite-dimensional tests for the signed-tail Schur gate.

These tests are algebra controls, not source-authentic Weil sign certificates.
"""
from fractions import Fraction as F


def inverse(matrix):
    n=len(matrix)
    a=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None: raise ValueError("singular")
        a[j],a[k]=a[k],a[j]
        z=a[j][j]
        a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j]
                a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    return tuple(tuple(row[n:]) for row in a)


def schur_scalar(a,b,d,lam):
    a,b,d,lam=map(F,(a,b,d,lam))
    if lam<=0 or d<0: raise ValueError("require nonnegative high block and positive shift")
    return a+lam-b*b/(d+lam)


def source_positive_tail_lower_bound(a,b,d,lam,tau):
    """Valid only for a nonnegative omitted tail, no RH conclusion."""
    a,b,d,lam,tau=map(F,(a,b,d,lam,tau))
    if tau<0: raise ValueError("positive tail required")
    return schur_scalar(a,b,d,lam)


def negative_depth_diagonal(diag):
    if not diag: raise ValueError("empty")
    return max(F(0),-min(map(F,diag)))


def compact_countermodel(rank,hidden,delta):
    if not 0<=rank<hidden or delta<=0: raise ValueError("bad finite observation")
    positive=(F(0),)*hidden
    negative=positive[:rank]+(F(-delta),)+positive[rank+1:]
    return {"same_observed_compression":positive[:rank]==negative[:rank],
            "positive_depth":negative_depth_diagonal(positive),
            "hidden_negative_depth":negative_depth_diagonal(negative)}


def receipt():
    shifts=[F(1,2),F(1,4),F(1,8),F(1,16)]
    s=[schur_scalar(F(1),F(1,2),F(1,16),v) for v in shifts]
    return {"shifts":[str(x) for x in shifts],"schur":[str(x) for x in s],
            "increasing_with_shift":all(s[i]>s[i+1] for i in range(len(s)-1)),
            "zero_shift_divergence_control":[str(schur_scalar(1,1,0,F(1,2**n))) for n in range(1,9)],
            "hidden_negative":{k:(str(v) if isinstance(v,F) else v) for k,v in compact_countermodel(5,8,F(1,7)).items()},
            "source_authentic_Weil_sign_proved":False,"RH_proved":False}
