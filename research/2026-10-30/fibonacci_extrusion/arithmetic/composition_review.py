"""Complementary exact checks of composition FIC01/FIC05, no front imports."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
import sympy as S

root=Path(__file__).resolve().parent
reviewed=root.parent/'composition'/'FIBONACCI_COMPOSITION.md'
# Recover un-tilted rate moments by direct polynomial integration.
x=S.symbols('x')
moments=[]
for degree in range(3):
    value=(2*S.integrate(x**degree,(x,0,3))+S.integrate(x**degree,(x,0,4))+S.integrate(x**degree,(x,0,5)))/15
    moments.append(value)
sigma=S.simplify(moments[2]-moments[1]**2)
assert moments[0]==1 and sigma==S.Rational(1379,900)
assert 10*sigma+S.Rational(125,6)==S.Rational(1627,45)

# Symmetric Dirichlet moments via factorial Gamma ratios, not copied formulas.
dirichlet=[]
for k in (2,3,7,29,101):
    ew2=S.factorial(3)*S.factorial(2*k-1)/S.factorial(2*k+1)
    ewij=4*S.factorial(2*k-1)/S.factorial(2*k+1)
    coefficient=S.simplify((1-k*ew2)/2)
    assert ew2==S.Rational(3,k*(2*k+1))
    assert ewij==S.Rational(2,k*(2*k+1))
    assert coefficient==S.Rational(k-1,2*k+1)
    dirichlet.append(dict(k=k,coefficient=str(coefficient)))

# Source mean from differentiation of the collapsed rational R.
a=S.symbols('a',positive=True)
R=(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))
mean=S.cancel(-S.diff(R,a)/R)
def m(t):return Q(str(mean.subs(a,S.Rational(t.numerator,t.denominator))))

def laplace(age,weight,frequency):
    age,weight,frequency=map(S.Rational,(age,weight,frequency))
    return S.cancel(R.subs(a,age+weight*frequency)/R.subs(a,age))

rows=[]
for age,s,c,d in ((Q(23,2),Q(5,11),Q(2,3),Q(7,5)),
                  (Q(31,3),Q(7,13),Q(3),Q(8)),
                  (Q(19,2),Q(2,7),Q(0),Q(9,4)),
                  (Q(41,3),Q(3,17),Q(5,3),Q(5,3))):
    t=s*max(c,d)
    endpoint=c*m(age+s*c)+d*m(age+s*d)
    common=(c+d)*m(age+t)
    unequal=bool(c and d and c!=d)
    assert (endpoint>common)==unequal
    lhs=laplace(age+s*c,c,Q(3,5))*laplace(age+s*d,d,Q(3,5))
    rhs=laplace(age+t,c,Q(3,5))*laplace(age+t,d,Q(3,5))
    assert (lhs!=rhs)==unequal
    rows.append(dict(a=str(age),s=str(s),c=str(c),d=str(d),forced_shift=str(t),
                     exact_mean_gap=str(endpoint-common),unequal_laws=unequal))

out=dict(status='PASS',scope='Complementary review of FIC01 and FIC05 only',
    reviewed_sha256=hashlib.sha256(reviewed.read_bytes()).hexdigest(),
    rate_moments=list(map(str,moments)),variance=str(sigma),
    dirichlet_cases=dirichlet,scalar_clock_cases=rows,
    reasoner_authority='Same-model sibling review; computational routes differ, no external referee')
(root/'composition_review_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
