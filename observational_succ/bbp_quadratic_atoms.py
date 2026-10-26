"""Exact quadratic atomic sources generating the classical 4-pole BBP formula.

The two primitive rational 2x2 transfers H (real split) and G (Gaussian)
produce a fourth-order linear filter and a common eighth-step I/16 return.
All certificates here use exact standard-library Fraction arithmetic and
contain no pi digits, floating-point bounds, or unproved normality claims.

Derived analytic identities (partial fractions, angular and log primitives,
positivity and finite infinite-tail integral) are proved in the companion
research/2026-10-26/BBP_TWO_QUADRATIC_ATOMS.md dossier. They are classical.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial


def clean(a):
    b = list(map(F, a))
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    return tuple(b)


def padd(a, b):
    return clean([F(a[i] if i < len(a) else 0) + F(b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def pscale(a, scalar):
    return clean([F(scalar) * v for v in a])


def pmul(a, b):
    out = [F()] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += F(u) * F(v)
    return clean(out)


def pdivmod(a, b):
    """Exact polynomial Euclidean division, low-first coefficients."""
    a, b = clean(a), clean(b)
    if not any(b):
        raise ZeroDivisionError('zero polynomial divisor')
    if len(a) < len(b):
        return (F(0),), a
    rem = list(a)
    q = [F(0)] * (len(a) - len(b) + 1)
    while len(rem) >= len(b) and any(rem):
        k = len(rem) - len(b)
        leading = rem[-1] / b[-1]
        q[k] += leading
        for j, v in enumerate(b):
            rem[k + j] -= leading * v
        rem = list(clean(rem))
    return clean(q), clean(rem)


def pintegral(a):
    return sum((F(coef, i + 1) for i, coef in enumerate(a)), F(0))


# 1-t^8/16 is the 8-step scalar-return denominator, not primitive.
OCTIC = (F(1), F(0), F(0), F(0), F(0), F(0), F(0), F(0), -F(1, 16))
BBP_TAPS = (F(4), F(0), F(0), F(-2), F(-1), F(-1), F(0), F(0))
P_SOURCE = clean(BBP_TAPS)
D_SPLIT = (F(1), F(0), -F(1, 2))             # det(I-tH)
D_ROTATE = (F(1), F(-1), F(1, 2))           # det(I-tG)
D_MINIMAL = pmul(D_SPLIT, D_ROTATE)
BOUNDARY = (F(4), F(-4))                   # 4(1-t)
D_CANCEL = pmul((F(1), F(0), F(1, 2)),
                (F(1), F(1), F(1, 2)))
# Rational pole denominators: t^2-2t+2 is 2*D_ROTATE.
ANGLE = (F(2), F(-2), F(1))


def source_polynomial_certificate():
    """All identities exact over Q[t]; no analytic continuation invoked."""
    return {
        'P_equals_boundary_times_cancelled': P_SOURCE == pmul(BOUNDARY, D_CANCEL),
        'octic_factorizes': OCTIC == pmul(D_MINIMAL, D_CANCEL),
        'reduced_identity': pmul(P_SOURCE, D_MINIMAL) == pmul(BOUNDARY, OCTIC),
        'd_minimal': D_MINIMAL,
        'numerator': P_SOURCE,
        'cancelled_factor': D_CANCEL,
        'four_pole_labels': (1, 4, 5, 6),
        'numerator_endpoint_zero': sum(P_SOURCE) == 0,
        'first_endpoint_jet': -sum(i * v for i, v in enumerate(P_SOURCE)) == F(15),
        'pi_normality_proved': False,
    }


# Primitive rational 2x2 sources, both start as one 2-state linear step.
HALF = F(1, 2)
G_GAUSSIAN = ((HALF, -HALF), (HALF, HALF))
H_REAL = ((F(0), F(1)), (HALF, F(0)))
IDENTITY = ((F(1), F(0)), (F(0), F(1)))
QUARTER_TURN = ((F(0), F(-1)), (F(1), F(0)))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mpow(a, n):
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative integer power needed')
    v, p = IDENTITY, a
    while n:
        if n & 1:
            v = matmul(v, p)
        p = matmul(p, p)
        n //= 2
    return v


def matrix_atoms_certificate():
    s = lambda r: tuple(tuple(r * v for v in row) for row in IDENTITY)
    q = tuple(tuple(v * F(1, 2) for v in row) for row in QUARTER_TURN)
    return {
        'G2_quarter_turn': mpow(G_GAUSSIAN, 2) == q,
        'H2_half_identity': mpow(H_REAL, 2) == s(HALF),
        'G4_negative': mpow(G_GAUSSIAN, 4) == s(-F(1, 4)),
        'H4_positive': mpow(H_REAL, 4) == s(F(1, 4)),
        'G8_H8_equal': mpow(G_GAUSSIAN, 8) == mpow(H_REAL, 8) == s(F(1, 16)),
        'least_common_positive_scalar_return': next(n for n in range(1, 33)
            if mpow(G_GAUSSIAN, n) == mpow(H_REAL, n)
            and mpow(G_GAUSSIAN, n)[0][1] == 0
            and mpow(G_GAUSSIAN, n)[1][0] == 0
            and mpow(G_GAUSSIAN, n)[0][0] > 0),
        'minimal_real_state_dimension_for_this_reduced_transfer': 4,
    }


def filter_coefficients(count):
    """Fourth-order SUCC recurrence of the BBP Taylor impulse response.

    (1-t+t^3/2-t^4/4) C(t)=4(1-t).  This is the *lower floor*
    from which the BBP four nonzero taps arise every eight steps.
    """
    if type(count) is not int or not 0 <= count <= 3000:
        raise ValueError('finite nonnegative count <=3000')
    out = []
    for n in range(count):
        at = lambda j: out[j] if 0 <= j < len(out) else F(0)
        source = F(4) if n == 0 else F(-4) if n == 1 else F(0)
        out.append(source + at(n - 1) - HALF * at(n - 3) + F(1, 4) * at(n - 4))
    return tuple(out)


def return_tap(n):
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative index')
    q, r = divmod(n, 8)
    return BBP_TAPS[r] * F(1, 16**q)


def authentic_fourpole(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive source time')
    return (F(4, 8*n-7) - F(2, 8*n-4)
            - F(1, 8*n-3) - F(1, 8*n-2))


def moment_from_taps(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive source time')
    return sum((c / (8*(n - 1) + k + 1) for k, c in enumerate(P_SOURCE)), F(0))


def bbp_prefix(N):
    if type(N) is not int or N < 0:
        raise ValueError('nonnegative prefix')
    return sum((authentic_fourpole(k + 1) / 16**k for k in range(N)), F(0))


def four_clock_integral_terms(k):
    """Two period-four streams: one signed radix -4, one unsigned +4.

    The k=2j/2j+1 pairs recover the original four-pole block j, exactly.
    """
    if type(k) is not int or k < 0:
        raise ValueError('nonnegative clock')
    first = F((-1)**k, 4**k) * (F(4, 4*k + 1) + F(2, 4*k + 2)
                                   - F(1, 4*k + 4))
    second = -F(1, 4**k) * (F(2, 4*k + 2) + F(1, 4*k + 4))
    return first, second


def paired_four_clock_prefix(N):
    return sum((sum(four_clock_integral_terms(k)) for k in range(2*N)), F(0))


def rational_radial_completion(N):
    """Exactly rational integrated logarithmic channel at eight-step cutoff.

    R_N=2 integral_0^1 (t^8/16)^N' log((2-t²)/((t-1)²+1)) dt.
    Proof: t^(8N)-16^N divisible by A=t²-2t+2, because
    (1+i)^8=16. The angular incomplete integral equals
    pi+(4/16^N) integral polynomial quotient.
    R_N = bbp_prefix(N)+(4/16^N) integral quotient, exactly Q.
    """
    if type(N) is not int or not 0 <= N <= 64:
        raise ValueError('finite completion horizon <=64')
    poly = [F(0)] * (8*N + 1)
    poly[0] = -F(16**N)
    poly[8*N] += F(1)
    quotient, rem = pdivmod(tuple(poly), ANGLE)
    if any(rem):
        raise ArithmeticError('Gaussian 8th return did not rationalize the log channel')
    return bbp_prefix(N) + F(4, 16**N) * pintegral(quotient)



# The SAME eighth-return rational transfer splits into an angular pi-channel
# and an exact-zero logarithmic channel (a nontrivial "Seinfeld source zero").
# Each channel alone has rational 8-shell moments; cancellation is GLOBAL.
ANGULAR_TAPS = (F(2), F(2), F(1), F(0), -F(1, 2), -F(1, 2), -F(1, 4), F(0))
RADIAL_TAPS = (F(2), -F(2), -F(1), -F(2), -F(1, 2), -F(1, 2), F(1, 4), F(0))


def signed_channel_certificate():
    """Check the exact angular/pi plus radial/null polynomial decomposition.

      P_ang /D8 = 4 /[(t-1)^2+1] ; integral_0^1 = pi.
      P_rad /D8 = 2 d/dt log[(2-t^2)/((t-1)^2+1)]; integral=0.

    Pointwise identities are exact Q[t] and the classical primitives in dossier.
    """
    pa = clean(ANGULAR_TAPS)
    pr = clean(RADIAL_TAPS)
    qreal = (F(2), F(0), F(-1))
    d_pole = pmul(qreal, ANGLE)
    derivative_numerator = padd(pscale(pmul((F(0), F(1)), ANGLE), -4),
                             pscale(pmul((F(-1), F(1)), qreal), -4))
    return {
        'taps_sum_to_original': padd(pa, pr) == P_SOURCE,
        'angular_equals_4_over_angle': pmul(pa, ANGLE) == pscale(OCTIC, 4),
        'radial_equals_logarithmic_derivative': pmul(pr, d_pole) == pmul(OCTIC, derivative_numerator),
        'original_radial_channel_integral': F(0),
        'original_angular_channel_integral': 'pi',
        'pi_normality_proved': False,
    }


def radial_channel_prefix(N):
    if type(N) is not int or not 0 <= N <= 10000:
        raise ValueError('finite nonnegative radial prefix')
    return sum((F(1, 16**k) * sum((co / (8*k + j + 1)
                                         for j, co in enumerate(RADIAL_TAPS)), F())
                for k in range(N)), F())


def angular_channel_prefix(N):
    if type(N) is not int or not 0 <= N <= 10000:
        raise ValueError('finite nonnegative angular prefix')
    return sum((F(1, 16**k) * sum((co / (8*k + j + 1)
                                         for j, co in enumerate(ANGULAR_TAPS)), F())
                for k in range(N)), F())


def same_atoms_different_source(epsilon):
    """Positive source mutant retaining the octic clock and endpoint first jet.

    P_eps = P + eps*(1-t)^2*D_CANCEL. For eps>=0 this is positive
    on [0,1) and has same simple endpoint-zero slope as genuine P,
    but its integral is pi + eps*positive, so NOT original BBP pi.
    No nonnormality claim is made about this mutant.
    """
    eps=F(epsilon)
    if eps < 0:
        raise ValueError('positive perturbation needed for this control')
    return padd(P_SOURCE, pscale(pmul((F(1),F(-2),F(1)),D_CANCEL),eps))


def endpoint_beta_log_rational_part(N):
    """On Beta(8N+1,2): E log[8N(1-t)] = log(8N)+ 1-H_(8N+2).

    Returns only the EXACT RATIONAL shift 1-H_(8N+2).
    Log(8N) and gamma remain analytic, not hard-coded finite values.
    """
    if type(N) is not int or not 1 <= N <= 10000:
        raise ValueError('positive index')
    return F(1)-sum((F(1,j) for j in range(1,8*N+3)),F())


def green_tail_bounds(N):
    """Rational outward enclosure for the authentic positive BBP Green tail.

    T_N = integral_0^1 t^(8N)(1-t)/[(2-t²)((t-1)²+1)] dt.
    1/[K(K+1)] - 6/[K(K+1)(K+2)] <= T_N <= 1/[K(K+1)]
    where K=8N+1, since 0<=1-1/D2<=3(1-t) on [0,1].
    """
    if type(N) is not int or not 1 <= N <= 1000000:
        raise ValueError('positive exact Green index')
    a = 8*N+1
    b = F(1, a*(a+1))
    return b - F(6, a*(a+1)*(a+2)), b


def bbp_remainder_bounds(N):
    """pi-bbp_prefix(N)=16^(1-N)*T_N; exact certified rational bounds."""
    lo, hi = green_tail_bounds(N)
    return F(16, 16**N)*lo, F(16, 16**N)*hi


def source_status():
    return {'original_four_pole_unchanged': True,
            'exact_two_quadratic_reduction': True,
            'classical_BBP_integral_proved': True,
            'is_a_new_source_specific_signed_Weyl_bound': False,
            'pi_normality_proved': False,
            'RH_proved': False}
