# CB-3 fitting-window escape: build the lattice-calibrated family p(tau) of Lemma 3.2 numerically and
# compute E b - delta = beta(I_n) - |I_n| EXACTLY in expectation (digit laws varying with index), far past A~10^3.
import mpmath as mp, math, random
mp.mp.dps=40
u=[mp.mpf(1)/16]*16
def phi(t):
    if t<=0.3 or t>=0.7: return 0.0
    if 0.4<=t<=0.6: return 1.0
    x=(t-0.3)/0.1 if t<0.4 else (0.7-t)/0.1
    return x*x*(3-2*x)          # C^1 bump
def Fp(p,t,depth=40):
    # distribution function of iid-digit measure with law p at t in [0,1]
    if t>=1: return mp.mpf(1)
    acc=mp.mpf(0); pref=mp.mpf(1)
    for _ in range(depth):
        t*=16; a=int(t); t-=a
        acc+=pref*sum(p[:a]); pref*=p[a]
    return acc
def plaw(t0,tau,lam):
    p=list(u); f=t0*phi(tau)
    p[2]+=f; p[3]-=f; p[1]+=lam; p[15]-=lam; return p
def solve_lam(t0,tau):
    if phi(tau)==0: return mp.mpf(0)
    tau=mp.mpf(tau)
    return mp.findroot(lambda l: Fp(plaw(t0,float(tau),l),tau)-tau, mp.mpf(0))
# 1) derivative bound of Lemma 3.2 at u
mind=min(( (Fp(plaw(0,0,mp.mpf('1e-20')),mp.mpf(t))-mp.mpf(t))/mp.mpf('1e-20'), t) for t in [0.3+0.4*i/400 for i in range(401)])
print("min d_v Phi(u,tau) on [0.3,0.7]:",mp.nstr(mind[0],6),"at",mind[1],"(claimed >0.86)")
t0=0.04
cache={}
def p_of(tau,cal=True):
    key=(round(tau,6),cal)
    if key not in cache: cache[key]=plaw(t0,tau,solve_lam(t0,round(tau,6)) if cal else 0)
    return cache[key]
lt=[];  # check calibration residual and probability vector
for i in range(41):
    tau=0.3+0.01*i; p=p_of(tau)
    lt.append((abs(Fp(p,mp.mpf(round(tau,6)))-round(tau,6)),min(p)))
print("max |F_p(tau)-tau| =",mp.nstr(max(x[0] for x in lt),3),"min prob entry",mp.nstr(min(x[1] for x in lt),5))
def tau_of(j): v=64.0*j*j; return 16.0**math.floor(math.log(v,16))/v
def T(n):
    n=mp.mpf(n); return mp.fsum((4/(8*(n+j)-7)-2/(8*(n+j)-4)-1/(8*(n+j)-3)-1/(8*(n+j)-2))/mp.mpf(16)**j for j in range(1,60))
def Fvar(laws,t):
    if t>=1: return mp.mpf(1)
    acc=mp.mpf(0); pref=mp.mpf(1)
    for q in laws:
        t*=16; a=int(t); t-=a
        acc+=pref*sum(q[:a]); pref*=q[a]
    return acc
random.seed(7)
for A in [10**3,10**4,10**6,10**9,10**12,10**15]:
    dmax=int(math.floor(math.log(64*A*A,16)))
    for cal in (True,False):
        worst=(0,None);
        for n in [A,2*A-1]+[random.randrange(A,2*A) for _ in range(6)]:
            for d in range(2,dmax+1):
                if mp.mpf(16)**d*T(n)>1: continue
                laws=[p_of(tau_of(n+d+i),cal) for i in range(1,36)]
                R=mp.mpf(16)**d*T(n)
                for m in range(1,d):
                    k=d-m; L=mp.mpf(16)**m*T(n+k)
                    e=abs(Fvar(laws,R)-Fvar(laws,L)-(R-L))
                    if e>worst[0]: worst=(e,(n,m,k,float(R)))
        print("A=%g calibrated=%s  sup|E b - delta| = %s at (n,m,k,R)=%s"%(A,cal,mp.nstr(worst[0],4),worst[1]))
