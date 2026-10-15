"""Source-identified dyadic Zeno/Weil operator convergence *error law*.

This compiles ancestor PR #85's authentic signed Suzuki Gamma/pole/prime
operator bounds into one finite-description, uniform-in-test dyadic schedule.
It DOES NOT build the N×N matrices for N=4^k, determine a sign, or prove RH.

Source validity: for 0<a<=1 the parent proves L_J(a)<=45+sum_{j<J}
2/(4j+1), and authentic omitted Gamma on L0² is PSD with
||T_J||<=2/(4J+1)^2+16/(4J+1)^3. For J=2^k,
sum 2/(4j+1)<=2+k/2 by dyadic blocks. Therefore the structural
norm error <=4a^2(47+k/2)/4^k+GammaTail(2^k).
A separately constructed interval-node error eta would add 2a*eta.
"""
from __future__ import annotations
from fractions import Fraction as Q

from .source_weil_hierarchy import authentic_positive_gamma_tail_norm


class WeilZenoError(ValueError):
    pass


def rat(x):
    if type(x) not in (int,Q):raise WeilZenoError("authentic rational radius only")
    return Q(x)


def level(k):
    if type(k) is not int or not 1<=k<=256:
        raise WeilZenoError("finite dyadic proof level k=1..256")
    return k


def dyadic_stage(a,k):
    """Mathematically defined exact source operator, NOT materialized matrix."""
    a=rat(a);level(k)
    if not 0<a<=1:raise WeilZenoError("fixed true-prime source window 0<a<=1")
    J=2**k;N=4**k
    real_place_upper=9 if a<=Q(1,2) else 45
    Lbound=real_place_upper+2+Q(k,2)
    cell_width=2*a/N
    spatial=2*a*cell_width*Lbound
    gamma=authentic_positive_gamma_tail_norm(J)
    result={
        "original_source":"AUTHENTIC_ZETA_PRIME_POWER_GAMMA_POLE_HALF_DENSITY",
        "real_place_radius":a,"level":k,"Gamma_modes":J,"cell_count":N,
        "finite_Zeno_clock":1-Q(1,2**k),
        "analytic_spatial_bound":spatial,
        "positive_Gamma_tail_bound":gamma,
        "structural_norm_error":spatial+gamma,
        "node_interval_error_included":False,
        "matrix_constructed":False,
        "negative_depth_vanishes_proved":False,
        "rh_proved":False
    }
    assert 0<result["structural_norm_error"]
    return result


def add_certified_node_error(contract, eta, *, authenticator=None):
    """A numeric eta without independent source proof cannot be promoted.

    This API reports CONDITIONAL unless an independent authenticated
    source-interval verifier is supplied; this bounded module has no
    such verifier for arbitrary dyadic J,N. The caller cannot spoof it
    by passing a free-form source label or string 'verified'.
    """
    eta=rat(eta)
    if eta<0:raise WeilZenoError("node interval error nonnegative")
    if not isinstance(contract,dict) or contract.get("original_source")!=(
        "AUTHENTIC_ZETA_PRIME_POWER_GAMMA_POLE_HALF_DENSITY"):
        raise WeilZenoError("original-source stage contract required")
    a=rat(contract.get("real_place_radius"))
    k=contract.get("level")
    canonical=dyadic_stage(a,k)
    if (set(contract)!=set(canonical)
        or any(type(contract[key]) is not type(canonical[key])
               for key in canonical)
        or contract!=canonical):
        raise WeilZenoError("forged, inexact, or modified stage/refinement data")
    if authenticator is not None:
        raise WeilZenoError("unimplemented proof adapter: no external testimony accepted")
    return {
       "source":"AUTHENTIC_THEORETICAL_G_J_FINITE_CELL",
       "total_error_if_node_bound_valid":
          contract["structural_norm_error"]+2*a*eta,
       "actual_all_nodes_interval_bound_authenticated":False,
       "arithmetic_operator_positivity_certified":False,
       "rh_proved":False,
    }


def structural_modulus(a,tolerance,*,max_level=256):
    """Finite level where UNROUNDED source-defined approximation bound < eps.

    This is a mathematical structural rate; actual matrix/transcendental
    evaluation still requires separate source-certified node intervals.
    """
    a=rat(a);eps=rat(tolerance)
    if eps<=0:raise WeilZenoError("positive rational accuracy required")
    level(max_level)
    for k in range(1,max_level+1):
        if dyadic_stage(a,k)["structural_norm_error"]<eps:return k
    raise WeilZenoError("structural rate beyond declared budget")


def signed_source_gap_contract(a,k):
    """No sign claim: the exact source diamond and its negative depth.

    If the exact dyadic approximate matrix has certified negative depth d,
    then |d_-(G_a)-d|<=structural_norm_error, but d is NOT evaluated here.
    """
    m=dyadic_stage(a,k)
    return {
        "source":m["original_source"],"level":k,
        "if_exact_stage_negative_depth_d_then_error_at_most":
          m["structural_norm_error"],
        "signed_global_negative_depth_identified":False,
        "requires_authentic_finite_operator_spectrum":True,
        "no_nontrivial_zero_input":True,
        "rh_proved":False
    }
