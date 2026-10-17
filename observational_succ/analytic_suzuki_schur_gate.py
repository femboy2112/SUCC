"""Source-gated first-window analytic Suzuki Schur trial (NO sampling grid).

Upstream signed source and Bessel high coercivity are verified, not replaced.
The first J gamma rungs are integrated piecewise-exactly, and the true Gamma
tail is bounded by inherited B3 source Sobolev estimates. RH remains open.
"""
from __future__ import annotations
from fractions import Fraction as F

from .piecewise_suzuki_integrator import I,genuine_piecewise_gram
from .direct_quotient_schur import exact_psd


def CertifiedAnalyticSuzukiTrial(U=(),*,J_deriv=6,J_galerkin=64,
                                 rank=None,digits=100,young_eta=F(1,8)):
    from . import suzuki_legendre_source as L
    from .certified_four_schur_trial import (
        CertifiedTrial,_trial_matrix_V,_L2_gram_of_trial,
        _sqrt_rat_upper,_sqrt_rat_lower,KAPPA_ODD_LOWER,
        KAPPA_EVEN_LOWER,A_RADIUS,
    )
    from .tate_suzuki_shorting import original_gamma_derivative_l1_tail
    if type(J_deriv) is not int or not 1<=J_deriv<=20:
        return {"verdict":"INVALID_SOURCE","reason":"J_deriv 1..20 required","RH_proved":False}
    if type(rank) is not int and rank is not None:
        return {"verdict":"INVALID_SOURCE","reason":"integer rank required","RH_proved":False}
    try:
        if type(young_eta) not in (int,F) or F(young_eta)<=0:
            raise ValueError("positive exact Young eta required")
        eta=F(young_eta)
    except (ValueError,TypeError,ZeroDivisionError):
        return {"verdict":"INVALID_SOURCE","reason":"bad exact eta","RH_proved":False}
    base=CertifiedTrial(U=U,J=J_galerkin,rank=rank)
    if base["verdict"]=="INVALID_SOURCE":return base
    rk=base["rank"]
    if rk>8:
        return {"verdict":"INVALID_SOURCE","reason":"analytic finite packet rank<=8","RH_proved":False}
    U_norm=tuple(tuple(F(v) for v in row) for row in base["U"])
    V=_trial_matrix_V(U_norm,rk)
    packet=genuine_piecewise_gram(J_deriv,rk,digits=digits)
    modeQ=packet["quotient_gram"]
    qmat=[[I.of(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(i,4):
            if (i-j)%2:continue
            accum=sum((V[k][i]*V[l][j]*modeQ[k][l]
                      for k in range(rk) for l in range(rk)
                      if V[k][i] and V[l][j]),I.of(0))
            qmat[i][j]=qmat[j][i]=accum

    # For every exact symmetric entry M_ij in [lo,hi], M is below
    # midpoint matrix plus per-parity max row sum radius times identity.
    Qupper=[[qmat[i][j].mid() for j in range(4)] for i in range(4)]
    rs={}
    for label,sector in (("odd",(0,2)),("even",(1,3))):
        r=max(sum((qmat[i][j].rad() for j in sector),F(0)) for i in sector)
        rs[label]=r
        for i in sector:Qupper[i][i]+=r

    # Original omitted Gamma derivative Sobolev estimate, not a finite-J fit.
    polys={k:L.legendre_polynomial(k,A_RADIUS) for k in range(1,rk+1)}
    ders={k:L.poly_derivative(polys[k]) for k in range(1,rk+1)}
    deriv_gram={(k,l):L.poly_integral(L.poly_mul(ders[k],ders[l]),-A_RADIUS,A_RADIUS)
                for k in range(1,rk+1) for l in range(1,rk+1)}
    d=4*J_deriv+1
    s=_sqrt_rat_lower(F(d))
    tail_half=F(2,3)/(d*s)+F(4)/(d*d*s)
    tail_bulk=F(1,d*d)+F(8,d*d*d)
    W=_L2_gram_of_trial(V,rk)
    # Correlated contact: actual C_inf = chosen rational midpoint + epsilon,
    # |epsilon| <= source radius. Project Q BEFORE bounding epsilon.
    # The derivative contact term is exactly epsilon * primitive(v_i).
    # The ORIGINAL source has one shared contact C, not independent
    # per-mode intervals. Closed-form Legendre primitive recurrence gives
    # the exact polynomial-orthogonal contact Gram in sparse parity bands.
    from .contact_ladder_projection import projected_contact_trial_gram
    source_contact_radius=packet["contact_source_rational_radius"]
    contact_gram=projected_contact_trial_gram(V,degree=3)
    contact_projection_norm2=[contact_gram[i][i] for i in range(4)]
    if any(v<0 for v in contact_projection_norm2):
        raise ArithmeticError("source contact projected Gram not PSD")
    tail=[]
    for i in range(4):
        norm2=sum((V[k][i]*V[l][i]*deriv_gram[k+1,l+1]
                   for k in range(rk) for l in range(rk)),F(0))
        endpoint_pos=abs(sum((V[k][i] for k in range(rk)),F(0)))
        endpoint_neg=abs(sum((V[k][i]*(-1 if (k+1)%2 else 1)
                              for k in range(rk)),F(0)))
        ibp=2*_sqrt_rat_upper(norm2)*tail_bulk+(endpoint_pos+endpoint_neg)*tail_half
        young=original_gamma_derivative_l1_tail(J_deriv)*_sqrt_rat_upper(W[i][i])
        # Gamma remainder and shared contact-source uncertainty are different
        # source channels. Their L2 upper bounds add by the triangle inequality.
        tail.append(min(ibp,young)+
                    source_contact_radius*_sqrt_rat_upper(contact_projection_norm2[i]))

    for sector in ((0,2),(1,3)):
        total=sum((tail[i] for i in sector),F(0))
        for i in sector:
            Qupper[i][i]=(1+eta)*Qupper[i][i]+(1+1/eta)*tail[i]*total
        for i in sector:
            for j in sector:
                if i!=j:Qupper[i][j]=(1+eta)*Qupper[i][j]
    Qupper=tuple(tuple(row) for row in Qupper)
    if not exact_psd(Qupper):
        raise ArithmeticError("source truncation projected energy upper not PSD")

    trial=tuple(tuple(F(v) for v in row) for row in base["source_trial_energy_midpoint"])
    source_radius=F(base["interval_loewner_radius_GJ"])
    lower=tuple(tuple(
        trial[i][j]-(source_radius if i==j else F(0))-
        Qupper[i][j]/(KAPPA_ODD_LOWER if i%2==0 else KAPPA_EVEN_LOWER)
        for j in range(4)) for i in range(4))
    source_positive=exact_psd(lower)
    # Source interval expressions may have >4300 decimal digits due to exact
    # rational antiderivatives. Export separate outward Loewner matrices with
    # finite 18-digit rational denominators, NOT false exact point estimates.
    from math import floor
    def compact_bound(matrix, direction):
        scale=10**18
        raw=tuple(tuple(F(v.numerator*scale//v.denominator,scale) for v in row)
                  for row in matrix)
        # Every element lies within 1/scale above its downward representative.
        # Gershgorin gives spectral comparison error <= 4/scale.
        correction=F(4,scale)*(1 if direction=="upper" else -1)
        return tuple(tuple(raw[i][j]+(correction if i==j else 0)
                           for j in range(4)) for i in range(4))
    reported_upper=compact_bound(Qupper,"upper")
    reported_lower=compact_bound(lower,"lower")
    if not exact_psd(tuple(tuple(reported_upper[i][j]-Qupper[i][j]
                           for j in range(4)) for i in range(4))):
        raise ArithmeticError("outward quotient reporting not Loewner upper")
    if not exact_psd(tuple(tuple(lower[i][j]-reported_lower[i][j]
                           for j in range(4)) for i in range(4))):
        raise ArithmeticError("outward Schur reporting not Loewner lower")

    return {
        "source":"PINNED_ORIGINAL_SUZUKI_ANALYTIC_GAMMA_PRIME2_FIRST_WINDOW",
        "verdict":"POSITIVE_CERTIFIED" if source_positive else "AMBIGUOUS",
        "source_passport_verified":True,"no_spatial_quadrature":True,
        "rank":rk,"Gamma_J":J_deriv,"Galerkin_J":J_galerkin,
        "prime2_hinge":(str(packet["genuine_prime2_hinge"].lo),
                        str(packet["genuine_prime2_hinge"].hi)),
        "finite_quotient_gram_midpoint_diagnostic_18digits":tuple(
            tuple(str(F(qmat[i][j].mid().numerator*10**18//
                        qmat[i][j].mid().denominator,10**18))
                  for j in range(4)) for i in range(4)),
        # Directed upper decimal rationals are diagnostics with finite text size.
        "finite_quotient_gram_radius_parity":{
            k:str(F((v.numerator*10**18+v.denominator-1)//v.denominator,10**18))
            for k,v in rs.items()},
        "omitted_Gamma_and_contact_derivative_L2_upper":tuple(
            str(x) for x in tail),
        "contact_source_radius":str(source_contact_radius),
        "contact_projected_primitive_norm2":tuple(str(x) for x in contact_projection_norm2),
        "true_quotient_gram_upper":tuple(tuple(str(v) for v in row) for row in reported_upper),
        "true_S4_Loewner_lower":tuple(tuple(str(v) for v in row) for row in reported_lower),
        "source_S4_lower_psd":source_positive,
        "RH_proved":False,
    }
