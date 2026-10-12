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
