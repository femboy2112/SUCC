"""No producer import: positive Frullani, Beta quadrature and SymPy transforms.

Numerical quadrature is calibration, not interval authority or external review.
"""
from pathlib import Path
from fractions import Fraction
import json
import mpmath as mp
import sympy as sp
root=Path(__file__).resolve().parent
mp.mp.dps=100

def rational(s):
    v=Fraction(s)
    return mp.mpf(v.numerator)/v.denominator

def R(a):return 6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5))

def fib(n):
    # Matrix powering, distinct from producer's iterative scalar recurrence.
    M=sp.Matrix([[1,1],[1,0]])**n
    return int(M[0,1])

record=json.loads((root/'exact_receipt.json').read_text())
rows=[]
for row in record['uniform_rows']:
    a=mp.mpf(row['a']);k=row['k'];norm=R(a)
    def f(v):
        ell=R(a*(1+v))/norm
        return (ell-ell**k)/v
    increment=mp.quad(f,[0,mp.mpf(1)/k,1,mp.inf])
    baseline=mp.digamma(2*k)-mp.digamma(2)
    gap=increment-baseline
    lo,hi=map(rational,row['gap'])
    assert lo<=gap<=hi
    rows.append({'k':k,'a':row['a'],'gap':mp.nstr(gap,75),'status':'PASS'})
holdouts=[]
for k,age in [(89,1009),(233,4093),(987,8191)]:
    a=mp.mpf(age);norm=R(a)
    gap=mp.quad(lambda v:(R(a*(1+v))/norm-(R(a*(1+v))/norm)**k)/v,
                [0,mp.mpf(1)/k,1,mp.inf])-mp.digamma(2*k)+mp.digamma(2)
    center=mp.mpf(1379)/900*(k-1)/(2*k+1)
    assert abs(a*a*gap-center)<=mp.mpf(1627)/(45*a)
    holdouts.append({'k':k,'a':age,'scaled_gap':mp.nstr(a*a*gap,75),'status':'PASS'})
lam=(mp.sqrt(5)-1)/2
native=[]
for row in record['source_arrow_rows']:
    a=rational(row['a']);norm=R(a)
    mean=-mp.diff(R,a)/norm
    def j(v):
        t=a*v
        lv=R(a+lam**2*t)*R(a+lam*t)/norm**2
        return (lv-mp.exp(-mean*t))/v
    gap=mp.quad(j,[0,1,mp.inf])
    bound_lo,bound_hi=map(rational,row['jensen_lower_interval'])
    assert gap>bound_hi>bound_lo>0
    native.append({'a':row['a'],'jensen_gap':mp.nstr(gap,75),'status':'PASS'})
s=mp.sqrt(5);phi=(1+s)/2
beta_log=mp.digamma(4)+mp.quad(lambda p:6*p*(1-p)*mp.log(lam**2*p+lam*(1-p)),[0,1])
closed=-mp.euler+5+2*s-(19+7*s)/2*mp.log(phi)
assert abs(beta_log-closed)<mp.mpf('1e-90')
gap=mp.log(2)-beta_log
lo,hi=map(rational,record['gamma_memory_gap_interval'])
assert lo<gap<hi
z=sp.symbols('z');sqrt5=sp.sqrt(5);l=(sqrt5-1)/2;A=1/l**2;B=1/l
rhs=(9+4*sqrt5)*(2/(z+A)+1/(z+A)**2-2/(z+B)+1/(z+B)**2)
assert sp.simplify(rhs-1/((1+l*l*z)**2*(1+l*z)**2))==0
assert sp.simplify(rhs.subs(z,0))==1
for n in range(2,41):
    assert fib(n-2)**2+fib(n-1)**2==fib(2*n-3)
# Finite reciprocal sum via independently produced matrix entries.
sum80=sum(Fraction(1,fib(j)) for j in range(1,81))
lo,hi=map(Fraction,record['reciprocal_F_interval'])
assert lo<=sum80<hi
out={'status':'PASS','authority':'separate positive-integral and symbolic oracle; numerical integrals are not certificates',
     'mpmath':mp.__version__,'sympy':sp.__version__,'dps':mp.mp.dps,
     'uniform_rows':rows,'fresh_joint_rank_holdouts':holdouts,'native_jensen_rows':native,
     'gamma_beta_log':mp.nstr(beta_log,75),'gamma_memory_gap':mp.nstr(gap,75),
     'symbolic_laplace_identities':2,'matrix_fibonacci_checks':39}
p=root/'oracle_receipt.json'
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
