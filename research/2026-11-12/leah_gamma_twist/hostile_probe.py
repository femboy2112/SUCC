"""Exact finite controls for HOSTILE.md, independent of the shared BBP modules.

This small four-pole oracle is intentionally separate from the production
implementation. Its outputs certify finite identities, not R0 or normality.
"""
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from math import floor
import json


def r(n):
    if n < 1:
        raise ValueError("source clock must be positive")
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def ceil_log16(n):
    if n < 1:
        raise ValueError("positive integer required")
    return ((n - 1).bit_length() + 3) // 4


def run():
    horizon = 320
    states = [F(0)]
    for n in range(1, horizon + 1):
        states.append(16 * states[-1] + r(n))
    lifts = [floor(u + F(1, 2)) for u in states]
    residues = [u - m for u, m in zip(states, lifts)]
    carries = [0] + [lifts[n] - 16*lifts[n-1] for n in range(1, horizon+1)]
    green_cases = 0
    for n in [1, 2, 7, 19, 31, 83, 127, 251]:
        for length in [1, 2, 5, 11, 23]:
            source_tail = sum((r(n+j) / 16**j for j in range(1, length+1)), F(0))
            pulse_tail = sum((F(carries[n+j], 16**j) for j in range(1, length+1)), F(0))
            assert residues[n] + source_tail == pulse_tail + residues[n+length] / 16**length
            green_cases += 1
    assert all(-8 <= a <= 8 for a in carries[2:])

    terminal_rows = []
    terminal_states = 0
    for block in [3, 8, 17, 37, 83, 127]:
        terminal = 2 * block
        seed = -states[terminal] / 16**terminal
        current = seed
        assert -F(1, 2) < current < 0
        for n in range(1, terminal + 1):
            current = 16 * current + r(n)
            assert -F(1, 2) < current <= 0
            assert floor(current + F(1, 2)) == 0
            terminal_states += 1
        assert current == 0
        terminal_rows.append({"B": block, "M": terminal, "terminal_zero": True})

    pulse_times = [16]
    while pulse_times[-1] <= 20000:
        pulse_times.append(pulse_times[-1] + ceil_log16(pulse_times[-1]))
    waiting_cases = 0
    for n in range(16, 8193):
        next_pulse = pulse_times[bisect_right(pulse_times, n)]
        assert next_pulse - n <= ceil_log16(n)
        assert F(1, 16**(next_pulse-n)) >= F(1, 16*n)
        waiting_cases += 1
    shell_rows = []
    for block in [16, 31, 64, 127, 256, 511, 1024, 2048, 4096, 8192]:
        count = bisect_left(pulse_times, 2*block) - bisect_right(pulse_times, block)
        max_gap = ceil_log16(2*block)
        floor_log = (block.bit_length()-1) // 4
        assert F(count) >= F(block, max_gap)-2
        # Weaker than H11's logarithmic upper bound; entirely rational oracle.
        assert count <= F(block, floor_log)+1
        shell_rows.append({"B": block, "K": count,
                           "rational_lower": str(F(block, max_gap)-2),
                           "rational_upper": str(F(block, floor_log)+1)})

    # Holographic repair: h=32,q=1 gives f(y)=exp(4 pi i y).
    # Endpoint pair and midpoint have phase +1; interior quarter points -1.
    # All responses here are exact roots of unity, recorded as integers.
    def real_root(turns):
        twice = 2 * turns
        assert twice.denominator == 1
        return (-1) ** twice.numerator
    def response(points):
        return sum((F(real_root(2*y), len(points)) for y in points), F(0))
    endpoint_response = response([F(0), F(1)])
    midpoint_response = response([F(1, 2)])
    interior_response = response([F(1, 4), F(3, 4)])
    assert abs(endpoint_response-midpoint_response) == 0
    assert abs(interior_response-midpoint_response) == 2

    return {
        "authority": "exact finite checks; conditional asymptotic claims have paper proofs",
        "source_green_cases": green_cases,
        "centered_carry_range_count": len(carries[2:]),
        "centered_carry_range_horizon": horizon,
        "terminal_states_checked": terminal_states,
        "terminal_root_rows": terminal_rows,
        "green_plus_terminal_grouped_cases": green_cases+terminal_states+2*len(terminal_rows),
        "waiting_time_cases": waiting_cases,
        "shell_count_cases": len(shell_rows),
        "shell_count_rows": shell_rows,
        "first_pulse_times": pulse_times[:12],
        "holographic_repair": {"h": 32, "q": 1, "endpoint_gap": 0, "interior_gap": 2},
        "status": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
