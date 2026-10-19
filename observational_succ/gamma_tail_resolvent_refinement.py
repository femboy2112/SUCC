"""Authentic Gamma-tail resolvent expansion with paid endpoint layers.

The leading tail Laplacian is retained in the true continuum action.  The
remainder is bounded on H^4(I) intersect H^2_0(I), NOT on H^4_0 by fiat.
Every certificate is exact rational; a negative Schur lower is AMBIGUOUS.
The original operator, contact, two poles, prime2 and half-density remain
those read from the frozen original_continuum_residual source adapter.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

from . import clamped_k_residual_bridge as B
from . import original_continuum_residual as R

SOURCE_SHA = R.SOURCE_SHA


class TailResolventError(ValueError):
    pass


def _integer(n, label, lower=1, upper=100000):
    if type(n) is not int or not lower <= n <= upper:
        raise TailResolventError(label)
    return n


def _polynomial(h):
    if not h or any(type(c) not in (int, F) for c in h):
        raise TailResolventError("exact nonempty polynomial required")
    return B.trim(tuple(F(c) for c in h))


def _clamped(h):
    h = _polynomial(h)
    if any(B.value(p, e) for p in (h, B.derivative(h))
           for e in (-R.A, R.A)):
        raise TailResolventError("genuine zero extension H2 traces required")
    return h


def _round_down(x, grid):
    return F(x.numerator * grid // x.denominator, grid)


@lru_cache(maxsize=128)
def tail_power_interval(J, power, count=256, grid=10**24):
    """Enclose sum_(j>=J) (4j+1)^(-power), with rational integral tail.

    Fixed-grid outward rounding avoids an enormous common denominator;
    every term's rounding is paid.  No floating evaluation is involved.
    """
    _integer(J, "positive original Gamma rung cutoff")
    _integer(power, "integer summable tail power", 2, 12)
    _integer(count, "finite rational tail budget", 1, 4096)
    _integer(grid, "positive rational enclosure grid", 1, 10**60)
    low = F(0)
    high = F(0)
    for j in range(J, J + count):
        v = F(1, (4*j+1)**power)
        z = _round_down(v, grid)
        low += z
        high += z if z == v else z + F(1, grid)
    d = 4*(J+count)+1
    integral = F(1, 4*(power-1)*d**(power-1))
    return (low + integral, high + integral + F(1, d**power))


def finite_power_sum(J, K, power):
    _integer(J, "positive original Gamma rung cutoff")
    _integer(K, "later original Gamma rung cutoff", J+1)
    _integer(power, "positive integer power", 2, 12)
    return sum((F(1, (4*j+1)**power) for j in range(J, K)), F(0))


def _negative_exp_upper(x, terms=48):
    """e^-x <= 1/sum_(k=0)^terms x^k/k!, x>=0."""
    if type(x) not in (F, int) or x < 0:
        raise TailResolventError("nonnegative exact exponential argument")
    return 1 / sum((F(x)**k / factorial(k) for k in range(terms+1)), F(0))


def gamma_tail_resolvent_bound(h, J, count=256):
    """Gamma_tail h = -a_J h'' + error, with authentic endpoint costs.

    a_J=16 sum d^-3.  Twice integrating the original OU resolvent gives
      Gamma_j h = -16/d^3 h'' -16/d^4 E_(d/2) h''''
        + exp[-d(x+a)/2]*(8/d^3 h''(-a)-16/d^4 h'''(-a))
        + exp[-d(a-x)/2]*(8/d^3 h''(a)+16/d^4 h'''(a)).
    Endpoint pairs are bounded jointly, retaining destructive parity signs.
    The result only needs h,h'=0 at the endpoints, not h'',h'''=0.
    """
    h = _clamped(h)
    _integer(J, "positive authentic Gamma tail cutoff")
    h2 = B.derivative(B.derivative(h))
    h3 = B.derivative(h2)
    h4 = B.derivative(h3)
    intervals = {p: tail_power_interval(J, p, count) for p in (3, 4, 5)}
    s3, s4, s5 = (intervals[p][1] for p in (3, 4, 5))
    alo, ahi = (16*z for z in intervals[3])
    amid, arad = (alo+ahi)/2, (ahi-alo)/2
    d = 4*J+1
    # For d'>=d>=5, d' exp(-d'/2) decreases.  This is a common
    # coefficient bound for the overlap of the two endpoint layers.
    overlap = d * _negative_exp_upper(F(d, 2))

    def endpoint_pair_norm(a, b):
        return B.sqrt_up(a*a+b*b+2*max(a*b, F(0))*overlap)

    b2left, b2right = (B.value(h2, x) for x in (-R.A, R.A))
    b3left, b3right = (B.value(h3, x) for x in (-R.A, R.A))
    # Cauchy over the authentic d_j, not independent fitted rungs:
    # sum d^-7/2 <= sqrt(S3*S4), sum d^-9/2 <= sqrt(S4*S5).
    edge2 = 8*endpoint_pair_norm(b2left, b2right)*B.sqrt_up(s3*s4)
    edge3 = 16*endpoint_pair_norm(-b3left, b3right)*B.sqrt_up(s4*s5)
    bulk = 64*s5*B.sqrt_up(R.norm_squared(h4))
    coefficient = arad*B.sqrt_up(R.norm_squared(h2))
    error = edge2+edge3+bulk+coefficient
    old = R.authentic_Gamma_tail_action_dual(h, J)["selected"]
    return {
        "J": J, "a_interval": (alo, ahi), "a_midpoint": amid,
        "coefficient_error_upper": coefficient,
        "endpoint_second_derivative_error_upper": edge2,
        "endpoint_third_derivative_error_upper": edge3,
        "interior_fourth_derivative_error_upper": bulk,
        "corrected_action_error_upper": error,
        "uncorrected_parent_action_error_upper": old,
        "retained_tail_action": B.scale(h2, -amid),
        "tail_energy_a_lower": alo, "tail_energy_b_upper": 64*s5,
        "zero_extension_H2": True,
        "requires_zero_second_or_third_endpoint_traces": False,
        "RH_proved": False,
    }


def corrected_source_action(h, J=8, M=80, P=18, parameters=None):
    h = _clamped(h)
    authenticated = R.source_parameters()
    if parameters is not None and parameters != authenticated:
        raise TailResolventError("mutated original Gamma/contact/poles/prime source parameters")
    finite = R.exact_piecewise_primitive_action(h, J, M, P, authenticated)
    tail = gamma_tail_resolvent_bound(h, J)
    pieces = tuple((l, r, B.add(p, tail["retained_tail_action"]))
                   for l, r, p in finite["pieces"])
    return {
        "pieces": pieces,
        "finite_source": finite,
        "tail": tail,
        "full_source_action_error_upper": (
            finite["finite_source_action_error_upper"]
            + tail["corrected_action_error_upper"]),
        "frozen_source_SHA": finite["frozen_source_SHA"],
    }


def fit_corrected_high_coefficients(J=8, M=80, P=18):
    """Select finite rational trials from corrected continuum residual only."""
    params = R.source_parameters()
    candidates = {name: corrected_source_action(data["poly"], J, M, P, params)
                  for name, data in B.CLAMPED.items()}
    result = {}
    for i in range(1, 5):
        h = R.high_boundary_match(i)["h"]
        p = corrected_source_action(h, J, M, P, params)["pieces"]
        q = candidates[R.clamped_name(i)]["pieces"]
        result[i] = R.safe_ratio_round(R.projected_piece_gram(p, q),
                                      R.projected_piece_gram(q, q))
    return result


def _matrix_psd_2(matrix):
    return (matrix[0][0] >= 0 and matrix[1][1] >= 0
            and matrix[0][0]*matrix[1][1] >= matrix[0][1]**2)


def source_tail_resolvent_schur_trial(J=8, M=80, P=18,
                                     fit="corrected", eta=F(1,4)):
    """Original all-four-low source Schur lower with the paid tail retained.

    Same source kappa hypothesis as PR177.  The all-high coercivity itself
    is inherited, not established by these finite arithmetic calculations.
    """
    _integer(J, "bounded parent source budget", 1, 24)
    eta = R.rat(eta)
    if eta <= 0 or fit not in ("corrected", "parent", "none"):
        raise TailResolventError("positive Young parameter and named fit")
    params = R.source_parameters()
    if params["sha"] != SOURCE_SHA:
        raise TailResolventError("frozen original source mismatch")
    if fit == "corrected":
        fitted = fit_corrected_high_coefficients(J, M, P)
    elif fit == "parent":
        fitted = R.fit_high_coefficients(J, M, P)
    else:
        fitted = {i: F(0) for i in range(1,5)}
    inputs = {}
    for i in range(1, 5):
        trial = R.high_boundary_match(i, fitted[i])
        packet = corrected_source_action(trial["h"], J, M, P, params)
        inputs[i] = (trial, packet)
    entry_cache = {}
    blocks = {}
    for parity, indices, kappa in (
            ("odd_derivative", (1,3), F(63,500)),
            ("even_derivative", (2,4), F(153,500))):
        pairs = [[R._actual_signed_interval(inputs[i][0]["derivative_coeff"],
                  inputs[j][0]["derivative_coeff"], J, entry_cache)
                  for j in indices] for i in indices]
        mid = [[sum(pairs[a][b])/2 for b in range(2)] for a in range(2)]
        rad = [[(pairs[a][b][1]-pairs[a][b][0])/2
                for b in range(2)] for a in range(2)]
        gram = [[R.projected_piece_gram(inputs[i][1]["pieces"],
                                       inputs[j][1]["pieces"])
                 for j in indices] for i in indices]
        # Fourier inequality x/(1+x)>=x-x*x gives an entire Loewner
        # lower, with independently enclosed authentic series constants.
        a = inputs[indices[0]][1]["tail"]["tail_energy_a_lower"]
        b = inputs[indices[0]][1]["tail"]["tail_energy_b_upper"]
        d1 = [B.derivative(inputs[i][0]["h"]) for i in indices]
        d2 = [B.derivative(h) for h in d1]
        energy = [[a*B.integral_product(d1[i], d1[j])
                   -b*B.integral_product(d2[i], d2[j])
                   for j in range(2)] for i in range(2)]
        used = energy if _matrix_psd_2(energy) else [[F(0)]*2 for _ in range(2)]
        errors = [inputs[i][1]["full_source_action_error_upper"] for i in indices]
        epssq = sum((e*e for e in errors), F(0))
        lower = [[mid[i][j]+used[i][j]-(sum(rad[i]) if i==j else F(0))
                  -((1+eta)*gram[i][j]+((1+1/eta)*epssq if i==j else F(0)))/kappa
                  for j in range(2)] for i in range(2)]
        if lower[0][1] != lower[1][0]:
            raise ArithmeticError("asymmetric source Schur lower")
        blocks[parity] = {
            "indices": indices, "source_kappa": kappa,
            "fitted_high_coefficients": tuple(fitted[i] for i in indices),
            "genuine_signed_qJ_intervals": pairs,
            "retained_tail_projected_action_Gram": gram,
            "refined_true_Gamma_tail_energy_lower": energy,
            "entire_tail_energy_lower_is_PSD": _matrix_psd_2(energy),
            "full_source_action_error_each": errors,
            "tail_remainder_each": [inputs[i][1]["tail"] for i in indices],
            "genuine_source_2x2_Schur_Loewner_lower": lower,
            "source_Schur_lower_PSD_certified": _matrix_psd_2(lower),
        }
    passed = all(b["source_Schur_lower_PSD_certified"] for b in blocks.values())
    return {
        "frozen_source_git_blob": SOURCE_SHA, "source_J": J,
        "finite_Gamma_Taylor_M": M, "polar_Taylor_P": P,
        "fit": fit, "eta": eta,
        "authentic_first_prime_wavefront": ((2,2),),
        "one_real_Gamma_contact_two_completed_poles": True,
        "four_original_parity_Schur_blocks": blocks,
        "all_four_source_S4_sign_certified": passed,
        "verdict": "CERTIFIED_FIRST_WINDOW_ONLY" if passed else "AMBIGUOUS",
        "RH_proved": False,
    }


def exact_ou_resolvent_polynomial(h, alpha):
    """Exact polynomial + two exponentials for the genuine finite OU action.

    Returned coefficients mean E_alpha h(x)=p(x)+left*exp[-alpha(x+a)]
    +right*exp[-alpha(a-x)]. This separate endpoint/ODE decomposition is
    used only for algebraic calibration here, not as a replacement source.
    """
    h = _polynomial(h)
    alpha = R.rat(alpha)
    if alpha <= 0:
        raise TailResolventError("positive original OU exponent")
    p = (F(0),)
    derivative = h
    k = 0
    while derivative != (F(0),):
        p = B.add(p, B.scale(derivative, 2/alpha**(2*k+1)))
        derivative = B.derivative(B.derivative(derivative))
        k += 1
    dp = B.derivative(p)
    left = (B.value(dp,-R.A)-alpha*B.value(p,-R.A))/(2*alpha)
    right = -(B.value(dp,R.A)+alpha*B.value(p,R.A))/(2*alpha)
    return {"polynomial": p, "left": left, "right": right, "alpha": alpha}


def _derivative_legendre_coefficients(h):
    derivative = B.derivative(h)
    result = tuple((k, (2*k+1)*B.integral_product(derivative,B.legendre(k)))
                   for k in range(1, len(derivative)))
    result = tuple((k,c) for k,c in result if c)
    reconstructed = (F(0),)
    for k,c in result:
        reconstructed = B.add(reconstructed, B.scale(B.legendre(k),c))
    if reconstructed != derivative:
        raise TailResolventError("primitive has unsupported nonzero mean derivative")
    return result


def independent_original_source_holdouts():
    """Unfitted H4 polynomial and J13->J23 authentic Gamma shell holdout.

    The archived Legendre/exponential source oracle is a different action
    decomposition, but shares the frozen mathematical source. This is
    method diversity, not independent provenance for the source itself.
    """
    h = (F(1),)
    for _ in range(4):
        h = B.mul(h,(F(1),F(0),F(-4)))
    coefficients = _derivative_legendre_coefficients(h)
    # Cache entries depend on J; never reuse the pair-only parent cache
    # across Gamma cutoffs. Each invocation receives its own source cache.
    original = {J:R._actual_signed_interval(coefficients, coefficients,J,{})
                for J in (7,13,23)}
    action = corrected_source_action(h,7,72)
    finite = action["finite_source"]
    full_nominal = sum((R.definite(B.mul(h,p),l,r)
                        for l,r,p in finite["pieces"]), F(0))
    full_error = B.sqrt_up(R.norm_squared(h))*finite["finite_source_action_error_upper"]
    full_intersects = (original[7][0] <= full_nominal+full_error
                       and full_nominal-full_error <= original[7][1])
    shell = (original[23][0]-original[13][1],
             original[23][1]-original[13][0])
    nominal = 16*finite_power_sum(13,23,3)*R.derivative_norm_squared(h)
    bound = gamma_tail_resolvent_bound(h,13)
    # We use the infinite-tail remainder bound for this finite sub-tail;
    # its positive coefficient majorants dominate every omitted shell term.
    error = B.sqrt_up(R.norm_squared(h))*(
        bound["endpoint_second_derivative_error_upper"]
        +bound["endpoint_third_derivative_error_upper"]
        +bound["interior_fourth_derivative_error_upper"])
    shell_intersects = shell[0] <= nominal+error and nominal-error <= shell[1]
    omitted_disjoint = shell[0] > error or shell[1] < -error
    wrong_sign_disjoint = shell[0] > -nominal+error or shell[1] < -nominal-error
    if not (full_intersects and shell_intersects and omitted_disjoint and wrong_sign_disjoint):
        raise ArithmeticError("original source held-out resolvent calibration failed")
    return {
        "frozen_source_git_blob": SOURCE_SHA,
        "unfitted_primitive": h,
        "unfitted_original_derivative_legendre_coefficients": coefficients,
        "full_signed_J7_source_interval": original[7],
        "full_signed_J7_action_pair": full_nominal,
        "full_signed_J7_action_error": full_error,
        "full_signed_channels_intersect": full_intersects,
        "heldout_Gamma_shell": (13,23),
        "original_Gamma_shell_pair_interval": shell,
        "leading_resolvent_pair": nominal,
        "rigorous_remainder_pair_upper": error,
        "source_shell_intersects": shell_intersects,
        "omitted_leading_Laplacian_mutant_disjoint": omitted_disjoint,
        "reversed_leading_sign_mutant_disjoint": wrong_sign_disjoint,
        "RH_proved": False,
    }
