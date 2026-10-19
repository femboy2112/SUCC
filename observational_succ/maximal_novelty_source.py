"""Finite-window novelty versus global algorithmic/source complexity.

Exact standard-library countermodels.  A maximal k-block transcript is not
a certificate of a nonperiodic source, of Martin-Loef randomness, or of a
continuous finite cyclic factor.  No randomness oracle is implemented.
"""
from __future__ import annotations

from collections import Counter


class NoveltyError(ValueError):
    pass


def de_bruijn_binary(order: int) -> tuple[int, ...]:
    """Construct B(2,order) by the FKM recursion; no random bits involved."""
    if type(order) is not int or not 1 <= order <= 12:
        raise NoveltyError("order must be an integer from 1 through 12")
    a = [0] * (2 * order + 2)
    seq: list[int] = []

    def db(t: int, p: int) -> None:
        if t > order:
            if order % p == 0:
                seq.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, 2):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    if len(seq) != (1 << order):
        raise ArithmeticError("invalid complete de Bruijn circuit")
    return tuple(seq)


def cyclic_blocks(bits: tuple[int, ...], width: int) -> Counter:
    """All cyclic source-window observations with their multiplicities."""
    if type(width) is not int or width < 1 or not bits:
        raise NoveltyError("positive width and nonempty source period needed")
    if any(type(b) is not int or b not in (0, 1) for b in bits):
        raise NoveltyError("literal binary source required")
    m = len(bits)
    return Counter(tuple(bits[(i + j) % m] for j in range(width))
                   for i in range(m))


def least_period(bits: tuple[int, ...]) -> int:
    if not bits or any(type(b) is not int or b not in (0, 1) for b in bits):
        raise NoveltyError("nonempty literal binary source required")
    n = len(bits)
    return next(d for d in range(1, n + 1)
                if n % d == 0 and all(bits[i] == bits[i % d] for i in range(n)))


def maximal_window_periodic_witness(order: int) -> dict:
    """Finite 'all words once' passes; infinite period is exactly 2**order."""
    bits = de_bruijn_binary(order)
    blocks = cyclic_blocks(bits, order)
    n = 1 << order
    if len(blocks) != n or any(count != 1 for count in blocks.values()):
        raise ArithmeticError("failed complete k-block novelty")
    period = least_period(bits)
    if period != n:
        raise ArithmeticError("source transcript should be periodic at 2**order")
    return {
        "order": order,
        "period_bits": "".join(map(str, bits)),
        "distinct_order_k_blocks": len(blocks),
        "all_order_k_blocks_exactly_once_per_cycle": True,
        "global_source_period": period,
        "globally_aperiodic": False,
        "Martin_Lof_randomness_certified": False,
        "continuous_universal_clock_factors_certified": False,
    }


def program_count_bound(length: int, deficiency: int) -> dict:
    """Counting bound, NOT a program computing Kolmogorov complexity.

    There are at most 2**(n-c)-1 binary programs with length < n-c,
    hence at most that many distinct n-bit outputs with such a program.
    """
    if type(length) is not int or type(deficiency) is not int or length < 0 or deficiency < 0:
        raise NoveltyError("nonnegative integer bit budgets only")
    eligible_bits = max(length - deficiency, 0)
    return {
        "length": length,
        "deficiency": deficiency,
        "number_of_binary_strings": 1 << length,
        "maximum_strings_describable_below_length_minus_deficiency":
            (1 << eligible_bits) - 1 if length > deficiency else 0,
        "algorithmic_randomness_decided": False,
    }


def exact_decoder_possible(source_and_report: tuple[tuple[object, object], ...]) -> bool:
    """Exact reconstructibility iff each report fiber has one source value."""
    for i, (source, report) in enumerate(source_and_report):
        for other, second in source_and_report[i + 1:]:
            if report == second and source != other:
                return False
    return True


def rooted_cycle_factor_possible(source_period: int, target_period: int) -> bool:
    """A rooted successor-equivariant map C_d -> C_m exists iff m | d."""
    if (type(source_period) is not int or type(target_period) is not int
            or source_period <= 0 or target_period <= 0):
        raise NoveltyError("positive integer periods only")
    return source_period % target_period == 0


def full_binary_shift_has_cyclic_factor(target_period: int) -> bool:
    """Proof-rule for full one-sided shift: fixed 000... forbids m>=2.

    A constant source tape is a fixed point. A pointed equivariant map to
    C_m would send it to a fixed point of the m-cycle, impossible for m>1.
    This is a mathematical model theorem, not sampled infinite state data.
    """
    if type(target_period) is not int or target_period < 1:
        raise NoveltyError("positive cycle period required")
    return target_period == 1
