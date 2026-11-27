"""Exact finite audit, independent of probe.mjs. Python standard library only."""
import itertools
import json
import math
from fractions import Fraction as Q


def run():
    checks = {}

    def check(name, condition):
        assert condition, name
        checks[name] = checks.get(name, 0) + 1

    # Enumerate finite cyclic waiting-time laws and ALL nonempty target sets.
    for q in range(1, 9):
        d = 2**q - 1
        mass = [Q(2**(q-r), d) for r in range(1, q+1)]
        check('cyclic_normalization', sum(mass) == 1)
        for x in range(q):
            for mask in range(1, 1 << q):
                hit = sum(mass[(y-x-1) % q] for y in range(q) if mask >> y & 1)
                check('cyclic_full_support_bound', hit >= Q(mask.bit_count(), d))

    # Independent finite graph reachability by Boolean matrix powers and exact
    # eventual absorption probability via two-state linear equations.
    graphs = {'reachableGraphs': 0, 'trapGraphs': 0}
    for a, b in itertools.product(range(1, 8), repeat=2):
        edges = [{j for j in range(3) if mask >> j & 1} for mask in (a, b)]
        good = {i for i in range(2) if 2 in edges[i]}
        good |= {i for i in range(2) if edges[i] & good}
        both = len(good) == 2
        graphs['reachableGraphs' if both else 'trapGraphs'] += 1
        p = [[Q(j in edges[i], len(edges[i])) for j in range(3)] for i in range(2)]
        if both:
            det = (1-p[0][0])*(1-p[1][1])-p[0][1]*p[1][0]
            h0 = (p[0][2]*(1-p[1][1])+p[0][1]*p[1][2])/det
            h1 = ((1-p[0][0])*p[1][2]+p[1][0]*p[0][2])/det
            check('graph_absorption_equations', h0 == h1 == 1)
        for i in good:
            hit2 = p[i][2] + sum(p[i][j]*p[j][2] for j in range(2))
            check('graph_two_step_bound', hit2 >= Q(1, 9))

    # A direct integer construction of the 2,3,5-smooth carrier, then exact
    # polynomial-character signature aliases instead of phase-grid enumeration.
    ns = sorted({2**a*3**b*5**c for a in range(8) for b in range(5)
                 for c in range(4) if 2**a*3**b*5**c <= 128})
    pairs = {}
    for q in (4, 8):
        aliases = []
        for m, n in itertools.combinations(ns, 2):
            a, b = m, n
            for p0 in (2, 3, 5):
                while a % (p0**q) == 0:
                    a //= p0**q
                while b % (p0**q) == 0:
                    b //= p0**q
            if a == b:
                aliases.append([m, n])
        pairs[str(q)] = aliases
    check('phase_4_alias_count', len(pairs['4']) == 9)
    check('phase_8_alias_count', len(pairs['8']) == 0)
    check('phase_carrier_size', len(ns) == 38)

    # Exact finite root test via arithmetic divisibility instead of characters.
    for N in range(1, 65):
        primes = [p for p in range(2, N+1) if all(p % d for d in range(2, math.isqrt(p)+1))]
        for n in range(1, N+1):
            check('divisibility_root', math.prod(int(n % p != 0) for p in primes) == int(n == 1))

    # All matrix products, all input coordinates; integer index maps, N=6.
    N = 6
    def E(m, n, x):
        return m if n == x else 0
    for m, n, k, l, x in itertools.product(range(1, N+1), repeat=5):
        check('matrix_composition_all_columns', E(m, n, E(k, l, x)) == (m if n == k and x == l else 0))

    # Survival from independent rational products, and coupon mean by recursion.
    mean = [Q(0)] * 5
    for seen in range(3, -1, -1):
        mean[seen] = Q(4, 4-seen) + mean[seen+1]
    check('coupon_mean', mean[0] == Q(25, 3))
    for k in range(1, 51):
        check('positive_hazards_not_enough', math.prod(1-Q(1, (t+1)**2) for t in range(1, k+1)) == Q(k+2, 2*(k+1)))
        check('almost_sure_infinite_mean', math.prod(1-Q(1, t+1) for t in range(1, k+1)) == Q(1, k+1))
    return {'scope': 'Independent finite exact checks; no infinite theorem/ML validation', 'checks': checks,
            'graphs': graphs, 'phase': {'smoothCount': len(ns), 'aliases': pairs}, 'coupon_mean': str(mean[0])}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
