"""Exact finite certificates for BBP full-source delay collisions.
Finite certificates + the separate Hensel/Morse proof imply all-level claims.
No real cancellation or normality claim is made.
"""
from collections import Counter, defaultdict
import json

def A(x): return 120*x*x-89*x+16
def D(x): return (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
def Ap(x): return 240*x-89
def Dp(x): return 2048*x**3-3072*x*x+1424*x-206

def source(x,p,L):
    q=p**L; a=A(x)%q; d=D(x)%q
    assert a%p or d%p, 'bad projective reduction'
    return (0,a*pow(d,-1,q)%q) if d%p else (1,d*pow(a,-1,q)%q)

def derivative(x,p):
    a=A(x)%p; d=D(x)%p
    w=(Ap(x)*d-a*Dp(x))%p
    return w*pow(d*d,-1,p)%p if d else -w*pow(a*a,-1,p)%p

def pair_det(x,y,p):
    return (-derivative(x,p)*derivative(y+1,p)
            +derivative(y,p)*derivative(x+1,p))%p

def collision_groups(p,L,k):
    q=p**L; vals=[source(x,p,L)for x in range(q)]
    groups=defaultdict(list)
    for x in range(q): groups[tuple(vals[(x+j)%q]for j in range(k))].append(x)
    return list(groups.values())

def collisions(groups): return sum(len(g)**2 for g in groups)

def run():
    rows=[]
    for p,Lmax,C1,kcrit in [(7,5,19,2),(11,3,27,1),(241,2,497,1)]:
        critical=[x for x in range(p)if derivative(x,p)==0]
        assert len(critical)==kcrit
        assert all(derivative(x,p) or derivative(x+1,p)for x in range(p))
        groups1=collision_groups(p,1,1)
        assert collisions(groups1)==C1
        # Each critical value has no other residue preimage.
        assert all(next(g for g in groups1 if c in g)==[c]for c in critical)
        # All critical points are simple: numerical mod p finite difference
        # of derivative is NOT used. Calculate W' exactly.
        for c in critical:
            a=A(c)%p;d=D(c)%p
            assert d, 'critical points here use finite chart'
            Dpp=(6144*c*c-6144*c+1424)%p
            Wp=(240*d-a*Dpp)%p
            assert Wp, 'critical point must be simple'
        groups2=collision_groups(p,1,2)
        off=[g for g in groups2 if len(g)>1]
        assert all(len(g)==2 and pair_det(*g,p) for g in off)
        assert len(off)==(0 if p==241 else 1)
        assert all(len(g)==1 for g in collision_groups(p,1,3))
        for L in range(1,Lmax+1):
            q=p**L
            cc=[collisions(collision_groups(p,L,k))for k in [1,2,3]]
            expected=[(C1+kcrit*(p-1)*(L-1))*p**(L-1),q+(0 if p==241 else 2),q]
            assert cc==expected,(p,L,cc,expected)
            rows.append({'p':p,'L':L,'counts':cc,'expected':expected})
        rows.append({'p':p,'critical':critical,'off_diagonal_pair_residues':off,
                     'off_diagonal_pair_determinants':[pair_det(*g,p)for g in off]})

    # Correct full-D control: two delays FAIL injectivity at 7 and 11.
    assert collision_groups(7,1,2).count([2,3])==1
    assert collision_groups(11,1,2).count([2,4])==1
    # Source-only mirror contains pole classes, so no pole is deleted.
    assert source(0,7,1)==source(2,7,1)==source(3,7,1)==source(4,7,1)==(1,0)
    # Mutant claim is rejected at first clean prime, first depth.
    assert collisions(collision_groups(7,1,1)) != 7+6
    return {'status':'exact finite certificates passed','rows':rows}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
