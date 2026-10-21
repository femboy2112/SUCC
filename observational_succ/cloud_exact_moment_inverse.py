"""Exact finite-moment refinement of a constrained primitive inverse.

All inequalities are rational. Source identification is the responsibility of
the separately pinned source probe; this module cannot confer proof authority.
See CLOUD_EXACT_MOMENT_INVERSE.md for the Hilbert-space theorem and errors.
"""
from fractions import Fraction as Q

from . import cloud_operator_transport as C


def constraints(parity):
    if parity == 'even':
        return ((Q(1),), (Q(-1, 2), Q(), Q(6)))
    if parity == 'odd':
        return ((Q(), Q(2)), (Q(), Q(-3), Q(), Q(20)))
    raise ValueError('primitive parity must be even or odd')


def matrix_psd(a):
    return (a[0][1] == a[1][0] and a[0][0] >= 0 and a[1][1] >= 0
            and a[0][0]*a[1][1] >= a[0][1]**2)


def matrix_pd(a):
    return (a[0][1] == a[1][0] and a[0][0] > 0
            and a[0][0]*a[1][1] > a[0][1]**2)


def inverse2(a):
    a = tuple(tuple(C.exact(x) for x in row) for row in a)
    if len(a) != 2 or any(len(row) != 2 for row in a) or not matrix_pd(a):
        raise ValueError('exact symmetric positive definite 2 by 2 matrix required')
    determinant = a[0][0]*a[1][1]-a[0][1]**2
    return ((a[1][1]/determinant, -a[0][1]/determinant),
            (-a[1][0]/determinant, a[0][0]/determinant))


def matrix_add(a, b, scale=1):
    scale = C.exact(scale)
    return tuple(tuple(a[i][j]+scale*b[i][j] for j in range(2)) for i in range(2))


def grid_upper(a, denominator=10**24):
    """A symmetric Loewner upper: <3/grid diagonal increase, including 2/grid safety."""
    if type(denominator) is not int or denominator <= 0:
        raise ValueError('positive integer grid denominator')
    return tuple(tuple(Q(-((-x.numerator*denominator)//x.denominator), denominator)
                       + (Q(2, denominator) if i == j else 0)
                       for j, x in enumerate(row)) for i, row in enumerate(a))


def _derivative(poly):
    return tuple(k*poly[k] for k in range(1, len(poly))) or (Q(),)


def _value(poly, x):
    # Horner evaluation is independent of the antiderivative pairing route.
    result = Q()
    for coefficient in reversed(poly):
        result = result*x+coefficient
    return result


def simpson_enclosure(poly, left, right, cells=32):
    """Composite Simpson with a rigorous fourth-derivative error on I.

    `cells` is an even number of subintervals of [left,right], which must lie
    in [-1/2,1/2]. This routine never calls polynomial antiderivatives.
    """
    poly = tuple(C.exact(x) for x in poly)
    left, right = C.exact(left), C.exact(right)
    if (type(cells) is not int or cells < 2 or cells % 2
            or not Q(-1, 2) <= left < right <= Q(1, 2)):
        raise ValueError('even positive grid and ordered subinterval of I required')
    step = (right-left)/cells
    total = _value(poly, left)+_value(poly, right)
    for i in range(1, cells):
        total += (4 if i % 2 else 2)*_value(poly, left+i*step)
    fourth = poly
    for _ in range(4):
        fourth = _derivative(fourth)
    error = (right-left)*step**4*C.sup_bound(fourth)/180
    return total*step/3, error


def constraint_gram(b, db, kappa, parity, w=Q(12, 25), cells=32):
    """M_b=L*B_b^-1 L and two independent certified upper enclosures.

    The first integrates polynomial antiderivatives exactly. The second uses
    only composite Simpson values with fourth-derivative remainders. Both pay
    the uncertainty in the true b and outward rational matrix rounding.
    """
    b, db, kappa, w = map(C.exact, (b, db, kappa, w))
    if db < 0 or not Q(1, 2) < b-db <= b+db < 1 or kappa <= 0 or w < 0:
        raise ValueError('invalid exact shift, uncertainty, gap or weight')
    h = constraints(parity)
    inv_h = tuple(C.inverse_polynomial_pieces(q, b, kappa, w) for q in h)
    whole = tuple(((Q(-1, 2), Q(1, 2), q),) for q in h)
    gram = tuple(tuple(C.piece_pairing(whole[i], inv_h[j])
                       for j in range(2)) for i in range(2))
    if not matrix_pd(gram):
        raise ArithmeticError('positive constraint Gram theorem failed')
    cross = w/(kappa*(kappa+2*w))
    directed_error = tuple(tuple(db*C.sup_bound(h[i])*
                                (4*C.sup_bound(h[j])/kappa
                                 + cross*C.sup_bound(_derivative(h[j])))
                                for j in range(2)) for i in range(2))
    errors = tuple(tuple(min(directed_error[i][j], directed_error[j][i])
                         for j in range(2)) for i in range(2))
    radius = max(sum(row, Q()) for row in errors)
    upper = grid_upper(tuple(tuple(gram[i][j]+(radius if i == j else 0)
                                   for j in range(2)) for i in range(2)))
    quadrature = []
    quadrature_errors = []
    for i in range(2):
        row, error_row = [], []
        for j in range(2):
            value = error = Q()
            for left, right, polynomial in inv_h[j]:
                part, remainder = simpson_enclosure(
                    C.poly_mul(h[i], polynomial), left, right, cells)
                value += part
                error += remainder
            row.append(value)
            error_row.append(error)
        quadrature.append(tuple(row))
        quadrature_errors.append(tuple(error_row))
    mid = tuple(tuple((quadrature[i][j]+quadrature[j][i])/2
                      for j in range(2)) for i in range(2))
    q_errors = tuple(tuple((quadrature_errors[i][j]+quadrature_errors[j][i])/2
                           + errors[i][j] for j in range(2)) for i in range(2))
    q_radius = max(sum(row, Q()) for row in q_errors)
    q_upper = grid_upper(tuple(tuple(mid[i][j]+(q_radius if i == j else 0)
                                     for j in range(2)) for i in range(2)))
    # Independent enclosure checks; no rounded eigenvalue ordering is used.
    if not all(abs(quadrature[i][j]-gram[i][j]) <= quadrature_errors[i][j]
               for i in range(2) for j in range(2)):
        raise ArithmeticError('independent Simpson enclosure misses exact Gram')
    return {'nominal_gram': gram, 'shift_entry_errors': errors,
            'shift_operator_radius': radius, 'gram_upper': upper,
            'inverse_lower': inverse2(upper),
            'quadrature_values': tuple(quadrature),
            'quadrature_errors': tuple(quadrature_errors),
            'quadrature_gram_upper': q_upper,
            'quadrature_inverse_lower': inverse2(q_upper),
            'quadrature_cells_per_piece': cells,
            'independent_quadrature_enclosures_verified': True}


def _weighted_lower(weight, moments, errors, theta):
    """Reverse Young for (Z+Δ)*W(Z+Δ), W PSD, with entrywise |Δ|≤errors."""
    if not matrix_psd(weight):
        raise ValueError('a positive weight is required for reverse Young')
    nominal = tuple(tuple(sum((moments[a][i]*weight[a][b]*moments[b][j]
                               for a in range(2) for b in range(2)), Q())
                          for j in range(2)) for i in range(2))
    energy_error = sum((abs(weight[a][b])*errors[a][i]*errors[b][i]
                        for i in range(2) for a in range(2) for b in range(2)), Q())
    penalty = (1/theta-1)*energy_error
    lower = tuple(tuple((1-theta)*nominal[i][j]-(penalty if i == j else 0)
                        for j in range(2)) for i in range(2))
    return lower, nominal, penalty


def exact_moment_constraint_saving(projected, b, db, kappa, parity,
                                   w=Q(12, 25), theta=Q(1, 1024), cells=32):
    """Certified additive gain beyond the earlier diagonal moment bound.

    The general exact-Gram inverse bound always exists. An additive improvement
    over the old diagonal estimate is returned only when its exact weight
    difference is PSD. Failure of that sufficient check is not source failure.
    """
    old = C.moment_constraint_saving(projected, b, db, kappa, parity, w, theta)
    kappa, theta = C.exact(kappa), C.exact(theta)
    packet = constraint_gram(b, db, kappa, parity, w, cells)
    old_weight = tuple(tuple(kappa/old['constraint_norms'][i] if i == j else Q()
                             for j in range(2)) for i in range(2))
    result = {'previous_certificate': old, 'gram_certificate': packet,
              'previous_weight': old_weight, 'theta': theta}
    for prefix, key in (('exact', 'inverse_lower'),
                        ('quadrature', 'quadrature_inverse_lower')):
        excess = matrix_add(packet[key], old_weight, -1)
        supported = matrix_psd(excess)
        result[prefix+'_weight_excess'] = excess
        result[prefix+'_weight_excess_psd'] = supported
        if supported:
            lower, nominal, penalty = _weighted_lower(
                excess, old['nominal_inverse_moments'], old['moment_error_bounds'], theta)
            result[prefix+'_additional_saving_lower'] = lower
            result[prefix+'_nominal_additional_saving'] = nominal
            result[prefix+'_additional_error_penalty'] = penalty
            result[prefix+'_combined_constraint_saving_lower'] = matrix_add(
                old['constraint_saving_lower'], lower)
    return result
