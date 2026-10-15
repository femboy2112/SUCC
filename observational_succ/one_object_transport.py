"""Source-faithful finite Weil <-> Suzuki transport and finite Connes clock.

Classical source formulae + exact Fraction contact/valuation certificates.
No nontrivial zero locations, no assumed Weil sign, no RH proof.

The analytic distribution identity for the finite Gamma stage is established
in the paired research proof, not inferred from floating quadrature tests.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, isqrt
from typing import Callable

from .completed_weil_transport import von_mangoldt_labels
from .tate_weil_source_bridge import TateWeilProfile


class OneObjectError(ValueError):
    """Unlawful original source, non-prime place, or untyped test boundary."""


def _int(value: int, lower: int = 0, upper: int = 100_000) -> int:
    if type(value) is not int or not lower <= value <= upper:
        raise OneObjectError("Exact integer outside source/test budget")
    return value


def _fraction(value: int | F, lower: F | None = None) -> F:
    if type(value) not in (int, F):
        raise OneObjectError("Exact integer/Fraction input required")
    value = F(value)
    if lower is not None and value < lower:
        raise OneObjectError("Out-of-domain rational input")
    return value


def _prime(p: int) -> int:
    _int(p, 2, 100_000)
    if any(p % k == 0 for k in range(2, isqrt(p)+1)):
        raise OneObjectError("Composite label is not a Tate local place")
    return p


def contact_rational_increment(J: int) -> F:
    """C_J-C_0 = sum_{j<J} [4/(4j+1)-2/(2j+1)], EXACT.

    C_0=gamma+log(4*pi) is the real-place Weil contact. The infinite
    increment equals pi/2+log(2), giving Suzuki's -psi(1/4)+log(pi).
    """
    _int(J, 0, 512)
    return sum((F(4, 4*j+1)-F(2, 2*j+1) for j in range(J)), F())


def contact_tail_majorant(J: int) -> F:
    """Exact bound for C_infty-C_J and omitted gamma screw potential.

    Both positive tails <= 1/4 * [1/(J+1/4)+1/(J+1/4)^2].
    Uses monotone integral + first-term bound for 1/(j+1/4)^2.
    """
    _int(J, 1, 512)
    q=F(J)+F(1, 4)
    return F(1, 4)*(1/q+1/(q*q))


def screw_uniform_tail_majorant(J: int, radius: int | F) -> F:
    """On |t|<=radius, |g(t)-g_J^aligned(t)| <= (1+radius/2) B_J.

    Here g_J^aligned uses the finite-stage contact C_J, not Suzuki's
    infinite contact with a truncated Gamma ladder. This distinction is
    necessary for the exact finite Weil/screw commuting square.
    """
    r = _fraction(radius, F())
    return (1+r/2)*contact_tail_majorant(J)


def original_prime_atoms(radius: int | F) -> tuple[tuple[int,int], ...]:
    """Actual source cutoff: n=p^k with log(n)<radius, with real threshold.

    This routine is numerical only for the cutoff decision; it rejects a
    near-threshold decision unless separated at the requested precision.
    Source authenticity (n=p^k) comes from the existing original tape.
    """
    r=_fraction(radius, F())
    if r>8:
        raise OneObjectError("Compact demonstration radius <=8")
    import mpmath as mp
    with mp.workdps(85):
        rr=mp.mpf(r.numerator)/r.denominator
        ceiling=int(mp.ceil(mp.exp(rr)))+1
        if ceiling>200000:
            raise OneObjectError("Bounded original-source prime-power horizon")
        all_atoms=von_mangoldt_labels(max(2,ceiling))
        selected=[]
        for n,p in all_atoms:
            d=mp.log(n)-rr
            if abs(d)<mp.mpf('1e-65'):
                raise OneObjectError("Prime wavefront touches uncertified cutoff")
            if d<0:
                selected.append((n,p))
        return tuple(selected)


def _mp(dps: int):
    _int(dps, 40, 160)
    import mpmath as mp
    mp.mp.dps=dps
    return mp


def _mfrac(mp, f: F):
    return mp.mpf(f.numerator)/f.denominator


def even_bump(t, radius: int | F):
    """(1-(t/R)^2)^3 on |t|<R, zero outside; real C_c^2."""
    r = _fraction(radius, F(1, 100))
    import mpmath as mp
    R=_mfrac(mp,r)
    x=_mfrac(mp,t) if type(t) in (int,F) else mp.mpf(t)
    return (1-(x/R)**2)**3 if abs(x)<R else mp.mpf(0)


def even_bump_second(t, radius: int | F):
    """Exact polynomial for the second derivative of even_bump."""
    r=_fraction(radius, F(1, 100))
    import mpmath as mp
    R=_mfrac(mp,r)
    x=_mfrac(mp,t) if type(t) in (int,F) else mp.mpf(t)
    if abs(x)>=R:
        return mp.mpf(0)
    u=(x/R)**2
    return (-6+36*u-30*u*u)/(R*R)


def _stage_constants(mp, radius: F, J: int):
    R=_mfrac(mp,radius)
    atoms=tuple((mp.log(n),mp.log(p)/mp.sqrt(n)) for n,p in original_prime_atoms(radius))
    C0=mp.euler+mp.log(4*mp.pi)
    CJ=C0+_mfrac(mp,contact_rational_increment(J))
    return R,atoms,C0,CJ


def _aligned_screw(mp, t, atoms, CJ, J):
    """Finite source Suzuki primitive with CONTACT EXACTLY MATCHED to W_J."""
    x=abs(mp.mpf(t))
    pole=-4*(mp.exp(x/2)+mp.exp(-x/2)-2)
    prime=mp.fsum(w*(x-b) for b,w in atoms if b<x)
    gamma=-mp.fsum(mp.mpf(4)/(4*j+1)**2*(1-mp.exp(-(4*j+1)*x/2)) for j in range(J))
    return pole+CJ*x/2+prime+gamma


def stage_identity_bump(radius: int | F, J: int, dps: int = 65,
                        screw_contact_mutation: int | F = 0) -> dict:
    """Independent quadratures of finite Weil W_J and -<g_J,h''>.

    Tests numerical equality of two analytically derived classical forms;
    the residual is NOT an outward-rounded theorem certificate.
    """
    r=_fraction(radius,F(1,100))
    if r>F(4):
        raise OneObjectError("Numerical calibration radius <=4")
    _int(J,0,64)
    mp=_mp(dps)
    R,atoms,C0,CJ=_stage_constants(mp,r,J)
    mutation=_fraction(screw_contact_mutation)
    CJ+=_mfrac(mp,mutation)
    h=lambda x:even_bump(x,r)
    h2=lambda x:even_bump_second(x,r)
    knots=[mp.mpf(0)]+[b for b,_ in atoms]+[R]
    knots=sorted(set(knots))
    pole=2*mp.quad(lambda x:h(x)*(mp.exp(x/2)+mp.exp(-x/2)),[0,R])
    prime=-2*mp.fsum(w*h(b) for b,w in atoms)
    arch=-C0
    for j in range(J):
        alpha=mp.mpf(4*j+1)/2
        arch+=mp.mpf(2)/(2*j+1)-2*mp.quad(lambda x:mp.exp(-alpha*x)*h(x),[0,R])
    W=pole+prime+arch
    primitive=-2*mp.quad(lambda x:_aligned_screw(mp,x,atoms,CJ,J)*h2(x),knots)
    residual=W-primitive
    return {"radius":str(r),"gamma_rungs":J,
            "prime_atoms":tuple(n for n,_ in original_prime_atoms(r)),
            "weil":mp.nstr(W,32),"suzuki":mp.nstr(primitive,32),
            "residual":mp.nstr(residual,12),
            "residual_abs":abs(residual),"dps":dps,
            "contact_mutation":str(mutation),
            "original_contact":mutation==0,
            "RH_proved":False}


def analytic_shift_no_go(test_point: int | F, impulse_position: int | F,
                          added_weight: int | F) -> dict:
    """Exact fake-source obstruction: a commuting square need not be positive.

    Mutant W=-w(delta_b+delta_-b), g(t)=w(|t|-b)_+.
    Then K_g(t,t)=-2w(t-b)<0 for any t>b and w>0.
    """
    t=_fraction(test_point,F())
    b=_fraction(impulse_position,F())
    w=_fraction(added_weight,F())
    if not t>b>0 or w<=0:
        raise OneObjectError("Explicit strictly positive synthetic impulse beyond threshold")
    diag=-2*w*(t-b)
    return {"mutant":"single_non_Euler_signed_prime_impulse",
            "gram_diagonal":diag,"distribution_to_primitive_commutes":True,
            "hilbert_factorization_possible":False,"authentic_zeta":False}


def anchored_kernel(g: Callable[[F], F], x: int | F, y: int | F) -> F:
    """Source-free exact algebra control, not a claimed original Weil Gram."""
    a,b=_fraction(x),_fraction(y)
    terms=(g(abs(a-b)),g(abs(a)),g(abs(b)),g(F()))
    if any(type(z) not in (int,F) for z in terms):
        raise OneObjectError("Algebraic calibration kernel must be exact rational")
    return F(terms[0])-F(terms[1])-F(terms[2])+F(terms[3])


def gram_two_point_determinant(g: Callable[[F],F], x: int | F, y: int | F) -> F:
    a=anchored_kernel(g,x,x)
    b=anchored_kernel(g,y,y)
    c=anchored_kernel(g,x,y)
    return a*b-c*c


def _unit(p: int, u: int):
    _prime(p)
    _int(abs(u),0,1_000_000)
    if type(u) is not int or gcd(p,u)!=1:
        raise OneObjectError("Scaling residue must be a unit at a genuine place")


def connes_finite_clock_trace(p:int,depth:int,unit:int) -> int:
    """Trace of the permutation of Z/p^depth induced by x -> unit*x.

    The same trace occurs on its Fourier-dual character basis. This
    finite-dimensional equality is NOT the global adele-class trace formula.
    """
    _unit(p,unit)
    _int(depth,1,12)
    if p**depth>200_000:
        raise OneObjectError("Finite clock dimension ceiling")
    return gcd(unit-1,p**depth)


def connes_local_fixed_point_factor(p:int,unit:int) -> int:
    """For unit !=1, stabilized finite trace = |1-unit|_p^-1.

    At the identity the finite clock trace grows without bound; the
    singular distribution requires separate analytic regularization.
    """
    _unit(p,unit)
    if unit==1:
        raise OneObjectError("Identity scaling is singular; not a finite trace")
    t=abs(unit-1)
    v=0
    while t%p==0:
        t//=p
        v+=1
    return p**v


def connes_trace_stabilization(p:int,unit:int,max_depth:int=6) -> dict:
    _unit(p,unit)
    _int(max_depth,1,12)
    if p**max_depth>200_000:
        raise OneObjectError("Finite clock dimension ceiling")
    stages=tuple(connes_finite_clock_trace(p,r,unit) for r in range(1,max_depth+1))
    stable=None if unit==1 else connes_local_fixed_point_factor(p,unit)
    return {"place":p,"scaling_unit":unit,"traces":stages,
            "stabilized_local_factor":stable,
            "trace_unbounded_in_depth_if_unit_one":unit==1,
            "global_adelic_trace_identified":False,"RH_proved":False}



def sonin_compact_defect_countermodel(index: int) -> dict:
    """Exact rank-one no-go for the tempting 'positive trace+compact defect' shortcut.

    In the finite subspace of ℓ²(N), T=diag(2^-k) is positive;
    rank-one D=-2*2^-index |e_index><e_index| is self-adjoint compact.
    T+D has the NEGATIVE eigenvalue -2^-index. Moreover ||D||=2^(1-index)
    tends to zero as index grows, so arbitrarily small compact corrections
    can invert sign in directions without a uniform positive gap.

    THIS IS A SYNTHETIC HILBERT COUNTERMODEL, NOT CONNES/WEIL SOURCE DATA.
    """
    n=_int(index,1,128)
    t=F(1,2**n)
    d=-2*t
    return {"index":n,"positive_trace_diagonal":t,
            "rank_one_defect":d,"combined_signed_eigenvalue":t+d,
            "defect_norm":-d,"defect_rank":1,
            "compactness_implies_Weil_sign":False,
            "original_zeta_source":False,"RH_proved":False}



def sonin_log_moment_annihilator(weight: int | F,
                                derivative_coefficient: int | F = F(1, 2)) -> F:
    """Exact local differential source map into the two Sonin moment nulls.

    For phi in Cc^infty(R), v=phi''+c phi' has the SAME compact support;
      integral e^(weight*x) v(x) dx
        = weight*(weight-c) integral e^(weight*x) phi(x) dx
    by two integrations by parts. In particular c=1/2 annihilates
    weights 0 and 1/2, equivalent to additive Fourier zeros z=0,i/2
    under the explicit convention hat(v)(z)=int v(x)exp(-izx)dx.
    Pure coefficient algebra; NO source Weil sign or global Sonin trace.
    """
    lam=_fraction(weight)
    c=_fraction(derivative_coefficient)
    return lam*(lam-c)
