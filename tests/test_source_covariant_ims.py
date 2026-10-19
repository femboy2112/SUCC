"""Exact toy-algebra controls plus authentic-source clock gates.

The finite model is not a discretized Suzuki positivity certificate.  The
universal continuum theorems are proved in the mathematical dossier.
"""
import sys
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.source_covariant_ims import (
    FiniteToySource, LocalizationError, finite_ims, prime_power_parent,
    affine_succ_fucc_square, gamma_prefix_multiplier, first_legendre_prime_overlap,
    first_prime_window_frequency_packet, authenticated_first_prime_window_packet,
)


def model():
    n = 6
    jump = tuple(tuple(F(0) if i == j else F(1, 1 + abs(i - j))
                       for j in range(n)) for i in range(n))
    return FiniteToySource(jump,((1,F(2,3)),(3,F(4,5))),F(3,2),
                           (F(1),F(2),F(3),F(1),F(2),F(3)),
                           (F(0),F(1),F(-1),F(0),F(2),F(1)))


def charts():
    pairs = ((F(3,5),F(4,5)),(F(4,5),F(3,5)),
             (F(1),F(0)),(F(0),F(1)),(F(-3,5),F(4,5)),(F(4,5),F(-3,5)))
    return tuple(tuple(p[i] for p in pairs) for i in (0,1))


class ExactSignedLocalization(unittest.TestCase):
    def test_full_original_channel_analogue(self):
        for vals in ((2,-1,3,0,2,-2),(1,1,1,1,1,1),(-2,3,0,4,-1,1),
                     (0,0,0,0,0,0)):
            with self.subTest(values=vals):
                receipt = finite_ims(model(),tuple(F(v) for v in vals), charts())
                self.assertEqual(receipt['actual'],receipt['reconstructed'])
                self.assertTrue(receipt['contact_cancels_exactly'])
                self.assertFalse(receipt['original_Suzuki_source_authenticated'])
                self.assertFalse(receipt['RH_proved'])

    def test_prime_and_gamma_interfaces_need_not_have_fixed_sign(self):
        signs_gamma=set(); signs_prime=set()
        for vv in ((1,)*6,(-1,1,-1,1,-1,1),
                   (1,-1,0,0,0,0),(1,1,0,0,0,0)):
            r=finite_ims(model(),vv,charts())
            signs_gamma.add((r['Gamma_interface']>0)-(r['Gamma_interface']<0))
            signs_prime.add((r['prime_interface']>0)-(r['prime_interface']<0))
        self.assertIn(1,signs_gamma)
        self.assertIn(-1,signs_gamma)
        self.assertIn(1,signs_prime)
        self.assertIn(-1,signs_prime)

    def test_missing_polar_reassembly_breaks_signed_identity(self):
        f=(F(1),F(2),F(-1),F(1),F(0),F(3))
        r=finite_ims(model(),f,charts())
        self.assertNotEqual(r['polar_reassembly'],0)
        self.assertNotEqual(r['local_total']-r['Gamma_interface']-r['prime_interface'],r['actual'])

    def test_counterexample_no_automatic_nonzero_prime_correlation(self):
        only_far_lag=FiniteToySource(model().jump, ((4,F(1)),), F(0),
                                      tuple(F(0) for _ in range(6)),
                                      tuple(F(0) for _ in range(6)))
        f=(F(2),F(-3),F(0),F(0),F(0),F(0))
        self.assertEqual(only_far_lag.components(f)['prime_shift'],0)
        self.assertGreater(only_far_lag.components(f)['Gamma_jump'],0)

    def test_discrete_FUCC_jump_positive_and_compensation_is_exact(self):
        for f in ((1,1,1,1,1,1),(1,-1,1,-1,1,-1),(0,0,1,0,0,0)):
            r=model().components(tuple(F(z) for z in f))
            self.assertGreaterEqual(r['positive_FUCC_jump'],0)
            self.assertEqual(r['prime_shift'],r['positive_FUCC_jump']
                            +r['compensating_negative_FUCC_potential'])
            self.assertEqual(r['total'],r['positive_Gamma_FUCC_transport']
                            +r['signed_contact_and_FUCC_potential']
                            +r['completed_polar'])

    def test_zero_prime_overlap_still_has_compensating_jump(self):
        only_far_lag=FiniteToySource(model().jump, ((4,F(1)),), F(0),
                                      tuple(F(0) for _ in range(6)),
                                      tuple(F(0) for _ in range(6)))
        f=(F(2),F(-3),F(0),F(0),F(0),F(0))
        r=only_far_lag.components(f)
        self.assertEqual(r['prime_shift'],0)
        self.assertEqual(r['positive_FUCC_jump'],26)
        self.assertEqual(r['compensating_negative_FUCC_potential'],-26)

    def test_one_shift_transparent_chart_not_simultaneously_transparent(self):
        # Finite graph model: a genuinely different second shift creates an
        # interface on a chart that exactly commutes with the first shift.
        n=6
        source=FiniteToySource(model().jump, ((2,F(1)),(3,F(1))), F(0),
            tuple(F(0) for _ in range(n)), tuple(F(0) for _ in range(n)))
        c1=tuple(F(3,5) if i%2==0 else F(4,5) for i in range(n))
        c2=tuple(F(4,5) if i%2==0 else F(3,5) for i in range(n))
        f=(F(1),)*n
        merged=finite_ims(source,f,(c1,c2))
        self.assertGreater(merged['prime_interface'],0)  # only shift 3 pays
        source2=FiniteToySource(model().jump, ((2,F(1)),), F(0),
            tuple(F(0) for _ in range(n)), tuple(F(0) for _ in range(n)))
        self.assertEqual(finite_ims(source2,f,(c1,c2))['prime_interface'],0)

    def test_forged_partition_not_normalized(self):
        bad=((F(1),)*6,(F(1),)*6)
        with self.assertRaises(LocalizationError):finite_ims(model(),(1,)*6,bad)

    def test_wrong_frozen_source_not_automatically_certified(self):
        with self.assertRaises(LocalizationError):FiniteToySource(((F(0),F(-2)),(F(-2),F(0))),(),F(1),(F(1),F(1)),(F(0),F(0)))
        with self.assertRaises(LocalizationError):FiniteToySource(((F(0),F(1)),(F(2),F(0))),(),F(1),(F(1),F(1)),(F(0),F(0)))
        with self.assertRaises(LocalizationError):FiniteToySource(((F(0),F(1)),(F(1),F(0))),((1,F(-1)),),F(1),(F(1),F(1)),(F(0),F(0)))

    def test_floats_bool_and_wrong_dimensions_rejected(self):
        with self.assertRaises(LocalizationError):finite_ims(model(),(F(1),)*5, charts())
        with self.assertRaises(LocalizationError):finite_ims(model(),(True,)*6, charts())
        with self.assertRaises(LocalizationError):finite_ims(model(),(0.0,)*6, charts())

    def test_phase_differences_for_two_incommensurable_log_primes(self):
        self.assertNotEqual(2**3,3**2)
        self.assertEqual(prime_power_parent(2),2)
        self.assertEqual(prime_power_parent(4),2)
        self.assertEqual(prime_power_parent(8),2)
        self.assertEqual(prime_power_parent(9),3)
        self.assertIsNone(prime_power_parent(6))
        with self.assertRaises(LocalizationError):prime_power_parent(1)

    def test_succ_fucc_affine_square_and_ghost_prime(self):
        for n in range(1,11):
            for p in (2,3,5,7):
                result=affine_succ_fucc_square(n,p)
                self.assertEqual(result['Vp_after_S'],result['Sp_after_Vp'])
                self.assertFalse(result['Hilbert_space_unitary_equivalence_claimed'])
        with self.assertRaises(LocalizationError):affine_succ_fucc_square(1,6)

    def test_gamma_multiplier_rational_prefix(self):
        for x in (F(1),F(5),F(9),F(20),F(41),F(101),F(101,2)):
            r=gamma_prefix_multiplier(x)
            self.assertGreaterEqual(r['partial_multiplier'],r['rational_harmonic_lower'])
            self.assertFalse(r['global_source_multiplier_certified'])

    def test_gamma_multiplier_explicit_budget(self):
        with self.assertRaises(LocalizationError):gamma_prefix_multiplier(F(0))
        with self.assertRaises(LocalizationError):gamma_prefix_multiplier(F(20000))

    def test_polynomial_prime_hinge_exact_lag_closed_formula(self):
        for b in (F(1,5),F(1,2),F(7,10),F(9,10)):
            calc=first_legendre_prime_overlap(F(1,2),b)
            want=-(1-b)**3 * (1+3*b+b*b) / 15
            self.assertEqual(calc['hinge_energy_per_unit_weight'],want)
            self.assertLess(want,0)
        with self.assertRaises(LocalizationError):
            first_legendre_prime_overlap(F(1,2),F(1))

    def test_actual_original_legendre_polynomial_if_installed(self):
        try:
            from observational_succ.suzuki_legendre_source import prime_hinge_integral_polynomial
        except ModuleNotFoundError as exc:
            self.skipTest('isolated toy missing original Legendre source: '+str(exc))
        poly=prime_hinge_integral_polynomial(1,1,F(1,2))
        for b in (F(1,5),F(1,2),F(7,10),F(9,10)):
            actual=sum((coefficient*b**k for k,coefficient in enumerate(poly)),F())
            self.assertEqual(actual,first_legendre_prime_overlap(F(1,2),b)['hinge_energy_per_unit_weight'])

    def test_first_window_finite_negative_witness_band_budget(self):
        d=first_prime_window_frequency_packet()
        self.assertEqual(d['band_radius'],2**24)
        self.assertEqual(d['Fourier_midpoint_sample_count'],2**49)
        self.assertEqual(d['negative_source_budget_upper'],'103/16')
        self.assertEqual(d['negative_direction_low_band_mass_fraction_strict_lower'],'1/2')
        self.assertFalse(d['negative_original_direction_exhibited'])

    def test_authentic_source_contract_if_installed(self):
        try:
            r=authenticated_first_prime_window_packet()
        except ModuleNotFoundError as e:
            self.skipTest('isolated toy checkout lacks frozen original SUCC: '+str(e))
        self.assertTrue(r['source_gate_verified'])
        self.assertEqual(r['genuine_wavefront'],((2,2),))
        self.assertEqual(r['pinned_source_blob'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')


if __name__=='__main__':unittest.main()
