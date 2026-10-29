"""Independent SymPy + rational integer oracle; no imports from the research module.

A distinct method verifies the bounding polynomial and adversarial all-boundary
zero runs. It is not an external blind proof or a hosted CI run.
"""
from fractions import Fraction as Q
from math import ceil, floor, gcd, isqrt, log
import json
import sympy as sp

n=sp.Symbol('n',integer=True,positive=True)
a=8*n-7
r=sp.cancel(sp.Rational(4,1)/a-sp.Rational(2,1)/(a+3)-1/(a+4)-1/(a+5))
assert sp.factor(r-(sp.Rational(6,1)/(a*(a+3))+sp.Rational(4,1)/(a*(a+4))+sp.Rational(5,1)/(a*(a+5)))) == 0

P=272*n**4-846*n**3+680*n**2-206*n+21
D=2*n*n*(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
assert sp.cancel(sp.Rational(1,2)/n**2-r-P/D)==0
z=sp.Symbol('z',integer=True,nonnegative=True)
translated=sp.expand(P.subs(n,z+3))
assert translated==272*z**4+2418*z**3+7754*z**2+10408*z+4713

# Independent direct recurrence using a chosen rational pre-event phase.
# No reliance on the implementation of the primary module.
checks=0
for n0 in range(3,385):
    rr=Q(4,8*n0-7)-Q(2,8*n0-4)-Q(1,8*n0-3)-Q(1,8*n0-2)
    ell=0
    while 16**(ell+1)<=n0*n0: ell+=1
    for c in range(1,17):
        x=(Q(c,1)-rr/2)/16
        bare=int(16*x)
        raw=16*x+rr
        carry=int(raw)
        x=raw-carry
        assert carry==c and bare==c-1 and x==rr/2
        checks+=1
        for t in range(n0+1,n0+ell+1):
            v=Q(4,8*t-7)-Q(2,8*t-4)-Q(1,8*t-3)-Q(1,8*t-2)
            raw=16*x+v
            carry=int(raw)
            assert carry==0
            x=raw-carry
            checks+=1

# Independent exact Walsh orthogonality and finite source marginal.
walsh_checks=0
for mask in range(16):
    for other in range(16):
        value=sum((-1)**((digit&mask).bit_count()+(digit&other).bit_count()) for digit in range(16))
        assert value==(16 if mask==other else 0)
        walsh_checks+=1

# Strong no-go: non-decaying forcing generates a correction at every time.
x=Q(0)
for t in range(1,101):
    bare=int(16*x)
    y=16*x+1
    carry=int(y)
    assert bare==0 and carry==1
    x=y-carry

# Finite return and zero-seed original trace, exact independent rational method.
x=Q(0)
N=2048
errors=[]
for t in range(1,N+1):
    v=Q(4,8*t-7)-Q(2,8*t-4)-Q(1,8*t-3)-Q(1,8*t-2)
    base=int(16*x)
    y=16*x+v
    carry=int(y)
    if base!=carry: errors.append(t)
    x=y-carry

result={
  "sympy_identity":"PASS",
  "translated_positive_polynomial":str(translated),
  "adversarial_rational_checks":checks,
  "walsh_checks":walsh_checks,
  "nondecaying_force_negative_control":"100 corrections / 100 steps",
  "authentic_zero_seed_horizon":N,
  "authentic_zero_seed_mismatches":errors,
  "status":"finite observations are not a proof of no future corrections"
}
print(json.dumps(result,sort_keys=True,indent=2))
