"""Exact rational symmetric-function countermodel to finite-jet zero localization.

This deliberately DOES NOT claim to construct the Riemann xi function. The
source class is all rational-coefficient polynomials invariant under s->1-s.
It shows a finite Taylor jet plus a reflection law cannot force zero locations.
"""
from __future__ import annotations
from fractions import Fraction as F


def _complex_mul(x:tuple[F,F],y:tuple[F,F])->tuple[F,F]:
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def _complex_inv(x:tuple[F,F])->tuple[F,F]:
    den=x[0]*x[0]+x[1]*x[1]
    if not den:raise ValueError("Zero Gaussian rational not invertible")
    return (x[0]/den,-x[1]/den)


def _poly_add(x:tuple[F,...],y:tuple[F,...])->tuple[F,...]:
    return tuple((x[i] if i<len(x) else F(0))+(y[i] if i<len(y) else F(0))
                 for i in range(max(len(x),len(y))))


def _poly_mul(x:tuple[F,...],y:tuple[F,...])->tuple[F,...]:
    coeff=[F(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):coeff[i+j]+=a*b
    return tuple(coeff)


def _poly_eval(poly:tuple[F,...],z:tuple[F,F])->tuple[F,F]:
    ans=(F(0),F(0))
    for c in reversed(poly):
        ans=_complex_mul(ans,z)
        ans=(ans[0]+c,ans[1])
    return ans


def symmetric_jet_with_forced_offline_zero(order:int,
      *,real_part:F=F(1,4),imag_part:F=F(1,10))->dict:
    """Construct rational F(s)=F(1-s), whose n-jet at 0 equals 1,
    yet F(z0)=0 at a prescribed nonreal z0 in the open critical strip,
    away from Re(z)=1/2. All proofs use only rational polynomial algebra.
    """
    if type(order) is not int or not 0<=order<=30:
        raise ValueError("Exact finite jet order 0..30 required")
    for a in (real_part,imag_part):
        if type(a) not in (int,F):
            raise ValueError("Only integer/Fraction coordinates, no floats")
    real_part,imag_part=F(real_part),F(imag_part)
    if not 0<real_part<1 or real_part==F(1,2) or imag_part==0:
        raise ValueError("Choose off-critical nonreal z inside the open strip")
    z=(real_part,imag_part)
    one_minus_z=(1-z[0],-z[1])
    g=_complex_mul(z,one_minus_z)
    if g[1]==0:
        raise ValueError("Need a nonreal s(1-s) coordinate")
    inverse=_complex_inv(g)
    h=(F(1),F(0))
    for _ in range(order+1):h=_complex_mul(h,inverse)
    # Solve A+B*g(z0)=g(z0)^(-(order+1)) using rational real A,B.
    B=h[1]/g[1]
    A=h[0]-B*g[0]
    gg=(F(0),F(1),F(-1)) # g(s)=s-s^2
    power=(F(1),)
    for _ in range(order+1):power=_poly_mul(power,gg)
    multiplier=_poly_add((A,),tuple(B*x for x in gg))
    correction=_poly_mul(power,multiplier)
    polynomial=_poly_add((F(1),),tuple(-x for x in correction))
    if polynomial[0]!=1 or any(polynomial[k] for k in range(1,order+1)):
        raise AssertionError("The claimed finite Taylor jet did not match")
    if _poly_eval(polynomial,z)!=(0,0):
        raise AssertionError("Off-critical prescribed zero missing")
    if _poly_eval(polynomial,(1-z[0],-z[1]))!=(0,0):
        raise AssertionError("Reflection symmetry missing at conjugate chart")
    # Verify full symbolic reflection by polynomial substitution s->1-s.
    reflection=(F(0),)
    base=(F(1),)
    for c in polynomial:
        reflection=_poly_add(reflection,tuple(c*v for v in base))
        base=_poly_mul(base,(F(1),F(-1)))
    if reflection!=polynomial:
        raise AssertionError("Polynomial reflection does not hold")
    return {"status":"EXACT_FINITE_JET_REFLECTION_INSUFFICIENT",
            "jet_order":order,"zero_real":real_part,"zero_imag":imag_part,
            "coefficients":polynomial,"auxiliary_A":A,"auxiliary_B":B,
            "other_witness":"reflection at 1-s and conjugation by real coefficients",
            "actual_Riemann_xi_used_or_modified":False}
