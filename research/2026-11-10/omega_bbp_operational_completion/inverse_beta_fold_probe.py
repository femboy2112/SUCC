"""Exact rational tests for the authentic BBP inverse-beta / Mellin fold.

No pi oracle, floating-point arithmetic, or external packages.
"""
from fractions import Fraction


P = {0: 4, 3: -2, 4: -1, 5: -1}


def mul(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, 0) + ai * bj
    return {i: v for i, v in out.items() if v}


def add(a, b):
    out = dict(a)
    for i, bi in b.items():
        out[i] = out.get(i, 0) + bi
    return {i: v for i, v in out.items() if v}


def shifted_scaled(a, scale, shift):
    return {i + shift: ai * scale for i, ai in a.items()}


def moment(a, n):
    assert n >= 0
    return sum((Fraction(ai, 8 * n + i + 1) for i, ai in a.items()), Fraction())


def four_poles(n):
    assert n >= 0
    return (Fraction(4, 8*n + 1) - Fraction(2, 8*n + 4)
            - Fraction(1, 8*n + 5) - Fraction(1, 8*n + 6))


def test():
    assert mul(mul({0: 1, 1: -1}, {0: 2, 2: 1}),
               {0: 2, 1: 2, 2: 1}) == P
    assert sum(P.values()) == 0   # source-selected endpoint zero
    assert sum({**P, 5: 0}.values()) == 1  # one-pole mutation breaks it

    probes = ({0: 1}, {0: 3, 2: 5, 7: -8},
              {1: -2, 9: 3, 12: 1}, {0: 11, 1: -7, 2: 2, 3: -1})
    count = 0
    for n in range(64):
        assert moment(P, n) == four_poles(n)
        for f in probes:
            analytic_step = add(P, shifted_scaled(f, Fraction(1, 16), 8))
            assert (moment(analytic_step, n) ==
                    four_poles(n) + moment(f, n + 1) / 16)
            count += 1

    for N in (1, 2, 3, 8, 16, 32):
        for n in (0, 1, 7, 23):
            prefix_kernel = {}
            for j in range(N):
                prefix_kernel = add(
                    prefix_kernel, shifted_scaled(P, Fraction(1, 16**j), 8*j)
                )
            tail_clock = sum(
                (Fraction(1, 16**j) * four_poles(n + j)
                 for j in range(N)), Fraction()
            )
            assert moment(prefix_kernel, n) == tail_clock
            assert moment(prefix_kernel, n) / 16 == sum(
                (Fraction(1, 16**(j+1)) * four_poles(n+j)
                 for j in range(N)), Fraction()
            )
            count += 1

    assert count == 280
    print(f"PASS: {count} exact polynomial/moment finite folds; "
          "four-pole factorization and pole-mutation control")


if __name__ == "__main__":
    test()
