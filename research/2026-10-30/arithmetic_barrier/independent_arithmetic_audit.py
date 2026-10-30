"""Root's separate exact oracle using the combined original rational forcing.

No campaign arithmetic, transfer or parent modules are imported. This audits
finite instances, not the universal proof. Cases declared here are holdouts
relative to the initial parent range.
"""
from fractions import Fraction as F
from math import isqrt, prod
import json


def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))


def r(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def prefix(end):
    u=F()
    values=[u]
    for n in range(1,end+1):
        u=16*u+r(n)
        values.append(u)
    return values


def reduce(q,m):
    return q.numerator*pow(q.denominator,-1,m)%m


def vp(q,p):
    n,d=q.numerator,q.denominator
    if n==0:
        raise ValueError('infinite valuation')
    value=0
    while n%p==0:
        n//=p
        value+=1
    while d%p==0:
        d//=p
        value-=1
    return value


def main():
    cases=[(p,a,k) for p in (7,11,13,17,19,23,29,31,43,47,59,67)
           for a in (1,2) for k in (1,2,3)
           if p>8*k-(2 if p**a%4==1 else 1)
           and p**a*(8*k-1)//8<2500]
    cases += [(11,3,1),(13,3,1)]
    clocks=[]
    for p,a,k in cases:
        q=p**a
        L=8*k-(2 if q%4==1 else 1)
        assert p > L, 'declared p-integrality domain required'
        clocks.append((q*L+8-(q*L)%8)//8)
    values=prefix(max(clocks))
    rows=[]
    weights={1:((1,4,5,6),(4,-2,-1,-1)),5:((1,4,5,6),(4,-2,-1,-1)),
             3:((2,3,4,7),(8,4,4,-1)),7:((2,3,4,7),(-32,-16,-16,4))}
    for (p,a,k),N in zip(cases,clocks):
        q=p**a
        offsets,cs=weights[q%8]
        v=sum((F(c*16**(k-j),8*(j-1)+d)
               for j in range(1,k+1) for d,c in zip(offsets,cs)),F())
        lhs=reduce(q*values[N],p)
        assert lhs==reduce(v,p)
        # Direct original-source regular-layer expansion; independent closed r
        # supplies the left operand, four signed poles supply this right operand.
        correction=F()
        for n in range(1,N+1):
            for d,c in ((1,4),(4,-2),(5,-1),(6,-1)):
                den=8*(n-1)+d
                exponent=0
                while den%p==0:
                    den//=p
                    exponent+=1
                if exponent==a-1:
                    correction+=F(c*16**(N-n),den)
        chi=1 if p%8 in (1,7) else -1
        theta=(chi*2**((p-1)//2)-1)//p
        L=8*k-(2 if q%4==1 else 1)
        derivative=L*v-sum(cs)*F(16**k-1,15)
        predicted=v+p*(theta*derivative+correction)
        assert reduce(q*values[N]-predicted,p*p)==0
        rows.append({'p':p,'a':a,'k':k,'N':N,'residue':lhs,'lift_mod_p2':reduce(q*values[N],p*p)})
    births=[]
    for p in (3,5,7,11,13,19):
        for a in range(1,5):
            q=p**a
            n=(q+7)//8 if q%8==1 else (q+3)//8 if q%8==5 else (q+1)//4
            if n>max(clocks):
                continue
            assert vp(values[n],p)==-a
            births.append({'p':p,'a':a,'n':n,'valuation':-a})
    grids=[]
    for n in (3,7,13,37,101,257,509):
        ps=[p for p in range(7,8*n-6) if prime(p) and
            ((p%4==1 and 2*n+2<p<=8*n-7) or
             (p%4==3 and 8*n+8<3*p and p<=4*n-1))]
        diff=values[n+1]-values[n]
        assert all(vp(diff,p)==-1 for p in ps)
        G=prod(ps)
        assert diff.denominator%G==0
        grids.append({'n':n,'primes':len(ps),'product_bits':G.bit_length(),
                      'adjacent_difference_denominator_bits':diff.denominator.bit_length()})
    assert [vp(values[n],19) for n in range(10,17)] == [0]*7
    assert vp(values[17],19)==-1
    assert values[274].denominator%73!=0
    assert reduce(13*values[10]-values[1],169)==65
    print(json.dumps({'status':'PASS_FINITE_EXACT','source':'combined original r(n), zero seed',
        'imports_from_other_campaign_implementations':False,'clock_and_lift_cases':len(rows),
        'rows':rows,'births':births,'translated_grid_cases':grids,
        'negative_controls':['p13 naive lift discrepancy65','p19 conductor loss10..16 and return17','p73k4 cancellation'],
        'pi_normality_proved':False},indent=2))


if __name__=='__main__':
    main()
