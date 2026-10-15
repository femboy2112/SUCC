"""Exact orthogonal complementary SUCC tower tests; no zeta-zero input."""
import unittest
from fractions import Fraction as Q
from observational_succ.dual_shell_observer import (
    DualShellError, add, project_level, decompose_shells, inner,
    shift_pullback, noncommuting_boundary_witness,
    meeting_certificate, late_hidden_source,
)


class DualShellObserverTests(unittest.TestCase):
    def test_source_reconstruction_and_parseval(self):
        sources = [{1: Q(1)}, {2: Q(1)},
                   {1: Q(1, 2), 2: Q(1, 3), 5: Q(-1, 7), 9: Q(1, 6)},
                   {k: Q((-1)**k, k+1) for k in range(1, 27)}, {}]
        for q in (2, 3, 5, 6):
            for f in sources:
                r = decompose_shells(f, q)
                self.assertTrue(r["reconstruction_exact"])
                self.assertTrue(r["Parseval_exact"])
                self.assertTrue(r["orthogonal"])
                self.assertEqual(sum(r["squared_norms"], Q()),
                                 r["source_squared_norm"])
                self.assertFalse(r["RH_proved"])

    def test_nested_projection_law_exact(self):
        f = {1: Q(2), 2: Q(-1), 5: Q(1, 4),
             6: Q(3, 7), 11: Q(2, 3)}
        for q in (2, 3):
            for a in range(4):
                for b in range(4):
                    self.assertEqual(
                        project_level(project_level(f, q, a), q, b),
                        project_level(f, q, max(a, b)))

    def test_range_vs_wandering_observation(self):
        f = {2: Q(1), 3: Q(-1, 2), 5: Q(3, 5)}
        p = project_level(f, 2, 1)
        w = add(f, p, -1)
        self.assertEqual(inner(p, w), 0)
        self.assertEqual(project_level(w, 2, 1), {})

    def test_additive_successor_does_not_commute(self):
        c = noncommuting_boundary_witness()
        self.assertEqual(c["commutator_at_cell_1"], "2/3")
        self.assertFalse(c["naive_additive_gluing_commutes"])
        f = {2: Q(1)}
        self.assertNotEqual(shift_pullback(project_level(f, 2, 1)),
                            project_level(shift_pullback(f), 2, 1))

    def test_two_observer_meeting_at_exact_boundary(self):
        f = {1: Q(1, 2), 3: Q(-2, 7),
             7: Q(5, 8), 15: Q(2, 3)}
        for q in (2, 3):
            for n in range(4):
                c = meeting_certificate(f, q, n)
                self.assertTrue(c["boundary_glued_exactly"])
                self.assertEqual(c["source_squared_norm"],
                                 c["resolved_squared_norm"] +
                                 c["tail_squared_norm"])

    def test_any_finite_dual_front_misses_some_source(self):
        for q, depth in ((2, 1), (2, 3), (2, 6), (3, 2), (5, 2)):
            f = late_hidden_source(q, depth)
            c = meeting_certificate(f, q, depth)
            self.assertEqual(c["resolved"], {})
            self.assertEqual(c["tail"], f)
            self.assertGreater(c["tail_squared_norm"], 0)
            final = decompose_shells(f, q)
            self.assertTrue(all(not s for s in final["shells"][:depth]))
            self.assertTrue(final["shells"][depth])

    def test_mutations_and_invalid_sources(self):
        for f, q in (({0: Q(1)}, 2), ({1: 0.1}, 2),
                     ({1: Q(1)}, 1), ({1: Q(1)}, 51)):
            with self.assertRaises(DualShellError):
                decompose_shells(f, q)
        with self.assertRaises(DualShellError):
            project_level({100_000: Q(1)}, 10, 5)


if __name__ == "__main__":
    unittest.main()
