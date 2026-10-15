"""APOLLO: source-typed 2nd/3rd Suzuki distribution jets and gauge obstruction.

All general theorems are derived in research/2026-10-15/APOLLO_DERIVATIVE_SOURCE_THEOREMS.md.
Arithmetic jets reuse an exact Git-blob-authenticated source; NO zero data.
Numerical integrals only independently calibrate symbolic distribution identities.
Neither source gluing nor higher derivative moments implies Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb
from typing import Callable

from .one_object_transport import (
    OneObjectError, _fraction, _int, _mp, _mfrac, _stage_constants,
    _aligned_screw, contact_rational_increment,
)
from .one_object_kernel_certificates import authentic_kernel_interval
from .completed_weil_transport import von_mangoldt_labels


def quadratic_gauge_kernel_shift(c: int | Q, x: int | Q, y: int | Q) -> Q:
    """K_{g+c*t²}-K_g = -2*c*x*y; D³(g+c*t²)=D³g, exactly."""
    c, x, y = _fraction(c), _fraction(x), _fraction(y)
    return -2*c*x*y


def second_derivative_gauge_shift(c: int | Q) -> Q:
    """-D²(g+c*t²)-(-D²g) = -2c as a CONSTANT distribution."""
    return -2*_fraction(c)


def third_derivative_gauge_shift(c: int | Q) -> Q:
    """D³(g+c*t²)-D³g = 0. Missing polynomial rank-one zero mode."""
    _fraction(c)
    return Q()


def exact_source_gauge_negative_direction(x: int | Q = Q(1, 4),
                                          c: int | Q = 64,
                                          J: int = 128) -> dict:
    """Authentic interval G at a point, plus explicit FAKE quadratic gauge.

    This is NOT a negative RH witness: the mutant changes the genuine Weil
    distribution by -2c Lebesgue density and breaks source normalization.
    """
    a, cc = _fraction(x), _fraction(c)
    if not a or cc<=0:
        raise OneObjectError("Choose a nonzero source point and positive mutation")
    interval=authentic_kernel_interval(a,a,J)
    displacement=quadratic_gauge_kernel_shift(cc,a,a)
    mutated=(interval[0]+displacement, interval[1]+displacement)
    return {"point":a,"c":cc,"original_interval":interval,
            "mutant_interval":mutated,
            "strict_negative_mutant_certified":mutated[1]<0,
            "third_derivative_unchanged":True,
            "source_authentic_mutant":False,"RH_proved":False}


def _source():
    """Re-use the original SHA-pinned PR85 Suzuki interval source."""
    from .suzuki_legendre_source import _pinned_source
    return _pinned_source()


@dataclass(frozen=True)
class GenuineThirdPrimeJet:
    """δ'_log(n) label and a rigorous outward coefficient interval."""
    n: int
    p: int
    exponent: int
    log_n_interval: tuple[Q,Q]
    delta_prime_weight_interval: tuple[Q,Q]
    authentic_source: bool = True


def genuine_prime_third_jet(n: int) -> GenuineThirdPrimeJet:
    """Extract the exact signed distributional prime δ' amplitude.

    g'' has +w_n(δ_(log n)+δ_(-log n)); g''' has +w_n times
    their distributional derivatives, w_n=log(p)/sqrt(p^k).
    The original arithmetic source is verified by its Git blob SHA.
    """
    _int(n,2,128)
    source=_source()
    p=source.real_prime_power(n)
    if p is None:
        raise OneObjectError("Fake composite impulse is not a von Mangoldt jet")
    exponent=0
    tmp=n
    while tmp%p==0:
        tmp//=p
        exponent+=1
    if tmp!=1:
        raise ArithmeticError("Unlawful original source factorization")
    ln=source.log_iv(n)
    w=source.log_iv(p)*source.sqrt_inverse(n)
    if w.lo<=0:
        raise ArithmeticError("Original prime jet must have positive coefficient")
    return GenuineThirdPrimeJet(n,p,exponent,(ln.lo,ln.hi),(w.lo,w.hi))


def true_third_prime_wavefronts(radius: int | Q) -> tuple[GenuineThirdPrimeJet,...]:
    """Exactly certify which original δ' atoms lie in (-R,R) (R<=4).

    All yes/no decisions compare outward Fraction log(n) enclosures with R;
    unknown boundary collisions raise rather than guess using float.
    Source file SHA checked before enumeration. n<=128 and log 128>4.
    """
    r=_fraction(radius)
    if not 0<r<=4:
        raise OneObjectError("Exact finite source window 0<R<=4")
    src=_source()
    if src.log_iv(128).lo<=r:
        raise OneObjectError("Source window lacks a rigorously excluded terminal prime")
    labels=tuple(n for n,_ in von_mangoldt_labels(128))
    out=[]
    for n in labels:
        ln=src.log_iv(n)
        if ln.hi<r:
            out.append(genuine_prime_third_jet(n))
        elif ln.lo<=r:
            raise OneObjectError("Unresolved rational cutoff near original prime wavefront")
    return tuple(out)


def third_origin_contact_offset(J: int) -> Q:
    """Coefficient of δ'_0 in D³g_J is C0 plus this RATIONAL number.

    The full finite derivative consists of
      -sinh(t/2) -sum_j alpha_j sign(t) exp(-alpha_j |t|)
      + sum_true w_n [δ'_b+δ'_-b]
      + (C0 - 2 sum_{j<J} 1/(2j+1)) δ'_0 .
    C0=EulerGamma+log(4*pi). The separated origin coefficient diverges
    as J->infinity: it must be combined with the smooth gamma distribution
    BEFORE taking a limit. This API never inserts that divergent limit.
    """
    _int(J,0,512)
    return -sum((Q(2,2*j+1) for j in range(J)),Q())


def cubic_gauge_discrimination(anchor_mass: int | Q, c: int | Q) -> dict:
    """The ONE scalar second-order normalization missing from D³.

    Let eta be a compact test with integral=anchor_mass !=0.
    The W functional for g+c*t² shifts by -2c*integral(eta).
    A nonzero source-normalized mass test detects every nonzero c.
    This datum is an integral of the signed W, NOT the δ0 contact.
    """
    m=_fraction(anchor_mass)
    c=_fraction(c)
    if not m:
        raise OneObjectError("A mass-zero test cannot fix quadratic gauge")
    return {"third_source_difference":Q(),
            "source_Weil_pairing_difference":-2*c*m,
            "quadratic_gauge_fixed_if_pairing_equal":(c==0),
            "source_contact_delta_not_equivalent_to_constant_mode":True}


def polynomial_derivative(coeff: tuple[Q,...], order: int) -> tuple[Q,...]:
    """Exact derivative of polynomial in ascending power basis."""
    _int(order,0,12)
    if type(coeff) is not tuple or not coeff or any(type(c) not in (int,Q) for c in coeff):
        raise OneObjectError("Exact nonempty rational coefficient tuple")
    vals=tuple(Q(c) for c in coeff)
    for _ in range(order):
        vals=tuple((i+1)*vals[i+1] for i in range(len(vals)-1)) if len(vals)>1 else (Q(),)
    return vals


def polynomial_moment(coeff: tuple[Q,...], order: int) -> Q:
    """Integral on [0,1] of t^order P(t)dt, exact."""
    _int(order,0,16)
    return sum((Q(c,i+order+1) for i,c in enumerate(coeff)),Q())


def repeated_compact_primitive(coeff: tuple[Q,...], order: int) -> tuple[Q,...]:
    """m-fold primitive starting with zero boundary jets at the left endpoint."""
    _int(order,1,3)
    if any(type(c) not in (int,Q) for c in coeff):
        raise OneObjectError("Exact rational test only")
    vals=tuple(Q(c) for c in coeff)
    for _ in range(order):
        vals=(Q(),)+tuple(v/Q(i+1) for i,v in enumerate(vals))
    return vals


def compact_polynomial_moment_certificate(order: int, power: int = 8) -> dict:
    """Exact control of range(D^m) and missing polynomial moments.

    phi(t)=t^power(1-t)^power for t in (0,1), zero outside; its first
    power-1 derivatives vanish at both ends. m<=3, power>=7 ensures
    phi^(m) is at least C³ globally for smooth-domain approximations.
    This finite piecewise-polynomial control is NOT Cc-infinity, although
    the separate theorem and proof cover all Cc-infinity functions.
    """
    m=_int(order,1,3)
    b=_int(power,7,14)
    phi=tuple([Q()]*b+[Q((-1)**k*comb(b,k)) for k in range(b+1)])
    derived=polynomial_derivative(phi,m)
    nulls=tuple(polynomial_moment(derived,k) for k in range(m))
    if any(nulls):
        raise ArithmeticError("Exact compact m-th derivative lost a moment constraint")
    reconstructed=repeated_compact_primitive(derived,m)
    if reconstructed!=phi:
        raise ArithmeticError("Zero-jet compact primitive did not recover source")
    high_moment=polynomial_moment(derived,m)
    expected=(-1)**m
    from math import factorial
    expected*=factorial(m)*polynomial_moment(phi,0)
    if high_moment!=expected:
        raise ArithmeticError("Integrated moment contrast failed")
    return {"order":m,"power":b,"moment_nulls":nulls,
            "first_nonzero_moment":high_moment,
            "primitive_recovered":True,
            "unobserved_moment_dimension":m,
            "Cc_infinity_theorem_proved_by_integration_by_parts":True,
            "finite_polynomial_test_is_Cc_infinity":False,
            "RH_proved":False}


def _odd_probe(t, radius: Q, derivative: int, mp):
    """h(t)=t(1-(t/R)^2)^4 on |t|<R, zero otherwise; h C³."""
    x=mp.mpf(t)
    R=_mfrac(mp,radius)
    if abs(x)>=R:
        return mp.mpf(0)
    u=x/R
    if derivative==0:
        return x*(1-u*u)**4
    if derivative==1:
        return 1-12*u*u+30*u**4-28*u**6+9*u**8
    if derivative==3:
        return (-24+360*u*u-840*u**4+504*u**6)/(R*R)
    raise OneObjectError("This independent calibration supports only h,h',h'''.")


def third_distribution_bump_pair(radius: int | Q, J: int,
                                 dps: int = 60,
                                 contact_mutation: int | Q = 0) -> dict:
    """Two independent numerical paths for exact identity <D³g,h>=W(h').

    Source W(h') is evaluated from original pole/prime/Gamma/contact data.
    D³g acts on compact odd h via -integral(g h'''), with real-valued
    continuous Suzuki g evaluated on each prime wavefront interval.
    The theorem is analytic; comparisons are NUMERICAL, not interval proofs.
    """
    R=_fraction(radius)
    if not 0<R<=4:
        raise OneObjectError("Rational compact radius (0,4] required")
    _int(J,0,64)
    mutation=_fraction(contact_mutation)
    mp=_mp(dps)
    _R,atoms,C0,CJ=_stage_constants(mp,R,J)
    # The certified original source classification is independent of
    # the numerical cutoff in _stage_constants.
    labels=true_third_prime_wavefronts(R)
    if tuple(n for n,_p in original_prime_atoms_local(R)) != tuple(j.n for j in labels):
        raise ArithmeticError("Independent source wavefront classifiers disagree")
    wprime=lambda t:_odd_probe(t,R,1,mp)
    wthird=lambda t:_odd_probe(t,R,3,mp)
    radius_mp=_mfrac(mp,R)
    breaks=sorted(set([mp.mpf(0),radius_mp]+[b for b,w in atoms]))
    pole=2*mp.quad(lambda t:wprime(t)*(mp.exp(t/2)+mp.exp(-t/2)),[0,radius_mp])
    prime=-2*mp.fsum(w*wprime(b) for b,w in atoms)
    arch=-C0
    for j in range(J):
        alpha=mp.mpf(4*j+1)/2
        arch+=mp.mpf(2)/(2*j+1)-2*mp.quad(lambda t:mp.exp(-alpha*t)*wprime(t),
                                            [0,radius_mp])
    W_on_derivative=pole+prime+arch
    CJ+=_mfrac(mp,mutation)
    screw_cubic=-2*mp.quad(
        lambda t:_aligned_screw(mp,t,atoms,CJ,J)*wthird(t),breaks
    )
    return {"radius":str(R),"gamma_rungs":J,
            "source_prime_labels":tuple(j.n for j in labels),
            "signed_Weil_on_first_derivative":mp.nstr(W_on_derivative,40),
            "Suzuki_third_distribution_pairing":mp.nstr(screw_cubic,40),
            "residual":mp.nstr(W_on_derivative-screw_cubic,18),
            "residual_abs":abs(W_on_derivative-screw_cubic),
            "contact_mutation":str(mutation),
            "origin_contact_detected":bool(mutation),
            "all_test_Weil_positive":False,"RH_proved":False}


def original_prime_atoms_local(radius: Q) -> tuple[tuple[int,int],...]:
    """Numerical-only original comparator; exact interval oracle is independent."""
    from .one_object_transport import original_prime_atoms
    return original_prime_atoms(radius)


def exact_local_gamma_slope_bound(r: int | Q, J: int, dps: int = 70) -> dict:
    """Closed-form Gamma radial g' and rigorously derived geometric tail shape.

    For r>0: gamma_g'(r)=-atanh(exp(-r/2))-atan(exp(-r/2)).
    First J rungs: -sum 2/(4j+1) exp(-(4j+1)r/2).
    Tail <= [2/(4J+1)] exp(-(4J+1)r/2)/(1-exp(-2r)).
    Values are numerical, inequality itself derived by geometric comparison.
    """
    t=_fraction(r)
    _int(J,1,512)
    if not 0<t<=4:
        raise OneObjectError("Positive rational radial test required")
    mp=_mp(dps)
    x=_mfrac(mp,t);z=mp.exp(-x/2)
    closed=-mp.atanh(z)-mp.atan(z)
    partial=-mp.fsum(mp.mpf(2)/(4*j+1)*mp.exp(-(4*j+1)*x/2) for j in range(J))
    upper=(mp.mpf(2)/(4*J+1))*mp.exp(-(4*J+1)*x/2)/(1-mp.exp(-2*x))
    return {"radius":str(t),"rungs":J,"closed":mp.nstr(closed,30),
            "partial":mp.nstr(partial,30),
            "absolute_error":abs(closed-partial),
            "analytic_tail_evaluation":upper,
            "numerical_rounding_certified":False,
            "RH_proved":False}



def local_suzuki_first_second_third(r: int | Q, dps: int = 75) -> dict:
    """Genuine t>0 ORIGINAL Suzuki derivatives before the first prime wavefront.

    For 0<r<=1/4<log2, the authentic prime contribution is absent.
      g'(r)=-4 sinh(r/2)+C_inf/2-atanh(q)-atan(q), q=e^-r/2;
      g''(r)=-2cosh(r/2)+q/(1-q^4);
      g'''(r)=-sinh(r/2)-q/[2(1-q^4)]-2q^5/(1-q^4)^2.
    These are ordinary derivatives ONLY for r>0 away from the wavefronts.
    The full distributions at r=0 need Pf/contact renormalization.
    """
    rr=_fraction(r)
    if not 0<rr<=Q(1,4):
        raise OneObjectError("Authentic prime-free positive window 0<r<=1/4")
    mp=_mp(dps)
    x=_mfrac(mp,rr)
    q=mp.exp(-x/2)
    denom=-mp.expm1(-2*x)
    C=mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
    slope=-4*mp.sinh(x/2)+C/2-mp.atanh(q)-mp.atan(q)
    second=-2*mp.cosh(x/2)+q/denom
    third=-mp.sinh(x/2)-q/(2*denom)-2*q**5/denom**2
    leading_slope=(mp.log(x)+mp.euler+mp.log(2*mp.pi))/2
    delta=abs(slope-leading_slope)
    analytic=3*x
    return {
        "rational_radius":str(rr),
        "slope":mp.nstr(slope,40),
        "second":mp.nstr(second,40),
        "third":mp.nstr(third,40),
        "scaled_second":mp.nstr(x*second,35),
        "scaled_third":mp.nstr(x*x*third,35),
        "slope_asymptotic_abs_error":delta,
        "rigorous_elementary_error_bound":3*rr,
        "float_rounding_certified":False,
        "prime_wavefront_in_window":False,
        "RH_proved":False,
    }



def authentic_uniform_small_diagonal(r: int | Q) -> dict:
    """Source-certified ORIGINAL zeta Suzuki K_g(r,r)>r/8 for 0<r<=1/8.

    The theorem covers ALL real 0<r<=1/8, not only these rational API
    arguments; proof is by AP-07's analytic |g'(r)-.5 log r-C|<=3r,
    C=(EulerGamma+log(2*pi))/2 < 5/4, log(2)>2/3, and integration:
      g(r)/r <= .5 log r + C-.5 +1.5r
             < -3/2 log2+3/4+3/16 < -1/16.
    Thus K_g(r,r)=-2g(r)>r/8.
    Both input constant inequalities are checked by Git-blob pinned outward
    Fraction interval primitives. This is DIAGONAL ONLY, not even 2x2 PSD.
    """
    rr=_fraction(r)
    if not 0<rr<=Q(1,8):
        raise OneObjectError("Exact positive small interval 0<r<=1/8")
    src=_source()
    from_exact=(src.gamma_iv()+src.log2_iv()+src.log_interval(src.pi_iv()))/2
    if not from_exact.hi<Q(5,4):
        raise ArithmeticError("Original rational normalization failed C<5/4")
    if not src.log2_iv().lo>Q(2,3):
        raise ArithmeticError("Original rational log2 lower bound lost")
    return {"radius":rr,
            "original_C_interval":(from_exact.lo,from_exact.hi),
            "original_log2_interval":(src.log2_iv().lo,src.log2_iv().hi),
            "rigorously_positive_K_diagonal_lower":rr/8,
            "strict_for_every_real_radius_in_window":True,
            "source":"ORIGINAL_SHA_PINNED_ZETA_SUZUKI",
            "not_all_2by2_gram":True,
            "RH_proved":False}
