"""SOURCE-EDGE: genuine prime-2 positive surplus on Suzuki's high carrier.

The original completed signed Weil source (one Gamma_R, both poles, contact,
prime n=2 with Lambda(2)/sqrt(2)) is NOT replaced by a positive covariance.

For F=Vu in the original first window I=(-1/2,1/2), b=log(2) lies in (1/2,1).
A=P_I(T_b+T_-b)P_I is exactly a two-edge flip plus a zero center:
       ||F||²-<F,A F> = ||F_C||²+||F_R-T_b F_L||² >=0.
The inherited genuine all-high Bessel certificate bounded -w<A F,F>
by -w||F||². Retaining the remainder yields a *new arithmetic* form:
 D_4 >= kappa_parity K + w(||F_C||²+||F_R-T_bF_L||²),
 plus 2|<F,cosh(x/2)>|² in the odd-derivative/even-primitive sector.

On the rational inner center C0=[-1/8,1/8], retain two orthogonal features
  l0(F)=integral_C0 F,  l1(F)=integral_C0 x F;
their exact weights are 4 and 768. These are globally lawful rank-two
source lower bounds, not finite sampled PSD extrapolations.

All source-specific adapters fail closed on the exact original Suzuki SHA,
real prime tape, half-density and true log2/sqrt2 inequalities.
No zero locations are inputs. S4 and RH remain OPEN.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from math import comb


class PrimeSurplusError(ValueError):
    """Invalid source, measure, parity, or exact arithmetic contract."""


def q(x):
    if type(x) not in (int,F):
        raise PrimeSurplusError("exact int/Fraction required, float/bool rejected")
    return F(x)


def require_2edge(a,b):
    a,b=q(a),q(b)
    if a<=0 or not a<b<2*a:
        raise PrimeSurplusError("disjoint two-edge grammar requires 0<a<b<2a")
    return a,b


def edge_intervals(a,b):
    """I=(-a,a): L=(-a,a-b), C=(a-b,b-a), R=(b-a,a)."""
    a,b=require_2edge(a,b)
    return ((-a,a-b),(a-b,b-a),(b-a,a))


def poly_add(a,b,scale=1):
    factor=q(scale)
    n=max(len(a),len(b))
    out=[F(0)]*n
    for i,v in enumerate(a):out[i]+=q(v)
    for i,v in enumerate(b):out[i]+=factor*q(v)
    return tuple(out)


def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]+=q(ai)*q(bj)
    return tuple(out)


def poly_int(a,lower,upper):
    lower,upper=q(lower),q(upper)
    return sum((q(c)*(upper**(i+1)-lower**(i+1))/(i+1)
                for i,c in enumerate(a)),F(0))


def poly_translate(p,shift):
    """P(x-shift) in powers of x, with no floating evaluation."""
    z=q(shift)
    out=[F(0)]*len(p)
    for k,c in enumerate(p):
        for j in range(k+1):
            out[j]+=q(c)*comb(k,j)*(-z)**(k-j)
    return tuple(out)


def edge_energy_polynomial(p,a,b):
    """Exact rational edge Dirichlet energy, holds only for a<b<2a."""
    a,b=require_2edge(a,b)
    p=tuple(q(x) for x in p)
    (ll,lr),(cl,cr),(rl,rr)=edge_intervals(a,b)
    norm=poly_int(poly_mul(p,p),-a,a)
    left=poly_translate(p,b)
    cross=poly_int(poly_mul(p,left),rl,rr)
    center=poly_int(poly_mul(p,p),cl,cr)
    mismatch=poly_int(poly_mul(poly_add(p,left,-1),
                               poly_add(p,left,-1)),rl,rr)
    if norm-2*cross != center+mismatch:
        raise ArithmeticError("original prime-2 edge graph identity fails")
    if center<0 or mismatch<0:
        raise ArithmeticError("edge energy must be nonnegative")
    return {
        "source_type":"RATIONAL_TWO_EDGE_CALIBRATION_NOT_ZETA",
        "norm":norm,"signed_shift_pair":2*cross,
        "central_energy":center,"edge_mismatch_energy":mismatch,
        "prime_surplus":center+mismatch,"actual_prime_source":False,
    }


def _trim(poly):
    p=list(poly)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)


def _shifted_cross_in_b(p,r,a=F(1,2)):
    """Polynomial in lag b for integral_[b-a,a] p(x) r(x-b) dx.

    The integration boundaries depend on b. Exact polynomial expansions
    ensure b may later be the true irrational log(2) with a rigorous interval.
    """
    p=tuple(q(x) for x in p);r=tuple(q(x) for x in r);a=q(a)
    out=[F(0)]*(len(p)+len(r)+2)
    for i,pi in enumerate(p):
        if not pi:continue
        for j,rj in enumerate(r):
            if not rj:continue
            for k in range(j+1):
                coefficient=pi*rj*comb(j,k)*(-1)**(j-k)
                exp=j-k
                d=i+k+1
                # upper endpoint a contributes a^d b^exp /d.
                out[exp]+=coefficient*a**d/F(d)
                # lower endpoint (b-a)^d = sum_h choose(d,h)b^h(-a)^(d-h)
                for h in range(d+1):
                    out[exp+h]-=coefficient*comb(d,h)*(-a)**(d-h)/F(d)
    return _trim(out)


def edge_mass_polynomial_in_b(p,r,a=F(1,2)):
    """Exact pair Gram <p,r>-<p,T_b r>-<r,T_b p> in powers of b.

    Works for zero-extended polynomial p,r restricted to (-a,a) and a<b<2a.
    """
    a=q(a); p=tuple(q(v) for v in p);r=tuple(q(v) for v in r)
    if a<=0:raise PrimeSurplusError("positive compact source interval")
    c1=_shifted_cross_in_b(p,r,a)
    c2=_shifted_cross_in_b(r,p,a)
    val=poly_int(poly_mul(p,r),-a,a)
    return _trim(poly_add(poly_add((val,),c1,-1),c2,-1))


def edge_source_polynomial_for_mode(mode):
    """Pure exact Legendre algebra; no claim about original source yet."""
    if type(mode) is not int or not 1<=mode<=12:
        raise PrimeSurplusError("Legendre mode 1..12 required")
    from .suzuki_legendre_source import legendre_polynomial,poly_primitive_zero_at_left
    a=F(1,2)
    primitive=poly_primitive_zero_at_left(legendre_polynomial(mode,a),a)
    return edge_mass_polynomial_in_b(primitive,primitive,a)


def exact_center_features(p,halfwidth=F(1,8)):
    s=q(halfwidth)
    if not 0<s<=F(1,8):
        raise PrimeSurplusError("certified center probes require 0<s<=1/8")
    p=tuple(q(v) for v in p)
    return (poly_int(p,-s,s),poly_int(poly_mul(p,(F(0),F(1))),-s,s))


def center_feature_gram(modes=(5,6),halfwidth=F(1,8)):
    """Exact finite-rank original Legendre witness in the genuine high carrier.

    This module constructs SOURCE-INDEPENDENT rational geometry. A separate
    SHA/source adapter must authenticate b=log2 and w=Lambda2/sqrt2.
    """
    if not isinstance(modes,(tuple,list)) or not 1<=len(modes)<=8:
        raise PrimeSurplusError("one through eight real high Legendre modes")
    if any(type(k) is not int or not 5<=k<=12 for k in modes):
        raise PrimeSurplusError("four-low genuine high modes k>=5 only")
    if len(set(modes))!=len(modes):
        raise PrimeSurplusError("repeated source mode")
    from .suzuki_legendre_source import legendre_polynomial,poly_primitive_zero_at_left
    s=q(halfwidth)
    primitives=tuple(poly_primitive_zero_at_left(
        legendre_polynomial(k,F(1,2)),F(1,2)) for k in modes)
    l0,l1=zip(*(exact_center_features(p,s) for p in primitives))
    norm0=2*s;norm1=2*s**3/F(3)
    M=tuple(tuple(l0[i]*l0[j]/norm0+l1[i]*l1[j]/norm1
                  for j in range(len(modes))) for i in range(len(modes)))
    return {"modes":tuple(modes),"primitives":primitives,"l0":tuple(l0),
            "l1":tuple(l1),"gram":M,"s":s,
            "orthogonal_center_features":True,"source_certified":False}


def feature_projected_norms(s=F(1,8)):
    """Norms of Q_poly<=3 applied to center 1 and x functions (exact)."""
    s=q(s)
    if not 0<s<=F(1,8):raise PrimeSurplusError("center inside genuine prime strip")
    from .suzuki_legendre_source import legendre_polynomial
    p=[legendre_polynomial(j,F(1,2)) for j in range(4)]
    m0=tuple(poly_int(z,-s,s) for z in p)
    m1=tuple(poly_int(poly_mul(z,(F(0),F(1))),-s,s) for z in p)
    n0=2*s-sum(((2*j+1)*m0[j]**2 for j in range(4)),F(0))
    n1=2*s**3/F(3)-sum(((2*j+1)*m1[j]**2 for j in range(4)),F(0))
    if n0<=0 or n1<=0:raise ArithmeticError("projected center feature is zero")
    return {"even_center_Qnorm2":n0,"odd_center_Qnorm2":n1,
            "moment0":m0,"moment1":m1}


def pole_p5_positive_lower():
    """Strict first nonzero Taylor term of authentic completed cosh-polar.

    For w=P5(2x), int w sinh(x/2) >=1/10644480 by Rodrigues and
    positivity of every surviving x^(5+2j) term. Primitive identity
    int Vw cosh(x/2) = -2 int w sinh(x/2), endpoints vanish.
    """
    return F(1,10644480)


@lru_cache(maxsize=1)
def original_prime_surplus_source_passport():
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .tate_weighted_bessel_four_schur import (
        source_parity_split_four_moment_coercivity_certificate
    )
    from .source_weil_hierarchy import (
        authenticated_prime_wavefront,log2_iv,sqrt_inverse
    )
    source=verify_original_suzuki_source()
    cert=source_parity_split_four_moment_coercivity_certificate()
    if cert["source_suzuki_blob"]!=source["source_git_blob"]:
        raise PrimeSurplusError("original signed source SHA/odd-even Bessel mismatch")
    if tuple(cert["genuine_prime_power_labels"])!=(2,) or \
       authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise PrimeSurplusError("fake composite/missing genuine first-prime source")
    log2=log2_iv()
    w2=log2*sqrt_inverse(2)
    if not (F(5,8)<log2.lo and log2.hi<F(3,4) and
            w2.lo>F(12,25) and w2.hi<F(1,2)):
        raise PrimeSurplusError("genuine log2 and Lambda2/sqrt2 source budget failed")
    odd=cert["odd_sector"]["kappa_odd_certified_rational"]
    even=cert["even_sector"]["kappa_even_certified_rational"]
    if odd!=F(63,500) or even!=F(153,500):
        raise PrimeSurplusError("inherited all-high parity coercivity drift")
    return {
        "source_sha":source["source_git_blob"],
        "true_prime_power_label":(2,2),
        "log2_interval":(log2.lo,log2.hi),
        "prime2_weight_interval":(w2.lo,w2.hi),
        "positive_source_weight_floor":F(12,25),
        "kappa_odd":odd,"kappa_even":even,
        "contact_and_both_poles_retained":True,
        "gamma_source_256_rungs_inherited":True,
        "RH_proved":False
    }


def original_high_surplus_certificate(modes=(5,6,7,8),*,prime=2):
    """Source-certified finite chart of a GLOBAL first-window form theorem.

    The form theorem on ALL high w is:
      D4(w,w)>=kappa_pi||Vw||²
             +w2[||F_C||²+||F_R-T_b F_L||²]
             +2|<F,cosh>|²  (odd derivative only).
    The finite returned matrices are not claimed complete G or an RH sign.
    """
    if type(prime) is not int or prime!=2:
        raise PrimeSurplusError("only genuine p=2 original first-window source")
    src=original_prime_surplus_source_passport()
    geometry=center_feature_gram(modes)
    from .suzuki_moment_schur import inverse_neumann_entry
    from .suzuki_legendre_source import polynomial_interval
    k=geometry["modes"];n=len(k);kl=src["kappa_odd"];ke=src["kappa_even"]
    wfloor=src["positive_source_weight_floor"]
    K=tuple(tuple(inverse_neumann_entry(F(1,2),i,j) for j in k) for i in k)
    base=tuple(tuple((kl if k[i]%2 else ke)*K[i][j] if (k[i]-k[j])%2==0 else F(0)
                     for j in range(n)) for i in range(n))
    feat=tuple(tuple(wfloor*x for x in row) for row in geometry["gram"])
    C=tuple(tuple(base[i][j]+feat[i][j] for j in range(n)) for i in range(n))
    # Exact log2 analytic source intervals for the WHOLE true p=2 mismatch
    mass=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if (k[i]-k[j])%2:
                row.append((F(0),F(0)));continue
            poly=edge_mass_polynomial_in_b(geometry["primitives"][i],
                                           geometry["primitives"][j])
            iv=polynomial_interval(poly,src["log2_interval"])
            row.append((iv.lo,iv.hi))
        mass.append(tuple(row))
    from .source_jump_spectral import is_psd
    if not is_psd(feat) or not is_psd(C):
        raise ArithmeticError("exact source rank-two comparator failed PSD")
    return {
        "source":"ORIGINAL_SIGNED_SUZUKI_PRIME2_EDGE_SURPLUS",
        "source_sha":src["source_sha"],
        "modes":k,"source_kappa":tuple(kl if i%2 else ke for i in k),
        "true_log2":src["log2_interval"],
        "true_prime2_weight":src["prime2_weight_interval"],
        "K":K,"base_scalar_gram":base,
        "center_rank_two_gram":feat,
        "source_non_scalar_comparator":C,
        "genuine_full_prime_mismatch_gram_intervals":tuple(mass),
        "p5_pole_amplitude_lower":pole_p5_positive_lower(),
        "source_all_high_theorem_claimed_conditional":True,
        "S4_sign":"UNVERIFIED","RH_proved":False,
    }
