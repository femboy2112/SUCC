"""Same-forcing periodic Green selectors: a conditional-energy obstruction.

For q=3**k the endpoint p/q gives V_n=16**n*p/q-T_n and the complete
original BBP forcing. Its initial value p/q-pi/16 is NOT the authentic zero
anchor. Every fixed finite frequency band can cancel while the conditional
inverse-branch energies tend to one, uniformly over all bin counts M>=q.

Infinite assertions are paper-proved. This module supplies rational Green
intervals, exact finite branch tables, and explicitly changed rational
initial states approximating this real control on a finite horizon.
It neither evaluates pi nor mislabels an interval midpoint as an orbit.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .bbp_source_memory import tail_interval
from .lambda_source_duality import BranchDefect, branch_defect
from .succ_internal_matrix_walk import authentic_r


def _integer(value, minimum=0, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the stated domain")
    if maximum is not None and value > maximum:
        raise ValueError("finite instrument budget exceeded")
    return value


@dataclass(frozen=True)
class PeriodicGreenSelector:
    """Symbolic real control with original forcing and changed initial state.

    The endpoint p/q is rational; the initial state p/q-pi/16 is irrational.
    Its representation is the source Green series, not a supplied pi value.
    """
    exponent: int
    numerator: int = 1

    def __post_init__(self):
        _integer(self.exponent, 2, 8)
        _integer(self.numerator, 1, self.conductor-1)
        if self.numerator % 3 == 0:
            raise ValueError("the periodic endpoint must be a 3-adic unit")

    @property
    def conductor(self):
        return 3**self.exponent

    @property
    def period(self):
        return 3**(self.exponent-1)

    @property
    def endpoint(self):
        return Q(self.numerator, self.conductor)

    @property
    def authentic_zero_anchor(self):
        return False

    @property
    def stable_from(self):
        """Smallest n>=1 with 4*n²>=q; then 16*T_n<1/q."""
        return isqrt((self.conductor-1)//4)+1

    def residue(self, time):
        _integer(time)
        return self.numerator*pow(16, time, self.conductor) % self.conductor

    def periodic_residues(self):
        return tuple(self.residue(n) for n in range(1, self.period+1))

    def periodic_character(self, frequency):
        """Return (amplitude, phase) for the normalized full-period mean.

        Amplitude is exactly zero or one; phase is a rational circle label.
        The evaluated root-of-unity assertion is proved cyclotomically in
        the dossier, separately from formal Q[Q/Z] phase bookkeeping.
        """
        _integer(abs(frequency) if type(frequency) is int else frequency)
        if frequency % self.period:
            return Q(), Q()
        return Q(1), (frequency*self.endpoint) % 1

    def finite_mode_error_upper(self, horizon, frequency):
        """Bound distance to the exact periodic limiting character.

        If period does not divide h, include the incomplete-period tail.
        The Green correction costs <11*abs(h)/(56*N). No smallness of
        an authentic zero-selected Weyl sum is claimed.
        """
        _integer(horizon, 1)
        if type(frequency) is not int:
            raise ValueError("integer Fourier frequency required")
        leftover = horizon % self.period if frequency % self.period else 0
        return (Q(min(leftover, self.period-leftover))
                +Q(11*abs(frequency), 56))/horizon

    def energy_lower_bounds(self, horizon, bins):
        """All-N paper bounds uniform over every M>=q, however large."""
        _integer(horizon, 1)
        _integer(bins, self.conductor)
        bad = min(horizon, self.stable_from-1)
        return max(Q(), 1-Q(4*bad, horizon)), max(Q(), 15-Q(32*bad, horizon))

    def initial_interval(self, terms=8):
        """Strict rational interval for p/q-T_0=p/q-pi/16."""
        _integer(terms, 1, 4096)
        lower, upper = tail_interval(0, terms)
        return self.endpoint-upper, self.endpoint-lower

    def phase_offset_interval(self, time, terms):
        lower, upper = tail_interval(time, terms)
        return -upper, -lower

    def endpoint_interval(self, precision_bits):
        return self.endpoint, self.endpoint


def sparse_tail_interval(time, precision_bits=64):
    """Strict rational bracket for {16**time * sum_k 16**(-2**k)}.

    Past sparse digits are integers. The omitted positive tail is bounded
    by the full radix-16 geometric series starting at its first term.
    """
    _integer(time, 0, 2000)
    _integer(precision_bits, 1, 16384)
    power, lower = 1, Q()
    while power <= time:
        power *= 2
    while 4*(power-time) < precision_bits:
        lower += Q(1, 16**(power-time))
        power *= 2
    return lower, lower+Q(16, 15*16**(power-time))


def sparse_total_upper(horizon):
    _integer(horizon, 1)
    return Q((horizon+1).bit_length(), 15)+Q(1, 225)


@dataclass(frozen=True)
class SparsePeriodicGreenSelector(PeriodicGreenSelector):
    """Endpoint 1/q+xi, xi=sum_k16**(-2**k), with the same BBP forcing.

    Its irrationality exponent is classically two. The infinite selector
    remains nonnormal but all modes below period cancel O(log(N)/N).
    Unlike a rational endpoint it is compatible with logarithmic absolute
    loss at EVERY fixed frequency. The zero initial state still fails.
    """

    def __post_init__(self):
        super().__post_init__()
        if self.numerator != 1:
            raise ValueError("the sparse family uses numerator one to certify a nonzero anchor")

    @property
    def sparse_window(self):
        length, power = 0, 1
        while power < 32*self.conductor:
            length, power = length+1, 16*power
        return length

    @property
    def tail_small_from(self):
        return isqrt((self.conductor-1)//2)+1

    def guaranteed_good(self, time):
        _integer(time, 1)
        next_power = 1 << time.bit_length()
        return time >= self.tail_small_from and next_power-time > self.sparse_window

    def exceptional_count_upper(self, horizon):
        _integer(horizon, 1)
        length = self.sparse_window
        return min(horizon, self.tail_small_from-1
                   +length*(horizon+length).bit_length())

    def energy_lower_bounds(self, horizon, bins):
        _integer(horizon, 1)
        _integer(bins, self.conductor)
        bad = self.exceptional_count_upper(horizon)
        return max(Q(), 1-Q(4*bad, horizon)), max(Q(), 15-Q(32*bad, horizon))

    def finite_mode_error_upper(self, horizon, frequency):
        _integer(horizon, 1)
        if type(frequency) is not int:
            raise ValueError("integer Fourier frequency required")
        leftover = horizon % self.period if frequency % self.period else 0
        correction = Q(44*abs(frequency), 7)*(sparse_total_upper(horizon)+Q(1, 32))
        return (min(leftover, self.period-leftover)+correction)/horizon

    def endpoint_interval(self, precision_bits):
        lower, upper = sparse_tail_interval(0, precision_bits)
        return self.endpoint+lower, self.endpoint+upper

    def initial_interval(self, terms=8):
        _integer(terms, 1, 1024)
        lower, upper = super().initial_interval(terms)
        sparse_lower, sparse_upper = sparse_tail_interval(0, 16*terms)
        return lower+sparse_lower, upper+sparse_upper

    def phase_offset_interval(self, time, terms):
        lower, upper = super().phase_offset_interval(time, terms)
        sparse_lower, sparse_upper = sparse_tail_interval(time, 16*terms)
        return lower+sparse_lower, upper+sparse_upper


@dataclass(frozen=True)
class CertifiedBranchCell:
    time: int
    lower_phase: Q
    upper_phase: Q
    digit: int
    tail_bin: int
    tail_terms: int

    @property
    def representative(self):
        """A rational bin representative; explicitly NOT the real orbit state."""
        return (self.lower_phase+self.upper_phase)/2


def certified_control_cell(selector, time, bins, maximum_terms=128):
    """Certify the real changed-selector digit/bin by strict Green intervals."""
    if not isinstance(selector, PeriodicGreenSelector):
        raise ValueError("typed changed-selector source required")
    _integer(time, 1, 2000)
    _integer(bins, 1, 4096)
    _integer(maximum_terms, 1, 4096)
    backbone = Q(selector.residue(time), selector.conductor)
    terms = 1
    while terms <= maximum_terms:
        lower_offset, upper_offset = selector.phase_offset_interval(time, terms)
        lower, upper = backbone+lower_offset, backbone+upper_offset
        winding = lower.__floor__()
        if upper.__floor__() == winding:
            lower, upper = lower-winding, upper-winding
            digit = (16*lower).__floor__()
            if (16*upper).__floor__() == digit:
                cell = (bins*(16*lower-digit)).__floor__()
                if (bins*(16*upper-digit)).__floor__() == cell:
                    return CertifiedBranchCell(time, lower, upper, digit, cell, terms)
        if terms == maximum_terms:
            break
        terms = min(2*terms, maximum_terms)
    raise ArithmeticError("declared Green precision did not separate this bin boundary")


@dataclass(frozen=True)
class CertifiedControlTable:
    selector: PeriodicGreenSelector
    cells: tuple[CertifiedBranchCell, ...]
    defect: BranchDefect
    source_forcing_preserved: bool = True
    authentic_zero_anchor: bool = False


def certified_control_table(selector, horizon, bins, maximum_terms=128):
    """Exact table of real control cells; midpoints only replay the cell labels."""
    _integer(horizon, 1, 2000)
    cells = tuple(certified_control_cell(selector, n, bins, maximum_terms)
                  for n in range(1, horizon+1))
    defect = branch_defect(tuple(cell.representative for cell in cells),
                           bins, authenticate=False)
    independently_counted = [[0]*16 for _ in range(bins)]
    for cell in cells:
        independently_counted[cell.tail_bin][cell.digit] += 1
    if defect.counts != tuple(tuple(row) for row in independently_counted):
        raise ArithmeticError("interval-certified branch labels failed replay")
    return CertifiedControlTable(selector, cells, defect)


@dataclass(frozen=True)
class RationalSelectorApproximation:
    initial: Q
    states: tuple[Q, ...]
    state_error_upper: Q
    source_forcing_preserved: bool = True
    authentic_zero_anchor: bool = False


def rational_selector_approximation(selector, horizon, extra_terms=8):
    """Same-forcing rational changed seed approaching the real control.

    Every n<=N has absolute full-lift error less than state_error_upper.
    For the non-sparse control the error is positive; the sparse control
    has two competing omitted tails. One approximation is chosen per
    finite horizon; it is not one rational seed with the infinite theorem.
    """
    if not isinstance(selector, PeriodicGreenSelector):
        raise ValueError("typed changed-selector source required")
    _integer(horizon, 1, 2000)
    _integer(extra_terms, 1, 128)
    lower, upper = tail_interval(0, horizon+extra_terms)
    endpoint_lower, endpoint_upper = selector.endpoint_interval(4*(horizon+extra_terms)+8)
    initial = endpoint_lower-lower
    if initial == 0:
        raise ArithmeticError("this requested approximation did not change the zero anchor")
    state, states = initial, []
    for n in range(1, horizon+1):
        state = 16*state+authentic_r(n)
        states.append(state)
    return RationalSelectorApproximation(initial, tuple(states),
                                          16**horizon*(upper-lower+endpoint_upper-endpoint_lower))
