import unittest
from fractions import Fraction as F
from math import comb, factorial
from composition import (SOURCE,SIGMA2,source,jets,jet_variance,ln_interval,
    proportion_moments,log_increment,rational_lower_bounds,golden_laplace,
    golden_excess,golden_interval,gadd,gscale,gmul,gpower)


class CompositionTests(unittest.TestCase):
    def test_authentic_source_passport(self):
        for n in (1,2,7,17,61,137):
            a=8*n-7
            expected=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            self.assertEqual(source(a),expected)
            self.assertEqual(source(a),F(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5)))

    def test_rate_variance_from_bounded_mixture(self):
        mean=F(2*3**2+4**2+5**2,30)
        second=F(2*3**3+4**3+5**3,45)
        self.assertEqual(mean,F(59,30))
        self.assertEqual(second-mean*mean,SIGMA2)
        self.assertEqual(jet_variance(),SIGMA2)
        self.assertEqual(jets(depth=3),[F(0),F(15),F(-59,2),F(81,2)])

    def test_log_enclosure_elementary_bounds(self):
        for q in (F(1,31),F(3,2),F(7,3),F(113),F(4089)):
            lo,hi=ln_interval(q)
            if q>1:
                self.assertGreater(lo,(q-1)/q)
                self.assertLess(hi,q-1)
            inv=ln_interval(1/q)
            self.assertEqual(inv,(-hi,-lo))
            self.assertLess(hi-lo,F(1,2**300))

    def test_all_a_proportion_lower_bound(self):
        for a in (F(3,2),1,9,37,113,389,1531):
            eb=proportion_moments(a)['EB']
            bound=rational_lower_bounds(a)['proportion_gap']
            self.assertGreater(bound,0)
            self.assertGreater(F(1,5)-eb[1],bound)

    def test_all_a_harmonic_lower_bound(self):
        for a in (F(3,2),1,9,37,113,389,1531):
            inc=log_increment(a)
            bound=rational_lower_bounds(a)['harmonic_gap']
            self.assertGreater(inc[0]-F(5,6),bound)

    def test_golden_positive_composition_term(self):
        for a in (1,9,49,129,505,1017,4089):
            l=golden_laplace(a)
            self.assertGreater(golden_interval(gadd(l,(-F(1),F(1))))[0],0)
            self.assertGreater(golden_interval(gadd((F(0),F(1)),gscale(l,-1)))[0],0)
            self.assertGreater(golden_interval(golden_excess(a))[0],0)

    def test_exact_golden_quadratic_identity(self):
        lam=(F(0),F(1)); q=(F(1),F(-1))
        for a in (1,3,11,79):
            l=golden_laplace(a)
            lhs=gadd(gmul(l,gadd((F(1),F(0)),gscale(l,-1))),gscale(gpower(lam,3),-1))
            self.assertEqual(lhs,golden_excess(a))
        self.assertEqual(gadd(lam,q),(F(1),F(0)))

    def test_wrong_mark_refutes_universal_quadratic_sign(self):
        a=F(1,1000); eta=F(1,3); t=1/(1+eta)
        l=source(a*(1+eta))/source(a)
        self.assertLess(l*(1-l)-t*t*(1-t*t),0)

    def test_gamma_control_exact_beta_moments(self):
        beta=lambda k: F(6*factorial(k+1)**2,factorial(2*k+3))
        self.assertEqual(beta(1),F(1,5))
        self.assertEqual(beta(2)-beta(1)**2,F(1,350))
        # Gamma(4): Cov(S,S²)=40; beta Cov(log U,B)=1/100.
        self.assertEqual(F(factorial(6),factorial(3))-4*F(factorial(5),factorial(3)),40)
        H=lambda n:sum((F(1,k) for k in range(1,n+1)),F(0))
        self.assertEqual(beta(1)*(H(2)-H(5)-(H(1)-H(3))),F(1,100))

    def test_matched_jet_controls(self):
        two=((F(0),F(225,59)),(F(59,15),F(-225,59)))
        self.assertEqual(jets(two,2),jets(SOURCE,2))
        self.assertEqual(jet_variance(two),F(3481,2700))
        self.assertNotEqual(jet_variance(two),SIGMA2)
        extra=tuple((F(j),F((-1)**j*comb(4,j))) for j in range(5))
        four=SOURCE+extra
        self.assertEqual(jets(four,3),jets(SOURCE,3))
        self.assertEqual(jet_variance(four),SIGMA2)
        for a in (9,37,113):
            self.assertNotEqual(source(a,source=four),source(a))
            authentic=proportion_moments(a)['EB']
            mutant=proportion_moments(a,four)['EB']
            self.assertTrue(authentic[1]<mutant[0] or mutant[1]<authentic[0])

    def test_gamma_coefficient_exact_normalization(self):
        for a in (1,9,37,113):
            r=source(a)
            first=sum((c/(a+d) for d,c in SOURCE),F(0))/r
            second=sum((ci*cj/((a+di)*(a+dj)) for di,ci in SOURCE for dj,cj in SOURCE),F(0))/r**2
            self.assertEqual(first,1)
            self.assertEqual(second,1)
            self.assertEqual(first-second,0)


if __name__=='__main__':
    unittest.main(verbosity=2)
