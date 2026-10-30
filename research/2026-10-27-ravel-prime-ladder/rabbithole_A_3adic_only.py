"""Pin down the EXACT discriminating statement for Rabbithole A.

The core claim to test precisely:
  Does D_N(1/3) -> 0 for the AUTHENTIC source, but NOT for the coherent control -T_n?

We need the control's FULL solenoid defect (with its real phase e(-a T_n) -> e(0) coherent)
and its 3-adic factor psi_3(a * frac_3(-T_n)).

Control real phase: e(a V_n) = e(-a T_n) -> e(0) = 1 as n -> inf (T_n -> 0, summable).
So the control's solenoid defect:
  D_N^control(a) = (1/N) sum_n [ e(-a T_n) psi_3(a frac_3(-T_n)) - e(-3a T_n) psi_3(3a frac_3(-T_n)) ]
Since T_n -> 0, e(-a T_n) -> 1 and e(-3a T_n) -> 1, so
  D_N^control(a) -> (1/N) sum_n [ psi_3(a z3_n^ctrl) - psi_3(3a z3_n^ctrl) ]
where z3_n^ctrl = frac_3(-T_n) is the control's 3-adic memory (v3=4, structured 19/81,34/81,...).

The KEY question: does this control limit go to 0 or stay bounded away?

Let me compute the control's 3-adic-factor-only defect (dropping the real phase which ->1),
and see if it decays or not.  This isolates whether the 3-adic memory ALONE discriminates.
"""
from fractions import Fraction
import cmath, math

def r(n):
    n=Fraction(n)
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)
def v3(B):
    v=0; b=B
    while b%3==0: b//=3; v+=1
    return v
def frac_3(A,B):
    v=v3(B)
    if v==0: return Fraction(0)
    b=B//(3**v)
    bi=pow(b,-1,3**v)
    return Fraction((A*bi)%(3**v),3**v)
def psi3(a,z3):
    m=a.numerator
    s=0; d3=a.denominator
    while d3%3==0: d3//=3; s+=1
    nz=z3.numerator; v=v3(z3.denominator)
    if s==0: return Fraction((m*nz)%(3**v),3**v) if v>0 else Fraction(0)
    return Fraction((m*nz)%(3**(s+v)),3**(s+v))
def phase_of(f): return cmath.exp(2j*math.pi*float(f))

def Tn_partial(n,J):
    s=Fraction(0)
    for j in range(1,J+1): s += Fraction(1,16**j)*r(n+j)
    return s

a=Fraction(1,3)
# Control 3-adic-factor defect (real phase -> 1 dropped)
def control_defect_3adic(N):
    s=0j
    for n in range(1,N+1):
        T=Tn_partial(n,30)
        z3=frac_3(T.numerator, T.denominator)  # frac_3(-T) = frac_3(T) (sign irrelevant mod 3^v? no: -T has -num)
        # careful: frac_3(-T_n) uses -num
        An=-T.numerator; Bn=T.denominator
        z3=frac_3(An,Bn)
        s += phase_of(psi3(a,z3)) - phase_of(psi3(3*a,z3))
    return s/N

print("=== CONTROL (-T_n) 3-adic-factor defect: does it decay? ===")
for N in [20,50,100,200,400]:
    d=abs(control_defect_3adic(N))
    print(f"  N={N}: |control D_N(1/3)| = {d:.6f}")

# Authentic 3-adic-factor defect (same computation, authentic U_n)
def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U
U=Us(400)
def authentic_defect_3adic(N):
    s=0j
    for n in range(1,N+1):
        A=U[n].numerator; B=U[n].denominator
        z3=frac_3(A,B)
        s += phase_of(psi3(a,z3)) - phase_of(psi3(3*a,z3))
    return s/N
print("\n=== AUTHENTIC 3-adic-factor defect: does it decay? ===")
for N in [20,50,100,200,400]:
    d=abs(authentic_defect_3adic(N))
    print(f"  N={N}: |auth D_N(1/3)| = {d:.6f}")
