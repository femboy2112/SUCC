"""
Round 2 f_4-transfer — exact computation receipts.

All phase identities exact in Fraction. Diagnostics only where noted.
No floating-point certificate is load-bearing.
"""
from fractions import Fraction
from sympy import factorint, symbols, series, oo, expand, gcd, nsimplify

def r(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def f(m, n):
    return Fraction(1,8*n-7)-Fraction(1,8*n-7+m)

def U(n):
    s=Fraction(0)
    for j in range(1,n+1): s += Fraction(16)**(n-j)*r(j)
    return s

def U_m(m, coeff, n):
    # U^{(m)}_n = sum_{j<=n} 16^{n-j} coeff_m f_m(j)
    s=Fraction(0)
    for j in range(1,n+1): s += Fraction(16)**(n-j)*coeff*f(m,j)
    return s

print("=== 1. f_m decomposition identity ===")
n = symbols('n')
lhs = 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
rhs = 2*(1/(8*n-7)-1/(8*n-4)) + 1*(1/(8*n-7)-1/(8*n-3)) + 1*(1/(8*n-7)-1/(8*n-2))
print("r == 2f3+f4+f5 :", expand(lhs-rhs)==0)

print("\n=== 2. f_m asymptotics (exact) ===")
for m in [3,4,5]:
    s = (1/(8*n-7)-1/(8*n-7+m)).series(n, oo, 5)
    print(f"f_{m}(n) ~ {s}")

print("\n=== 3. f_m increments / smoothness: f_m(n+1)-f_m(n) ===")
for m in [3,4,5]:
    d = expand((1/(8*(n+1)-7)-1/(8*(n+1)-7+m)) - (1/(8*n-7)-1/(8*n-7+m)))
    # asymptotic
    ds = ((1/(8*(n+1)-7)-1/(8*(n+1)-7+m)) - (1/(8*n-7)-1/(8*n-7+m))).series(n, oo, 6)
    print(f"f_{m}(n+1)-f_{m}(n) ~ {ds}")

print("\n=== 4. f_m exact numerators (quadratic) ===")
for m in [3,4,5]:
    num = expand((8*n-7+m)-(8*n-7))  # numerator of 1/(8n-7) - 1/(8n-7+m)
    print(f"f_{m}: num = {num} (constant), denom=(8n-7)(8n-7+{m})")

print("\n=== 5. p=13 window: exact edge isolation of pole ===")
p = 13
a = (p+3)//8
b = (p+1)//2
c = Fraction(-1)
print(f"p={p}, a_p={a}, b_p={b}, window [{a},{b})")
print(f"f_3(a)={f(3,a)}, f_4(a)={f(4,a)}, f_5(a)={f(5,a)}")
# confirm pole -1/p in f_4(a) only
print("f_4(a) =", f(4,a), "= 1/(p-4)-1/p =", Fraction(1,p-4)-Fraction(1,p), "->", f(4,a)==Fraction(1,p-4)-Fraction(1,p))

print("\n=== 6. V_{p,n} decomposition by edge, p=13 (unit coeff in U_m) ===")
for nn in range(a, b):
    Vn = U(nn) - c*Fraction(16)**(nn-a)/p
    U3 = U_m(3, 1, nn)
    U5 = U_m(5, 1, nn)
    U4 = U_m(4, 1, nn)
    # U_n = 2 U3 + U4 + U5  (exact)
    assert U(nn) == 2*U3 + U4 + U5, f"U decomposition fails at n={nn}"
    # V = U_n + 16^{n-a}/p = 2 U3 + U5 + (U4 + 16^{n-a}/p)   [pole removed from f_4(a)]
    Vn_decomp = 2*U3 + U5 + (U4 + Fraction(16)**(nn-a)/p)
    ok = (Vn == Vn_decomp)
    print(f"n={nn}: U==2U3+U4+U5 : True ; V==2U3+U5+(U4+16^{nn-a}/p) : {ok}")

print("\n=== 7. increment magnitude: V_{p,n+1}-V_{p,n} vs V_{p,n} (p=13) ===")
for nn in range(a, b-1):
    Vn = U(nn) - c*Fraction(16)**(nn-a)/p
    Vn1 = U(nn+1) - c*Fraction(16)**(nn+1-a)/p
    inc = Vn1 - Vn
    print(f"n={nn}: V={float(Vn):.3e}, inc={float(inc):.3e}, inc/V={float(inc/Vn):.3f}, "
          f"check inc==15V+r(n+1): {inc == 15*Vn + r(nn+1)}")
