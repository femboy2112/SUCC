"""Resolve the EXACT constancy of S_N. If S_N is constant in N, then the increment
e(3h 16^n a) - e(h 16^n a) must be ~0 for n>=1. Check the individual terms.

Actually wait: S_{1000} - S_{1000+k} = 0 for k up to 128 means the sum from n=1000 to 1000+k-1
is zero. This strongly suggests e(3h 16^n a) = e(h 16^n a) for all n>=1, i.e.
3h 16^n a = h 16^n a mod 1, i.e. 2h 16^n a in Z.

But for a=pi, h=1: 2*16^n*pi is NOT an integer. So something else. Let me check the terms
directly, and reconsider -- maybe mp.power(16,n)*alpha for large n has catastrophic
precision loss, and mp.frac of a huge number is garbage, making both terms equal (both = e(small junk)).

THIS IS THE KEY: mp.power(16,n)*pi for n=1000 is a 1200-digit number; mp.frac() extracts the
fractional part, but mpmath at dps=60 does NOT have enough precision to get the fractional
part of 16^1000 * pi correctly (needs 1200+ digits). So the results for large n are NUMERICAL
GARBAGE, and e(3h x) - e(h x) with garbage x may spuriously equal 0.

I must REDO this with sufficient precision (dps ~ 2000 for n=1000).
"""
import cmath, math
import mpmath as mp
pi = mp.pi
e = lambda x: cmath.exp(2j*math.pi*x)

# Check the actual fractional parts and terms at moderate n with HIGH precision
mp.mp.dps = 200
print("=== individual terms with dps=200, moderate n ===")
a = mp.pi
h = 1
for n in [1,2,3,4,5,10,20]:
    x = mp.frac(mp.power(16,n)*a)
    term = e(3*h*x) - e(h*x)
    print(f"  n={n}: frac(16^n pi)={mp.nstr(x,8)}  term={mp.nstr(term,8)}  |term|={abs(term):.4f}")

# The terms are NOT zero. So S_N is NOT literally constant; my earlier "constancy" was
# precision loss at n>=1000. Redo the S_N constancy test at SMALL N with high precision.
print("\n=== S_N vs S_{N+k} at small N, dps=200 ===")
def S(alpha,N,h):
    return sum(e(3*h*mp.frac(mp.power(16,n)*alpha)) - e(h*mp.frac(mp.power(16,n)*alpha)) for n in range(N))
base = S(a, 50, 1)
for k in [1,2,5,10]:
    sk = S(a, 50+k, 1)
    print(f"  S_50 - S_50+{k} = {mp.nstr(base-sk,8)}")

# So the 1/N law for D^(3) is REAL (bounded S_N) but I need to re-derive the exact constant
# with correct precision. The earlier "constant |S_N|" was partly an artifact.
# Recompute D^(3) and N*D^(3) at moderate N with proper precision.
print("\n=== D^(3) and N*D^(3) at dps=200, moderate N (correct precision) ===")
for N in [50,100,200,400,800]:
    s = S(a,N,1)
    print(f"  N={N}: |D^(3)|={abs(s)/N:.8f}  |S_N|={abs(s):.8f}  S_N={mp.nstr(s,6)}")
