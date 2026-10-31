"""Exact bounded-packet holdouts for CG-01; not proof of an asymptotic rate."""
from fractions import Fraction as F
from math import ceil
import json
from independent_arithmetic_audit import prefix, prime, reduce, vp


def shadows(last):
    tables={}
    for cls,offsets,coefficients in ((1,(1,4,5,6),(4,-2,-1,-1)),
                                   (5,(1,4,5,6),(4,-2,-1,-1)),
                                   (3,(2,3,4,7),(8,4,4,-1)),
                                   (7,(2,3,4,7),(-32,-16,-16,4))):
        v=F()
        for k in range(1,last+1):
            partial=16*v
            for d,c in zip(offsets,coefficients):
                partial += F(c,8*(k-1)+d)
                assert (partial>0) == (cls!=7)
                assert partial != 0
                tables[cls,k,d]=partial
            v=partial
    return tables


def main():
    # Independent times, including the known p73 cancellation within packet4.
    times=(97,127,211,274,383,761,1021)
    values=prefix(max(times)+1)
    tables=shadows(32)
    rows=[]
    cancelled=[]
    for n in times:
        tested=0
        for p in range(max(37,ceil(n/4)),8*n+1):
            if not prime(p):
                continue
            cls=p%8
            D=(1,4,5,6) if cls in (1,5) else (2,3,4,7)
            events=[]
            for q in range(1,(8*n-2)//p+1):
                if q%8 not in D:
                    continue
                j=(p*q+8-p*q%8)//8
                if j<=n:
                    events.append((q,j))
            if not events:
                continue
            q,j=events[-1]
            k,s=q//8+1,q%8
            assert k<=5 and p>8*k-1
            L=8*k-(2 if cls in (1,5) else 1)
            M=(p*L+8-(p*L)%8)//8
            H=tables[cls,k,s]
            expected=reduce(H,p)
            actual=reduce(p*values[n],p)*pow(16,M-n,p)%p
            assert actual==expected
            if expected:
                assert vp(values[n],p)==-1
                if all((8*(n+1)-d)%p for d in (7,4,3,2)):
                    assert vp(values[n+1]-values[n],p)==-1
            else:
                assert values[n].denominator%p != 0
                cancelled.append({'n':n,'p':p,'packet':k,'offset':s})
            tested+=1
        rows.append({'n':n,'comparably_large_born_primes_checked':tested,
                     'state_denominator_bits':values[n].denominator.bit_length(),
                     'difference_denominator_bits':(values[n+1]-values[n]).denominator.bit_length()})
    assert {'n':274,'p':73,'packet':4,'offset':6} in cancelled
    print(json.dumps({'status':'PASS_FINITE_EXACT','partial_rationals_checked':len(tables),
                     'rows':rows,'retained_exact_cancellations':cancelled,
                     'asymptotic_rate_certified_by_this_run':False},indent=2))


if __name__=='__main__':
    main()
