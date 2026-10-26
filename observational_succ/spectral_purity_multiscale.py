"""Exact prefix/jet-matched positive odd-conductor NONNORMAL controls.

This module constructs changed sources, never an alternative authentication
of BBP.  The universal theorem and all error constants are proved in
research/2026-10-25/SPECTRAL_PURITY_MULTISCALE.md.  Every computation is rational.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, factorial, prod

from .succ_internal_matrix_walk import authentic_r, original_state


def _nat(n: int, minimum: int = 0, maximum: int = 100000) -> int:
    if type(n) is not int or not minimum <= n <= maximum:
        raise ValueError("bounded integer index required")
    return n


def _trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def _add(p, q):
    out = [Q()] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return _trim(out)


def _scale(p, c):
    return _trim(x * c for x in p)


def _mul(p, q):
    out = [Q()] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            if x and y:
                out[i+j] += x*y
    return _trim(out)


def _power(p, k):
    out = (Q(1),)
    for _ in range(k):
        out = _mul(out, p)
    return out


def _divide_one_minus(p, order):
    """Exact polynomial division by (1-s)^order, including residual checks."""
    out = tuple(p)
    for _ in range(order):
        if len(out) < 2 or sum(out) != 0:
            raise ArithmeticError("endpoint jet divisibility failed")
        quotient = []
        running = Q()
        for coefficient in out[:-1]:
            running += coefficient
            quotient.append(running)
        out = _trim(quotient)
    return out


def even_moment(coefficients, n: int) -> Q:
    """Integral t^(8n) times a polynomial in t^2, on [0,1]."""
    _nat(n, maximum=10**25)
    coefficients = tuple(coefficients)
    if any(type(c) not in (int, Q) for c in coefficients):
        raise ValueError("exact integer or Fraction coefficients required")
    return sum((Q(c) / (8*n+2*j+1) for j, c in enumerate(coefficients)), Q())


def beta_even(n: int, order: int) -> Q:
    """Exact integral t^(8n)(1-t^2)^order dt."""
    _nat(n, maximum=10**25)
    _nat(order, maximum=512)
    return Q(2**order * factorial(order),
             prod(8*n+2*j+1 for j in range(order+1)))


def _approximating_polynomial(level: int):
    """A_L(s), positive >=56/225; endpoint jets agree with A through L."""
    _nat(level, 1, 256)
    b, term = (Q(),), (Q(1),)
    for j in range(level+1):
        m = j+1
        a = Q(comb(2*m, m), 4**m * (2*m-1))
        b = _add(b, _scale(term, a))
        term = _mul(term, (Q(1), Q(-1)))
    denominator, term = (Q(),), (Q(1),)
    for j in range(level+1):
        denominator = _add(denominator, _scale(term, Q((-1)**j, 15**(j+1))))
        term = _mul(term, (Q(1), Q(), Q(), Q(), Q(-1)))
    return _mul(_mul((Q(2), Q(1)), _add((Q(2),), (Q(),)+b)), denominator)


def _newton_coefficients(values):
    row, out = list(values), []
    while row:
        out.append(row[0])
        row = [b-a for a, b in zip(row, row[1:])]
    return tuple(out)


def _newton_value(coefficients, x):
    x, choose, out = Q(x), Q(1), Q()
    for j, coefficient in enumerate(coefficients):
        out += coefficient * choose
        choose *= (x-j)/(j+1)
    return out


def _odd_seed(depth: int) -> Q:
    """Odd-denominator lower approximation to T0 using authentic r only.

    Error < 1/(16^D+1) + r(D+1)/(15*16^D); no pi oracle.
    """
    prefix = sum((authentic_r(j)/16**j for j in range(1, depth+1)), Q())
    denominator = 16**depth+1
    return Q((denominator*prefix).__floor__(), denominator)


@dataclass(frozen=True)
class PrefixJetCounterfeit:
    """A changed positive rational source with certified finite BBP agreement."""
    prefix: int
    jet_order: int
    approximation_level: int
    seed: Q
    density: tuple[Q, ...]  # R(t) = sum density[j] t^(2j)
    correction_quotient: tuple[Q, ...]
    correction_newton: tuple[Q, ...]
    correction_denominator_degree: int

    @property
    def correction_norm(self) -> Q:
        return sum(map(abs, self.correction_quotient), Q())

    @property
    def positivity_margin(self) -> Q:
        return Q(56, 225)-self.correction_norm

    @property
    def difference_constant(self) -> Q:
        level = self.approximation_level
        tail = Q(comb(2*level+2, level+1), 4**(level+1))
        return self.correction_norm + tail/5 + Q(3, 5)*Q(4, 15)**(level+1)

    def tail(self, n: int) -> Q:
        return even_moment(self.density, n)

    def forcing(self, n: int) -> Q:
        _nat(n, 1, 10**25)
        return 16*self.tail(n-1)-self.tail(n)

    def state(self, n: int) -> Q:
        _nat(n, maximum=2000)
        return 16**n*self.seed-self.tail(n)

    def forcing_difference_bound(self, time: int, difference_order: int = 0) -> Q:
        """Bound |Delta^b(r*(n+1)-r(n+1))|, all n,b in domain."""
        _nat(time, maximum=10**25)
        _nat(difference_order, maximum=60)
        b = difference_order
        return 16*self.difference_constant*4**b*beta_even(time, self.jet_order+b+1)

    def correction_tail(self, n: int) -> Q:
        _nat(n, maximum=10**25)
        d = self.correction_denominator_degree
        denominator = prod(8*n+2*i+1 for i in range(d))
        return _newton_value(self.correction_newton, n)/denominator


def prefix_jet_counterfeit(prefix: int, jet_order: int, *, max_level: int = 128) -> PrefixJetCounterfeit:
    """Construct and certify; a finite cap failure is explicit, never success.

    For every fixed prefix M and order K>=1 some refinement succeeds (paper
    theorem).  The bounded executable only returns after a rational global
    positivity certificate; the cap does not purport to prove nonexistence.
    """
    _nat(prefix, 0, 12)
    _nat(jet_order, 1, 12)
    _nat(max_level, max(1, jet_order), 256)
    states = tuple(original_state(j) for j in range(prefix+1))
    d = prefix+jet_order+1
    level = max(1, jet_order)
    while level <= max_level:
        a = _approximating_polynomial(level)
        density = _mul((Q(1), Q(-1)), a)
        seed = _odd_seed(level+prefix+4)
        residual = tuple(16**j*seed-states[j]-even_moment(density, j)
                         for j in range(prefix+1))
        targets = tuple(residual[j]*prod(8*j+2*i+1 for i in range(d+1))
                        for j in range(prefix+1))
        newton = _newton_coefficients(targets)
        correction = tuple(
            _newton_value(newton, -Q(2*i+1, 8)) /
            prod(2*(j-i) for j in range(d+1) if i != j)
            for i in range(d+1))
        quotient = _divide_one_minus(correction, jet_order+1)
        candidate = PrefixJetCounterfeit(prefix, jet_order, level, seed,
                                        _add(density, correction), quotient, newton, d+1)
        if candidate.correction_norm < Q(1, 10):
            if candidate.tail(0) != seed or any(candidate.state(j) != states[j]
                                               for j in range(prefix+1)):
                raise ArithmeticError("source prefix or zero anchor failed")
            if any(c.denominator % 2 == 0 for c in newton):
                raise ArithmeticError("odd-conductor Newton certificate failed")
            return candidate
        level *= 2
    raise ValueError("global positivity not certified within declared refinement budget")
