from fractions import Fraction as Fr
import mpmath as mp, math, random
mp.mp.dps=400
def r(n): return Fr(4,8*n-7)-Fr(2,8*n-4)-Fr(1,8*n-3)-Fr(1,8*n-2)
def r2(n): return Fr(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
assert all(r(n)==r2(n) for n in range(1,300)); print("r forms agree; r(1)=",r(1))
# U_n exact for seed s rational
def run(s,N):
    U=[s];
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U
def frac(x): return x-math.floor(x)
def S(k,n): return sum(16**(k-j)*r(n+j) for j in range(1,k+1))
# CB1 exact check, random rational seeds
bad=0;cnt=0
for s in [Fr(0),Fr(1,3),Fr(5,7),Fr(123,1000)]:
    U=run(s,140)
    for n in range(2,100):
        for m in range(1,4):
            for k in range(1,4):
                d=m+k; sig=S(d,n)
                if sig>=1: continue
                x=lambda j: U[j]-math.floor(U[j])
                theta=frac(16**d*x(n)); delta=frac(16**m*S(k,n))
                b=1 if theta+delta>=1 else 0
                eps=S(m,n+k); y=x(n+d)
                b2=1 if (eps<=y<sig) else 0
                cnt+=1
                if b!=b2 or delta!=sig-eps: bad+=1
print("CB1 exact checks",cnt,"bad",bad)
# CB1g with s=0, alpha=pi/16, high precision
pi16=mp.pi/16
def T(n,K=120): return mp.fsum(mp.mpf(16)**(-i)*mp.mpf(r(n+i).numerator)/r(n+i).denominator for i in range(1,K))
U=run(Fr(0),200)
bad=0;cnt=0
for n in range(2,120):
    for m in range(1,5):
        for k in range(1,5):
            d=m+k
            if mp.mpf(16)**d*T(n)>1: continue
            z=mp.frac(mp.mpf(16)**(n+d)*pi16)
            lo=mp.mpf(16)**m*T(n+k); hi=mp.mpf(16)**d*T(n)
            bg=1 if lo<=z<hi else 0
            xn=U[n]-math.floor(U[n]); theta=frac(16**d*xn); delta=frac(16**m*S(k,n))
            b=1 if theta+delta>=1 else 0
            cnt+=1; bad+= (b!=bg)
print("CB1g checks",cnt,"bad",bad)
# j>=0 claim: ratio 16^d T_n / (16 tau_{n+d+1}) when d=e+1
def tau(j):
    L=mp.log(64*j*j,16); e=int(mp.floor(L)); return mp.mpf(16)**e/(64*j*j), e
worst=None
for n in list(range(2,400))+[10**4,10**5]:
    Tn=T(n)
    for d in range(1,40):
        if mp.mpf(16)**d*Tn>1: break
        t,e=tau(n+d+1)
        jj=e-d
        if jj<0: print("j<0 at",n,d)
print("j>=0 scan done")
