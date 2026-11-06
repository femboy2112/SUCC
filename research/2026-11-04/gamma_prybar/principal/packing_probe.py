"""Construct a worst-case seed on the source's odd epoch-entry grid."""
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from math import lcm
import json

from reset_probe import forcing


def ordered_close(points, width):
    ordered = sorted(points)
    circle = [x + k for k in (-1, 0, 1) for x in ordered]
    return sum(bisect_right(circle, x+width) - bisect_left(circle, x-width)
               for x in ordered)


def run(a):
    u, clock = [F()], 1
    for n in range(1, 3*a+1):
        addition = forcing(n)
        if n <= a:
            clock = lcm(clock, addition.denominator)
        u.append(16*u[-1] + addition)
    alpha = u[-1] / 16**(3*a)
    width = F(1, a**3)
    length, radix = 0, 1
    while radix < 8 / width:
        length += 1
        radix *= 16
    sites = list(range(a, 2*a, length))
    entry = F()
    for n in reversed(sites):
        tail = 16**n*alpha - u[n]
        word = -((-radix*(tail+width/4)) // 1)
        assert 0 <= word < radix and F(word+1, radix) <= tail+3*width/4
        entry = (word+entry)/radix
    z = round(clock * (entry-16**a*alpha))
    seed = F((pow(16**a, -1, clock)*z) % clock, clock)
    assert seed and clock % seed.denominator == 0
    genuine = [v % 1 for v in u[a:2*a]]
    shifted = [(u[n] + 16**n * seed) % 1 for n in range(a, 2*a)]
    assert all(0 <= shifted[n-a] <= width for n in sites)
    counts = [ordered_close(values, width) for values in (genuine, shifted)]
    if a == 91:
        for count, points in zip(counts, (genuine, shifted)):
            assert count == sum(min(abs(x-y), 1-abs(x-y)) <= width for x in points for y in points)
    assert counts[1] >= len(sites)**2
    assert all(forcing(n)-forcing(n+1) >= F(1,512*a**3) for n in range(a,2*a))
    return dict(A=a, width=str(width), word_length=length, forced_visits=len(sites),
                seed_denominator_bits=seed.denominator.bit_length(),
                genuine_ordered_pairs=counts[0], shifted_ordered_pairs=counts[1])


if __name__ == "__main__":
    print(json.dumps([run(a) for a in (91,211,367)], indent=2))
