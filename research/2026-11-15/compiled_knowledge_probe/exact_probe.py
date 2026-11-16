"""Exact finite controls for observer-relative compiled probes.

This models a fixed equality oracle and a cached key. No claims about P vs NP,
physical experiments, or genuine source authentication are made.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Discovery:
    key: int
    oracle_calls: int


def discover(n: int, hidden_key: int) -> Discovery:
    """Sequential elimination; the last candidate is inferred without a query."""
    if type(n) is not int or n < 1 or n > 10:
        raise ValueError("Model supports 1 <= n <= 10")
    cardinality = 1 << n
    if type(hidden_key) is not int or not 0 <= hidden_key < cardinality:
        raise ValueError("Key is outside the n-bit source")
    for candidate in range(cardinality - 1):
        if candidate == hidden_key:  # one equality-oracle interaction
            return Discovery(candidate, candidate + 1)
    return Discovery(cardinality - 1, cardinality - 1)


def compiled_probe(remembered_key: int, query: int) -> bool:
    """Pure cached equality test; no call to the source oracle."""
    return query == remembered_key


def run_checks() -> dict[str, int]:
    sources_checked = 0
    fresh_questions_checked = 0
    rival_pairs_checked = 0
    drift_failures_checked = 0
    for n in range(1, 9):
        cardinality = 1 << n
        for key in range(cardinality):
            record = discover(n, key)
            assert record.key == key
            assert record.oracle_calls == min(key + 1, cardinality - 1)
            assert record.oracle_calls <= cardinality - 1
            sources_checked += 1
            for query in range(cardinality):
                assert compiled_probe(record.key, query) == (query == key)
                fresh_questions_checked += 1

        # All these observations are zero for BOTH surviving keys.
        a, b = cardinality - 2, cardinality - 1
        for i in range(cardinality - 2):
            assert (i == a) is False
            assert (i == b) is False
        assert a != b
        rival_pairs_checked += 1
        assert discover(n, b).oracle_calls == cardinality - 1

        # A source change invalidates the cached certificate on a fresh query.
        for old in range(cardinality):
            new = (old + 1) % cardinality
            x = old
            assert compiled_probe(old, x)
            assert (x == new) is False
            drift_failures_checked += 1

    assert discover(3, 7) == Discovery(7, 7)
    for call in (lambda: discover(0, 0), lambda: discover(2, 4),
                 lambda: discover(2, -1), lambda: discover(True, 0)):
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed source was accepted")

    return {
        "finite_sources_checked": sources_checked,
        "fresh_cached_queries_checked": fresh_questions_checked,
        "unresolved_rival_pairs": rival_pairs_checked,
        "stale_source_mismatches_checked": drift_failures_checked,
        "max_discovery_calls_for_8_bits": (1 << 8) - 1,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), sort_keys=True))
