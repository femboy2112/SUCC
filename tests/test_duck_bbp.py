"""Independent exact holdouts; no finite census is a normality proof."""

from fractions import Fraction as Q
import unittest

from observational_succ.duck_bbp import (
    coefficient_budget, forcing, forced_orbit, lifted_orbit,
    partial_transport_residual, pi_interval, source_tail_budget, tail_budget, tail_interval,
)


def machin_interval(terms=100):
    def atan(q):
        s = sum(((-1)**i*q**(2*i+1)/(2*i+1) for i in range(terms)), Q())
        r = (-1)**terms*q**(2*terms+1)/(2*terms+1)
        return min(s, s+r), max(s, s+r)
    a,b = atan(Q(1,5))
    c,d = atan(Q(1,239))
    return 16*a-4*d, 16*b-4*c


class BaileyCrandallExactTests(unittest.TestCase):
    def test_independent_fraction_source_and_polynomial_certificates(self):
        for m in list(range(1,80)) + [101,257,1009,65537]:
            direct=Q(4,8*m-7)-Q(2,8*m-4)-Q(1,8*m-3)-Q(1,8*m-2)
            self.assertEqual(forcing(m),direct)
            self.assertTrue(Q(15,64*m*m) <= forcing(m) <= coefficient_budget(m))
            self.assertLess(forcing(m+1),forcing(m))
            u=m-1;den=(2*m-1)*(4*m-1)*(8*m-7)*(8*m-3)
            num=120*m*m-89*m+16
            self.assertEqual(47*den-15*m*m*num,
                22264*u**4+42263*u**3+26429*u*u+5443*u)
        self.assertEqual(forcing(1),Q(47,15))
        self.assertGreater(forcing(1),3)  # Reject an overstrong constant.

    def test_source_sensitive_bounds_from_positive_fraction_decomposition(self):
        for n in [0,1,2,7,31,257,65536]:
            m=n+1
            positive=Q(6,(8*m-7)*(8*m-4))+Q(4,(8*m-7)*(8*m-3))+Q(5,(8*m-7)*(8*m-2))
            self.assertEqual(forcing(m),positive)
            self.assertLessEqual(source_tail_budget(n),tail_budget(n))
            self.assertLessEqual(source_tail_budget(n),Q(1,(8*n+1)**2))
            lo,hi=tail_interval(n,24)
            self.assertGreater(lo,forcing(m)/16)
            self.assertLess(hi,source_tail_budget(n))
            u=m-1;den=(2*m-1)*(4*m-1)*(8*m-7)*(8*m-3)
            num=120*m*m-89*m+16
            self.assertEqual(15*den-(8*m-7)**2*num,
                3776*u**3+5136*u*u+2007*u+178)

    def test_effective_tail_leading_term(self):
        for n in [0,1,2,7,31,257,65536]:
            x=n+1;u=x-1
            lo,hi=tail_interval(n,24)
            leading=Q(1,64*x*x)
            self.assertGreater(lo,leading-Q(1,480*x**3))
            self.assertLess(hi,leading+Q(2783,14400*x**3))
            den=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
            num=120*x*x-89*x+16
            self.assertEqual((225*x+2783)*den-960*x**3*num,
                1279936*u**4+2414792*u**3+1499906*u*u+306607*u)
            for k in [0,1,2,7,31]:
                self.assertEqual(Q(1,(x+k)**2)-Q(1,x*x)+Q(2*k,x**3),
                    Q(k*k*(3*x+2*k),x**3*(x+k)**2))

    def test_infinite_tail_enclosures_against_separate_deeper_sum(self):
        for n in [0,1,2,7,31,257]:
            old=(Q(),tail_budget(n))
            for depth in [0,1,2,4,8,16]:
                lo,hi=tail_interval(n,depth)
                self.assertLess(lo,hi)
                self.assertGreaterEqual(lo,old[0]);self.assertLessEqual(hi,old[1])
                independent=sum((Q(4,8*(n+k)-7)-Q(2,8*(n+k)-4)
                    -Q(1,8*(n+k)-3)-Q(1,8*(n+k)-2))/16**k
                    for k in range(1,depth+24))
                self.assertLess(lo,independent);self.assertLess(independent,hi)
                old=(lo,hi)

    def test_independent_machin_source_and_phase_index(self):
        pilo,pihi=machin_interval()
        for terms in range(1,33):
            lo,hi=pi_interval(terms)
            self.assertLess(lo,pilo);self.assertLess(pihi,hi)
            x=forced_orbit(terms)
            a=16**(terms-1)*pilo-x;b=16**(terms-1)*pihi-x
            carry=a//1
            tlo,thi=tail_interval(terms,8)
            self.assertLess(tlo,a-carry);self.assertLess(b-carry,thi)
        # Wrong exponent n instead of n-1 already fails at n=1.
        wrong=(16*pilo-forced_orbit(1))%1
        self.assertGreater(wrong,tail_budget(1))

    def test_finite_lifted_transport_and_reduction(self):
        for n in range(1,33):
            self.assertEqual(forced_orbit(n),lifted_orbit(n)%1)
            for depth in [0,1,2,5,11]:
                self.assertEqual(partial_transport_residual(n,depth),0)
        self.assertEqual(forced_orbit(0),0)

    def test_wrong_denominator_and_erased_clock_controls(self):
        wrong=Q(4,2)-Q(2,4)-Q(1,5)-Q(1,6)
        self.assertNotEqual(wrong,forcing(1))
        self.assertNotEqual(forced_orbit(2),(16*forced_orbit(1))%1)
        self.assertNotEqual(forcing(1),forcing(2))

    def test_exact_input_domain(self):
        for bad in [True,False,1.0,Q(1),float('nan'),float('inf'),-1]:
            for fn in [forcing,tail_budget,source_tail_budget,lifted_orbit,forced_orbit,pi_interval]:
                with self.assertRaises(ValueError):fn(bad)
        with self.assertRaises(ValueError):forcing(0)
        with self.assertRaises(ValueError):tail_interval(0,False)
        with self.assertRaises(ValueError):partial_transport_residual(0,1)


if __name__ == '__main__':
    unittest.main()
