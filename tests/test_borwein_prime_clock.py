"""Independent exact controls for Borwein simplex and prime-clock delta walks."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import factorial, prod

from observational_succ.borwein_prime_clock import (
    BorweinClockError, GatedStep, borwein_window_mass, clock_gate,
    exact_character_projector, exact_gated_succ_walk, first_boundary_leak,
    phase_distance, prime_borwein_widths, prime_clocks, softened_prime_clock_score,
    symmetric_succ_return_coefficients, uniform_cumulant_four, uniform_sum_cdf,
)


def independent_first_simplex(widths):
    """Separate volume argument: deficits Y_j=a_j-U_j in [0,2a_j]."""
    excess = sum(widths, F()) - 1
    if excess <= 0:
        return F()
    assert excess <= 2 * min(widths)
    return F(2 * excess**len(widths),
             factorial(len(widths)) * prod(2*a for a in widths))


def brute_gated_paths(start, clocks, steps):
    """Enumerate whole paths, not the module's dynamic program."""
    numerator = F()
    modulus = prod(clocks)
    all_jumps = [tuple(range(-s.half_width, s.half_width+1)) for s in steps]
    norm = prod(len(js) for js in all_jumps)
    for word in product(*all_jumps):
        state = start
        survives = True
        for step, jump in zip(steps, word):
            state += step.succ + jump
            k = state % step.prime
            if step.kind == "one":
                good = k == 1
            elif step.kind == "minus_one":
                good = k == (step.prime-1)
            else:
                good = k != 0
            if not good:
                survives = False
                break
        if survives:
            numerator += F(1, norm)
    return numerator


class BorweinPrimeClockTests(unittest.TestCase):
    def test_classical_borwein_plateau_and_first_crossing(self):
        first_six = tuple(F(1, q) for q in (3,5,7,9,11,13))
        self.assertLess(sum(first_six), 1)
        self.assertEqual(borwein_window_mass(first_six), 1)
        eight_sinc = first_six + (F(1,15),)
        from_simplex = independent_first_simplex(eight_sinc)
        self.assertEqual(1-borwein_window_mass(eight_sinc), from_simplex)
        self.assertEqual(first_boundary_leak(eight_sinc), from_simplex)
        self.assertEqual(from_simplex,
                         F(6879714958723010531,467807924720320453655260875000))

    def test_prime_only_borwein_first_failure_at_29(self):
        before=(3,5,7,11,13,17,19,23)
        after=before+(29,)
        self.assertEqual(borwein_window_mass(prime_borwein_widths(before)),1)
        widths=prime_borwein_widths(after)
        self.assertEqual(sum(widths),F(3343015913,3234846615))
        self.assertEqual(1-borwein_window_mass(widths),
                         independent_first_simplex(widths))
        self.assertEqual(first_boundary_leak(widths),
                         independent_first_simplex(widths))
        self.assertLess(float(1-borwein_window_mass(widths)), 2e-12)
        self.assertGreater(float(1-borwein_window_mass(widths)), 1e-12)

    def test_general_inclusion_exclusion_against_analytic_triangular_law(self):
        widths=(F(1,2),F(1,2))
        self.assertEqual(uniform_sum_cdf(widths,F(0)),F(1,2))
        self.assertEqual(uniform_sum_cdf(widths,F(1,2)),F(7,8))
        self.assertEqual(uniform_sum_cdf(widths,F(-1,2)),F(1,8))
        self.assertEqual(borwein_window_mass((F(1,2),)*3),F(23,24))
        self.assertEqual(borwein_window_mass((F(2),)),F(1,2))
        self.assertEqual(borwein_window_mass((F(2),),F(1)),
                         uniform_sum_cdf((F(2),),F(0))
                         - uniform_sum_cdf((F(2),),F(-2)))

    def test_borwein_shift_is_not_a_hard_clock_projector(self):
        clocks=(3,5)
        self.assertTrue(clock_gate(31,3,"one"))
        self.assertTrue(clock_gate(31,5,"one"))
        self.assertEqual(softened_prime_clock_score(31,clocks),F(1))
        self.assertFalse(clock_gate(11,3,"one"))
        self.assertEqual(softened_prime_clock_score(11,clocks),F(1))
        self.assertLess(softened_prime_clock_score(17,clocks),F(1))
        self.assertEqual(softened_prime_clock_score(31,clocks,F(0)),F(1))
        self.assertEqual(softened_prime_clock_score(11,clocks,F(0)),F(1))
        self.assertEqual(phase_distance(11,3),F(1,3))

    def test_exact_dirac_residue_orthogonality(self):
        for q in (2,3,5,7,11):
            for residue in range(q):
                for n in range(0,3*q):
                    self.assertEqual(exact_character_projector(n,q,residue),
                                     int(n%q==residue))
        self.assertEqual(clock_gate(31,5,"one"),True)
        self.assertEqual(clock_gate(31,5,"minus_one"),False)
        self.assertEqual(clock_gate(29,5,"minus_one"),True)
        self.assertEqual(clock_gate(25,5,"nonzero"),False)
        self.assertEqual(clock_gate(31,5,"nonzero"),True)
        self.assertEqual(clock_gate(31,2,"one"),clock_gate(31,2,"minus_one"))

    def test_gated_succ_word_brute_path_oracle(self):
        steps=(GatedStep(1,1,5,"minus_one"),GatedStep(0,2,3,"one"))
        # 31 + jitter +1 -> 31,32,33, hence modulo 5: 1,2,3.
        # For 'minus_one'=4 there are no survivors.
        self.assertEqual(exact_gated_succ_walk(31,(3,5),steps).survivors,F(0))
        live=(GatedStep(1,1,5,"nonzero"),GatedStep(0,2,3,"one"))
        result=exact_gated_succ_walk(31,(3,5),live)
        self.assertEqual(result.survivors,brute_gated_paths(31,(3,5),live))
        self.assertLessEqual(result.survivors,F(1))
        for steps2 in (
            (GatedStep(1,1,5,"one"),),
            (GatedStep(1,1,5,"nonzero"),GatedStep(1,1,3,"nonzero")),
            (GatedStep(2,1,3,"minus_one"),GatedStep(0,1,5,"one")),
            (GatedStep(0,1,3,"one"),GatedStep(0,1,5,"one")),
        ):
            model=exact_gated_succ_walk(31,(3,5),steps2)
            self.assertEqual(model.survivors,brute_gated_paths(31,(3,5),steps2))

    def test_poisson_succ_coefficients_and_non_gaussian_cumulant(self):
        self.assertEqual(symmetric_succ_return_coefficients(5,5),
                         (F(1),F(),F(1,2),F(),F(3,8),F(1,16)))
        self.assertEqual(symmetric_succ_return_coefficients(7,5),
                         (F(1),F(),F(1,2),F(),F(3,8),F()))
        w=prime_borwein_widths((3,5,7))
        self.assertEqual(uniform_cumulant_four(w),
                         -F(2,15)*sum((a**4 for a in w),F()))
        self.assertLess(uniform_cumulant_four(w),0)

    def test_fake_prime_and_malformed_input_controls(self):
        for bad in ((3,4), (3,3), (5,3), (), [3,5], (True,3)):
            with self.assertRaises(BorweinClockError):
                prime_clocks(bad)
        for bad in ((F(0),), (F(-1),), (1,), [], tuple()):
            with self.assertRaises(BorweinClockError):
                borwein_window_mass(bad)
        with self.assertRaises(BorweinClockError):
            first_boundary_leak((F(4),F(1,100)))
        for bad in (True, 2.5, -1):
            with self.assertRaises(BorweinClockError):
                exact_character_projector(bad,5,1)
        with self.assertRaises(BorweinClockError):
            exact_character_projector(7,4,1)
        with self.assertRaises(BorweinClockError):
            clock_gate(31,5,"imaginary")
        with self.assertRaises(BorweinClockError):
            GatedStep(1,1,4,"one")
        with self.assertRaises(BorweinClockError):
            exact_gated_succ_walk(31,(3,5),(GatedStep(1,1,7,"one"),))
        with self.assertRaises(BorweinClockError):
            softened_prime_clock_score(31,(3,5),F(-1))


if __name__ == "__main__":
    unittest.main()
