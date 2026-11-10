from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent))
from intervals import SCALE, Interval, phase, contains_rational
from history_certificate import authenticate_history, certificate, sqrt_box
from source import common_history
from observational_succ.selected_orbit import original_forcing


class HistoryCertificateTests(unittest.TestCase):
    def test_source_gate_rejects_seed_mutation_and_wrapping(self):
        states = [Q(0)]
        for n in range(1, 17):
            states.append(16*states[-1]+original_forcing(n))
        self.assertTrue(authenticate_history(states))
        for mutant in ([s % 1 for s in states], [s+16**n*Q(1, 17) for n, s in enumerate(states)],
                       [s+(Q(1, 3) if n == 7 else 0) for n, s in enumerate(states)]):
            with self.assertRaises(ValueError):
                authenticate_history(mutant)

    def test_nonresonant_partition_certifies_zero(self):
        a = [phase(0), phase(0), phase(1, 2), phase(1, 2)]
        b = [phase(0), phase(1, 2), phase(0), phase(1, 2)]
        result = certificate(a, b, [0, 0, 1, 1])
        self.assertLess(result['full_bound_expression'][1], SCALE//10**8)
        self.assertGreater(result['prime_leakage_squared'][0], SCALE-100)
        self.assertGreater(result['complement_residual_squared'][0], SCALE-100)

    def test_coherent_control_stays_large_at_every_refinement(self):
        a = [phase(j, 4) for j in range(4)]
        b = [z.conjugate() for z in a]
        for labels in ([0]*4, [0, 0, 1, 1], list(range(4))):
            result = certificate(a, b, labels)
            self.assertGreater(result['full_bound_expression'][0], SCALE*999//1000)
            self.assertLessEqual(result['full_bound_expression'][0], SCALE)
            self.assertGreaterEqual(result['full_bound_expression'][1], SCALE)

    def test_sqrt_and_domains(self):
        for n in range(21):
            x = Q(n, 7)
            square = Interval.ratio(x.numerator**2, x.denominator**2)
            self.assertTrue(contains_rational(sqrt_box(square), x))
        with self.assertRaises(ValueError):
            sqrt_box(Interval(-1, 2))
        with self.assertRaises(ValueError):
            certificate([], [], [])


if __name__ == '__main__':
    unittest.main()
