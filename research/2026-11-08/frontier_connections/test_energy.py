import unittest
from energy_oracle import critical_check, debruijn, normal_control, source_energy


class ReplicaEnergyTests(unittest.TestCase):
    def test_stationary_families(self):
        for b in range(2, 34, 2):
            self.assertEqual(len(critical_check(b)['exact_minimizers_turns']), 2)

    def test_parity_hypothesis(self):
        for b in (0, 1, 3, 15):
            with self.assertRaises(ValueError):
                critical_check(b)

    def test_euler_word_coverage_and_temporal_repeat(self):
        self.assertGreater(normal_control()['exact_word_counts_checked'], 4000)

    def test_actual_source_energy(self):
        self.assertEqual(len(source_energy()['rows']), 8)

    def test_invalid_word_model(self):
        for b,k in ((1,1),(2,0)):
            with self.assertRaises(ValueError):
                debruijn(b,k)


if __name__ == '__main__':
    unittest.main()
