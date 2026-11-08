from dataclasses import replace
from fractions import Fraction as Q
import unittest

from observational_succ.carrier_relative_targets import CarrierError
from observational_succ.finite_fourier_carrier import CyclotomicElement as C
from observational_succ.fourier_yoneda_pinbed import CircleLaw, finite_affine_push
from observational_succ.driven_pinbed_observer import (
    SourceSnapshot, WindowProtocol, DrivenReadout, PhaseFrame, observe,
    phase_cycle, demodulate, reconstruct, bbp_snapshot, verify_bbp_snapshot,
    binned_moment, b2_scan_coefficient, b2_scan_alias_bound, conjugate,
    calibrate_constant_gain,
)


def weights(m):
    total = sum((j+1)**2 for j in range(m))
    return tuple(Q((j+1)**2, total) for j in range(m))


class TestDrivenPinbed(unittest.TestCase):
    def setUp(self):
        self.source = SourceSnapshot(weights(8))
        self.protocol = WindowProtocol(8, 4, Q(2, 3))

    def test_local_inverse_every_calibration_point(self):
        for m in (4, 6, 8):
            for length in range(1, m):
                p = WindowProtocol(m, length)
                for x in range(m):
                    source = SourceSnapshot(tuple(Q(j == x) for j in range(m)))
                    self.assertEqual(reconstruct(observe(source, p), expected=source), source.weights)

    def test_fresh_rational_holdouts(self):
        for m in (7, 9, 11, 13):
            source = SourceSnapshot(weights(m), "prospective rational holdout")
            for length in (1, m//2, m-1):
                p = WindowProtocol(m, length, Q(3, 5))
                recovered = demodulate(phase_cycle(source, p))
                self.assertEqual(reconstruct(recovered, expected=source), source.weights)

    def test_four_phase_demodulation(self):
        self.assertEqual(demodulate(phase_cycle(self.source, self.protocol)),
                         observe(self.source, self.protocol))

    def test_phase_order_is_labelled(self):
        frames = phase_cycle(self.source, self.protocol)
        self.assertEqual(demodulate(tuple(reversed(frames))), observe(self.source, self.protocol))

    def test_direct_nonnegative_phase_masks_on_four_clock(self):
        source = SourceSnapshot((Q(1, 10), Q(2, 10), Q(3, 10), Q(4, 10)))
        p = WindowProtocol(4, 3, Q(1, 2))
        cosine = (1, 0, -1, 0)
        for frame in phase_cycle(source, p):
            for y, value in enumerate(frame.values):
                expected = sum((source.weights[(y+j) % 4]
                                * (1+p.amplitude*cosine[(frame.phase-j) % 4])
                                for j in range(3)), Q(0))
                self.assertGreaterEqual(expected, 0)
                self.assertEqual(value, C.scalar(4, expected))

    def test_static_alias_is_split(self):
        u = SourceSnapshot((Q(1, 6),)*6)
        v = SourceSnapshot((Q(1, 4), Q(1, 8), Q(1, 8))*2)
        p = WindowProtocol(6, 3)
        left, right = observe(u, p), observe(v, p)
        self.assertEqual(left.static, right.static)
        self.assertNotEqual(left.coherent, right.coherent)
        self.assertNotEqual(reconstruct(left), reconstruct(right))

    def test_coherent_profile_covariance_with_exact_dft(self):
        m, n = 8, self.protocol.conductor
        readout = observe(self.source, self.protocol)
        for h in range(m):
            measured = C.scalar(n, 0)
            moment = C.scalar(n, 0)
            kernel = C.scalar(n, 0)
            for y in range(m):
                measured = measured + C.root(n, -(n//m)*h*y)*readout.coherent[y]
                moment = moment + C.root(n, -(n//m)*h*y).scale(self.source.weights[y])
            for j in range(self.protocol.length):
                kernel = kernel + C.root(n, (n//m)*(h-1)*j)
            self.assertEqual(measured, kernel*moment)

    def test_mixed_source_snapshots_are_rejected(self):
        first = list(phase_cycle(self.source, self.protocol))
        other = SourceSnapshot(tuple(reversed(self.source.weights)))
        first[1] = phase_cycle(other, self.protocol)[1]
        with self.assertRaises(CarrierError):
            demodulate(first)

    def test_same_weights_different_history_are_rejected(self):
        frames = list(phase_cycle(self.source, self.protocol))
        other = replace(self.source, trace_hash="different source clock")
        frames[2] = phase_cycle(other, self.protocol)[2]
        with self.assertRaises(CarrierError):
            demodulate(frames)

    def test_mixed_protocols_are_rejected(self):
        frames = list(phase_cycle(self.source, self.protocol))
        frames[0] = phase_cycle(self.source, WindowProtocol(8, 3))[0]
        with self.assertRaises(CarrierError):
            demodulate(frames)

    def test_duplicate_or_missing_phase_is_rejected(self):
        frames = phase_cycle(self.source, self.protocol)
        for bad in (frames[:3], frames[:3]+(frames[0],)):
            with self.assertRaises(CarrierError):
                demodulate(bad)

    def test_inconsistent_dc_is_rejected(self):
        frames = list(phase_cycle(self.source, self.protocol))
        frame = frames[1]
        values = (frame.values[0]+C.scalar(frame.protocol.conductor, 1),)+frame.values[1:]
        frames[1] = replace(frame, values=values)
        with self.assertRaises(CarrierError):
            demodulate(frames)

    def test_range_coherence_is_required_beyond_positive_inverse(self):
        readout = observe(self.source, self.protocol)
        m, n = self.protocol.sites, self.protocol.conductor
        ghost = tuple(z+C.root(n, (n//m)*y).scale(Q(1, 7))
                      for y, z in enumerate(readout.coherent))
        with self.assertRaisesRegex(CarrierError, "coherence"):
            reconstruct(replace(readout, coherent=ghost))

    def test_wrong_mass_is_rejected(self):
        readout = observe(self.source, self.protocol)
        bad = replace(readout, static=tuple(z.scale(2) for z in readout.static),
                      coherent=tuple(z.scale(2) for z in readout.coherent))
        with self.assertRaises(CarrierError):
            reconstruct(bad)

    def test_consistent_signed_law_is_rejected(self):
        p = WindowProtocol(4, 2)
        a = observe(SourceSnapshot((Q(1), Q(0), Q(0), Q(0))), p)
        b = observe(SourceSnapshot((Q(0), Q(1), Q(0), Q(0))), p)
        bad = replace(a, static=tuple(x.scale(2)+y.scale(-1) for x, y in zip(a.static, b.static)),
                      coherent=tuple(x.scale(2)+y.scale(-1) for x, y in zip(a.coherent, b.coherent)))
        with self.assertRaisesRegex(CarrierError, "nonnegative"):
            reconstruct(bad)

    def test_wrong_quadrature_orientation_is_rejected(self):
        frames = list(phase_cycle(self.source, self.protocol))
        one, three = frames[1], frames[3]
        frames[1], frames[3] = replace(three, phase=1), replace(one, phase=3)
        with self.assertRaises(CarrierError):
            reconstruct(demodulate(frames))

    def test_expected_source_binding(self):
        readout = observe(self.source, self.protocol)
        with self.assertRaises(CarrierError):
            reconstruct(readout, expected=replace(self.source, source="another source"))

    def test_nonreal_phase_frame_is_rejected(self):
        n = self.protocol.conductor
        with self.assertRaises(CarrierError):
            PhaseFrame(self.protocol, self.source.fingerprint, 0,
                       (C.root(n, n//4),)*self.protocol.sites)

    def test_truncated_profile_is_rejected(self):
        readout = observe(self.source, self.protocol)
        with self.assertRaises(CarrierError):
            replace(readout, static=readout.static[:-1])

    def test_exact_source_replay(self):
        source = bbp_snapshot(5, 8)
        self.assertTrue(verify_bbp_snapshot(source))
        self.assertEqual(reconstruct(demodulate(phase_cycle(source, self.protocol)), expected=source),
                         source.weights)

    def test_source_hash_mutation_fails_authentication(self):
        source = bbp_snapshot(5, 8)
        self.assertFalse(verify_bbp_snapshot(replace(source, trace_hash="changed zero seed")))

    def test_source_mass_mutation_fails_authentication(self):
        source = bbp_snapshot(5, 8)
        self.assertFalse(verify_bbp_snapshot(replace(source, weights=(Q(1, 8),)*8)))

    def test_snapshot_fingerprint_binds_all_source_fields(self):
        source = bbp_snapshot(5, 8)
        self.assertNotEqual(source.fingerprint, replace(source, epoch=6).fingerprint)
        self.assertNotEqual(source.fingerprint, replace(source, source="counterseed").fingerprint)

    def test_constant_unknown_complex_gain_self_calibrates(self):
        for m in (4, 8, 12):
            source, p = SourceSnapshot(weights(m)), WindowProtocol(m, m//2)
            original = observe(source, p)
            n = p.conductor
            gain = C.scalar(n, 2)+C.root(n, n//4).scale(Q(3, 2))
            measured = replace(original, coherent=tuple(gain*z for z in original.coherent))
            corrected, recovered_gain = calibrate_constant_gain(measured)
            self.assertEqual(recovered_gain, gain)
            self.assertEqual(corrected, original)
            self.assertEqual(reconstruct(corrected, expected=source), source.weights)

    def test_zero_gain_is_rejected(self):
        readout = observe(self.source, self.protocol)
        zero = (C.scalar(self.protocol.conductor, 0),)*self.protocol.sites
        with self.assertRaises(CarrierError):
            calibrate_constant_gain(replace(readout, coherent=zero))

    def test_gain_calibration_requires_mass_reference(self):
        readout = observe(self.source, self.protocol)
        with self.assertRaises(CarrierError):
            calibrate_constant_gain(replace(readout, static=tuple(z.scale(2) for z in readout.static)))

    def test_noninvertible_abstract_action_after_recovery(self):
        source = SourceSnapshot(weights(6))
        p = WindowProtocol(6, 3)
        pushed = SourceSnapshot(finite_affine_push(source.weights, 16, 1), "abstract affine action")
        recovered = reconstruct(demodulate(phase_cycle(source, p)))
        self.assertEqual(finite_affine_push(recovered, 16, 1),
                         reconstruct(demodulate(phase_cycle(pushed, p))))

    def test_binned_character_sign_and_conjugacy(self):
        source = SourceSnapshot((Q(0), Q(1), Q(0), Q(0)))
        self.assertEqual(binned_moment(source, 1), C.root(4, -1))
        self.assertEqual(binned_moment(source, -1), conjugate(binned_moment(source, 1)))

    def test_b2_scan_exact_simple_case(self):
        law = CircleLaw(((Q(0), Q(1)),))
        self.assertEqual(b2_scan_coefficient(law, 4, 1), C.scalar(4, Q(1, 16)))
        self.assertEqual(b2_scan_alias_bound(4, 1), Q(3, 8))

    def test_b2_scan_symmetry(self):
        law = CircleLaw(((Q(1, 7), Q(2, 5)), (Q(3, 8), Q(3, 5))))
        self.assertEqual(b2_scan_coefficient(law, 8, -2), conjugate(b2_scan_coefficient(law, 8, 2)))

    def test_no_zero_or_out_of_band_scan(self):
        law = CircleLaw(((Q(0), Q(1)),))
        for mode in (0, 3, True, Q(1)):
            with self.assertRaises(CarrierError):
                b2_scan_coefficient(law, 4, mode)
            with self.assertRaises(CarrierError):
                b2_scan_alias_bound(4, mode)

    def test_protocol_and_probability_domains(self):
        for args in ((8, 8), (8, 0), (True, 1), (49, 2), (8, 4, Q(0)), (8, 4, Q(2))):
            with self.assertRaises(CarrierError):
                WindowProtocol(*args)
        for weights_ in ((Q(1), Q(-1)), (Q(1), Q(1)), (0.5, 0.5), (True, False)):
            with self.assertRaises(CarrierError):
                SourceSnapshot(weights_)


if __name__ == "__main__":
    unittest.main()
