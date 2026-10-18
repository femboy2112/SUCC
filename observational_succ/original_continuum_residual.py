"""Complete first-prime SIGNED Suzuki primitive action: certified continuum residual.

The main mathematical object is the full L2 norm of Q_E H_J h, NOT a
finite Galerkin matrix.  H_J uses the original real-Gamma OU rungs, true
prime2 with half density, contact and BOTH signed poles. We approximate
it by an explicitly constructed Fraction piecewise polynomial; the
operator error is rigorously bounded using Taylor+translation+source
intervals, not numerical sampling or invented positive covariance.

On clamped h in H2_0, the authentic omitted Gamma action has O(J^-2)
bound. Exact source signed low/high Gram supplies Q_J(h) as a lower for
completed Q(h). A primitive-space variational Schur bound then follows.
All-positive SIGN claims are conditional on passing exact source sign.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as F
from math import comb, factorial

from . import clamped_k_residual_bridge as B

SOURCE_SHA = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
A = F(1, 2)


class OriginalResidualError(ValueError):
    pass


def rat(x):
    if type(x) not in (int, F):
        raise OriginalResidualError("only exact Fraction/int source data")
    return F(x)


def poly_integral(p):
    return B.trim((F(0),) + tuple(v/F(i+1) for i,v in enumerate(p)))


def definite(p,left=-A,right=A):
    antiderivative = poly_integral(p)
    return B.value(antiderivative,right)-B.value(antiderivative,left)


def anchor_integral(p):
    z=poly_integral(p)
    return B.add(z,(-B.value(z,-A),))


def shifted(p,b):
    b=rat(b)
    z=[F(0)]*len(p)
    for i,ci in enumerate(p):
        if ci:
            for j in range(i+1):
                z[j]+=ci*comb(i,j)*b**(i-j)
    return B.trim(z)


def norm_squared(p):
    return definite(B.mul(p,p))


def derivative_norm_squared(p):
    return norm_squared(B.derivative(p))


def low_primitive(i):
    if type(i) is not int or i not in (1,2,3,4):
        raise OriginalResidualError("only original low Legendre 1..4")
    return anchor_integral(B.legendre(i))


def high_matching(i):
    return (5,6,5,6)[i-1]


def clamped_name(i):
    return "odd_derivative" if i%2 else "even_derivative"


def high_boundary_match(i,t=F(0)):
    """h=V(P_i-P_{m_i})-t F_clamped is true H2_0.

    x=V P_{m_i}+t F_clamped lies in source high E, and h=V P_i-x.
    The endpoint derivative zero is an exact source-geometry condition.
    """
    t=rat(t)
    if type(i) is not int or i not in (1,2,3,4):
        raise OriginalResidualError("true original low mode index 1..4")
    name=clamped_name(i)
    B.checked_trial(name)
    raw=B.add(low_primitive(i),B.scale(anchor_integral(B.legendre(high_matching(i))),-1))
    h=B.add(raw,B.scale(B.CLAMPED[name]["poly"],-t))
    dh=B.derivative(h)
    for endpoint in (-A,A):
        if B.value(h,endpoint)!=0 or B.value(dh,endpoint)!=0:
            raise ArithmeticError("not an H2_0 zero exterior source trial")
    coeff={i:F(1),high_matching(i):F(-1)}
    for k,c in B.CLAMPED[name]["coeff"]:
        coeff[k]=coeff.get(k,F(0))-t*c
    coeff=tuple(sorted((k,c) for k,c in coeff.items() if c))
    if any(B.integral_product(dh,B.legendre(k)) for k in (0,)) :
        # A difference of two genuine mean-zero Legendre modes.
        raise ArithmeticError("source mean-zero derivative violated")
    return {"low":i,"matched_high":high_matching(i),
        "clamped_high":name,"coefficient":t,"h":h,
        "derivative_coeff":coeff,
        "norm_sq":norm_squared(h),"derivative_norm_sq":derivative_norm_squared(h),
        "second_derivative_norm_sq":norm_squared(B.derivative(dh)),
        "H2_zero_extended":True,"RH_proved":False}


def _shift_moment(p,k):
    # Integral (y+1/2)^k p(y) dy exact.
    shifted_power=tuple(F(comb(k,j))*A**(k-j) for j in range(k+1))
    return definite(B.mul(p,shifted_power))


@lru_cache(maxsize=256)
def _convolution_powers(p,M):
    """Exact K_k(x)=integral_I |x-y|^k p(y) dy for all k<=M.

    K_1''=2p; K_k''=k(k-1)K_(k-2) for k>=2.
    Anchor values and one-sided derivatives at -1/2 are polynomial moments.
    This is an independent exact alternative to Suzuki's exp antiderivatives.
    """
    if type(M) is not int or not 0<=M<=192:
        raise OriginalResidualError("finite exact Gamma Taylor degree 0..192")
    k0=(definite(p),)
    if M==0:return (k0,)
    k1=B.add(B.add((_shift_moment(p,1),),
                   B.scale((A,F(1)),-definite(p))),
             B.scale(anchor_integral(anchor_integral(p)),2))
    out=[k0,k1]
    for k in range(2,M+1):
        prev=out[k-2]
        second=B.scale(anchor_integral(anchor_integral(prev)),k*(k-1))
        new=B.add(B.add(second,(_shift_moment(p,k),)),
                  B.scale((A,F(1)),-k*_shift_moment(p,k-1)))
        out.append(new)
    return tuple(out)


def gamma_ou_taylor_sum(p,J,M):
    """Exact polynomial approximation of the genuine finite Gamma OU sum."""
    if type(J) is not int or not 1<=J<=32:
        raise OriginalResidualError("original Gamma proof budget J=1..32")
    if type(M) is not int or not 16<=M<=192:
        raise OriginalResidualError("Gamma series degree 16..192")
    alpha=tuple(F(4*j+1,2) for j in range(J))
    coeff=[sum(((-v)**k for v in alpha),F(0))/factorial(k)
           for k in range(M+1)]
    terms=_convolution_powers(tuple(p),M)
    out=(F(0),)
    for k,pk in enumerate(terms):
        if coeff[k]:
            out=B.add(out,B.scale(pk,coeff[k]))
    # Taylor-Lagrange: 0<=s<=1, |R_M(e^(-alpha*s))|
    # <= (alpha*s)^(M+1)/(M+1)! (because derivative <=1).
    eps=sum((v**(M+1) for v in alpha),F(0))/factorial(M+1)
    return out,eps


def polar_taylor(P):
    if type(P) is not int or not 4<=P<=64:
        raise OriginalResidualError("genuine polar Taylor budget 4..64")
    c=tuple(F(1,2**k*factorial(k)) if k%2==0 else F(0)
            for k in range(P+1))
    s=tuple(F(1,2**k*factorial(k)) if k%2 else F(0)
            for k in range(P+1))
    # exp(±x/2), |x/2|<=1/4, and e^(1/4)<2.
    err=2*F(1,4)**(P+1)/factorial(P+1)
    return B.trim(c),B.trim(s),err


def source_parameters():
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from . import source_weil_hierarchy as src
    receipt=verify_original_suzuki_source()
    if receipt["source_git_blob"]!=SOURCE_SHA:
        raise OriginalResidualError("authentic frozen signed source SHA drift")
    if (src.authenticated_prime_wavefront(A)!=((2,2),)
        or src.real_prime_power(6) is not None):
        raise OriginalResidualError("fake original prime power event")
    b=src.log2_iv()
    w=b*src.sqrt_inverse(2)
    contact=src.contact_iv()
    if not F(5,8)<b.lo<=b.hi<F(3,4) or not F(0)<w.lo<=w.hi<F(1):
        raise OriginalResidualError("source prime2 normalization invalid")
    def snap(v,den=10**12):
        raw=v.mid()*den
        n=(raw+F(1,2)).numerator//(raw+F(1,2)).denominator
        v0=F(n,den)
        return v0,max(abs(v.lo-v0),abs(v.hi-v0))
    b0,db=snap(b)
    w0,dw=snap(w)
    c0,dc=snap(contact)
    return {"b":b0,"db":db,"w":w0,"dw":dw,
            "contact":c0,"dc":dc,
            "sha":receipt["source_git_blob"],"real_gamma_count":1,
            "half_density":"1/2","snap_denominator":10**12}


def exact_piecewise_primitive_action(h,J=8,M=80,P=18,parameters=None):
    """Full source H_J h via a Fraction-valued piecewise polynomial + error.

    c_J h - sum E_alpha_j h - C h - (log2/sqrt2) A_b h
    + 2<c,h>c - 2<s,h>s.
    Error includes all authentic source-parameter interval uncertainties,
    true prime-shift lag (L2 translation Lipschitz) and Taylor remainders.
    """
    h=tuple(rat(v) for v in h)
    if not h or norm_squared(h)<=0:
        raise OriginalResidualError("nonzero exact polynomial primitive")
    params=source_parameters() if parameters is None else parameters
    b=params["b"];w=params["w"];C=params["contact"]
    if not A<b<1 or any(type(params[z]) is not F for z in
                         ("db","dw","dc")):
        raise OriginalResidualError("no unlicensed source parameters")
    ou,ou_error=gamma_ou_taylor_sum(h,J,M)
    c,s,polar_error=polar_taylor(P)
    polar=B.add(B.scale(c,2*B.integral_product(c,h)),
                B.scale(s,-2*B.integral_product(s,h)))
    scalar=sum((F(4,4*j+1) for j in range(J)),F(0))-C
    common=B.add(B.add(B.scale(h,scalar),B.scale(ou,-1)),polar)
    pieces=((-A,A-b,B.add(common,B.scale(shifted(h,b),-w))),
            (A-b,b-A,common),
            (b-A,A,B.add(common,B.scale(shifted(h,-b),-w))))
    # ||c||,||s|| <=2 by cosh(1/4)<2. Rank-one perturbation
    # ||2(cc*-cc_M*)-2(ss*-ss_M*)|| <=4*eps*(4+eps).
    source_error=(ou_error+params["dc"]+params["dw"]
                  +4*polar_error*(4+polar_error))*B.sqrt_up(norm_squared(h))
    # Full translations on the zero-extended H1_0 carrier are Lipschitz.
    source_error+=2*abs(w)*params["db"]*B.sqrt_up(derivative_norm_squared(h))
    return {"pieces":pieces,"finite_source_action_error_upper":source_error,
        "Gamma_kernel_Taylor_upper":ou_error,
        "pole_Taylor_upper":polar_error,
        "source_parameters":params,"J":J,"M":M,"P":P,
        "frozen_source_SHA":params["sha"],"RH_proved":False}


def _integrate_piece_pair(a,b):
    # Partition endpoints are source b0, so both piece sets match.
    if len(a)!=len(b):
        raise OriginalResidualError("piecewise source partition mismatch")
    return sum((definite(B.mul(x[2],y[2]),x[0],x[1])
                for x,y in zip(a,b)
                if x[0]==y[0] and x[1]==y[1]),F(0))


def projected_piece_moments(pieces):
    return tuple(sum((definite(B.mul(p,B.legendre(k)),l,r)
                      for l,r,p in pieces),F(0))
                 for k in range(4))


def projected_piece_gram(p,q):
    if tuple((z[0],z[1]) for z in p)!=tuple((z[0],z[1]) for z in q):
        raise OriginalResidualError("different source b partition")
    m=projected_piece_moments(p)
    n=projected_piece_moments(q)
    return _integrate_piece_pair(p,q)-sum((F(2*k+1)*a*b
                for k,(a,b) in enumerate(zip(m,n))),F(0))


def safe_ratio_round(n,d,denom=4096,bound=F(8)):
    n,d=rat(n),rat(d)
    if d<=0 or type(denom) is not int or denom<1 or bound<=0:
        raise OriginalResidualError("positive response scalar denominator")
    # Symmetric nearest-integer deterministic rational model selector.
    x=max(-bound,min(bound,n/d))
    if x>=0:y=F((x*denom+F(1,2)).numerator//(x*denom+F(1,2)).denominator,denom)
    else:y=-F(((-x)*denom+F(1,2)).numerator//((-x)*denom+F(1,2)).denominator,denom)
    return y


def fit_high_coefficients(J=8,M=80,P=18):
    """Fit only on source-authenticated FINITE Gamma H_J action; validate later."""
    params=source_parameters()
    clamped={}
    for name,model in B.CLAMPED.items():
        clamped[name]=exact_piecewise_primitive_action(model["poly"],J,M,P,params)
    fitted={}
    for i in (1,2,3,4):
        baseline=high_boundary_match(i,F(0))
        piece=exact_piecewise_primitive_action(baseline["h"],J,M,P,params)
        candidate=clamped[clamped_name(i)]
        num=projected_piece_gram(piece["pieces"],candidate["pieces"])
        den=projected_piece_gram(candidate["pieces"],candidate["pieces"])
        t=safe_ratio_round(num,den)
        fitted[i]=t
    return fitted


def _actual_signed_interval(coeff_a,coeff_b,J,entry_cache):
    from .suzuki_legendre_source import authentic_full_low_entry
    lo=hi=F(0)
    for i,ci in coeff_a:
        for j,cj in coeff_b:
            if (i,j) not in entry_cache:
                entry_cache[(i,j)]=authentic_full_low_entry(i,j,A,J)
            entry=entry_cache[(i,j)]
            z=ci*cj
            lo+=z*(entry.lo if z>=0 else entry.hi)
            hi+=z*(entry.hi if z>=0 else entry.lo)
    return lo,hi



def frozen_operator_matrix_holdout(J=4,M=56,P=18):
    """Independent ARCHIVED exp source vs Taylor-moment continuum action.

    Exact integrated polynomial pairing, with a charged L2 source error.
    This compares all original prime/Gamma/contact/both-pole channels.
    """
    params=source_parameters()
    sample=[
      ("P1_P1",1,1),
      ("P1_P5",1,5),
      ("P5_P5",5,5),
      ("P2_P2",2,2),
      ("P2_P6",2,6),
      ("P1_P3",1,3),
    ]
    cache={}
    action_cache={}
    results={}
    for tag,i,j in sample:
        ha=anchor_integral(B.legendre(i))
        hb=anchor_integral(B.legendre(j))
        if any(B.value(p,end)!=0 for p in (ha,hb) for end in (-A,A)):
            raise OriginalResidualError("source zero-extended primitive H1 trace")
        if j not in action_cache:
            action_cache[j]=exact_piecewise_primitive_action(hb,J,M,P,params)
        packet=action_cache[j]
        nominal=sum((definite(B.mul(ha,p),l,r)
                     for l,r,p in packet["pieces"]),F(0))
        action_error=B.sqrt_up(norm_squared(ha))*packet["finite_source_action_error_upper"]
        original=_actual_signed_interval(((i,F(1)),),((j,F(1)),),J,cache)
        if original[0]>nominal+action_error or original[1]<nominal-action_error:
            raise ArithmeticError("FROZEN ORIGINAL signed matrix and independently derived true primitive H_J action disagree: "+tag)
        results[tag]={"original_sha":params["sha"],
           "signed_original_interval":tuple(map(str,original)),
           "independent_action_pair":str(nominal),
           "rigorous_action_pair_error_upper":str(action_error),
           "independent_enclosures_intersect":True}
    return {"original_source_sha":params["sha"],"J":J,"M":M,
        "all_original_signed_channels_tested":True,
        "independent_exp_matrix_vs_Taylor_continuum_action":results,
        "RH_proved":False}


def source_residual_schur_trial(J=8,M=80,P=18,fit=True,eta=F(1,4)):
    """Full source-authentic FOUR-mode Schur Loewner lower.

    Full true residual is ||Q H_infty h_i|| <=
      ||Q approximate H_J h_i|| + finite-action-error
                                 + genuine H2_0 Gamma action tail.
    Source q_infty(h)>=q_J(h) since omitted real Gamma rungs PSD.
    For each parity block, Young + Cauchy control joint residual
    Gram by (1+eta) M +(1+1/eta)sum(delta_i²)I; source κ by parity.
    A negative lower certificate remains AMBIGUOUS, not negative Weil.
    """
    eta=rat(eta)
    if eta<=0:raise OriginalResidualError("valid positive Young parameter")
    if J<1 or J>24:raise OriginalResidualError("bounded finite original trial J")
    params=source_parameters()
    fitted=fit_high_coefficients(J,M,P) if fit else {i:F(0) for i in (1,2,3,4)}
    inputs={}
    entry_cache={}
    for i in (1,2,3,4):
        obj=high_boundary_match(i,fitted[i])
        x=exact_piecewise_primitive_action(obj["h"],J,M,P,params)
        projected_sq=projected_piece_gram(x["pieces"],x["pieces"])
        if projected_sq<0:
            raise ArithmeticError("exact projected primitive norm must be PSD")
        finiteerr=x["finite_source_action_error_upper"]
        tail=B.gamma_action_tail(J)*B.sqrt_up(obj["second_derivative_norm_sq"])
        budget=B.sqrt_up(projected_sq)+finiteerr+tail
        inputs[i]={"h":obj,"approx":x,"residual":budget,
            "finite_residual_norm_squared":projected_sq,
            "finite_source_error":finiteerr,"gamma_full_tail_action":tail}
    results={}
    for parity,indices,kappa in (
        ("odd_derivative",(1,3),F(63,500)),
        ("even_derivative",(2,4),F(153,500))):
        # source block q_J(h_i,h_j) with outward interval arithmetic
        pairs=[[_actual_signed_interval(inputs[i]["h"]["derivative_coeff"],
                                         inputs[j]["h"]["derivative_coeff"],
                                         J,entry_cache)
               for j in indices] for i in indices]
        if not all(max(pairs[i][j][0],pairs[j][i][0])
                   <=min(pairs[i][j][1],pairs[j][i][1])
                   for i in range(2) for j in range(2)):
            raise ArithmeticError("original signed source symmetry intervals do not meet")
        mid=[[sum(pairs[i][j])/2 for j in range(2)] for i in range(2)]
        rad=[[(pairs[i][j][1]-pairs[i][j][0])/2
              for j in range(2)] for i in range(2)]
        qm=[[projected_piece_gram(inputs[i]["approx"]["pieces"],
                                   inputs[j]["approx"]["pieces"])
             for j in indices] for i in indices]
        epssq=sum(((inputs[i]["finite_source_error"]+inputs[i]["gamma_full_tail_action"])**2
                   for i in indices),F(0))
        lower=[[
            mid[a][b]-(sum(rad[a]) if a==b else F(0))-
            ((1+eta)*qm[a][b]+
             ((1+1/eta)*epssq if a==b else F(0)))/kappa
            for b in range(2)] for a in range(2)]
        if lower[0][1]!=lower[1][0]:
            raise ArithmeticError("exact signed 2x2 Schur lower asymmetry")
        sign=(lower[0][0]>=0 and lower[1][1]>=0
              and lower[0][0]*lower[1][1]>=lower[0][1]**2)
        results[parity]={"indices":indices,"source_kappa":str(kappa),
            "fitted_high_coefficients":tuple(str(fitted[i]) for i in indices),
            "genuine_signed_qJ_intervals":tuple(tuple(
                 tuple(map(str,pairs[a][b])) for b in range(2)) for a in range(2)),
            "surrogate_QE_action_residual_gram_exact":
                tuple(tuple(str(qm[a][b]) for b in range(2)) for a in range(2)),
            "combined_residual_norm_upper_each":
                tuple(str(inputs[i]["residual"]) for i in indices),
            "genuine_source_2x2_Schur_Loewner_lower":
                tuple(tuple(str(lower[a][b]) for b in range(2)) for a in range(2)),
            "source_Schur_lower_PSD_certified":bool(sign),
            "trial_is_in_original_high_domain":True}
    return {"frozen_source_git_blob":params["sha"],
        "authentic_first_prime_wavefront":((2,2),),
        "one_real_Gamma_contact_two_completed_poles":True,
        "source_J":J,"finite_Gamma_Taylor_M":M,"polar_Taylor_P":P,
        "source_clamped_H2_0_boundary_matching":True,
        "original_high_kappa_relative_to_K":("63/500","153/500"),
        "four_original_parity_Schur_blocks":results,
        "exact_source_matrix_entries_evaluated":len(entry_cache),
        "all_four_source_S4_sign_certified":all(r["source_Schur_lower_PSD_certified"]
                                     for r in results.values()),
        "RH_proved":False}
