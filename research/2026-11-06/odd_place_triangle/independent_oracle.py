"""Different exact CRT/provenance route with SymPy direct symbolic formula."""
from fractions import Fraction
from math import gcd
import sympy as s
from adelic_triangle import state, source, prime_birth

n=s.symbols('n',integer=True,positive=True)
r=s.cancel(s.Rational(4)/(8*n-7)-s.Rational(2)/(8*n-4)-1/(8*n-3)-1/(8*n-2))
a=(120*n**2-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
assert s.factor(r-a)==0

# Direct CRT by selecting idempotents of the odd denominator, without
# importing or using the implementation's p-principal-part function.
for n0 in [1,2,5,7,13,21,29,37,41]:
    u=state(n0)
    den=u.denominator;num=u.numerator
    fac=s.factorint(den)
    assert 2 not in fac
    q_total=0
    for p,exp in fac.items():
        P=int(p**exp);cop=den//P
        residue=(num*pow(cop,-1,P))%P
        q_total+=Fraction(residue,P)
    assert (q_total-u).denominator==1

# Independently reconstruct first-pole location without the source code's
# predicted_first_pole function: find D roots and verify p*r residue.
for p in [7,11,13,17,19,23,29,37,53,101,149,181,197,269,293]:
    first=next(j for j in range(1,p+1) if ((2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))%p==0)
    assert first==prime_birth(p)[0]
    v=p*source(first)
    assert v.denominator%p!=0 and v.numerator%p!=0

# Gauss digamma gamma cancellation against exact silver-ratio closed form
w=[4,-2,-1,-1];a0=[7,4,3,2]
expr=-s.Add(*(s.Rational(ww,8)*s.digamma(1-s.Rational(aa,8)) for ww,aa in zip(w,a0)))
silver=s.pi*(4+5*s.sqrt(2))/16+s.Rational(5,8)*s.log(2)+5*s.sqrt(2)/8*s.log(1+s.sqrt(2))
assert abs(complex(s.N(expr-silver,70)))<1e-60
assert sum(w)==0
print('INDEPENDENT_EXACT_CRT_SOURCE_ORACLE_PASS 9 CRT states, 15 p births, symbolic four poles, silver digamma')
