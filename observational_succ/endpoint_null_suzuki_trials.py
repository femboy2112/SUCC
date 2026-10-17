"""Exact endpoint-null high SUCC responses for original Suzuki Gamma tail.

On I=(-1/2,1/2), u_k=P_k(2x), low k=1..4, high m>=5.
A same-parity trial v=u_k-u_m has v(±1/2)=0; choose the first
admissible high m of matching parity (m=5 odd, m=6 even).
This MINIMIZES ||v'||² among all endpoint-null, finite high-sector
responses, with no claim about the original full signed Weil form.
"""
from __future__ import annotations
from fractions import Fraction as F


class EndpointNullError(ValueError):
    pass


def _exact_integer(k):
    if type(k) is not int or k<1:
        raise EndpointNullError("positive exact mode integer required")
    return k


def legendre_derivative_pair(k,l):
    """Exact <P_k(2x)',P_l(2x)'> on (-1/2,1/2)."""
    _exact_integer(k);_exact_integer(l)
    if (k-l)%2:return F(0)
    t=min(k,l)
    return F(2*t*(t+1))


def first_high_same_parity(k,cut=4):
    """Smallest high mode m>cut with m≡k mod 2."""
    _exact_integer(k)
    if type(cut) is not int or cut<k:
        raise EndpointNullError("proper original low/high cut required")
    m=cut+1
    return m if (m-k)%2==0 else m+1


def endpoint_null_minimal_energy(k,cut=4):
    """Sharp min H1 derivative energy under endpoint constraints.

    For high expansion h=Σ_{m>cut} c_m P_m with h(±a)=P_k(±a),
    both parity classes satisfy separate sum constraints; the optimal
    same-parity high mode m is first_high_same_parity. Other components
    contribute nonnegative mutually independent derivative-increments.
    """
    m=first_high_same_parity(k,cut)
    exact=legendre_derivative_pair(k,k)+legendre_derivative_pair(m,m) -2*legendre_derivative_pair(k,m)
    assert exact==2*(m*(m+1)-k*(k+1))
    return {"low":k,"first_high":m,"derivative_energy_min":exact,
            "old_low_derivative_energy":legendre_derivative_pair(k,k),
            "endpoint_mismatch_plus":F(0),"endpoint_mismatch_minus":F(0),
            "source_independent_analytic_theorem":True,"RH_proved":False}


def endpoint_null_U(rank=6,cut=4):
    if type(rank) is not int or not 6<=rank<=12 or cut!=4:
        raise EndpointNullError("original four-mode source with rank 6..12 required")
    U=[[F(0)]*4 for _ in range(rank-4)]
    for k in range(1,5):
        m=first_high_same_parity(k,cut)
        U[m-5][k-1]=F(1)
    return tuple(tuple(row) for row in U)


def endpoint_null_gamma_tail_certificate(J=20):
    """Actual original B3 Gamma derivative tail; no invented Gamma rung.

    Compare the L2 tail upper at U=0 vs endpoint-null U. Both are valid
    source-conditional B3 analytic bounds; sign of S4 is not evaluated here.
    """
    if type(J) is not int or not 1<=J<=20:
        raise EndpointNullError("true Gamma truncation J 1..20 required")
    from .certified_four_schur_trial import _sqrt_rat_upper,_sqrt_rat_lower
    from .tate_suzuki_shorting import original_gamma_derivative_l1_tail
    d=4*J+1
    rootd=_sqrt_rat_lower(F(d))
    bulk=F(1,d*d)+F(8,d*d*d)
    edge=F(2,3)/(d*rootd)+F(4)/(d*d*rootd)
    young=original_gamma_derivative_l1_tail(J)
    rows=[]
    for k in range(1,5):
        m=first_high_same_parity(k)
        old_d=legendre_derivative_pair(k,k)
        new_d=endpoint_null_minimal_energy(k)["derivative_energy_min"]
        old_l2=F(1,2*k+1)
        new_l2=old_l2+F(1,2*m+1)
        old_ibp=2*_sqrt_rat_upper(old_d)*bulk+2*edge
        new_ibp=2*_sqrt_rat_upper(new_d)*bulk
        old_upper=min(old_ibp,young*_sqrt_rat_upper(old_l2))
        new_upper=min(new_ibp,young*_sqrt_rat_upper(new_l2))
        rows.append({
            "low_mode":k,"high_mode":m,
            "old_source_Gamma_tail_L2":old_upper,
            "endpoint_null_source_Gamma_tail_L2":new_upper,
            "strict_improvement":new_upper<old_upper,
            "endpoint_term_exactly_zero":True,
        })
    return {"J":J,"d":d,"sector_comparison":tuple(rows),
            "all_low_columns_strict_improvement":all(a["strict_improvement"] for a in rows),
            "Gamma_tail_B3_source_conditional":True,"S4_sign":"UNVERIFIED","RH_proved":False}


def genuine_endpoint_null_S4_trial(J_deriv=2,J_galerkin=64):
    from .analytic_suzuki_schur_gate import CertifiedAnalyticSuzukiTrial
    if type(J_deriv) is not int or not 1<=J_deriv<=20:
        raise EndpointNullError("original finite Gamma J 1..20 required")
    result=CertifiedAnalyticSuzukiTrial(U=endpoint_null_U(),rank=6,
                                       J_deriv=J_deriv,J_galerkin=J_galerkin,
                                       digits=100)
    return {
        "original_source_authentication":result.get("source_passport_verified",False),
        "first_window_verdict":result["verdict"],
        "rational_response_U":endpoint_null_U(),
        "gamma_tail":endpoint_null_gamma_tail_certificate(J_deriv),
        "RH_proved":False,
    }
