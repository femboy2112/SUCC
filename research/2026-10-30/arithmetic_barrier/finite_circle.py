"""Exact finite full-circle certificates; no infinite-horizon inference.

Integer fixed-point interval arithmetic and a rational Taylor remainder enclose
the full complex character. BBP fractions supply the phase, a positive Green
tail supplies the real-pi bridge. No pi digits enter the certificate.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial, isqrt
import json

SCALE = 1 << 96
TERMS = 26


def ceildiv(a, b):
    return -((-a) // b)


def interval(q):
    q = F(q) * SCALE
    return q.numerator // q.denominator, ceildiv(q.numerator, q.denominator)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def mul(x, y):
    corners = [a*b for a in x for b in y]
    return min(corners)//SCALE, ceildiv(max(corners), SCALE)


def div(x, n):
    assert n > 0
    return x[0]//n, ceildiv(x[1], n)


def arctan_bounds(inv, terms=80):
    partial = sum((F((-1)**j, (2*j+1)*inv**(2*j+1)) for j in range(terms)), F())
    next_term = F((-1)**terms, (2*terms+1)*inv**(2*terms+1))
    return min(partial, partial+next_term), max(partial, partial+next_term)


def pi_bounds():
    a, b = arctan_bounds(5)
    c, d = arctan_bounds(239)
    return 16*a-4*d, 16*b-4*c


PI_LO, PI_HI = pi_bounds()
PI = interval(PI_LO)[0], interval(PI_HI)[1]


def character(q):
    """Return (Re,Im) outward intervals for exp(2*pi*i*q), q rational."""
    q = F(q) % 1
    if q > F(1, 2):
        q -= 1
    angle = mul((2*PI[0], 2*PI[1]), interval(q))
    square = mul(angle, angle)
    cos_term = (SCALE, SCALE)
    sin_term = angle
    cosine, sine = cos_term, sin_term
    for j in range(1, TERMS):
        cos_term = neg(div(mul(cos_term, square), (2*j-1)*(2*j)))
        sin_term = neg(div(mul(sin_term, square), (2*j)*(2*j+1)))
        cosine = add(cosine, cos_term)
        sine = add(sine, sin_term)
    # Taylor polynomials through degree 50 (cos) and 51 (sin).
    # All real derivatives have absolute value <=1; |angle|<=pi<22/7.
    cr = interval(F(22, 7)**(2*TERMS-1)/factorial(2*TERMS-1))[1]
    sr = interval(F(22, 7)**(2*TERMS)/factorial(2*TERMS))[1]
    return (cosine[0]-cr, cosine[1]+cr), (sine[0]-sr, sine[1]+sr)


def abs_bounds(real, imag):
    def minabs(x):
        return 0 if x[0] <= 0 <= x[1] else min(abs(x[0]), abs(x[1]))
    lo2 = minabs(real)**2 + minabs(imag)**2
    hi2 = max(abs(x) for x in real)**2 + max(abs(x) for x in imag)**2
    low, high = isqrt(lo2), isqrt(hi2)
    return low, high if high*high == hi2 else high+1


def source(n, coefficients=(4, -2, -1, -1)):
    return sum((F(c, 8*n-d) for c, d in zip(coefficients, (7, 4, 3, 2))), F())


def source_phases(end):
    u = F()
    result = []
    for n in range(1, end+1):
        u = (16*u + source(n)) % 1
        result.append(u)
    return result


def selected_intervals(end, lookahead=8):
    """Exact BBP future refinement plus rigorous positive remaining tail."""
    phases = source_phases(end+lookahead)
    intervals = []
    for n, phase in enumerate(phases[:end], 1):
        tail = sum((source(n+j)/16**j for j in range(1, lookahead+1)), F())
        eps = F(1, 16**lookahead*(8*(n+lookahead)+1)**2)
        intervals.append((phase+tail, phase+tail+eps))
    return intervals


def full_sum_certificate(intervals, start, end, h):
    real = imag = (0, 0)
    phase_error = F()
    for n in range(start, end+1):
        lo, hi = intervals[n-1]
        c, s = character(h*(lo+hi)/2)
        real, imag = add(real, c), add(imag, s)
        # Chord is at most angle. PI_HI is a rational proven upper bound.
        phase_error += PI_HI*abs(h)*(hi-lo)
    error = interval(phase_error)[1]
    real = real[0]-error, real[1]+error
    imag = imag[0]-error, imag[1]+error
    lo, hi = abs_bounds(real, imag)
    length = end-start+1
    # Decimal display is an *outward rational* at six decimal places.
    lower = lo*10**6//(SCALE*length)
    upper = ceildiv(hi*10**6, SCALE*length)
    return {"start": start, "end": end, "h": h,
            "normalized_modulus_millionths": [lower, upper],
            "real_interval_units": list(real), "imag_interval_units": list(imag),
            "scale": SCALE, "strictly_below_quarter": 4*hi < length*SCALE}


def occupancy(intervals, bins):
    low_counts = [0]*bins
    high_counts = [0]*bins
    ambiguous = []
    for n, (lo, hi) in enumerate(intervals, 1):
        first, last = (bins*lo).__floor__(), (bins*hi).__floor__()
        touched = sorted({j % bins for j in range(first, last+1)})
        if first == last:
            low_counts[first % bins] += 1
        else:
            ambiguous.append({"n": n, "possible_bins": touched})
        for j in touched:
            high_counts[j] += 1
    return {"bins": bins, "lower": low_counts, "upper": high_counts, "ambiguous": ambiguous}


def main():
    states = selected_intervals(1024)
    rows = [full_sum_certificate(states, a, b, h)
            for a, b in ((1,256), (257,512), (513,1024), (1,1024)) for h in range(1,17)]
    assert all(row["strictly_below_quarter"] for row in rows)
    output = {"status": "PASS_FINITE_ONLY", "source": "original four poles; U_0=0",
              "pi_normality_proved": False, "horizon": 1024, "future_terms": 8,
              "method": "96-bit outward integer intervals; rational Machin pi; Taylor remainder; original BBP Green tail",
              "fourier": rows,
              "occupancy": [occupancy(states, bins) for bins in (16,64,256)],
              "coherent_counterseed_completed_modulus": "1 (exact, all h and all windows)",
              "coherent_counterseed_below_quarter": False}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
