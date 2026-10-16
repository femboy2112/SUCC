"""Exact finite instances and hostile controls; no analytic-source sign claims."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product as cartesian
import unittest

from observational_succ import observer_schur as O
from observational_succ.recursive_operator_gluing import block, pd, product, psd, transpose
from observational_succ.source_field_inverse_limits import FieldSourcePassport


def model(rows, source="observer-schur-test-model", epoch=0):
    space = O.RationalSourceSpace(FieldSourcePassport(source, "linear-observation", epoch),
                                  tuple(f"e{i}" for i in range(len(rows))))
    return O.QuadraticModel(space, rows)


def split(a, b, d):
    return O.BlockModel(model(block(a, b, d)), len(a))


class ObserverSchurTests(unittest.TestCase):
    def test_cross_term_kernel_vanishes_but_not_radical(self):
        m = model(((0, 1), (1, 0)))
        obs = O.LinearObservation(m.space, ((1, 0),))
        self.assertEqual(m.energy((0, 7)), 0)
        r = O.energy_factorization(m, obs)
        self.assertFalse(r["factors"])
        u, v = r["witness"]
        self.assertEqual(obs.observe(u), obs.observe(v))
        self.assertNotEqual(m.energy(u), m.energy(v))
        self.assertEqual(r["energies"], (0, 2))

    def test_energy_radical_decoder_and_unreachable_artifact(self):
        m = model(((3, 0), (0, 0)))
        obs = O.LinearObservation(m.space, ((1, 0), (2, 0)))
        self.assertTrue(O.energy_factorization(m, obs)["factors"])
        self.assertEqual(O.decode_energy(m, obs, (2, 4)), 12)
        with self.assertRaises(O.ObserverSchurError):
            O.decode_energy(m, obs, (2, 3))

    def test_constant_observation_nonconstant_target(self):
        m = model(((1, 0), (0, 0)))
        obs = O.LinearObservation(m.space, ((0, 0),))
        self.assertFalse(O.energy_factorization(m, obs)["factors"])
        with self.assertRaises(O.ObserverSchurError):
            O.decode_energy(m, obs, (0,))

    def test_joint_linear_observations_restore_factorization(self):
        m = model(((1, 0), (0, -1)))
        for rows in (((1, 0),), ((0, 1),)):
            self.assertFalse(O.energy_factorization(m, O.LinearObservation(m.space, rows))["factors"])
        joint = O.LinearObservation(m.space, ((1, 0), (0, 1)))
        self.assertTrue(O.energy_factorization(m, joint)["factors"])

    def test_source_epoch_and_basis_are_load_bearing(self):
        m = model(((1, 0), (0, 0)))
        other = model(m.gram, epoch=1)
        with self.assertRaises(O.ObserverSchurError):
            O.energy_factorization(m, O.LinearObservation(other.space, ((1, 0),)))
        reordered = replace(m.space, basis=("e1", "e0"))
        with self.assertRaises(O.ObserverSchurError):
            O.energy_factorization(m, O.LinearObservation(reordered, ((1, 0),)))
        self.assertNotEqual(m.fingerprint, other.fingerprint)

    def test_hash_and_source_token_do_not_issue_authority(self):
        m = model(((1, 0), (0, 1)), source="PINNED_ORIGINAL_SUZUKI")
        r = O.energy_factorization(m, O.LinearObservation(m.space, ((1, 0),)))
        self.assertFalse(r["factors"])
        self.assertFalse(r["source_identification_discharged"])
        self.assertFalse(r["Lean_kernel_replayed"])
        self.assertFalse(r["infinite_operator_sign_certified"])

    def test_float_boolean_nonsymmetric_and_budget_rejection(self):
        for rows in (((1.0, 0), (0, 1)), ((True, 0), (0, 1)), ((0, 1), (0, 0))):
            with self.assertRaises(O.ObserverSchurError):
                model(rows)
        with self.assertRaises(O.ObserverSchurError):
            O.kernel_basis([[0]*9])
        with self.assertRaises(O.ObserverSchurError):
            split(((1,),), ((0,),), ((-1,),))

    def test_nullspace_and_solve_are_complete(self):
        a = ((1, 2, 3), (2, 4, 6))
        self.assertEqual(O.kernel_basis(a), ((-2, 1, 0), (-3, 0, 1)))
        self.assertEqual(O.solve_linear(a, (5, 10)), (5, 0, 0))
        self.assertIsNone(O.solve_linear(a, (5, 9)))
        self.assertEqual(O.kernel_basis(((1, 0), (0, 1))), ())

    def test_sign_positive_form_is_constant_but_energy_hidden(self):
        s = split(((1,),), ((0,),), ((1,),))
        self.assertTrue(O.sign_factorization(s)["factors"])
        self.assertFalse(O.energy_factorization(s.model, s.observation)["factors"])

    def test_sign_d_zero_allows_indefinite_low(self):
        s = split(((1, 0), (0, -1)), ((0,), (0,)), ((0,),))
        r = O.sign_factorization(s)
        self.assertTrue(r["factors"])
        self.assertEqual(r["case"], "D_ZERO_B_ZERO")
        self.assertFalse(psd(s.a))
        self.assertTrue(O.energy_factorization(s.model, s.observation)["factors"])

    def test_sign_d_zero_cross_mutant(self):
        s = split(((0,),), ((1,),), ((0,),))
        r = O.sign_factorization(s)
        self.assertFalse(r["factors"])
        self.assertEqual(r["energies"], (-1, 1))

    def test_positive_diagonal_blocks_negative_schur(self):
        s = split(((1,),), ((2,),), ((1,),))
        r = O.schur_envelope(s)
        self.assertTrue(pd(s.a) and pd(s.d))
        self.assertEqual(r["schur"], ((-3,),))
        self.assertFalse(O.contraction_certificate(s)["contraction_at_most_one"])
        sign = O.sign_factorization(s)
        self.assertFalse(sign["factors"])
        self.assertLess(sign["energies"][0], 0)
        self.assertGreater(sign["energies"][1], 0)

    def test_singular_range_failure_and_fiber_specific_finiteness(self):
        s = split(((1, 0), (0, 1)), ((1, 0), (0, 1)), ((1, 0), (0, 0)))
        self.assertFalse(O.schur_envelope(s)["all_fibers_finite"])
        self.assertTrue(O.fiber_envelope(s, (1, 0))["finite"])
        r = O.fiber_envelope(s, (0, 1))
        self.assertFalse(r["finite"])
        self.assertEqual(r["ray_linear_coefficient"], -2)
        for t in (0, 1, 3, 100):
            high = tuple(t*z for z in r["hidden_ray"])
            self.assertEqual(s.model.energy((0, 1)+high), 1-2*t)

    def test_singular_valid_range_and_nonunique_minimizers(self):
        s = split(((3,),), ((2, 0),), ((2, 0), (0, 0)))
        r = O.schur_envelope(s)
        self.assertTrue(r["all_fibers_finite"])
        self.assertEqual(r["schur"], ((1,),))
        env = O.fiber_envelope(s, (2,))
        self.assertEqual(env["value"], 4)
        for z in (-99, 0, 37):
            self.assertEqual(s.model.energy((2, -2, z)), 4)

    def test_completed_square_by_direct_polynomial_expansion(self):
        # Independent enumeration evaluates original block coefficients directly.
        s = split(((7, 2), (2, 5)), ((1, 2), (3, -1)), ((2, 1), (1, 3)))
        r = O.schur_envelope(s)
        for values in cartesian((-2, 0, 1), repeat=4):
            x, h = values[:2], values[2:]
            z = tuple(h[i]+sum(r["response_map"][i][j]*x[j] for j in range(2)) for i in range(2))
            rhs = O.quadratic(r["schur"], x)+O.quadratic(s.d, z)
            lhs = sum(F(values[i])*s.model.gram[i][j]*values[j] for i in range(4) for j in range(4))
            self.assertEqual(lhs, rhs)

    def test_sign_classification_exhaustive_scalar_blocks(self):
        count = 0
        for a, b, d in cartesian(range(-2, 3), range(-3, 4), range(4)):
            s = split(((a,),), ((b,),), ((d,),))
            expected = b == 0 if d == 0 else (a >= 0 and a*d-b*b >= 0)
            r = O.sign_factorization(s)
            self.assertEqual(r["factors"], expected)
            if not expected:
                u, v = r["witness"]
                self.assertEqual(u[:1], v[:1])
                self.assertLess(s.model.energy(u), 0)
                self.assertGreater(s.model.energy(v), 0)
            count += 1
        self.assertEqual(count, 140)

    def test_independent_negative_direction_vs_principal_minors(self):
        # Different criterion: congruence elimination vs ALL principal minors.
        for a, b, c, d, e, f in cartesian((-1, 0, 1), repeat=6):
            g = ((a, b, c), (b, d, e), (c, e, f))
            v = O.negative_direction(g)
            self.assertEqual(v is None, psd(g))
            if v is not None:
                self.assertLess(O.quadratic(g, v), 0)

    def test_two_by_two_determinant_does_not_suffice_alone(self):
        r = O.psd_two_by_two(((-1, 0), (0, -1)))
        self.assertEqual(r["determinant"], 1)
        self.assertFalse(r["psd"])
        self.assertTrue(O.psd_two_by_two(((1, 1), (1, 1)))["psd"])
        self.assertFalse(O.psd_two_by_two(((0, 1), (1, 0)))["psd"])

    def test_complex_paper_completion_conjugation_mutant(self):
        # Exact Gaussian rational pairs; production matrices remain real only.
        def add(z, w):
            return (z[0]+w[0], z[1]+w[1])
        def mul(z, w):
            return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
        def conj(z):
            return (z[0], -z[1])
        def norm(z):
            return z[0]**2+z[1]**2
        one, i = (F(1), F(0)), (F(0), F(1))
        x, y, z = i, one, i
        gx = add(x, mul(z, y))
        gy = add(mul(conj(z), x), y)
        true_q = add(mul(conj(x), gx), mul(conj(y), gy))
        self.assertEqual(true_q, (4, 0))
        self.assertEqual(norm(add(x, mul(z, y))), 4)
        self.assertEqual(norm(add(x, mul(conj(z), y))), 0)
        with self.assertRaises(O.ObserverSchurError):
            O.psd_two_by_two(((1, 1j), (-1j, 1)))

    def test_contraction_boundary_and_positive_a_gate(self):
        for b, expected in ((F(1, 2), True), (F(1), True), (F(3, 2), False)):
            s = split(((1,),), ((b,),), ((1,),))
            r = O.contraction_certificate(s)
            self.assertEqual(r["contraction_at_most_one"], expected)
        with self.assertRaises(O.ObserverSchurError):
            O.contraction_certificate(split(((0,),), ((0,),), ((1,),)))
        with self.assertRaises(O.ObserverSchurError):
            O.contraction_certificate(split(((1,),), ((1,),), ((0,),)))

    def test_full_parity_not_just_low_symmetry(self):
        a = ((2, 0, 1, 0), (0, 2, 0, 1), (1, 0, 2, 0), (0, 1, 0, 2))
        b = ((1, 0), (0, 1), (1, 0), (0, 1))
        s = split(a, b, ((2, 0), (0, 2)))
        signs = (-1, 1, -1, 1, -1, 1)
        sectors = O.parity_sectors(s, signs)
        self.assertEqual(tuple(z["low_indices"] for z in sectors), ((0, 2), (1, 3)))
        self.assertTrue(all(O.psd_two_by_two(z["schur"])["psd"] for z in sectors))
        wrong = split(a, ((1, 1),)+b[1:], ((2, 0), (0, 2)))
        with self.assertRaises(O.ObserverSchurError):
            O.parity_sectors(wrong, signs)

    def test_parity_does_not_discharge_range(self):
        s = split(((1,),), ((1,),), ((0,),))
        with self.assertRaises(O.ObserverSchurError):
            O.parity_sectors(s, (1, 1))

    def test_negative_sufficient_lower_is_not_negative_schur(self):
        s = split(((2,),), ((1,),), ((1,),))
        r = O.trial_enclosure(s, ((0,),), ((1,),), F(1, 10))
        self.assertEqual(r["lower"], ((-8,),))
        self.assertEqual(r["upper"], ((2,),))
        self.assertEqual(r["exact_schur"], ((1,),))
        self.assertFalse(r["sufficient_lower_psd"])
        self.assertTrue(r["exact_schur_psd"])

    def test_exact_response_closes_trial_bracket(self):
        s = split(((2,),), ((1,),), ((1,),))
        r = O.trial_enclosure(s, ((1,),), ((1,),), F(1, 10))
        self.assertEqual(r["lower"], r["upper"])
        self.assertEqual(r["residual"], ((0,),))
        with self.assertRaises(O.ObserverSchurError):
            O.trial_enclosure(s, ((0,),), ((1,),), 2)

    def test_bounded_linear_factorization_and_kernel_failure(self):
        m = model(((0, 0), (0, 0)))
        obs = O.LinearObservation(m.space, ((1, 0),))
        r = O.linear_factorization(obs, ((2, 0),), 2)
        self.assertTrue(r["factors"] and r["bound_valid"])
        self.assertEqual(r["decoder_rows"], ((2,),))
        self.assertFalse(O.linear_factorization(obs, ((0, 1),))["factors"])
        self.assertFalse(O.linear_factorization(obs, ((2, 0),), 1)["bound_valid"])

    def test_diagonal_decoder_bound_grows_at_every_finite_stage(self):
        for n in range(1, 9):
            ident = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
            rows = tuple(tuple(F(int(i == j), i+1) for j in range(n)) for i in range(n))
            obs = O.LinearObservation(model(ident).space, rows)
            self.assertTrue(O.linear_factorization(obs, ident, n)["bound_valid"])
            self.assertFalse(O.linear_factorization(obs, ident, F(2*n-1, 2))["bound_valid"])

    def test_nonattainment_example_finite_prefix_identity(self):
        # Infinite theorem is in the paper; these exact sums only check prefixes.
        for n in (1, 2, 3, 7):
            partial = sum((F(1, 4**k) for k in range(1, n+1)), F())
            self.assertEqual(F(1, 3)-partial, F(1, 3*4**n))
        self.assertGreater(F(1, 3*4**7), 0)


if __name__ == "__main__":
    unittest.main()
