"""Source-pinned radius transport and genuine prime-power support transitions.

Only finite low forms and operator continuity are certified here. The high
coercivity theorem at a=1/2 is not transported to another radius.
"""
from __future__ import annotations

from fractions import Fraction as F

from . import suzuki_legendre_source as L
from . import source_weil_hierarchy as S
from .all_places_zeta import (
    product_formula_rational, rational_place_valuations, place_primes,
    additive_character_integer_defect,
)
from .suzuki_moment_schur import inverse_neumann_entry
from .tate_suzuki_shorting import verify_original_suzuki_source


class WavefrontTransportError(ValueError):
    pass


def _radius(a):
    a = S.q(a)
    if not 0 < a <= 1:
        raise WavefrontTransportError('exact radius 0<a<=1 required')
    return a


def _mode(i):
    if type(i) is not int or not 1 <= i <= 8:
        raise WavefrontTransportError('positive Legendre mode 1..8 required')
    return i


def active_wavefronts(a):
    """Exact support decision using outward log intervals; ambiguous is rejected."""
    a = _radius(a)
    verify_original_suzuki_source()
    active = []
    for n, p in S.AUTHENTIC_TAPE:
        clock = S.log_iv(n)
        if clock.hi < 2*a:
            active.append((n, p))
        elif clock.lo >= 2*a:
            continue
        else:
            raise WavefrontTransportError('support boundary unresolved by log enclosure')
    return tuple(active)


def hinge_entry(i, j, a, n):
    """Unnormalized physical Legendre form of one authenticated hinge."""
    i, j, a = _mode(i), _mode(j), _radius(a)
    verify_original_suzuki_source()
    if type(n) is not int or n not in dict(S.AUTHENTIC_TAPE):
        raise WavefrontTransportError('genuine source prime-power address required')
    p = dict(S.AUTHENTIC_TAPE)[n]
    active = active_wavefronts(a)
    if (n, p) not in active or (i+j) % 2:
        return S.iv(0)
    poly = L.prime_hinge_integral_polynomial(i, j, a)
    return L.polynomial_interval(poly, S.log_iv(n))*S.log_iv(p)*S.sqrt_inverse(n)


def source_partial_entry(i, j, a, gamma_modes=32):
    """All signed channels, Gamma truncated; no first-prime-only adapter."""
    i, j, a = _mode(i), _mode(j), _radius(a)
    if type(gamma_modes) is not int or not 1 <= gamma_modes <= 64:
        raise WavefrontTransportError('Gamma budget 1..64 required')
    verify_original_suzuki_source()
    active_wavefronts(a)
    if (i+j) % 2:
        return S.iv(0)
    return (L.authentic_gamma_low_entry(i, j, a, gamma_modes)
            + L.authentic_pole_low_entry(i, j, a)
            - S.contact_iv()*inverse_neumann_entry(a, i, j)
            + sum((hinge_entry(i, j, a, n) for n, _ in active_wavefronts(a)), S.iv(0)))


def transported_low_bracket(a, gamma_modes=32):
    """Exact 4x4 Loewner bounds on the low compression on reference interval.

    U_a f(t)=sqrt(2a)f(2at). Reference basis P_i(2t), metric W_i=1/(2i+1).
    Original physical pairings must be divided by 2a, not multiplied.
    Gamma tail is positive and <=tau I; entry rounding uses row-radius norm.
    """
    a = _radius(a)
    entries = tuple(tuple(source_partial_entry(i, j, a, gamma_modes)/(2*a)
                          for j in range(1, 5)) for i in range(1, 5))
    rho = max(sum((z.radius() for z in row), F()) for row in entries)
    mid = tuple(tuple(z.mid() for z in row) for row in entries)
    tau = S.authentic_positive_gamma_tail_norm(gamma_modes)
    lower = tuple(tuple(mid[i][j] - (rho if i == j else 0)
                        for j in range(4)) for i in range(4))
    upper = tuple(tuple(mid[i][j] + (rho+tau/F(2*i+3) if i == j else 0)
                        for j in range(4)) for i in range(4))
    return {'radius': a, 'active_prime_powers': active_wavefronts(a),
            'source': verify_original_suzuki_source(), 'Gamma_modes': gamma_modes,
            'partial_entry_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in entries),
            'interval_row_radius': rho, 'positive_Gamma_tail_norm': tau,
            'reference_metric_diagonal': tuple(F(1, 2*i+3) for i in range(4)),
            'lower_form': lower, 'upper_form': upper,
            'scope': 'FULL_SOURCE_LOW_COMPRESSION_ONLY',
            'high_coercivity_transferred': False, 'Schur_sign_proved': False}


def radius_continuity_bound(a, b, gamma_modes=64):
    """HS/operator bound for transported complete kernels, all 0<a,b<=1.

    For delta>0: 2delta M + 2b(2delta L_J + 2tau_J), where
    M=2 max(a,b)L_J+tau_J. J finite, full Gamma remainder retained.
    Taking J to infinity after delta to zero proves continuity (paper).
    """
    a, b = _radius(a), _radius(b)
    if type(gamma_modes) is not int or not 1 <= gamma_modes <= 128:
        raise WavefrontTransportError('Gamma budget 1..128 required')
    verify_original_suzuki_source()
    delta = abs(a-b)
    if not delta:
        return F()
    lip = S.lipschitz_safe(max(a, b), gamma_modes)
    tail = S.gamma_tail(gamma_modes)
    size = 2*max(a, b)*lip + tail
    # Both orderings are valid; take the smaller multiplier.
    return 2*delta*size + 2*min(a, b)*(2*delta*lip + 2*tail)


def primitive_transport_scale(a):
    """U_a V_a U_a^-1=2a V_ref, hence K transports by (2a)^2."""
    a = _radius(a)
    return {'primitive': 2*a, 'inverse_Neumann': (2*a)**2}


def product_formula_observation(q, primes):
    """Exact rational instance; a fixed prime menu need not see all valuations."""
    q = S.q(q)
    if not q or abs(q.numerator) > 10**10 or q.denominator > 10**10:
        raise WavefrontTransportError('bounded nonzero rational input required')
    primes = place_primes(primes)
    valuations = rational_place_valuations(q)
    partial = abs(q)
    for p in primes:
        partial *= F(p)**(-valuations.get(p, 0))
    return {'input': q, 'observed_primes': primes, 'valuations': valuations,
            'partial_norm_product': partial, 'full_norm_product': product_formula_rational(q),
            'missing_nontrivial_places': tuple(p for p in valuations if p not in primes and valuations[p]),
            'additive_reciprocity_integer_defect': additive_character_integer_defect(q),
            'spectral_tail_bound_obtained': False}
