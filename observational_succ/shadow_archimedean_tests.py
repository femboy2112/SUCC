"""Empirical Shadow-SUCC tests for competing Archimedean test functions.

Positive result: among positive Gaussian SCALE MIXTURES, f(0)=integral f=1
and one exact Mellin moment C(2)=1 select the standard Gaussian. The exact
gap equals variance of the scale and bounds full L1 source error.

Negative result: beyond that class, finite Mellin/pointwise probes cannot
select the Gaussian even among strictly POSITIVE, Fourier-SELF-DUAL real
Schwartz functions. The alternative f=e^(-pi*x*x)*(1+eta P(pi*x*x))
is constructed from real Fourier +1 Hermite eigenfunctions H_(4j); ALL
specified finite probes are exactly equal to the canonical Gaussian.

Hermite eigenfunction Fourier transformation and Gamma Mellin identity are
classical analytic theorems cited in the dossier. The code's finite rational
polynomial identities and positivity bounds are checked exactly; neither
symbolic proof nor software supplies an empirical Archimedean source oracle.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial
from typing import Iterable

from .shadow_source_inference import ShadowSourceError,solve_system


def rational(v:object)->Q:
    if type(v) is Q or type(v) is int:
        return Q(v)
    raise ShadowSourceError("Rational analytic certificates do not accept floats")


def polynomial_eval(coeffs:tuple[Q,...],y:Q)->Q:
    y=rational(y)
    return sum((c*y**k for k,c in enumerate(coeffs)),Q(0))


def polynomial_add(a:tuple[Q,...],b:tuple[Q,...]) -> tuple[Q,...]:
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))


def polynomial_scale(a:tuple[Q,...],w:Q)->tuple[Q,...]:
    w=rational(w)
    return tuple(w*v for v in a)


def hermite_fourier_one(index:int)->tuple[Q,...]:
    """H_{4j}(sqrt(2*y)), Fourier eigenvalue exactly +1.

    Physicists Hermite formula: H_n(z)=n! sum_{k=0}^{floor(n/2)}
      (-1)^k(2z)^(n-2k)/(k!(n-2k)!). n=4j and z=sqrt(2y).
    """
    if type(index) is not int or index<0 or index>24:
        raise ShadowSourceError("Hermite Fourier +1 mode index 0..24")
    n=4*index
    coefficients=[Q(0)]*(n//2+1)
    for j in range(n//2+1):
        power=(n-2*j)//2
        coefficients[power]+=Q((-1)**j*factorial(n)*8**power,
                               factorial(j)*factorial(2*power))
    return tuple(coefficients)


def rising(x:Q,n:int)->Q:
    if type(n) is not int or n<0:
        raise ShadowSourceError("Nonnegative integer rise")
    result=Q(1)
    for j in range(n):
        result*=x+j
    return result


def relative_mellin_polynomial(coeffs:tuple[Q,...],even_s:int)->Q:
    """For s=2m>0, relative Mellin perturbation of G*P(pi*x²)
    is E[P(Y)] where Y has gamma shape m, so E Y^k=(m)_k.
    """
    if type(even_s) is not int or even_s<=0 or even_s%2:
        raise ShadowSourceError("Machine-checked Mellin probes require even integer s>0")
    m=Q(even_s,2)
    return sum((c*rising(m,k) for k,c in enumerate(coeffs)),Q(0))


@dataclass(frozen=True)
class GaussianScaleShadow:
    """Source f(x)=sum w_b exp(-pi*x²/b²), w_b>=0, sum w_b=1.

    Fourier self-duality requires w_(1/b)=b*w_b in this basis.
    If mean b=1, f0=integral f=1. C(2)=E b².
    """
    source_id:str
    scales:tuple[Q,...]
    weights:tuple[Q,...]

    def __post_init__(self):
        if not self.source_id or not self.scales or len(self.scales)!=len(self.weights):
            raise ShadowSourceError("Nonempty source and scales/weights")
        bs=tuple(rational(b) for b in self.scales)
        ws=tuple(rational(w) for w in self.weights)
        if any(b<=0 for b in bs) or any(w<0 for w in ws) or sum(ws,Q(0))!=1:
            raise ShadowSourceError("Positive scales and nonnegative normalized weights")
        if len(set(bs))!=len(bs):
            raise ShadowSourceError("Combine repeated Gaussian scales before proving source")
        object.__setattr__(self,'scales',bs)
        object.__setattr__(self,'weights',ws)

    @property
    def first_scale_moment(self)->Q:
        return sum((w*b for w,b in zip(self.weights,self.scales)),Q(0))

    @property
    def second_scale_moment(self)->Q:
        return sum((w*b*b for w,b in zip(self.weights,self.scales)),Q(0))

    def prove_fourier_selfdual(self)->bool:
        mass=dict(zip(self.scales,self.weights))
        return all(mass.get(1/b,Q(0))==b*w for b,w in mass.items())

    def moment_shadow(self)->dict:
        if self.first_scale_moment!=1:
            raise ShadowSourceError("Integral f must equal f(0)=1 for normalized shadow")
        gap=self.second_scale_moment-1
        var=sum((w*(b-1)**2 for b,w in zip(self.scales,self.weights)),Q(0))
        if gap!=var or gap<0:
            raise AssertionError("Exact Gaussian-source variance theorem failed")
        triangle=sum((w*abs(b-1) for b,w in zip(self.scales,self.weights)),Q(0))
        if triangle**2>gap:
            raise AssertionError("Cauchy-Schwarz source error certificate failed")
        canonical=all(not w or b==1 for b,w in zip(self.scales,self.weights))
        if canonical!=(gap==0):
            raise AssertionError("Within-cone Gaussian rigidity failed")
        return {'C2':self.second_scale_moment,'variance_gap':gap,
                'canonical_gaussian_forced':canonical,
                'certified_L1_error_squared_upper':gap,
                'triangle_L1_error_upper':triangle,
                'fourier_selfdual':self.prove_fourier_selfdual(),
                'scope':'POSITIVE GAUSSIAN SCALE MIXTURES ONLY'}

    def compact_mellin_multiplier_zero_exclusion(self,imag_height:int)->dict:
        """Sufficient, not necessary, no-auxiliary-zero certificate in
        0<=Re(s)<=1, |Im(s)|<=T, for normalized positive scale mixtures.

        For 0<=Re(s)<=2, |C(s)-1| <= 2|s|sqrt(gap)+21 gap,
        via a safe region b in [1/2,3/2], and Chebyshev outside.
        Compare rational squares with |s|<=T+1, without floats.
        NEVER a zero-free claim about canonical xi or zeta.
        """
        if type(imag_height) is not int or imag_height<0 or imag_height>10**9:
            raise ShadowSourceError("Bounded nonnegative imaginary height")
        gap=self.moment_shadow()['variance_gap']
        remainder=1-21*gap
        certified=(remainder>0 and remainder**2 > 4*(imag_height+1)**2*gap)
        return {'certificate':certified,'gap':gap,
                'bound_real_interval':(0,1),'imag_height':imag_height,
                'inequality_left':remainder**2,
                'inequality_right':4*(imag_height+1)**2*gap,
                'scope':'AUXILIARY ARCHIMEDEAN MULTIPLIER ONLY; NO RH CLAIM'}


@dataclass(frozen=True)
class HermiteShadowImpostor:
    """Exact rational noncanonical positive Fourier-selfdual Schwartz source.

    f(x)=G(x)*(1+epsilon*P(pi*x²)); the classical Fourier eigenfunction
    identity guarantees F(f)=f for P in span(H_4j(sqrt(2*y))).
    """
    source_id:str
    polynomial:tuple[Q,...]
    epsilon:Q
    positivity_cutoff:Q
    sampled_moments:tuple[int,...]
    sampled_y:tuple[Q,...]
    modes:tuple[int,...]

    def __post_init__(self):
        if not self.source_id or type(self.polynomial) is not tuple or not self.polynomial:
            raise ShadowSourceError("Nonempty source and perturbation polynomial")
        pp=tuple(rational(v) for v in self.polynomial)
        e=rational(self.epsilon)
        cutoff=rational(self.positivity_cutoff)
        if not any(pp) or pp[-1]<=0 or e<=0 or cutoff<1:
            raise ShadowSourceError("Nontrivial positive-leading perturbation required")
        object.__setattr__(self,'polynomial',pp)
        object.__setattr__(self,'epsilon',e)
        object.__setattr__(self,'positivity_cutoff',cutoff)
        for moment in self.sampled_moments:
            if relative_mellin_polynomial(pp,moment)!=0:
                raise ShadowSourceError("Forged Mellin agreement")
        for x in self.sampled_y:
            if polynomial_eval(pp,x)!=0:
                raise ShadowSourceError("Forged point-probe agreement")
        if pp[0]!=0:
            raise ShadowSourceError("f(0)=1 is not preserved")
        # Given cutoff R>=1, positive leading term dominates lower degrees
        # for y>=R; for 0<=y<=R, bound absolute polynomial by sum |c| R^j.
        degree=len(pp)-1
        if degree<1:
            raise ShadowSourceError("Need nonconstant polynomial")
        lower=sum((abs(c) for c in pp[:-1]),Q(0))
        if pp[-1]*(cutoff-1)<lower:
            raise ShadowSourceError("Unproved positive tail")
        bounded=sum((abs(c)*cutoff**j for j,c in enumerate(pp)),Q(0))
        if e*bounded>Q(1,2):
            raise ShadowSourceError("No uniform positivity margin")

    def checks(self)->dict:
        return {'fourier_eigenvalue':1,'f_at_zero':1,'integral_f':1,
                'finite_mellin_shadow_agreement':tuple(self.sampled_moments),
                'point_shadow_agreement':self.sampled_y,
                'f_lower_bound_ratio_to_gaussian':Q(1,2),
                'perturbation_nonzero':True,
                'canonical_gaussian_forced':False,
                'scope':'FOURIER-EIGENFUNCTION ANALYTIC IDENTITY, EXACT RATIONAL COEFFICIENTS'}

    def ratio_at_y(self,y:Q)->Q:
        if rational(y)<0:
            raise ShadowSourceError("Only y=pi*x*x >=0")
        result=1+self.epsilon*polynomial_eval(self.polynomial,y)
        if result<Q(1,2):
            raise AssertionError("Unconditional positivity proof failed")
        return result


def _first_null_direction(rows:list[tuple[Q,...]],dimension:int)->tuple[Q,...]:
    solved=solve_system(rows,(Q(0),)*len(rows),dimension)
    if solved['status']!='CONSISTENT' or not solved['nullspace']:
        raise ShadowSourceError("Number of Fourier modes did not exceed shadow constraints")
    return tuple(solved['nullspace'][0])


def construct_hermite_impostor(moment_exponents:Iterable[int],
                                sampled_y:Iterable[Q]=(),
                                *,source_id='Hermite-shadow-alternative')->HermiteShadowImpostor:
    """Build f != Gaussian matching any FINITE family of even Mellin
    moments and rational point probes, while f>0, self-Fourier, normalized.
    This is not a proof of universal impossibility for infinite probes.
    """
    moments=tuple(moment_exponents)
    sampled=tuple(rational(v) for v in sampled_y)
    if len(set(moments))!=len(moments) or len(set(sampled))!=len(sampled):
        raise ShadowSourceError("Deduplicate observation types")
    if any(type(m) is not int or m<2 or m%2 for m in moments):
        raise ShadowSourceError("Machine certificates support even positive Mellin probes")
    if any(y<0 for y in sampled):
        raise ShadowSourceError("Point probes use nonnegative y=pi*x²")
    if len(moments)+len(sampled)>18:
        raise ShadowSourceError("Finite research dimension budget exceeded")
    # Include constant H0, then H4,H8... (all Fourier eigenvalue +1).
    number=len(moments)+len(sampled)+3
    if number>25:
        raise ShadowSourceError("Hermite mode resource limit")
    modes=tuple(range(number))
    basis=tuple(hermite_fourier_one(k) for k in modes)
    rows=[]
    rows.append(tuple(p[0] for p in basis))
    rows.extend(tuple(relative_mellin_polynomial(p,m) for p in basis) for m in moments)
    rows.extend(tuple(polynomial_eval(p,y) for p in basis) for y in sampled)
    direction=_first_null_direction(rows,number)
    coefficients=(Q(0),)
    for c,b in zip(direction,basis):
        coefficients=polynomial_add(coefficients,polynomial_scale(b,c))
    while len(coefficients)>1 and coefficients[-1]==0:
        coefficients=coefficients[:-1]
    if not any(coefficients):
        raise AssertionError("Distinct Hermite eigenmodes produced zero polynomial")
    if coefficients[-1]<0:
        coefficients=polynomial_scale(coefficients,Q(-1))
    if coefficients[0]!=0:
        raise AssertionError("Origin sample did not survive")
    lower=sum((abs(c) for c in coefficients[:-1]),Q(0))
    cutoff=1+lower/coefficients[-1]
    bound=sum((abs(c)*cutoff**j for j,c in enumerate(coefficients)),Q(0))
    epsilon=Q(1)/(2*bound)
    return HermiteShadowImpostor(source_id,tuple(coefficients),epsilon,cutoff,
                                moments,sampled,modes)


def explicit_positive_hermite_multiplier(s:Q,
                                         epsilon:Q=Q(1,20_000_000))->Q:
    """Exact Mellin multiplier for positive non-Gaussian selfdual source
    f=G*(1+epsilon*P(pi*x²)) where
    P(y)=1024*y*(4*y³-28*y²+39*y-6).

    Positive for epsilon=1/20_000_000 by elementary polynomial bounds.
    Zeros of multiplier are NOT input zeta zero locations.
    """
    s=rational(s)
    epsilon=rational(epsilon)
    if epsilon!=Q(1,20_000_000):
        raise ShadowSourceError("Only the explicitly certified positive example")
    return 1+256*epsilon*s*(s-1)*(s-2)*(s+1)
