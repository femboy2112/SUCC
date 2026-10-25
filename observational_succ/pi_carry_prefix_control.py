"""Exact finite controls for incomplete BBP source authentication.

These controls change y_0. They do not counterfeit the selected source y_0=0,
and every constructed trajectory eventually equals the selected trajectory.
Paper proof: research/2026-10-24/PI_LAG_ADVERSARIAL_REVIEW.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .pi_source_collision import bbp_states, tail_upper


def _natural(value: int, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f"integer at least {lower} required")
    return value


@dataclass(frozen=True)
class CarryPrefixControl:
    first: int
    last: int
    cells: int
    prefix_length: int
    odd_modulus: int
    depth: int
    initial: Q
    target_initial: Q
    prefix_radius: Q
    lift_lower: Q
    lift_upper: Q
    phases: tuple[Q, ...]

    @property
    def diameter_upper(self) -> Q:
        """Width of one real interval containing all displayed phase lifts."""
        return self.lift_upper - self.lift_lower


def carry_prefix_control(first: int, last: int, cells: int,
                         prefix_length: int = 0,
                         odd_modulus: int = 1) -> CarryPrefixControl:
    """Preserve finite early carries and odd data; saturate a later window.

    The caller must choose first > prefix_length, 2*16**(-first) less than
    the exact prefix cylinder radius, and tail_upper(first) < 1/(2*cells).
    The result uses the complete authentic forcing with a DIFFERENT nonzero
    rational initial state. Its initial numerator is a multiple of the
    prescribed odd modulus before reduction. It coalesces by ``depth``.
    All calculations, including the rounding choice, are exact rational.
    """
    _natural(first, 1)
    _natural(last, first)
    _natural(cells, 1)
    _natural(prefix_length)
    _natural(odd_modulus, 1)
    if odd_modulus % 2 == 0:
        raise ValueError("odd modulus required")
    if first <= prefix_length:
        raise ValueError("target window must follow the retained carry prefix")
    source = bbp_states(last)
    prefix_radius = min((Q(1)-source[n])/16**n
                        for n in range(1, prefix_length+1)) if prefix_length else Q(1)
    if 2*Q(1, 16**first) >= prefix_radius:
        raise ValueError("target starts too early for the retained carry prefix")
    beta = tail_upper(first)
    if beta >= Q(1, 2*cells):
        raise ValueError("target resolution exceeds the proved tail budget")

    # Finite Green tail h_n=sum_{j=n+1}^last 16**(n-j)*r(j).
    # Compute from unwrapped source increments, not any supplied pi digits.
    from .pi_source_collision import bbp_forcing
    tails = [Q(0)] * (last-first+1)
    for n in range(last-1, first-1, -1):
        tails[n-first] = (bbp_forcing(n+1)+tails[n-first+1])/16
    eta = (-source[first]-tails[0]) % 1
    target = eta / 16**first
    depth = last
    while 16**(depth-last) < 2*cells*odd_modulus:
        depth += 1
    lattice = Q(odd_modulus, 16**depth)
    initial = lattice * ((target/lattice).__floor__()+1)
    error = initial-target
    # Strict upward rounding also makes initial nonzero when target=0.
    if not (0 < error <= lattice and 0 < initial < prefix_radius):
        raise ArithmeticError("initial-cylinder construction failed")
    lifts = tuple(16**n*error-tails[n-first]
                  for n in range(first, last+1))
    upper = Q(odd_modulus, 16**(depth-last))
    if not all(-beta < z <= upper for z in lifts):
        raise ArithmeticError("finite Green lift enclosure failed")
    phases = tuple(z % 1 for z in lifts)
    if phases != tuple((source[n]+16**n*initial) % 1
                       for n in range(first, last+1)):
        raise ArithmeticError("changed-source reconstruction failed")
    return CarryPrefixControl(first, last, cells, prefix_length, odd_modulus,
                              depth, initial, target, prefix_radius,
                              -beta, upper, phases)
