"""Positive carrier realization, Part II: field of definition, ghost freedom, blind spot.

Exact tests (Fractions and Q(sqrt5) only).  Every theorem-level claim of
research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY_II.md that has a
finite certificate is re-executed here, together with the mutation
controls that break each certificate's hypotheses.
"""
from fractions import Fraction as Q
import unittest

from observational_succ.carrier_field_of_definition import (
    Quad, fibonacci_cat_system, golden_carrier, golden_rays, q_dot, quadratic_cone_carrier,
    rational_interval_invariance, rational_interval_search, rational_root_free,
    two_dimensional_contact_certificate,
)
from observational_succ.carrier_lawful_profile import (
    diagonal_contraction_system, diagonal_triangle_generators, ghost_block_certificate,
    minimal_lawful_phantom, operational_profile, phantom_walk_carrier,
    profile_equivalence_certificate, public_menu, simplicial_grid_search,
    support_uniform_completion, carrier_realization_oracle_ii,
)
from observational_succ.carrier_realization import (
    BOT, LinearSystem, PositiveCarrier, RealizationError, availability_square,
    carrier_from_cone, carrier_realization_oracle, charpoly, closed_loop_law,
    cone_coordinates, dot, equivalence_certificate, mat, matvec, minimal_realization,
    normalize_ray, path_walk_carrier, reachable_cone_refinement, verify_cone,
)


class TestQuadraticField(unittest.TestCase):
    def test_exact_arithmetic_and_order(self):
        r5 = Quad(Q(0), Q(1), 5)
        self.assertEqual(r5 * r5, Quad.of(5, 5))
        phi = (Quad.of(1, 5) + r5) / 2
        self.assertEqual(phi * phi, phi + 1)          # phi^2 = phi + 1
        self.assertTrue(phi > 1 and phi < 2)
        self.assertTrue((phi - Quad(Q(8, 5), Q(0), 5)) > 0)   # phi > 1.6
        self.assertTrue((phi - Quad(Q(13, 8), Q(0), 5)) < 0)  # phi < 1.625
        self.assertEqual((phi.inv() + phi), r5)       # phi + 1/phi = sqrt5
        with self.assertRaises(RealizationError):
            Quad(Q(1), Q(1), 4)

    def test_sign_cases(self):
        self.assertEqual(Quad(Q(2), Q(-1), 5).sign(), -1)   # 2 - sqrt5 < 0
        self.assertEqual(Quad(Q(3), Q(-1), 5).sign(), 1)    # 3 - sqrt5 > 0
        self.assertEqual(Quad(Q(-2), Q(1), 5).sign(), 1)
        self.assertEqual(Quad(Q(0), Q(0), 5).sign(), 0)


class TestFibonacciCatSystem(unittest.TestCase):
    def setUp(self):
        self.fib = fibonacci_cat_system()
        self.R = minimal_realization(self.fib)

    def test_valid_two_dimensional_behavior(self):
        self.assertTrue(self.fib.mass_conserving())
        self.assertEqual(self.R.dimension, 2)
        self.assertTrue(self.R.mass_conserving())
        letters = [(a, z) for a in self.fib.actions for z in self.fib.outcomes(a)]
        frontier = [self.fib.preparations["s"]]
        for _ in range(6):
            nxt = []
            for v in frontier:
                for a, z in letters:
                    u = matvec(self.fib.event(a, z), v)
                    self.assertGreaterEqual(dot(self.fib.mass, u), 0)
                    if any(x != 0 for x in u):
                        nxt.append(u)
            frontier = nxt

    def test_inverse_pair_and_spectrum(self):
        T1 = self.fib.events["a"]["tick"]
        T2 = self.fib.events["b"]["tock"]
        prod = tuple(tuple(sum((T1[i][k] * T2[k][j] for k in range(2)), Q(0)) for j in range(2)) for i in range(2))
        self.assertEqual(prod, ((Q(1, 16), 0), (0, Q(1, 16))))   # tick * tock = I/16
        self.assertEqual(charpoly(T1), (Q(1), Q(-3, 4), Q(1, 16)))
        self.assertEqual(charpoly(T2), (Q(1), Q(-3, 4), Q(1, 16)))
        # tick and tock commute; tick and the b-reset do not
        self.assertEqual(prod, tuple(tuple(sum((T2[i][k] * T1[k][j] for k in range(2)), Q(0)) for j in range(2)) for i in range(2)))
        Rb = self.fib.events["b"]["reset"]
        lhs = tuple(tuple(sum((T1[i][k] * Rb[k][j] for k in range(2)), Q(0)) for j in range(2)) for i in range(2))
        rhs = tuple(tuple(sum((Rb[i][k] * T1[k][j] for k in range(2)), Q(0)) for j in range(2)) for i in range(2))
        self.assertNotEqual(lhs, rhs)

    def test_orbit_slopes_are_fibonacci_ratios(self):
        v = self.fib.preparations["s"]
        slopes = []
        for _ in range(6):
            slopes.append(v[1] / v[0])
            v = matvec(self.fib.events["a"]["tick"], v)
        self.assertEqual(slopes, [Q(0), Q(1, 2), Q(3, 5), Q(8, 13), Q(21, 34), Q(55, 89)])

    def test_golden_carrier_is_an_exact_real_carrier(self):
        c = golden_carrier()
        self.assertTrue(c.intertwining_exact and c.nonnegative and c.column_stochastic
                        and c.preparations_convex)
        self.assertFalse(c.all_entries_rational)
        lam = Quad(Q(3, 8), Q(1, 8), 5)      # (3 + sqrt5)/8
        lam2 = Quad(Q(3, 8), Q(-1, 8), 5)    # (3 - sqrt5)/8
        self.assertEqual(c.event_matrices["a"]["tick"], ((lam, Quad.of(0, 5)), (Quad.of(0, 5), lam2)))
        self.assertEqual(c.event_matrices["b"]["tock"], ((lam2, Quad.of(0, 5)), (Quad.of(0, 5), lam)))
        self.assertEqual(lam + lam2, Quad.of(Q(3, 4), 5))
        self.assertEqual(c.preparations["s"], (Quad(Q(1, 2), Q(1, 10), 5), Quad(Q(1, 2), Q(-1, 10), 5)))

    def test_golden_rays_are_eigenvectors_and_tau_normalized(self):
        e, ep = golden_rays()
        T1 = self.fib.events["a"]["tick"]
        for g, lam in ((e, Quad(Q(3, 8), Q(1, 8), 5)), (ep, Quad(Q(3, 8), Q(-1, 8), 5))):
            img = tuple(sum((Quad.of(T1[i][j], 5) * g[j] for j in range(2)), Quad.of(0, 5)) for i in range(2))
            self.assertEqual(img, tuple(lam * x for x in g))
            self.assertEqual(q_dot(self.fib.mass, g, 5), Quad.of(1, 5))
        # slopes solve s^2 + s - 1 = 0
        for g in (e, ep):
            sl = g[1]
            self.assertTrue((sl * sl + sl - 1).is_zero())

    def test_irrational_contact_certificate(self):
        cert = two_dimensional_contact_certificate(self.fib, (("a", "tick"),), (("b", "tock"),))
        self.assertEqual(cert["verdict"], "FINITE_OBSTRUCTION")
        self.assertEqual(cert["D"], 5)
        self.assertTrue(cert["C1_contact_ray_reachable_limit"])
        self.assertTrue(cert["C2_contact_ray_extreme_in_prediction_cone"])
        self.assertTrue(cert["C3_contact_ray_irrational"])
        # symmetric certificate with the roles of the words exchanged (contact ray e')
        cert2 = two_dimensional_contact_certificate(self.fib, (("b", "tock"),), (("a", "tick"),))
        self.assertEqual(cert2["verdict"], "FINITE_OBSTRUCTION")
        self.assertNotEqual(cert["contact_ray_tau_normalized"], cert2["contact_ray_tau_normalized"])

    def test_contact_certificate_mutation_controls(self):
        # same word twice: the ray is dominant, not subdominant, for word_out -> no certificate
        same = two_dimensional_contact_certificate(self.fib, (("a", "tick"),), (("a", "tick"),))
        self.assertEqual(same["verdict"], "NOT_APPLICABLE")
        # a system with the inverse action removed: P is strictly larger than R near e,
        # the contact condition C2 cannot be certified from a single operator
        only_a = LinearSystem(2, {"a": self.fib.events["a"]}, {"s": self.fib.preparations["s"]}, self.fib.mass)
        c = two_dimensional_contact_certificate(only_a, (("a", "tick"),), (("a", "reset"),))
        self.assertEqual(c["verdict"], "NOT_APPLICABLE")
        # and that system has a RATIONAL two-state carrier (grid finds it): no Q/R gap
        Ro = minimal_realization(only_a)
        self.assertEqual(Ro.dimension, 2)
        found = rational_interval_search(Ro, denominators=(1, 2, 3, 4), bound=3)
        self.assertEqual(found["verdict"], "LAWFUL_REALIZATION")
        car = carrier_from_cone(found["certificate"])
        self.assertTrue(equivalence_certificate(only_a, car)["equivalent"])
        # rational-root check on the golden polynomial, and a control that has a rational root
        self.assertTrue(rational_root_free([Q(1), Q(1), Q(-1)])["no_rational_root"])
        self.assertFalse(rational_root_free([Q(1), Q(-3), Q(2)])["no_rational_root"])

    def test_no_rational_interval_and_creeping_refinement(self):
        for p, q in [(Q(-2), Q(1)), (Q(-17, 10), Q(7, 10)), (Q(-55, 34), Q(55, 89))]:
            self.assertFalse(rational_interval_invariance(self.R, p, q)["invariant_sandwiched"])
        self.assertEqual(rational_interval_search(self.R, denominators=(1, 2, 3, 4, 5, 6), bound=3)["verdict"],
                         "UNRESOLVED")
        res = reachable_cone_refinement(self.R, depth=3, max_generators=12, max_rounds=8)
        self.assertEqual(res["verdict"], "UNRESOLVED")
        self.assertIn("round budget", res["reason"])
        # the creeping generators carry Fibonacci denominators
        dens = {x.denominator for g in res["generators"] for x in g}
        fib_numbers = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
                       6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229}
        self.assertTrue(dens & fib_numbers)


class TestGhostFreedom(unittest.TestCase):
    def test_phantom_profile_is_one_state(self):
        ph = phantom_walk_carrier(1)
        mini = minimal_lawful_phantom(1)
        prof = operational_profile(ph, 3)
        self.assertEqual(prof.menus(), {("b",)})
        self.assertTrue(all(p == 1 for p, _ in prof.entries.values()))
        eq = profile_equivalence_certificate(ph, mini)
        self.assertTrue(eq["same_operational_profile"])
        self.assertEqual(minimal_realization(mini).dimension, 1)
        self.assertEqual(minimal_realization(ph).dimension, 4)
        g = ghost_block_certificate(ph, "sigma", "a")
        self.assertEqual((g["block_rank"], g["fooling_size"], g["bottom_completion_lower_bound"]), (3, 4, 5))
        self.assertFalse(g["action_available_at_source"])
        self.assertEqual(g["refusal_mass"], Q(1, 2))
        # the ghost values are never part of the legal behavior: 'a' is illegal at sigma
        self.assertFalse(ph.legal("sigma", (("a", (0,)),)))
        self.assertEqual(ph.probability("sigma", (("a", (0,)),)), Q(1, 8))   # a ghost value

    def test_phantom_with_legal_source(self):
        ph = phantom_walk_carrier(1, legal_source=True)
        mini = minimal_lawful_phantom(1, legal_source=True)
        eq = profile_equivalence_certificate(ph, mini)
        self.assertTrue(eq["same_operational_profile"])
        self.assertEqual(mini.dimension, 2)
        self.assertTrue(ph.available("eta", (), "a"))
        self.assertFalse(ph.available("sigma", (), "a"))
        prior = {"sigma": Q(1, 2), "eta": Q(1, 2)}
        self.assertEqual(public_menu(ph, prior, ()), ("b",))
        self.assertEqual(public_menu(ph, prior, (("a", (0,)),)), ("a", "b"))
        self.assertEqual(ghost_block_certificate(ph, "sigma", "a")["bottom_completion_lower_bound"], 5)
        # a policy that executes 'a' at the empty history is illegal for sigma in both carriers
        with self.assertRaises(RealizationError):
            closed_loop_law(ph, "sigma", lambda u: {"a": Q(1)}, 1)
        with self.assertRaises(RealizationError):
            closed_loop_law(mini, "sigma", lambda u: {"a": Q(1)}, 1)
        # and the lawful closed-loop law of 'b then b' agrees
        pol = lambda u: {"b": Q(1)}  # noqa: E731
        self.assertEqual(closed_loop_law(ph, "sigma", pol, 2), closed_loop_law(mini, "sigma", pol, 2))

    def test_unbounded_ghost_gap(self):
        ph = phantom_walk_carrier(2)
        g = ghost_block_certificate(ph, "sigma", "a")
        self.assertEqual((g["block_rank"], g["fooling_size"], g["bottom_completion_lower_bound"]), (9, 16, 17))
        self.assertTrue(profile_equivalence_certificate(ph, minimal_lawful_phantom(2))["same_operational_profile"])

    def test_profile_certificate_controls(self):
        fine, coarse = availability_square()
        sq = profile_equivalence_certificate(fine, coarse)
        self.assertFalse(sq["same_operational_profile"])
        self.assertEqual(sq["kind"], "menu_difference")
        self.assertEqual(sq["source"], "mixed")
        pw = path_walk_carrier(1)
        rep = carrier_realization_oracle(pw, proposed_dimension=4)
        self.assertTrue(profile_equivalence_certificate(pw, rep["carrier"])["same_operational_profile"])
        # a legal-value difference: two total one-state carriers with different outcome laws
        k1 = PositiveCarrier((0,), {"a": {"x": ((Q(1, 2),),), "y": ((Q(1, 2),),)}}, {"s": (1,)})
        k2 = PositiveCarrier((0,), {"a": {"x": ((Q(1, 3),),), "y": ((Q(2, 3),),)}}, {"s": (1,)})
        d = profile_equivalence_certificate(k1, k2)
        self.assertFalse(d["same_operational_profile"])
        self.assertEqual(d["kind"], "legal_value_difference")

    def test_support_uniform_completion_realizes_refusal_behavior(self):
        fine, _ = availability_square()
        su = support_uniform_completion(fine)
        self.assertEqual(su.dimension, 3)
        self.assertTrue(all(su.is_total(a) for a in su.actions))
        # refusal is all-or-nothing: at 'mixed', b refuses with probability one
        self.assertEqual(su.probability("mixed", (("b", BOT),)), 1)
        self.assertEqual(su.probability("mixed", (("b", "ok"),)), 0)
        self.assertEqual(su.probability("pure", (("b", "ok"),)), 1)
        # whereas the bottom completion keeps the partial-execution ghost value 1/2
        self.assertEqual(fine.probability("mixed", (("b", "ok"),)), Q(1, 2))
        self.assertEqual(fine.probability("mixed", (("b", BOT),)), Q(1, 2))


class TestBlindSpot(unittest.TestCase):
    def setUp(self):
        self.ds = diagonal_contraction_system()
        self.R = minimal_realization(self.ds)

    def test_dimension_and_non_polyhedral_reachable_cone(self):
        self.assertTrue(self.ds.mass_conserving())
        self.assertEqual(self.R.dimension, 3)
        rays = []
        v = self.R.vectors["sstar"]
        for _ in range(8):
            rays.append(normalize_ray(self.R, v))
            v = matvec(self.R.operators["clock"]["tick"], v)
        axis = normalize_ray(self.R, self.R.vectors["s0"])
        for i, g in enumerate(rays):
            others = [axis] + [h for j, h in enumerate(rays) if j != i]
            self.assertIsNone(cone_coordinates(others, g))

    def test_refinement_stalls_but_triangle_and_grid_succeed(self):
        res = reachable_cone_refinement(self.R, depth=3, max_generators=14)
        self.assertEqual(res["verdict"], "UNRESOLVED")
        cert = verify_cone(self.R, diagonal_triangle_generators(self.R))
        self.assertTrue(cert.valid)
        car = carrier_from_cone(cert)
        self.assertEqual(car.dimension, 3)
        self.assertTrue(equivalence_certificate(self.ds, car)["equivalent"])
        grid = simplicial_grid_search(self.R, system=self.ds, denominators=(1, 2), bound=2, max_candidates=5000)
        self.assertEqual(grid["verdict"], "LAWFUL_REALIZATION")
        car2 = carrier_from_cone(grid["certificate"])
        self.assertTrue(equivalence_certificate(self.ds, car2)["equivalent"])
        # mutation: shrinking the triangle so that it misses v_* breaks the cone
        bad = [tuple(x / 2 if i else x for i, x in enumerate(g)) for g in diagonal_triangle_generators(self.R)]
        bad = [tuple(c / dot(self.R.mass, g) for c in g) for g in bad]
        self.assertFalse(verify_cone(self.R, bad).valid)

    def test_composed_oracle_routes(self):
        fib = fibonacci_cat_system()
        r = carrier_realization_oracle_ii(fib, cone_depth=3, cone_budget=12)
        self.assertEqual((r["verdict"], r["field"]), ("FINITE_OBSTRUCTION", "Q"))
        self.assertEqual(r["positive_dimension_over_R"], 2)
        r = carrier_realization_oracle_ii(self.ds, cone_depth=3, cone_budget=12)
        self.assertEqual((r["verdict"], r["carrier_dimension"]), ("LAWFUL_REALIZATION", 3))
        r = carrier_realization_oracle_ii(path_walk_carrier(1), proposed_dimension=3)
        self.assertEqual(r["verdict"], "UNRESOLVED")   # lower bound 3 from rank only; no fooling block passed
        r = carrier_realization_oracle_ii(path_walk_carrier(1), proposed_dimension=4)
        self.assertEqual((r["verdict"], r["carrier_dimension"]), ("LAWFUL_REALIZATION", 4))
        fine, _ = availability_square()
        r = carrier_realization_oracle_ii(fine)
        self.assertEqual((r["verdict"], r["carrier_dimension"]), ("LAWFUL_REALIZATION", 2))

    def test_grid_search_is_never_an_impossibility_verdict(self):
        fib = fibonacci_cat_system()
        Rf = minimal_realization(fib)
        res = simplicial_grid_search(Rf, denominators=(1, 2), bound=2, max_candidates=100)
        self.assertEqual(res["verdict"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
