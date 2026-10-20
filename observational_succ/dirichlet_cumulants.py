"""Formal Dirichlet cumulants and the multiplicativity characterization
(Operation Rigidity Forge, Part V -- Deliverable D).

This module develops the *formal* Dirichlet-convolution logarithm as a cumulant
generator and proves/tests the structural characterization of multiplicativity
that it encodes. The convolution throughout is the Dirichlet / multiplicative one

    (f *x g)(n) = sum_{d | n} f(d) g(n/d),

with identity ``delta`` (``delta(1) = 1``, else ``0``). This is the SAME
operation as :func:`observational_succ.arithmetic_interactions.dirichlet_convolution`;
here we work with 1-indexed exact coefficient arrays so convolution *powers* are
cheap, and we cross-check against the existing
:func:`observational_succ.dirichlet_lambert.star_log_unit` (an independent
implementation of the same formal log).

Core object
-----------
For an arithmetic function ``a`` with ``a(1) = 1`` put ``h = a - delta`` (so
``h(1) = 0``). The **formal Dirichlet logarithm** is

    b = log_* a = sum_{k >= 1} (-1)^(k+1) / k * h^{*k}.

On a fixed ``n`` only the terms with ``2^k <= n`` contribute (every factor in a
``k``-fold Dirichlet convolution of ``h`` is ``>= 2`` because ``h(1) = 0``), so
``k <= floor(log2 n)`` and the sum is a *finite*, exact rational (or symbolic)
combination of the values ``a(d)``, ``d | n``. There is **no convergence
question** for the formal object: it is pure algebra in the completed Dirichlet
ring. We call ``b(n)`` the *n-th formal Dirichlet cumulant* of ``a``; the mixed
ones ``b(pq)``, ``b(pqr)``, ... are the connected mixed-prime correlations, in
exact analogy with log of a moment generating function being the cumulant
generating function. (The moment/cumulant wording is an analogy, not a theorem.)

What is proved here (all FORMAL, status CLASSICAL -- standard formal
Dirichlet-algebra theory; the SUCC contribution is the exact, tested
implementation):

1.  First mixed cumulant identity: for distinct primes ``p, q``,
        b(pq) = a(pq) - a(p) a(q).
2.  Characterization theorem:
        a is multiplicative  <=>  b(n) = 0 for every n with at least two
        distinct prime factors (i.e. b is supported on prime powers).
    with the prime-power support decomposition ``b = sum_p log_*(a_p)`` and the
    converse. Completely multiplicative sources satisfy the stronger
    ``b(p^k) = a(p)^k / k``.
3.  Formal Euler product:
        a multiplicative  <=>  its formal Dirichlet series factors as
        prod_p ( sum_{k>=0} a(p^k) p^{-ks} ) as formal power series in each
        p^{-s}  <=>  a(n) = prod_{p^e || n} a(p^e).
4.  Finite-detection result (honest, non-overclaimed):
      * For any FIXED bound ``B`` the least mixed-prime cumulant ``<= B`` is
        found exactly by inspecting the finitely many ``n <= B`` with
        ``omega(n) >= 2`` (each ``b(n)`` uses only ``a(d)``, ``d | n``). PROVED.
      * There is NO single finite window ``B`` that certifies multiplicativity
        for ALL sources: for every ``B`` a source passes the window test yet is
        non-multiplicative (``window_evasion_source``). PROVED (counterexample).
        This is exactly the forbidden ``(forall a)(exists B)`` -> ``(exists
        B)(forall a)`` quantifier swap, flagged by ``proof_contracts``.

HARD FIREWALL (preserved here):
  * Exact arithmetic only. Floats are rejected on input; a float is NEVER a
    certificate.
  * The FORMAL Dirichlet/Euler-product statements and the ANALYTICALLY
    convergent Euler product are DIFFERENT claims. Everything above is FORMAL.
    Analytic convergence is a separate, explicitly-labeled statement carried by
    :func:`analytic_convergence_claim` with a declared half-plane; we give one
    source that converges (zeta, Re(s) > 1) and one whose formal object is fine
    but whose Dirichlet series diverges for *every* ``s`` (coefficients grow too
    fast). Never conflate the two.
  * A correct (formal or analytic) Euler-product source does NOT imply Weil
    positivity. No zeta zero, no half-density, no phase is used anywhere in this
    module. RH stays OPEN and untouched.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Callable, Dict, List, Mapping, Optional, Sequence, Tuple, Union

import sympy as sp

from .arithmetic_interactions import is_prime_power
from .proof_contracts import ProofContract, Quantifier

__all__ = [
    "DirichletCumulantError",
    # arithmetic-function helpers
    "num_distinct_prime_factors", "is_mixed", "mixed_indices",
    "delta_array", "dirichlet_convolve",
    # the formal log / exp and cumulants
    "dirichlet_log", "dirichlet_exp",
    "mixed_prime_cumulant", "first_mixed_cumulant_closed_form",
    # characterization
    "is_multiplicative_via_cumulants", "first_nonzero_mixed_cumulant",
    "multiplicative_extension", "formal_euler_product_matches",
    "local_euler_factor_coeffs",
    # control sources
    "constant_one", "mobius_source", "liouville_source",
    "divisor_count_source", "euler_phi_source",
    "completely_multiplicative", "multiplicative_from_prime_powers",
    "factorial_completely_multiplicative",
    # finite detection / window evasion
    "next_mixed_integer_above", "window_evasion_source",
    # analytic (SEPARATE, labeled) claims
    "AnalyticConvergenceClaim", "analytic_convergence_claim",
    "completely_multiplicative_term_test_failure",
    # proof contracts
    "characterization_contract", "pointwise_window_contract",
    "uniform_window_contract",
]

MAX_BOUND = 4096


class DirichletCumulantError(ValueError):
    pass


# --------------------------------------------------------------------------
# exactness firewall + small helpers
# --------------------------------------------------------------------------

def _exact(x) -> sp.Expr:
    """Coerce to an exact sympy value; reject floats (a float is never a cert)."""
    if isinstance(x, float):
        raise DirichletCumulantError(
            "float is never a certificate; pass int, Fraction, or exact sympy"
        )
    if isinstance(x, Fraction):
        return sp.Rational(x.numerator, x.denominator)
    v = sp.sympify(x)
    if v.has(sp.Float):
        raise DirichletCumulantError(
            "float is never a certificate; pass int, Fraction, or exact sympy"
        )
    return v


def _simp(x: sp.Expr) -> sp.Expr:
    x = sp.sympify(x)
    if x.is_Rational or x.is_Integer:
        return x
    return sp.simplify(x)


def _is_zero(x) -> bool:
    x = sp.sympify(x)
    if x.is_Rational or x.is_Integer:
        return x == 0
    return sp.simplify(x) == 0


def _check_bound(bound: int) -> int:
    if type(bound) is not int or not 2 <= bound <= MAX_BOUND:
        raise DirichletCumulantError(f"bound must be an int in 2..{MAX_BOUND}, got {bound!r}")
    return bound


def num_distinct_prime_factors(n: int) -> int:
    """omega(n): number of DISTINCT primes dividing n (omega(1) = 0)."""
    if type(n) is not int or n < 1:
        raise DirichletCumulantError(f"need integer n>=1, got {n!r}")
    return len(sp.factorint(n)) if n > 1 else 0


def is_mixed(n: int) -> bool:
    """True iff n has at least two distinct prime factors (omega(n) >= 2)."""
    return num_distinct_prime_factors(n) >= 2


def mixed_indices(bound: int) -> List[int]:
    """All n <= bound with omega(n) >= 2, ascending (smallest is 6)."""
    _check_bound(bound)
    return [n for n in range(2, bound + 1) if num_distinct_prime_factors(n) >= 2]


# --------------------------------------------------------------------------
# coefficient arrays (1-indexed; index 0 is an unused pad set to 0)
# --------------------------------------------------------------------------

ArithFn = Union[Callable[[int], object], Mapping[int, object], Sequence[object]]


def _coeff_array(a: ArithFn, bound: int, *, require_one: bool = True) -> List[sp.Expr]:
    """Build [0, a(1), ..., a(bound)] as exact sympy values.

    ``a`` may be a callable ``a(n)``, a mapping ``n -> a(n)``, or a 1-indexed
    sequence (``a[0]`` ignored). With ``require_one`` (the default for a
    normalized source) we enforce ``a(1) = 1``.
    """
    _check_bound(bound)
    arr: List[sp.Expr] = [sp.Integer(0)]
    if callable(a):
        for n in range(1, bound + 1):
            arr.append(_exact(a(n)))
    elif isinstance(a, Mapping):
        for n in range(1, bound + 1):
            if n not in a:
                raise DirichletCumulantError(f"missing source coefficient a({n})")
            arr.append(_exact(a[n]))
    elif isinstance(a, (list, tuple)):
        if len(a) < bound + 1:
            raise DirichletCumulantError(
                f"sequence too short: need 1-indexed length >= {bound + 1}"
            )
        for n in range(1, bound + 1):
            arr.append(_exact(a[n]))
    else:
        raise DirichletCumulantError("source must be callable, Mapping, or 1-indexed sequence")
    if require_one and not _is_zero(arr[1] - 1):
        raise DirichletCumulantError(f"normalized source requires a(1)=1, got {arr[1]}")
    return arr


def _b_array(b: ArithFn, bound: int) -> List[sp.Expr]:
    """Build the b-coefficient array for the exp side; enforce b(1) = 0."""
    arr = _coeff_array(b, bound, require_one=False)
    if not _is_zero(arr[1]):
        raise DirichletCumulantError(f"augmentation-ideal input requires b(1)=0, got {arr[1]}")
    return arr


def delta_array(bound: int) -> List[sp.Expr]:
    """The Dirichlet identity delta: delta(1) = 1, else 0, as a 1-indexed array."""
    _check_bound(bound)
    d = [sp.Integer(0)] * (bound + 1)
    d[1] = sp.Integer(1)
    return d


def dirichlet_convolve(f: Sequence[sp.Expr], g: Sequence[sp.Expr]) -> List[sp.Expr]:
    """(f *x g)(n) = sum_{d | n} f(d) g(n/d) on equal-length 1-indexed arrays."""
    n = len(f) - 1
    if len(g) - 1 != n:
        raise DirichletCumulantError("convolution needs equal-length coefficient arrays")
    out = [sp.Integer(0)] * (n + 1)
    for d in range(1, n + 1):
        fd = f[d]
        if fd == 0:
            continue
        for e in range(1, n // d + 1):
            ge = g[e]
            if ge != 0:
                out[d * e] += fd * ge
    return out


# --------------------------------------------------------------------------
# the formal Dirichlet logarithm (cumulant generator) and its inverse
# --------------------------------------------------------------------------

def _dirichlet_log_array(a: ArithFn, bound: int) -> List[sp.Expr]:
    arr = _coeff_array(a, bound)
    h = [sp.Integer(0)] * (bound + 1)
    for n in range(2, bound + 1):
        h[n] = arr[n]
    b = [sp.Integer(0)] * (bound + 1)
    power = h[:]                      # h^{*1}
    k = 1
    while (1 << k) <= bound:          # only k with 2^k <= bound contribute
        coeff = sp.Rational((-1) ** (k + 1), k)
        for n in range(2, bound + 1):
            if power[n] != 0:
                b[n] += coeff * power[n]
        power = dirichlet_convolve(power, h)
        k += 1
    return [_simp(x) for x in b]


def dirichlet_log(a: ArithFn, bound: int) -> Dict[int, sp.Expr]:
    """Formal Dirichlet logarithm b = log_* a, as ``{n: b(n)}`` for n in 1..bound.

    ``a`` has ``a(1) = 1``; ``b(1) = 0``. Exact and finite at every n (no
    convergence assumption). This is the cumulant generator of ``a``.
    """
    b = _dirichlet_log_array(a, bound)
    return {n: b[n] for n in range(1, bound + 1)}


def dirichlet_exp(b: ArithFn, bound: int) -> Dict[int, sp.Expr]:
    """Formal Dirichlet exponential a = exp_* b, inverse of :func:`dirichlet_log`.

    ``b`` is in the augmentation ideal (``b(1) = 0``); returns ``a(1) = 1``.
    """
    barr = _b_array(b, bound)
    out = delta_array(bound)
    power = delta_array(bound)        # b^{*0} = delta
    k = 1
    while (1 << k) <= bound:
        power = dirichlet_convolve(power, barr)
        inv = sp.Rational(1, factorial(k))
        for n in range(2, bound + 1):
            if power[n] != 0:
                out[n] += inv * power[n]
        k += 1
    return {n: _simp(out[n]) for n in range(1, bound + 1)}


# --------------------------------------------------------------------------
# (1) first mixed-prime cumulant identity
# --------------------------------------------------------------------------

def first_mixed_cumulant_closed_form(a: ArithFn, p: int, q: int) -> sp.Expr:
    """Closed form a(pq) - a(p) a(q) for distinct primes p, q."""
    if p == q:
        raise DirichletCumulantError("need DISTINCT primes p != q")
    if not (is_prime_power(p)[0] and is_prime_power(p)[2] == 1):
        raise DirichletCumulantError(f"p={p} is not prime")
    if not (is_prime_power(q)[0] and is_prime_power(q)[2] == 1):
        raise DirichletCumulantError(f"q={q} is not prime")
    arr = _coeff_array(a, p * q)
    return _simp(arr[p * q] - arr[p] * arr[q])


def mixed_prime_cumulant(a: ArithFn, p: int, q: int) -> sp.Expr:
    """b(pq) for distinct primes p, q, computed from log_* a.

    Self-checking: raises unless it equals the closed form a(pq) - a(p) a(q)
    (the proven first mixed-prime cumulant identity, PROVED FORMAL).
    """
    closed = first_mixed_cumulant_closed_form(a, p, q)
    b = _dirichlet_log_array(a, p * q)
    val = b[p * q]
    if not _is_zero(val - closed):
        raise DirichletCumulantError(
            f"identity b(pq)=a(pq)-a(p)a(q) FAILED at pq={p * q}: {val} != {closed}"
        )
    return val


# --------------------------------------------------------------------------
# (2) characterization of multiplicativity via cumulant support
# --------------------------------------------------------------------------

def is_multiplicative_via_cumulants(a: ArithFn, bound: int) -> bool:
    """True iff b(n) = log_*a (n) = 0 for every n <= bound with omega(n) >= 2.

    By the characterization theorem this is EXACTLY "a is multiplicative up to
    bound" (a(mn) = a(m)a(n) for all coprime m, n with mn <= bound). It does NOT
    certify global multiplicativity -- see ``window_evasion_source``.
    """
    b = _dirichlet_log_array(a, bound)
    return all(_is_zero(b[n]) for n in mixed_indices(bound))


def first_nonzero_mixed_cumulant(a: ArithFn, bound: int) -> Optional[int]:
    """Least n <= bound with omega(n) >= 2 and b(n) != 0, else None."""
    b = _dirichlet_log_array(a, bound)
    for n in mixed_indices(bound):
        if not _is_zero(b[n]):
            return n
    return None


def multiplicative_extension(a: ArithFn, bound: int) -> List[sp.Expr]:
    """The multiplicative function hat-a(n) = prod_{p^e || n} a(p^e), 1-indexed.

    This is the coefficient array of the FORMAL Euler product of ``a`` (the
    product of the local prime factors). It equals ``a`` exactly iff ``a`` is
    multiplicative up to ``bound``.
    """
    arr = _coeff_array(a, bound)
    hat = [sp.Integer(0)] * (bound + 1)
    hat[1] = sp.Integer(1)
    for n in range(2, bound + 1):
        r = sp.Integer(1)
        for p, e in sp.factorint(n).items():
            r *= arr[p ** e]
        hat[n] = _simp(r)
    return hat


def formal_euler_product_matches(a: ArithFn, bound: int) -> bool:
    """True iff a(n) = prod_{p^e || n} a(p^e) for all n <= bound.

    This is the FORMAL Euler-product criterion: the Dirichlet series of ``a``
    factors as prod_p ( sum_k a(p^k) p^{-ks} ) as formal power series iff this
    holds. It is NOT an analytic-convergence statement (see
    :func:`analytic_convergence_claim`).
    """
    arr = _coeff_array(a, bound)
    hat = multiplicative_extension(a, bound)
    return all(_is_zero(arr[n] - hat[n]) for n in range(1, bound + 1))


def local_euler_factor_coeffs(a: ArithFn, p: int, bound: int) -> List[Tuple[int, sp.Expr]]:
    """The local Euler factor coefficients [(k, a(p^k))] for p^k <= bound, k>=0.

    These are the coefficients of the formal local DGF sum_k a(p^k) x^k with
    x = p^{-s}; a(p^0) = a(1) = 1.
    """
    pp, pr, _ = is_prime_power(p)
    if not (pp and pr == p):
        raise DirichletCumulantError(f"p={p} is not prime")
    _check_bound(bound)
    arr = _coeff_array(a, bound)
    out: List[Tuple[int, sp.Expr]] = [(0, sp.Integer(1))]
    k = 1
    while p ** k <= bound:
        out.append((k, arr[p ** k]))
        k += 1
    return out


# --------------------------------------------------------------------------
# (3) exact control sources
# --------------------------------------------------------------------------

def constant_one(n: int) -> int:
    """a(n) = 1 (completely multiplicative; DGF = zeta(s))."""
    return 1


def mobius_source(n: int) -> int:
    """Moebius mu (multiplicative, not completely; DGF = 1/zeta(s))."""
    return int(sp.mobius(n))


def liouville_source(n: int) -> int:
    """Liouville lambda(n) = (-1)^Omega(n) (completely multiplicative)."""
    if n < 1:
        raise DirichletCumulantError("need n>=1")
    return (-1) ** sum(sp.factorint(n).values()) if n > 1 else 1


def divisor_count_source(n: int) -> int:
    """tau(n) = number of divisors (multiplicative, not completely)."""
    return int(sp.divisor_count(n))


def euler_phi_source(n: int) -> int:
    """Euler totient phi(n) (multiplicative, not completely)."""
    return int(sp.totient(n))


def completely_multiplicative(prime_value: Callable[[int], object]) -> Callable[[int], sp.Expr]:
    """Build the completely multiplicative a with a(p) = prime_value(p).

    Then a(n) = prod_{p} prime_value(p)^{v_p(n)} and a(p^k) = a(p)^k. Exact.
    """
    def a(n: int) -> sp.Expr:
        if n < 1:
            raise DirichletCumulantError("need n>=1")
        if n == 1:
            return sp.Integer(1)
        r = sp.Integer(1)
        for p, e in sp.factorint(n).items():
            r *= _exact(prime_value(p)) ** e
        return _simp(r)
    return a


def multiplicative_from_prime_powers(g: Callable[[int, int], object]) -> Callable[[int], sp.Expr]:
    """Build the multiplicative a with a(p^k) = g(p, k) for k>=1, a(1)=1.

    a(n) = prod_{p^e || n} g(p, e). Exact. (General multiplicative, need not be
    completely multiplicative.)
    """
    def a(n: int) -> sp.Expr:
        if n < 1:
            raise DirichletCumulantError("need n>=1")
        if n == 1:
            return sp.Integer(1)
        r = sp.Integer(1)
        for p, e in sp.factorint(n).items():
            r *= _exact(g(p, e))
        return _simp(r)
    return a


def factorial_completely_multiplicative(n: int) -> sp.Expr:
    """Completely multiplicative source with a(p) = p! (prime factorial).

    FORMAL object is fine; its Dirichlet series DIVERGES for every s because the
    general term a(p) p^{-s} = p! p^{-sigma} -> infinity along primes (necessary
    condition for convergence fails). See
    :func:`completely_multiplicative_term_test_failure`.
    """
    return completely_multiplicative(lambda p: factorial(p))(n)


# --------------------------------------------------------------------------
# (5) finite detection and the window-evasion counterexample
# --------------------------------------------------------------------------

def next_mixed_integer_above(B: int) -> int:
    """Least integer > B with omega >= 2 (always exists, e.g. the next 2*odd)."""
    if type(B) is not int or B < 1:
        raise DirichletCumulantError("B must be a positive int")
    n = B + 1
    while num_distinct_prime_factors(n) < 2:
        n += 1
    return n


def window_evasion_source(B: int) -> Tuple[Callable[[int], int], int]:
    """A source that PASSES the window test up to B yet is NOT multiplicative.

    Returns ``(a, N)`` where ``N = next_mixed_integer_above(B)`` and ``a`` equals
    the constant-1 (completely multiplicative) source except ``a(N) = 2``. Then
    ``b(n) = 0`` for every mixed ``n <= B`` but ``b(N) = 1 != 0``, so no fixed
    finite window certifies multiplicativity for all sources. (Minimal
    counterexample to the illegal ``(exists B)(forall a)`` uniformization.)
    """
    N = next_mixed_integer_above(B)

    def a(n: int) -> int:
        if n < 1:
            raise DirichletCumulantError("need n>=1")
        return 2 if n == N else 1
    return a, N


# --------------------------------------------------------------------------
# (4) analytic convergence -- a SEPARATE, explicitly labeled statement
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class AnalyticConvergenceClaim:
    """A labeled claim about the ANALYTIC Dirichlet series sum a(n) n^{-s}.

    This is deliberately distinct from every FORMAL statement in this module.
    ``converges`` is True/False/None(open); ``half_plane`` names the declared
    region of absolute convergence when it converges; ``status`` uses the
    proof_contracts vocabulary.
    """
    source: str
    converges: Optional[bool]
    half_plane: Optional[str]
    status: str
    justification: str


_ANALYTIC_CLAIMS: Dict[str, AnalyticConvergenceClaim] = {
    "constant_one": AnalyticConvergenceClaim(
        "constant_one", True, "Re(s) > 1", "CLASSICAL",
        "sum 1 * n^{-s} = zeta(s), abscissa of absolute convergence sigma_a = 1.",
    ),
    "mobius_source": AnalyticConvergenceClaim(
        "mobius_source", True, "Re(s) > 1", "CLASSICAL",
        "sum mu(n) n^{-s} = 1/zeta(s); |mu| <= 1 so it is dominated by zeta(sigma), "
        "absolutely convergent for Re(s) > 1.",
    ),
    "liouville_source": AnalyticConvergenceClaim(
        "liouville_source", True, "Re(s) > 1", "CLASSICAL",
        "sum lambda(n) n^{-s} = zeta(2s)/zeta(s); |lambda| = 1 so dominated by "
        "zeta(sigma), absolutely convergent for Re(s) > 1.",
    ),
    "divisor_count_source": AnalyticConvergenceClaim(
        "divisor_count_source", True, "Re(s) > 1", "CLASSICAL",
        "sum tau(n) n^{-s} = zeta(s)^2, absolutely convergent for Re(s) > 1.",
    ),
    "factorial_completely_multiplicative": AnalyticConvergenceClaim(
        "factorial_completely_multiplicative", False, None, "PROVED LOCAL",
        "Completely multiplicative with a(p) = p!. For EVERY s with Re(s) = sigma "
        "the general term along primes is |a(p) p^{-s}| = p! p^{-sigma} -> infinity "
        "(since p!/p^sigma -> infinity), so the necessary condition term -> 0 fails "
        "and the Dirichlet series diverges for all s. The FORMAL log/Euler product "
        "is nonetheless perfectly well defined.",
    ),
}


def analytic_convergence_claim(name: str) -> AnalyticConvergenceClaim:
    """Return the curated, labeled ANALYTIC convergence claim for a named source.

    These are hand-verified classical facts kept strictly separate from the
    formal statements. Unknown names raise.
    """
    if name not in _ANALYTIC_CLAIMS:
        raise DirichletCumulantError(
            f"no curated analytic claim for {name!r}; known: {sorted(_ANALYTIC_CLAIMS)}"
        )
    return _ANALYTIC_CLAIMS[name]


def completely_multiplicative_term_test_failure(
    prime_value: Callable[[int], object], sigma, *, prime_bound: int = 300
) -> Optional[int]:
    """Smallest prime p <= prime_bound with |prime_value(p)| * p^{-sigma} > 1.

    For a completely multiplicative source with a(p) = prime_value(p), finding
    such a prime exhibits (exactly, no floats) that the general term of
    sum a(n) n^{-s} does not tend to 0 at Re(s) = sigma, hence the series cannot
    converge there. Returns the witness prime, or None if none is found in range
    (which is NOT a convergence certificate -- absence of a witness in a finite
    window proves nothing analytic).
    """
    sig = _exact(sigma)
    for p in sp.primerange(2, prime_bound + 1):
        val = abs(_exact(prime_value(p)))
        # |a(p)| p^{-sigma} > 1  <=>  |a(p)| > p^{sigma}
        if val > sp.Integer(p) ** sig:
            return int(p)
    return None


# --------------------------------------------------------------------------
# proof contracts (quantifier bookkeeping for the finite-detection result)
# --------------------------------------------------------------------------

def characterization_contract() -> ProofContract:
    """The main theorem as a checked proof contract (CLASSICAL, FORMAL)."""
    return ProofContract(
        name="dirichlet_cumulant_characterization",
        statement=(
            "For a with a(1)=1 and b = log_* a (formal Dirichlet logarithm): "
            "a is multiplicative  <=>  b(n) = 0 for all n with omega(n) >= 2."
        ),
        prefix=[
            Quantifier("forall", "a", "arithmetic functions with a(1)=1"),
            Quantifier("forall", "n", "integers n>=1", depends_on=("a",)),
        ],
        hypotheses=[
            "convolution is the Dirichlet product (commutative, assoc., identity delta)",
            "b = log_* a defined by the finite formal series (2^k <= n terms)",
        ],
        constant_dependencies={},
        finite_to_infinite=(
            "No finite->infinite step: the equivalence is a pointwise FORMAL "
            "identity for each n. Global multiplicativity is the conjunction over "
            "ALL n and is NOT implied by any finite sub-conjunction."
        ),
        source_authentic=True,
        method="exp_*/log_* group isomorphism; prime-power support decomposition b = sum_p log_*(a_p)",
        status="CLASSICAL",
        open_obligations=[],
    )


def pointwise_window_contract() -> ProofContract:
    """Legitimate pointwise detection: (forall a)(exists B_a) detecting non-mult.

    For every non-multiplicative source ``a`` there is a bound ``B_a`` (its first
    mixed-defect location) such that inspecting ``{n <= B_a : omega(n) >= 2}``
    reveals b(n) != 0. ``B`` DEPENDS on ``a`` -- this is sound. PROVED LOCAL.
    """
    return ProofContract(
        name="pointwise_finite_detection",
        statement=(
            "For every non-multiplicative a there EXISTS a finite bound B (its "
            "first mixed-prime defect) such that inspecting the n <= B with "
            "omega(n) >= 2 detects a nonzero cumulant."
        ),
        prefix=[
            Quantifier("forall", "a", "non-multiplicative arithmetic functions with a(1)=1"),
            Quantifier("exists", "B", "finite bounds", depends_on=("a",)),
        ],
        hypotheses=["b(n) uses only a(d), d | n (finite, exact)"],
        constant_dependencies={"B": ["a"]},
        finite_to_infinite="B is chosen per source; no uniform window is claimed.",
        source_authentic=True,
        method="b = log_* a has a least mixed n with b(n) != 0; take B = that n",
        status="PROVED LOCAL",
        open_obligations=[],
    )


def uniform_window_contract() -> ProofContract:
    """The REFUTED uniform claim: (exists B)(forall a). Illegal quantifier swap.

    Claims a single finite window ``B`` certifies multiplicativity for ALL
    sources. Refuted by ``window_evasion_source`` for every ``B``. Feeding this to
    ``pointwise_window_contract().assert_not_uniformized_from`` (or vice versa)
    fires the proof_contracts guard.
    """
    return ProofContract(
        name="uniform_finite_detection_REFUTED",
        statement=(
            "[REFUTED] There exists a single finite bound B such that for every "
            "source a, b(n) = 0 for all mixed n <= B implies a is multiplicative."
        ),
        prefix=[
            Quantifier("exists", "B", "finite bounds"),
            Quantifier("forall", "a", "arithmetic functions with a(1)=1", depends_on=("B",)),
        ],
        hypotheses=["(false) one window fits all sources"],
        constant_dependencies={"B": []},
        finite_to_infinite=(
            "Illegal (forall a)(exists B) -> (exists B)(forall a) swap. "
            "Counterexample: window_evasion_source(B) for each B."
        ),
        source_authentic=True,
        method="refuted by explicit per-window counterexample",
        status="REFUTED",
        open_obligations=["none -- permanently refuted"],
    )
