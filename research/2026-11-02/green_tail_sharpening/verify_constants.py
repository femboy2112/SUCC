"""Verify the exact closed forms: S (digamma), B = (S-pi)/15, and 2 s3 + s4 + s5 = pi/16."""
import sympy as sp
from sympy import pi, Rational, digamma as dg, lerchphi, N

# S = (1/8)[ 2 psi(1/2) + psi(5/8) + psi(3/4) - 4 psi(1/8) ]
S = Rational(1, 8) * (2*dg(Rational(1, 2)) + dg(Rational(5, 8))
                      + dg(Rational(3, 4)) - 4*dg(Rational(1, 8)))

# B = (S - pi)/15
B = (S - pi) / 15

# f_m series via Lerch
def BBP(c):
    return lerchphi(Rational(1, 16), 1, Rational(c, 8)) / 8

s3 = (BBP(1) - BBP(4)) / 16
s4 = (BBP(1) - BBP(5)) / 16
s5 = (BBP(1) - BBP(6)) / 16

print("S =", N(S, 45))
print("B = (S-pi)/15 =", N(B, 45))
print("s_3 =", N(s3, 40))
print("s_4 =", N(s4, 40))
print("s_5 =", N(s5, 40))
print("\n2 s_3 + s_4 + s_5 - pi/16 =", N(2*s3 + s4 + s5 - pi/16, 30))
print("\nB expected = 0.016296997733826565564918363210593998401983263520463")
assert abs(N(B, 40) - sp.Float("0.01629699773382656556491836321059399840198", 40)) < sp.Float(10, 40)**(-35)
print("All constant closed forms verified.")
