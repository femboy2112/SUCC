"""Collision audit instruments for the authentic BBP prime-window source.

Exact rational finite diagnostics.  Neither a collision bound for the true
source nor pi normality is proved.  See BBP_RESONANCE_COLLISION_AUDIT.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .pi_source_collision import bbp_states, cell_collision, prime_window


def _integer(value: int, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("integer in the declared domain required")
    return value


@dataclass(frozen=True)
class CollisionLadderBudget:
    """Paper certificate |S_N(h)/N| <= sqrt((energy-1)/modes)+error.

    The square-root expression is deliberately not evaluated by floating point.
    The energy is a finite exact source statistic, not an asymptotic estimate.
    """
    count: int
    cells: int
    frequency: int
    modes: int
    energy: Q
    recurrence_error: Q
    cell_error: Q

    @property
    def error(self) -> Q:
        return self.recurrence_error + self.cell_error

    @property
    def squared_upper(self) -> Q:
        """Weaker rational consequence by (a+b)^2 <= 2a^2+2b^2."""
        return min(Q(1), 2*(self.energy-1)/self.modes + 2*self.error**2)


def collision_ladder_budget(count: int, depth: int, frequency: int = 1,
                            modes: int | None = None) -> CollisionLadderBudget:
    """Authenticate y0=0 and return the finite Bessel/recurrence budget.

    Requires |h|16^(J-1)<M so the J discrete Fourier modes are distinct and
    nonzero modulo M=16^depth. Default J=max(1,floor(depth/2)).
    """
    _integer(count, 1); _integer(depth, 1); _integer(frequency)
    if frequency == 0:
        raise ValueError("nonzero frequency required")
    if modes is None:
        modes = max(1, depth//2)
    _integer(modes, 1)
    cells = 16**depth
    top = abs(frequency)*16**(modes-1)
    if top >= cells:
        raise ValueError("Fourier ladder aliases or meets the zero residue")
    energy = cell_collision(bbp_states(count)[1:], cells)
    # r(n+1)<15/(64n^2), sum n^-2<2, and 2*pi<44/7.
    rec = Q(2*(modes-1), count) + Q(11*abs(frequency)*(16**(modes-1)-1), 56*count)
    bins = Q(44*top, 7*cells)
    return CollisionLadderBudget(count, cells, frequency, modes, energy, rec, bins)


@dataclass(frozen=True)
class ConductorSupportedCounterfeit:
    """Countercontrol using only the authentic allowed conductor at each time.

    The rounded complement's denominator DIVIDES the authentic complementary
    denominator. Exact denominator equality and BBP recurrence are not claimed.
    """
    prime: int
    local: tuple[Q, ...]
    allowed_denominators: tuple[int, ...]
    complement: tuple[Q, ...]
    selected: tuple[Q, ...]

    @property
    def minimum_denominator(self) -> int:
        return min(self.allowed_denominators)

    def normalized_sum_distance_from_one_upper(self, frequency: int = 1) -> Q:
        _integer(frequency)
        return Q(44*abs(frequency), 7*self.minimum_denominator)


def conductor_supported_counterfeit(prime: int) -> ConductorSupportedCounterfeit:
    """Round anti-phase on each genuine complement's own denominator grid.

    No new prime factor or larger conductor is introduced at any time. This
    refutes a proposed inference from allowed denominators, not from the full
    source recurrence with U0=0, which still uniquely authenticates the source.
    """
    window = prime_window(prime)
    denominators = tuple(w.denominator for w in window.complement)
    fake = []
    selected = []
    for source, local, denominator in zip(window.states, window.local, denominators):
        if source.denominator != prime*denominator:
            raise ArithmeticError("original source denominator split failed")
        target = (-local) % 1
        numerator = -((-target*denominator).__floor__())
        complement = Q(numerator, denominator) % 1
        phase = (local+complement) % 1
        if not 0 < phase < Q(1, denominator):
            raise ArithmeticError("coprime-grid rounding certificate failed")
        if denominator % complement.denominator:
            raise ArithmeticError("counterfeit introduced a new denominator")
        fake.append(complement)
        selected.append(phase)
    return ConductorSupportedCounterfeit(prime, window.local, denominators,
                                         tuple(fake), tuple(selected))
