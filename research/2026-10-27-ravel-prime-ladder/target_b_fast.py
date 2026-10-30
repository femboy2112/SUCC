"""Fast vectorized brute-force for literal Target B inequality."""
import cmath, math, random
import numpy as np

def dist(x): return np.abs(x - np.round(x))

def W(seq, h):  # seq complex phase contributions precomputed as e(h x)
    return np.exp(2j*math.pi*h*seq).mean()

def C(seq, eta): return (dist(seq) < eta).mean()

def Omega(k):
    k=abs(k); c=0; d=2
    while d*d<=k:
        while k%d==0: k//=d; c+=1
        d+=1
    if k>1: c+=1
    return c

_primes_cache = {}
def primes(n):
    if n in _primes_cache: return _primes_cache[n]
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    ps = np.nonzero(sieve)[0].tolist()
    _primes_cache[n]=ps
    return ps

def Delta(seq, H):
    ps = primes(H)
    best = 0.0
    for p in ps:
        j = 1
        while p*j <= H:
            d = abs(W(seq, p*j) - W(seq, j))
            if d > best: best = d
            j += 1
    return best

rng = np.random.default_rng(7)
viol = 0
N = 400
total = 8000
for trial in range(total):
    mode = trial % 6
    if mode==0: seq = rng.random(N)
    elif mode==1: seq = rng.normal(0,0.15,N)
    elif mode==2:
        c = rng.choice([0.01,0.02,0.05,0.1,0.13,0.17,0.2,0.25]); seq = rng.normal(c,0.005,N)
    elif mode==3:
        a=rng.random(); b=rng.random(); seq = np.where(rng.random(N)<0.5,a,b)
    elif mode==4:
        r = rng.choice([2,3,5,7,9,11,13]); num=rng.integers(1,r); seq = num/r + rng.normal(0,1e-4,N)
    else:
        seq = np.where(rng.random(N)<0.7, rng.normal(0,0.3,N), rng.random(N))

    h = rng.integers(1,9)
    K = int(rng.choice([2,3,4,5,8,16]))
    eta = float(rng.choice([0.02,0.04,0.06,0.1,0.15,0.2,0.3]))
    H = abs(h)*K

    lhs = abs(W(seq,h))
    rhs = C(seq,eta) + 1/(2*K*eta) + (Omega(h)+int(math.log2(K)))*Delta(seq,H)
    if lhs > rhs + 1e-9:
        viol += 1
        if viol <= 12:
            print(f"VIOL mode={mode} h={h} K={K} eta={eta}: LHS={lhs:.4f} RHS={rhs:.4f} C={C(seq,eta):.3f} Del={Delta(seq,H):.4f}")
print(f"violations: {viol}/{total}")
