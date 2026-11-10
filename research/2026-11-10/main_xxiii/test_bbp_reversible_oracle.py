from dataclasses import replace
from fractions import Fraction
from random import Random
import unittest

from bbp_reversible_oracle import build_oracle


def direct_source(j):
    return (
        Fraction(4, 8 * j + 1) - Fraction(2, 8 * j + 4)
        - Fraction(1, 8 * j + 5) - Fraction(1, 8 * j + 6)
    )


class ReversibleCarryTest(unittest.TestCase):
    def check_seed(self, oracle, seed):
        initial = oracle.encode_seed(seed)
        result = oracle.simulate(initial)
        self.assertEqual(oracle.simulate(result, inverse=True), initial)
        value = seed
        integral = value.numerator // value.denominator
        for j, (next_integer, residue, carry) in enumerate(oracle.decode_history(result)):
            value = 16 * value + direct_source(j)
            self.assertEqual(Fraction(next_integer) + Fraction(residue, oracle.denominator), value)
            self.assertTrue(0 <= residue < oracle.denominator)
            self.assertTrue(0 <= carry <= 19)
            self.assertEqual(next_integer - 16 * integral, carry)
            integral = next_integer
        return result

    def test_exhaustive_short_seed_lattice(self):
        oracle = build_oracle(1)
        for numerator in range(-oracle.denominator, oracle.denominator):
            self.check_seed(oracle, Fraction(numerator, oracle.denominator))

    def test_source_prefix_and_coherent_control(self):
        rng = Random(5280)
        for length in (2, 6, 11, 24):
            oracle = build_oracle(length)
            prefix = sum(direct_source(j) / 16 ** (j + 1) for j in range(length))
            seeds = (Fraction(0), -prefix, Fraction(-1), Fraction(1, 16))
            heldout = Fraction(rng.randrange(-oracle.denominator, oracle.denominator), oracle.denominator)
            for seed in (*seeds, heldout):
                result = self.check_seed(oracle, seed)
                for n in (0, 1, length):
                    self.assertEqual(oracle.completed_phase(result, n), 16 ** n * (seed + prefix))

    def test_a_mutant_can_still_reverse_but_fails_the_source_check(self):
        oracle = build_oracle(2)
        gate_to_remove = next(i for i, gate in enumerate(oracle.gates) if len(gate) == 1)
        mutant = replace(oracle, gates=oracle.gates[:gate_to_remove] + oracle.gates[gate_to_remove + 1:])
        initial = mutant.encode_seed(Fraction(0))
        output = mutant.simulate(initial)
        self.assertEqual(mutant.simulate(output, inverse=True), initial)
        self.assertNotEqual(mutant.completed_phase(output, 0), sum(direct_source(j) / 16 ** (j + 1) for j in range(2)))

    def test_resource_and_distinct_wire_contract(self):
        for length in (1, 6, 24):
            oracle = build_oracle(length)
            bits = oracle.denominator.bit_length()
            width = bits + 6
            self.assertEqual(oracle.qubits, 1 + bits + length * (17 * width + 5))
            self.assertTrue(all(len(set(gate)) == len(gate) for gate in oracle.gates))
            counts = oracle.gate_counts()
            self.assertLessEqual(counts["Toffoli"], 16 * width * length)
            self.assertLessEqual(counts["CNOT"], (29 * width + 5) * length)
            self.assertLessEqual(counts["X"], (6 * width + 5) * length)


if __name__ == "__main__":
    unittest.main()
