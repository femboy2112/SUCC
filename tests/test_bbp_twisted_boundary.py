"""Exact seam, pole, boundary-layer, and source-selection controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_cyclotomic_birth import p_primary_phase
from observational_succ.bbp_resonance_controls import (
    authentic_history_failures, exact_forced_history,
)
from observational_succ.bbp_source_memory import tail_interval
from observational_succ.bbp_twisted_boundary import (
    affine_repeat_defect, generating_identity_certificate,
    generating_pole_residue_interval, reciprocal_reversal_certificate,
    solve_affine_seam, source_commuting_affine, twisted_boundary_certificate,
)


def direct_forcing(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def independent_history(N, initial=Q()):
    """Closed convolution, independent of the production forward recurrence."""
    return tuple(16**n * initial + sum(
        (16**(n-k) * direct_forcing(k) for k in range(1, n+1)), Q())
        for n in range(N+1))


class AffineSeamTests(unittest.TestCase):
    def test_unique_seams_against_independent_convolution(self):
        for N in (1, 3, 8, 17):
            for lam, beta in ((-1, 0), (1, 0), (Q(2, 3), Q(7, 11)), (16**N+1, -2)):
                solved = solve_affine_seam(N, lam, beta)
                self.assertEqual(solved["kind"], "unique")
                states = independent_history(N, solved["initial"])
                self.assertEqual(states[-1], lam*states[0]+beta)
                self.assertEqual(authentic_history_failures(states), ("initial-state",))
                self.assertNotEqual(states[-1], lam*states[0]+beta+Q(1, 13))

    def test_singular_cases_do_not_divide_by_zero_or_choose_a_seed(self):
        for N in (1, 4, 11):
            U_N = independent_history(N)[-1]
            all_states = solve_affine_seam(N, 16**N, U_N)
            self.assertEqual(all_states["kind"], "all")
            self.assertIsNone(all_states["initial"])
            self.assertTrue(all_states["authentic_compatible"])
            for c in (Q(), Q(1, 3), Q(-11, 7)):
                states = independent_history(N, c)
                self.assertEqual(states[-1], 16**N*c+U_N)
            impossible = solve_affine_seam(N, 16**N, U_N+1)
            self.assertEqual(impossible["kind"], "none")
            self.assertFalse(impossible["authentic_compatible"])

    def test_authentic_seed_requires_exact_source_offset(self):
        for N in (2, 7, 16):
            U_N = independent_history(N)[-1]
            for lam in (-1, 0, 1, Q(5, 3)):
                authentic = solve_affine_seam(N, lam, U_N)
                self.assertEqual(authentic["initial"], 0)
                self.assertTrue(authentic["authentic_compatible"])
                self.assertFalse(solve_affine_seam(N, lam, U_N+Q(1, 19))[
                    "authentic_compatible"])
                self.assertEqual(authentic_history_failures(independent_history(N)), ())

    def test_one_endpoint_seam_does_not_repeat_forcing(self):
        for N in (1, 2, 8, 31):
            for lam in (-1, 1):
                seam = solve_affine_seam(N, lam)
                states = independent_history(N+1, seam["initial"])
                defect = states[N+1] - lam*states[1]
                self.assertEqual(defect, affine_repeat_defect(N, lam))
                self.assertEqual(defect, direct_forcing(N+1)-lam*direct_forcing(1))
                self.assertNotEqual(defect, 0)
                self.assertGreater(defect, 0) if lam == -1 else self.assertLess(defect, 0)

    def test_twist_changes_even_the_first_prime_birth_clock(self):
        for p in (17, 41, 73, 97):
            m, N = (p-1)//8, 4*((p-1)//8)
            seam = solve_affine_seam(N, -1)
            states = independent_history(N, seam["initial"])
            self.assertNotEqual(p_primary_phase(states[0], p), 0)
            for t, state in enumerate(states[m+1:]):
                self.assertEqual(p_primary_phase(state, p), 2*pow(16, t, p) % p)
                self.assertNotEqual(p_primary_phase(state, p), 4*pow(16, t, p) % p)

    def test_all_affine_commuting_maps_and_anchored_reflection(self):
        for n in range(7):
            for a in (Q(-1), Q(), Q(2, 3), Q(1)):
                for b0 in (Q(), Q(-3, 5)):
                    slope, intercept = source_commuting_affine(n, a, b0)
                    next_slope, next_intercept = source_commuting_affine(n+1, a, b0)
                    for x in (Q(), Q(2, 7), Q(-11)):
                        lhs = next_slope*(16*x+direct_forcing(n+1))+next_intercept
                        rhs = 16*(slope*x+intercept)+direct_forcing(n+1)
                        self.assertEqual(lhs, rhs)
                    if not b0:
                        U_n = independent_history(n)[-1]
                        self.assertEqual(slope*U_n+intercept, U_n)
            U_n = independent_history(n)[-1]
            slope, intercept = source_commuting_affine(n, -1)
            self.assertEqual(intercept, 2*U_n)
            for x in (Q(1, 3), Q(-2)):
                self.assertEqual(slope*(slope*x+intercept)+intercept, x)
            # A time-dependent slope cannot satisfy the coefficient of x.
            self.assertNotEqual(16*Q(n+2), 16*Q(n+1))


class BoundaryAndPoleTests(unittest.TestCase):
    def test_tail_identity_intervals_enclose_independent_finite_tail(self):
        for N in (3, 8, 21):
            for n in (0, N//2, N):
                data = twisted_boundary_certificate(N, n, terms=9)
                c = data["initial"]
                self.assertEqual(data["state"], independent_history(n, c)[-1])
                # Finite prefix plus a certified residual: the two independently
                # enclosed expressions must overlap, not match endpoints.
                t_lo, t_hi = tail_interval(n, 12)
                lo, hi = data["bounded_shadow_error_interval"]
                self.assertLess(lo, data["state"]+t_hi)
                self.assertGreater(hi, data["state"]+t_lo)
                self.assertGreater(lo, 0)
                a_lo, a_hi = data["alpha_interval"]
                c_lo, c_hi = data["initial_limit_error_interval"]
                self.assertLess(c_lo, c+a_hi)
                self.assertGreater(c_hi, c+a_lo)

    def test_fixed_index_convergence_but_nonuniform_terminal_limit(self):
        previous = None
        for N in (4, 8, 16, 32):
            interior = twisted_boundary_certificate(N, 2, terms=10)
            upper = interior["bounded_shadow_error_interval"][1]
            if previous is not None:
                self.assertLess(upper, previous)
            previous = upper
            endpoint = twisted_boundary_certificate(N, N, terms=10)
            self.assertGreater(endpoint["state"], Q(19, 100))
            self.assertGreater(endpoint["bounded_shadow_error_interval"][0], Q(19, 100))
            self.assertLess(endpoint["state"], endpoint["alpha_interval"][1])
        self.assertLess(previous, Q(1, 10**30))

    def test_terminal_layer_quantitative_profile_budget(self):
        for N in (8, 16, 32):
            for j in (0, 1, 3):
                # Exponentially small endpoint sign needs correspondingly
                # refined source intervals; fixed precision cannot certify it.
                data = twisted_boundary_certificate(N, N-j, terms=N+8)
                lo, hi = data["terminal_profile_error_interval"]
                budget = data["terminal_profile_error_budget"]
                self.assertLess(max(abs(lo), abs(hi)), budget)
                if j == 0:
                    self.assertLess(hi, 0)

    def test_generating_identity_includes_truncation_boundary(self):
        for N in (0, 1, 5, 13):
            for c in (0, Q(2, 7)):
                for z in (0, Q(1, 16), Q(-1, 3), 2):
                    data = generating_identity_certificate(N, c, z)
                    self.assertEqual(data["left"], data["right"])
                    self.assertEqual(data["residual"], 0)
                    if z and (N or c):
                        self.assertNotEqual(data["endpoint_term"], 0)
                        self.assertNotEqual(data["left"], data["numerator"])

    def test_pole_sign_and_finite_twist_pole_not_removed(self):
        lo, hi = generating_pole_residue_interval(0, 12)
        self.assertLess(lo, hi)
        self.assertLess(hi, 0)
        for N in (2, 4, 8):
            c = solve_affine_seam(N, -1)["initial"]
            lo, hi = generating_pole_residue_interval(c, N+8)
            self.assertLess(hi, 0)
        # Merely rounding the bounded seed does not remove the pole exactly.
        lo, hi = generating_pole_residue_interval(Q(-1, 5), 12)
        self.assertGreater(lo, 0)


class ReciprocalControls(unittest.TestCase):
    def test_reversal_survives_but_reciprocal_quotient_fails(self):
        for value in (Q(2), Q(-3, 7), Q(5, 11), Q(1), Q(-1)):
            data = reciprocal_reversal_certificate(value)
            self.assertEqual(data["JFJ"], data["inverse_F"])
            self.assertEqual(data["quotient_pair_preserved"], value in (-1, 1))
        witness = reciprocal_reversal_certificate(2)
        self.assertEqual(witness["F_value"], 32)
        self.assertEqual(witness["F_reciprocal"], 8)
        self.assertNotIn(Q(8), (Q(32), Q(1, 32)))

    def test_reciprocal_is_not_a_circle_map_and_decay_is_not_cancellation(self):
        self.assertEqual(Q(2) % 1, Q(3) % 1)
        self.assertNotEqual((1/Q(2)) % 1, (1/Q(3)) % 1)
        for n in range(8):
            y = 16**n
            self.assertEqual(y % 1, 0)
            self.assertEqual(Q(1, y), Q(1, 16**n))

    def test_exact_domains_fail_closed(self):
        for bad in (0, -1, True, 2.0):
            with self.assertRaises(ValueError):
                solve_affine_seam(bad, -1)
        for bad in (0.5, True, "1"):
            with self.assertRaises(ValueError):
                solve_affine_seam(2, bad)
            with self.assertRaises(ValueError):
                generating_pole_residue_interval(bad)
        with self.assertRaises(ValueError):
            twisted_boundary_certificate(3, 4)
        with self.assertRaises(ValueError):
            reciprocal_reversal_certificate(0)
        with self.assertRaises(ValueError):
            affine_repeat_defect(2, -1, step=0)


if __name__ == "__main__":
    unittest.main()
