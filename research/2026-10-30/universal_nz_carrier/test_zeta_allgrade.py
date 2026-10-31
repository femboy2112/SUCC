from unittest import TestCase,main
from math import comb
import mpmath as mp

mp.mp.dps=95

def A(n):
    assert n>=1
    return mp.fsum([(-1)**k*comb(n,k)*mp.mpf(k+1)*mp.log(k+1) for k in range(n+1)])

def projected_ratio(M):
    return mp.mpf(10)/3*mp.log(2)-4*mp.fsum(A(n)/2**(n+1) for n in range(2,M+1))

def integral_A(n):
    assert n>=2
    f=lambda t: mp.exp(-t)*(-mp.expm1(-t))**n/t**2 if t else (mp.mpf(1) if n==2 else mp.mpf(0))
    return mp.quad(f,[0,1,5,mp.inf])

class AllGradeTests(TestCase):
 def test_degree_one_value_truncates(self):
    for n in range(2,27):
        self.assertEqual(sum((-1)**k*comb(n,k)*(k+1) for k in range(n+1)),0)
 def test_derivative_grade_one_is_negative(self):
    self.assertAlmostEqual(float(A(1)),float(-2*mp.log(2)),places=60)
 def test_nonzero_derivative_grades(self):
    a2=A(2)
    for n in range(2,31):
        self.assertGreater(A(n),0)
        self.assertLessEqual(A(n),a2+mp.mpf('1e-70'))
 def test_positive_integral_independently(self):
    for n in (2,3,4,6,9,13):
        self.assertLess(abs(A(n)-integral_A(n)),mp.mpf('1e-78'))
 def test_zeta_log_derivative_finite_certificates(self):
    goal=mp.diff(mp.zeta,-1)/mp.zeta(-1)
    A2=3*mp.log(3)-4*mp.log(2)
    for M in (2,3,5,10,20,35,60):
        top=projected_ratio(M)
        self.assertGreater(top,goal)
        self.assertLess(top-goal,4*A2/2**(M+1))
 def test_integral_closed_form(self):
    f=lambda t:mp.exp(-t)*(-mp.expm1(-t))**2/((1+mp.exp(-t))*t*t) if t else mp.mpf('0.5')
    I=mp.quad(f,[0,1,5,mp.inf])
    goal=mp.diff(mp.zeta,-1)/mp.zeta(-1)
    self.assertLess(abs(mp.mpf(10)/3*mp.log(2)-I-goal),mp.mpf('1e-85'))
 def test_prime_reflection_cross_check(self):
    L=-mp.diff(mp.zeta,2)/mp.zeta(2)
    target=mp.log(2*mp.pi)+mp.euler-1+L
    self.assertLess(abs(target-mp.diff(mp.zeta,-1)/mp.zeta(-1)),mp.mpf('1e-85'))
 def test_positive_integral_bounds(self):
    for n in range(2,18):
        self.assertLessEqual(integral_A(n),integral_A(2)+mp.mpf('1e-75'))

if __name__=='__main__':main()
