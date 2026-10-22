"""Exact independent Hilbert-character oracle for the existing Q[Q/Z] transfer.

Cyclotomic values are reduced modulo Phi_D, not compared as formal phase
polynomials. This finite oracle does not certify C*-norm faithfulness.
See research/2026-10-22/ARITHMETIC_OPERATOR_INTERFACE.md for the paper proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm

from .affine_pontryagin_transfer import RationalCharacterAlgebra


def _positive(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive exact integer required")
    return n


def _trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def _divmod_monic(p, q):
    p, q = _trim(p), _trim(q)
    if q[-1] != 1:
        raise ValueError("monic divisor required")
    out = [F(0)] * max(1, len(p)-len(q)+1)
    while len(p) >= len(q) and any(p):
        degree, lead = len(p)-len(q), p[-1]
        out[degree] = lead
        for i, x in enumerate(q):
            p[i+degree] -= lead*x
        p = _trim(p)
    return tuple(_trim(out)), tuple(p)


@lru_cache(maxsize=512)
def cyclotomic_polynomial(conductor):
    """Integer Phi_D in ascending degree, via x^D-1=prod_(d|D) Phi_d."""
    d = _positive(conductor)
    if d > 1024:
        raise ValueError("finite oracle conductor budget is 1024")
    poly = (-1,) + (0,)*(d-1) + (1,)
    for k in range(1, d):
        if d % k == 0:
            poly, remainder = _divmod_monic(poly, cyclotomic_polynomial(k))
            if any(remainder):
                raise ArithmeticError("cyclotomic division was not exact")
    return tuple(int(x) for x in poly)


def character_value(element, n, conductor=None):
    """Evaluate the old source-typed transfer element at integer n, exactly.

    Result is (D, coefficients modulo Phi_D). Different D are deliberately
    different representations; supply a common conductor before comparison.
    """
    if not isinstance(element, RationalCharacterAlgebra) or type(n) is not int:
        raise ValueError("source-typed rational character algebra and exact n required")
    needed = lcm(*(r.denominator for r, _ in element.terms))
    d = needed if conductor is None else _positive(conductor)
    if d % needed:
        raise ValueError("conductor does not contain all source phases")
    modulus = cyclotomic_polynomial(d)
    poly = [F(0)] * d
    for r, c in element.terms:
        poly[(n*r.numerator*(d//r.denominator)) % d] += c
    _, rem = _divmod_monic(poly, modulus)
    return d, rem + (F(0),)*(len(modulus)-1-len(rem))


def root_average_receipt(r, m, n):
    """Compare existing rho_m with direct V_m E(r) V_m* on |n>."""
    _positive(m)
    _positive(n)
    e = RationalCharacterAlgebra.basis(r)
    averaged = e.rho(m)
    d = lcm(*(s.denominator for s, _ in averaged.terms))
    actual = character_value(averaged, n, d)
    direct = character_value(e, n//m, d) if n % m == 0 else character_value(e.zero(), 0, d)
    return {"actual": actual, "direct": direct, "equal": actual == direct}


def basis_action(word, n):
    """Chronological V_m, V_m*, E(r) word on an untruncated basis vector.

    ('V',m) multiplies, ('D',m) takes the adjoint, ('E',r) accumulates a
    rational phase. None is the zero vector. Composite m is legitimate here.
    """
    _positive(n)
    phase = F(0)
    for op, arg in word:
        if op == "V":
            n *= _positive(arg)
        elif op == "D":
            _positive(arg)
            if n % arg:
                return None
            n //= arg
        elif op == "E":
            if type(arg) not in (int, F):
                raise ValueError("exact rational phase required")
            phase = (phase+n*arg) % 1
        else:
            raise ValueError("unknown operator")
    return n, phase


def shift_refinement_defect(small, large):
    """Matrix of T_large J-J T_small, cutoffs inclusive 0..small/large.

    A nonzero defect on the top input is preserved at every strict refinement.
    Sparse entries are (output,input,value); no norm computation is hidden.
    """
    if type(small) is not int or type(large) is not int or not 0 <= small <= large:
        raise ValueError("ordered nonnegative integer cutoffs required")
    entries = []
    for k in range(small+1):
        left = k+1 if k < large else None
        right = k+1 if k < small else None
        if left != right:
            if left is not None:
                entries.append((left, k, F(1)))
            if right is not None:
                entries.append((right, k, F(-1)))
    return tuple(entries)


def thermal_refinement_defect_squared(q, cutoff):
    """Squared state-dependent defect for geometric amplitudes on 0..cutoff."""
    if type(q) not in (int, F) or not 0 < q < 1:
        raise ValueError("exact geometric parameter 0<q<1 required")
    if type(cutoff) is not int or cutoff < 0:
        raise ValueError("nonnegative integer cutoff required")
    q = F(q)
    return q**cutoff / sum((q**j for j in range(cutoff+1)), F(0))


def _monomial(monomial):
    """V_m E(r) V_n*, with an exact rational frequency."""
    m, r, n = monomial
    _positive(m)
    _positive(n)
    if type(r) not in (int, F):
        raise ValueError("exact rational frequency required")
    return m, F(r) % 1, n


def multiply_monomials(left, right):
    m, r, n = _monomial(left)
    k, s, ell = _monomial(right)
    d = gcd(n, k)
    return m*(k//d), ((k//d)*r+(n//d)*s) % 1, ell*(n//d)


def critical_state_monomial(monomial):
    """Proved beta-downarrow-one limit on the concrete arithmetic C*-algebra.

    Positivity is proved by the Gibbs-state limit in the paper, not by this
    scalar evaluator. This is not an analytically continued density matrix.
    """
    m, r, n = _monomial(monomial)
    return F(1, m) if m == n and not r else F(0)
