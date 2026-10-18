"""Infinite original real-Gamma boundary tower: exact rational proof receipts.

Continuum Carleman essential-norm and H01 results are derived in the
accompanying paper, not inferred from finite tests or a false positive Gram.
Never identifies a signed Weil / Suzuki S4 positivity theorem.
"""
from fractions import Fraction as F
from math import factorial, isqrt


class GammaTowerError(ValueError):
    pass


def integer(x, minimum=1):
    if type(x) is not int or x < minimum:
        raise GammaTowerError("integer source rung budget required")
    return x


def rational(x):
    if type(x) not in (F, int):
        raise GammaTowerError("exact int or Fraction only")
    return F(x)


def alpha(j):
    return F(4 * integer(j, 0) + 1, 2)


def finite_geometric(q, count):
    q, count = rational(q), integer(count, 0)
    if not 0 < q < 1:
        raise GammaTowerError("strict decay parameter required")
    direct = sum((q**j for j in range(count)), F(0))
    closed = (1-q**count)/(1-q)
    if direct != closed:
        raise ArithmeticError("direct/source geometric series disagree")
    return {"ratio":str(q),"count":count,"finite_sum":str(direct),
            "closed":str(closed),"exact_equal":True}


def gamma_spacing_coefficient(spacing):
    spacing = rational(spacing)
    if spacing <= 0:
        raise GammaTowerError("positive real-Gamma rung spacing required")
    return 1/spacing


def exp_negative_interval(x, pairs=12):
    """Outward exact alternating-series bracket for 0<=x<=1."""
    x, pairs = rational(x), integer(pairs)
    if not 0 <= x <= 1:
        raise GammaTowerError("Taylor source probe is scoped to [0,1]")
    hi = sum(((-x)**k/F(factorial(k)) for k in range(2*pairs+1)),F(0))
    lo = hi-x**(2*pairs+1)/F(factorial(2*pairs+1))
    if not 0 < lo <= hi <= 1:
        raise ArithmeticError("outward Taylor exp bounds incorrect")
    return lo,hi


def analytic_gamma_kernel_window(s, J):
    """Independent rational infinite geometric ratio versus finite rungs.

    Original exponents alpha_j=(4j+1)/2. Only small s with all Taylor
    arguments <=1 are accepted. No zero positions or fitted coefficients.
    """
    s, J = rational(s), integer(J)
    if s <= 0 or 2*s > 1 or alpha(J-1)*s > 1:
        raise GammaTowerError("source Taylor argument outside rigor window")
    nlo,nhi = exp_negative_interval(s/2)
    dlo,dhi = exp_negative_interval(2*s)
    inf_lo,inf_hi = nlo/(1-dlo),nhi/(1-dhi)
    finite = [exp_negative_interval(alpha(j)*s) for j in range(J)]
    flo = sum((v[0] for v in finite),F(0))
    fhi = sum((v[1] for v in finite),F(0))
    if not (inf_lo <= inf_hi and flo <= fhi):
        raise ArithmeticError("invalid Gamma source series bracket")
    return {"s":str(s),"J":J,
       "infinite_exact_series_lower":str(inf_lo),
       "infinite_exact_series_upper":str(inf_hi),
       "finite_original_rungs_lower":str(flo),
       "finite_original_rungs_upper":str(fhi),
       "tail_lower":str(inf_lo-fhi),"tail_upper":str(inf_hi-flo),
       "singular_coefficient":str(gamma_spacing_coefficient(2)),
       "RH_proved":False}


def dyadic_nonnorm_witness(cutoff):
    """Uniform exact lower for one actual Carleman corner's missing tail.

    f_delta=1_[delta,2delta]/sqrt(delta), delta=1/[32(J+1)].
    K_inf(s)>=1/(2s)-1/4 and finite K_J(s)<=J.
    On square with s<=4delta, <f,(K_inf-K_J)f> >=
    1/8 - delta*(J+1/4) >= 3/32.
    Center and edge widths >1/4 under authenticated log2 bounds.
    """
    J = integer(cutoff)
    delta = F(1,32*(J+1))
    lower = F(1,8)-delta*(J+F(1,4))
    if not 2*delta < F(1,4) or lower < F(3,32):
        raise ArithmeticError("dyadic source witness geometry fails")
    return {"gamma_prefix_count":J,"corner_interval_delta":str(delta),
            "finite_prefix_upper_on_normalized_packet":str(J*delta),
            "entire_tower_lower_on_packet":str(F(1,8)-delta/4),
            "tail_cross_block_lower":str(lower),
            "uniform_nonzero_lower":str(F(3,32)),
            "operator_norm_convergence_refuted":True,
            "RH_proved":False}


def sqrt_lower(x,digits=10**7):
    x = rational(x)
    if x <= 0 or type(digits) is not int or not 1 <= digits <= 10**9:
        raise GammaTowerError("positive rational with safe denominator budget")
    k = isqrt((x.numerator*digits*digits)//x.denominator)
    lo = F(k,digits)
    if not (lo > 0 and lo*lo <= x and (lo+F(1,digits))**2 > x):
        raise ArithmeticError("floor sqrt certificate invalid")
    return lo


def h01_tail_bound(cutoff):
    """Original a=1/2, 5/8<log2<3/4: rigorous H01xH01 tail upper.

    t=alpha_J. Four singular corners contribute <=
    (2sqrt(pi)/3)/t^1.5 + (2sqrt(pi))/t^2.5.
    Four smooth same-edge pieces contribute
    <=4ell^2 exp(-t*d)(1+1/(2d)); ell<3/8, d>1/4.
    Bound sqrt(pi)<2, exp(-t/4)<=8!*4^8/t^8,
    and use an exact rational floor for sqrt(t).
    """
    J = integer(cutoff)
    t = alpha(J)
    root = sqrt_lower(t)
    corners = F(4,3)/(t*root)+F(4)/(t*t*root)
    edges = F(27,16)*factorial(8)*4**8/t**8
    total = corners+edges
    if total <= 0:
        raise ArithmeticError("invalid source H01 tail budget")
    return {"gamma_prefix_count":J,"gamma_tail_first_alpha":str(t),
            "sqrt_alpha_lower":str(root),
            "four_corner_H01_budget":str(corners),
            "smooth_edge_H01_budget":str(edges),
            "two_sided_H01_commutator_error_upper":str(total),
            "qualitative_convergence":"O(J^-3/2) on H01 cross H01",
            "requires_original_endpoint_zero_domain":True,
            "full_L2_operator_norm_convergence":False,
            "source_S4_positive_proved":False,"RH_proved":False}


def original_source_infinite_gamma_contract():
    """Authenticate original source, true prime2 and one real Gamma."""
    from . import source_weil_hierarchy as src
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .finite_gamma_fucc_fredholm import gamma_scalar_prefix
    sha = verify_original_suzuki_source()["source_git_blob"]
    if sha != "0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise GammaTowerError("original signed Suzuki source blob changed")
    if (src.authenticated_prime_wavefront(F(1,2))!=((2,2),)
            or src.real_prime_power(6) is not None):
        raise GammaTowerError("not genuine first-prime source")
    b = src.log2_iv()
    if not F(5,8)<b.lo<=b.hi<F(3,4):
        raise GammaTowerError("original prime shift outside two-edge geometry")
    for J in (1,2,8,64):
        if gamma_scalar_prefix(J)!=sum((F(4,4*j+1) for j in range(J)),F(0)):
            raise GammaTowerError("one real Gamma scalar ladder mismatch")
    return {"source_git_blob":sha,"true_prime_power":((2,2),),
            "true_log2_interval":(str(b.lo),str(b.hi)),
            "true_alpha_j":"(4j+1)/2",
            "infinite_carleman_boundary":"PAPER_PROVED_NOT_ZERO_INPUT",
            "essential_norm_pi_over_two":"PAPER_PROVED_WITH_MELLIN",
            "source_S4_positive_proved":False,"RH_proved":False}
