"""Exact computation of the authentic four-pole BBP source, and real probes.

Authentic source:
  r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)  (n>=1)
       = (120n^2-89n+16)/((2n-1)(4n-1)(8n-7)(8n-3))
  U_0 = 0,  U_{n+1} = 16 U_n + r(n+1).
  U_n = 16^{n-1} pi - T_n,  T_n = sum_{j>=1} 16^{-j} r(n+j),  0<T_n<1/(15(n+1)^2).

All U_n are rational with odd denominator (U_n in Q ∩ Z_2).
We compute U_n exactly as Fractions, then probe:
  1. W_N(h) = (1/N) sum e(h U_n)  -- the ultimate Weyl sum (real phase).
  2. D^{(3)}_{N,h} = W_N(3h)-W_N(h)  -- the transversal x3 defect (rank-2 rigidity route).
  3. Prime-frequency defect Delta_N(H).
  4. Near-zero concentration C_N(eta).
  5. Denominator prime support growth.
"""
import math, cmath
from fractions import Fraction
import sympy as sp

e = lambda x: cmath.exp(2j*math.pi*x)

def r(n):
    n = Fraction(n)
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))

def r_canceled(n):
    n = Fraction(n)
    num = 120*n*n - 89*n + 16
    den = (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return num/den

# verify canceled form
for n in range(1, 5):
    assert r(n) == r_canceled(n), f"cancel mismatch n={n}"
print("canceled form exact: OK")

def Us(N):
    U = [Fraction(0)]
    for n in range(1, N+1):
        U.append(16*U[-1] + r(n))
    return U  # U[0..N], with U_n = U[n]

# Green tail identity check: U_n = 16^{n-1} pi - T_n. Verify via rational Green tail partial sum
def green_tail_partial(n, J):
    # T_n ~ sum_{j=1}^{J} 16^{-j} r(n+j); exact rational
    s = Fraction(0)
    for j in range(1, J+1):
        s += Fraction(1, 16**j) * r(n+j)
    return s

# Verify U_n + T_n = 16^{n-1} pi. Check the RATIONAL identity: U_n = 16^{n-1} pi - T_n
# means 16^{n-1} pi = U_n + T_n. We can only check the tail bound 0 < T_n < 1/(15(n+1)^2).
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi

N = 40
U = Us(N)
print("\n-- authentic U_n (rational, odd denom) --")
for n in range(1, 6):
    print(f"  U_{n} = {U[n]}  (den {U[n].denominator}, odd={U[n].denominator % 2 == 1})")

# Tail bound check (exact rational partial sum + rigorous bound)
print("\n-- Green tail identity: 16^{n-1} pi = U_n + T_n,  0<T_n<1/(15(n+1)^2) --")
for n in [1,2,3,5,10,20]:
    J = 200
    Tn_rat = sum(Fraction(1, 16**j) * r(n+j) for j in range(1, J+1))
    Tn = mp.mpf(Tn_rat.numerator)/mp.mpf(Tn_rat.denominator)
    lhs = mp.power(16, n-1) * pi
    un = mp.mpf(U[n].numerator)/mp.mpf(U[n].denominator)
    diff = lhs - un - Tn  # = - (tail beyond J), tiny
    bound = mp.mpf(1)/(15*(n+1)**2)
    ok = (0 < Tn < bound)
    print(f"  n={n}: T_n={mp.nstr(Tn,5)} (bound {mp.nstr(bound,4)}, ok={ok}),  |16^{{n-1}}pi-U_n-T_n|={mp.nstr(abs(diff),3)}")

# Weyl sums and transversal defect for the REAL source phases
print("\n-- Weyl sums W_N(h) = (1/N)sum e(h U_n), and x3 defect D^(3) = W(3h)-W(h) --")
for h in [1,2,3,5,7]:
    for Nn in [10,20,40]:
        W = sum(e(h*mp.mpf(U[n].numerator)/U[n].denominator) for n in range(1, Nn+1))/Nn
        W3 = sum(e(3*h*mp.mpf(U[n].numerator)/U[n].denominator) for n in range(1, Nn+1))/Nn
        D = W3 - W
        print(f"  h={h} N={Nn}: |W_N(h)|={abs(W):.5f}  |D^(3)|={abs(D):.5f}")

# Prime-frequency defect
def Omega(k):
    k=abs(k); c=0; d=2
    while d*d<=k:
        while k%d==0: k//=d; c+=1
        d+=1
    if k>1: c+=1
    return c
def primes(n):
    ps=[]
    for i in range(2,n+1):
        if all(i%p for p in ps): ps.append(i)
    return ps
def W(seq,h):
    return sum(e(h*mp.mpf(x.numerator)/x.denominator) for x in seq)/len(seq)
def Delta(seq,H):
    ps=primes(H); b=0.0
    for p in ps:
        j=1
        while p*j<=H:
            b=max(b,abs(W(seq,p*j)-W(seq,j))); j+=1
    return b

seq = U[1:41]  # U_1..U_40
print("\n-- prime-frequency defect Delta_N(H) (real phases) --")
for H in [6,10,20,40]:
    print(f"  N=40 H={H}: Delta={Delta(seq,H):.5f}")

# Near-zero concentration
def C(seq,eta):
    return sum(1 for x in seq if abs(mp.mpf(x.numerator)/x.denominator - mp.nint(mp.mpf(x.numerator)/x.denominator)) < eta)/len(seq)
print("\n-- near-zero concentration C_N(eta) for U_n (note: U_n = 16^{n-1}pi - T_n ~ huge real, NOT near 0) --")
for eta in [0.05,0.1,0.2,0.3,0.45]:
    print(f"  eta={eta}: C={C(seq,eta):.4f}")

# denominator prime support
print("\n-- denominator prime support growth --")
for n in range(1, 16):
    d = U[n].denominator
    facs = sp.factorint(d)
    print(f"  n={n}: den={d}, primes={sorted(facs)}")

# x3 transversal defect D^(3) more carefully, larger N, using fractional parts of 16^{n-1}pi
# Actually U_n = 16^{n-1}pi - T_n, so e(h U_n) = e(h 16^{n-1} pi) * e(-h T_n).
# The leading term is e(h 16^{n-1} pi) = e(h * frac(16^{n-1} pi)) = the REAL digit orbit of pi.
print("\n-- the real pi orbit: e(h * {16^{n-1} pi})  (this is what normality means) --")
for h in [1,3]:
    for Nn in [20,40,80]:
        Wpi = sum(e(h*mp.frac(mp.power(16,n-1)*pi)) for n in range(1,Nn+1))/Nn
        print(f"  h={h} N={Nn}: |(1/N)sum e(h{{16^{{n-1}}pi}})| = {abs(Wpi):.5f}")
