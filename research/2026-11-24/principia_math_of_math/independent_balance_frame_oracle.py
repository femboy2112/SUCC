"""Independent SymPy exact inverse/conditioning check for the real CM source."""
from fractions import Fraction
from itertools import product
import sympy as sp
from observational_succ.principia_cm_theta import construct_cm_theta_certificate
from observational_succ.principia_balance_frame import cm_balance_frame

nchecked=0
for p,n,q in product((3,7),(1,2,3),(Fraction(1,2),Fraction(2,3))):
    c=construct_cm_theta_certificate(p,n,q)
    for gaussian in (False,True):
        frame=cm_balance_frame(c,analytic=gaussian)
        exact=sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row]
                         for row in frame.observation])
        original=sp.Matrix(c.matrix)
        if gaussian:
            expected=original*sp.diag(*(sp.Rational(q.numerator,q.denominator)**degree for degree in c.gaussian_norms))
        else:expected=original
        assert exact==expected
        inverse=exact.inv()
        computed=tuple(tuple(Fraction(inverse[i,j]) for j in range(n)) for i in range(n))
        assert computed==frame.inverse
        opnorm=max(sum((abs(a) for a in row),Fraction(0)) for row in computed)
        assert opnorm==frame.inverse_infinity_norm
        # Directly construct a noise vector saturating the norm.
        maxrow=max(range(n),key=lambda i:sum(abs(a) for a in computed[i]))
        noise=sp.Matrix([1 if inverse[maxrow,j]>0 else -1 if inverse[maxrow,j]<0 else 0 for j in range(n)])
        response=inverse*noise
        assert max(abs(Fraction(response[i])) for i in range(n))==opnorm
        nchecked+=1
print('INDEPENDENT_CM_BALANCE_FRAME_PASS',nchecked,'exact inverse/norm/attainment models')
