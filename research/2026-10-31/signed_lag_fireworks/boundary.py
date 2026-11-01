"""Exact finite instruments for two-scale energy and dyadic BBP shadows.

Analytic statements and quantifiers are proved in BOUNDARY.md. Symbolic seeds
q-pi/16 are never represented as rational values or confused with seed zero.
"""
from fractions import Fraction as F


def _positive(value, name):
    if type(value) is not int or value < 1:
        raise ValueError(name + ' must be a positive integer')


def _phases(z):
    if not z:
        raise ValueError('nonempty rational Gaussian phase sequence')
    out = []
    for a, b in z:
        if type(a) not in (int, F) or type(b) not in (int, F):
            raise ValueError('exact rational coordinates required')
        if a*a+b*b > 1:
            raise ValueError('phase norms must be at most one')
        out.append((F(a), F(b)))
    return tuple(out)


def window_energy(z, K):
    """B_N,K for zero-extended exact rational Gaussian inputs, no trig."""
    _positive(K, 'K')
    z = _phases(z)
    N = len(z)
    total = F(0)
    for t in range(N+K-1):
        window = z[max(0, t-K+1):min(N, t+1)]
        a = sum((x[0] for x in window), F(0))
        b = sum((x[1] for x in window), F(0))
        total += a*a+b*b
    return total/(N*K*K)


def two_scale_energy_upper(small_energy, K, m):
    """Jensen bound B_N,K <= (K-r)/K B_N,m + r/K, r=K mod m."""
    _positive(K, 'K')
    _positive(m, 'm')
    if m > K or type(small_energy) not in (int, F) or not 0 <= small_energy <= 1:
        raise ValueError('1<=m<=K and exact small energy in [0,1]')
    r = K % m
    return F(K-r, K)*small_energy + F(r, K)


def selected_state(M):
    """Original four signed poles and literal zero boundary, exact lift."""
    _positive(M, 'M')
    u = F(0)
    for n in range(1, M+1):
        forcing = F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)
        u = 16*u+forcing
    return u


def shadow_rounding_depth(M):
    """Least J with 16^J >= 64 M^2; logarithmic delay to coherence."""
    _positive(M, 'M')
    J, scale = 0, 1
    while scale < 64*M*M:
        J, scale = J+1, scale*16
    return J


def dyadic_shadow(M, J=None):
    """Return rational target q; the changed seed is SYMBOLIC q-pi/16.

    Its distance to zero is < seed_distance_upper. Its completed orbit
    becomes integral at time coherence_start=M+J for every fixed harmonic.
    """
    _positive(M, 'M')
    if J is None:
        J = shadow_rounding_depth(M)
    if type(J) is not int or J < 0:
        raise ValueError('J must be a nonnegative integer')
    u = selected_state(M)
    scale = 16**J
    a = (scale*u.numerator)//u.denominator
    delta = u-F(a, scale)
    tail_upper = F(1, 64*M*M)
    budget = tail_upper+F(1, scale)
    return {'M': M, 'J': J, 'q': F(a, 16**(M+J)),
            'rounding_defect': delta, 'coherence_start': M+J,
            'tail_upper': tail_upper,
            'seed_distance_upper': budget/16**M}


def shadow_prefix_weyl_error_upper(M, h=1, J=None):
    """Strict upper for entire first M complex-sum error; pi<22/7."""
    if type(h) is not int or not h:
        raise ValueError('nonzero integer harmonic')
    data = dyadic_shadow(M, J)
    return F(44*abs(h), 7)*data['seed_distance_upper']*F(16*(16**M-1), 15)


def shadow_lag_error_upper(M, N, K, h=1, J=None):
    """Strict selected-prefix lag-score error bound for symbolic shadow."""
    _positive(N, 'N')
    _positive(K, 'K')
    if N > M or K > N or type(h) is not int or not h:
        raise ValueError('N<=M, K<=N, and nonzero integer harmonic')
    d = dyadic_shadow(M, J)['seed_distance_upper']
    weighted = sum((F(K-k, K)*(16**k-1)*F(16*(16**(N-k)-1), 15)
                    for k in range(1, K)), F(0))
    return F(88*abs(h), 7*K*N)*d*weighted


def shadow_lag_lower(N, K, h, M, J=None):
    """All-N lower bound from original transport and finite-prefix penalty.

    Uses PR434's conservative all-source error, not the improved clipped
    transport in this dossier. Fixed shadow: critical-log score tends to one.
    """
    _positive(N, 'N')
    _positive(K, 'K')
    if K > N or type(h) is not int or not h:
        raise ValueError('K<=N and nonzero integer harmonic')
    L = dyadic_shadow(M, J)['coherence_start']
    mass = F(K-1, K)*(1-F(K+1, 3*N))
    error = F(11*abs(h), 28*K*N)*sum(
        (F(K-k, K)*(16**k-1) for k in range(1, K)), F(0))
    prefix = F(4, K*N)*sum((F(K-k, K)*min(N-k, L-1)
                            for k in range(1, K)), F(0))
    return mass-error-prefix
