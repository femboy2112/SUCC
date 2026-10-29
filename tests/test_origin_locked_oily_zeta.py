"""Exact origin/frame/source countermodels and Oily two-mode arithmetic tests."""
import cmath
import unittest
from fractions import Fraction as F
from math import log, sin
from observational_succ.origin_locked_oily_zeta import (
    oily_rates, oily_packet, upper_two_mode, transfer_source_response,
    symmetric_character, frame_transform, readout, anchored_gauge_lower_shear,
    is_anchored_upper_labeled, origin_fiber, divisors,divisor_multiplicity,
    fiber_dimension_by_prime, prime_exponents,
    conditional_imbalance_variance_coefficients,
    conditional_imbalance_variance_numeric, prime_split_even_moment,
    conditional_path_character_numeric, exact_source_gibbs_marginal,
    exact_source_gibbs_pair_mass, exact_two_mode_pair_mass,
    prime_local_oily_coefficient,
    counterfeit_character_same_source_different_coupling,
    naive_prime_one_channel_fidelity_squared,naive_prime_compressed_shift_sq,
    cumulative_prime_recoherence_fidelity_squared,harmonic_recoherence_budget,
)
from observational_succ.zeta_wavefront_regeneration import check_beta


class OriginLockedOilyZetaTests(unittest.TestCase):
    def test_oily_authentic_exact_source_packets(self):
        for x in (F(0),F(1,4),F(2,3),F(7,8),F(1)):
            u,v=oily_rates(x)
            self.assertEqual(u+v,x)
            for j in range(20):
                expected=(1-x)*sum((u**k*v**(j-k) for k in range(j+1)),F(0))/4
                self.assertEqual(oily_packet(x,j),expected)

    def test_lorentz_null_coordinates_from_source(self):
        for x in (F(1,64),F(1,8),F(1,3),F(1)):
            u,v=oily_rates(x)
            self.assertEqual((u-v)/(u+v),1-x)
            self.assertEqual((u+v)**2-(u-v)**2,4*u*v)

    def test_oily_critical_jordan_and_prime_two_factor(self):
        u,v=oily_rates(F(1))
        self.assertEqual((u,v),(F(1,2),F(1,2)))
        for j in range(30):
            expected=F(j+1,2**j)
            self.assertEqual(transfer_source_response(u,v,j),expected)
            self.assertEqual(prime_local_oily_coefficient(2,1,j),expected)
            self.assertEqual(expected/4,F(j+1,2**(j+2)))
        with self.assertRaises(ValueError):check_beta(1) # locally valid, globally nonnormalizable

    def test_exact_marked_source_is_not_just_the_character(self):
        for u,v in ((F(1,4),F(1,3)),(F(1,2),F(1,2)),(F(1,4),F(1,2))):
            for j in range(9):
                character,a,b=counterfeit_character_same_source_different_coupling(u,v,j)
                self.assertEqual(character,a)
                self.assertEqual(b,0)
                self.assertNotEqual(a,b)
                self.assertEqual(transfer_source_response(u,v,j,F(3,2)),a*F(3,2))

    def test_source_frame_conjugation_all_three_maps(self):
        G=((F(2),F(3)),(F(1),F(4)))
        origin=(F(0),F(1)); read=(F(1),F(0))
        for u,v in ((F(1,2),F(1,2)),(F(1,3),F(1,4))):
            M=upper_two_mode(u,v)
            m,b,ell=frame_transform(M,origin,read,G)
            for k in range(1,15):
                self.assertEqual(readout(M,origin,read,k),readout(m,b,ell,k))
            # This test rejects the common mistake: changing M alone without b,ell.
            self.assertNotEqual(readout(M,origin,read,1),readout(m,origin,read,1))

    def test_fully_marked_anchored_form_has_no_unpaid_gauge(self):
        u,v=F(1,2),F(1,2)
        M=upper_two_mode(u,v)
        b=(F(0),F(1));ell=(F(1),F(0))
        for c in (F(-3),F(-1),F(0),F(2),F(7,3)):
            G=anchored_gauge_lower_shear(c)
            m,bb,ll=frame_transform(M,b,ell,G)
            self.assertEqual(bb,b)
            self.assertEqual(ll,ell)
            self.assertEqual(is_anchored_upper_labeled(m,u,v),c==0)

    def test_divisor_fibers_exact(self):
        values={1:1,2:2,3:2,4:3,6:4,12:6,36:9,60:12,72:12,120:16}
        for n,d in values.items():
            self.assertEqual(len(origin_fiber(n)),d)
            self.assertEqual(fiber_dimension_by_prime(n),d)
            self.assertEqual(set(divisors(n)),{a for a,b in origin_fiber(n)})
            self.assertTrue(all(a*b==n for a,b in origin_fiber(n)))
            self.assertEqual(origin_fiber(n),tuple(reversed([(b,a) for a,b in origin_fiber(n)])))

    def test_prime_successor_is_not_a_fiber_unitary(self):
        self.assertEqual(divisor_multiplicity(1),1)
        self.assertEqual(divisor_multiplicity(2),2)
        self.assertEqual(divisor_multiplicity(4),3)
        self.assertEqual(divisor_multiplicity(8),4)
        self.assertEqual(divisor_multiplicity(6),4)
        self.assertEqual(divisor_multiplicity(12),6)
        for n in range(1,48):
            for p in (2,3,5):
                j=dict(prime_exponents(n)).get(p,0)
                self.assertEqual(F(divisor_multiplicity(n*p),divisor_multiplicity(n)),F(j+2,j+1))

    def test_uniform_fiber_second_moment_exact(self):
        for j in range(0,43):
            self.assertEqual(F(prime_split_even_moment(j),j+1),F(j*(j+2),3))
        self.assertEqual(conditional_imbalance_variance_coefficients(1),{})
        self.assertEqual(conditional_imbalance_variance_coefficients(12),{2:F(8,3),3:F(1)})
        self.assertEqual(conditional_imbalance_variance_coefficients(36),{2:F(8,3),3:F(8,3)})

    def test_conditional_finite_phase_factors_and_variance(self):
        for n in (1,2,4,6,12,36,80,120):
            for t in (0.0,0.0125,0.1,0.33):
                z=conditional_path_character_numeric(n,t)
                self.assertLessEqual(abs(z),1.000000000001)
                prod=complex(1)
                for p,j in prime_exponents(n):
                    zvar=t*log(p)
                    val=sin((j+1)*zvar)/((j+1)*sin(zvar)) if abs(zvar)>1e-12 else 1.0
                    prod*=val
                self.assertAlmostEqual(z.real,prod.real,places=11)
                self.assertAlmostEqual(z.imag,0.0,places=11)
            if n>1:
                h=1e-4
                approx=(2-2*conditional_path_character_numeric(n,h).real)/(h*h)
                self.assertAlmostEqual(approx,conditional_imbalance_variance_numeric(n),delta=1e-4)

    def test_anchor_isometry_marginals_do_not_double_count(self):
        for cutoff in (6,12,24):
            for n in range(1,cutoff+1):
                expected=exact_source_gibbs_marginal(n,2,cutoff)
                source_total=sum((exact_source_gibbs_pair_mass(a,b,2,cutoff) for a,b in origin_fiber(n)),F(0))
                self.assertEqual(source_total,expected)
            self.assertEqual(sum((exact_source_gibbs_pair_mass(a,b,2,cutoff)
                                  for n in range(1,cutoff+1) for a,b in origin_fiber(n)),F(0)),1)

    def test_double_mode_field_has_different_source_marginal(self):
        n=4; cutoff=16
        source=sum((exact_source_gibbs_pair_mass(a,b,2,cutoff) for a,b in origin_fiber(n)),F(0))
        double=sum((exact_two_mode_pair_mass(a,b,2,cutoff) for a,b in origin_fiber(n)),F(0))
        self.assertNotEqual(source,double)
        self.assertEqual(source/exact_source_gibbs_pair_mass(1,4,2,cutoff),3)
        self.assertEqual(double/exact_two_mode_pair_mass(1,4,2,cutoff),3)
        self.assertEqual(exact_source_gibbs_pair_mass(1,4,2,cutoff),source/3)

    def test_p_fixed_source_phase_character_requires_correct_kernels(self):
        self.assertAlmostEqual(conditional_path_character_numeric(2,1.5).real,
                               __import__('math').cos(1.5*log(2)),places=13)
        self.assertEqual(conditional_path_character_numeric(1,1.234),1+0j)

    def test_sharp_fiber_recoherence_fidelity(self):
        for n in range(1,81):
            for p in (2,3,5,7):
                observed=naive_prime_one_channel_fidelity_squared(n,p)
                self.assertEqual(observed,F(divisor_multiplicity(n),divisor_multiplicity(n*p)))
                self.assertEqual(observed,naive_prime_compressed_shift_sq(n,p))
                self.assertTrue(F(0)<observed<F(1))
        self.assertEqual(naive_prime_one_channel_fidelity_squared(1,2),F(1,2))

    def test_oscillator_prime_depth_telescopes_and_gamma_defect(self):
        from math import log
        import mpmath as mp
        mp.mp.dps=40
        for j in range(50):
            self.assertEqual(cumulative_prime_recoherence_fidelity_squared(2,j),F(1,j+1))
            self.assertEqual(cumulative_prime_recoherence_fidelity_squared(3,j),F(1,j+1))
            if j>=1:
                delta=float(harmonic_recoherence_budget(j))-log(j+1)
                self.assertGreater(delta,0)
        for j in (10,100,1000,10000):
            gamma_defect=float(harmonic_recoherence_budget(j))-log(j+1)
            self.assertGreater(0.57721567,gamma_defect)
        self.assertAlmostEqual(float(harmonic_recoherence_budget(10000))-log(10001),float(mp.euler),delta=0.000051)

    def test_source_nonconstant_recoherence_gain(self):
        self.assertEqual(naive_prime_compressed_shift_sq(1,2),F(1,2))
        self.assertEqual(naive_prime_compressed_shift_sq(2,2),F(2,3))
        self.assertNotEqual(naive_prime_compressed_shift_sq(1,2),naive_prime_compressed_shift_sq(2,2))
        with self.assertRaises(ValueError):naive_prime_one_channel_fidelity_squared(6,4)

    def test_negative_inputs_rejected(self):
        for val in (0,-1,1.3):
            with self.assertRaises((TypeError,ValueError)):origin_fiber(val)
        with self.assertRaises(ValueError):transfer_source_response(F(1,3),F(1,4),-1)
        with self.assertRaises(ValueError):prime_local_oily_coefficient(4,1,3)
        with self.assertRaises(ValueError):prime_local_oily_coefficient(2,0,3)
        with self.assertRaises(ValueError):frame_transform(upper_two_mode(F(1,2),F(1,2)),
                                                          (F(0),F(1)),(F(1),F(0)),
                                                          ((F(1),F(2)),(F(2),F(4))))


if __name__=='__main__':unittest.main()
