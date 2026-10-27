"""PROVE the universal 1/N law for D^(3), and identify the exact constant.

Claim: For ANY real alpha, D^(3)_{N,h}(alpha) = (1/N) * C(alpha,h) + O(1/N^2)?  No --
numerically N*|D^(3)| is EXACTLY constant, meaning S_N = sum_{n=0}^{N-1} [e(3h 16^n a)-e(h 16^n a)]
has |S_N| exactly constant => S_N = C (a fixed vector), i.e. the increment is zero for n>=1.

But e(3h 16^n a) != e(h 16^n a) for n>=1 in general. So S_N is NOT exactly constant;
rather |S_N| is constant to ~8 digits but the PHASE may rotate. Let me check if S_N (complex)
is constant or rotating.

Earlier (closed_form.py) I found S_N = (-5.6096494 - 24.0644852j) EXACTLY constant for
N=100..25600 with dps=80, using hex_orbit (precision-safe). That means the increment
e(3h 16^n a) - e(h 16^n a) is EXACTLY ZERO for n >= some n0.  For n >= n0, the fractional
part {16^n a} must make e(3h x) = e(h x), i.e. e(2h x) = 1, i.e. 2h {16^n a} in Z.

But {16^n a} is irrational for irrational a, so 2h{16^n a} is never an integer. Contradiction!

RESOLUTION: the "exact constancy" from closed_form.py used dps=80 and mp.frac(16^n a) for
n up to 25600, which needs ~25600*1.2 ~ 30000 digits of precision, NOT 80. So closed_form.py's
"exact constancy" was ALSO a precision artifact (same trap as before, at larger n).

The CORRECT conclusion (from generic_1overN.py, which used the PRECISION-SAFE digit-shift
x -> frac(16x)): N*|D^(3)| is constant to ~7-8 digits but that too may drift at larger N.
Let me push precision-safe to HUGE N and check if N*|D| is truly constant or slowly drifts.

THIS IS THE CRUX. If N*|D^(3)| -> constant EXACTLY, then D^(3) ~ 1/N is a universal
trigonometric identity (provable). If it drifts (e.g. grows like sqrt(log N) or N^eps),
then it's a genuine quantitative fact about x16 orbits that could differ between
normal and non-normal alpha -- and THAT would be the tunnel.
"""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

def S_complex(alpha,N,h):
    x=mp.frac(alpha); s=mp.mpc(0)
    for _ in range(N):
        s += e(3*h*x)-e(h*x)
        x=mp.frac(16*x)
    return s

# Precision-safe: push to large N and watch N*|D| = |S_N| for drift.
print("=== |S_N| = N*|D^(3)| for pi, h=1, precision-safe, large N ===")
for N in [1000, 10000, 100000, 1000000, 3000000]:
    s = S_complex(pi,N,1)
    print(f"  N={N}: |S_N| = {mp.nstr(abs(s),12)}")

print("\nIf |S_N| is exactly constant -> universal 1/N trigonometric identity (provable).")
print("If |S_N| drifts upward -> D^(3) decays slower than 1/N -> potentially discriminates.")
