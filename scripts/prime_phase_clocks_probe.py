#!/usr/bin/env python3
"""Repeatable finite prime-phase search; pure JSON, source/budget labels included.

No number-theoretic infinitude or Weil positivity is inferred from this script.
"""
from __future__ import annotations

import argparse
import json

from observational_succ.prime_phase_clocks import (
    PhaseClockError, aligned_primes, euclid_witness, ghost_two_adic_pair,
    phase_window, prime_clock_profile, prime_prefix, primes_up_to, primorial,
    sqrt_window_perfect,
)


def probe(limit: int = 100_000, clock_depth: int = 4) -> dict:
    if type(limit) is not int or not 100 <= limit <= 1_000_000:
        raise PhaseClockError("bounded census horizon must be 100..1000000")
    if type(clock_depth) is not int or not 1 <= clock_depth <= 8:
        raise PhaseClockError("clock depth must be a positive prefix <=8")
    clocks = prime_prefix(clock_depth)
    if limit <= clocks[-1]:
        raise PhaseClockError("horizon does not reach the fixed clock window")
    winners_count, winners_prefix, best_count, best_prefix = [], [], -1, -1
    locked_in_window = []
    prime_count = 0
    for p in primes_up_to(limit):
        prime_count += 1
        prof = prime_clock_profile(p)
        if prof.synchronized_count > best_count:
            best_count, winners_count = prof.synchronized_count, [p]
        elif prof.synchronized_count == best_count and len(winners_count) < 10:
            winners_count.append(p)
        if prof.prefix_depth > best_prefix:
            best_prefix, winners_prefix = prof.prefix_depth, [p]
        elif prof.prefix_depth == best_prefix and len(winners_prefix) < 10:
            winners_prefix.append(p)
        if p > clocks[-1] and phase_window(p, clocks).perfectly_locked:
            if len(locked_in_window) < 12:
                locked_in_window.append(p)
    depth_exemplars = []
    for k in range(1, 8):
        M = primorial(k)
        first = aligned_primes(k, 30, 3)
        candidate, prime_candidate, factor = euclid_witness(k)
        depth_exemplars.append({
            "k": k, "modulus": M, "first_verified_primes": [
                {"multiplier": t, "prime": p} for t, p in first
            ],
            "primorial_plus_one": candidate,
            "plus_one_prime": prime_candidate,
            "plus_one_composite_factor": factor,
        })
    return {
        "source": "genuine primes, ordinary Z/q clock with successor +1",
        "horizon": limit,
        "declared_clock_primes": list(clocks),
        "prime_count": prime_count,
        "greatest_synced_distinct_prime_count": best_count,
        "first_winners_by_count": winners_count,
        "greatest_initial_prefix_depth": best_prefix,
        "first_winners_by_prefix": winners_prefix,
        "first_full_window_locks": locked_in_window,
        "wheel_reverse_search": depth_exemplars,
        "ghost_same_first_digit_mod_four": list(ghost_two_adic_pair(3)),
        "sqrt_clock_pure_under_1000": [
            p for p in primes_up_to(1000) if sqrt_window_perfect(p)
        ],
        "finite_search_is_universal_proof": False,
        "dirichlet_is_external_theorem": True,
        "ABC_proved": False,
        "RH_proved": False,
        "signed_Weil_S4_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--clock-depth", type=int, default=4)
    args = parser.parse_args()
    print(json.dumps(probe(args.limit, args.clock_depth), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
