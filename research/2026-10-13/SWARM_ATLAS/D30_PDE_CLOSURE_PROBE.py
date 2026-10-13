#!/usr/bin/env python3
"""Bounded exact Fourier closure witnesses; standard library, no PDE time stepping."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform


@dataclass(frozen=True)
class C:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    def __add__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-other if isinstance(other, C) else -C(other))

    def __mul__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def conj(self):
        return C(self.r, -self.i)

    def norm2(self):
        return self.r * self.r + self.i * self.i


ZERO = C()
I = C(0, 1)


def clean(p):
    result = {k: z for k, z in p.items() if z != ZERO}
    assert len(result) <= 128, "Bounded probe exceeded its support cap"
    return result


def add(*polys):
    out = {}
    for p in polys:
        for k, z in p.items():
            out[k] = out.get(k, ZERO) + z
    return clean(out)


def scale(a, p):
    return clean({k: a * z for k, z in p.items()})


def multiply(p, q):
    out = {}
    for k, z in p.items():
        for l, t in q.items():
            m = (k[0] + l[0], k[1] + l[1])
            out[m] = out.get(m, ZERO) + z * t
    return clean(out)


def derivative(p, j):
    return clean({k: I * k[j] * z for k, z in p.items()})


def laplace(p):
    return clean({k: -(k[0] ** 2 + k[1] ** 2) * z for k, z in p.items()})


def cutoff(p, n=1):
    return {k: z for k, z in p.items() if max(map(abs, k)) <= n}


def cosine(k):
    return {k: C(Q(1, 2)), (-k[0], -k[1]): C(Q(1, 2))}


def sine(k):
    return {k: C(0, Q(-1, 2)), (-k[0], -k[1]): C(0, Q(1, 2))}


def vector(a, p):
    return tuple(scale(t, p) for t in a)


def vadd(*vs):
    return tuple(add(*(v[j] for v in vs)) for j in range(2))


def vscale(a, v):
    return tuple(scale(a, p) for p in v)


def project(v):
    return tuple(cutoff(p) for p in v)


def divergence(v):
    return add(derivative(v[0], 0), derivative(v[1], 1))


def validate(v):
    for p in v:
        for k, z in p.items():
            if p.get((-k[0], -k[1]), ZERO) != z.conj():
                raise ValueError("Source coefficients must define a real field")
    if divergence(v):
        raise ValueError("Incompressible source must be divergence-free")


def leray(v):
    out = ({}, {})
    for k in set(v[0]) | set(v[1]):
        z = tuple(p.get(k, ZERO) for p in v)
        denominator = k[0] ** 2 + k[1] ** 2
        # No inverse-Laplacian pole at zero: the mean is retained explicitly.
        dot = k[0] * z[0] + k[1] * z[1]
        for j in range(2):
            out[j][k] = z[j] if not denominator else z[j] - Q(k[j], denominator) * dot
    return tuple(clean(p) for p in out)


def stress(v, w):
    return tuple(tuple(multiply(v[i], w[j]) for j in range(2)) for i in range(2))


def div_stress(t):
    return tuple(add(*(derivative(t[i][j], j) for j in range(2))) for i in range(2))


def advect(v, w):
    return tuple(add(*(multiply(v[j], derivative(w[i], j)) for j in range(2))) for i in range(2))


def acceleration(v):
    validate(v)
    return vadd(tuple(laplace(p) for p in v), vscale(-1, leray(advect(v, v))))


def norm2(v):
    return sum((z.norm2() for p in v for z in p.values()), Q())


def encode(p):
    return [{"mode": list(k), "real": str(z.r), "imag": str(z.i)} for k, z in sorted(p.items())]


def encode_vector(v):
    return [encode(p) for p in v]


def mixed_projection(p):
    """Orthogonal projection onto constants and cos x + cos 2x."""
    phi = add(cosine((1, 0)), cosine((2, 0)))
    inner = sum((p.get(k, ZERO) * z.conj() for k, z in phi.items()), ZERO)
    out = scale(inner, phi)  # normalized L2 norm squared of phi is one.
    if (0, 0) in p:
        out[(0, 0)] = p[(0, 0)]
    return out


def rejected(v):
    try:
        validate(v)
    except ValueError:
        return True
    return False


def main():
    null = ({}, {})
    a = vector((0, 1), cosine((2, 0)))
    b = vector((1, 2), cosine((-2, 1)))
    w = vadd(a, b)
    validate(w)
    assert project(w) == null
    t = stress(w, w)
    filtered_t = tuple(tuple(cutoff(p) for p in row) for row in t)
    force = project(leray(div_stress(t)))
    expected_force = vector((Q(-1, 2), 0), sine((0, 1)))
    assert force == expected_force and norm2(force) == Q(1, 8)
    assert advect(w, w) == div_stress(t)
    assert project(acceleration(w)) == vscale(-1, expected_force)
    assert project(acceleration(null)) == null
    assert project(vadd(acceleration(w), vscale(-1, acceleration(null)))) != null

    # Constant hidden stress exists, but its force vanishes: retain this control.
    mean_t = tuple(tuple(cutoff(p) for p in row) for row in stress(a, a))
    assert mean_t[1][1] == {(0, 0): C(Q(1, 2))}
    assert div_stress(mean_t) == null

    # Complete factorial resolved/hidden control; each single plane wave is null.
    v = vector((0, 1), cosine((1, 0)))
    h = b
    mixed = vadd(project(acceleration(vadd(v, h))),
                 vscale(-1, project(acceleration(v))),
                 vscale(-1, project(acceleration(h))), project(acceleration(null)))
    assert project(h) == null and project(v) == v
    assert project(acceleration(v)) == tuple(laplace(p) for p in v)
    assert project(acceleration(h)) == null
    expected_mixed = vector((1, 1), sine((-1, 1)))
    assert mixed == expected_mixed and norm2(mixed) == 1
    hidden_only_model = vadd(project(acceleration(v)), project(acceleration(h)))
    assert project(acceleration(vadd(v, h))) != hidden_only_model

    def maxwell_linear(fields):
        return (scale(-1, derivative(fields[1], 0)),
                scale(-1, derivative(fields[0], 0)))

    maxwell_fields = (add(cosine((1, 0)), cosine((2, 0))), cosine((2, 0)))
    assert project(maxwell_linear(maxwell_fields)) == maxwell_linear(project(maxwell_fields))

    # Fourier derivative/projection commutation; hostile mixed-eigenspace filter.
    for p in w:
        assert cutoff(cutoff(p)) == cutoff(p)
        assert cutoff(laplace(p)) == laplace(cutoff(p))
        for j in range(2):
            assert cutoff(derivative(p, j)) == derivative(cutoff(p), j)
    assert leray(leray(div_stress(t))) == leray(div_stress(t))
    f = cosine((1, 0))
    assert mixed_projection(mixed_projection(f)) == mixed_projection(f)
    dq = add(mixed_projection(derivative(f, 0)), scale(-1, derivative(mixed_projection(f), 0)))
    lq = add(mixed_projection(laplace(f)), scale(-1, laplace(mixed_projection(f))))
    assert dq and lq == scale(Q(3, 2), cosine((2, 0)))
    assert norm2((lq, {})) == Q(9, 8)
    # Omitting Leray, derivative direction or reality/incompressibility is caught.
    assert project(div_stress(t)) != expected_force
    swapped = tuple(add(derivative(t[i][0], 1), derivative(t[i][1], 0)) for i in range(2))
    assert project(leray(swapped)) != expected_force
    assert rejected(vector((1, 0), cosine((2, 0))))
    assert rejected(({(2, 0): C(1)}, {}))
    mean = ({(0, 0): C(2)}, {(0, 0): C(-3)})
    assert leray(mean) == mean and divergence(mean) == {}

    # Fresh changed-frequency instance, chosen before execution.
    fresh = vadd(vector((0, 1), cosine((3, 0))),
                 vector((1, 3), cosine((-3, 1))))
    validate(fresh)
    assert project(fresh) == null
    assert project(leray(div_stress(stress(fresh, fresh)))) == expected_force

    source_paths = ["provenance/IMPORT_MANIFEST.json",
                    "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
                    "research/2026-10-12/HISTORICAL_GALILEO_LORENTZ_SUCC_TRANSITION.md",
                    "research/2026-10-12/DYNAMIC_FOURIER_VIRTUAL_ZERO_FRONTIER.md",
                    "research/2026-10-12/FIELD_RELATIVE_CLOSURE_AND_OBSTRUCTION_CALCULUS.md"]
    hashes = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in source_paths}
    hashes[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps({
        "dossier": "D30", "status": "TESTED MODEL", "arithmetic": "Gaussian rationals",
        "base_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "origin_commit": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
        "origin_foundations_blob": "04408ed96bd369b5063868eb5ad5664824d18043",
        "python": platform.python_version(), "domain": "T^2=(R/2piZ)^2",
        "projection": "componentwise |k|_infinity <= 1; Leray(0)=I",
        "norm": "normalized L2, Parseval sum of coefficient moduli squared",
        "hidden_source": encode_vector(w), "projected_source": encode_vector(project(w)),
        "projected_stress": [[encode(p) for p in row] for row in filtered_t],
        "projected_leray_stress_force": encode_vector(force), "force_norm_squared": "1/8",
        "resolved_acceleration": encode_vector(project(acceleration(w))),
        "mean_stress_control": [[encode(p) for p in row] for row in mean_t],
        "mean_stress_divergence": encode_vector(div_stress(mean_t)),
        "factorial_cross_acceleration": encode_vector(mixed), "cross_norm_squared": "1",
        "factorial_sources": {"resolved_v": encode_vector(v), "hidden_h": encode_vector(h)},
        "factorial_cells": {"00": encode_vector(project(acceleration(null))),
                            "10": encode_vector(project(acceleration(v))),
                            "01": encode_vector(project(acceleration(h))),
                            "11": encode_vector(project(acceleration(vadd(v, h))))},
        "noncommuting_filter_derivative_defect": encode(dq),
        "noncommuting_filter_laplacian_defect": encode(lq), "defect_norm_squared": "9/8",
        "controls": {"omitted_leray_killed": True, "omitted_cross_terms_killed": True,
                     "swapped_derivatives_killed": True, "noncommuting_filter_killed": True,
                     "compressible_source_rejected": True, "nonreal_source_rejected": True,
                     "zero_mode_pole_guard_passed": True, "fresh_frequency_passed": True,
                     "linear_maxwell_commutation_passed": True},
        "input_sha256": hashes,
        "scope": "Instantaneous identities, not time integration, formal proof or physical attestation"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
