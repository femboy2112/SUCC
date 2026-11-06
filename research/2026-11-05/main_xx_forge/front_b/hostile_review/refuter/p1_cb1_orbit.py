# CB-1 exact check on actual orbits for several rational seeds, ALL (m,k) with S_d(n)<1 (not only admissible).
import sys
from fractions import Fraction as F
def r(n): return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
def S(k,n):
    t=F(0)
    for j in range(1,k+1): t=16*t+r(n+j)
    return t
N=int(sys.argv[1])
seeds=[F(0),F(1,5),F(-1,3),F(15,16),F(1,7),F(2**61-1,2**62)]
tot=0;bad=[];bnd=0
for s in seeds:
    xs=[s%1]
    for n in range(1,N+40): xs.append((16*xs[-1]+r(n))%1)
    for n in range(1,N):
        d=2
        while True:
            sig=S(d,n)
            if sig>=1: break
            for m in range(1,d):
                k=d-m
                theta=(16**d*xs[n])%1; delta=(16**m*S(k,n))%1
                bdef=int(theta+delta>=1)
                eps=S(m,n+k); y=xs[n+d]
                bwin=int(eps<=y<sig)
                tot+=1
                if bdef!=bwin or delta!=sig-eps: bad.append((s,n,m,k))
            d+=1
print("checks",tot,"mismatches",len(bad),bad[:5])
