import dataclasses
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.minimal_observation import (
    FiniteObservation, FactorizationCertificate, ObservationError,
    compile_factorization, replay_factorization, decode, minimum_in_menu,
    chi4_observation, PrimitiveRealCharacter, newton_coefficients,
    newton_value, polynomial_descent,
)
from observational_succ.minimal_weil_window import (
    minimum_arithmetic_window, autocorrelation_atom_witness, integer_log_bounds,
)
from observational_succ.tate_chi4 import Chi4TateSource, two_adic_hecke, ramified_test


class FactorizationTests(unittest.TestCase):
    def test_all_binary_tables(self):
        for n in range(5):
            for obs in product((0, 1), repeat=n):
                for target in product((0, 1), repeat=n):
                    p = FiniteObservation("entire finite source", 3, obs, target)
                    c = compile_factorization(p)
                    self.assertTrue(replay_factorization(p, c))
                    # A separate brute force decoder enumeration, not the fiber algorithm.
                    decoders = [d for d in product((0, 1), repeat=2)
                                if all(d[obs[i]] == target[i] for i in range(n))]
                    self.assertEqual(c.outcome == "PROVEN_FACTORIZATION", bool(decoders))

    def test_source_and_authority_forgery(self):
        p = FiniteObservation("source", 2, (0, 0, 1), (2, 2, 3))
        c = compile_factorization(p)
        for other in (dataclasses.replace(p, epoch=3), dataclasses.replace(p, source_id="alias"),
                      dataclasses.replace(p, laws=("different domain",))):
            self.assertFalse(replay_factorization(other, c))
        for forged in (dataclasses.replace(c, authority="LEAN_KERNEL_PROVED"),
                       dataclasses.replace(c, decoder=((0, 3), (1, 3))),
                       dataclasses.replace(c, decoder=((0, 2), (1, 3), (2, 0))),
                       dataclasses.replace(c, decoder=((0, 2), (1, 3), (1, 3)))):
            self.assertFalse(replay_factorization(p, forged))

    def test_unreachable_and_empty_coimage(self):
        p = FiniteObservation("empty", 0, (), ())
        c = compile_factorization(p)
        self.assertTrue(replay_factorization(p, c))
        with self.assertRaises(ObservationError):
            decode(c, "unreachable")
        with self.assertRaises(ObservationError):
            FiniteObservation("bad", 0, (False,), (0,))

    def test_false_collision_and_bool_alias(self):
        p = FiniteObservation("s", 0, (0, 1), (0, 1))
        c = compile_factorization(p)
        self.assertFalse(replay_factorization(p, dataclasses.replace(c, decoder=((0, False), (1, 1)))))
        self.assertFalse(replay_factorization(p, FactorizationCertificate(p.digest, "REFUTED", collision=(0, 1))))

    def test_least_menu_and_joint_obstruction(self):
        p = FiniteObservation("s", 0, (0, 1, 2, 3), (0, 0, 1, 1))
        r = minimum_in_menu(p, ((0, 1, 2, 3), (0, 0, 1, 1), (7, 7, 7, 7)))
        self.assertEqual(r["least_indices"], (1,))
        self.assertEqual(r["outcome"], "PROVEN_MINIMUM_IN_MENU")
        self.assertEqual(minimum_in_menu(p, ((0, 0, 0, 0),))["outcome"], "PROVEN_TOOLKIT_OBSTRUCTION")
        incomparable = minimum_in_menu(p, ((0, 1, 2, 2), (0, 0, 1, 2)))
        self.assertEqual(incomparable["outcome"], "UNRESOLVED_MINIMUM_IN_MENU")
        xor = dataclasses.replace(p, target=(0, 1, 1, 0))
        joint = minimum_in_menu(xor, ((0, 0, 1, 1), (0, 1, 0, 1)))
        self.assertEqual(joint["joint_certificate"].outcome, "PROVEN_FACTORIZATION")
        self.assertEqual(joint["outcome"], "UNRESOLVED_MINIMUM_IN_MENU")


class ArithmeticObservationTests(unittest.TestCase):
    def test_chi4_all_moduli_and_large_integer(self):
        table = (0, 1, 0, -1)
        for n in tuple(range(1, 129)) + (10**30, 10**30+1, 10**30+2):
            c = chi4_observation(n, Chi4TateSource("original", 8))
            self.assertEqual(c["outcome"] == "PROVEN_FACTORIZATION", n % 4 == 0)
            self.assertEqual((c["source_id"], c["epoch"]), ("original", 8))
            if c["collision"]:
                s, t = c["collision"]
                self.assertEqual(s % n, t % n)
                self.assertNotEqual(table[s % 4], table[t % 4])
            else:
                self.assertTrue(all(table[x % 4] == table[(x+n) % 4] for x in range(-16, 17)))
        for n in (0, -1, True, 4.0):
            with self.assertRaises(ObservationError):
                chi4_observation(n)

    def test_ramified_component_distinction(self):
        self.assertEqual(ramified_test(2), 0)
        self.assertEqual(two_adic_hecke(2), 1)
        self.assertEqual(two_adic_hecke(6), -1)
        self.assertEqual(ramified_test(3), -1)

    def test_primitive_family_and_imprimitive_trap(self):
        tables = ((0, 1, -1), (0, 1, 0, -1), (0, 1, -1, -1, 1),
                  (0, 1, 0, -1, 0, -1, 0, 1))
        for table in tables:
            chi = PrimitiveRealCharacter(table)
            for n in range(1, 81):
                result = chi.observation(n)
                self.assertEqual(result["collision"] is None, n % len(table) == 0)
                if result["collision"]:
                    a, b = result["collision"]
                    self.assertEqual(a % n, b % n)
                    self.assertNotEqual(table[a % len(table)], table[b % len(table)])
        for bad in ((0, 1, 1), (0, 1, -1, 0), (0, 1, 0, 1)):
            with self.assertRaises(ObservationError):
                PrimitiveRealCharacter(bad)

    def test_newton_interpolation_and_negative_inputs(self):
        # Independent monomial oracle includes integer-valued rational coefficients.
        functions = (lambda x: x*x-3*x+2, lambda x: x*(x-1)//2,
                     lambda x: x*(x-1)*(x-2)//6 + 4*x)
        for f in functions:
            coeff = newton_coefficients(tuple(f(x) for x in range(5)))
            for x in range(-20, 21):
                self.assertEqual(newton_value(coeff, x), f(x))

    def test_basis_ablation_and_quotient_descent(self):
        for d in range(5):
            for omitted in range(d+1):
                values = tuple(int(j == omitted) for j in range(d+1))
                c = newton_coefficients(values)
                self.assertEqual(tuple(newton_value(c, j) for j in range(d+1)), values)
        self.assertEqual(polynomial_descent((0, 0, 1), 2)["collision"], (0, 2))
        for c in product(range(-1, 2), repeat=4):
            for n in range(1, 7):
                outcome = polynomial_descent(c, n)
                brute = all((newton_value(c, x+n)-newton_value(c, x)) % n == 0
                            for x in range(-20, 21))
                self.assertEqual(outcome["outcome"] == "PROVEN_DESCENT", brute)


class ArithmeticWindowTests(unittest.TestCase):
    def test_genuine_source_windows(self):
        self.assertEqual(minimum_arithmetic_window(Q(1, 12))["active"], ())
        self.assertEqual(tuple(n for n, _, _ in minimum_arithmetic_window(Q(1, 2))["active"]), (2,))
        self.assertEqual(tuple(n for n, _, _ in minimum_arithmetic_window(1)["active"]), (2, 3, 4, 5, 7))
        for a in (Q(1, 2), Q(1), Q(3, 2)):
            window = minimum_arithmetic_window(a)
            for n, _, _ in window["active"]:
                w = autocorrelation_atom_witness(a, n)
                e = w["epsilon"]
                lo, hi = w["log_interval"]
                self.assertLess(hi/2+e, a)
                self.assertGreater(lo, 2*e)
                for m, _, (ml, mh) in window["active"]:
                    self.assertGreater(ml, 2*e)
                    if m != n:
                        self.assertTrue(mh+2*e < lo or hi+2*e < ml)
                self.assertGreater(w["unit_paired_coefficient_response_abs_lower_strict"], 0)
        for n in (6, 9):
            with self.assertRaises(ValueError):
                autocorrelation_atom_witness(Q(1, 2), n)

    def test_unresolved_endpoint_does_not_guess(self):
        lo, hi = integer_log_bounds(2, terms=1)
        a = (lo+hi)/4
        result = minimum_arithmetic_window(a, terms=1)
        self.assertEqual(result["outcome"], "UNRESOLVED")
        self.assertEqual(result["unresolved"][0][0], 2)
        self.assertEqual(autocorrelation_atom_witness(a, 2, terms=1)["outcome"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
