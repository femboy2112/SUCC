"""SUCC/FUCC words: exact affine normal form and two-probe equality basis.

Word steps are applied LEFT-TO-RIGHT to x in N: ('S',t) sends x to x+t;
('V',p) sends x to p*x, where p must actually be prime. The affine pair
(a,b) means x -> a*x+b. The two-probe theorem is algebraic (0 and 1),
not a claim that two finite observations reveal an unknown physical source.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isqrt
from typing import Sequence


class AffinePresentationError(ValueError):
    pass


def _prime(p: int) -> bool:
    return (type(p) is int and p >= 2 and
            all(p % d for d in range(2, isqrt(p) + 1)))


def _steps(word: Sequence[tuple[str, int]]) -> tuple[tuple[str, int], ...]:
    if not isinstance(word, (list, tuple)):
        raise AffinePresentationError("Finite sequence of public SUCC/FUCC actions required")
    if len(word) > 128:
        raise AffinePresentationError("Finite proof word exceeds 128-step safety budget")
    out = tuple(word)
    for step in out:
        if type(step) is not tuple or len(step) != 2:
            raise AffinePresentationError("Each action must be a typed (kind,parameter) pair")
        kind, t = step
        if kind == "S" and type(t) is int and 0 <= t <= 1_000_000:
            continue
        if kind == "V" and type(t) is int and t <= 1_000_000 and _prime(t):
            continue
        raise AffinePresentationError("S needs a natural shift; V needs a genuine prime")
    return out


@dataclass(frozen=True)
class AffineMap:
    multiplier: int
    offset: int

    def __post_init__(self) -> None:
        if (type(self.multiplier) is not int or self.multiplier <= 0 or
                type(self.offset) is not int or self.offset < 0 or
                self.multiplier.bit_length() > 4096 or self.offset.bit_length() > 4096):
            raise AffinePresentationError("The original natural carrier needs bounded a>=1,b>=0")

    def evaluate(self, x: int) -> int:
        if type(x) is not int or x < 0:
            raise AffinePresentationError("Original input must belong to N")
        return self.multiplier * x + self.offset

    def compose_after(self, other: "AffineMap") -> "AffineMap":
        """Self after other: (a,b) o (c,d) = (ac,ad+b)."""
        if not isinstance(other, AffineMap):
            raise AffinePresentationError("Only composable affine endomorphisms")
        return AffineMap(self.multiplier * other.multiplier,
                         self.multiplier * other.offset + self.offset)


def normalize_word(word: Sequence[tuple[str, int]]) -> AffineMap:
    """Compute the exact map on all N by structural fold, not finite sampling."""
    a, b = 1, 0
    for kind, t in _steps(word):
        if kind == "S":
            b += t
        else:
            a, b = t*a, t*b
        if a.bit_length() > 4096 or b.bit_length() > 4096:
            raise AffinePresentationError("Finite affine normal form exceeds bit budget")
    return AffineMap(a, b)


def evaluate_direct(word: Sequence[tuple[str, int]], x: int) -> int:
    if type(x) is not int or x < 0:
        raise AffinePresentationError("Original input must belong to N")
    for kind, t in _steps(word):
        x = x + t if kind == "S" else t * x
        if x.bit_length() > 4096:
            raise AffinePresentationError("Direct finite source witness exceeds bit budget")
    return x


def two_probe_certificate(
    first: Sequence[tuple[str, int]], second: Sequence[tuple[str, int]],
    modulus: int, *, source_id: str, epoch: int
) -> dict:
    """For affine maps mod n, equality at 0,1 iff equality everywhere.

    Mathematically proven from f(0)=b and f(1)-f(0)=a modulo n.
    Runtime receipt checks the declared exact normal forms and witnesses.
    """
    if type(modulus) is not int or not 2 <= modulus <= 1000000:
        raise AffinePresentationError("Finite nontrivial residue source 2<=n<=1e6 required")
    if (type(source_id) is not str or not source_id.strip() or
            type(epoch) is not int or epoch < 0):
        raise AffinePresentationError("Declare a source and epoch")
    f, g = normalize_word(first), normalize_word(second)
    eq0 = (f.offset - g.offset) % modulus == 0
    eq1 = ((f.multiplier + f.offset) - (g.multiplier + g.offset)) % modulus == 0
    equal = eq0 and eq1
    pair_eq = ((f.multiplier - g.multiplier) % modulus == 0 and
               (f.offset - g.offset) % modulus == 0)
    if equal != pair_eq:
        raise AssertionError("Two-probe affine generator theorem violated")
    witness = None if equal else 0 if not eq0 else 1
    if witness is not None and f.evaluate(witness) % modulus == g.evaluate(witness) % modulus:
        raise AssertionError("Claimed separating finite source witness is invalid")
    return {
        "source_id": source_id, "epoch": epoch, "modulus": modulus,
        "normal_form_first": (f.multiplier, f.offset),
        "normal_form_second": (g.multiplier, g.offset),
        "equal_as_source_N_maps": f == g,
        "equal_on_entire_finite_affine_carrier": equal,
        "separating_probe": witness,
        "structural_affine_proof_not_exhaustive_search": True,
        "physical_source_authenticated": False, "RH_proved": False,
    }
