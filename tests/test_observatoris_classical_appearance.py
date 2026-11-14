"""Exact witnesses: classical appearance is a family of independent diagnostics."""
from fractions import Fraction as Q
from itertools import product
import random
import unittest

from observational_succ.carrier_relative_targets import (
    Carrier, Instrument, Target, behavioral_partition, plan_target,
)
from observational_succ.observatoris_classical_appearance import (
    QUBIT_OPERATIONS,
    classical_bit_transcripts,
    classical_four_state_transcripts,
    disturbing_instruments,
    final_readout_marginal,
    future_readouts,
    is_free_observation,
    predictive_ambiguity,
    qubit_transcripts,
    static_partition,
    transcript_is_static,
    window_carrier,
)


def blocks(partition):
    return {frozenset(b) for b in partition}


def random_carrier(rng, size, instruments, outputs):
    return Carrier("random", size, tuple(
        Instrument(f"i{k}", f"chart{k}",
                   tuple(Q(rng.randrange(outputs)) for _ in range(size)),
                   tuple(rng.randrange(size) for _ in range(size)))
        for k in range(instruments)))


class FreeObservation(unittest.TestCase):
    def test_free_observation_makes_behaviour_static(self):
        # CA-1: whenever no instrument disturbs, the behaviour quotient is the
        # joint one-shot readout quotient and transcripts are static.
        rng = random.Random(20261114)
        free = 0
        for _ in range(4000):
            c = random_carrier(rng, rng.randint(1, 4), rng.randint(1, 2), 2)
            if is_free_observation(c):
                free += 1
                self.assertEqual(blocks(behavioral_partition(c)), blocks(static_partition(c)))
                self.assertTrue(transcript_is_static(c, 4))
        self.assertGreater(free, 100)

    def test_free_observation_exhaustive_three_states_one_instrument(self):
        for outputs in product(range(2), repeat=3):
            for nxt in product(range(3), repeat=3):
                c = Carrier("x", 3, (Instrument("a", "A", tuple(Q(v) for v in outputs), nxt),))
                if is_free_observation(c):
                    self.assertEqual(blocks(behavioral_partition(c)),
                                     blocks(static_partition(c)))
                    self.assertTrue(transcript_is_static(c, 5))

    def test_static_behaviour_does_not_imply_free_observation(self):
        # Converse fails: a swap with distinct readouts has discrete static and
        # behaviour partitions, yet every use changes the behaviour class.
        c = Carrier("swap", 2, (Instrument("a", "A", (Q(0), Q(1)), (1, 0)),))
        self.assertEqual(blocks(behavioral_partition(c)), blocks(static_partition(c)))
        self.assertEqual(disturbing_instruments(c), (("a", 0), ("a", 1)))
        self.assertFalse(transcript_is_static(c, 2))

    def test_free_observation_makes_counterfactual_knowledge_executable(self):
        # With free observation one copy suffices: reading every instrument once
        # identifies the behaviour class, hence every identifiable target.
        rng = random.Random(5)
        checked = 0
        for _ in range(3000):
            c = random_carrier(rng, rng.randint(2, 4), 2, 2)
            if not is_free_observation(c):
                continue
            owner = {x: j for j, b in enumerate(behavioral_partition(c)) for x in b}
            target = Target("random", "class", tuple(Q(owner[x]) for x in range(c.size)))
            result = plan_target(c, target, budget=2)
            self.assertIsNotNone(result.policy)
            checked += 1
        self.assertGreater(checked, 50)

    def test_destructive_instruments_break_executability(self):
        # Inherited SUCC control (CARRIER_RELATIVE_TARGETS section 3).
        c = Carrier("abc", 3, (
            Instrument("a", "A", (Q(1), Q(0), Q(0)), (0, 0, 0)),
            Instrument("b", "B", (Q(0), Q(1), Q(0)), (0, 0, 0)),
        ))
        self.assertFalse(is_free_observation(c))
        self.assertEqual(len(behavioral_partition(c)), 3)
        target = Target("abc", "is-C", (Q(0), Q(0), Q(1)))
        self.assertIsNone(plan_target(c, target, budget=6).policy)


class PredictiveHorizon(unittest.TestCase):
    def test_window_shift_is_free_deterministic_and_locally_lawful(self):
        c = window_carrier(4, 2)
        # The readout never disturbs; only the declared dynamics moves the state.
        self.assertEqual({name for name, _ in disturbing_instruments(c)}, {"step"})
        # the all-experiment behaviour quotient is discrete: nothing is hidden forever
        self.assertEqual(len(behavioral_partition(c)), 16)

    def test_prediction_fails_exactly_at_the_resolution(self):
        # Known window of r bits predicts the future window with ambiguity
        # 2**min(r, t): perfect at t = 0, nothing left at t >= r.
        for bits, width in ((4, 1), (4, 2), (3, 1)):
            c = window_carrier(bits, width)
            for t in range(bits - width + 1):
                self.assertEqual(predictive_ambiguity(c, t), 2 ** min(width, t))
        c = window_carrier(4, 2)
        for future in future_readouts(c, 2).values():
            self.assertEqual(future, {Q(0), Q(1), Q(2), Q(3)})


class DeclaredHilbertModel(unittest.TestCase):
    def test_commuting_toolkit_is_a_classical_bit(self):
        # Restricted to X and the Z readout, every transcript of the declared
        # qubit is deterministic and equals the one-bit machine's.
        for length in range(8):
            for word in product(("X", "Z"), repeat=length):
                self.assertEqual(qubit_transcripts(word), classical_bit_transcripts(word))

    def test_z_readout_is_repeatable_on_the_commuting_toolkit(self):
        for word in product(("X", "Z"), repeat=5):
            base = qubit_transcripts(word + ("Z",))
            twice = qubit_transcripts(word + ("Z", "Z"))
            self.assertEqual({k + (k[-1],): p for k, p in base.items()}, twice)

    def test_one_new_instrument_ends_determinism_and_free_observation(self):
        self.assertEqual(qubit_transcripts(("H", "Z")), {(0,): Q(1, 2), (1,): Q(1, 2)})
        # H H is the identity ...
        self.assertEqual(qubit_transcripts(("H", "H", "Z")), {(0,): Q(1)})
        # ... but looking in between changes the later statistics.
        disturbed = final_readout_marginal(qubit_transcripts(("H", "Z", "H", "Z")))
        self.assertEqual(disturbed, {0: Q(1, 2), 1: Q(1, 2)})

    def test_a_classical_stochastic_machine_still_matches_every_transcript(self):
        # Appearance is not ontology in the other direction either: four
        # classical states with a coin reproduce the enlarged toolkit exactly.
        for length in range(7):
            for word in product(QUBIT_OPERATIONS, repeat=length):
                self.assertEqual(qubit_transcripts(word),
                                 classical_four_state_transcripts(word))

    def test_probabilities_are_normalised_exact_rationals(self):
        for word in product(QUBIT_OPERATIONS, repeat=6):
            dist = qubit_transcripts(word)
            self.assertEqual(sum(dist.values()), 1)
            self.assertTrue(all(type(p) is Q and p > 0 for p in dist.values()))

    def test_operations_outside_the_toolkit_are_refused(self):
        with self.assertRaises(ValueError):
            qubit_transcripts(("T",))
        with self.assertRaises(ValueError):
            classical_bit_transcripts(("H",))


if __name__ == "__main__":
    unittest.main()
