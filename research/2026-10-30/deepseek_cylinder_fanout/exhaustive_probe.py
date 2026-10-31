"""Exhaustively calibrate MS-01 on all short base-2 and base-3 streams.

Finite checks are not proof authority for the analytic KL/Pinsker bound.
"""
from itertools import product
from math import log, sqrt
from moving_certificate import collision_energy, l1_short_block


def main():
    checked = 0
    smallest_gap = float('inf')
    sharpest = None
    for base in (2, 3):
        for N in range(1, 6):
            for m in range(1, 5):
                if base ** (N + m - 1) > 9000:
                    continue
                for digits in product(range(base), repeat=N + m - 1):
                    q = collision_energy(digits, N, m, base)
                    for k in range(1, m + 1):
                        l1 = float(l1_short_block(digits, N, k, base))
                        bound = sqrt(2 * log(q) / (m // k)) + 2*m/N
                        gap = bound-l1
                        if gap < smallest_gap:
                            smallest_gap, sharpest = gap, (base, N, m, k)
                        assert gap >= -1e-10, (base, N, m, k, digits, gap)
                        checked += 1
    print({'exhaustive_cases': checked, 'smallest_bound_minus_l1': smallest_gap,
           'tightest_case': sharpest})


if __name__ == '__main__':
    main()
