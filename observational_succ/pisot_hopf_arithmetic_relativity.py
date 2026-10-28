"""Exact arithmetic clock defects, Pisot returns, and quaternionic Hopf curvature.

Research only. The quaternionic structure is an OBSERVER on the original
Q(i)⊕Q(i) chiral BBP source; it does not change its multiplication or seed.
All fractions are exact. A nonzero gauge or clock defect is not spacetime
curvature, gravitational dilation, a π-normality proof, or physical simultaneity.

See research/2026-10-28/pisot_relativistic_geometry/ARITHMETIC_RELATIVITY_DOSSIER.md.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache

from .hopf_source_exact import (H, ONE, ZERO, SOURCE_ORIGIN, t_step, t_iter,
                                original_forcing, unwrapped_zero_seed)


def _positive_integer(n: int, field: str, *, at_least: int = 1) -> int:
    if type(n) is not int or n < at_least:
        raise ValueError(f"{field} must be an integer >= {at_least}")
    return n


@lru_cache(maxsize=10000)
def harmonic_clock_at(n: int) -> F:
    """Clock τ_H(n)=H_(n-1) on the integer source n>=1."""
    _positive_integer(n, "n")
    return sum((F(1, k) for k in range(1, n)), F(0))


def harmonic_succ_tick(n: int) -> F:
    _positive_integer(n, "n")
    return F(1, n)


def harmonic_prime_tick(n: int, p: int) -> F:
    """EXACT integrable prime edge from H_(n-1) to H_(pn-1)."""
    _positive_integer(n, "n")
    _positive_integer(p, "p", at_least=2)
    return sum((F(1, j) for j in range(n, p*n)), F(0))


def harmonic_dilation_braid_defect(n: int, p: int) -> F:
    """Nonzero clock mismatch if succ tick=1/n but dilation tick=log(p).

    The log(p) prime edges cancel between the two affine-braid paths.
    Returns Σ_(j=1)^(p-1) j / (p*n*(p*n+j)) > 0.
    """
    _positive_integer(n, "n")
    _positive_integer(p, "p", at_least=2)
    return sum((F(j, p*n*(p*n+j)) for j in range(1, p)), F(0))


def harmonic_dilation_braid_direct(n: int, p: int) -> F:
    _positive_integer(n, "n")
    _positive_integer(p, "p", at_least=2)
    return F(1, n)-sum((F(1, p*n+j) for j in range(p)), F(0))


def braid_defect_bounds(n: int, p: int) -> tuple[F,F,F]:
    """Lower, sharp leading term, and error envelope as n->∞.

    lower <= D < leading, and 0 < leading-D <= remainder.
    """
    _positive_integer(n, "n")
    _positive_integer(p, "p", at_least=2)
    lo=F(p-1, 2*n*(p*n+p-1))
    leading=F(p-1, 2*p*n*n)
    remainder=F((p-1)*(2*p-1), 6*p*p*n*n*n)
    return lo,leading,remainder


def integrable_braid_defect(n: int, p: int) -> F:
    """All squares close when prime tick is H_(pn-1)-H_(n-1)."""
    _positive_integer(n,"n")
    _positive_integer(p,"p",at_least=2)
    return (
        harmonic_succ_tick(n)
        +harmonic_prime_tick(n+1,p)
        -harmonic_prime_tick(n,p)
        -sum((harmonic_succ_tick(p*n+j) for j in range(p)), F(0))
    )


def lagged_harmonic_log_defect(n: int) -> F:
    """H_n is rational; subtract log(n+1) externally to obtain gamma limit.

    Output H_n alone, to allow exact comparison with independent log clocks.
    """
    _positive_integer(n,"n",at_least=0)
    return harmonic_clock_at(n+1)


def pisot_quadratic_coefficients(m: int, k: int) -> tuple[int,int]:
    """β_m^k=a_k β_m+b_k, β_m²=mβ_m+1. Exact Z arithmetic."""
    _positive_integer(m,"m")
    _positive_integer(k,"k",at_least=0)
    a,b=0,1
    # (a,b) represents β^0=1; multiply by β: aβ+b -> (m*a+b)β+a
    for _ in range(k):
        a,b=m*a+b,a
    return a,b


def pisot_quadratic_trace(m: int, k: int) -> int:
    """Tr(β_m^k) ∈ Z; companion root β_m'=-1/β_m."""
    _positive_integer(m,"m")
    _positive_integer(k,"k",at_least=0)
    if k==0:return 2
    if k==1:return m
    a,b=2,m
    for _ in range(2,k+1):
        a,b=b,m*b+a
    return b


def chiral_eight_step_sync(x: H, n: int) -> bool:
    """Source-exact dual clock identity 16^n T^(8n)x=x (n>=0)."""
    _positive_integer(n,"n",at_least=0)
    if n>100:return False  # validation budget, no theorem inference
    return t_iter(x,8*n).scale(F(16**n))==x


def pure_imag(q: H) -> H:
    return H(0,q.b,q.c,q.d)


def hopf_local_connection(x: H, v: H) -> H:
    """Canonical right Hopf/Sp(1) instanton chart A_x(v)=Im(conj(x)v)/(1+||x||²)."""
    return pure_imag(x.conj()*v).scale(F(1,1+x.norm2()))


def hopf_curvature_origin(v: H,w: H) -> H:
    """F_0(v,w)=2 Im(conj(v)w), exact curvature of canonical connection."""
    return pure_imag(v.conj()*w-w.conj()*v)


def hopf_section_link(x: H,y: H) -> H:
    """Unnormalized quaternionic overlap of (x,1) and (y,1): 1+conj(x)y.

    Valid rational link for specified gauge only. Holonomy magnitude/real parts
    can be normalized separately; overall positive scale does not affect angle.
    """
    return ONE+x.conj()*y


def hopf_wilson_rectangle(v: H, w: H, eps: F) -> H:
    """Exact overlap product for 0,eps*v,eps*(v+w),eps*w,0.

    Product transforms by conjugation under changes of local right gauge;
    its scalar part is gauge-invariant. This is a controlled two-parameter
    source span, NOT the realized one-dimensional BBP orbit.
    """
    eps=F(eps)
    if not 0<eps<=F(1,2):raise ValueError("0<eps<=1/2 required")
    v0=ZERO
    v1=v.scale(eps)
    v2=(v+w).scale(eps)
    v3=w.scale(eps)
    return (hopf_section_link(v0,v1)*hopf_section_link(v1,v2)*
            hopf_section_link(v2,v3)*hopf_section_link(v3,v0))


def hopf_wilson_rectangle_reverse(v:H,w:H,eps:F)->H:
    eps=F(eps)
    if not 0<eps<=F(1,2):raise ValueError("0<eps<=1/2 required")
    v0=ZERO;v1=v.scale(eps);v2=(v+w).scale(eps);v3=w.scale(eps)
    return (hopf_section_link(v0,v3)*hopf_section_link(v3,v2)*
            hopf_section_link(v2,v1)*hopf_section_link(v1,v0))


def source_curvature_probe() -> H:
    """Nonzero SU2 curvature on the DECLARED plane span(b,Tb) at x=0."""
    return hopf_curvature_origin(SOURCE_ORIGIN,t_step(SOURCE_ORIGIN))


def source_clock_latitude_energy(n: int) -> F:
    """Source-chart B_n=(||T^n b||²-1)/(||T^n b||²+1)."""
    _positive_integer(n,"n",at_least=0)
    E=F(4,2**n)
    return (E-1)/(E+1)


def source_clock_latitude_step(B: F) -> F:
    """Möbius/rapidity recurrence B'=(3B-1)/(3-B)."""
    B=F(B)
    if not -1<=B<=1:raise ValueError("B must lie in [-1,1]")
    return (3*B-1)/(3-B)


def source_prime_frame_commutator(n: int,p: int) -> F:
    """Commutator on REAL BBP state variable u, not integer clock n.

    At time n: S_n(u)=16u+r(n+1), V_p(u)=p*u. Then
    V_p(S_n(u))-S_n(V_p(u))=(p-1)*r(n+1), for every u.
    Declared source frame transform is not an intrinsic Lorentz boost.
    """
    _positive_integer(n,"n",at_least=0)
    _positive_integer(p,"p",at_least=2)
    return (p-1)*original_forcing(n+1)


def source_prime_frame_commutator_direct(n: int,p: int, u:F=F(0))->F:
    _positive_integer(n,"n",at_least=0)
    _positive_integer(p,"p",at_least=2)
    u=F(u)
    r=original_forcing(n+1)
    return p*(16*u+r)-(16*p*u+r)


def zero_seed_compact_clock(n: int) -> F:
    """π/16-directed, source-selected Zeno coordinate U_n/16^n.

    Its first difference r(n)/16^n is exact; its limit π/16 uses the
    original BBP identity and is NOT normality.
    """
    _positive_integer(n,"n",at_least=0)
    if n>256:raise ValueError("finite original zero seed budget")
    return unwrapped_zero_seed(n)/F(16**n)


def zero_seed_compact_clock_tick(n: int)->F:
    _positive_integer(n,"n")
    return original_forcing(n)/F(16**n)
