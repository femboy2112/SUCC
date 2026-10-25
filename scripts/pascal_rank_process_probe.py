"""Exact post-discovery calibration of the all-Pascal-rank countermodel."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from observational_succ.pascal_rank_process import (
    binomial_rank_law, block_law, character, enumerate_window_law,
    four_word_formula, symbol_table, window_rank_law,
)


def main() -> None:
    rows = []
    for length in range(11):
        rank = defaultdict(Q)
        law = enumerate_window_law(length)
        for w, p in law.items():
            rank[sum(w)] += p
        assert dict(rank) == window_rank_law(length) == binomial_rank_law(length)
        rows.append({"length": length, "word_atoms": len(law), "exact_binomial": True})
    holdouts = []
    for t in (Q(-1, 2), Q(1, 3)):
        for length in (7, 11, 19, 33, 64):
            assert window_rank_law(length, t) == binomial_rank_law(length)
            holdouts.append({"parameter": str(t), "length": length, "exact_binomial": True})
    law4 = enumerate_window_law(4)
    assert law4 == four_word_formula()
    assert law4[(0, 0, 1, 0)] == Q(9, 128)
    assert law4[(0, 1, 0, 0)] == Q(7, 128)
    first = sum(p * character(w, (0, 1, 3)) for w, p in law4.items())
    second = sum(p * character(w, (0, 2, 3)) for w, p in law4.items())
    assert first == Q(1, 16) and second == -first
    root = Path(__file__).resolve().parents[1]
    inputs = (
        "observational_succ/pascal_rank_process.py",
        "tests/test_pascal_rank_process.py",
        "scripts/pascal_rank_process_probe.py",
    )
    result = {
        "status": "EXACT FINITE; paper supplies infinite stationarity/ergodicity and rank proof",
        "registration": "POST_DISCOVERY: kernel chosen from positional Walsh reasoning before these checks",
        "scope": "All individual window-rank distributions, not their entire joint time law; not BBP",
        "default_parameter": "1/4",
        "block_law": {"".join(map(str, w)): str(p) for w, p in block_law().items()},
        "direct_enumeration_vs_independent_convolution": rows,
        "additional_exact_parameter_and_length_controls": holdouts,
        "four_word_0010": str(law4[(0, 0, 1, 0)]),
        "four_word_0100": str(law4[(0, 1, 0, 0)]),
        "uniform_four_word_target": "1/16",
        "signed_chi_124": str(first), "signed_chi_134": str(second),
        "deterministic_coding_alphabet_size": len(symbol_table()),
        "pi_normality": "OPEN",
        "sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in inputs},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
