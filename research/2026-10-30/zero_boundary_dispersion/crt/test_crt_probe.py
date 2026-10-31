from fractions import Fraction as F
from math import comb, gcd, lcm
import unittest
import crt_probe as c


class ExactCRTTests(unittest.TestCase):
    def test_original_source(self):
        self.assertEqual(c.source(1),F(47,15))
        for n in range(1,41):
            expected=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(c.source(n),expected)

    def test_lcm_divisibility_not_size_only(self):
        for m in range(31):
            for s in range(1,20):
                a,b=c.interval_lcm_bound(m,s)
                self.assertEqual(b%a,0)

    def test_filter_moving_degree(self):
        u=c.orbit(180)
        for n,d in ((19,3),(43,17),(97,43),(101,61)):
            for coefficients in ([-1]+[0]*(d-1)+[1],list(range(1,d+2))):
                c.filter_certificate(n,coefficients,u)

    def test_annihilator_is_typed(self):
        u=c.orbit(40)
        r=c.filter_certificate(17,[-16,1],u)
        self.assertEqual(r['P16'],'0')
        self.assertEqual((u[18]-16*u[17]).denominator,c.source(18).denominator)

    def test_primary_reconstruction(self):
        for d in range(1,250):
            for p in (2,3,5,7,11):
                x=F(17,d);a=c.primary(x,p);v=c.circle(x-a)
                self.assertEqual(c.primary(v,p),0)
                self.assertEqual(c.circle(a+v),c.circle(x))

    def test_exact_no_wrap_cylinder(self):
        for A in (3,11,37):
            for L in (1,2,4,9):
                lo,hi=c.cylinder(A,L)
                points=[F(k,1024) for k in range(-64,65)]+[lo,hi,(lo+hi)/2,lo-F(1,16**(L+2)),hi+F(1,16**(L+2))]
                for x in points:
                    y=x; good=True
                    for j in range(L):
                        good &= c.distance(y)<=F(1,20)
                        y=16*y+c.source(A+j+2)-c.source(A+j+1)
                    self.assertEqual(good,lo<=c.centered(x)<=hi)

    def test_no_wrap_domain_guard(self):
        with self.assertRaises(ValueError):c.cylinder(1,2,h=10000)
        with self.assertRaises(ValueError):c.cylinder(10,2,delta=F(1,17))

    def test_dyadic_shadow(self):
        u=c.orbit(80)
        for A,L in ((9,7),(23,19),(41,29)):
            seed,upper,alias=c.dyadic_shadow(A,L,u)
            self.assertLess(upper,F(1,20))
            self.assertEqual(seed.denominator&(seed.denominator-1),0)
            for n in range(A,A+L):
                self.assertLessEqual(c.distance(u[n+1]-u[n]+15*16**n*seed),upper)
            self.assertEqual(c.circle(16**alias*seed),0)

    def test_odd_projections_of_shadow_all_tested_times(self):
        u=c.orbit(100);seed,_,_=c.dyadic_shadow(17,41,u)
        for p in (3,5,7,13,19,73):
            for n in range(101):
                self.assertEqual(c.primary(u[n]+16**n*seed,p),c.primary(u[n],p))

    def test_real_alias_after_dyadic_transient(self):
        u=c.orbit(60);s,_,B=c.dyadic_shadow(9,13,u)
        for n in range(B,60):
            self.assertEqual(c.circle(u[n]+16**n*s),u[n])

    def test_prime_power_full_phase_is_not_top_digit(self):
        u=c.orbit(50);p=11;Q=p*p;b=c.birth(Q)
        self.assertEqual(b,16)
        self.assertNotEqual(c.primary(u[17],p),c.circle(16*c.primary(u[16],p)))
        self.assertEqual(c.rational_mod(Q*u[17],p),16*c.rational_mod(Q*u[16],p)%p)

    def test_actual_cancellations(self):
        u=c.orbit(275)
        for n in range(10,17):self.assertEqual(c.primary(u[n],19),0)
        self.assertNotEqual(c.primary(u[17],19),0)
        self.assertEqual(c.primary(u[274],73),0)

    def test_null_zero_seed_is_coherent(self):
        u=c.orbit(100,c.NULL_C,tuple(range(1,8)))
        for n in range(25,100):
            self.assertLess(c.distance(u[n+1]-u[n]),F(1,20))


if __name__=='__main__':unittest.main()
