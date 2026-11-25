"""Independent source checks; SymPy/mPMath are optional and not a proof engine."""
from fractions import Fraction
from math import isqrt
from random import Random
import sympy as sp
from observational_succ.principia_cm_theta import (
    construct_cm_theta_certificate, verify_cm_theta_certificate,
    theta_shell_moment, lemniscate_derivative_jets, lemniscate_hasse_invariant,
)

rng = Random(20261124)
M = 0
for p in (3, 7, 11, 19, 23):
    for rank in range(1, 5):
        c = construct_cm_theta_certificate(p, rank, Fraction(1, rng.randrange(2, 7)))
        report = verify_cm_theta_certificate(c)
        s = sp.Matrix(c.matrix)
        det = int(s.det(method='domain-ge'))
        assert det == report['determinant'] and s.rank() == rank
        q = sp.Rational(c.q.numerator, c.q.denominator)
        weighted = s * sp.diag(*(q**n for n in c.gaussian_norms))
        exact_det = sp.factor(weighted.det(method='domain-ge'))
        assert exact_det**2 == report['weighted_determinant_squared']
        # Independently form H via explicit (a+bi) symbolic powers on Z[i].
        for r in range(rank):
            for i,n in enumerate(c.gaussian_norms):
                h = 0
                for a in range(-isqrt(n), isqrt(n)+1):
                    b2 = n-a*a
                    b = isqrt(b2)
                    if b*b==b2:
                        h += (sp.Integer(a)+sp.I*b)**(4*r)
                        if b: h += (sp.Integer(a)-sp.I*b)**(4*r)
                assert sp.expand(h) == c.matrix[r][i]
        M += 1
print('SYMPY_INDEPENDENT_CM_THETA_CERTIFICATES_PASS',M)

# Distinct independent solution of sl''=-2 sl^3 via formal SymPy-series inversion
x=sp.symbols('x')
phi=x+sum(sp.binomial(2*k,k)*x**(4*k+1)/(4**k*(4*k+1)) for k in range(1,5))
sl=sp.series_inverse(phi, x, 0, 19) if hasattr(sp,'series_inverse') else None
if sl is None:
    s=x
    for degree in range(5,18,4):
        residual=sp.Poly(sp.series(phi.subs(x,s),x,0,degree+1).removeO(),x).nth(degree)
        s=sp.expand(s-residual*x**degree)
    sl=s
ref=lemniscate_derivative_jets(17)
for n in (1,5,9,13,17):
    got=int(sp.Poly(sl,x).nth(n)*sp.factorial(n))
    assert got==ref[n],(n,got,ref[n])
print('SYMPY_INDEPENDENT_LEMNISCATE_INVERSION_PASS',5)

# Different kind of probe: analytic period/holomorphic moments, numerical ONLY.
import mpmath as mp
mp.mp.dps=80
pi=mp.pi
omega=mp.beta(mp.mpf(1)/4,mp.mpf(1)/2)/2
q=mp.e**(-pi)
L=9
T=[]
for k in range(4):
    total=mp.mpc(0)
    for a in range(-L,L+1):
      for b in range(-L,L+1):
        lam=mp.mpc(a,b)
        total+=lam**(4*k) * mp.exp(-pi*(a*a+b*b))
    T.append(mp.re(total))
T0=T[0]
assert abs(T0-mp.sqrt(2)*omega/pi) < mp.mpf('1e-70')
expected=[sp.Rational(1),sp.Rational(1,4),sp.Rational(17,16),sp.Rational(-111,64)]
for k in range(1,4):
    actual=T[k]/(T0*(omega/pi)**(4*k))
    target=mp.mpf(int(expected[k].p))/int(expected[k].q)
    assert abs(actual-target)<mp.mpf('1e-65'), (k,mp.nstr(actual,40),target)
print('NUMERICAL_CM_PERIOD_THETA_CHECK_PASS (not an interval proof)',mp.nstr(T0,18))
