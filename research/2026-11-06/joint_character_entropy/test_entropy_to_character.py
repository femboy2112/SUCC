"""Scope-controlled numerical tests of J19; not rigorous entropy intervals."""
import unittest
from joint_entropy import certified_source_digits,pole_clock,mealy_run
from entropy_to_character import source_clock_character_bound
from signed_certificate import source_completed_samples,certified_weyl

class SignedEntropyBridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw,_=certified_source_digits(917)
        clock=[pole_clock(n,7) for n in range(917)]
        cls.output,_=mealy_run(raw,clock)

    def test_original_selected_epochs_respect_the_finite_bridge(self):
        for A in (223,457):
            signed=certified_weyl(source_completed_samples(A),1)
            for k,L in ((1,1),(1,3),(2,4),(2,8)):
                out=self.output[A:2*A+k-1]
                row=source_clock_character_bound(out,k=k,L=L,h=1)
                self.assertEqual(row['A'],A)
                self.assertGreaterEqual(row['rhs_diagnostic']+1e-9,float(signed['upper']))

    def test_current_observer_entropy_gate_is_vacuous_at_finite_epochs(self):
        # Failed would be the interesting outcome. We report these honest results.
        for A in (223,457):
            for k,L in ((1,1),(1,3),(2,4),(2,8)):
                out=self.output[A:2*A+k-1]
                row=source_clock_character_bound(out,k=k,L=L,h=1)
                self.assertFalse(row['nonvacuous_below_one'])

    def test_invalid_frequency_and_divisibility_are_rejected(self):
        with self.assertRaises(ValueError):
            source_clock_character_bound((1,2,3),k=1,L=2,h=16)
        with self.assertRaises(ValueError):
            source_clock_character_bound((1,2,3),k=2,L=3,h=1)

if __name__=='__main__':
    unittest.main(verbosity=2)
