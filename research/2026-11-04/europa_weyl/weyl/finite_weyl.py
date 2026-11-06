"""Finite Weyl labels and source coordinates; no dense matrices or pi oracle."""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm

TAPS = tuple(map(Fraction, (2, 2, 1, 0, "-1/2", "-1/2", "-1/4", 0)))


def forcing(n):
    if n < 1:
        raise ValueError("positive source time required")
    return sum(w / (8 * (n - 1) + j) for j, w in enumerate(TAPS, 1))


def trajectory(t):
    if t < 0:
        raise ValueError("negative horizon")
    conductor = 1
    positions = [Fraction(0)]
    for n in range(1, t + 1):
        inc = forcing(n)
        conductor = lcm(conductor, inc.denominator)
        positions.append((16 * positions[-1] + inc) % 1)
    return conductor, positions


def coordinate(value, modulus):
    residue = (value % 1) * modulus
    if residue.denominator != 1:
        raise ValueError("unrepresented rational position")
    return int(residue)


def preimage(position, increment, modulus):
    return ((position - increment) * pow(16, -1, modulus)) % modulus


def action(label, ket, modulus):
    """D(u,h) ket = e_M(h*x+uh/2) |x+u>, return ket index and phase exponent."""
    u, h = label
    return (ket + u) % modulus, (h * (ket + u * pow(2, -1, modulus))) % modulus


def cocycle(left, right, modulus):
    u, h = left
    v, k = right
    return ((h * v - k * u) * pow(2, -1, modulus)) % modulus


def affine_conjugate(label, increment, modulus):
    u, h = label
    dual = h * pow(16, -1, modulus) % modulus
    return (16 * u % modulus, dual), (-increment * dual) % modulus


def empirical_character(positions, h, modulus):
    """Exact formal root-of-unity sum, divided by sample size by the caller."""
    return Counter(h * coordinate(x, modulus) % modulus for x in positions)


def character_lift(coarse, fine):
    """Smallest nonnegative *additive global section* of labels, at h=1."""
    if fine % coarse or coarse < 1:
        raise ValueError("expected divisible conductors")
    ratio = fine // coarse
    if gcd(ratio, coarse) != 1:
        raise ValueError("restriction does not split")
    return ratio * pow(ratio, -1, coarse)
