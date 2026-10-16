"""Round II authentic-source Schur experiments and exact ansatz obstructions.

No infinite source sign is inferred from a numerical matrix. The source is
PR85's byte-pinned signed Suzuki kernel on L2_0(-1/2,1/2). See the assigned
2026-10-16 dossier for all domains, quantifiers and continuum proof debt.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache

from . import suzuki_legendre_source as L
from . import one_object_relative_residual as R
from .four_low_schur_proof_teeth import SHARPER_KAPPA, source_snapshot
from .suzuki_moment_schur import inverse_neumann_entry
from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
from .tate_suzuki_shorting import verify_original_suzuki_source


class ObserverSourceError(ValueError):
    pass


def _integer(x, lo, hi):
    if type(x) is not int or not lo <= x <= hi:
        raise ObserverSourceError(f'exact integer {lo}..{hi} required')
    return x


def _q(x):
    if type(x) not in (int, F):
        raise ObserverSourceError('exact int/Fraction required; no bool or float')
    return F(x)


def parity_psd_test(matrix):
    """Congruence-free exact real 4x4 test in low order (P1,P2,P3,P4).

    Applies to a supplied finite FORM matrix only. A coefficient Gram metric
    is irrelevant to Loewner sign, but is needed for operator eigenvalues.
    This function authenticates no arithmetic source and proves no premises.
    """
    a = R.matrix(matrix, square=True)
    if len(a) != 4 or not R.sym(a):
        raise ObserverSourceError('real symmetric four-low form required')
    if any(a[i][j] for i in range(4) for j in range(4) if (i-j) % 2):
        raise ObserverSourceError('reflection intertwining fails')
    sectors = {}
    for name, ix in (('odd', (0, 2)), ('even', (1, 3))):
        block = tuple(tuple(a[i][j] for j in ix) for i in ix)
        determinant = R.det(block)
        sectors[name] = {'matrix': block, 'determinant': determinant,
                         'PSD': block[0][0] >= 0 and block[1][1] >= 0 and determinant >= 0}
    return {'sectors': sectors, 'PSD': all(s['PSD'] for s in sectors.values()),
            'status': 'EXACT_FINITE_CHECK', 'authentic_source_identified': False}


@lru_cache(maxsize=2048)
def _gamma_entry(i, j, gamma_modes):
    """Existing exact OU pair kernel, extended finite budget, same source.

    For alpha>256 use 0<exp(-alpha)<2^-floor(alpha), since e>2.
    No transcendental point value is accepted as an interval endpoint.
    """
    source = L._pinned_source()
    z = source.iv(0)
    for k in range(gamma_modes):
        d, alpha = 4*k+1, F(4*k+1, 2)
        if alpha <= 256:
            pair = L.source_ou_pair_interval(i, j, F(1, 2), alpha)
        else:
            a, b = L.source_ou_pair_affine(i, j, F(1, 2), alpha)
            exponential = (F(), F(1, 2**(alpha.numerator//alpha.denominator)))
            pair = L.source_interval_round(source, L.interval_add((a, a), L.interval_scale(exponential, b)))
        z += F(4, d*d)*pair
    return z


def polynomial_source_entry(i, j, gamma_modes=512):
    """Full-source entry interval, with an explicit WHOLE Gamma tail.

    Polynomials are unnormalized P_i(2t); i,j>=1. The conservative tail
    tau/sqrt((2i+1)(2j+1)) is enlarged rationally to tau/min(2i+1,2j+1).
    The true tail is PSD; the symmetric entry enclosure deliberately does
    not count that positivity twice.
    """
    _integer(i, 1, 16); _integer(j, 1, 16); _integer(gamma_modes, 1, 768)
    source = L._pinned_source()
    if (i+j) % 2:
        return source.iv(0)
    i, j = sorted((i, j))
    z = (_gamma_entry(i, j, gamma_modes)
         + L.authentic_first_prime_low_entry(i, j)
         + L.authentic_pole_low_entry(i, j)
         - source.contact_iv()*inverse_neumann_entry(F(1, 2), i, j))
    error = authentic_positive_gamma_tail_norm(gamma_modes)/min(2*i+1, 2*j+1)
    return source.I(z.lo-error, z.hi+error)


def _upper_matrix(interval_matrix):
    """A true symmetric interval matrix M satisfies M<=mid(M)+rho I.

    rho=max row sum of radii; follows from the symmetric operator norm
    bound. Fractions retain outward source intervals throughout.
    """
    n = len(interval_matrix)
    midpoint = tuple(tuple(z.mid() for z in row) for row in interval_matrix)
    if not R.sym(midpoint) or any(interval_matrix[i][j] != interval_matrix[j][i]
                                  for i in range(n) for j in range(n)):
        raise ObserverSourceError('symmetric interval form required')
    radius = max(sum((z.radius() for z in row), F()) for row in interval_matrix)
    upper = tuple(tuple(midpoint[i][j] + (radius if i == j else 0)
                        for j in range(n)) for i in range(n))
    return upper, radius


def _ldl_pivots(a):
    n = len(a)
    lower = [[F(i == j) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        dj = a[j][j]-sum((lower[j][k]**2*diagonal[k] for k in range(j)), F())
        diagonal.append(dj)
        if dj <= 0:
            return tuple(diagonal)
        for i in range(j+1, n):
            lower[i][j] = (a[i][j]-sum((lower[i][k]*lower[j][k]*diagonal[k]
                                       for k in range(j)), F()))/dj
    return tuple(diagonal)


def certify_degree_eight_family(kappa=SHARPER_KAPPA, gamma_modes=512):
    """Certify failure for ALL v=P2+c6 P6+c8 P8, c6,c8 real/complex.

    For q-space span(P6,P8,P10,P12), C_quot(v)>=c(v)*K_q^-1*c(v).
    Therefore the sufficient lower criterion <= v*M*v. This function
    encloses M with genuine source intervals and tests its NEGATIVE
    definiteness. It does not test negativity of the original G or S0.
    Even kappa=1/5 is an intentionally HYPOTHETICAL strengthened constant:
    failure there excludes every 0<kappa<=1/5, without claiming D>=K/5.
    """
    kap = _q(kappa)
    if kap <= 0:
        raise ObserverSourceError('positive residual comparison constant required')
    _integer(gamma_modes, 1, 768)
    verify_original_suzuki_source()
    source = L._pinned_source()
    vmodes, qmodes = (2, 6, 8), (6, 8, 10, 12)
    vv = tuple(tuple(polynomial_source_entry(i, j, gamma_modes) for j in vmodes) for i in vmodes)
    cross = tuple(tuple(polynomial_source_entry(i, j, gamma_modes) for j in vmodes) for i in qmodes)
    K = tuple(tuple(inverse_neumann_entry(F(1, 2), i, j) for j in qmodes) for i in qmodes)
    if not R.pd(K):
        raise ArithmeticError('actual finite K Gram is not positive definite')
    kinv = R.inv(K)
    # Set lower triangle by symmetry, so rounding path never invents skew.
    m = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            entry = vv[i][j] - sum((cross[a][i]*cross[b][j]*kinv[a][b]/kap
                                    for a in range(4) for b in range(4)), source.iv(0))
            m[i][j] = m[j][i] = entry
    upper, radius = _upper_matrix(m)
    pivots = _ldl_pivots(R.scale(-1, upper))
    proved = len(pivots) == 3 and all(d > 0 for d in pivots)
    max_bound, optimizer = None, None
    if proved:
        hh = tuple(tuple(upper[i][j] for j in (1, 2)) for i in (1, 2))
        b = ((upper[1][0],), (upper[2][0],))
        ihb = R.mm(R.inv(hh), b)
        max_bound = upper[0][0]-R.mm(R.trans(b), ihb)[0][0]
        optimizer = tuple(-row[0] for row in ihb)
        if max_bound >= 0:
            raise ArithmeticError('negative-definite square completion inconsistent')
    return {'source_git_blob': verify_original_suzuki_source()['source_git_blob'],
            'source_radius': F(1, 2), 'low_input': 'P2(2t)',
            'trial_family': 'ALL U(P2) in complex span(P6(2t),P8(2t))',
            'coefficients_quantified': 'ALL real or complex c6,c8, not a finite search',
            'high_residual_probe_modes': qmodes, 'kappa_tested': kap,
            'this_kappa_certified_as_source_high_bound': kap <= SHARPER_KAPPA,
            'gamma_modes': gamma_modes,
            'whole_Gamma_tail_norm_upper': authentic_positive_gamma_tail_norm(gamma_modes),
            'full_source_vv_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in vv),
            'full_source_cross_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in cross),
            'K_probe_Gram': K, 'K_probe_inverse': kinv,
            'criterion_interval_matrix': tuple(tuple((z.lo, z.hi) for z in row) for row in m),
            'criterion_Loewner_upper': upper, 'entry_radius_row_sum': radius,
            'minus_upper_LDL_pivots': pivots,
            'all_coefficients_criterion_fails': proved,
            'criterion_uniform_upper_for_P2': max_bound,
            'upper_majorant_maximizer': optimizer,
            'status': 'PAPER_PROVED_WITH_EXACT_SOURCE_INTERVAL_CERTIFICATE' if proved else 'UNRESOLVED',
            'source_original_sign': 'OPEN', 'source_original_negative_direction': False,
            'RH_PROVED': False}


def threshold_response_basis(knots=(F(0), F(1, 8), F(193147, 1000000), F(1, 4), F(3, 8), F(1, 2))):
    """Exact parity-preserving degree-zero splines projected into QH.

    The rational knot 193147/10^6 approximates log2-1/2 for trial selection
    ONLY. Actual kernel displacement remains the authenticated log2. The
    first even cell is omitted to remove the sole constant-step dependency.
    Low polynomials P0..P4 are subtracted with exact rational moments.
    """
    ks = tuple(_q(k) for k in knots)
    if (not 3 <= len(ks) <= 18 or ks[0] != 0 or ks[-1] != F(1, 2)
            or any(a >= b for a, b in zip(ks, ks[1:]))):
        raise ObserverSourceError('strict increasing rational half-interval partition required')
    result = []
    for parity in (1, -1):
        for j, (left, right) in enumerate(zip(ks, ks[1:])):
            if parity == 1 and j == 0:
                continue
            projection = []
            for n in range(5):
                p = L.legendre_polynomial(n, F(1, 2))
                moment = L.poly_integral(p, left, right)+parity*L.poly_integral(p, -right, -left)
                projection.append((2*n+1)*moment)
            norm2 = 2*(right-left)-sum((c*c/F(2*n+1) for n, c in enumerate(projection)), F())
            if norm2 <= 0:
                raise ArithmeticError('projected cell vanished')
            result.append({'left': left, 'right': right, 'reflection_eigenvalue': parity,
                           'P0_to_P4_projection': tuple(projection), 'L2_norm_squared': norm2})
    return tuple(result)


def _numerical_kernel_channels(r):
    """Full authentic g(r) by a mod-4 dilogarithm filter; NOT an enclosure.

    4 sum_(n=1 mod 4) z^n/n^2 = Li2(z)-Li2(-z)+2 Im Li2(i z).
    Its derivative is -atanh(exp(-r/2))-atan(exp(-r/2)). Thus this
    evaluates the COMPLETE real Gamma tower, not a finite Gamma stage.
    """
    import numpy as np
    from scipy.special import spence
    s = L._pinned_source()
    r = np.asarray(r, dtype=float)
    if np.any(r < 0) or np.any(r > 1+1e-14):
        raise ObserverSourceError('first-prime kernel distance outside [0,1]')
    z = np.exp(-r/2)
    gamma = (spence(1-z)-spence(1+z)+2*np.imag(spence(1-1j*z))
             -(np.pi*np.pi/4+2*0.91596559417721901505))
    # Catalan's numerical constant is a quadrature ingredient, never a proof.
    b = float(s.log2_iv().mid()); w = b*float(s.sqrt_inverse(2).mid())
    return {'poles': -8*(np.cosh(r/2)-1),
            'contact': float(s.contact_iv().mid())*r/2,
            'prime2': w*np.maximum(r-b, 0), 'gamma': gamma}


def numerical_threshold_grid(basis, nodes_per_panel=12):
    """Whole-source convolution on threshold-aware projected step responses.

    Step derivative responses are exact identities g(x-l)-g(x-r), then
    numerically evaluated via complete dilogarithms. Polynomial low columns
    use direct g' convolution, a different representation of the same source.
    Quadrature error estimates do NOT certify the continuum Gram.
    """
    import numpy as np
    from scipy.integrate import quad_vec
    from scipy.special import eval_legendre
    _integer(nodes_per_panel, 4, 40)
    verify_original_suzuki_source()
    _validate_threshold_basis(basis)
    source = L._pinned_source()
    b = float(source.log2_iv().mid()); weight = b*float(source.sqrt_inverse(2).mid())
    contact = float(source.contact_iv().mid())
    edges = {-.5, 0., .5}
    for c in basis:
        edges.update((float(c['left']), float(c['right']), -float(c['left']), -float(c['right'])))
    cuts = sorted(edges | {x for e in edges for x in (e-b, e+b) if -.5 < x < .5})
    roots, weights = np.polynomial.legendre.leggauss(nodes_per_panel)
    xs, ws = [], []
    for left, right in zip(cuts, cuts[1:]):
        if right-left < 1e-12:
            continue
        xs.extend((left+right)/2+(right-left)/2*roots)
        ws.extend((right-left)/2*weights)
    x, w = np.array(xs), np.array(ws)
    lowd, estimates = [], []
    modes = np.arange(5)
    for xx in x:
        def integrand(y):
            d = xx-y; r = abs(d)
            if r == 0:
                return np.zeros(5)
            z = np.exp(-r/2)
            gp = (-4*np.sinh(r/2)+contact/2
                  -(np.log1p(z)-np.log(-np.expm1(-r/2)))/2-np.arctan(z)
                  +(weight if r > b else 0))
            return np.sign(d)*gp*eval_legendre(modes, 2*y)
        splits = sorted({xx, *[t for t in (xx-b, xx+b) if -.5 < t < .5]})
        val, error = quad_vec(integrand, -.5, .5, points=splits, epsabs=1e-11, epsrel=1e-11)
        lowd.append(val); estimates.append(float(error))
    lowd = np.asarray(lowd)
    def g(r):
        return sum(_numerical_kernel_channels(abs(r)).values())
    derivatives = [lowd[:, n] for n in range(1, 5)]
    primitive_low = [np.polynomial.Polynomial([float(c) for c in L.poly_primitive_zero_at_left(
                     L.legendre_polynomial(n, F(1, 2)), F(1, 2))])(x) for n in range(5)]
    primitives = primitive_low[1:]
    for col in basis:
        l, r, parity = float(col['left']), float(col['right']), col['reflection_eigenvalue']
        coeff = np.array(col['P0_to_P4_projection'], dtype=float)
        derivatives.append(g(x-l)-g(x-r)+parity*(g(x+r)-g(x+l))-lowd@coeff)
        rawprim = np.clip(x-l, 0, r-l)+parity*np.clip(x+r, 0, r-l)
        primitives.append(rawprim-np.column_stack(primitive_low)@coeff)
    derivatives = np.column_stack(derivatives)
    primitives = np.column_stack(primitives)
    rawmatrix = -primitives.T@(w[:, None]*derivatives)
    asymmetry = float(np.max(abs(rawmatrix-rawmatrix.T)))
    matrix = (rawmatrix+rawmatrix.T)/2
    momentbasis = np.column_stack([np.sqrt(2*n+1)*eval_legendre(n, 2*x) for n in range(4)])
    qr = derivatives-momentbasis@(momentbasis.T@(w[:, None]*derivatives))
    gram = qr.T@(w[:, None]*qr)
    return {'x': x, 'weights': w, 'source_matrix': matrix, 'quotient_gram': gram,
            'derivative_columns': derivatives, 'primitive_columns': primitives,
            'raw_matrix_asymmetry': asymmetry, 'inner_error_estimates_max': max(estimates),
            'nodes_per_panel': nodes_per_panel, 'panels': len(cuts)-1,
            'basis_identity': repr(basis),
            'rigorous_continuum_error_bound': False}


def numerical_threshold_trial(basis, grid, method='relative_optimal', frozen=None):
    """Frozen rational finite responses: Galerkin, K-least-squares, or bound-optimal.

    All three fit within the SAME source/domain/high carrier. Relative-optimal
    maximizes the Loewner lower quadratic within this finite trial space if
    its high Hessian is negative definite. That optimization is numerical.
    """
    import numpy as np
    from scipy.linalg import eigvalsh
    if method not in ('galerkin', 'relative_least_squares', 'relative_optimal'):
        raise ObserverSourceError('unrecognized response method')
    _validate_threshold_basis(basis)
    if grid.get('basis_identity') != repr(basis):
        raise ObserverSourceError('numerical source matrix belongs to a different response basis')
    g, c = grid['source_matrix'], grid['quotient_gram']
    n = len(basis); kap = float(SHARPER_KAPPA)
    U = np.zeros((n, 4))
    if frozen is None:
        objective = {'galerkin': g, 'relative_least_squares': c,
                     'relative_optimal': g-c/kap}[method]
        for parity in (1, -1):
            lo = [i for i in range(4) if (-1)**(i+1) == parity]
            hi = [4+i for i, col in enumerate(basis) if col['reflection_eigenvalue'] == parity]
            block = objective[np.ix_(hi, hi)]
            eigenvalues = np.linalg.eigvalsh(block)
            if method == 'relative_optimal' and eigenvalues[-1] >= 0:
                raise ObserverSourceError('relative-objective Hessian not negative definite')
            if method != 'relative_optimal' and eigenvalues[0] <= 0:
                raise ObserverSourceError('finite fit Gram not positive definite')
            U[np.ix_(np.array(hi)-4, lo)] = np.linalg.solve(block, objective[np.ix_(hi, lo)])
        frozen = tuple(tuple(F(round(float(z)*10**10), 10**10) for z in row) for row in U)
    else:
        frozen = tuple(tuple(_q(z) for z in row) for row in frozen)
        if len(frozen) != n or any(len(row) != 4 for row in frozen):
            raise ObserverSourceError('frozen response dimension mismatch')
    for i, row in enumerate(frozen):
        for j, z in enumerate(row):
            if z and basis[i]['reflection_eigenvalue'] != (-1)**(j+1):
                raise ObserverSourceError('frozen response violates exact parity')
    U = np.asarray(frozen, dtype=float)
    V = np.concatenate((np.eye(4), -U))
    W = np.sqrt(np.array([3, 5, 7, 9]))
    upper, cq = V.T@g@V, V.T@c@V
    lower = upper-cq/kap
    A = g[:4, :4]
    out = {'method': method, 'frozen_rational_U': frozen, 'high_dimension': n,
           'nodes_per_panel': grid['nodes_per_panel'], 'source_radius': '1/2',
           'status': 'TESTED_MODEL_NUMERICAL_ONLY', 'original_sign_certified': False,
           'continuum_Gram_error_certified': False, 'RH_PROVED': False,
           'raw_quadrature_matrix_asymmetry': grid['raw_matrix_asymmetry'],
           'estimated_inner_quadrature_error_max': grid['inner_error_estimates_max'],
           'upper_unnormalized': upper.tolist(), 'C_quot_unnormalized': cq.tolist(),
           'lower_unnormalized': lower.tolist(), 'sectors': {}}
    for name, ix in (('odd', [0, 2]), ('even', [1, 3])):
        idx = np.ix_(ix, ix)
        orth = W[ix, None]*W[None, ix]
        us, cs, ls, aa = upper[idx], cq[idx], lower[idx], A[idx]
        required = float(eigvalsh(cs, us)[-1]) if np.linalg.eigvalsh(us)[0] > 0 else None
        out['sectors'][name] = {'upper_operator_eigenvalues': np.linalg.eigvalsh(us*orth).tolist(),
                                'lower_operator_eigenvalues': np.linalg.eigvalsh(ls*orth).tolist(),
                                'required_kappa_for_this_numerical_trial': required,
                                'coupling_squared_upper_estimates': eigvalsh(aa-ls, aa).tolist(),
                                'coupling_squared_lower_estimates': eigvalsh(aa-us, aa).tolist()}
    return out


def numerical_channel_mutations():
    """Full kernel channel discrimination; mutants are NEVER genuine sources."""
    import numpy as np
    from .tate_suzuki_shorting import PINNED_TAPE, gammas_from_prime_mutation, ShortingContractError
    sample = np.array([.125, .375, .625, .875])
    ch = _numerical_kernel_channels(sample)
    s = L._pinned_source()
    b = float(s.log2_iv().mid())
    wrong_half = b*np.maximum(sample-b, 0)-ch['prime2']
    # Wrong real Gamma parity: d=4j+3 changes derivative tower, not a sign choice.
    wrong_gamma = sum(4/(4*j+3)**2*np.expm1(-(4*j+3)*sample/2) for j in range(1024))
    deltas = {'missing_prime2': -ch['prime2'], 'duplicated_prime2': ch['prime2'],
              'deleted_poles': -ch['poles'], 'sign_flipped_poles': -2*ch['poles'],
              'duplicated_real_Gamma': ch['gamma'], 'wrong_Gamma_parity_truncated_control': wrong_gamma-ch['gamma'],
              'wrong_half_density': wrong_half, 'deleted_contact': -ch['contact']}
    rejected = False
    try:
        gammas_from_prime_mutation(PINNED_TAPE+((6, 6),))
    except ShortingContractError:
        rejected = True
    return {'sample_distances': sample.tolist(),
            'source_channel_values': {k: v.tolist() for k, v in ch.items()},
            'mutation_max_abs_changes': {k: float(np.max(abs(v))) for k, v in deltas.items()},
            'all_mutations_preserve_reflection': True, 'fake_composite6_tape_rejected': rejected,
            'fake6_invisible_at_this_radius': s.log_iv(6).lo > 1,
            'mutation_authentication': 'REJECTED_NOT_ALTERNATIVE_ZETA_SOURCES',
            'status': 'NUMERICAL_CHANNEL_DISCRIMINATION_AND_EXACT_TAPE_REJECTION'}


def certified_high_kappa_ceiling(gamma_modes=512):
    """One genuine high Rayleigh upper bounds EVERY valid D>=kappa K.

    This is not a high lower bound. The frozen rational high vector was
    selected from an exploratory finite generalized eigenproblem; source
    intervals certify its displayed upper independently of that selection.
    """
    _integer(gamma_modes, 1, 768)
    modes, coeff = (5, 7, 11), (F(1), F(3, 2), -F(1, 2))
    source = L._pinned_source()
    value = sum((coeff[i]*coeff[j]*polynomial_source_entry(a, b, gamma_modes)
                 for i, a in enumerate(modes) for j, b in enumerate(modes)), source.iv(0))
    energy = sum((coeff[i]*coeff[j]*inverse_neumann_entry(F(1, 2), a, b)
                  for i, a in enumerate(modes) for j, b in enumerate(modes)), F())
    if energy <= 0:
        raise ArithmeticError('nonzero high vector must have positive K energy')
    return {'high_modes': modes, 'rational_coefficients': coeff, 'K_energy': energy,
            'G_energy_interval': (value.lo, value.hi),
            'every_valid_kappa_upper': value.hi/energy,
            'this_is_a_source_high_lower_bound': False,
            'does_this_exclude_kappa_above_one_fifth': value.hi/energy <= F(1, 5),
            'status': 'EXACT_SOURCE_INTERVAL_UPPER_BOUND', 'source_original_sign': 'OPEN'}


def _validate_threshold_basis(basis):
    """Check the actual high projection, not just a source-label string."""
    if type(basis) is not tuple or not 1 <= len(basis) <= 33:
        raise ObserverSourceError('bounded tuple of exact response columns required')
    seen = set()
    for c in basis:
        left, right = _q(c['left']), _q(c['right'])
        parity = c['reflection_eigenvalue']
        if (type(parity) is not int or parity not in (-1, 1)
                or not 0 <= left < right <= F(1, 2)
                or (left, right, parity) in seen):
            raise ObserverSourceError('invalid or duplicate reflected response cell')
        seen.add((left, right, parity))
        expected = []
        for n in range(5):
            p = L.legendre_polynomial(n, F(1, 2))
            expected.append((2*n+1)*(L.poly_integral(p, left, right)
                                      + parity*L.poly_integral(p, -right, -left)))
        supplied = tuple(_q(z) for z in c['P0_to_P4_projection'])
        if supplied != tuple(expected):
            raise ObserverSourceError('response column lacks the actual Q-high projection')
        norm2 = 2*(right-left)-sum((z*z/F(2*n+1) for n, z in enumerate(expected)), F())
        if _q(c['L2_norm_squared']) != norm2 or norm2 <= 0:
            raise ObserverSourceError('response Gram normalization mismatch')


def certified_polynomial_upper_short(gamma_modes=512):
    """True continuum S0 <= H_U <= explicit rational parity form.

    A NEW rational response is selected from the midpoint degree-eight source
    matrix, then frozen and re-evaluated with full-source intervals. Its
    selection is not the proof. This gives an upper bound only: positive
    eigenvalue caps never establish positivity of S0.
    """
    _integer(gamma_modes, 1, 768)
    source = L._pinned_source()
    entries = tuple(tuple(polynomial_source_entry(i, j, gamma_modes) for j in range(1, 9))
                    for i in range(1, 9))
    midpoint = tuple(tuple(z.mid() for z in row) for row in entries)
    U = [[F()]*4 for _ in range(4)]
    for lo, hi in (((0, 2), (4, 6)), ((1, 3), (5, 7))):
        D = tuple(tuple(midpoint[i][j] for j in hi) for i in hi)
        if not R.pd(D):
            raise ObserverSourceError('midpoint finite response solve not positive definite')
        Bstar = tuple(tuple(midpoint[i][j] for j in lo) for i in hi)
        fitted = R.mm(R.inv(D), Bstar)
        for i, high in enumerate(hi):
            for j, low in enumerate(lo):
                # Round the exact rational candidate to a declared finite grid.
                U[high-4][low] = F(round(fitted[i][j]*10**9), 10**9)
    v = tuple(tuple(F(i == j) if i < 4 else -U[i-4][j] for j in range(4)) for i in range(8))
    h = [[None]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            z = sum((v[a][i]*v[b][j]*entries[a][b] for a in range(8) for b in range(8)
                     if v[a][i] and v[b][j]), source.iv(0))
            h[i][j] = h[j][i] = z
    upper, radius = _upper_matrix(h)
    caps = {}
    for name, ix in (('odd', (0, 2)), ('even', (1, 3))):
        block = tuple(tuple(upper[i][j] for j in ix) for i in ix)
        metric = tuple(tuple(F(1, 2*i+3) if i == j else F() for j in ix) for i in ix)
        def valid(c):
            return R.psd(R.add(R.scale(c, metric), block, -1))
        left, right = F(), F(1)
        if not valid(right):
            raise ObserverSourceError('upper-cap search interval exhausted')
        for _ in range(32):
            middle = (left+right)/2
            if valid(middle):
                right = middle
            else:
                left = middle
        if not valid(right):
            raise ArithmeticError('exact generalized Loewner cap failed')
        caps[name] = {'operator_eigenvalue_upper': right, 'low_coordinate_metric': metric,
                      'upper_form_matrix': block,
                      'cap_minus_form_exact_PSD': True}
    return {'source_git_blob': verify_original_suzuki_source()['source_git_blob'],
            'gamma_modes': gamma_modes, 'frozen_rational_U_P5_to_P8_by_P1_to_P4': tuple(map(tuple, U)),
            'H_U_full_source_entry_intervals': tuple(tuple((z.lo, z.hi) for z in row) for row in h),
            'S0_upper_form': upper, 'entry_radius_row_sum': radius,
            'parity_operator_upper_caps': caps,
            'certified_order': 'S0 <= H_U <= S0_upper_form (unnormalized Legendre form coordinates)',
            'status': 'EXACT_SOURCE_INTERVAL_UPPER_BOUND',
            'source_sign_proved_by_positive_upper': False, 'source_original_sign': 'OPEN',
            'inherited_response_scalar_cap': F(75625, 20699),
            'inherited_lower_order': 'A - (75625/20699) I <= S0',
            'RH_PROVED': False}
