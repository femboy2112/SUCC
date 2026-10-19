"""Original Suzuki source-attested projector-first FIRST-WINDOW trial.

Uses only the pinned 1/2-window source oracles already verified by the parent
repository. It does NOT assert a sign for S4 or RH unless exact source-backed
Loewner lower certificate actually clears. Its error budget is conservative.
"""
from __future__ import annotations

from fractions import Fraction as F

from .direct_quotient_schur import certified_projector_first_upper, exact_psd


def CertifiedSourceDirectQuotientTrial(U=(), *, J_deriv=3, grid=8,
                                       J_galerkin=64, rank=None, eta=F(1,4)):
    """Source-conditional exact rational bracket for the genuine first-window S4.

    Separate SOURCE proof obligations in upstream inherited modules:
    genuine prime2 wavefront, original Gamma+two poles+contact, Bessel4 parity
    coercivity, pointwise G_J derivative intervals, proved BV/Lipschitz bound,
    and omitted-Gamma H1 tail. This adapter only combines those results with
    exact polynomial projection and rational interval comparison. No zeros.
    """
    from . import suzuki_legendre_source as L
    from .certified_four_schur_trial import (
        CertifiedTrial, _trial_matrix_V, _L2_gram_of_trial,
        _sqrt_rat_upper, _sqrt_rat_lower, authentic_suzuki_mode_derivative_point,
        KAPPA_ODD_LOWER, KAPPA_EVEN_LOWER, A_RADIUS,
    )
    from .tate_suzuki_shorting import (
        original_first_prime_derivative_bv_bound,
        original_gamma_derivative_l1_tail,
    )
    base=CertifiedTrial(U=U,J=J_galerkin,rank=rank)
    if base['verdict']=='INVALID_SOURCE':
        return base
    if type(J_deriv) is not int or not 1<=J_deriv<=20 or type(grid) is not int or not 4<=grid<=256 or grid%2:
        return {'verdict':'INVALID_SOURCE','reason':'J_deriv 1..20, even grid 4..256 required','RH_proved':False}
    try:
        if type(eta) not in (int,F): raise ValueError('exact rational eta required')
        eta=F(eta)
        if eta<=0: raise ValueError('positive eta required')
    except (ValueError,ZeroDivisionError,TypeError):
        return {'verdict':'INVALID_SOURCE','reason':'invalid rational Young eta','RH_proved':False}
    rk=base['rank']
    U_norm=tuple(tuple(F(x) for x in row) for row in base['U'])
    V=_trial_matrix_V(U_norm,rk)
    lip_raw=original_first_prime_derivative_bv_bound(J_deriv)
    lips=tuple(lip_raw*sum((abs(V[k][i]) for k in range(rk)), F(0)) for i in range(4))

    modes=tuple(k+1 for k in range(rk) if any(V[k][i] for i in range(4)))
    # Do NOT interpolate or average across the real prime-2 hinge. Each
    # derivative sample is evaluated by the inherited pinned-source oracle.
    pos_rows=[]
    for cell in range(grid//2):
        x=F(2*cell+1,2*grid)
        samples={k:authentic_suzuki_mode_derivative_point(k,x,J_deriv) for k in modes}
        row=[]
        for i in range(4):
            lo=hi=F(0)
            for k in range(rk):
                c=V[k][i]
                if c:
                    iv=samples[k+1]
                    lo+=c*(iv.lo if c>0 else iv.hi)
                    hi+=c*(iv.hi if c>0 else iv.lo)
            row.append((lo,hi))
        pos_rows.append(tuple(row))

    # ORIGINAL Gamma derivative L2 tail: same source-conditional B3 lemma as
    # inherited CertifiedDerivativeEnergyTrial, with an independent wrapper.
    polys={m:L.legendre_polynomial(m,A_RADIUS) for m in range(1,rk+1)}
    ders={m:L.poly_derivative(polys[m]) for m in range(1,rk+1)}
    gram={(m,n):L.poly_integral(L.poly_mul(ders[m],ders[n]),-A_RADIUS,A_RADIUS)
          for m in range(1,rk+1) for n in range(1,rk+1)}
    d=4*J_deriv+1
    sqrt_d_lo=_sqrt_rat_lower(F(d))
    tail_32=F(2,3)/(d*sqrt_d_lo)+F(4)/(d*d*sqrt_d_lo)
    tail_2=F(1,d*d)+F(8,d*d*d)
    eta_young=original_gamma_derivative_l1_tail(J_deriv)
    W=_L2_gram_of_trial(V,rk)
    tails=[]
    for i in range(4):
        norm2=sum((V[m][i]*V[n][i]*gram[(m+1,n+1)] for m in range(rk) for n in range(rk)), F(0))
        end_pos=abs(sum((V[m][i] for m in range(rk)),F(0)))
        end_neg=abs(sum((V[m][i]*(-1 if (m+1)%2 else 1) for m in range(rk)),F(0)))
        ibp=2*_sqrt_rat_upper(norm2)*tail_2+(end_pos+end_neg)*tail_32
        young=eta_young*_sqrt_rat_upper(W[i][i])
        tails.append(min(ibp,young))

    q=certified_projector_first_upper(pos_rows,lips,tails,eta=eta)
    # Parent bound: true source <Vx,GVx> >= mid_J - r I since omitted Gamma
    # modes are PSD. Conditional high D>=kappa_parity K. Therefore:
    #   S4 >= (mid_J-rI) - diag_parity(1/kappa)*T_quot_upper.
    mid=tuple(tuple(F(v) for v in row) for row in base['source_trial_energy_midpoint'])
    r=F(base['interval_loewner_radius_GJ'])
    quotient=q['quotient_loewner_upper']
    low=tuple(tuple((mid[i][j]-(r if i==j else F(0)))-
                    quotient[i][j]/(KAPPA_ODD_LOWER if i%2==0 else KAPPA_EVEN_LOWER)
                    for j in range(4)) for i in range(4))
    if any(low[i][j]!=low[j][i] for i in range(4) for j in range(4)):
        raise ArithmeticError('source parity/no-ghost Loewner symmetry failed')
    positive=exact_psd(low)
    return {
        'source':'PINNED_SUZUKI_FIRST_WINDOW_PROJECTOR_FIRST',
        'verdict':'POSITIVE_CERTIFIED' if positive else 'AMBIGUOUS',
        'source_gate_passed':True,'first_window_only':True,
        'J_deriv':J_deriv,'J_galerkin':J_galerkin,'grid':grid,
        'kappa_by_parity':(str(KAPPA_ODD_LOWER),str(KAPPA_EVEN_LOWER)),
        'gamma_tail_l2_by_column':tuple(str(t) for t in tails),
        'quotient_proxy_gram':tuple(tuple(str(v) for v in row) for row in q['quotient_proxy_gram']),
        'quotient_loewner_upper':tuple(tuple(str(v) for v in row) for row in quotient),
        'certified_S4_lower':tuple(tuple(str(v) for v in row) for row in low),
        'lower_psd_certified':positive,
        'RH_proved':False,
    }
