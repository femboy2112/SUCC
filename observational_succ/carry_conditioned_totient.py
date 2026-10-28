"""Literal-carry Oily totients and exact dyadic character transport.

The source adapter is the existing integer-native zero-seeded BBP engine.
The declared coupling adds the actual L-carry word to the auxiliary packet
grade J.  This is source authenticated, but no canonical uniqueness or signed
Fourier saving follows.  Odd primitive filtering exposes a growing alias mode.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd

from .integer_bbp_carrier import source_states
from .oily_macaroni_totient import compiler_error, packet_polynomial


def _integer(value, minimum=0, maximum=100000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError("bounded ordinary integer required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact rational required")
    return Q(value)


@dataclass(frozen=True)
class CarryWord:
    time: int
    depth: int
    radix_power: int
    word: int
    residue: int
    carries: tuple[int, ...]
    conductor: int
    forcing_numerator: int
    final_remainder: int
    initial_phase: Q
    final_phase: Q
    source_id: str = "Q:Coherent-Main-X-four-pole-BBP:zero-seed"

    @property
    def conductor_decoded_residue(self):
        """Q A = 16^L Q{x_n}+B-R, reduced modulo 16^L."""
        return ((self.forcing_numerator-self.final_remainder)
                * pow(self.conductor, -1, self.radix_power)) % self.radix_power

    @property
    def is_primitive(self):
        return gcd(self.word, self.radix_power) == 1


def authentic_carry_words(horizon: int, depth: int) -> tuple[CarryWord, ...]:
    """Words at n=1..N, retaining full integer lifts and the common Q_(n+L).

    The word may exceed 16^L-1 because a literal forced carry can equal 16.
    Its cyclic residue, rather than a silently clipped digit tape, is used.
    """
    _integer(horizon, 1, 2000)
    _integer(depth, 1, 64)
    if horizon+depth > 2000:
        raise ValueError("exact source budget exceeded")
    states = source_states(horizon+depth)
    q = 16**depth
    out = []
    for n in range(1, horizon+1):
        left, right = states[n], states[n+depth]
        conductor = right.conductor
        left_lift = Q(left.numerator, left.conductor)
        right_lift = Q(right.numerator, conductor)
        forcing = conductor*(right_lift-q*left_lift)
        if forcing.denominator != 1:
            raise ArithmeticError("source conductor failed to clear forcing")
        carries = tuple(states[k].integer_part-16*states[k-1].integer_part
                        for k in range(n+1, n+depth+1))
        word = right.integer_part-q*left.integer_part
        out.append(CarryWord(n, depth, q, word, word % q, carries,
                             conductor, forcing.numerator, right.remainder,
                             Q(left.remainder, left.conductor),
                             Q(right.remainder, conductor)))
    return tuple(out)


def word_distribution(words: tuple[CarryWord, ...]) -> tuple[Q, ...]:
    """Exact empirical cyclic carry law. It is not assumed uniform."""
    if not words or any(type(w) is not CarryWord for w in words):
        raise ValueError("nonempty source word history required")
    q = words[0].radix_power
    _integer(q, 2, 4096)
    if any(w.radix_power != q for w in words):
        raise ValueError("one common word modulus required")
    out = [Q() for _ in range(q)]
    for word in words:
        out[word.residue] += Q(1, len(words))
    return tuple(out)


def endpoint_wrapped_packet(modulus: int) -> tuple[Q, ...]:
    """Exact law of J mod q for w_j=(j+1)/2^(j+2), with no grade cutoff."""
    q = _integer(modulus, 1, 4096)
    t = Q(1, 2**q)
    return tuple(Q(1, 2**(a+2))*((a+1)/(1-t)+q*t/(1-t)**2)
                 for a in range(q))


def cyclic_shift(values, steps: int):
    """Mass-preserving deterministic SUCC on a declared cyclic law."""
    vals = tuple(_rational(v) for v in values)
    if not vals or type(steps) is not int:
        raise ValueError("nonempty rational vector and integer shift required")
    q = len(vals)
    return tuple(vals[(a-steps) % q] for a in range(q))


def endpoint_carry_packet_law(words: tuple[CarryWord, ...]) -> tuple[Q, ...]:
    """Law of A_(n,L)+J mod q, n uniform, J at the endpoint packet law.

    This retains literal carries but uses the limiting packet law.  The
    genuine time-n packet replacement has the explicit H_N/N error below.
    """
    law = word_distribution(words)
    packet = endpoint_wrapped_packet(len(law))
    out = [Q() for _ in law]
    for a, weight in enumerate(law):
        if weight:
            for b, mass in enumerate(packet):
                out[(a+b) % len(law)] += weight*mass
    return tuple(out)


def finite_source_carry_packet_law(words: tuple[CarryWord, ...], depth: int):
    """Exact finite normalized source law for A_(n,L)+J, 0<=J<M.

    Uses the existing source packet polynomial rather than an independent
    stochastic law.  At each n the rational packet integrals are normalized
    before averaging times; a universal TV error is recorded separately.
    """
    _integer(depth, 1, 64)
    word_distribution(words)  # validate the finite common modulus
    q = words[0].radix_power
    polynomials = tuple(packet_polynomial(j) for j in range(depth))
    out = [Q() for _ in range(q)]
    for word in words:
        masses = tuple(sum((c/Q(8*word.time+k+1)
                            for k, c in enumerate(poly)), Q())
                       for poly in polynomials)
        total = sum(masses, Q())
        if total <= 0 or any(mass < 0 for mass in masses):
            raise ArithmeticError("positive source packet integral failed")
        for j, mass in enumerate(masses):
            out[(word.residue+j) % q] += mass/(total*len(words))
    return tuple(out)


def primitive_projection(values):
    """Actual arithmetic unit projector on Z/q; q is the word modulus."""
    vals = tuple(_rational(v) for v in values)
    if not vals:
        raise ValueError("nonempty cyclic law required")
    return tuple(v if gcd(a, len(vals)) == 1 else Q()
                 for a, v in enumerate(vals))


def invert_endpoint_packet(values):
    """Exact inverse (2I-S)^2: convolution has not destroyed information.

    The inverse has l1 operator norm at most 9. It is signed, not a Markov
    kernel.  On the authenticated convolved law it recovers the carry law.
    """
    vals = tuple(_rational(v) for v in values)
    one, two = cyclic_shift(vals, 1), cyclic_shift(vals, 2)
    return tuple(4*a-4*b+c for a, b, c in zip(vals, one, two))


def dyadic_character(values, frequency: int) -> tuple[Q, ...]:
    """EXACT character in Q[X]/(X^(q/2)+1), X=primitive qth root.

    For q a power of two, this is its cyclotomic field basis. Thus these
    tuples prove equalities of complex characters without float tolerances.
    They do not provide inequalities of complex absolute values.
    """
    vals = tuple(_rational(v) for v in values)
    q = len(vals)
    if q < 2 or q & (q-1) or type(frequency) is not int:
        raise ValueError("dyadic cyclic law and integer frequency required")
    out = [Q() for _ in range(q//2)]
    for a, value in enumerate(vals):
        exponent = (frequency*a) % q
        out[exponent % (q//2)] += value if exponent < q//2 else -value
    return tuple(out)


def carry_packet_transport_budget(horizon: int, depth: int,
                                 frequency: int, packet_depth: int | None = None):
    """Rational ALL-N error budgets; none bounds a selected sum by o(N).

    Word character F vs selected U character S/N:
      <=119|h|/(648N)+112|h|/(15*16^L).
    Time-n packet vs endpoint translated packet law, for bounded tests:
      <=H_N/N; finite normalized M layers add <=2*rho_M.
    """
    _integer(horizon, 1)
    _integer(depth, 1, 64)
    if type(frequency) is not int:
        raise ValueError("integer frequency required")
    harmonic = sum((Q(1, n) for n in range(1, horizon+1)), Q())
    packet = harmonic/horizon
    if packet_depth is not None:
        packet += 2*compiler_error(packet_depth)
    return {"word_to_selected": Q(119*abs(frequency), 648*horizon)
                                + Q(112*abs(frequency), 15*16**depth),
            "source_packet_to_endpoint": packet,
            "proves_selected_cancellation": False}
