"""Independent exact rational source/gauge/shadow checks.

This script doesn't import observational_succ.seed_source_rank or the BBP code.
Its finite computations corroborate formulas; do not prove Wall's theorem or
pi normality, or source-moduli Baker rigidity.
"""
from fractions import Fraction as F


def native(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def state(g,s,n):
    v=s
    for j in range(1,n+1):
        v=16*v+sum(F(a,8*j-7+k) for k,a in enumerate(g))
    return v


def h_at(h,n):
    return sum(F(a,8*n+1+k) for k,a in enumerate(h))


g=(4,0,0,-2,-1,-1)
checks=0
for h in ((1,), (0,1), (F(1,3),F(-2,5),1)):
    gp=[F(0)]*max(len(g),len(h)+8)
    for i,a in enumerate(g): gp[i]+=a
    for i,a in enumerate(h): gp[i]-=16*a;gp[i+8]+=a
    for n in range(35):
        assert state(gp,h_at(h,0),n)-state(g,F(0),n)==h_at(h,n)
        checks+=1
for N in (4,8,16,32,64):
    pN=sum((native(j)/16**j for j in range(1,N+1)),F(0))
    for n in range(N+1):
        left=state(g,-pN,n)
        right=-sum((native(j)/16**(j-n) for j in range(n+1,N+1)),F(0))
        assert left==right
        assert -native(n+1)/15<left<=0
        checks+=1
# Independent source-integrand factorization and null-source residue signs.
# Polynomial products as coefficient arrays.
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)
K=mul((2,0,1),(2,2,1))
assert mul((1,-1),K)==g
assert mul((2,-4,1),K)==(8,-8,-4,-8,-2,-2,1)  # trailing zero is cosmetic
assert sum(g)==0
assert sum((8,-8,-4,-8,-2,-2,1,0))==-15
checks+=4
print(f"INDEPENDENT_ORACLE_PASS exact rational checks={checks}")
