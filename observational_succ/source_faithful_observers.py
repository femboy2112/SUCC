"""Source-labelled carry interventions and calibrated arithmetic parameter boxes.

Paper authority: research/2026-10-23/SOURCE_FAITHFUL_OBSERVERS.md. The arbitrary
carrier quotient theorem is proved there, not by finite tests here. Existing
future_safe_quotient.py remains the finite Moore/Mealy implementation.

All experiments in this module are mathematical/synthetic. No string, matrix
entry or successful interval calculation authenticates a physical instrument.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction as Q

from .reality_pin_arithmetic import log_interval, primes_through
from .reality_pin_continuum import exp_interval


class ObserverSourceError(ValueError):
    """The declared exact source or calibration contract was violated."""


def _integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise ObserverSourceError("integer outside declared domain")
    return x


def _q(x):
    if type(x) not in (int, Q):
        raise ObserverSourceError("exact int/Fraction required; floats are not certificates")
    return Q(x)


def _band(x):
    if type(x) is not tuple or len(x) != 2:
        raise ObserverSourceError("closed interval needs two exact endpoints")
    lo, hi = map(_q, x)
    if lo > hi:
        raise ObserverSourceError("reversed interval")
    return lo, hi


def quotient(n, radix):
    """The one-based authentic source quotient, not n//radix."""
    _integer(n, 1)
    _integer(radix, 2)
    return (n - 1) // radix + 1


def carry_horizon_partition(radix, horizon):
    """Residue classes with equal quotient readings at all times 0..horizon.

    Formula is valid for every block m>=1 on N>=1; no cyclic wrap or cutoff.
    """
    _integer(radix, 2)
    _integer(horizon)
    h = min(horizon, radix - 1)
    return (tuple(range(radix - h)),) + tuple((r,) for r in range(radix - h, radix))


def carry_separator(left, right, radix):
    """Shortest nonnegative successor time separating the quotient readings."""
    a, b = quotient(left, radix), quotient(right, radix)
    if left == right:
        return None
    if a != b:
        return 0
    r, s = (left - 1) % radix, (right - 1) % radix
    return radix - max(r, s)


def recover_carry(radix, initial_quotient, readings):
    """Decode the frozen 'stop at first carry, else at p-1' protocol.

    readings contains every q(S^t n), including t=0. Reject early stopping,
    missing readings and continuing beyond the declared stop rule.
    """
    _integer(radix, 2)
    _integer(initial_quotient, 1)
    if type(readings) is not tuple or not 1 <= len(readings) <= radix:
        raise ObserverSourceError("immutable nonempty sequential transcript required")
    if any(type(x) is not int for x in readings) or readings[0] != initial_quotient:
        raise ObserverSourceError("initial calibration mismatch")
    for t, value in enumerate(readings):
        if value == initial_quotient:
            continue
        if value != initial_quotient + 1 or t == 0 or t != len(readings)-1:
            raise ObserverSourceError("not a first-carry stopping transcript")
        residue = radix - t
        if not 1 <= residue < radix:
            raise ObserverSourceError("invalid carry time")
        return residue
    if len(readings) != radix:
        raise ObserverSourceError("unresolved: no carry yet and horizon is too short")
    return 0


def carry_protocol(n, radix, action_cost=1, read_cost=0):
    """Execute a synthetic nondestructive quotient-read/SUCC protocol.

    The unknown input n is used by the synthetic source only. The decoder sees
    radix, initial quotient, and the public transcript. Cost includes initial
    reading and each later reading. Worst-case actions p-1 are sharp.
    """
    m = quotient(n, radix)
    action_cost, read_cost = map(_q, (action_cost, read_cost))
    if action_cost < 0 or read_cost < 0:
        raise ObserverSourceError("costs must be nonnegative")
    readings = [m]
    for t in range(1, radix):
        readings.append(quotient(n+t, radix))
        if readings[-1] != m:
            break
    transcript = tuple(readings)
    residue = recover_carry(radix, m, transcript)
    steps = len(transcript)-1
    return {"initial_quotient": m, "readings": transcript, "residue": residue,
            "source_reconstruction": radix*(m-1)+residue+1,
            "successor_actions": steps, "readings_count": len(transcript),
            "cost": steps*action_cost+len(transcript)*read_cost,
            "physical_measurement_authenticated": False}


def _outward(band, bits):
    """Outward dyadic rounding bounds rational growth without losing soundness."""
    lo, hi = band
    scale = 1 << bits
    return Q((lo*scale).__floor__(), scale), Q((hi*scale).__ceil__(), scale)


def _mul(a, b):
    values = tuple(x*y for x in a for y in b)
    return min(values), max(values)


def _div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ObserverSourceError("division interval contains zero")
    values = tuple(x/y for x in a for y in b)
    return min(values), max(values)


def _exp_band(x, bits):
    if x[0] < 0:
        raise ObserverSourceError("this exponential enclosure requires nonnegative arguments")
    width = Q(1, 1 << bits)
    return _outward((exp_interval(x[0], width)[0], exp_interval(x[1], width)[1]), bits)


@dataclass(frozen=True)
class ArithmeticPin:
    """Conditional enclosures for M=gK+bI, with g>0 and sigma>1.

    No offset is returned: the three off-diagonal entries do not identify b.
    Dependencies between boxes are discarded conservatively.
    """
    sigma: tuple[Q, Q]
    gain: tuple[Q, Q]
    lam: tuple[Q, Q]
    physical_measurement_authenticated: bool = field(default=False, init=False)

    def __post_init__(self):
        for value in (self.sigma, self.gain, self.lam):
            _band(value)
        if self.sigma[0] <= 1 or self.gain[0] <= 0:
            raise ObserverSourceError("pin domain requires sigma>1 and positive gain")


def pin_arithmetic_entries(x23, x13, x15, *, bits=40, log_terms=18):
    """Enclose lambda,sigma,g from exact bands for M23,M13,M15.

    Requires the *whole supplied ratio band* to certify sigma>1. Refusal on a
    broad band is inconclusive, not evidence that the source is inconsistent.
    Source identity M=gK+bI is a hypothesis, not inferred from fitting 3 entries.
    """
    _integer(bits, 8)
    _integer(log_terms, 1)
    x, y, z = map(_band, (x23, x13, x15))
    if z[0] <= 0 or y[0] <= z[1]:
        raise ObserverSourceError("positive separated prime-entry bands required")
    ratio = _div(y, z)
    numerator = (log_interval(ratio[0], log_terms)[0],
                 log_interval(ratio[1], log_terms)[1])
    denominator = log_interval(Q(5, 3), log_terms)
    sigma = _outward(_div(numerator, denominator), bits)
    if sigma[0] <= 1:
        raise ObserverSourceError("precision/source domain unresolved: sigma>1 not certified")
    log3 = _outward(log_interval(Q(3), log_terms), bits)
    exponent = _outward(_mul(sigma, log3), bits)
    gain = _outward(_mul(y, _exp_band(exponent, bits)), bits)
    if gain[0] <= 0:
        raise ObserverSourceError("positive gain unresolved at this precision")
    lam = _outward(_div(x, gain), bits)
    return ArithmeticPin(sigma, gain, lam)


def arithmetic_prime_holdout(pin, prime, *, bits=40, log_terms=18):
    """Predicted band M_(1,p)=g*p^-sigma for a predeclared prime p>=7.

    p=2 is contaminated by the successor channel; p=3,5 fitted the pin.
    Any excluded composite needs its own source law, not this primitive formula.
    """
    if type(pin) is not ArithmeticPin:
        raise ObserverSourceError("typed conditional pin required")
    _integer(prime, 7)
    _integer(bits, 8)
    _integer(log_terms, 1)
    if prime not in primes_through(prime):
        raise ObserverSourceError("a prime holdout source is required")
    exponent = _outward(_mul(pin.sigma, _outward(log_interval(Q(prime), log_terms), bits)), bits)
    return _outward(_div(pin.gain, _exp_band(exponent, bits)), bits)


def off_diagonal_entry(n, i, j, lam=1, sigma=2, gain=1, offset=0):
    """Independent exact model for selected source entries at integer sigma>=2.

    Scalar offset times I contributes only on the diagonal. This function
    deliberately rejects diagonal entries, whose log term needs enclosures.
    n is the source horizon, and all declared entries must lie inside it.
    """
    _integer(n, 1)
    _integer(i, 1)
    _integer(j, 1)
    _integer(sigma, 2)
    lam, gain, _ = map(_q, (lam, gain, offset))
    if max(i, j) > n or i == j or gain <= 0:
        raise ObserverSourceError("distinct in-horizon labels and positive gain required")
    i, j = sorted((i, j))
    value = lam if j == i+1 else Q()
    if j % i == 0:
        p = j//i
        if p in primes_through(p):
            value += Q(1, p**sigma)
    return gain*value


def polarized_entry(plus_energy, minus_energy):
    """Band for Re M_ij from energies of (e_i +/- e_j)/sqrt(2).

    The difference removes one common additive sensor offset. The state labels,
    relative sign, common gain and nondestructive/ensemble access are supplied
    hypotheses; a fit alone certifies none of them.
    """
    plus, minus = _band(plus_energy), _band(minus_energy)
    return (plus[0]-minus[1])/2, (plus[1]-minus[0])/2
