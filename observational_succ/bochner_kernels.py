"""Bochner / Schoenberg negative-type kernels  (Operation Rigidity Forge, Part VI).

For an even function ``Psi`` with ``Psi(0) = 0`` this module studies the kernel

    K_Psi(s, t) = Psi(s) + Psi(t) - Psi(s - t).

The point of the module is the *classical* Schoenberg relationship and, just as
important, the four SEPARATE predicates that it is forbidden to conflate:

    (i)   a FINITE positive-semidefinite (PSD) matrix              -- one Gram, one node set
    (ii)  a GLOBALLY positive-(semi)definite kernel               -- PSD on *every* finite set
    (iii) a POSITIVE spectral / Levy-Khintchine measure           -- the representing measure
    (iv)  an actually source-IDENTIFIED signed Weil kernel         -- a genuine arithmetic object

Only (i) is decidable by finite exact arithmetic. (ii) needs a feature
factorisation / the conditional-negative-definite (CND) characterisation; a
single failing finite Gram refutes it, but no finite family of successes proves
it. (iii) is the Bochner / Levy-Khintchine side: the representing measure. (iv)
is the firewall: a generic even ``Psi`` with ``Psi(0)=0`` is NOT an arithmetic
source, carries no Gamma factor, no prime/pole structure, no half-density and no
conductor/phase, so there is NO valid map to the authentic signed Weil form.
This module exhibits a kernel (``1 - cos``) that passes (i), (ii), (iii)
cleanly and FAILS (iv) -- a reusable NEGATIVE CONTROL for SUCC's
source-to-Weil firewall. RH stays OPEN.

Sign-convention bridge to the repo
----------------------------------
``observational_succ.one_object_kernel_certificates`` works with
``K_g(x, y) = g(x - y) - g(x) - g(-y) + g(0)``. For an even ``g`` with
``g(0) = 0`` this is exactly ``-K_g_here = -(g(x)+g(y)-g(x-y)) = -K_Psi`` with
``Psi = g``. So the authentic SUCC Weil kernel and the Bochner kernel here are
the same algebraic family up to an overall sign; the *only* thing the authentic
module has and this one does not is a SOURCE. That difference is the whole point.

Exactness discipline
--------------------
Every certificate is exact (sympy ``Rational`` / symbolic, with sign decided by
``.is_nonnegative`` or by an exact rational comparison). A float is NEVER a
certificate: ``_exact`` rejects Python floats outright. Numerical values, if any
appear, are labelled illustrative.

Status vocabulary: CLASSICAL / PROVED LOCAL / TESTED MODEL / HYPOTHESIS /
CONJECTURED / UNVERIFIED / REFUTED  (AGENTS.md / proof_contracts).
"""
from __future__ import annotations

from fractions import Fraction
from typing import Callable, Dict, List, Sequence, Tuple

import sympy as sp

from .proof_contracts import ProofContract, Quantifier, _VALID_STATUS

CLASSICAL = "CLASSICAL"
PROVED_LOCAL = "PROVED LOCAL"
REFUTED = "REFUTED"

assert {CLASSICAL, PROVED_LOCAL, REFUTED} <= _VALID_STATUS


class BochnerKernelError(ValueError):
    """Raised on a firewall or exactness violation."""


# --------------------------------------------------------------------------- #
# Exact helpers                                                               #
# --------------------------------------------------------------------------- #
def _exact(x) -> sp.Expr:
    """Coerce to an EXACT sympy object. Reject Python floats (firewall).

    int / Fraction / sympy are accepted; a ``float`` is a non-certificate and is
    refused so a rounded value can never masquerade as an exact one.
    """
    if isinstance(x, float):
        raise BochnerKernelError(
            f"float {x!r} is not an exact value; floats are illustrative only, "
            "never certificates"
        )
    if isinstance(x, Fraction):
        return sp.Rational(x.numerator, x.denominator)
    if isinstance(x, int):
        return sp.Integer(x)
    return sp.sympify(x)


def _to_matrix(M) -> sp.Matrix:
    if isinstance(M, sp.MatrixBase):
        return sp.Matrix(M)
    return sp.Matrix([[_exact(v) for v in row] for row in M])


def _is_symmetric_exact(M: sp.Matrix) -> bool:
    n, m = M.shape
    if n != m:
        return False
    return all(sp.simplify(M[i, j] - M[j, i]) == 0 for i in range(n) for j in range(i + 1, n))


def _sign_nonnegative(expr: sp.Expr) -> bool:
    """Exact 'expr >= 0'. Raise if the sign cannot be decided exactly."""
    s = sp.simplify(expr)
    nn = s.is_nonnegative
    if nn is None:
        raise BochnerKernelError(
            f"cannot decide the sign of {s!r} exactly; refusing to guess"
        )
    return bool(nn)


def _sign_positive(expr: sp.Expr) -> bool:
    s = sp.simplify(expr)
    pos = s.is_positive
    if pos is None:
        raise BochnerKernelError(
            f"cannot decide strict positivity of {s!r} exactly; refusing to guess"
        )
    return bool(pos)


# --------------------------------------------------------------------------- #
# Core kernel + exact PSD test                                                #
# --------------------------------------------------------------------------- #
def kernel_gram(Psi: Callable, nodes: Sequence) -> sp.Matrix:
    """Exact Gram of ``K_Psi(s, t) = Psi(s) + Psi(t) - Psi(s - t)`` on ``nodes``.

    ``Psi`` must return an exact (sympy / int / Fraction) value. ``nodes`` may be
    ints, ``Fraction``s or sympy expressions (e.g. ``sympy.pi/3``). The result is
    an exact sympy ``Matrix``; it is symmetric because ``Psi`` is intended to be
    even (``Psi(s-t) = Psi(t-s)``) -- symmetry is asserted downstream, not here.
    """
    xs = [_exact(x) for x in nodes]
    n = len(xs)

    def psi(v):
        return _exact(Psi(v))

    pv = [psi(x) for x in xs]
    G = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            G[i, j] = sp.simplify(pv[i] + pv[j] - psi(xs[i] - xs[j]))
    return G


def leading_principal_minors(M) -> List[sp.Expr]:
    """Exact leading principal minors D_1, ..., D_n (Sylvester data)."""
    M = _to_matrix(M)
    n = M.shape[0]
    return [sp.simplify(M[:k, :k].det()) for k in range(1, n + 1)]


def is_positive_definite_exact(M) -> bool:
    """Sylvester's criterion: PD iff every leading principal minor is > 0.

    This is the strict positive-DEFINITE test. It does NOT test PSD: e.g.
    ``[[0,0],[0,-1]]`` has leading minors 0, 0, which Sylvester cannot reject,
    yet the matrix is indefinite. Use ``is_psd_exact`` for semidefiniteness.
    """
    M = _to_matrix(M)
    if not _is_symmetric_exact(M):
        raise BochnerKernelError("PD test requires a symmetric matrix")
    return all(_sign_positive(d) for d in leading_principal_minors(M))


def characteristic_coefficients(M) -> List[sp.Expr]:
    """Coefficients of det(lam*I - M) in descending powers (monic, length n+1)."""
    M = _to_matrix(M)
    lam = sp.Symbol("_lam")
    return list(M.charpoly(lam).all_coeffs())


def is_psd_exact(M) -> bool:
    """Exact positive-SEMIdefinite test for a symmetric matrix.

    A real symmetric matrix has only real eigenvalues, so it is PSD iff the
    characteristic polynomial ``p(lam) = det(lam*I - M) = lam^n + a_{n-1} lam^{n-1}
    + ... + a_0`` has no negative root. For a real-rooted monic polynomial this
    holds iff ``(-1)^k a_{n-k} >= 0`` for every ``k`` (the k-th elementary
    symmetric function of the eigenvalues is nonnegative). This is a genuine PSD
    criterion -- unlike leading principal minors, which only test PD -- and it is
    exact (rational coefficients give decidable signs; surd coefficients are
    decided by ``is_nonnegative``).
    """
    M = _to_matrix(M)
    if not _is_symmetric_exact(M):
        raise BochnerKernelError("PSD test requires a symmetric matrix")
    coeffs = characteristic_coefficients(M)  # [1, a_{n-1}, ..., a_0]
    n = M.shape[0]
    for k in range(1, n + 1):
        if not _sign_nonnegative((-1) ** k * coeffs[k]):
            return False
    return True


# --------------------------------------------------------------------------- #
# NEGATIVE benchmark: Psi(t) = t^4                                            #
# --------------------------------------------------------------------------- #
def t4_negative_benchmark() -> Dict:
    """``Psi(t)=t^4`` on nodes {-1, 1}: Gram [[2,-14],[-14,2]], det -192 < 0.

    Confirms NOT PSD, hence ``t^4`` is NOT conditionally negative definite and
    the kernel fails. Everything exact.
    """
    Psi = lambda t: t ** 4
    G = kernel_gram(Psi, [-1, 1])
    det = sp.simplify(G.det())
    expected = sp.Matrix([[2, -14], [-14, 2]])
    if sp.simplify(G - expected) != sp.zeros(2, 2):
        raise BochnerKernelError(f"t^4 Gram mismatch: {G}")
    if det != -192:
        raise BochnerKernelError(f"t^4 determinant mismatch: {det}")
    return {
        "Psi": "t^4",
        "nodes": (-1, 1),
        "gram": G,
        "determinant": det,
        "is_psd": is_psd_exact(G),       # -> False
        "eigen_sign_certificate": "charpoly lam^2 - 4 lam - 192; root -12 < 0",
        "conditionally_negative_definite": False,
        "status": REFUTED,               # t^4 is refuted as CND / negative-type
        "RH_proved": False,
    }


# --------------------------------------------------------------------------- #
# POSITIVE benchmark: Psi(t) = 1 - cos t  (explicit feature factorisation)     #
# --------------------------------------------------------------------------- #
def one_minus_cos_feature(t) -> sp.Matrix:
    """Feature map phi(t) = (1 - cos t, sin t) in R^2 realising K_Psi as a Gram.

    1 - cos(s-t) = 1 - cos s cos t - sin s sin t, so
        K_Psi(s,t) = (1-cos s) + (1-cos t) - (1 - cos(s-t))
                   = (1-cos s)(1-cos t) + sin s sin t
                   = < phi(s), phi(t) >.
    """
    t = _exact(t)
    return sp.Matrix([1 - sp.cos(t), sp.sin(t)])


def verify_one_minus_cos_identity() -> bool:
    """Symbolic proof that K_Psi(s,t) == <phi(s),phi(t)> for ALL s,t.

    This is the certificate that ``1 - cos`` gives a GLOBALLY PSD kernel: a Gram
    of inner products of real feature vectors is PSD on every node set.
    """
    s, t = sp.symbols("s t", real=True)
    Psi = lambda x: 1 - sp.cos(x)
    lhs = Psi(s) + Psi(t) - Psi(s - t)
    phi_s, phi_t = one_minus_cos_feature(s), one_minus_cos_feature(t)
    rhs = (phi_s.T * phi_t)[0, 0]
    return sp.simplify(lhs - rhs) == 0


def one_minus_cos_gram_from_circle_points(points: Sequence[Tuple]) -> sp.Matrix:
    """Exact RATIONAL (1-cos) Gram from rational unit-circle points.

    Each ``point = (a, b)`` is a *node* identified by its position on the unit
    circle, ``a = cos(theta)``, ``b = sin(theta)`` with ``a^2 + b^2 = 1``. Then
    ``Psi(theta_i) = 1 - a_i`` and ``cos(theta_i - theta_j) = a_i a_j + b_i b_j``,
    so every Gram entry ``(1-a_i)(1-a_j) + b_i b_j`` is exactly rational -- no
    transcendental evaluation, a fully rigorous finite certificate.
    """
    pts = []
    for a, b in points:
        a, b = _exact(a), _exact(b)
        if sp.simplify(a ** 2 + b ** 2 - 1) != 0:
            raise BochnerKernelError(f"({a},{b}) is not on the unit circle")
        pts.append((a, b))
    n = len(pts)
    G = sp.zeros(n, n)
    for i in range(n):
        ai, bi = pts[i]
        for j in range(n):
            aj, bj = pts[j]
            G[i, j] = sp.simplify((1 - ai) * (1 - aj) + bi * bj)
    return G


# A few Pythagorean-style rational points on the unit circle (a^2 + b^2 = 1).
RATIONAL_CIRCLE_POINTS: Tuple[Tuple, ...] = (
    (sp.Integer(1), sp.Integer(0)),
    (sp.Rational(3, 5), sp.Rational(4, 5)),
    (sp.Rational(5, 13), sp.Rational(12, 13)),
    (sp.Rational(8, 17), sp.Rational(15, 17)),
    (sp.Rational(20, 29), sp.Rational(21, 29)),
    (sp.Rational(-3, 5), sp.Rational(4, 5)),
    (sp.Rational(-7, 25), sp.Rational(24, 25)),
)


def one_minus_cos_positive_benchmark() -> Dict:
    """``Psi(t)=1-cos t``: global-PSD certificate + several exact rational Grams."""
    identity_ok = verify_one_minus_cos_identity()
    grams = []
    for k in range(2, len(RATIONAL_CIRCLE_POINTS) + 1):
        pts = RATIONAL_CIRCLE_POINTS[:k]
        G = one_minus_cos_gram_from_circle_points(pts)
        # Cross-check: G must equal Phi Phi^T, Phi rows = phi(point).
        Phi = sp.Matrix([[1 - a, b] for a, b in pts])
        gram_is_feature_gram = sp.simplify(G - Phi * Phi.T) == sp.zeros(k, k)
        grams.append(
            {
                "num_nodes": k,
                "is_psd": is_psd_exact(G),              # -> True
                "equals_feature_gram": gram_is_feature_gram,
            }
        )
    return {
        "Psi": "1 - cos t",
        "feature_map": "phi(t) = (1 - cos t, sin t)",
        "symbolic_identity_K_equals_inner_product": identity_ok,  # -> True (all s,t)
        "global_psd": identity_ok,
        "rational_point_grams": grams,
        "conditionally_negative_definite": True,
        "status": PROVED_LOCAL,
        "RH_proved": False,
    }


# --------------------------------------------------------------------------- #
# Levy-Khintchine representation check (predicate iii)                        #
# --------------------------------------------------------------------------- #
def levy_khintchine_verify(Psi: Callable, c, atoms: Sequence[Tuple]) -> bool:
    """Verify Psi(x) = c*x^2 + sum_a mass_a * (1 - cos(u_a * x)) symbolically.

    ``c >= 0`` and every ``mass_a >= 0`` (positivity of the spectral / Levy
    measure) are checked exactly; the functional identity is checked symbolically
    for a free real ``x``. Returns True iff a genuine positive-measure
    representation holds.
    """
    x = sp.Symbol("x", real=True)
    c = _exact(c)
    if not _sign_nonnegative(c):
        return False
    expr = c * x ** 2
    for u, mass in atoms:
        u, mass = _exact(u), _exact(mass)
        if not _sign_nonnegative(mass):
            return False
        expr += mass * (1 - sp.cos(u * x))
    return sp.simplify(expr - _exact(Psi(x))) == 0


def levy_khintchine_benchmarks() -> Dict:
    """Exact positive-measure representations for 1-cos and t^2; none for t^4."""
    one_minus_cos_ok = levy_khintchine_verify(lambda x: 1 - sp.cos(x), 0, [(1, 1)])
    t2_ok = levy_khintchine_verify(lambda x: x ** 2, 1, [])
    # t^4 has NO positive-measure representation: such a representation would make
    # t^4 conditionally negative definite, but the {-1,1} Gram det = -192 < 0
    # refutes CND. We therefore record the obstruction, we do not fabricate atoms.
    t4 = t4_negative_benchmark()
    return {
        "one_minus_cos": {
            "c": 0,
            "levy_measure": "nu = delta_1  (unit point mass at u=1; symmetric 1/2(d_1+d_-1) equivalently)",
            "positive_measure": one_minus_cos_ok,   # -> True
            "status": CLASSICAL,
        },
        "t_squared": {
            "c": 1,
            "levy_measure": "nu = 0  (pure Gaussian / Brownian local term c*x^2)",
            "positive_measure": t2_ok,              # -> True
            "status": CLASSICAL,
        },
        "t_fourth": {
            "positive_measure": False,
            "obstruction": "would force CND; {-1,1} Gram det -192 < 0 refutes it",
            "finite_witness_det": t4["determinant"],
            "status": REFUTED,
        },
    }


# --------------------------------------------------------------------------- #
# Schoenberg polarisation identity (the exact intermediate lemma)             #
# --------------------------------------------------------------------------- #
def schoenberg_polarization_check(Psi: Callable, nodes: Sequence, coeffs: Sequence) -> Dict:
    """Exact check of the polarisation identity that drives Schoenberg's theorem.

        sum_ij c_i c_j K_Psi(t_i,t_j)
          = 2 (sum_i c_i)(sum_j c_j Psi(t_j)) - sum_ij c_i c_j Psi(t_i - t_j).

    On the hyperplane ``sum_i c_i = 0`` the first term vanishes, so the quadratic
    form of ``K_Psi`` equals ``- sum_ij c_i c_j Psi(t_i - t_j)``; thus ``K_Psi``
    PSD on {sum c_i = 0} <=> ``Psi(.-.)`` conditionally negative definite. This
    is the engine of the equivalence (i)<->(ii), verified here as an EXACT
    algebraic identity (no analysis, no limits).
    """
    xs = [_exact(x) for x in nodes]
    cs = [_exact(c) for c in coeffs]
    n = len(xs)
    psi = lambda v: _exact(Psi(v))
    G = kernel_gram(Psi, xs)
    quad = sp.simplify(sum(cs[i] * cs[j] * G[i, j] for i in range(n) for j in range(n)))
    sum_c = sp.simplify(sum(cs))
    sum_cpsi = sp.simplify(sum(cs[i] * psi(xs[i]) for i in range(n)))
    diff_form = sp.simplify(sum(cs[i] * cs[j] * psi(xs[i] - xs[j]) for i in range(n) for j in range(n)))
    rhs = sp.simplify(2 * sum_c * sum_cpsi - diff_form)
    on_hyperplane = sum_c == 0
    return {
        "identity_holds": sp.simplify(quad - rhs) == 0,
        "quadratic_form": quad,
        "sum_of_coeffs": sum_c,
        "on_zero_sum_hyperplane": on_hyperplane,
        "equals_minus_diff_form_on_hyperplane": (sp.simplify(quad + diff_form) == 0) if on_hyperplane else None,
    }


# --------------------------------------------------------------------------- #
# The four SEPARATE certified spectral predicates (i)-(iv)                     #
# --------------------------------------------------------------------------- #
def four_way_spectral_report(name: str) -> Dict:
    """Report the four SEPARATE predicates for a named benchmark kernel.

    (i)   finite_psd            : is SOME explicit finite Gram PSD? (decidable, exact)
    (ii)  global_pd_kernel      : PSD on EVERY finite node set? (feature map / CND; not finitary)
    (iii) positive_spectral_measure : positive Levy-Khintchine measure? (Bochner side)
    (iv)  source_identified_signed_weil : an authentic arithmetic source map? (ALWAYS None here)

    (iv) is the firewall. For a generic even Psi with Psi(0)=0 there is NO Gamma
    factor, NO prime/pole structure, NO half-density, NO conductor/phase and NO
    source, hence NO valid map to the completed signed Weil form. We RECORD the
    absence; we do not paper a gap. (i)/(ii)/(iii) holding tells us NOTHING about
    RH.
    """
    if name == "1 - cos t":
        pos = one_minus_cos_positive_benchmark()
        lk = levy_khintchine_benchmarks()["one_minus_cos"]
        finite_psd = pos["rational_point_grams"][0]["is_psd"]
        global_pd = pos["global_psd"]
        pos_measure = lk["positive_measure"]
    elif name == "t^4":
        neg = t4_negative_benchmark()
        finite_psd = neg["is_psd"]            # False, witness {-1,1}
        global_pd = False                      # refuted by the same witness
        pos_measure = levy_khintchine_benchmarks()["t_fourth"]["positive_measure"]
    else:
        raise BochnerKernelError(f"unknown benchmark {name!r}")

    return {
        "kernel": f"K_Psi, Psi = {name}",
        "i_finite_psd": finite_psd,
        "ii_global_pd_kernel": global_pd,
        "iii_positive_spectral_measure": pos_measure,
        "iv_source_identified_signed_weil": None,   # NOT identified -- recorded failure
        "iv_reason": (
            "generic even Psi with Psi(0)=0 is not an arithmetic source: no "
            "Gamma factor, no prime/pole term, no half-density, no conductor/"
            "phase. No derived map to the completed signed Weil distribution "
            "exists. This is a BOUNDARY, not a gap to be papered over."
        ),
        "negative_control": name == "1 - cos t",
        "sign_bridge_to_repo": (
            "K_Psi = -K_g of one_object_kernel_certificates (g=Psi, even, g(0)=0); "
            "same algebraic family, but THAT module carries an exact SHA-pinned "
            "source and this one carries none."
        ),
        "RH_proved": False,
        "Weil_PSD_proved": False,
        "source_authentic": False,
    }


# --------------------------------------------------------------------------- #
# Proof contract for the classical theorem                                    #
# --------------------------------------------------------------------------- #
def schoenberg_contract() -> ProofContract:
    """The classical Schoenberg / Levy-Khintchine theorem as a proof contract.

    Status CLASSICAL, ``source_authentic=False``: the theorem is about a generic
    function, not about an arithmetic source, and the open obligation records
    that no map to the authentic signed Weil form is supplied.
    """
    return ProofContract(
        name="schoenberg_negative_type",
        statement=(
            "For even Psi: R->R with Psi(0)=0 and K_Psi(s,t)=Psi(s)+Psi(t)-Psi(s-t): "
            "(a) K_Psi is PSD on every finite node set  <=>  "
            "(b) (s,t)|->Psi(s-t) is conditionally negative definite  <=>  "
            "(c) [Psi additionally continuous] Psi(x)=c*x^2 + integral (1-cos(x u)) dnu(u), "
            "c>=0, nu>=0 a symmetric Levy measure with integral min(1,u^2) dnu < infinity."
        ),
        prefix=[
            Quantifier("forall", "Psi", "even real functions with Psi(0)=0"),
            Quantifier("forall", "F", "finite node multisets in R"),
            Quantifier("forall", "c", "R^|F|", depends_on=("F",)),
        ],
        hypotheses=[
            "Psi even and real with Psi(0)=0",
            "(a)<=>(b): pure finite linear algebra; NO continuity needed",
            "(b)<=>(c): additionally requires Psi continuous",
        ],
        constant_dependencies={"c": ["F"]},
        finite_to_infinite=(
            "The direction 'finite PSD Grams => global/CND/measure' is NOT finitary: "
            "no finite family of PSD Grams licenses (ii) or (iii); the integral "
            "representation (c) further needs continuity. A single failing Gram, "
            "however, refutes (ii)."
        ),
        source_authentic=False,
        method="classical Schoenberg (1938); Levy-Khintchine representation",
        status=CLASSICAL,
        open_obligations=[
            "NO map from K_Psi to the authentic source-identified signed Weil form "
            "(iv) is supplied or claimed; recorded as a boundary.",
            "RH remains OPEN.",
        ],
    )


def summary() -> Dict:
    """One-call rollup of every certificate (exact)."""
    return {
        "contract": schoenberg_contract().as_record(),
        "negative_benchmark_t4": t4_negative_benchmark(),
        "positive_benchmark_1_minus_cos": one_minus_cos_positive_benchmark(),
        "levy_khintchine": levy_khintchine_benchmarks(),
        "four_way_1_minus_cos": four_way_spectral_report("1 - cos t"),
        "four_way_t4": four_way_spectral_report("t^4"),
    }
