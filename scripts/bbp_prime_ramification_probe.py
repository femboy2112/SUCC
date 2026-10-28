"""Small standalone exact Gaussian/ramification BBP source probe.

No production source changes. No numerical π approximation or normality claim.
The large local finite research probe is separate; this tests source integers.
"""
from collections import Counter
from fractions import Fraction as Q

def A(n): return 120*n*n-89*n+16
POLES=((2,-1),(4,-1),(8,-7),(8,-3))
def D(n):
    z=1
    for a,b in POLES: z*=a*n+b
    return z
def r(n): return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
def Res(a,b): return 120*b*b+89*a*b+16*a*a
def pair(L,M): return L[0]*M[1]-M[0]*L[1]
def coll(p,L):
    q=p**L
    c=Counter(A(n)%q for n in range(q))
    return sum(v*v for v in c.values())
def expected(p,L):
    return p**L if p in (2,3,5) else p**L+L*(p-1)*p**(L-1)
def main():
    assert all(r(n)==Q(A(n),D(n)) for n in range(1,110))
    rr=[Res(*factor) for factor in POLES]
    assert rr==[6,20,1920,-32],rr
    prod=1
    for v in rr:prod*=v
    assert prod==-2**15*3**2*5**2
    disc=1
    for i,left in enumerate(POLES):
        for right in POLES[i+1:]:disc*=pair(left,right)**2
    assert disc==2**24*3**2*5**2
    assert 89**2-4*120*16==241
    lam=complex(1,1)
    assert lam**8==16
    for p,L in [(2,4),(3,3),(5,3),(7,1),(7,2),(7,3),(11,2),(13,2),(241,1)]:
        observed=coll(p,L)
        assert observed==expected(p,L),(p,L,observed,expected(p,L))
        print('collision p,L,count:',p,L,observed)
    assert all(A(n)%7==((n+1)**2+1)%7 and A(n)%7!=0 for n in range(7))
    assert D(0)%7==0 and D(5)%7==2
    # Source mutation immediately introduces another pole resultant prime.
    assert Res(8,-5)==464 != Res(8,-7)
    assert {n for n in range(7) if (120*n*n-88*n+16)%7==0}=={5,6}
    # Exact signed mirror energy for four cyclotomic phases.
    for p in (7,11):
        z=[(1+0j,1j,-1+0j,-1j)[(n*n+2*n+3*(n//p))%4] for n in range(5*p)]
        Z=[sum((z[n] for n in range(5*p) if n%p==j),0j) for j in range(p)]
        YA=[sum((Z[j] for j in range(p) if A(j)%p==a),0j) for a in range(p)]
        c=89*pow(120,-1,p)%p
        b=c*pow(2,-1,p)%p
        lhs=sum((t*t.conjugate() for t in YA),0j)
        rhs=sum((t*t.conjugate() for t in Z),0j)
        rhs+=sum((Z[j]*Z[(c-j)%p].conjugate() for j in range(p)),0j)
        rhs-=Z[b]*Z[b].conjugate()
        assert lhs==rhs and lhs.imag==0 and lhs.real>=0
    print('EXACT SOURCE GAUSSIAN/RAMIFICATION PROBE PASSED; PI NORMALITY OPEN')

if __name__=="__main__": main()
