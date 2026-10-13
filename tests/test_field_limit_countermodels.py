"""Hostile finite checks for three separately proved infinite-completion results."""
import unittest
from observational_succ.field_limit_countermodels import (
    OMEGA,LimitError,delayed_rival_shadow,omega_rival_at_horizon,
    unrealizable_limit_prefix,halting_reduction_probe,partition_refinement_depth,cantor_real_target_prefix,
)

class LimitBoundaryTests(unittest.TestCase):
    def test_finite_delayed_rival_survives_every_tested_prefix(self):
        for n in range(0,60):
            r=omega_rival_at_horizon(n)
            self.assertEqual(r['rival'],n+1)
            self.assertEqual(r['status'],"FINITE_PREFIX_INSUFFICIENT")
            for k in range(1,n+1):
                self.assertEqual(delayed_rival_shadow(k,OMEGA),
                                 delayed_rival_shadow(k,n+1))

    def test_first_distinguisher_is_an_actual_new_probe(self):
        for k in range(1,35):
            self.assertEqual(delayed_rival_shadow(k,k),1)
            self.assertEqual(delayed_rival_shadow(k,OMEGA),0)

    def test_same_infinite_record_cannot_be_concluded_from_short_prefix(self):
        self.assertEqual(omega_rival_at_horizon(5)['first_distinguishing_probe'],6)

    def test_noncompact_finite_realizability_does_not_imply_global_realization(self):
        for n in range(0,70):
            r=unrealizable_limit_prefix(n)
            self.assertEqual(r['finite_all_zero_history'],(0,)*n)
            self.assertEqual(r['finite_realizing_source'],n+1)
            self.assertFalse(r['infinite_report_realizable'])

    def test_halting_probe_requires_supplied_bounded_halting_evidence(self):
        self.assertEqual(halting_reduction_probe(False,0),0)
        self.assertEqual(halting_reduction_probe(False,1),0)
        self.assertEqual(halting_reduction_probe(True,0),0)
        self.assertEqual(halting_reduction_probe(True,1),1)

    def test_horizon_halting_example_only_becomes_separable_after_actual_halt(self):
        # Known toy execution halts at step 7; no claimed universal decider.
        for stage in range(1,12):
            self.assertEqual(halting_reduction_probe(stage>=7,1),int(stage>=7))

    def test_source_size_bounds_number_of_strict_partition_changes(self):
        for n in range(1,30):
            self.assertTrue(partition_refinement_depth(n,n-1))
            self.assertFalse(partition_refinement_depth(n,n))

    def test_time_of_first_strict_refinement_not_bounded_by_source_size(self):
        # A two-state source can remain aliased for an arbitrarily delayed
        # probe horizon, then split once; N-1 counts splits, not their time.
        n=2
        for delay in (2,10,100,10_000):
            reports=[(0,0)]*(delay-1)+[(0,1)]
            self.assertEqual(sum(pair!=(0,0) for pair in reports),1)
            self.assertTrue(partition_refinement_depth(n,1))

    def test_compact_cantor_source_has_omega_real_target_but_finite_error(self):
        from fractions import Fraction
        for n in range(1,45):
            report=cantor_real_target_prefix(n)
            self.assertEqual(report['max_tail_span'],Fraction(1,2**n))
            self.assertEqual(report['same_prefix_target_gap_witness'],Fraction(1,2**(n+1)))
            self.assertEqual(report['status'],"FINITE_APPROXIMATION_NOT_EXACT_IDENTIFICATION")
        with self.assertRaises(LimitError):cantor_real_target_prefix(-1)

    def test_no_bad_source_or_probe_numbers_are_silently_coerced(self):
        with self.assertRaises(LimitError): delayed_rival_shadow(0,OMEGA)
        with self.assertRaises(LimitError): delayed_rival_shadow(1,0)
        with self.assertRaises(LimitError): omega_rival_at_horizon(-1)
        with self.assertRaises(LimitError): unrealizable_limit_prefix(-1)
        with self.assertRaises(LimitError): halting_reduction_probe(True,2)

    def test_closed_unobservable_target_is_not_equal_to_no_source_realization(self):
        a=omega_rival_at_horizon(20)
        b=unrealizable_limit_prefix(20)
        self.assertEqual(a['rival'],21)
        self.assertEqual(b['finite_realizing_source'],21)
        self.assertNotIn('infinite_report_realizable',a)
        self.assertFalse(b['infinite_report_realizable'])

if __name__=='__main__':unittest.main()
