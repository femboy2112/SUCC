"""Exact charge/character controls for the twisted arithmetic cylinder.

Character sums are evaluated algebraically through the roots-of-unity identity.
Independent tests also reduce their polynomials modulo cyclotomic polynomials.
No floating-point cancellation is used to classify a prime.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import prime_observer as po


def omega(n: int) -> int:
    """Total number of prime factors, with multiplicity; omega(1)=0."""
    po.integer(n, 1)
    count, d = 0, 2
    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 1
    return count + int(n > 1)


def character_average(charge: int, clock: int, target: int = 0) -> int:
    """(1/M) sum_j exp(2pi*i*j*(charge-target)/M), exactly."""
    po.integer(charge)
    po.integer(clock, 1)
    po.integer(target)
    return int((charge - target) % clock == 0)


def single_clock_bound(window: int) -> int:
    """Safe exact mode-1 clock for all 1<=n<=window, including unit rejection."""
    po.integer(window, 2)
    return max(2, window.bit_length() - 1)


def pair_clock_bound(N: int) -> int:
    """Safe exact total-degree-2 clock for 2<=k<=N-2, N even>=4."""
    po.integer(N, 4)
    if N % 2:
        raise ValueError("even N required")
    half = N // 2
    # 2 <= Omega(k)+Omega(N-k) <= floor(log2((N/2)^2)).
    return max(1, (half * half).bit_length() - 2)


def pair_twist_receipt(N: int, clock: int | None = None) -> dict:
    po.integer(N, 4)
    if N % 2:
        raise ValueError("even N required")
    bound = pair_clock_bound(N)
    clock = bound if clock is None else po.integer(clock, 1)
    charges = [omega(k) for k in range(2, N - 1)]
    histogram = Counter(a + b for a, b in zip(charges, reversed(charges)))
    exact_pairs = histogram.get(2, 0)
    sampled = sum(count * character_average(charge, clock, 2)
                  for charge, count in histogram.items())
    difference_survivors = sum(a == b for a, b in zip(charges, reversed(charges)))
    return {"N": N, "clock": clock, "sufficient_clock_bound": bound,
            "clock_certified_by_window": clock >= bound,
            "charge_histogram": dict(sorted(histogram.items())),
            "same_orientation_exact_pairs": exact_pairs,
            "same_orientation_clock_survivors": sampled,
            "opposite_orientation_survivors": difference_survivors,
            "alias_count": sampled - exact_pairs,
            "goldbach_proved": False}


def wiggle_edges(window: int, step: int, *, prime_only=False) -> list[tuple[int, int]]:
    """Edges retained by conjugation twirl or by actual prime compression.

    Full undirected edges represent S^h+(S*)^h on the finite observation window.
    This returns an edge set, not the finite-time quantum walk propagator.
    """
    po.integer(window, 2)
    po.integer(step, 1)
    if type(prime_only) is not bool:
        raise ValueError("prime_only must be boolean")
    result = []
    for n in range(2, window - step + 1):
        a, b = omega(n), omega(n + step)
        retained = (a == b == 1) if prime_only else (a == b)
        if retained:
            result.append((n, n + step))
    return result


def multiplier(state: dict[int, int], m: int, *, adjoint=False) -> dict[int, int]:
    """Finite-support V_m or V_m*, including the unit/vacuum label 1."""
    po.integer(m, 1)
    if type(adjoint) is not bool:
        raise ValueError("adjoint must be boolean")
    out = Counter()
    for n, amplitude in state.items():
        po.integer(n, 1)
        if type(amplitude) is not int:
            raise ValueError("this finite probe uses integer amplitudes")
        if adjoint:
            if n % m:
                continue
            out[n // m] += amplitude
        else:
            out[m * n] += amplitude
    return {n: a for n, a in out.items() if a}


def multiplicative_wiggle(state: dict[int, int], m: int) -> dict[int, int]:
    forward, backward = multiplier(state, m), multiplier(state, m, adjoint=True)
    return {n: forward.get(n, 0) + backward.get(n, 0)
            for n in forward.keys() | backward.keys()
            if forward.get(n, 0) + backward.get(n, 0)}


def prime_compress(state: dict[int, int]) -> dict[int, int]:
    return {n: a for n, a in state.items() if omega(n) == 1 and a}


def twisted_transfer_charges(p: int, q: int, start: int) -> dict:
    """Coefficients of P K_p exp(i theta N) K_q P on one prime label.

    Values map output labels to their intermediate-degree polynomial.
    These integer Laurent coefficients specify phases exactly.
    """
    for label in (p, q, start):
        po.integer(label, 2)
        if omega(label) != 1:
            raise ValueError("prime labels required for this two-kick probe")
    result = {}
    for middle, amplitude in multiplicative_wiggle({start: 1}, q).items():
        charge = omega(middle)
        for end, coefficient in prime_compress(multiplicative_wiggle({middle: amplitude}, p)).items():
            result.setdefault(end, Counter())[charge] += coefficient
    return {end: dict(sorted(charges.items())) for end, charges in sorted(result.items())}


def fejer_weights(steps: int) -> dict[int, Fraction]:
    po.integer(steps, 1)
    return {r: Fraction(steps - abs(r), steps * steps)
            for r in range(1 - steps, steps)}


def fejer_window_error(window: int, steps: int) -> Fraction:
    """Proved upper bound, not a computed irrational phase amplitude.

    Carrier is 2<=n<=window and twist is exp(2pi*i*sqrt(2)*(Omega-1)).
    """
    po.integer(window, 2)
    po.integer(steps, 1)
    largest_charge = window.bit_length() - 2
    return min(Fraction(1), Fraction(4 * largest_charge ** 2, steps ** 2))


def probe() -> dict:
    bound = single_clock_bound(10000)
    flags = po.sieve_mask(10000)
    singles = all(character_average(omega(n), bound, 1) == flags[n]
                  for n in range(1, 10001))
    if not singles:
        raise AssertionError("window clock bound failed")
    pair_samples = [pair_twist_receipt(N) for N in (4, 8, 20, 100, 512, 2048, 16384)]
    for row in pair_samples:
        flags = po.sieve_mask(row["N"])
        expected = sum(flags[k] * flags[row["N"] - k] for k in range(2, row["N"] - 1))
        if row["same_orientation_clock_survivors"] != expected:
            raise AssertionError("pair character projection failed")
    aliases = []
    for clock in (2, 3, 4, 8, 16):
        n = 2 ** (clock + 1)
        aliases.append({"clock": clock, "n": n, "omega": omega(n),
                        "mode1_survives": character_average(omega(n), clock, 1),
                        "is_prime": False})
    actual_degrees = Counter(omega(n) for n in range(2, 99))
    transported_degrees = Counter(omega(po.relabel(n)) for n in range(2, 99))
    transported_pair_degree2 = sum(omega(po.relabel(k)) + omega(po.relabel(100 - k)) == 2
                                  for k in range(2, 99))
    if actual_degrees != transported_degrees or transported_pair_degree2 != 0:
        raise AssertionError("single-cylinder isospectral control failed")
    return {"single_window": 10000, "single_clock": bound,
            "single_window_exact": singles, "pair_samples": pair_samples,
            "finite_clock_aliases": aliases,
            "conjugation_composite_edge": [14, 15],
            "conjugation_odd_composite_edge": [33, 35],
            "step1_prime_edges_through_100": wiggle_edges(100, 1, prime_only=True),
            "step2_prime_edges_through_100": wiggle_edges(100, 2, prime_only=True),
            "opposite_twist_false_pair": {"N": 8, "pair": [4, 4], "charges": [2, 2]},
            "unit_contamination_false_pair": {"N": 10, "pair": [1, 9], "charges": [0, 2]},
            "commutator_rank_one_control": {"from": 4, "to": 8, "degree_difference": 1,
                                             "belongs_to_arithmetic_shift_algebra": False},
            "two_step_wiggle_3_5": {
                "from5_via_unit": multiplier(multiplier({5: 1}, 5, adjoint=True), 3),
                "from5_via_composite15": multiplier(multiplier({5: 1}, 3), 5, adjoint=True),
                "compressed_final": prime_compress(multiplicative_wiggle(multiplicative_wiggle({5: 1}, 5), 3)),
                "compressed_each_step": prime_compress(multiplicative_wiggle(prime_compress(multiplicative_wiggle({5: 1}, 5)), 3))},
            "interposed_twist_3_5": {"from3": twisted_transfer_charges(3, 5, 3),
                                       "from5": twisted_transfer_charges(3, 5, 5)},
            "isospectral_single_cylinder": {
                "window": [2, 98], "ordinary": dict(sorted(actual_degrees.items())),
                "transported": dict(sorted(transported_degrees.items())),
                "ordinary_pair_degree2_at100": 12, "transported_pair_degree2_at100": 0},
            "fejer_bound": {"window": 10000, "steps": 256,
                             "error_upper": str(fejer_window_error(10000, 256)),
                             "is_analytic_bound_not_numeric_phase_measurement": True},
            "global_infinite_clock_accuracy_claimed": False,
            "quantum_speedup_proved": False, "goldbach_proved": False}


if __name__ == "__main__":
    import json
    print(json.dumps(probe(), indent=2, sort_keys=True))
