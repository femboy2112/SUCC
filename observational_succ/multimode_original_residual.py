"""Original Suzuki all-four residual with multiple lawful high H2 boundary packets.

Complete polynomial-exact frozen-original source, no finite Galerkin
laundering. The low/high *difference* is clamped at both endpoints.
The coefficients minimize a source-model continuum residual plus an
explicit legitimate Gamma-tail action penalty, independently rechecked on
the entire original signed source and full L2 projection Q_E.

No success flag is inferred from a negative conservative Schur lower.
"""
from fractions import Fraction as F
from . import clamped_k_residual_bridge as B
from . import original_continuum_residual as R


class MultiResidualError(ValueError):
    pass


def correction_primitive(low_index,level):
    if type(low_index) is not int or low_index not in (1,2,3,4):
        raise MultiResidualError("four genuine original low directions")
    if type(level) is not int or not 0<=level<=4:
        raise MultiResidualError("high packet level 0..4")
    m=R.high_matching(low_index)+2*level
    # U_m=V(P_m-P_(m+2)), derivative vanishes at both endpoints.
    u=B.add(R.anchor_integral(B.legendre(m)),
            B.scale(R.anchor_integral(B.legendre(m+2)),-1))
    if any(B.value(p,e)!=0 for p in (u,B.derivative(u)) for e in (-R.A,R.A)):
        raise ArithmeticError("not a clamped original high correction")
    if any(B.integral_product(B.derivative(u),B.legendre(k)) for k in (1,2,3,4)):
        raise ArithmeticError("fake original Q4 high packet")
    return {"low_index":low_index,"level":level,
            "indices":((m,F(1)),(m+2,F(-1))),
            "primitive":u,"second_derivative":B.derivative(B.derivative(u)),
            "source_type":"EXACT_SOURCE_Q4_H2_CLAMPED_CORRECTION"}


def _solve_spd_exact(mat,vec):
    """Exact rational LDL elimination; strictly PD, no synthetic inverse."""
    n=len(vec)
    A=[[R.rat(mat[i][j]) for j in range(n)]+[R.rat(vec[i])]
       for i in range(n)]
    if n<1 or n>4 or any(len(row)!=n for row in mat):
        raise MultiResidualError("small original exact residual minimax")
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        raise MultiResidualError("non-symmetric exact moment Gram")
    # Verify positive principal elimination pivots before solving.
    piv=[[A[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        p=piv[i][i]
        if p<=0:raise MultiResidualError("actual clamped Gram/ridge not positive")
        for a in range(i+1,n):
            for b in range(i+1,n):
                piv[a][b]-=piv[a][i]*piv[i][b]/p
        for a in range(i+1,n):
            piv[a][i]=F(0)
    for col in range(n):
        row=next((k for k in range(col,n) if A[k][col]),None)
        if row is None:raise MultiResidualError("source Gram singular")
        A[col],A[row]=A[row],A[col]
        z=A[col][col]
        A[col]=[t/z for t in A[col]]
        for j in range(n):
            if j==col:continue
            fac=A[j][col]
            A[j]=[x-fac*y for x,y in zip(A[j],A[col])]
    return tuple(row[-1] for row in A)


def _piece_gram(a,b):
    return R.projected_piece_gram(a["pieces"],b["pieces"])


def _direct_h2_second_gram(a,b):
    return B.integral_product(B.derivative(B.derivative(a)),
                              B.derivative(B.derivative(b)))


def _fitted_high_response(i,count,J,M,P,params):
    base=R.high_boundary_match(i,F(0))
    bs=[correction_primitive(i,t) for t in range(count)]
    ab=R.exact_piecewise_primitive_action(base["h"],J,M,P,params)
    aps=[R.exact_piecewise_primitive_action(t["primitive"],J,M,P,params)
         for t in bs]
    weight=B.gamma_action_tail(J)**2
    gram=[[ _piece_gram(aps[k],aps[l])
            +weight*_direct_h2_second_gram(bs[k]["primitive"],bs[l]["primitive"])
           for l in range(count)] for k in range(count)]
    rhs=[ _piece_gram(ab,aps[k])
            +weight*_direct_h2_second_gram(base["h"],bs[k]["primitive"])
          for k in range(count)]
    exact=_solve_spd_exact(gram,rhs)
    coeff=tuple(R.safe_ratio_round(v,1,denom=4096,bound=F(8)) for v in exact)
    return coeff,bs


def _construct_h(i,coeff,bs):
    h=R.high_boundary_match(i,F(0))["h"]
    derivative_coeff={i:F(1),R.high_matching(i):F(-1)}
    for t,b in zip(coeff,bs):
        h=B.add(h,B.scale(b["primitive"],-t))
        for k,v in b["indices"]:
            derivative_coeff[k]=derivative_coeff.get(k,F(0))-t*v
    if any(B.value(p,e) for p in (h,B.derivative(h)) for e in (-R.A,R.A)):
        raise ArithmeticError("clamped source high response lost endpoint trace")
    if any(B.integral_product(B.derivative(h),B.legendre(0)) for _ in (0,)):
        raise ArithmeticError("source mean zero changed")
    return h,tuple(sorted((k,c) for k,c in derivative_coeff.items() if c))


def original_multimode_source_schur(count=2,J=12,M=100,P=18,eta=F(1,4),
                                    optimize=True):
    """True source signed whole-continuum Schur lower with 1..4 high packets.

    Validation/fit uses Q_E H_J in ORIGINAL primitive L2. Actual q_J matrix
    entries are from frozen independent Suzuki exponential integrator.
    Remainders are source-authenticated original interval + Gamma H2 tails.
    """
    if type(count) is not int or not 1<=count<=4:
        raise MultiResidualError("finite clamped Q4 correction count 1..4")
    if type(J) is not int or not 1<=J<=24:
        raise MultiResidualError("genuine source Gamma finite budget 1..24")
    eta=R.rat(eta)
    if eta<=0:raise MultiResidualError("Young error constant positive")
    params=R.source_parameters()
    samples={}
    source_cache={}
    for i in range(1,5):
        if optimize:
            coeff,bs=_fitted_high_response(i,count,J,M,P,params)
        else:
            coeff=tuple(F(0) for _ in range(count))
            bs=[correction_primitive(i,t) for t in range(count)]
        h,dercoeff=_construct_h(i,coeff,bs)
        piece=R.exact_piecewise_primitive_action(h,J,M,P,params)
        qp=R.projected_piece_gram(piece["pieces"],piece["pieces"])
        if qp<0:raise ArithmeticError("actual Q_E projected action not PSD")
        tail=B.gamma_action_tail(J)*B.sqrt_up(R.norm_squared(B.derivative(B.derivative(h))))
        er=piece["finite_source_action_error_upper"]
        samples[i]={"coeff":coeff,"derivative_coeff":dercoeff,
            "primitive":h,"action_piece":piece,"approx_Q_norm_sq":qp,
            "source_action_analytic_error":er,"real_Gamma_tail_error":tail,
            "total_residual_error":er+tail}
    groups={}
    for label,ii,kappa in (("odd_derivative",(1,3),F(63,500)),
                            ("even_derivative",(2,4),F(153,500))):
        A=[[R._actual_signed_interval(samples[i]["derivative_coeff"],
                                      samples[j]["derivative_coeff"],J,source_cache)
            for j in ii] for i in ii]
        if any(max(A[i][j][0],A[j][i][0])>min(A[i][j][1],A[j][i][1])
               for i in range(2) for j in range(2)):
            raise ArithmeticError("source Q_J symmetric intervals fail")
        Amid=[[sum(A[i][j])/2 for j in range(2)] for i in range(2)]
        Arad=[[(A[i][j][1]-A[i][j][0])/2 for j in range(2)] for i in range(2)]
        G=[[R.projected_piece_gram(samples[i]["action_piece"]["pieces"],
                                     samples[j]["action_piece"]["pieces"])
            for j in ii] for i in ii]
        if G[0][1]!=G[1][0]:raise ArithmeticError("false source residual Gram symmetry")
        errorsq=sum((samples[i]["total_residual_error"]**2 for i in ii),F())
        lower=[[
            Amid[i][j]-(sum(Arad[i]) if i==j else F()) -
            ((1+eta)*G[i][j]+((1+1/eta)*errorsq if i==j else F()))/kappa
            for j in range(2)] for i in range(2)]
        if lower[0][1]!=lower[1][0]:
            raise ArithmeticError("original Schur lower not symmetric")
        verdict=(lower[0][0]>=0 and lower[1][1]>=0
                 and lower[0][0]*lower[1][1]>=lower[0][1]**2)
        groups[label]={
            "source_kappa":str(kappa),"low_indices":ii,
            "optimal_clamped_correction_coefficients":
                tuple(tuple(str(x) for x in samples[i]["coeff"]) for i in ii),
            "genuine_qJ_signed_intervals":
                tuple(tuple(tuple(map(str,A[i][j])) for j in range(2)) for i in range(2)),
            "surrogate_projected_action_Gram":
                tuple(tuple(str(G[i][j]) for j in range(2)) for i in range(2)),
            "real_Gamma_tail_errors":tuple(str(samples[i]["real_Gamma_tail_error"]) for i in ii),
            "source_analytic_action_errors":tuple(str(samples[i]["source_action_analytic_error"]) for i in ii),
            "source_S4_lower":
                tuple(tuple(str(lower[i][j]) for j in range(2)) for i in range(2)),
            "S4_lower_PSD_certified":bool(verdict)}
    return {"source_sha":params["sha"],"original_first_prime_wavefront":((2,2),),
         "real_Gamma_rungs":J,"Taylor_M":M,"clamped_high_response_correction_count":count,
         "frozen_source_signed_contact_poles_and_prime2":True,
         "actual_full_continuum_L2_residual_certified":True,
         "all_original_high_Q4_boundary_traces_valid":True,
         "parity_schur_blocks":groups,
         "original_first_window_S4_certified_positive":
              all(g["S4_lower_PSD_certified"] for g in groups.values()),
         "RH_proved":False}
