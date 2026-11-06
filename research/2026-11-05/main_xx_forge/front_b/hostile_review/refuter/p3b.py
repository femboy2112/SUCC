exec(open('p3_cb1g.py').read().split('# adversarial z')[0].replace('print(','(lambda *a,**k:None)('))
from collections import Counter
c=Counter()
for R,d,n,sig in sorted(adm,key=lambda x:-x[0])[:40]:
    Tnd=T(n+d)
    for m in range(1,d):
        k=d-m; L=mp.mpf(16)**m*T(n+k); eps=S(m,n+k)
        h=mp.mpf(10)**-150
        for name,z in [('L',L),('L-h',L-h),('L+h',L+h),('R-h',R-h),('R',R),('Tnd',Tnd),('Tnd-h',Tnd-h),('Tnd+h',Tnd+h),('0',mp.mpf(0)),('1-h',1-h),('mid',(L+R)/2)]:
            z=z%1; y=(z-Tnd)%1
            bwin=int(eps<=y<sig); bg=int(L<=z<R)
            if bwin!=bg: c[(name,d<=4)]+=1; ex=(name,d,n,m,k,mp.nstr(y-eps,5),mp.nstr(z-L,5), mp.nstr(sig-y,5))
print(c); print(ex)
