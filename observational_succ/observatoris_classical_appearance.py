"""Model-relative classical appearance as a FAMILY of exact diagnostics.

Principia Observatoris, Second Forge.  The founding note (PR #618, section 8)
proposes that a system *appears* classical when observation is free, the
effective law is predictive, and geometry matches computation.  This module
gives exact finite instruments for three of those diagnostics and exact
witnesses showing that they are logically independent, so that no single
predicate "classical" is available.  Alignment (no hidden wire) is handled in
observatoris_response_geometry.

Deterministic carriers reuse the existing carrier_relative_targets contract.
The qubit computations are exact in Q(sqrt 2) on a DECLARED two-dimensional
Hilbert model with three declared operations.  Nothing here says what any
physical system is; "appears classical" always means "relative to a toolkit".
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from .carrier_relative_targets import Carrier, Instrument, behavioral_partition, trace


# --- Diagnostic B: free (non-disturbing) observation -----------------------

def static_partition(carrier: Carrier) -> tuple[tuple[int, ...], ...]:
    """States grouped by their joint ONE-SHOT readouts, with no dynamics."""
    groups: dict[tuple, list[int]] = {}
    for x in range(carrier.size):
        key = tuple(a.outputs[x] for a in carrier.instruments)
        groups.setdefault(key, []).append(x)
    return tuple(tuple(g) for g in groups.values())


def disturbing_instruments(carrier: Carrier,
                           readouts: tuple[str, ...] | None = None) -> tuple[tuple[str, int], ...]:
    """Pairs (instrument, state) where using the instrument changes the
    behaviour class of the state.

    `readouts` names the operations DECLARED to be observations; the others are
    dynamics or actions and are expected to move the state.  With `readouts`
    omitted every operation is treated as an observation.  Behaviour classes
    are always taken with respect to the whole toolkit.
    """
    owner = {x: j for j, block in enumerate(behavioral_partition(carrier)) for x in block}
    names = {a.name for a in carrier.instruments}
    if readouts is not None and not set(readouts) <= names:
        raise ValueError("declared readout outside the toolkit")
    return tuple((a.name, x) for a in carrier.instruments for x in range(carrier.size)
                 if (readouts is None or a.name in readouts)
                 and owner[a.next_states[x]] != owner[x])


def is_free_observation(carrier: Carrier, readouts: tuple[str, ...] | None = None) -> bool:
    """No declared observation changes the behaviour class of any state."""
    return not disturbing_instruments(carrier, readouts)


def transcript_is_static(carrier: Carrier, max_length: int) -> bool:
    """Every transcript of every word up to max_length equals the list of
    one-shot readouts of the INITIAL state (order-free, repeatable)."""
    names = tuple(a.name for a in carrier.instruments)
    for length in range(max_length + 1):
        for word in product(names, repeat=length):
            for x in range(carrier.size):
                history, _ = trace(carrier, x, word)
                want = tuple((n, carrier.operation(n).chart, carrier.operation(n).outputs[x])
                             for n in word)
                if history != want:
                    return False
    return True


# --- Diagnostic C: predictive closure at a horizon -------------------------

def window_carrier(bits: int, width: int) -> Carrier:
    """A cyclic shift register observed through a window of `width` bits.

    The law is deterministic, invertible and local, and the readout does not
    disturb.  It is the finite exact stand-in for a chaotic map read at finite
    resolution: each step moves one unseen bit into view.
    """
    if not (1 <= width <= bits and 2 ** bits <= 24):
        raise ValueError("window must fit the register and the carrier size limit")
    size = 2 ** bits
    mask = size - 1

    def rot(x: int) -> int:
        return ((x << 1) & mask) | (x >> (bits - 1))

    look = Instrument("look", "window", tuple(Fraction(x >> (bits - width))
                                              for x in range(size)), tuple(range(size)))
    step = Instrument("step", "tick", tuple(Fraction(0) for _ in range(size)),
                      tuple(rot(x) for x in range(size)))
    return Carrier(f"shift-{bits}-{width}", size, (look, step))


def future_readouts(carrier: Carrier, steps: int) -> dict[Fraction, set[Fraction]]:
    """For each initial `look` value, the set of `look` values after `steps`
    uses of `step`, over all source states compatible with that initial value."""
    look, step = carrier.operation("look"), carrier.operation("step")
    out: dict[Fraction, set[Fraction]] = {}
    for x in range(carrier.size):
        y = x
        for _ in range(steps):
            y = step.next_states[y]
        out.setdefault(look.outputs[x], set()).add(look.outputs[y])
    return out


def predictive_ambiguity(carrier: Carrier, steps: int) -> int:
    """Worst-case number of future readouts compatible with one present readout."""
    return max(len(v) for v in future_readouts(carrier, steps).values())


def window_ambiguity_formula(bits: int, width: int, steps: int) -> int:
    """Closed form for `window_carrier`: 2 ** min(s, bits-s, width, bits-width)
    with s = steps mod bits.  The register is cyclic, so the unseen part of the
    future window grows, saturates, and then SHRINKS again: prediction fails at
    some horizons and recovers at others (it is perfect whenever s = 0)."""
    s = steps % bits
    return 2 ** min(s, bits - s, width, bits - width)


# --- A declared Hilbert model with exact amplitudes in Q(sqrt 2) -----------

class Root2:
    """a + b*sqrt(2) with rational a, b."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(self, o):
        return Root2(self.a + o.a, self.b + o.b)

    def __mul__(self, o):
        return Root2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    def __eq__(self, o):
        return isinstance(o, Root2) and (self.a, self.b) == (o.a, o.b)

    def __hash__(self):
        return hash((self.a, self.b))

    def rational(self) -> Fraction:
        if self.b != 0:
            raise ValueError("not rational")
        return self.a


_HALF_ROOT = Root2(0, Fraction(1, 2))          # 1/sqrt(2)
_NEG_HALF_ROOT = Root2(0, Fraction(-1, 2))
QUBIT_OPERATIONS = ("X", "H", "Z")              # two gates and a projective Z readout


def qubit_transcripts(word: tuple[str, ...]) -> dict[tuple[int, ...], Fraction]:
    """Exact Born probabilities of every Z-outcome string for `word` from |0>.

    Unnormalised branches are kept, so no square root is ever taken: the
    probability of a branch is the squared norm of its final vector.
    """
    branches: dict[tuple[int, ...], tuple[Root2, Root2]] = {(): (Root2(1), Root2(0))}
    for op in word:
        updated: dict[tuple[int, ...], tuple[Root2, Root2]] = {}
        for outcomes, (u, v) in branches.items():
            if op == "X":
                updated[outcomes] = (v, u)
            elif op == "H":
                updated[outcomes] = (_HALF_ROOT * u + _HALF_ROOT * v,
                                     _HALF_ROOT * u + _NEG_HALF_ROOT * v)
            elif op == "Z":
                if u != Root2(0):
                    updated[outcomes + (0,)] = (u, Root2(0))
                if v != Root2(0):
                    updated[outcomes + (1,)] = (Root2(0), v)
            else:
                raise ValueError("operation outside the declared toolkit")
        branches = updated
    return {k: (u * u + v * v).rational() for k, (u, v) in branches.items()}


def classical_bit_transcripts(word: tuple[str, ...]) -> dict[tuple[int, ...], Fraction]:
    """A one-bit deterministic machine: X flips, Z reads without disturbing.
    It has no H; words containing H are outside its toolkit."""
    bit, seen = 0, []
    for op in word:
        if op == "X":
            bit ^= 1
        elif op == "Z":
            seen.append(bit)
        else:
            raise ValueError("operation outside the declared toolkit")
    return {tuple(seen): Fraction(1)}


def classical_four_state_transcripts(word: tuple[str, ...]) -> dict[tuple[int, ...], Fraction]:
    """A four-state classical STOCHASTIC machine on {0, 1, +, -}.

    X fixes + and -, swaps 0 and 1; H swaps 0 with + and 1 with -; the Z
    readout of + or - is a fair coin that resets the state to its outcome.
    """
    x_map = {"0": "1", "1": "0", "+": "+", "-": "-"}
    h_map = {"0": "+", "+": "0", "1": "-", "-": "1"}
    dist: dict[tuple[tuple[int, ...], str], Fraction] = {((), "0"): Fraction(1)}
    for op in word:
        updated: dict[tuple[tuple[int, ...], str], Fraction] = {}

        def add(key, p):
            updated[key] = updated.get(key, Fraction(0)) + p

        for (outcomes, state), p in dist.items():
            if op == "X":
                add((outcomes, x_map[state]), p)
            elif op == "H":
                add((outcomes, h_map[state]), p)
            elif op == "Z":
                if state in "01":
                    add((outcomes + (int(state),), state), p)
                else:
                    add((outcomes + (0,), "0"), p / 2)
                    add((outcomes + (1,), "1"), p / 2)
            else:
                raise ValueError("operation outside the declared toolkit")
        dist = updated
    out: dict[tuple[int, ...], Fraction] = {}
    for (outcomes, _), p in dist.items():
        out[outcomes] = out.get(outcomes, Fraction(0)) + p
    return out


def final_readout_marginal(dist: dict[tuple[int, ...], Fraction]) -> dict[int, Fraction]:
    """Distribution of the LAST recorded outcome."""
    out: dict[int, Fraction] = {}
    for outcomes, p in dist.items():
        out[outcomes[-1]] = out.get(outcomes[-1], Fraction(0)) + p
    return out
