# CB-1g at 16^d T_n nearest 1, high precision (mpmath, 200 dps; adversarial test, not a certificate).
import mpmath as mp
mp.mp.dps=200
def r(n): n=mp.mpf(n); return 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
def T(n,terms=180): return mp.fsum(r(n+j)/mp.mpf(16)**j for j in range(1,terms))
def S(k,n): return mp.fsum(mp.mpf(16)**(k-j)*r(n+j) for j in range(1,k+1))
rows=[];gap=[]
for d in range(2,60):
    N0=2**(2*d-3)
    for n in range(max(1,N0-3),N0+4):
        R=mp.mpf(16)**d*T(n); sig=S(d,n)
        rows.append((R,d,n,sig))
        if sig<1<R: gap.append((d,n))
adm=[x for x in rows if x[0]<=1]
R,d,n,sig=max(adm,key=lambda x:x[0])
print("max admissible 16^dT_n: 1-R =",mp.nstr(1-R,8),"at d,n",d,n)
print("cases with S_d(n)<1<16^dT_n (CB-1 applies, CB-1g hypothesis fails):",gap)
# margin: for each d, 1 - 16^d T_n at the largest-R admissible n and at the smallest non-admissible n
for d in (2,3,4,10,30,59):
    N0=2**(2*d-3)
    print(d,[ (n, mp.nstr(mp.mpf(16)**d*T(n)-1,6), mp.nstr(S(d,n)-1,6)) for n in (N0-1,N0,N0+1)])
# adversarial z at the admissible near-1 triple(s): compare b via x_{n+d}={z-T_{n+d}} vs gauge interval
bad=0;tot=0
for R,d,n,sig in sorted(adm,key=lambda x:-x[0])[:40]:
    Tnd=T(n+d)
    for m in range(1,d):
        k=d-m; L=mp.mpf(16)**m*T(n+k); eps=S(m,n+k)
        h=mp.mpf(10)**-150
        for z in [L,L-h,L+h,R-h,R,Tnd,Tnd-h,Tnd+h,mp.mpf(0),1-h,(L+R)/2]:
            z=z%1; y=(z-Tnd)%1
            bwin=int(eps<=y<sig); bg=int(L<=z<R)
            tot+=1; bad+= (bwin!=bg)
print("CB-1g adversarial checks",tot,"mismatches",bad)
