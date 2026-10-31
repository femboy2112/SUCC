"""Exact positive BBP period fibers. Controls, never replacement BBP source.

Polynomial coefficients are ascending. All construction/proofs use rational
arithmetic; the separate oracle uses SymPy integration and its linear solver.
"""
from fractions import Fraction as F
from math import comb, factorial
import json

Q = (F(4), F(0), F(0), F(-2), F(-1), F(-1))

def trim(p):
    p = list(map(F, p))
    while len(p)>1 and not p[-1]: p.pop()
    return tuple(p)

def add(p,q):
    return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q)))])

def scale(p,c): return trim([c*x for x in p])

def mul(p,q):
    v=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): v[i+j]+=a*b
    return trim(v)

def derivative(p): return trim([i*p[i] for i in range(1,len(p))] or [0])
def at(p,x):
    y=F(0)
    for a in reversed(p): y=y*x+a
    return y
def integral(p,power=0): return sum((c/F(i+power+1) for i,c in enumerate(p)),F(0))
def one_minus(k): return tuple(F((-1)**j*comb(k,j)) for j in range(k+1))
def beta(a,b): return F(factorial(b-1),prod(range(a,a+b)))
def prod(v):
    z=1
    for a in v:z*=a
    return z

def solve(matrix,rhs):
    a=[list(map(F,row))+[F(b)] for row,b in zip(matrix,rhs)]
    n=len(a)
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        t=a[j][j];a[j]=[x/t for x in a[j]]
        for i in range(n):
            if i!=j:
                t=a[i][j];a[i]=[x-t*y for x,y in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

def orthogonal(m,N):
    """Monic p_N(x), x=z^8, weight z^8(1-z)^(m+1) dz."""
    if m<2 or N<0:raise ValueError('m>=2 and N>=0 required')
    if not N:return (F(1),)
    moment=lambda j:beta(8*(j+1)+1,m+2)
    return solve([[moment(i+j) for j in range(N)] for i in range(N)],
                 [-moment(i+N) for i in range(N)])+(F(1),)

def construction(m,N):
    p=orthogonal(m,N)
    lifted=[F(0)]*(8*N+1)
    for j,c in enumerate(p):lifted[8*j]=c
    R=mul((0,1),mul(one_minus(m+1),lifted))
    Rp=derivative(R)
    # R'=(1-z)^m H. Compute H directly to avoid polynomial division.
    H=add(mul((1,-(m+2)),lifted),mul((0,1,-1),derivative(lifted)))
    assert mul(one_minus(m),H)==Rp
    B=sum(map(abs,H));eps=F(1,8*B)
    D=mul((16,0,0,0,0,0,0,0,-1),Rp)
    source=add(Q,scale(D,eps))
    return {'m':m,'N':N,'p':p,'R':R,'H':H,'D':D,'B':B,
            'epsilon':eps,'source':source}

def forcing(poly,n):
    if n<1:raise ValueError('n>=1')
    return integral(poly,8*n-8)

def orbit(poly,count):
    out=[F(0)]
    for n in range(1,count+1):out.append(16*out[-1]+forcing(poly,n))
    return out

def delta_orbit(c,n):
    if not n:return F(0)
    return c['epsilon']*8*n*integral(c['R'],8*n-1)

def certificate(m,N):
    c=construction(m,N);limit=N+13
    original=orbit(Q,limit);mutant=orbit(c['source'],limit)
    assert all(mutant[n]-original[n]==delta_orbit(c,n) for n in range(limit+1))
    assert all(forcing(c['D'],n)==0 for n in range(1,N+1))
    assert integral(derivative(c['R']))==0
    assert at(c['R'],F(0))==at(c['R'],F(1))==0
    assert delta_orbit(c,N+1)>0
    norm=sum((a*b*beta(8*(i+j+1)+1,m+2)
              for i,a in enumerate(c['p']) for j,b in enumerate(c['p'])),F(0))
    assert delta_orbit(c,N+1)==c['epsilon']*8*(N+1)*norm
    derivatives=[];v=c['D']
    for j in range(m):
        derivatives.append(at(v,F(1)));v=derivative(v)
    assert not any(derivatives)
    # Global proof: |epsilon D/Q| <= 4 epsilon ||H||_1 = 1/2.
    positive_bound=4*c['epsilon']*c['B'];assert positive_bound==F(1,2)
    pnorm=sum(map(abs,c['p']))
    for n in range(1,limit+1):
        assert abs(delta_orbit(c,n)) <= c['epsilon']*pnorm*F(factorial(m+1),(8*n)**(m+1))
    return {'m':m,'N':N,'p':list(map(str,c['p'])),
        'epsilon':str(c['epsilon']),'degree':len(c['source'])-1,
        'relative_positivity_bound':str(positive_bound),
        'prefix_forcings_equal':N,'first_orbit_difference':str(delta_orbit(c,N+1)),
        'positive_norm_square':str(norm),'endpoint_derivatives':list(map(str,derivatives)),
        'period_difference':'0 (integral of R prime)',
        'orbit_replays':limit+1,'source_coefficients':list(map(str,c['source']))}

def main():
    planned=[(m,N) for m in (2,4,7) for N in (0,1,3,5)]
    holdouts=[(3,2),(6,4),(9,6)]
    # Removing R(1)=0 gives nonzero exact period shift epsilon, falsifying the claim.
    assert integral(derivative((0,1)))==1
    print(json.dumps({'planned':[certificate(*x) for x in planned],
                      'fresh_holdouts':[certificate(*x) for x in holdouts],
                      'negative_control_period_shift':'1 before epsilon scaling'},indent=2))

if __name__=='__main__':main()
