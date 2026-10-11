import json
import random
import unittest
from fractions import Fraction as Q

from observational_succ import (AffineChart, BasisLift, BudgetExceeded, DomainError,
                           Engine, Frame, I, ONE, Operation, Scalar, execute)


class FieldTests(unittest.TestCase):
    def test_natural_inverse_boundary(self):
        with self.assertRaises(DomainError): Frame().succ(0, -1)
        self.assertEqual(Frame().succ(1, -1), (Q(0),))

    def test_integer_negative_successor(self):
        f = Frame("Z", "integer")
        self.assertEqual(f.succ(0, -1), (-1,))
        self.assertEqual(f.succ(-1), (0,))

    def test_cycles_have_distinct_events(self):
        for m in [2, 3, 5, 6, 11]:
            e = Engine(Frame(f"Z/{m}Z", "modular", (1,), m))
            for _ in range(2*m): e.advance(context="same")
            self.assertEqual(e.coordinate, (0,))
            self.assertEqual(e.state["tick"], 2*m)
            self.assertEqual(len(e.shadow_inverse()["witnesses"]), 2)
            self.assertFalse(e.shadow_inverse()["unique_event"])
            self.assertEqual(len({json.loads(r.after)["pending"]["event"] for r in e.records if r.kind == "step"}), 2*m)

    def test_vector_steps(self):
        f = Frame("Q2", "rational", (Q(1, 2), Q(-2, 3)))
        self.assertEqual(f.succ((0, 0)), (Q(1, 2), Q(-2, 3)))
        self.assertEqual(f.succ(f.succ((0, 0)), -1), (0, 0))

    def test_invalid_field_inputs(self):
        for factory in [lambda: Frame(step=(0,)), lambda: Frame(domain="physical continuum"),
                        lambda: Frame("bad", "modular", (2,), 2), lambda: Frame(step=(Q(1, 2),)),
                        lambda: Frame().point(1.1), lambda: Frame().point(True),
                        lambda: Frame().point((1, 2)), lambda: Frame().succ(1, 0),
                        lambda: Frame().succ(1, True)]:
            with self.assertRaises(DomainError): factory()

    def test_modular_division_is_partial(self):
        f = Frame("Z6", "modular", (1,), 6)
        with self.assertRaises(DomainError): f.scale(4, 2, inverse=True)
        self.assertEqual(f.scale(f.scale(2, 5), 5, inverse=True), (2,))

    def test_integer_division_is_not_rounding(self):
        with self.assertRaises(DomainError): Frame().scale(3, 2, inverse=True)
        self.assertEqual(Frame().scale(4, 2, inverse=True), (2,))

    def test_history_horizons(self):
        short = execute(Frame(), 2, [Operation("divide", 2), Operation("multiply", 2)])
        long = execute(Frame(), 2, [Operation("multiply", 2), Operation("divide", 2)])
        self.assertEqual(short.states[-1], long.states[-1])
        self.assertTrue(short.fits(2))
        self.assertFalse(long.fits(2))
        self.assertTrue(long.fits(4))
        self.assertEqual(long.reverse().states, tuple(reversed(long.states)))

    def test_path_no_fake_inverse(self):
        with self.assertRaises(DomainError): execute(Frame(), 3, [Operation("divide", 2)])
        with self.assertRaises(DomainError): Operation("succ", 2)
        with self.assertRaises(BudgetExceeded): execute(Frame(), 0, [Operation("succ")]*3, 2)

    def test_frame_covariance_holdouts(self):
        rng = random.Random(9173)
        for dim in [1, 2, 3, 7]:
            for _ in range(25):
                e = tuple(Q(rng.randint(1, 5), rng.randint(1, 7)) for _ in range(dim))
                f = Frame("Q", "rational", e)
                x = tuple(Q(rng.randint(-10, 10), 3) for _ in range(dim))
                a = tuple(Q(rng.choice([-3, -2, 1, 2, 5]), 2) for _ in range(dim))
                b = tuple(Q(rng.randint(-3, 3), 5) for _ in range(dim))
                chart = AffineChart(a, b)
                other = chart.frame(f)
                self.assertEqual(chart.point(f.succ(x)), other.succ(chart.point(x)))
                self.assertEqual(chart.inverse().point(chart.point(x)), x)
                # Deliberately unchanged unit direction is NOT covariance.
                if a != (1,)*dim:
                    self.assertNotEqual(chart.point(f.succ(x)), f.succ(chart.point(x)))

    def test_arithmetic_adapter_not_on_residue_labels(self):
        with self.assertRaises(DomainError): Engine(Frame("F2", "modular", (1,), 2), arithmetic=True)
        with self.assertRaises(DomainError): Engine(Frame(step=(2,)), arithmetic=True)

    def test_exact_scalar_and_lift(self):
        self.assertEqual(I*I, Scalar(-1))
        self.assertEqual((Scalar(2, 3)/Scalar(2, 3)), ONE)
        self.assertEqual(Scalar.from_data(Scalar("2/3", "-1/7").data()), Scalar("2/3", "-1/7"))
        lift = BasisLift("rotation", ((Q(3, 5), Q(-4, 5)), (Q(4, 5), Q(3, 5))), (ONE, I))
        x = lift.initial
        for _ in range(12): x = lift.apply(x)
        for _ in range(12): x = lift.apply(x, -1)
        self.assertEqual(x, lift.initial)
        with self.assertRaises(DomainError): BasisLift("bad", (("101/100",),), (1,))


if __name__ == "__main__": unittest.main()
