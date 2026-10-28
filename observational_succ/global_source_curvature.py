"""Paid source-curvature bounds for signed BBP sums at moving frequencies.

The paper proves the universal inequalities; exact finite instruments below
authenticate the original four poles and zero boundary. The estimates hold for
every seed under this forcing. They do NOT imply fixed-frequency cancellation.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .succ_internal_matrix_walk import authentic_r


def _integer(value, name, lower=None):
    if type(value) is not int or (lower is not None and value < lower):
        raise ValueError(f"{name}: ordinary integer >= {lower} required")
    return value


def source_derivative(n: int) -> Q:
    _integer(n, "source index", 1)
    return authentic_r(n + 1) - authentic_r(n + 2)


def quadratic_band_bound(m: int, h: int) -> Q:
    """Upper bound for |sum_{n=m+1}^{2m} e(h U_n)|, all same-forcing seeds.

    PAPER theorem: m>=128 and m²<=|h|<=2m². Effective, no pi digits.
    """
    _integer(m, "block start", 128)
    _integer(h, "frequency")
    if not m*m <= abs(h) <= 2*m*m:
        raise ValueError("frequency outside the proved quadratic band")
    return Q(m) - Q(m // 4, 64 * 289)


def cubic_band_bound(m: int, h: int) -> Q:
    """Effective all-seed bound m-max(0,m-33)/289 on the cubic band."""
    _integer(m, "block start", 16)
    _integer(h, "frequency")
    if not m**3 <= abs(h) <= 16*m**3 // 15:
        raise ValueError("frequency outside the proved cubic band")
    return Q(m) - Q(max(0, m - 33), 289)


def source_window(m: int) -> tuple[Q, ...]:
    """Literal unwrapped zero-selected states; no altered source or pi oracle."""
    _integer(m, "finite block start", 1)
    if m > 2000:
        raise ValueError("finite exact replay budget exceeded")
    value = Q()
    states = []
    for n in range(1, 2*m + 1):
        value = 16*value + authentic_r(n)
        if n > m:
            states.append(value)
    return tuple(states)


def authenticate_window(states: tuple[Q, ...], m: int) -> None:
    """Reject a changed seed even when its interior recurrence still holds."""
    if type(states) is not tuple or any(type(x) is not Q for x in states):
        raise ValueError("exact immutable unwrapped states required")
    if states != source_window(m):
        raise ValueError("window does not have the original zero source passport")


def cubic_source_certificate(m: int, h: int) -> dict:
    """Authenticate every forcing increment behind one moving-band theorem."""
    bound = cubic_band_bound(m, h)
    if m > 2000:
        raise ValueError("finite exact replay budget exceeded")
    increments = tuple(abs(h)*source_derivative(n)
                       for n in range(m + 1, 2*m - 1))
    if not all(Q(1, 32) < x < Q(1, 2) for x in increments):
        raise ArithmeticError("source first-derivative separation failed")
    if not all(a > b for a, b in zip(increments, increments[1:])):
        raise ArithmeticError("source complete-monotonicity consequence failed")
    return {"m": m, "h": h, "increment_min": min(increments),
            "increment_max": max(increments), "forcing_sum_upper": Q(32),
            "selected_sum_upper": bound, "all_same_forcing_seeds": True,
            "fixed_frequency_decay_proved": False}


def quadratic_source_certificate(m: int, h: int) -> dict:
    bound = quadratic_band_bound(m, h)
    if m > 2000:
        raise ValueError("finite exact replay budget exceeded")
    count = m // 4
    early = range(m + 1, m + count + 1)
    late_start = (7*m + 3) // 4
    late = range(late_start, late_start + count)
    gaps = tuple(abs(h)*(authentic_r(a+1)-authentic_r(b+1))
                 for a, b in zip(early, late))
    if not all(Q(1, 16) < x < Q(1, 2) for x in gaps):
        raise ArithmeticError("disjoint source-pair separation failed")
    return {"m": m, "h": h, "pairs": count,
            "gap_min": min(gaps), "gap_max": max(gaps),
            "selected_sum_upper": bound, "all_same_forcing_seeds": True,
            "fixed_frequency_decay_proved": False}


def energy_transport(u: tuple[Q, ...], w: tuple[Q, ...]) -> tuple[Q, Q, Q]:
    """Exact finite check of the real core, retaining both endpoint costs."""
    if (type(u) is not tuple or type(w) is not tuple or len(u) != len(w)+1
            or not w or any(type(x) is not Q or x < 0 for x in u+w)):
        raise ValueError("nonnegative exact vectors of lengths T+1,T required")
    if any(v > u[i+1]+16*u[i] for i, v in enumerate(w)):
        raise ValueError("missing local source-distance hypothesis")
    left = sum((v*v for v in w), Q())
    full = 289 * sum((x*x for x in u), Q())
    boundary = full - 17*u[0]**2 - 272*u[-1]**2
    if not left <= boundary <= full:
        raise ArithmeticError("finite real energy inequality failed")
    return left, boundary, full


def changed_green_control(m: int, h: int) -> dict:
    """Paper theorem for V_n=-T_n; no numerical evaluation of irrational seed.

    At every cubic-band h the actual whole changed-seed block has modulus <=512.
    Every fixed nonzero frequency nevertheless has Weyl mean tending to one.
    """
    cubic_band_bound(m, h)
    return {"m": m, "h": h, "seed": "-pi/16",
            "same_four_poles": True, "zero_selector": False,
            "tail_increment_lower": Q(1, 512),
            "tail_increment_upper": Q(1, 30),
            "moving_sum_upper": min(Q(m), Q(512)),
            "fixed_nonzero_frequency_limit": Q(1),
            "authority": "PAPER-PROVED, not finite evaluation of T_n"}
