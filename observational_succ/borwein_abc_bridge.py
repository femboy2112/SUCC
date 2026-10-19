"""Two-view interface: real p-adic ABC contact vs chosen Borwein smoothing.

Neither view is a substitute for the other. The exact hard gate reads
genuine prime-power residue of a+b; the soft view uses an explicitly
chosen uniform-jump model with widths 1/p^k and circular distance.
Independent pointwise order fails in BOTH directions, with exact examples.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, prod

from .borwein_abc_contacts import ContactError, prime_power
from .borwein_prime_clock import borwein_window_mass

MAX_BRIDGE_CLOCKS = 11
MAX_BRIDGE_PRODUCT = 10**12


@dataclass(frozen=True)
class BorweinABCContact:
    a: int
    b: int
    c: int
    source_prime_powers: tuple[tuple[int,int],...]
    modulus: int
    actual_residues: tuple[int,...]
    hard_all_locked: bool
    smoothed_mass: Q
    scale: Q
    archimedean_forbidden: bool


def borwein_abc_contact(a: int, b: int,
                        prime_depths: tuple[tuple[int,int],...],
                        scale: Q = Q(1)) -> BorweinABCContact:
    """Return separate authenticated and modeled readouts, without inference."""
    if (type(a) is not int or type(b) is not int or
            not 1 <= a <= MAX_BRIDGE_PRODUCT//2 or
            not 1 <= b <= MAX_BRIDGE_PRODUCT//2 or gcd(a,b)!=1):
        raise ContactError("positive primitive a,b in finite source budget required")
    if (type(prime_depths) is not tuple or
            not 1 <= len(prime_depths) <= MAX_BRIDGE_CLOCKS or
            any(type(x) is not tuple or len(x)!=2 for x in prime_depths)):
        raise ContactError("nonempty typed prime-power tuple required")
    if type(scale) is not Q or scale < 0:
        raise ContactError("nonnegative rational smoothing scale required")
    moduli = tuple(prime_power(p,e) for p,e in prime_depths)
    if (tuple(sorted(set(p for p,e in prime_depths))) !=
            tuple(p for p,e in prime_depths)):
        raise ContactError("distinct ascending genuine prime places required")
    modulus = prod(moduli)
    if modulus > MAX_BRIDGE_PRODUCT:
        raise ContactError("CRT product exceeds budget")
    c = a+b
    residues = tuple(c%m for m in moduli)
    widths = tuple(Q(1,m) for m in moduli)
    signed_distance = sum((Q(min(r,m-r),m)
                           for r,m in zip(residues,moduli)), Q())
    soft = borwein_window_mass(widths, scale*signed_distance)
    hard = all(r == 0 for r in residues)
    if hard != (c%modulus==0):
        raise AssertionError("actual source CRT contact mismatch")
    if modulus>c and hard:
        raise AssertionError("Archimedean impossible prime power survived")
    return BorweinABCContact(a,b,c,prime_depths,modulus,residues,
                             hard,soft,scale,modulus>c)
