"""Independent SymPy/mpmath oracle; imports no project continuum_probe code.

The analytic proofs live in THEOREMS.md. Finite checks do not certify an
infinite theorem or imply pi normality.
"""
import sympy as sp
import mpmath as mp
from fractions import Fraction


def run():
    exact = 0
    numerical = 0
    t = sp.symbols('t')
    q = 4-2*t**3-t**4-t**5
    assert sp.expand(q - (1-t)*(t*t+2)*(t*t+2*t+2)) == 0
    exact += 1

    for n in range(1, 21):
        direct = sp.Rational(4,8*n-7)-sp.Rational(2,8*n-4)-sp.Rational(1,8*n-3)-sp.Rational(1,8*n-2)
        moment = sp.integrate(t**(8*n-8)*q, (t,0,1))
        assert direct == moment
        exact += 1

    for x in (sp.Rational(1,7),sp.Rational(23,13),sp.Rational(-17,11)):
        j = [sp.Mod(x / 16**m, 1) for m in range(9)]
        for m in range(8):
            assert sp.Mod(16*j[m+1], 1) == j[m]
            exact += 1
        for k in (1,16,16**3):
            other = [sp.Mod((x+k)/16**m, 1) for m in range(9)]
            assert j[0] == other[0]
            assert j != other
            exact += 2
    mp.mp.dps = 55
    c = mp.log(16)
    for k in (1,2,5,11,32,64):
        # Independent cosine-integral formula, not Simpson quadrature.
        val = 2 - 2*(mp.ci(2*mp.pi*k*16)-mp.ci(2*mp.pi*k))/c
        budget = 15/(16*mp.pi*k*c)
        assert abs(val-2) < budget
        numerical += 1

    # Gamma(shape 1) integral evaluated through complex incomplete Gamma.
    a = 1/c
    for integer_time in (0,1,2,3,4):
        A = 2*mp.pi*mp.power(16,integer_time)
        phi = (-1j*A)**a * mp.gammainc(-a, -1j*A, mp.inf)/c
        upper = 1/(mp.pi*c*mp.power(16,integer_time))
        assert abs(phi) < upper*(1+mp.mpf('1e-27'))
        numerical += 1

    # The relative winding grows with discrete epoch even for identical
    # integer-circle observations; exact integer arithmetic, no complex floats.
    for k in (-5,-1,1,3):
        for n in range(8):
            assert k*(16**(n+1)-16**n) == 15*k*16**n
            exact += 1

    print('INDEPENDENT_AUDIT_PASS', f'exact={exact}', f'high_precision={numerical}', 'dps=55')


if __name__ == '__main__':
    run()
