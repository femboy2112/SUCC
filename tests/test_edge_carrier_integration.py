"""Cross-implementation checks against previously existing SUCC Tate source laws."""
import random
import unittest
from fractions import Fraction as F
from itertools import combinations

from observational_succ.edge_carrier_reconstruction import (
    RationalSpan, SLocalization, ProfiniteProgram, GaussianInteger,
)
from observational_succ.finite_adele_localization import (
    FiniteAdeleSpan, RationalArchimedeanAdeleChart,
)
from observational_succ.tate_lattice_descent import (
    s_integer, multiplicative_reciprocity, modulo_padic_integral,
)


class EdgeCarrierIntegrationControls(unittest.TestCase):
    def test_all_small_primes_S_integer_atlas_matches_existing_tate_lattice(self):
        rng=random.Random(9340)
        sources=(2,3,5,7)
        for r in range(5):
            for subset in combinations(sources,r):
                S=SLocalization(subset)
                for _ in range(35):
                    x=RationalSpan(rng.randint(-100,100),rng.randint(1,100))
                    self.assertEqual(S.contains(x),s_integer(x.as_fraction(),subset))

    def test_new_profinite_integer_clock_matches_existing_genuine_padic_residue(self):
        for n in (-133,-6,-1,0,1,17,209):
            prog=ProfiniteProgram.integer(n)
            for p in (2,3,5,7):
                for k in (1,2,3,4):
                    modulus=p**k
                    self.assertEqual(prog.residue(modulus),
                                     modulo_padic_integral(F(n),p,k))

    def test_Q_is_exact_diagonal_in_new_Af_and_existing_product_formula(self):
        for rational in (F(1,6), F(7,12), F(-17,25), F(0), F(19)):
            a=RationalSpan(rational.numerator,rational.denominator)
            ad=FiniteAdeleSpan.diagonal_rational(a)
            arch=RationalArchimedeanAdeleChart.diagonal_rational(a)
            self.assertEqual(arch.real,rational)
            for p in (2,3,5,7):
                for k in (1,2):
                    r=ad.local_integral_scaled(p,k)
                    denom=rational.denominator
                    v=0
                    while denom%p==0:
                        denom//=p
                        v+=1
                    self.assertEqual(r["residue_of_p_to_v_times_x"],
                                     (rational.numerator*pow(denom,-1,p**k))%(p**k))
            if rational:
                self.assertEqual(multiplicative_reciprocity(rational)["global_product"],F(1))

    def test_imaginary_quadratic_source_does_not_fake_a_finite_adelic_place(self):
        z=GaussianInteger.from_pair(3,4)
        self.assertEqual(z.norm(),25)
        # Gaussian i is algebraic over Q, not a p-adic place or new prime p=4.
        with self.assertRaises(ValueError):
            # Existing source cannot construe 4 as authentic prime place.
            from observational_succ.diagonal_adele_zeta import valuation
            valuation(1,4)


if __name__=="__main__":
    unittest.main()
