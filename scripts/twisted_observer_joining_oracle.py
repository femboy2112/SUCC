#!/usr/bin/env python3
"""Independent exact controls for the twisted-observer research dossier.

This script does not import the production BBP implementation.  Its finite
grid laws are invariant under multiplication by 16 and have identical first,
second, and difference *trajectory* laws, but different sum laws.  They are
unforced control systems, not the BBP-selected source.  The second control
uses the genuine four-pole forcing with four distinct rational initial
states.  It verifies loss of the common signal in synchronized differences;
it makes no asymptotic claim about any rationally shifted BBP orbit.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from json import dumps
from math import isqrt


Q = Fraction


def _integer(value: int, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f"expected an integer at least {lower}")
    return value


def _odd_prime(q: int) -> int:
    _integer(q, 3)
    if q % 2 == 0 or any(q % d == 0 for d in range(3, isqrt(q) + 1, 2)):
        raise ValueError("an odd prime is required")
    return q


def grid_law(q: int, coupling: str) -> dict[tuple[int, int], Q]:
    """Product or anti-diagonal probability law on two q-clocks."""
    _odd_prime(q)
    if coupling == "product":
        return {(x, y): Q(1, q * q) for x in range(q) for y in range(q)}
    if coupling == "antidiagonal":
        return {(x, (-x) % q): Q(1, q) for x in range(q)}
    raise ValueError("coupling must be product or antidiagonal")


def trajectory_law(law: dict[tuple[int, int], Q], q: int,
                   a: int, b: int, horizon: int) -> dict[tuple[int, ...], Q]:
    """Law of the complete finite history of a*x_t+b*y_t mod q."""
    _odd_prime(q)
    _integer(horizon, 1)
    if type(a) is not int or type(b) is not int:
        raise ValueError("integer character coefficients required")
    out: defaultdict[tuple[int, ...], Q] = defaultdict(Q)
    for (x, y), mass in law.items():
        value = (a * x + b * y) % q
        history = tuple(value * pow(16, n, q) % q for n in range(horizon))
        out[history] += mass
    return dict(out)


def pushed_law(law: dict[tuple[int, int], Q], q: int) -> dict[tuple[int, int], Q]:
    out: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for (x, y), mass in law.items():
        out[(16 * x % q, 16 * y % q)] += mass
    return dict(out)


def _law_digest(law: dict[tuple[int, ...], Q]) -> str:
    records = [(list(history), str(mass)) for history, mass in sorted(law.items())]
    return sha256(dumps(records, separators=(",", ":")).encode()).hexdigest()


def joining_receipt(q: int = 31, horizon: int = 7) -> dict:
    product, anti = (grid_law(q, c) for c in ("product", "antidiagonal"))
    if pushed_law(product, q) != product or pushed_law(anti, q) != anti:
        raise AssertionError("the declared grid laws are not invariant")
    probes = {"first": (1, 0), "second": (0, 1), "difference": (1, -1)}
    same = {}
    for name, (a, b) in probes.items():
        p = trajectory_law(product, q, a, b, horizon)
        s = trajectory_law(anti, q, a, b, horizon)
        if p != s:
            raise AssertionError(f"{name} trajectory laws differ")
        same[name] = {"histories": len(p), "sha256": _law_digest(p)}
    p_sum = trajectory_law(product, q, 1, 1, horizon)
    a_sum = trajectory_law(anti, q, 1, 1, horizon)
    if a_sum != {(0,) * horizon: Q(1)} or len(p_sum) != q:
        raise AssertionError("the target sum laws fail to distinguish the controls")
    uniform = {(k,): Q(1, q) for k in range(q)}
    checked = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            got = trajectory_law(anti, q, a, b, 1)
            expected = {(0,): Q(1)} if (a - b) % q == 0 else uniform
            if got != expected:
                raise AssertionError("anti-diagonal character exponent law failed")
            checked += 1
    return {
        "status": "VERIFIED_FINITE",
        "q": q,
        "horizon": horizon,
        "source_scope": "unforced rational grid controls; not authentic BBP",
        "T16_invariant_both_laws": True,
        "identical_full_trajectory_laws": same,
        "product_sum_history_count": len(p_sum),
        "antidiagonal_sum_history_count": len(a_sum),
        "antidiagonal_sum_history": [0] * horizon,
        "exact_character_exponent_laws_checked": checked,
        "target_character_mean_product": "0 (uniform q-root exponent law)",
        "target_character_mean_antidiagonal": "1 (zero exponent surely)",
        "unknown_global_swap_preserves_target_sum": True,
    }


def forcing_direct(n: int) -> Q:
    _integer(n, 1)
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def source_trajectory(initial: Q, horizon: int,
                      impulse: tuple[int, Q] | None = None) -> tuple[Q, ...]:
    """Independent original four-pole recurrence; impulse is a failing control."""
    _integer(horizon)
    if not isinstance(initial, Q):
        raise ValueError("an exact Fraction initial state is required")
    values = [initial % 1]
    for n in range(1, horizon + 1):
        r = forcing_direct(n)
        if impulse is not None and n == impulse[0]:
            r += impulse[1]
        values.append((16 * values[-1] + r) % 1)
    return tuple(values)


def differential(left: tuple[Q, ...], right: tuple[Q, ...]) -> tuple[Q, ...]:
    if len(left) != len(right):
        raise ValueError("synchronized trajectories must have equal lengths")
    return tuple((r - l) % 1 for l, r in zip(left, right))


def source_receipt(horizon: int = 48) -> dict:
    _integer(horizon, 5)
    a, b, delta = Q(0), Q(1, 7), Q(1, 15)
    la, ra, lb, rb = (source_trajectory(x, horizon)
                      for x in (a, a + delta, b, b + delta))
    expected = tuple((16 ** n * delta) % 1 for n in range(horizon + 1))
    if differential(la, ra) != expected or differential(lb, rb) != expected:
        raise AssertionError("same-forcing differential did not cancel the common source")
    if any(x.denominator % 2 == 0 for path in (la, ra, lb, rb) for x in path):
        raise AssertionError("declared odd rational carrier was lost")
    if la == lb:
        raise AssertionError("the common signals were not changed")
    common_shift = tuple((y - x) % 1 for x, y in zip(la, lb))
    if common_shift != tuple((16 ** n * (b - a)) % 1 for n in range(horizon + 1)):
        raise AssertionError("common homogeneous shift failed")
    if len(set(common_shift)) == 1:
        raise AssertionError("control accidentally reduced to a fixed global phase")
    for epsilon in (-1, 1):
        twist = tuple((epsilon * (-1) ** n * d) % 1 for n, d in enumerate(expected))
        observed = tuple((epsilon * (-1) ** n * d) % 1
                         for n, d in enumerate(differential(lb, rb)))
        if twist != observed:
            raise AssertionError("twisted differential histories failed to match")
    bad = source_trajectory(b + delta, horizon, impulse=(5, Q(1, 11)))
    if differential(lb, bad) == expected:
        raise AssertionError("forcing-mutation control was not detected")
    return {
        "status": "VERIFIED_FINITE",
        "horizon": horizon,
        "source_scope": "exact BBP forcing; initial states explicitly varied",
        "initial_pairs": [[str(a), str(a + delta)], [str(b), str(b + delta)]],
        "identical_differential_history_length": len(expected),
        "exact_differential_at_every_checked_time": str(delta),
        "odd_rational_carrier_all_checked_states": True,
        "common_signal_shift_values": sorted(map(str, set(common_shift))),
        "common_signal_temporally_nonconstant": True,
        "both_global_wire_orientations_checked": True,
        "forcing_mutation_detected": True,
        "authentic_initial_zero_preserved_for_all_four_wires": False,
        "asymptotic_normality_claim": "none",
    }


def main() -> None:
    print(dumps({"joining": joining_receipt(), "source": source_receipt()},
                indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
