"""Positive carrier realization: exact tests, negative controls, mutations.

Every assertion is exact rational arithmetic.  Lower bounds are checked by
independent witnesses (fooling sets, Frobenius imprimitivity orders), upper
bounds by explicit carriers with exact behavior-equivalence certificates.
"""
import itertools
import random
import unittest
from fractions import Fraction as Q

from observational_succ.carrier_realization import (
    BOT, PositiveCarrier, RealizationError,
    availability_square, calibration_matrix, carrier_from_cone,
    carrier_realization_oracle, charpoly, closed_loop_law, cone_coordinates,
    cyclotomic, cyclotomic_clock, distinguishing_experiment,
    equivalence_certificate, euler_phi, fooling_set_lower_bound,
    hankel_block, is_fooling_set, legality_pattern, mat, matmul,
    minimal_realization, orbit_cone_carrier, path_walk_carrier,
    peripheral_spectrum_certificate, permutation_event, promotion_witness,
    quadratic_root_of_unity_test, rank, rational_clock,
    rational_roots_and_remainder, reachable_cone_refinement,
    scaled_cyclotomic_order, source_posterior, tensor_fooling_set, vec,
    verify_cone, words_up_to,
)

TICK = ("clock", "tick")
RESET = ("clock", "reset")
BOK = ("b", "ok")


class TestCalibration(unittest.TestCase):
    """Section 4 of the brief: P has rank 3 and nonnegative rank 4."""

    def test_row_stochastic_rank_three_dependence(self):
        P = calibration_matrix()
        for row in P:
            self.assertEqual(sum(row, Q(0)), 1)
        self.assertEqual(rank(P), 3)
        dep = tuple(P[0][j] - P[1][j] - P[2][j] + P[3][j] for j in range(4))
        self.assertEqual(dep, (Q(0),) * 4)

    def test_fooling_set_certificate(self):
        P = calibration_matrix()
        cells = ((0, 0), (1, 2), (2, 1), (3, 3))
        self.assertTrue(is_fooling_set(P, cells))
        size, found = fooling_set_lower_bound(P)
        self.assertEqual(size, 4)
        self.assertTrue(is_fooling_set(P, found))

    def test_mutation_rank_three_matrix_with_nonneg_rank_three_has_no_four_fooling_set(self):
        h = Q(1, 2)
        # rows r1, r2, r3 and (r1+r2)/2: rank 3, explicit 3-term factorization
        M = mat([[h, h, 0, 0], [h, 0, h, 0], [0, h, 0, h], [h, Q(1, 4), Q(1, 4), 0]])
        self.assertEqual(rank(M), 3)
        self.assertLessEqual(fooling_set_lower_bound(M)[0], 3)

    def test_fooling_cells_must_be_positive_and_pairwise_fooling(self):
        P = calibration_matrix()
        self.assertFalse(is_fooling_set(P, ((0, 0), (0, 1))))      # same row
        self.assertFalse(is_fooling_set(P, ((0, 2), (1, 2))))      # zero cell
        self.assertFalse(is_fooling_set(P, ((0, 0), (1, 0))))      # rectangle


class TestPathWalkFamily(unittest.TestCase):
    """PW_n: linear dimension 3^n, positive carrier dimension 4^n."""

    def test_pw1_linear_dimension_three_and_behavior_equality(self):
        pw = path_walk_carrier(1)
        R = minimal_realization(pw)
        self.assertEqual(R.dimension, 3)
        self.assertTrue(R.mass_conserving())
        for w in words_up_to(pw, 3):
            for s in pw.preparations:
                self.assertEqual(R.probability(s, w), pw.probability(s, w))

    def test_pw1_actions_do_not_commute(self):
        pw = path_walk_carrier(1)
        A = tuple(tuple(sum((pw.events["a"][z][i][j] for z in range(4)), Q(0))
                        for j in range(4)) for i in range(4))
        B = pw.events["b"]["s"]
        self.assertNotEqual(matmul(A, B), matmul(B, A))

    def test_pw1_single_source_block_forces_four_states(self):
        pw = path_walk_carrier(1)
        rows = [("u", (("a", z),)) for z in range(4)]
        cols = [(("a", z),) for z in range(4)]
        H = hankel_block(pw, rows, cols)
        self.assertEqual(rank(H), 3)
        self.assertEqual(fooling_set_lower_bound(H)[0], 4)
        rep = carrier_realization_oracle(pw, proposed_dimension=3, hankel_rows=rows,
                                         hankel_cols=cols)
        self.assertEqual(rep["verdict"], "FINITE_OBSTRUCTION")
        self.assertEqual(rep["positive_dimension_lower_bound"], 4)

    def test_pw1_oracle_recovers_four_state_carrier(self):
        pw = path_walk_carrier(1)
        rep = carrier_realization_oracle(pw, proposed_dimension=4, cone_depth=2)
        self.assertEqual(rep["verdict"], "LAWFUL_REALIZATION")
        self.assertEqual(rep["carrier_dimension"], 4)
        self.assertTrue(rep["equivalence"]["equivalent"])

    def test_pw2_dimensions_nine_and_sixteen(self):
        pw2 = path_walk_carrier(2)
        self.assertEqual(pw2.dimension, 16)
        R = minimal_realization(pw2)
        self.assertEqual(R.dimension, 9)
        rows = [(("u", "u"), (("a", (z1, z2)),)) for z1 in range(4) for z2 in range(4)]
        cols = [(("a", (z1, z2)),) for z1 in range(4) for z2 in range(4)]
        H = hankel_block(pw2, rows, cols)
        self.assertEqual(rank(H), 9)
        F1 = fooling_set_lower_bound(hankel_block(
            path_walk_carrier(1), [("u", (("a", z),)) for z in range(4)],
            [(("a", z),) for z in range(4)]))[1]
        F2 = tensor_fooling_set(F1, (4, 4), F1, (4, 4))
        self.assertEqual(len(F2), 16)
        self.assertTrue(is_fooling_set(H, F2))

    def test_linear_dependence_persists_under_silent_swap(self):
        """f_1 - f_2 - f_3 + f_4 = 0 on every word; the swap preserves it."""
        pw = path_walk_carrier(1)
        eps = (1, -1, -1, 1)
        for w in words_up_to(pw, 4):
            total = sum((eps[i] * pw.probability(f"d{i}", w) for i in range(4)), Q(0))
            self.assertEqual(total, 0)


class TestConeTheorem(unittest.TestCase):
    def test_cone_coordinates_exact_lp(self):
        gens = [vec([1, 0]), vec([1, 1])]
        self.assertEqual(cone_coordinates(gens, vec([3, 1])), (Q(2), Q(1)))
        self.assertIsNone(cone_coordinates(gens, vec([0, 1])))
        self.assertIsNone(cone_coordinates(gens, vec([-1, 0])))

    def test_verify_cone_rejects_unnormalized_and_noninvariant(self):
        pw = path_walk_carrier(1)
        R = minimal_realization(pw)
        gens = [R.vectors[f"d{i}"] for i in range(4)]
        cert = verify_cone(R, gens)
        self.assertTrue(cert.valid)
        car = carrier_from_cone(cert)
        self.assertEqual(car.dimension, 4)
        self.assertTrue(equivalence_certificate(pw, car)["equivalent"])
        bad = verify_cone(R, [tuple(2 * x for x in gens[0])] + gens[1:])
        self.assertFalse(bad.valid)
        self.assertIn("normalized", bad.reason)
        partial = verify_cone(R, gens[:3])
        self.assertFalse(partial.valid)

    def test_cone_carrier_event_matrices_are_stochastic(self):
        pw = path_walk_carrier(1)
        R = minimal_realization(pw)
        cert = verify_cone(R, [R.vectors[f"d{i}"] for i in range(4)])
        for a in cert.event_matrices:
            for i in range(4):
                col = sum((cert.event_matrices[a][z][j][i]
                           for z in cert.event_matrices[a] for j in range(4)), Q(0))
                self.assertEqual(col, 1)


class TestRationalClock(unittest.TestCase):
    def test_minimal_dimension_three_and_mass_conservation(self):
        ck = rational_clock()
        self.assertTrue(ck.mass_conserving())
        self.assertEqual(minimal_realization(ck).dimension, 3)

    def test_all_word_probabilities_nonnegative_to_length_six(self):
        ck = rational_clock()
        for n in range(7):
            for w in itertools.product((TICK, RESET, BOK), repeat=n):
                for s in ("s0", "sstar"):
                    self.assertGreaterEqual(ck.probability(s, w), 0)

    def test_pure_tick_sequence_closed_form(self):
        ck = rational_clock()
        # (4/5) 2^-n (1 + cos(n theta)/4), cos(n theta) = Re((3+4i)/5)^n
        a, b = 1, 0  # (3+4i)^n = a + b i exactly in integers
        for n in range(8):
            cos_n = Q(a, 5 ** n)
            expect = Q(4, 5) * Q(1, 2) ** n * (1 + cos_n / 4)
            self.assertEqual(ck.probability("sstar", (TICK,) * n), expect)
            a, b = 3 * a - 4 * b, 4 * a + 3 * b
            self.assertEqual(b % 5, 4)  # the Lean-checked invariant

    def test_peripheral_obstruction_fires_with_exact_witness(self):
        ck = rational_clock()
        R = minimal_realization(ck)
        cert = peripheral_spectrum_certificate(R, (TICK,))
        self.assertEqual(cert["verdict"], "FINITE_OBSTRUCTION")
        self.assertEqual(cert["lower_bound"], "infinity")
        self.assertEqual(cert["witness"]["det"], Q(1, 4))
        self.assertEqual(cert["witness"]["trace"], Q(3, 5))
        self.assertEqual(charpoly(R.operators["clock"]["tick"]),
                         (Q(1), Q(-11, 10), Q(11, 20), Q(-1, 8)))
        rep = carrier_realization_oracle(ck, obstruction_words=[(TICK,)])
        self.assertEqual(rep["verdict"], "FINITE_OBSTRUCTION")

    def test_reset_word_has_no_obstruction_and_search_is_unresolved(self):
        ck = rational_clock()
        R = minimal_realization(ck)
        self.assertEqual(peripheral_spectrum_certificate(R, (TICK, BOK))["verdict"],
                         "NO_OBSTRUCTION")
        self.assertEqual(reachable_cone_refinement(R, depth=2, max_generators=12)["verdict"],
                         "UNRESOLVED")

    def test_quadratic_root_of_unity_test_exact(self):
        self.assertFalse(quadratic_root_of_unity_test(Q(3, 5), Q(1, 4)))
        self.assertTrue(quadratic_root_of_unity_test(Q(0), Q(1, 4)))     # 90 degrees
        self.assertTrue(quadratic_root_of_unity_test(Q(1, 2), Q(1, 4)))  # 60 degrees
        self.assertTrue(quadratic_root_of_unity_test(Q(2), Q(2)))        # 45 degrees
        with self.assertRaises(RealizationError):
            quadratic_root_of_unity_test(Q(2), Q(1))


class TestCyclotomicClocks(unittest.TestCase):
    """C_k: r = 1 + phi(k), d+ = k exactly."""

    def test_cyclotomic_polynomials(self):
        self.assertEqual(cyclotomic(1), (Q(1), Q(-1)))
        self.assertEqual(cyclotomic(4), (Q(1), Q(0), Q(1)))
        self.assertEqual(cyclotomic(6), (Q(1), Q(-1), Q(1)))
        self.assertEqual(cyclotomic(12), (Q(1), Q(0), Q(-1), Q(0), Q(1)))
        self.assertEqual(euler_phi(30), 8)
        scaled = tuple(c * Q(1, 2) ** i for i, c in enumerate(cyclotomic(10)))
        self.assertEqual(scaled_cyclotomic_order(scaled, Q(1, 2)), 10)
        self.assertIsNone(scaled_cyclotomic_order(scaled, Q(1, 3)))

    def test_family_exact_dimensions(self):
        for k in (4, 6, 8, 10, 12):
            sysk = cyclotomic_clock(k)
            R = minimal_realization(sysk)
            self.assertEqual(R.dimension, 1 + euler_phi(k))
            self.assertTrue(R.mass_conserving())
            cert = peripheral_spectrum_certificate(R, (TICK,))
            self.assertEqual(cert["verdict"], "LOWER_BOUND")
            self.assertEqual(cert["lower_bound"], k)
            R2, cone = orbit_cone_carrier(sysk, "sstar", (TICK,), k)
            self.assertTrue(cone.valid, cone.reason)
            car = carrier_from_cone(cone)
            self.assertEqual(car.dimension, k)
            self.assertTrue(equivalence_certificate(sysk, car)["equivalent"])

    def test_k_minus_one_orbit_generators_do_not_suffice(self):
        for k in (4, 6):
            sysk = cyclotomic_clock(k)
            _, cone = orbit_cone_carrier(sysk, "sstar", (TICK,), k - 1)
            self.assertFalse(cone.valid)

    def test_nonnegative_to_length_five(self):
        sysk = cyclotomic_clock(6)
        for n in range(6):
            for w in itertools.product((TICK, RESET, BOK), repeat=n):
                for s in ("s0", "sstar"):
                    self.assertGreaterEqual(sysk.probability(s, w), 0)

    def test_hankel_is_strictly_positive_so_support_bounds_are_blind(self):
        """Lower bound 6 for C_6 is invisible to any fooling-set argument."""
        sysk = cyclotomic_clock(6)
        _, cone = orbit_cone_carrier(sysk, "sstar", (TICK,), 6)
        car = carrier_from_cone(cone)
        rows = [("sstar", (TICK,) * i) for i in range(6)]
        cols = [(TICK,) * j + (RESET,) for j in range(6)]
        H = hankel_block(car, rows, cols)
        self.assertTrue(all(x > 0 for r in H for x in r))
        self.assertEqual(fooling_set_lower_bound(H)[0], 1)

    def test_prime_order_gives_no_gap(self):
        sysk = cyclotomic_clock(5)
        self.assertEqual(minimal_realization(sysk).dimension, 5)
        self.assertEqual(peripheral_spectrum_certificate(
            minimal_realization(sysk), (TICK,))["lower_bound"], 5)


class TestAvailabilityAndPolicies(unittest.TestCase):
    def test_minimal_failed_square(self):
        fine, coarse = availability_square()
        w = promotion_witness(fine, coarse, 2)
        self.assertEqual(w["source"], "mixed")
        self.assertEqual(w["word"], ())
        self.assertEqual(set(w["fine_menu"]), {"a"})
        self.assertEqual(set(w["coarse_menu"]), {"a", "b"})
        self.assertIsNone(promotion_witness(fine, fine, 2))

    def test_legal_word_probabilities_agree_but_completions_differ(self):
        fine, coarse = availability_square()
        for s in ("pure", "mixed"):
            for u in legality_pattern(fine, s, 3):
                self.assertEqual(fine.probability(s, u), coarse.probability(s, u))
        self.assertEqual(minimal_realization(fine).dimension, 2)
        self.assertEqual(minimal_realization(coarse).dimension, 1)
        self.assertEqual(fine.probability("mixed", (("b", BOT),)), Q(1, 2))
        self.assertEqual(fine.probability("pure", (("b", BOT),)), 0)

    def test_illegal_policy_rejected_in_fine_accepted_in_coarse(self):
        fine, coarse = availability_square()
        with self.assertRaises(RealizationError):
            closed_loop_law(fine, "mixed", lambda u: {"b": Q(1)}, 1)
        self.assertEqual(closed_loop_law(coarse, "mixed", lambda u: {"b": Q(1)}, 1),
                         {(("b", "ok"),): Q(1)})

    def test_closed_loop_transport_for_legal_policies(self):
        fine, coarse = availability_square()
        pol = lambda u: {"a": Q(1)}  # noqa: E731
        for s in ("pure", "mixed"):
            self.assertEqual(closed_loop_law(fine, s, pol, 3), closed_loop_law(coarse, s, pol, 3))
        pw = path_walk_carrier(1)
        R = minimal_realization(pw)
        car = carrier_from_cone(verify_cone(R, [R.vectors[f"d{i}"] for i in range(4)]))

        def randomized(u):
            # public-history randomized policy: weights depend on the history only
            seen = sum(1 for a, z in u if a == "a" and z in (1, 2))
            p = Q(1 + seen, 4) if seen < 3 else Q(1)
            return {"a": p, "b": 1 - p}
        law1 = closed_loop_law(pw, "u", randomized, 3)
        law2 = closed_loop_law(car, "u", randomized, 3)
        self.assertEqual(law1, law2)
        self.assertEqual(sum(law1.values(), Q(0)), 1)

    def test_posterior_is_a_function_of_the_behavior(self):
        pw = path_walk_carrier(1)
        prior = {f"d{i}": Q(1, 4) for i in range(4)}
        post = source_posterior(pw, prior, (("a", 0),))
        self.assertEqual(post, {"d0": Q(1, 2), "d1": Q(1, 2), "d2": Q(0), "d3": Q(0)})
        self.assertIsNone(source_posterior(pw, {"d3": Q(1)}, (("a", 0),)))

    def test_distinguishing_experiment_is_illegal_in_fine(self):
        fine, coarse = availability_square()
        d = distinguishing_experiment(fine, coarse)
        self.assertEqual(d["verdict"], "MORE_EXPERIMENTS_REQUIRED")
        self.assertFalse(d["legal_in_first"])

    def test_bot_is_not_a_sensor(self):
        with self.assertRaises(RealizationError):
            PositiveCarrier((0, 1), {"b": {BOT: ((Q(1), Q(0)), (Q(0), Q(1)))}},
                            {"s": (Q(1, 2), Q(1, 2))}, {"b": (True, False)})


class TestExactness(unittest.TestCase):
    def test_floats_rejected(self):
        from observational_succ.carrier_indexed import CarrierError
        with self.assertRaises(CarrierError):
            PositiveCarrier((0,), {"a": {"z": ((0.5,),)}}, {"s": (1,)})

    def test_rational_roots_and_remainder(self):
        roots, rem = rational_roots_and_remainder((Q(1), Q(-11, 10), Q(11, 20), Q(-1, 8)))
        self.assertEqual(roots, [Q(1, 2)])
        self.assertEqual(rem, (Q(1), Q(-3, 5), Q(1, 4)))

    def test_equivalence_certificate_detects_mutation(self):
        pw = path_walk_carrier(1)
        P = calibration_matrix()
        Pm = mat([list(r) for r in P[:3]] + [[Q(0), Q(1, 2), Q(0), Q(1, 2)]])
        from observational_succ.carrier_realization import observed_chain_events
        mut = PositiveCarrier((0, 1, 2, 3), {"a": observed_chain_events(Pm),
                                             "b": {"s": permutation_event((1, 0, 3, 2))}},
                              dict(pw.preparations))
        eq = equivalence_certificate(pw, mut)
        self.assertFalse(eq["equivalent"])
        self.assertNotEqual(eq["p1"], eq["p2"])

    def test_random_two_state_carriers_have_invariant_dirac_cones(self):
        """Carrier => cone: the state prediction vectors of any positive carrier
        generate a normalized invariant cone in its observable span."""
        rng = random.Random(1185)
        found_two = 0
        for _ in range(30):
            cols = []
            for _c in range(2):
                weights = [Q(rng.randint(0, 3), 3) for _ in range(4)]
                tot = sum(weights, Q(0)) or Q(1)
                cols.append([w / tot for w in weights])
            M0 = ((cols[0][0], cols[1][0]), (cols[0][1], cols[1][1]))
            M1 = ((cols[0][2], cols[1][2]), (cols[0][3], cols[1][3]))
            car = PositiveCarrier((0, 1), {"a": {0: M0, 1: M1}},
                                  {"s": (Q(1, 2), Q(1, 2)), "d0": (1, 0), "d1": (0, 1)})
            R = minimal_realization(car)
            self.assertLessEqual(R.dimension, 2)
            gens = []
            for name in ("d0", "d1"):
                g = R.vectors[name]
                if g not in gens:
                    gens.append(g)
            cert = verify_cone(R, gens)
            self.assertTrue(cert.valid, cert.reason)
            self.assertTrue(equivalence_certificate(car, carrier_from_cone(cert))["equivalent"])
            if R.dimension == 2:
                found_two += 1
        self.assertGreater(found_two, 5)

    def test_refinement_search_never_claims_impossibility(self):
        ck = rational_clock()
        out = reachable_cone_refinement(minimal_realization(ck), depth=1, max_generators=6)
        self.assertIn(out["verdict"], ("UNRESOLVED", "LAWFUL_REALIZATION"))
        self.assertEqual(out["verdict"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
