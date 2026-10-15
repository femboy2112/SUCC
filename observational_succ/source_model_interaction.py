"""Source-indexed finite-prime/real-place theta gluing and analytic error guards.

Only finite arithmetic and rational enclosures are computed by this module.
Global Poisson summation, Mellin continuation and Gamma pole properties are
CLASSICAL ANALYTIC imports proved/derived in the accompanying theorem dossier.
Nothing here reads nontrivial zeta zeros or proves Weil positivity / RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, isqrt


class SourceInteractionError(ValueError):
    pass


def _nat(n: int, low: int = 0, high: int = 100000) -> int:
    if type(n) is not int or not low <= n <= high:
        raise SourceInteractionError(f"integer must be in [{low}, {high}]")
    return n


def _rational(x) -> Q:
    if type(x) not in (int, Q):
        raise SourceInteractionError("exact integer or Fraction required")
    return Q(x)


def _prime(p: int) -> int:
    _nat(p, 2, 10**12)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise SourceInteractionError("primitive Euler place must be genuinely prime")
    return p


def prime_set(primes) -> tuple[int, ...]:
    if not isinstance(primes, (tuple, list)) or len(primes) > 12:
        raise SourceInteractionError("bounded ordered prime-list required")
    out = tuple(_prime(x) for x in primes)
    if out != tuple(sorted(set(out))):
        raise SourceInteractionError("use strictly increasing, unique primes")
    return out


def factor(n: int) -> dict[int, int]:
    _nat(n, 1, 10**12)
    fs: dict[int,int] = {}
    k = n
    d = 2
    while d * d <= k:
        while k % d == 0:
            fs[d] = fs.get(d, 0) + 1
            k //= d
        d += 1
    if k > 1:
        fs[k] = fs.get(k, 0) + 1
    return fs


def padic_v(q: int | Q, p: int) -> int:
    _prime(p)
    q = _rational(q)
    if not q:
        raise SourceInteractionError("zero does not define a multiplicative place")
    return factor(abs(q.numerator)).get(p, 0) - factor(q.denominator).get(p, 0)


def global_product_formula(q: int | Q) -> dict:
    q = _rational(q)
    if not q:
        raise SourceInteractionError("nonzero diagonal rational required")
    places = sorted(set(factor(abs(q.numerator))) | set(factor(q.denominator)))
    local = {p: Q(p) ** (-padic_v(q, p)) for p in places}
    finite = Q(1)
    for value in local.values():
        finite *= value
    real = abs(q)
    if real * finite != 1:
        raise ArithmeticError("normalized rational product formula contradicted")
    return {"q":str(q), "arch_norm":str(real),
            "finite_local_norms":{str(p):str(local[p]) for p in places},
            "product_one":True, "no_infinite_event_performed":True}


def diagonal_source_filter(q: int | Q, visible_primes=()) -> dict:
    """Finite p-observers see q in Z_p; all finite places see Z diagonal."""
    q = _rational(q)
    primes = prime_set(visible_primes)
    if not q:
        return {"q":"0", "passed_visible":True,"all_places_integral":True,
                "unseen_denominator_places":[], "ghost_possible":False}
    bad = set(factor(q.denominator))
    missing = sorted(bad - set(primes))
    return {"q":str(q),"passed_visible":not bool(bad & set(primes)),
            "all_places_integral":not bool(bad),"unseen_denominator_places":missing,
            "ghost_possible":bool(missing) and not bool(bad & set(primes))}


def unobserved_denominator_witness(visible_primes=()) -> dict:
    primes = prime_set(visible_primes)
    p = 2
    while p in primes or any(p % d == 0 for d in range(2,isqrt(p)+1)):
        p += 1
    out = diagonal_source_filter(Q(1,p),primes)
    if not out["ghost_possible"]:
        raise ArithmeticError("finite-place alias impossible to construct")
    return {"checked_primes":list(primes),"source":str(Q(1,p)),
            "hidden_prime":p,"legal_visible_integrality":True,
            "illegal_global_integrality":True}


def local_euler_shell(p: int, s: int, depth: int) -> dict:
    p = _prime(p)
    s = _nat(s,1,12)
    depth = _nat(depth,0,100)
    t = Q(1,p**s)
    prefix=sum((t**k for k in range(depth+1)), Q())
    limit=1/(1-t)
    tail=t**(depth+1)/(1-t)
    assert prefix+tail==limit
    return {"prime":p,"s":s,"depth":depth,"prefix":str(prefix),
            "tail":str(tail),"limit":str(limit),
            "local_multiplicative_haar_Zp_units_normalized":True}


def finite_euler_model(primes, s: int) -> dict:
    primes = prime_set(primes)
    s = _nat(s,1,12)
    product=Q(1)
    for p in primes:
        product *= Q(p**s, p**s-1)
    h=sum((Q(1,n) for n in range(1,max(primes,default=1)+1)),Q())
    # If 1..P is covered by all primes <=P, its Dirichlet prefix embeds.
    complete_up_to_P = bool(primes) and primes==tuple(
        n for n in range(2,primes[-1]+1) if all(n%d for d in range(2,isqrt(n)+1)))
    if s==1 and complete_up_to_P and product<h:
        raise ArithmeticError("finite Euler dominates its positive integer prefix")
    return {"primes":list(primes),"sigma":s,"local_product":str(product),
            "harmonic_lower_at_sigma_one":str(h) if complete_up_to_P else None,
            "valid_Euler_convergence_for_sigma_gt_one_only":True}


def e3_gt_20() -> bool:
    """Finite rational Taylor receipt for the bound exp(-3)<1/20."""
    return sum((Q(3**k,factorial(k)) for k in range(9)),Q())>20


def power_geometric_upper(r: int, terms: int | None = None) -> Q:
    """Exact envelope for sum_(m>=1) m^r/20^m with geometric tail."""
    r=_nat(r,0,12)
    M= max(32,2*r+8) if terms is None else _nat(terms,2,200)
    ratio=Q(1,20)*Q(M+2,M+1)**r
    if ratio>=1:
        raise SourceInteractionError("finite tail ratio not contractive")
    prefix=sum((Q(m**r,20**m) for m in range(1,M+1)),Q())
    tail=Q((M+1)**r,20**(M+1))/(1-ratio)
    return prefix+tail


def smooth_prime_theta_obstruction(primes, dyadic_depth: int) -> dict:
    """Rigorous finite-P non-modularity on t=4^-h; all bounds rational.

    Theta_P(t) = 1 + 2 sum_{n P-smooth} exp(-pi n^2 t).
    The normalized modular defect at t=4^-h tends to -1 for fixed P.
    """
    primes=prime_set(primes)
    h=_nat(dyadic_depth,1,200)
    r=len(primes)
    if not e3_gt_20():
        raise ArithmeticError("finite exponential bound failed")
    positive_count=(h+1)**r
    smooth_upper=Q(1)+2*(positive_count+(h+2)**r*power_geometric_upper(r))
    normalized_upper=smooth_upper/Q(2**h)
    # 2^-h(Theta_P(4^-h) - 2^h Theta_P(4^h)) <= upper - 1.
    return {"prime_set":list(primes),"dyadic_depth":h,
            "theta_P_near_zero_upper":str(smooth_upper),
            "normalized_theta_upper":str(normalized_upper),
            "normalized_modular_defect_upper":str(normalized_upper-1),
            "strict_nonmodularity_proved_at_depth":normalized_upper<1,
            "global_modular_identity_from_finite_P":False,
            "no_zero_locations_read":True}


def completed_function_mutant(s: int | Q) -> dict:
    """Functional eq + pole residues do not authenticate Euler source."""
    s=_rational(s)
    c=1+10*s*(s-1)
    reflection=1+10*(1-s)*(-s)
    if c!=reflection:
        raise ArithmeticError("symmetric ghost normalization mismatch")
    return {"s":str(s), "multiplier":str(c),"symmetric":True,
            "preserves_xi_at_0_and_1":True,
            "source_identical_on_Re_gt_one":c==1,
            "not_a_source_Weil_form":True}


def wrong_conductor_theta_scale(m: int) -> dict:
    """Selecting mZ from all finite p-adic gate changes Fourier Haar factor."""
    m=_nat(m,2,1000)
    return {"integer_source":"mZ", "m":m,"real_theta":"theta(m^2*t)",
            "Fourier_dual":"theta(1/(m^2*t))/(m*sqrt(t))",
            "naive_selfdual_theta_conductor":False,
            "composite_not_Euler_prime": len(factor(m))!=1 or list(factor(m).values())[0]!=1}


def upper_exp_neg(x: Q, steps: int = 128) -> Q:
    """exp(-x) <= (steps/(steps+x))^steps by exp(y)>=1+y."""
    x=_rational(x)
    steps=_nat(steps,1,1000)
    if x<0: raise SourceInteractionError("positive exponential tail argument required")
    return (Q(steps)/(steps+x))**steps


def _ceil(q:Q)->int:
    return -((-q.numerator)//q.denominator)


def exponential_moment_tail(lam:Q, start: int, degree:int, steps:int=128)->Q:
    """Rational upper bound on int_start^inf t^degree exp(-lam*t)dt."""
    lam=_rational(lam)
    start=_nat(start,1,1000)
    degree=_nat(degree,0,48)
    if lam<=0: raise SourceInteractionError("positive exponential rate required")
    poly=sum((Q(factorial(degree),factorial(degree-j))*Q(start)**(degree-j)/lam**(j+1)
              for j in range(degree+1)),Q())
    return upper_exp_neg(lam*start,steps)*poly


def analytic_theta_tail(sigma_min:int|Q,sigma_max:int|Q,
                        modes:int,endpoint:int,derivative:int=0,steps:int=128)->dict:
    """Uniform in ALL imaginary ordinates on declared vertical strip.

    The finite integrand is theta psi_N over t in [1,endpoint].
    The bound covers missing n>N and missing t>endpoint, not numerical quadrature.
    """
    lo,hi=_rational(sigma_min),_rational(sigma_max)
    if lo>hi or lo<-40 or hi>40:
        raise SourceInteractionError("bounded ordered real strip needed")
    N=_nat(modes,1,64)
    T=_nat(endpoint,1,1000)
    order=_nat(derivative,0,2)
    B=max(0,_ceil(hi/2-1),_ceil((1-lo)/2-1))
    m=B+order
    # theta psi_N missing n>N: at t>=1 at most 2 exp(-3(N+1)^2 t).
    # theta full t-tail: at most 2 exp(-3t).
    bound=Q(4,2**order)*(
        exponential_moment_tail(Q(3*(N+1)**2),1,m,steps)+
        exponential_moment_tail(Q(3),T,m,steps))
    return {"sigma_min":str(lo),"sigma_max":str(hi),
            "modes":N,"integration_endpoint":T,"derivative_order":order,
            "power_envelope":B,"rational_upper":str(bound),
            "uniform_in_imaginary_direction":True,
            "requires_certified_finite_integral_for_full_numeric_enclosure":True,
            "zero_locations_read":False}


def xi_tail_envelopes(sigma_min:int|Q,sigma_max:int|Q,
                      abs_s_max:int|Q,modes:int,endpoint:int,steps:int=128)->dict:
    R=_rational(abs_s_max)
    lo,hi=_rational(sigma_min),_rational(sigma_max)
    if R<0 or max(abs(lo),abs(hi))>R:
        raise SourceInteractionError("radius must cover supplied strip real coordinates")
    e=[Q(analytic_theta_tail(lo,hi,modes,endpoint,k,steps)["rational_upper"]) for k in range(3)]
    c=R*(R+1)/2
    return {"xi_error_upper":str(c*e[0]),
            "xi_prime_error_upper":str((R+Q(1,2))*e[0]+c*e[1]),
            "xi_second_error_upper":str(e[0]+2*(R+Q(1,2))*e[1]+c*e[2]),
            "theta_integral_derivative_errors":[str(v) for v in e],
            "applies_where_abs_s_le":str(R),
            "not_a_numerical_quadrature_certificate":True}


def real_strip_nonvanishing() -> dict:
    """Exact all-interval proof: xi(s)>59/120 for real s in [0,1]."""
    assert e3_gt_20()
    # psi(t) <= 2 exp(-3t), and the two powers <=1 for real 0<=s<=1.
    integral_upper=Q(1,15)
    xi_lower=Q(1,2)-Q(1,8)*integral_upper
    assert xi_lower==Q(59,120)
    return {"real_s_interval":"[0,1]", "xi_strict_lower_bound":str(xi_lower),
            "zeta_negative_on_open_interval":True,
            "uses_only_Poisson_theta_global_source":True,
            "not_RH_or_vertical_strip_nonvanishing":True}


def trivial_zero_certificate(index:int)->dict:
    index=_nat(index,1,10000)
    s=-2*index
    return {"argument":s,"zeta_zero_simple":True,
            "reason":"xi(s)>1/2 for real s<0; reciprocal Gamma(s/2) has a simple zero at negative integer",
            "zeta_0":"-1/2", "zeta_pole_at_1_residue":"1",
            "nontrivial_zeros_unknown":True}



def contact_constant_bridge()->dict:
    """Classical analytic consequence of theta/Poisson and digamma reflection.

    xi'(1/2)=0, xi(1/2)>0 and
    2 zeta'(1/2)/zeta(1/2) = gamma+pi/2+3 log2+log pi.
    No oracle for nontrivial zeros; this is a symbolic theorem receipt.
    """
    return {"parameter":"s=1/2", "xi_derivative_at_midpoint":"0",
            "xi_nonzero":True,"zeta_logarithmic_derivative_twice":
            "EulerGamma+pi/2+3*log(2)+log(pi)",
            "equal_to_authentic_Suzuki_Gamma_contact_C":True,
            "from_functional_equation_plus_Gamma_logarithmic_derivative":True,
            "classical_identity_not_new_RH_progress":True}


def completed_prime_current_source_rule()->dict:
    """Meromorphic all-s continuation of the original Euler prime current.

    On Re s>1, -zeta'/zeta = sum_n Lambda(n)n^(-s).
    Elsewhere the same source's meromorphic continuation is
    -xi'/xi+1/s+1/(s-1)+(psi(s/2)-log pi)/2,
    on points where the terms are separately defined. No primes are summed
    outside their original convergence domain and no unknown zero is queried.
    """
    return {"Euler_halfplane":"Re(s)>1", 
            "model_interaction_meromorphic_expression":
            "-xi_prime/xi + 1/s + 1/(s-1) + (digamma(s/2)-log(pi))/2",
            "meromorphic_identity_by_overlap":True,
            "cannot_evaluate_at_unknown_poles_without_guard":True,
            "not_a_convergent_prime_sum_outside_Euler_halfplane":True,
            "no_nontrivial_zero_inputs":True}


def derivative_of_trivial_zero(index:int)->dict:
    """Functional-equation value outside Euler halfplane, symbolically exact.

    zeta'(-2m)=(-1)^m (2m)!/[2 (2pi)^(2m)] zeta(2m+1).
    """
    m=_nat(index,1,1000)
    rational_coeff=Q((-1)**m*factorial(2*m), 2*4**m)
    return {"m":m,"argument":-2*m,
            "rational_coefficient":str(rational_coeff),
            "formula":f"zeta_prime({-2*m})={rational_coeff}/pi^{2*m}*zeta({2*m+1})",
            "absolute_sign":"negative" if m%2 else "positive",
            "classical_functional_equation_identity":True,
            "nontrivial_zero_inputs":False}


def interaction_receipt()->dict:
    return {"source_diagonal_product_formula":global_product_formula(Q(-84,125)),
            "finite_place_invisible_ghost":unobserved_denominator_witness((2,3,5)),
            "local_p2_shell":local_euler_shell(2,2,6),
            "finite_P_modular_obstruction":smooth_prime_theta_obstruction((2,3,5),26),
            "conductor_mutation":wrong_conductor_theta_scale(2),
            "theta_tail_vertical_strip":analytic_theta_tail(-2,3,4,16),
            "theta_derivative_tail":analytic_theta_tail(-2,3,4,16,1),
            "xi_tail":xi_tail_envelopes(-2,3,8,4,16),
            "critical_real_segment":real_strip_nonvanishing(),
            "Suzuki_contact_identity":contact_constant_bridge(),
            "continued_prime_current":completed_prime_current_source_rule(),
            "trivial_zero_derivative":derivative_of_trivial_zero(1),
            "outside_euler_trivial_zero":trivial_zero_certificate(1),
            "fake_symmetric_completed_multiplier":completed_function_mutant(Q(1,2)),
            "RH_proved":False,"zero_coordinates_read":False,
            "full_Weil_form_positive":False,"global_physical_carrier_authenticated":False}
