import math
def F(p,t,depth=40):
    # distribution function of iid-digit measure
    tot=0.0; pref=1.0
    for i in range(depth):
        s=int(16*t); s=min(s,15)
        tot+=pref*sum(p[:s]); pref*=p[s]; t=16*t-s
    return tot
u=[1/16]*16
def pv(lam,t0=0.0,ph=0.0):
    p=list(u); p[1]+=lam; p[15]-=lam; p[2]+=t0*ph; p[3]-=t0*ph; return p
h=1e-7; mn=9
for i in range(4001):
    t=0.3+0.4*i/4000
    d=(F(pv(h),t)-F(pv(-h),t))/(2*h); mn=min(mn,d)
print("min dPhi/dv on [0.3,0.7] =",mn, " bound 1-2.21/16=",1-2.21/16, " exact sum",256/225+16/15)
# solve lambda for t0=0.02, bump=1 on whole, check calibration and |lambda|
t0=0.02; ml=0
for i in range(201):
    t=0.3+0.4*i/200
    lo,hi=-0.03,0.03
    for _ in range(60):
        mid=(lo+hi)/2
        if F(pv(mid,t0,1.0),t)-t>0: hi=mid
        else: lo=mid
    ml=max(ml,abs(mid))
print("max |lambda| at t0=0.02, phi=1:",ml)
# lower density of {j: tau_j in [0.4,0.6]}
def inset(j):
    L=math.log(64*j*j,16); e=math.floor(L); t=16**e/(64*j*j); return 0.4<=t<=0.6
c=0; mind=1
for j in range(1,3*10**6):
    c+=inset(j)
    if j>1000: mind=min(mind,c/j)
print("lower Cesaro density (j<3e6) ~",mind, " predicted (sqrt1.5-1)/3=",(math.sqrt(1.5)-1)/3)
# union-bound exponent: 3*(1-log16(1+16 t0)) > 2 ?
for t0 in [0.01,0.02,0.05,0.09]: print(t0, 3*(1-math.log(1+16*t0,16)), 3*(1-math.log(1+32*t0,16)))
