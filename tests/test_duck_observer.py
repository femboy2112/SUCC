from dataclasses import FrozenInstanceError, replace
from itertools import product
import hashlib
import json
import unittest

from observational_succ.duck_observer import (
    FiniteObserver, DistinguishingWord, ClosedRelation, ObserverError,
    ProbeBudgetExceeded, distinguish, verify_certificate, observable_quotient,
    is_morphism, common_observable_factor, from_causal_endo, as_eos_morphism,
    lean_closed_relation_certificate,
)


def model(transitions, outputs, source="test"):
    return FiniteObserver(source, 0, "readout", tuple(map(str, range(len(outputs)))),
                          tuple("a" + str(i) for i in range(len(transitions))),
                          tuple(tuple(t) for t in transitions), tuple(outputs))


def exhaustive_word(left, right, x, y):
    """Independent word census: no BFS, production run or partition routine."""
    for length in range(len(left.states) * len(right.states)):
        for word in product(range(len(left.actions)), repeat=length):
            a, b = x, y
            for act in word:
                a, b = left.transitions[act][a], right.transitions[act][b]
            if left.outputs[a] != right.outputs[b]:
                return tuple(left.actions[i] for i in word)
    return None


class DuckObserverTests(unittest.TestCase):
    def test_exact_lean_certificate_export_and_hostile_labels(self):
        left = model(((1, 0),), ("same", "same"), source="A\naxiom fake : False")
        right = model(((0,),), ("same",), source="B")
        cert = distinguish(left, right, 0, 0)
        source = lean_closed_relation_certificate(left, right, cert)
        payload_line = next(line for line in source.splitlines()
                            if line.startswith("-- Exact declared-model/certificate JSON: "))
        payload = payload_line.split(": ", 1)[1]
        self.assertEqual(json.loads(payload)["left"]["source_id"], left.source_id)
        self.assertIn(hashlib.sha256(payload.encode("ascii")).hexdigest(), source)
        self.assertNotIn("\naxiom fake", source)
        self.assertIn("def stepLeft : Fin 1 → Fin 2 → Fin 2", source)
        self.assertIn("theorem all_words (word : List (Fin 1))", source)
        self.assertEqual(source, lean_closed_relation_certificate(left, right, cert))
        with self.assertRaises(ObserverError):
            lean_closed_relation_certificate(left, right, replace(cert, pairs=((0, 0),)))
        with self.assertRaises(ObserverError):
            lean_closed_relation_certificate(replace(left, epoch=1), right, cert)
        empty = model((), ("same",))
        self.assertIn("fun a => Fin.elim0 a", lean_closed_relation_certificate(
            empty, empty, distinguish(empty, empty, 0, 0)))

    def test_exhaustive_unary_models_and_partition(self):
        comparisons = 0
        for n in range(1, 4):
            for row in product(range(n), repeat=n):
                for outputs in product(("0", "1"), repeat=n):
                    system = model((row,), outputs)
                    quotient = observable_quotient(system)
                    self.assertTrue(is_morphism(system, quotient.target, quotient.projection, onto=True))
                    self.assertLessEqual(quotient.strict_refinements, max(0, n - len(set(outputs))))
                    for x, y in product(range(n), repeat=2):
                        cert = distinguish(system, system, x, y)
                        oracle = exhaustive_word(system, system, x, y)
                        self.assertTrue(verify_certificate(system, system, cert))
                        self.assertEqual(type(cert) is ClosedRelation, oracle is None)
                        self.assertEqual(quotient.projection[x] == quotient.projection[y], oracle is None)
                        if oracle is not None:
                            self.assertEqual(cert.word, oracle)
                            self.assertLessEqual(len(cert.word), n*n-1)
                            self.assertLessEqual(len(cert.word), max(0, n-2))
                        comparisons += 1
        self.assertEqual(comparisons, 2010)

    def test_independent_cross_model_two_action_census(self):
        models = [model((r, s), outputs) for r in product(range(2), repeat=2)
                  for s in product(range(2), repeat=2)
                  for outputs in product(("0", "1"), repeat=2)]
        comparisons = 0
        for left in models:
            for right in models:
                for x, y in product(range(2), repeat=2):
                    cert = distinguish(left, right, x, y)
                    oracle = exhaustive_word(left, right, x, y)
                    self.assertTrue(verify_certificate(left, right, cert))
                    self.assertEqual(type(cert) is ClosedRelation, oracle is None)
                    if oracle is not None:
                        self.assertEqual(cert.word, oracle)
                        self.assertLessEqual(len(cert.word), len(left.states)+len(right.states)-2)
                    comparisons += 1
        self.assertEqual(comparisons, 16384)

    def test_sharp_linear_depth_bound(self):
        for n in range(1, 25):
            chain = model((tuple(min(i+1, n-1) for i in range(n)),),
                          ("zero",)*(n-1)+("one",))
            idle = model(((0,),), ("zero",))
            witness = distinguish(chain, idle, 0, 0)
            self.assertEqual(len(witness.word), n-1)
            self.assertTrue(verify_certificate(chain, idle, witness))
            if n >= 2:
                internal = distinguish(chain, chain, 0, 1)
                self.assertEqual(len(internal.word), n-2)

    def test_mutated_relation_cannot_drop_closure(self):
        left = model(((1, 1),), ("0", "1"))
        right = model(((0,),), ("0",))
        false = ClosedRelation(left, right, (0, 0), ((0, 0),))
        self.assertFalse(verify_certificate(left, right, false))
        self.assertFalse(verify_certificate(left, right, replace(false, pairs=((0, 0), (1, 0)))))
        witness = distinguish(left, right, 0, 0)
        self.assertEqual(witness.word, ("a0",))
        self.assertFalse(verify_certificate(left, right, replace(witness, word=())))

    def test_certificate_exact_binding_and_immutability(self):
        a = model(((1, 0),), ("same", "same"), source="A")
        cert = distinguish(a, a, 0, 1)
        for b in (replace(a, epoch=1), replace(a, source_id="B"),
                  replace(a, transitions=((0, 1),)), replace(a, outputs=("x", "y"))):
            with self.assertRaises(ObserverError):
                verify_certificate(b, a, cert)
        with self.assertRaises(FrozenInstanceError):
            cert.pairs = ()
        self.assertFalse(verify_certificate(a, a, replace(cert, pairs=())))
        self.assertFalse(verify_certificate(a, a, replace(cert, pairs=cert.pairs*2)))

    def test_budget_is_not_a_verdict(self):
        a = model(((1, 2, 3, 3),), ("0", "0", "0", "1"))
        b = model(((0,),), ("0",))
        with self.assertRaises(ProbeBudgetExceeded):
            distinguish(a, b, 0, 0, max_pairs=2)
        result = distinguish(a, b, 0, 0)
        self.assertEqual(result.word, ("a0",)*3)
        self.assertTrue(verify_certificate(a, b, result))

    def test_erasure_is_not_identity_factor(self):
        flip = model(((1, 0),), ("erased", "erased"))
        idle = model(((0, 1),), ("erased", "erased"))
        self.assertIsInstance(distinguish(flip, idle, 0, 0), ClosedRelation)
        self.assertFalse(is_morphism(flip, idle, (0, 1)))
        self.assertIsNone(common_observable_factor(flip, idle))
        trivial = common_observable_factor(flip, idle, require_nontrivial=False)
        self.assertEqual(len(trivial.common.states), 1)

    def test_nontrivial_common_factor_with_unequal_hidden_sizes(self):
        a = model(((1, 0),), ("0", "1"), "two")
        b = model(((1, 0, 3, 2),), ("0", "1", "0", "1"), "four")
        common = common_observable_factor(a, b)
        self.assertEqual(len(common.common.states), 2)
        self.assertTrue(is_morphism(a, common.common, common.left_projection, onto=True))
        self.assertTrue(is_morphism(b, common.common, common.right_projection, onto=True))
        self.assertFalse(len(a.states) == len(b.states))
        mismatch = model(((0, 1),), ("0", "1"))
        self.assertIsNone(common_observable_factor(a, mismatch))

    def test_common_factor_matches_independent_bijection_search(self):
        models = [model((r, s), outputs) for r in product(range(2), repeat=2)
                  for s in product(range(2), repeat=2)
                  for outputs in product(("0", "1"), repeat=2)]
        checks = 0
        for left in models:
            for right in models:
                # Two-state nontrivial separated common factors must be
                # isomorphic.  Check BOTH bijections directly, independently
                # of quotient construction and the production morphism checker.
                oracle = exhaustive_word(left, left, 0, 1) is not None and any(
                    all(right.outputs[i] == left.outputs[p[i]] for i in range(2))
                    and all(p[right.transitions[a][i]] == left.transitions[a][p[i]]
                            for a in range(2) for i in range(2))
                    for p in ((0, 1), (1, 0)))
                self.assertEqual(common_observable_factor(left, right) is not None, oracle)
                checks += 1
        self.assertEqual(checks, 4096)
        hidden_clock = model(((1, 0),), ("erased", "erased"))
        self.assertTrue(is_morphism(hidden_clock, hidden_clock, (0, 1), onto=True))
        self.assertIsNone(common_observable_factor(hidden_clock, hidden_clock))

    def test_empty_action_and_empty_carrier_boundaries(self):
        a = model((), ("0", "1", "0"))
        self.assertEqual(distinguish(a, a, 0, 1).word, ())
        self.assertIsInstance(distinguish(a, a, 0, 2), ClosedRelation)
        self.assertEqual(observable_quotient(a).classes, ((0, 2), (1,)))
        empty = model((), ())
        q = observable_quotient(empty)
        self.assertEqual(q.classes, ())
        self.assertTrue(is_morphism(empty, q.target, (), onto=True))
        with self.assertRaises(ObserverError):
            distinguish(empty, empty, 0, 0)

    def test_exact_input_guards(self):
        a = model(((1, 0),), ("0", "1"))
        for bad in (True, 1.0, "1"):
            with self.assertRaises(ObserverError):
                replace(a, transitions=((bad, 0),))
            with self.assertRaises(ObserverError):
                distinguish(a, a, 0, 1, max_pairs=bad)
        with self.assertRaises(ObserverError):
            replace(a, outputs=["0", "1"])
        with self.assertRaises(ObserverError):
            distinguish(a, replace(a, basis="different"), 0, 0)
        with self.assertRaises(ObserverError):
            distinguish(a, replace(a, actions=("other",)), 0, 0)

    def test_existing_causal_and_eos_adapters(self):
        from fractions import Fraction
        from observational_succ.causal_nerode_succ import SourceChart, CausalInstrument
        chart = SourceChart("original", 0, "readout", ("s0", "s1", "s2", "s3"), ("0", "1", "0", "1"))
        act = CausalInstrument("flip", chart, chart, ("s1", "s0", "s3", "s2"))
        source = from_causal_endo(chart, (act,))
        quotient = observable_quotient(source)
        eos = as_eos_morphism(source, quotient.target, quotient.projection, target_id="current-readout")
        verdict = eos.verify()
        self.assertTrue(verdict["all_actions_and_outputs_compatible"])
        self.assertFalse(verdict["independent_physical_provenance_authenticated"])
        self.assertEqual(eos.concrete.action("flip").step(0), (1, 1))
        future = replace(chart, epoch=1)
        changing = CausalInstrument("later", chart, future, act.transitions)
        with self.assertRaises(ObserverError):
            from_causal_endo(chart, (changing,))
        with self.assertRaises(ObserverError):
            from_causal_endo(chart, (replace(act, cost=Fraction(2)),))
        self.assertEqual(eos.concrete.source_id, "original/epoch=0")


if __name__ == "__main__":
    unittest.main()
