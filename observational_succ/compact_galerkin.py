"""Exact controls for compact compression and relative Schur approximation.

Paper proofs and domains: research/2026-10-16/COMPACT_SOURCE_GALERKIN.md.
The Suzuki bound replays the existing signed-source enclosure. Countermodels
are explicitly synthetic. No finite control certifies the original Schur sign.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

from . import suzuki_legendre_source as L
from .one_object_residual_schur import original_source_cancellation_certificate
from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
from .tate_suzuki_shorting import (
    original_gamma_derivative_l1_tail, rational_psd, verify_original_suzuki_source,
)


class CompactGalerkinError(ValueError):
    pass


def _integer(value, low=1, high=1000000):
    if type(value) is not int or not low <= value <= high:
        raise CompactGalerkinError(f'exact integer in [{low}, {high}] required')
    return value


def _rational(value):
    if type(value) not in (int, F):
        raise CompactGalerkinError('exact int/Fraction required, not bool or float')
    return F(value)


SOURCE_PATHS = (
    'observational_succ/source_weil_hierarchy.py',
    'observational_succ/signed_gprime_enclosure.py',
    'observational_succ/one_object_residual_schur.py',
    'observational_succ/tate_suzuki_shorting.py',
    'observational_succ/suzuki_legendre_source.py',
    'observational_succ/four_low_schur_proof_teeth.py',
    'provenance/IMPORT_MANIFEST.json',
)


def source_snapshot():
    root = Path(__file__).resolve().parents[1]
    return dict(verify_original_suzuki_source(), sha256={
        name: sha256((root/name).read_bytes()).hexdigest() for name in SOURCE_PATHS
    })


@lru_cache(maxsize=1)
def _derivative_budget():
    # Exact whole-interval cancellation enclosure, not point quadrature.
    return original_source_cancellation_certificate()


def source_legendre_bound(degree, gamma_modes=None):
    """Bound ||G-P_N G P_N|| on mean-zero L2(-1/2,1/2).

    P_N spans the authentic interval's Legendre modes 1..N. The optional
    gamma tail is for P_N G_J P_N, with exact source matrix entries; it is
    not a quadrature/midpoint error bound. Full analytic proof is CG-03.
    """
    n = _integer(degree)
    if gamma_modes is not None:
        _integer(gamma_modes)
    passport = verify_original_suzuki_source()
    r = _derivative_budget()
    c = r['gprime_L1_STRICT_upper']
    c2 = r['gprime_L2_squared_STRICT_upper']
    spectral_weight = (n+1)*(n+2)
    gamma_tail = (F() if gamma_modes is None else
                  authentic_positive_gamma_tail_norm(gamma_modes))
    return {
        'authority': 'PAPER_PROVED_WITH_REPLAYED_EXACT_SOURCE_ENCLOSURE',
        'source': passport, 'a': F(1, 2), 'mean_zero': True,
        'projection': 'orthogonal Legendre modes 1..N on (-1/2,1/2)',
        'degree': n, 'first_omitted_eigenvalue': spectral_weight,
        'gprime_L1_strict_upper': c,
        'gprime_L2_squared_strict_upper': c2,
        'operator_error_squared_strict_upper': c*c/spectral_weight,
        'hilbert_schmidt_error_squared_strict_upper': c2/(2*spectral_weight),
        'operator_error_rational_strict_upper': c/(n+1),
        'simple_operator_error_strict_upper': F(11, 40*(n+1)),
        'gamma_modes': gamma_modes,
        'positive_gamma_tail_operator_upper': gamma_tail,
        'compressed_GJ_total_error_strict_upper': c/(n+1)+gamma_tail,
        'requires_exact_compression_or_separate_matrix_entry_error': True,
        'inverse_or_zero_shift_error_certified': False,
        'original_S0_sign': 'OPEN', 'RH_PROVED': False,
    }


def polynomial_legendre_tail(coefficients, degree):
    """Exact independent control of the weighted Legendre tail inequality.

    Coefficients are in unnormalized P_j(2t), including j=0. Existing
    source polynomial algebra performs actual derivative integration.
    This is finite polynomial algebra, not an infinite theorem oracle.
    """
    n = _integer(degree, low=0, high=39)
    cs = tuple(_rational(x) for x in coefficients)
    if not cs or len(cs) > 41:
        raise CompactGalerkinError('one to 41 Legendre coefficients required')
    polynomial = (F(),)
    for j, c in enumerate(cs):
        polynomial = L.poly_add(polynomial, L.legendre_polynomial(j, F(1, 2)), c)
    derivative = L.poly_derivative(polynomial)
    derivative_square = L.poly_mul(derivative, derivative)
    weighted = L.poly_integral(L.poly_mul((F(1, 4), F(), -F(1)),
                                         derivative_square), -F(1, 2), F(1, 2))
    raw = L.poly_integral(derivative_square, -F(1, 2), F(1, 2))
    spectral = sum((F(j*(j+1), 2*j+1)*c*c for j, c in enumerate(cs)), F())
    tail = sum((c*c/F(2*j+1) for j, c in enumerate(cs) if j > n), F())
    bound = weighted/((n+1)*(n+2))
    if weighted != spectral or not tail <= bound <= raw/(4*(n+1)*(n+2)):
        raise ArithmeticError('exact weighted Legendre control failed')
    return {'authority': 'EXACT_FINITE_CHECK', 'tail_squared': tail,
            'weighted_derivative_squared': weighted, 'spectral_sum': spectral,
            'ordinary_derivative_squared': raw, 'tail_squared_upper': bound,
            'authentic_weil_source': False}


def diagonal_compression_control(degree, exponent=2):
    """Exact norm tails on l2: diag(j^-p); p=0 is noncompact identity."""
    n = _integer(degree)
    p = _integer(exponent, low=0, high=8)
    return {'source': 'SYNTHETIC_DIAGONAL_L2', 'degree': n, 'exponent': p,
            'operator_norm_error': F(1, (n+1)**p),
            'norm_I_minus_projection': F(1),
            'witness_index': n+1, 'compact_iff_exponent_positive': p > 0,
            'authority': 'EXACT_FINITE_CHECK_OF_PAPER_COUNTERMODEL',
            'authentic_weil_source': False}


def zero_shift_discontinuity(index, shift=F(1, 10)):
    """Fixed compact D=diag(j^-2), changing b_m=e_m/m -> 0.

    G_m -> diag(1/2,D) in norm, but R0(G_m)=1 and R0(limit)=0.
    Same D=K and uniform relative coercivity do not repair this without
    convergence of b in its relative source norm. This is not Suzuki.
    """
    m = _integer(index)
    lam = _rational(shift)
    if lam <= 0:
        raise CompactGalerkinError('positive shift required; no inverse at zero')
    return {
        'source': 'CHANGING_CROSS_SOURCE_FIXED_COMPACT_D_SYNTHETIC',
        'index': m, 'operator_norm_distance_to_limit': F(1, m),
        'active_high_eigenvalue': F(1, m*m), 'cross_coefficient': F(1, m),
        'relative_source_norm_squared': F(1),
        'response_zero_shift': F(1), 'limit_response_zero_shift': F(),
        'short': -F(1, 2), 'limit_short': F(1, 2),
        'negative_vector_low_high': (F(1), -F(m)),
        'negative_energy': -F(1, 2),
        'shift': lam, 'positive_shift_response': 1/(1+lam*m*m),
        'authentic_weil_source': False,
    }


def positive_shift_response_error(high_error, cross_error, cross_norm,
                                  approximant_cross_norm, shift):
    """Conditional resolvent perturbation budget for positive D,E.

    Inputs bound ||D-E||, ||b-c||, ||b||, ||c|| and lambda>0.
    Positivity/source identity are external hypotheses, not inferred here.
    """
    delta, epsilon, b, c, lam = map(_rational, (
        high_error, cross_error, cross_norm, approximant_cross_norm, shift))
    if min(delta, epsilon, b, c) < 0 or lam <= 0:
        raise CompactGalerkinError('nonnegative errors/norms and positive shift required')
    return {'conditional_response_error_upper': (b+c)*epsilon/lam+c*c*delta/(lam*lam),
            'hypotheses': ('D and E bounded positive on the same high carrier',
                           'the four input bounds hold for actual operators',
                           'lambda strictly positive'),
            'zero_shift_bound': None, 'authority': 'CONDITIONAL_RATIONAL_BOUND'}


def graph_failure_block(index):
    """One exact block in the fixed-source counterexample CG-07.

    D >= K>0; K^-1/2 D is Hilbert-Schmidt over all blocks. Both Galerkin
    energy convergence and failure of K-relative residual convergence are
    proved for the whole infinite family in the dossier.
    """
    j = _integer(index, high=128)
    s = F(1, 2**j)
    d = ((s**8, s**7/2), (s**7/2, s**6))
    k = s**8/2
    b = (s**5, F())
    u = (1/s**3, F())
    r = (F(), -s**4/2)
    return {'source': 'FIXED_SYNTHETIC_DIRECT_SUM', 'index': j, 's': s,
            'D': d, 'K_scalar': k, 'b': b, 'partial_Galerkin_u': u,
            'partial_residual': r,
            'det_D_minus_K': s**14*(1-s*s)/4,
            'D_minus_K_leading_minor': s**8/2,
            'block_response': 4*s*s/3,
            'partial_response': s*s,
            'block_relative_source_squared': 2*s*s,
            'partial_K_residual_squared': F(1, 2),
            'relative_map_HS_squared': 2*s**8+s**6+2*s**4,
            'exact_response_vector': (4/(3*s**3), -2/(3*s*s)),
            'authentic_weil_source': False}


def graph_failure_stage(index, complete_block=False):
    """Exact full infinite-tail formulas, certified by geometric sums CG-07.

    N=2j-1 (partial block) versus N=2j. Future source coefficients are
    included analytically: the residual is not a finite compressed residual.
    """
    block = graph_failure_block(index)
    if type(complete_block) is not bool:
        raise CompactGalerkinError('complete_block must be an actual bool')
    s2 = block['s']**2
    error = (4 if complete_block else 7)*s2/9
    residual = 2*s2/3 + (F() if complete_block else F(1, 2))
    return {'source': 'FIXED_SYNTHETIC_DIRECT_SUM', 'index': index,
            'observed_coordinates': 2*index-int(not complete_block),
            'complete_block': complete_block, 'R0': F(4, 9),
            'Galerkin_response': F(4, 9)-error,
            'true_D_relative_residual_squared': error,
            'full_K_relative_residual_squared': residual,
            'full_relative_source_squared': F(2, 3),
            'compact_relative_map_HS_squared': F(2, 255)+F(1, 63)+F(2, 15),
            'coercivity_kappa': F(1),
            'exact_response_in_l2': False,
            'low_A': F(1, 2), 'true_short': F(1, 18),
            'upper_short': F(1, 18)+error,
            'sufficient_lower': F(1, 18)+error-residual,
            'authentic_weil_source': False}


def clamped_polynomial_control(coefficients):
    """Exact polynomial instance of CG-08, C = inverse clamped biharmonic.

    Input is f=C u in powers of t on (0,1), with f=f'=0 at both ends.
    In this synthetic model b=C1, K=C², D=C(-d²)C, and kappa=1.
    Every such polynomial is in Ran C, with u=f''''. Full infinite
    statements and the all-trial bound are proved separately in CG-08.
    """
    f = tuple(_rational(x) for x in coefficients)
    if not f or len(f) > 33:
        raise CompactGalerkinError('nonempty polynomial, degree at most 32')
    df = L.poly_derivative(f)
    if any(L.poly_eval(p, x) for p in (f, df) for x in (F(), F(1))):
        raise CompactGalerkinError('clamped endpoints f=f\' =0 at 0 and 1 required')
    ddf = L.poly_derivative(df)
    def integral(p):
        return L.poly_integral(p, F(), F(1))
    c2 = integral(L.poly_mul(ddf, ddf))
    f2 = integral(L.poly_mul(f, f))
    df2 = integral(L.poly_mul(df, df))
    response = 2*integral(f)-df2
    residual = L.poly_add((F(1),), ddf)
    gram = integral(L.poly_mul(residual, residual))
    low = F(1, 6)-response-gram
    if not (gram == 1+c2 and f2 <= df2/6 and df2 <= c2/6
            and low <= -F(4, 5)):
        raise ArithmeticError('clamped exact controls violated')
    high_input = L.poly_derivative(L.poly_derivative(ddf))
    return {'source': 'SYNTHETIC_CLAMPED_BIHARMONIC',
            'f': f, 'high_u_equals_fourth_derivative': high_input,
            'mean_second_derivative': integral(ddf),
            'first_moment_second_derivative': integral(L.poly_mul((F(), F(1)), ddf)),
            'f_squared': f2, 'df_squared': df2, 'ddf_squared': c2,
            'L_U': response, 'K_relative_residual_squared': gram,
            'A': F(1, 6), 'R0': F(1, 12), 'true_S0': F(1, 12),
            'coercivity_kappa_used': F(1),
            'sufficient_lower': low, 'all_trial_lower_upper': -F(4, 5),
            'authentic_weil_source': False}


def gamma_residual_gram_upper(truncated_gram, trial_gram, gamma_modes, epsilon=F(1)):
    """Conditional whole-source derivative-Gram upper, reusing Gamma tail.

    If CJ is the EXACT/enclosed truncated derivative Gram and W is the
    Gram of trial columns v_i, the full Gram is <= (1+eps)CJ +
    (1+1/eps) eta_J² W. PSD data alone do not establish these identifications.
    """
    j = _integer(gamma_modes)
    eps = _rational(epsilon)
    if eps <= 0:
        raise CompactGalerkinError('positive epsilon required')
    cj = tuple(tuple(_rational(x) for x in row) for row in truncated_gram)
    w = tuple(tuple(_rational(x) for x in row) for row in trial_gram)
    n = len(cj)
    if not 1 <= n <= 4 or len(w) != n or any(len(row) != n for row in cj+w):
        raise CompactGalerkinError('matching square Gram matrices, rank 1..4 required')
    if not rational_psd(cj)[0] or not rational_psd(w)[0]:
        raise CompactGalerkinError('positive semidefinite Gram bounds required')
    eta = original_gamma_derivative_l1_tail(j)
    upper = tuple(tuple((1+eps)*cj[i][k]+(1+1/eps)*eta*eta*w[i][k]
                        for k in range(n)) for i in range(n))
    return {'authority': 'CONDITIONAL_EXACT_FINITE_BOUND',
            'gamma_modes': j, 'derivative_tail_L1_upper': eta,
            'epsilon': eps, 'upper': upper,
            'requires_independently_verified': (
                'same original signed source and same trial columns',
                'CJ bounds the whole-continuum projected derivative Gram for GJ',
                'W bounds the L2 Gram of those trial columns'),
            'source_identification_inferred_from_PSD': False,
            'original_S0_sign': 'OPEN', 'RH_PROVED': False}
