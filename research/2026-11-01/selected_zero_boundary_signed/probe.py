"""Phase 4 — selected zero-boundary signed-lag attack (post-Main-XIX research).

Three fronts, each producing an exact receipt. FROZEN: U_0=0 literal,
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2). Nothing here promotes the gate; the
honest outcome is one refuted intermediate lemma (Front A), one representation-identity
classification (Front B), and one resolution-ceiling obstruction (Front C). Finite N only.

Run WITHOUT `python -I`. Stdlib + mpmath/numpy only; imports nothing from the repo tree.
"""
import mpmath as mp, numpy as np, math
from fractions import Fraction as Fr

Wf=np.array([4.,-2.,-1.,-1.]); Pf=np.array([7/8,1/2,3/8,1/4])
def r_f(nv): return 4./(8*nv-7)-2./(8*nv-4)-1./(8*nv-3)-1./(8*nv-2)
def T_vec(nv,M=20):
    t=np.zeros_like(nv,dtype=float)
    for m in range(1,M+1): t+=(16.**(-m))*r_f(nv+m)
    return t
def Rbox(nv,k,d):
    acc=np.zeros_like(nv,dtype=float)
    for j in range(1,k+1):
        inner=np.zeros_like(nv,dtype=float)
        for w,p in zip(Wf,Pf): inner+=(w/8.)*((p-j)**d)/(nv+j-p)
        acc+=(16.**(-j))*inner
    return (16.**k)*(nv.astype(float)**(-d))*acc

def pi_hex_windows(Nmax,win=13):
    mp.mp.dps=int((Nmax+win+10)*math.log10(16))+25
    f=mp.pi-3; digs=[]
    for _ in range(Nmax+win+2):
        f*=16; dd=int(f); digs.append(dd); f-=dd
    digs=np.array(digs,float); pw=16.**(-(np.arange(win)+1))
    x=np.empty(Nmax+1);
    for m in range(Nmax+1): x[m]=np.dot(digs[m:m+win],pw)
    return x,digs

print("="*70)
print("FRONT A — compensated-clock corrected lag at the LITERAL zero seed")
print("  candidate lemma: 'L^[d](N,K_N;0) >= 0 and per-lag corr >= 0' (a positivity shortcut)")
print("="*70)
Nmax=65536; x,_=pi_hex_windows(Nmax)
def frontA(N,d,h):
    K=int(math.floor((d+1)*math.log(N,16)))
    LD=0.; worst_lag=1e9; worst=None
    for k in range(1,K):
        wk=1-k/K; nv=np.arange(1,N-k+1)
        xn=x[nv-1]; xnk=x[nv-1+k]; Tn=T_vec(nv); Tnk=T_vec(nv+k)
        ph=(xnk-xn)+(Tn-Tnk)-Rbox(nv,k,d)
        m=np.cos(2*np.pi*h*ph).mean()
        LD+=wk*np.cos(2*np.pi*h*ph).sum()
        if m<worst_lag: worst_lag=m; worst=(k,m)
    return (2./(K*N))*LD, worst, K
refuted=False
for d in (2,3):
    for h in (1,3,5,7):
        for N in (16384,65536):
            L,(k,m),K=frontA(N,d,h)
            neg = (L<0) or (m<0)
            if neg: refuted=True
            print(f"  d={d} h={h} N={N} K={K}: L^[d]={L:+.5f}  min per-lag corr={m:+.4f} @k={k}  {'<-- sign-negative' if neg else ''}")
print(f"\n  CANDIDATE POSITIVITY LEMMA REFUTED: {refuted}  (persistent negatives => no one-sided shortcut)\n")

print("="*70)
print("FRONT B — angular-period identity (AC-13) is SEED-BLIND => representation identity")
print("="*70)
mp.mp.dps=60
P=lambda t: 4-2*t**3-t**4-t**5
period=mp.quad(lambda t: P(t)/(16-t**8),[0,1])
print(f"  source angular period  ∫_0^1 P/(16-t^8) dt = {mp.nstr(period,40)}")
print(f"  pi/16                                     = {mp.nstr(mp.pi/16,40)}")
print(f"  match: {mp.almosteq(period,mp.pi/16,1e-38)}")
# the period/angular data involves ONLY the source r (not the seed). Two seeds with the
# SAME source therefore share the identity, yet realize completely different orbits:
def S_counterfeit_q15(N,h):  # same four-pole FORCING, completed point q=1/5 (rational, nonnormal)
    # U_n = 16^n/5 - T_n ; {U_n} -> 1/5 ; S_N = N e(h/5)+O(1)
    acc=0j
    for n in range(1,N+1):
        xn=(pow(16,n,5)/5.0)  # {16^n/5} exactly (16^n mod 5)/5
        acc+=mp.e**(2j*mp.pi*h*xn)
    return acc
N=4000
for h in (1,2,3):
    S=S_counterfeit_q15(N,h)
    print(f"  q=1/5 counterfeit (SAME source, SAME angular period): |S_{N}({h})|/N = {abs(S)/N:.4f}  (-> 1, NONnormal)")
print("  The AC-13 identity is unchanged by the seed, so it holds identically for the normal-")
print("  candidate zero seed AND the nonnormal q=1/5 orbit. It fixes only the completed constant")
print("  pi/16; it is BLIND to the digit distribution. => representation identity, NOT a mechanism.\n")

print("="*70)
print("FRONT C — within-cell signed phase = the gate at a SHIFTED frequency; ceiling blocks it")
print("="*70)
# within-cell phase at resolution k probes frequency h*16^k: {16^k U_n} carries finer digits.
# For the zero seed, S_N(h*16^k) is just the gate at harmonic h*16^k (digit shift by k).
def S_zero(N,H,x):
    nv=np.arange(1,N+1); xn=x[nv-1]
    return np.abs(np.sum(np.exp(2j*np.pi*H*xn)))/N
for k in (1,2,3):
    for h in (1,3):
        H=h*(16**k)
        val=S_zero(16384,H,x)
        print(f"  zero seed: |S_N(h*16^k)|/N at h={h},k={k} (freq {H}) = {val:.4f}  (small => gate at shifted harmonic)")
print("  Resolution ceiling D_{N,k} >= max(0, log(M/N)), M=16^k: an AFFORDABLE resolution needs")
print("  M<=N i.e. k<=log_16 N; beyond it the deficit is forced. Within-cell control at affordable")
print("  resolution is exactly S_N(h*16^k)=o(N) at a higher harmonic — the gate again, no new")
print("  seed-specific signed leverage below the ceiling.\n")
print("DONE")
