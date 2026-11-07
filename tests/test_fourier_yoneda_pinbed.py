"""Exact controls for the pin-bed theorems; finite tests do not prove normality."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product

from observational_succ.carrier_relative_targets import (
    Carrier, CarrierError, Instrument, Target, resolve_target,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement, exact_dft
from observational_succ.fourier_yoneda_pinbed import (
    CircleLaw, FuturePinBed, affine_push, bbp_epoch,
    bbp_surface_norm_error_squared, bernoulli2, finite_affine_push,
    completed_surface_translation_bound_squared,
    finite_convolution, finite_pin_support, law_support_closure, pin_surface,
    relative_truth_certificate, surface_covariance, surface_distance_squared,
    surface_energy, surface_energy_pairs, transported_pin, verify_bbp_trace,
)


def grid(q, offset=Q(0)):
    return CircleLaw.empirical(tuple(offset+Q(j, q) for j in range(q)))


def hidden_bit_carrier():
    # T(x1,x2,x3)=(x2,1,x3+1); only x1 is directly readable.
    step = tuple(((x >> 1) & 1) | 2 | ((((x >> 2) & 1) ^ 1) << 2)
                 for x in range(8))
    return Carrier("pinbed-f2-declared", 8, (
        Instrument("read", "bit-character", tuple(Q((-1)**(x & 1)) for x in range(8)),
                   tuple(range(8))),
        Instrument("advance", "no-readout", (Q(0),)*8, step),
    ))


def conjugate(value):
    answer = CyclotomicElement.scalar(value.modulus, 0)
    for j, coefficient in enumerate(value.polynomial):
        answer = answer + CyclotomicElement.root(value.modulus, -j).scale(coefficient)
    return answer


def finite_spectral_distance(left, right, weights):
    m = len(left)
    a, b = exact_dft(left), exact_dft(right)
    out = CyclotomicElement.scalar(m, 0)
    for h, weight in weights:
        difference = a[h % m] + b[h % m].scale(-1)
        out = out + (difference*conjugate(difference)).scale(weight)
    return out


class ContinuousPinSurfaceTests(unittest.TestCase):
    def test_normalization_and_raw_nonnegative_height(self):
        law = CircleLaw(((Q(1, 7), Q(2, 3)), (Q(3, 5), Q(1, 3))))
        for j in range(31):
            height = pin_surface(law, Q(j, 31)) + Q(1, 12)
            self.assertGreaterEqual(height, 0)
            self.assertLessEqual(height, Q(1, 4))
        self.assertEqual(bernoulli2(0), bernoulli2(1))

    def test_realization_rejects_mass_negativity_float_and_empty(self):
        for atoms in ((), ((Q(0), Q(1, 2)),),
                      ((Q(0), Q(2)), (Q(1, 2), Q(-1))),
                      ((0.0, Q(1)),), ((True, Q(1)),)):
            with self.assertRaises(CarrierError):
                CircleLaw(atoms)

    def test_circle_lifts_merge_without_changing_law(self):
        self.assertEqual(CircleLaw(((Q(-1), Q(1, 3)), (Q(2), Q(2, 3)))), grid(1))

    def test_delta_and_grid_calibration(self):
        for q in (1, 2, 3, 5, 7, 11):
            self.assertEqual(surface_energy(grid(q)), Q(1, 180*q**4))
            self.assertEqual(surface_energy_pairs(grid(q)), Q(1, 180*q**4))

    def test_dirac_distance_exact_geometry(self):
        for d in (Q(0), Q(1, 7), Q(1, 3), Q(1, 2), Q(5, 6)):
            self.assertEqual(surface_distance_squared(grid(1), grid(1, d)),
                             d*d*(1-d)**2/3)

    def test_pair_and_sorted_formulas_weighted_laws(self):
        for denominator in (5, 7, 11):
            law = CircleLaw(tuple((Q(j*j, denominator), Q(j+1, 10)) for j in range(4)))
            self.assertEqual(surface_energy(law), surface_energy_pairs(law))

    def test_rotation_invariance_and_nonzero_atomic_energy(self):
        law = CircleLaw.empirical((Q(1, 5), Q(1, 4), Q(4, 7)))
        self.assertGreater(surface_energy(law), 0)
        for a in (Q(1, 9), Q(-7, 4), Q(1)):
            self.assertEqual(surface_energy(affine_push(law, 1, a)), surface_energy(law))

    def test_actual_affine_naturality_at_seams(self):
        law = CircleLaw(((Q(0), Q(1, 3)), (Q(2, 7), Q(2, 3))))
        for b in (1, 2, 3, 16):
            for a in (Q(0), Q(1, 5), Q(-2, 3)):
                for t in (Q(0), Q(1), a, b*Q(2, 7)+a, Q(3, 11)):
                    self.assertEqual(pin_surface(affine_push(law, b, a), t),
                                     transported_pin(law, b, a, t))

    def test_naturality_mutations_are_visible(self):
        law, b, a, t = grid(1, Q(1, 7)), 3, Q(1, 5), Q(2, 9)
        correct = pin_surface(affine_push(law, b, a), t)
        self.assertNotEqual(correct, transported_pin(law, b, -a, t))
        self.assertNotEqual(correct, transported_pin(law, b, a, t)/b)
        self.assertNotEqual(correct, transported_pin(law, b, a, t)/b**2)

    def test_functor_composition_with_actual_source_offsets(self):
        law = grid(3, Q(2, 17))
        b, a, c, d = 2, Q(1, 7), 3, Q(2, 11)
        sequential = affine_push(affine_push(law, b, a), c, d)
        composed = affine_push(law, c*b, c*a+d)
        self.assertEqual(sequential, composed)
        for t in (Q(0), Q(1, 3), Q(3, 5)):
            nested = c*sum((transported_pin(law, b, a, (t-d+j)/c)
                            for j in range(c)), Q(0))
            self.assertEqual(nested, transported_pin(law, b*c, c*a+d, t))

    def test_sharp_expansion_on_realized_finite_laws(self):
        for b in (2, 3, 16):
            left, right = grid(b), grid(b, Q(1, 5*b))
            before = surface_distance_squared(left, right)
            after = surface_distance_squared(affine_push(left, b), affine_push(right, b))
            self.assertGreater(before, 0)
            self.assertEqual(after, b**4*before)
            self.assertGreater(after, before)  # false universal contraction rejected

    def test_finite_heights_match_haar_for_all_future_steps_but_law_differs(self):
        for q in (1, 3, 5, 7, 9, 17):
            law = CircleLaw(tuple((Q(j, q)+Q(k, 3*q), p/q)
                                  for j in range(q)
                                  for k, p in ((0, Q(1, 4)), (1, Q(3, 8)), (2, Q(3, 8)))))
            self.assertEqual(affine_push(law, 16), law)
            for i in range(q):
                self.assertEqual(pin_surface(law, Q(i, q)), 0)
            self.assertEqual(surface_energy(law), Q(1, 6480*q**4))

    def test_completed_metric_translation_bound_keeps_regularization_cost(self):
        delta, rho, b, depth = Q(1, 100), Q(3, 4), 2, 4
        actual_partial = sum((rho**j*surface_distance_squared(grid(1), grid(1, b**j*delta))
                              for j in range(depth+1)), Q(0))
        bound = completed_surface_translation_bound_squared(delta, b, rho, depth)
        self.assertLessEqual(actual_partial, bound)
        self.assertGreater(bound, delta**2/3)
        self.assertEqual(completed_surface_translation_bound_squared(0, b, rho, depth), 0)


class SourceAndFiniteLawTests(unittest.TestCase):
    def test_bbp_literal_source_binding_and_wrong_seed_rejection(self):
        law, states = bbp_epoch(5)
        self.assertTrue(verify_bbp_trace(states))
        self.assertEqual(Q(states[1].numerator, states[1].conductor), Q(47, 15))
        self.assertEqual(surface_energy(law), surface_energy_pairs(law))
        changed = (replace(states[0], numerator=1),)+states[1:]
        self.assertFalse(verify_bbp_trace(changed))
        changed_last = states[:-1]+(replace(states[-1], numerator=states[-1].numerator+1),)
        self.assertFalse(verify_bbp_trace(changed_last))
        self.assertFalse(verify_bbp_trace(states[1:]))

    def test_independent_four_pole_source_naturality(self):
        unwrapped = Q(0)
        for n in range(1, 6):
            forcing = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            old = grid(1, unwrapped)
            unwrapped = 16*unwrapped+forcing
            for t in (Q(0), Q(2, 9)):
                self.assertEqual(pin_surface(grid(1, unwrapped), t),
                                 transported_pin(old, 16, forcing, t))

    def test_tail_bound_constant_and_domain(self):
        self.assertEqual(bbp_surface_norm_error_squared(3), Q(1, 2700*3**4))
        with self.assertRaises(CarrierError):
            bbp_surface_norm_error_squared(0)

    def test_static_alias_can_split_after_one_lawful_step(self):
        k = (Q(1, 3),)*3+(Q(0),)*3
        uniform = (Q(1, 6),)*6
        alternative = (Q(1, 4), Q(1, 8), Q(1, 8), Q(1, 4), Q(1, 8), Q(1, 8))
        self.assertEqual(finite_convolution(k, uniform), finite_convolution(k, alternative))
        self.assertNotEqual(finite_convolution(k, finite_affine_push(uniform, 2)),
                            finite_convolution(k, finite_affine_push(alternative, 2)))
        support = finite_pin_support(k)
        self.assertEqual(support, (0, 1, 3, 5))
        self.assertEqual(law_support_closure(6, support, (2,)),
                         ((0, 1, 3, 5), (0, 1, 2, 3, 4, 5)))

    def test_incomplete_bed_can_be_autonomous(self):
        support = finite_pin_support((Q(1), Q(1))+(Q(0),)*10)
        self.assertNotIn(6, support)
        self.assertEqual(len(law_support_closure(12, support, (5,))), 1)
        self.assertIn(6, law_support_closure(12, support, (2,))[-1])

    def test_one_point_character_is_not_one_law_moment(self):
        mu, nu = (Q(1, 2), Q(0), Q(1, 2), Q(0)), (Q(0), Q(1, 2), Q(0), Q(1, 2))
        m, n = exact_dft(mu), exact_dft(nu)
        self.assertEqual(m[1], n[1])
        self.assertNotEqual(m[2], n[2])
        self.assertNotEqual(m[2], m[1]*m[1])

    def test_cyclic_fourier_affine_sign_and_nonunit_multiplier(self):
        law = (Q(1, 2), Q(1, 4), Q(0), Q(1, 4), Q(0), Q(0))
        before = exact_dft(law)
        after = exact_dft(finite_affine_push(law, 2, 1))
        for h in range(6):
            self.assertEqual(after[h], CyclotomicElement.root(6, h)*before[(2*h) % 6])

    def test_finite_joint_history_packet_has_periodic_law_counterfeit(self):
        q, b = 17, 2
        uniform = (Q(1, q),)*q
        self.assertEqual(finite_affine_push(uniform, b), uniform)
        spectrum = exact_dft(uniform)
        zero, one = CyclotomicElement.scalar(q, 0), CyclotomicElement.scalar(q, 1)
        for packet in product((-1, 0, 1), repeat=4):
            frequency = sum(h*b**j for j, h in enumerate(packet))
            self.assertLess(abs(frequency), q)
            self.assertEqual(spectrum[frequency % q], one if frequency == 0 else zero)
        self.assertEqual(spectrum[q % q], one)  # Haar would be zero at this untested mode


class FutureCompletionTests(unittest.TestCase):
    def bed(self):
        return FuturePinBed(((-2, Q(1, 5)), (-1, Q(1)), (1, Q(1)), (2, Q(1, 5))),
                            2, Q(3, 4))

    def test_exact_sum_and_least_envelope_recurrences(self):
        bed, w = self.bed(), dict(self.bed().base)
        for h in range(-63, 64):
            if h:
                self.assertEqual(bed.weight(2*h), w.get(2*h, 0)+bed.discount*bed.weight(h))
                self.assertEqual(bed.weight(2*h, least_envelope=True),
                                 max(w.get(2*h, 0), bed.discount*bed.weight(h, least_envelope=True)))
                self.assertLessEqual(bed.weight(h, least_envelope=True), bed.weight(h))

    def test_sum_completion_is_not_claimed_minimal(self):
        bed = self.bed()
        self.assertGreater(bed.weight(2), bed.weight(2, least_envelope=True))

    def test_no_invented_off_ray_observations(self):
        bed = self.bed()
        self.assertEqual(bed.weight(3), 0)
        self.assertEqual(bed.weight(6), 0)
        self.assertGreater(bed.weight(32), 0)

    def test_mass_lipschitz_and_tail_formulas(self):
        bed = self.bed()
        self.assertEqual(bed.total_base_weight, Q(12, 5))
        self.assertEqual(bed.total_completed_weight, Q(48, 5))
        self.assertEqual(bed.squared_lipschitz_bound, Q(4, 3))
        for j in range(6):
            finite = sum(dict(bed.finite_weights(j)).values(), Q(0))
            residual = bed.total_completed_weight-finite
            self.assertEqual(bed.squared_distance_tail(j), 4*residual)
            self.assertGreater(residual, 0)  # dropping the tail is not exact

    def test_discounted_future_identity_by_independent_finite_dft(self):
        bed = self.bed()
        left, right = (Q(1), Q(0), Q(0), Q(0)), (Q(0), Q(1, 2), Q(1, 2), Q(0))
        direct = finite_spectral_distance(left, right, bed.finite_weights(4))
        expected = CyclotomicElement.scalar(4, 0)
        for j in range(5):
            expected = expected + finite_spectral_distance(left, right, bed.base).scale(bed.discount**j)
            left, right = finite_affine_push(left, 2, 1), finite_affine_push(right, 2, 1)
        self.assertEqual(direct, expected)

    def test_invalid_weights_discounts_and_precision_rejected(self):
        for rho in (Q(0), Q(1), 0.5, True):
            with self.assertRaises(CarrierError):
                FuturePinBed(((-1, Q(1)), (1, Q(1))), 2, rho)
        for weights in (((1, Q(1)),), ((0, Q(1)),), ((-1, Q(-1)), (1, Q(-1))),
                        (1,), ((1, Q(1), Q(2)),)):
            with self.assertRaises(CarrierError):
                FuturePinBed(weights, 2, Q(1, 2))


class RelativeTruthTests(unittest.TestCase):
    def test_true_compatible_is_valid_with_false_witness_retained(self):
        c = hidden_bit_carrier()
        target = Target(c.source, "hidden x3 is zero", tuple(Q(1-((x >> 2) & 1)) for x in range(8)))
        receipt = relative_truth_certificate(c, target, 4)
        self.assertEqual(receipt["fiber"], (0, 4))
        self.assertEqual(receipt["relative_truth"], "TRUE_COMPATIBLE")
        self.assertEqual(receipt["true_witness"], 0)
        self.assertEqual(receipt["false_witness"], 4)
        self.assertEqual(receipt["target_resolution"], "AMBIGUOUS")
        self.assertIsNone(receipt["invariant_truth"])

    def test_future_pin_identifies_currently_hidden_target(self):
        c = hidden_bit_carrier()
        target = Target(c.source, "x2 is zero", tuple(Q(1-((x >> 1) & 1)) for x in range(8)))
        receipt = relative_truth_certificate(c, target, 0)
        self.assertEqual(receipt["target_resolution"], "IDENTIFIED")
        self.assertTrue(receipt["invariant_truth"])
        self.assertEqual(receipt["fiber"], (0, 4))  # full state still unreconstructed

    def test_source_and_target_hashes_bind_real_tables(self):
        c = hidden_bit_carrier()
        target = Target(c.source, "constant", (Q(1),)*8)
        r1 = relative_truth_certificate(c, target, 0)
        r2 = relative_truth_certificate(c, replace(target, values=(Q(0),)*8), 0)
        self.assertNotEqual(r1["target_fingerprint"], r2["target_fingerprint"])
        with self.assertRaises(CarrierError):
            relative_truth_certificate(c, replace(target, source="different source"), 0)
        self.assertFalse(r1["physical_source_attestation"])

    def test_empty_fiber_and_non_boolean_target_do_not_promote(self):
        c = hidden_bit_carrier()
        target = Target(c.source, "constant", (Q(1),)*8)
        self.assertEqual(resolve_target(c, target, ()).status, "INCOHERENT")
        with self.assertRaises(CarrierError):
            relative_truth_certificate(c, target, -1)
        with self.assertRaises(CarrierError):
            relative_truth_certificate(c, replace(target, values=(Q(1, 2),)*8), 0)


if __name__ == "__main__":
    unittest.main()
