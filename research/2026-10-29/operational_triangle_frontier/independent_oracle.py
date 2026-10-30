"""Independent SymPy/mpmath oracle: does NOT import operational_triangle.

Checks the joint first jet by a separately written moment expansion; samples
finite integrals for high-precision, NON-INTERVAL numerical holdouts.
"""
import json
import sympy as s
from mpmath import mp

z,t,y=s.symbols('z t y')
b=z-1
d=2+t-z
# Exact Gamma(2) moments: integral y^k exp(-d*y) dy = k!/d^(k+1).
def moment(k):
    return s.factorial(k) / d**(k+1)

# Original Q(y/a)/(aR(a)) first correction:
#  (59/240)(2-y)*y*exp(-y), n=clock-to-infinity.
density = s.Rational(59,240)*(2*moment(1)-moment(2))
# Bernoulli conditional correction on *leading* Gamma(2) density:
binomial = b*(s.Rational(7,8)*moment(2)-s.Rational(1,2)*moment(3)) - b*b*moment(3)/2
original = s.factor(density+binomial)
fake = s.factor(binomial)
source_specific = s.factor(original-fake)
expected = (59*t*t+92*t*z-33*t-511*z*z+813*z-302)/(120*d**4)
expected_defect = s.Rational(59,120)*(1+t-z)/d**3
assert s.simplify(original-expected)==0
assert s.simplify(source_specific-expected_defect)==0
assert s.simplify(original.subs(t,0)-(1-z)*(511*z-302)/(120*(2-z)**4))==0
assert s.simplify(original.subs({t:0,z:0})+s.Rational(151,960))==0
assert s.simplify(s.integrate(source_specific.subs(t,0)/(1-z),(z,0,1))-s.Rational(59,320))==0

# Authentic source is Q(x)=sum coefficients, all four poles intact.
mp.dps=75
coeffs=((0,4),(3,-2),(4,-1),(5,-1))

def trueR(a):
    return mp.fsum(c/(a+k) for k,c in coeffs)

def sourceQ(x):
    return 4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)

def finite_joint(n,z,t,mutant=False):
    a=8*n-7
    za=mp.mpf(z); ta=mp.mpf(t)
    def integrand(yy):
        q=(15*yy/a) if mutant else sourceQ(yy/a)
        norm=(15/mp.mpf(a*a)) if mutant else trueR(a)
        return mp.exp(-(1+ta)*yy)*q/(a*norm) * (za+(1-za)*mp.exp(-8*yy/a))**n
    return mp.quad(integrand,[0,5,20,mp.inf])

cases=[(0,0),(mp.mpf('0.5'),mp.mpf('0.5')),(mp.mpf('0.75'),mp.mpf('1'))]
receipts=[]
for zz,tt in cases:
    exact1=mp.mpf(str(original.subs({z:s.Rational(str(zz)),t:s.Rational(str(tt))}).evalf(70)))
    exact_fake=mp.mpf(str(fake.subs({z:s.Rational(str(zz)),t:s.Rational(str(tt))}).evalf(70)))
    for n in (20,40,80):
        orig=finite_joint(n,zz,tt)
        mut=finite_joint(n,zz,tt,True)
        leading=(2+tt-zz)**-2
        residual_o=n*(orig-leading)-exact1
        residual_m=n*(mut-leading)-exact_fake
        receipts.append({
            'n':n,'z':str(zz),'t':str(tt),
            'first_jet':mp.nstr(exact1,25),
            'fake_first_jet':mp.nstr(exact_fake,25),
            'scaled_error_original':mp.nstr(residual_o,20),
            'scaled_error_fake':mp.nstr(residual_m,20),
            'source_defect_inferred':mp.nstr(n*(orig-mut),24),
            'source_defect_predicted':mp.nstr(exact1-exact_fake,24),
        })
        # Loose numerical convergence sanity; not an asymptotic certificate.
        assert abs(residual_o) < mp.mpf('0.5')
        assert abs(residual_m) < mp.mpf('0.5')
# Gamma--Poisson fixed point and source-derived Oily special value.
lam=(mp.sqrt(5)-1)/2
qstar=lam*lam
assert mp.almosteq((2-qstar)**-2,qstar)
assert mp.almosteq(mp.digamma(2)-(1+lam)**-2,lam-mp.euler)
print(json.dumps({
 'symbolic': 'joint polynomial, density-vs-binomial decomposition, z=0 jet, harmonic source defect PASS',
 'numerical': '3 (z,t) points x 3 native clocks x 2 sources; high precision, non-interval',
 'n_cases':len(receipts),'cases':receipts,
},indent=2))
