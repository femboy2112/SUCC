"""Independent integer-denominator and inverse-interval oracle.

Does not import crt_probe. Its BBP source is the reduced rational polynomial;
its orbit updates integer numerator/denominator pairs, and no-wrap cylinders
are constructed by all admissible inverse branches. Same-model provenance.
"""
from fractions import Fraction as Q
from math import gcd,isqrt,comb,lcm
from pathlib import Path
import json
import sys


def states(N):
    a,b=0,1; out=[(a,b)]
    for n in range(1,N+1):
        top=120*n*n-89*n+16
        bot=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        a,b=(16*a*bot+top*b)%(b*bot),b*bot
        g=gcd(a,b);a//=g;b//=g
        out.append((a,b))
    return out


def source(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def pair_lag(v,n,h=1):
    a,b=v[n+1];c,d=v[n]
    A=h*(a*d-c*b);B=b*d;g=gcd(A,B)
    return A//g,B//g


def slip(A,B):
    A%=B
    return 20*min(A,B-A)>=B


def egcd(a,b):
    if not b:return 1,0,a
    x,y,g=egcd(b,a%b)
    return y,x-(a//b)*y,g


def split(A,B,p):
    q=B;P=1
    while q%p==0:q//=p;P*=p
    if P==1:return (0,1),(A,B)
    inv,_,g=egcd(q,P);assert g==1
    a=A*inv%P
    numerator=A-a*q;den=B
    g=gcd(numerator,den)
    return (a,P),(numerator//g,den//g)


def inverse_cylinder(A,L,delta=Q(1,20)):
    parts=[(-delta,delta)]
    branches=0
    for j in range(L-2,-1,-1):
        f=source(A+j+2)-source(A+j+1)
        new=[]
        for lo,hi in parts:
            for k in range(-17,18):
                x=max(-delta,(lo+k-f)/16)
                y=min(delta,(hi+k-f)/16)
                if x<=y:new.append((x,y));branches+=1
        parts=new
    return parts,branches


def run():
    sys.set_int_max_str_digits(0)
    root=Path(__file__).resolve().parent
    saved=json.loads((root/'receipts/probe.log').read_text())
    v=states(3000)
    joint_count=0
    for row in saved['joint_windows']:
        A=row['birth'];p=row['p'];h=row['h'];counts=[0,0,0,0]
        for n in range(A,A+row['lags']):
            num,den=pair_lag(v,n,h)
            (pa,pd),(ca,cd)=split(num,den,p)
            fs=slip(num,den);ps=slip(pa,pd);cs=slip(ca,cd)
            counts[0]+=fs;counts[1]+=ps;counts[2]+=cs;counts[3]+=ps and not fs
        assert counts==[row[k] for k in ('full_slips','primary_slips','cofiber_slips','primary_large_full_small')]
        joint_count+=1
    inverse_rows=[]
    for A in (3,11,37):
        for L in (1,2,4,9):
            parts,branches=inverse_cylinder(A,L)
            assert len(parts)==1
            lo,hi=parts[0]
            assert hi-lo<=Q(1,10*16**(L-1))
            for x in (lo,hi,(lo+hi)/2):
                for j in range(L):
                    z=x-x.numerator//x.denominator
                    assert min(z,1-z)<=Q(1,20)
                    x=16*x+source(A+j+2)-source(A+j+1)
            inverse_rows.append({'A':A,'L':L,'intervals':len(parts),'surviving_inverse_branches':branches,'lo':str(lo),'hi':str(hi)})
    shadow_count=0
    for row in saved['dyadic_shadows']:
        s=Q(row['seed']);A=row['A'];L=row['L']
        dist=[]
        for n in range(A,A+L):
            a,b=pair_lag(v,n)
            x=Q(a,b)+15*16**n*s
            f=x-x.numerator//x.denominator
            dist.append(min(f,1-f))
        assert str(max(dist))==row['max_lag_distance']
        assert max(dist)<=Q(row['proved_lag_upper'])<Q(1,20)
        parts,_=inverse_cylinder(A,L)
        assert len(parts)==1
        assert str(parts[0][1]-parts[0][0])==row['cylinder_width']
        shadow_count+=1
    prime_valuations=0
    for m in range(80):
        for s in range(1,24):
            product=comb(m+s,s)*lcm(*range(1,s+1))
            for p in range(2,m+s+1):
                if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
                def vp(n):
                    e=0
                    while n%p==0:n//=p;e+=1
                    return e
                assert vp(product)>=max(vp(n) for n in range(m+1,m+s+1))
                prime_valuations+=1
    result={'authority':'separate implementation, shared model; finite cross-check only',
        'joint_rows_checked':joint_count,'shadows_checked':shadow_count,
        'inverse_cylinders':inverse_rows,'short_interval_prime_valuation_checks':prime_valuations,
        'source':'combined polynomial, integer numerator/denominator orbit; no crt_probe imports'}
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
