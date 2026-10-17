"""Hostile finite controls and exact source-constant inequalities for first-prime compensation."""
import unittest
from fractions import Fraction as F
from observational_succ.gamma_edge_compensation import (
    CompensationError, harmonic_gamma_lower, proof_by_exact_harmonic_arithmetic,
    true_first_edge_packet, rational_source_constant_control,
    gamma_logarithmic_edge_lower, resolution_cost_bound,
    buffered_edge_bulk_gluing, source_authenticated_compensation,
    signed_two_port_bound, countermodel_gluing,
)
from observational_succ.prime_hinge_chiral_edge import (
    EdgeHinge, high_moment_chiral_certificate,
)


class RationalGammaEdgeTests(unittest.TestCase):
    def test_rational_source_constants_no_float(self):
        d=rational_source_constant_control()
        self.assertTrue(d['strictly_below_47_over_8'])
        self.assertLess(d['combined_upper'],F(47,8))
        self.assertLess(d['log2'][1],F(7,10))
        self.assertGreater(d['weight2'][0],0)
        self.assertLess(d['weight2'][1],F(1,2))
        self.assertLess(d['contact'][1]-d['contact'][0],F(1,10**9))

    def test_exact_partial_sum(self):
        d=proof_by_exact_harmonic_arithmetic()
        self.assertGreater(d['true_gamma_partial_sum'],F(223,32))
        self.assertGreater(d['uniform_K_margin_lower'],F(11,128))
        self.assertEqual(d['modal_terms'],16)

    def test_at_width_extremum(self):
        bound=true_first_edge_packet(F(1,32))
        self.assertGreater(bound['total_K_relative_lower'],F(11,128))
        self.assertTrue(bound['uniform_11_over_128_if_16_modes'])
        self.assertFalse(bound['source_checked'])

    def test_all_certified_widths(self):
        for n in range(5,30):
            d=F(1,2**n)
            z=true_first_edge_packet(d)
            self.assertGreater(z['total_K_relative_lower'],F(11,128))
            self.assertGreater(harmonic_gamma_lower(16,2*d),0)

    def test_boundary_and_wrong_sources_denied(self):
        for delta in (F(0),F(-1,128),F(1,31),F(1),False,.001):
            with self.subTest(delta=repr(delta)),self.assertRaises(CompensationError):
                true_first_edge_packet(delta)
        for terms in (0,True,-1,10001,2.1):
            with self.subTest(terms=terms),self.assertRaises(CompensationError):
                harmonic_gamma_lower(terms,F(1,16))

    def test_separated_original_chiral_shock(self):
        hinge=EdgeHinge(F(1,2),F(3,4),F(1))
        for m in range(0,9):
            for sign in (-1,1):
                c=high_moment_chiral_certificate(hinge,m,sign=sign)
                self.assertEqual(c['sharp_ratio'],-sign)
                self.assertEqual(c['gradient_to_K_cost'],F(2*(2*m+1)*(2*m+5),hinge.width**2))

    def test_mixed_source_not_diagonal_votes(self):
        self.assertEqual(signed_two_port_bound(1,1,1,1)['edge_energy'],-2)
        self.assertEqual(signed_two_port_bound(1,1,-1,1)['edge_energy'],2)
        for a,b,q in ((1,1,2),(-1,1,0),(1,0,1)):
            with self.assertRaises(CompensationError):signed_two_port_bound(a,b,q,1)

    def test_bulk_coercivity_missing_is_a_real_debt(self):
        p=buffered_edge_bulk_gluing(F(1,4096),F(1,16),F(1,4),F(1))
        self.assertFalse(p['bulk_source_coercivity_authenticated'])
        self.assertFalse(p['RH_proved'])
        self.assertGreater(p['mixed_cross_coefficient_squared_upper'],0)
        self.assertEqual(countermodel_gluing()['negative_joint_energy'],-2)

    def test_buffer_gap_and_budget_reject(self):
        for args in ((F(1,32),0,F(1,4),F(1)),
                     (F(1,32),F(1,100),F(1,1),F(1)),
                     (F(1,31),F(1,16),F(1,4),F(1)),
                     (F(1,64),F(1,16),F(1,4),F(-1)),
                     (F(1,64),F(1,16),F(1,4),False)):
            with self.subTest(args=args), self.assertRaises(CompensationError):
                buffered_edge_bulk_gluing(*args)

    def test_logarithmic_gamma_growth(self):
        prev=F(-1)
        for ell in (F(1,8),F(1,16),F(1,32),F(1,64),F(1,128),F(1,256)):
            x=gamma_logarithmic_edge_lower(ell)
            self.assertGreater(x['whole_gamma_K_lower'],prev)
            prev=x['whole_gamma_K_lower']
            self.assertGreaterEqual(x['exact_used_rung_lower'],prev)
        with self.assertRaises(CompensationError):gamma_logarithmic_edge_lower(F(1,4))

    def test_gradient_and_nonphysical_energy(self):
        for d in (F(1,32),F(1,64),F(1,256)):
            p=resolution_cost_bound(d)
            self.assertGreater(p['specific_four_moment_witness_squared_ratio'],p['strict_squared_L2_to_K_lower'])
            self.assertFalse(p['source_l2_bandwidth_claim'])

    def test_true_repository_source_gate(self):
        try:
            import observational_succ.source_weil_hierarchy  # noqa
            import observational_succ.tate_suzuki_shorting  # noqa
        except ImportError:
            self.skipTest('full original SUCC source module absent in isolated test fixture')
        certificate=source_authenticated_compensation()
        self.assertTrue(certificate['source_checked'])
        self.assertGreater(certificate['total_K_relative_lower'],F(11,128))
        self.assertFalse(certificate['all_high_space_coercivity_proved'])
        self.assertFalse(certificate['RH_proved'])


if __name__ == '__main__':unittest.main()
