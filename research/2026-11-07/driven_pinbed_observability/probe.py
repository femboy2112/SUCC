"""Prospective exact source replay and calibrated oscillator controls."""
from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.carrier_relative_targets import CarrierError
from observational_succ.finite_fourier_carrier import CyclotomicElement as C, exact_dft
from observational_succ.driven_pinbed_observer import (
    SourceSnapshot, WindowProtocol, observe, phase_cycle, demodulate,
    reconstruct, bbp_snapshot, verify_bbp_snapshot, binned_moment,
    calibrate_constant_gain,
)
from observational_succ.integer_bbp_carrier import source_states


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, C):
        return {"conductor": value.modulus, "coefficients": [str(x) for x in value.polynomial]}
    raise TypeError(f"unregistered receipt value {type(value)!r}")


def rejected(action):
    try:
        action()
    except CarrierError:
        return True
    raise AssertionError("a calibrated invalid observation was accepted")


def run():
    cases = []
    checked_steps = 0
    for a in (19, 37, 73, 137):
        states = source_states(2*a-1)
        unwrapped = Q(0)
        assert (states[0].numerator, states[0].conductor) == (0, 1)
        for n, state in enumerate(states[1:], 1):
            unwrapped = 16*unwrapped + Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            assert unwrapped == Q(state.numerator, state.conductor)
            checked_steps += 1
        for m in (8, 12, 16):
            snapshot = bbp_snapshot(a, m)
            p = WindowProtocol(m, m//2, Q(3, 4))
            assert verify_bbp_snapshot(snapshot)
            frames = phase_cycle(snapshot, p)
            readout = demodulate(frames)
            recovered = reconstruct(readout, expected=snapshot)
            assert recovered == snapshot.weights
            moments = {h: binned_moment(snapshot, h) for h in (1, 2, 3)}
            direct_dft = exact_dft(recovered)
            assert all(moments[h] == direct_dft[-h % m] for h in moments)
            cases.append({"epoch": a, "sites": m, "length": p.length,
                          "source_fingerprint": snapshot.fingerprint,
                          "full_prefix_trace_sha256": snapshot.trace_hash,
                          "weights": recovered, "modes": moments,
                          "source_rebuilt_exactly": True,
                          "four_phase_exact_reconstruction": True})

    u = SourceSnapshot((Q(1, 6),)*6)
    v = SourceSnapshot((Q(1, 4), Q(1, 8), Q(1, 8))*2)
    p = WindowProtocol(6, 3)
    left, right = observe(u, p), observe(v, p)
    assert left.static == right.static and left.coherent != right.coherent
    frames = phase_cycle(v, p)
    mixed = (phase_cycle(u, p)[0],)+frames[1:]
    fake_source = replace(bbp_snapshot(19, 8), trace_hash="changed source seed")
    assert not verify_bbp_snapshot(fake_source)
    gain = C.scalar(p.conductor, 2)+C.root(p.conductor, p.conductor//4).scale(Q(3, 2))
    measured = replace(right, coherent=tuple(gain*z for z in right.coherent))
    calibrated, recovered_gain = calibrate_constant_gain(measured)
    assert recovered_gain == gain and calibrated == right
    assert reconstruct(calibrated, expected=v) == v.weights
    ghost = tuple(z+C.root(p.conductor, (p.conductor//p.sites)*y).scale(Q(1, 7))
                  for y, z in enumerate(right.coherent))
    non_gaussian_calibrations = []
    for m in (5, 7, 9):
        source = SourceSnapshot(tuple(Q(j+1, m*(m+1)//2) for j in range(m)))
        protocol = WindowProtocol(m, m//2)
        original = observe(source, protocol)
        complex_gain = C.scalar(protocol.conductor, 2)+C.root(protocol.conductor, 1)
        altered = replace(original, coherent=tuple(complex_gain*z for z in original.coherent))
        restored, found_gain = calibrate_constant_gain(altered)
        assert found_gain == complex_gain and restored == original
        non_gaussian_calibrations.append({"sites": m, "exact_gain_recovered": True})
    # Derived adversarial control, not one of the predeclared source holdouts:
    # an unmodelled position-dependent phase can produce another valid law.
    even = SourceSnapshot((Q(1, 2), Q(0), Q(1, 2), Q(0)), "even clock law")
    odd = SourceSnapshot((Q(0), Q(1, 2), Q(0), Q(1, 2)), "odd clock law")
    p4 = WindowProtocol(4, 2)
    even_read, odd_read = observe(even, p4), observe(odd, p4)
    drifted = replace(even_read, coherent=tuple(C.root(4, -1+2*y)*z
                                              for y, z in enumerate(even_read.coherent)))
    assert drifted.static == odd_read.static and drifted.coherent == odd_read.coherent
    assert reconstruct(drifted) == odd.weights
    corrected_drift, apparent_gain = calibrate_constant_gain(drifted)
    assert apparent_gain == C.scalar(4, 1) and corrected_drift == drifted
    mutations = {
        "mixed_snapshot": rejected(lambda: demodulate(mixed)),
        "missing_phase": rejected(lambda: demodulate(frames[:3])),
        "duplicate_phase": rejected(lambda: demodulate(frames[:3]+(frames[0],))),
        "wrong_expected_source": rejected(lambda: reconstruct(right, expected=u)),
        "incoherent_positive_inverse": rejected(lambda: reconstruct(replace(right, coherent=ghost))),
        "full_aperture": rejected(lambda: WindowProtocol(6, 6)),
        "zero_drive": rejected(lambda: WindowProtocol(6, 3, Q(0))),
        "changed_authentic_trace": not verify_bbp_snapshot(fake_source),
        "realizable_varying_phase_substitution_with_expected_source": rejected(
            lambda: reconstruct(drifted, expected=even)),
    }
    files = ["observational_succ/driven_pinbed_observer.py",
             "tests/test_driven_pinbed_observer.py",
             "observational_succ/integer_bbp_carrier.py",
             "research/2026-11-07/driven_pinbed_observability/PREREGISTRATION.md",
             "research/2026-11-07/driven_pinbed_observability/probe.py"]
    return {"status": "EXACT_FINITE_PASS", "base_commit": "e8a4126754dc95eddeca758ea92ead50246da630",
            "source": "original four signed poles and literal U0=0",
            "source_recurrence_steps_including_repeated_prefixes": checked_steps,
            "fresh_source_readouts": cases,
            "static_alias_split_by_coherent_drive": True,
            "unknown_constant_complex_gain_calibrated": recovered_gain,
            "non_gaussian_gain_calibrations": non_gaussian_calibrations,
            "derived_varying_phase_control": {
                "static_laws_identical": True, "drifted_law_is_realizable": True,
                "apparent_constant_gain": apparent_gain,
                "original_source_substitution_rejected": True,
                "scope": "expected-snapshot binding; arbitrary drift is not self-calibrated"},
            "mutations_rejected": mutations,
            "sha256": {f: sha256((ROOT/f).read_bytes()).hexdigest() for f in files},
            "physical_attestation": False,
            "finite_run_proves_universal_theorems": False,
            "source_selected_Weyl_decay": "OPEN", "pi_base16_normality": "OPEN"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, default=encode))
