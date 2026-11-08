"""Independent stdlib exact controls for the oscillator constructor.

Prospective domains: cyclic sizes 2..19, 23, 29; every proper aperture;
three rational laws and every translated position. Continuum checks use
exact rational coefficient inequalities, with a Machin-series pi enclosure.
No SUCC implementation is imported. Infinite claims rest on the proof note.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divide(p, q):
    r = trim(list(map(Q, p)))
    q = trim(list(map(Q, q)))
    out = [Q(0)] * max(1, len(r)-len(q)+1)
    while r != [0] and len(r) >= len(q):
        k = len(r)-len(q)
        c = r[-1]/q[-1]
        out[k] += c
        for j, v in enumerate(q):
            r[j+k] -= c*v
        r = trim(r)
    return trim(out), r


PHI = {1: [Q(-1), Q(1)]}


def cyclotomic(n):
    if n not in PHI:
        p = [Q(-1)] + [Q(0)]*(n-1) + [Q(1)]
        for d in range(1, n):
            if n % d == 0:
                p, rem = divide(p, cyclotomic(d))
                assert rem == [0]
        PHI[n] = p
    return PHI[n]


class Field:
    def __init__(self, m):
        self.m = m
        self.phi = cyclotomic(m)
        self.degree = len(self.phi)-1
        self.zero = (Q(0),)*self.degree
        self.one = (Q(1),)+(Q(0),)*(self.degree-1)
        self.powers = []
        for k in range(m):
            _, r = divide([Q(0)]*k+[Q(1)], self.phi)
            self.powers.append(tuple(r+[Q(0)]*(self.degree-len(r))))

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x-y for x, y in zip(a, b))

    def scale(self, a, q):
        return tuple(q*x for x in a)

    def mul(self, a, b):
        p = [Q(0)]*(2*self.degree-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                p[i+j] += x*y
        _, r = divide(p, self.phi)
        return tuple(r+[Q(0)]*(self.degree-len(r)))

    def root(self, k):
        return self.powers[k % self.m]

    def sum(self, values):
        result = self.zero
        for value in values:
            result = self.add(result, value)
        return result


def readout(field, law, length):
    m = field.m
    zero = tuple(sum(law[(y+j) % m] for j in range(length))
                 for y in range(m))
    one = tuple(field.sum(field.scale(field.root(-j), law[(y+j) % m])
                          for j in range(length))
                for y in range(m))
    return zero, one


def atan_enclosure(x, terms):
    s = sum(((-1)**j*x**(2*j+1)/Q(2*j+1)
             for j in range(terms)), Q(0))
    remainder = x**(2*terms+1)/Q(2*terms+1)
    return (s, s+remainder) if terms % 2 == 0 else (s-remainder, s)


def affine_interval(a, b, interval):
    lo, hi = interval
    return ((a+b*lo, a+b*hi) if b >= 0 else (a+b*hi, a+b*lo))


def half_weight_times_pi_squared(h):
    h = abs(h)
    assert h >= 1
    if h == 1:
        return Q(4), Q(1, 2)
    if h % 2:
        return Q(4, h*h), Q(0)
    return Q(4*(h*h+1), (h*h-1)**2), Q(0)


def main():
    count = {"local_inverse": 0, "mean_calibration": 0,
             "half_frame": 0, "times16_bound": 0,
             "primitive_energy": 0, "full_window_alias": 0}
    rejected = {k: 0 for k in
                ("omit_relative_phase", "omit_static_difference",
                 "reverse_reconstruction_sign", "omit_denominator",
                 "wrong_boundary_phase")}
    for m in tuple(range(2, 20))+(23, 29):
        field = Field(m)
        laws = [
            tuple(Q(i == 0) for i in range(m)),
            tuple(Q(i == m-1) for i in range(m)),
            tuple(Q(2*(i+1), m*(m+1)) for i in range(m)),
        ]
        for length in range(1, m):
            omega = field.root(-length)
            denominator = field.sub(omega, field.one)
            assert denominator != field.zero
            for law in laws:
                r0, r1 = readout(field, law, length)
                mean_sum = field.sum(r1)
                expected = field.sum(field.root(-j) for j in range(length))
                assert mean_sum == expected
                count["mean_calibration"] += 1
                for y in range(m):
                    nxt = (y+1) % m
                    delta0 = r0[nxt]-r0[y]
                    delta1 = field.sub(field.mul(field.root(-1), r1[nxt]), r1[y])
                    numerator = field.sub(delta1, field.scale(omega, delta0))
                    target = field.scale(denominator, law[y])
                    assert numerator == target
                    count["local_inverse"] += 1
                    bad = {
                        "omit_relative_phase":
                            field.sub(field.sub(r1[nxt], r1[y]),
                                      field.scale(omega, delta0)),
                        "omit_static_difference": delta1,
                        "reverse_reconstruction_sign": field.scale(numerator, -1),
                        "omit_denominator": field.scale(field.one, law[y]),
                        "wrong_boundary_phase":
                            field.sub(delta1, field.scale(field.root(-length-1), delta0)),
                    }
                    for name, value in bad.items():
                        rejected[name] += value != target
    assert all(rejected.values())

    # At a full window only mass and one character remain.
    field = Field(4)
    uniform = (Q(1, 4),)*4
    opposite = (Q(1, 2), Q(0), Q(1, 2), Q(0))
    assert uniform != opposite
    assert readout(field, uniform, 4) == readout(field, opposite, 4)
    count["full_window_alias"] += 1

    # Machin's identity follows from tangent addition and the quadrant bounds.
    a5 = atan_enclosure(Q(1, 5), 20)
    a239 = atan_enclosure(Q(1, 239), 20)
    pi_interval = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
    assert Q(314, 100) < pi_interval[0] < pi_interval[1] < Q(22, 7)
    pi2 = (pi_interval[0]**2, pi_interval[1]**2)
    c16sq = Q(116281, 205)
    for h in range(1, 258):
        c, d = half_weight_times_pi_squared(h)
        lower = affine_interval(h*h*c-4, h*h*d, pi2)[0]
        upper = affine_interval(4-h*h*c, Q(1, 2)-h*h*d, pi2)[0]
        assert lower >= 0 and upper >= 0
        count["half_frame"] += 1
        cb, db = half_weight_times_pi_squared(16*h)
        assert db == 0
        top = affine_interval(c, d, pi2)[1]/cb
        assert top <= c16sq
        if h == 2:
            assert c/cb == c16sq
        count["times16_bound"] += 1

    # Direct integration of the centered piecewise linear primitive.
    relocations = []
    for epsilon in (Q(1, 7), Q(2, 19), Q(1, 101)):
        mean = epsilon**2/2
        coeff = (epsilon-mean, Q(-1))
        square = (coeff[0]**2, 2*coeff[0]*coeff[1], coeff[1]**2)
        integral_inside = sum((c*epsilon**(j+1)/Q(j+1)
                               for j, c in enumerate(square)), Q(0))
        integral_outside = (1-epsilon)*mean**2
        energy = integral_inside+integral_outside
        assert energy == epsilon**3/3-epsilon**4/4
        count["primitive_energy"] += 1
        relocations.append({"epsilon": str(epsilon), "Hminus1_squared": str(energy),
                            "interval_discrepancy_supremum": str(epsilon)})

    report = {
        "status": "PASS",
        "arithmetic": "exact fractions and independently built cyclotomic quotients",
        "domains": {
            "cyclic_sizes": list(range(2, 20))+[23, 29],
            "apertures": "all 1<=L<m",
            "laws_per_aperture": 3,
            "positions": "all y mod m",
            "continuum_frequencies": "1..257",
        },
        "checks": count,
        "mutation_rejections": rejected,
        "half_times16_sharp_squared": str(c16sq),
        "pi_interval": [str(x) for x in pi_interval],
        "local_mass_relocations": relocations,
        "universal_theorems_established_by_finite_run": False,
        "implementation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
