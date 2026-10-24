"""Exact finite relative-Galois BBP small-ball pair-count checks."""
from fractions import Fraction as F
from math import gcd
import json

def r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def circle(x):
    return x % 1

def dist(x):
    z=circle(x)
    return min(z,1-z)

def order(p):
    x=16%p
    k=1
    while x!=1:
        x=x*16%p
        k+=1
    return k

def source_window(p):
    assert p%8==1
    m=(p-1)//8
    y=F(0)
    values=[]
    for n in range(1,4*m+1):
        y=circle(16*y+r(n))
        if n>=m+1:
            values.append(y)
    local=[F(4*pow(16,t,p)%p,p) for t in range(3*m)]
    complement=[circle(y-u) for y,u in zip(values,local)]
    assert all(gcd(x.denominator,p)==1 for x in complement)
    assert all(circle(u+w)==y for y,u,w in zip(values,local,complement))
    return values,local,complement

def direct_average(p,local,complement,tau):
    delta=len(local)
    hits=[]
    for a in range(1,p):
        z=[circle(a*u+w) for u,w in zip(local,complement)]
        count=sum(dist(x-y)<=tau for x in z for y in z)
        hits.append(count)
    return F(sum(hits),(p-1)*delta*delta),hits

def pair_grid_average(p,local,complement,tau):
    total=0
    equal=0
    for i,u in enumerate(local):
        for j,v in enumerate(local):
            shift=complement[i]-complement[j]
            if u==v:
                equal+=1
                total+=(p-1)*int(dist(shift)<=tau)
            else:
                total+=sum(dist(F(k,p)+shift)<=tau for k in range(1,p))
    delta=len(local)
    assert equal==delta*delta//order(p)
    return F(total,(p-1)*delta*delta)

def universal_bound(p,tau):
    L=order(p)
    grid=F(min(p-1,(2*p*tau).__floor__()+1),p-1)
    return F(1,L)+(1-F(1,L))*grid

def main():
    rows=[]
    for p in [17,41,73,97]:
        y,local,w=source_window(p)
        delta=len(y)
        for M in [4,16,64]:
            tau=F(1,M)
            mean,hits=direct_average(p,local,w,tau)
            grid=pair_grid_average(p,local,w,tau)
            assert mean==grid
            bound=universal_bound(p,tau)
            assert mean<=bound
            rows.append({"p":p,"L":order(p),"Delta":delta,"M":M,
                         "mean_scaled_collision":str(M*mean),
                         "bound_scaled_collision":str(M*bound),
                         "selected_scaled_collision":str(F(M*hits[0],delta*delta)),
                         "selected_at_or_above_mean":F(hits[0],delta*delta)>=mean})
    p=17
    local=[F(4*pow(16,t,p)%p,p) for t in range(6)]
    w=[F(0)]*6
    tau=F(1,100)
    mean,_=direct_average(p,local,w,tau)
    assert mean==F(1,order(p))
    wrong_grid_only=F((2*p*tau).__floor__()+1,p-1)
    assert mean>wrong_grid_only
    receipt={"status":"VERIFIED_FINITE","rows":rows,
             "source_checks":"Exact rational BBP recurrence and p-free complement",
             "independent_identity_checks":len(rows),
             "mutation":{"control":"equal-phase term omitted", "true_mean":str(mean),"false_bound":str(wrong_grid_only),"rejected":True},
             "pi_normality":"OPEN","selected_asymptotic_collision_bound":"UNVERIFIED"}
    print(json.dumps(receipt,indent=2))

if __name__=="__main__":
    main()
