"""Original source regression tests, with full-checkout bridge if import exists."""
import unittest
from fractions import Fraction as F
from observational_succ.origin_fiber_arithmetic_observer import (
    compressed_channel_additive_sq, source_carry_difference_times_sq,
)


def frozen_original_forcing_formula(n):
    if type(n) is not int or n<1:raise ValueError('source starts n=1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def original_orbit(max_n,seed=F(0)):
    U=F(seed);out=[U]
    for n in range(1,max_n+1):
        U=16*U+frozen_original_forcing_formula(n)
        out.append(U)
    return out


class GenuineBBPSourceFiberTests(unittest.TestCase):
    def test_original_four_poles_rational(self):
        for n in range(1,70):
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            a=120*n*n-89*n+16
            self.assertEqual(frozen_original_forcing_formula(n),F(a,d))

    def test_original_original_r_positive(self):
        for n in range(1,70):self.assertGreater(frozen_original_forcing_formula(n),0)

    def test_source_15torsion_seed_gauge(self):
        # Original recurrence U_n(s)=U_n(0)+16^n s. If 15 s integer,
        # 16^n s-s is integer for every n. Relative phases cannot tell
        # these changed seeds apart; absolute origin phase can.
        for s in [F(1,3),F(1,5),F(1,15),F(7,15)]:
            A=original_orbit(16)
            B=original_orbit(16,s)
            for n in range(0,17):
                self.assertEqual(B[n]-A[n]-s,(16**n-1)*s)
                self.assertEqual((B[n]-A[n])%1,s%1)

    def test_source_carry_commutator_not_a_normality_proof(self):
        import cmath,math
        orbit=original_orbit(26)
        f=lambda n:complex(cmath.exp(2j*math.pi*float(orbit[n]%1)))
        for n in range(1,13):
            E=source_carry_difference_times_sq(n,f)
            self.assertGreaterEqual(E,0)
            self.assertLessEqual(E,2.00000001)
        # A uniform global root of unity multiplies all f(n), preserving
        # every quadratic relative-difference energy.
        phase=complex(cmath.exp(2j*math.pi/3))
        for n in range(1,13):
            g=lambda j:phase*f(j)
            self.assertAlmostEqual(source_carry_difference_times_sq(n,f),source_carry_difference_times_sq(n,g),places=12)

    def test_source_exact_import_full_checkout(self):
        try:
            from observational_succ.bbp_natural_carrier import exact_forcing
            from observational_succ.rank_two_chiral_towers import authentic_four_poles
        except ImportError:
            self.skipTest('requires full Main XIII/SUCC checkout; isolated local code does not include original modules')
        for n in range(1,80):
            self.assertEqual(frozen_original_forcing_formula(n),exact_forcing(n))
            self.assertEqual(frozen_original_forcing_formula(n),authentic_four_poles(n))

if __name__=='__main__':unittest.main()
