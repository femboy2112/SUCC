"""Exact controls for compact-policy termination, not a topology oracle.

The general compactness proof is in SWARM_ATLAS/ROOT_POLICY_COMPACTNESS.md.
These finite rational controls cannot certify compactness or an infinite run.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache


def first_zero_wait(ones: int) -> tuple[int, ...]:
    """The source 1^ones 0^infinity, stopped at its first zero."""
    if type(ones) is not int or ones < 0:
        raise ValueError("A nonnegative integer source cutoff is required")
    return (1,) * ones + (0,)


def compact_discontinuous_wait(point: Fraction) -> tuple[int, ...]:
    """Read equality to 0,1,1/2,... on K={0} union {1/n:n>=1}.

    K is compact, but equality to 0 is not a continuous binary readout.
    Each instrument leaves the carrier unchanged. A finite source address
    is supplied; this function does not infer it from the public history.
    """
    if type(point) is not Fraction or point < 0:
        raise ValueError("Exact rational point in the declared source K required")
    if point == 0:
        return (1,)
    if point.numerator != 1:
        raise ValueError("Point is outside the compact source K")
    return (0,) * point.denominator + (1,)


def destructive_xor_policy_exists(depth: int, *, erase: bool = True) -> bool:
    """Independent bounded policy enumeration for two initial source bits.

    Each read returns the selected CURRENT bit, then erases the other bit.
    A belief retains (original,current) pairs. No reset is available.
    The recursion ranges over all deterministic adaptive trees up to depth.
    """
    if type(depth) is not int or depth < 0 or type(erase) is not bool:
        raise ValueError("Invalid depth or source mutation")

    @lru_cache(None)
    def wins(belief: tuple[tuple[int, int], ...], remaining: int) -> bool:
        if len({(source // 2) ^ (source % 2) for source, _ in belief}) == 1:
            return True
        if not remaining:
            return False
        for bit in (0, 1):
            branches: dict[int, list[tuple[int, int]]] = {}
            for source, current in belief:
                outcome = current // 2 if bit == 0 else current % 2
                after = current
                if erase:
                    after = 2 * outcome if bit == 0 else outcome
                branches.setdefault(outcome, []).append((source, after))
            if all(wins(tuple(sorted(set(child))), remaining - 1)
                   for child in branches.values()):
                return True
        return False

    return wins(tuple((source, source) for source in range(4)), depth)


def policy_topology_receipt() -> dict:
    """Finite controls with constructive unbounded-family formulas."""
    sampled = (0, 1, 2, 8, 31, 100)
    zero_lengths = tuple(len(first_zero_wait(n)) for n in sampled)
    point_lengths = tuple(len(compact_discontinuous_wait(Fraction(1, n + 1)))
                          for n in sampled)
    assert zero_lengths == tuple(n + 1 for n in sampled)
    assert point_lengths == tuple(n + 2 for n in sampled)
    assert compact_discontinuous_wait(Fraction(0)) == (1,)
    destructive = tuple(destructive_xor_policy_exists(n) for n in range(7))
    repaired = tuple(destructive_xor_policy_exists(n, erase=False)
                     for n in range(3))
    assert not any(destructive) and repaired == (False, False, True)
    return {
        "source_cutoffs": sampled,
        "noncompact_first_zero_lengths": zero_lengths,
        "compact_discontinuous_lengths": point_lengths,
        "compact_continuous_finite_control_bound": max(zero_lengths),
        "counterfactual_initial_bit_reports_identify_xor": True,
        "reset_free_destructive_xor_policy_by_depth_0_through_6": destructive,
        "nondestructive_xor_policy_by_depth_0_through_2": repaired,
        "general_no_reset_impossibility_proved_by_erased_source_pair": True,
        "topological_compactness_verified_by_this_program": False,
        "infinite_source_or_policy_simulated": False,
        "RH_or_physical_hardware_claimed": False,
    }
