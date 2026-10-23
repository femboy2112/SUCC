"""Independent integer, source-prime and hostile circle time-carry tests."""
import math
import unittest
from fractions import Fraction as Q

from observational_succ.circle_time_carry import (
    chord_fourier,prime_carry_product,time_frequency_table,haar_joint,
    first_time_carry_defect,orbit_3adic,periodic_moment,
    periodic_fejer_energy,periodic_joint,finite_probe_alias,
    hankel_det,haar_single,select_3adic_counterfeit)
from observational_succ.circle_collision_rigidity import covering,pi_interval

class TimeCarryExact(unittest.TestCase):
    def test_prime_carries_agree_with_independent_binomial(self):
        for k in range(13):
            self.assertEqual(chord_fourier(k,True),chord_fourier(k))
            for h in range(-k,k+1):
                self.assertEqual(prime_carry_product(k+h,k-h),
                                 math.comb(2*k,k+h))
    def test_all_times_haar_low_degree_independence(self):
        for base in (2,3,4,16):
            for ts in ((0,1),(0,2,5),(1,4,7)):
                ks=tuple(1+(i%(base-1)) for i in range(len(ts)))
                value=math.prod(math.comb(2*k,k) for k in ks)
                self.assertEqual(haar_joint(base,ts,ks),value)
                self.assertEqual(haar_joint(base,ts,ks,True),value)
    def test_sharp_first_time_carry_via_independent_chord_polynomial(self):
        for base in (2,3,4,5,16):
            expected=2*(-1 if base%2==0 else 1)
            self.assertEqual(first_time_carry_defect(base),expected)
            other=sum(c*math.comb(2*(base+j),base+j)
                      for j,c in enumerate(covering(base)))
            self.assertEqual(other-2*math.comb(2*base,base),expected)
    def test_joint_character_table_from_complete_prime_carries(self):
        for base in (2,3,16):
            self.assertEqual(time_frequency_table(base,(0,1,2),(1,2,1),True),
                             time_frequency_table(base,(0,1,2),(1,2,1)))
    def test_true_3adic_single_orbit(self):
        for r in range(2,8):
            self.assertEqual(set(orbit_3adic(r)),set(range(1,3**r,3)))
    def test_arbitrarily_deep_exact_haar_moment_alias(self):
        for r in range(2,9):
            L=3**(r-1)
            for k in (0,1,2,min(7,L-1),L-1):
                self.assertEqual(periodic_moment(r,k),math.comb(2*k,k))
            self.assertEqual(periodic_moment(r,L),math.comb(2*L,L)+1)
            self.assertEqual(math.comb(2*L,L)%3,2)
            self.assertEqual(periodic_moment(r,L)%3,0)
    def test_first_fejer_probe_and_invisible_band(self):
        for r in range(2,9):
            L=3**(r-1)
            self.assertEqual(periodic_fejer_energy(r,L-1),1)
            self.assertEqual(periodic_fejer_energy(r,L),1+Q(2,L+1))
            self.assertEqual(periodic_fejer_energy(r,2*L-1),2)
    def test_any_finite_chord_time_language_has_periodic_alias(self):
        cases=[((0,),(12,)),((0,1),(1,1)),
               ((0,1,3),(2,1,1)),((0,2,4),(5,2,1))]
        for ts,ks in cases:
            r=2
            while not finite_probe_alias(r,ts,ks): r+=1
            self.assertEqual(periodic_joint(r,ts,ks),haar_joint(16,ts,ks))
        self.assertEqual(periodic_joint(2,(0,1),(1,1)),3)
        self.assertEqual(haar_joint(16,(0,1),(1,1)),4)
    def test_arcsine_hankel_determinant(self):
        for n in range(12):
            self.assertEqual(hankel_det(haar_single,n),2**n)
    def test_sharp_first_hankel_failure(self):
        for r in (2,3,4):
            L=3**(r-1);n=(L+1)//2
            f=lambda k:periodic_moment(r,k)
            self.assertEqual(hankel_det(f,n-1),2**(n-1))
            self.assertEqual(hankel_det(f,n),Q(3,4)*2**n)
    def test_source_only_pi_bracket_has_rational_counterfeit(self):
        lo,hi=pi_interval(23,80)
        for r,N in ((10,2),(13,3),(17,4)):
            x,err=select_3adic_counterfeit(lo,hi,r)
            L=3**(r-1)
            self.assertEqual(x.denominator,3**r)
            self.assertEqual(x.numerator%3,1)
            self.assertLessEqual(err,Q(1,2*L)+(hi-lo)/2)
            self.assertLess(err*16**(N-1),Q(1,100))
            self.assertEqual(periodic_fejer_energy(r,L-1),1)

    def test_prime_covering_probes_do_not_equal_prime_moment_probes(self):
        # All prime covering degrees, even infinitely many, are non-separating:
        # one actual 16-periodic 1/27 orbit returns Haar mean 2 for F_p.
        # Prime EXPONENT moment probes are a different family.
        for p in (2,3,5,7,11,13,17,19,29):
            polynomial=covering(p)
            value=sum(c*periodic_moment(3,j)
                      for j,c in enumerate(polynomial))
            self.assertEqual(value,2)
        self.assertEqual(periodic_moment(3,11),
                         math.comb(22,11)+231)
        self.assertNotEqual(periodic_moment(3,11),
                            math.comb(22,11))

    def test_negative_mutations_and_source_refusal(self):
        self.assertNotEqual(haar_joint(16,(0,1),(16,1)),
                            2*math.comb(32,16))
        self.assertNotEqual(periodic_moment(3,9),math.comb(18,9))
        with self.assertRaises(ValueError):
            orbit_3adic(1)
        with self.assertRaises(ValueError):
            prime_carry_product(-1,3)
        with self.assertRaises(ValueError):
            select_3adic_counterfeit(3,4,2)

if __name__=="__main__":
    unittest.main()
