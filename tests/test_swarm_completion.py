"""Independent finite-source and infinity-boundary adversarial controls."""
import unittest
from itertools import product
from random import Random
from observational_succ.swarm_completion import (
    CompletionError, PartialEvidence, LassoStream, patch_tail, power_marker_patch,
    finite_refutation_search, verify_refutation, minimum_prefix_generator,
    marker_gap_bound, MooreSource, least_proof_support_stage,
)
from observational_succ.godel_succ import delayed_halt, halted_by, two_counter_loop


def brute_minimum_generator(word):
    """Independent exhaustive stationary transition/output tables, not lassos."""
    if not word:
        return 1
    alphabet = tuple(set(word))
    for n in range(1, len(word)+1):
        for step in product(range(n), repeat=n):
            for reports in product(alphabet, repeat=n):
                state = 0
                for expected in word:
                    if reports[state] != expected:
                        break
                    state = step[state]
                else:
                    return n


def refinement_classes(source):
    """Independent partition refinement, not the pair-BFS implementation."""
    part = tuple(source.outputs)
    while True:
        signatures = tuple((source.outputs[i], tuple(part[source.states.index(t)] for t in row))
                           for i, row in enumerate(source.transitions))
        dictionary = {}
        nxt = tuple(dictionary.setdefault(x, len(dictionary)) for x in signatures)
        equal = all((part[i] == part[j]) == (nxt[i] == nxt[j])
                    for i in range(len(part)) for j in range(len(part)))
        part = nxt
        if equal:
            return {frozenset(s for s, label in zip(source.states, part) if label == k)
                    for k in set(part)}


class CompletionTests(unittest.TestCase):
    def test_partial_evidence_transport_join_and_conflict(self):
        a = PartialEvidence(((0, 1), (3, 0)))
        b = PartialEvidence(((2, 1), (3, 0)))
        merged = a.join(b)
        self.assertTrue(merged.extends(a) and merged.extends(b))
        self.assertEqual(merged.shift(), a.shift().join(b.shift()))
        self.assertFalse(a.extends(b))
        with self.assertRaises(CompletionError):
            a.join(PartialEvidence(((3, 1),)))
        self.assertEqual(a.shift().entries, ((2, 0),))

    def test_same_arbitrary_transcript_opposite_tail_and_periodicity(self):
        rng = Random(14013)
        for _ in range(150):
            indices = sorted(rng.sample(range(250), rng.randrange(25)))
            evidence = PartialEvidence(tuple((n, rng.randrange(2)) for n in indices))
            zero = patch_tail(evidence, (0,))
            ones = patch_tail(evidence, (1,))
            sparse = power_marker_patch(evidence)
            self.assertTrue(all(evidence.agrees(s) for s in (zero, ones, sparse)))
            cutoff = 1+max(indices, default=-1)
            self.assertEqual(zero(cutoff+100), 0)
            self.assertEqual(ones(cutoff+100), 1)
            power = 1 << (cutoff+1).bit_length()
            self.assertGreaterEqual(power, cutoff)
            self.assertEqual(sparse(power), 1)
            self.assertEqual(sparse(power+1), 0)

    def test_effective_refutation_retains_at_most_one_witness_per_state(self):
        states = tuple(range(13))
        trace = lambda s, n: int(n == s*7)
        profile = lambda n: 0
        receipt = finite_refutation_search(states, trace, profile, range(100))
        self.assertEqual(receipt['status'], 'REFUTED')
        self.assertEqual(receipt['inspected_probe_count'], 85)
        self.assertEqual(len(receipt['witnesses']), len(states))
        self.assertTrue(verify_refutation(states, trace, profile, receipt))
        forged = dict(receipt, witnesses=tuple((s, 1) for s in states))
        self.assertFalse(verify_refutation(states, trace, profile, forged))
        unresolved = finite_refutation_search(states, trace, profile, range(80))
        self.assertEqual(unresolved['status'], 'UNRESOLVED')
        self.assertEqual(unresolved['remaining_states'], (12,))

    def test_single_state_halting_reduction_delayed_and_never(self):
        for delay in (0, 1, 7, 55):
            program = (("HALT",),) if delay == 0 else delayed_halt(delay)
            target = lambda n: int(halted_by(program, n))
            result = finite_refutation_search(('s',), lambda s, n: 0, target, range(delay+2))
            self.assertTrue(verify_refutation(('s',), lambda s, n: 0, target, result))
        never = finite_refutation_search(('s',), lambda s, n: 0,
                         lambda n: int(halted_by(two_counter_loop(), n)), range(200))
        self.assertEqual(never['status'], 'UNRESOLVED')

    def test_empty_source_has_empty_refutation(self):
        result = finite_refutation_search((), lambda s, n: 0, lambda n: 0, ())
        self.assertTrue(verify_refutation((), lambda s, n: 0, lambda n: 0, result))

    def test_sharp_finite_prefix_count_exhaustive_binary_sources(self):
        checked = 0
        for length in range(6):
            for word in product((0, 1), repeat=length):
                result = minimum_prefix_generator(word)
                self.assertEqual(result['state_count'], brute_minimum_generator(word), word)
                self.assertEqual(tuple(result['stream'](i) for i in range(length)), word)
                checked += 1
        self.assertEqual(checked, 63)
        self.assertEqual(minimum_prefix_generator((0, 0, 0, 1))['state_count'], 4)
        self.assertEqual(minimum_prefix_generator((0, 1, 0, 1, 0, 1))['state_count'], 2)
        self.assertEqual(minimum_prefix_generator(('a', 'b', 'a', 'b'))['state_count'], 2)

    def test_marker_gap_accepts_nonconstant_interior_and_is_sharp(self):
        word = ('x', 'y', 'x', 'y', 'END')
        receipt = marker_gap_bound(word, 0, 4)
        self.assertEqual(receipt['state_lower_bound'], 5)
        self.assertEqual(minimum_prefix_generator(word)['state_count'], 5)
        with self.assertRaises(CompletionError):
            marker_gap_bound(('x', 'END', 'y', 'END'), 0, 3)

    def test_sparse_nested_and_arbitrary_alphabet_prefixes(self):
        for powers in ((2**k for k in range(7)), (2**(2**k) for k in range(4))):
            markers = tuple(powers)
            word = tuple('M' if n in markers else ('a' if n % 2 else 'b')
                         for n in range(markers[-1]+1))
            for previous, stop in zip(markers, markers[1:]):
                bound = marker_gap_bound(word, previous+1, stop)['state_lower_bound']
                self.assertEqual(bound, stop-previous)
            self.assertGreaterEqual(minimum_prefix_generator(word)['state_count'],
                                    markers[-1]-markers[-2])

    def test_multi_action_final_semantics_vs_independent_refinement(self):
        rng = Random(1513)
        for trial in range(120):
            count = rng.randrange(1, 10)
            states = tuple(range(count))
            source = MooreSource(states, ('L', 'R'), tuple(rng.randrange(3) for _ in states),
                    tuple(tuple(rng.choice(states) for _ in range(2)) for s in states))
            groups = source.behavioral_classes()
            self.assertEqual({frozenset(g) for g in groups}, refinement_classes(source))
            quotient = source.minimal_quotient()
            index = {s: i for i, g in enumerate(groups) for s in g}
            for s in states:
                for length in range(4):
                    for word in product(source.actions, repeat=length):
                        self.assertEqual(source.observe(s, word), quotient.observe(index[s], word))
                for t in states:
                    separator = source.separator(s, t)
                    if separator is not None:
                        self.assertNotEqual(source.observe(s, separator), source.observe(t, separator))

    def test_visible_report_equality_is_not_behavioral_equivalence(self):
        machine = MooreSource((0, 1, 2), ('a',), (0, 0, 1), ((0,), (2,), (2,)))
        self.assertEqual(machine.separator(0, 1), ('a',))
        self.assertEqual(len(machine.behavioral_classes()), 3)

    def test_proof_support_stage_and_omega_rule_boundary(self):
        stages = tuple(frozenset(range(n)) for n in range(8))
        self.assertEqual(least_proof_support_stage((0, 3, 5), stages), 6)
        self.assertIsNone(least_proof_support_stage((100,), stages))
        self.assertEqual(least_proof_support_stage((), stages), 0)
        with self.assertRaises(CompletionError):
            least_proof_support_stage((1,), (frozenset({1}), frozenset()))

    def test_malformed_inputs(self):
        for entries in (((True, 0),), ((2, 0), (1, 0)), ((1, 0), (1, 1))):
            with self.assertRaises(CompletionError):
                PartialEvidence(entries)
        with self.assertRaises(CompletionError):
            LassoStream((), ())
        with self.assertRaises(CompletionError):
            power_marker_patch(PartialEvidence(), default=0, marker=0)
        with self.assertRaises(CompletionError):
            MooreSource((0,), ('a',), (0,), ((9,),))
        with self.assertRaises(CompletionError):
            minimum_prefix_generator([0, 1])


if __name__ == '__main__':
    unittest.main()
