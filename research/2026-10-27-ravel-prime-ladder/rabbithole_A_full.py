"""Final honest assessment of Rabbithole A: does the FULL solenoid defect (real x 3-adic)
discriminate the authentic source from the coherent control -T_n?

We compute the FULL defect with BOTH factors for authentic and control, using exact
rational arithmetic.  The real phase e(a U_n) for authentic is exact (U_n rational).
For control, e(-a T_n) with T_n exact rational (partial sum, J=30 gives <16^-30 error).

The decisive question: is there a character a and a schedule where authentic -> 0 but
control stays bounded away?  If not, Rabbithole A is REFUTED as a discriminating handle,
and the honest result is a NEGATIVE one (the 3-adic memory does NOT restore discrimination).
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

def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U

U=Us(300)
a=Fraction(1,3)

# FULL authentic defect (real x 3adic)
def full_auth(N):
    s=0j
    for n in range(1,N+1):
        A=U[n].numerator; B=U[n].denominator
        u=Fraction(A,B); z3=frac_3(A,B)
        s += phase_of((a*u)%1)*phase_of(psi3(a,z3)) - phase_of(((3*a)*u)%1)*phase_of(psi3(3*a,z3))
    return s/N

# FULL control defect: V_n = -T_n. real phase e(a V_n)=e(-a T_n), 3adic = frac_3(-T_n)
def full_control(N):
    s=0j
    for n in range(1,N+1):
        T=Tn_partial(n,30)
        An=-T.numerator; Bn=T.denominator
        v = Fraction(An,Bn)  # V_n = -T_n
        z3=frac_3(An,Bn)
        s += phase_of((a*v)%1)*phase_of(psi3(a,z3)) - phase_of(((3*a)*v)%1)*phase_of(psi3(3*a,z3))
    return s/N

print("=== FULL solenoid defect D_N(1/3): authentic vs control -T_n ===")
for N in [30,60,120,240,300]:
    da=abs(full_auth(N)); dc=abs(full_control(N))
    print(f"  N={N}: auth={da:.5f}  control={dc:.5f}  ratio={dc/(da+1e-12):.3f}")

print()
print("=== interpretation ===")
print("If auth -> 0 and control stays bounded away: DISCRIMINATING (genuine new handle).")
print("If both decay similarly: the real phase dominates and we're back at the Weyl wall.")
print("If both stay bounded: the 3-adic factor doesn't help; Rabbithole A refuted.")
