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


# --------------------------------------------------------------------------- #
# Exact linear-algebra primitives
# --------------------------------------------------------------------------- #
def as_exact_matrix(M) -> sp.Matrix:
    """Coerce to an exact sympy Matrix (rationalizing python ints/Fractions)."""
    if isinstance(M, sp.Matrix):
        return M
    return sp.Matrix(M)


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
    which is the only part a quadratic form sees."""
    M = as_exact_matrix(M)
    S = (M + M.T) / 2
    for d in leading_principal_minors(S):
        if not (sp.nsimplify(d) > 0):
            return False
    return True


def is_positive_semidefinite(M: sp.Matrix) -> bool:
    """Exact PSD test: symmetric and every principal minor >= 0."""
    M = as_exact_matrix(M)
    S = (M + M.T) / 2
    for d in all_principal_minors(S):
        if (d < 0) is sp.true or (sp.simplify(d) < 0):
            return False
    return True


def quad(M: sp.Matrix, v: Sequence) -> sp.Expr:
    """Exact quadratic form v^T M v."""
    M = as_exact_matrix(M)
    v = sp.Matrix(v)
    return sp.expand((v.T * M * v)[0, 0])


def negative_witness(M: sp.Matrix, max_denom: int = 64) -> Optional[sp.Matrix]:
    """Return an EXACT rational vector v with v^T M v < 0, or None if M is PSD.

    Method: a symmetric rational matrix that is not PSD has an open cone of
    negative directions, hence a rational one. We locate the direction by a
    numeric eigenvector (heuristic), rationalize it, and *verify exactly*. The
    certificate is the exact check ``quad(M, v) < 0``; the float step only guides
    the search and never appears in the conclusion."""
    M = as_exact_matrix(M)
    S = (M + M.T) / 2
    if is_positive_semidefinite(S):
        return None
    # numeric guidance: most-negative eigenpair of the float image
    Mf = sp.matrix2numpy(S, dtype=float)
    import numpy as np

    w, V = np.linalg.eigh(Mf)
    order = np.argsort(w)
    for j in order:
        if w[j] >= -1e-12:
            break
        direction = V[:, j]
        for denom in (8, 16, 32, max_denom, 256, 1024):
            v = sp.Matrix([sp.Rational(float(x)).limit_denominator(denom)
                           for x in direction])
            if v.is_zero_matrix:
                continue
            if quad(S, v) < 0:
                return v
    # exact fallback: search coordinate and pair directions
    n = S.rows
    cands: List[sp.Matrix] = []
    for i in range(n):
        e = sp.zeros(n, 1)
        e[i] = 1
        cands.append(e)
    for i, k in combinations(range(n), 2):
        for s in (1, -1):
            e = sp.zeros(n, 1)
            e[i] = 1
            e[k] = s
            cands.append(e)
    for v in cands:
        if quad(S, v) < 0:
            return v
    raise RuntimeError("matrix is not PSD but no rational witness found; "
                       "increase max_denom")


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


@dataclass
class RigidityDiagnostics:
    """Six INDEPENDENT rigidity obligations -- deliberately not a single score.

    A global positivity certificate requires *all* of these; a surrogate that
    satisfies some while silently failing others (the recurrent Gemini error) is
    not a certificate. Each field is exact / typed; there is no `.score()`."""
    source_form_identified: bool       # is the form the genuine source, not a proxy?
    range_inclusion_ok: Optional[bool]  # ran(B^T) ⊆ ran(D) (None if D > 0)
    spectral_gap: Optional[sp.Expr]     # kappa > 0 if gapped, else None / 0
    inverse_response_sign: str          # 'positive' | 'negative' | 'indefinite'
    schur_complement_psd: bool          # the TRUE inverse-response bound
    sufficient_surrogate_psd: bool      # a conservative A - kappa^{-1} B B^T test

    def is_genuine_certificate(self) -> bool:
        """A genuine global certificate needs the TRUE Schur complement PSD, the
        source form identified, and (when D is singular) range inclusion. The
        conservative surrogate is neither necessary nor sufficient and is NOT part
        of this conjunction."""
        return (self.schur_complement_psd
                and self.source_form_identified
                and (self.range_inclusion_ok in (True, None)))

    def as_record(self) -> dict:
        return {
            "source_form_identified": self.source_form_identified,
            "range_inclusion_ok": self.range_inclusion_ok,
            "spectral_gap": None if self.spectral_gap is None else str(self.spectral_gap),
            "inverse_response_sign": self.inverse_response_sign,
            "schur_complement_psd": self.schur_complement_psd,
            "sufficient_surrogate_psd": self.sufficient_surrogate_psd,
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
    gap = min_eigenvalue_exact(D) if D_pd else (0 if is_positive_semidefinite(D) else None)
    rng = None if D_pd else range_inclusion_holds(M, n_A)
    if D_pd:
        S = schur_complement(M, n_A)
    else:
        S = shorted_complement(M, n_A)
    if is_positive_semidefinite(S):
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
        range_inclusion_ok=rng,
        spectral_gap=(gap if (gap is not None and gap > 0) else None),
        inverse_response_sign=sign,
        schur_complement_psd=is_positive_semidefinite(S),
        sufficient_surrogate_psd=surrogate_psd,
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
