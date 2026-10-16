"""Source-typed finite cyclic quotient retraction, orthogonal projector, and Fourier gate.

Classical finite-dimensional algebra on Z/m -> Z/n (n|m), not a theorem about
all profinite points, adelic completion, completed Weil signs, or RH. Universal
proofs are in the paired research handoff; exact runtime checks are specimens.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


class QuotientRetractError(ValueError):
    """Invalid carrier, source or coefficient for a finite retraction."""


def _vector(values: Sequence[int | Q], width: int) -> tuple[Q, ...]:
    if not isinstance(values, (list, tuple)) or len(values) != width:
        raise QuotientRetractError("Vector must have the declared finite carrier width")
    if any(type(x) not in (int, Q) for x in values):
        raise QuotientRetractError("Only exact integer/Fraction amplitudes are admitted")
    return tuple(Q(x) for x in values)


def _dot(x: tuple[Q, ...], y: tuple[Q, ...]) -> Q:
    return sum((a * b for a, b in zip(x, y)), Q())


@dataclass(frozen=True)
class FiniteQuotientRetract:
    """The quotient Z/m -> Z/n with m=n*k, k>1 and declared source identity.

    U: Q^n -> Q^m is pullback; P=U*: Q^m -> Q^n sums fibers;
    A=P/k, A U=id; E=U A is the self-adjoint idempotent on Q^m.
    Inner products use counting measure, NOT normalized probability measure.
    """
    fine: int
    coarse: int
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        m, n = self.fine, self.coarse
        if (type(m) is not int or type(n) is not int or
                not 2 <= n < m <= 100 or m % n):
            raise QuotientRetractError("Require a proper finite quotient with 2<=n<m<=100 and n|m")
        if (type(self.source_id) is not str or not self.source_id.strip() or
                type(self.epoch) is not int or self.epoch < 0):
            raise QuotientRetractError("Declare a nonempty source ID and nonnegative integer epoch")

    @property
    def multiplicity(self) -> int:
        return self.fine // self.coarse

    def assert_source(self, source_id: str, epoch: int) -> None:
        if (source_id, epoch) != (self.source_id, self.epoch):
            raise QuotientRetractError("Original-source identity or epoch mismatch")

    def pullback(self, coarse_values: Sequence[int | Q]) -> tuple[Q, ...]:
        f = _vector(coarse_values, self.coarse)
        return tuple(f[x % self.coarse] for x in range(self.fine))

    def pushforward(self, fine_values: Sequence[int | Q]) -> tuple[Q, ...]:
        g = _vector(fine_values, self.fine)
        return tuple(sum((g[r + t * self.coarse] for t in range(self.multiplicity)), Q())
                     for r in range(self.coarse))

    def average(self, fine_values: Sequence[int | Q]) -> tuple[Q, ...]:
        return tuple(s / self.multiplicity for s in self.pushforward(fine_values))

    def project(self, fine_values: Sequence[int | Q]) -> tuple[Q, ...]:
        return self.pullback(self.average(fine_values))

    def dual_injection(self, frequency: int) -> int:
        """The PLUS-phase character pullback: a mod n -> k*a mod m."""
        if type(frequency) is not int:
            raise QuotientRetractError("Dual character label must be an integer")
        return (frequency % self.coarse) * self.multiplicity

    def exact_instance(self, fine_values: Sequence[int | Q]) -> dict:
        """Exact, bounded *instance* receipt. Not a universal proof by enumeration."""
        g = _vector(fine_values, self.fine)
        p = self.project(g)
        e = tuple(x - y for x, y in zip(g, p))
        a = self.average(g)
        if self.average(self.pullback(a)) != a or self.project(p) != p:
            raise AssertionError("Retract or idempotence failed")
        if self.average(e) != (Q(),) * self.coarse or _dot(p, e):
            raise AssertionError("Projection/residual orthogonality failed")
        if _dot(g, g) != _dot(p, p) + _dot(e, e):
            raise AssertionError("Pythagoras failed over the original finite source")
        return {
            "fine": self.fine, "coarse": self.coarse,
            "source_id": self.source_id, "epoch": self.epoch,
            "multiplicity": self.multiplicity,
            "projected": p, "residual": e,
            "projected_energy": _dot(p, p), "unseen_energy": _dot(e, e),
            "total_energy": _dot(g, g), "exact_finite_instance": True,
            "proves_universal_law_by_enumeration": False,
            "physical_source_authenticated": False, "RH_proved": False,
        }

    def fourier_instance(self, coarse_values: Sequence[int | Q]) -> dict:
        """Exact cyclotomic test of F_m(Uf), using SUCC's PLUS-phase DFT.

        Nonzero only at b=k*a, with value k*embed(F_n f)(a). Unlike
        pushforward Fourier restriction this is the *dual* pullback direction.
        """
        from .dynamic_fourier_tower import lift_character
        from .finite_fourier_carrier import CyclotomicElement, exact_dft

        f = _vector(coarse_values, self.coarse)
        small = exact_dft(f)
        large = exact_dft(self.pullback(f))
        zero = CyclotomicElement.scalar(self.fine, 0)
        for b, got in enumerate(large):
            expected = (lift_character(small[b // self.multiplicity], self.fine)
                        .scale(self.multiplicity) if b % self.multiplicity == 0 else zero)
            if got != expected:
                raise AssertionError("Fourier pullback square or normalization failed")
        return {
            "fine": self.fine, "coarse": self.coarse,
            "source_id": self.source_id, "epoch": self.epoch,
            "dual_injection": tuple(self.dual_injection(a) for a in range(self.coarse)),
            "positive_exponential_convention": True,
            "unnormalized_DFT_multiplies_by_fiber_size": self.multiplicity,
            "exact_finite_fourier_instance": True,
            "proves_global_adelic_theorem": False, "RH_proved": False,
        }
