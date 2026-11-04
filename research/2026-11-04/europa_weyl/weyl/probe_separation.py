"""Preregistered exact checks for the prime-sieve spectral consequence EW6."""
from math import isqrt
import json
from finite_weyl import trajectory


def primes(maximum):
    return [p for p in range(3, maximum+1, 2)
            if all(p % k for k in range(3, isqrt(p)+1, 2))]


def probe(t_max):
    _, points = trajectory(t_max)
    prime_list = primes(8*t_max)
    collisions = []
    misses = []
    pairs = 0
    for t in range((t_max+1)//2,t_max+1):
        band = [p for p in prime_list if 4*t < p <= 8*t-7]
        for n in range(t):
            pairs += 1
            if points[n] == points[t]:
                collisions.append([n,t])
            if not any(p > 8*n or (p <= 8*n-7 and pow(16,t-n,p) != 1)
                       for p in band):
                misses.append([n,t])
    return {"T":t_max, "pairs":pairs, "repeated_phases":collisions,
            "top_window_without_witness":misses}


if __name__ == "__main__":
    print(json.dumps([probe(t) for t in (127,193)], indent=2))
