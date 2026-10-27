"""AR-3 transport corridor + AR-4 rank-1 slice recovery, computed on the AUTHENTIC source.

AR-3: |F^SUCC - F^pi| <= (4 sqrt(pi|h|/15))/(N prod M_j) * prod_j (q_j^{M_j/2}-1)/(sqrt(q_j)-1)

AR-4: f_0 = (1/M) sum_m f_m + (1/M) sum_{m=0}^{M-2} (M-1-m)(f_m - f_{m+1})

We verify AR-3 numerically on the exact source, and CRUCIALLY check the rank-1 slice
recovery identity AR-4 exactly, which is the load-bearing "does rank-2 Haar imply rank-1 Haar"
question. Then we check: does the rank-2 bulk average actually approach the rank-1 Weyl sum,
or does the transverse defect carry the mass?
"""
import math, cmath
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
e = lambda x: cmath.exp(2j*math.pi*x)

def r(n):
    n = Fraction(n)
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U

N=60
U=Us(N)
def uf(n): return mp.mpf(U[n].numerator)/U[n].denominator

# AR-3 rank 2, q=3: F^SUCC_{N,M}(h) = (1/(NM)) sum_{n=0}^{N-1} sum_{m=0}^{M-1} e(h 3^m U_{n+1})
def Fsucc(N,M,h):
    s=0j
    for n in range(N):
        for m in range(M):
            s += e(h * mp.power(3,m) * uf(n+1))
    return s/(N*M)

def Fpi(N,M,h):
    s=0j
    for n in range(N):
        for m in range(M):
            s += e(h * mp.power(16,n) * mp.power(3,m) * pi)
    return s/(N*M)

def bound_ar3(N,M,h):
    return (4*mp.sqrt(mp.pi*abs(h)/15)/(N*M)) * (mp.power(3,M/2)-1)/(mp.sqrt(3)-1)

print("=== AR-3 transport corridor (rank 2, q=3) on authentic source ===")
for h in [1,3]:
    for N in [20,40]:
        M = int(2*mp.log(N,3))  # M ~ 2 log_3 N
        Fs = Fsucc(N,M,h); Fp = Fpi(N,M,h)
        diff = abs(Fs-Fp)
        bd = bound_ar3(N,M,h)
        print(f"  h={h} N={N} M={M}: |F^SUCC-F^pi| = {mp.nstr(diff,4)}, bound={mp.nstr(bd,4)}, ok={diff<=bd+1e-12}")

# AR-4: rank-1 slice recovery. f_m = (1/N) sum_n e(h 3^m U_{n+1})
print("\n=== AR-4: does rank-2 bulk average recover rank-1 slice? ===")
def fm(N,h,m):
    return sum(e(h*mp.power(3,m)*uf(n+1)) for n in range(N))/N

for h in [1,3]:
    for N in [20,40]:
        M = int(2*mp.log(N,3))
        f0 = fm(N,h,0)
        bulk = sum(fm(N,h,m) for m in range(M))/M
        defect = sum((M-1-m)*(fm(N,h,m)-fm(N,h,m+1)) for m in range(M-1))/M
        print(f"  h={h} N={N} M={M}: f0={mp.nstr(f0,5)}  bulk={mp.nstr(bulk,5)}  defect={mp.nstr(defect,5)}  |f0-(bulk+defect)|={abs(f0-bulk-defect):.2e}")
        print(f"     |bulk|={abs(bulk):.5f}  |defect|={abs(defect):.5f}  -> does bulk alone vanish? {abs(bulk)<0.1}")

# Key question: as M grows, does the bulk average (rank-2 Haar surrogate) vanish while f_0 stays?
print("\n=== bulk average vs rank-1 slice as M grows (the AR-4 trap) ===")
h=1; N=40
for M in [2,4,8,16,32,64]:
    f0 = fm(N,h,0)
    bulk = sum(fm(N,h,m) for m in range(M))/M
    defect = sum((M-1-m)*(fm(N,h,m)-fm(N,h,m+1)) for m in range(M-1))/M
    print(f"  M={M}: |f0|={abs(f0):.5f}  |bulk|={abs(bulk):.5f}  |defect|={abs(defect):.5f}  |bulk+defect|={abs(bulk+defect):.5f}")
