exec(open('p4_cb3.py').read().split('random.seed(7)')[0].replace('print(','(lambda *a,**k:None)('))
# target the bump: n with tau_{n+d+1} in [0.42,0.58], extreme splits m=1,k=d-1 and m=d-1,k=1, maximal d
random.seed(3)
for A in [10**3,10**5,10**8,10**12,10**16,10**20]:
    dmax=int(math.floor(math.log(64*A*A,16)))
    res={True:(0,None),False:(0,None)}
    tried=0
    for d in range(2,dmax+1):
        # candidates n in [A,2A) with tau_{n+d+1} in bump core
        cands=[n for n in [random.randrange(A,2*A) for _ in range(4000)] if 0.42<=tau_of(n+d+1)<=0.58][:3]
        for n in cands:
            if mp.mpf(16)**d*T(n)>1: continue
            R=mp.mpf(16)**d*T(n)
            for cal in (True,False):
                laws=[p_of(tau_of(n+d+i),cal) for i in range(1,36)]
                for m in sorted({1,d-1,max(1,d//2)}):
                    k=d-m; L=mp.mpf(16)**m*T(n+k)
                    e=abs(Fvar(laws,R)-Fvar(laws,L)-(R-L)); tried+=1
                    if e>res[cal][0]: res[cal]=(e,(n,m,k,round(float(R),4)))
    print("A=%g (dmax=%d, %d evals)  calibrated sup=%s %s | UNcalibrated control sup=%s"%(A,dmax,tried,mp.nstr(res[True][0],4),res[True][1],mp.nstr(res[False][0],4)))
