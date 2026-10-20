"""Exact holdouts for primitive completion and constrained inverse transport.

Finite arithmetic here checks the paper formulas; it does not authenticate a
source or prove an infinite-dimensional statement by testing finite matrices.
The optional source probe supplies its own pinned source inputs.
"""
from fractions import Fraction as Q
from math import comb, isqrt


def exact(value):
    if type(value) not in (int, Q):
        raise ValueError("exact int or Fraction required")
    return Q(value)


def poly_add(a, b):
    return tuple((a[k] if k < len(a) else Q()) +
                 (b[k] if k < len(b) else Q())
                 for k in range(max(len(a), len(b))))


def poly_scale(a, scalar):
    scalar = exact(scalar)
    return tuple(exact(x) * scalar for x in a)


def poly_mul(a, b):
    out = [Q()] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += exact(x) * exact(y)
    return tuple(out)


def poly_shift(a, shift):
    """Coefficients of a(x + shift), by the binomial identity."""
    shift = exact(shift)
    return tuple(sum((exact(a[j]) * comb(j, k) * shift**(j-k)
                      for j in range(k, len(a))), Q())
                 for k in range(len(a)))


def integrate(a, left=Q(-1, 2), right=Q(1, 2)):
    left, right = exact(left), exact(right)
    return sum((exact(c) * (right**(k+1)-left**(k+1))/(k+1)
                for k, c in enumerate(a)), Q())


def sup_bound(a):
    """Monomial triangle upper bound on the complete interval [-1/2,1/2]."""
    return sum((abs(exact(c))/2**k for k, c in enumerate(a)), Q())


def piece_sup_bound(a, left, right):
    """Endpoint + Cauchy-Schwarz bound avoids Taylor-coefficient cancellation."""
    derivative = tuple(k*exact(a[k]) for k in range(1,len(a))) or (Q(),)
    energy = (right-left)*integrate(poly_mul(derivative, derivative), left, right)
    if energy < 0:
        raise ValueError("negative exact derivative energy")
    scale = 10**24
    radical_upper = Q(isqrt(energy.numerator*scale**2//energy.denominator)+1, scale)
    endpoint = sum((exact(c)*left**k for k,c in enumerate(a)), Q())
    return min(sup_bound(a), abs(endpoint)+radical_upper)


def inverse_polynomial_pieces(q, b, kappa, w):
    """Exact B_b^-1 q for B_b=kappa I+w(I-A_b), 1/2<b<1."""
    b, kappa, w = map(exact, (b, kappa, w))
    q = tuple(map(exact, q))
    if not Q(1, 2) < b < 1 or kappa <= 0 or w < 0:
        raise ValueError("two-edge geometry, positive gap, nonnegative weight")
    den = kappa*(kappa+2*w)
    direct, cross = (kappa+w)/den, w/den
    return ((Q(-1, 2), Q(1, 2)-b,
             poly_add(poly_scale(q, direct), poly_scale(poly_shift(q, b), cross))),
            (Q(1, 2)-b, b-Q(1, 2), poly_scale(q, 1/(kappa+w))),
            (b-Q(1, 2), Q(1, 2),
             poly_add(poly_scale(q, direct), poly_scale(poly_shift(q, -b), cross))))


def piece_pairing(first, second):
    total = Q()
    for left, right, a in first:
        for low, high, b in second:
            lo, hi = max(left, low), min(right, high)
            if lo < hi:
                total += integrate(poly_mul(a, b), lo, hi)
    return total


def moment_constraint_saving(projected, b, db, kappa, parity,
                             w=Q(12, 25), theta=Q(1, 1024)):
    """Certified 2x2 lower for the polynomial-constraint inverse correction.

    The TRUE shift lies in [b-db,b+db]. The supplied residual approximants
    have exact zero moments through degree 3. No source authority is implied
    by a caller's parameters. The source probe checks actual provenance.
    """
    b, db, kappa, w, theta = map(exact, (b, db, kappa, w, theta))
    if (db < 0 or not Q(1, 2) < b-db <= b+db < 1 or
            kappa <= 0 or w < 0 or not 0 < theta < 1 or len(projected) != 2):
        raise ValueError("invalid exact constraint certificate parameters")
    if parity == "even":
        constraints = ((Q(1),), (Q(-1, 2), Q(), Q(6)))
    elif parity == "odd":
        constraints = ((Q(), Q(2)), (Q(), Q(-3), Q(), Q(20)))
    else:
        raise ValueError("primitive parity must be even or odd")
    expected = ((Q(-1, 2), Q(1, 2)-b),
                (Q(1, 2)-b, b-Q(1, 2)), (b-Q(1, 2), Q(1, 2)))
    for pieces in projected:
        if tuple((a, z) for a, z, _ in pieces) != expected:
            raise ValueError("complete nominal source partition required")
        for degree in range(4):
            polynomial = (Q(),)*degree + (Q(1),)
            if piece_pairing(pieces, ((Q(-1,2), Q(1,2), polynomial),)):
                raise ValueError("nominal residual is outside the high moment space")
    norms = [integrate(poly_mul(q, q)) for q in constraints]
    assert integrate(poly_mul(*constraints)) == 0
    maxima = [max(piece_sup_bound(p, a, z) for a, z, p in pieces)
              for pieces in projected]
    z = []
    errors = []
    cross = w/(kappa*(kappa+2*w))
    for q in constraints:
        inverse_q = inverse_polynomial_pieces(q, b, kappa, w)
        z.append(tuple(piece_pairing(pieces, inverse_q) for pieces in projected))
        derivative = tuple(k*q[k] for k in range(1, len(q))) or (Q(),)
        factor = db*(4*sup_bound(q)/kappa + cross*sup_bound(derivative))
        errors.append(tuple(factor*s for s in maxima))
    nominal = tuple(tuple(kappa*sum((z[j][i]*z[j][k]/norms[j]
                                    for j in range(2)), Q())
                          for k in range(2)) for i in range(2))
    penalty = (1/theta-1)*kappa*sum(
        (e*e/norms[j] for j in range(2) for e in errors[j]), Q())
    lower = tuple(tuple((1-theta)*nominal[i][k] - (penalty if i == k else 0)
                        for k in range(2)) for i in range(2))
    return {"primitive_parity": parity, "nominal_inverse_moments": z,
            "moment_error_bounds": errors, "constraint_norms": norms,
            "nominal_saving": nominal, "penalty": penalty,
            "constraint_saving_lower": lower, "theta": theta}


def nonclosable_sequence_pair(m, n):
    """Exact sequence proof data for F_m=(1/m,...,1/m,0,...).

    On l2, q(F)=||F||²+|sum F_n|² (domain V(l2), V=diag(1/n)).
    F_m -> 0; q(F_m-F_n) -> 0; q(F_m) -> 1, contradicting closability.
    """
    if type(m) is not int or type(n) is not int or min(m, n) < 1:
        raise ValueError("positive integer sequence indices required")
    return {"norm2_Fm": Q(1, m), "q_Fm": 1+Q(1,m),
            "q_difference": Q(1,m)+Q(1,n)-Q(2,max(m,n)),
            "original_u_norm2": Q((m+1)*(2*m+1), 6*m)}
