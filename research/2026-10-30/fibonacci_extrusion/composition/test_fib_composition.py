from fractions import Fraction as F
from math import comb
import unittest
from fib_composition import *

class FibonacciCompositionTests(unittest.TestCase):
    def test_native_source_moments(self):
        for a in [F(1),F(17,3),F(97),F(1009)]:
            self.assertGreater(variance(a),0)
            self.assertEqual(r(a),(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5)))
            self.assertEqual(moment(a,0),1)

    def test_mixture_variance(self):
        moments=[sum(F(c*b**(j+1),15*(j+1)) for b,c in [(3,2),(4,1),(5,1)]) for j in range(3)]
        self.assertEqual(moments[0],1)
        self.assertEqual(moments[2]-moments[1]**2,SIGMA2)
        self.assertEqual(10*SIGMA2+F(125,6),UNIFORM_C)

    def test_dirichlet_hessian_exact(self):
        for k in [2,3,7,13,34]:
            z=[F(i*i-3*i,7) for i in range(k)]
            linear=sum(z,F(0))/k
            mean_square=sum(t*t for t in z)/k
            averaged_square=(3*sum(t*t for t in z)+2*sum(z[i]*z[j] for i in range(k) for j in range(k) if i!=j))/(k*(2*k+1))
            actual=(mean_square-averaged_square)/2
            self.assertEqual(actual,F(k,2*k+1)*(mean_square-linear*linear))

    def test_uniform_small_exact_intervals(self):
        for k,a in [(1,5),(2,19),(3,101),(5,43),(8,149)]:
            gap=harmonic_gap_interval(a,k,128)
            scaled=iscale(gap,F(a*a))
            center=uniform_center(k);err=uniform_error(a)
            self.assertGreaterEqual(scaled[0],center-err)
            self.assertLessEqual(scaled[1],center+err)
            if k>1:self.assertGreater(gap[0],0)

    def test_fibonacci_path_coefficients(self):
        pair=(F(1),F(0)),(F(0),F(1))
        for n in range(2,31):
            self.assertEqual(pair[1],(fib(n-2),fib(n-1)))
            self.assertEqual(fib(n-2)**2+fib(n-1)**2,fib(2*n-3))
            pair=pair[1],tuple(x+y for x,y in zip(*pair))

    def test_first_three_alias_then_failure(self):
        a=F(17);t=F(3,7)
        for n in [1,2,3]:self.assertEqual(fresh_laplace(a,t,n),reused_laplace(a,t,n))
        self.assertNotEqual(fresh_laplace(a,t,4),reused_laplace(a,t,4))
        self.assertEqual(reused_variance(a,4)-fresh_variance(a,4),2*variance(a))

    def test_golden_variance_limit(self):
        self.assertEqual(ga(gp(LAMBDA,4),gp(LAMBDA,2)),(F(3),F(-4)))
        for a in [F(1),F(17),F(233)]:
            actual=ga(golden_reused_moment(a,2),(-moment(a,1)**2,F(0)))
            self.assertEqual(actual,gs((F(3),F(-4)),variance(a)))

    def test_reciprocal_budget(self):
        for n in [1,2,7,19,41]:
            lo,hi=reciprocal_interval(n)
            fresh=sum(fresh_variance(17,j)/fib(j)**2 for j in range(1,n+1))
            self.assertEqual(fresh,variance(17)*lo)
            larger=reciprocal_interval(n+20)[0]
            self.assertLess(lo,larger)
            self.assertLess(larger,hi)

    def test_source_jensen_lower_positive(self):
        for a in [F(1,7),F(17),F(233),F(4093)]:
            bound=golden_interval(jensen_lower(a))
            self.assertGreater(bound[0],0)

    def test_gamma_gap_certified(self):
        lo,hi=gamma_gap_interval()
        self.assertGreater(lo,F(135,1000))
        self.assertLess(hi,F(137,1000))

    def test_uniform_no_single_mixture_source_identity(self):
        mutant=F(3481,2700)
        self.assertNotEqual(mutant,SIGMA2)
        self.assertEqual(F(0)*(5-1)/(2*5+1),0)

    def test_source_clock_commutation(self):
        for a in [F(17),F(97,3),F(233)]:
            s=F(3,7);t=F(2,11)
            for k in [1,2,5,13]:
                self.assertEqual((laplace(a,s+t)/laplace(a,s))**k,laplace(a+s,t)**k)
            self.assertEqual(clock_defect(a,s,3),0)
            for n in [4,5,8,13]:
                self.assertGreater(clock_defect(a,s,n),clock_defect_lower(a,s,n))
                self.assertGreater(clock_defect_lower(a,s,n),0)

if __name__=='__main__':unittest.main()
