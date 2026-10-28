"""Source-authentic carry-spill sparsity and conditional dyadic transport.

The four-pole zero-initial source is imported unchanged. A positive spill
forces a growing zero-carry interval. This bounds a representation error;
it supplies no smallness theorem for the surviving selected branch energy.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .lambda_source_duality import (
    BranchDefect, branch_defect, original_history, witness_selected_branches,
)
from .succ_internal_matrix_walk import authentic_r


def _nat(value, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(f"ordinary integer >= {minimum} required")
    return value


def spill_refractory_length(transition_index: int, scale: int = 1) -> int:
    """max(0,floor(log_16(4*(k-1)^2/a))), using integer comparisons.

    A spill at source transition k forces the next L literal carries of
    the scaled orbit {a U_n} to be zero. k>=2 and a>=1 are required.
    """
    _nat(transition_index, 2)
    _nat(scale)
    bound = 4*(transition_index-1)**2
    result, power = 0, scale
    while 16*power <= bound:
        result, power = result+1, 16*power
    return result


def spill_cutoff(horizon: int, scale: int = 1) -> int:
    """Preset R=max(2,1+floor((a*N^2)^(1/4))); no source data are read."""
    _nat(horizon)
    _nat(scale)
    return max(2, 1+isqrt(isqrt(scale*horizon*horizon)))


def spill_count_upper(horizon: int, scale: int = 1,
                      cutoff: int | None = None) -> int:
    """All-N upper bound for positive spills at transitions 2,...,N+1.

    The preset cutoff gives o(N) for any prescribed integer a_N=o(N^2).
    For a=1 it gives O(N/log N). All future frequencies and tail-bin
    choices remain outside this count; no orbit measurements choose R.
    """
    _nat(horizon)
    _nat(scale)
    R = spill_cutoff(horizon, scale) if cutoff is None else _nat(cutoff, 2)
    if R > horizon+1:
        return horizon
    gap = spill_refractory_length(R, scale)+1
    late_length = horizon+2-R
    late_count = (late_length+gap-1)//gap
    return min(horizon, R-2+late_count)


@dataclass(frozen=True)
class ScaledSpillPoint:
    branch_index: int
    scale: int
    original_lift: Q
    original_forcing: Q
    scaled_phase: Q
    unforced_digit: int
    scaled_literal_carry: int
    spill: int
    forced_zero_carry_steps: int


def authentic_spill_points(horizon: int, scale: int = 1) -> tuple[ScaledSpillPoint, ...]:
    """Exact original-source scaled observations, without changing its forcing.

    Early scaled spills may exceed one and are retained literally. This
    is an observer at frequency/scale a, not a mutated primary source.
    """
    _nat(horizon)
    _nat(scale)
    if horizon > 1999:
        raise ValueError("declared finite source prefix budget exceeded")
    states = original_history(horizon+1)
    result = []
    for n, (previous, arrival) in enumerate(zip(states, states[1:]), 1):
        phase = (scale*previous) % 1
        digit = (16*phase).__floor__()
        carry = (scale*arrival).__floor__()-16*(scale*previous).__floor__()
        spill = carry-digit
        forcing = authentic_r(n+1)
        if spill != ((16*phase) % 1+scale*forcing).__floor__() or spill < 0:
            raise ArithmeticError("source spill identity failed")
        result.append(ScaledSpillPoint(n, scale, previous, forcing, phase,
                                      digit, carry, spill,
                                      spill_refractory_length(n+1, scale) if spill else 0))
    return tuple(result)


def _counts(counts):
    rows = tuple(tuple(row) for row in counts)
    if (not rows or any(len(row) != 16 for row in rows) or
            any(type(x) is not int or x < 0 for row in rows for x in row)):
        raise ValueError("nonnegative integer 16-column contingency table required")
    N = sum(map(sum, rows))
    if not N:
        raise ValueError("positive total sample count required")
    return rows, N


def rational_dyadic_energy(counts, frequency: int) -> Q:
    """Exact conditional h=4,8,12 energy, retaining quarter-turn signs."""
    if type(frequency) is not int or frequency % 16 not in (4, 8, 12):
        raise ValueError("a quarter-turn or parity frequency is required")
    rows, N = _counts(counts)
    result = Q()
    for row in rows:
        size = sum(row)
        if not size:
            continue
        residues = tuple(sum(row[r::4]) for r in range(4))
        if frequency % 16 == 8:
            numerator = (residues[0]+residues[2]-residues[1]-residues[3])**2
        else:
            numerator = (residues[0]-residues[2])**2+(residues[1]-residues[3])**2
        result += Q(numerator, N*size)
    return result


def endpoint_totient_parity_energy(carry_counts) -> Q:
    """324 times conditional squared distance of endpoint totient mass to 1/2.

    PR311's declared endpoint packet coupling has primitive mass
    Phi_b=4/9+P(carry odd | bin b)/9. This statistic is EXACTLY carry
    parity energy, not a claim that the packet coupling selects Haar.
    """
    rows, N = _counts(carry_counts)
    result = Q()
    for row in rows:
        size = sum(row)
        if size:
            phi = Q(4, 9)+Q(sum(row[1::2]), 9*size)
            result += 324*Q(size, N)*(phi-Q(1, 2))**2
    return result


def quarter_opposition_overlap(counts) -> Q:
    """The exact missing opposite-residue pairing in E4=(1+E8)/2-4*overlap."""
    rows, N = _counts(counts)
    result = Q()
    for row in rows:
        size = sum(row)
        if size:
            p = tuple(sum(row[r::4]) for r in range(4))
            result += Q(p[0]*p[2]+p[1]*p[3], N*size)
    return result


@dataclass(frozen=True)
class CarryBranchComparison:
    source_id: str
    horizon: int
    bins: int
    original_digits: tuple[int, ...]
    literal_carries: tuple[int, ...]
    spill_transition_indices: tuple[int, ...]
    digit_defect: BranchDefect
    carry_defect: BranchDefect
    universal_spill_count_upper: int
    universal_mode_energy_error_upper: Q
    universal_chi_squared_error_upper: Q


def carry_branch_comparison(horizon: int, bins: int = 4) -> CarryBranchComparison:
    """Compare selected digits and literal carries in the SAME original tail bins.

    Literal carry 16 is preserved in the receipt; only character evaluation
    uses its residue modulo 16. No future-bin replacement is performed here.
    """
    _nat(horizon)
    _nat(bins)
    if horizon > 1999 or bins > 4096:
        raise ValueError("declared exact contingency budget exceeded")
    states = original_history(horizon+1)
    witnesses = witness_selected_branches(states)
    digit_defect = branch_defect(states[:-1], bins)
    rows = [[0]*16 for _ in range(bins)]
    spills = []
    for point in witnesses:
        b = (bins*point.remainder).__floor__()
        rows[b][point.literal_carry % 16] += 1
        if point.literal_carry != point.digit:
            if point.literal_carry != point.digit+1:
                raise ArithmeticError("unscaled source spill is not zero or one")
            spills.append(point.source_index+1)
    chi = sum((Q(16*sum(c*c for c in row), horizon*sum(row))
               for row in rows if sum(row)), Q())-1
    carry_defect = BranchDefect(horizon, bins, tuple(map(tuple, rows)), chi)
    cap = spill_count_upper(horizon)
    if len(spills) > cap:
        raise ArithmeticError("source spill count exceeded the universal bound")
    return CarryBranchComparison(
        "Q:Coherent-Main-X-four-pole-BBP", horizon, bins,
        tuple(point.digit for point in witnesses),
        tuple(point.literal_carry for point in witnesses), tuple(spills),
        digit_defect, carry_defect, cap, min(Q(1), Q(4*cap, horizon)),
        min(Q(15), Q(32*cap, horizon)),
    )
