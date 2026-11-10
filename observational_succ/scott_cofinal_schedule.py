"""Proof-backed affine schedules and honest finite-prefix diagnostics.

A subset of N_0 x N_0 is cofinal when every target is jointly dominated by
one member.  Separate unbounded coordinate images alone do NOT suffice for
an arbitrary sequence.  They suffice for a coordinatewise nondecreasing
sequence, because one can take the later of two witnessing indices.

This module decides cofinality only for its explicit nondecreasing affine
schedule family.  A finite prefix cannot certify an infinite extension.
Scott continuity concerns preservation of directed suprema; no equality of
the Scott topology on a product and the product of Scott topologies is used.
"""
from __future__ import annotations

from dataclasses import dataclass


def _natural(value: int, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")
    return value


@dataclass(frozen=True)
class AffineSchedule:
    """The infinite schedule k -> (n_start+n_step*k, L_start+L_step*k).

    Nonnegative slopes make both coordinates nondecreasing.  Positive
    slopes give an explicit simultaneous domination witness for every
    target.  This statement follows from the formula, not sampled values.
    """
    n_start: int = 0
    n_step: int = 1
    L_start: int = 0
    L_step: int = 1

    def __post_init__(self) -> None:
        for name in ("n_start", "n_step", "L_start", "L_step"):
            _natural(getattr(self, name), name)

    def at(self, k: int) -> tuple[int, int]:
        _natural(k, "k")
        return self.n_start + self.n_step*k, self.L_start + self.L_step*k

    def dominates_after(self, n_target: int, L_target: int) -> int:
        """Least k whose value dominates the target, or ValueError if none.

        Every later stage also dominates it, by nonnegative slopes.
        """
        _natural(n_target, "n_target")
        _natural(L_target, "L_target")
        thresholds = []
        for start, step, target in (
            (self.n_start, self.n_step, n_target),
            (self.L_start, self.L_step, L_target),
        ):
            gap = max(0, target-start)
            if not step and gap:
                raise ValueError("bounded coordinate cannot reach this target")
            thresholds.append((gap+step-1)//step if step else 0)
        return max(thresholds)

    def prefix(self, length: int) -> tuple[list[int], list[int]]:
        _natural(length, "length")
        pairs = [self.at(k) for k in range(length)]
        return [p[0] for p in pairs], [p[1] for p in pairs]


def is_cofinal_schedule(schedule: AffineSchedule, Ls=None) -> bool:
    """Decide the declared affine family, never an arbitrary finite prefix.

    The old two-list call was unsound and now raises TypeError.  Use
    ``prefix_diagnostics`` for observations with an UNVERIFIED truth state.
    """
    if Ls is not None or type(schedule) is not AffineSchedule:
        raise TypeError("infinite cofinality requires an AffineSchedule formula; "
                        "finite prefixes cannot certify it")
    return schedule.n_step > 0 and schedule.L_step > 0


def prefix_diagnostics(ns, Ls) -> dict:
    """Observed finite geometry only; arbitrary extensions may differ.

    Monotonicity of a finite prefix is neither evidence of unboundedness nor
    a necessary condition for an arbitrary sequence to be cofinal later.
    """
    ns, Ls = tuple(ns), tuple(Ls)
    if len(ns) != len(Ls):
        raise ValueError('equal lengths required')
    for n in ns:
        _natural(n, "n")
    for L in Ls:
        _natural(L, "L")
    return {
        'n_max': max(ns) if ns else None,
        'L_max': max(Ls) if Ls else None,
        'n_tends_up': all(a <= b for a,b in zip(ns, ns[1:])),
        'L_tends_up': all(a <= b for a,b in zip(Ls, Ls[1:])),
        'cofinal': None,
        'status': 'UNVERIFIED_FROM_FINITE_PREFIX',
    }


def cofinal_iff_unbounded_both(ns, Ls) -> dict:
    """Legacy finite-prefix wrapper; it does not decide the named theorem."""
    return prefix_diagnostics(ns, Ls)


SEAM_SCHEDULE = AffineSchedule(n_start=1, n_step=1, L_start=1, L_step=1)
FROZEN_HORIZON_SCHEDULE = AffineSchedule(n_start=1, n_step=1, L_start=2, L_step=0)


def seam_schedule(k: int):
    """Finite prefix of the declared cofinal (k+1,k+1) generator."""
    return SEAM_SCHEDULE.prefix(k)


def diagonal_schedule(k: int):
    """Historical name: prefix of the noncofinal (k+1,2) generator."""
    return FROZEN_HORIZON_SCHEDULE.prefix(k)


def verify_cofinality_theorem() -> dict:
    """Scoped formula checks; no infinite conclusion from prefix samples."""
    return {
        'seam_schedule_cofinal': is_cofinal_schedule(SEAM_SCHEDULE),
        'diagonal_schedule_L_bounded': FROZEN_HORIZON_SCHEDULE.L_step == 0,
        'diagonal_NOT_cofinal': not is_cofinal_schedule(FROZEN_HORIZON_SCHEDULE),
    }


if __name__ == '__main__':
    print(verify_cofinality_theorem())
