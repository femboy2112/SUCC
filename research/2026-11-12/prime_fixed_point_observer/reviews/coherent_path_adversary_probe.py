"""Exact present-output controls for phase, coherence, recovery and causality.

Self-contained Gaussian-rational matrix implementation; no floating decisions,
quantum device, history oracle, or assertion about physical collapse.  All
input states below are finite.  Universal claims belong to the companion proof.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path
from random import Random


@dataclass(frozen=True)
class Q:
    real: F = F(0)
    imag: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "real", F(self.real))
        object.__setattr__(self, "imag", F(self.imag))

    def __add__(self, value):
        value = number(value)
        return Q(self.real + value.real, self.imag + value.imag)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.real, -self.imag)

    def __sub__(self, value):
        return self + (-number(value))

    def __mul__(self, value):
        value = number(value)
        return Q(self.real * value.real - self.imag * value.imag,
                 self.real * value.imag + self.imag * value.real)

    __rmul__ = __mul__

    def __truediv__(self, value):
        return Q(self.real / F(value), self.imag / F(value))

    def conjugate(self):
        return Q(self.real, -self.imag)

    def abs2(self):
        return self.real ** 2 + self.imag ** 2


def number(value):
    return value if isinstance(value, Q) else Q(value)


ZERO, ONE, I = Q(), Q(1), Q(0, 1)


def mat(rows):
    rows = tuple(tuple(number(value) for value in row) for row in rows)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("nonempty rectangular matrix required")
    return rows


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def mul(a, b):
    if len(a[0]) != len(b):
        raise ValueError("matrix shape mismatch")
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
                       for j in range(len(b[0]))) for i in range(len(a)))


def tensor(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def scale(a, c):
    return tuple(tuple(c * value for value in row) for row in a)


def plus(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix shape mismatch")
    return tuple(tuple(x + y for x, y in zip(row, other))
                 for row, other in zip(a, b))


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def density(v):
    v = tuple(number(value) for value in v)
    norm = sum(value.abs2() for value in v)
    if not norm:
        raise ValueError("nonzero vector required")
    return tuple(tuple(x * y.conjugate() / norm for y in v) for x in v)


def transform(a, rho):
    return mul(mul(a, rho), dagger(a))


def keep_left(rho, left, right):
    return tuple(tuple(sum((rho[i * right + k][j * right + k]
                            for k in range(right)), ZERO)
                       for j in range(left)) for i in range(left))


def keep_right(rho, left, right):
    return tuple(tuple(sum((rho[k * right + i][k * right + j]
                            for k in range(left)), ZERO)
                       for j in range(right)) for i in range(right))


def moment(rho, observable):
    return trace(mul(rho, observable))


def rho_gamma(gamma):
    gamma = number(gamma)
    if gamma.abs2() > 1:
        raise ValueError("coherence parameter lies outside the unit disk")
    return mat([[F(1, 2), 0, 0, gamma / 2],
                [0, 0, 0, 0], [0, 0, 0, 0],
                [gamma.conjugate() / 2, 0, 0, F(1, 2)]])


def run():
    checks = Counter()

    def check(group, condition):
        checks[group] += 1
        if not condition:
            raise AssertionError(f"{group}: check {checks[group]} failed")

    ident = eye(2)
    x = mat([[0, 1], [1, 0]])
    y = mat([[0, -I], [I, 0]])
    z = mat([[1, 0], [0, -1]])
    xx, xy, yy, zz = [tensor(a, b) for a, b in [(x, x), (x, y), (y, y), (z, z)]]
    zi = tensor(z, ident)
    phi = rho_gamma(ONE)
    check("calibration", I * I == Q(-1))
    check("calibration", mul(x, y) == scale(z, I))
    check("calibration", mul(phi, phi) == phi)
    check("calibration", trace(phi) == ONE)
    try:
        rho_gamma(Q(1, 1))
    except ValueError:
        check("calibration", True)
    else:
        check("calibration", False)

    # Denominator 13 is a fresh region outside the design examples on /5.
    families = {}
    for denominator in (5, 13):
        cases = [Q(F(a, denominator), F(b, denominator))
                 for a in range(-denominator, denominator + 1)
                 for b in range(-denominator, denominator + 1)
                 if a * a + b * b <= denominator * denominator]
        families[denominator] = len(cases)
        for gamma in cases:
            rho = rho_gamma(gamma)
            check("quadrature_reconstruction", rho == dagger(rho))
            check("quadrature_reconstruction", trace(rho) == ONE)
            check("quadrature_reconstruction", moment(rho, zz) == ONE)
            check("quadrature_reconstruction", moment(rho, zi) == ZERO)
            check("quadrature_reconstruction", moment(rho, xx) == Q(gamma.real))
            check("quadrature_reconstruction", moment(rho, xy) == Q(-gamma.imag))
            check("quadrature_reconstruction", moment(rho, yy) == Q(-gamma.real))
            check("quadrature_reconstruction",
                  moment(rho, xx) - I * moment(rho, xy) == gamma)
            check("purity_and_marginals", trace(mul(rho, rho)) == Q((1 + gamma.abs2()) / 2))
            check("purity_and_marginals", keep_left(rho, 2, 2) == scale(ident, F(1, 2)))
            check("purity_and_marginals", keep_right(rho, 2, 2) == scale(ident, F(1, 2)))
            check("bell_overlap", moment(rho, phi) == Q((1 + gamma.real) / 2))

    # Same one-quadrature/current Bell output; different accessible purity.
    pure, mixed = rho_gamma(I), rho_gamma(ZERO)
    check("phase_vs_leakage", moment(pure, phi) == moment(mixed, phi) == Q(F(1, 2)))
    check("phase_vs_leakage", moment(pure, xx) == moment(mixed, xx) == ZERO)
    check("phase_vs_leakage", moment(pure, xy) == Q(-1))
    check("phase_vs_leakage", moment(mixed, xy) == ZERO)
    check("phase_vs_leakage", trace(mul(pure, pure)) == ONE)
    check("phase_vs_leakage", trace(mul(mixed, mixed)) == Q(F(1, 2)))
    for p in (ONE, -ONE, I, -I, Q(F(3, 5), F(4, 5)), Q(F(5, 13), F(12, 13))):
        for radius in (F(0), F(2, 7), F(3, 5), F(1)):
            phase_correction = tensor(mat([[1, 0], [0, p]]), ident)
            before = rho_gamma(radius * p)
            after = transform(phase_correction, before)
            check("phase_calibration", after == rho_gamma(radius))
            check("phase_calibration", trace(mul(before, before)) == trace(mul(after, after)))
    check("holonomy_without_decoherence", transform(tensor(z, ident), phi) == rho_gamma(-ONE))
    check("global_phase", transform(scale(eye(4), -ONE), phi) == phi)
    # A wrong but unitary assignment to a declared involution still admits twins.
    wrong = mat([[1, 0], [0, I]])
    check("shared_invalid_relation", mul(wrong, wrong) != ident)
    check("shared_invalid_relation", transform(tensor(wrong, dagger(wrong)), phi) == phi)

    # Deliberate outside-family states defeat an unguarded XX/XY-only protocol.
    product_plus = density([1, 1, 1, 1])
    odd_bell = density([0, 1, 1, 0])
    for rho in (product_plus, odd_bell):
        check("sector_guard", moment(rho, xx) == ONE and moment(rho, xy) == ZERO)
        check("sector_guard", moment(rho, zz) != ONE)
    imbalanced = density([3, 0, 0, 4])
    check("sector_guard", moment(imbalanced, zz) == ONE)
    check("sector_guard", moment(imbalanced, zi) != ZERO)

    # Explicit unitary environment record generation with rational amplitudes.
    for c, s in ((F(1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(0), F(1))):
        for p in (ONE, I, Q(F(3, 5), F(4, 5))):
            vector = [ZERO] * 8
            vector[0], vector[6], vector[7] = ONE, c * p, s * p
            whole = density(vector)
            reduced = keep_left(whole, 4, 2)
            check("environment_overlap", trace(mul(whole, whole)) == ONE)
            check("environment_overlap", reduced == rho_gamma(c * p.conjugate()))

    # A local trace-preserving operation has no effect on the other marginal.
    rotation = mat([[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]])
    channels = [
        (rotation,),
        (mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]])),
        (mat([[1, 0], [0, F(3, 5)]]), mat([[0, F(4, 5)], [0, 0]])),
        (mat([[1, 0], [0, 0]]), mat([[0, 1], [0, 0]])),
    ]
    rng = Random(2026111291)
    inputs = [density([Q(F(rng.randrange(-5, 6), 7), F(rng.randrange(-5, 6), 11))
                       for _ in range(4)]) for _ in range(16)]
    for kraus in channels:
        completeness = mat([[0, 0], [0, 0]])
        for k in kraus:
            completeness = plus(completeness, mul(dagger(k), k))
        check("no_signalling", completeness == ident)
        for rho in inputs:
            after = mat([[0] * 4 for _ in range(4)])
            for k in kraus:
                after = plus(after, transform(tensor(k, ident), rho))
            check("no_signalling", keep_right(after, 2, 2) == keep_right(rho, 2, 2))
            check("no_signalling", trace(after) == ONE)

    # Current purity after meeting postselection is not a path certificate.
    accepted = mul(mul(phi, mixed), phi)
    probability = trace(accepted)
    check("postselection_counterexample", probability == Q(F(1, 2)))
    check("postselection_counterexample", scale(accepted, F(2)) == phi)
    check("postselection_counterexample", trace(mul(mixed, mixed)) == Q(F(1, 2)))

    # GHZ record, environmental eraser, and feed-forward at the present meeting.
    ghz = density([1, 0, 0, 0, 0, 0, 0, 1])
    check("eraser", keep_left(ghz, 4, 2) == mixed)
    branches = []
    corrected = mat([[0] * 4 for _ in range(4)])
    for sign in (1, -1):
        env_projector = scale(mat([[1, sign], [sign, 1]]), F(1, 2))
        branch = transform(tensor(eye(4), env_projector), ghz)
        check("eraser", trace(branch) == Q(F(1, 2)))
        current = keep_left(branch, 4, 2)
        check("eraser", scale(current, F(2)) == rho_gamma(sign))
        branches.append(current)
        correction = eye(4) if sign == 1 else tensor(z, ident)
        corrected = plus(corrected, transform(correction, current))
    check("eraser", plus(*branches) == mixed)
    check("eraser", corrected == phi)

    # Two different internal histories have exactly the same final joint state.
    permutation = [[0] * 8 for _ in range(8)]
    for source in range(8):
        target = source ^ (1 if source & 4 else 0)
        permutation[target][source] = 1
    cnot_ae = mat(permutation)
    initial = density([1, 0, 0, 0, 0, 0, 1, 0])
    intermediate = transform(cnot_ae, initial)
    final = transform(cnot_ae, intermediate)
    check("history_nonidentifiability", intermediate == ghz)
    check("history_nonidentifiability", final == initial)
    check("history_nonidentifiability", keep_left(intermediate, 4, 2) == mixed)
    check("history_nonidentifiability", keep_left(final, 4, 2) == phi)
    phase_average = scale(plus(rho_gamma(ONE), rho_gamma(-ONE)), F(1, 2))
    check("mechanism_nonidentifiability", phase_average == keep_left(ghz, 4, 2))

    # Imperfect sector guards: test exact algebra on arbitrary current states.
    even_projector = mat([[1, 0, 0, 0], [0, 0, 0, 0],
                          [0, 0, 0, 0], [0, 0, 0, 1]])
    guard_inputs = inputs + [plus(scale(inputs[j], F(3, 7)),
                                  scale(inputs[(j + 3) % len(inputs)], F(4, 7)))
                             for j in range(len(inputs))]
    guard_inputs += [phi, mixed, product_plus, imbalanced, scale(eye(4), F(1, 4))]
    for rho in guard_inputs:
        zv, uv, xv, yv = [moment(rho, observable)
                          for observable in (zz, zi, xx, xy)]
        check("robust_guard_algebra", all(value.imag == 0 for value in (zv, uv, xv, yv)))
        epsilon = (1 - zv.real) / 2
        p = 1 - epsilon
        check("robust_guard_algebra", 0 <= epsilon < 1)
        tau = scale(mul(mul(even_projector, rho), even_projector), 1 / p)
        gamma = 2 * rho[0][3] / p
        imbalance = (rho[0][0].real - rho[3][3].real) / p
        check("robust_guard_algebra", trace(tau) == ONE)
        check("robust_guard_algebra", gamma.abs2() <= 1)
        check("robust_guard_algebra", imbalance ** 2 <= ((abs(uv.real) + epsilon) / p) ** 2)
        check("robust_guard_algebra", xv - I * yv == 2 * rho[0][3] + 2 * rho[1][2].conjugate())
        check("robust_guard_algebra", (2 * rho[1][2]).abs2() <= epsilon ** 2)
        check("robust_guard_algebra", ((xv - I * yv) / p - gamma).abs2() <= (epsilon / p) ** 2)
        balanced_difference = plus(tau, scale(rho_gamma(gamma), -1))
        expected_difference = mat([[imbalance / 2, 0, 0, 0], [0, 0, 0, 0],
                                   [0, 0, 0, 0], [0, 0, 0, -imbalance / 2]])
        check("robust_guard_algebra", balanced_difference == expected_difference)

    # Radial projection is checked on exact rational rays outside the disk.
    unit_rays = (ONE, -ONE, I, -I, Q(F(3, 5), F(4, 5)), Q(F(5, 13), F(-12, 13)))
    disk_targets = (ZERO, ONE, I, Q(F(1, 3), F(2, 3)), Q(F(-3, 5), F(4, 5)))
    for unit_ray in unit_rays:
        for radius in (F(1), F(6, 5), F(2), F(17, 3)):
            for gamma in disk_targets:
                estimate = radius * unit_ray
                projected = unit_ray
                check("radial_projection_contraction",
                      (projected - gamma).abs2() <= (estimate - gamma).abs2())

    # Independent complete trace distance on commuting Bell-diagonal states.
    # The columns of this matrix have norm sqrt(2), so divide by two after
    # conjugation. This avoids approximating square roots or eigenvalues.
    bell_basis = mat([[1, 1, 0, 0], [0, 0, 1, 1],
                      [0, 0, 1, -1], [1, -1, 0, 0]])
    check("robust_trace_distance_calibration", mul(dagger(bell_basis), bell_basis) == scale(eye(4), 2))

    def bell_distance(rho, other):
        difference = plus(rho, scale(other, -1))
        rotated = scale(mul(mul(dagger(bell_basis), difference), bell_basis), F(1, 2))
        if any(rotated[i][j] != ZERO for i in range(4) for j in range(4) if i != j):
            raise AssertionError("Bell-distance oracle used outside its commuting domain")
        if any(rotated[i][i].imag != 0 for i in range(4)):
            raise AssertionError("Hermitian difference has nonreal diagonal")
        return sum(abs(rotated[i][i].real) for i in range(4)) / 2

    even_to_odd = tensor(x, ident)
    for square_root in (F(0), F(1, 10), F(3, 10), F(1, 2), F(3, 4)):
        epsilon, p = square_root ** 2, 1 - square_root ** 2
        for a in (F(-1), F(-3, 5), F(0), F(3, 5), F(1)):
            for b in (F(-1), F(-3, 5), F(0), F(3, 5), F(1)):
                rho = plus(scale(rho_gamma(a), p),
                           scale(transform(even_to_odd, rho_gamma(b)), epsilon))
                sx, sy = moment(rho, xx), moment(rho, xy)
                check("robust_full_bound", moment(rho, zz) == Q(1 - 2 * epsilon))
                check("robust_full_bound", moment(rho, zi) == ZERO)
                check("robust_full_bound", sx == Q(p * a + epsilon * b) and sy == ZERO)
                for perturbation in (F(0), F(-1, 10), F(1, 10)):
                    unprojected = (sx.real + perturbation) / p
                    g = min(F(1), max(F(-1), unprojected))
                    distance = bell_distance(rho, rho_gamma(g))
                    bound = min(F(1), square_root +
                                (2 * epsilon + abs(perturbation)) / (2 * p))
                    check("robust_noisy_quadratures", distance <= bound)
                    check("robust_noisy_quadratures", (g - a) ** 2 <=
                          ((epsilon + abs(perturbation)) / p) ** 2)

    # Pure cross-sector states attain the sqrt(epsilon) projection loss.
    # Pythagorean triples give rational square roots for exact comparison.
    for a, b, hypotenuse in ((1, 0, 1), (4, 3, 5), (12, 5, 13), (99, 20, 101)):
        for phase in (ONE, I, Q(F(3, 5), F(4, 5))):
            rho = density([a, b * phase, b * phase, a])
            epsilon, p = F(b * b, hypotenuse * hypotenuse), F(a * a, hypotenuse * hypotenuse)
            tau = scale(mul(mul(even_projector, rho), even_projector), 1 / p)
            check("robust_pure_projection", tau == phi)
            check("robust_pure_projection", ONE - moment(rho, phi) == Q(epsilon))
            check("robust_pure_projection", moment(rho, xx) == ONE and moment(rho, xy) == ZERO)
            bound = min(F(1), F(b, hypotenuse) + epsilon / p)
            check("robust_pure_projection", epsilon <= bound * bound)
    check("robust_zero_sector_boundary", moment(odd_bell, zz) == Q(-1))

    return {
        "status": "PASS", "exact_checks": sum(checks.values()), "groups": dict(checks),
        "gamma_grid_cases": families,
        "key_counterexample": {
            "pure_gamma": "i", "mixed_gamma": "0", "both_bell_overlap": "1/2",
            "pure_XY": "-1", "mixed_XY": "0", "pure_purity": "1", "mixed_purity": "1/2",
            "same_local_marginals": "I/2",
        },
        "postselection": {"dephased_input_success_probability": "1/2", "conditional_output": "Phi+"},
        "scope": "Exact finite matrix controls, not a device run, history reconstruction, arithmetic theorem or objective-collapse experiment.",
        "source_dependency": "Self-contained standard-library Gaussian-rational and tensor implementation; companion universal proofs are separate from the finite enumeration.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if options.output:
        options.output.write_text(rendered)
    print(rendered, end="")
