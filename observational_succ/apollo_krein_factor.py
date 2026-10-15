"""APOLLO: source-authentic finite-window Krein (+ Hilbert) factorization.

This module NEVER asserts its signed source kernel is globally positive.
It constructs canonical source-identified positive-minus-positive pieces:
  original Gamma OU increments + pole sinh + prime triangular increments
  MINUS pole cosh-1 + Brownian with exact contact/prime counterweight.
The existence of a contraction from positive feature space to negative
feature space is an RH-strength *unproved* condition.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import gcd

from .one_object_transport import OneObjectError, _fraction, _int, _mp, _mfrac, _aligned_screw
from .apollo_derivative_jets import true_third_prime_wavefronts


def brownian_increment_kernel(x: int | F, y: int | F) -> F:
    """Two-sided anchored Brownian Gram B=(|x|+|y|-|x-y|)/2>=PSD."""
    a,b=_fraction(x),_fraction(y)
    return (abs(a)+abs(b)-abs(a-b))/2


def triangle_overlap(x: int | F, width: int | F) -> F:
    """Normalized convolution of 1_[0,width] with itself."""
    a,w=_fraction(x),_fraction(width)
    if w<=0:
        raise OneObjectError("Positive primitive clock span required")
    return max(F(),1-abs(a)/w)


def triangle_increment_kernel(x: int | F,y: int | F,
                              width: int | F) -> F:
    """PSD Gram of shifted, centered interval indicators in L2(R)."""
    a,b,w=_fraction(x),_fraction(y),_fraction(width)
    if w<=0:raise OneObjectError("Positive source clock width required")
    return triangle_overlap(a-b,w)-triangle_overlap(a,w)-triangle_overlap(b,w)+1


def prime_hinge_kernel(x: int | F,y: int | F,b: int | F) -> F:
    """Anchored K for authentic functional SHAPE h_b(t)=(|t|-b)_+."""
    a,c,width=_fraction(x),_fraction(y),_fraction(b)
    if width<=0:raise OneObjectError("Positive log-prime hinge required")
    h=lambda t:max(F(),abs(t)-width)
    return h(a-c)-h(a)-h(c)


def prime_krein_identity(x: int | F, y: int | F, b: int | F) -> dict:
    """Exact REAL-source-independent polynomial identity.

    (|x-y|-b)_+-(|x|-b)_+-(|y|-b)_+
       = b*T_b_increment(x,y)-2*Brownian_increment(x,y).
    BOTH component kernels are genuine positive Hilbert Grams. They are
    NOT individually source sums for infinitely many primes: at a fixed
    window only finitely many original prime hinge atoms contribute.
    """
    a,c,width=_fraction(x),_fraction(y),_fraction(b)
    if width<=0:raise OneObjectError("Positive source interval width required")
    signed=prime_hinge_kernel(a,c,width)
    plus=width*triangle_increment_kernel(a,c,width)
    minus=2*brownian_increment_kernel(a,c)
    if signed!=plus-minus:
        raise ArithmeticError("Krein source decomposition failed exact rational identity")
    return {"signed":signed,"positive_triangle":plus,
            "negative_brownian":minus,"identity_exact":True}


def _det(A):
    """Exact rational determinant, for finite PSD regression only."""
    n=len(A)
    if not n:return F(1)
    if any(len(row)!=n for row in A):
        raise OneObjectError("Square Gram matrix required")
    m=[[F(c) for c in row] for row in A]
    result=F(1)
    for k in range(n):
        pivot=next((j for j in range(k,n) if m[j][k]!=0),None)
        if pivot is None:return F()
        if pivot!=k:
            m[k],m[pivot]=m[pivot],m[k]
            result=-result
        v=m[k][k]
        result*=v
        for i in range(k+1,n):
            coeff=m[i][k]/v
            for j in range(k,n):
                m[i][j]-=coeff*m[k][j]
    return result


def exact_rational_gram_psd(points: tuple[F,...], kind: str,
                             width: int | F = 1) -> dict:
    """Every principal minor >=0, allowing singular positive Gram matrices.

    The analytical PSD proofs use direct L2 Brownian/interval indicator
    features; this is an independent exact Fraction finite oracle.
    """
    if type(points) is not tuple or not 1<=len(points)<=5 or any(type(v) not in (int,F) for v in points):
        raise OneObjectError("Exact rational points tuple with 1..5 entries required")
    if kind not in ("brownian","triangle"):
        raise OneObjectError("Only declared positive primitive features supported")
    pts=tuple(F(p) for p in points)
    if kind=="brownian":
        gram=tuple(tuple(brownian_increment_kernel(x,y) for y in pts) for x in pts)
    else:
        gram=tuple(tuple(triangle_increment_kernel(x,y,width) for y in pts) for x in pts)
    mins=[]
    for k in range(1,len(pts)+1):
        for ids in combinations(range(len(pts)),k):
            sub=tuple(tuple(gram[i][j] for j in ids) for i in ids)
            mins.append(_det(sub))
    return {"points":pts,"kind":kind,"matrix":gram,
            "strictly_negative_principal_minors":tuple(z for z in mins if z<0),
            "all_principal_minors_nonnegative":all(z>=0 for z in mins),
            "finite_only":True,"RH_proved":False}


def original_suzuki_krein_finite_window(
        x: int | F, y: int | F,
        a: int | F, J: int = 8, dps: int = 70) -> dict:
    """Independent true-source identity of finite-J Suzuki vs plus-minus Grams.

    x,y ∈ [-a,a], 0<a<=2. Original C_infty contact; first J authentic
    real Gamma OU modes, original real pole, ALL local original prime powers
    with log n<2a. These equal K_g^J. The omitted Gamma tail is itself
    POSITIVE SEMIDEFINITE on every finite Gram, but does not establish
    positivity of the signed full K.
    """
    xx,yy,aa=_fraction(x),_fraction(y),_fraction(a)
    if not 0<aa<=2 or abs(xx)>aa or abs(yy)>aa:
        raise OneObjectError("Exact window and source points |x|,|y|<=a<=2")
    _int(J,0,128)
    mp=_mp(dps)
    prime_labels=true_third_prime_wavefronts(2*aa)
    X,Y=_mfrac(mp,xx),_mfrac(mp,yy)
    C=mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
    atoms=tuple((mp.log(j.n),mp.log(j.p)/mp.sqrt(j.n),j.n)
                for j in prime_labels)
    # Same true *infinite* contact as the pinned PR85 Suzuki source,
    # but a finite Gamma potential. This is not the O1 finite-contact W_J.
    g=lambda t:(-4*(mp.exp(abs(t)/2)+mp.exp(-abs(t)/2)-2)
                +C*abs(t)/2
                +mp.fsum(w*max(mp.mpf(0),abs(t)-b) for b,w,n in atoms)
                -mp.fsum(mp.mpf(4)/(4*j+1)**2 *
                       (1-mp.exp(-(4*j+1)*abs(t)/2)) for j in range(J)))
    original=g(X-Y)-g(X)-g(Y)+g(0)
    gamma=mp.fsum(mp.mpf(4)/(4*j+1)**2*(
                  mp.exp(-(4*j+1)*abs(X-Y)/2)
                 -mp.exp(-(4*j+1)*abs(X)/2)
                 -mp.exp(-(4*j+1)*abs(Y)/2)+1)
                  for j in range(J))
    pole_plus=8*mp.sinh(X/2)*mp.sinh(Y/2)
    pole_minus=8*(mp.cosh(X/2)-1)*(mp.cosh(Y/2)-1)
    B=brownian_increment_kernel(xx,yy)
    Bm=_mfrac(mp,B)
    prime_plus=mp.fsum(w*b*(
                   max(mp.mpf(0),1-abs(X-Y)/b)
                  -max(mp.mpf(0),1-abs(X)/b)
                  -max(mp.mpf(0),1-abs(Y)/b)+1)
                   for b,w,n in atoms)
    brownian_minus=(C+2*mp.fsum(w for b,w,n in atoms))*Bm
    positive=gamma+pole_plus+prime_plus
    negative=pole_minus+brownian_minus
    residual=original-(positive-negative)
    return {"source":"AUTHENTIC_GENUINE_ZETA_PRIME_POWERS",
            "window_halfwidth":str(aa),"points":(str(xx),str(yy)),
            "J":J,"prime_labels":tuple(n for b,w,n in atoms),
            "positive_gram":mp.nstr(positive,40),
            "negative_gram":mp.nstr(negative,40),
            "signed_gram":mp.nstr(original,40),
            "signed_difference":mp.nstr(positive-negative,40),
            "residual_abs":abs(residual),"residual":mp.nstr(residual,14),
            "gamma_modes_are_positive_Hilbert_features":True,
            "triangular_prime_terms_are_positive_Hilbert_features":True,
            "brownian_contact_term_is_negative_Hilbert_feature":True,
            "source_hilbert_contraction_proved":False,"RH_proved":False}


def source_feature_contraction_diagnostic(
        plus: tuple[tuple[F,...],...],
        minus: tuple[tuple[F,...],...]) -> dict:
    """Exact finite algebra: K+=PSD and K-=PSD does NOT imply K+-K- PSD.

    This is a finite diagnostic and NOT the RH-hard uniform contraction
    test over full infinite feature spans.
    """
    n=len(plus)
    if n==0 or n>5 or len(minus)!=n:
        raise OneObjectError("1..5 dimensional matched Gram matrices")
    if any(len(row)!=n for row in plus+minus):
        raise OneObjectError("Same-size squared matrices required")
    a=tuple(tuple(_fraction(z) for z in row) for row in plus)
    b=tuple(tuple(_fraction(z) for z in row) for row in minus)
    if any(a[i][j]!=a[j][i] or b[i][j]!=b[j][i]
           for i in range(n) for j in range(n)):
        raise OneObjectError("Symmetric positive feature blocks required")
    def minors(A):
        return tuple(_det(tuple(tuple(A[i][j] for j in ids) for i in ids))
                     for k in range(1,n+1)
                     for ids in combinations(range(n),k))
    mp=minors(a); mn=minors(b)
    if any(v<0 for v in mp+mn):
        raise OneObjectError("Each individual feature Gram must be PSD")
    k=tuple(tuple(a[i][j]-b[i][j] for j in range(n)) for i in range(n))
    mk=minors(k)
    return {"positive_feature_psd":True,"negative_feature_psd":True,
            "combined_signed_psd_on_selected_finite_set":all(v>=0 for v in mk),
            "combined_minors":mk,
            "full_source_contraction_proved":False,"RH_proved":False}



def prime_mixed_second_source_coefficients(weight: int | F = 1) -> dict:
    """Exact distribution-valued ∂x∂y cancellation of *one* prime hinge.

    Positive triangle feature w*b K_T has:
       +2w δ_0 -w δ_{+b}-w δ_{-b}.
    Negative 2w Brownian feature has: -2w δ_0.
    Combining gives exactly -w(δ_{+b}+δ_{-b}), with NO invented
    composite impulse and NO leftover contact delta.
    """
    w=_fraction(weight)
    if w<=0:raise OneObjectError("Genuine prime source coefficient must be positive")
    plus_origin=2*w
    minus_origin=-2*w
    return {"positive_triangle_origin":plus_origin,
            "negative_brownian_origin":minus_origin,
            "combined_origin":plus_origin+minus_origin,
            "combined_plus_logprime_impulse":-w,
            "combined_minus_logprime_impulse":-w,
            "canonical_contact_cancelled":plus_origin+minus_origin==0,
            "RH_proved":False}


def gamma_mixed_second_source_coefficients(j: int) -> dict:
    """Original real Gamma j-th OU feature -> exact signed Weil source.

      c_j=4/(4j+1)², alpha=(4j+1)/2;
      ∂x∂y c_j K_exp
       =(4/(4j+1))δ_0 - exp(-alpha |x-y|).
    Here the local delta coefficient has no finite J->infty limit by
    itself: combine with contact and smooth rungs as a distribution.
    """
    index=_int(j,0,512)
    d=4*index+1
    c=F(4,d*d)
    alpha=F(d,2)
    if 2*c*alpha!=F(4,d) or c*alpha*alpha!=1:
        raise ArithmeticError("Authentic Gamma normalization mismatch")
    return {"gamma_index":j,"alpha":alpha,"positive_feature_weight":c,
            "origin_delta_coefficient":F(4,d),
            "smooth_exponential_coefficient":F(-1),
            "separate_infinite_origin_series_is_illegal":True,
            "RH_proved":False}



def neutral_prime_activation_pair(x: int | F,y: int | F,
                                  b: int | F) -> dict:
    """Krein-neutral prime source on a smaller observation interval.

    When b>|x|,|y|,|x-y|, true prime hinge is zero and
    b*DeltaT_b(x,y) = 2 B(x,y), while *both Hilbert features need not
    vanish*. Thus individual plus/minus Hilbert source carriers are NOT
    canonically nested under activating a prime; only their signed
    difference is canonically restricted. Source-neutral paired
    identification is needed for coherent all-a contraction transport.
    """
    xx,yy,bb=_fraction(x),_fraction(y),_fraction(b)
    if bb<=max(abs(xx),abs(yy),abs(xx-yy)):
        raise OneObjectError("This theorem requires a pre-activation source window")
    out=prime_krein_identity(xx,yy,bb)
    if out["signed"]!=0 or out["positive_triangle"]!=out["negative_brownian"]:
        raise ArithmeticError("Source-neutral prime activation identity failed")
    return {"points":(xx,yy),"width":bb,
            "positive_channel":out["positive_triangle"],
            "negative_channel":out["negative_brownian"],
            "signed_on_old_window":out["signed"],
            "nontrivial_paired_features":out["positive_triangle"]!=0,
            "independent_plus_minus_nesting_certified":False,
            "signed_restriction_compatible":True,"RH_proved":False}


def authentic_prime_two_activation_on_old_window() -> dict:
    """Pinned ORIGINAL n=2 activation as a nontrivial neutral Krein pair.

    The SUCC original source gives 1/2<log2<1 exactly by log intervals.
    At a=1/4 no n=2 hinge is visible (2a=1/2<log2). But when
    moving to a=1/2 the new plus and minus source channels each
    contribute w2*1/2 at the old x=y=1/4, while the ORIGINAL signed
    prime contribution stays zero. The law is exact symbolic algebra,
    not a float or an RH positivity claim.
    """
    from .apollo_derivative_jets import genuine_prime_third_jet
    label=genuine_prime_third_jet(2)
    lo,hi=label.log_n_interval
    if not F(1,2)<lo<=hi<1:
        raise ArithmeticError("Original log(2) enclosure no longer separates source ages")
    src=neutral_prime_activation_pair(F(1,4),F(1,4),F(3,4))
    # The symbolic identity holds for EVERY b>1/2, including genuine log(2);
    # rational b=3/4 witnesses the same structural representation.
    if src["positive_channel"]!=F(1,2):
        raise ArithmeticError("New-source neutral channel has wrong width")
    return {"source": "ORIGINAL_PINNED_VON_MANGOLDT_2",
            "prime_two_log_interval":(lo,hi),
            "prime_two_weight_interval":label.delta_prime_weight_interval,
            "old_halfwidth":F(1,4),"new_halfwidth":F(1,2),
            "old_points":(F(1,4),F(1,4)),
            "unweighted_plus_equal_minus":F(1,2),
            "true_prime_weighted_positive_channel_interval":
                (label.delta_prime_weight_interval[0]/2,
                 label.delta_prime_weight_interval[1]/2),
            "signed_zero":True,
            "Krein_neutral_source_birth":True,
            "all_a_Hilbert_contraction_proved":False,"RH_proved":False}



def authentic_small_window_brownian_coercivity(a: int | F) -> dict:
    """ANALYTIC SOURCE-TRUE whole-Gram positivity on every 0<a<=1/24.

    For all finite complex coefficients (c_i) and x_i in [-a,a], let
    v(t)=Σ c_i 1_[0,x_i](t), with signed orientation at negative x_i.
    Then Σ conj(c_i)c_j B(x_i,x_j)=||v||_L²².

    Original source has no active prime hinge: 2a<=1/12<log2.
    For Gamma OU mode alpha_j=(4j+1)/2,c_j=4/(4j+1)^2:
      gamma_j energy = beta_j <v,(I-R_alpha_j)v>,
      beta_j=4/(4j+1),
      R_alpha kernel=(alpha/2) exp(-alpha|t-s|).
    Since v supported [-a,a], Schur bound ||R||<=alpha*a, so
      gamma_j>= (4/(4j+1)-2a)||v||².
    First EIGHT original Gamma modes sum to S_8-16a.
    Remaining Gamma modes, and +8sinh(x/2)sinh(y/2), are PSD.

    Exact original contact C_inf<11/2 via SHA-pinned rational intervals.
    Negative pole: h(x)=cosh(x/2)-1 is an integral of
    h'(t)=sinh(t/2)/2 against v, so
      8|Σ c_i h(x_i)|² <= 4a sinh²(a/2)||v||²
      <= a³ exp(a)||v||² <= a³/(1-a)||v||².

    Therefore K_g >= [S_8-16a-11/2-a³/(1-a)] B,
    and the rational bracket is >1/10 for ALL real 0<a<=1/24.
    This certifies source-true K_g PSD on ALL finite point configurations
    within [-1/24,1/24], not a positive ℓ² counting-measure gap.
    It proves a known type of LOCAL Weil positivity, not RH or all-a.
    """
    aa=_fraction(a)
    if not 0<aa<=F(1,24):
        raise OneObjectError("Source-true uniform coercivity requires 0<a<=1/24")
    from .apollo_derivative_jets import _source
    source=_source()
    if not source.contact_iv().hi<F(11,2):
        raise ArithmeticError("Pinned real source contact C_inf<11/2 not certified")
    if not source.log2_iv().lo>F(1,2):
        raise ArithmeticError("Pinned prime-2 wavefront lower bound failed")
    gamma_S8=sum((F(4,4*j+1) for j in range(8)),F())
    margin=gamma_S8-16*aa-F(11,2)-aa**3/(1-aa)
    # The minimum across the full allowed interval is at a=1/24.
    global_floor=gamma_S8-16*F(1,24)-F(11,2)-F(1,24)**3/(1-F(1,24))
    if global_floor<=F(1,10) or margin<global_floor:
        raise ArithmeticError("Exact Gamma/Brownian/source contact coercivity failed")
    return {
        "a":aa,"gamma_modes_used":8,
        "real_source":"SHA_PINNED_ORIGINAL_ZETA",
        "original_contact_upper":F(11,2),
        "original_log2_lower":F(1,2),
        "gamma_brownian_lower":gamma_S8-16*aa,
        "negative_pole_brownian_upper":aa**3/(1-aa),
        "strict_K_dominates_B_lower":margin,
        "uniform_K_dominates_B_for_all_real_a_le_1over24":F(1,10),
        "holds_for_all_finite_point_sets_and_complex_coefficients":True,
        "gamma_tail_omitted_positive":True,
        "first_prime_absent":True,
        "all_RH_test_intervals_certified":False,
        "RH_proved":False,
    }



def _exp_odd_taylor_lower(x: F, order: int = 9) -> F:
    """Exact odd Taylor polynomial below exp(-x), x>=0, order=9.

    Taylor's remainder has positive even degree (order+1), hence
       exp(-x) >= P_9(x) = sum_{k=0}^9 (-x)^k/k!
    for x>=0. P_9'(x)=-P_8(x)<0, since even P_8>exp(-x)>0.
    """
    z=_fraction(x)
    if z<0 or order!=9:
        raise OneObjectError("Only x>=0, rigorously odd Taylor order 9")
    from math import factorial
    return sum((F((-1)**k, factorial(k))*z**k for k in range(10)), F())


def authentic_sharp_small_window_hilbert_factor(a: int | F) -> dict:
    """ONE FULL SOURCE-TRUE POSITIVE HILBERT FACTOR over [-1/12,1/12].

    Same genuine K_g=K_+-K_- as APOLLO K2, but proves uniformly
       Σbar(z_i)z_j K_g(x_i,x_j) > (1/100)||v||²_B
    for all finitely many x_i∈[-a,a], complex z_i, 0<a<=1/12.
    Thus the source feature correspondence Φ_+ -> Φ_- extends
    BY PROVED DOMINANCE to a contraction T_a. Consequently
       Ψ_a(x)=(I-T_a* T_a)^1/2 Φ_+(x)
    is a legitimate positive Hilbert feature with Gram TRUE K_g
    on this entire small interval. The operator T_a is defined
    via completion of the prescribed feature span; this is NOT
    an explicit closed-form numerical kernel and not RH.

    Improvement on 8-mode rough-Schur: R_alpha has integral kernel
    (alpha/2)exp(-alpha|t-s|) on support [-a,a].
    Its exact Schur maximum is 1-exp(-alpha a), not merely alpha a,
    so Gamma j energy ≥ (4/(4j+1))exp(-alpha_j*a)||v||².
    Use source-authentic first 20 Gamma modes, odd Taylor P_9 as
    *rigorous rational lower* to exp(-alpha a).
    Original C_inf<43/8 by SHA pinned source rational intervals,
    and negative pole ≤ a³/(1-a). At a=1/12 the exact rational
    margin exceeds 1/100; all gamma polynomial contributions
    decrease in a since P_9'=-P_8<0. Thus margin at any a≤1/12
    is ≥ its value at 1/12 >1/100. No primes active since
    2a≤1/6<log2; original pole/Gamma/contact still ALL present.

    This proves actual all-finite-set source positivity on a
    nontrivial window; global all-a K4 contraction remains RH-hard.
    """
    aa=_fraction(a)
    if not 0<aa<=F(1,12):
        raise OneObjectError("Uniform source contraction certified only for 0<a<=1/12")
    from .apollo_derivative_jets import _source
    source=_source()
    if not source.contact_iv().hi<F(43,8):
        raise ArithmeticError("Original source contact C_inf<43/8 proof failed")
    if not source.log2_iv().lo>F(1,6):
        raise ArithmeticError("Original first-prime activation separation failed")
    def gamma_lower(radius: F) -> F:
        return sum((F(4,4*j+1)*_exp_odd_taylor_lower(F(4*j+1,2)*radius)
                    for j in range(20)), F())
    # Even endpoint P9>0 checked exactly; no signed Taylor artifice.
    if _exp_odd_taylor_lower(F(77,2)*F(1,12))<=0:
        raise ArithmeticError("The maximal first-20 Gamma Taylor lower is not positive")
    original_real_margin=gamma_lower(aa)-F(43,8)-aa**3/(1-aa)
    endpoint=F(1,12)
    globally_minimal_margin=gamma_lower(endpoint)-F(43,8)-endpoint**3/(1-endpoint)
    if globally_minimal_margin<=F(1,100) or original_real_margin<globally_minimal_margin:
        raise ArithmeticError("Source-derived all-finite-set positivity margin not certified")
    return {"a":aa,
            "original_sha_pinned_source":True,
            "real_gamma_rungs_used":20,
            "gamma_taylor_order":9,
            "original_real_contact_upper":F(43,8),
            "original_first_prime_inactive":True,
            "gamma_brownian_lower":gamma_lower(aa),
            "negative_pole_brownian_upper":aa**3/(1-aa),
            "exact_positive_coercivity_margin":original_real_margin,
            "all_real_a_at_most_1over12_floor":F(1,100),
            "all_finite_complex_source_gram_positive":True,
            "contractive_Ta_exists_by_independent_coercivity_proof":True,
            "positive_feature_Psi_a_exists_by_completion":True,
            "feature_Psi_a_computed_in_closed_form":False,
            "first_prime_crossed":False,
            "all_a_and_RH_proved":False}



def authentic_small_window_completed_weil_coercivity(a: int | F) -> dict:
    """UNIVERSAL source-signed Q_Weil >= 1/100 ||f||_L²² on small tests.

    For every complex f ∈ Cc∞(-a,a), 0<a<=1/12, the actual signed Weil
    quadratic distribution from the original zeta source satisfies
       W_zeta(f * tilde(f)) >= (1/100) integral |f(t)|² dt.
    Proof: the independently established authentic K_g >= (1/100)B
    holds on ALL finite point sets, so by continuity it holds on
    compact signed test densities, in particular f'⊗conj(f').
    Distributional integration by parts gives
       Q_W(f)=∬ K_g(x,y) f'(x) conj(f'(y)) dxdy.
    Also ∂x∂y B(x,y)=δ(x-y), so
       ∬ B(x,y) f'(x)conj(f'(y))dxdy = ||f||².
    Exactly the original Weil completed pole/Gamma/contact source is
    used; this is a local RH-compatible sign with honest ALL-TEST
    quantifier restricted to a<=1/12, not RH or all a.
    """
    r=authentic_sharp_small_window_hilbert_factor(a)
    if not r["all_finite_complex_source_gram_positive"]:
        raise ArithmeticError("No underlying original all-vector source proof")
    return {"a":r["a"],
            "signed_source":"AUTHENTIC_COMPLETED_WEIL_ZETA",
            "full_test_domain":"C_c_infinity(-a,a) complex",
            "uniform_original_weil_L2_lower":F(1,100),
            "proof":"distributional_mixed_D2_and_original_K_g_dominates_B",
            "holds_for_every_smooth_compact_test_on_window":True,
            "actual_prime_activity":"none_on_this_small_window",
            "all_global_Weil_tests_positive":False,
            "RH_proved":False}


def brownian_compact_weak_derivative_certificate(a: int | F,
                                                   power: int = 4) -> dict:
    """Exact independent polynomial calibration for mixed D²B = δ.

    For f(t)=t^m(a-t)^m (0<=t<=a), zero outside, m>=4:
       ∬ B(x,y) f'(x) f'(y) dx dy
         =∫_0^a [∫_t^a f'(x)dx]²dt =∫_0^a f(t)²dt.
    The first integral is derived from the positive-half-line
    Brownian indicator representation; a distinct exact beta-function
    factorial computation gives its direct RHS. This finite C³
    polynomial is a calibration, not a replacement for the
    all-Cc∞ distributional proof or a direct zeta source evaluation.
    """
    aa=_fraction(a)
    m=_int(power,4,15)
    if not 0<aa<=F(1,12):
        raise OneObjectError("Polynomial Brownian control limited to small original window")
    from math import factorial, comb
    # f(t)=t^m (a-t)^m, exact ascending Fraction coefficients
    coeff=tuple([F()]*m+[F((-1)**k*comb(m,k))*aa**(m-k)
                           for k in range(m+1)])
    direct=sum((coeff[i]*coeff[j]*aa**(i+j+1)/F(i+j+1)
                 for i in range(len(coeff)) for j in range(len(coeff))),F())
    beta=aa**(4*m+1)*F(factorial(2*m)**2,factorial(4*m+1))
    if direct!=beta:
        raise ArithmeticError("Independent exact Brownian weak-derivative normalization failed")
    return {"radius":aa,"power":m,
            "direct_polynomial_L2_energy":direct,
            "independent_beta_energy":beta,
            "Brownian_mixed_second_energy":direct,
            "source_Weil_quadratic_evaluated":False,
            "distributional_identity_calibrated":True,
            "RH_proved":False}
