"""Quantitative rigidity core (Operation Rigidity Forge, Part III).

A compositional, *exact* theory of positive forms, Schur complements / shorting,
and the obstructions that separate a genuine global positivity certificate from a
merely-sufficient (and often invalid) finite surrogate.

Everything here is exact (sympy ``Rational`` / symbolic). **A float is never a
certificate** -- floats appear only as search heuristics whose output is then
re-verified exactly (see :func:`negative_witness`).

The module is deliberately NOT organized around a single scalar "rigidity score".
Rigidity is a *vector* of independent obligations -- source adequacy, approximation
quality, spectral gap, range inclusion, inverse response, source-form identification
-- and collapsing them into one number is exactly the error this module exists to
prevent (:class:`RigidityDiagnostics`).

Theorems implemented / certified here
-------------------------------------
* **Finite Schur (2.1).** For ``M = [[A, B], [B^T, D]]`` real symmetric with
  ``D > 0``: ``M >= 0  <=>  A - B D^{-1} B^T >= 0``. Exact PD/PSD certificates,
  exact negative-vector witnesses, exact square-completion identity, and the
  ``D >= 0`` singular extension via the Moore-Penrose / shorted operator with the
  correct range-inclusion hypothesis ``ran(B^T) ⊆ ran(D)``.
* **Gapped vs gapless (2.2).** The square-completion identity
  ``Q(x⊕y) = <(A - W^*W)x, x> + ||D^{1/2}y + Wx||^2`` with ``B^T = D^{1/2} W``,
  verified in the exact ``D``-form (no irrational ``D^{1/2}`` needed), plus the
  gapless witness ``D = diag(1, 1/2, 1/3, ...)`` where every finite compression is
  strictly coercive yet no uniform gap ``kappa I`` survives.
* **Form-core positivity transport (2.3).** Stated in the dossier; the *necessity*
  of a true form core (not mere L^2-density) is witnessed here exactly by
  :func:`form_core_negative_control`.

See ``research/2026-10-20/QUANTITATIVE_RIGIDITY.md`` for statements and proofs, and
``observational_succ/gemini_crucible.py`` for the hostile audit that reuses this
machinery.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations
from typing import List, Optional, Sequence, Tuple

import sympy as sp

Rat = sp.Rational


class RigidityInputError(TypeError):
    """A non-exact input reached the trusted exact-certificate path.

    Raised when a Python ``float`` or a sympy ``Float`` entry is handed to a
    certificate predicate. A float is never a certificate: rationalize inputs
    with :class:`sympy.Rational` (or an exact algebraic number) first. This is a
    hard boundary, not a silent ``nsimplify`` -- approximate numbers must not be
    laundered into claimed exact premises."""


class UndecidableSignError(RuntimeError):
    """The exact sign of a quantity could not be decided (e.g. it carries a free
    symbol). The trusted path reports this explicitly rather than returning an
    accidental boolean certificate (the fourth verdict: UNKNOWN, not False)."""


# --------------------------------------------------------------------------- #
# Exact linear-algebra primitives
# --------------------------------------------------------------------------- #
def as_exact_matrix(M, *, require_exact: bool = True) -> sp.Matrix:
    """Coerce to an exact sympy Matrix, REJECTING floating-point entries.

    The trusted certificate path is exact-only: any Python ``float`` or sympy
    ``Float`` entry raises :class:`RigidityInputError`. Exact rationals,
    integers and exact algebraic numbers (e.g. ``sqrt(2)``) are accepted.

    Pass ``require_exact=False`` only for a throwaway *numeric hint* matrix whose
    value will never back an emitted certificate (no such call currently exists
    in the trusted path; numeric guidance is confined to private helpers that
    re-verify their output exactly)."""
    if not isinstance(M, sp.Matrix):
        M = sp.Matrix(M)
    if require_exact and M.atoms(sp.Float):
        raise RigidityInputError(
            "floating-point entry in the exact-certificate path; a float is "
            "never a certificate -- rationalize with sympy.Rational first")
    return M


def _symmetric_part(M: sp.Matrix) -> sp.Matrix:
    """(M + M^T)/2, the only part a real quadratic form sees (exact)."""
    M = as_exact_matrix(M)
    return (M + M.T) / 2


def _sign(x) -> int:
    """Exact sign of a number-valued expression: +1 / 0 / -1.

    Raises :class:`UndecidableSignError` when the sign is not exactly decidable
    (free symbols, or an algebraic expression sympy cannot resolve). Never
    guesses, never rounds."""
    x = sp.sympify(x)
    if x.is_zero:
        return 0
    if x.is_positive:
        return 1
    if x.is_negative:
        return -1
    raise UndecidableSignError(f"cannot exactly decide the sign of {x!s}")


def is_symmetric_exact(M: sp.Matrix) -> bool:
    M = as_exact_matrix(M)
    return M.rows == M.cols and sp.simplify(M - M.T).is_zero_matrix


def leading_principal_minors(M: sp.Matrix) -> List[sp.Expr]:
    """det of the top-left k x k block, k = 1..n (exact)."""
    M = as_exact_matrix(M)
    return [M[:k, :k].det() for k in range(1, M.rows + 1)]


def all_principal_minors(M: sp.Matrix) -> List[sp.Expr]:
    """det of every principal submatrix (all index subsets), exact.

    Used for the PSD test: a symmetric matrix is positive *semi*definite iff
    *every* principal minor is >= 0 (leading ones alone do not suffice -- that is
    only the strict/PD Sylvester criterion)."""
    M = as_exact_matrix(M)
    n = M.rows
    minors: List[sp.Expr] = []
    for k in range(1, n + 1):
        for idx in combinations(range(n), k):
            sub = M[idx, idx]
            minors.append(sub.det())
    return minors


def is_positive_definite(M: sp.Matrix) -> bool:
    """Exact PD test via Sylvester (leading principal minors all > 0).

    Requires symmetry; a non-symmetric argument is judged by its symmetric part,
    which is the only part a quadratic form sees. Signs are decided exactly
    (:func:`_sign`); an undecidable sign raises :class:`UndecidableSignError`
    rather than silently returning a boolean."""
    S = _symmetric_part(M)
    return all(_sign(d) > 0 for d in leading_principal_minors(S))


def is_positive_semidefinite(M: sp.Matrix) -> bool:
    """Exact PSD test: symmetric and every principal minor >= 0.

    Leading minors alone decide only PD (Sylvester); PSD genuinely needs *all*
    principal minors (the ``[[0,0],[0,-1]]`` trap). Signs are decided exactly;
    an undecidable sign raises :class:`UndecidableSignError`."""
    S = _symmetric_part(M)
    return all(_sign(d) >= 0 for d in all_principal_minors(S))


def quad(M: sp.Matrix, v: Sequence) -> sp.Expr:
    """Exact quadratic form v^T M v."""
    M = as_exact_matrix(M)
    v = sp.Matrix(v)
    return sp.expand((v.T * M * v)[0, 0])


def _congruence_reduce(S: sp.Matrix) -> Tuple[bool, Optional[sp.Matrix]]:
    """Lagrange symmetric-congruence reduction of an exact symmetric matrix.

    Returns ``(True, None)`` when ``S`` is positive semidefinite, or
    ``(False, v)`` with ``v`` an exact column vector such that ``v^T S v < 0``.

    **Completeness.** Every symmetric matrix over an ordered field is congruent
    to a diagonal form. This routine realises that congruence while tracking the
    transform ``P`` so that ``P^T S P`` equals the running matrix ``W`` at all
    times. Each step either (a) finds a strictly negative diagonal pivot -> the
    current basis vector ``P[:, i]`` is an exact negative direction; (b) uses a
    strictly positive pivot to eliminate its row/column by congruence (the
    classic Schur step), removing one index; (c) with all remaining diagonals
    zero but some off-diagonal ``c != 0``, the indefinite block
    ``[[0, c], [c, 0]]`` gives the exact direction ``P[:, i] -/+ P[:, k]``; or
    (d) the remaining block is entirely zero, so ``S`` is PSD. Case (b) strictly
    shrinks the active set, so the loop terminates in <= n steps. There is NO
    numerical step, hence no spurious third 'failed' verdict for a supported
    exact input -- the recurrence that defeated the old float heuristic
    (``[[1, -5000], [-5000, 24999999]]``, witness ``(5000, 1)``) is handled
    structurally by the positive-pivot elimination.

    An undecidable diagonal sign (free symbols) raises
    :class:`UndecidableSignError`."""
    S = as_exact_matrix(S)
    n = S.rows
    W = S.copy()                      # running congruent matrix  W = P^T S P
    P = sp.eye(n)                     # columns: current basis vectors in orig coords
    remaining = list(range(n))
    while remaining:
        # Guard: every remaining diagonal sign must be exactly decidable.
        for i in remaining:
            if W[i, i].is_zero is None and not W[i, i].is_number:
                raise UndecidableSignError(
                    f"undecidable diagonal entry during reduction: {W[i, i]!s}")
        # (a) a strictly negative diagonal pivot is an immediate witness.
        neg = [i for i in remaining if W[i, i].is_negative]
        if neg:
            return False, P[:, neg[0]]
        # (b) eliminate a strictly positive pivot by symmetric congruence.
        pos = [i for i in remaining if W[i, i].is_positive]
        if pos:
            i = pos[0]
            piv = W[i, i]
            mult = {j: W[i, j] / piv for j in remaining if j != i}  # exact / exact
            for j, m in mult.items():        # column op: W <- W E,  P <- P E
                if m == 0:
                    continue
                W[:, j] = W[:, j] - m * W[:, i]
                P[:, j] = P[:, j] - m * P[:, i]
            for j, m in mult.items():        # row op: W <- E^T W   (same m)
                if m == 0:
                    continue
                W[j, :] = W[j, :] - m * W[i, :]
            remaining.remove(i)
            continue
        # (c) all remaining diagonals are zero; a nonzero off-diagonal is a
        #     [[0, c], [c, 0]] indefinite 2x2 block -> exact negative direction.
        found = None
        for a in range(len(remaining)):
            for b in range(a + 1, len(remaining)):
                i, k = remaining[a], remaining[b]
                if not W[i, k].is_zero:
                    found = (i, k, W[i, k])
                    break
            if found:
                break
        if found is not None:
            i, k, c = found
            # (e_i - e_k)^T W (e_i - e_k) = -2c ;  (e_i + e_k)^T W (e_i + e_k) = +2c
            v = P[:, i] - P[:, k] if c.is_positive else P[:, i] + P[:, k]
            return False, v
        # (d) remaining block is entirely zero -> contributes 0 -> S is PSD.
        break
    return True, None


def negative_witness(M: sp.Matrix, max_denom: Optional[int] = None) -> Optional[sp.Matrix]:
    """Return an EXACT vector v with ``v^T M v < 0``, or ``None`` if M is PSD.

    Complete and deterministic. Runs the Lagrange symmetric-congruence reduction
    (:func:`_congruence_reduce`) on the symmetric part. For a supported exact
    (rational / exact-algebraic) input the outcome is ALWAYS one of two verdicts:
    ``None`` (CERTIFIED PSD) or an exact ``v`` with ``v^T M v < 0`` (CERTIFIED
    NON-PSD). There is no numerical-failure third outcome -- the old
    float-eigenvector + bounded-denominator search is gone (it could miss a thin
    negative cone, e.g. ``[[1, -5000], [-5000, 24999999]]`` whose witness
    ``(5000, 1)`` needs denominator 5000, far past the tested bound).

    ``max_denom`` is accepted and ignored (the method no longer rounds); it is
    retained only for backward call compatibility."""
    del max_denom  # no rounding; the algorithm is exact and complete
    S = _symmetric_part(M)
    psd, v = _congruence_reduce(S)
    if psd:
        return None
    # the witness is exact; re-verify the defining obligation exactly.
    if not (quad(S, v) < 0):
        raise RuntimeError(
            "internal invariant violated: congruence witness was not negative "
            f"(got {quad(S, v)!s}); this should be unreachable")
    return v


# --------------------------------------------------------------------------- #
# Schur complement (2.1) and the shorted / generalized complement (D >= 0)
# --------------------------------------------------------------------------- #
def _split(M: sp.Matrix, n_A: int) -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    M = as_exact_matrix(M)
    A = M[:n_A, :n_A]
    B = M[:n_A, n_A:]
    D = M[n_A:, n_A:]
    return A, B, D


def schur_complement(M: sp.Matrix, n_A: int) -> sp.Matrix:
    """A - B D^{-1} B^T, requiring D invertible (D > 0 for the theorem)."""
    A, B, D = _split(M, n_A)
    if D.det() == 0:
        raise ValueError("D is singular; use shorted_complement with the "
                         "range-inclusion hypothesis instead")
    return sp.simplify(A - B * D.inv() * B.T)


def range_inclusion_holds(M: sp.Matrix, n_A: int) -> bool:
    """ran(B^T) ⊆ ran(D), the exact hypothesis for the D >= 0 shorted complement.

    Equivalent to (I - D D^+) B^T = 0 with D^+ the Moore-Penrose pseudoinverse."""
    A, B, D = _split(M, n_A)
    Dp = D.pinv()
    I = sp.eye(D.rows)
    return sp.simplify((I - D * Dp) * B.T).is_zero_matrix


def shorted_complement(M: sp.Matrix, n_A: int) -> sp.Matrix:
    """Generalized Schur complement A - B D^+ B^T (Moore-Penrose).

    For D >= 0 with the range inclusion ran(B^T) ⊆ ran(D) this equals the shorted
    operator and the equivalence M >= 0  <=>  shorted >= 0 continues to hold. If
    the range inclusion FAILS, M cannot be PSD (B^T leaks outside ran(D)); callers
    should check :func:`range_inclusion_holds` first."""
    A, B, D = _split(M, n_A)
    return sp.simplify(A - B * D.pinv() * B.T)


def square_completion_identity(M: sp.Matrix, n_A: int,
                               x: Sequence, y: Sequence) -> bool:
    """Verify, exactly, the completed-square decomposition (D > 0):

        [x; y]^T M [x; y]  ==  <S x, x> + <D (y + D^{-1} B^T x), (y + D^{-1} B^T x)>

    where S = A - B D^{-1} B^T is the Schur complement. This is the exact,
    irrational-sqrt-free form of ``Q = <(A - W^*W)x,x> + ||D^{1/2}y + Wx||^2`` with
    ``B^T = D^{1/2} W`` and ``W^*W = B D^{-1} B^T``."""
    A, B, D = _split(M, n_A)
    if D.det() == 0:
        raise ValueError("square-completion here assumes D > 0")
    x = sp.Matrix(x)
    y = sp.Matrix(y)
    full = sp.Matrix.vstack(x, y)
    lhs = quad(M, full)
    S = A - B * D.inv() * B.T
    shift = y + D.inv() * B.T * x
    rhs = (x.T * S * x)[0, 0] + (shift.T * D * shift)[0, 0]
    return sp.simplify(lhs - rhs) == 0


@dataclass
class FiniteSchurCertificate:
    """Exact certificate for the finite Schur theorem on M = [[A,B],[B^T,D]]."""
    n_A: int
    D_positive_definite: bool
    D_positive_semidefinite: bool
    range_inclusion: Optional[bool]          # only meaningful when D is singular
    schur: sp.Matrix                          # A - B D^{-1} B^T  (or shorted)
    schur_psd: bool
    M_psd: bool
    equivalence_holds: bool                   # M_psd <=> schur_psd (under D cond.)
    negative_vector: Optional[sp.Matrix]      # exact v with v^T M v < 0 if M not PSD
    note: str = ""

    def as_record(self) -> dict:
        return {
            "n_A": self.n_A,
            "D_positive_definite": self.D_positive_definite,
            "D_positive_semidefinite": self.D_positive_semidefinite,
            "range_inclusion": self.range_inclusion,
            "schur": str(self.schur.tolist()),
            "schur_psd": self.schur_psd,
            "M_psd": self.M_psd,
            "equivalence_holds": self.equivalence_holds,
            "negative_vector": None if self.negative_vector is None
            else str(self.negative_vector.T.tolist()),
            "note": self.note,
        }


def finite_schur_certificate(M: sp.Matrix, n_A: int) -> FiniteSchurCertificate:
    """Build the exact finite Schur certificate (theorem 2.1 + 2.1-extension).

    Checks D > 0 (the clean hypothesis) or, when D is singular PSD, the range
    inclusion and uses the shorted complement. Confirms the equivalence
    ``M >= 0 <=> complement >= 0`` holds under the stated D-condition, and returns
    an exact negative-vector witness when M is not PSD."""
    A, B, D = _split(M, n_A)
    if not is_symmetric_exact(M):
        raise ValueError("M must be symmetric")
    D_pd = is_positive_definite(D)
    D_psd = is_positive_semidefinite(D)
    M_psd = is_positive_semidefinite(M)

    note = ""
    rng: Optional[bool] = None
    if D_pd:
        S = schur_complement(M, n_A)
    elif D_psd:
        rng = range_inclusion_holds(M, n_A)
        S = shorted_complement(M, n_A)
        if not rng:
            note = ("D singular and ran(B^T) ⊄ ran(D): M cannot be PSD "
                    "(coupling leaks outside ran(D)).")
    else:
        # D not even PSD: M is not PSD (D is a principal submatrix of M).
        S = shorted_complement(M, n_A)
        note = ("D is not PSD, so M (which contains D as a principal block) "
                "is not PSD regardless of the complement -- this is exactly the "
                "A=(1), D=(-1), B=0 trap: complement = A > 0 but M indefinite.")

    S_psd = is_positive_semidefinite(S)

    # equivalence: under D >= 0 + range inclusion (or D > 0), M_psd <=> S_psd.
    if D_pd or (D_psd and rng):
        equivalence = (M_psd == S_psd)
    else:
        # hypothesis of the theorem not met; equivalence is not claimed
        equivalence = (M_psd is False)  # at least: M is correctly non-PSD

    neg = None if M_psd else negative_witness(M)
    return FiniteSchurCertificate(
        n_A=n_A, D_positive_definite=D_pd, D_positive_semidefinite=D_psd,
        range_inclusion=rng, schur=S, schur_psd=S_psd, M_psd=M_psd,
        equivalence_holds=equivalence, negative_vector=neg, note=note,
    )


def coupling_negative_vector(M: sp.Matrix, n_A: int, x: Sequence) -> sp.Matrix:
    """Given an x with <S x, x> < 0 (S the Schur complement, D > 0), return the
    exact full-space vector v = (x, -D^{-1} B^T x) realizing v^T M v = <S x, x> < 0.

    This is the "direct negative vector for the full quadratic form" that exposes
    a restricted/compressed positivity certificate as invalid (Gemini 1.1)."""
    A, B, D = _split(M, n_A)
    x = sp.Matrix(x)
    y = -D.inv() * B.T * x
    return sp.Matrix.vstack(x, y)


# --------------------------------------------------------------------------- #
# Gapped vs gapless (2.2) and uniform-limit obstructions (2.4)
# --------------------------------------------------------------------------- #
def inverse_decay_block(N: int) -> sp.Matrix:
    """D_N = diag(1, 1/2, ..., 1/N): every finite compression is strictly coercive
    (PD), yet inf spectrum -> 0, so NO uniform gap kappa I survives the limit.
    The canonical gapless witness (Gemini 1.8 / Part III 2.4)."""
    return sp.diag(*[Rat(1, k) for k in range(1, N + 1)])


def min_eigenvalue_exact(M: sp.Matrix) -> sp.Expr:
    """Exact least eigenvalue of a symmetric rational matrix (min charpoly root).

    For a diagonal matrix this is just the least diagonal entry; in general we use
    the real roots of the characteristic polynomial."""
    M = as_exact_matrix(M)
    S = (M + M.T) / 2
    if S.is_diagonal():
        return min(S[i, i] for i in range(S.rows))
    eigs = list(S.eigenvals().keys())   # exact algebraic eigenvalues
    # order real eigenvalues by numeric value (float used ONLY to order; a tiny
    # spurious imaginary part from radical evalf is chopped); return exact min.
    return min(eigs, key=lambda e: float(sp.re(e.evalf(chop=True))))


def certified_pd_margin(M: sp.Matrix) -> sp.Expr:
    """A certified EXACT rational lower bound r >= 0 on the least eigenvalue of
    the symmetric part of M: r > 0 with ``M - r I`` positive definite (verified by
    Sylvester, which is linear in the dimension -- unlike a full eigen-decomposition
    this stays cheap on large matrices). Returns 0 if M is not PD.

    A numeric eigenvalue only *guides* the choice of r; the returned r is verified
    exactly, so it is a genuine certificate of coercivity >= r."""
    M = as_exact_matrix(M)
    S = (M + M.T) / 2
    if not is_positive_definite(S):
        return sp.Integer(0)
    import numpy as np

    lam = float(np.linalg.eigvalsh(sp.matrix2numpy(S, dtype=float))[0])
    r = sp.Rational(lam * 9, 10).limit_denominator(10 ** 6) if lam > 0 else sp.Integer(0)
    I = sp.eye(S.rows)
    while r > 0 and not is_positive_definite(S - r * I):
        r = r / 2
    return r


def uniform_gap_profile(family, Ns: Sequence[int]) -> List[Tuple[int, sp.Expr]]:
    """For a block family N -> D_N, tabulate (N, least eigenvalue). A sequence
    tending to 0 proves the absence of a uniform spectral gap even when every
    entry is PD."""
    return [(N, min_eigenvalue_exact(family(N))) for N in Ns]


#: the four disjoint certificate verdicts (never collapse them to one bool)
CERT_VERIFIED = "VERIFIED"         # all mathematical obligations met -> M >= 0, source-identified
CERT_REFUTED = "REFUTED"           # an obligation definitely FAILS -> not a certificate
CERT_INAPPLICABLE = "INAPPLICABLE"  # math is fine but this is not a *source* certificate
CERT_UNKNOWN = "UNKNOWN"           # an obligation could not be decided


@dataclass
class RigidityDiagnostics:
    """INDEPENDENT rigidity obligations -- deliberately not a single score.

    A global positivity certificate requires *all* of the load-bearing ones; a
    surrogate that satisfies some while silently failing others (the recurrent
    Gemini error) is not a certificate. Each field is exact / typed; there is no
    `.score()`.

    The soundness fix (Proof Forge III, Part I.1): ``high_block_psd`` is now a
    first-class, load-bearing obligation. An invalid high block ``D`` must never
    receive a successful verdict merely because a low complement happened to be
    positive -- the exact trap ``M = diag(1, -1)`` (A=1, B=0, D=-1) has a
    positive shorted complement (A=1) and trivial range inclusion (B=0), yet
    ``e_2^T M e_2 = -1 < 0``. Without the high-block check that matrix was
    certified. It is now ``REFUTED``."""
    source_form_identified: bool        # is the form the genuine source, not a proxy?
    high_block_psd: Optional[bool]      # D >= 0 (load-bearing: D is a principal block of M)
    range_inclusion_ok: Optional[bool]  # ran(B^T) ⊆ ran(D) (None if D > 0, i.e. N/A)
    spectral_gap: Optional[sp.Expr]     # kappa > 0 if gapped, else None / 0
    inverse_response_sign: str          # 'positive' | 'negative' | 'indefinite'
    schur_complement_psd: Optional[bool]  # the TRUE (generalized) Schur complement >= 0
    sufficient_surrogate_psd: bool      # a conservative A - kappa^{-1} B B^T test (NOT a cert)
    m_psd: Optional[bool] = None        # ground-truth M >= 0 (cross-check; None if not computed)

    def certificate_status(self) -> str:
        """One of VERIFIED / REFUTED / INAPPLICABLE / UNKNOWN.

        The obligations, in order, for a genuine *source* positivity certificate
        on ``M = [[A, B], [B^T, D]]``:

        1. the high block is PSD (``D >= 0``) -- else M has a negative principal
           block and cannot be PSD;
        2. when ``D`` is singular, the coupling does not leak outside ``ran(D)``
           (range inclusion);
        3. the true generalized Schur complement is PSD;
        4. the source form is actually identified (a perfectly real positivity
           fact about a *proxy* form is INAPPLICABLE as a source certificate).

        An obligation that is explicitly ``None`` (undecided) yields UNKNOWN; a
        definitely-failed obligation yields REFUTED. The conservative surrogate
        plays NO role in this verdict."""
        # undecided obligations -> UNKNOWN (never a silent False/True)
        if self.high_block_psd is None or self.schur_complement_psd is None:
            return CERT_UNKNOWN
        # definite failures -> REFUTED
        if self.high_block_psd is False:
            return CERT_REFUTED
        if self.range_inclusion_ok is False:      # D singular and coupling leaks out
            return CERT_REFUTED
        if self.schur_complement_psd is False:
            return CERT_REFUTED
        # math holds; is it a *source* certificate?
        if not self.source_form_identified:
            return CERT_INAPPLICABLE
        return CERT_VERIFIED

    def is_genuine_certificate(self) -> bool:
        """True iff :meth:`certificate_status` is VERIFIED. This now requires the
        high block ``D >= 0`` and (when D is singular) range inclusion, in
        addition to the true Schur complement being PSD and the source form being
        identified. The conservative surrogate is neither necessary nor
        sufficient and is NOT part of the conjunction."""
        return self.certificate_status() == CERT_VERIFIED

    def as_record(self) -> dict:
        return {
            "source_form_identified": self.source_form_identified,
            "high_block_psd": self.high_block_psd,
            "range_inclusion_ok": self.range_inclusion_ok,
            "spectral_gap": None if self.spectral_gap is None else str(self.spectral_gap),
            "inverse_response_sign": self.inverse_response_sign,
            "schur_complement_psd": self.schur_complement_psd,
            "sufficient_surrogate_psd": self.sufficient_surrogate_psd,
            "m_psd": self.m_psd,
            "certificate_status": self.certificate_status(),
            "is_genuine_certificate": self.is_genuine_certificate(),
        }


def conservative_surrogate(M: sp.Matrix, n_A: int, kappa: sp.Expr) -> sp.Matrix:
    """A - kappa^{-1} B B^T: the "restricted coercivity" surrogate. When D >= kappa I
    this is a LOWER bound for the Schur complement (A - B D^{-1} B^T >= A - kappa^{-1} B B^T),
    hence SUFFICIENT for positivity -- but its failure is NOT a negative witness
    (Gemini 1.2) and it is invalid unless D >= kappa I actually holds on the
    coupling range (Gemini 1.1)."""
    A, B, D = _split(M, n_A)
    return sp.simplify(A - (B * B.T) / kappa)


def diagnostics_from_block(M: sp.Matrix, n_A: int, *,
                           source_form_identified: bool,
                           kappa: Optional[sp.Expr] = None) -> RigidityDiagnostics:
    A, B, D = _split(M, n_A)
    D_pd = is_positive_definite(D)
    D_psd = True if D_pd else is_positive_semidefinite(D)
    gap = min_eigenvalue_exact(D) if D_pd else (0 if D_psd else None)
    rng = None if D_pd else range_inclusion_holds(M, n_A)
    if D_pd:
        S = schur_complement(M, n_A)
    else:
        S = shorted_complement(M, n_A)
    schur_psd = is_positive_semidefinite(S)
    if schur_psd:
        sign = "positive"
    elif is_positive_semidefinite(-S):
        sign = "negative"
    else:
        sign = "indefinite"
    surrogate_psd = False
    if kappa is not None:
        surrogate_psd = is_positive_semidefinite(conservative_surrogate(M, n_A, kappa))
    return RigidityDiagnostics(
        source_form_identified=source_form_identified,
        high_block_psd=D_psd,
        range_inclusion_ok=rng,
        spectral_gap=(gap if (gap is not None and gap > 0) else None),
        inverse_response_sign=sign,
        schur_complement_psd=schur_psd,
        sufficient_surrogate_psd=surrogate_psd,
        m_psd=is_positive_semidefinite(M),
    )


# --------------------------------------------------------------------------- #
# Form-core positivity transport (2.3): the negative control
# --------------------------------------------------------------------------- #
@dataclass
class FormCoreNegativeControl:
    N: int
    a_squared: sp.Expr
    test_gram_pd: bool            # q >= 0 (in fact > 0) on the test subspace
    test_gram_coercivity_lb: sp.Expr  # certified exact rational LOWER BOUND on the
                                  # least eigenvalue (not the exact least eigenvalue)
    global_negative_value: sp.Expr  # q[e_1] < 0  (missed by the test subspace)
    threshold_a_squared: sp.Expr  # the PD/indefinite threshold for a^2 at this N

    def as_record(self) -> dict:
        return {
            "N": self.N,
            "a_squared": str(self.a_squared),
            "test_gram_pd": self.test_gram_pd,
            "test_gram_coercivity_lb": str(self.test_gram_coercivity_lb),
            "global_negative_value": str(self.global_negative_value),
            "threshold_a_squared": str(self.threshold_a_squared),
        }


def form_core_negative_control(N: int, a_squared: Optional[sp.Expr] = None,
                               neg_weight: sp.Expr = Rat(9)) -> FormCoreNegativeControl:
    """An EXACT finite witness that L^2-density does NOT suffice for positivity
    transport -- a true *form core* is required (Part III 2.3).

    Model (truncation of an unbounded indefinite form on l^2):
        coordinate 1 carries weight ``-neg_weight`` (so q[e_1] = -neg_weight < 0);
        coordinates 2..N carry weight n^2;
        the test subspace is ker(phi), phi(f) = f_1 - a * sum_{n=2}^N f_n, with
        a a fixed coefficient (bounded; a^2 stays below the PD threshold, which
        tends to 1/(9(pi^2/6 - 1))). It is the FUNCTIONAL NORM ||phi|| = a*sqrt(N-1)
        that grows without bound as N->infinity, making phi discontinuous in the
        limit, so ker(phi) is L^2-dense yet its form-closure misses e_1.

    On the test subspace, with basis w_j = e_j + a e_1 (j = 2..N), the restricted
    form has Gram  G = diag(j^2) - neg_weight * a^2 * 1 1^T. This is PD iff
    ``neg_weight * a^2 < 1 / sum_{j=2}^N 1/j^2``. We pick a^2 strictly below the
    threshold: q > 0 on the (L^2-dense) test subspace for every finite N, while the
    global form has q[e_1] = -neg_weight < 0. Hence "q >= 0 on an L^2-dense set"
    does NOT certify "q >= 0", and the certifying set must be a form core."""
    js = list(range(2, N + 1))
    inv_sq_sum = sum(Rat(1, j * j) for j in js)           # sum_{2}^{N} 1/j^2
    threshold = Rat(1) / (neg_weight * inv_sq_sum)         # a^2 threshold for PD
    if a_squared is None:
        a_squared = threshold / 2                          # strictly PD, exact
    a2 = sp.nsimplify(a_squared)
    Dp = sp.diag(*[Rat(j * j) for j in js])
    ones = sp.ones(len(js), 1)
    G = Dp - neg_weight * a2 * (ones * ones.T)
    pd = is_positive_definite(G)
    return FormCoreNegativeControl(
        N=N, a_squared=a2, test_gram_pd=pd,
        test_gram_coercivity_lb=certified_pd_margin(G),  # certified exact lower bound
        global_negative_value=-neg_weight,
        threshold_a_squared=threshold,
    )
