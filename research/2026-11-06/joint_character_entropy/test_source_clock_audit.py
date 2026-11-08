"""Exact controls for the preregistered coefficient-sensitive BBP clock."""
import unittest
from fractions import Fraction
from joint_entropy import four_pole,mealy_run,decode_reversible_observer
from source_clock_audit import (coefficient_clock,index_clock,mutant_clock,
    denominator,numerator,mutant_numerator,verified_source_clock)

class SourceClockAuditTests(unittest.TestCase):
    def test_exact_full_signed_source_clearing(self):
        self.assertTrue(verified_source_clock())
        for n in (1,2,7,23,107,1007):
            self.assertEqual(denominator(n)*four_pole(n),numerator(n))
    def test_clock_is_source_coefficient_sensitive_but_not_unique(self):
        self.assertNotEqual([coefficient_clock(i) for i in range(7)],
                            [index_clock(i) for i in range(7)])
        self.assertNotEqual([coefficient_clock(i) for i in range(7)],
                            [mutant_clock(i) for i in range(7)])
        for n in range(77):
            self.assertEqual(coefficient_clock(n+7),coefficient_clock(n))
            self.assertEqual(mutant_clock(n+7),mutant_clock(n))
        for n in (1,2,31):
            self.assertEqual(mutant_numerator(n),
                denominator(n)*(four_pole(n)+Fraction(1,8*n-7)))
    def test_reversible_audit_and_wrong_clock_control(self):
        d=(0,1,15,6,2,10,7,4,14,12,3,5,11,8,9,13)*4
        original=tuple(coefficient_clock(i) for i in range(len(d)))
        mutant=tuple(mutant_clock(i) for i in range(len(d)))
        encoded,_=mealy_run(d,original)
        self.assertEqual(decode_reversible_observer(encoded,original),d)
        self.assertNotEqual(decode_reversible_observer(encoded,mutant),d)
    def test_source_label_domain(self):
        for bad in (0,-1,1.5):
            with self.assertRaises(ValueError):denominator(bad)
        for bad in (-1,0.5):
            with self.assertRaises(ValueError):coefficient_clock(bad)

if __name__=="__main__":unittest.main()
