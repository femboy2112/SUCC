from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.minimal_observation import FiniteObservation
from observational_succ.observer_discovery import (
    CoordinateObservation, DiscoveryError, RationalForm, conditional_rule,
    discover, joint_probe_minima, nested_envelope, replay_envelope, schur_envelope,
)


class EnvelopeDiscoveryTests(unittest.TestCase):
    def form(self, entries=((1, 2), (2, 1))):
        return RationalForm("declared-complete-model", 7, ("x", "y"), entries)

    def test_signed_blocks_do_not_imply_positive_short(self):
        g = self.form()
        cert = schur_envelope(g, CoordinateObservation.on(g, ("x",)))
        self.assertEqual(cert.result.coefficients, ((Q(-3),),))
        self.assertEqual(g.energy((1, -2)), -3)
        self.assertEqual(g.energy((1, 0)), 1)
        self.assertTrue(replay_envelope(g, cert))

    def test_singular_range_is_required_not_inferred_from_psd(self):
        invalid = self.form(((0, 1), (1, 0)))
        with self.assertRaisesRegex(DiscoveryError, "RANGE_CONDITION_FAILED"):
            schur_envelope(invalid, CoordinateObservation.on(invalid, ("x",)))
        self.assertEqual(invalid.energy((0, 100)), 0)
        self.assertEqual(invalid.energy((1, -100)), -200)
        valid = self.form(((-2, 0), (0, 0)))
        cert = schur_envelope(valid, CoordinateObservation.on(valid, ("x",)))
        self.assertEqual(cert.result.coefficients, ((Q(-2),),))
        self.assertEqual(cert.response, ((Q(0),),))

    def test_negative_high_block_rejected(self):
        g = self.form(((1, 0), (0, -1)))
        with self.assertRaisesRegex(DiscoveryError, "HIGH_PSD_FAILED"):
            schur_envelope(g, CoordinateObservation.on(g, ("x",)))

    def test_identity_observation_and_noncontiguous_coordinates(self):
        g = RationalForm("source", 0, ("x", "y", "z"),
                         ((2, 1, 0), (1, 2, 1), (0, 1, 2)))
        identity = schur_envelope(g, CoordinateObservation.on(g, g.axes))
        self.assertEqual(identity.result, g)
        self.assertEqual(identity.response, ())
        cert = schur_envelope(g, CoordinateObservation.on(g, ("x", "z")))
        self.assertEqual(cert.result.coefficients, ((Q(3, 2), Q(-1, 2)),
                                                   (Q(-1, 2), Q(3, 2))))

    def test_source_epoch_coefficients_and_basis_are_binding(self):
        g = self.form()
        observation = CoordinateObservation.on(g, ("x",))
        mutants = (replace(g, epoch=8), replace(g, source_id="other"),
                   replace(g, coefficients=((2, 2), (2, 1))),
                   replace(g, axes=("x", "hidden")))
        for mutant in mutants:
            with self.assertRaisesRegex(DiscoveryError, "SOURCE_MISMATCH"):
                schur_envelope(mutant, observation)
        with self.assertRaises(DiscoveryError):
            CoordinateObservation.on(g, ("x", "ghost"))
        with self.assertRaises(DiscoveryError):
            CoordinateObservation.on(g, ("y", "x"))

    def test_forgeries_do_not_become_proof_authority(self):
        g = self.form()
        cert = schur_envelope(g, CoordinateObservation.on(g, ("x",)))
        bad = (replace(cert, authority="LEAN_KERNEL_PROVED"),
               replace(cert, rule="inferred by 100 samples"),
               replace(cert, response=((Q(1),),)),
               replace(cert, result=replace(cert.result, coefficients=((Q(1),),))),
               replace(cert, result=replace(cert.result, epoch=8)),
               replace(cert, response=((True,),)))
        for forged in bad:
            self.assertFalse(replay_envelope(g, forged))
        # Independent verifier permits a different correct solution in ker D.
        singular = self.form(((1, 0), (0, 0)))
        cert = schur_envelope(singular, CoordinateObservation.on(singular, ("x",)))
        self.assertTrue(replay_envelope(singular, replace(cert, response=((Q(99),),))))

    def test_invalid_scalar_types_and_dimension(self):
        for bad in (True, 1.0, "1"):
            with self.assertRaises(DiscoveryError):
                self.form(((1, bad), (bad, 1)))
        for axes in (("x", "x"), (), tuple("abcde")):
            with self.assertRaises(DiscoveryError):
                RationalForm("bad", 0, axes, ((1,),))
        with self.assertRaises(DiscoveryError):
            self.form().energy((True, 1))
        with self.assertRaises(DiscoveryError):
            self.form(((1, 2), (3, 1)))

    def test_nested_singular_envelope_and_type_mismatch(self):
        g = RationalForm("nested", 0, ("x", "y", "z"),
                         ((-1, 1, 1), (1, 1, 1), (1, 1, 1)))
        result = nested_envelope(g, ("x", "y"), ("x",))
        self.assertEqual(result["direct"].result.coefficients, ((Q(-2),),))
        with self.assertRaises(DiscoveryError):
            nested_envelope(g, ("x", "y"), ("z",))
        with self.assertRaisesRegex(DiscoveryError, "SOURCE_MISMATCH"):
            schur_envelope(result["first"].result, CoordinateObservation.on(g, ("x",)))

    def test_independent_gram_expansion_checks_all_matrix_coefficients(self):
        # Construct D=v v', C=Dw. Expected short from independent outer products;
        # no call to the producer's solver or the inherited PSD/minor helpers.
        for v in ((0, 0), (1, 0), (0, 1), (1, -1), (2, 1)):
            d = tuple(tuple(Q(i*j) for j in v) for i in v)
            for w in product((-1, 0, 1), repeat=2):
                c = tuple(sum(d[i][j]*w[j] for j in range(2)) for i in range(2))
                g = RationalForm("gram-model", 0, ("x", "y", "z"),
                                 ((-1, *c), (c[0], *d[0]), (c[1], *d[1])))
                cert = schur_envelope(g, CoordinateObservation.on(g, ("x",)))
                expected = -1-sum(v[i]*w[i] for i in range(2))**2
                self.assertEqual(cert.result.coefficients, ((expected,),))
                x = cert.response
                # Compare coefficients of the whole quadratic polynomial on R^3.
                for i in range(3):
                    for j in range(3):
                        u = (x[0][0], x[1][0]) if i == 0 else tuple(Q(i-1 == k) for k in range(2))
                        t = (x[0][0], x[1][0]) if j == 0 else tuple(Q(j-1 == k) for k in range(2))
                        reconstructed = sum(u[k]*d[k][l]*t[l] for k in range(2) for l in range(2))
                        if i == j == 0:
                            reconstructed += expected
                        self.assertEqual(reconstructed, g.coefficients[i][j])

    def test_failed_staged_range_is_not_an_extended_real_conclusion(self):
        g = RationalForm("bad-stage", 0, ("x", "y", "z"),
                         ((0, 1, 0), (1, 0, 0), (0, 0, 1)))
        with self.assertRaisesRegex(DiscoveryError, "RANGE_CONDITION_FAILED"):
            nested_envelope(g, ("x", "y"), ("x",))
        # Direct inspection: x=0 has infimum 0, x=1 has infimum -infinity.
        self.assertEqual(g.energy((0, -1000, 0)), 0)
        self.assertEqual(g.energy((1, -1000, 0)), -2000)
        self.assertIn("extended-real", conditional_rule("OD-03")["name"])


class SearchAndMenuTests(unittest.TestCase):
    def test_five_smallest_countermodels_replay_without_envelope_helper(self):
        r = discover()
        self.assertEqual(r["nested_exact_instances"], 28)
        self.assertEqual(r["illegal_compositions_rejected"], 1)
        expected = (((0, 1), (1, 0)), ((1, 2), (2, 1)), ((0, 1), (1, 1)),
                    ((0, 0), (0, 1)), ((0, 1), (1, 0)))
        for i, row in enumerate(r["refutation_candidates"]):
            self.assertEqual(row["outcome"], "REFUTED")
            witness = row["witness"]
            self.assertEqual(witness["form"]["coefficients"], expected[i])
            a, b, d = expected[i][0][0], expected[i][0][1], expected[i][1][1]
            evaluate = lambda x, y: a*x*x+2*b*x*y+d*y*y
            if i == 0:
                self.assertEqual(evaluate(0, 123), 0)
                self.assertNotEqual(evaluate(1, 0), evaluate(1, 1))
            elif i == 1:
                self.assertLess(evaluate(*witness["vector"]), 0)
                self.assertGreater(a*d, 0)
            elif i == 2:
                self.assertNotEqual(a, evaluate(1, witness["minimizer_y"]))
            elif i == 3:
                self.assertNotEqual(evaluate(0, 1), evaluate(0, 0))
            else:
                slope = evaluate(1, witness["ray_y"])-evaluate(1, 0)
                self.assertLess(slope, 0)
                self.assertEqual(d, 0)

    def test_exhaustion_and_conditional_rules_never_promote_samples(self):
        r = discover(0)
        self.assertTrue(all(c["outcome"] == "UNRESOLVED" for c in r["refutation_candidates"]))
        self.assertFalse(r["search_proves_universal_theorems"])
        for rule in r["surviving_rules"]:
            self.assertTrue(rule["retained_hypotheses"])
            self.assertFalse(rule["runtime_issued_universal_proof"])
            self.assertFalse(rule["Lean_kernel_replayed"])
        for bad in (True, -1, 126):
            with self.assertRaises(DiscoveryError):
                discover(bad)
        with self.assertRaises(DiscoveryError):
            conditional_rule("prove RH by matrix hash")

    def test_search_reproducibility_and_budget_prefix_minimality(self):
        report = discover()
        self.assertEqual(report, discover())
        for index, row in enumerate(report["refutation_candidates"]):
            smaller = discover(row["matrices_examined"]-1)
            self.assertEqual(smaller["refutation_candidates"][index]["outcome"], "UNRESOLVED")

    def test_chi4_joint_bits_need_both_probes(self):
        p = FiniteObservation("entire chi4 residue source", 0, (0, 1, 2, 3), (0, 1, 0, -1))
        menu = ((0, 1, 0, 1), (0, 0, 1, 1))
        r = joint_probe_minima(p, menu)
        self.assertEqual(r["minimum_cardinality"], 2)
        self.assertEqual(r["minimum_subsets"], ((0, 1),))
        self.assertEqual(len(r["ablation_pairs"]), 2)
        for receipt in r["ablation_pairs"]:
            s, t = receipt["source_pair"]
            j = receipt["removed_probe"]
            self.assertNotEqual(p.target[s], p.target[t])
            self.assertEqual(menu[1-j][s], menu[1-j][t])
            self.assertNotEqual(menu[j][s], menu[j][t])

    def test_global_minimum_not_confused_with_irredundancy(self):
        p = FiniteObservation("bits", 0, (0, 1, 2, 3), (0, 1, 1, 0))
        menu = ((0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0))
        r = joint_probe_minima(p, menu)
        self.assertEqual(r["minimum_cardinality"], 1)
        self.assertEqual(r["minimum_subsets"], ((2,),))
        self.assertEqual(r["inclusion_minimal_subsets"], ((2,), (0, 1)))
        self.assertFalse(r["adaptive_optimality_claimed"])

    def test_empty_menu_constant_target_and_true_joint_obstruction(self):
        constant = FiniteObservation("constant", 0, (1, 2), (3, 3))
        self.assertEqual(joint_probe_minima(constant, ())["minimum_cardinality"], 0)
        nonconstant = replace(constant, target=(3, 4))
        r = joint_probe_minima(nonconstant, ((0, 0), (1, 1)))
        self.assertEqual(r["outcome"], "PROVEN_JOINT_OBSTRUCTION")
        self.assertIsNone(r["minimum_cardinality"])
        self.assertEqual(r["all_subset_receipts"][-1]["certificate"]["collision"], (0, 1))

    def test_joint_menu_independent_exhaustive_decoders(self):
        # Independent function-table enumeration on three states, two binary probes.
        for target in product((0, 1), repeat=3):
            p = FiniteObservation("complete-three-state", 0, (0, 1, 2), target)
            for left in product((0, 1), repeat=3):
                right = (0, 1, 0)
                r = joint_probe_minima(p, (left, right))
                expected = []
                for subset in ((), (0,), (1,), (0, 1)):
                    artifacts = tuple(product((0, 1), repeat=len(subset)))
                    observations = [tuple((left, right)[j][s] for j in subset) for s in range(3)]
                    decodes = any(all(values[artifacts.index(observations[s])] == target[s]
                                      for s in range(3))
                                  for values in product((0, 1), repeat=len(artifacts)))
                    if decodes:
                        expected.append(subset)
                actual = [row["subset"] for row in r["all_subset_receipts"]
                          if row["certificate"]["outcome"] == "PROVEN_FACTORIZATION"]
                self.assertEqual(actual, expected)

    def test_menu_budget_and_source_hash_guards(self):
        p = FiniteObservation("s", 0, (0, 1), (0, 1))
        with self.assertRaises(DiscoveryError):
            joint_probe_minima(p, ((0, 1),)*9)
        with self.assertRaises(DiscoveryError):
            joint_probe_minima(FiniteObservation("s", 0, (0,)*65, (0,)*65), ())
        old = joint_probe_minima(p, ((0, 1),))
        new = joint_probe_minima(replace(p, epoch=1), ((0, 1),))
        self.assertNotEqual(old["source_digest"], new["source_digest"])


if __name__ == "__main__":
    unittest.main()
