"""Prime-clock-to-hologram transport calculus: exact composition / naturality.

Built on :mod:`observational_succ.factorial_borwein_hologram`.  On PRECISELY
declared domains the factorial Borwein embedding ``I_N`` and the source-recovering
integer sampler ``R_N`` satisfy

    R_N I_N = id            (ONLY on the range of I_N),
    T_{M<-N} = I_M R_N      (an operator  ran(I_N) -> ran(I_M)),

and the composition / naturality law

    T_{L<-M} o T_{M<-N} = T_{L<-N}       on ran(I_N).

Authentic integer residue projectors ``P_{p,r}`` (reusing the genuine-prime
oracles of :mod:`observational_succ.rad_ris_transport` and
:mod:`observational_succ.prime_phase_clocks`) and the SUCC shift ``S : n -> n+1``
are transported through these maps.  With the correct phase orientation the
shift intertwines the projectors,

    S P_{p,r} = P_{p,(r+1) mod p} S                      (covariance),

and this intertwining is natural: it commutes with every transport ``T_{M<-N}``.

STATUS (per AGENTS.md): PROVED LOCAL + TESTED MODEL.  All objects are exact
``Fraction`` / finitely supported coefficient vectors.  No floats are used as
certificates and no randomness enters.

FIREWALL (load-bearing):
  * ``R_N I_N = id`` holds ONLY on ran(I_N).  Point evaluation / ``R_N`` is
    REFUSED on an abstract L^2 equivalence class -- it is NEVER globalized to
    bounded point sampling of arbitrary L^2 functions.
  * The three "factorials" stay DISTINCT: Borwein simplex volume (1/m! in the
    uniform-sum CDF), Poisson jump-time (1/k! in the SUCC clock series), and the
    arithmetic Legendre occupation v_p(N!).  This module touches only the last
    (through window structure) and the cardinal lift; it introduces no new
    normalization that conflates them.
  * No RH / Weil / Suzuki-Schur object is constructed or asserted here.  A
    nonnegative probability kernel with a coercive translate Gram is NOT a
    positive signed Weil form.  RH PROVED: NO.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction as F

from .factorial_borwein_hologram import (
    MAX_FACTORIAL_HORIZON,
    interpolant,
    source_clock_gate,
)
from .rad_ris_transport import is_prime
from .prime_phase_clocks import prime as phase_prime


class HologramTransportError(ValueError):
    """Out-of-domain input, malformed coefficient source, or firewall breach."""


# ---------------------------------------------------------------------------
# Exact coefficient vectors in ell^2(Z): canonical, finitely supported.
# ---------------------------------------------------------------------------

Coeffs = tuple  # alias for documentation: tuple[tuple[int, F], ...]


def _canon(coeffs) -> tuple[tuple[int, F], ...]:
    """Canonicalize a finitely supported ell^2(Z) vector (EXACT).

    Accepts a mapping ``{site: Fraction}`` or a sequence of ``(site, Fraction)``
    pairs.  Validates plain-int sites (``bool`` rejected) and exact ``Fraction``
    values, rejects duplicate sites, drops exact zeros, and sorts by site.
    """
    if isinstance(coeffs, Mapping):
        pairs = list(coeffs.items())
    elif isinstance(coeffs, (tuple, list)):
        pairs = list(coeffs)
    else:
        raise HologramTransportError(
            "coefficients must be a mapping or sequence of (int site, Fraction) pairs")
    seen: set[int] = set()
    out: list[tuple[int, F]] = []
    for pair in pairs:
        if not (isinstance(pair, tuple) and len(pair) == 2):
            raise HologramTransportError(
                "each coefficient must be a 2-tuple (int site, Fraction value)")
        m, v = pair
        if type(m) is not int:
            raise HologramTransportError("coefficient sites must be plain integers (bool rejected)")
        if type(v) is not F:
            raise HologramTransportError("coefficient values must be exact Fractions")
        if m in seen:
            raise HologramTransportError("coefficient sites must be unique")
        seen.add(m)
        if v != 0:
            out.append((m, v))
    out.sort()
    return tuple(out)


def _horizon(n: int, label: str = "horizon N") -> int:
    if type(n) is not int or not 1 <= n <= MAX_FACTORIAL_HORIZON:
        raise HologramTransportError(f"{label} must be an integer in 1..{MAX_FACTORIAL_HORIZON}")
    return n


# ---------------------------------------------------------------------------
# Exact carriers of the two domains: ran(I_N) and the abstract-L^2 complement.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RangeFunction:
    """An exact representative of an element of ``ran(I_N) subset L^2(R)``.

    ``I_N`` is injective on finitely supported sequences (FBH-02), so the pair
    ``(horizon=N, coeffs=c)`` faithfully names the function ``(I_N c)(x) =
    sum_m c_m B_N(x - m)``.  Equality is STRUCTURAL over ``(horizon, coeffs)``:
    two range functions are equal iff they are the same element of the same
    range, which is exactly what the composition law needs to be meaningful
    (the horizon label is load-bearing -- the off-lattice shape depends on N).
    """

    horizon: int
    coeffs: tuple[tuple[int, F], ...]

    def __post_init__(self) -> None:
        _horizon(self.horizon)
        if _canon(self.coeffs) != self.coeffs:
            raise HologramTransportError("coeffs must already be canonical; build via lift()")

    def evaluate(self, x: F) -> F:
        """Exact pointwise value ``(I_N c)(x)`` at a rational ``x`` (EXACT)."""
        return interpolant(self.horizon, self.coeffs, x)


@dataclass(frozen=True)
class AbstractL2:
    """An arbitrary L^2(R) equivalence class with NO defined integer sampling.

    Models the firewall boundary: point evaluation is not a bounded functional
    on L^2, so ``R_N`` (integer sampling) is UNDEFINED here.  Passing one of
    these to :func:`sample` or :func:`transport` is REFUSED on purpose.
    """

    label: str = "abstract-L2-equivalence-class"


# ---------------------------------------------------------------------------
# The three maps:  I_N (lift),  R_N (sample),  T_{M<-N} (transport).
# ---------------------------------------------------------------------------

def lift(N: int, c) -> RangeFunction:
    """``I_N`` : finitely supported ``c`` in ell^2(Z)  ->  ``I_N c`` in ran(I_N).

    PROVED LOCAL (FBH-01/02): ``I_N`` is a bounded injective cardinal lift with
    ``(1 - S_N)||c||^2 <= ||I_N c||^2 <= ||c||^2`` and ``1 - S_N > 1/12``.
    """
    return RangeFunction(_horizon(N), _canon(c))


def sample(N: int, f_on_range: RangeFunction) -> tuple[tuple[int, F], ...]:
    """``R_N`` : ran(I_N)  ->  ell^2(Z), by exact integer-lattice sampling.

    DOMAIN (firewall): ``R_N`` is defined ONLY on ``ran(I_N)``.  The argument
    must be a :class:`RangeFunction` whose ``horizon`` equals ``N``.  An
    :class:`AbstractL2` class, a bare coefficient tuple, or a range function of
    a different horizon is REFUSED -- ``R_N I_N = id`` is never globalized.

    The recovery is a GENUINE computation through the kernel: every integer
    sample ``(I_N c)(m) = sum_j c_j B_N(m-j) = c_m`` is recomputed via
    ``interpolant`` (because ``B_N(integer) = delta``), and the result is
    asserted to reproduce the stored coefficients -- i.e. this function is the
    exact witness of ``R_N I_N = id`` on the range.
    """
    _horizon(N, "sampling horizon N")
    if isinstance(f_on_range, AbstractL2):
        raise HologramTransportError(
            "R_N refuses point evaluation on an abstract L^2 class; "
            "R_N I_N = id holds ONLY on ran(I_N), never on arbitrary L^2 classes")
    if not isinstance(f_on_range, RangeFunction):
        raise HologramTransportError("R_N domain is ran(I_N): pass a RangeFunction")
    if f_on_range.horizon != N:
        raise HologramTransportError(
            f"R_{N} is defined on ran(I_{N}); got a function in "
            f"ran(I_{f_on_range.horizon}) -- out of domain")
    if not f_on_range.coeffs:
        return ()
    sites = [m for m, _ in f_on_range.coeffs]
    lo, hi = min(sites) - 1, max(sites) + 1
    recovered = _canon(tuple((m, f_on_range.evaluate(F(m))) for m in range(lo, hi + 1)))
    if recovered != f_on_range.coeffs:
        raise AssertionError("R_N I_N = id failed: integer samples did not recover the source")
    return recovered


def transport(M: int, N: int, thing) -> RangeFunction:
    """``T_{M<-N} = I_M R_N`` : ran(I_N)  ->  ran(I_M).

    ``thing`` may be an element of ran(I_N) (a :class:`RangeFunction` with
    ``horizon == N``) or a bare coefficient source ``c`` (interpreted as the
    point ``I_N c`` of ran(I_N)).  The step ``R_N`` enforces membership in
    ran(I_N); the step ``I_M`` re-homes the SAME arithmetic source coefficients
    onto the horizon-M off-lattice geometry.

    PROVED LOCAL: the integer samples (the arithmetic source) are preserved;
    the off-lattice analytic representation changes with the horizon.
    """
    if isinstance(thing, AbstractL2):
        raise HologramTransportError("T_{M<-N} is undefined on abstract L^2 classes")
    source = thing if isinstance(thing, RangeFunction) else lift(N, thing)
    c = sample(N, source)          # R_N  (refuses anything outside ran(I_N))
    return lift(M, c)              # I_M


# ---------------------------------------------------------------------------
# SUCC shift and authentic integer residue projectors on ell^2(Z).
# ---------------------------------------------------------------------------

def succ_shift(c) -> tuple[tuple[int, F], ...]:
    """SUCC shift ``S`` with the declared orientation n -> n+1.

    ``(S c)(m) = c(m-1)``: mass at site ``s`` moves to ``s+1``.  EXACT.
    """
    return _canon(tuple((m + 1, v) for m, v in _canon(c)))


def residue_projector(c, p: int, r: int) -> tuple[tuple[int, F], ...]:
    """Authentic integer residue projector ``P_{p,r}`` onto class r mod p.

    The modulus ``p`` must be a GENUINE prime -- authenticated by BOTH
    ``rad_ris_transport.is_prime`` and ``prime_phase_clocks.prime`` (the same
    authentic q-clock source used elsewhere in SUCC).  ``(P_{p,r} c)(m) = c(m)``
    when ``m % p == r`` (Python's non-negative remainder matches
    ``source_clock_gate``'s ``site % p``), else 0.  EXACT.
    """
    if not (is_prime(p) and phase_prime(p)):
        raise HologramTransportError("residue modulus must be an authenticated prime")
    if type(r) is not int or not 0 <= r < p:
        raise HologramTransportError("residue class r must be an integer in 0..p-1")
    return _canon(tuple((m, v) for m, v in _canon(c) if m % p == r))


def residue_projector_matches_clock_gate(c, p: int, kind: str) -> bool:
    """Confirm ``residue_projector`` agrees with the authentic q-clock gate.

    Reuses ``factorial_borwein_hologram.source_clock_gate`` on the SAME integer
    sites.  ``kind`` 'one' <-> r=1, 'minus_one' <-> r=p-1, 'nonzero' <-> the
    union of all residues != 0.  Returns True iff the two selections coincide.
    """
    cc = _canon(c)
    if kind == "one":
        projected = residue_projector(cc, p, 1)
    elif kind == "minus_one":
        projected = residue_projector(cc, p, p - 1)
    elif kind == "nonzero":
        projected = _canon(tuple((m, v) for m, v in cc if m % p != 0))
    else:
        raise HologramTransportError("kind must be one, minus_one, or nonzero")
    gated = _canon(tuple((m, v) for m, v in cc if source_clock_gate(m, p, kind)))
    return projected == gated


# ---------------------------------------------------------------------------
# Lifted operators on ran(I_N) and the naturality / covariance theorem.
# ---------------------------------------------------------------------------

def lifted_succ(N: int, f: RangeFunction) -> RangeFunction:
    """``I_N S R_N`` : the SUCC shift lifted to ran(I_N)."""
    return lift(N, succ_shift(sample(N, f)))


def lifted_residue(N: int, f: RangeFunction, p: int, r: int) -> RangeFunction:
    """``I_N P_{p,r} R_N`` : the authentic residue projector lifted to ran(I_N)."""
    return lift(N, residue_projector(sample(N, f), p, r))


def residue_projector_covariance(p: int, r: int, coeffs, N: int, M: int) -> dict:
    """Prove (exactly) the covariance of residue projectors under n -> n+1 and
    its naturality through the transport ``T_{M<-N}``.

    Verified identities (each raises on failure):
      (A) SUCC covariance on ell^2(Z):   S P_{p,r} = P_{p,(r+1) mod p} S.
      (B) shift naturality:    T_{M<-N} (I_N S R_N)   = (I_M S R_M) T_{M<-N}.
      (C) projector naturality:T_{M<-N} (I_N P R_N)   = (I_M P R_M) T_{M<-N}.
      (D) transported intertwining: in ran(I_M),  (I_M S R_M)(I_M P_r R_M)
                                     = (I_M P_{r+1} R_M)(I_M S R_M).
    Reported negative control (NOT raised):
      (E) wrong phase orientation r-1 breaks (A) for p >= 3 whenever the source
          meets class r -- i.e. the +1 orientation is load-bearing.

    STATUS: PROVED LOCAL + TESTED MODEL, EXACT.
    """
    c = _canon(coeffs)
    r_next = (r + 1) % p

    # (A) covariance on ell^2(Z)
    lhs = succ_shift(residue_projector(c, p, r))
    rhs = residue_projector(succ_shift(c), p, r_next)
    if lhs != rhs:
        raise AssertionError("SUCC covariance S P_{p,r} = P_{p,r+1} S failed")

    # (B) shift naturality through transport
    f = lift(N, c)
    if transport(M, N, lifted_succ(N, f)) != lifted_succ(M, transport(M, N, f)):
        raise AssertionError("shift naturality through transport T_{M<-N} failed")

    # (C) projector naturality through transport
    if transport(M, N, lifted_residue(N, f, p, r)) != \
            lifted_residue(M, transport(M, N, f), p, r):
        raise AssertionError("residue-projector naturality through transport failed")

    # (D) transported intertwining inside ran(I_M)
    g = transport(M, N, f)
    d_left = lifted_succ(M, lifted_residue(M, g, p, r))
    d_right = lifted_residue(M, lifted_succ(M, g), p, r_next)
    if d_left != d_right:
        raise AssertionError("transported intertwining S P_r = P_{r+1} S failed")

    # (E) negative control: wrong orientation
    wrong = residue_projector(succ_shift(c), p, (r - 1) % p)
    return {
        "covariance_holds": True,
        "shift_natural": True,
        "projector_natural": True,
        "intertwining_transported": True,
        "wrong_orientation_differs": lhs != wrong,
        "source_class_r": r,
        "image_class": r_next,
        "image_coeffs": lhs,
    }


# ---------------------------------------------------------------------------
# Self-certifying verifiers (the exact assertions the deliverable requires).
# ---------------------------------------------------------------------------

def verify_range_retraction(N: int, coeffs) -> tuple[tuple[int, F], ...]:
    """Assert ``R_N I_N = id`` on the range for an explicit source (EXACT)."""
    c = _canon(coeffs)
    recovered = sample(N, lift(N, c))
    if recovered != c:
        raise AssertionError("R_N I_N = id failed on range")
    return recovered


def verify_composition_law(L: int, M: int, N: int, coeffs) -> RangeFunction:
    """Assert ``T_{L<-M} o T_{M<-N} = T_{L<-N}`` on an explicit source (EXACT).

    Also asserts both sides equal ``I_L c``: the arithmetic source coefficients
    are transported invariantly, only the horizon-L geometry is installed.
    """
    c = _canon(coeffs)
    left = transport(L, M, transport(M, N, c))
    right = transport(L, N, c)
    if left != right:
        raise AssertionError("composition law T_{L<-M} T_{M<-N} = T_{L<-N} failed")
    if left != lift(L, c):
        raise AssertionError("transport did not preserve the arithmetic source coeffs")
    return left


# ---------------------------------------------------------------------------
# Required nonrecoverability counterexample.
# ---------------------------------------------------------------------------

def nonrecoverability_witness() -> dict:
    """Two DISTINCT continuous off-lattice functions with IDENTICAL integer
    samples -- integer sampling alone cannot recover the off-lattice label.

    Take the single arithmetic source ``c = delta_0``.  Then ``f = I_4 c = B_4``
    and ``g = I_6 c = B_6`` are both continuous (N >= 4), lie in L^2(R), and have
    IDENTICAL integer samples (delta_0).  They are DISTINCT: at the off-lattice
    point 3/10 they disagree exactly (B_4 = 1 on its wider plateau, B_6 < 1).
    The off-lattice point 1/10 lies in BOTH plateaus, so it is a flat collision
    (equal there) -- no single off-lattice probe is guaranteed to separate them
    either.  This is the exact firewall witness: ``R_N`` recovers the source
    COEFFICIENTS, not the off-lattice function.

    STATUS: PROVED LOCAL + TESTED MODEL, EXACT.
    """
    c = ((0, F(1)),)
    f = lift(4, c)
    g = lift(6, c)

    samples_f = {m: f.evaluate(F(m)) for m in range(-3, 4)}
    samples_g = {m: g.evaluate(F(m)) for m in range(-3, 4)}
    if samples_f != samples_g:
        raise AssertionError("witness integer samples disagree -- not a sample collision")
    if sample(4, f) != sample(6, g):
        raise AssertionError("R-recovered sources disagree -- not a sample collision")

    collision_point = F(1, 10)
    separating_point = F(3, 10)
    f_flat, g_flat = f.evaluate(collision_point), g.evaluate(collision_point)
    f_sep, g_sep = f.evaluate(separating_point), g.evaluate(separating_point)
    if f_flat != g_flat:
        raise AssertionError("1/10 was expected to be a flat collision point")
    if f_sep == g_sep or f == g:
        raise AssertionError("witness functions are not distinct off-lattice")

    return {
        "source": c,
        "f": f,                       # B_4
        "g": g,                       # B_6
        "equal_integer_samples": samples_f,     # {-3:0,...,0:1,...,3:0}
        "flat_collision_point": collision_point,
        "flat_value_f": f_flat, "flat_value_g": g_flat,   # both 1
        "separating_point": separating_point,
        "value_f_at_separating": f_sep,         # 1
        "value_g_at_separating": g_sep,         # 30922061/31104000
        "functions_distinct": f != g,
    }


# ---------------------------------------------------------------------------
# Import-time-free demonstration (run as a script).
# ---------------------------------------------------------------------------

def _demo() -> None:  # pragma: no cover - manual probe
    src = ((-2, F(3, 5)), (0, F(1)), (1, F(-7, 4)), (5, F(2)))
    print("R_N I_N = id :", verify_range_retraction(6, src))
    cl = verify_composition_law(10, 6, 4, src)
    print("composition  : T_{10<-6} T_{6<-4} = T_{10<-4} =", cl)
    cov = residue_projector_covariance(3, 1, ((0, F(1)), (1, F(2)), (3, F(5)), (4, F(7))), 4, 6)
    print("covariance   :", cov)
    w = nonrecoverability_witness()
    print("nonrecover.  : B_4(3/10)=", w["value_f_at_separating"],
          " B_6(3/10)=", w["value_g_at_separating"],
          " equal samples=", w["equal_integer_samples"])


if __name__ == "__main__":  # pragma: no cover
    _demo()
