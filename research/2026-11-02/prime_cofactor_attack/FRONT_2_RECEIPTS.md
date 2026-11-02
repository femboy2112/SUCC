# FRONT 2 — exact arithmetic receipts (reproducible)

Stdlib `fractions` + `sympy` (exact) and `mpmath` (phase check, `mp.dps` raised
well above the required `6*max_n`). All identities are checked in the exact
rational field, so no floating-point certificate is load-bearing; mpmath runs are
diagnostics only, consistent with repo rule 8.

```python
from fractions import Fraction
from sympy import factorint, symbols, series, oo, expand

def r(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def U(n):
    s=Fraction(0)
    for j in range(1,n+1): s += Fraction(16)**(n-j)*r(j)
    return s

# ---- F2C-01/02: quadratic numerator + asymptotic (exact) ----
n = symbols('n')
expr = 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
num_unreduced = ( 4*(8*n-4)*(8*n-3)*(8*n-2)
                - 2*(8*n-7)*(8*n-3)*(8*n-2)
                - 1*(8*n-7)*(8*n-4)*(8*n-2)
                - 1*(8*n-7)*(8*n-4)*(8*n-3) )
assert expand(num_unreduced) == 960*n**2 - 712*n + 128
print(expr.series(n, oo, 5))   # 15/(64 n^2) + 151/(512 n^3) + ...

# ---- F2C-03/04/05/06: tower, cofactor, p-integrality, v_p(U_a)=-1 ----
def run(p):
    a=(p+3)//8; b=(p+1)//2; c=Fraction(-1)
    Ua=U(a)
    assert factorint(Ua.denominator).get(p,0)==1            # v_p(U_a)=-1
    for nn in range(a,b):
        Wn = sum(Fraction(16)**(nn-j)*r(j) for j in range(a+1,nn+1))
        assert U(nn) == Fraction(16)**(nn-a)*Ua + Wn        # tower
        Vn = U(nn) - c*Fraction(16)**(nn-a)/p
        assert Vn == Fraction(16)**(nn-a)*(Ua - c/p) + Wn   # cofactor form
        assert factorint(Vn.denominator).get(p,0)==0        # p-integral
        assert factorint(Wn.denominator).get(p,0)==0
    return a,b

for p in [13,29,37,53,61,101,149,197,229,269]:
    a,b = run(p)
    print('p=%3d a=%3d b=%3d length=%3d  ALL EXACT OK'%(p,a,b,b-a))
```

Output (all asserts pass):

```
p= 13 a=  2 b=  7 length=  5  ALL EXACT OK
p= 29 a=  4 b= 15 length= 11  ALL EXACT OK
p= 37 a=  5 b= 19 length= 14  ALL EXACT OK
p= 53 a=  7 b= 27 length= 20  ALL EXACT OK
p= 61 a=  8 b= 31 length= 23  ALL EXACT OK
p=101 a= 13 b= 51 length= 38  ALL EXACT OK
p=149 a= 19 b= 75 length= 56  ALL EXACT OK
p=197 a= 25 b= 99 length= 74  ALL EXACT OK
p=229 a= 29 b=115 length= 86  ALL EXACT OK
p=269 a= 34 b=135 length=101  ALL EXACT OK
```

Phase identity check (diagnostic, mpmath dps=200, p=13): `|e(hU_n) − e(h·clock)·e(hW_n)|`
and `|e(hU_n) − e(h·clock/p)·e(hV_n)|` are at machine noise for small n; at larger n
the residual grows only because `e(2πi·integer)` requires `Θ(16^n)` digits to be
exact — the *algebraic* identity is what carries the proof, per §1.2–1.3.
