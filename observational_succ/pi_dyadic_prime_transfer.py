"""Dyadic carry tomography and exact cross-radix mesh transfer.

Local arithmetic identities only: none establishes a selected-source
collision saving or normality of pi. Every certificate is integer/Fraction
exact; the 2-adic *digit filtration* is not the 2-primary torsion quotient.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt

Q = Fraction


def _natural(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _prime(p: int) -> int:
    _natural(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("prime required")
    return p


def cross_radix_bad_cylinders(base: int, digits: int, bits: int) -> dict:
    """Exact number of length-'bits' dyadic cylinders straddling a b^-digits grid.

    Requires binary resolution >= target resolution (2^bits >= base^digits).
    Distinct grid boundaries then lie in distinct dyadic cells. A boundary
    aligns iff base^digits divides a*2^bits, giving exactly gcd-1 aligned
    interior boundaries. Thus bad = base^digits - gcd(base^digits,2^bits).
    """
    _natural(base, 2)
    _natural(digits, 1)
    _natural(bits)
    q, binary_cells = base ** digits, 1 << bits
    if binary_cells < q:
        raise ValueError("binary resolution must be at least target resolution")
    bad = q - gcd(q, binary_cells)
    return {"base": base, "digits": digits, "bits": bits,
            "target_cells": q, "binary_cells": binary_cells,
            "ambiguous_binary_cells": bad,
            "bad_haar_mass": Q(bad, binary_cells)}


def decode_target_prefix(binary_prefix: int, bits: int, base: int,
                         digits: int) -> int | None:
    """Decode a b-adic prefix from one dyadic interval, or refuse if ambiguous.

    Integer k represents the half-open interval [k/2^bits,(k+1)/2^bits).
    The output is an integer in 0,...,base^digits-1, not an assumed digit law.
    """
    _natural(bits)
    _natural(base, 2)
    _natural(digits, 1)
    _natural(binary_prefix)
    H = 1 << bits
    if binary_prefix >= H:
        raise ValueError("binary prefix outside range")
    b = base ** digits
    first = b * binary_prefix // H
    last = (b * (binary_prefix + 1) - 1) // H
    return first if first == last else None


def opposite_sides_same_binary_prefix(base: int, bits: int) -> tuple[Q, Q]:
    """Adversarial phases straddling 1/base inside one binary cylinder.

    For an odd base the boundary 1/base never lies on any dyadic grid.
    Hence for every finite bit-depth there are two indistinguishable binary
    prefixes with opposite first base-b digits. No *uniform* decoder delay.
    """
    _natural(base, 3)
    if base % 2 == 0:
        raise ValueError("odd base required")
    _natural(bits, 1)
    H = 1 << bits
    j = H // base
    t = Q(H, base) - j
    left = (j + t / 2) / H
    right = (j + (1 + t) / 2) / H
    assert Q(j, H) <= left < Q(1, base) < right < Q(j + 1, H)
    assert (int(H * left), int(H * right)) == (j, j)
    assert int(base * left) == 0 and int(base * right) >= 1
    return left, right


def _centered(value: Q) -> Q:
    return (value + Q(1, 2)) % 1 - Q(1, 2)


def _bbp_forcing(n: int) -> Q:
    _natural(n, 1)
    return (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
            - Q(1, 8 * n - 3) - Q(1, 8 * n - 2))


def _bbp_states(last_index: int) -> tuple[Q, ...]:
    _natural(last_index)
    states = [Q()]
    for n in range(1, last_index + 1):
        y = (16 * states[-1] + _bbp_forcing(n)) % 1
        assert y.denominator % 2 == 1
        states.append(y)
    return tuple(states)


def ramanujan_power_two(order: int, residue: int) -> int:
    """Primitive 2^order-th character shell as an exact *integer*."""
    _natural(order, 1)
    if order > 4:
        raise ValueError("this test instrument uses the 16-branch spectrum")
    _natural(residue)
    mod, half = 1 << order, 1 << (order - 1)
    if residue % mod == 0:
        return half
    if residue % half == 0:
        return -half
    return 0


def dyadic_carry_branch_certificate(p: int, radius: Q) -> dict:
    """All 16 centered BBP pair-carry branches, four binary gates, four shells.

    The authentic source y0=0 is reconstructed directly by Fraction. W is
    [m+1,4m) with m=(p-1)/8; W+ shifts by one, n=3m-1. epsilon bounds
    forcing difference. For epsilon<tau<=1/4, central κ=0 is exactly
    Z_W(tau) = {successor-close pairs with |current delta|<=1/32}.

    Each Q_j counts successor-close pairs with κ=0 (mod 2^j), 0<=j<=4.
    Q4=Z, and 16*Q4 = Q0 + sum_j primitive_2^j_shell.
    """
    _prime(p)
    if p % 8 != 1:
        raise ValueError("p must be 1 modulo 8")
    if type(radius) not in (int, Q):
        raise ValueError("integer or Fraction radius required")
    radius = Q(radius)
    m = (p - 1) // 8
    a, b = m + 1, 4 * m
    n = b - a
    # Keep source indexing explicit: forcing is defined for indices >=1.
    forces = [Q()] + [_bbp_forcing(i) for i in range(1, b + 1)]
    states = _bbp_states(b)
    epsilon = forces[a + 1] - forces[b]
    if not (Q() < epsilon < radius <= Q(1, 4)):
        raise ValueError("need actual source bound epsilon < tau <= 1/4")
    hist = [0] * 16
    central_direct = 0
    literal_carry_nonzero_at_central = 0
    for s in range(a, b):
        for t in range(a, b):
            delta = _centered(states[t] - states[s])
            nxt = _centered(states[t + 1] - states[s + 1])
            eta = forces[t + 1] - forces[s + 1]
            assert abs(eta) <= epsilon
            kappa = 16 * delta + eta - nxt
            assert kappa.denominator == 1 and -8 <= kappa <= 8
            if abs(nxt) > radius:
                continue
            label = int(kappa) % 16
            hist[label] += 1
            direct = abs(delta) <= Q(1, 32)
            if direct:
                central_direct += 1
                carry_t = (16 * states[t] + forces[t + 1]) // 1
                carry_s = (16 * states[s] + forces[s + 1]) // 1
                literal_carry_nonzero_at_central += (carry_t != carry_s)
            assert direct == (label == 0)
    counts = [sum(hist[k] for k in range(16) if k % (1 << j) == 0)
              for j in range(5)]
    shells = [sum(hist[k] * ramanujan_power_two(j, k)
                  for k in range(16)) for j in range(1, 5)]
    assert counts[4] == central_direct == hist[0]
    assert 16 * counts[4] == counts[0] + sum(shells)
    assert counts[0] >= n  # all diagonals remain
    # Positive deltas here quantify the *minimal observed additive allowance*
    # for each putative Qj<=Q(j-1)/2+cj*n. They do not certify uniform cj.
    gate_defect_per_n = [Q(2 * counts[j] - counts[j - 1], 2 * n)
                         for j in range(1, 5)]
    return {"prime": p, "window_start": a, "window_end_exclusive": b,
            "window_length": n, "radius": str(radius),
            "forcing_drift": str(epsilon), "branch_histogram": hist,
            "dyadic_nested_counts": counts,
            "ramanujan_shells": shells,
            "observed_gate_defect_per_n": list(map(str, gate_defect_per_n)),
            "zero_centered_branch": central_direct,
            "central_pairs_with_different_literal_carries":
                literal_carry_nonzero_at_central,
            "spectral_identity_verified": True}
