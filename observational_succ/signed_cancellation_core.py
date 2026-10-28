"""Shared signed-cancellation primitive layer for the pi-normality program.

This module is the single auditable home for the objects that ~34 research
branches (#306..#340) previously re-derived independently. It consolidates,
with one typed exact-rational implementation each:

  1. the authentic four-pole BBP recurrence and its real-circle orbit;
  2. the exact rational Weyl sum S_N(h) = sum_{n<=N} e(h U_n);
  3. the PROVED SGO-09 transport reduction (pi base-16 normality iff
     S_N(h)=o(N) for every fixed nonzero h);
  4. the PROVED energy gate E and its equivalence to normality (E3);
  5. the signed-pushforward / transport lemmas (SCT-style).

Status discipline: every load-bearing object carries an explicit status label
PROVED / OPEN / REFUTED mirroring docs/CLAIM_SUPPLEMENT_SIGNED_CANCELLATION_BARRIER.md
(SCB-01..15). Nothing here asserts pi normality, o(N), or RH. In particular the
sublinear signed cancellation S_N(h)=o(N) is the OPEN gate and is exposed only
as an *uncertified predicate* that no downstream branch may silently treat as
a theorem. There is deliberately no function that returns "True" for the gate.

Arithmetic is exact: phases are formal elements of the rational group algebra
Q[Q/Z] (see succ_internal_matrix_walk.PhasePoly), never floating-point. Any
numerical complex evaluation is an explicit, separately-labelled diagnostic.
Heavy imports (numpy/scipy) are avoided; only fractions.Fraction and, for the
optional diagnostic, mpmath are used.

No existing module is modified. The authentic recurrence engine is imported
unchanged from succ_internal_matrix_walk.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .succ_internal_matrix_walk import (
    MatrixWalkError,
    PhasePoly,
    authentic_r,
    circle,
    natural,
    original_state,
    rat,
)

__all__ = [
    "SOURCE_ID",
    "SGO_TAIL_BOUND",
    "SGO_TRANSPORT_CONSTANT",
    "TRANSPORT_STATUS",
    "GATE_STATUS",
    "ENERGY_EQUIVALENCE_STATUS",
    "SCB_STATUS",
    "bbp_forcing",
    "bbp_lift",
    "bbp_circle_point",
    "weyl_sum",
    "weyl_sum_poly",
    "evaluate_poly",
    "sgo_tail_partial",
    "sgo_tail_upper",
    "sgo_transport_bound",
    "normal_iff_weyl_sublinear",
    "energy_gate",
    "energy_gate_equivalence",
    "signed_pushforward_partition",
    "SignedPushforwardIdentity",
    "certify_weyl_o_N",
]


# ---------------------------------------------------------------------------
# Status labels (single source of truth, mirroring the barrier ledger).
# ---------------------------------------------------------------------------
SOURCE_ID = "Q:Coherent-Main-X-four-pole-BBP"

# SCB-05 / SGO-09: the PROVED transport reduction.  Do not edit these constants
# without a paper proof in the stated domain.
SGO_TAIL_BOUND = Q(17, 648)          # sum_{n>=1} T_n <= 17/648
SGO_TRANSPORT_CONSTANT = Q(119, 648)  # |S_N(h) - sum e(hU_n)| < (119/648)|h|

TRANSPORT_STATUS = "PROVED"          # SGO-09 (#293), paper-proved, hand re-derived
GATE_STATUS = "OPEN"                 # S_N(h)=o(N) for every fixed nonzero h
ENERGY_EQUIVALENCE_STATUS = "PROVED"  # E3 / SCB-06: energy gate <=> normality
PUSHFORWARD_STATUS = "PROVED"         # SK2-B: partition-coarsening invariant

# Registry of barrier-ledger statuses this module is allowed to reference.
SCB_STATUS = {
    "SCB-04": "PROVED",
    "SCB-05": "PROVED",
    "SCB-06": "PROVED",
    "SCB-12": "OPEN",
    "SCB-13": "OPEN",
}


# ---------------------------------------------------------------------------
# 1. The authentic four-pole BBP recurrence (imported, re-exposed).
# ---------------------------------------------------------------------------
def bbp_forcing(n: int) -> Q:
    """The literal original signed four-pole BBP forcing r(n), n>=1.

    r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2).

    Status: PROVED source definition (do not alter; SCB-10 exact rational).
    """
    return authentic_r(n)


def bbp_lift(n: int) -> Q:
    """The exact unwrapped rational lift U_n, from U_0=0, U_{k+1}=16 U_k + r(k+1).

    Status: PROVED source definition (exact rational; no pi value enters).
    """
    return original_state(n)


def bbp_circle_point(n: int) -> Q:
    """The real-circle observation x_n = {U_n} = U_n mod 1 in [0,1).

    Status: PROVED source definition.
    """
    return circle(original_state(n))


# ---------------------------------------------------------------------------
# 2. Exact rational Weyl sum.
# ---------------------------------------------------------------------------
def weyl_sum_poly(n: int, frequency: int) -> PhasePoly:
    """The exact formal Weyl sum S_N(h) = sum_{n<=N} e(h U_n) in Q[Q/Z].

    The result is a formal element of the rational group algebra Q[Q/Z]: an
    exact sum of monomials e({h U_n}) with rational coefficients, with no
    floating-point evaluation. This is the object whose O(1)-size is the OPEN
    gate; the exact representation itself is PROVED (finite, rational).

    Status: PROVED finite construction; the asymptotic size is OPEN.
    """
    natural(n, 1, 2000)
    if type(frequency) is not int or frequency == 0:
        raise MatrixWalkError("nonzero integer frequency required")
    acc = PhasePoly.zero()
    for j in range(1, n + 1):
        acc = acc + PhasePoly.monomial(circle(frequency * original_state(j)))
    return acc


def weyl_sum(n: int, frequency: int) -> PhasePoly:
    """Alias for weyl_sum_poly (exact formal Weyl sum S_N(h))."""
    return weyl_sum_poly(n, frequency)


def evaluate_poly(poly: PhasePoly, precision: int = 50) -> complex:
    """Numerical diagnostic evaluation of a PhasePoly; never a certificate.

    This returns an ordinary complex float/mpmath value for inspection only.
    No asymptotic statement may be inferred from a finite set of such values.
    """
    return poly.evaluation(precision)


# ---------------------------------------------------------------------------
# 3. PROVED transport reduction (SGO-09 / #293).
# ---------------------------------------------------------------------------
def sgo_tail_partial(n: int, terms: int = 40) -> Q:
    """Exact rational *partial* sum of the future tail T_n, n>=1.

    Returns sum_{j=1..terms} 16^{-j} r(n+j) exactly, which is a positive
    rational lower bound of the full convergent tail
        T_n = sum_{j>=1} 16^{-j} r(n+j) > 0,
    satisfying U_n + T_n = 16^{n-1} pi. The full T_n is irrational (it equals
    a pi translate); only the partial sum and the PROVED uniform bound
    sum_{n>=1} T_n <= 17/648 are exact rational statements.

    Status: PROVED source-exact identity; the partial sum is a finite rational
    enclosure, not the irrational T_n itself.
    """
    natural(n, 1, 10**6)
    natural(terms, 1, 1000)
    return sum((Q(authentic_r(n + j)) / (16 ** j) for j in range(1, terms + 1)), Q())


def sgo_tail_upper() -> Q:
    """The PROVED uniform tail bound sum_{n>=1} T_n <= 17/648 (exact rational).

    Status: PROVED (SGO-09 / SCB-05).
    """
    return SGO_TAIL_BOUND


def sgo_transport_bound(n: int, frequency: int) -> Q:
    """The PROVED SGO-09 transport error upper bound, exact.

    For all N>=1 and h!=0:
        | sum_{n<=N} e(h 16^{n-1} pi) - sum_{n<=N} e(h U_n) | < (119/648) |h|.

    The bound returned here is the exact rational (119/648)*|h| (strict <),
    holding uniformly in N. It is the transport *equivalence*, not any
    cancellation; the normalized Weyl sums differ by O_h(1/N).

    Status: PROVED (SGO-09 / #293 / SCB-05).
    """
    natural(n, 1)
    if type(frequency) is not int or frequency == 0:
        raise MatrixWalkError("nonzero integer frequency required")
    return SGO_TRANSPORT_CONSTANT * abs(frequency)


def normal_iff_weyl_sublinear() -> dict:
    """State the PROVED equivalence without asserting either side.

    pi is base-16 normal iff S_N(h) = o(N) for every fixed nonzero integer h.

    This function returns a *record* of the theorem (a statement of the
    reduction), never a truth value for the gate. Status of the reduction is
    PROVED; status of the right-hand side (and hence of pi normality) is OPEN.
    """
    return {
        "reduction": "pi base-16 normal <=> S_N(h)=o(N) for every fixed h!=0",
        "reduction_status": TRANSPORT_STATUS,
        "transport_constant": SGO_TRANSPORT_CONSTANT,
        "tail_bound": SGO_TAIL_BOUND,
        "gate_status": GATE_STATUS,
        "asserts_normality": False,
    }


# ---------------------------------------------------------------------------
# 4. Energy gate E and its equivalence to normality (E3 / SCB-06).
# ---------------------------------------------------------------------------
def energy_gate(n: int, modulus: int, frequency: int) -> PhasePoly:
    """Exact formal energy E_{N,M}(h) = (M/N^2) sum_t |sum_{n=t mod M} e(hU_n)|^2.

    The sum over residue classes t is exact in Q[Q/Z]: each class sum
    S_t = sum_{n<=N, n=t mod M} e(h U_n) is a PhasePoly, and |S_t|^2 is the
    formal star product S_t * S_t^*. E is the exact rational-linear combination.

    Status: PROVED finite construction (SCB-04); the decay E->0 is the OPEN
    gate (equivalent to normality by the PROVED E3 / SCB-06 reduction).
    """
    natural(n, 1, 2000)
    natural(modulus, 1, 2000)
    if type(frequency) is not int or frequency == 0:
        raise MatrixWalkError("nonzero integer frequency required")
    class_sums = [PhasePoly.zero() for _ in range(modulus)]
    for j in range(1, n + 1):
        t = j % modulus
        class_sums[t] = class_sums[t] + PhasePoly.monomial(
            circle(frequency * original_state(j))
        )
    # E = (M/N^2) * sum_t S_t S_t^*
    total = PhasePoly.zero()
    for S in class_sums:
        total = total + (S * S.star())
    return total * (Q(modulus) / Q(n * n))


def energy_gate_equivalence() -> dict:
    """State the PROVED E3 / SCB-06 equivalence without asserting the gate.

    The following are equivalent (paper-proved):
      1. pi is normal to base 16;
      2. for one fixed M>=1, E(N,M,h)->0 for every fixed nonzero h;
      3. for every fixed M>=1 the same holds;
      4. there is a monotone schedule M(N)=3*16^j -> inf, o(N), with the same.

    Fixed-M and existential-slowly-growing energy gates are equivalent to
    normality. A *prescribed* growing schedule is genuinely stronger (SCB-07,
    SCB-14, SCB-15: normal counterexamples with limsup E=1 exist).

    Status: PROVED equivalence; the decay itself is OPEN.
    """
    return {
        "equivalence": (
            "E_{N,M}(h)->0 for fixed M (or some M(N)=3*16^j -> inf, o(N)) "
            "for every fixed h!=0  <=>  pi base-16 normal"
        ),
        "equivalence_status": ENERGY_EQUIVALENCE_STATUS,
        "gate_status": GATE_STATUS,
        "prescribed_schedule_note": (
            "A prescribed growing schedule M(N) is strictly stronger than "
            "normality; normal finite-type carriers exist with limsup E>=1/4 "
            "(SCB-07/14/15)."
        ),
        "asserts_normality": False,
    }


# ---------------------------------------------------------------------------
# 5. Signed pushforward / transport lemmas (SCT / SK2-B).
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class SignedPushforwardIdentity:
    """The partition-coarsening invariant of SK2-B.

    With z_n = e(h U_n), the identity
        |S_N(h)|^2 = sum_A |S_A|^2 + sum_{A!=B} S_A conj(S_B)
    is a partition-coarsening invariant: refinement only moves mass between the
    within-cell diagonal and the signed cross term. The cross term is
    sign-indefinite and carries no provable negative bias.

    Status: PROVED (no-go, SK2-B). It yields no saving by itself.
    """

    cells: tuple[tuple[int, ...], ...]
    cell_sums: tuple[PhasePoly, ...]
    within_diagonal: PhasePoly
    signed_cross: PhasePoly
    total_squared: PhasePoly


def signed_pushforward_partition(
    n: int, frequency: int, cells: tuple[tuple[int, ...], ...]
) -> SignedPushforwardIdentity:
    """Exact signed pushforward decomposition of |S_N(h)|^2 over a partition.

    cells is a partition of {1..n}; each cell is a tuple of indices. The
    identity |S_N|^2 = within-diagonal + signed-cross is computed exactly in
    Q[Q/Z]. This is a PROVED partition-coarsening invariant (SK2-B); it
    supplies no cancellation and the cross term is sign-indefinite.

    Status: PROVED (SK2-B). No o(N) saving follows.
    """
    natural(n, 1, 2000)
    if type(frequency) is not int or frequency == 0:
        raise MatrixWalkError("nonzero integer frequency required")
    flat = [j for cell in cells for j in cell]
    if sorted(flat) != list(range(1, n + 1)):
        raise ValueError("cells must be a partition of {1..n}")
    cell_sums = []
    for cell in cells:
        S = PhasePoly.zero()
        for j in cell:
            S = S + PhasePoly.monomial(circle(frequency * original_state(j)))
        cell_sums.append(S)
    within = PhasePoly.zero()
    for S in cell_sums:
        within = within + (S * S.star())
    total = sum(cell_sums, PhasePoly.zero())
    total_squared = total * total.star()
    cross = total_squared - within
    return SignedPushforwardIdentity(
        cells=cells, cell_sums=tuple(cell_sums),
        within_diagonal=within, signed_cross=cross,
        total_squared=total_squared,
    )


# ---------------------------------------------------------------------------
# 6. The OPEN gate — an uncertified predicate, never a theorem.
# ---------------------------------------------------------------------------
def certify_weyl_o_N(n: int, frequency: int, tolerance: Q) -> dict:
    """Attempt to certify |S_N(h)|/N <= tolerance; the result is NEVER a proof.

    This is a *finite diagnostic* that returns the exact ratio |S_N(h)|/N as a
    formal PhasePoly (whose size is exact) plus a clear `certified` flag that
    is always False. A naive claim that a finite small ratio certifies o(N)
    is exactly what the regression test must reject. No branch may call this
    and treat the output as a normality certificate.

    Status: the sublinear gate is OPEN; this function never certifies it.
    """
    natural(n, 1, 2000)
    if type(frequency) is not int or frequency == 0:
        raise MatrixWalkError("nonzero integer frequency required")
    tol = rat(tolerance)
    S = weyl_sum_poly(n, frequency)
    ratio = S * (Q(1) / Q(n))
    # The "size" is the exact L1 mass of the formal ratio; this is diagnostic.
    mass = sum(abs(c) for _, c in ratio.terms)
    return {
        "n": n,
        "frequency": frequency,
        "ratio_mass": mass,
        "tolerance": tol,
        "within_tolerance": bool(mass <= tol),
        "certified": False,  # never True: finite mass is not o(N)
        "gate_status": GATE_STATUS,
    }
