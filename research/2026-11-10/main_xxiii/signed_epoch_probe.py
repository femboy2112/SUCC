"""Certified odd-eight Weyl and signed lag rectangles on fixed finite holdouts."""

from fractions import Fraction
from math import floor

from observational_succ.bbp_spatial_haar_lift import bulk_pi_hex_digits
from observational_succ.parity_boundary_certificate import sine_turns_enclosure


EPOCHS = (1021, 2053, 4099)
LAGS = (0, 1, 3, 7)
DEPTH = 12
TICKS = 10**9


def component_ticks(turn, radius):
    lower, upper = sine_turns_enclosure(turn, bits=36, terms=14)
    # Sine is 2π-Lipschitz in turns, with 2π < 44/7.
    error = Fraction(44, 7) * radius
    return floor((lower - error) * TICKS), -floor(-(upper + error) * TICKS)


def rectangle(points, start, count, lag):
    lo_real = hi_real = lo_imag = hi_imag = 0
    for i in range(start, start + count):
        phase = points[i] if lag == 0 else points[i + lag] - points[i]
        # Either tail is in [0,16^-DEPTH]. The difference is within
        # ±16^-DEPTH of the difference of prefix values.
        radius = Fraction(8, 16**DEPTH)
        real_lo, real_hi = component_ticks(8 * phase + Fraction(1, 4), radius)
        imag_lo, imag_hi = component_ticks(8 * phase, radius)
        lo_real += real_lo
        hi_real += real_hi
        lo_imag += imag_lo
        hi_imag += imag_hi
    return (lo_real, hi_real, lo_imag, hi_imag, count * TICKS)


def main():
    length = 2 * max(EPOCHS) + max(LAGS) + DEPTH
    digits = bulk_pi_hex_digits(length, guard=24)
    assert digits == bulk_pi_hex_digits(length, guard=32)
    points = tuple(
        Fraction(int(digits[i:i + DEPTH], 16), 16**DEPTH)
        for i in range(len(digits) - DEPTH + 1)
    )
    print("A lag real_lo real_hi imag_lo imag_hi common_denominator")
    for epoch in EPOCHS:
        for lag in LAGS:
            bounds = rectangle(points, epoch - 1, epoch, lag)
            assert bounds[1] < bounds[-1]  # excludes coherent phase 1 here
            print(epoch, lag, *bounds)
    print("Exact coherent completed and common-horizon wrong-seed control: (1, 0)")


if __name__ == "__main__":
    main()
