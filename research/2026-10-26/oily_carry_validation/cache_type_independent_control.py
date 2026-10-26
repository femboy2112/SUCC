"""Replay the discovered type-alias cache bug without mutating any source.

Run from the repository root with PYTHONPATH=. . Both deliberately untyped
wrappers reproduce the defect; both production typed caches reject it.
"""
from fractions import Fraction as Q
from functools import lru_cache

from observational_succ.oily_signed_certificate import (
    character_enclosure, machin_pi_enclosure,
)


def main():
    pairs = (
        (character_enclosure, {"phase": Q(1, 4)}, {"phase": 0.25}),
        (machin_pi_enclosure, {"terms": 1}, {"terms": True}),
    )
    for function, valid_args, invalid_args in pairs:
        function.cache_clear()
        function(**valid_args)
        try:
            function(**invalid_args)
        except ValueError:
            print(function.__name__, "typed-cache rejects invalid equal-valued input")
        else:
            raise AssertionError("Production guard bypassed")
        mutant = lru_cache(maxsize=32, typed=False)(function.__wrapped__)
        assert mutant(**valid_args) == mutant(**invalid_args)
        print(function.__name__, "untyped-cache mutant bypass reproduced")
    print("PASS: two typed-cache guards, two independent alias mutants")


if __name__ == "__main__":
    main()
