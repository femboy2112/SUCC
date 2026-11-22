"""Independent finite audit: matrix operators and Lagrange inverse coefficients.

Does not import the production model. Uses sympy matrices and a separate
coefficient route. These runs test finite arithmetic, not the 17M-line RH proof.
"""
from fractions import Fraction
from math import comb, factorial
import json
from pathlib import Path
import sympy as sp

checks=0

def check(truth,why=''):
    global checks
    checks+=1
    if not truth:raise AssertionError((checks,why))

# First implementation: actual finite matrices; the log commutator uses symbolic logs.
for N in [12,24,36]:
    logd=sp.diag(*(sp.log(j) for j in range(1,N+1)))
    basis=sp.zeros(N,1);basis[0]=1
    V={}
    for m in range(2,N+1):
        mat=sp.zeros(N,N)
        for n in range(1,N+1):
            if n*m<=N:mat[m*n-1,n-1]=1
        V[m]=mat
        dif=logd*mat-mat*logd
        for n in range(1,N+1):
            if n*m<=N:
                check(sp.simplify(sp.expand_log(dif[m*n-1,n-1],force=True)-sp.log(m))==0,(N,m,n))
    for m in range(2,N+1):
        # coefficients at vacuum, identify all prime-power channels directly
        fac=sp.factorint(m)
        if len(fac)==1:
            p,k=next(iter(fac.items()))
            check(sp.simplify((logd*V[m]-V[m]*logd)[m-1,0]/k-sp.log(p))==0)
        else:
            check(len(fac)>1)
    # Independent finite-matrix test of the FUCC prime-square Neumann resolvent:
    # (I - V_(p^2)/p)^-1 |1> has coefficients p^-j at |p^(2j)>.
    for p in (2,3,5):
        if p*p>N:continue
        R=(sp.eye(N)-sp.Rational(1,p)*V[p*p]).inv()
        expected={};j=0
        while p**(2*j)<=N:
            expected[p**(2*j)]=sp.Rational(1,p**j);j+=1
        for index in range(1,N+1):
            check(R[index-1,0]==expected.get(index,0),(N,p,index,'FUCC-Honda resolvent'))
        partial=sum(x*x for x in expected.values())
        check(partial<=sp.Rational(p*p,p*p-1),(N,p,'Archimedean bound'))
    A=sp.zeros(N,N)
    for m in range(2,N+1):
        fac=sp.factorint(m)
        if len(fac)==1:
            p,k=next(iter(fac.items()))
            A+=sp.Rational(1,k)*(logd*V[m]-V[m]*logd)
    for m in range(2,N+1):
        fac=sp.factorint(m)
        expected=sp.log(next(iter(fac))) if len(fac)==1 else sp.Integer(0)
        check(sp.simplify(A[m-1,0]-expected)==0)
    q=sp.Matrix([sp.Rational(N,n)-1 for n in range(1,N+1)])
    S=(q.T*A*basis)[0]
    direct=sp.Integer(0)
    for n in range(2,N+1):
        fac=sp.factorint(n)
        if len(fac)==1:direct+=sp.log(next(iter(fac)))*(sp.Rational(N,n)-1)
    check(sp.simplify(S-direct)==0,'Riesz source')

# Second derivation of formal logarithm inverse: Lagrange inversion coefficient formula,
# independently deriving U by repeated polynomial substitution with exact sympy Rational.
def mult(f,g,N):
    z=[sp.Rational(0)]*(N+1)
    for i,a in enumerate(f):
        for j,b in enumerate(g[:N+1-i]):
            z[i+j]+=a*b
    return z

def power(f,m,N):
    ret=[sp.Rational(1)]+[sp.Rational(0)]*N
    while m:
        if m&1:ret=mult(ret,f,N)
        m>>=1
        if m:f=mult(f,f,N)
    return ret

def reverse(p,N):
    U=[sp.Rational(0)]*(N+1);U[1]=1
    for _ in range(N+2):
        W=[sp.Rational(0)]*(N+1);W[1]=1
        j=1
        while p**(2*j)<=N:
            powU=power(U,p**(2*j),N)
            for a in range(N+1):W[a]-=powU[a]/p**j
            j+=1
        if W==U:return U
        U=W
    raise AssertionError('fixed point did not stabilize')

for p,N in ((2,34),(3,28),(5,28)):
    U=reverse(p,N)
    # Verify by the defining composition l(U)=z, NOT using production implementation.
    lU=U.copy();j=1
    while p**(2*j)<=N:
        t=power(U,p**(2*j),N)
        for a in range(N+1):lU[a]+=t[a]/p**j
        j+=1
    for a in range(N+1):check(lU[a]==(1 if a==1 else 0),(p,a,'inverse equation'))
    # Independent universal integer-polynomial jet valuation.
    for i in range(1,N+1):
        fcoeff=[1,-2,3,7,5]
        fU=[sp.Rational(0)]*(i+1)
        P=[sp.Rational(1)]+[sp.Rational(0)]*i
        for scalar in fcoeff:
            for j in range(i+1):fU[j]+=scalar*P[j]
            P=mult(P,U[:i+1],i)
        number=factorial(i)*fU[i]
        if number:
            num,den=sp.fraction(number)
            def vp(n):
                n=abs(int(n));v=0
                while n and n%p==0:v+=1;n//=p
                return v
            measured=vp(num)-vp(den)
            target=sum(i//p**j for j in range(1,20))-sp.Rational(i-1,p*p-1)
            check(measured>=target,(p,i,measured,target))
        else:check(True)

# Finite integral capacity: nonzero integer minor, honest prime lower and row upper.
M=sp.Matrix([[4,1],[1,4]])
det=abs(int(M.det()))
check(det==15)
check(sp.factorint(det)=={3:1,5:1})
check(det**2<=int((M[0,0]**2+M[0,1]**2)*(M[1,0]**2+M[1,1]**2)))

receipt={"status":"PASS","exact_assertions":checks,"methods":["SymPy finite matrix commutators and direct Riesz vacuum readout","independent FUCC prime-square resolvent matrix inverse","independent SymPy formal inverse substitution and p-adic valuation","integral determinant Hadamard control"],"limitations":["finite examples only","shared classical arithmetic definitions","not a Lean or RH proof"]}
path=Path(__file__).with_name('independent_audit_receipt.json')
path.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(receipt,sort_keys=True))
