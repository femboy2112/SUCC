"""Exact finite pushforward of signed source mass and cross-path pairings.

A mathematical quotient preserves all class-constant linear and bilinear
observables exactly iff it retains their pushed-forward coefficients. This
implements exact rational calculations; it does not assert a theta-Petersson
identity or a proof of RH.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json


class MassSourceError(ValueError):
    pass


@dataclass(frozen=True)
class CoupledMass:
    source: str
    paths: tuple[str, ...]
    classes: tuple[str, ...]  # source path -> retained observational class
    linear: tuple[Fraction, ...]  # signed source weights
    pairing: tuple[tuple[Fraction, ...], ...]  # full cross-path kernel


def make_mass(source, paths, classes, linear, pairing) -> CoupledMass:
    m = CoupledMass(str(source), tuple(paths), tuple(classes),
                    tuple(Fraction(a) for a in linear),
                    tuple(tuple(Fraction(a) for a in row) for row in pairing))
    validate_mass(m)
    return m


def validate_mass(m: CoupledMass) -> None:
    n = len(m.paths)
    if not m.source or len(set(m.paths)) != n or any(type(p) is not str or not p for p in m.paths):
        raise MassSourceError('source or path labels are malformed')
    if len(m.classes) != n or any(type(c) is not str or not c for c in m.classes):
        raise MassSourceError('path quotient labels are malformed')
    if len(m.linear) != n or len(m.pairing) != n or any(len(row) != n for row in m.pairing):
        raise MassSourceError('incomplete source weights or pair coupling')
    if any(type(x) is not Fraction for x in m.linear) or any(
        type(x) is not Fraction for row in m.pairing for x in row):
        raise MassSourceError('non-rational or untyped source value')


def source_digest(m: CoupledMass) -> str:
    validate_mass(m)
    payload = [m.source, m.paths, m.classes,
               tuple((a.numerator, a.denominator) for a in m.linear),
               tuple(tuple((a.numerator, a.denominator) for a in row) for row in m.pairing)]
    return sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest()


@dataclass(frozen=True)
class CompressedMass:
    source: str
    classes: tuple[str, ...]
    linear: tuple[Fraction, ...]
    pairing: tuple[tuple[Fraction, ...], ...]


def compress_mass(m: CoupledMass) -> CompressedMass:
    """Push forward signed weights and EVERY cross-path kernel coefficient."""
    validate_mass(m)
    labels = tuple(dict.fromkeys(m.classes))
    k = len(labels)
    where = {label: i for i, label in enumerate(labels)}
    linear = [Fraction(0) for _ in range(k)]
    pairing = [[Fraction(0) for _ in range(k)] for _ in range(k)]
    for i, label in enumerate(m.classes):
        linear[where[label]] += m.linear[i]
        for j, other in enumerate(m.classes):
            pairing[where[label]][where[other]] += m.pairing[i][j]
    return CompressedMass(source_digest(m), labels, tuple(linear),
                          tuple(tuple(row) for row in pairing))


def verify_compressed_mass(m: CoupledMass, claim: CompressedMass) -> CompressedMass:
    """Independent by-group sums over the original path fiber."""
    if claim.source != source_digest(m):
        raise MassSourceError('changed source/coupling under compressed label')
    labels = tuple(dict.fromkeys(m.classes))
    if claim.classes != labels or len(claim.linear) != len(labels) or len(claim.pairing) != len(labels):
        raise MassSourceError('forged class quotient or dimensions')
    if any(len(row) != len(labels) for row in claim.pairing):
        raise MassSourceError('missing cross-path coefficients')
    for a, label in enumerate(labels):
        fiber = [i for i, c in enumerate(m.classes) if c == label]
        if claim.linear[a] != sum((m.linear[i] for i in fiber), Fraction(0)):
            raise MassSourceError('source linear mass not preserved')
        for b, label2 in enumerate(labels):
            fiber2 = [j for j, c in enumerate(m.classes) if c == label2]
            expected = sum((m.pairing[i][j] for i in fiber for j in fiber2), Fraction(0))
            if claim.pairing[a][b] != expected:
                raise MassSourceError('source cross-path coupling not preserved')
    return claim


def evaluate_compression(m: CoupledMass, claim: CompressedMass,
                         f, g=None) -> tuple[Fraction, Fraction]:
    """Returns (linear value, bilinear value), checking BOTH routes exactly.

    f and g are features on the CLASS quotient, not arbitrary source-path
    functions. A feature that varies within a class requires a finer quotient.
    """
    verify_compressed_mass(m, claim)
    f = tuple(Fraction(x) for x in f)
    g = f if g is None else tuple(Fraction(x) for x in g)
    if len(f) != len(claim.classes) or len(g) != len(claim.classes):
        raise MassSourceError('feature not defined on the quotient')
    idx = {label: i for i, label in enumerate(claim.classes)}
    raw_linear = sum((a * f[idx[c]] for a, c in zip(m.linear, m.classes)), Fraction(0))
    raw_pair = sum((m.pairing[i][j] * f[idx[ci]] * g[idx[cj]]
                    for i, ci in enumerate(m.classes) for j, cj in enumerate(m.classes)), Fraction(0))
    shrunk_linear = sum((a*x for a,x in zip(claim.linear,f)),Fraction(0))
    shrunk_pair = sum((claim.pairing[i][j]*f[i]*g[j]
                       for i in range(len(f)) for j in range(len(g))),Fraction(0))
    if (raw_linear, raw_pair) != (shrunk_linear, shrunk_pair):
        raise MassSourceError('compressed quantities disagree with original source')
    return shrunk_linear, shrunk_pair


def gaussian_shell_coupling(norm: int, order: int) -> CoupledMass:
    """Actual Z[i] shell; real/imaginary source channels computed EXACTLY."""
    from .principia_cm_theta import gaussian_shell, gaussian_power
    if norm < 0 or order < 0:
        raise MassSourceError('invalid Gaussian norm/jet order')
    points = gaussian_shell(norm)
    # For order divisible by 4 the complex powers are real; for order=2 on
    # norm=2 we retain the imaginary parts as an independent signed channel.
    if order % 4 == 0:
        weights = tuple(Fraction(gaussian_power(a,b,order)[0]) for a,b in points)
        if any(gaussian_power(a,b,order)[1] != 0 for a,b in points):
            raise MassSourceError('source powers are not in declared real channel')
        channel='real'
    elif order == 2:
        weights = tuple(Fraction(gaussian_power(a,b,order)[1]) for a,b in points)
        channel='imaginary'
    else:
        raise MassSourceError('unsupported source comparison channel')
    paths = tuple(f'point({a},{b})' for a,b in points)
    # The target observable has intentionally forgotten individual point labels.
    classes = tuple('Gaussian-shell-aggregate' for _ in points)
    kernel = tuple(tuple(a*b for b in weights) for a in weights)
    return make_mass(f'Z[i]:N={norm}:holomorphic-power={order}:channel={channel}',
                     paths, classes, weights, kernel)
