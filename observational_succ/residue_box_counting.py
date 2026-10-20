r"""Residue-constrained integer-box counting (Proof Forge III, Part IV).

The quantitative-ascent benchmark: translate a finite residue constraint modulo
``W`` into an integer-box count with an EXPLICIT, modulus-dependent error term,
and locate the exact regime where the error overwhelms the main term as the
modulus grows with ``X``.

Theorem (residue-box count).
    Let ``W >= 1`` be an integer, ``R`` a set of allowed residue pairs in
    ``(Z/WZ)^2``, and ``X >= 1`` an integer. With

        N_R(X) = #{ (a, b) in Z_{>0}^2 : a + b <= X, (a mod W, b mod W) in R },

    one has

        N_R(X) = (|R| / W^2) * (X^2 / 2) + E_R(X),      |E_R(X)| <= 5 |R| (X/W + 1).

    The local density is |R| / W^2; the main-term shape X^2/2 is the area of the
    simplex {a, b > 0, a + b <= X}; the absolute constant 5 is explicit.

Proof (lattice points -- see RESIDUE_BOX_COUNTING.md for the full write-up and an
independent floor-sum derivation). For each allowed pair ``(r, s)`` represent the
classes by ``t_r, t_s in {1, ..., W}`` (so residue 0 <-> representative W). Then
``a = t_r + W i``, ``b = t_s + W j`` with ``i, j >= 0`` automatically give
``a, b >= 1``, and ``a + b <= X`` becomes ``i + j <= Y`` with
``Y = (X - t_r - t_s)/W``. The number of nonnegative lattice points under a
triangle is ``(n+1)(n+2)/2`` with ``n = floor(Y)``; comparing to ``Y^2/2`` and
then to ``X^2/(2 W^2)`` costs at most ``5X/W + 4`` per pair, and summing over the
``|R|`` pairs gives the stated bound.

Growing modulus (the research frontier). The error ``5|R|(X/W + 1)`` is smaller
than the main term ``|R| X^2 / (2 W^2)`` iff ``X > 10 W``. So the asymptotic is
informative for ``W < X / 10`` and DEGENERATES at ``W asymptotic to X`` -- the
honest failure boundary with an explicit constant.

Everything here is exact (``int`` / ``fractions.Fraction``). A float is never a
certificate; the error bound is a proved rational inequality, not a fit.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Callable, Dict, FrozenSet, Iterable, List, Tuple

ResiduePair = Tuple[int, int]


class ResidueBoxError(ValueError):
    pass


# --------------------------------------------------------------------------- #
# Validation and representatives
# --------------------------------------------------------------------------- #
def _check(X: int, W: int, R: Iterable[ResiduePair]) -> FrozenSet[ResiduePair]:
    if not isinstance(W, int) or W < 1:
        raise ResidueBoxError(f"modulus W must be an integer >= 1, got {W!r}")
    if not isinstance(X, int):
        raise ResidueBoxError(f"X must be an integer (box bound), got {X!r}")
    Rset = frozenset(R)
    for (r, s) in Rset:
        if not (isinstance(r, int) and isinstance(s, int)):
            raise ResidueBoxError(f"residue pair {(r, s)!r} must be integers")
        if not (0 <= r < W and 0 <= s < W):
            raise ResidueBoxError(
                f"residue pair {(r, s)!r} not in (Z/{W}Z)^2 -- invalid residue class")
    return Rset


def _rep(r: int, W: int) -> int:
    """Representative of residue r in {1, ..., W} (class 0 -> W)."""
    return r if r != 0 else W


# --------------------------------------------------------------------------- #
# Three independent EXACT count routes (they must agree on every input)
# --------------------------------------------------------------------------- #
def residue_box_count(X: int, W: int, R: Iterable[ResiduePair]) -> int:
    """Closed-form exact count via the 2D lattice-point formula (the theorem's
    proof made executable). O(|R|)."""
    Rset = _check(X, W, R)
    total = 0
    for (r, s) in Rset:
        tr, ts = _rep(r, W), _rep(s, W)
        if X < tr + ts:
            continue
        n = (X - tr - ts) // W            # floor(Y), Y = (X - tr - ts)/W >= 0
        total += (n + 1) * (n + 2) // 2
    return total


def _count_in_window(M: int, s: int, W: int) -> int:
    """c_s(M) = #{1 <= b <= M : b mod W == s}, exact."""
    if M < 1:
        return 0
    ts = _rep(s, W)
    if M < ts:
        return 0
    return (M - ts) // W + 1


def residue_box_count_floorsum(X: int, W: int, R: Iterable[ResiduePair]) -> int:
    """Independent 1D floor-sum route: sum over a of the admissible-b counts.
    O(X * |rows|). A genuinely different computation from the 2D formula; both
    equal the brute-force count."""
    Rset = _check(X, W, R)
    rows: Dict[int, List[int]] = {}
    for (r, s) in Rset:
        rows.setdefault(r, []).append(s)
    total = 0
    for a in range(1, X):                 # need b >= 1 so a <= X - 1
        ss = rows.get(a % W)
        if not ss:
            continue
        M = X - a
        total += sum(_count_in_window(M, s, W) for s in ss)
    return total


def residue_box_count_bruteforce(X: int, W: int, R: Iterable[ResiduePair]) -> int:
    """Direct O(X^2) enumeration -- the ground-truth oracle for tests (small X)."""
    Rset = _check(X, W, R)
    total = 0
    for a in range(1, X):
        for b in range(1, X - a + 1):
            if (a % W, b % W) in Rset:
                total += 1
    return total


# --------------------------------------------------------------------------- #
# Main term, exact error, and the proved error bound
# --------------------------------------------------------------------------- #
def local_density(W: int, R: Iterable[ResiduePair]) -> Fraction:
    Rset = _check(1, W, R)
    return Fraction(len(Rset), W * W)


def main_term(X: int, W: int, R: Iterable[ResiduePair]) -> Fraction:
    """(|R| / W^2) * (X^2 / 2), exact."""
    Rset = _check(X, W, R)
    return Fraction(len(Rset) * X * X, 2 * W * W)


def error_exact(X: int, W: int, R: Iterable[ResiduePair]) -> Fraction:
    """Exact N_R(X) - main_term."""
    return residue_box_count(X, W, R) - main_term(X, W, R)


def error_bound(X: int, W: int, R: Iterable[ResiduePair]) -> Fraction:
    """The proved bound 5 |R| (X/W + 1), exact."""
    Rset = _check(X, W, R)
    return Fraction(5 * len(Rset) * (X + W), W)


@dataclass(frozen=True)
class ResidueBoxCertificate:
    X: int
    W: int
    cardinality_R: int
    count: int
    main_term: Fraction
    error_exact: Fraction
    error_bound: Fraction
    bound_holds: bool
    routes_agree: bool
    local_density: Fraction

    def as_record(self) -> dict:
        return {
            "X": self.X, "W": self.W, "|R|": self.cardinality_R,
            "count": self.count, "main_term": str(self.main_term),
            "error_exact": str(self.error_exact), "error_bound": str(self.error_bound),
            "bound_holds": self.bound_holds, "routes_agree": self.routes_agree,
            "local_density": str(self.local_density),
        }


def residue_box_certificate(X: int, W: int, R: Iterable[ResiduePair],
                            *, check_bruteforce: bool = True) -> ResidueBoxCertificate:
    """Build the exact certificate: all count routes agree, and the proved error
    bound holds. ``check_bruteforce`` is O(X^2) and should be left on only for
    small X."""
    Rset = _check(X, W, R)
    c2d = residue_box_count(X, W, Rset)
    cfs = residue_box_count_floorsum(X, W, Rset)
    routes = (c2d == cfs)
    if check_bruteforce:
        routes = routes and (c2d == residue_box_count_bruteforce(X, W, Rset))
    mt = main_term(X, W, Rset)
    err = c2d - mt
    bnd = error_bound(X, W, Rset)
    return ResidueBoxCertificate(
        X=X, W=W, cardinality_R=len(Rset), count=c2d, main_term=mt,
        error_exact=err, error_bound=bnd, bound_holds=abs(err) <= bnd,
        routes_agree=routes, local_density=Fraction(len(Rset), W * W))


# --------------------------------------------------------------------------- #
# Growing modulus W = W(X): the explicit failure boundary
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class GrowthRegime:
    W: int
    X: int
    main_term: Fraction
    error_bound: Fraction
    main_dominates: bool          # error_bound < main_term
    dominance_threshold_X: int    # smallest X making the main term certainly dominate

    def as_record(self) -> dict:
        return {
            "W": self.W, "X": self.X, "main_term": str(self.main_term),
            "error_bound": str(self.error_bound),
            "main_dominates": self.main_dominates,
            "dominance_threshold_X": self.dominance_threshold_X,
        }


def growth_regime(X: int, W: int, R: Iterable[ResiduePair]) -> GrowthRegime:
    """Compare the main term to the proved error bound. The main term dominates
    iff ``X > 10 W`` (independently of |R|, since both scale with |R|): with
    ``|R| X^2 / (2 W^2) > 5 |R| (X/W + 1)`` <=> ``X^2 > 10 W X + 10 W^2``, which
    holds once ``X > 10 W``. That inequality is the explicit degeneration
    boundary for a modulus growing with X."""
    Rset = _check(X, W, R)
    mt = main_term(X, W, Rset)
    bnd = error_bound(X, W, Rset)
    # smallest integer X0 with X0^2 - 10 W X0 - 10 W^2 > 0  (and |R| > 0)
    threshold = 10 * W + 1
    return GrowthRegime(W=W, X=X, main_term=mt, error_bound=bnd,
                        main_dominates=(bnd < mt) and len(Rset) > 0,
                        dominance_threshold_X=threshold)


# --------------------------------------------------------------------------- #
# Residue-set builders (genuine arithmetic constraints -> density)
# --------------------------------------------------------------------------- #
def residues_from_predicate(W: int,
                            pred: Callable[[int, int], bool]) -> FrozenSet[ResiduePair]:
    """All (r, s) in (Z/WZ)^2 satisfying a predicate -- the generic constraint
    builder. The downstream abc lane (Part V) uses this to encode genuine
    primitive a+b=c prime-power constraints."""
    if not isinstance(W, int) or W < 1:
        raise ResidueBoxError(f"modulus W must be an integer >= 1, got {W!r}")
    return frozenset((r, s) for r in range(W) for s in range(W) if pred(r, s))


def coprime_pair_residues(W: int) -> FrozenSet[ResiduePair]:
    """{(r, s) : gcd(r, W) = gcd(s, W) = 1}. A genuine arithmetic constraint whose
    density is (phi(W)/W)^2 -- the model case for 'a and b each prime to the
    modulus'. (Note: this is coprimality to W, not gcd(a,b)=1, which is not a
    single-modulus residue condition.)"""
    units = [r for r in range(W) if gcd(r, W) == 1]
    uset = set(units)
    return frozenset((r, s) for r in uset for s in uset)


def coprime_sum_residues(W: int) -> FrozenSet[ResiduePair]:
    """{(r, s) : gcd(r + s, W) = 1}: the primitive-sum constraint 'c = a + b is
    prime to the modulus'. Density = phi(W)/W (each r admits exactly phi(W)
    admissible s)."""
    return residues_from_predicate(W, lambda r, s: gcd((r + s) % W, W) == 1)
