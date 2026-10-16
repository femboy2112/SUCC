"""Authentic finite Legendre response certificates, with no zero-shift gap claim.

All source bounds retain the signed poles, contact, prime-2 half density and
entire real Gamma tower. See AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md for the
conditional paper theorem. Fractions are proof data; midpoints only select trials.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
import inspect
from math import isqrt
from pathlib import Path
from types import CodeType, FunctionType

from . import suzuki_legendre_source as L
from . import one_object_relative_residual as R
from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
from .suzuki_moment_schur import inverse_neumann_entry
from .tate_suzuki_shorting import verify_original_suzuki_source


class ResolventError(ValueError):
    pass


def integer(n, low, high):
    if type(n) is not int or not low <= n <= high:
        raise ResolventError(f'integer in {low}..{high} required')
    return n


def rational(x):
    if type(x) not in (int, F):
        raise ResolventError('exact rational required')
    return F(x)


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


@lru_cache(maxsize=4)
def _compiled_source_codes(data, filename):
    code = compile(data, filename, 'exec', dont_inherit=True)
    return {c.co_name: c for c in code.co_consts
            if isinstance(c, CodeType) and not c.co_name.startswith('<')}


def verify_runtime_source():
    """Check live function bytecode against freshly compiled pinned source bytes.

    This guard executes BEFORE any cached source entry is returned. It detects
    changed live functions, interval methods, SCALE and prime tape even when
    the on-disk Git blob is unchanged. It is not a hostile-Python sandbox.
    """
    source = L._pinned_source()
    path = Path(source.__file__)
    codes = _compiled_source_codes(path.read_bytes(), str(path))
    for name, code in codes.items():
        actual = getattr(source, name, None)
        if isinstance(actual, type):
            for method in (c for c in code.co_consts if isinstance(c, CodeType)):
                member = getattr(actual, method.co_name, None)
                if not isinstance(member, FunctionType) or member.__code__ != method:
                    raise ResolventError('loaded source method drift: '+name+'.'+method.co_name)
        else:
            function = inspect.unwrap(actual)
            if not isinstance(function, FunctionType) or function.__code__ != code:
                raise ResolventError('loaded source function drift: '+name)
    if (source.SCALE != 10**32 or source.F is not F or
            source.AUTHENTIC_TAPE != ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))):
        raise ResolventError('loaded source constants drift')
    return source


@lru_cache(maxsize=256)
def correlation(i, j):
    integer(i, 1, 20); integer(j, 1, 20)
    return L.poly_two_variable_cross(i, j, F(1, 2))


def correlation_ou_affine(i, j, alpha):
    """Integrate rho_ij(t) exp(-alpha*t) on [0,1], exactly as A+B exp(-alpha).

    This correlation representation differs from the inherited double integral
    antiderivative. It uses the same arithmetic source, not an independent source.
    """
    alpha = rational(alpha)
    if alpha <= 0:
        raise ResolventError('positive OU decay required')
    aa, bb = 1/alpha, -1/alpha
    total_a = total_b = F()
    for k, c in enumerate(correlation(i, j)):
        if k:
            aa, bb = k*aa/alpha, (k*bb-1)/alpha
        total_a += c*aa
        total_b += c*bb
    return total_a, total_b


@lru_cache(maxsize=2048)
def _exp(alpha, digits):
    if alpha <= 256:
        return L.tight_exp_neg(alpha, digits)
    return F(), F(1, 2**(alpha.numerator//alpha.denominator))


@lru_cache(maxsize=512)
def _truncated_entry(i, j, gamma_modes):
    source = L._pinned_source()
    if (i+j) % 2:
        return source.iv(0)
    gamma = source.iv(0)
    for k in range(gamma_modes):
        d = 4*k+1
        alpha = F(d, 2)
        a, b = correlation_ou_affine(i, j, alpha)
        exponential = _exp(alpha, L.adaptive_precision_budget(b))
        pair = L.source_interval_round(source, L.interval_add((a, a), L.interval_scale(exponential, b)))
        gamma += F(4, d*d)*pair
    return (gamma + L.authentic_first_prime_low_entry(i, j)
            + L.authentic_pole_low_entry(i, j)
            - source.contact_iv()*inverse_neumann_entry(F(1, 2), i, j))


def truncated_entry(i, j, gamma_modes):
    integer(i, 1, 20); integer(j, 1, 20); integer(gamma_modes, 1, 2048)
    verify_runtime_source()  # authenticate even cached or parity-zero results
    return _truncated_entry(min(i, j), max(i, j), gamma_modes)


def full_entry(i, j, gamma_modes):
    z = truncated_entry(i, j, gamma_modes)
    if (i+j) % 2:
        return z
    source = L._pinned_source()
    e = authentic_positive_gamma_tail_norm(gamma_modes)/min(2*i+1, 2*j+1)
    return source.I(z.lo-e, z.hi+e)


def metric(modes):
    return tuple(tuple(F(1, 2*i+1) if i == j else F() for j in modes) for i in modes)


def solve(a, b):
    """Exact rational Gaussian solve; bounded to at most eight high modes/sector."""
    a, b = R.matrix(a, square=True), R.matrix(b)
    if len(a) != len(b) or not R.sym(a):
        raise ResolventError('symmetric compatible finite solve required')
    if not R.pd(a):
        raise ResolventError('candidate midpoint is not positive definite')
    x = R.mm(R.inv(a), b)
    if R.mm(a, x) != b:
        raise ArithmeticError('exact solve residual nonzero')
    return x


def freeze_candidate(degree=16, gamma_modes=64, shift=F(), denominator=10**10):
    """Select by exact midpoint solve, round, and freeze BEFORE certification."""
    integer(degree, 10, 20); integer(gamma_modes, 1, 2048)
    integer(denominator, 1, 10**12)
    shift = rational(shift)
    if shift < 0:
        raise ResolventError('nonnegative selection shift required')
    verify_original_suzuki_source()
    u = [[F()]*4 for _ in range(degree-4)]
    solves = {}
    for name, low in (('odd', (1, 3)), ('even', (2, 4))):
        high = tuple(n for n in range(5, degree+1) if n % 2 == low[0] % 2)
        a = tuple(tuple(truncated_entry(i, j, gamma_modes).mid()
                        + (shift/F(2*i+1) if i == j else 0) for j in high) for i in high)
        b = tuple(tuple(truncated_entry(i, j, gamma_modes).mid() for j in low) for i in high)
        fitted = solve(a, b)
        solves[name] = {'high_modes': high, 'exact_equation_verified': R.mm(a, fitted) == b}
        for i, h in enumerate(high):
            for j, l in enumerate(low):
                u[h-5][l-1] = F(round(fitted[i][j]*denominator), denominator)
    record = {'degree': degree, 'selection_gamma_modes': gamma_modes,
              'selection_shift': shift, 'denominator': denominator,
              'U': tuple(map(tuple, u)), 'exact_sector_solves': solves,
              'selection_status': 'EXACT_RATIONAL_MIDPOINT_SELECTION_NOT_SOURCE_PROOF'}
    record['candidate_sha256'] = candidate_digest(record)
    return record


def candidate_digest(record):
    payload = {k: v for k, v in record.items() if k != 'candidate_sha256'}
    return sha256(json.dumps(serial(payload), sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def validate_candidate(record):
    degree = integer(record['degree'], 10, 20)
    u = tuple(tuple(rational(x) for x in row) for row in record['U'])
    if len(u) != degree-4 or any(len(row) != 4 for row in u):
        raise ResolventError('invalid frozen response dimensions')
    if any(u[h-5][l-1] for h in range(5, degree+1) for l in range(1, 5) if (h-l) % 2):
        raise ResolventError('response violates reflection parity')
    if record['candidate_sha256'] != candidate_digest(record):
        raise ResolventError('frozen candidate digest mismatch')
    return degree, u


def trial_columns(record):
    degree, u = validate_candidate(record)
    return tuple(tuple(F(i == j) if i < 4 else -u[i-4][j] for j in range(4)) for i in range(degree))


def interval_congruence(entries, v):
    source = L._pinned_source()
    n = len(v[0]); result = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            z = sum((v[a][i]*v[b][j]*entries[a][b] for a in range(len(v)) for b in range(len(v))
                     if v[a][i] and v[b][j]), source.iv(0))
            result[i][j] = result[j][i] = z
    return tuple(map(tuple, result))


def interval_majorants(entries):
    """Exact symmetric row-radius Loewner bounds, separately per parity sector."""
    if len(entries) != 4 or any(len(row) != 4 for row in entries):
        raise ResolventError('four-low interval form required')
    if any(entries[i][j] != entries[j][i] for i in range(4) for j in range(4)):
        raise ResolventError('interval matrix is not symmetric')
    if any(entries[i][j].lo or entries[i][j].hi for i in range(4) for j in range(4) if (i-j) % 2):
        raise ResolventError('interval matrix violates parity')
    mid = tuple(tuple(z.mid() for z in row) for row in entries)
    radii = tuple(max(sum((entries[i][j].radius() for j in sector), F()) for i in sector)
                  for sector in ((0, 2), (1, 3)))
    error = tuple(tuple(radii[i % 2] if i == j else F() for j in range(4)) for i in range(4))
    return R.add(mid, error, -1), R.add(mid, error), radii


def sector_caps(form, bits=40):
    integer(bits, 1, 60)
    form = R.matrix(form, square=True)
    if len(form) != 4 or not R.sym(form) or any(form[i][j] for i in range(4) for j in range(4) if (i-j) % 2):
        raise ResolventError('symmetric parity form required')
    result = {}
    for name, ix in (('odd', (0, 2)), ('even', (1, 3))):
        block = tuple(tuple(form[i][j] for j in ix) for i in ix)
        w = metric(tuple(i+1 for i in ix))
        def slack(c):
            return R.add(R.scale(c, w), block, -1)
        left, right = -F(16), F(16)
        if not R.psd(slack(right)) or R.psd(slack(left)):
            raise ResolventError('bounded cap search exhausted')
        for _ in range(bits):
            middle = (left+right)/2
            if R.psd(slack(middle)):
                right = middle
            else:
                left = middle
        result[name] = {'operator_upper_cap': right, 'W': w, 'form': block,
                        'cap_slack': slack(right), 'cap_slack_exact_PSD': R.psd(slack(right))}
    return result


def certify_upper(record, gamma_modes=512):
    degree, u = validate_candidate(record)
    integer(gamma_modes, 1, 2048)
    source = verify_original_suzuki_source()
    v = trial_columns(record)
    entries = tuple(tuple(truncated_entry(i, j, gamma_modes) for j in range(1, degree+1)) for i in range(1, degree+1))
    h = interval_congruence(entries, v)
    lo, hi, radii = interval_majorants(h)
    vgram = R.mm(R.mm(R.trans(v), metric(tuple(range(1, degree+1)))), v)
    ugram = R.add(vgram, metric((1, 2, 3, 4)), -1)
    tail = authentic_positive_gamma_tail_norm(gamma_modes)
    upper = R.add(hi, R.scale(tail, vgram))
    return {'candidate_sha256': record['candidate_sha256'], 'degree': degree,
            'source_git_blob': source['source_git_blob'], 'gamma_modes': gamma_modes,
            'whole_Gamma_tail_norm_upper': tail, 'V_Gram': vgram, 'U_Gram': ugram,
            'truncated_H_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in h),
            'entry_radii_by_sector': radii, 'H_lower': lo, 'S0_upper_form': upper,
            'parity_caps': sector_caps(upper),
            'certified_order': 'H_lower <= H_U; S0 <= H_U <= S0_upper_form',
            'status': 'EXACT_SOURCE_INTERVAL_UPPER_BOUND_CONDITIONAL_ON_INHERITED_RANGE_THEOREM',
            'zero_shift_lower_improved': False, 'source_sign': 'OPEN', 'RH_PROVED': False}


def shifted_certificate(record, shift, gamma_modes=512, cutoff=None):
    """H_lambda - C/lambda <= S_lambda <= H_lambda, with certified residual C.

    The finite residual includes all modes 5..cutoff and full Gamma intervals.
    The orthogonal spatial tail uses the inherited ||g'||_1 < 11/40 theorem.
    No conclusion S0 >= the shifted lower is permitted.
    """
    shift = rational(shift)
    if shift <= 0:
        raise ResolventError('strictly positive shift required; no zero-gap substitution')
    degree, u = validate_candidate(record)
    cutoff = degree if cutoff is None else integer(cutoff, degree, 20)
    # The previous optional external certificate was a trust-boundary defect.
    # A candidate hash does not authenticate H, V*V, or U*U. Always replay.
    upper = certify_upper(record, gamma_modes)
    source = L._pinned_source(); v = trial_columns(record)
    finite = []
    for q in range(5, cutoff+1):
        row = []
        for j in range(4):
            z = sum((v[a][j]*full_entry(q, a+1, gamma_modes) for a in range(degree) if v[a][j]), source.iv(0))
            if q <= degree:
                z -= shift*u[q-5][j]/F(2*q+1)
            row.append(z)
        finite.append(row)
    gram = [[None]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            z = sum((F(2*q+1)*finite[q-5][i]*finite[q-5][j] for q in range(5, cutoff+1)), source.iv(0))
            gram[i][j] = gram[j][i] = z
    _, finite_upper, radii = interval_majorants(gram)
    spatial = F(11, 40)**2/F(4*(cutoff+1)*(cutoff+2))
    residual = R.add(finite_upper, R.scale(spatial, upper['V_Gram']))
    lower = R.add(R.add(upper['H_lower'], R.scale(shift, upper['U_Gram'])), R.scale(1/shift, residual), -1)
    high = R.add(upper['S0_upper_form'], R.scale(shift, upper['U_Gram']))
    return {'shift': shift, 'cutoff': cutoff, 'candidate_sha256': record['candidate_sha256'],
            'finite_residual_form_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in finite),
            'finite_residual_Gram_upper': finite_upper, 'finite_Gram_radii': radii,
            'one_sided_spatial_tail_squared': spatial, 'residual_Gram_upper': residual,
            'response_error_upper': R.scale(1/shift, residual),
            'S_lambda_lower_form': lower, 'S_lambda_upper_form': high,
            'certified_order': 'S_lambda_lower_form <= S_lambda <= S_lambda_upper_form',
            'status': 'CONDITIONAL_PAPER_BOUND_WITH_EXACT_AUTHENTIC_SOURCE_INTERVALS',
            'regularization_gap_S_lambda_minus_S0': 'UNBOUNDED_BY_THIS_CERTIFICATE',
            'zero_shift_sign': 'OPEN', 'RH_PROVED': False}


def regularization_counterexample(index, shift=F(1, 100)):
    """Exact synthetic missing-tail control, not an alternative arithmetic source.

    Hidden mode D=K=index^-2, b=index^-1, A=1/2: R0=1 despite
    Rlambda tending to zero. Embed at an unseen coordinate of diag(j^-2).
    """
    integer(index, 1, 10**9); shift = rational(shift)
    if shift <= 0:
        raise ResolventError('positive shift required')
    response = 1/(1+shift*index*index)
    return {'index': index, 'shift': shift, 'hidden_D': F(1, index*index),
            'hidden_b': F(1, index), 'R0': F(1), 'R_lambda': response,
            'regularization_gap': 1-response, 'S0': -F(1, 2),
            'S_lambda': F(1, 2)-response, 'arithmetic_source': False,
            'status': 'EXACT_SYNTHETIC_COUNTEREXAMPLE_NOT_AUTHENTIC_NO_GO'}


def finite_family_obstruction(degree=16, probe_degree=20, gamma_modes=512,
                              kappa=F(20699, 1000000)):
    """Bound ALL even coefficients of P2 + span(P6,...,P_degree).

    A restricted K-dual supremum LOWER-bounds the true quotient residual,
    hence UPPER-bounds the sufficient lower certificate. Failure is a no-go
    for this finite family and this kappa, never negativity of the source.
    """
    integer(degree, 10, 16); integer(probe_degree, degree, 20)
    kappa = rational(kappa)
    if kappa <= 0:
        raise ResolventError('positive comparison constant required')
    vm = (2,) + tuple(range(6, degree+1, 2))
    qm = tuple(range(6, probe_degree+1, 2))
    source = L._pinned_source()
    vv = tuple(tuple(full_entry(i, j, gamma_modes) for j in vm) for i in vm)
    cross = tuple(tuple(full_entry(i, j, gamma_modes) for j in vm) for i in qm)
    kg = tuple(tuple(inverse_neumann_entry(F(1, 2), i, j) for j in qm) for i in qm)
    if not R.pd(kg):
        raise ArithmeticError('true K probe Gram not positive definite')
    ki = R.inv(kg)
    m = [[None]*len(vm) for _ in vm]
    for i in range(len(vm)):
        for j in range(i, len(vm)):
            z = vv[i][j] - sum((cross[a][i]*cross[b][j]*ki[a][b]/kappa
                                for a in range(len(qm)) for b in range(len(qm))), source.iv(0))
            m[i][j] = m[j][i] = z
    radius = max(sum((z.radius() for z in row), F()) for row in m)
    upper = tuple(tuple(m[i][j].mid() + (radius if i == j else 0)
                        for j in range(len(vm))) for i in range(len(vm)))
    proved = R.pd(R.scale(-1, upper))
    maximum = None
    if proved:
        hh = tuple(tuple(row[1:]) for row in upper[1:])
        b = tuple((row[0],) for row in upper[1:])
        maximum = upper[0][0]-R.mm(R.mm(R.trans(b), R.inv(hh)), b)[0][0]
        if maximum >= 0:
            raise ArithmeticError('negative completion failed')
    return {'trial_modes': vm, 'residual_probe_modes': qm, 'kappa': kappa,
            'gamma_modes': gamma_modes, 'source_git_blob': verify_original_suzuki_source()['source_git_blob'],
            'K_Gram': kg, 'K_inverse': ki,
            'source_trial_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in vv),
            'source_cross_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in cross),
            'criterion_upper': upper, 'entry_radius': radius,
            'all_complex_coefficients_excluded': proved, 'uniform_criterion_upper': maximum,
            'status': 'EXACT_SOURCE_FINITE_FAMILY_NO_GO' if proved else 'UNRESOLVED_INTERVAL_MAJORANT',
            'source_negative_direction': False, 'source_sign': 'OPEN', 'RH_PROVED': False}


def sqrt_upper(value, denominator=10**12):
    """Directed rational square-root upper; no floating acceptance."""
    value = rational(value); integer(denominator, 1, 10**15)
    if value < 0:
        raise ResolventError('nonnegative radicand required')
    n = isqrt(value.numerator*denominator**2//value.denominator)
    if F(n*n, denominator**2) < value:
        n += 1
    return F(n, denominator)


def certified_zero_trial_lower(gamma_modes=20, grid=512):
    """Source-specific R0 caps from U=0, per-sector derivative Hilbert-Schmidt norm.

    The exact finite-J derivative is Lipschitz with V_J, because |P_k|<=1
    for k=1..4. On each full cell integrate (m+V_J*|x-mid|)^2 exactly.
    Tail Young gives OPERATOR error eta_J, not a finite-stage source claim.
    """
    from .tate_suzuki_shorting import (authentic_suzuki_legendre_derivative_point,
        original_first_prime_derivative_bv_bound, original_gamma_derivative_l1_tail)
    integer(gamma_modes, 1, 20); integer(grid, 2, 1024)
    if grid % 2:
        raise ResolventError('even grid required for exact reflection reuse')
    verify_runtime_source()
    h = F(1, grid)
    lip = original_first_prime_derivative_bv_bound(gamma_modes)
    eta = original_gamma_derivative_l1_tail(gamma_modes)
    columns = []
    for k in range(1, 5):
        samples = []
        midpoint_energy = linear_error = quadratic_error = F()
        for i in range(grid//2):
            x = F(2*i+1, 2*grid)
            z = authentic_suzuki_legendre_derivative_point(k, x, gamma_modes)
            samples.append((x, z.lo, z.hi))
            m = max(abs(z.lo), abs(z.hi))
            # Factor 2 reuses reflection; this covers the WHOLE interval.
            midpoint_energy += 2*h*m*m
            linear_error += m*lip*h*h
            quadratic_error += lip*lip*h**3/6
        columns.append({'mode': k, 'positive_half_midpoint_intervals': tuple(samples),
                        'midpoint_absolute_energy_upper': midpoint_energy,
                        'between_cell_linear_error': linear_error,
                        'between_cell_quadratic_error': quadratic_error,
                        'finite_J_whole_interval_energy_upper': midpoint_energy+linear_error+quadratic_error})
    kappa = F(20699, 1000000)
    sectors = {}
    for name, modes in (('odd', (1, 3)), ('even', (2, 4))):
        trace = sum(((2*k+1)*columns[k-1]['finite_J_whole_interval_energy_upper'] for k in modes), F())
        root = sqrt_upper(trace)
        full = (root+eta)**2
        sectors[name] = {'modes': modes, 'finite_J_normalized_trace_upper': trace,
                         'trace_sqrt_upper': root, 'full_derivative_operator_squared_upper': full,
                         'R0_operator_upper_cap': full/kappa,
                         'whole_Gamma_derivative_operator_tail': eta}
    verify_runtime_source()
    return {'status': 'EXACT_SOURCE_INTERVAL_LOWER_BOUND_CONDITIONAL_ON_INHERITED_COERCIVITY',
            'source_git_blob': verify_original_suzuki_source()['source_git_blob'],
            'trial': 'U=0', 'gamma_modes': gamma_modes, 'grid': grid,
            'columns': columns, 'BV_Lipschitz': lip, 'Legendre_sup': F(1),
            'kappa': kappa, 'sectors': sectors,
            'certified_order': 'A - direct_sum(c_odd I_odd,c_even I_even) <= S0',
            'quotient_projection_used': 'contraction only, no subtraction',
            'Gamma_tail_closed_for_this_lower_bound': True,
            'target_S0_sign': 'OPEN', 'RH_PROVED': False}
