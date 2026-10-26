"""Independent rational witnesses for the prefix/jet obstruction theorem."""
import unittest
from fractions import Fraction as Q
from math import comb, factorial, prod

from observational_succ.spectral_purity_multiscale import (
    beta_even, even_moment, prefix_jet_counterfeit,
)
from observational_succ.succ_internal_matrix_walk import (
    authentic_r, formal_character, original_state,
)


def difference(function, n, order):
    return sum(((-1)**(order-j)*comb(order, j)*function(n+j)
                for j in range(order+1)), Q())


class MatchedPositiveOddSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = prefix_jet_counterfeit(2, 2)
        cls.holdout = prefix_jet_counterfeit(6, 6)

    def test_literal_signed_source_prefix_and_zero_anchor(self):
        for c in (self.witness, self.holdout):
            u = Q()
            self.assertEqual(c.state(0), 0)
            for n in range(1, c.prefix+1):
                literal = Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
                self.assertEqual(c.forcing(n), literal)
                u = 16*u+literal
                self.assertEqual(c.state(n), u)

    def test_full_lift_recurrence_on_unfitted_times(self):
        c = self.holdout
        for n in (0, 7, 23, 59, 127):
            self.assertEqual(c.state(n+1), 16*c.state(n)+c.forcing(n+1))

    def test_global_positivity_certificate_is_rational(self):
        for c in (self.witness, self.holdout):
            self.assertLess(c.correction_norm, Q(1,10))
            self.assertGreater(c.positivity_margin, Q(1,10))
            self.assertTrue(all(type(x) is Q for x in c.density))

    def test_independent_beta_expansion(self):
        for n in (0, 1, 5, 31):
            for k in range(9):
                expanded = sum((Q((-1)**j*comb(k,j), 8*n+2*j+1)
                                for j in range(k+1)), Q())
                self.assertEqual(beta_even(n,k), expanded)

    def test_tail_and_forcing_have_odd_denominators_on_holdouts(self):
        for c in (self.witness, self.holdout):
            self.assertEqual(c.seed.denominator % 2, 1)
            self.assertTrue(all(x.denominator % 2 for x in c.correction_newton))
            for n in (0, 1, 2, 7, 31, 257, 1009, 65537):
                self.assertEqual(c.tail(n).denominator % 2, 1)
                self.assertEqual(c.forcing(n+1).denominator % 2, 1)
                self.assertGreater(c.tail(n), 0)
                self.assertGreater(c.forcing(n+1), 0)

    def test_direct_density_source_integrals(self):
        c = self.witness
        for n in (0, 4, 17, 101):
            direct = sum((x*(Q(16,8*n+2*j+1)-Q(1,8*n+2*j+9))
                          for j,x in enumerate(c.density)), Q())
            self.assertEqual(direct, c.forcing(n+1))

    def test_newton_tail_against_independent_unexpanded_integrals(self):
        c = self.witness
        level = c.approximation_level
        def beta(exponent, order):
            return Q(2**order*factorial(order),
                     prod(exponent+2*j+1 for j in range(order+1)))
        for n in (0, 2, 13, 61):
            base = Q()
            for i in range(level+1):
                for r in range(i+1):
                    coefficient = Q((-1)**(i+r)*comb(i,r),15**(i+1))
                    base += coefficient*(4*beta(8*n+8*r,1)+2*beta(8*n+8*r+2,1))
                    for j in range(level+1):
                        m=j+1
                        a=Q(comb(2*m,m),4**m*(2*m-1))
                        base += coefficient*a*(2*beta(8*n+8*r+2,m)+beta(8*n+8*r+4,m))
            self.assertEqual(c.tail(n)-base, c.correction_tail(n))

    def test_endpoint_jets_against_literal_bbp_density(self):
        for c in (self.witness, self.holdout):
            # P(t)=4-2t^3-t^4-t^5, entirely separate from A_L construction.
            authentic = {0:Q(4),3:Q(-2),4:Q(-1),5:Q(-1)}
            forcing_density = {}
            for j,x in enumerate(c.density):
                forcing_density[2*j] = forcing_density.get(2*j,Q())+16*x
                forcing_density[2*j+8] = forcing_density.get(2*j+8,Q())-x
            for k in range(c.jet_order+1):
                def derivative(poly):
                    return sum((x*Q(factorial(j),factorial(j-k))
                                for j,x in poly.items() if j >= k), Q())
                self.assertEqual(derivative(forcing_density), derivative(authentic))

    def test_all_order_difference_bound_on_fresh_times(self):
        c = self.holdout
        for n in (0, 1, 11, 31, 257):
            for b in range(6):
                changed = difference(lambda k:c.forcing(k+1), n, b)
                original = difference(lambda k:authentic_r(k+1), n, b)
                self.assertLessEqual(abs(changed-original), c.forcing_difference_bound(n,b))
                self.assertGreater((-1)**b*changed, 0)

    def test_n_squared_and_n_cubed_bands_with_certified_mutation_error(self):
        c = self.witness
        for n in (4, 16, 64, 256, 4096):
            original_angle = n*n*authentic_r(n+1)
            counterfeit_angle = n*n*c.forcing(n+1)
            self.assertLessEqual(abs(counterfeit_angle-original_angle),
                                 n*n*c.forcing_difference_bound(n))
            original_drift = n**3*(authentic_r(n+1)-authentic_r(n+2))
            counterfeit_drift = n**3*(c.forcing(n+1)-c.forcing(n+2))
            self.assertLessEqual(abs(counterfeit_drift-original_drift),
                                 n**3*c.forcing_difference_bound(n,1))

    def test_periodic_seed_character_retains_maximal_limit(self):
        c = self.witness
        h = c.seed.denominator
        for n in (1, 3, 17, 31):
            self.assertEqual(formal_character(h,c.state(n)), formal_character(-h,c.tail(n)))
        # At the particular fixed character h, the paper proof T_n->0 gives 1.
        self.assertEqual(c.seed.denominator % 2, 1)

    def test_exact_four_pole_passport_is_not_claimed(self):
        c = self.witness
        self.assertNotEqual(c.forcing(c.prefix+1), authentic_r(c.prefix+1))
        self.assertNotEqual(c.state(c.prefix+1), original_state(c.prefix+1))

    def test_source_sign_and_anchor_mutations_rejected_by_equalities(self):
        n=2
        wrong = Q(4,8*n-7)+Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
        self.assertNotEqual(self.witness.forcing(n), wrong)
        self.assertNotEqual(self.witness.state(0)+Q(1,3), 0)

    def test_invalid_parameters_and_refinement_failure(self):
        for args in ((True,2),(1,0),(-1,2),(1,False)):
            with self.assertRaises(ValueError):
                prefix_jet_counterfeit(*args)
        with self.assertRaises(ValueError):
            prefix_jet_counterfeit(6,6,max_level=6)
        with self.assertRaises(ValueError):
            even_moment((0.5,),0)


if __name__ == '__main__':
    unittest.main()
