#!/usr/bin/env python3
"""Sketch: exact s_n structure and cofiber for the signed Weyl decomposition.

All orbit/tail arithmetic in exact Fraction; pi-phase via mpmath at high dps.
This is exploratory; the rigorous bound lives in the markdown + verify script.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 200

# r(n) exact rational coefficients
def r(n):
    return Fraction(4, 8*n-7) - Fraction(2, 8*n-4) - Fraction(1, 8*n-3) - Fraction(1, 8*n-2)

# exact tail T_n = sum_{j>=1} 16^{-j} r(n+j)  (truncate)
def T_exact(n, terms=80):
    s = Fraction(0)
    for j in range(1, terms+1):
        s += Fraction(1, 16**j) * r(n+j)
    return s

# exact orbit
def U_exact(n, terms=80):
    # U_n = 16^{n-1} pi - T_n  ; we only need frac(U_n) exactly up to T_n
    # frac(U_n) = frac(16^{n-1} pi - T_n)
    return T_exact(n, terms)

def frac_pi_times_16k(k, dps=200):
    """frac(16^k * pi) exactly via mpmath pi."""
    x = mp.mpf(16)**k * mp.pi
    return x - mp.floor(x)

# s_n = M{U_n} - a_n, a_n = floor(M{U_n}), {U_n} = frac(16^{n-1} pi - T_n)
def frac_U(n, terms=80, dps=200):
    f = frac_pi_times_16k(n-1, dps)
    t = T_exact(n, terms)
    # {f - t} : f - t could dip below 0
    val = mp.mpf(f) - mp.mpf(t.numerator) / mp.mpf(t.denominator)
    return val - mp.floor(val)

if __name__ == "__main__":
    for n in [1,2,3,5,10,100]:
        Tn = T_exact(n)
        fU = frac_U(n)
        print(f"n={n}: T_n={float(Tn):.3e}  frac(U_n)={mp.nstr(fU,12)}")
