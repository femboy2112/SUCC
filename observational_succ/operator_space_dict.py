"""Exact witnesses for the absolute-vs-K-relative gap distinction (Proof Forge III,
Lane C — operator-space reconciliation).

The original Suzuki/Weil high block is described two ways in the repository:

* in the DERIVATIVE carrier (``u in L^2_0(-1/2,1/2)``) the inherited coercivity is
  ``D_4 >= kappa Q_4 K Q_4`` with ``K = V^* V = (-Delta_N)^{-1}`` -- a *K-relative*
  gap (``certified_four_schur_trial``, ``tate_weighted_bessel_four_schur``);
* in the PRIMITIVE carrier (``E = (deg<=3 polys)^perp subset L^2(I)``) the same
  inequality reads ``D >= kappa I_E`` -- an *absolute* ``L^2`` gap, under inherited
  source/closure hypotheses (``DIRECTIONAL_ORIGINAL_INVERSE``,
  ``ORIGINAL_SOURCE_FORM_CLOSURE``).

Meanwhile ``RH_RIGIDITY_LANE`` records that the authentic high block is GAPLESS in
the derivative-``L^2`` metric (the Suzuki kernel is compact, so ``0 in sigma`` in the
limit; the ``diag(1,1/2,1/3,...)`` phenomenon). This module makes rigorous, with small
EXACT witnesses, the standing caution that:

    a compact / gapless operator in one metric does NOT imply absence of coercivity
    in a differently-normed representation, AND a K-relative gap must never be
    substituted for an absolute gap -- doing so can FLIP a certified Schur sign.

Everything is exact (``sympy.Rational``). A float is never a certificate. These are
GENERIC exact linear-algebra witnesses; they are NOT the authentic signed source and
must never be read as a signed-Weil positivity result (the ``source_form_identified``
obligation of :class:`~observational_succ.quantitative_rigidity.RigidityDiagnostics`
is FALSE for every object built here). No zeta-zero coordinate is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import sympy as sp

from .quantitative_rigidity import (
    as_exact_matrix,
    min_eigenvalue_exact,
    schur_complement,
    conservative_surrogate,
    negative_witness,
    coupling_negative_vector,
    quad,
    inverse_decay_block,
    uniform_gap_profile,
    RigidityDiagnostics,
    diagnostics_from_block,
)

Rat = sp.Rational


def _is_psd_by_least_eig(M: sp.Matrix) -> bool:
    """PSD test via the exact least eigenvalue (``min_eigenvalue_exact(M) >= 0``).

    Used in place of ``quantitative_rigidity.is_positive_semidefinite`` here because
    that routine enumerates all ``2^n - 1`` principal minors -- fine for the 2x2/3x3
    Schur blocks it is built for, but exponential on the ``diag(1,1/2,...,1/N)``
    gapless family (``N`` up to 64) these witnesses use. ``min_eigenvalue_exact`` has a
    fast exact diagonal path and otherwise uses characteristic-polynomial roots; a real
    symmetric matrix is PSD iff its least eigenvalue is ``>= 0``."""
    return min_eigenvalue_exact(M) >= 0


# --------------------------------------------------------------------------- #
# The two gap notions, stated as exact predicates (never conflated)
# --------------------------------------------------------------------------- #
def absolute_gap_holds(D: sp.Matrix, kappa: sp.Expr) -> bool:
    """``D >= kappa I`` as forms (exact): D - kappa I is PSD.

    This is the ABSOLUTE gap. ``D >= kappa I`` with ``kappa > 0`` makes ``D`` boundedly
    invertible with ``||D^{-1}|| <= 1/kappa`` -- the hypothesis the finite Schur
    theorem (``quantitative_rigidity.schur_complement``, requiring ``D > 0``) needs to
    transport positivity with a *bounded* inverse response ``A - kappa^{-1} B B^*``."""
    D = as_exact_matrix(D)
    I = sp.eye(D.rows)
    return _is_psd_by_least_eig(D - sp.sympify(kappa) * I)


def k_relative_gap_holds(D: sp.Matrix, K: sp.Matrix, kappa: sp.Expr) -> bool:
    """``D >= kappa K`` as forms (exact): D - kappa K is PSD.

    This is the K-RELATIVE gap. With ``K = V^* V`` it bounds the inverse response by
    ``kappa^{-1} K^{-1}`` (an UNBOUNDED operator when ``K`` is compact), NOT by a
    bounded ``kappa^{-1} I``. It is a strictly weaker statement than the absolute gap
    whenever ``K`` is not bounded below (``0 in sigma(K)``)."""
    D = as_exact_matrix(D)
    K = as_exact_matrix(K)
    return _is_psd_by_least_eig(D - sp.sympify(kappa) * K)


# --------------------------------------------------------------------------- #
# Witness 1: gapless (absolute) yet uniformly K-relative-coercive
# --------------------------------------------------------------------------- #
@dataclass
class GapNotionWitness:
    """One ``N`` of the ``D_N = diag(1,1/2,...,1/N)`` family (the authentic
    gaplessness model, ``inverse_decay_block``)."""
    N: int
    absolute_min_eig: sp.Expr          # = 1/N  -> 0 : no uniform absolute gap
    absolute_gap_at_1: bool            # D_N >= 1*I ?  (False for N>=2)
    k_relative_gap_at_1_with_K_eq_D: bool  # D_N >= 1*K with K=D_N ?  (always True)

    def as_record(self) -> dict:
        return {
            "N": self.N,
            "absolute_min_eig": str(self.absolute_min_eig),
            "absolute_gap_at_1": self.absolute_gap_at_1,
            "k_relative_gap_at_1_with_K_eq_D": self.k_relative_gap_at_1_with_K_eq_D,
        }


def gap_notion_witness(N: int) -> GapNotionWitness:
    """For ``D_N = diag(1,1/2,...,1/N)``: exhibit that the ABSOLUTE gap collapses
    (``min eig = 1/N -> 0``) while a UNIFORM K-relative gap ``kappa = 1`` survives,
    taking ``K = D_N`` (so ``D_N = 1 * K`` identically).

    This is exactly the authentic situation in miniature: the derivative-``L^2``
    (absolute) gap of the compact-kernel high block vanishes, yet ``D_4 >= kappa K``
    (``K = V^*V``) is a genuine uniform bound. The two notions are NOT interchangeable."""
    D = inverse_decay_block(N)          # quantitative_rigidity canonical gapless witness
    return GapNotionWitness(
        N=N,
        absolute_min_eig=min_eigenvalue_exact(D),       # 1/N
        absolute_gap_at_1=absolute_gap_holds(D, Rat(1)),
        k_relative_gap_at_1_with_K_eq_D=k_relative_gap_holds(D, D, Rat(1)),
    )


def gapless_profile(Ns: List[int]) -> List[Tuple[int, sp.Expr]]:
    """``(N, min eig D_N)`` tabulated exactly; the sequence ``1/N -> 0`` proves the
    absence of a uniform absolute gap (thin wrapper over
    ``quantitative_rigidity.uniform_gap_profile(inverse_decay_block, Ns)``)."""
    return uniform_gap_profile(inverse_decay_block, Ns)


# --------------------------------------------------------------------------- #
# Witness 2: a K-relative gap MISREAD as an absolute gap FLIPS the Schur sign
# --------------------------------------------------------------------------- #
@dataclass
class TransportDefectWitness:
    """The exact transport defect: substituting a (true) K-relative gap for an
    absolute gap flips the certified sign of the Schur complement."""
    M: sp.Matrix
    n_A: int
    kappa: sp.Expr
    K_high: sp.Matrix
    D_has_absolute_gap: bool           # D >= kappa I ?   (FALSE: the illegal premise)
    D_has_k_relative_gap: bool         # D >= kappa K ?   (TRUE: the real premise)
    true_schur: sp.Matrix              # A - B D^{-1} B^*  (the genuine complement)
    true_schur_psd: bool
    absolute_surrogate: sp.Matrix      # A - kappa^{-1} B B^*  (valid ONLY if D>=kappa I)
    absolute_surrogate_psd: bool
    sign_flips: bool                   # surrogate PSD while true Schur not PSD
    negative_vector_of_M: sp.Matrix    # exact v, v^T M v < 0
    coupling_vector: sp.Matrix         # (x; -D^{-1}B^* x) realizing <S x,x>

    def as_record(self) -> dict:
        return {
            "M": str(self.M.tolist()),
            "n_A": self.n_A,
            "kappa": str(self.kappa),
            "K_high": str(self.K_high.tolist()),
            "D_has_absolute_gap": self.D_has_absolute_gap,
            "D_has_k_relative_gap": self.D_has_k_relative_gap,
            "true_schur": str(self.true_schur.tolist()),
            "true_schur_psd": self.true_schur_psd,
            "absolute_surrogate": str(self.absolute_surrogate.tolist()),
            "absolute_surrogate_psd": self.absolute_surrogate_psd,
            "sign_flips": self.sign_flips,
            "negative_vector_of_M": str(self.negative_vector_of_M.T.tolist()),
            "coupling_vector": str(self.coupling_vector.T.tolist()),
        }


def k_relative_misread_as_absolute() -> TransportDefectWitness:
    """Exact witness that reading a K-relative gap as an absolute gap is UNSOUND.

    ``M = [[2, 0, 1], [0, 1, 0], [1, 0, 1/10]]``, ``n_A = 1`` (one low mode, two high).
    High block ``D = diag(1, 1/10)``, ``kappa = 1``, ``K = D``.

    * ``D >= kappa K`` holds (``D - 1*K = 0``): a genuine, uniform K-relative gap.
    * ``D >= kappa I`` FAILS (``D - I = diag(0, -9/10)`` is not PSD): there is no
      absolute gap at ``kappa = 1``; ``||D^{-1}|| = 10 > 1``.
    * The ABSOLUTE surrogate ``A - kappa^{-1} B B^* = [2 - 1] = [1] > 0`` would CERTIFY
      ``S >= 0`` -- but it is only valid under the (false) absolute gap.
    * The TRUE Schur complement ``A - B D^{-1} B^* = [2 - 10] = [-8] < 0`` is indefinite.

    So the surrogate reports POSITIVE while the truth is NEGATIVE: the sign flips.
    An exact negative vector of the full ``M`` is returned for independent recheck."""
    M = sp.Matrix([[2, 0, 1],
                   [0, 1, 0],
                   [1, 0, Rat(1, 10)]])
    n_A = 1
    kappa = Rat(1)
    D_high = sp.Matrix([[1, 0], [0, Rat(1, 10)]])   # = K (the inverse-Neumann-style metric)
    K_high = D_high

    S = schur_complement(M, n_A)                     # A - B D^{-1} B^*  (exact)
    surrogate = conservative_surrogate(M, n_A, kappa)  # A - kappa^{-1} B B^*
    S_psd = _is_psd_by_least_eig(S)
    surr_psd = _is_psd_by_least_eig(surrogate)
    neg = negative_witness(M)                        # exact v, v^T M v < 0
    coup = coupling_negative_vector(M, n_A, [1])     # (x; -D^{-1} B^* x)

    return TransportDefectWitness(
        M=M, n_A=n_A, kappa=kappa, K_high=K_high,
        D_has_absolute_gap=absolute_gap_holds(D_high, kappa),
        D_has_k_relative_gap=k_relative_gap_holds(D_high, K_high, kappa),
        true_schur=S, true_schur_psd=S_psd,
        absolute_surrogate=surrogate, absolute_surrogate_psd=surr_psd,
        sign_flips=(surr_psd and not S_psd),
        negative_vector_of_M=neg,
        coupling_vector=coup,
    )


def transport_defect_diagnostics() -> RigidityDiagnostics:
    """The same block fed through :func:`diagnostics_from_block` with
    ``source_form_identified=False``. Its ``certificate_status`` is REFUTED (the true
    Schur complement is not PSD); even had it been PSD it would be INAPPLICABLE, since
    the form is a generic model, not the identified signed Weil source. This shows the
    quantitative-rigidity verdict machinery is NOT fooled by the absolute surrogate."""
    M = sp.Matrix([[2, 0, 1],
                   [0, 1, 0],
                   [1, 0, Rat(1, 10)]])
    return diagnostics_from_block(M, 1, source_form_identified=False, kappa=Rat(1))


__all__ = [
    "absolute_gap_holds",
    "k_relative_gap_holds",
    "GapNotionWitness",
    "gap_notion_witness",
    "gapless_profile",
    "TransportDefectWitness",
    "k_relative_misread_as_absolute",
    "transport_defect_diagnostics",
]
