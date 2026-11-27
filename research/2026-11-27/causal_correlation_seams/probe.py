"""Exact standalone controls for causal correlation seams; no floating phase arithmetic."""
from fractions import Fraction as Q
from itertools import product
from math import comb, prod
import json


def forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def history(seed, r, b=16):
    out = [Q(seed)]
    for v in r:
        out.append(b*out[-1]+v)
    return tuple(out)


def ports(z, b=16):
    return tuple((z[j]-b*z[j-1]) % 1 for j in range(1,len(z)))


def reconstruct(anchor, w, b=16):
    return tuple(v % 1 for v in history(anchor,w,b))


def decompose(k, b=16):
    """k = charge*e0 + sum a_j(e_j-b*e_{j-1})."""
    a = [0]*(len(k)-1)
    carry = 0
    for j in range(len(k)-1,0,-1):
        carry = k[j]+b*carry
        a[j-1] = carry
    return k[0]+b*carry, tuple(a)


def expand(q, a, b=16):
    k = [q]+[0]*len(a)
    for j,v in enumerate(a,1):
        k[j-1] -= b*v
        k[j] += v
    return tuple(k)


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),Q())


def mean(x):
    return sum(x,Q())/len(x)


def conditional_mean(x, labels):
    return tuple(mean([v for v,z in zip(x,labels) if z==l]) for l in labels)


def poly_substitution_rank(m,K):
    # Number of distinct nonzero monomials under t -> t^m mod t^(K+1).
    return len({m*j for j in range(K+1) if m*j<=K})


def run():
    counts = dict(character=0, gauge=0, source=0, gram=0, jets=0, mask=0, intervention=0)
    for b in (2,3,16):
        for n in range(1,5):
            for k in product(range(-2,3),repeat=n+1):
                q,a = decompose(k,b)
                assert q==sum(v*b**j for j,v in enumerate(k))
                assert expand(q,a,b)==k
                z=tuple(Q(j*j+1,37)%1 for j in range(n+1))
                assert (dot(k,z)-q*z[0]-dot(a,ports(z,b)))%1==0
                counts['character']+=1
            for x in range(17):
                z=tuple(Q(x+j*j,17)%1 for j in range(n+1))
                w=ports(z,b)
                assert reconstruct(z[0],w,b)==z
                for p in range(17):
                    v=tuple((u+Q(p*b**j,17))%1 for j,u in enumerate(z))
                    assert ports(v,b)==w
                    assert reconstruct(v[0],w,b)==v
                    counts['gauge']+=1
    r=tuple(forcing(n) for n in range(1,33))
    assert all(v>0 for v in r)
    assert all(r[j]>r[j+1] for j in range(len(r)-1))
    for seed in (Q(0), Q(1,16), Q(-4,7), Q(123,11)):
        u=history(seed,r)
        assert ports(u)==tuple(v%1 for v in r)
        assert tuple(u[j]-16*u[j-1] for j in range(1,len(u)))==r
        assert all(v%1==0 for v in ports(tuple(16**j*seed for j in range(33))))
        counts['source']+=32
    # Native forcing source with explicitly counterfactual multiplicative probes.
    for n in range(1,17):
        base=history(0,r[:n])
        for j in range(n+1):
            eps=Q(1,1009)
            rr=list(r[:n]); seed=Q()
            if j: rr[j-1]*=1+eps
            else: seed=eps
            changed=history(seed,rr)
            d=tuple((a-b)/eps for a,b in zip(changed,base))
            expected=tuple(Q(16**i) if j==0 else (16**(i-j)*r[j-1] if i>=j else Q()) for i in range(n+1))
            assert d==expected
            assert tuple(d[i]-16*d[i-1] for i in range(1,n+1))==tuple(r[i-1] if i==j else Q() for i in range(1,n+1))
            counts['intervention']+=1
    labels=(0,0,1,1)
    for x in product(range(-1,2),repeat=4):
        for y in product(range(-1,2),repeat=4):
            px,py=conditional_mean(x,labels),conditional_mean(y,labels)
            dx=tuple(a-b for a,b in zip(x,px)); dy=tuple(a-b for a,b in zip(y,py))
            assert dot(x,y)==dot(px,py)+dot(dx,dy)
            assert dot(px,dy)==dot(dx,py)==0
            counts['gram']+=1
    # Exact truncated polynomial rank and composition order; m odd => real bijection.
    for m,n,K in product((1,3,5,7),(1,3,5),range(1,32)):
        assert poly_substitution_rank(m,K)==K//m+1
        assert poly_substitution_rank(m*n,K)==K//(m*n)+1
        for a,b in ((2,3),(-2,5),(Q(1,3),Q(2,5))):
            assert b*(a*Q(2)**m)**n==(b*a**n)*Q(2)**(m*n)
            counts['jets']+=1
    # Marginal and all proper-subset indistinguishability; top parity separates.
    for n in range(2,8):
        laws=[tuple(x for x in product((-1,1),repeat=n) if prod(x)==s) for s in (-1,1)]
        for mask in range(1<<n):
            sums=[mean([prod(x[j] for j in range(n) if mask>>j&1) for x in law]) for law in laws]
            assert sums==([-1,1] if mask==(1<<n)-1 else ([1,1] if mask==0 else [0,0]))
            counts['mask']+=1
    # Factorial blindness, Hasse coefficient still 1 in characteristic p.
    for p in (2,3,5,7,11):
        assert prod(range(1,p+1))%p==0 and comb(p,p)==1
    return {'status':'PASS', 'counts':counts, 'total_counted':sum(counts.values()),
            'forcing_first':str(r[0]), 'forcing_second':str(r[1]),
            'scope':'standalone finite exact controls; not full repository validation or proof by enumeration'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
