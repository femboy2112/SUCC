"""Exact phase-cycled pin observations with source and protocol binding.

Finite calibration of the continuous two-tone aperture theorem.  Quadratures
live in the existing cyclotomic carrier; no floating arithmetic or pi digits
enter an authenticated BBP source.  Full translated profiles are required by
the local inverse.  Snapshot fingerprints are digital integrity, not physical
attestation or a guarantee of access to repeated measurements.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from math import gcd, lcm
from typing import Sequence

from .carrier_relative_targets import CarrierError, rational
from .finite_fourier_carrier import CyclotomicElement as C
from .fourier_yoneda_pinbed import CircleLaw, pin_surface
from .integer_bbp_carrier import source_states


def _integer(value, minimum=0, maximum=None):
    if type(value) is not int or value < minimum or (maximum is not None and value > maximum):
        raise CarrierError("integer outside the declared finite domain")
    return value


def _hash(value):
    return sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


@lru_cache(maxsize=32768)
def _root(n, exponent):
    return C.root(n, exponent % n)


def _zero(n):
    return C.scalar(n, 0)


def _sub(left, right):
    return left + right.scale(-1)


def conjugate(value: C) -> C:
    if type(value) is not C:
        raise CarrierError("cyclotomic value required")
    out = _zero(value.modulus)
    for j, coefficient in enumerate(value.polynomial):
        if coefficient:
            out = out + _root(value.modulus, -j).scale(coefficient)
    return out


def _root_minus_one_inverse(n, exponent):
    """1/(omega-1)=sum_(j=0)^(d-1) j omega^j / d, for omega of order d>1."""
    exponent %= n
    order = n // gcd(n, exponent)
    if order == 1:
        raise CarrierError("drive and aperture have a common blind boundary")
    out = _zero(n)
    for j in range(1, order):
        out = out + _root(n, exponent*j).scale(Q(j, order))
    return out


def _field_inverse(value):
    """Exact inverse by the cyclotomic Galois norm; used only for calibration."""
    n = value.modulus
    if value == _zero(n):
        raise CarrierError("zero coherent gain cannot be calibrated")
    product = C.scalar(n, 1)
    for unit in range(2, n):
        if gcd(unit, n) != 1:
            continue
        transformed = _zero(n)
        for j, coefficient in enumerate(value.polynomial):
            if coefficient:
                transformed = transformed + _root(n, unit*j).scale(coefficient)
        product = product*transformed
    norm = value*product
    if len(norm.polynomial) != 1 or norm.polynomial[0] == 0:
        raise AssertionError("nonzero cyclotomic element must have nonzero rational norm")
    return product.scale(1/norm.polynomial[0])


@dataclass(frozen=True)
class SourceSnapshot:
    weights: tuple[Q, ...]
    source: str = "declared finite probability"
    epoch: int | None = None
    trace_hash: str = ""

    def __post_init__(self):
        if type(self.weights) is not tuple or not 2 <= len(self.weights) <= 48:
            raise CarrierError("immutable finite probability on 2..48 sites required")
        p = tuple(rational(x) for x in self.weights)
        if min(p) < 0 or sum(p, Q(0)) != 1:
            raise CarrierError("nonnegative probability of exact mass one required")
        if type(self.source) is not str or not self.source.strip() or type(self.trace_hash) is not str:
            raise CarrierError("source identity must be explicit")
        if self.epoch is not None:
            _integer(self.epoch, 1)
        object.__setattr__(self, "weights", p)

    @property
    def fingerprint(self):
        return _hash((self.source, self.epoch, self.trace_hash,
                      tuple(str(x) for x in self.weights)))


def bbp_snapshot(epoch: int, sites: int) -> SourceSnapshot:
    """Exact bins of the original U0=0 source on [A,2A), with full-prefix hash."""
    a, m = _integer(epoch, 1), _integer(sites, 2, 48)
    states = source_states(2*a-1)
    counts = [0]*m
    for state in states[a:2*a]:
        counts[(m*state.remainder)//state.conductor] += 1
    history = tuple((s.n, str(s.conductor), str(s.numerator)) for s in states)
    return SourceSnapshot(tuple(Q(c, a) for c in counts),
                          "original BBP four signed poles; literal U0=0", a, _hash(history))


def verify_bbp_snapshot(snapshot: SourceSnapshot) -> bool:
    if type(snapshot) is not SourceSnapshot or snapshot.epoch is None:
        raise CarrierError("a source-labelled BBP epoch snapshot is required")
    return snapshot == bbp_snapshot(snapshot.epoch, len(snapshot.weights))


@dataclass(frozen=True)
class WindowProtocol:
    sites: int
    length: int
    amplitude: Q = Q(1)

    def __post_init__(self):
        m = _integer(self.sites, 2, 48)
        _integer(self.length, 1, m-1)
        amplitude = rational(self.amplitude)
        if not 0 < amplitude <= 1:
            raise CarrierError("nonnegative four-phase drive requires 0<amplitude<=1")
        object.__setattr__(self, "amplitude", amplitude)

    @property
    def conductor(self):
        return lcm(self.sites, 4)

    @property
    def fingerprint(self):
        return _hash(("forward window; tone -1; phases 0,pi/2,pi,3pi/2",
                      self.sites, self.length, str(self.amplitude)))


def _validate_profile(values, protocol):
    if (type(values) is not tuple or len(values) != protocol.sites or
            any(type(v) is not C or v.modulus != protocol.conductor for v in values)):
        raise CarrierError("complete translated profile on the declared cyclotomic clock required")


@dataclass(frozen=True)
class DrivenReadout:
    protocol: WindowProtocol
    source_fingerprint: str
    static: tuple[C, ...]
    coherent: tuple[C, ...]

    def __post_init__(self):
        if type(self.protocol) is not WindowProtocol:
            raise CarrierError("typed window protocol required")
        if type(self.source_fingerprint) is not str or not self.source_fingerprint:
            raise CarrierError("source snapshot binding required")
        _validate_profile(self.static, self.protocol)
        _validate_profile(self.coherent, self.protocol)


def observe(snapshot: SourceSnapshot, protocol: WindowProtocol) -> DrivenReadout:
    if type(snapshot) is not SourceSnapshot or type(protocol) is not WindowProtocol:
        raise CarrierError("typed source and protocol required")
    m, n, length = protocol.sites, protocol.conductor, protocol.length
    if len(snapshot.weights) != m:
        raise CarrierError("source and observer clocks disagree")
    static, coherent = [], []
    for y in range(m):
        r0, r1 = _zero(n), _zero(n)
        for j in range(length):
            p = snapshot.weights[(y+j) % m]
            r0 = r0 + C.scalar(n, p)
            r1 = r1 + _root(n, -(n//m)*j).scale(p)
        static.append(r0); coherent.append(r1)
    return DrivenReadout(protocol, snapshot.fingerprint, tuple(static), tuple(coherent))


@dataclass(frozen=True)
class PhaseFrame:
    protocol: WindowProtocol
    source_fingerprint: str
    phase: int
    values: tuple[C, ...]

    def __post_init__(self):
        if type(self.protocol) is not WindowProtocol:
            raise CarrierError("typed window protocol required")
        _integer(self.phase, 0, 3)
        if type(self.source_fingerprint) is not str or not self.source_fingerprint:
            raise CarrierError("source binding required")
        _validate_profile(self.values, self.protocol)
        if any(v != conjugate(v) for v in self.values):
            raise CarrierError("physical phase-cycle readings must be real")


def phase_cycle(snapshot: SourceSnapshot, protocol: WindowProtocol) -> tuple[PhaseFrame, ...]:
    """Y_theta=R0+epsilon Re(e^(i theta) R1), four nonnegative spatial masks."""
    readout = observe(snapshot, protocol)
    n = protocol.conductor
    frames = []
    for phase in range(4):
        shift = _root(n, phase*(n//4))
        values = []
        for r0, r1 in zip(readout.static, readout.coherent):
            z = shift*r1
            real = (z + conjugate(z)).scale(Q(1, 2))
            values.append(r0 + real.scale(protocol.amplitude))
        frames.append(PhaseFrame(protocol, snapshot.fingerprint, phase, tuple(values)))
    return tuple(frames)


def demodulate(frames: Sequence[PhaseFrame]) -> DrivenReadout:
    frames = tuple(frames)
    if len(frames) != 4 or any(type(f) is not PhaseFrame for f in frames):
        raise CarrierError("exactly four typed phase frames required")
    if {f.phase for f in frames} != set(range(4)):
        raise CarrierError("all four distinct phase settings are required")
    first = frames[0]
    if any(f.protocol != first.protocol or f.source_fingerprint != first.source_fingerprint
           for f in frames):
        raise CarrierError("phase frames mix protocols or source snapshots")
    ys = {f.phase: f.values for f in frames}
    amplitude, n = first.protocol.amplitude, first.protocol.conductor
    static, coherent = [], []
    imaginary_unit = _root(n, n//4)
    for j in range(first.protocol.sites):
        r0 = (ys[0][j]+ys[2][j]).scale(Q(1, 2))
        if r0 != (ys[1][j]+ys[3][j]).scale(Q(1, 2)):
            raise CarrierError("inconsistent phase-cycle DC readings")
        real = _sub(ys[0][j], ys[2][j]).scale(1/(2*amplitude))
        imag = _sub(ys[3][j], ys[1][j]).scale(1/(2*amplitude))
        static.append(r0); coherent.append(real+imaginary_unit*imag)
    return DrivenReadout(first.protocol, first.source_fingerprint,
                         tuple(static), tuple(coherent))


def reconstruct(readout: DrivenReadout, *, expected: SourceSnapshot | None = None) -> tuple[Q, ...]:
    """Local two-channel inverse plus range, positivity, mass and source checks."""
    if type(readout) is not DrivenReadout:
        raise CarrierError("typed two-channel readout required")
    protocol = readout.protocol
    m, n, length = protocol.sites, protocol.conductor, protocol.length
    unit = _root(n, -(n//m))
    omega = _root(n, -(n//m)*length)
    inverse = _root_minus_one_inverse(n, -(n//m)*length)
    probabilities = []
    for y in range(m):
        nxt = (y+1) % m
        delta0 = _sub(readout.static[nxt], readout.static[y])
        delta1 = _sub(unit*readout.coherent[nxt], readout.coherent[y])
        value = _sub(delta1, omega*delta0)*inverse
        if len(value.polynomial) != 1 or value.polynomial[0] < 0:
            raise CarrierError("recovered law is not a rational nonnegative probability")
        probabilities.append(value.polynomial[0])
    weights = tuple(probabilities)
    if sum(weights, Q(0)) != 1:
        raise CarrierError("recovered law has wrong probability mass")
    replay = observe(SourceSnapshot(weights), protocol)
    if replay.static != readout.static or replay.coherent != readout.coherent:
        raise CarrierError("two-channel profile fails realization coherence")
    if expected is not None:
        if type(expected) is not SourceSnapshot:
            raise CarrierError("expected source must be a snapshot")
        if readout.source_fingerprint != expected.fingerprint or weights != expected.weights:
            raise CarrierError("readout does not realize the declared source snapshot")
    return weights


def calibrate_constant_gain(readout: DrivenReadout) -> tuple[DrivenReadout, C]:
    """Recover one unknown nonzero complex channel gain from known total mass.

    Assumes a common position-independent gain on the entire coherent profile.
    Source/time-varying drift is outside this calibration model. The returned
    profile must still pass reconstruct(), including its range and mass checks.
    """
    if type(readout) is not DrivenReadout:
        raise CarrierError("typed readout required")
    p = readout.protocol
    m, n = p.sites, p.conductor
    total0, total1 = _zero(n), _zero(n)
    for value in readout.static:
        total0 = total0 + value
    for value in readout.coherent:
        total1 = total1 + value
    if total0 != C.scalar(n, p.length):
        raise CarrierError("static mass reference is not calibrated")
    u = _root(n, -(n//m))
    inverse_h = _sub(u, C.scalar(n, 1))*_root_minus_one_inverse(n, -(n//m)*p.length)
    gain = total1*inverse_h
    inverse_gain = _field_inverse(gain)
    corrected = DrivenReadout(p, readout.source_fingerprint, readout.static,
                              tuple(inverse_gain*z for z in readout.coherent))
    return corrected, gain


def binned_moment(snapshot: SourceSnapshot, mode: int) -> C:
    _integer(abs(mode) if type(mode) is int else mode)
    if type(snapshot) is not SourceSnapshot:
        raise CarrierError("source snapshot required")
    m = len(snapshot.weights)
    out = _zero(m)
    for j, p in enumerate(snapshot.weights):
        out = out + _root(m, -mode*j).scale(p)
    return out


def b2_scan_coefficient(law: CircleLaw, pins: int, mode: int) -> C:
    """Exact sampled Fourier coefficient; multiply by 2*pi²*h² to estimate m_h.

    The coefficient is algebraic. Its analytic normalization and the bounded
    infinite alias tail are proved in the accompanying dossier.
    """
    m = _integer(pins, 2, 100)
    if type(mode) is not int or mode == 0 or 2*abs(mode) > m:
        raise CarrierError("nonzero mode within the declared scan band required")
    if type(law) is not CircleLaw:
        raise CarrierError("exact circle law required")
    out = _zero(m)
    for j in range(m):
        out = out + _root(m, -mode*j).scale(pin_surface(law, Q(j, m))/m)
    return out


def b2_scan_alias_bound(pins: int, mode: int) -> Q:
    m = _integer(pins, 2, 100)
    if type(mode) is not int or mode == 0 or 2*abs(mode) > m:
        raise CarrierError("nonzero mode within the declared scan band required")
    return Q(6*mode*mode, m*m)
