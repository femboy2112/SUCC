"""Hostile exact tests for proposed empirical-carrier SUCC interface.

All test sources are stipulated finite mathematical worlds. No collision data,
no real detector response, no experimental QFT reconstruction is claimed.
"""

import itertools
import math
import unittest
from fractions import Fraction as Q

from observational_succ.empirical_carrier import (
    CarrierEvidenceError, HiggsChannel, RateFactorization,
    angular_even_moment, audit_higgs_scale, calibrated_angular_dimension,
    compatible_angular_carriers, effective_angular_dimension,
    finite_euler_coefficients, gaussian_radial_mellin, gram_example,
    gram_positive_definite, local_shell_factor, phase_gauge,
    quantum_rate_signature, quantum_triangle_phase, rate_reparameterize,
    normalized_archimedean_mellin,
)


def h(name, sector, mass, vertex, *, source='calibration-A', epoch=2):
    return HiggsChannel(name,sector,Q(mass),Q(vertex),source,epoch)


class HiggsCrossSectorCalibration(unittest.TestCase):
    def test_independent_fermion_vector_v_agreement(self):
        channels=(h('f','fermion',3,Q(1,4)),h('V','vector',6,6),
                  h('g','fermion',2,Q(1,6)))
        result=audit_higgs_scale(channels)
        self.assertEqual(result.scales,(Q(12),)*3)
        self.assertTrue(result.compatible)
        self.assertTrue(result.cross_sector)
        self.assertFalse(result.empirical_measurement_claimed)

    def test_anomalous_vector_coupling_exposes_cross_sector_conflict(self):
        result=audit_higgs_scale((h('f','fermion',3,Q(1,4)),h('V','vector',6,8)))
        self.assertFalse(result.compatible)
        self.assertEqual(result.scales,(Q(12), Q(9)))
        self.assertEqual(result.first_conflict,('f','V'))

    def test_one_channel_fits_every_positive_v_by_choice_of_vertex(self):
        # No model selection possible from mass alone: full finite counterfamily.
        mass=Q(3)
        for v in range(2,31):
            self.assertEqual(h('f','fermion',mass,mass/Q(v)).inferred_vev,Q(v))

    def test_wrong_epoch_and_source_cannot_be_compared(self):
        a=h('f','fermion',3,Q(1,4))
        for b in (h('V','vector',6,6,epoch=3),h('V','vector',6,6,source='another')):
            with self.assertRaises(CarrierEvidenceError):
                audit_higgs_scale((a,b))

    def test_scheme_float_and_invalid_vertex_are_rejected(self):
        with self.assertRaises(CarrierEvidenceError):
            h('V','vector',6,0)
        with self.assertRaises(CarrierEvidenceError):
            HiggsChannel('f','fermion',3,0.25,'s',0)
        with self.assertRaises(CarrierEvidenceError):
            HiggsChannel('f','fermion',Q(3),Q(1,4),'s',0,'renormalized-one-loop')


class GeometryAcceptanceIdentifiability(unittest.TestCase):
    def test_isotropic_second_and_fourth_moments(self):
        self.assertEqual(angular_even_moment(3,1),Q(1,3))
        self.assertEqual(angular_even_moment(3,2),Q(1,5))
        self.assertEqual(angular_even_moment(5,1),Q(1,5))
        self.assertEqual(angular_even_moment(5,2),Q(3,35))

    def test_complete_angular_distribution_alias_in_every_checked_moment(self):
        # Analytic theorem: A(u)=(1-u^2) for 3D isotropy produces 5D isotropy.
        # Unit test checks exact moments; full density identity is proved in note.
        eff=effective_angular_dimension(3,1)
        self.assertEqual(eff,5)
        # Independent elementary integral of u^(2j) (1-u^2) du on [-1,1].
        for order in range(0,16):
            actual_from_three_dimensions = Q(3,(2*order+1)*(2*order+3))
            self.assertEqual(actual_from_three_dimensions,angular_even_moment(eff,order))

    def test_aliased_dimension_with_calibration(self):
        candidates=compatible_angular_carriers(Q(1,5))
        self.assertEqual(candidates,((5,0),(3,1)))
        self.assertEqual(calibrated_angular_dimension(Q(1,5),1),3)
        self.assertEqual(calibrated_angular_dimension(Q(1,5),0),5)
        with self.assertRaises(CarrierEvidenceError):
            calibrated_angular_dimension(Q(1,5),2)

    def test_general_integer_power_gauge_all_small_dimensions(self):
        for d,k,j in itertools.product(range(2,9),range(4),range(8)):
            eff=effective_angular_dimension(d,k)
            self.assertIn((d,k),compatible_angular_carriers(angular_even_moment(eff,1)))
            self.assertEqual(calibrated_angular_dimension(angular_even_moment(eff,1),k),d)
            self.assertEqual(angular_even_moment(eff,j),
                             angular_even_moment(d+2*k,j))

    def test_independent_odd_dimensional_polynomial_integral(self):
        # When d is odd, true isotropic angular density times (1-u^2)^k
        # is a POLYNOMIAL. Integrate the polynomial, not the beta recurrence.
        for d,k,j in itertools.product((3,5,7),range(4),range(8)):
            power=(d-3)//2+k
            def integral(n):
                return sum((Q((-1)**r*math.comb(power,r)*2,2*n+2*r+1)
                            for r in range(power+1)),Q(0))
            independent = integral(j)/integral(0)
            self.assertEqual(independent, angular_even_moment(d+2*k,j))

    def test_acceptance_and_dimension_mutants(self):
        with self.assertRaises(CarrierEvidenceError):
            effective_angular_dimension(3,-1)
        with self.assertRaises(CarrierEvidenceError):
            angular_even_moment(1,1)
        self.assertEqual(compatible_angular_carriers(Q(2,7)),())


class RateGeometryAndQuantumPhase(unittest.TestCase):
    def test_rate_gauge_preserves_every_source_observation(self):
        source=RateFactorization((Q(1),Q(2),Q(3)),
                                 (Q(2),Q(3),Q(4)),
                                 (Q(1),Q(1,2),Q(1,4)))
        mutant=rate_reparameterize(source,(Q(2),Q(1,3),Q(7,2)))
        self.assertEqual(source.observations,mutant.observations)
        self.assertNotEqual(source.phase_space,mutant.phase_space)
        self.assertNotEqual(source.amplitude_sq,mutant.amplitude_sq)
        self.assertEqual(source.observations,(Q(2),Q(3),Q(3)))

    def test_detector_acceptance_must_be_physical(self):
        with self.assertRaises(CarrierEvidenceError):
            RateFactorization((Q(1),),(Q(1),),(Q(2),))

    def test_same_pairwise_quantum_rates_different_cycle_sign(self):
        kplus,kminus=gram_example(1),gram_example(-1)
        self.assertTrue(gram_positive_definite(kplus))
        self.assertTrue(gram_positive_definite(kminus))
        self.assertEqual(quantum_rate_signature(kplus),quantum_rate_signature(kminus))
        self.assertEqual(quantum_rate_signature(kplus),(Q(1,16),)*3)
        self.assertEqual(quantum_triangle_phase(kplus),Q(1,64))
        self.assertEqual(quantum_triangle_phase(kminus),Q(-1,64))
        # Since triple products are gauge invariant, no unitary preserving the
        # labeled rays can identify the two triples via individual phases.

    def test_phase_gauge_sweep_and_mutant(self):
        k=gram_example(-1)
        for signs in itertools.product((-1,1),repeat=3):
            changed=phase_gauge(k,signs)
            self.assertTrue(gram_positive_definite(changed))
            self.assertEqual(quantum_rate_signature(changed),quantum_rate_signature(k))
            self.assertEqual(quantum_triangle_phase(changed),quantum_triangle_phase(k))
        non_psd=((Q(1),Q(2),Q(0)),(Q(2),Q(1),Q(0)),(Q(0),Q(0),Q(1)))
        self.assertFalse(gram_positive_definite(non_psd))

    def test_independent_principal_minor_oracle(self):
        for sign in (-1,1):
            k=gram_example(sign)
            # Separate expansion of 3x3 determinant by permutation formula.
            det=sum(((-1)**(sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))) *
                     math.prod(k[i][p[i]] for i in range(3)) for p in itertools.permutations(range(3))),Q(0))
            self.assertGreater(det,0)
            self.assertEqual(det,Q(27,32) if sign==1 else Q(25,32))


class ArithmeticSourceVersusContinuum(unittest.TestCase):
    def test_prime_shell_geometric_identity(self):
        for p,s,depth in itertools.product((2,3,5,7),(1,2,3),(0,1,2,4,7)):
            partial=local_shell_factor(p,s,depth)
            limit=local_shell_factor(p,s)
            self.assertEqual(limit-partial,Q(1,p**((depth+1)*s))*limit)
            self.assertGreater(limit,partial)

    def test_fake_composite_has_no_qp_place(self):
        with self.assertRaises(CarrierEvidenceError):
            local_shell_factor(6,2)
        self.assertEqual(local_shell_factor(6,2,prime_required=False),Q(36,35))
        with self.assertRaises(CarrierEvidenceError):
            finite_euler_coefficients((2,3,6),24)

    def test_fake_euler_overcounts_six_source(self):
        good=finite_euler_coefficients((2,3),36)
        bad=finite_euler_coefficients((2,3,6),36,enforce_primes=False)
        self.assertEqual(good[6],1)
        self.assertEqual(bad[6],2)
        self.assertEqual(good[36],1)
        self.assertEqual(bad[36],3)
        self.assertEqual(good[1],bad[1])

    def test_archimedean_gamma_dimensional_normalization(self):
        # The proof is the polar-coordinate integral in the research dossier;
        # tests are numeric diagnostics, not analytic continuation certificates.
        for d in range(1,9):
            for s in (0.5,1.0,2.0,3.0,4.0):
                target=math.pi**(-s/2)*math.gamma(s/2)
                self.assertAlmostEqual(normalized_archimedean_mellin(d,s),target,places=12)
        self.assertAlmostEqual(normalized_archimedean_mellin(3,2),1/math.pi,places=12)
        self.assertAlmostEqual(normalized_archimedean_mellin(3,3),1/(2*math.pi),places=12)

    def test_gaussian_real_radial_normalization(self):
        for d in range(1,9):
            self.assertAlmostEqual(gaussian_radial_mellin(d,float(d)),1,places=12)
        self.assertAlmostEqual(gaussian_radial_mellin(1,2),1/math.pi,places=12)
        self.assertAlmostEqual(gaussian_radial_mellin(2,4),1/math.pi,places=12)


if __name__=='__main__':
    unittest.main()
