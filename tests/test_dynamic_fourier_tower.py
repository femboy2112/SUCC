"""Exact source and full/partial Fourier debt regressions; no infinity claims."""
import random
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.diagonal_adele_zeta import DiagonalSourceError
from observational_succ.dynamic_fourier_tower import (
    _moduli, sum_fibers, lift_character, exact_fourier_restriction,
    exact_spectral_debt, verify_fourier_tower, observational_alias,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement, exact_dft


class FiniteDynamicFourierTests(unittest.TestCase):
    def test_exact_character_naturality_Z4_Z2(self):
        x = (F(1), F(2), F(-1), F(3))
        r = exact_fourier_restriction(x, 2, place_prime=2)
        self.assertEqual(r['dual_injection'], (0, 2))
        self.assertTrue(r['all_character_squares_exact'])
        self.assertEqual(sum_fibers(x, 2), (F(0), F(5)))

    def test_nonzero_fine_source_can_be_invisible_coarsely(self):
        x = (1, 0, -1, 0)
        y = (0, 0, 0, 0)
        r = observational_alias(x, y, 2)
        self.assertTrue(r['same_coarse_report'])
        self.assertFalse(r['source_states_identical'])
        self.assertEqual(r['fine_difference_energy'], 2)
        z = exact_spectral_debt(x, 2)
        self.assertEqual(z['retained_energy'], 0)
        self.assertEqual(z['fine_energy'], F(2))
        self.assertEqual(z['unseen_spectral_debt'], F(2))
        self.assertFalse(z['observer_can_know_debt_from_coarse_report_alone'])

    def test_exact_rational_parseval_small_exhaustion(self):
        for x in product((-1, 0, 1), repeat=4):
            r = exact_spectral_debt(x, 2)
            self.assertEqual(r['unseen_spectral_debt'],
                             r['omitted_fourier_energy'])
            self.assertGreaterEqual(r['unseen_spectral_debt'], 0)

    def test_fourier_functor_across_nontrivial_divisors(self):
        for m, n in ((4, 2), (6, 2), (6, 3), (8, 2),
                     (8, 4), (9, 3), (12, 3), (12, 4)):
            x = tuple(F(i*i-3*i+2, i+1) for i in range(m))
            receipt = exact_fourier_restriction(x, n)
            self.assertTrue(receipt['all_character_squares_exact'])
            self.assertEqual(len(receipt['dual_injection']), n)

    def test_genuinely_composite_refinement(self):
        x = tuple(F((i*7)%11, i+1) for i in range(12))
        self.assertEqual(sum_fibers(sum_fibers(x, 6), 2), sum_fibers(x, 2))
        self.assertEqual(sum_fibers(sum_fibers(x, 4), 2), sum_fibers(x, 2))
        a = verify_fourier_tower(x, (12, 6, 2), source_id='Q-clock',source_version=1)
        b = verify_fourier_tower(x, (12, 4, 2), source_id='Q-clock',source_version=1)
        self.assertEqual(a['total_debt'], b['total_debt'])
        self.assertNotEqual(a['stage_debts'], b['stage_debts'])

    def test_prime_power_places(self):
        for p, levels in ((2, (8, 4, 2)),(3, (9, 3)), (2, (16, 4, 2))):
            x = tuple(F(i%5-2) for i in range(levels[0]))
            r = verify_fourier_tower(x, levels, source_id=f'p{p}',source_version=0,
                                     place_prime=p)
            self.assertTrue(r['composition_square'])
            self.assertEqual(sum(r['stage_debts']),r['total_debt'])

    def test_character_lift_exact_against_restriction(self):
        for m, n in ((4,2),(6,3),(8,4),(12,3)):
            x = tuple(F(i%7-3) for i in range(m))
            A=exact_dft(sum_fibers(x,n)); B=exact_dft(x)
            for r in range(n):
                self.assertEqual(lift_character(A[r],m), B[(m//n)*r])

    def test_zero_source_has_no_debt(self):
        r = verify_fourier_tower((0,)*8,(8,4,2),source_id='zeros',source_version=0)
        self.assertEqual(r['total_debt'],0)
        self.assertEqual(r['stage_debts'],(F(0),F(0)))

    def test_perfectly_retained_constant_source(self):
        r = verify_fourier_tower((1,)*8,(8,4,2),source_id='constant',source_version=0)
        self.assertEqual(r['total_debt'],0)
        self.assertEqual(r['energy_by_level'],(F(8),F(8),F(8)))

    def test_sparse_mutations_cause_positive_unobserved_energy(self):
        x=(1,0,0,0,0,0,0,0)
        r=verify_fourier_tower(x,(8,4,2),source_id='spike',source_version=5)
        self.assertEqual(r['energy_by_level'],(F(1),F(1,2),F(1,4)))
        self.assertEqual(r['stage_debts'],(F(1,2),F(1,4)))
        self.assertEqual(r['total_debt'],F(3,4))

    def test_fake_source_and_incompatible_clocks_rejected(self):
        with self.assertRaises(DiagonalSourceError):
            exact_spectral_debt((1,2,3,4),3)
        with self.assertRaises(DiagonalSourceError):
            exact_spectral_debt((1,2,3,4),2,place_prime=6)
        with self.assertRaises(DiagonalSourceError):
            exact_spectral_debt((1,2,3,4,5,6),2,place_prime=2)
        with self.assertRaises(DiagonalSourceError):
            verify_fourier_tower((1,)*8,(8,2,4),source_id='x',source_version=0)
        with self.assertRaises(DiagonalSourceError):
            verify_fourier_tower((1,)*8,(8,4,2),source_id='',source_version=0)
        with self.assertRaises(DiagonalSourceError):
            verify_fourier_tower((1,)*8,(8,4,2),source_id='x',source_version=-1)
        with self.assertRaises(DiagonalSourceError):
            exact_spectral_debt((1.0,2,3,4),2)

    def test_random_independent_energy_crosschecks(self):
        rng = random.Random(10112)
        for m, n in ((4,2),(6,3),(8,4),(9,3),(12,6)):
            for _ in range(15):
                x=tuple(F(rng.randrange(-3,4), rng.randrange(1,5)) for i in range(m))
                receipt=exact_spectral_debt(x,n)
                self.assertEqual(receipt['fine_energy']-receipt['retained_energy'],
                                 receipt['omitted_fourier_energy'])


if __name__=='__main__':
    unittest.main()

class FourierClaimTransportTests(unittest.TestCase):
    def test_claim_factors_through_coarse_exactly_for_fiber_constant_weights(self):
        from observational_succ.dynamic_fourier_tower import claim_target_debt
        x = (1,0,-1,0)
        yes = claim_target_debt(x, (2,3,2,3), 2)
        self.assertTrue(yes['claim_factors_through_coarse_observer'])
        self.assertEqual(yes['actual_squared_claim_loss'],0)
        no = claim_target_debt(x, (1,0,-1,0), 2)
        self.assertFalse(no['claim_factors_through_coarse_observer'])
        self.assertEqual(no['source_debt'],2)
        self.assertEqual(no['actual_squared_claim_loss'],4)
        self.assertEqual(no['upper_squared_claim_loss'],4)

    def test_unbounded_claim_prevents_spurious_limit_transport(self):
        from observational_succ.dynamic_fourier_tower import disappearing_energy_unbounded_claim
        for n in (1,2,5,20,100):
            r=disappearing_energy_unbounded_claim(n)
            self.assertEqual(r['unseen_energy'],F(2,n*n))
            self.assertEqual(r['squared_original_claim_error'],4*n*n)
            self.assertFalse(r['uniform_operator_norm_available'])

    def test_claim_transport_exhaustive_small_rational(self):
        from observational_succ.dynamic_fourier_tower import claim_target_debt
        for x in product((0,1,-1),repeat=4):
            for a in ((1,0,1,0),(1,0,-1,0),(1,2,3,4),(-1,1,-1,1)):
                r=claim_target_debt(x,a,2)
                self.assertLessEqual(r['actual_squared_claim_loss'],r['upper_squared_claim_loss'])

class DynamicSourceChangeTests(unittest.TestCase):
    @staticmethod
    def matrix_from_action(m,func):
        rows=[[F(0)]*m for _ in range(m)]
        for j in range(m):
            rows[func(j)][j]=F(1)
        return rows

    def test_shift_and_unit_fucc_act_on_coarse_observers(self):
        from observational_succ.dynamic_fourier_tower import source_update_descent
        for m,n in ((4,2),(8,4),(9,3),(12,3)):
            shift=self.matrix_from_action(m,lambda j:(j+1)%m)
            r=source_update_descent(shift,n)
            self.assertTrue(r['coarse_dynamics_exists'])
            for h in range(n):
                self.assertEqual(r['induced_coarse_matrix'][(h+1)%n][h],1)
        for m,n,mult in ((4,2,3),(9,3,2),(8,2,3)):
            shift=self.matrix_from_action(m,lambda j:(mult*j)%m)
            r=source_update_descent(shift,n)
            self.assertTrue(r['coarse_dynamics_exists'])

    def test_reversible_shear_reveals_hidden_fine_source(self):
        from observational_succ.dynamic_fourier_tower import source_update_descent
        # Matrix U=I+E_{0,2} invertible with inverse I-E_{0,2}.
        rows=[[F(int(i==j)) for j in range(4)] for i in range(4)]
        rows[0][2]=1
        r=source_update_descent(rows,2)
        self.assertFalse(r['coarse_dynamics_exists'])
        self.assertEqual(r['obstruction_invisible_source'],(-1,0,1,0))
        self.assertEqual(r['obstruction_revealed_report'],(1,0))
        self.assertFalse(r['RH_or_physical_entanglement_claimed'])

    def test_fine_update_preserves_kernel_not_necessarily_source(self):
        from observational_succ.dynamic_fourier_tower import source_update_descent
        # Reshuffle only within each quotient fiber.
        rows=self.matrix_from_action(4,lambda j:(j+2)%4)
        r=source_update_descent(rows,2)
        self.assertTrue(r['coarse_dynamics_exists'])
        self.assertEqual(r['induced_coarse_matrix'],((1,0),(0,1)))

    def test_random_two_coarsening_test(self):
        from observational_succ.dynamic_fourier_tower import source_update_descent
        rng=random.Random(712)
        for m,n in ((4,2),(6,3),(8,4)):
            for _ in range(30):
                # Build U by arbitrary independent permutations INSIDE each fiber.
                targets=list(range(m))
                for h in range(n):
                    fiber=[h+t*n for t in range(m//n)]
                    new=fiber[:]
                    rng.shuffle(new)
                    for i,j in zip(fiber,new): targets[i]=j
                U=self.matrix_from_action(m,lambda j:targets[j])
                r=source_update_descent(U,n)
                self.assertTrue(r['coarse_dynamics_exists'])
                self.assertEqual(r['induced_coarse_matrix'],tuple(tuple(F(i==j) for j in range(n)) for i in range(n)))

    def test_invalid_source_update_rejected(self):
        from observational_succ.dynamic_fourier_tower import source_update_descent
        with self.assertRaises(DiagonalSourceError):
            source_update_descent(((1,0),(0,1)),3)
        with self.assertRaises(DiagonalSourceError):
            source_update_descent(((1,2,3,4),)*4,2.0)
        with self.assertRaises(DiagonalSourceError):
            source_update_descent(((1,2),(3,4),(5,6),(7,8)),2)
