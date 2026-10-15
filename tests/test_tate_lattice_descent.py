"""Exact finite controls for Tate S-lattice/character compatibility.

Checks rational dense coordinate arithmetic; NOT a numerical or formal
verification of the full locally compact/topological or analytic theorems.
"""
import random
import unittest
from fractions import Fraction as F

from observational_succ.tate_lattice_descent import (
    RationalSChart, TateLatticeError, character_naturality,
    finite_depth_alias, prime_atlas, s_integer, s_modulus_receipt, s_unit,
    successor_history_kernel, prime_extension_obstruction,
)


class AtlasAndLatticeTests(unittest.TestCase):
    def test_valid_prime_atlas(self):
        self.assertEqual(prime_atlas(()), ())
        self.assertEqual(prime_atlas((2, 3, 5)), (2, 3, 5))
        for ps in ((4,), (6,), (2, 2), (5, 2), (1,), (True,), [2, 3]):
            with self.subTest(primes=ps), self.assertRaises(TateLatticeError):
                prime_atlas(ps)

    def test_s_integers_s_units(self):
        self.assertTrue(s_integer(F(7, 24), (2, 3)))
        self.assertFalse(s_integer(F(7, 35), (2, 3)))
        self.assertTrue(s_unit(F(-72, 25), (2, 3, 5)))
        self.assertFalse(s_unit(F(7, 24), (2, 3)))
        self.assertTrue(s_integer(0, ()))
        self.assertFalse(s_unit(0, ()))

    def test_lattice_automorphism_rigidity(self):
        for S in ((), (2,), (2, 3), (2, 3, 5)):
            nums = (-1, 1) + tuple(F(p) for p in S)
            for a in nums:
                for b in nums:
                    if b == 0:
                        continue
                    q = F(a) / F(b)
                    if s_unit(q, S):
                        receipt = s_modulus_receipt(q, S)
                        self.assertEqual(receipt['local_haar_modulus'], 1)
                        self.assertTrue(receipt['lattice_automorphism'])
                        self.assertEqual(receipt['quotient_cover_degree'], 1)

    def test_missing_primes_and_cover_degree(self):
        receipt = s_modulus_receipt(30, (2, 3))
        self.assertEqual(receipt['local_haar_modulus'], 5)
        self.assertEqual(receipt['outside_prime_defect'], 5)
        self.assertTrue(receipt['lattice_inclusion'])
        self.assertFalse(receipt['lattice_automorphism'])
        self.assertEqual(receipt['quotient_cover_degree'], 5)
        miss = s_modulus_receipt(F(1, 7), (2, 3))
        self.assertEqual(miss['local_haar_modulus'], F(1, 7))
        self.assertFalse(miss['lattice_inclusion'])
        self.assertIsNone(miss['quotient_cover_degree'])
        self.assertEqual(s_modulus_receipt(F(-12, 25), (2, 3, 5))['outside_prime_defect'], 1)

    def test_zero_forbidden(self):
        with self.assertRaises(TateLatticeError):
            s_modulus_receipt(0, (2,))


class GaugeAndDescentTests(unittest.TestCase):
    def test_phase_cancellation_for_lattice(self):
        for S in ((), (2,), (3,), (2, 3), (2, 3, 5)):
            for gamma in (0, 1, -5, F(1, 6), F(-7, 8), F(5, 9)):
                if not s_integer(gamma, S):
                    continue
                chart = RationalSChart(S, F(gamma), tuple(F(gamma) for _ in S))
                for q in (0, 1, -7, F(1, 6), F(-5, 8), F(2, 9)):
                    if s_integer(q, S):
                        self.assertEqual(chart.character_phase(q), 0)

    def test_canonical_gauge_invariance(self):
        original = RationalSChart((2, 3), F(13, 17), (F(-17, 24), F(25, 18)))
        normal = original.canonical()
        self.assertTrue(original.equivalent(normal))
        self.assertEqual(normal, normal.canonical())
        for d in (1, -3, F(5, 18), F(11, 16)):
            shifted = original.diagonal_shift(d)
            self.assertTrue(original.equivalent(shifted))
            self.assertEqual(normal, shifted.canonical())
            for q in (0, 1, -3, F(1, 18), F(7, 8)):
                self.assertEqual(original.character_phase(q), shifted.character_phase(q))

    def test_archimedean_only_is_circle(self):
        x = RationalSChart((), F(17, 6), ())
        self.assertEqual(x.canonical().arch, F(5, 6))
        self.assertEqual(x.character_phase(3), F(1, 2))
        self.assertTrue(x.equivalent(x.diagonal_shift(-2)))
        with self.assertRaises(TateLatticeError):
            x.diagonal_shift(F(1, 2))

    def test_projection_single_omitted_place(self):
        chart = RationalSChart((2,), F(0), (F(1, 2),))
        projected = chart.project(())
        self.assertEqual(projected.arch, F(1, 2))
        self.assertEqual(chart.character_phase(1), projected.character_phase(1))
        self.assertNotEqual(chart.character_phase(1), F(0))
        self.assertEqual(chart.project((2,)).canonical(), chart.canonical())

    def test_projection_tower_and_character_naturality(self):
        T = (2, 3, 5)
        charts = [
            RationalSChart(T, F(4, 7), (F(1, 2), F(1, 3), F(1, 5))),
            RationalSChart(T, F(-17, 91), (F(17, 16), F(-11, 27), F(3, 125))),
        ]
        subsets = ((), (2,), (3,), (5,), (2, 3), (2, 5), (3, 5), T)
        for x in charts:
            for S in subsets:
                ys = x.project(S)
                self.assertEqual(ys, ys.canonical())
                for q in (0, 1, -1, 7, F(1, 8), F(-7, 9), F(6, 25), F(1, 30)):
                    if s_integer(q, S):
                        self.assertTrue(character_naturality(x, S, q)['commutes'])
                for R in subsets:
                    if set(R).issubset(S):
                        self.assertEqual(x.project(S).project(R), x.project(R))

    def test_mutation_naive_drop_is_not_a_bonding_map(self):
        x = RationalSChart((2,), F(0), (F(1, 2),))
        naive_phase = x.arch % 1  # naive loss of 2-adic coordinate
        self.assertNotEqual(naive_phase, x.character_phase(1))
        self.assertEqual(x.project(()).character_phase(1), x.character_phase(1))

    def test_source_and_domain_firewalls(self):
        x = RationalSChart((2,), 0, (F(1, 2),), 'authentic', 7)
        y = RationalSChart((2,), 0, (F(1, 2),), 'forged', 7)
        with self.assertRaises(TateLatticeError):
            x.equivalent(y)
        with self.assertRaises(TateLatticeError):
            x.project((3,))
        with self.assertRaises(TateLatticeError):
            x.character_phase(F(1, 3))
        with self.assertRaises(TateLatticeError):
            x.diagonal_shift(F(1, 3))
        with self.assertRaises(TateLatticeError):
            RationalSChart.from_places((2, 3), 0, {2: 0}, source_id='authentic')
        with self.assertRaises(TateLatticeError):
            RationalSChart((2,), 0, (F(1, 2),), '', 0)

    def test_cross_stage_gauge_descent(self):
        x = RationalSChart((2, 3, 5), F(-4, 7), (F(2, 3), F(4, 9), F(6, 25)))
        y = x.diagonal_shift(F(7, 30))
        for S in ((), (2,), (3, 5), (2, 3, 5)):
            self.assertTrue(x.project(S).equivalent(y.project(S)))

    def test_seeded_holdout_exact(self):
        rng = random.Random(882035)
        base = (2, 3, 5)
        menus = ((), (2,), (2, 3), (3, 5), base)
        for _ in range(250):
            vals = [F(rng.randint(-40, 40), rng.randint(1, 40)) for _ in range(4)]
            x = RationalSChart(base, vals[0], tuple(vals[1:]))
            gamma = F(rng.randint(-30, 30), 2**rng.randint(0, 3)*3**rng.randint(0, 3))
            y = x.diagonal_shift(gamma)
            for S in menus:
                self.assertEqual(x.project(S), y.project(S))
                for q in (0, 1, F(1, 8), F(1, 9), F(1, 25), F(1, 30)):
                    if s_integer(q, S):
                        self.assertEqual(x.character_phase(q), x.project(S).character_phase(q))


class HistoryFaithfulnessTests(unittest.TestCase):
    def test_nonzero_successor_collapses_on_quotient(self):
        for S, d in (((), 1), ((2,), F(1, 2)), ((2, 3), F(-5, 18))):
            result = successor_history_kernel(S, d)
            self.assertTrue(result['lift_changes'])
            self.assertTrue(result['same_global_quotient_state'])
            self.assertFalse(result['quotient_state_functor_faithful_on_events'])
            self.assertEqual(result['event_displacement'], d)

    def test_unlawful_successor_rejected(self):
        with self.assertRaises(TateLatticeError):
            successor_history_kernel((2,), F(1, 3))
        with self.assertRaises(TateLatticeError):
            successor_history_kernel((2,), 0)


class FiniteObservabilityTests(unittest.TestCase):
    def test_hidden_source_until_deeper_probe(self):
        for p in (2, 3, 5):
            for k in (0, 1, 2, 4, 8):
                r = finite_depth_alias(p, k)
                self.assertTrue(r['all_shallow_character_phases_zero'])
                self.assertTrue(r['nonzero_quotient_class'])
                self.assertNotEqual(r['first_deeper_phase'], 0)
                self.assertFalse(r['finite_depth_complete'])

    def test_a_finite_probe_family_does_not_identify_global_source(self):
        x = RationalSChart((2,), 0, (F(2**20),))
        z = RationalSChart((2,), 0, (F(0),))
        self.assertFalse(x.equivalent(z))
        self.assertEqual([x.character_phase(F(1, 2**j)) for j in range(10)], [F(0)]*10)
        self.assertEqual(x.character_phase(F(1, 2**21)), F(1, 2))


class NonsplitPrimeExtensionTests(unittest.TestCase):
    def test_p_extension_nonzero_kernel_and_dual_torsion(self):
        for S, new_p in (((), 2), ((), 3), ((2,), 3), ((2, 3), 5), ((3, 5), 2)):
            r = prime_extension_obstruction(S, new_p)
            self.assertTrue(r['projects_to_identity'])
            self.assertTrue(r['nonzero_rational_kernel_class'])
            self.assertEqual(r['order_in_dual_quotient'], new_p)
            self.assertFalse(r['global_extension_split'])
            self.assertFalse(r['continuous_section_exists'])
            self.assertFalse(r['full_topological_claim_proved_by_execution'])

    def test_new_prime_must_be_genuine_and_not_repeated(self):
        for S, p in (((2,), 2), ((2,), 6), ((), 1), ((), True), ((2, 3), 4)):
            with self.subTest(S=S, p=p), self.assertRaises(TateLatticeError):
                prime_extension_obstruction(S, p)

    def test_kernel_nonzero_is_not_quasi_prime_multiplication(self):
        r = prime_extension_obstruction((), 5)
        self.assertEqual(r['T'], (5,))
        self.assertEqual(r['dual_torsion_witness'], F(1, 5))
        self.assertFalse(s_integer(F(1, 5), ()))
        self.assertTrue(s_integer(F(1, 5), (5,)))


if __name__ == '__main__':
    unittest.main()
