"""Fresh algebraic review cases; does not import any front's implementation."""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import hashlib,json
import sympy as S

def r(a):return 4/a-2/(a+3)-1/(a+4)-1/(a+5)
def raw_moment(a,j):
    from math import factorial
    return sum((c*Q(factorial(j),(a+d)**(j+1)) for d,c in ((0,4),(3,-2),(4,-1),(5,-1))),Q())/r(Q(a))

# Alternate radices are held out from the native239 derivation.
modular=[]
for b in (2,3,5,11,17,31):
    D=b*b-b-1
    for m in (5,7,13,19,31):
        actual={(x,y) for x in range(m) for y in range(m)
                if (x+y-b*x)%m==0 and (x-b*y)%m==0}
        expected={(b*t%m,t) for t in range(m) if D*t%m==0}
        assert actual==expected
        assert len(actual)==gcd(m,D)
        modular.append({'radix':b,'modulus':m,'rows':len(actual)})

# Direct symbolic characteristic function/density for the Gamma memory limit.
t=S.symbols('t',nonnegative=True)
sq=S.sqrt(5); lam=(sq-1)/2; phi=(sq+1)/2
A=phi**2;B=phi;C=9+4*sq
density_transform=C*(2/(t+A)+1/(t+A)**2-2/(t+B)+1/(t+B)**2)
target=(1+lam**2*t)**-2*(1+lam*t)**-2
assert S.simplify(density_transform-target)==0

# Native source mean derivative and variance lower bound at fresh age/tilt.
a=S.symbols('a',positive=True)
mean=-S.diff(r(a),a)/r(a)
variance=S.diff(S.log(r(a)),a,2)
assert S.simplify(S.diff(mean,a)+variance)==0
clock=[]
for av,sv,c,d in ((Q(97),Q(5,11),3,5),(Q(233),Q(7,13),8,13),
                  (Q(31,3),Q(11,17),21,34)):
    mu=lambda x:raw_moment(x,1)
    defect=(c+d)*mu(av+sv)-c*mu(av+c*sv)-d*mu(av+d*sv)
    lower=2*c*(1/(av+sv+5)-1/(av+c*sv+5))+2*d*(1/(av+sv+5)-1/(av+d*sv+5))
    assert defect>lower>0
    clock.append({'a':str(av),'s':str(sv),'weights':[c,d],
                  'defect':str(defect),'lower':str(lower)})

# Twice integrated residual moment factors, independent symbolic Fubini check.
z,t=S.symbols('z t',nonnegative=True)
residual_factors=[]
for L in (1,5,17):
    for k in (0,1,2,3,4,5,8,13):
        val=S.integrate(z**(k+L)*(t-z),(z,0,t))
        target=t**(k+L+2)/((k+L+1)*(k+L+2))
        assert S.simplify(val-target)==0
        residual_factors.append([L,k])

root=Path(__file__).resolve().parent
papers=['composition/FIBONACCI_COMPOSITION.md','arrows/FIBONACCI_ARROWS.md',
        'clock_constants/CLOCK_CONSTANTS.md']
out={'status':'PASS','authority':'complementary shared-model algebra checks; not a formal proof checker',
     'radix_modulus_cases':modular,'gamma_transform_identity':True,
     'source_clock_cases':clock,'residual_fubini_cases':residual_factors,
     'reviewed_hashes':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in papers}}
print(json.dumps(out,indent=2))
