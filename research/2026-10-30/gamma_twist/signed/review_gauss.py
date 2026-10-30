"""Scoped adversarial review of GG03/04/06/07, independent of gauss_exact."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd,lcm
import hashlib
import json
import sympy as s


def main():
    values=[F()]
    for n in range(1,81):
        r=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        values.append((16*values[-1]+r)%1)
    checks=0
    for n,u in enumerate(values[1:],1):
        assert u.denominator%2
        for p in (3,5,7,13,19,73,257):
            P=1;D=u.denominator
            while D%p==0:P*=p;D//=p
            assert P<=8*n
            a=u.numerator*pow(D,-1,P)%P if P>1 else 0
            v=(u-F(a,P))%1
            assert v.denominator==D
            for h in (1,3,7):
                order=(h*v).denominator
                assert order==D//gcd(D,h)
                assert order*h>=D
                checks+=1
    degree_rows=[]
    for M in (1,3,5,13,3*5*13,3*5*7*13):
        for ell in (3,5,7,11,13):
            for a in (2,3):
                degree=int(s.totient(lcm(8*M,ell**a))/s.totient(8*M))
                assert degree>=ell**(a-1)>1
                degree_rows.append([M,ell,a,degree])
    x=s.Symbol('x')
    trace_rows=[]
    for D in (3,5,9,15,21,25,35,45,63,105,315):
        P=s.Poly(s.cyclotomic_poly(D,x),x)
        primitive=s.Poly.from_dict({(a,):1 for a in range(D) if gcd(a,D)==1},x)
        remainder=primitive.rem(P)
        assert remainder==s.Poly(s.mobius(D),x)
        trace_rows.append([D,int(s.mobius(D)),int(s.totient(D))])
    paper=Path(__file__).resolve().parent.parent/'gauss'/'GAUSS_UNIT_BLINDNESS.md'
    print(json.dumps({'status':'PASS','reviewed_claims':['GG03','GG04','GG06','GG07'],
        'paper_sha256':hashlib.sha256(paper.read_bytes()).hexdigest(),
        'cofiber_and_fixed_h_checks':checks,'degree_checks':len(degree_rows),
        'degree_rows':degree_rows,'Ramanujan_trace_rows':trace_rows,
        'reasoner_independence':'separate agent, same model family and shared source context',
        'scope':'finite checks plus written proof review; no independent normality authority'},indent=2))


if __name__=='__main__':main()
