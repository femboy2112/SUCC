"""Exact radix-16/2-adic/3-adic/5-adic digit seams and Collatz calibration.

All assertions are elementary arithmetic in *declared* source-independent
radix models.  Original four-pole BBP is used only in bbp_prefix, with the
literal zero seed.  No general Collatz or pi-normality claim.
"""
from __future__ import annotations
from fractions import Fraction

BASE = 16


def journal(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("n >= 0 required")
    return (BASE ** n - 1) // (BASE - 1)


def repeated_digit(d: int, n: int) -> int:
    if type(d) is not int or not 0 <= d <= 15:
        raise ValueError("hex digit 0..15 required")
    return d * journal(n)


def valuation(n: int, p: int) -> int:
    if type(n) is not int or n == 0 or type(p) is not int or p < 2:
        raise ValueError("nonzero integer and prime p required")
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def mirror_register(reg: int, length: int) -> int:
    if type(reg) is not int or type(length) is not int or length < 0 or not 0 <= reg < 16 ** length:
        raise ValueError("invalid finite register")
    return 16 ** length - 1 - reg


def digit_step(reg: int, digit: int) -> int:
    if type(reg) is not int or reg < 0 or type(digit) is not int or not 0 <= digit < 16:
        raise ValueError("invalid register/digit")
    return 16 * reg + digit


def two_adic_reversal(digits: tuple[int, ...] | list[int]) -> int:
    """First N recorded digit labels, earliest digit least 2-adic significant."""
    if any(type(d) is not int or not 0 <= d < 16 for d in digits):
        raise ValueError("invalid digit")
    return sum(d * 16**j for j, d in enumerate(digits))


def real_fractional_prefix(digits: tuple[int, ...] | list[int]) -> Fraction:
    if any(type(d) is not int or not 0 <= d < 16 for d in digits):
        raise ValueError("invalid digit")
    return sum((Fraction(d, 16**(j+1)) for j, d in enumerate(digits)), Fraction(0))


def readout_235(previous_mod15: int, current_mod3: int, current_mod5: int, current_parity: int) -> int:
    """Recover one new digit from independently calibrated 3-, 5-, 2-heads."""
    if (type(previous_mod15) is not int or not 0 <= previous_mod15 < 15
        or type(current_mod3) is not int or not 0 <= current_mod3 < 3
        or type(current_mod5) is not int or not 0 <= current_mod5 < 5
        or type(current_parity) is not int or current_parity not in (0, 1)):
        raise ValueError("bad head readings")
    candidates = [d for d in range(16)
                  if (previous_mod15 + d) % 3 == current_mod3
                  and (previous_mod15 + d) % 5 == current_mod5
                  and d % 2 == current_parity]
    if len(candidates) != 1:
        raise AssertionError("unexpected non-unique joint CRT digit")
    return candidates[0]


def collatz_shortcut(n: int) -> int:
    if type(n) is not int or n <= 0:
        raise ValueError("positive integer required")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def collatz_odd_accelerated(n: int) -> int:
    if type(n) is not int or n <= 0 or n % 2 == 0:
        raise ValueError("positive odd integer required")
    num = 3 * n + 1
    return num // (2 ** valuation(num, 2))


def five_suffix_decompose(number: int, k: int) -> tuple[int, bool]:
    if type(number) is not int or number < 0 or type(k) is not int or k <= 0:
        raise ValueError("nonnegative number and k>=1 required")
    radix = 16**k
    high, low = divmod(number, radix)
    return high, low == repeated_digit(5, k)


def bbp_forcing(n: int) -> Fraction:
    """The original four signed BBP poles, *not* a replacement 3x+1 source."""
    if type(n) is not int or n < 1:
        raise ValueError("n>=1 required")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_prefix(n: int, depth: int | None = None) -> tuple[int, ...]:
    """Certified digits of x=pi/16 using exact rational four-pole tail bound.

    Only tests correctness relative to standard classical BBP identity.
    """
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 required")
    if depth is None:
        depth = n + 2
    if type(depth) is not int or depth < n:
        raise ValueError("depth must be >= n")
    p = sum((bbp_forcing(j) / 16**j for j in range(1, depth+1)), Fraction(0))
    tail = bbp_forcing(depth+1) / (15 * 16**depth)
    a = (p * 16**n).__floor__()
    b = ((p + tail) * 16**n).__floor__()
    if a != b:
        raise ArithmeticError("insufficient certified precision")
    return tuple((a // 16**(n-1-j)) % 16 for j in range(n))


def two_adic_digit_shift(y: int) -> tuple[int, int]:
    """Finite exact truncation of 2-adic digit-left shift, low nibble first."""
    if type(y) is not int or y < 0:
        raise ValueError("nonnegative finite register")
    return y % 16, y // 16


def two_adic_word(y: int, start: int, length: int) -> int:
    """Read a length-digit chronological word from 2-adic prefix memory."""
    if any(type(v) is not int or v < 0 for v in (y,start,length)):
        raise ValueError("nonnegative integer arguments")
    return (y//(16**start)) % (16**length)


def defect_first_mismatch(digits: tuple[int, ...] | list[int], q: int) -> int | None:
    """v2(q*y+1) from first departure from repeated d=15/q in 2-adic digits.

    Returns None if the supplied prefix agrees entirely: a later digit is
    necessary to determine finite valuation.  q in {3,5,15}.
    """
    if q not in (3,5,15) or any(type(j) is not int or not 0 <= j < 16 for j in digits):
        raise ValueError("q in (3,5,15) and valid digits required")
    d=15//q
    for k,j in enumerate(digits):
        if j != d:
            return 4*k+valuation(j-d,2)
    return None
