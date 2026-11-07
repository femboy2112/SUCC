#!/usr/bin/env python3
"""Independent exact finite affine-pin checker, without SUCC imports.

Exhaustive scope: all linear maps on F_2^2 and F_2^3, every translation,
and every nonzero single-character initial pin. The character-closure oracle
and the source transition partition-refinement oracle are implemented
separately. This finite check calibrates an implementation; it is not a proof
of the all-finite-abelian-group theorem.

This is the checker actually executed by the constructor agent, reorganized
into a callable entry point without changing its algorithms or case scope.
"""
from itertools import product
import json


def act(rows, x):
    return sum(((r & x).bit_count() & 1) << i for i, r in enumerate(rows))


def dual(rows, h):
    y = 0
    for i, r in enumerate(rows):
        if h >> i & 1:
            y ^= r
    return y


def close(rows, initial_characters):
    subgroup = {0, *initial_characters}
    while True:
        enlarged = (
            subgroup
            | {a ^ b for a in subgroup for b in subgroup}
            | {dual(rows, a) for a in subgroup}
        )
        if enlarged == subgroup:
            return subgroup
        subgroup = enlarged


def part(rows, translation, initial_characters, dimension):
    states = range(1 << dimension)
    classes = [
        tuple((h & x).bit_count() & 1 for h in initial_characters)
        for x in states
    ]
    for _ in range(1 << dimension):
        names = {}
        old = [names.setdefault(c, len(names)) for c in classes]
        classes = [(old[x], old[act(rows, x) ^ translation]) for x in states]
        names = {}
        new = [names.setdefault(c, len(names)) for c in classes]
        if new == old:
            return tuple(new)
    raise AssertionError("partition refinement failed to terminate")


def run_check():
    count = 0
    by_dimension = {}
    for dimension in (2, 3):
        dimension_count = 0
        for rows in product(range(1 << dimension), repeat=dimension):
            for h in range(1, 1 << dimension):
                closure = close(rows, (h,))
                for translation in range(1 << dimension):
                    partition = part(rows, translation, (h,), dimension)
                    for x, y in product(range(1 << dimension), repeat=2):
                        expected = all(
                            ((g & (x ^ y)).bit_count() & 1) == 0
                            for g in closure
                        )
                        if (partition[x] == partition[y]) != expected:
                            raise AssertionError(
                                (rows, translation, h, x, y, partition, closure)
                            )
                    count += 1
                    dimension_count += 1
        by_dimension[str(dimension)] = dimension_count
    assert count == 28864
    assert by_dimension == {"2": 192, "3": 28672}
    return {
        "models_checked": count,
        "models_by_dimension": by_dimension,
        "method_1": "dual subgroup and pullback closure",
        "method_2": "exact source transition partition refinement",
        "status": "passed",
    }


def example():
    rows = (2, 0, 4)
    translation = 6
    pins = (1,)
    closure = close(rows, pins)
    partition = part(rows, translation, pins, 3)
    return {
        "rows": rows,
        "translation": translation,
        "initial_pins": pins,
        "dual_closure": sorted(closure),
        "behavior_classes": partition,
        "retained_hidden_direction": 4,
    }


def main():
    print(json.dumps({"exhaustive_check": run_check(), "example": example()}, sort_keys=True))


if __name__ == "__main__":
    main()
