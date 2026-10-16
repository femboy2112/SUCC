"""Canonical convergent-domain unit/prime SUCC -> Tate Mellin/source bridge.

Reuses actual StandardTateSource, normalized p-adic Haar, true von Mangoldt
coefficients, and source Weil intervals. No finite computation certifies Tate
Poisson universally, a physical observer, the Weil sign, or RH.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial
from .unit_prime_succ import prime, prime_list, prime_smooth


class UnitTateBridgeError(ValueError):
    pass


def _integer(value: int, *, low: int = 1, high: int = 300) -> int:
    if type(value) is not int or not low <= value <= high:
        raise UnitTateBridgeError(f"Exact integer within {low}..{high} required")
    return value


def _source(source):
    from .tate_idelic_zeta import StandardTateSource
    if type(source) is not StandardTateSource:
        raise UnitTateBridgeError("Canonical StandardTateSource required, not arbitrary Tate test")
    return source


def local_prime_occupation(p: int, beta: int, max_valuation: int = 5) -> dict:
    """Local Gibbs k>=0 is geometric; exact finite prefix and infinite tail."""
    _integer(p, low=2, high=300)
    if not prime(p):
        raise UnitTateBridgeError("Independent Euler-place label must be prime")
    _integer(beta, low=2, high=16)
    _integer(max_valuation, low=0, high=40)
    q = Q(1, p**beta)
    states = tuple((k, (1-q)*q**k) for k in range(max_valuation+1))
    tail = q**(max_valuation+1)
    assert sum((prob for _, prob in states), Q())+tail == 1
    return {"p":p,"beta":beta,"shells":states,"tail":tail,
            "mean_valuation":Q(1,p**beta-1),
            "variance_valuation":Q(p**beta,(p**beta-1)**2),
            "real_probability_not_Qp_valued_Haar":True}


def source_prime_stage(source, prime_cutoff: int, beta: int, *,
                       shell_depth: int = 5, integer_prefix: int | None = None) -> dict:
    """Genuine Tate local p-shells vs independent weighted prime SUCC path.

    The finite product is NOT a global additive Schwartz--Bruhat test.
    """
    source=_source(source)
    _integer(prime_cutoff,low=2,high=100)
    _integer(beta,low=2,high=12)
    _integer(shell_depth,low=0,high=30)
    if integer_prefix is None:
        integer_prefix=min(2*prime_cutoff,240)
    _integer(integer_prefix,low=prime_cutoff,high=1000)
    from .tate_idelic_zeta import (
        finite_euler_stage, multiplicative_shell_mass, euler_exhaustion_bound,
    )
    ps=prime_list(prime_cutoff)
    actual=finite_euler_stage(ps,beta,shell_depth)
    independent_product=Q(1)
    factors=[]
    for p in ps:
        ball=source.local_test(p)
        if ((ball.source_id,ball.epoch)!=(source.source_id,source.epoch)
                or (ball.p,ball.a,ball.k)!=(p,Q(0),0)):
            raise UnitTateBridgeError("Wrong local Zp Schwartz source/provenance")
        if multiplicative_shell_mass(p,0)!=1 or multiplicative_shell_mass(p,2)!=1:
            raise UnitTateBridgeError("Wrong local multiplicative Haar normalization")
        factor=Q(p**beta,p**beta-1)
        independent_product*=factor
        factors.append((p,factor))
    if independent_product!=actual["complete_finite_place_product"]:
        raise UnitTateBridgeError("Prime FUCC and genuine Tate place factors disagree")
    integers=prime_smooth(ps,integer_prefix,beta)
    if any(weight!=Q(1,n**beta) for n,weight in integers.items()):
        raise UnitTateBridgeError("Prime traversals lost the correct unit weights")
    if any(n not in integers for n in range(1,prime_cutoff+1)):
        raise UnitTateBridgeError("Genuine prime prefix omitted a source integer")
    tail=euler_exhaustion_bound(prime_cutoff,beta)["absolute_error_bound"]
    return {"source_id":source.source_id,"epoch":source.epoch,
            "beta":beta,"primes":ps,"unit_coefficient":Q(1),
            "local_test":"canonical 1_Zp at every finite prime",
            "local_factors":tuple(factors),
            "stage_zeta":independent_product,
            "finite_shell_zeta":actual["finite_shell_product"],
            "finite_shell_tail":actual["exact_shell_tail"],
            "smooth_integer_prefix":integer_prefix,
            "smooth_state_count":len(integers),
            "zeta_interval":(independent_product,independent_product+tail),
            "global_Tate_test_is_finite_prime_product":False,
            "full_infinite_Euler_product_executed":False,
            "current_is_Weil_positive":False,"RH_proved":False}


def prime_variance_tail_bound(P: int, beta: int) -> Q:
    """Certified rational upper for omitted prime log-energy variance.

    beta>=2, P>=3. Derive from monotone (log x)^2/x^beta, using
    log(P)<=ceil(log_2(P)) and (1-p^-beta)^-2 <= (1-2^-beta)^-2.
    """
    _integer(P,low=3,high=300)
    _integer(beta,low=2,high=16)
    L=Q((P-1).bit_length())
    b=beta-1
    return Q(P)**(1-beta) * (
        L*L/b + 2*L/b**2 + Q(2,b**3)
    ) / (1-Q(1,2**beta))**2


def finite_prime_current(source, P: int, beta: int) -> dict:
    """True prime-current/variance rational intervals, only beta>=2.

    Uses actual inherited von Mangoldt tape (6 is NOT a logarithmic atom).
    """
    source=_source(source)
    _integer(P,low=2,high=100)
    _integer(beta,low=2,high=12)
    from .source_weil_hierarchy import iv, log_iv
    from .tate_idelic_zeta import log_derivative_tail_bound
    source_jets=source.logarithmic_coefficients(P,beta)
    actual=dict(source_jets["formal_logp_coefficients"])
    ps=prime_list(P)
    expected={}
    for p in ps:
        power=p
        while power<=P:
            expected[p]=expected.get(p,Q())+Q(1,power**beta)
            power*=p
    if actual!=expected or 6 in dict(source_jets["prime_power_labels"]):
        raise UnitTateBridgeError("Euler source coefficients != true prime-power jets")
    curr=iv(0)
    var=iv(0)
    for p in ps:
        l=log_iv(p)
        curr+=l*Q(1,p**beta-1)
        var+=l*l*Q(p**beta,(p**beta-1)**2)
    tail=log_derivative_tail_bound(P,beta)
    vtail=prime_variance_tail_bound(P,beta) if P>=3 else None
    return {"source_id":source.source_id,"epoch":source.epoch,
            "beta":beta,"prime_cutoff":P,
            "prime_occupation_mean_logH_partial":curr,
            "prime_occupation_variance_logH_partial":var,
            "full_prime_current_interval":(curr.lo,curr.hi+tail),
            "full_prime_variance_interval":(
                (var.lo,var.hi+vtail) if vtail is not None else None
            ),
            "source_prime_variance_tail_upper":vtail,
            "source_von_Mangoldt_tail_upper":tail,
            "current_identity":"-zeta'/zeta=sum Lambda(n)*n^-s",
            "current_is_Weil_positive":False,"RH_proved":False}


def archimedean_even_source(source, beta: int) -> dict:
    """Canonical Gaussian Mellin and first two log-clock cumulants.

    gamma_R(2m)=(m-1)!pi^-m;
    (log gamma_R)'(2m)=(H_(m-1)-gamma-logpi)/2;
    (log gamma_R)''(2m)=(pi^2/6-H2_(m-1))/4.
    """
    source=_source(source)
    _integer(beta,low=2,high=20)
    if beta%2:
        raise UnitTateBridgeError("Exact Gamma/pi chart requires even beta")
    from .tate_idelic_zeta import real_gamma_even_integer
    from .source_weil_hierarchy import I, iv, pi_iv, log_interval, gamma_iv
    coeff,power=real_gamma_even_integer(beta)
    m=beta//2
    if (coeff,power)!=(factorial(m-1),-m):
        raise UnitTateBridgeError("Noncanonical real Gaussian Mellin factor")
    pi=pi_iv()
    gaussian=I(Q(coeff,1)/pi.hi**m,Q(coeff,1)/pi.lo**m)
    H1=sum((Q(1,k) for k in range(1,m)),Q())
    H2=sum((Q(1,k*k) for k in range(1,m)),Q())
    arch_mean=(iv(H1)-gamma_iv()-log_interval(pi))/2
    arch_var=(pi*pi/6-iv(H2))/4
    if arch_var.lo<=0 or gaussian.lo<=0:
        raise UnitTateBridgeError("Gaussian Mellin log variance invalid")
    c2,p2=real_gamma_even_integer(beta+2)
    if (Q(c2,coeff),p2-power)!=(Q(beta,2),-1):
        raise UnitTateBridgeError("Gaussian 2-step Mellin ladder mismatch")
    return {"source_id":source.source_id,"epoch":source.epoch,
            "beta":beta,"gaussian":"exp(-pi*x^2) on R",
            "local_Mellin":"integral_Rtimes phi(x)|x|^beta dx/|x|",
            "gamma_pi_monomial":(coeff,power),
            "gamma_interval":gaussian,
            "arch_mean_log_abs":arch_mean,
            "arch_variance_log_abs":arch_var,
            "mellin_s_to_s_plus_2_ratio":(Q(beta,2),-1),
            "real_sign_multiplier":2,
            "source_Gaussian_self_dual":True,
            "RH_proved":False}


def completed_tate_clock(source, P: int, beta: int) -> dict:
    """Bound canonical Lambda(beta), derivative and log-norm variance.

    The ALL-test Tate/Poisson theorem is imported from its existing dossier.
    """
    from .source_weil_hierarchy import I
    from .tate_idelic_zeta import TateZeroModes
    from .tate_weil_distribution import TateWeilSource
    source=_source(source)
    weil=TateWeilSource.from_tate(source)
    if (weil.character,weil.source_id,weil.epoch)!=(
        "zeta",source.source_id,source.epoch
    ):
        raise UnitTateBridgeError("Canonical Tate/Weil passport mismatch")
    finite=source_prime_stage(source,P,beta)
    arch=archimedean_even_source(source,beta)
    prime_curr=finite_prime_current(source,P,beta)
    z0,z1=finite["zeta_interval"]
    gaussian=arch["gamma_interval"]
    completed=gaussian*I(z0,z1)
    a=arch["arch_mean_log_abs"]
    c0,c1=prime_curr["full_prime_current_interval"]
    logder=I(a.lo-c1,a.hi-c0)
    xi_logder=logder+Q(1,beta)+Q(1,beta-1)
    av=arch["arch_variance_log_abs"]
    pv=prime_curr["full_prime_variance_interval"]
    total_variance=I(av.lo+pv[0],av.hi+pv[1]) if pv is not None else None
    zero=TateZeroModes()
    if zero.residues!=(Q(-1),Q(1)):
        raise UnitTateBridgeError("Tate Poisson zero-mode residues changed")
    if not (completed.lo>0 and logder.lo<=logder.hi):
        raise UnitTateBridgeError("Completed source interval invalid")
    return {"source_id":source.source_id,"epoch":source.epoch,
            "beta":beta,"zeta_interval":finite["zeta_interval"],
            "gamma_interval":gaussian,"completed_Lambda_interval":completed,
            "prime_current_interval":prime_curr["full_prime_current_interval"],
            "completed_log_derivative_interval":logder,
            "entire_xi_log_derivative_interval":xi_logder,
            "completed_log_norm_variance_interval":total_variance,
            "polar_zero_modes":zero.residues,
            "units_multiplicative_Haar_mass":1,
            "global_Poisson_theorem_imported_not_finite_tested":True,
            "not_Weil_PSD_certificate":True,
            "RH_proved":False}


def scalar_gaussian_rescaling(beta: int, scale: int | Q) -> dict:
    """A different real Gaussian shares EVERY prime factor but changes Mellin."""
    _integer(beta,low=2,high=20)
    if beta%2:
        raise UnitTateBridgeError("Exact rational scale ratio requires even beta")
    if type(scale) not in (int,Q) or Q(scale)<=0:
        raise UnitTateBridgeError("Positive rational Gaussian scale required")
    a=Q(scale)
    return {"beta":beta,"a":a,
            "new_to_canonical_Mellin_ratio":a**(-(beta//2)),
            "prime_weights_unchanged":True,
            "standard_Fourier_self_dual":a==1,
            "same_canonical_Tate_test":a==1,
            "RH_proved":False}


def truncated_prime_product_is_adelic_schwartz_test(P: int) -> bool:
    """False: infinitely many outside unit constraints violate additive local constancy."""
    _integer(P,low=2,high=300)
    return False


def finite_coherent_vs_diagonal_gibbs(beta: int) -> dict:
    """Synthetic {1,2} restriction: same diagonal, unequal offdiagonal states."""
    _integer(beta,low=2,high=12)
    if beta%2:
        raise UnitTateBridgeError("Rational amplitudes require even beta")
    amp=Q(1,2**(beta//2))
    Z=1+amp**2
    return {"beta":beta,"diagonal_probs":(1/Z,amp**2/Z),
            "pure_exchange_expectation":2*amp/Z,
            "diagonal_Gibbs_exchange_expectation":Q(),
            "same_diagonal_distribution":True,
            "same_state_on_all_observables":False}


def diagonal_norm_unit(rational: int | Q) -> Q:
    """Adelic norm-one diagonal Q×, NOT only the Dirichlet basis vector 1."""
    from .all_places_zeta import product_formula_rational
    if type(rational) not in (int,Q) or not rational:
        raise UnitTateBridgeError("Nonzero exact diagonal rational required")
    return product_formula_rational(Q(rational))
