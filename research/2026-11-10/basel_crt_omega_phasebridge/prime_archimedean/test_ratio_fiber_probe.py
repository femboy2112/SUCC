"""Hostile finite controls for a prime torus inside a bounded ratio window."""
import unittest
from math import gcd, log
from fractions import Fraction
from ratio_fiber_probe import (
    factor, signed_prime_exponents, local_total_variation,
    prime_compensation_root, J_32, K_32, v_p, is_prime,
    ord16_mod_prime, K_32_is_divisible, mixed_exponent,
    multiplicative_defect_is_one, toral_next,
    exact_mean_log_gcd_by_divisors, direct_mean_log_gcd,
    direct_mean_compensation, r_one_based, source_prefix_one_based,
    original_phase_fiber_interval,
)


class RatioFiberTests(unittest.TestCase):
    def test_exact_product_formula_and_compensation(self):
        for n in range(2,58):
            for m in range(2,58):
                g = gcd(n,m)
                d = signed_prime_exponents(n,m)
                self.assertEqual(Fraction(n,m), Fraction(
                    __import__('math').prod(p**k for p,k in d.items() if k>0),
                    __import__('math').prod(p**(-k) for p,k in d.items() if k<0)))
                self.assertEqual(local_total_variation(n,m), n*m//(g*g))
                self.assertEqual(prime_compensation_root(n,m), min(n,m)//g)
                self.assertEqual(local_total_variation(n,m)*min(n,m),
                                 max(n,m)*prime_compensation_root(n,m)**2)

    def test_every_prime_under_2A_visible_in_some_ratio(self):
        for A in (3,6,12,29,48):
            band = range(A,2*A)
            for p in (p for p in range(2,2*A) if is_prime(p)):
                self.assertTrue(any(v_p(n,p)!=v_p(m,p)
                                    for n in band for m in band), (A,p))

    def test_fiber_exact_band_and_ratio(self):
        for A in (3,6,10,12,17,24,25,60,101):
            direct = [ell for ell in range(1,2*A)
                      if 2*ell in range(A,2*A) and 3*ell in range(A,2*A)]
            self.assertEqual(J_32(A),direct)
            self.assertLessEqual(abs(len(direct)-A/6),2)
            for ell in direct:
                self.assertEqual(Fraction(3*ell,2*ell),Fraction(3,2))

    def test_phase_exponent_increases_and_recurrence(self):
        for ell in range(1,16):
            k0,k1,k2=K_32(ell),K_32(ell+1),K_32(ell+2)
            self.assertLess(k0,k1)
            self.assertEqual(k2,toral_next(k0,k1))
            self.assertEqual(k0,16**(3*ell-1)-16**(2*ell-1))

    def test_2_3_5_lte_prime_passport(self):
        for ell in range(1,60):
            k=K_32(ell)
            self.assertEqual(v_p(k,2),8*ell-4)
            self.assertEqual(v_p(k,3),1+v_p(ell,3))
            self.assertEqual(v_p(k,5),1+v_p(ell,5))

    def test_all_odd_prime_orders(self):
        for p in [3,5,7,11,13,17,19,23,31,37,41,43,47,53,59]:
            d = ord16_mod_prime(p)
            self.assertEqual((p-1)%d,0)
            for ell in range(1,3*d+2):
                self.assertEqual(K_32_is_divisible(ell,p),ell%d==0)
                self.assertEqual(K_32(ell)%p==0,ell%d==0)

    def test_all_primes_through_finite_fiber(self):
        for A in (12,18,24,60,120,240):
            J=J_32(A)
            for p in range(2,len(J)+2):
                if is_prime(p):
                    self.assertTrue(any(K_32_is_divisible(ell,p) for ell in J),(A,p))

    def test_multiplicative_rigidity_gcd(self):
        x,y=mixed_exponent(2,2),mixed_exponent(2,3)
        self.assertEqual((x,y),(4065,1048305))
        self.assertEqual(gcd(x,y),15)
        self.assertEqual(9026*x-35*y,15)
        for alpha in [Fraction(0),Fraction(1,15),Fraction(2,15),
                      Fraction(1,4065),Fraction(1,1048305),Fraction(1,17),
                      Fraction(1,7),Fraction(1,255)]:
            for h in (1,2,8):
                both=(multiplicative_defect_is_one(alpha,h,2,2)
                      and multiplicative_defect_is_one(alpha,h,2,3))
                self.assertEqual(both,(15*h*alpha).denominator==1)
                self.assertEqual(both,all((h*alpha*(16**(n-1)-1)).denominator==1
                                          for n in range(1,8)))

    def test_wrong_seed_pure_gauge_not_a_signed_bound(self):
        alpha=Fraction(0)
        self.assertTrue(all((alpha*K_32(ell)).denominator==1
                            for ell in range(1,50)))
        # The coherent control has fiber mean 1 for every band; the same
        # prime passports remain valid. This refutes a source-blind inference.
        self.assertTrue(K_32_is_divisible(3,7))

    def test_log_gcd_independent_formula(self):
        for A in (2,5,12,30,64):
            self.assertAlmostEqual(exact_mean_log_gcd_by_divisors(A),
                                   direct_mean_log_gcd(A),places=11)

    def test_compensation_average_grows(self):
        for A in (10,16,25,64):
            d=direct_mean_compensation(A)
            self.assertGreaterEqual(d,0.0)
            self.assertLess(d,2*log(2*A))
            self.assertGreater(d,log(A)/2)

    def test_independent_four_pole_source(self):
        from prime_weil_probe import original_four_pole_R, original_zero_prefix
        for j in range(0,35):
            self.assertEqual(r_one_based(j+1),original_four_pole_R(j))
        for L in (1,3,12,24,32):
            self.assertEqual(source_prefix_one_based(L),original_zero_prefix(L))

    def test_authentic_h8_prime_fiber_opposite_signs(self):
        # Both 3/2 edges lie strictly in the same A=14 epoch: 14->21,
        # 16->24. Full phase = h*(16^n-16^m)*(pi/16), with no reduction
        # before propagating the exact rational 32-term BBP enclosure.
        self.assertIn(7,J_32(14))
        self.assertIn(8,J_32(14))
        poslo,poshi=original_phase_fiber_interval(7,h=8,L=32)
        neglo,neghi=original_phase_fiber_interval(8,h=8,L=32)
        self.assertTrue(Fraction(17,20)<poslo<poshi<Fraction(19,20))
        self.assertTrue(Fraction(1,4)<neglo<neghi<Fraction(3,4))
        # cos(2pi x) >0 for x in (3/4,1); <0 on (1/4,3/4).
        # Coherent wrong seed instead has both edge cosines exactly 1.

    def test_rational_phase_budget_rejects_short_horizon(self):
        with self.assertRaises(ValueError):
            original_phase_fiber_interval(8,h=8,L=1)

    def test_haar_orthogonality_formal_positive_negative(self):
        # Fourier characters e(h K_ell alpha) are pairwise orthogonal under
        # uniform alpha iff the K_ell are distinct. Exactly L diagonal terms.
        for L in (1,2,3,15):
            coeff=[K_32(i) for i in range(1,L+1)]
            self.assertEqual(sum(int(u==v) for u in coeff for v in coeff),L)
            self.assertEqual(Fraction(L,L*L),Fraction(1,L))


if __name__ == '__main__':
    unittest.main()
