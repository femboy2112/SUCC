"""Separate common-denominator and high-precision nonlinear oracle.

Imports neither signed_transport nor the inherited finite-circle instrument.
The mpmath comparisons are cross-checks, not the authority for enclosures.
"""
from fractions import Fraction
from math import gcd,lcm
from pathlib import Path
import json
import mpmath as mp
import sympy as sy

mp.mp.dps=100
R=Fraction


def state_oracle(end):
    num,den=0,1
    values=[R()]
    for n in range(1,end+1):
        poles=[8*n-7,8*n-4,8*n-3,8*n-2]
        d=lcm(*poles)
        a=sum(c*(d//q) for c,q in zip((4,-2,-1,-1),poles))
        num,den=16*num*d+a*den,den*d
        g=gcd(num,den);num//=g;den//=g
        # Reducing modulo one here is a circle recurrence; source integers retained.
        num%=den
        values.append(R(num,den))
    return values


def forcing(n):
    return R(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def real(q):
    q=R(q)
    return mp.mpf(q.numerator)/q.denominator


def contains(pair,value):
    a,b=map(real,pair)
    assert a<=value<=b,(a,value,b)


def exact_tail_difference(n):
    # Separate deeper truncation; geometric remainder is far below oracle tolerance.
    return sum((forcing(n+j)-forcing(n+j+1))/16**j for j in range(1,81))


def main():
    probe=json.loads((Path(__file__).parent/'probe_receipt.json').read_text())
    values=state_oracle(460)
    count=0
    for row in probe['SC06_rows']:
        b,L,h=row['birth'],row['L'],row['h']
        energy=sum(1-mp.cos(2*mp.pi*real(h*(values[n+1]-values[n])))
                   for n in range(b,b+L-1))/(L-1)
        contains(row['energy'],energy)
        count+=1
    minima=[]
    for row in probe['minimization_certificates']:
        A,L,h=row['A'],row['L'],row['h']
        d=[h*real(exact_tail_difference(n)) for n in range(A,A+L)]
        a=[mp.mpf(16)**(j-L+1) for j in range(L)]
        def derivative(t):
            return sum(x*mp.sin(2*mp.pi*(v+x*t)) for x,v in zip(a,d))
        lo,hi=-2*d[-1],mp.mpf(0)
        assert derivative(lo)<0<derivative(hi)
        for _ in range(210):
            mid=(lo+hi)/2
            if derivative(mid)>0:hi=mid
            else:lo=mid
        tau=(lo+hi)/2
        minimum=sum(1-mp.cos(2*mp.pi*(v+x*tau)) for x,v in zip(a,d))/L
        coherent=sum(1-mp.cos(2*mp.pi*v) for v in d)/L
        contains(row['mean_minimum'],minimum)
        contains(row['mean_coherent'],coherent)
        minima.append({'A':A,'L':L,'h':h,'minimum':mp.nstr(minimum,35),
                       'coherent':mp.nstr(coherent,35),
                       'method':'210-step derivative bisection, 100 decimal digits'})
    x=sy.symbols('x')
    source=(120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))
    leading=sy.limit(x*x*source,x,sy.oo)
    difference=sy.limit(x**3*(source-source.subs(x,x+1)),x,sy.oo)
    assert leading==sy.Rational(15,64)
    assert difference==sy.Rational(15,32)
    # Geometric future resolvent has total weight 1/15.
    assert difference/sy.Integer(15)==sy.Rational(1,32)
    grid_path=Path(__file__).parent/'approximate_grid_receipt-corrected.json'
    grid_checks=0
    if grid_path.exists():
        grid=json.loads(grid_path.read_text())
        for row in grid['BBP_cases']:
            p,b,L,q=row['p'],row['birth'],row['L'],row['best_q']
            turns=[(q*values[n])%1 for n in range(b,b+L)]
            # Independent all-cuts shortest-arc computation, without sorted gaps.
            width=min(max((t-origin)%1 for t in turns) for origin in turns)
            radius=width/(2*q)
            assert radius>R(1,p*p)
            contains(row['best_radius'],real(radius))
            grid_checks+=1
    print(json.dumps({'status':'PASS','SC06_interval_crosschecks':count,
        'source_states_independently_rebuilt':461,'minimum_interval_crosschecks':len(minima),
        'r_leading':str(leading),'r_difference_leading':str(difference),
        'tail_difference_leading':'1/32','minimum_rows':minima,'grid_best_radius_crosschecks':grid_checks,
        'authority':'independent implementation and representation; shared source/model; mpmath numerical cross-check only'},indent=2))


if __name__=='__main__':main()
