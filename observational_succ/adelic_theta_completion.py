"""Source-factored Euler/Gamma bridge with exact finite receipts.

The analytic Tate/Poisson/theta functional equation is proved IN THE DOSSIER
using classical harmonic analysis, not by sampling finitely many points.
Machine-executable statements here: exact local Euler factors, rational pi
brackets from a Machin identity, interval enclosure of Lambda(2), mutation
witnesses and high-precision theta diagnostics (explicitly NON-certificates).
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

from .diagonal_adele_zeta import DiagonalSourceError, local_euler_product, prime, rational


def atan_reciprocal_bracket(denominator:int,terms:int)->tuple[F,F]:
    """Alternating atan series on 0<1/denominator<=1, rational bracket."""
    if type(denominator) is not int or denominator<1 or type(terms) is not int or terms<1:
        raise DiagonalSourceError("Positive integer reciprocal and term count needed")
    z=F(1,denominator)
    cur=sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    next_term=(-1)**terms*z**(2*terms+1)/F(2*terms+1)
    return min(cur,cur+next_term),max(cur,cur+next_term)


def pi_machin_bracket(terms:int=6)->tuple[F,F]:
    """pi=16 atan(1/5)-4 atan(1/239); exact rational intervals.

    Machin identity follows by checking
    (5+i)^4/(239+i) has argument pi/4 and all angles are in range.
    """
    a,aa=atan_reciprocal_bracket(5,terms)
    b,bb=atan_reciprocal_bracket(239,terms)
    lo,hi=16*a-4*bb,16*aa-4*b
    if not F(3)<lo<hi<F(4):
        raise AssertionError("Incorrect rational Machin interval")
    return lo,hi


def gamma_factor_at_even(s:int)->dict:
    """Exact symbolic real-place Gaussian Mellin factor at s=2k>0.

    Z_infty(s)=pi^(-s/2) Gamma(s/2). At s=2k this is (k-1)!/pi^k.
    No numerical Gamma approximation or statement beyond this domain.
    """
    if type(s) is not int or s<2 or s%2:
        raise DiagonalSourceError("Only positive even Mellin indices implemented")
    return {"s":s,"coefficient":F(factorial(s//2-1)),"pi_power":-(s//2),
            "test_function":"exp(-pi*x*x)",
            "normalized_multiplicative_measure":"dx/abs(x)"}


def completed_s2_interval(prime_cutoff:int,pi_terms:int=8)->dict:
    """Exact rational interval for Lambda(2)=zeta(2)/pi.

    Finite Euler product is in its ABSOLUTE convergence region, with a
    rigorous universal prime-tail multiplier (P+1)/P. Pi interval is
    rigorous from alternating atan bounds. No zeros or FE assumed.
    """
    product=local_euler_product(prime_cutoff,2)
    lo_pi,hi_pi=pi_machin_bracket(pi_terms)
    lower=product['lower']/hi_pi
    upper=product['upper']/lo_pi
    if not 0<lower<=upper:
        raise AssertionError("Invalid arch completion interval")
    return {"s":2,"prime_cutoff":prime_cutoff,"pi_terms":pi_terms,
            "euler_lower":product['lower'],"euler_upper":product['upper'],
            "pi_lower":lo_pi,"pi_upper":hi_pi,"lambda_lower":lower,
            "lambda_upper":upper,"gamma_symbolic":gamma_factor_at_even(2),
            "continuation_claimed":False,"RH_claimed":False}


def deleted_euler_factor_asymmetry(p:int,s:int)->dict:
    """Multiplying a symmetric Lambda by 1-p^-s breaks s<->1-s.

    Not an unconditional independent derivation of the zeta FE;
    it is an exact source-mutation test *conditional* on the classical FE.
    """
    if not prime(p) or type(s) is not int or s in (0,1):
        raise DiagonalSourceError("True prime and integer s not in {0,1} required")
    lhs=1-F(p)**(-s)
    rhs=1-F(p)**(-(1-s))
    return {"p":p,"s":s,"left_mutation":lhs,"dual_mutation":rhs,
            "noncommuting_factor":lhs-rhs,"preserves_unmodified_completion":lhs==rhs}


def theta_poisson_diagnostic(t:str="2",terms:int=12,digits:int=70)->dict:
    """High-precision experimental theta transform, NEVER a formal certificate.

    The universally valid theta identity follows analytically from Poisson
    summation on R; finitely many mpmath values cannot prove it.
    """
    if type(terms) is not int or terms<1 or terms>100:
        raise DiagonalSourceError("Finite theta truncation 1..100 required")
    if type(digits) is not int or not 30<=digits<=200:
        raise DiagonalSourceError("Precision outside diagnostic budget")
    import mpmath as mp
    with mp.workdps(digits):
        x=mp.mpf(t)
        if x<=0:
            raise DiagonalSourceError("Heat parameter t must be positive")
        theta=lambda u:1+2*mp.fsum(mp.exp(-mp.pi*n*n*u) for n in range(1,terms+1))
        direct=theta(x)
        dual=theta(1/x)/mp.sqrt(x)
        return {"t":str(x),"direct_theta":mp.nstr(direct,35),
                "dual_theta":mp.nstr(dual,35),
                "absolute_truncation_residual":mp.nstr(abs(direct-dual),12),
                "formal_error_interval_provided":False,
                "analytic_identity_proved_by_code":False}


def lambda_theta_diagnostic(s:str="2",terms:int=9,digits:int=65)->dict:
    """Compare pole-subtracted theta integral with Gamma*zeta at example s.

    The proof of the integral identity and entire continuation is analytic,
    supplied in the dossier. Numeric residual is NOT a proof certificate.
    """
    if type(terms) is not int or terms<3 or terms>30 or type(digits) is not int or not 30<=digits<=150:
        raise DiagonalSourceError("Unsupported numeric diagnostic budget")
    import mpmath as mp
    with mp.workdps(digits):
        if 'j' in s:
            c=complex(s)  # numerical diagnostic only; not an exact representation
            val=mp.mpc(str(c.real),str(c.imag))
        else:
            val=mp.mpf(s)
        if abs(val)<mp.mpf('1e-25') or abs(val-1)<mp.mpf('1e-25'):
            raise DiagonalSourceError("Pole-subtracted form excludes s=0,1")
        rho=lambda u:2*mp.fsum(mp.exp(-mp.pi*n*n*u) for n in range(1,terms+1))
        integral=lambda z:mp.quad(lambda u:rho(u)*u**(z/2-1),[1,mp.inf])
        cont=1/(val-1)-1/val + (integral(val)+integral(1-val))/2
        source=mp.power(mp.pi,-val/2)*mp.gamma(val/2)*mp.zeta(val)
        return {"s":str(s),"continuation_value":mp.nstr(cont,32),
                "zeta_gamma_value":mp.nstr(source,32),
                "symmetry_residual":mp.nstr(abs(cont-(1/((1-val)-1)-1/(1-val)+(integral(1-val)+integral(val))/2)),10),
                "source_match_residual":mp.nstr(abs(cont-source),12),
                "numeric_diagnostic_not_proof":True}


def normalized_self_dual_gaussian_pair(root_scale:F,s:int=2)->dict:
    """Exact, nonunique archimedean self-dual Schwartz source family.

    For r>0 rational and a=r^2, set
      f_r(x)=(exp(-pi*a*x*x)+r^-1 exp(-pi*x*x/a))/(1+r^-1).
    The real Fourier transform swaps the two Gaussians; f_r is positive,
    self-dual, f_r(0)=integral f_r=1, even Schwartz. Its Mellin factor is
      Z_inf(f_r,s)=pi^-s/2 Gamma(s/2) C_r(s)
      C_r(s)=(r^-s+r^(s-1))/(1+r^-1), C_r(s)=C_r(1-s).
    At r=2, C(2)=C(-1)=3/2 while C(0)=C(1)=1. Thus even self-duality,
    common Euler factors and pole normalization DO NOT determine the
    classical standard completion uniquely.

    This routine certifies rational prefactors at integer s and records
    the analytic Fourier/Gamma identities as separately proved statements.
    """
    r=rational(root_scale)
    if r<=0 or type(s) is not int:
        raise DiagonalSourceError("Positive rational root scale and integer s required")
    C=lambda z:(r**(-z)+r**(z-1))/(1+1/r)
    cs=C(s)
    dual=C(1-s)
    if cs!=dual or C(0)!=1 or C(1)!=1:
        raise AssertionError("Fourier-symmetric prefactor invalid")
    return {"root_scale":r,"scale_square":r*r,"mellin_index":s,
            "normalized_first_gaussian_weight":1/(1+1/r),
            "normalized_second_gaussian_weight":(1/r)/(1+1/r),
            "mellin_relative_to_standard":cs,
            "reflection_partner_relative":dual,
            "pole_zero_normalization_C0":C(0),
            "pole_one_normalization_C1":C(1),
            "claimed_Fourier_self_dual":True,
            "analytic_identity_requires_Gaussian_Fourier_theorem":True,
            "coincides_with_standard_mellin_at_s":cs==1}
