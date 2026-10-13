"""Independent finite oracles and hostile source-map controls."""
import itertools
import unittest

from observational_succ.self_anchor_gauge import (
    CandidateWorld, SourceGaugeError, adaptive_gauge_shadow, decoder_audit, diagnose_signature, equality_signature,
    minimal_calibrations, permutation_worlds, sensor_transport,
    transported_change,
)


def independent_decoder_exists(worlds, anchors):
    """Separate brute-force candidate-decoder enumeration, not a fiber test."""
    cases = []
    for w in worlds:
        for i in range(len(w.states)):
            cases.append(((w.reports[i], *(w.references[j] for j in anchors)), w.targets[i]))
    keys = tuple(dict.fromkeys(k for k, _ in cases))
    output_alphabet = tuple(dict.fromkeys(t for _, t in cases))
    return any(all(dict(zip(keys, guessed))[k] == t for k, t in cases)
               for guessed in itertools.product(output_alphabet, repeat=len(keys)))


class TestCrossWorldSourceMap(unittest.TestCase):
    def test_per_source_success_does_not_give_cross_world_decoder(self):
        worlds = permutation_worlds(2)
        self.assertTrue(all(decoder_audit([w]).sufficient for w in worlds))
        result = decoder_audit(worlds)
        self.assertFalse(result.sufficient)
        self.assertIsNotNone(result.witness)
        a, b = result.witness
        self.assertEqual(a.report, b.report)
        self.assertNotEqual(a.target, b.target)
        self.assertEqual(minimal_calibrations(worlds), ((0,), (1,)))
        self.assertTrue(decoder_audit(worlds, (0,)).sufficient)

    def test_full_symmetric_groups_have_exact_n_minus_one_calibration_cost(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                worlds = permutation_worlds(n)
                minima = minimal_calibrations(worlds)
                self.assertEqual({len(m) for m in minima}, {max(0, n-1)})
                self.assertEqual(set(minima), set(itertools.combinations(range(n), max(0, n-1))))
                for anchors in itertools.combinations(range(n), max(0, n-2)):
                    if n >= 2:
                        self.assertFalse(decoder_audit(worlds, anchors).sufficient)

    def test_exhaustive_independent_decoder_enumeration(self):
        p = permutation_worlds(2)
        families = ((p[0],), p, (p[1],))
        for worlds in families:
            for anchors in ((), (0,), (1,), (0, 1)):
                self.assertEqual(decoder_audit(worlds, anchors).sufficient,
                                 independent_decoder_exists(worlds, anchors))

    def test_reference_calibration_is_not_source_state_observation(self):
        # A reference is a separately prepared *known* state (under an explicit
        # stable-map hypothesis), not an illicit query for the unknown source.
        worlds = permutation_worlds(3)
        a = decoder_audit(worlds, (0, 1))
        self.assertTrue(a.sufficient)
        for w in worlds:
            for state in range(3):
                report = (w.reports[state], w.references[0], w.references[1])
                self.assertEqual(a.decoder[report], state)

    def test_source_drift_defeats_all_previous_reference_calibration(self):
        # Equal marginal sensor alphabets do not license the *joint* same-map
        # constraint. Old and new dictionaries can change independently.
        perms = tuple(itertools.permutations(range(2)))
        worlds = tuple(CandidateWorld(
            name=f"old={p},new={q}", source_id="drifting", target_epoch=1,
            states=(0, 1), reports=q, targets=(0, 1), references=p,
            reference_epoch=0) for p in perms for q in perms)
        self.assertFalse(decoder_audit(worlds, (0, 1)).sufficient)
        self.assertEqual(minimal_calibrations(worlds), ())
        self.assertTrue(all(decoder_audit([w]).sufficient for w in worlds))

    def test_noninjective_readout_cannot_be_repaired_by_dictionary_calibration(self):
        # Even an exactly known map cannot restore information erased by q.
        w = CandidateWorld('collapse', 'src', 1, (0, 1), (0, 0), (0, 1), (0, 1))
        self.assertFalse(decoder_audit([w], (0, 1)).sufficient)
        self.assertEqual(minimal_calibrations([w]), ())

    def test_reject_mixed_sources_epochs_reference_bases_and_malformed_anchors(self):
        w = permutation_worlds(2)[0]
        kwargs = dict(name='other', source_id='other-source', target_epoch=1,
                      states=(0, 1), reports=(0, 1), targets=(0, 1), references=(0, 1))
        with self.assertRaises(SourceGaugeError):
            decoder_audit([w, CandidateWorld(**kwargs)])
        kwargs['source_id'] = w.source_id
        kwargs['target_epoch'] = 2
        with self.assertRaises(SourceGaugeError):
            decoder_audit([w, CandidateWorld(**kwargs)])
        kwargs['target_epoch'] = 1
        kwargs['reference_epoch'] = 1
        with self.assertRaises(SourceGaugeError):
            decoder_audit([w, CandidateWorld(**kwargs)])
        for anchors in ((0, 0), (2,), (-1,), (True,), (1, 0)):
            with self.subTest(anchors=anchors), self.assertRaises(SourceGaugeError):
                decoder_audit([w], anchors)
        with self.assertRaises(SourceGaugeError):
            CandidateWorld('bad', 'src', 1, (0, 0), (0, 1), (0, 1), (0, 1))
        with self.assertRaises(SourceGaugeError):
            decoder_audit([])


class TestSelfRelativeGaugeInvariants(unittest.TestCase):
    def test_equality_signature_is_complete_for_global_label_permutation(self):
        alphabet = tuple(range(3))
        per = tuple(itertools.permutations(alphabet))
        for length in range(5):
            words = tuple(itertools.product(alphabet, repeat=length))
            orbits = {w: {tuple(p[x] for x in w) for p in per} for w in words}
            for a in words:
                for b in words:
                    self.assertEqual(equality_signature(a) == equality_signature(b),
                                     b in orbits[a])

    def test_permutation_transport_exact_for_all_states_and_frame_pairs(self):
        per = tuple(itertools.permutations(range(3)))
        for old in per:
            for new in per:
                t = sensor_transport(old, new)
                for x in range(3):
                    for y in range(3):
                        self.assertEqual(transported_change(old[x], new[y], t), x != y)

    def test_raw_delta_can_invert_source_change_under_frame_drift(self):
        old, new = (0, 1), (1, 0)
        # The source stays 0 yet the raw observation appears to change.
        self.assertNotEqual(old[0], new[0])
        self.assertFalse(transported_change(old[0], new[0], sensor_transport(old, new)))
        # The source changes yet the raw observation appears constant.
        self.assertEqual(old[0], new[1])
        self.assertTrue(transported_change(old[0], new[1], sensor_transport(old, new)))

    def test_invalid_transport_and_unhashable_report_rejected(self):
        for before, after in (((0, 0), (0, 1)), ((0, 1), (0, 0)), ((0, 1), (0,))):
            with self.assertRaises(SourceGaugeError):
                sensor_transport(before, after)
        for args in ((-1, 1, (0, 1)), (0, 2, (0, 1)), (0, 1, (0, 0))):
            with self.assertRaises(SourceGaugeError):
                transported_change(*args)
        with self.assertRaises(SourceGaugeError):
            equality_signature([['not hashable']])



class TestLanguageAdequacyDiagnostics(unittest.TestCase):
    def test_conditional_identification_can_revert_under_model_expansion(self):
        small = (permutation_worlds(2)[0],)
        full = permutation_worlds(2)
        a = diagnose_signature(small, (0,))
        b = diagnose_signature(full, (0,))
        self.assertEqual(a.status, "IDENTIFIED")
        self.assertEqual(a.possible_targets, (0,))
        self.assertEqual(b.status, "AMBIGUOUS")
        self.assertEqual(set(b.possible_targets), {0, 1})
        self.assertTrue(set(a.compatible_cases).issubset(set(b.compatible_cases)))

    def test_unpredicted_observation_triggers_out_of_model_not_impossible_reality(self):
        worlds = permutation_worlds(2)
        observed = diagnose_signature(worlds, ("new sensory value",))
        self.assertEqual(observed.status, "OUT_OF_MODEL")
        self.assertEqual(observed.compatible_cases, ())
        self.assertEqual(observed.possible_targets, ())

    def test_observation_plus_known_reference_changes_diagnostic(self):
        worlds = permutation_worlds(2)
        self.assertEqual(diagnose_signature(worlds, (0,)).status, "AMBIGUOUS")
        self.assertEqual(diagnose_signature(worlds, (0, 0), (0,)).status, "IDENTIFIED")
        self.assertEqual(diagnose_signature(worlds, (0, 1), (0,)).status, "IDENTIFIED")
        self.assertEqual(diagnose_signature(worlds, (0, 9), (0,)).status, "OUT_OF_MODEL")

    def test_model_expansion_monotonically_enlarges_surviving_source_cases(self):
        all_worlds = permutation_worlds(3)
        for cut in range(1, len(all_worlds)):
            for anchors in ((), (0,), (0, 1)):
                for report in range(3):
                    for refs in itertools.product(range(3), repeat=len(anchors)):
                        sig = (report, *refs)
                        before = diagnose_signature(all_worlds[:cut], sig, anchors)
                        after = diagnose_signature(all_worlds, sig, anchors)
                        self.assertTrue(set(before.compatible_cases).issubset(set(after.compatible_cases)))
                        self.assertTrue(set(before.possible_targets).issubset(set(after.possible_targets)))

    def test_signature_shape_guard(self):
        with self.assertRaises(SourceGaugeError):
            diagnose_signature(permutation_worlds(2), (0, 1), ())
        with self.assertRaises(SourceGaugeError):
            diagnose_signature(permutation_worlds(2), (0,), (0,))


class TestAdaptiveSourceGaugeNoGo(unittest.TestCase):
    def test_all_feedback_policies_respect_equivariant_symmetry(self):
        # C_n acts by cyclic rotations. These nontrivial authorized actions
        # commute with C_n, so feedback cannot attach absolute source labels.
        for n in (2, 3, 4):
            rotations = [tuple((i + offset) % n for i in range(n)) for offset in range(n)]
            dictionaries = tuple(itertools.permutations(range(n)))
            actions = tuple(rotations)
            for mode in range(3):
                decisions = {}
                for width in range(1, 5):
                    for history in itertools.product(range(n), repeat=width):
                        decisions[history] = (0 if mode == 0 else
                                              history[-1] % n if mode == 1 else
                                              (sum(history) + width) % n)
                for gauge in rotations:
                    for dictionary in dictionaries:
                        for initial in range(n):
                            shadow = adaptive_gauge_shadow(initial, dictionary, gauge, actions,
                                                            decisions, rounds=3)
                            self.assertEqual(shadow.first_reports, shadow.alternative_reports)
                            self.assertEqual(len(shadow.choices), 3)
                            self.assertEqual(shadow.alternative_source, gauge[initial])
                            if gauge != rotations[0]:
                                self.assertNotEqual(shadow.first_source, shadow.alternative_source)

    def test_semantically_named_non_equivariant_action_is_real_symmetry_breaker(self):
        # Constant f(x)=0 commutes with neither the two-state swap nor its
        # transformed source labeling; this is NOT an action-only no-go case.
        with self.assertRaisesRegex(SourceGaugeError, "breaks"):
            adaptive_gauge_shadow(0, (0, 1), (1, 0), ((0, 0),), {(0,): 0}, 1)

    def test_no_ghost_policy_actions_or_history_length(self):
        for table, rounds in (({}, 1), ({(0,): 2}, 1)):
            with self.assertRaises(SourceGaugeError):
                adaptive_gauge_shadow(0, (0, 1), (1, 0), ((0, 1),), table, rounds)
        with self.assertRaises(SourceGaugeError):
            adaptive_gauge_shadow(0, (0, 1), (1, 0), ((0, 1),), {}, -1)


if __name__ == '__main__':
    unittest.main()
