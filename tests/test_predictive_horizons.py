"""Exact controls for global report-horizon certificates and finite realizations."""

from dataclasses import replace
from itertools import product
import unittest

from observational_succ.predictive_horizons import (
    AdditiveHorizonMonoid, FiniteReportedSource, HorizonCertificate,
    certify_horizon, compose_horizons, horizon_profile, power_map,
    realize_horizon_monoid, verify_horizon, verify_profile,
)


class PredictiveHorizonTests(unittest.TestCase):
    def test_later_steps_can_be_known_while_next_step_is_hidden(self):
        source = FiniteReportedSource((1, 2, 2), (0, 0, 1))
        self.assertEqual([certify_horizon(source, n).predictable for n in range(7)],
                         [True, False, True, True, True, True, True])
        negative = certify_horizon(source, 1)
        self.assertTrue(verify_horizon(source, negative))
        self.assertEqual(negative.collision, (0, 1))
        combined = compose_horizons(source, certify_horizon(source, 2), certify_horizon(source, 3))
        self.assertEqual(combined.horizon, 5)
        self.assertTrue(verify_horizon(source, combined))

    def test_permutation_only_even_times(self):
        source = FiniteReportedSource((1, 2, 3, 0), (0, 0, 1, 1))
        profile = horizon_profile(source)
        self.assertTrue(verify_profile(source, profile))
        self.assertEqual((profile.preperiod, profile.period), (0, 4))
        for n in [0, 1, 2, 3, 4, 19, 20, 10**30, 10**30 + 1]:
            self.assertEqual(profile.contains(n), n % 2 == 0)

    def test_no_positive_time_is_possible(self):
        source = realize_horizon_monoid(AdditiveHorizonMonoid(()))
        profile = horizon_profile(source)
        self.assertTrue(verify_profile(source, profile))
        self.assertTrue(profile.contains(0))
        for n in (1, 2, 100, 10**20):
            self.assertFalse(profile.contains(n))

    def test_certificate_mutations_rejected(self):
        source = FiniteReportedSource((1, 2, 3, 0), (0, 0, 1, 1))
        positive = certify_horizon(source, 2)
        negative = certify_horizon(source, 1)
        for mutation in (
            replace(positive, horizon=1), replace(positive, source_sha256="wrong"),
            replace(positive, induced=(0, 1)), replace(positive, induced=(1, True)),
            replace(positive, collision=(0, 1)), replace(negative, collision=(0, 2)),
            replace(negative, collision=(-1, 2)), replace(negative, horizon=-1),
            HorizonCertificate(source.fingerprint, 0),
        ):
            self.assertFalse(verify_horizon(source, mutation), mutation)
        changed_source = FiniteReportedSource((0, 1, 2, 3), source.report)
        self.assertFalse(verify_horizon(changed_source, positive))
        with self.assertRaises(ValueError):
            compose_horizons(source, positive, negative)

    def test_profile_mutations_and_budget(self):
        source = FiniteReportedSource((1, 2, 2), (0, 0, 1))
        profile = horizon_profile(source)
        self.assertTrue(verify_profile(source, profile))
        self.assertFalse(verify_profile(source, replace(profile, admitted=(True, True, True))))
        self.assertFalse(verify_profile(source, replace(profile, period=2)))
        self.assertFalse(verify_profile(source, replace(profile, source_sha256="other")))
        with self.assertRaises(RuntimeError):
            horizon_profile(source, max_powers=1)

    def test_apery_matches_independent_coin_dynamic_program(self):
        for generators in ((), (1,), (2,), (2, 3), (3, 5), (4, 6), (4, 7, 9), (6, 10, 15)):
            monoid = AdditiveHorizonMonoid(generators)
            reachable = [False] * 161
            reachable[0] = True
            for n in range(1, len(reachable)):
                reachable[n] = any(n >= g and reachable[n - g] for g in generators)
            self.assertEqual([monoid.contains(n) for n in range(161)], reachable)
            c, d = monoid.tail_parameters()
            for n in range(c, 161):
                self.assertEqual(monoid.contains(n), bool(generators) and n % d == 0)

    def test_all_monoid_realizations_match_direct_source_walks(self):
        for generators in ((), (1,), (2,), (2, 3), (3, 5), (4, 6), (4, 7, 9), (6, 10, 15)):
            monoid = AdditiveHorizonMonoid(generators)
            source = realize_horizon_monoid(monoid)
            states = list(range(len(source.transition)))
            profile = horizon_profile(source)
            self.assertTrue(verify_profile(source, profile))
            for n in range(80):
                direct = all(source.report[i] != source.report[j]
                             or source.report[states[i]] == source.report[states[j]]
                             for i in range(len(states)) for j in range(i))
                self.assertEqual(direct, monoid.contains(n))
                self.assertEqual(profile.contains(n), direct)
                certificate = certify_horizon(source, n)
                self.assertEqual(certificate.predictable, direct)
                self.assertTrue(verify_horizon(source, certificate))
                states = [source.transition[x] for x in states]

    def test_a_different_target_does_not_have_additive_times(self):
        # P(T^n x) from h(x) is NOT the same full-report endomorphism contract.
        source = FiniteReportedSource((1, 2, 3, 0), (0, 0, 1, 2))
        target = (0, 0, 0, 1)
        flags = []
        for n in range(3):
            power = power_map(source, n)
            flags.append(all(source.report[x] != source.report[z]
                             or target[power[x]] == target[power[z]]
                             for x in range(4) for z in range(x)))
        self.assertEqual(flags, [True, True, False])

    def test_one_realized_fiber_does_not_have_additive_times(self):
        source = FiniteReportedSource((2, 3, 0, 3), (0, 0, 1, 1))
        flags = [len({source.report[power_map(source, n)[x]] for x in (0, 1)}) == 1
                 for n in range(3)]
        self.assertEqual(flags, [True, True, False])

    def test_input_guards(self):
        for transition, report in (((), ()), ((1,), (0,)), ((0,), (1,)), ((0,), (True,))):
            with self.assertRaises(ValueError):
                FiniteReportedSource(transition, report)
        source = FiniteReportedSource((0,), (0,))
        for value in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                certify_horizon(source, value)
        for generators in ((0,), (-1,), (True,), (1.5,)):
            with self.assertRaises(ValueError):
                AdditiveHorizonMonoid(generators)

    def test_program_words_need_not_have_finitely_many_generators(self):
        actions = {"a": (1, 1, 3, 3), "b": (0, 0, 0, 0)}
        report = (0, 1, 0, 2)
        for length in range(11):
            for word in product("ab", repeat=length):
                image = tuple(range(4))
                for action in word:
                    image = tuple(actions[action][state] for state in image)
                source = FiniteReportedSource(image, report)
                actual = certify_horizon(source, 1).predictable
                self.assertEqual(actual, not word or "b" in word)
        for n in range(11):
            word = "a" * n + "b"
            self.assertFalse(any("b" in word[:i] and "b" in word[i:]
                                 for i in range(1, len(word))))


if __name__ == "__main__":
    unittest.main()
