"""Definitive: is D^(3) for the SOURCE provably easier than D^(3) for the ORBIT?

The source gives U_{n+1} = 16^n pi - T_{n+1} with 0 < T_{n+1} < 1/(15(n+2)^2), SUMMABLE.

x3-invariance of the SOURCE:
  D_source = (1/N) sum_n [ e(3h U_{n+1}) - e(h U_{n+1}) ].

x3-invariance of the ORBIT:
  D_orbit = (1/N) sum_n [ e(3h 16^n pi) - e(h 16^n pi) ].

Their difference:
  e(3h U_{n+1}) - e(3h 16^n pi) = e(3h 16^n pi)[ e(-3h T_{n+1}) - 1 ],
  magnitude <= 2 pi |3h| T_{n+1} <= 2 pi |3h| / (15(n+2)^2).
  Sum over n: (1/N) * sum_n O(1/n^2) = O(1/N).

So |D_source - D_orbit| = O(|h|/N) -> 0.

THEREFORE: D_source -> 0  IFF  D_orbit -> 0.  They are EQUIVALENT.

The signed four-pole source does NOT make x3-invariance easier; it only transports the
problem back to the orbit with an O(1/N) error (this is exactly AR-3/AR-5's content).

This is a RIGOROUS theorem and it is the definitive answer: there is no free lunch.
The source's rational structure transports, it does not cancel.

Let me verify numerically.
"""
import math, cmath
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 50
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

def r(n):
    n=Fraction(n)
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)
def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U
def uf(U,n): return mp.mpf(U[n].numerator)/U[n].denominator

N=500
U=Us(N)

def Dsource(h):
    return sum(e(3*h*uf(U,n+1))-e(h*uf(U,n+1)) for n in range(N))/N
def Dorbit(h):
    return sum(e(3*h*mp.frac(mp.power(16,n)*pi))-e(h*mp.frac(mp.power(16,n)*pi)) for n in range(N))/N

print("=== |D_source - D_orbit| = O(|h|/N)? ===")
for h in [1,2,3,5]:
    ds = Dsource(h); do = Dorbit(h)
    print(f"  h={h}: |D_source|={mp.nstr(abs(ds),6)}  |D_orbit|={mp.nstr(abs(do),6)}  diff={mp.nstr(abs(ds-do),6)}  bound O(|h|/N)={mp.nstr(2*pi*3*h/N,6)}")

# The difference should decay like 1/N. Check.
print("\n=== 1/N decay of the difference ===")
for NN in [200,400,800,1600]:
    UU=Us(NN)
    def ufn(U,n): return mp.mpf(U[n].numerator)/U[n].denominator
    ds = sum(e(3*ufn(UU,n+1))-e(ufn(UU,n+1)) for n in range(NN))/NN
    do = sum(e(3*mp.frac(mp.power(16,n)*pi))-e(mp.frac(mp.power(16,n)*pi)) for n in range(NN))/NN
    print(f"  N={NN}: |D_source - D_orbit| = {mp.nstr(abs(ds-do),6)}")
