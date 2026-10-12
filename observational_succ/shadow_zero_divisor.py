"""Exact symbolic source-shadow zero-divisor descent, no unknown zeros read.

For an analytic source F, two test-function shadows F_i=C_i F have common
zero divisor equal to that of F wherever C_1,C_2 have no common zero.
This is an identity of vanishing orders, not a numerical RH result.

Genuine Gaussian scale-pair Fourier-selfdual tests with integer prime
scales 2 and 3 have disjoint additional Mellin-factor zero sets, but
those zero sets approach arbitrarily close at unbounded imaginary heights.
Thus algebraic uniqueness does NOT give a uniformly bounded decoder.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .shadow_source_inference import ShadowSourceError


def prime(n:int)->bool:
    return type(n) is int and n>1 and all(n%d for d in range(2,isqrt(n)+1))


def normalized_gaussian_scale_pair(scale:Q)->tuple[Q,Q]:
    """f_r=(G_r+r*G_(1/r))/(1+r) in length-scale G_r(x)=G(x/r)."""
    if type(scale) not in (int,Q):
        raise ShadowSourceError("Only exact rational scales")
    r=Q(scale)
    if r<=0 or r==1:
        raise ShadowSourceError("Positive nonunit scale required for auxiliary zeros")
    return (Q(1,1+r),r/(1+r))


@dataclass(frozen=True)
class CommonAnalyticShadow:
    """Symbolic proof: F_1=C_1 F and F_2=C_2 F, with coprime
    holomorphic multipliers, imply gcd zero-divisor = divisor of F.

    Analytic factorization is a REQUIRED SOURCE HYPOTHESIS and is not
    automatically established by a dictionary or by the returned receipt.
    """
    source_id:str
    source_theory:str
    multiplier_a:str
    multiplier_b:str
    disjoint_reason:str

    def __post_init__(self):
        if not all(type(x) is str and x for x in (self.source_id,self.source_theory,
                self.multiplier_a,self.multiplier_b,self.disjoint_reason)):
            raise ShadowSourceError("A global analytic source and separate test vectors are mandatory")

    def certificate(self)->dict:
        return {
            'divisor_rule':'min(ord(F*C1),ord(F*C2))=ord(F) if min(ord(C1),ord(C2))=0',
            'shared_analytic_source_assumed':self.source_theory,
            'multipliers':(self.multiplier_a,self.multiplier_b),
            'coprimality_reason':self.disjoint_reason,
            'does_not_input_unknown_zeta_zero_positions':True,
            'RH_or_Weil_positivity_proved':False,
            'physical_source_authentication':False,
        }


def distinct_prime_scale_shadows(p:int,q:int)->CommonAnalyticShadow:
    """Self-Fourier normalized positive Gaussian scale-pair factors
    C_r(s)=[r^-s+r^(s-1)]/[1+r^-1] have zeros only at
      s=1/2+(k+1/2)*pi*i/log r.
    Distinct integer prime scales have NO common zeros, since equality
    forces a nonzero odd integer power of p to equal an odd power of q.
    """
    if not prime(p) or not prime(q) or p==q:
        raise ShadowSourceError("Two distinct AUTHENTIC rational primes required")
    return CommonAnalyticShadow(
        'diagonal-rational-source','classical Tate local zeta factorization',
        f'C_{p}(s)=(p^(-s)+p^(s-1))/(1+1/p)',
        f'C_{q}(s)=(q^(-s)+q^(s-1))/(1+1/q)',
        f'zeros meet only if {p}^(2k+1)={q}^(2l+1), impossible by unique factorization')


def offcritical_vs_line_shadow(epsilon:Q,scale:int=2)->CommonAnalyticShadow:
    """The DZ9 positive selfdual f_epsilon multiplier has off-line
    auxiliary roots for 4/5<epsilon<1; a Gaussian pair C_scale(s)
    has all its auxiliary roots on Re(s)=1/2. Thus disjoint.
    """
    if type(epsilon) not in (int,Q):
        raise ShadowSourceError("Only exact rational epsilon")
    e=Q(epsilon)
    if not Q(4,5)<e<1:
        raise ShadowSourceError("This exact disjointness theorem needs 4/5<epsilon<1")
    if not prime(scale):
        raise ShadowSourceError("Authentic prime scale required for mutation control")
    return CommonAnalyticShadow(
        'diagonal-rational-source','classical Tate local zeta factorization',
        f'C_eps(s)=[1+eps(4^(-s)+4^(s-1))]/[1+5*eps/4], eps={e}',
        f'C_{scale}(s)=(scale^(-s)+scale^(s-1))/(1+1/scale)',
        'first auxiliary zeros have Re(s)!=1/2, second all have Re(s)=1/2')


def two_prime_shadow_conditioning_obstruction(p:int=2,q:int=3)->dict:
    """Analytic theorem: for two distinct primes, on Re(s)=1/2,
      C_p=K_p cos(t log p), C_q=K_q cos(t log q).
    Their exact zeros are disjoint; yet inf_t(|C_p|+|C_q|)=0.

    Proof of infimum: t_k=(k+1/2)*pi/log p sets C_p=0. Irrational
    log q/log p (unique factorization) implies the rotated orbit
    (k+1/2)*log q/log p modulo 1 is dense. Thus subsequence has
    C_q->0. No numerical or unknown zeta-zero input is needed.

    Therefore there are NO uniformly bounded decoder coefficient
    functions A,B on the WHOLE critical line with AC_p+BC_q=1.
    This only concerns auxiliary test multipliers, not RH.
    """
    shadows=distinct_prime_scale_shadows(p,q)
    return {'prime_scales':(p,q),
            'exact_auxiliary_zero_sets_disjoint':True,
            'infimum_of_sum_of_absolute_multipliers_on_critical_line':0,
            'zero_approach_not_attained':True,
            'global_uniformly_bounded_bezout_decoder_exists':False,
            'source_of_instability':'irrational log(q)/log(p) phases',
            'proof':'irrational rotation density plus exact zero of first multiplier',
            'unknown_zeta_zero_positions_used':False,
            'independent_source_attestation':False,
            'gcd_zero_divisor_rule':shadows.certificate()['divisor_rule']}


def _poly(coeffs)->tuple[Q,...]:
    """Rational Q[z] coefficients in ascending-degree order."""
    if type(coeffs) not in (tuple,list) or not coeffs:
        raise ShadowSourceError("Declare nonempty analytic-polynomial expression")
    if any(type(v) not in (int,Q) for v in coeffs):
        raise ShadowSourceError("Exact polynomial expressions require rational coefficients")
    seq=[Q(v) for v in coeffs]
    while len(seq)>1 and seq[-1]==0:
        seq.pop()
    return tuple(seq)


def _poly_mul(a,b)->tuple[Q,...]:
    a,b=_poly(a),_poly(b)
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return _poly(out)


def _poly_sub(a,b)->tuple[Q,...]:
    a,b=_poly(a),_poly(b)
    return _poly([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
                  for i in range(max(len(a),len(b)))])


def _poly_divmod(a,b)->tuple[tuple[Q,...],tuple[Q,...]]:
    a,b=_poly(a),_poly(b)
    if not any(b):
        raise ShadowSourceError("Zero analytic multiplier cannot be divided")
    q=[Q(0)]*max(1,len(a)-len(b)+1)
    r=a
    while any(r) and len(r)>=len(b):
        power=len(r)-len(b)
        coef=r[-1]/b[-1]
        q[power]+=coef
        subtract=[Q(0)]*power+list(coef*x for x in b)
        r=_poly_sub(r,subtract)
    return (_poly(q),r)


def _poly_gcd(a,b)->tuple[Q,...]:
    a,b=_poly(a),_poly(b)
    while any(b):
        _,r=_poly_divmod(a,b)
        a,b=b,r
    if not any(a):
        return (Q(0),)
    return tuple(x/a[-1] for x in a)


def construct_global_polynomial_from_shadows(
    c1:tuple[Q,...],c2:tuple[Q,...],
    observed_f1:tuple[Q,...],observed_f2:tuple[Q,...])->dict:
    """Construct F from two certified polynomial test-function shadows WITHOUT
    supplying F beforehand. Source compatibility C2*F1=C1*F2 is NECESSARY;
    if C1,C2 coprime it is also SUFFICIENT. Q[z] toy analogue of analytic
    sheaf descent, NOT a reconstruction from finitely many sampled values.
    """
    c1,c2,f1,f2=map(_poly,(c1,c2,observed_f1,observed_f2))
    if not any(c1) or not any(c2):
        raise ShadowSourceError("Nonzero test multiplier is required")
    discrepancy=_poly_sub(_poly_mul(c2,f1),_poly_mul(c1,f2))
    if any(discrepancy):
        return {'status':'INCOMPATIBLE_SOURCE_SHADOWS',
                'commuting_square_defect':discrepancy,
                'source_global_factor':None}
    gcd=_poly_gcd(c1,c2)
    if gcd!=(Q(1),):
        return {'status':'NONCOPRIME_UNCERTIFIED',
                'common_multiplier':gcd,
                'source_global_factor':None}
    quotient1,rem1=_poly_divmod(f1,c1)
    quotient2,rem2=_poly_divmod(f2,c2)
    if any(rem1) or any(rem2) or quotient1!=quotient2:
        raise AssertionError("Coprime analytic descent produced inconsistent quotient")
    F=quotient1
    if _poly_mul(c1,F)!=f1 or _poly_mul(c2,F)!=f2:
        raise AssertionError("Constructed global polynomial fails original shadows")
    return {'status':'GLOBAL_SOURCE_CONSTRUCTED',
            'global_polynomial':F,
            'multipliers_coprime':True,
            'both_observation_squares_verified':True,
            'global_factor_was_given_as_input':False,
            'analytic_scope':'EXACT Q[z] ONLY; entire-function version uses analytic gluing'}
