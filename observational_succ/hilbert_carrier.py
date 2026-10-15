"""Hilbert-SUCC: exact dyadic space-filling observation and quadrature instruments.

Mathematical source: canonical 2D Hilbert ordering of 4^k dyadic square cells
and source-declared rational polynomials. The *limit* is a classical
continuous measure-preserving surjection [0,1] -> [0,1]^2 (not a finite
path, not an injective map, not a bi-Lipschitz/Sobolev equivalence).

No physical supertask, source-free completeness, Hilbert-space covariance,
or completed-Weil positivity is inferred by this finite executable module.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

class HilbertCarrierError(ValueError):
    pass

def exact(v):
    if type(v) not in (Q,int):
        raise HilbertCarrierError("exact rational/integer input required")
    return Q(v)

def order_gate(k):
    if type(k) is not int or not 1<=k<=12:
        raise HilbertCarrierError("positive finite 2D Hilbert order 1..12")
    return k

def index_gate(order,index):
    k=order_gate(order)
    if type(index) is not int or not 0<=index<4**k:
        raise HilbertCarrierError("finite Hilbert index out of range")
    return k,index

def _rot(size,x,y,rx,ry):
    if not ry:
        if rx:
            x=size-1-x
            y=size-1-y
        x,y=y,x
    return x,y

def point(order,index):
    """Canonical Hilbert d->(x,y), order k visits all 2^k x 2^k cells."""
    k,d=index_gate(order,index)
    n=1<<k
    x=y=0
    step=1
    while step<n:
        rx=(d//2)&1
        ry=(d^rx)&1
        x,y=_rot(step,x,y,rx,ry)
        x+=step*rx
        y+=step*ry
        d//=4
        step*=2
    if not 0<=x<n or not 0<=y<n:
        raise ArithmeticError("Hilbert source left original square")
    return x,y

def index(order,x,y):
    """Independent inverse by MSB-to-LSB Hilbert coordinate traversal."""
    k=order_gate(order)
    n=1<<k
    if any(type(v) is not int or not 0<=v<n for v in (x,y)):
        raise HilbertCarrierError("exact grid coordinates required")
    d=0
    step=n//2
    while step:
        rx=1 if x&step else 0
        ry=1 if y&step else 0
        d+=step*step*((3*rx)^ry)
        x,y=_rot(step,x,y,rx,ry)
        step//=2
    return d

def time_cell(order,d):
    """Half-open 4-adic interval closure for ONE original finite cell."""
    k,d=index_gate(order,d)
    size=4**k
    return Q(d,size),Q(d+1,size)

def spatial_cell(order,d):
    """Closed dyadic square; overlapping boundaries have measure zero."""
    k,d=index_gate(order,d)
    x,y=point(k,d)
    n=1<<k
    return (Q(x,n),Q(x+1,n)),(Q(y,n),Q(y+1,n))

def center(order,d):
    k,d=index_gate(order,d)
    x,y=point(k,d)
    n=1<<k
    return Q(2*x+1,2*n),Q(2*y+1,2*n)

def prefix_square(fine_order,index,coarse_order):
    """Original Hilbert orientation forces 4-adic cylinders to dyadic tiles."""
    fine_order,d=index_gate(fine_order,index)
    if type(coarse_order) is not int or not 1<=coarse_order<=fine_order:
        raise HilbertCarrierError("nested finite prefix 1<=coarse<=fine")
    parent_index=d//(4**(fine_order-coarse_order))
    parent_point=point(coarse_order,parent_index)
    x,y=point(fine_order,d)
    scale=1<<(fine_order-coarse_order)
    if (x//scale,y//scale)!=parent_point:
        raise ArithmeticError("Hilbert parent-child source cylinder mismatch")
    return {
        "fine_order":fine_order,
        "coarse_order":coarse_order,
        "source_index":d,
        "parent_index":parent_index,
        "parent_cell":parent_point,
        "child_count_per_parent":4**(fine_order-coarse_order),
        "coherent_dyadic_source":True,
    }

def coverage(order,*,max_order=7):
    """Finite exhaustive exact certificate; all cells visited once and adjacent."""
    k=order_gate(order)
    if k>max_order:
        raise HilbertCarrierError("exhaustive coverage budget must be explicit")
    n=1<<k
    seen=set()
    previous=None
    jumps=0
    for d in range(n*n):
        p=point(k,d)
        if p in seen:
            raise ArithmeticError("Hilbert path repeats a finite source cell")
        seen.add(p)
        if previous is not None:
            step=abs(p[0]-previous[0])+abs(p[1]-previous[1])
            if step!=1:
                raise ArithmeticError("nonadjacent Hilbert step")
            jumps=max(jumps,step)
        previous=p
    if len(seen)!=n*n:
        raise ArithmeticError("missing source cells")
    return {
        "order":k,"cells":n*n,"grid_side":n,
        "each_cell_visited_once":True,"maximum_l1_consecutive_jump":jumps,
        "dyadic_cell_area":Q(1,n*n),
        "matched_4adic_time_interval_length":Q(1,n*n),
        "finite_centers_cover_continuum":False,
        "limit_surjection_classical_theorem_not_finite_empirical_test":True,
    }

def raster_jump(order):
    k=order_gate(order)
    return 1<<k  # end-of-row (n-1,y) to (0,y+1) has L1 distance n

def adjacent_parameter_far_apart(order):
    """Spatial neighbors can be distant in 1D order; inverse locality fails."""
    k=order_gate(order)
    if k>7:raise HilbertCarrierError("exhaustive inverse-locality test budget")
    n=1<<k
    inv={(x,y):index(k,x,y) for x in range(n) for y in range(n)}
    best=(0,(0,0),(0,0))
    for x in range(n):
        for y in range(n):
            for nx,ny in ((x+1,y),(x,y+1)):
                if nx>=n or ny>=n:continue
                gap=abs(inv[(x,y)]-inv[(nx,ny)])
                if gap>best[0]:best=(gap,(x,y),(nx,ny))
    return {
        "order":k,
        "max_index_separation_of_spatial_edge_neighbors":best[0],
        "witness_cells":(best[1],best[2]),
        "witness_times":(Q(inv[best[1]],n*n),Q(inv[best[2]],n*n)),
        "inverse_locality_globally_guaranteed":False,
    }

@dataclass(frozen=True)
class RationalPolynomial:
    """Original DECLARED source polynomial on the entire unit square."""
    source_id:str
    epoch:int
    terms:tuple[tuple[int,int,Q],...]
    basis:str="CARTESIAN_DYADIC"

    def __post_init__(self):
        if (type(self.source_id) is not str or not self.source_id.strip()
            or type(self.epoch) is not int or self.epoch<0
            or self.basis!="CARTESIAN_DYADIC"):
            raise HilbertCarrierError("original polynomial source/epoch/basis")
        if type(self.terms) is not tuple or not self.terms or len(self.terms)>30:
            raise HilbertCarrierError("nonempty 30-term finite source")
        seen=set()
        for t in self.terms:
            if type(t) is not tuple or len(t)!=3:
                raise HilbertCarrierError("exact source monomial triples required")
            i,j,c=t
            if (type(i) is not int or type(j) is not int
                or not 0<=i<=8 or not 0<=j<=8 or type(c) not in (Q,int)):
                raise HilbertCarrierError("bounded exact rational polynomial")
            if (i,j) in seen:raise HilbertCarrierError("ambiguous source monomial")
            seen.add((i,j))

    def value(self,x,y):
        x,y=exact(x),exact(y)
        if not 0<=x<=1 or not 0<=y<=1:
            raise HilbertCarrierError("source polynomial domain [0,1]^2")
        return sum((Q(c)*x**i*y**j for i,j,c in self.terms),Q())

    def integral(self):
        """Exact double integral from source, not sampled/extrapolated."""
        return sum((Q(c)/((i+1)*(j+1)) for i,j,c in self.terms),Q())

    def gradient_sup_bound(self):
        """Coordinate gradient bounds via |x|,|y|<=1."""
        return (
            sum((abs(Q(c))*i for i,j,c in self.terms),Q()),
            sum((abs(Q(c))*j for i,j,c in self.terms),Q())
        )

    def hessian_sup_bound(self):
        return (
            sum((abs(Q(c))*i*(i-1) for i,j,c in self.terms),Q()),
            sum((abs(Q(c))*i*j for i,j,c in self.terms),Q()),
            sum((abs(Q(c))*j*(j-1) for i,j,c in self.terms),Q()),
        )

def exact_quadrature(poly:RationalPolynomial,order):
    """1D Hilbert successor enumerates 2D cell midpoint quadrature.

    For exact rational poly f, bounded all-square source derivatives give:
       |integral(f)-sum f(center)/4^k|
         <= (Mxx+Myy)*h²/24 + Mxy*h²/16
    via midpoint Taylor cancellation and uniform Hessian entries.

    No unknown Lipschitz parameter or statistical posterior is trusted.
    """
    if type(poly) is not RationalPolynomial:
        raise HilbertCarrierError("source-indexed polynomial required")
    k=order_gate(order)
    if k>6:raise HilbertCarrierError("exact quadrature resource order<=6")
    N=4**k
    approximant=sum((poly.value(*center(k,d)) for d in range(N)),Q())/N
    true=poly.integral()
    h=Q(1,2**k)
    mx,mxy,my=poly.hessian_sup_bound()
    sharpened=h*h*((mx+my)/24+mxy/16)
    gx,gy=poly.gradient_sup_bound()
    crude=(gx+gy)*h/2
    if abs(approximant-true)>min(sharpened,crude):
        raise ArithmeticError("independently sourced quadrature error failed")
    return {
       "source_id":poly.source_id,"epoch":poly.epoch,"basis":poly.basis,
       "order":k,"cell_count":N,
       "hilbert_midpoint_integral":approximant,
       "original_analytic_integral":true,
       "absolute_error_exact":abs(approximant-true),
       "source_hessian_error_upper":sharpened,
       "source_gradient_error_upper":crude,
       "quadrature_is_source_authenticated":True,
       "mathematical_2d_integral_proved":True,
       "actual_physical_observations":False,
       "measure_preserving_global_curve_is_classical_import":True,
    }
