"""Source-authentic prime-power kink geometry ordered by the Hilbert curve.

For Suzuki's genuine signed g(x-y), every true prime-power n=p^k contributes
a hinge (|x-y|-log n)_+. Its nonsmooth loci within [-a,a]^2 are exactly
the lines x-y = +/- log(n). These are CODIMENSION ONE, even though the
operator kernel acts on a two-dimensional (x,y) carrier.

An adaptive dyadic/Hilbert quadtree can certify which cells intersect those
arithmetic wavefronts while never introducing composite n=6 as an independent
Euler place. This is only singular-set/geometric preprocessing: it does not
approximate the smooth pole/contact/Gamma contributions or prove Weil sign.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

from . import source_weil_hierarchy as source
from .hilbert_carrier import HilbertCarrierError,point,index,order_gate

class PrimeWavefrontError(ValueError):
    pass

def _radius(a):
    if type(a) not in (int,Q):raise PrimeWavefrontError("exact rational source radius")
    a=Q(a)
    if not 0<a<=1:raise PrimeWavefrontError("first-window true-source 0<a<=1")
    return a

def box(a,depth,ix,iy):
    a=_radius(a)
    if type(depth) is not int or not 0<=depth<=9:
        raise PrimeWavefrontError("bounded dyadic refinement")
    n=1<<depth
    if any(type(z) is not int or not 0<=z<n for z in (ix,iy)):
        raise PrimeWavefrontError("true dyadic square cell required")
    h=2*a/n
    return (-a+ix*h,-a+(ix+1)*h,-a+iy*h,-a+(iy+1)*h)

def hinge_status(a,depth,ix,iy,n):
    """Interval-certified ACTIVE / INACTIVE / TRANSITION for true p-power."""
    a=_radius(a)
    if type(n) is not int or (n,source.real_prime_power(n)) not in source.AUTHENTIC_TAPE:
        raise PrimeWavefrontError("no independent false prime place or fake 6")
    threshold=source.log_iv(n)
    x0,x1,y0,y1=box(a,depth,ix,iy)
    dl=x0-y1
    dh=x1-y0
    minabs=Q(0) if dl<=0<=dh else min(abs(dl),abs(dh))
    maxabs=max(abs(dl),abs(dh))
    if maxabs<threshold.lo:return "INACTIVE"
    if minabs>threshold.hi:return "ACTIVE"
    return "TRANSITION"

@dataclass(frozen=True)
class WavefrontLeaf:
    depth:int
    x:int
    y:int
    hilbert_start:int
    hilbert_span:int
    statuses:tuple[tuple[int,str],...]

def adaptive_profile(a,order):
    a=_radius(a)
    k=order_gate(order)
    if k>8:raise PrimeWavefrontError("budget k<=8")
    active=source.authenticated_prime_wavefront(a)
    leaves=[]
    def recurse(depth,ix,iy):
        statuses=tuple((n,hinge_status(a,depth,ix,iy,n)) for n,p in active)
        if depth==k or not any(s=="TRANSITION" for n,s in statuses):
            if depth==0: d=0
            else:d=index(depth,ix,iy)
            leaves.append(WavefrontLeaf(
                depth,ix,iy,d*4**(k-depth),4**(k-depth),statuses))
            return
        for dx in (0,1):
            for dy in (0,1):
                recurse(depth+1,2*ix+dx,2*iy+dy)
    recurse(0,0,0)
    ordered=tuple(sorted(leaves,key=lambda v:v.hilbert_start))
    cursor=0
    for leaf in ordered:
        if leaf.hilbert_start!=cursor:
            raise ArithmeticError("Hilbert adaptive subtree overlaps or omits cells")
        cursor+=leaf.hilbert_span
    if cursor!=4**k:
        raise ArithmeticError("adaptive carrier did not cover original full grid")
    transition=tuple(v for v in ordered
        if v.depth==k and any(s=="TRANSITION" for n,s in v.statuses))
    ngrid=1<<k
    if active and len(transition)>8*ngrid*len(active):
        # A single arithmetic kink consists of TWO diagonals; each
        # intersects O(n) cells. The 8n cap includes boundary/interval
        # ambiguities for rigorous true log intervals shorter than h.
        raise ArithmeticError("source wavefront geometric O(N) bound violated")
    total_area=sum(((2*a/(1<<v.depth))**2 for v in ordered),Q())
    if total_area!=(2*a)**2:
        raise ArithmeticError("adaptive leaves change source physical area")
    return {
      "source":"AUTHENTIC_Q_ZETA_PRIME_POWER_HINGES",
      "radius":a,"order":k,"active_true_prime_powers":active,
      "hilbert_ordered_leaves":ordered,
      "adaptive_leaf_count":len(ordered),
      "full_uniform_grid_cell_count":4**k,
      "wavefront_transition_finest_cells":len(transition),
      "certified_transition_O_side_upper":8*ngrid*len(active),
      "original_square_area":total_area,
      "exact_hilbert_prefix_partition":True,
      "smooth_Gamma_pole_contact_quadrature_completed":False,
      "signed_Weil_positive_proved":False,
    }


def absolute_value_diagonal_status(a,depth,ix,iy):
    """g_J(|x-y|) may be nonsmooth at x=y even with NO prime active.

    This is independent of the genuine prime hinges. In particular,
    original |r| contact and finite OU exp(-alpha|r|) are piecewise smooth
    but cannot be treated as one C² formula across the diagonal.
    """
    x0,x1,y0,y1=box(a,depth,ix,iy)
    lo=x0-y1
    hi=x1-y0
    if lo>0:return "POSITIVE_SIDE"
    if hi<0:return "NEGATIVE_SIDE"
    return "DIAGONAL_TRANSITION"

@dataclass(frozen=True)
class CompleteSingularLeaf:
    depth:int
    x:int
    y:int
    hilbert_start:int
    hilbert_span:int
    diagonal_status:str
    true_prime_power_status:tuple[tuple[int,str],...]

def operator_singularity_profile(a,order,J):
    """Adaptive ORIGINAL finite-J Suzuki g_J: diagonal AND all true p-wavefronts.

    The allowed affine/smooth-in-each-cell decomposition is only VALID
    when |x-y| has fixed sign and each (|x-y|-log n)_+ is fixed branch.
    The finite Gamma and pole parts are analytic in r on such cells.
    No actual second-derivative bound, quadrature or sign is returned.
    """
    a=_radius(a)
    k=order_gate(order)
    if k>8:raise PrimeWavefrontError("budget k<=8")
    if type(J) is not int or not 1<=J<=36:
        raise PrimeWavefrontError("genuine finite Gamma source rung cutoff")
    active=source.authenticated_prime_wavefront(a)
    leaves=[]
    def recurse(depth,ix,iy):
        dg=absolute_value_diagonal_status(a,depth,ix,iy)
        ps=tuple((n,hinge_status(a,depth,ix,iy,n)) for n,p in active)
        crossing=(dg=="DIAGONAL_TRANSITION" or
                  any(status=="TRANSITION" for n,status in ps))
        if depth==k or not crossing:
            d=0 if depth==0 else index(depth,ix,iy)
            leaves.append(CompleteSingularLeaf(depth,ix,iy,
                         d*4**(k-depth),4**(k-depth),dg,ps))
            return
        for dx in (0,1):
            for dy in (0,1):
                recurse(depth+1,2*ix+dx,2*iy+dy)
    recurse(0,0,0)
    leaves=tuple(sorted(leaves,key=lambda item:item.hilbert_start))
    next_start=0
    for leaf in leaves:
        if leaf.hilbert_start!=next_start:
            raise ArithmeticError("nonsmooth operator atlas overlaps/misses source")
        next_start+=leaf.hilbert_span
    if next_start!=4**k:
        raise ArithmeticError("source operator quadtree incomplete")
    transition=tuple(leaf for leaf in leaves if leaf.depth==k and
        (leaf.diagonal_status=="DIAGONAL_TRANSITION" or
         any(s=="TRANSITION" for _,s in leaf.true_prime_power_status)))
    n=1<<k
    proven_count_cap=(4+8*len(active))*n
    if len(transition)>proven_count_cap:
        raise ArithmeticError("original source finite wavefront codimension bound failed")
    total_area=sum(((2*a/(1<<v.depth))**2 for v in leaves),Q())
    if total_area!=(2*a)**2:
        raise ArithmeticError("finite Suzuki source carrier area changed")
    return {
        "source":"GENUINE_SUZUKI_G_J_DIAGONAL_PLUS_PRIME_WAVEFRONTS",
        "radius":a,"order":k,"original_Gamma_rungs":J,
        "original_prime_powers":active,
        "ordered_leaves":leaves,
        "leaf_count":len(leaves),
        "uniform_grid_cells":4**k,
        "finest_transition_cell_count":len(transition),
        "analytic_codimension_one_upper":proven_count_cap,
        "total_source_area":total_area,
        "all_declared_nonsmooth_loci_classified":True,
        "rigorous_C2_quadrature_done":False,
        "original_Weil_operator_positive":False,
    }
