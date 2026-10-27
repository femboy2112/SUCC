"""Independent finite development checks; not universal proof authority."""
from fractions import Fraction as F
from itertools import product


def debruijn(base, order):
    a = [0] * (base * order)
    out = []

    def rec(t, period):
        if t > order:
            if order % period == 0:
                out.extend(a[1:period + 1])
        else:
            a[t] = a[t - period]
            rec(t + 1, period)
            for value in range(a[t - period] + 1, base):
                a[t] = value
                rec(t + 1, t)

    rec(1, 1)
    return out


def partition(z, modulus):
    groups = [z[t::modulus] for t in range(modulus)]
    return [(len(g), F(sum(g), len(g)) if g else F(0)) for g in groups]


def conditional_energy(z, modulus):
    return sum(c * x * x for c, x in partition(z, modulus)) / len(z)


def residue_energy(z, modulus):
    return F(modulus, len(z) ** 2) * sum(
        (c * x) ** 2 for c, x in partition(z, modulus)
    )


def main():
    count = 0
    for base, order in ((2, 1), (2, 2), (2, 3), (2, 4), (16, 1), (16, 2)):
        word = debruijn(base, order)
        assert len(word) == base ** order
        for length in range(1, order + 1):
            counts = {v: 0 for v in product(range(base), repeat=length)}
            for t in range(len(word)):
                counts[tuple(word[(t + j) % len(word)] for j in range(length))] += 1
            assert set(counts.values()) == {base ** (order - length)}
            count += len(counts)
        print('debruijn', base, order, 'period', len(word), 'all circular blocks exact')

    checks = strict = 0
    for size in range(2, 11):
        for z in product((-1, 1), repeat=size):
            for modulus, refinement in ((1, 2), (1, 3), (2, 4), (3, 6)):
                if refinement > size:
                    continue
                parent = partition(z, modulus)
                children = partition(z, refinement)
                gain = sum(
                    c * (x - parent[s % modulus][1]) ** 2
                    for s, (c, x) in enumerate(children)
                ) / size
                assert conditional_energy(z, refinement) - conditional_energy(z, modulus) == gain >= 0
                assert abs(residue_energy(z, modulus) - conditional_energy(z, modulus)) <= F(modulus, size)
                assert residue_energy(z, modulus) <= 1 + F(modulus * modulus, 4 * size * size)
                if size % refinement == 0:
                    assert residue_energy(z, refinement) - residue_energy(z, modulus) == gain
                strict += gain > 0
                checks += 1
    print('exact block frequencies checked', count)
    print('exact martingale identities checked', checks, 'strict refinements', strict)
    z = [1, -1] * 16
    assert residue_energy(z, 1) == 0 and residue_energy(z, 2) == 1
    print('negative control E_1=0 E_2=1 PASSED')


if __name__ == '__main__':
    main()
