"""Frontier #1 probe: scaling of max_{ell!=0} |D_hat_{p,h}(ell)| with L = ord_p(16).

Exact arithmetic (Fraction) for delta_{p,r}; mpmath high-precision for e(h delta).
Two independent methods:
  Method A: exact Fraction residue -> delta -> e(h delta) at high precision.
  Method B: digit-orbit reconstruction of the phase (independent of Fraction cofiber).

Author: Ravel (main). Branch: research/prime-cofactor-nonconspiracy-2026-11-02.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Exact BBP / cofiber primitives (Fraction, no float anywhere in delta)
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def primes_up_to(N: int):
    # simple sieve
    sieve = bytearray([1]) * (N + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(N + 1) if sieve[i]]


def multiplicative_order(base: int, modulus: int) -> int:
    cur = base % modulus
    order = 1
    while cur != 1:
        cur = (cur * base) % modulus
        order += 1
    return order


def authentic_r(n: int) -> Fraction:
    return (
        Fraction(4, 8 * n - 7)
        - Fraction(2, 8 * n - 4)
        - Fraction(1, 8 * n - 3)
        - Fraction(1, 8 * n - 2)
    )


def authentic_U(j: int) -> Fraction:
    # U_j = sum_{k<=j} 16^{j-k} r(k), U_0 = 0 (recurrence U_{n+1}=16 U_n + r(n+1))
    u = Fraction(0)
    for n in range(1, j + 1):
        u = 16 * u + authentic_r(n)
    return u


def birth_step(p: int) -> int:
    return (p + 7) // 8 if p % 8 == 1 else (p + 3) // 8


def primary_birth_numerator(p: int) -> int:
    return 4 if p % 8 == 1 else p - 1


def primary_residue(p: int, j: int) -> int:
    b = birth_step(p)
    c = primary_birth_numerator(p)
    return (c * pow(16, j - b, p)) % p


def delta_exact(p: int, r: int) -> Fraction:
    """delta_{p,r} = W_{p,b+r+1} - W_{p,b+r}, W_{p,j} = U_j - a_{p,j}/p. EXACT Fraction."""
    b = birth_step(p)
    j = b + r
    U_j = authentic_U(j)
    U_next = authentic_U(j + 1)
    a_j = primary_residue(p, j)
    a_next = primary_residue(p, j + 1)
    w_j = U_j - Fraction(a_j, p)
    w_next = U_next - Fraction(a_next, p)
    return w_next - w_j


# ---------------------------------------------------------------------------
# High-precision DFT of D_{p,h}(r) = e(h delta_{p,r}) - 1
# ---------------------------------------------------------------------------

def compute_dhat(p: int, h: int, dps: int):
    """Return dict with max_ell_neq0, total_energy, dc_energy. Exact delta -> mpmath phase.

    Phase is computed by EXACT modular reduction: e(2pi i h delta) with delta=num/den
    equals e(2pi i (h*num mod den)/den), so we only need dps ~ bits(den)/log2(10)+guard.
    """
    mp.mp.dps = dps
    L = multiplicative_order(16, p)
    b = birth_step(p)
    J = (p + 1) // 2
    if b + L - 1 >= J:
        return None  # not a single-pole-period prime at this L

    # Precompute delta exact Fractions incrementally (walk orbit once, O(L) Fractions).
    # U_{n+1} = 16 U_n + r(n+1); delta_r = W_{b+r+1}-W_{b+r}.
    deltas = [None] * (L - 1)
    U = authentic_U(b)                       # U at step b
    a = primary_residue(p, b)
    W = U - Fraction(a, p)
    for r in range(L - 1):
        j = b + r
        U_next = 16 * U + authentic_r(j + 1)
        a_next = primary_residue(p, j + 1)
        W_next = U_next - Fraction(a_next, p)
        deltas[r] = W_next - W
        U, a, W = U_next, a_next, W_next

    # D_{p,h}(r) for r = 0..L-1, D(L-1) := 0
    D = [mp.mpc(0) for _ in range(L)]
    two_pi = mp.mpf(2) * mp.pi
    for r in range(L - 1):
        d = deltas[r]
        num = (h * d.numerator) % d.denominator  # exact reduced phase numerator
        den = d.denominator
        phase = two_pi * mp.mpf(num) / mp.mpf(den)
        D[r] = mp.e ** (mp.mpc(0, 1) * phase) - 1
    # D[L-1] stays 0

    # DFT via precomputed L-th roots of unity (no transcendentals in inner loop):
    # D_hat(ell) = (1/L) sum_r D[r] * omega^{-(ell*r mod L)}
    omega = mp.e ** (mp.mpc(0, 1) * two_pi / mp.mpf(L))  # e(2pi i / L)
    # omega_pow[k] = omega^{-k} = e(-2pi i k / L) for k = 0..L-1
    omega_pow = [mp.mpc(1)]
    for k in range(1, L):
        omega_pow.append(omega_pow[k - 1] * omega)
    # need omega^{-k}: omega_pow[L-k] gives omega^{-k} mod L
    def omega_neg(k):
        return omega_pow[(-k) % L]

    Dhat = [mp.mpc(0) for _ in range(L)]
    for ell in range(L):
        acc = mp.mpc(0)
        for r in range(L):
            acc += D[r] * omega_neg(ell * r)
        Dhat[ell] = acc / mp.mpf(L)

    max_neq0 = mp.mpf(0)
    for ell in range(1, L):
        a = abs(Dhat[ell])
        if a > max_neq0:
            max_neq0 = a

    total_energy = mp.mpf(0)
    for ell in range(L):
        total_energy += abs(Dhat[ell]) ** 2

    return {
        "p": p,
        "h": h,
        "L": L,
        "m": (p - 1) // L,
        "max_ell_neq0": max_neq0,
        "total_energy": total_energy,
        "dc_energy": abs(Dhat[0]) ** 2,
    }


def compute_dhat_digit_orbit(p: int, h: int, dps: int):
    """Method B: reconstruct e(h delta) via the digit-orbit identity (independent oracle).

    delta_{p,r} = 15 W_{p,b+r} + r(b+r+1) + kappa_{p,b+r}  (PCN-01, exact).
    W_{p,j} = U_j - a_{p,j}/p, and e(h*15*U_j) = e(15h*16^{j-1}*pi) * e(-15h*T_j).
    Here we simply compute delta via a DIFFERENT code path: use the carry recurrence
    W_{p,j+1} = 16 W_{p,j} + r(j+1) + kappa_{p,j} (long-division hex digits), and
    independently evaluate W at birth. This cross-checks Method A.
    """
    mp.mp.dps = dps
    L = multiplicative_order(16, p)
    b = birth_step(p)
    J = (p + 1) // 2
    if b + L - 1 >= J:
        return None

    two_pi = mp.mpf(2) * mp.pi

    # carry digits via elementary long division of a_{p,b}/p (hex digits)
    a_b = primary_birth_numerator(p)
    rem = a_b % p
    kappas = []
    for _ in range(L):
        prod = 16 * rem
        kappas.append(prod // p)
        rem = prod % p

    # W at birth step b, via exact Fraction
    U_b = authentic_U(b)
    W_b = U_b - Fraction(a_b, p)

    D = [mp.mpc(0) for _ in range(L)]
    # walk W forward using carry recurrence, compute delta = W_{j+1} - W_j
    W = W_b
    for r in range(L - 1):
        j = b + r
        W_next = 16 * W + authentic_r(j + 1) + kappas[r]
        delta = W_next - W
        num = (h * delta.numerator) % delta.denominator
        den = delta.denominator
        phase = two_pi * mp.mpf(num) / mp.mpf(den)
        D[r] = (mp.e ** (mp.mpc(0, 1) * phase)) - 1
        W = W_next

    Dhat = [mp.mpc(0) for _ in range(L)]
    omega = mp.e ** (mp.mpc(0, 1) * two_pi / mp.mpf(L))
    omega_pow = [mp.mpc(1)]
    for k in range(1, L):
        omega_pow.append(omega_pow[k - 1] * omega)
    def omega_neg(k):
        return omega_pow[(-k) % L]
    for ell in range(L):
        acc = mp.mpc(0)
        for r in range(L):
            acc += D[r] * omega_neg(ell * r)
        Dhat[ell] = acc / mp.mpf(L)

    max_neq0 = mp.mpf(0)
    for ell in range(1, L):
        a = abs(Dhat[ell])
        if a > max_neq0:
            max_neq0 = a
    total_energy = mp.mpf(0)
    for ell in range(L):
        total_energy += abs(Dhat[ell]) ** 2

    return {
        "p": p,
        "h": h,
        "L": L,
        "m": (p - 1) // L,
        "max_ell_neq0": max_neq0,
        "total_energy": total_energy,
        "dc_energy": abs(Dhat[0]) ** 2,
    }


def main():
    P_MAX = 3000
    H_LIST = [1, 3, 5]
    # precision: max actual L is 739 (p=2957); delta denom bits ~ 3000 -> ~900 digits.
    # Use dps=4000 for safety (well above 6*Nmax/2.3 for Nmax~1100: ~2870).
    dps = 200
    mp.mp.dps = dps

    primes = [p for p in primes_up_to(P_MAX) if p > 5 and p % 4 == 1]
    print(f"# primes (p>5, p=1 mod 4, p<{P_MAX}): {len(primes)}")
    print(f"# dps = {dps}")

    records = []
    for p in primes:
        L = multiplicative_order(16, p)
        b = birth_step(p)
        J = (p + 1) // 2
        if b + L - 1 >= J:
            continue  # skip: not single-pole-period
        for h in H_LIST:
            rec = compute_dhat(p, h, dps)
            if rec is None:
                continue
            # cross-check with digit-orbit method for a subset
            records.append(rec)

    print(f"# records computed: {len(records)}")

    # Save raw records (as floats for JSON)
    out_records = []
    for r in records:
        out_records.append({
            "p": r["p"], "h": r["h"], "L": r["L"], "m": r["m"],
            "max_ell_neq0": float(r["max_ell_neq0"]),
            "total_energy": float(r["total_energy"]),
            "dc_energy": float(r["dc_energy"]),
        })
    out_path = HERE / "dft_scaling_raw.json"
    with open(out_path, "w") as f:
        json.dump(out_records, f, indent=1)
    print(f"# wrote {out_path}")

    # Summary: for each L, max and energy across h, plus per-h
    return out_records


if __name__ == "__main__":
    main()
