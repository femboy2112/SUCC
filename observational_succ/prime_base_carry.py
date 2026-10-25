"""Exact finite inverse-circle covers and their shared prime-base carry.

For a root x in [0, 1), the label a modulo m represents (x+a)/m.
Multiplication by q transports it to the root {qx} and label
q*a + floor(q*x) modulo m.  One bounded integer carry serves every
compatible prime-power projection.  These are classical arithmetic
identities about labels; no selected-source law, independence, entropy,
pi-normality, or identification of different p-adic fields is asserted.

The full inverse-cover limit has an invertible multiplication by q when
the q-coordinate is retained.  A finite inverse must spend precision:
an image label modulo q*m determines a preimage label only modulo m.
If q is coprime to the available modulus, the missing q-coordinate leaves
q distinct preimages.  Both boundaries are explicit below.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"an integer >= {minimum} is required")
    return value


def _root(value: Q | int) -> Q:
    if type(value) not in (Q, int):
        raise ValueError("an exact Fraction or integer root is required")
    root = Q(value)
    if not 0 <= root < 1:
        raise ValueError("the canonical root must lie in [0, 1)")
    return root


@dataclass(frozen=True)
class CoverPoint:
    """A canonical root and one finite inverse-cover label.

    ``modulus`` is the cover degree, not a decimal or p-adic precision
    inferred from data.  Representatives are canonical rather than silently
    normalized, which keeps boundary and precision mistakes visible.
    """

    root: Q
    label: int
    modulus: int

    def __post_init__(self) -> None:
        root = _root(self.root)
        _integer(self.modulus, 1)
        _integer(self.label)
        if self.label >= self.modulus:
            raise ValueError("label must be in range(modulus)")
        object.__setattr__(self, "root", root)

    @property
    def circle_point(self) -> Q:
        """The represented inverse image, with no numerical approximation."""
        return (self.root + self.label) / self.modulus


def circle_carry(root: Q | int, multiplier: int) -> tuple[Q, int]:
    """Return ({q*x}, floor(q*x)); the carry is in 0,...,q-1."""
    x = _root(root)
    q = _integer(multiplier, 1)
    unwrapped = q*x
    carry = unwrapped.numerator // unwrapped.denominator
    return unwrapped-carry, carry


def transport_cover(point: CoverPoint, multiplier: int) -> CoverPoint:
    """Multiply the actual circle point and transport its cover label."""
    if not isinstance(point, CoverPoint):
        raise ValueError("a CoverPoint is required")
    root, carry = circle_carry(point.root, multiplier)
    label = (multiplier*point.label+carry) % point.modulus
    return CoverPoint(root, label, point.modulus)


def reduce_cover(point: CoverPoint, divisor: int) -> CoverPoint:
    """Project to a lower cover whose degree divides the current degree."""
    if not isinstance(point, CoverPoint):
        raise ValueError("a CoverPoint is required")
    modulus = _integer(divisor, 1)
    if point.modulus % modulus:
        raise ValueError("the lower cover degree must divide the current one")
    return CoverPoint(point.root, point.label % modulus, modulus)


def carry_cocycle(root: Q | int, q: int, r: int) -> tuple[int, int, int]:
    """Return direct, r-then-q, and q-then-r integer carries.

    Their equality is the exact composition identity
    floor(q*r*x)=q*floor(r*x)+floor(q*{r*x}), with the symmetric formula.
    This function retains the separate expressions for finite checking.
    """
    x = _root(root)
    _integer(q, 1)
    _integer(r, 1)
    r_root, r_carry = circle_carry(x, r)
    q_root, q_carry = circle_carry(x, q)
    direct = circle_carry(x, q*r)[1]
    r_then_q = q*r_carry+circle_carry(r_root, q)[1]
    q_then_r = r*q_carry+circle_carry(q_root, r)[1]
    return direct, r_then_q, q_then_r


def invert_with_q_coordinate(image: CoverPoint, multiplier: int) -> CoverPoint:
    """Invert using the available q-coordinate, spending one factor q.

    If the image label is known modulo q*m, its residue k modulo q fixes
    the root preimage (x'+k)/q.  The remaining label (a'-k)/q is known only
    modulo m.  Returning modulus q*m would invent unavailable precision.
    """
    if not isinstance(image, CoverPoint):
        raise ValueError("a CoverPoint is required")
    q = _integer(multiplier, 2)
    if image.modulus % q:
        raise ValueError("the image modulus must contain a full factor q")
    k = image.label % q
    return CoverPoint((image.root+k)/q, (image.label-k)//q,
                      image.modulus//q)


def inverse_candidates_without_q_coordinate(
    image: CoverPoint, multiplier: int,
) -> tuple[CoverPoint, ...]:
    """Return all q preimages when q is coprime to the available modulus.

    The finite non-q fibre can invert multiplication by q, but cannot choose
    which of the q circle roots was used.  No preferred candidate is selected.
    A partially present composite q-coordinate is outside this contract.
    """
    if not isinstance(image, CoverPoint):
        raise ValueError("a CoverPoint is required")
    q = _integer(multiplier, 2)
    if gcd(q, image.modulus) != 1:
        raise ValueError("q must be coprime to the available modulus")
    q_inverse = pow(q, -1, image.modulus)
    return tuple(CoverPoint((image.root+k)/q,
                            (q_inverse*(image.label-k)) % image.modulus,
                            image.modulus)
                 for k in range(q))
