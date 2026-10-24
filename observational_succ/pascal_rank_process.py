"""Exact stationary countermodel for all one-window Pascal rank laws.

Independent four-bit blocks have a signed positional perturbation; a uniform
alignment makes their concatenation stationary. Every contiguous-window rank
law is binomial, while positional four-word probabilities are not uniform.
This synthetic process is not the authenticated BBP source. Its infinite
stationarity/ergodicity and rank identities are proved in PI_ALL_RANK_OBSERVERS.md.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, lcm

Word = tuple[int, ...]
WORDS: tuple[Word, ...] = tuple(product((0, 1), repeat=4))
DEFAULT_PARAMETER = Fraction(1, 4)


def _nat(value: int, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")
    return value


def _parameter(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError("parameter must be an exact integer or Fraction")
    value = Fraction(value)
    if abs(value) > Fraction(1, 2):
        raise ValueError("parameter must lie in [-1/2,1/2]")
    return value


def _offset(value: int) -> int:
    if type(value) is not int or not 0 <= value < 4:
        raise ValueError("alignment must be one of 0,1,2,3")
    return value


def character(word: Word, indices: tuple[int, ...]) -> int:
    """Binary Walsh character; indices are distinct zero-based positions."""
    if any(type(x) is not int or x not in (0, 1) for x in word):
        raise ValueError("word must contain literal binary integers")
    if len(set(indices)) != len(indices) or any(
        type(i) is not int or not 0 <= i < len(word) for i in indices
    ):
        raise ValueError("character indices must be distinct positions in word")
    return (-1) ** sum(word[i] for i in indices)


def block_law(parameter: int | Fraction = DEFAULT_PARAMETER) -> dict[Word, Fraction]:
    """P_t(w)=2^-4[1+t(chi_124(w)-chi_134(w))], |t|<=1/2."""
    t = _parameter(parameter)
    return {
        w: (1 + t * (character(w, (0, 1, 3)) - character(w, (0, 2, 3)))) / 16
        for w in WORDS
    }


def block_segment_law(
    start: int, length: int, parameter: int | Fraction = DEFAULT_PARAMETER
) -> dict[Word, Fraction]:
    """A contiguous segment inside one authentic countermodel block."""
    _nat(start, "start")
    _nat(length, "length")
    if start + length > 4:
        raise ValueError("segment must be contained in a four-bit block")
    result: dict[Word, Fraction] = defaultdict(Fraction)
    for w, mass in block_law(parameter).items():
        result[w[start:start + length]] += mass
    return dict(result)


def _segments(length: int, alignment: int) -> list[tuple[int, int]]:
    result = []
    remaining, start = length, alignment
    while remaining:
        take = min(4 - start, remaining)
        result.append((start, take))
        remaining -= take
        start = 0
    return result


def window_rank_law(
    length: int, parameter: int | Fraction = DEFAULT_PARAMETER,
    alignment: int | None = None,
) -> dict[int, Fraction]:
    """Compute count laws by independent-block convolution, without binomial input.

    None averages over all four alignments. A fixed alignment is also useful:
    every alignment has the same rank law, although full word laws differ.
    """
    _nat(length, "length")
    _parameter(parameter)
    offsets = range(4) if alignment is None else (_offset(alignment),)
    total: dict[int, Fraction] = defaultdict(Fraction)
    for offset in offsets:
        running = {0: Fraction(1)}
        for start, take in _segments(length, offset):
            counts: dict[int, Fraction] = defaultdict(Fraction)
            for w, mass in block_segment_law(start, take, parameter).items():
                counts[sum(w)] += mass
            nxt: dict[int, Fraction] = defaultdict(Fraction)
            for i, a in running.items():
                for j, b in counts.items():
                    nxt[i + j] += a * b
            running = dict(nxt)
        for k, mass in running.items():
            total[k] += mass / len(offsets)
    return dict(total)


def binomial_rank_law(length: int) -> dict[int, Fraction]:
    """Independent combinatorial reference law, not used by convolution."""
    _nat(length, "length")
    return {k: Fraction(comb(length, k), 2**length) for k in range(length + 1)}


def enumerate_window_law(
    length: int, parameter: int | Fraction = DEFAULT_PARAMETER,
    alignment: int | None = None, max_combinations: int = 1_000_000,
) -> dict[Word, Fraction]:
    """Enumerate independent whole blocks and retain the requested window.

    The explicit resource cap concerns enumeration only, not the paper theorem.
    This calculation does not use the claimed four-word or binomial formulas.
    """
    _nat(length, "length")
    _nat(max_combinations, "max_combinations")
    offsets = tuple(range(4)) if alignment is None else (_offset(alignment),)
    block_counts = tuple((offset + length + 3) // 4 if length else 0 for offset in offsets)
    if sum(16**count for count in block_counts) > max_combinations:
        raise ValueError("requested whole-block enumeration exceeds resource cap")
    law = block_law(parameter)
    denominator = lcm(*(mass.denominator for mass in law.values()))
    weights = tuple(int(law[word] * denominator) for word in WORDS)
    total: dict[Word, Fraction] = defaultdict(Fraction)
    for offset, count in zip(offsets, block_counts):
        integers: dict[Word, int] = defaultdict(int)
        for chosen in product(range(16), repeat=count):
            mass = 1
            flat: tuple[int, ...] = ()
            for index in chosen:
                mass *= weights[index]
                flat += WORDS[index]
            integers[flat[offset:offset + length]] += mass
        scale = len(offsets) * denominator**count
        for word, numer in integers.items():
            total[word] += Fraction(numer, scale)
    return dict(total)


def four_word_formula(parameter: int | Fraction = DEFAULT_PARAMETER) -> dict[Word, Fraction]:
    """Stationary four-word law: one aligned perturbation out of four."""
    t = _parameter(parameter)
    return {
        w: Fraction(1, 16) * (
            1 + t * (character(w, (0, 1, 3)) - character(w, (0, 2, 3))) / 4
        ) for w in WORDS
    }


def symbol_table(parameter: int | Fraction = DEFAULT_PARAMETER) -> tuple[Word, ...]:
    """Finite deterministic alphabet map with exactly the block-law multiplicities.

    A normal sequence over this alphabet gives the stationary process's window
    frequencies after block coding; the default alphabet has 32 symbols.
    """
    law = block_law(parameter)
    denominator = lcm(*(mass.denominator for mass in law.values()))
    if denominator > 16384:
        raise ValueError("exact symbol table exceeds resource cap")
    return tuple(w for w in WORDS for _ in range(int(law[w] * denominator)))
