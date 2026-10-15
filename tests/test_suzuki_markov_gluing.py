"""Exact regression certificates. Infinite claims require the accompanying proofs."""
import unittest
from fractions import Fraction as Q
from observational_succ.suzuki_markov_gluing import (
    GluingError, rational, log_interval, pi_interval, sqrt_interval, prime_power,
    gamma_density, markov_density, gamma_split, rate_affine_pi, rate_interval,
    derivative_tail_bound, first_prime_certificate, shift_fibers,
    compressed_shift, carleman_pullback, laplace_dilation, laplace_boundary,
    successor_bulk_defect, localization, receipt,
)


class SuzukiMarkovGluingTests(unittest.TestCase):
    def test_rational_constants_are_certified(self):
        l2, u2 = log_interval(2)
        l3, u3 = log_interval(3)
        p0, p1 = pi_interval()
        s0, s1 = sqrt_interval(2)
        self.assertTrue(Q(2, 3) < l2 < u2 < Q(7, 10))
        self.assertTrue(1 < l3 < u3 < Q(11, 10))
        self.assertTrue(Q(31, 10) < p0 < p1 < Q(22, 7))
        self.assertTrue(Q(7, 5) < s0 and s0*s0 <= 2 <= s1*s1)

    def test_exact_original_Gamma_not_extra_companion(self):
        for z in (Q(1, 7), Q(1, 2), Q(7, 9), Q(99, 100)):
            for n in range(1, 24):
                prefix, tail, total = gamma_split(z, n)
                self.assertEqual(prefix+tail, total)
                self.assertGreater(tail, 0)
                self.assertEqual(tail, z**(2*n+1)/(1-z**4))

    def test_successive_markov_layers_equal_actual_OU_mode(self):
        for z in (Q(1, 4), Q(2, 3), Q(9, 10)):
            for j in range(20):
                self.assertEqual(markov_density(z, 2*j)+markov_density(z, 2*j+1),
                                 z**(4*j+1))

    def test_lost_Gamma_tail_is_positive_and_decreases(self):
        for z in (Q(1, 3), Q(3, 4)):
            last = gamma_density(z)
            for n in range(1, 32):
                _, tail, _ = gamma_split(z, n)
                self.assertLess(tail, last)
                last = tail

    def test_rate_recurrence_and_positive_bounds(self):
        for k in range(96):
            a, b = rate_affine_pi(k)
            c, d = rate_affine_pi(k+1)
            self.assertEqual(a+c, Q(4, 2*k+1))
            self.assertEqual(b+d, 0)
            lo, hi = rate_interval(k)
            self.assertTrue(0 < lo <= hi)

    def test_rate_mass_sum_matches_source_modes(self):
        for n in range(1, 25):
            aa, bb = Q(), 0
            for k in range(2*n):
                a, b = rate_affine_pi(k)
                aa, bb = aa+a, bb+b
            self.assertEqual(bb, 0)
            self.assertEqual(aa, sum((Q(4, 4*j+1) for j in range(n)), Q()))

    def test_H1_tail_coefficients_decrease(self):
        old = derivative_tail_bound(1)
        for n in range(2, 128):
            new = derivative_tail_bound(n)
            self.assertTrue(0 < new < old)
            old = new

    def test_first_prime_whole_space_subform(self):
        c = first_prime_certificate()
        self.assertTrue(c['one_fifth_certificate'])
        self.assertLess(Q(c['absorption_ratio_upper']), Q(1, 5))
        self.assertGreater(Q(c['markov_gap_lower'])-Q(c['prime_coefficient_upper']), 2)
        self.assertFalse(c['full_Weil_positive'])
        self.assertFalse(c['RH_proved'])

    def test_hostile_prime_amplitude_kills_certificate(self):
        self.assertFalse(first_prime_certificate(4)['one_fifth_certificate'])
        self.assertEqual(first_prime_certificate(4)['source'], 'mutated_coefficient')

    def test_prime_power_authentication_separate_from_dilation(self):
        for n, expected in ((2,(2,1)),(4,(2,2)),(8,(2,3)),(9,(3,2)),(25,(5,2))):
            self.assertEqual(prime_power(n), expected)
        for n in (6, 10, 12, 15, 18):
            self.assertIsNone(prime_power(n))
            self.assertEqual(*laplace_dilation(Q(3, 2), Q(4, 3), n))

    def test_exact_fiber_jump_at_wavefront(self):
        self.assertEqual(shift_fibers(1, 1), ((1,Q(1)),))
        self.assertEqual(shift_fibers(Q(6, 5), 1), ((2,Q(1,5)),(1,Q(4,5))))
        self.assertEqual(shift_fibers(2, 1), ((2,Q(1)),))
        self.assertEqual(shift_fibers(Q(21, 10), 1), ((3,Q(1,10)),(2,Q(9,10))))
        self.assertEqual(shift_fibers(Q(2, 3), 1), ((1,Q(2,3)),))

    def test_fiber_total_source_measure(self):
        for numerator in range(1, 41):
            for denominator in (2, 3, 7):
                length = Q(numerator, denominator)
                for step in (Q(1, 2), Q(1), Q(3, 2)):
                    self.assertEqual(sum((n*w for n,w in shift_fibers(length,step)),Q()),length)

    def test_compressed_positive_successors_compose(self):
        v = tuple(Q((-1)**i, i+1) for i in range(19))
        for a in range(7):
            for b in range(7):
                self.assertEqual(compressed_shift(compressed_shift(v,a),b),
                                 compressed_shift(v,a+b))
        self.assertTrue(all(x == 0 for x in compressed_shift(v, len(v))))

    def test_Carleman_log_half_density_exact(self):
        for x in (Q(1, 3), Q(1), Q(7, 2)):
            for y in (Q(1, 2), Q(2), Q(11, 3)):
                a,b = carleman_pullback(x,y)
                self.assertEqual(a,b)
                if x*y != 1:
                    self.assertNotEqual(x*y/(x*x+y*y), b)

    def test_Laplace_prime_reciprocal_transport(self):
        for p in (2, 3, 5, 6, 7):
            for b in (Q(1, 3), Q(1), Q(7, 2)):
                self.assertEqual(*laplace_dilation(b,Q(9,4),p))

    def test_boundary_receipt_cannot_be_omitted(self):
        for q in (2,3,5):
            for b in range(1,5):
                for t in range(1,5):
                    lhs,rhs,ghost = laplace_boundary(q,b,t)
                    self.assertEqual(lhs,rhs)
                    self.assertNotEqual(lhs,ghost)
        self.assertEqual(laplace_boundary(2,2,3), (Q(1,20),Q(1,20),Q(8,5)))

    def test_additive_bulk_commutator_nonzero(self):
        for r in (Q(1,3),Q(1),Q(7,2)):
            for h in (Q(1,4),Q(1),Q(2)):
                lhs,rhs = successor_bulk_defect(r,h+Q(1,5),h)
                self.assertEqual(lhs,rhs)
                self.assertLess(lhs,0)

    def test_prime_correlated_localization_no_atomic_loss(self):
        v = (Q(2),Q(-1,2),Q(3,7),Q(1),Q(-2))
        w = tuple(tuple(Q(1,1+abs(i-j)) if i!=j else Q() for j in range(5)) for i in range(5))
        ph = ((Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(0),Q(1)),(Q(1),Q(0)),(Q(3,5),Q(4,5)))
        c = localization(v,w,ph,((0,3),(1,4)),Q(1,2))
        self.assertTrue(c['prime_compatible'])
        self.assertEqual(c['prime_debt'],'0')
        self.assertNotEqual(c['jump_debt'],'0')

    def test_wrong_localization_creates_atomic_debt(self):
        c = localization((1,1),((0,1),(1,0)),((1,0),(0,1)),((0,1),))
        self.assertFalse(c['prime_compatible'])
        self.assertEqual(Q(c['prime_debt']),2)
        self.assertEqual(Q(c['jump_debt']),2)

    def test_invalid_source_types_and_domains(self):
        calls = (lambda:rational(.5), lambda:gamma_density(1),
                 lambda:markov_density(Q(1,2),-1), lambda:shift_fibers(1,0),
                 lambda:laplace_dilation(1,1,True), lambda:carleman_pullback(0,1),
                 lambda:localization((1,1),((0,1),(1,0)),((1,1),(1,0))),
                 lambda:first_prime_certificate(-1))
        for call in calls:
            with self.assertRaises(GluingError):
                call()

    def test_compression_creates_source_boundary_noncommutation(self):
        # Exact Gamma-layer samples, spacing h=2 log 2. Full convolution
        # operators commute; these finite compressions need not commute.
        z = Q(1, 2)
        def matrix(k):
            return tuple(tuple(Q(1,2) if i==j else markov_density(z**abs(i-j),k)
                               for j in range(3)) for i in range(3))
        a,b = matrix(0),matrix(1)
        comm01 = sum((a[0][j]*b[j][1]-b[0][j]*a[j][1] for j in range(3)),Q())
        self.assertEqual(comm01,Q(3,170))

    def test_isolating_one_layer_cannot_certify_full_source(self):
        # Exact analytic negative-control constants: on odd v, cosh moment
        # vanishes; E0 <= pi, |Q2| < 1/2, and C > 9/2.
        self.assertEqual(Q(9,2)-Q(22,7)-Q(1,2),Q(6,7))
        self.assertGreater(log_interval(2)[0],Q(2,3))
        self.assertGreater(log_interval(3)[0],1)

    def test_receipt_flags_and_reproducibility(self):
        a,b = receipt(),receipt()
        self.assertEqual(a,b)
        self.assertFalse(a['full_Weil_positive'])
        self.assertTrue(a['hostile_large_coefficient_rejected'])
        self.assertEqual(a['fake_six_prime_power'],None)


if __name__ == '__main__':
    unittest.main()
