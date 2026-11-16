"""Exact scoped tests, not an empirical source experiment or universal formal proof."""
import unittest
from fractions import Fraction as Q
from math import gcd
from cmath import pi
from observational_succ.causal_suspension_gamma import (
    lcm_clock, clock_thread, forward_winding, suspension_circle,
    forward_phase, consistent_thread, gamma_latency_moments,
    gamma_laplace_of_forward_clock, gamma_clock_fourier, clock_fourier_limit,
    positive_power_difference, eta_negative_euler, eta_negative_recurrence,
    negative_gamma_distribution_coefficients, negative_gamma_laplace_symbol,
    gamma_inverse_volume_identity, noninteger_crt_thread,
    zeta_negative_euler, prospective_even_zero,
)

class ForwardSuspensionTests(unittest.TestCase):
    def test_known_clocks(self):
        self.assertEqual([lcm_clock(j) for j in range(1,11)],
                         [1,2,6,12,60,60,420,840,2520,2520])

    def test_negative_integer_from_forward_origin(self):
        for m in range(1,20):
            values=forward_winding(m,16)
            self.assertEqual(values,clock_thread(-m,16))
            self.assertTrue(consistent_thread(values))

    def test_seam_orientation(self):
        for L in [2,6,12,60,420]:
            for a in range(L):
                self.assertEqual(suspension_circle(L,a,Q(1)),
                                 suspension_circle(L,(a-1)%L,Q(0)))
            self.assertEqual(forward_phase(L,Q(1)),Q(L-1))

    def test_each_fractional_time_projects_consistently(self):
        for t in (Q(0),Q(1,5),Q(7,3),Q(11,2),Q(89)):
            coords=[forward_phase(lcm_clock(N),t) for N in range(1,17)]
            for N in range(1,16):
                self.assertEqual(coords[N] % lcm_clock(N),coords[N-1])

    def test_no_spurious_positive_ordinary_integer_limit(self):
        # At depth N, -1 has positive representative L_N-1; that
        # representative changes with N: never a fixed natural integer.
        self.assertNotEqual(forward_winding(1,7)[-1],forward_winding(1,8)[-1])

    def test_noninteger_crt_phantom_is_finitely_realized(self):
        xs=noninteger_crt_thread(18)
        self.assertTrue(consistent_thread(xs))
        for n,x in enumerate(xs,1):
            L=lcm_clock(n)
            p2=L & -L
            odd=L//p2
            self.assertEqual(x%odd,0)
            if p2>1:self.assertEqual(x%p2,1)
        # Any fixed ordinary integer cannot equal every CRT coordinate: \n        # vanishing mod unbounded odd powers forces integer=0, but 2-adic parity=1.
        self.assertNotEqual(xs[-1],forward_winding(1,18)[-1])

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):lcm_clock(0)
        with self.assertRaises(ValueError):forward_phase(12,Q(-1,4))
        with self.assertRaises(ValueError):suspension_circle(12,2,Q(4,3))

class GammaCausalVolumeTests(unittest.TestCase):
    def test_exact_moments(self):
        for m in range(1,20):
            for k in (1,2,5,10,30):
                self.assertEqual(gamma_latency_moments(m,k), (Q(m),Q(m,k)))

    def test_laplace_exact(self):
        self.assertEqual(gamma_laplace_of_forward_clock(2,2,Q(1)),Q(16,81))
        for m in range(1,8):
            self.assertEqual(gamma_laplace_of_forward_clock(m,2,Q(0)),1)
            self.assertGreater(gamma_laplace_of_forward_clock(m,4,Q(1)),0)

    def test_fourier_concentrates_to_forward_winding(self):
        for L in (6,12,60):
            for m in (1,2,4):
                errors=[abs(gamma_clock_fourier(m,k,L)-clock_fourier_limit(m,L))
                        for k in (10,40,160)]
                self.assertLess(errors[-1],errors[0])
                self.assertLess(errors[-1],0.16)

    def test_character_power_bonding_not_direct_equality(self):
        for low, high in [(6,12),(12,60),(60,420)]:
            for m in (1,2,4):
                z=clock_fourier_limit(m,high)
                self.assertAlmostEqual(abs(z**(high//low)-clock_fourier_limit(m,low)),0,places=12)

    def test_negative_gamma_is_a_distribution_not_probability(self):
        for m in range(1,12):
            self.assertEqual(negative_gamma_distribution_coefficients(m),
                             tuple(__import__("math").comb(m,j) for j in range(m+1)))
            for p in (Q(0),Q(1,3),Q(1),Q(5)):
                self.assertEqual(gamma_inverse_volume_identity(m,p),1)
            self.assertGreater(negative_gamma_laplace_symbol(m,Q(1)),1)

    def test_gamma_and_deterministic_not_same_at_finite_rate(self):
        self.assertNotAlmostEqual(gamma_clock_fourier(2,5,12),clock_fourier_limit(2,12))

class ZetaForwardDifferenceTests(unittest.TestCase):
    def test_finite_difference_annihilation(self):
        for m in range(0,18):
            for n in range(m+1,m+8):
                self.assertEqual(positive_power_difference(m,n),0)

    def test_eta_two_routes_agree(self):
        for m in range(0,25):
            self.assertEqual(eta_negative_euler(m),eta_negative_recurrence(m))

    def test_trivial_zeros(self):
        for n in range(1,15):
            self.assertTrue(prospective_even_zero(n))
            self.assertEqual(zeta_negative_euler(2*n),0)

    def test_known_zeta_values(self):
        known={0:Q(-1,2),1:Q(-1,12),2:Q(0),3:Q(1,120),4:Q(0),5:Q(-1,252),6:Q(0),7:Q(1,240)}
        for n,ans in known.items():self.assertEqual(zeta_negative_euler(n),ans)

    def test_euler_formula_signs(self):
        self.assertEqual([eta_negative_euler(n) for n in range(6)],
                         [Q(1,2),Q(1,4),Q(0),Q(-1,8),Q(0),Q(1,4)])

    def test_no_unjustified_raw_series(self):
        self.assertNotEqual(sum(n*n for n in range(1,30)),zeta_negative_euler(2))

if __name__ == '__main__':unittest.main(verbosity=2)
