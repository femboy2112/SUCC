"""Independent arithmetic oracle: never imports primary implementation.

1. Exact big-Fraction recurrence at remote times.
2. Separate event-sum over multiples of p in four source denominators.
3. Euler/Legendre class check and arbitrary coefficient mutant.
4. Numerical sanity of CRT reconstructed complex phases (NOT a proof of pi normality).
"""
from fractions import Fraction
from math import gcd
import json

POLES=((7,4),(4,-2),(3,-1),(2,-1))

def isprime(p):
    return p>=2 and all(p%q for q in range(2,int(p**0.5)+1))

def fraction_source(n,weights=(4,-2,-1,-1)):
    return sum((Fraction(weights[i],8*n-off) for i,(off,_) in enumerate(POLES)),Fraction(0))

def selected(n,weights=(4,-2,-1,-1)):
    v=Fraction(0)
    for j in range(1,n+1):
        v=16*v+fraction_source(j,weights)
    return v

def modq(q,p):
    q=Fraction(q)
    assert q.denominator%p
    return (q.numerator*pow(q.denominator,-1,p))%p

def strobe(p,k):
    assert p%4==1 and p>8*k-2
    return ((4*k-1)*p+1)//4

def event_sum(p,k,weights):
    end=strobe(p,k)
    val=0
    event_details=[]
    for j in range(1,end+1):
        for i,(offset,_) in enumerate(POLES):
            den=8*j-offset
            if den%p==0:
                q=den//p
                assert 1<=q<p
                contrib=modq(Fraction(weights[i],q),p)*pow(16,end-j,p)%p
                val=(val+contrib)%p
                event_details.append((j,q,offset,contrib))
    assert len(event_details)==4*k
    return val,event_details

def transformed(weights,p):
    A,B,C,D=weights
    return weights if p%8==1 else (Fraction(-4*C),B,Fraction(-A,4),D)

def main():
    primes=[p for p in range(13,120) if isprime(p) and p%8 in(1,5)]
    rows=[]
    count=0
    for p in primes:
        legendre=pow(2,(p-1)//2,p)
        assert legendre == (1 if p%8==1 else p-1)
        for k in range(1,5):
            if p<=8*k-2:continue
            N=strobe(p,k)
            for weights in [(4,-2,-1,-1),(5,7,2,-3),(4,0,-1,0)]:
                lhs=modq(p*selected(N,weights),p)
                independently,events=event_sum(p,k,weights)
                rhs=modq(selected(k,transformed(weights,p)),p)
                assert lhs==independently==rhs,(p,k,weights,lhs,rhs)
                count+=1
                if weights==(4,-2,-1,-1):
                    rows.append(dict(p=p,class8=p%8,k=k,N=N,
                                     source_residue=lhs,earlier_residue=rhs,
                                     events=len(events)))
    # Validate exact rational modular decompositions via CRT without primary helpers.
    crt=[]
    for p,k in ((13,1),(17,1),(29,2),(41,3),(73,4)):
        U=selected(strobe(p,k))
        A,D0=U.numerator,U.denominator
        if D0%p==0:
            D=D0//p
            assert D%p
            a=A*pow(D,-1,p)%p
            b=(A*pow(p,-1,D))%D if D>1 else 0
        else:
            a,D,b=0,D0,A%D0
        assert (U-Fraction(a,p)-Fraction(b,D)).denominator==1
        crt.append(dict(p=p,k=k,p_part=a,cofiber_denominator_digits=len(str(D)),
                        p_conductor_present=D0%p==0))
    print(json.dumps(dict(status="PASS",external_novelty="not assessed",primes=primes,
        independent_equalities=count,main_cases=rows,crt_controls=crt),indent=2))

if __name__=='__main__':main()
