#!/usr/bin/env python3
"""Bounded hostile audit; independent exact witnesses, then landed API probes.

No zeros, full test suite, Lean compilation, commits, or source mutations.
Polynomial hinge expectations use twice integrated primitives and translated
overlaps, not the producer's difference-correlation/hinge-polynomial algorithm.
Passing this audit never establishes the original Suzuki Schur sign.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha1, sha256
import importlib
from itertools import combinations, permutations
import json
from math import comb, isqrt
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
PIN = '0cc8510b71d178fc79e8d410a86d8b6014cf9178'
ORIGIN = 'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc'
SOURCE = 'observational_succ/source_weil_hierarchy.py'
MODULES = ('prime_wavefront_geometry', 'spectral_response',
           'arithmetic_source_range', 'arithmetic_resolvent', 'cross_prime_wavefront',
           'spectral_tail_contract')
CHECKS = []
EVIDENCE = {}
PENDING = []


def check(name, condition, **evidence):
    CHECKS.append({'name': name, 'pass': bool(condition), **evidence})


def rejects(name, call):
    try:
        call()
    except (ValueError, TypeError, ArithmeticError) as exc:
        check(name, True, exception=type(exc).__name__, message=str(exc))
    else:
        check(name, False, reason='invalid input accepted')


def add(p, q, scale=F(1)):
    return tuple((p[i] if i < len(p) else F()) +
                 scale*(q[i] if i < len(q) else F())
                 for i in range(max(len(p), len(q))))


def mul(p, q):
    out = [F()]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return tuple(out)


def derivative(p):
    return tuple(i*p[i] for i in range(1, len(p))) or (F(),)


def value(p, x):
    out = F()
    for c in reversed(p):
        out = out*x+c
    return out


def primitive(p, left):
    out = (F(),)+tuple(c/F(i+1) for i, c in enumerate(p))
    return add(out, (-value(out, left),))


def integral(p, left, right):
    prim = primitive(p, left)
    return value(prim, right)


def shift(p, h):
    return tuple(sum((p[k]*comb(k, j)*h**(k-j)
                      for k in range(j, len(p))), F()) for j in range(len(p)))


def legendre(n, a=F(1, 2)):
    """Three-term recurrence, physical P_n(x/a)."""
    p, q = (F(1),), (F(), 1/a)
    if not n:
        return p
    for k in range(1, n):
        p, q = q, tuple(v/F(k+1) for v in
                        add(mul((F(), F(2*k+1)/a), q), p, -F(k)))
    return q


def norm2(p, a=F(1, 2)):
    return integral(mul(p, p), -a, a)


def log_box(n, terms=100):
    """Independent rational atanh series with a positive geometric tail."""
    k, x = 0, F(n)
    while x >= 2:
        x /= 2
        k += 1

    def unit(z):
        t = (z-1)/(z+1)
        lo = sum((2*t**(2*j+1)/F(2*j+1) for j in range(terms)), F())
        return lo, lo+2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    lo, hi = unit(x)
    l2, h2 = unit(F(2))
    return round_box((lo+k*l2, hi+k*h2), 70)


def round_box(box, digits=70):
    grid = 10**digits
    lo, hi = box
    return (F(lo.numerator*grid//lo.denominator, grid),
            -F((-hi).numerator*grid//hi.denominator, grid))


def ivmul(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def ivadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def ivscale(a, c):
    return ivmul(a, (c, c))


def ivpoly(p, x):
    out = F(), F()
    for c in reversed(p):
        out = ivadd(ivmul(out, x), (c, c))
    return out


def exp_box(x):
    """Outward rational exponential; positive series and exact geometric tail."""
    if x < 0:
        lo, hi = exp_box(-x)
        return round_box((1/hi, 1/lo), 90)
    squarings = 0
    while x > F(1, 2):
        x /= 2
        squarings += 1
    term, total = F(1), F(1)
    for n in range(1, 90):
        term *= x/n
        total += term
    nxt = term*x/90
    box = round_box((total, total+nxt/(1-x/91)), 90)
    grid = 10**90
    for _ in range(squarings):
        lo, hi = box[0]**2, box[1]**2
        box = F(lo.numerator*grid//lo.denominator, grid), -F((-hi).numerator*grid//hi.denominator, grid)
    return box


def exp_poly_integral(p, h, alpha):
    """Integral_0^h p(r) exp(-alpha*r) by scalar moment recurrence."""
    e = exp_box(-alpha*h)
    moment = ivscale(ivadd((F(1), F(1)), ivscale(e, -1)), 1/alpha)
    out = ivscale(moment, p[0])
    for k in range(1, len(p)):
        moment = ivscale(ivadd(ivscale(moment, F(k)), ivscale(e, -h**k)), 1/alpha)
        out = ivadd(out, ivscale(moment, p[k]))
    return out


def independent_derivative_box(mode, x, J):
    """Different integration representation; shares pinned contact enclosure.

    Substitute r=x-y, split positive/negative r, and integrate scalar moments.
    No producer derivative, antiderivative, Legendre or matrix helper is used.
    """
    S = importlib.import_module('observational_succ.source_weil_hierarchy')
    poly = legendre(mode)
    shifted = shift(poly, x)
    positive = tuple((-1)**k*v for k, v in enumerate(shifted))
    negative = shifted
    contact = S.contact_iv()
    log2 = log_box(2)
    grid = 10**70
    root = isqrt(2*grid*grid)
    weight = ivmul(log2, (F(grid, root+1), F(grid, root)))

    def side(p, h):
        out = ivadd(ivscale(exp_poly_integral(p, h, -F(1, 2)), -F(2)),
                    ivscale(exp_poly_integral(p, h, F(1, 2)), F(2)))
        out = ivadd(out, ivscale((contact.lo, contact.hi), integral(p, F(), h)/2))
        if h > log2[1]:
            prim = primitive(p, F())
            mass = ivadd((value(prim, h),)*2, ivscale(ivpoly(prim, log2), -1))
            out = ivadd(out, ivmul(weight, mass))
        else:
            assert h <= log2[0]
        for j in range(J):
            d = 4*j+1
            out = ivadd(out, ivscale(exp_poly_integral(p, h, F(d, 2)), -F(2, d)))
        return out
    return round_box(ivadd(side(positive, x+F(1, 2)), ivscale(side(negative, F(1, 2)-x), -1)), 60)


def hinge_primitive_pair(i, j, a, ell):
    """-integral F(y+ell)H(y)-integral F(y-ell)H(y), zero extensions."""
    if ell >= 2*a or (i+j) % 2:
        return F()
    fp = primitive(legendre(i, a), -a)
    hp = primitive(legendre(j, a), -a)
    assert value(fp, a) == value(hp, a) == 0
    return (-integral(mul(shift(fp, ell), hp), -a, a-ell)
            -integral(mul(shift(fp, -ell), hp), -a+ell, a))


def independent_hinge_box(i, j, a, n, p):
    ell = log_box(n)
    if ell[0] >= 2*a or (i+j) % 2:
        return F(), F()
    assert ell[1] < 2*a
    midpoint = sum(ell)/2
    center = hinge_primitive_pair(i, j, a, midpoint)
    # |P_n(x/a)|<=1, so derivative of the double hinge form in ell
    # is bounded by the area (2a)^2. This controls uncertain log n.
    error = (2*a)**2*(ell[1]-ell[0])/2
    grid = 10**70
    floor = isqrt(n*grid*grid)
    invsqrt = F(grid, floor+1), F(grid, floor)
    return ivmul((center-error, center+error), ivmul(log_box(p), invsqrt))


def matmul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def inverse(a):
    n = len(a)
    rows = [list(map(F, row))+[F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        d = rows[k][k]
        rows[k] = [x/d for x in rows[k]]
        for i in range(n):
            if i != k:
                c = rows[i][k]
                rows[i] = [x-c*y for x, y in zip(rows[i], rows[k])]
    return tuple(tuple(row[n:]) for row in rows)


def subtract(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))


def determinant(a):
    n = len(a)
    total = F()
    for order in permutations(range(n)):
        sign = (-1)**sum(order[i] > order[j] for i in range(n) for j in range(i+1, n))
        term = F(sign)
        for i, j in enumerate(order):
            term *= a[i][j]
        total += term
    return total


def psd(a):
    """Independent principal-minor criterion, matrices of size at most four."""
    assert 1 <= len(a) <= 4
    if tuple(map(tuple, a)) != transpose(a):
        return False
    return all(determinant(tuple(tuple(a[i][j] for j in ix) for i in ix)) >= 0
               for size in range(1, len(a)+1) for ix in combinations(range(len(a)), size))


def source_pins():
    raw = (ROOT/SOURCE).read_bytes()
    blob = sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    origin = subprocess.run(['git', 'show', ORIGIN+':'+SOURCE], cwd=ROOT,
                            capture_output=True, check=True, timeout=10).stdout
    check('live source and originating commit byte-identical', raw == origin and blob == PIN,
          blob=blob, sha256=sha256(raw).hexdigest(), origin=ORIGIN)
    EVIDENCE['source_before'] = sha256(raw).hexdigest()


def independent_proofs():
    p4, p6 = legendre(4), legendre(6)
    f = add(p6, p4, -F(1, 2))
    before = norm2(derivative(f))*norm2(f)
    after = norm2(derivative(p6))*norm2(p6)
    check('REFUTED derivative HS contraction through four-low compression',
          before == F(147, 26) and after == F(84, 13) and after > before,
          G='f tensor f, f=P6(2t)-P4(2t)/2', derivative_HS_squared=before,
          compressed_derivative_HS_squared=after, squared_ratio=after/before)
    # Projection after differentiation is contractive: polynomial coefficients
    # are removed using actual L2 inner products, not derivative coefficients.
    d = derivative(f)
    projected = d
    for j in range(1, 5):
        pj = legendre(j)
        coeff = integral(mul(d, pj), -F(1, 2), F(1, 2))/norm2(pj)
        projected = add(projected, pj, -coeff)
    check('projection AFTER derivative positive control', norm2(projected) <= norm2(d))
    # Weighted derivative diagonalization survives the hostile witness.
    weighted_before = integral(mul((F(1, 4), F(), -F(1)), mul(d, d)), -F(1, 2), F(1, 2))
    dp6 = derivative(p6)
    weighted_after = integral(mul((F(1, 4), F(), -F(1)), mul(dp6, dp6)), -F(1, 2), F(1, 2))
    check('weighted Legendre derivative contraction survives', weighted_after <= weighted_before,
          before=weighted_before, after=weighted_after)
    D = ((F(2), F(1)), (F(1), F(2)))
    b = ((F(1),), (F(),))
    response = matmul(transpose(b), matmul(inverse(D), b))[0][0]
    finite = F(1, 2)
    A = F(3, 5)
    check('finite response is LOWER; finite short is UPPER', response == F(2, 3) and finite < response,
          finite_response=finite, full_response=response, finite_short=A-finite, true_short=A-response)
    check('positive finite short does not certify full sign', A-finite > 0 > A-response)
    for n in (2, 7, 31):
        delta, bnorm = F(1, n*n), F(1, n)
        check(f'soft mode response remains one at n={n}', bnorm*bnorm/delta == 1,
              compact_eigenvalue=delta, cross_norm=bnorm)
    # Range countermodel: D_n=n^-4,b_n=n^-3; D^-1/2 b=(1/n) in l2,
    # whereas D^-1 b=(n) not in l2. Proof is in the paper, this is exact data.
    EVIDENCE['range_countermodel'] = {'D_n': 'n^-4', 'b_n': 'n^-3',
        'energy_response_n': '1/n', 'inverse_response_n': 'n',
        'bounded_inverse_claim': 'REFUTED', 'source_specific': False}
    for a in (F(1, 4), F(1, 2), F(3, 4), F(1)):
        # Polynomial kernel g(r)=r^2 gives an exact nontrivial scaling control.
        physical = -2*integral(mul((F(), F(1)), legendre(1, a)), -a, a)**2
        ref = -2*(2*a)**3*integral(mul((F(), F(1)), legendre(1)), -F(1, 2), F(1, 2))**2
        check(f'unitary kernel factor and physical form division a={a}', physical/(2*a) == ref,
              physical_form=physical, reference_form=ref)
        kp = norm2(primitive(legendre(1, a), -a), a)
        kr = norm2(primitive(legendre(1), -F(1, 2)))
        check(f'unitary primitive squared scale a={a}', kp/(2*a) == (2*a)**2*kr)
    # At ell=0 the hinge is the Green identity -2 <Vf,Vh>.
    for i, j in ((1, 1), (2, 4), (5, 7)):
        target = -2*integral(mul(primitive(legendre(i), -F(1, 2)),
                                 primitive(legendre(j), -F(1, 2))), -F(1, 2), F(1, 2))
        check(f'independent hinge zero-threshold calibration {i},{j}',
              hinge_primitive_pair(i, j, F(1, 2), F()) == target)


def audit_cross_prime():
    C = importlib.import_module('observational_succ.cross_prime_wavefront')
    S = importlib.import_module('observational_succ.source_weil_hierarchy')
    witnesses = []
    for a, expected in ((F(1, 4), ()), (F(1, 2), ((2, 2),)),
                        (F(3, 4), ((2, 2), (3, 3), (4, 2))),
                        (F(1), ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7)))):
        check(f'prime-power support a={a}', C.active_wavefronts(a) == expected)
        check(f'primitive transport API a={a}', C.primitive_transport_scale(a) ==
              {'primitive': 2*a, 'inverse_Neumann': (2*a)**2})
        for n, p in expected:
            for i, j in ((1, 1), (1, 3), (2, 4), (3, 4)):
                lo, hi = independent_hinge_box(i, j, a, n, p)
                z = C.hinge_entry(i, j, a, n)
                check(f'true hinge primitive-overlap enclosure a={a},n={n},i={i},j={j}',
                      z.lo <= lo <= hi <= z.hi)
                witnesses.append({'a': a, 'n': n, 'i': i, 'j': j,
                                  'independent': (lo, hi), 'producer': (z.lo, z.hi)})
    EVIDENCE['independent_hinges'] = witnesses
    for a in (F(), -F(1), F(1001, 1000), 0.5, True):
        rejects(f'cross radius rejects {a!r}', lambda a=a: C.active_wavefronts(a))
    for n in (6, 9, True, 2.0):
        rejects(f'cross rejects fake/unsupported address {n!r}',
                lambda n=n: C.hinge_entry(1, 1, F(1), n))
    for a in (F(1, 2), F(3, 4)):
        r = C.transported_low_bracket(a, 2)
        rho = r['interval_row_radius']
        tail = r['positive_Gamma_tail_norm']
        d = 9
        check(f'positive omitted Gamma exact cap a={a}', tail == F(2, d*d)+F(16, d**3))
        for i in range(4):
            for j in range(4):
                lo, hi = r['partial_entry_intervals'][i][j]
                mid = (lo+hi)/2
                check(f'full matrix Loewner bracket a={a},i={i},j={j}',
                      r['lower_form'][i][j] == mid-(rho if i == j else 0) and
                      r['upper_form'][i][j] == mid+(rho+tail/F(2*i+3) if i == j else 0))
        check(f'cross does not transfer high coercivity a={a}',
              r['high_coercivity_transferred'] is False and r['Schur_sign_proved'] is False)
    a, b, J = F(1, 2), F(501, 1000), 8
    delta = b-a
    lip = F(45)+sum((F(2, 4*j+1) for j in range(J)), F())
    tail = F(1, 4*J+1)+F(4, (4*J+1)**2)
    expected = 2*delta*(2*b*lip+tail)+2*a*(2*delta*lip+2*tail)
    check('continuity uses whole-kernel O(1/J) remainder',
          C.radius_continuity_bound(a, b, J) == expected,
          whole_kernel_tail=tail, smaller_mean_zero_operator_tail=S.authentic_positive_gamma_tail_norm(J))
    obs = C.product_formula_observation(F(7, 10), (2, 5))
    check('missing prime cannot be replaced by finite menu',
          obs['full_norm_product'] == 1 and obs['partial_norm_product'] != 1 and
          obs['missing_nontrivial_places'] == (7,) and obs['spectral_tail_bound_obtained'] is False)


def audit_geometry():
    G = importlib.import_module('observational_succ.prime_wavefront_geometry')
    for a, ell in ((F(1, 2), F()), (F(1, 2), F(2, 3)),
                   (F(3, 4), F(1, 3)), (F(1, 2), F(1))):
        for i, j in ((1, 1), (2, 4), (3, 2), (5, 7)):
            result = G.hinge_matrix(a, (legendre(i, a),), (legendre(j, a),),
                                    (G.Hinge(ell),))[0][0]
            check(f'rational hinge via primitive overlaps a={a},ell={ell},{i},{j}',
                  result == hinge_primitive_pair(i, j, a, ell))
    for b, c in ((F(), F(1)), (F(1, 3), F(2)), (F(3, 4), -F(3)), (F(2), F(1))):
        h = G.Hinge(b, c)
        delta = max(F(), 1-b)
        check(f'raw hinge HS exact b={b},c={c}',
              G.hinge_hs_inner(F(1, 2), h, h) == c*c*delta**4/6 and
              G.hinge_hs_inner(F(1, 2), h, h, derivative=True) == c*c*delta**2)
    clipped = G.clipped_hinge(F(1), G.Hinge(F(3, 4), F(2)))
    distribution = G.zero_extension_second_derivative(clipped)
    for k in range(7):
        test = (F(),)*k+(F(1),)
        second = derivative(derivative(test))
        expected = sum((integral(mul(poly, second), left, right)
                        for poly, left, right in zip(clipped.pieces, clipped.breaks, clipped.breaks[1:])), F())
        check(f'zero-extension boundary atoms distribution duality degree={k}',
              distribution.pair_polynomial(test) == expected)
    jumps = G.PiecewisePolynomial((-F(1), F(), F(1)), ((F(),), (F(1),)))
    rejects('piecewise jump cannot be discarded by weak derivative', jumps.weak_derivative)
    rejects('source geometry rejects missing half density',
            lambda: G.source_prime_geometry(F(1, 2), half_density=F(1)))
    rejects('source geometry rejects fake invisible composite',
            lambda: G.source_prime_geometry(F(1, 4), tape=((2, 2), (3, 3), (4, 2), (5, 5), (6, 6), (7, 7), (8, 2))))
    # Independent integration of the FULL two-variable differentiated projected
    # kernel, rather than reusing the producer's finite-rank HS identity.
    isolated = G.source_first_prime_projection_bound()
    b = isolated['rational_reference_threshold']
    direct = direct_projected_hinge_derivative_hs(b)
    check('prime2 projected reference via full two-variable kernel integral',
          direct == isolated['unweighted_reference_audit']['D_Q_T_Q_HS_squared'], exact_reference=direct)
    eta = isolated['threshold_error_upper']
    S = sum((F(2*n*(n+1)*(2*n+1)) for n in range(5)), F())
    error = 4*eta+2*S*eta*eta
    eps = F(1, 100)
    unweighted = (1+eps)*direct+(1+1/eps)*error
    weight = isolated['source_weight_interval']
    independent_upper = weight.hi**2*unweighted
    denominator = isolated['D_G2_HS_squared_interval']
    check('prime2 transfer has complete derivative and projection errors',
          S == isolated['DP_operator_squared_upper'] and
          error == isolated['unweighted_derivative_perturbation_squared_upper'] and
          independent_upper <= isolated['D_Q_G2_Q_HS_squared_upper'] and
          isolated['D_Q_G2_Q_HS_squared_upper'] < denominator.lo/5 and
          isolated['full_signed_source_included'] is False and
          isolated['universal_output_projection_contraction'] is False)
    EVIDENCE['isolated_prime2_projection'] = {'reference_exact': direct,
        'threshold_error': eta, 'projection_error_squared': error,
        'derivative_HS_squared_upper': isolated['D_Q_G2_Q_HS_squared_upper'],
        'mean_zero_derivative_HS_squared_lower': denominator.lo,
        'scope': 'isolated true prime2 ONLY; no full signed source contraction'}


def direct_projected_hinge_derivative_hs(b):
    """Direct polynomial integration on nine rectangles and two corner triangles.

    For a=1/2 and 1/2<b<1, expand the actual kernel D_x(R T_b R).
    The smooth correction is bivariate polynomial on each rectangle. Its
    cross term with sign(x-y)1_|x-y|>b is integrated on the corner triangles.
    This avoids the producer's adjoint/HS finite-rank correction algorithm.
    """
    a = F(1, 2)
    assert a < b < 1
    cuts = (-a, a-b, b-a, a)
    basis = [legendre(n) for n in range(5)]
    norms = [F(1, 2*n+1) for n in range(5)]
    responses = []
    for p in basis:
        first = primitive(p, -a)
        second = primitive(first, -a)
        pieces = []
        for left, right in zip(cuts, cuts[1:]):
            x = (left+right)/2
            poly = (F(),)
            if x > b-a:
                poly = add(poly, shift(second, -b))
            if x < a-b:
                rightpart = add(shift(second, b), ((a-b)*value(first, a)-value(second, a), -value(first, a)))
                poly = add(poly, rightpart)
            pieces.append(poly)
        responses.append(pieces)
    matrix = [[sum((integral(mul(basis[i], responses[j][s]), cuts[s], cuts[s+1])
                    for s in range(3)), F()) for j in range(5)] for i in range(5)]

    def outer(acc, p, q, c):
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                acc[i, j] = acc.get((i, j), F())+c*x*y

    norm_correction = cross = F()
    for sx in range(3):
        for sy in range(3):
            poly = {}
            for n in range(5):
                outer(poly, derivative(responses[n][sx]), basis[n], -1/norms[n])
                outer(poly, derivative(basis[n]), responses[n][sy], -1/norms[n])
                for m in range(5):
                    outer(poly, derivative(basis[n]), basis[m], matrix[n][m]/(norms[n]*norms[m]))
            poly = {key: c for key, c in poly.items() if c}
            square = {}
            for (i, j), c in poly.items():
                for (k, l), d in poly.items():
                    square[i+k, j+l] = square.get((i+k, j+l), F())+c*d
            for (i, j), c in square.items():
                ix = (cuts[sx+1]**(i+1)-cuts[sx]**(i+1))/F(i+1)
                iy = (cuts[sy+1]**(j+1)-cuts[sy]**(j+1))/F(j+1)
                norm_correction += c*ix*iy
            if (sx, sy) in ((2, 0), (0, 2)):
                for (i, j), c in poly.items():
                    power = (F(),)*(j+1)+(F(1),)
                    if sx == 2:
                        inner = add(shift(power, -b), (-(-a)**(j+1),))
                        sign = F(1)
                    else:
                        inner = add((a**(j+1),), shift(power, b), -1)
                        sign = -F(1)
                    cross += sign*c/F(j+1)*integral((F(),)*i+inner, cuts[sx], cuts[sx+1])
    return (1-b)**2+2*cross+norm_correction


def audit_spectral():
    S = importlib.import_module('observational_succ.spectral_response')
    rotation = ((F(3, 5), -F(4, 5)), (F(4, 5), F(3, 5)))
    diag = ((F(1, 4), F()), (F(), F(4)))
    D = matmul(rotation, matmul(diag, transpose(rotation)))
    b = ((F(1, 3), -F(2, 5)), (F(2, 7), F(1, 2)))
    eigencoupling = matmul(transpose(rotation), b)
    measure = S.SpectralMeasure.from_diagonal((F(1, 4), F(4)), eigencoupling)
    for lam in (F(), F(1, 8), F(1), F(9)):
        shifted = tuple(tuple(D[i][j]+(lam if i == j else 0) for j in range(2)) for i in range(2))
        target = matmul(transpose(b), matmul(inverse(shifted), b))
        check(f'spectral response versus rotated Schur solve shift={lam}', measure.response(lam) == target)
        if lam:
            gap = subtract(measure.response(), target)
            check(f'spectral shift gap PSD and exact shift={lam}', measure.shift_gap(lam) == gap and psd(gap))
            U = matmul(inverse(shifted), b)
            # L_U=b*U+U*b-U*DU, derived directly from square completion.
            bU = matmul(transpose(b), U)
            Utb = transpose(bU)
            energy = matmul(transpose(U), matmul(D, U))
            L = tuple(tuple(bU[i][j]+Utb[i][j]-energy[i][j] for j in range(2)) for i in range(2))
            check(f'completion gap is distinct from regularization gap shift={lam}',
                  measure.completion_gap(lam) == subtract(measure.response(), L) and
                  measure.completion_gap(lam) != gap)
            bounds = measure.fractional_bounds(F(1), lam, F(1))
            check(f'fractional matrix bounds retain cross terms shift={lam}',
                  psd(subtract(bounds['tail_upper'], measure.inverse_tail(1))) and
                  psd(subtract(bounds['shift_upper'], gap)) and
                  psd(subtract(bounds['completion_upper'], measure.completion_gap(lam))))
    first, second = measure.stieltjes_tail_parts(F(1))
    total = tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(first, second))
    check('Stieltjes tail exact boundary term and integral', total == measure.inverse_tail(1))
    kernel = S.SpectralMeasure.from_diagonal((F(), F(1)), ((F(1),), (F(1),)))
    rejects('nonzero kernel coupling rejects zero response', kernel.response)
    check('positive shift allows kernel coupling', kernel.response(F(1)) == ((F(3, 2),),))
    rejects('PSD atom requires full matrix not diagonal signs',
            lambda: S.SpectralMeasure(((F(1), ((F(1), F(2)), (F(2), F(1)))),)))
    for order in (0, 1, 3, 5):
        base, changed = S.matched_moment_measures(order, F(1, 1000))
        check(f'matched finite moments do not fix inverse order={order}',
              all(base.moment(k) == changed.moment(k) for k in range(order+1)) and
              changed.response()[0][0] > base.response()[0][0]+100)
    tail = S.slow_tail_enclosure(8, F(1, 100))
    prefix = S.slow_tail_prefix(40)
    for key, observed in (('response', prefix.response()[0][0]),
                          ('shift_gap', prefix.shift_gap(F(1, 100))[0][0]),
                          ('completion_gap', prefix.completion_gap(F(1, 100))[0][0])):
        check('slow tail prefix respects infinite upper: '+key, observed <= tail[key][1])


def audit_resolvent():
    A = importlib.import_module('observational_succ.arithmetic_resolvent')
    # Source cap replay remains a separately identified Rodrigues lineage.
    for i, j in ((1, 1), (1, 3), (2, 2), (3, 4)):
        z = A.full_entry(i, j, 2)
        check(f'resolvent full-entry parity and finite enclosure {i},{j}',
              z.lo <= z.hi and ((i+j) % 2 == 0 or z.lo == z.hi == 0))
    record = {'degree': 10, 'U': tuple((F(),)*4 for _ in range(6))}
    record['candidate_sha256'] = A.candidate_digest(record)
    zero = tuple((F(),)*4 for _ in range(4))
    fake = {'candidate_sha256': record['candidate_sha256'], 'gamma_modes': 1,
            'V_Gram': zero, 'U_Gram': zero,
            'H_lower': tuple(tuple(F(1000*(i == j)) for j in range(4)) for i in range(4)),
            'S0_upper_form': tuple(tuple(F(1000*(i == j)) for j in range(4)) for i in range(4))}
    try:
        accepted = A.shifted_certificate(record, F(1), gamma_modes=1, upper=fake)
    except (ValueError, TypeError, KeyError) as exc:
        check('forged optional source upper certificate rejected', True,
              exception=type(exc).__name__, message=str(exc))
    else:
        check('forged optional source upper certificate rejected', False,
              forged_input=fake, observed_status=accepted['status'],
              fabricated_lower_form=accepted['S_lambda_lower_form'])
    rejects('zero shift cannot enter positive-shift certificate',
            lambda: A.shifted_certificate(record, F(), gamma_modes=1))
    for index in (3, 29):
        r = A.regularization_counterexample(index, F(1, 10))
        check(f'resolvent soft mode counterexample index={index}',
              r['R0'] == 1 and r['S0'] == -F(1, 2) and
              r['R_lambda'] == 1/(1+F(1, 10)*index*index))
    # Unequal Legendre metric tests a common form/operator eigenvalue error.
    form = tuple(tuple(F(i == j, 2*i+3) for j in range(4)) for i in range(4))
    caps = A.sector_caps(form, bits=12)
    for name, expected in (('odd', (F(1, 3), F(1, 7))), ('even', (F(1, 5), F(1, 9)))):
        r = caps[name]
        check('resolvent cap uses correct metric '+name,
              r['operator_upper_cap'] == 1 and
              tuple(r['W'][i][i] for i in range(2)) == expected and psd(r['cap_slack']))


def audit_source_range():
    R = importlib.import_module('observational_succ.arithmetic_source_range')
    for n in (5, 6, 11):
        c = R.primitive_control(n)
        p = primitive(legendre(n), -F(1, 2))
        check(f'primitive high-domain independent coefficients n={n}',
              tuple(c['primitive']) == p and c['K_energy'] == norm2(p) and
              c['primitive_endpoints'] == (0, 0) and
              all(v == 0 for v in c['primitive_moments_through_3']))
    for xi in (F(), F(3, 2), F(33, 2)):
        e = R.gamma_multiplier_enclosure(xi, 8)
        partial = sum((F(16)*xi*xi/(F(4*j+1)*((4*j+1)**2+4*xi*xi)) for j in range(8)), F())
        tail = 16*xi*xi/33**3+2*xi*xi/33**2
        check(f'Gamma multiplier whole tower tail xi={xi}',
              e['lower'] == partial and e['upper'] == partial+tail and
              e['compressed_operator_eigenvalue'] is False)
    for n in (1, 8, 32):
        b = R.logarithmic_band_lower(n)
        measured = R.gamma_multiplier_enclosure(b['frequency'], n)
        check(f'logarithmic spectral lower band n={n}', measured['lower'] >= b['lower'])
    for mode, rung in ((5, 0), (6, 2)):
        g = R.gamma_primitive_identity(mode, rung)
        check(f'Gamma primitive integration-by-parts n={mode},j={rung}',
              tuple(g['difference_affine']) == (0, 0))
    bad = R.gamma_primitive_identity(boundary_mutant=True)
    check('nonzero endpoint mutant retains boundary defect', any(bad['difference_affine']))
    rejects('numerical derivative refuses singular diagonal', lambda: R.numerical_gprime(0))
    claims = R.claim_boundaries()
    check('source range preserves fractional and Schur debt',
          claims['fractional_D_power_above_half'].startswith('OPEN') and
          claims['source_S0_sign'] == 'OPEN' and claims['kernel_proof'] is False)


def audit_tail_contract():
    T = importlib.import_module('observational_succ.spectral_tail_contract')
    capsules = json.loads((ROOT/'research/2026-10-16/OBSERVER_SCHUR_CAPSULES.json').read_text())
    evidence_path = 'research/2026-10-16/CROSS_PRIME_WAVEFRONT_CONTINUATION.md'
    evidence = [{'path': evidence_path, 'sha256': sha256((ROOT/evidence_path).read_bytes()).hexdigest(),
                 'kind': 'PAPER_SOURCE_APPLICATION'}]
    packet = T.make_open_tail_packet(capsules, evidence)
    clean = T.audit_tail_packet(packet, ROOT)
    check('valid open packet grants no semantic authority',
          clean['semantic_authority_issued'] is None and not clean['source_tail_rate_proved'] and
          not clean['source_sign_proved'] and not clean['dependency_audit']['theorems_proved_by_this_audit'])
    attacks = (
        ('source_sign', 'PROVED'), ('proof_authority', 'LEAN_KERNEL_PROVED'),
        ('outstanding_obligations', []), ('source_upper_matrix', [[1]]),
        ('source_lower_matrix', [[1]]), ('global_conclusion', 'RH'),
        ('estimate_status', 'PROVED_SOURCE'), ('RH_proved', True),
        ('kernel_proof_of_analytic_source', True), ('new_proof_claim', 'FORGED'))
    for key, forged in attacks:
        p = copy.deepcopy(packet)
        p[key] = forged
        p['sha256'] = T.digest(p)
        rejects('canonical-rehashed packet forgery '+key, lambda p=p: T.audit_tail_packet(p, ROOT))
    for key, forged in (('coordinate_metric', ['1']*4), ('radius', '3/4'),
                        ('signed_channels', ['real_Gamma_all_modes']), ('source_epoch', 'foreign')):
        p = copy.deepcopy(packet)
        p['source'][key] = forged
        p['sha256'] = T.digest(p)
        rejects('canonical-rehashed source forgery '+key, lambda p=p: T.audit_tail_packet(p, ROOT))
    p = copy.deepcopy(packet)
    p['analytic_error_budgets']['Gamma_derivative_tail'] = p['analytic_error_budgets']['Gamma_operator_tail']
    p['sha256'] = T.digest(p)
    rejects('canonical-rehashed derivative budget substitution', lambda: T.audit_tail_packet(p, ROOT))
    p = copy.deepcopy(packet)
    consumer = next(c for c in p['capsules'] if c['claim_id'] == 'OS-APPROX-CONSUMER')
    consumer['hypotheses'] = []
    p['sha256'] = T.digest(p)
    rejects('canonical-rehashed transitive open premise laundering', lambda: T.audit_tail_packet(p, ROOT))
    p = copy.deepcopy(packet)
    p['capsules'][0]['statement'] = 'False source-specific prose cannot become a proof by rehashing.'
    p['sha256'] = T.digest(p)
    no_proof = T.audit_tail_packet(p, ROOT)
    check('hash-valid false prose remains nonauthoritative', no_proof['semantic_authority_issued'] is None and
          not no_proof['source_sign_proved'])
    consumer = next(c for c in clean['dependency_audit']['claims'] if c['claim_id'] == 'OS-APPROX-CONSUMER')
    check('transitive dependency debt actually retained', 'OS-RANGE-OPEN' in consumer['open_dependencies'] and
          'Source residual operator is bounded and trials have dense union' in consumer['retained_hypotheses'])


def audit_lower_receipts():
    folder = ROOT/'research/2026-10-16/arithmetic_resonance_receipts'
    paths = sorted(folder.glob('resolvent-lower*.json'))
    if not paths:
        PENDING.append('genuine lower receipt')
        return
    # Low Legendre sup=1 independently from elementary factorizations on z in [-1,1]:
    # 1-P2=3(1-z²)/2, 1+P2=(1+3z²)/2;
    # 1-P3=(1-z)(5z²+5z+2)/2 and its reflection;
    # 1-P4=5(1-z²)(7z²+1)/8; 1+P4=(35z^4-30z²+11)/8>0.
    check('Legendre sup factorizations have positive residual discriminants',
          5*5-4*5*2 < 0 and (-30)**2-4*35*11 < 0)
    # Source non-Gamma BV < 5+8+2=15<16: pole 8sinh(1/2)<5,
    # contact C<8 (gamma<1, pi/2<2, 3log2<3, logpi<2), prime 2w<2.
    e = exp_box(F(1, 2))
    pole_upper = 4*(e[1]-1/e[1])
    check('independent non-Gamma BV constant fits 16', pole_upper < 5 and F(5+8+2) < 16)
    all_receipts = []
    for path in paths:
        r = json.loads(path.read_text())
        if 'columns' not in r or 'sectors' not in r:
            continue
        J, grid = r['gamma_modes'], r['grid']
        lip = F(16)+8*sum((F(1, 4*j+1) for j in range(J)), F())
        eta = F(2, 4*J+1)+F(8, (4*J+1)**2)
        check(path.name+' source/BV/domain pins', r['source_git_blob'] == PIN and
              F(r['BV_Lipschitz']) == lip and F(r['Legendre_sup']) == 1 and
              F(r['kappa']) == F(20699, 1000000) and grid % 2 == 0 and J <= 20)
        energies = {}
        for col in r['columns']:
            mode = col['mode']
            samples = [tuple(map(F, row)) for row in col['positive_half_midpoint_intervals']]
            check(f'{path.name} whole positive-half cells mode={mode}',
                  [s[0] for s in samples] == [F(2*i+1, 2*grid) for i in range(grid//2)] and
                  all(lo <= hi for _, lo, hi in samples))
            h = F(1, grid)
            m = [max(abs(lo), abs(hi)) for _, lo, hi in samples]
            midpoint = sum((2*h*x*x for x in m), F())
            linear = sum((x*lip*h*h for x in m), F())
            quadratic = F(len(samples))*lip*lip*h**3/6
            total = midpoint+linear+quadratic
            check(f'{path.name} reflected exact cell integration mode={mode}',
                  F(col['midpoint_absolute_energy_upper']) == midpoint and
                  F(col['between_cell_linear_error']) == linear and
                  F(col['between_cell_quadratic_error']) == quadratic and
                  F(col['finite_J_whole_interval_energy_upper']) == total)
            energies[mode] = total
            # Three independent points per column straddle/approach prime support,
            # without re-running the producer's full grid computation.
            for idx in (0, len(samples)//2, len(samples)-1):
                x, lo, hi = samples[idx]
                independent = independent_derivative_box(mode, x, J)
                check(f'{path.name} independent displacement moments mode={mode},cell={idx}',
                      lo <= independent[1] and independent[0] <= hi,
                      independent=independent, source_interval=(lo, hi))
        caps = {}
        for name, modes in (('odd', (1, 3)), ('even', (2, 4))):
            s = r['sectors'][name]
            trace = sum(((2*k+1)*energies[k] for k in modes), F())
            root = F(s['trace_sqrt_upper'])
            full = (root+eta)**2
            cap = full/F(20699, 1000000)
            check(path.name+' normalized sector trace/tail '+name,
                  F(s['finite_J_normalized_trace_upper']) == trace and root >= 0 and root*root >= trace and
                  F(s['whole_Gamma_derivative_operator_tail']) == eta and
                  F(s['full_derivative_operator_squared_upper']) == full and
                  F(s['R0_operator_upper_cap']) == cap and cap < F(75625, 20699))
            caps[name] = cap
        all_receipts.append({'path': str(path.relative_to(ROOT)), 'sha256': sha256(path.read_bytes()).hexdigest(),
                             'caps': caps, 'sample_scope': 'three independent midpoint checks per column; all cell sums replayed'})
    EVIDENCE['lower_receipt_replays'] = all_receipts


def audit_upper_receipt():
    """Full best-candidate source replay via prior independent Rodrigues code.

    This reuses that audit lineage: it is NOT a second independent algorithm
    relative to source_cap_audit.py. No producer integration helpers are called.
    """
    folder = ROOT/'research/2026-10-16/arithmetic_resonance_receipts'
    cp = folder/'resolvent-candidates-initial.json'
    up = folder/'resolvent-upper-initial.json'
    if not cp.is_file() or not up.is_file():
        PENDING.append('candidate/upper source receipts')
        return
    candidates, uppers = json.loads(cp.read_text()), json.loads(up.read_text())
    candidate = next(c for c in candidates if c['degree'] == 20)
    upper = next(u for u in uppers if u['candidate_sha256'] == candidate['candidate_sha256'])
    payload = {k: v for k, v in candidate.items() if k != 'candidate_sha256'}
    check('frozen best candidate canonical digest', sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
          == candidate['candidate_sha256'])
    review = ROOT/'reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md'
    code = review.read_text().split('```python\n', 1)[1].split('\n```', 1)[0].split('start=time.monotonic()', 1)[0]
    ns = {}
    exec(compile(code, str(review)+'::definitions-only', 'exec'), ns)
    U = tuple(tuple(map(F, row)) for row in candidate['U'])
    degree, J = candidate['degree'], upper['gamma_modes']
    v = tuple(tuple(F(i == j) if i < 4 else -U[i-4][j] for j in range(4)) for i in range(degree))
    vg = tuple(tuple(sum((v[k][i]*v[k][j]/F(2*k+3) for k in range(degree)), F()) for j in range(4)) for i in range(4))
    check('best candidate actual whole-column Gram', vg == tuple(tuple(map(F, row)) for row in upper['V_Gram']))
    polynomials = [ns['combine']([v[k][j] for k in range(degree)]) for j in range(4)]
    reconstructed = [[(F(), F())]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            if (i-j) % 2:
                continue
            rho = ns['rho'](polynomials[i], polynomials[j])
            check(f'best-candidate exact mean-zero correlation {i},{j}', ns['integ'](rho) == 0)
            contact = ns['scale'](ns['CONTACT'], ns['integ']([F()]+rho)/2)
            poles = ns['scale'](ns['add'](ns['epair'](rho, -F(1, 2)), ns['epair'](rho, F(1, 2))), -4)
            prime = ns['mul'](ns['WEIGHT'], ns['hinge'](rho))
            gamma = ns['sumiv'](ns['scale'](ns['epair'](rho, F(4*k+1, 2)), F(4, (4*k+1)**2)) for k in range(J))
            z = ns['sumiv']((contact, poles, prime, gamma))
            reconstructed[i][j] = reconstructed[j][i] = z
            lo, hi = map(F, upper['truncated_H_intervals'][i][j])
            check(f'best-candidate independent whole source trial interval {i},{j}', lo <= z[0] <= z[1] <= hi)
    boxes = [[tuple(map(F, box)) for box in row] for row in upper['truncated_H_intervals']]
    radii = [max(sum(((boxes[i][j][1]-boxes[i][j][0])/2 for j in ix), F()) for i in ix)
             for ix in ((0, 2), (1, 3))]
    tau = F(2, (4*J+1)**2)+F(16, (4*J+1)**3)
    reconstructed_upper = tuple(tuple(sum(boxes[i][j])/2+(radii[i % 2] if i == j else 0)+tau*vg[i][j]
                                      for j in range(4)) for i in range(4))
    check('best-candidate full PSD Gamma correction and row radii',
          reconstructed_upper == tuple(tuple(map(F, row)) for row in upper['S0_upper_form']) and
          tuple(radii) == tuple(map(F, upper['entry_radii_by_sector'])) and
          F(upper['whole_Gamma_tail_norm_upper']) == tau)
    for name, ix in (('odd', (0, 2)), ('even', (1, 3))):
        cap = F(upper['parity_caps'][name]['operator_upper_cap'])
        slack = tuple(tuple((cap/F(2*i+3) if i == j else F())-reconstructed_upper[i][j] for j in ix) for i in ix)
        check('best candidate independent metric-aware cap '+name, psd(slack))
    EVIDENCE['best_upper_replay'] = {'degree': degree, 'gamma_modes': J,
        'candidate_sha256': candidate['candidate_sha256'], 'candidate_file_sha256': sha256(cp.read_bytes()).hexdigest(),
        'upper_file_sha256': sha256(up.read_bytes()).hexdigest(), 'Rodrigues_definitions_sha256': sha256(code.encode()).hexdigest(),
        'partial_source_intervals': reconstructed,
        'caps': {name: r['operator_upper_cap'] for name, r in upper['parity_caps'].items()},
        'lineage': 'Prior auditor Rodrigues/incomplete-gamma; same algorithm as source_cap_audit.py',
        'source_sign': 'OPEN'}


def run_section(name, fun):
    try:
        fun()
    except Exception as exc:
        check(name+' execution', False, exception=type(exc).__name__, message=str(exc))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--allow-pending', action='store_true')
    parser.add_argument('--replay-upper', action='store_true', help='replay six full degree-20 trial entries through independent Rodrigues route')
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_AS, (768*1024**2, 768*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU, (180, 185))
    signal.alarm(240)
    start = time.monotonic()
    hashes = {}
    for name in MODULES:
        path = ROOT/'observational_succ'/f'{name}.py'
        if path.exists():
            hashes[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
        else:
            PENDING.append(name)
    run_section('source pins', source_pins)
    run_section('independent exact proofs', independent_proofs)
    if 'cross_prime_wavefront' not in PENDING:
        run_section('cross prime', audit_cross_prime)
    for name, audit in (('prime_wavefront_geometry', audit_geometry),
                        ('spectral_response', audit_spectral),
                        ('arithmetic_resolvent', audit_resolvent),
                        ('arithmetic_source_range', audit_source_range),
                        ('spectral_tail_contract', audit_tail_contract)):
        if name not in PENDING:
            run_section(name, audit)
    run_section('source lower receipts', audit_lower_receipts)
    if args.replay_upper:
        run_section('independent best upper source replay', audit_upper_receipt)
    if 'source_before' in EVIDENCE:
        check('original source unchanged at audit end',
              EVIDENCE['source_before'] == sha256((ROOT/SOURCE).read_bytes()).hexdigest())
    for name, digest in hashes.items():
        check('inspected module stable during audit: '+name,
              sha256((ROOT/name).read_bytes()).hexdigest() == digest)
    failures = [c['name'] for c in CHECKS if not c['pass']]
    report = {'schema': 'ARITHMETIC_RESONANCE_INDEPENDENT_AUDIT_V1',
        'utc': datetime.now(timezone.utc).isoformat(), 'argv': sys.argv,
        'cwd': str(ROOT), 'python': sys.version,
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'status': 'FAIL' if failures else 'PENDING_MODULES' if PENDING else 'PASS_WITH_OPEN_SIGN',
        'checks': CHECKS, 'failures': failures, 'pending_modules': PENDING,
        'evidence': EVIDENCE, 'inspected_module_sha256': hashes,
        'audit_script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic()-start,
        'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits': {'address_space_MiB': 768, 'CPU_seconds': 180, 'wall_seconds': 240},
        'source_S0_sign': 'OPEN', 'RH_PROVED': False, 'nontrivial_zeros_used': False,
        'formal_kernel_claim': False, 'full_test_suite_run': False,
        'independence': 'Independent primitive-overlap hinge implementation and exact synthetic controls; source lineage shared.'}
    encoded = json.dumps(report, default=str, indent=2)+'\n'
    if args.output:
        dest = args.output.resolve()
        owned = ROOT/'research/2026-10-16/arithmetic_resonance_receipts'
        if dest.parent != owned or not dest.name.startswith('audit'):
            parser.error('output must be an audit* file in the assigned receipt directory')
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(encoded)
        print(json.dumps({k: report[k] for k in ('status', 'failures', 'pending_modules', 'elapsed_seconds', 'peak_rss_kib')}, indent=2))
    else:
        print(encoded, end='')
    return 1 if failures else 2 if PENDING and not args.allow_pending else 0


if __name__ == '__main__':
    raise SystemExit(main())
