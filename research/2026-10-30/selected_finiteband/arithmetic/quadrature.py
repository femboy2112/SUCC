"""Positive rational source mutants; exact certification, LP discovery only."""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

COEFFS=(4,-2,-1,-1)
OFFSETS=(1,4,5,6)

def source(n, coeffs=COEFFS):
    return sum((F(c,8*n-8+d) for c,d in zip(coeffs,OFFSETS)),F())

def prefix(N, coeffs=COEFFS, seed=F()):
    u=seed; out=[u]
    for n in range(1,N+1):
        u=16*u+source(n,coeffs); out.append(u)
    return out

def geometric_moment(k):
    # Sum_{j>=1} j^k /16^j, from Eulerian polynomial recurrence.
    coeff=[0,1]  # q/(1-q), k=0
    for d in range(k):
        new=[0]*(len(coeff)+1)
        # q[(1-q)P' +(d+1)P] /(1-q)^(d+2)
        for i,c in enumerate(coeff):
            if i: new[i]+=i*c; new[i+1]-=i*c
            new[i+1]+=(d+1)*c
        coeff=new
    q=F(1,16)
    return sum((F(c)*q**i for i,c in enumerate(coeff)),F())/(1-q)**(k+1)

def green_moment(k):
    # T_n=integral (n+b)^-2 dnu; b=j-7/8+t/8.
    total=F()
    for l in range(k+1):
        offset_integral=sum((F(w)*(F(d-7)**(l+1)-F(-7)**(l+1))/((l+1)*8**l)
                             for d,w in ((3,2),(4,1),(5,1))),F())
        total+=F(comb(k,l),64)*geometric_moment(k-l)*offset_integral
    return total

def row(b,M,J):
    return [16/(F(n-1)+b)**2-1/(F(n)+b)**2 for n in range(1,M+1)] + [b**k for k in range(J+1)]

def target(M,J):
    return [source(n) for n in range(1,M+1)]+[green_moment(k) for k in range(J+1)]

def rational_solve(matrix, rhs):
    n=len(rhs); a=[list(map(F,r))+[F(y)] for r,y in zip(matrix,rhs)]
    for col in range(n):
        piv=next((i for i in range(col,n) if a[i][col]),None)
        if piv is None: raise ValueError('singular')
        a[col],a[piv]=a[piv],a[col]
        q=a[col][col]; a[col]=[v/q for v in a[col]]
        for i in range(n):
            if i!=col:
                q=a[i][col]; a[i]=[x-q*y for x,y in zip(a[i],a[col])]
    return [r[-1] for r in a]

def certify(M,J,nodes,weights):
    assert len(nodes)==len(weights)
    assert all(b>0 and w>0 for b,w in zip(nodes,weights))
    got=[sum((w*v for w,v in zip(weights,vals)),F()) for vals in zip(*(row(b,M,J) for b in nodes))]
    assert got==target(M,J)
    return True

def discover(M,J,step=32,blocks=5):
    import numpy as np
    from scipy.optimize import linprog
    nodes=[F(j,step) for j in range(1,blocks*step+1)
           if any(F(t)-F(7,8)<=F(j,step)<=F(t)-F(1,4) for t in range(1,blocks+1))]
    d=M+J+1
    columns=[row(b,M,J) for b in nodes]; rhs=target(M,J)
    mat=np.array([[float(c[i]/rhs[i]) for c in columns] for i in range(d)])
    attempts=[]
    for trial in range(40):
        rng=np.random.default_rng(20261030+trial)
        cost=rng.uniform(-1,1,len(nodes))
        sol=linprog(cost,A_eq=mat,b_eq=np.ones(d),bounds=(0,None),method='highs',
                    options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        support=[] if not sol.success else [i for i,w in enumerate(sol.x) if w>1e-12]
        rec={'trial':trial,'lp_success':bool(sol.success),'support_size':len(support)}
        attempts.append(rec)
        if len(support)!=d: continue
        bs=[nodes[i] for i in support]
        try: ws=rational_solve(list(map(list,zip(*(row(b,M,J) for b in bs)))),rhs)
        except ValueError: continue
        rec['exact_positive']=all(w>0 for w in ws)
        if all(w>0 for w in ws):
            certify(M,J,bs,ws)
            return {'M':M,'J':J,'nodes':list(map(str,bs)),'weights':list(map(str,ws)),
                    'completed_constant':str(16*sum((w/b**2 for b,w in zip(bs,ws)),F())),
                    'attempts':attempts,'status':'EXACT_POSITIVE_CERTIFICATE'}
    raise RuntimeError((M,J,attempts))

def mutant_g(n,nodes,weights):
    return sum((w/(F(n)+b)**2 for b,w in zip(nodes,weights)),F())

def mutant_source(n,nodes,weights):
    return 16*mutant_g(n-1,nodes,weights)-mutant_g(n,nodes,weights)

def primary(x,p):
    d=x.denominator; P=1
    while d%p==0: d//=p; P*=p
    return F((x.numerator*pow(d,-1,P))%P,P) if P>1 else F()

def main():
    rows=[]
    for M,J in ((2,1),(3,2),(4,1),(4,3)):
        rows.append(discover(M,J))
    print(json.dumps({'status':'PASS','rows':rows,'moments':list(map(str,(green_moment(k) for k in range(7))))},indent=2))

if __name__=='__main__':main()
