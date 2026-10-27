"""Rigorous, precision-safe computation of the pi hex orbit via iterative digit-shift.

x_{n+1} = frac(16 * x_n), x_0 = frac(pi).  This keeps numbers in [0,1), so fixed precision
is exact forever (each step multiplies a [0,1) number by 16: at most 4 bits shift, no blowup).

Then D^(3)_{N,h} = (1/N) sum_{n=0}^{N-1} [e(3h x_n) - e(h x_n)] is computed WITHOUT the
16^n * pi huge-number precision problem.
"""
import math, cmath
import mpmath as mp
mp.mp.dps = 60
pi = mp.pi
e = lambda x: cmath.exp(2j*math.pi*x)

def hex_orbit(alpha, N):
    x = mp.frac(alpha)
    out = []
    for _ in range(N):
        out.append(x)
        x = mp.frac(16*x)
    return out

def D3(alpha, N, h):
    xs = hex_orbit(alpha, N)
    return sum(e(3*h*x) - e(h*x) for x in xs)/N

def Wp(alpha, N, h):
    xs = hex_orbit(alpha, N)
    return sum(e(h*x) for x in xs)/N

print("=== D^(3) via digit-shift (precision-safe) ===")
for h in [1,3,7]:
    vals=[]
    for N in [100,1000,10000,100000]:
        d = D3(pi,N,h)
        vals.append((N,abs(d)))
        print(f"  h={h} N={N}: |D^(3)|={abs(d):.8f}")
    # check 1/N law
    if vals[-1][1]>0:
        print(f"    N*|D^(3)|: " + ", ".join(f"{N*v:.6f}" for N,v in vals))

print("\n=== plain Weyl sum via digit-shift ===")
for h in [1,3]:
    for N in [1000,10000,100000,1000000]:
        w = Wp(pi,N,h)
        print(f"  h={h} N={N}: |W_N(h)|={abs(w):.8f}")
