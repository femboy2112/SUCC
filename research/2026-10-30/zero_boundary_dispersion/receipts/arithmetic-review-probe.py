"""Complementary arithmetic check; imports none of the CRT implementation."""
from fractions import Fraction as Q
from math import comb, gcd, lcm, isqrt
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent
BASE=HERE.parent


def r(k):
    return Q(120*k*k-89*k+16,(2*k-1)*(4*k-1)*(8*k-7)*(8*k-3))


def prefix(n):
    return sum((16**(n-k)*r(k) for k in range(1,n+1)),Q())


def run():
    interval_cases=0
    for m in list(range(61))+[997,10**6]:
        for length in range(1,21):
            a=lcm(*range(m+1,m+length+1))
            b=comb(m+length,length)*lcm(*range(1,length+1))
            assert b%a==0
            interval_cases+=1
    filters=[]
    for n in (19,47,89,173):
        for d in sorted(set((1,4,isqrt(n),max(1,n//10)))):
            for c in ([-1]+[0]*(d-1)+[1],
                      [(-1)**j*(j+2) for j in range(d+1)]):
                values=[prefix(n+j) for j in range(d+1)]
                M=sum(c[j]*16**j for j in range(d+1))
                assert M!=0
                R=sum((sum(c[j]*16**(j-t) for j in range(t,d+1))*r(n+t)
                       for t in range(1,d+1)),Q())
                actual=sum((c[j]*values[j] for j in range(d+1)),Q())
                assert actual==M*values[0]+R
                D=values[0].denominator
                den=actual.denominator
                B=lcm(*(r(n+t).denominator for t in range(1,d+1)))
                assert (D*B)%den==0
                assert (den*B)%(D//gcd(D,abs(M)))==0
                assert comb(8*n+8*d,8*d)*lcm(*range(1,8*d+1))%B==0
                filters.append({'n':n,'degree':d,'denominator_bits':den.bit_length(),
                                'sandwich_and_identity':True})
    field_cases=0
    for p in (3,5,7,13,19):
        for f in range(1,5):
            conductor=p*(p**f-1)
            for D in range(1,122,2):
                if gcd(D,p)!=1: continue
                contained=s.totient(lcm(D,conductor))==s.totient(conductor)
                assert contained==((p**f-1)%D==0)
                field_cases+=1
    recorded=json.loads((BASE/'crt/receipts/field-polynomial.log').read_text())
    orders=[]
    for row in recorded['character_field']:
        p=row['p'];n=row['n'];D=prefix(n).denominator
        while D%p==0:D//=p
        assert str(D)==row['cofiber_denominator']
        f=int(s.n_order(p,D)) if D>1 else 1
        assert str(f)==row['minimal_extension_degree']
        orders.append({'p':p,'n':n,'order':str(f),'bits':f.bit_length()})
    x=s.symbols('x')
    supports=([2,0,-3,1],[0,1,0,-1],[3])
    symbolic=[]
    for co in supports:
        t=sum(c*(120*(x+j+1)**2-89*(x+j+1)+16)/
                ((2*(x+j+1)-1)*(4*(x+j+1)-1)*(8*(x+j+1)-7)*(8*(x+j+1)-3))
              for j,c in enumerate(co) if c)
        top,bot=s.fraction(s.cancel(t))
        expected=4*sum(c!=0 for c in co)
        assert s.degree(bot,x)==expected
        assert s.gcd(top,bot)==1
        symbolic.append({'quotient_coefficients':co,'denominator_degree':expected})
    return {'status':'PASS','independence':'separate implementation; same model/context',
            'interval_lcm_cases':interval_cases,'moving_filter_cases':filters,
            'cyclotomic_degree_cases':field_cases,'independent_orders':orders,
            'distinct_annihilator_symbolic_cases':symbolic}


if __name__=='__main__': print(json.dumps(run(),indent=2))
