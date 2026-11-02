"""Independent exact algorithms: the four original poles and determinant solve.

Uses no code from finite_history.py and does not share its Gaussian eliminator.
"""
from __future__ import annotations
from fractions import Fraction as F


def exact_source(x:int)->F:
    return F(4,8*x-7)-F(2,8*x-4)-F(1,8*x-3)-F(1,8*x-2)


def determinant(M):
    """Fraction-free Bareiss elimination on an integer matrix."""
    n=len(M)
    a=[list(map(int,row)) for row in M]
    swaps=0
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];swaps+=1
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*v-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):
            a[i][k]=0
        prev=v
    return (-1 if swaps%2 else 1)*a[-1][-1]


def determinant_fraction(M):
    """Compute exact determinant after rowwise denominators cleared."""
    from math import lcm
    a=[];mult=1
    for row in M:
        scale=lcm(*(F(x).denominator for x in row))
        mult*=scale
        a.append([int(F(x)*scale) for x in row])
    return F(determinant(a),mult)


def fit_by_cramer(pairs):
    if len(pairs)!=7:return None
    rows=[];rs=[]
    for x,y in pairs:
        x=F(x);y=F(y)
        rows.append([F(1),x,x*x,-y,-y*x,-y*x*x,-y*x*x*x])
        rs.append(y*x**4)
    D=determinant_fraction(rows)
    if D==0:raise ValueError('singular exact source interpolation')
    result=[]
    for j in range(7):
        m=[row[:] for row in rows]
        for i in range(7):m[i][j]=rs[i]
        result.append(determinant_fraction(m)/D)
    return tuple(result[:3]),tuple(result[3:])+(F(1),)


def independent_future(n:int,J:int)->F:
    """No Wilson curvature, directly convolve four independent poles."""
    return sum((exact_source(n+k)/16**k for k in range(1,J+1)),F(0))


def machin_pi_bounds(terms:int=110)->tuple[F,F]:
    """Independent rigorous rational bounds for mathematical π.

    Machin 16atan(1/5) -4atan(1/239), alternating finite remainders.
    No external π digits, floating arithmetic or original BBP source.
    """
    if terms<1:raise ValueError('positive Taylor horizon required')
    def atan_bounds(q):
        t=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),F(0))
        rem=F(1,(2*terms+1)*q**(2*terms+1))
        return (t-rem,t) if terms%2 else (t,t+rem)
    l5,u5=atan_bounds(5)
    l239,u239=atan_bounds(239)
    return 16*l5-4*u239,16*u5-4*l239
