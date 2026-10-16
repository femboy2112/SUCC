"""Authentic four-low Schur research: quotient residuals and signed trials.

Analytic statements and domains: FOUR_LOW_SCHUR_CROSSPOLLINATION.md.
Exact polynomial algebra and pinned source intervals are certificates only
within their stated scope. mpmath/numpy/scipy results are NUMERICAL, not
continuum sign certificates. No zero coordinates or compact inverse at zero.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path

from . import suzuki_legendre_source as L
from .suzuki_moment_schur import parity_blocks
from .tate_suzuki_shorting import verify_original_suzuki_source

KAPPA = F(1, 50)
SHARPER_KAPPA = F(20699, 1000000)
LOW_MODES = (1, 2, 3, 4)
SOURCE_FILES = (
    'observational_succ/source_weil_hierarchy.py',
    'observational_succ/signed_gprime_enclosure.py',
    'observational_succ/tate_weighted_bessel_four_schur.py',
    'observational_succ/tate_four_low_compensator.py',
    'observational_succ/one_object_residual_schur.py',
    'observational_succ/one_object_relative_residual.py',
    'observational_succ/suzuki_moment_schur.py',
    'observational_succ/tate_suzuki_shorting.py',
    'observational_succ/suzuki_legendre_source.py',
    'research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_SCHUR.md',
    'provenance/IMPORT_MANIFEST.json',
)


class FourLowError(ValueError):
    pass


def _integer(n, lo, hi):
    if type(n) is not int or not lo <= n <= hi:
        raise FourLowError(f'exact integer in [{lo},{hi}] required')
    return n


def source_snapshot():
    """Actual bytes; the founding import is distinct from the later PR85 pin."""
    passport = verify_original_suzuki_source()
    root = Path(__file__).resolve().parents[1]
    return dict(passport, sha256={p: sha256((root/p).read_bytes()).hexdigest()
                                 for p in SOURCE_FILES})


def quotient_polynomial_gram(columns):
    """Exact derivative Gram modulo derivatives of P1..P4, on I=(-1/2,1/2).

    This verifies algebra on polynomial inputs, not authenticity of a source.
    The analytic theorem licenses the same quotient for H1 source responses.
    """
    if not columns or len(columns) > 4:
        raise FourLowError('one to four polynomial columns required')
    polys = tuple(tuple(L.q(x) for x in p) for p in columns)
    if any(not p or len(p) > 41 for p in polys):
        raise FourLowError('nonempty polynomial of degree <=40 required')
    ds = tuple(L.poly_derivative(p) for p in polys)
    basis = tuple(L.legendre_polynomial(k, F(1, 2)) for k in range(4))
    def pairing(p, q):
        return L.poly_integral(L.poly_mul(p, q), -F(1, 2), F(1, 2))
    coeff = tuple(tuple((2*k+1)*pairing(d, p) for k, p in enumerate(basis))
                  for d in ds)
    residuals = []
    for d, cs in zip(ds, coeff):
        for c, p in zip(cs, basis):
            d = L.poly_add(d, p, -c)
        residuals.append(d)
    raw = tuple(tuple(pairing(p, q) for q in ds) for p in ds)
    quotient = tuple(tuple(pairing(p, q) for q in residuals) for p in residuals)
    return {'raw': raw, 'quotient': quotient, 'removed_coefficients': coeff,
            'residual_polynomials': tuple(residuals), 'source_sign_certified': False}


def exact_parity_four(matrix):
    """Reject a symmetry violation; do not zero it by decree."""
    a = tuple(tuple(L.q(x) for x in row) for row in matrix)
    if len(a) != 4 or any(len(row) != 4 for row in a):
        raise FourLowError('four by four exact low matrix required')
    return parity_blocks(a, 4)


def certified_scalar_improvement():
    """Re-run inherited rational proof, then retain its stronger constant.

    This sharpens a coarse response/explicit counterterm, not original sign.
    """
    from .tate_weighted_bessel_four_schur import source_weighted_four_moment_certificate
    from .one_object_residual_schur import original_source_cancellation_certificate
    source = source_weighted_four_moment_certificate()
    norm = original_source_cancellation_certificate()
    if source['elementary_rational_lower'] != SHARPER_KAPPA:
        raise FourLowError('inherited exact high bound changed')
    if not norm['gprime_L1_STRICT_upper'] < F(11, 40):
        raise FourLowError('source derivative bound not established')
    response = F(11, 40)**2/SHARPER_KAPPA
    return {'kappa': SHARPER_KAPPA, 'response_upper': response,
            'old_response_upper': F(121, 32),
            'explicit_counterterm': F(4),
            'corrected_low_margin': F(4)-F(11, 40)-response,
            'inherited_fraction_sha256': source['source_fraction_bytes_sha256'],
            'original_sign_certified': False, 'RH_PROVED': False}


def source_low_intervals(rank=8, gamma_modes=64):
    """Reuse source-native exact polynomial/exponential integrals, no new kernel."""
    _integer(rank, 4, 12)
    _integer(gamma_modes, 1, 75)
    verify_original_suzuki_source()
    matrix = []
    for i in range(1, rank+1):
        row = []
        for j in range(1, rank+1):
            row.append(matrix[j-1][i-1] if j < i else
                       L.authentic_full_low_entry(i, j, J=gamma_modes))
        matrix.append(tuple(row))
    from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
    return {'matrix': tuple(matrix), 'J': gamma_modes,
            'positive_tail_operator_upper': authentic_positive_gamma_tail_norm(gamma_modes),
            'coordinates': 'unnormalized P_n(2t)', 'full_source_sign_certified': False}


def numerical_full_source_matrix(rank=12, digits=60):
    """Full signed source by independently integrating g' against pair primitives.

    For rho_ij from the EXISTING exact Legendre adapter and R'=rho, R(1)=0,
    <Pi,G Pj>=-integral_0^1 g'(r) R(r) dr. g(0)=0 and both poles,
    original contact, true p2 and the complete Gamma derivative are retained.
    mpmath quadrature is explicitly NOT an interval enclosure.
    """
    import mpmath as mp
    _integer(rank, 4, 20)
    _integer(digits, 35, 100)
    source = L._pinned_source()
    verify_original_suzuki_source()
    with mp.workdps(digits):
        def scalar(q):
            return mp.mpf(q.numerator)/q.denominator
        contact = scalar(source.contact_iv().mid())
        b = scalar(source.log2_iv().mid())
        weight = b*scalar(source.sqrt_inverse(2).mid())
        def gp(r, prime=True):
            z = mp.exp(-r/2)
            gamma = -(mp.log1p(z)-mp.log(-mp.expm1(-r/2)))/2-mp.atan(z)
            return -4*mp.sinh(r/2)+contact/2+gamma+(weight if prime and r > b else 0)
        moments = [mp.quad(lambda r, k=k: gp(r)*(r**k-1), [0, b, 1])
                   for k in range(1, 2*rank+3)]
        rows = []
        for i in range(1, rank+1):
            row = []
            for j in range(1, rank+1):
                if (i+j) % 2:
                    value = mp.mpf(0)
                elif j < i:
                    value = rows[j-1][i-1]
                else:
                    rho = L.poly_two_variable_cross(i, j, F(1, 2))
                    value = -mp.fsum(scalar(c)*moments[k]/(k+1)
                                     for k, c in enumerate(rho))
                row.append(value)
            rows.append(row)
        return {'matrix_decimal': [[mp.nstr(x, digits-8) for x in row] for row in rows],
                'digits': digits, 'rank': rank, 'gamma': 'complete analytic derivative',
                'source': 'PINNED_ORIGINAL_SUZUKI_NUMERICAL_QUADRATURE',
                'source_sign_certified': False, 'nontrivial_zero_coordinates_used': False}


def numerical_derivative_grid(rank=12, nodes_per_panel=24):
    """Separate scipy convolution of the full source g' with Legendre columns.

    Split both inner/outer quadrature at original prime2 wavefronts and the
    logarithmic diagonal. Stored errors are quadrature estimates, NOT bounds.
    """
    import numpy as np
    from scipy.integrate import quad_vec
    from scipy.special import eval_legendre
    _integer(rank, 4, 20)
    _integer(nodes_per_panel, 8, 128)
    source = L._pinned_source()
    verify_original_suzuki_source()
    b = float(source.log2_iv().mid())
    weight = b*float(source.sqrt_inverse(2).mid())
    contact = float(source.contact_iv().mid())
    modes = np.arange(1, rank+1)
    roots, weights = np.polynomial.legendre.leggauss(nodes_per_panel)
    cuts = [-.5, .5-b, 0., b-.5, .5]
    xs, ws = [], []
    for left, right in zip(cuts, cuts[1:]):
        xs.extend((left+right)/2+(right-left)/2*roots)
        ws.extend((right-left)/2*weights)
    values, errors = [], []
    for x in xs:
        def integrand(y):
            delta = x-y
            r = abs(delta)
            if r == 0:  # arbitrary value on a measure-zero set
                return np.zeros(rank)
            z = np.exp(-r/2)
            gp = (-4*np.sinh(r/2)+contact/2
                  -(np.log1p(z)-np.log(-np.expm1(-r/2)))/2-np.arctan(z)
                  +(weight if r > b else 0))
            return np.sign(delta)*gp*eval_legendre(modes, 2*y)
        splits = sorted({-.5, .5, x, *[t for t in (x-b, x+b) if -.5 < t < .5]})
        v, error = quad_vec(integrand, -.5, .5, points=splits[1:-1],
                            epsabs=2e-12, epsrel=2e-12)
        values.append(v)
        errors.append(float(error))
    return {'x': np.asarray(xs), 'weights': np.asarray(ws),
            'derivatives': np.asarray(values), 'estimated_inner_errors': errors,
            'nodes_per_panel': nodes_per_panel, 'rigorous_error_bound': False}


def numerical_trial(full_matrix, derivative_grid, rank=8, trial='galerkin', frozen_U=None):
    """Parity-respecting finite high responses, evaluated on full source grid.

    A finite solve is a trial U only. The continuum lower bracket remains
    numerical because its derivative Gram is quadrature, not certified.
    'quotient_least_squares' minimizes the quotient derivative residual on
    this grid and is checked at a separate quadrature resolution in the probe.
    """
    import numpy as np
    from scipy.special import eval_legendre
    _integer(rank, 4, min(20, len(full_matrix['matrix_decimal'])))
    if trial not in ('zero', 'galerkin', 'quotient_least_squares'):
        raise FourLowError('unknown finite response trial')
    norms = np.sqrt(2*np.arange(1, rank+1)+1)
    g = np.asarray(full_matrix['matrix_decimal'], dtype=float)[:rank, :rank]
    g = norms[:, None]*g*norms[None, :]
    w, x = derivative_grid['weights'], derivative_grid['x']
    deriv = derivative_grid['derivatives'][:, :rank]*norms[None, :]
    p = np.stack([np.sqrt(2*k+1)*eval_legendre(k, 2*x) for k in range(4)], axis=1)
    quot = deriv-p@(p.T@(w[:, None]*deriv))
    U = np.zeros((rank-4, 4))
    for parity in (() if frozen_U is not None else (0, 1)):
        lo = [i for i in range(4) if (i+1) % 2 == parity]
        hi = [i for i in range(4, rank) if (i+1) % 2 == parity]
        if hi and trial == 'galerkin':
            if np.linalg.eigvalsh(g[np.ix_(hi, hi)])[0] <= 0:
                raise FourLowError('finite high solve not positive')
            response = np.linalg.solve(g[np.ix_(hi, hi)], g[np.ix_(hi, lo)])
            U[np.ix_(np.asarray(hi)-4, lo)] = response
        elif hi and trial == 'quotient_least_squares':
            response = np.linalg.lstsq(np.sqrt(w)[:, None]*quot[:, hi],
                                      np.sqrt(w)[:, None]*quot[:, lo], rcond=None)[0]
            U[np.ix_(np.asarray(hi)-4, lo)] = response
    if frozen_U is not None:
        U = np.asarray(frozen_U, dtype=float)
        if U.shape != (rank-4, 4) or not np.isfinite(U).all():
            raise FourLowError('frozen high response has invalid shape/values')
        for i in range(rank-4):
            for j in range(4):
                if (i-j) % 2 and U[i, j] != 0:
                    raise FourLowError('frozen trial mixes reflection parities')
    V = np.concatenate((np.eye(4), -U))
    Ltrial = g[:4, 4:]@U+U.T@g[4:, :4]-U.T@g[4:, 4:]@U
    raw = deriv@V
    qr = quot@V
    Craw = raw.T@(w[:, None]*raw)
    Cquot = qr.T@(w[:, None]*qr)
    upper = g[:4, :4]-Ltrial
    lower = upper-Cquot/float(KAPPA)
    # A second matrix bearing from the actual derivative convolution.
    primitive = np.stack([(eval_legendre(n+1, 2*x)-eval_legendre(n-1, 2*x))
                           /(2*np.sqrt(2*n+1)) for n in range(1, rank+1)], axis=1)
    alternative = -primitive.T@(w[:, None]*deriv)
    def blocks(a):
        return {label: a[np.ix_(ix, ix)].tolist()
                for label, ix in (('odd', [0, 2]), ('even', [1, 3]))}
    return {'rank': rank, 'trial': trial, 'trial_frozen_before_evaluation': frozen_U is not None,
            'coordinates': 'orthonormal sqrt(2n+1) P_n(2t)',
            'U': U.tolist(), 'A': g[:4, :4].tolist(), 'L_U': Ltrial.tolist(),
            'C_raw': Craw.tolist(), 'C_quotient': Cquot.tolist(),
            'upper_short': upper.tolist(), 'quotient_lower_short': lower.tolist(),
            'upper_parity': blocks(upper), 'lower_parity': blocks(lower),
            'upper_eigenvalues': np.linalg.eigvalsh(upper).tolist(),
            'raw_lower_eigenvalues': np.linalg.eigvalsh(upper-Craw/float(KAPPA)).tolist(),
            'quotient_lower_eigenvalues': np.linalg.eigvalsh(lower).tolist(),
            'raw_gram_trace': float(np.trace(Craw)),
            'quotient_gram_trace': float(np.trace(Cquot)),
            'full_source_matrix_crosscheck_max_difference': float(np.max(abs(g-alternative))),
            'finite_high_minimum': float(np.linalg.eigvalsh(g[4:, 4:])[0]) if rank > 4 else None,
            'status': 'FINITE_NUMERICAL_ONLY', 'original_sign_certified': False,
            'RH_PROVED': False}


def source_specific_controls(full_matrix):
    """Actual-source channel mutations, each explicitly barred from authentication.

    A fake primitive 6 is invisible inside |r|<=1; its tape MUST be checked.
    Missing p2 / duplicated Gamma / contact shift are parity-even too, so
    parity cannot authenticate the source. No control replaces the live source.
    """
    import numpy as np
    from .tate_suzuki_shorting import gammas_from_prime_mutation, PINNED_TAPE, ShortingContractError
    from .suzuki_moment_schur import low_inverse_neumann
    source = L._pinned_source()
    verify_original_suzuki_source()
    rank = 4
    g = np.asarray(full_matrix['matrix_decimal'], dtype=float)[:rank, :rank]
    prime = np.array([[float(L.authentic_first_prime_low_entry(i, j).mid())
                       for j in LOW_MODES] for i in LOW_MODES])
    pole = np.array([[float(L.authentic_pole_low_entry(i, j).mid())
                      for j in LOW_MODES] for i in LOW_MODES])
    K = np.array(low_inverse_neumann(F(1, 2), 4), dtype=float)
    gamma = g-prime-pole+float(source.contact_iv().mid())*K
    fake_rejected = False
    try:
        gammas_from_prime_mutation(PINNED_TAPE+((6, 6),))
    except ShortingContractError:
        fake_rejected = True
    mutations = (prime, gamma, K, pole)
    parity_preserved = all(a[i, j] == 0 for a in mutations
                           for i in range(4) for j in range(4) if (i-j) % 2)
    fake_invisible = source.log_iv(6).lo > 1 and source.real_prime_power(6) is None
    return {'missing_true_prime2_low_delta_frobenius': float(np.linalg.norm(prime)),
            'duplicate_gamma_low_delta_frobenius': float(np.linalg.norm(gamma)),
            'contact_plus_one_low_delta_frobenius': float(np.linalg.norm(K)),
            'pole_deletion_low_delta_frobenius': float(np.linalg.norm(pole)),
            'all_these_mutations_preserve_parity': parity_preserved,
            'fake_primitive6_has_no_first_window_hinge': fake_invisible,
            'fake_primitive6_tape_rejected': fake_rejected,
            'matched_nonEuler_outside_window': 'same local source, extra symmetric hinge at log(6)',
            'local_parity_or_Gram_cannot_authenticate_global_Euler_source': True,
            'mutations_accepted_as_authentic': False}


def certified_trial_obstruction(v, high_witness, gamma_modes=64):
    """Actual-source obstruction to this trial's sufficient residual criterion.

    v=x-Ux and q in QH are explicit real rational Legendre polynomials.
    S_trial(x)=<v,Gv>; C_quot(x)>=|<q,Gv>|^2/<q,Kq>.
    Thus a STRICTLY NEGATIVE returned upper proves the LOWER CERTIFICATE
    A-L_U-50 C_quot fails on x. It does NOT prove S0 or G is negative.
    All omitted Gamma rungs are included with a proven operator norm cap.
    """
    from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
    from .suzuki_moment_schur import inverse_neumann_entry
    source = L._pinned_source()
    verify_original_suzuki_source()
    _integer(gamma_modes, 1, 75)
    v, q = tuple(L.q(x) for x in v), tuple(L.q(x) for x in high_witness)
    if len(v) != len(q) or not 5 <= len(v) <= 20 or any(q[:4]) or not any(q):
        raise FourLowError('same 5..20 Legendre coordinates, nonzero Q-high witness required')
    if not any(v[:4]):
        raise FourLowError('nonzero low x required for a Schur trial obstruction')
    nzv = [i for i, x in enumerate(v, 1) if x]
    nzq = [i for i, x in enumerate(q, 1) if x]
    cache = {}
    def entry(i, j):
        key = tuple(sorted((i, j)))
        if key not in cache:
            cache[key] = L.authentic_full_low_entry(*key, J=gamma_modes)
        return cache[key]
    vv = source.iv(0)
    qv = source.iv(0)
    for i in nzv:
        for j in nzv:
            vv += v[i-1]*v[j-1]*entry(i, j)
    for i in nzq:
        for j in nzv:
            qv += q[i-1]*v[j-1]*entry(i, j)
    vnorm2 = sum((c*c/F(2*i+1) for i, c in enumerate(v, 1)), F())
    qnorm2 = sum((c*c/F(2*i+1) for i, c in enumerate(q, 1)), F())
    def sqrt_upper(r):
        scale = 10**12
        numerator = r.numerator*scale*scale
        k = isqrt(numerator//r.denominator)
        if k*k*r.denominator < numerator:
            k += 1
        return F(k, scale)
    tail = authentic_positive_gamma_tail_norm(gamma_modes)
    cross_error = tail*sqrt_upper(vnorm2*qnorm2)
    cross_lo, cross_hi = qv.lo-cross_error, qv.hi+cross_error
    abs_lower = max(F(), cross_lo, -cross_hi)
    kneumann = sum((q[i-1]*q[j-1]*inverse_neumann_entry(F(1, 2), i, j)
                    for i in nzq for j in nzq), F())
    if kneumann <= 0:
        raise FourLowError('nonzero high witness has invalid primitive norm')
    residual_lower = abs_lower**2/kneumann
    short_upper = vv.hi+tail*vnorm2
    criterion_upper = short_upper-residual_lower/KAPPA
    return {'v_unnormalized_Legendre': v, 'high_witness': q, 'gamma_modes': gamma_modes,
            'positive_Gamma_tail_norm_upper': tail,
            'full_source_cross_interval': (cross_lo, cross_hi),
            'high_witness_K_energy': kneumann, 'quotient_residual_energy_lower': residual_lower,
            'trial_short_upper': short_upper,
            'sufficient_criterion_direction_upper': criterion_upper,
            'this_trial_sufficient_criterion_certifiably_fails': criterion_upper < 0,
            'source_original_G_negative': False, 'source_original_sign': 'OPEN',
            'RH_PROVED': False}
