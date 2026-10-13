"""Independent exact arithmetic controls; paper proofs remain separate."""
import itertools
import random
import unittest
from fractions import Fraction as Q
from math import comb, factorial, gcd

from observational_succ.arithmetic import factorization, source_at
from observational_succ.core import Scalar, I, ONE, ZERO
from observational_succ.swarm_arithmetic import (
    AffineAction, ArithmeticTransportError, cyclic_frame_offsets,
    verify_cyclic_frame, factor_square, factorial_valuation,
    mahler_prefix_ambiguity, dirichlet_log, euler_audit,
    valuation_covariance, gamma_cutoff_recurrence, gaussian_component,
    verify_gaussian_closed, displacement_transport,
    projected_resolvent_numerator,
)


def ordered_factor_log(source, n):
    """Independent signed ordered-factor history expansion, not recurrence."""
    result = ZERO
    def visit(remainder, length, amplitude):
        nonlocal result
        if remainder == 1:
            result += Q((-1)**(length+1), length)*amplitude
            return
        for d in range(2, remainder+1):
            if remainder % d == 0:
                visit(remainder//d, length+1, amplitude*source[d])
    visit(n, 0, ONE)
    return result


def prime_oracle(n):
    return n >= 2 and all(n % d for d in range(2, n))


def gaussian_oracle(z):
    a, b = z
    if a and b:
        return prime_oracle(a*a+b*b)
    t = abs(a or b)
    return prime_oracle(t) and t % 4 == 3


class AffineTransportTests(unittest.TestCase):
    def test_noncommuting_relation_and_associativity(self):
        s = AffineAction(1, 1)
        for p in (2, 3, 5, 6, 11):
            v = AffineAction(p)
            self.assertEqual(v.compose(s), AffineAction(1, p).compose(v))
            self.assertNotEqual(v.compose(s), s.compose(v))
        rng = random.Random(336)
        for _ in range(160):
            x, y, z = [AffineAction(rng.randint(1, 6), rng.randint(0, 8)) for _ in range(3)]
            self.assertEqual(x.compose(y).compose(z), x.compose(y.compose(z)))
            for n in (0, 1, 19):
                self.assertEqual(x.compose(y)(n), x(y(n)))

    def test_all_small_permutations_independent_classification(self):
        for m in range(1, 8):
            for slopes in ((), (3,), (3, 5), (2,), (6,)):
                observed = tuple(p for p in itertools.permutations(range(m))
                                 if verify_cyclic_frame(p, slopes))
                predicted = tuple(tuple((x+c) % m for x in range(m))
                                  for c in cyclic_frame_offsets(m, slopes))
                self.assertEqual(observed, predicted)

    def test_missing_prime_two_retains_half_clock_gauge(self):
        self.assertEqual(cyclic_frame_offsets(12, (3, 5, 7)), (0, 6))
        self.assertEqual(cyclic_frame_offsets(12, (2, 3, 5, 7)), (0,))
        self.assertEqual(cyclic_frame_offsets(12, (5,)), (0, 3, 6, 9))
        self.assertFalse(verify_cyclic_frame(tuple(reversed(range(7))), (2,)))

    def test_quotient_square_keeps_action_cross_term(self):
        for m in (2, 3, 12, 35):
            for n in range(80):
                a = AffineAction(6, 7)
                self.assertEqual(a(n) % m, a(n % m) % m)
        self.assertEqual(AffineAction(6, 1).residue(3, 5), 4)
        self.assertEqual(AffineAction(1, 1).compose(AffineAction(6))(3), 19)
        self.assertEqual(AffineAction(6).compose(AffineAction(1, 1))(3), 24)

    def test_domain_mutations(self):
        for args in ((0, 1), (2, -1), (True, 1), (2.0, 1)):
            with self.assertRaises(ArithmeticTransportError):
                AffineAction(*args)
        with self.assertRaises(ArithmeticTransportError): verify_cyclic_frame((0, 0), (2,))
        with self.assertRaises(ArithmeticTransportError): verify_cyclic_frame((0, 1), (False,))


class ValuationAndMahlerTests(unittest.TestCase):
    def test_factor_square_and_valuation_event_ladder(self):
        for n in range(1, 181):
            expected = tuple((d, n//d) for d in range(1, n+1) if n % d == 0 and d*d <= n)
            self.assertEqual(factor_square(n), expected)
            for p in (2, 3, 5, 7):
                event_sum = sum(dict(factorization(k)).get(p, 0) for k in range(1, n+1))
                self.assertEqual(factorial_valuation(n, p), event_sum)
        self.assertEqual(factor_square(36), ((1, 36), (2, 18), (3, 12), (4, 9), (6, 6)))

    def test_unbounded_successor_valuation_jump(self):
        for p in (2, 3, 5):
            for r in range(1, 8):
                if p**r <= 1_000_000:
                    self.assertEqual(dict(factorization(p**r-1)).get(p, 0), 0)
                    self.assertEqual(dict(factorization(p**r)).get(p, 0), r)

    def test_mahler_rivals_agree_then_separate(self):
        for n in (0, 1, 9, 31, 128):
            for p in (2, 3, 5):
                r = mahler_prefix_ambiguity(n, p)
                self.assertEqual(r['zero_prefix'], r['continuous_polynomial_prefix'])
                self.assertEqual(r['continuous_polynomial_next'], comb(n+1, n+1))
                self.assertGreater(r['discontinuous_spike_first'], n)
                self.assertEqual(r['discontinuous_spike_first'], p**r['discontinuous_spike_exponent'])
        with self.assertRaises(ArithmeticTransportError): mahler_prefix_ambiguity(10, 6)


class DirichletLogTests(unittest.TestCase):
    def test_independent_ordered_paths_random_complex_holdouts(self):
        rng = random.Random(36038)
        for _ in range(24):
            a = {1: ONE}
            a.update({n: Scalar(Q(rng.randint(-3, 3), 2), Q(rng.randint(-2, 2), 3))
                      for n in range(2, 25)})
            b = dirichlet_log(a, 24)
            for n in range(2, 25):
                self.assertEqual(b[n], ordered_factor_log(a, n))
            euler_audit(a, 24)

    def test_zeta_prime_power_support_and_degree_one_rays(self):
        a = {n: ONE for n in range(1, 129)}
        b = dirichlet_log(a, 128)
        for n in range(2, 129):
            f = factorization(n)
            self.assertEqual(b[n], Scalar(Q(1, f[0][1])) if len(f) == 1 else ZERO)
        r = euler_audit(a, 128, conductor=1)
        self.assertFalse(r['mixed_log_support'])
        self.assertFalse(r['degree_one_ray_defects'])
        self.assertFalse(r['unit_or_ramification_defects'])
        self.assertFalse(r['conductor_periodicity_defects'])

    def test_prime_support_does_not_imply_degree_one(self):
        # divisor-count source: Euler local factor (1-X)^-2.
        a = {n: Scalar(len([d for d in range(1, n+1) if n % d == 0])) for n in range(1, 65)}
        r = euler_audit(a, 64)
        self.assertFalse(r['mixed_log_support'])
        self.assertIn(4, r['degree_one_ray_defects'])
        self.assertIn(2, r['unit_or_ramification_defects'])
        self.assertEqual(dirichlet_log(a, 64)[4], ONE)

    def test_fake_six_nonunit_and_non_euler_controls(self):
        z = {n: ONE for n in range(1, 65)}
        z[6] = Scalar(2)
        self.assertEqual(dirichlet_log(z, 64)[6], ONE)
        self.assertIn(6, euler_audit(z, 64)['mixed_log_support'])
        nonunit = {n: Scalar(2**dict(factorization(n)).get(2, 0)) for n in range(1, 65)}
        r = euler_audit(nonunit, 64)
        self.assertFalse(r['mixed_log_support'])
        self.assertFalse(r['degree_one_ray_defects'])
        self.assertIn(2, r['unit_or_ramification_defects'])
        mixture = {n: source_at(n, 'mixture5') for n in range(1, 65)}
        self.assertIn(6, euler_audit(mixture, 64)['mixed_log_support'])

    def test_authentic_character_and_altered_prime_phase(self):
        chi = {n: source_at(n, 'chi5') for n in range(1, 65)}
        r = euler_audit(chi, 64, conductor=5)
        self.assertTrue(all(not r[k] for k in (
            'mixed_log_support', 'degree_one_ray_defects',
            'unit_or_ramification_defects', 'conductor_periodicity_defects')))
        # Change only the prime-2 phase and propagate multiplicatively.
        mutant = {n: chi[n]*((-ONE)**dict(factorization(n)).get(2, 0)) for n in chi}
        m = euler_audit(mutant, 64, conductor=5)
        self.assertFalse(m['mixed_log_support'])
        self.assertFalse(m['degree_one_ray_defects'])
        self.assertFalse(m['unit_or_ramification_defects'])
        self.assertIn(2, m['conductor_periodicity_defects'])
        self.assertEqual(valuation_covariance(chi, 64, (2, 3)),
                         valuation_covariance(mutant, 64, (2, 3)))

    def test_prefix_filtration_and_missing_source_not_zero(self):
        a = {n: Scalar((n % 5)-2) for n in range(2, 65)}
        a[1] = ONE
        self.assertEqual(dirichlet_log(a, 64)[:25], dirichlet_log(a, 24))
        del a[6]
        with self.assertRaises(ArithmeticTransportError): dirichlet_log(a, 64)
        with self.assertRaises(ArithmeticTransportError): dirichlet_log({1: 2, 2: 1}, 2)

    def test_covariance_indistinguishability_countermodel(self):
        authentic = {n: ONE for n in range(1, 33)}
        mutant = dict(authentic)
        mutant[6] = -ONE
        c = valuation_covariance(authentic, 32, (2, 3))
        self.assertEqual(c, valuation_covariance(mutant, 32, (2, 3)))
        self.assertGreater(c[0][0], 0)
        self.assertGreater(c[1][1], 0)
        self.assertGreater(c[0][0]*c[1][1]-c[0][1]*c[1][0], 0)
        self.assertEqual(dirichlet_log(authentic, 32)[6], ZERO)
        self.assertEqual(dirichlet_log(mutant, 32)[6], Scalar(-2))


class BoundaryAndSpectralTests(unittest.TestCase):
    def test_exact_gamma_boundary_defect_independent_factorials(self):
        for n in (2, 3, 17, 64):
            for z in (1, 2, 5, 12):
                gamma = lambda k: Q(factorial(n)*n**k, factorial(n+k)//factorial(k-1))
                r = gamma_cutoff_recurrence(n, z)
                self.assertEqual(gamma(z+1)/gamma(z), r['ratio'])
                self.assertEqual(r['defect'], r['boundary_defect'])
                self.assertGreater(r['defect'], 0)

    def test_gaussian_actual_source_closed_component_mutations(self):
        c = gaussian_component((1, 1), 1)
        self.assertEqual(c, ((1, 1), (1, 2), (2, 1)))
        self.assertTrue(verify_gaussian_closed(c, 1))
        self.assertFalse(verify_gaussian_closed(c[1:], 1))
        self.assertTrue(all(gaussian_oracle(z) for z in c))
        with self.assertRaises(ArithmeticTransportError): verify_gaussian_closed(c+((3, 4),), 1)
        with self.assertRaises(ArithmeticTransportError): gaussian_component((1, 1), 1, max_vertices=2)
        with self.assertRaises(ArithmeticTransportError): gaussian_component((3, 4), 1)
        self.assertFalse(verify_gaussian_closed(c, 2))

    def test_gaussian_source_classification_independent_window(self):
        from observational_succ.gaussian_holonomy import gaussian_prime
        for a in range(-9, 10):
            for b in range(-9, 10):
                self.assertEqual(gaussian_prime((a, b)), gaussian_oracle((a, b)))

    def test_actual_displacement_and_quotient_winding(self):
        path = ((1, 1), (1, 2), (2, 2), (2, 1), (1, 1))
        self.assertEqual(displacement_transport(path), (0, 0))
        self.assertEqual(displacement_transport(((0, 1), (5, 1))), (5, 0))
        self.assertEqual((0 % 5, 1 % 5), (5 % 5, 1 % 5))

    def test_projection_zeros_move_source_poles_fixed(self):
        for alpha in (Q(1, 5), Q(1, 2), Q(4, 5)):
            r = projected_resolvent_numerator(alpha)
            z = r['numerator_zero']
            self.assertEqual(alpha/(z-1)+(1-alpha)/(z-2), 0)
            self.assertEqual(r['source_poles'], (1, 2))
            self.assertTrue(r['zero_is_uncancelled'])
        self.assertFalse(projected_resolvent_numerator(0)['zero_is_uncancelled'])
        self.assertFalse(projected_resolvent_numerator(1)['zero_is_uncancelled'])
        with self.assertRaises(ArithmeticTransportError): projected_resolvent_numerator(0.5)

    def test_full_basis_similarity_preserves_characteristic_polynomial(self):
        # Rational unitary basis; the full characteristic polynomial is
        # invariant even though scalar projection zeros vary with readout.
        u = ((Q(3, 5), Q(-4, 5)), (Q(4, 5), Q(3, 5)))
        transformed = tuple(tuple(sum(u[k][i]*(k+1)*u[k][j] for k in (0, 1))
                                  for j in (0, 1)) for i in (0, 1))
        for z in (Q(-1), Q(0), Q(1), Q(3, 2), Q(2), Q(7)):
            determinant = ((z-transformed[0][0])*(z-transformed[1][1])
                           - transformed[0][1]*transformed[1][0])
            self.assertEqual(determinant, (z-1)*(z-2))


if __name__ == '__main__':
    unittest.main()
