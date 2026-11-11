"""Audit finite arithmetic behind the Hamiltonian endpoint theorem."""

from fractions import Fraction
from math import fsum, isqrt, log, prod


def primes_through(limit):
    return [
        n for n in range(2, limit + 1)
        if all(n % divisor for divisor in range(2, isqrt(n) + 1))
    ]


def check_edge_coordinates():
    primes = primes_through(120)
    weights = {p: Fraction(1, p * p) for p in primes}
    for hub in range(1, 121):
        from_edges = [Fraction() for _ in range(hub)]
        for p in primes:
            if hub % p == 0:
                for a in range(1, p):
                    from_edges[a] += weights[p]
        from_rows = [Fraction()]
        for a in range(1, hub):
            leaf = hub + a
            from_rows.append(sum(
                (weights[p] for p in primes if p * (leaf // p) == hub),
                Fraction(),
            ))
        assert from_edges == from_rows, hub

    primorial = prod(primes)
    for a in range(1, 120):
        leaf = primorial + a
        from_rows = sum(
            (weights[p] for p in primes if p * (leaf // p) == primorial),
            Fraction(),
        )
        assert from_rows == sum(
            (weights[p] for p in primes if a < p),
            Fraction(),
        ), a


def euler_coefficients(modes, limit):
    coefficients = [0] * (limit + 1)
    coefficients[1] = 1
    for mode in modes:
        for n in range(mode, limit + 1, mode):
            coefficients[n] += coefficients[n // mode]
    return coefficients


def check_fake_euler_control():
    limit = 120
    primes = primes_through(limit)
    authenticated = euler_coefficients(primes, limit)
    assert authenticated[1:] == [1] * limit
    for composite in (4, 6, 25, 77):
        fake = euler_coefficients([*primes, composite], limit)
        assert fake[:composite] == authenticated[:composite]
        assert fake[composite] == 2


def primorial_upward_squared_norm(limit):
    weights = {
        p: log(p) * p**-1.5
        for p in primes_through(limit)
    }
    accumulated = 0.0
    squares = []
    for a in range(limit - 1, 0, -1):
        accumulated += weights.get(a + 1, 0.0)
        squares.append(accumulated**2)
    return fsum(squares)


def main():
    check_edge_coordinates()
    check_fake_euler_control()
    print("Exact upward rows and edges agree. Composite Euler modes fail.")
    print("Y, squared norm of upward coordinates on the primorial unit vector")
    for limit in (32, 128, 512, 2048, 8192):
        print(f"{limit}, {primorial_upward_squared_norm(limit):.9f}")


if __name__ == "__main__":
    main()
