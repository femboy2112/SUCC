"""Source-relative virtual/offline zeros; no canonical zeta-zero claims."""
import unittest
from fractions import Fraction as F
from observational_succ.diagonal_adele_zeta import DiagonalSourceError
from observational_succ.virtual_mellin_zeros import (
    mellin_factor_integer, epsilon_from_mellin2, zero_class,
    model_completion_receipt, VirtualCompletionObserver,
    virtual_zero_parameter_threshold_report,
)


class VirtualMellinZeroTests(unittest.TestCase):
    def test_normalized_source_pole_residues_for_every_model(self):
        for e in (F(0),F(1,10),F(4,5),F(10,11),F(1),F(7,5),F(50)):
            self.assertEqual(mellin_factor_integer(e,0),1)
            self.assertEqual(mellin_factor_integer(e,1),1)
            for s in range(-5,6):
                self.assertEqual(mellin_factor_integer(e,s),
                                 mellin_factor_integer(e,1-s))

    def test_exact_prior_DZ9_quadratic_recovered(self):
        r=model_completion_receipt(F(10,11))
        self.assertEqual(r['quadratic_t_constant_first'],(F(1),F(11,5),F(1)))
        self.assertEqual(r['zero_classification'],
                         'EXTRA_OFFLINE_ZEROS_INSIDE_OPEN_CRITICAL_STRIP')
        self.assertFalse(r['actual_Riemann_zeta_modified'])

    def test_all_zero_location_regimes_exact(self):
        cases={
            F(0):'CANONICAL_MULTIPLIER_NO_ZEROS',
            F(1,10):'EXTRA_ZEROS_OUTSIDE_CLOSED_CRITICAL_STRIP',
            F(4,5):'EXTRA_ZEROS_ON_CRITICAL_STRIP_BOUNDARY',
            F(10,11):'EXTRA_OFFLINE_ZEROS_INSIDE_OPEN_CRITICAL_STRIP',
            F(1):'EXTRA_DOUBLE_ZEROS_ON_CRITICAL_LINE',
            F(2):'EXTRA_ZEROS_ON_CRITICAL_LINE',
        }
        for k,v in cases.items():
            self.assertEqual(zero_class(k),v)

    def test_strip_triangle_exact_threshold(self):
        for e in (F(1,100),F(1,2),F(799,1000)):
            v=virtual_zero_parameter_threshold_report(e)
            self.assertTrue(v['proves_no_C_zeros_in_closed_strip_by_triangle'])
            self.assertLess(v['strict_stripsup_bound'],1)
        self.assertFalse(virtual_zero_parameter_threshold_report(F(4,5))['proves_no_C_zeros_in_closed_strip_by_triangle'])
        self.assertFalse(virtual_zero_parameter_threshold_report(F(10,11))['proves_no_C_zeros_in_closed_strip_by_triangle'])

    def test_virtual_zero_exists_under_incomplete_observer_signature(self):
        e=VirtualCompletionObserver(F(0),F(1),'true finite Euler+unknown arch')
        r=e.classify()
        self.assertTrue(r['offcritical_strip_zero_possible_in_a_completion'])
        self.assertFalse(r['offcritical_strip_zero_forced_in_every_completion'])
        self.assertTrue(r['canonical_completion_still_possible'])
        self.assertFalse(r['canonical_zeta_offcritical_zero_claimed'])

    def test_source_resolution_eliminates_virtual_zero_by_one_exact_probe(self):
        e=VirtualCompletionObserver(F(0),F(1),'same source',3)
        next_e=e.observe_exact_mellin2(F(1),source_id='same source',source_version=3)
        self.assertEqual(next_e.lower,0)
        self.assertEqual(next_e.upper,0)
        self.assertFalse(next_e.classify()['offcritical_strip_zero_possible_in_a_completion'])
        self.assertEqual(next_e.source_version,4)

    def test_source_resolution_can_select_a_noncanonical_model(self):
        e=VirtualCompletionObserver(F(0),F(1),'source')
        selected=e.observe_exact_mellin2(mellin_factor_integer(F(10,11),2),
                                         source_id='source',source_version=0)
        self.assertEqual(selected.lower,F(10,11))
        self.assertTrue(selected.classify()['offcritical_strip_zero_forced_in_every_completion'])
        self.assertFalse(selected.classify()['canonical_completion_still_possible'])

    def test_single_second_mellin_probe_identifies_parameter(self):
        for d in range(1,30):
            for j in range(0,8):
                e=F(j,d)
                m=mellin_factor_integer(e,2)
                self.assertEqual(epsilon_from_mellin2(m),e)

    def test_approximant_zero_escape_and_Hurwitz_nonpersistence(self):
        for e in (F(1,3),F(1,10),F(1,1000)):
            a=virtual_zero_parameter_threshold_report(e)
            self.assertTrue(a['compact_convergence_to_one_as_e_to_zero'])
            self.assertTrue(a['no_C_zeros_persist_on_any_fixed_compact_in_limit'])
            self.assertFalse(a['RH_or_zero_free_statement_about_xi'])

    def test_forged_and_stale_evidence_rejected(self):
        o=VirtualCompletionObserver(F(0),F(1),'real place',2)
        m=mellin_factor_integer(F(1,2),2)
        with self.assertRaises(DiagonalSourceError):
            o.observe_exact_mellin2(m,source_id='false place',source_version=2)
        with self.assertRaises(DiagonalSourceError):
            o.observe_exact_mellin2(m,source_id='real place',source_version=1)
        with self.assertRaises(DiagonalSourceError):
            o.observe_exact_mellin2(F(13,4),source_id='real place',source_version=2)
        with self.assertRaises(DiagonalSourceError):
            o.observe_exact_mellin2(F(4),source_id='real place',source_version=2)
        with self.assertRaises(DiagonalSourceError):
            o.observe_exact_mellin2(F(5,2),source_id='real place',source_version=2)

    def test_inconsistent_source_priors_rejected(self):
        with self.assertRaises(DiagonalSourceError):
            VirtualCompletionObserver(F(1),F(0),'source')
        with self.assertRaises(DiagonalSourceError):
            VirtualCompletionObserver(F(-1),F(0),'source')
        with self.assertRaises(DiagonalSourceError):
            zero_class(F(-1))
        with self.assertRaises(DiagonalSourceError):
            mellin_factor_integer(0.5,2)

    def test_critical_strip_virtual_test_fails_to_choose_zeta(self):
        a=model_completion_receipt(F(0))
        b=model_completion_receipt(F(10,11))
        keys=['source_positive_Schwartz','source_normalized_at_zero',
              'source_Fourier_self_dual_analytically','finite_Euler_factors_unchanged',
              'functional_equation_symmetry','Mellin_C0','Mellin_C1']
        self.assertEqual(tuple(a[k] for k in keys), tuple(b[k] for k in keys))
        self.assertNotEqual(a['Mellin_C2'],b['Mellin_C2'])
        self.assertNotEqual(a['zero_classification'],b['zero_classification'])

if __name__=='__main__':
    unittest.main()

class PositiveMixtureRigidityTests(unittest.TestCase):
    def test_finite_positive_mixture_has_nonnegative_mellin2_gap(self):
        from observational_succ.virtual_mellin_zeros import positive_gaussian_mixture_mellin2
        for r in (F(1,4), F(1,2), F(1), F(2), F(4)):
            a=positive_gaussian_mixture_mellin2(((r,1),))
            self.assertEqual(a['nonnegative_rigidity_gap'],(r-1)**2/r)
            self.assertEqual(a['Mellin2'],r+1/r-1)
            self.assertEqual(a['unique_canonical_G1_in_declared_mixture_class'],r==1)

    def test_mellin2_equal_one_forces_all_positive_components_canonical(self):
        from observational_succ.virtual_mellin_zeros import positive_gaussian_mixture_mellin2
        good=positive_gaussian_mixture_mellin2(((1,F(7,9)),(1,F(2,9)),(2,0)))
        self.assertEqual(good['Mellin2'],1)
        self.assertTrue(good['unique_canonical_G1_in_declared_mixture_class'])
        for w in (F(1,100),F(1,2),F(10)):
            bad=positive_gaussian_mixture_mellin2(((1,1),(2,w),(F(1,2),F(1,7))))
            self.assertGreater(bad['Mellin2'],1)
            self.assertFalse(bad['full_Schwartz_class_uniqueness_claimed'])

    def test_negative_mixture_weights_rejected(self):
        from observational_succ.virtual_mellin_zeros import positive_gaussian_mixture_mellin2
        with self.assertRaises(DiagonalSourceError):
            positive_gaussian_mixture_mellin2(((2,-1),(1,2)))
        with self.assertRaises(DiagonalSourceError):
            positive_gaussian_mixture_mellin2(((1,0),))
        with self.assertRaises(DiagonalSourceError):
            positive_gaussian_mixture_mellin2(((0,1),))
