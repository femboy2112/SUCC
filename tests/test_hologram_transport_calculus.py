"""Exact adversarial probes of the prime-clock-to-hologram transport calculus.

Covers: R_N I_N = id on the range; the composition / naturality law
T_{L<-M} T_{M<-N} = T_{L<-N}; the SUCC n -> n+1 covariance of authentic residue
projectors and its naturality through transport; the nonrecoverability
counterexample; and the domain / firewall guards (abstract-L^2 point evaluation
refused, wrong-horizon sampling refused, composite moduli refused).

All exact: Fraction / finitely supported coefficient vectors only.
"""
import unittest
from fractions import Fraction as F

from observational_succ.hologram_transport_calculus import (
    AbstractL2,
    HologramTransportError,
    RangeFunction,
    _canon,
    lift,
    lifted_residue,
    lifted_succ,
    nonrecoverability_witness,
    residue_projector,
    residue_projector_covariance,
    residue_projector_matches_clock_gate,
    sample,
    succ_shift,
    transport,
    verify_composition_law,
    verify_range_retraction,
)

# A representative finitely supported arithmetic source (negative sites included).
SRC = ((-3, F(2)), (-1, F(1, 3)), (0, F(1)), (1, F(-7, 4)), (4, F(5, 2)), (7, F(9)))
HORIZONS = (4, 5, 6, 7, 8, 10, 16)


class RangeRetractionTests(unittest.TestCase):
    def test_R_after_I_is_identity_on_range(self):
        for n in HORIZONS:
            self.assertEqual(verify_range_retraction(n, SRC), _canon(SRC))
            self.assertEqual(sample(n, lift(n, SRC)), _canon(SRC))

    def test_sample_is_a_genuine_kernel_computation(self):
        # The recovered values are produced by evaluating the actual kernel at
        # integers, not read back from storage: single delta must sample to 1 at
        # 0 and 0 at neighbours, through interpolant / B_N(integer)=delta.
        f = lift(6, ((0, F(1)),))
        self.assertEqual(f.evaluate(F(0)), F(1))
        self.assertEqual(f.evaluate(F(1)), F(0))
        self.assertEqual(f.evaluate(F(-1)), F(0))
        self.assertEqual(sample(6, f), ((0, F(1)),))

    def test_empty_source_round_trips(self):
        self.assertEqual(sample(5, lift(5, ())), ())
        self.assertEqual(sample(5, lift(5, {})), ())


class CompositionLawTests(unittest.TestCase):
    def test_composition_law_three_horizons(self):
        triples = ((10, 6, 4), (4, 6, 8), (16, 5, 7), (8, 8, 8), (4, 5, 6), (7, 4, 16))
        for L, M, N in triples:
            left = transport(L, M, transport(M, N, SRC))
            right = transport(L, N, SRC)
            self.assertEqual(left, right)
            # both equal I_L c: arithmetic source preserved, geometry re-homed
            self.assertEqual(left, lift(L, SRC))
            self.assertEqual(verify_composition_law(L, M, N, SRC), lift(L, SRC))

    def test_transport_preserves_source_changes_geometry(self):
        # Same integer samples (coeffs) after transport, but a genuinely
        # different off-lattice function when the horizon changes.
        t46 = transport(6, 4, ((0, F(1)),))
        self.assertEqual(sample(6, t46), ((0, F(1)),))           # arithmetic source kept
        self.assertEqual(t46, lift(6, ((0, F(1)),)))
        self.assertNotEqual(t46, lift(4, ((0, F(1)),)))          # distinct range element
        self.assertNotEqual(t46.evaluate(F(3, 10)),
                            lift(4, ((0, F(1)),)).evaluate(F(3, 10)))

    def test_transport_endpoint_is_identity(self):
        self.assertEqual(transport(6, 6, SRC), lift(6, SRC))     # T_{N<-N} = id on ran(I_N)
        f = lift(6, SRC)
        self.assertEqual(transport(6, 6, f), f)

    def test_transport_accepts_range_element_and_raw_source(self):
        # transport of the range element equals transport of its raw coeffs.
        self.assertEqual(transport(10, 4, lift(4, SRC)), transport(10, 4, SRC))


class CovarianceTests(unittest.TestCase):
    def test_succ_covariance_on_ell2(self):
        c = _canon(((0, F(1)), (1, F(2)), (2, F(3)), (3, F(4)), (4, F(5)), (6, F(7))))
        for p in (2, 3, 5, 7):
            for r in range(p):
                lhs = succ_shift(residue_projector(c, p, r))
                rhs = residue_projector(succ_shift(c), p, (r + 1) % p)
                self.assertEqual(lhs, rhs)

    def test_covariance_and_naturality_through_transport(self):
        c = ((0, F(1)), (1, F(2)), (3, F(5)), (4, F(7)), (6, F(-1)), (7, F(8)))
        for p in (3, 5, 7):
            for r in range(p):
                result = residue_projector_covariance(p, r, c, 4, 6)
                self.assertTrue(result["covariance_holds"])
                self.assertTrue(result["shift_natural"])
                self.assertTrue(result["projector_natural"])
                self.assertTrue(result["intertwining_transported"])
                self.assertEqual(result["image_class"], (r + 1) % p)

    def test_wrong_phase_orientation_is_load_bearing(self):
        # Source meets class r; for p >= 3 the r-1 orientation disagrees with r+1.
        c = ((0, F(1)), (1, F(2)), (2, F(3)), (3, F(4)), (4, F(5)), (5, F(6)), (6, F(7)))
        for p in (3, 5, 7):
            for r in range(p):
                result = residue_projector_covariance(p, r, c, 4, 6)
                self.assertTrue(result["wrong_orientation_differs"],
                                f"orientation not load-bearing at p={p}, r={r}")
        # p=2 is the degenerate case r+1 == r-1 (mod 2); not a counterexample.
        res2 = residue_projector_covariance(2, 1, c, 4, 6)
        self.assertFalse(res2["wrong_orientation_differs"])

    def test_lifted_operators_realize_the_intertwining(self):
        # Directly: in ran(I_M), lifted_succ o lifted_residue(r) = lifted_residue(r+1) o lifted_succ.
        c = ((0, F(1)), (1, F(2)), (3, F(5)), (4, F(7)))
        g = transport(6, 4, c)
        p, r = 3, 1
        left = lifted_succ(6, lifted_residue(6, g, p, r))
        right = lifted_residue(6, lifted_succ(6, g), p, (r + 1) % p)
        self.assertEqual(left, right)

    def test_residue_projector_matches_authentic_clock_gate(self):
        c = tuple((m, F(m * m + 1, 3)) for m in range(-5, 12))
        for p in (3, 5, 7):
            for kind in ("one", "minus_one", "nonzero"):
                self.assertTrue(residue_projector_matches_clock_gate(c, p, kind))


class NonrecoverabilityTests(unittest.TestCase):
    def test_distinct_functions_identical_integer_samples(self):
        w = nonrecoverability_witness()
        # identical integer samples (the shared arithmetic source delta_0)
        self.assertEqual(w["equal_integer_samples"],
                         {-3: F(0), -2: F(0), -1: F(0), 0: F(1),
                          1: F(0), 2: F(0), 3: F(0)})
        self.assertEqual(sample(4, w["f"]), ((0, F(1)),))
        self.assertEqual(sample(6, w["g"]), ((0, F(1)),))
        # distinct as functions: exact disagreement at 3/10
        self.assertEqual(w["value_f_at_separating"], F(1))
        self.assertEqual(w["value_g_at_separating"], F(30922061, 31104000))
        self.assertNotEqual(w["value_f_at_separating"], w["value_g_at_separating"])
        self.assertTrue(w["functions_distinct"])
        self.assertNotEqual(w["f"], w["g"])
        # 1/10 is a flat collision: even an off-lattice probe need not separate
        self.assertEqual(w["flat_value_f"], w["flat_value_g"])
        self.assertEqual(w["flat_value_f"], F(1))

    def test_witness_is_reconstructed_by_hand(self):
        # Independent of the helper: B_4 and B_6 agree on Z, differ at 3/10.
        f, g = lift(4, ((0, F(1)),)), lift(6, ((0, F(1)),))
        for m in range(-4, 5):
            self.assertEqual(f.evaluate(F(m)), g.evaluate(F(m)))
        self.assertNotEqual(f.evaluate(F(3, 10)), g.evaluate(F(3, 10)))


class DomainGuardTests(unittest.TestCase):
    def test_point_evaluation_on_abstract_L2_is_refused(self):
        with self.assertRaises(HologramTransportError):
            sample(6, AbstractL2())
        with self.assertRaises(HologramTransportError):
            sample(6, AbstractL2("mystery class with no bounded point sampling"))
        with self.assertRaises(HologramTransportError):
            transport(10, 6, AbstractL2())

    def test_sampling_outside_the_declared_range_is_refused(self):
        # R_N is defined on ran(I_N) only: a function of a different horizon,
        # or a bare coefficient tuple, is out of domain.
        with self.assertRaises(HologramTransportError):
            sample(6, lift(4, SRC))          # f in ran(I_4), not ran(I_6)
        with self.assertRaises(HologramTransportError):
            sample(6, SRC)                   # a raw coeff tuple is not a RangeFunction

    def test_transport_through_mismatched_range_element_is_refused(self):
        # transport(M, N, f) demands f in ran(I_N): horizon must match N.
        with self.assertRaises(HologramTransportError):
            transport(10, 6, lift(4, SRC))   # f in ran(I_4), N declared 6

    def test_composite_or_fake_modulus_is_refused(self):
        for bad in (4, 6, 9, 1, 0):
            with self.assertRaises(HologramTransportError):
                residue_projector(SRC, bad, 0)
        with self.assertRaises(HologramTransportError):
            residue_projector(SRC, 5, 5)     # r out of range 0..p-1
        with self.assertRaises(HologramTransportError):
            residue_projector(SRC, 5, -1)

    def test_malformed_source_is_refused(self):
        with self.assertRaises(HologramTransportError):
            lift(6, ((0, 0.1),))             # float value, not a Fraction
        with self.assertRaises(HologramTransportError):
            lift(6, ((True, F(1)),))         # bool site rejected
        with self.assertRaises(HologramTransportError):
            lift(6, ((0, F(1)), (0, F(2))))  # duplicate site
        with self.assertRaises(HologramTransportError):
            lift(0, SRC)                     # horizon out of 1..256
        with self.assertRaises(HologramTransportError):
            lift(257, SRC)
        with self.assertRaises(HologramTransportError):
            RangeFunction(6, ((1, F(1)), (0, F(1))))  # non-canonical (unsorted)


class FirewallTests(unittest.TestCase):
    def test_three_factorials_stay_distinct(self):
        # Arithmetic v_p(N!) (Legendre occupation) is an integer exponent;
        # the Borwein simplex volume contributes 1/m! and the Poisson jump-time
        # series 1/k!.  Verify these are genuinely different quantities, so the
        # transport calculus never silently fuses them.
        from observational_succ.factorial_borwein_hologram import (
            legendre_exponent, poisson_wheel_polynomial,
        )
        from observational_succ.borwein_prime_clock import uniform_sum_cdf
        from math import factorial

        arithmetic = legendre_exponent(6, 2)            # v_2(6!) = 4, an exponent
        self.assertEqual(arithmetic, 4)
        # Poisson jump-time tail is exactly t^(M+1)/(M+1)! -- a 1/k! normalization.
        _, poisson_tail = poisson_wheel_polynomial(0, ((3, "one"),), F(1), 3)
        self.assertEqual(poisson_tail, F(1, factorial(4)))
        # Borwein simplex factorial lives in the uniform-sum CDF denominator; a
        # non-degenerate CDF value is neither the integer exponent nor the tail.
        borwein_mass = uniform_sum_cdf((F(1, 4), F(1, 8)), F(0))
        self.assertEqual(borwein_mass, F(1, 2))         # symmetric CDF at 0
        self.assertNotEqual(borwein_mass, F(arithmetic))
        self.assertNotEqual(borwein_mass, poisson_tail)
        self.assertNotEqual(F(arithmetic), poisson_tail)


if __name__ == "__main__":
    unittest.main()
