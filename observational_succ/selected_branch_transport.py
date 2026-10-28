"""Exact conditional carry tables and signed, source-selected transport.

The source is imported unchanged from PR #312.  A conditional second moment
is NOT a bound tending to zero.  Moving a record between arbitrary bins changes
one character energy by at most 4/N and total chi-square by at most 32/N.
The paper proves these bounds; tests and intervals certify finite instances.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .lambda_source_duality import (
    Cyclo16, authentic_r, branch_fourier, circle, exact_int,
    verify_original_history,
)
from .pi_succ_character_intervals import (
    characteristic_interval, machin_pi_interval, square_interval,
)


@dataclass(frozen=True)
class ConditionalTable:
    """Sparse occupied bins; labels are characters of literal integers mod 16."""

    observations: int
    bins: int
    rows: tuple[tuple[int, tuple[int, ...]], ...]

    def __post_init__(self):
        exact_int(self.observations, "observations", 1)
        exact_int(self.bins, "bins", 1)
        if type(self.rows) is not tuple:
            raise ValueError("immutable sparse rows required")
        previous, total = -1, 0
        for b, row in self.rows:
            exact_int(b, "occupied bin", 0, self.bins - 1)
            if b <= previous or type(row) is not tuple or len(row) != 16:
                raise ValueError("ordered unique bins with sixteen counts required")
            for count in row:
                exact_int(count, "count", 0)
            if sum(row) == 0:
                raise ValueError("empty bins must be omitted")
            previous = b
            total += sum(row)
        if total != self.observations:
            raise ValueError("conditional mass does not equal observation count")

    @classmethod
    def from_records(cls, records, bins):
        exact_int(bins, "bins", 1)
        records = tuple(records)
        if not records:
            raise ValueError("at least one record required")
        grouped = {}
        for b, label in records:
            exact_int(b, "bin", 0, bins - 1)
            exact_int(label, "literal integer label")
            grouped.setdefault(b, [0] * 16)[label % 16] += 1
        return cls(len(records), bins,
                   tuple((b, tuple(row)) for b, row in sorted(grouped.items())))

    def energy(self, h):
        exact_int(h, "frequency")
        answer = Cyclo16.zero()
        for _, row in self.rows:
            nb = sum(row)
            f = branch_fourier(tuple(Q(c, nb) for c in row), h)
            answer += f * f.conjugate() * Q(nb, self.observations)
        return answer

    def rational_energy(self, h):
        """Exact rational modes h=4,8,12 (and multiples thereof)."""
        exact_int(h, "frequency")
        if h % 4:
            raise ValueError("rational quarter-turn or parity mode required")
        value = self.energy(h)
        if any(value.coefficients[1:]):
            raise ArithmeticError("rational mode escaped Q")
        return value.coefficients[0]

    def chi_squared(self):
        return Q(16, self.observations) * sum(
            (Q(sum(c*c for c in row), sum(row)) for _, row in self.rows), Q()
        ) - 1

    def totient_parity_energy(self):
        """324 E[(Phi_b-1/2)^2], Phi_b=4/9+Pr(c odd|b)/9.

        This is the endpoint translated-packet scalar law from pinned #311,
        evaluated on the declared conditional carry law.  No independent
        source-packet randomness or decay is asserted.
        """
        answer = Q()
        for _, row in self.rows:
            nb = sum(row)
            phi = Q(4, 9) + Q(sum(row[1::2]), 9*nb)
            answer += Q(nb, self.observations) * (phi - Q(1, 2))**2
        return 324 * answer


def record_change_bounds(first, second):
    """Universal exact replacement budgets, not measured energy differences."""
    first, second = tuple(first), tuple(second)
    if not first or len(first) != len(second):
        raise ValueError("equally sized nonempty record lists required")
    for b, label in first + second:
        exact_int(b, "bin", 0)
        exact_int(label, "literal integer label")
    changes = sum((b, j % 16) != (c, k % 16)
                  for (b, j), (c, k) in zip(first, second))
    return {"changed_records": changes,
            "mode_energy_error": min(Q(1), Q(4*changes, len(first))),
            "chi_squared_error": min(Q(15), Q(32*changes, len(first)))}


def source_branch_records(states, bins):
    """Both representations of the SAME authenticated N observations.

    Original records: (floor(M t_n), j_n).
    Future records: (floor(M x_(n+1)), literal c_(n+1)).
    The returned carries include 16; reduction happens only in characters.
    """
    exact_int(bins, "bins", 1)
    if len(states) < 2 or not verify_original_history(states):
        raise ValueError("original zero-selected states U_1,...,U_(N+1) required")
    before, after, changed_bins, changed_digits = [], [], 0, 0
    for u, v in zip(states, states[1:]):
        x, y = circle(u), circle(v)
        j = (16*x).__floor__()
        t = circle(16*x)
        c = v.__floor__() - 16*u.__floor__()
        b, a = (bins*t).__floor__(), (bins*y).__floor__()
        before.append((b, j))
        after.append((a, c))
        changed_bins += b != a
        changed_digits += j != c
    return {"original": tuple(before), "future": tuple(after),
            "bin_changes": changed_bins, "digit_changes": changed_digits}


def source_tables(states, bins):
    records = source_branch_records(states, bins)
    return (ConditionalTable.from_records(records["original"], bins),
            ConditionalTable.from_records(records["future"], bins), records)


def source_energy_transport_budget(observations, bins):
    """Prior all-N source budget, independent of the observed contingency table.

    This bounds change of conditional energies, NOT either energy itself.
    It tends to zero for every prescribed bins=o(observations**2).
    """
    from .selected_branch_arithmetic import spill_count_upper
    exact_int(observations, "observations", 1)
    exact_int(bins, "bins", 1)
    single = spill_count_upper(observations, 1)
    scaled = spill_count_upper(observations, bins)
    changed = min(observations, single + scaled)
    return {"digit_spills_upper": single, "scaled_spills_upper": scaled,
            "changed_records_upper": changed,
            "mode_energy_error": min(Q(1), Q(4*changed, observations)),
            "chi_squared_error": min(Q(15), Q(32*changed, observations)),
            "energy_decay_proved": False}


def midpoint_phases(table):
    """Exact rational phase/multiplicity pairs; retains every cross-bin sign."""
    if not isinstance(table, ConditionalTable):
        raise ValueError("validated conditional table required")
    return tuple((Q(j, 16) + Q(2*b+1, 32*table.bins), count)
                 for b, row in table.rows for j, count in enumerate(row) if count)


def midpoint_rectangle(table, h, *, order=12):
    exact_int(h, "frequency")
    if h == 0:
        raise ValueError("nonzero character required")
    bracket = machin_pi_interval()
    total = [Q()] * 4
    # Coalescing identical phases is exact and preserves source multiplicities.
    phases = Counter()
    for phase, count in midpoint_phases(table):
        phases[circle(h*phase)] += count
    for phase, count in sorted(phases.items()):
        box = characteristic_interval(phase, bracket, order)
        for k in range(4):
            total[k] += Q(count, table.observations)*box[k]
    return (max(Q(-1), total[0]), min(Q(1), total[1]),
            max(Q(-1), total[2]), min(Q(1), total[3]))


def rectangle_squared(box):
    a, b = square_interval(*box[:2]), square_interval(*box[2:])
    return max(Q(), a[0]+b[0]), min(Q(1), a[1]+b[1])


def sqrt_upper(q, bits=48):
    if type(q) is not Q or q < 0:
        raise ValueError("nonnegative rational required")
    exact_int(bits, "precision bits", 1, 256)
    scale = 1 << bits
    return Q(isqrt((q.numerator*scale*scale)//q.denominator)+1, scale)


def source_signed_certificate(states, bins, h, *, order=12):
    """Outward finite Weyl upper using literal carry and successor bins.

    Exact identity x_n=(c_(n+1)+x_(n+1)-r(n+1))/16 gives error
    pi |h|/(16 M) + pi |h| sum_(n=1)^N r(n+1)/(8 N).
    No energy-decay hypothesis or cancellation of off-diagonal terms is used.
    """
    exact_int(h, "frequency")
    if h == 0:
        raise ValueError("nonzero character required")
    _, future, records = source_tables(states, bins)
    N = future.observations
    box = midpoint_rectangle(future, h, order=order)
    squared = rectangle_squared(box)
    forcing_sum = sum((authentic_r(n+1) for n in range(1, N+1)), Q())
    error = Q(22*abs(h), 7*16*bins) + Q(22*abs(h), 7*8*N)*forcing_sum
    return {"observations": N, "bins": bins, "frequency": h,
            "midpoint_rectangle": box, "midpoint_squared": squared,
            "source_transport_error": error,
            "normalized_modulus_upper": min(Q(1), sqrt_upper(squared[1]) + error),
            "record_changes": record_change_bounds(records["original"], records["future"]),
            "authentic_zero_source": True,
            "asymptotic_cancellation_proved": False, "pi_normality_proved": False}
