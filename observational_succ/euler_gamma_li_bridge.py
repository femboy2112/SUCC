"""Successor Stieltjes defects -> completed Li coefficients, without zero input.

CLASSICAL identities, with exact rational interval transport and explicit
finite-jet countercontrols.  Standard convention:

    zeta(1+z) = 1/z + sum_j (-1)^j gamma_j z^j/j!.

The Gamma factor, pole normalization and log(pi) term are kept in the
completed coefficient formula.  Finite positive coefficients do not prove
the all-degree Li criterion.  Supplying arbitrary intervals does not
authenticate them as Stieltjes or zeta values; ``certified_li_prefix``
constructs its inputs from elementary integer sums and proved tails.

No nontrivial zero locations or numerical special functions are inputs.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial

from .observer_reflection import RationalInterval as I
from .source_prime_certificates import rational_log_integer
from .suzuki_arch_intervals import log2_interval, log_pi_interval


class GammaLiError(ValueError):
    """Invalid exact input, finite horizon or completion data."""


def _q(value):
    if type(value) is int or isinstance(value, Q):
        return Q(value)
    raise GammaLiError("exact int/Fraction required; no floats or bools")


def _degree(value, maximum=32):
    if type(value) is not int or not 1 <= value <= maximum:
        raise GammaLiError(f"degree must be an integer in 1..{maximum}")
    return value


def _exact_values(values):
    if type(values) is not tuple:
        raise GammaLiError("a nonempty finite tuple of exact coefficients is required")
    _degree(len(values))
    return tuple(_q(x) for x in values)


def _interval_values(values):
    if type(values) is not tuple or not values:
        raise GammaLiError("a nonempty finite tuple of rational intervals is required")
    _degree(len(values))
    if not all(isinstance(x, I) for x in values):
        raise GammaLiError("every coefficient must be a RationalInterval")
    return values


def _grid(interval, places):
    """Outward rational rounding; its denominator controls expression growth."""
    scale = 10**places
    lo = (interval.lower * scale).__floor__()
    hi = (interval.upper * scale).__ceil__()
    return I(Q(lo, scale), Q(hi, scale))


def _nonnegative_power(interval, exponent):
    if interval.lower < 0:
        raise GammaLiError("nonnegative interval required for endpoint power")
    return I(interval.lower**exponent, interval.upper**exponent)


def stieltjes_log_coefficients(stieltjes):
    """Exact coefficients b_1..b_d of log(z*zeta(1+z)).

    For a_n=(-1)^(n-1) gamma_(n-1)/(n-1)! and a_0=1,
      b_n=a_n-(1/n) sum_(j=1)^(n-1) j*b_j*a_(n-j).
    The recurrence is valid formally for any rational input jet; it does
    not assert that an arbitrary jet belongs to the authentic zeta source.
    """
    g = _exact_values(stieltjes)
    a = (Q(1),) + tuple((-1)**j*x/factorial(j) for j, x in enumerate(g))
    b = [Q(0)]
    for n in range(1, len(a)):
        b.append(a[n]-sum((j*b[j]*a[n-j] for j in range(1, n)), Q(0))/n)
    return tuple(b[1:])


def stieltjes_log_intervals(stieltjes):
    """Outward version of the formal logarithm, conditional on input bounds."""
    g = _interval_values(stieltjes)
    a = (I.exact(1),) + tuple(x.scale(Q((-1)**j, factorial(j)))
                             for j, x in enumerate(g))
    b = [I.exact(0)]
    for n in range(1, len(a)):
        cross = I.exact(0)
        for j in range(1, n):
            cross += (b[j]*a[n-j]).scale(j)
        b.append(a[n]-cross.scale(Q(1, n)))
    return tuple(b[1:])


def li_from_stieltjes(stieltjes, *, log_four_pi, integer_zeta, arch_euler_gamma=None):
    """Exact rational model of the fully completed Li transfer.

    log(xi(1+z)/xi(1))=sum c_k z^k, with
      c_1=1+gamma_0-gamma_arch/2-log(4*pi)/2,
      c_k=(-1)^(k+1)/k+(-1)^k*(1-2^-k)*zeta(k)/k+b_k (k>=2).
    Then lambda_n=n*sum_(k=1)^n C(n-1,k-1)*c_k.
    Authentic zeta has gamma_arch=gamma_0; that equality is the default.
    For a changed arithmetic source with FIXED Gamma completion, supply
    ``arch_euler_gamma`` separately rather than changing it with gamma_0.
    ``integer_zeta`` must contain every integer k=2..degree, even if a
    caller intends to omit a completion channel.
    """
    g = _exact_values(stieltjes)
    ell = _q(log_four_pi)
    arch_gamma = g[0] if arch_euler_gamma is None else _q(arch_euler_gamma)
    b = stieltjes_log_coefficients(g)
    if not isinstance(integer_zeta, dict):
        raise GammaLiError("integer_zeta must map 2..degree to exact values")
    try:
        zv = {k: _q(integer_zeta[k]) for k in range(2, len(g)+1)}
    except KeyError as exc:
        raise GammaLiError("missing completed Gamma/zeta integer coefficient") from exc
    c = [Q(0), Q(1)+g[0]-arch_gamma/2-ell/2]
    for k in range(2, len(g)+1):
        c.append(Q((-1)**(k+1), k)
                 + Q((-1)**k, k)*(1-Q(1, 2**k))*zv[k]+b[k-1])
    return tuple(n*sum((comb(n-1, k-1)*c[k] for k in range(1, n+1)), Q(0))
                 for n in range(1, len(g)+1))


def li_intervals_from_stieltjes(stieltjes, *, log_four_pi, integer_zeta, arch_euler_gamma=None):
    """Rigorous finite transport conditional on authentic input enclosures."""
    g = _interval_values(stieltjes)
    if not isinstance(log_four_pi, I) or not isinstance(integer_zeta, dict):
        raise GammaLiError("rational intervals and an integer-zeta mapping are required")
    if arch_euler_gamma is not None and not isinstance(arch_euler_gamma, I):
        raise GammaLiError("arch_euler_gamma must be a rational interval")
    if any(k not in integer_zeta or not isinstance(integer_zeta[k], I)
           for k in range(2, len(g)+1)):
        raise GammaLiError("every completed integer-zeta interval is required")
    b = stieltjes_log_intervals(g)
    # The default uses the genuine equality gamma_arch=gamma_0 exactly,
    # avoiding an artificial interval dependency penalty at first order.
    first = (I.exact(1)+g[0].scale(Q(1, 2))-log_four_pi.scale(Q(1, 2))
             if arch_euler_gamma is None else
             I.exact(1)+g[0]-arch_euler_gamma.scale(Q(1, 2))-log_four_pi.scale(Q(1, 2)))
    c = [I.exact(0), first]
    for k in range(2, len(g)+1):
        c.append(I.exact(Q((-1)**(k+1), k))
                 + integer_zeta[k].scale(Q((-1)**k, k)*(1-Q(1, 2**k)))+b[k-1])
    out = []
    for n in range(1, len(g)+1):
        total = I.exact(0)
        for k in range(1, n+1):
            total += c[k].scale(n*comb(n-1, k-1))
        out.append(total)
    return tuple(out)


def stieltjes_successor_intervals(cutoff, degree, *, log_terms=16, places=24):
    """Construct gamma_0..gamma_(degree-1) from finite integer successors.

    A_(N,m)=sum_(k<=N)log(k)^m/k-log(N)^(m+1)/(m+1).
    For N>=3^m>e^m, f_m(x)=log(x)^m/x decreases on [N,infinity),
      A_(N,m)-f_m(N) <= gamma_m <= A_(N,m).
    The assertion also holds at m=0,N=1.  Exact logarithm intervals and
    outward rounding enclose every summand and the entire infinite tail.
    These intentionally elementary bounds are not an efficient method
    for large Stieltjes index.
    """
    _degree(degree, maximum=9)
    if type(cutoff) is not int or not 3**(degree-1) <= cutoff <= 10000:
        raise GammaLiError("need 3^(degree-1) <= cutoff <= 10000 for monotone tails")
    if type(log_terms) is not int or not 2 <= log_terms <= 100:
        raise GammaLiError("log_terms must be in 2..100")
    if type(places) is not int or not 6 <= places <= 60:
        raise GammaLiError("outward decimal grid places must be in 6..60")
    sums = [I.exact(0) for _ in range(degree)]
    log_n = None
    for k in range(1, cutoff+1):
        log_k = _grid(rational_log_integer(k, terms=log_terms), places)
        for m in range(degree):
            sums[m] += _grid(_nonnegative_power(log_k, m).scale(Q(1, k)), places)
        if k == cutoff:
            log_n = log_k
    out = []
    for m, total in enumerate(sums):
        a = total-_nonnegative_power(log_n, m+1).scale(Q(1, m+1))
        tail = _nonnegative_power(log_n, m).upper/cutoff
        out.append(_grid(I(a.lower-tail, a.upper), places))
    return tuple(out)


def integer_zeta_interval(exponent, cutoff, *, places=24):
    """Positive Dirichlet source with integral-test tail, all rational."""
    if type(exponent) is not int or not 2 <= exponent <= 32:
        raise GammaLiError("integer zeta exponent must be in 2..32")
    if type(cutoff) is not int or not 1 <= cutoff <= 10000:
        raise GammaLiError("integer zeta cutoff must be in 1..10000")
    if type(places) is not int or not 6 <= places <= 60:
        raise GammaLiError("outward decimal grid places must be in 6..60")
    total = I.exact(0)
    for k in range(1, cutoff+1):
        total += _grid(I.exact(Q(1, k**exponent)), places)
    return total+I(Q(1, (exponent-1)*(cutoff+1)**(exponent-1)),
                   Q(1, (exponent-1)*cutoff**(exponent-1)))


def certified_li_prefix(degree=3, cutoff=512, *, log_terms=16, places=24):
    """Finite source-derived Li enclosures; no all-degree positivity claim."""
    g = stieltjes_successor_intervals(cutoff, degree, log_terms=log_terms, places=places)
    a, b = log2_interval(24)
    c, d = log_pi_interval(32)
    ell = I(2*a+c, 2*b+d)
    zs = {k: integer_zeta_interval(k, cutoff, places=places) for k in range(2, degree+1)}
    ls = li_intervals_from_stieltjes(g, log_four_pi=ell, integer_zeta=zs)
    positive = 0
    for interval in ls:
        if interval.lower <= 0:
            break
        positive += 1
    return {"degree": degree, "cutoff": cutoff, "stieltjes": g,
            "log_four_pi": ell, "integer_zeta": zs, "li": ls,
            "strictly_positive_through": positive, "RH_proved": False,
            "construction": "integer successor sums, elementary log bounds, monotone tails; full Gamma/poles"}


def first_new_stieltjes_sensitivity(order, *, coupled_arch_gamma=False):
    """Changing only gamma_m first changes lambda_(m+1) by this times delta.

    With Gamma completion fixed it is (-1)^m*(m+1)/m! for all m>=0.
    If gamma_arch is ALSO varied with gamma_0 (the coupled authentic
    formula used by default in li_from_stieltjes), the m=0 factor is 1/2.
    These are different perturbations and must not be conflated.
    """
    if type(order) is not int or not 0 <= order <= 31:
        raise GammaLiError("Stieltjes order must be an integer in 0..31")
    if type(coupled_arch_gamma) is not bool:
        raise GammaLiError("coupled_arch_gamma must be a bool")
    return (Q(1, 2) if order == 0 and coupled_arch_gamma
            else Q((-1)**order*(order+1), factorial(order)))


def symmetric_anchor_polynomial(order, anchor=Q(3, 4)):
    """Coefficients in z=s-1 of [s(s-1)/(q(q-1))]^m, exactly.

    For genuine xi, xi_tilde(s)=xi(s)-xi(q)*P_m(s) is entire, real and
    symmetric, preserves its jet through m-1 at 1 and has off-line zeros
    q and 1-q.  It changes the arithmetic source; it is not a zeta
    counterexample.  No genuine nontrivial zero is read or inserted.
    """
    if type(order) is not int or not 2 <= order <= 32:
        raise GammaLiError("mutation order must be an integer in 2..32")
    q = _q(anchor)
    if not 0 < q < 1 or q == Q(1, 2):
        raise GammaLiError("a rational off-line anchor in (0,1) is required")
    scale = (q*(q-1))**order
    return (Q(0),)*order + tuple(Q(comb(order, j), 1)/scale for j in range(order+1))


def finite_jet_countermodel_contract(order, anchor=Q(3, 4)):
    """Finite observational agreement, with changed-source scope explicit."""
    polynomial = symmetric_anchor_polynomial(order, anchor)
    q = _q(anchor)
    return {"polynomial_in_s_minus_one": polynomial,
            "same_xi_jet_through": order-1,
            "same_li_coefficients_through": order-1,
            "same_stieltjes_constants_through": order-2,
            "off_line_anchors": (q, 1-q),
            "preserves_completed_reflection": True,
            "preserves_entire_order_at_most_one": True,
            "changes_arithmetic_source": True,
            "original_zeta_counterexample": False,
            "RH_proved": False}
