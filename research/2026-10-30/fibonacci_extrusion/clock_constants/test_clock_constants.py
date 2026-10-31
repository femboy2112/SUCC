import unittest
from fractions import Fraction as Q
import clock_constants as c


class ClockConstantsTests(unittest.TestCase):
    def test_fibonacci_normalizations(self):
        self.assertEqual([c.fib(n) for n in range(10)], [0,1,1,2,3,5,8,13,21,34])
        self.assertEqual(c.fib(21),10946)

    def test_exact_reciprocal_tail_covers_fresh_partial_sum(self):
        for p in (1,2,3):
            for n in (7,14,23):
                lo,hi=c.zeta_fib(p,n)
                later=sum((Q(1,c.fib(j)**p) for j in range(2,n+35)),Q(0))
                self.assertLess(lo,later)
                self.assertLess(later,hi)

    def test_log_series_transport_identity(self):
        for a,b in ((Q(3,7),Q(11,2)),(Q(17,5),Q(91,29)),(Q(144),Q(233))):
            x=c.add(c.ln(a),c.ln(b)); y=c.ln(a*b)
            self.assertLessEqual(max(x[0],y[0]),min(x[1],y[1]))

    def test_harmonic_error_difference_exact(self):
        for m in (1,2,13,21,55,144):
            lhs=c.add(c.harmonic_error(m),c.scale(c.harmonic_error(m+1),-1))
            rhs=c.add(c.ln(Q(m+1,m)),c.point(-Q(1,m+1)))
            self.assertLessEqual(max(lhs[0],rhs[0]),min(lhs[1],rhs[1]))
            lo,hi=c.harmonic_error(m)
            self.assertGreater(lo,Q(1,2*m)-Q(1,12*m*m))
            self.assertLess(hi,Q(1,2*m))

    def test_golden_normalization_and_wrong_root(self):
        l,u=c.golden()
        self.assertLess(l*l+l,1)
        self.assertGreater(u*u+u,1)
        self.assertNotEqual(Q(1,2)**2+Q(1,2),1)
        # Removing the negative conjugate sign would give F1<1.
        self.assertLess((1-l*l)/(2*l+1)/l,1)

    def test_golden_tail_difference(self):
        l,u=c.golden()
        for m in (1,3,8,21,55):
            d=c.add(c.golden_tail(m),c.scale(c.golden_tail(m+1),-1))
            expected=(l**(m+1)/(m+1),u**(m+1)/(m+1))
            self.assertLessEqual(max(d[0],expected[0]),min(d[1],expected[1]))

    def test_outward_rounding(self):
        for x in ((Q(1,3),Q(2,3)),(Q(-2,3),Q(-1,3))):
            r=c.outward(x,5)
            self.assertLessEqual(Q(int(r['lo_numerator']),int(r['denominator'])),x[0])
            self.assertGreaterEqual(Q(int(r['hi_numerator']),int(r['denominator'])),x[1])


if __name__=='__main__':
    unittest.main()
