"""Exact finite learning adapters; no new category or asymptotic authority.

The source engine is main's selected_orbit. Unwrapped lifts and carries are
retained separately. All seed families and probe capabilities are declared.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product

from observational_succ.selected_orbit import SelectedOrbit, original_forcing
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
from observational_succ.operational_yoneda_descent import BeliefGame, ObservationPathCategory


@dataclass(frozen=True)
class SourceSignature:
    radix: int = 16
    weights: tuple = (4, -2, -1, -1)
    poles: tuple = (7, 4, 3, 2)
    chronology: str = "U_n=16 U_(n-1)+r(n), n>=1"
    baseline: str = "d32342d375f44ddf62221ad6aff2f534abdc0a03"
    boundary: Q = Q(0)

    def authenticate_original_zero(self):
        if self != SourceSignature():
            raise ValueError("signature differs from the pinned original zero source")
        return True


@dataclass(frozen=True)
class LiftedHistory:
    signature: SourceSignature
    unwrapped: tuple
    circle: tuple
    carries: tuple


def exact_history(seed, horizon):
    if type(horizon) is not int or horizon < 0:
        raise ValueError("nonnegative integer horizon required")
    seed = Q(seed)
    engine = SelectedOrbit(seed)
    unwrapped, phases, carries = [seed], [seed % 1], []
    for n in range(1, horizon + 1):
        forcing = original_forcing(n)
        unwrapped.append(16 * unwrapped[-1] + forcing)
        lifted_circle = 16 * phases[-1] + forcing
        carries.append(lifted_circle // 1)
        phases.append(lifted_circle % 1)
        assert phases[-1] == engine.state(n) == unwrapped[-1] % 1
    return LiftedHistory(SourceSignature(boundary=seed), tuple(unwrapped),
                         tuple(phases), tuple(carries))


def calibrated_digits(seed, depth):
    """Declared ideal source reference; exact finite rational arithmetic."""
    h, zero = exact_history(seed, depth), exact_history(0, depth)
    return tuple(int(16 * ((x - y) % 1))
                 for x, y in zip(h.circle[:depth], zero.circle[:depth]))


def digit_carrier(seeds, depth, labels):
    """Finite main-API adapter with immutable source IDs and hidden audit state.

    `pin` reads a calibrated digit then advances; `wait` only advances.
    Hidden simulator index (time, original candidate) is never a report.
    """
    seeds = tuple(Q(s) for s in seeds)
    if (not seeds or len(set(seeds)) != len(seeds) or type(depth) is not int
            or depth < 1 or len(labels) != len(seeds)):
        raise ValueError("distinct seeds, positive depth, one target per seed required")
    width, count = len(seeds), len(seeds) * (depth + 1)
    words = tuple(calibrated_digits(s, depth) for s in seeds)
    enabled = tuple(t < depth for t in range(depth + 1) for _ in seeds)
    transitions = tuple(min(t + 1, depth) * width + i
                        for t in range(depth + 1) for i in range(width))
    pin = tuple(words[i][t] if t < depth else 0
                for t in range(depth + 1) for i in range(width))
    source_id = "original-four-pole:declared-rational-candidates:" + repr(seeds)
    field = FiniteCarrier(count, (
        Instrument("pin", pin, transitions, enabled),
        Instrument("wait", (0,) * count, transitions, enabled)),
        source_id, "source-zero-phase-calibration:exact-16-cells")
    targets = tuple(str(v) for _ in range(depth + 1) for v in labels)
    return field, tuple(range(width)), targets


def history_category(seeds, depth, labels):
    field, sources, targets = digit_carrier(seeds, depth, labels)
    game = BeliefGame.build(field, sources, targets, target_id="declared-ancestral-target")
    return ObservationPathCategory(game, depth)


def residual_layers(targets, radix, depth):
    """Minimal online memory signatures for a FULL fixed-length word domain.

    targets is lexicographically ordered on {0,...,radix-1}^depth.
    Prefixes are equivalent iff their entire remaining target tables agree.
    The theorem is not asserted for partially defined/adaptive languages.
    """
    if type(radix) is not int or radix < 2 or type(depth) is not int or depth < 0:
        raise ValueError("integer radix >=2 and nonnegative depth required")
    targets = tuple(targets)
    if len(targets) != radix ** depth:
        raise ValueError("complete target table required")
    layers = []
    for t in range(depth + 1):
        suffixes = radix ** (depth - t)
        rows = tuple(targets[p*suffixes:(p+1)*suffixes] for p in range(radix**t))
        unique = tuple(dict.fromkeys(rows))
        owner = tuple(unique.index(r) for r in rows)
        layers.append((unique, owner))
    # Verify the right-congruence law, not just the cardinalities.
    for t in range(depth):
        seen = {}
        for prefix, state in enumerate(layers[t][1]):
            for digit in range(radix):
                key = state, digit
                next_state = layers[t+1][1][radix*prefix+digit]
                if key in seen and seen[key] != next_state:
                    raise ArithmeticError("residual quotient is not a lawful update")
                seen[key] = next_state
    return tuple(layers)


def late_index_target(data_digits):
    """Binary target: later hex address selects one bit of earlier data.

    Uses the smallest address length encoding all 4*data_digits bit indices.
    Extra addresses wrap modulo 4*data_digits, making the domain complete.
    """
    if type(data_digits) is not int or data_digits < 1:
        raise ValueError("positive data length required")
    address_digits = 1
    while 16 ** address_digits < 4 * data_digits:
        address_digits += 1
    depth = data_digits + address_digits
    if depth > 4:
        raise ValueError("explicit table limited to 65536 entries")
    table = []
    for word in product(range(16), repeat=depth):
        address = 0
        for digit in word[data_digits:]:
            address = 16 * address + digit
        address %= 4 * data_digits
        table.append((word[address // 4] >> (address % 4)) & 1)
    return tuple(table), depth


def affine_open_phase(seed, n, t, harmonic=1):
    """Exact phase of K_(n,t); NOT a source-corrected closed holonomy."""
    if any(type(k) is not int or k < 0 for k in (n,t)):
        raise ValueError("nonnegative integer times required")
    if type(harmonic) is not int:
        raise ValueError("integer Fourier harmonic required")
    h = exact_history(seed, max(n, t))
    return (harmonic * (h.unwrapped[n] - h.unwrapped[t])) % 1


def seed_charge(times, coefficients):
    if len(times) != len(coefficients):
        raise ValueError("one integer coefficient per time required")
    if any(type(t) is not int or t < 0 for t in times):
        raise ValueError("nonnegative integer times required")
    if any(type(c) is not int for c in coefficients):
        raise ValueError("integer Fourier coefficients required")
    return sum(c * 16**t for c, t in zip(coefficients, times))
