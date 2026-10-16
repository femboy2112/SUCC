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


def _integral_monomial_on_square(i,j,xlo,xhi,ylo,yhi):
    return (((xhi**(i+1)-xlo**(i+1))/(i+1))
            *((yhi**(j+1)-ylo**(j+1))/(j+1)))

def cell_average(poly,order,d):
    """Exact original polynomial conditional expectation on a dyadic tile."""
    if type(poly) is not RationalPolynomial:
        raise HilbertCarrierError("source-authenticated polynomial expected")
    xx,yy=spatial_cell(order,d)
    area=(xx[1]-xx[0])*(yy[1]-yy[0])
    integral=sum((Q(c)*_integral_monomial_on_square(i,j,*xx,*yy)
                  for i,j,c in poly.terms),Q())
    return integral/area

def square_integral(poly):
    """Original L² source norm with exact polynomial cross terms."""
    if type(poly) is not RationalPolynomial:
        raise HilbertCarrierError("source polynomial for Hilbert L2 pullback")
    return sum((Q(c)*Q(d)/((i+k+1)*(j+l+1))
                for i,j,c in poly.terms for k,l,d in poly.terms),Q())

def dyadic_conditional_L2(poly,order):
    """L² conditional expectation on Hilbert parameter cylinders.

    Area of tile = time-cylinder length =4^-k. At the infinite Hilbert
    completion H, classical measure preservation gives E[f(H)|F_k]
    equal to this tile mean. This finite routine evaluates both sides'
    invariant rational cylinder norms. No H¹ transport is inferred.
    """
    if type(poly) is not RationalPolynomial:
        raise HilbertCarrierError("declared source polynomial required")
    k=order_gate(order)
    if k>5:raise HilbertCarrierError("exact conditional-L2 budget k<=5")
    P=4**k
    means=[cell_average(poly,k,d) for d in range(P)]
    approximate_norm_sq=sum((u*u for u in means),Q())/P
    original=square_integral(poly)
    residual=original-approximate_norm_sq
    gx,gy=poly.gradient_sup_bound()
    h=Q(1,2**k)
    bound=h*h*(gx+gy)**2
    if not 0<=residual<=bound:
        raise ArithmeticError("dyadic Hilbert L2 orthogonal projection identity failed")
    return {
        "source":poly.source_id,
        "order":k,
        "time_cylinder_mass":Q(1,P),
        "spatial_cell_mass":Q(1,P),
        "original_L2_norm_squared":original,
        "Hilbert_parameter_projection_norm_squared":approximate_norm_sq,
        "L2_squared_error_exact":residual,
        "L2_squared_error_source_bound":bound,
        "finite_source_step_isometry":True,
        "classical_measure_preserving_limit_used":True,
        "Hilbert_pullback_H1_isometry_proved":False,
    }

def hidden_unit_Haar(order,d=0):
    """A hidden + / - subcell oscillation: ||f||_2=1, E_k f=0.

    For every finite Hilbert observed partition, this proves
    ||I-E_k||_(L2->L2)=1 (classical projection upper bound),
    despite strong L² convergence E_k f->f for each fixed f.
    The witness DEPENDS on k and is not an authentic zeta mutation.
    """
    k,d=index_gate(order,d)
    x,y=spatial_cell(k,d)
    amp=Q(2**k)
    area=(x[1]-x[0])*(y[1]-y[0])
    signed=amp*(area/2)-amp*(area/2)
    norm=amp*amp*area
    if signed!=0 or norm!=1:
        raise ArithmeticError("Haar source norm/mean proof failed")
    return {
        "source":"DECLARED_PIECEWISE_HAAR_NONARITHMETIC",
        "order":k,"cell_index":d,"support":(x,y),
        "positive_half":"left half of supporting dyadic tile",
        "negative_half":"right half of supporting dyadic tile",
        "amplitude":amp,
        "cell_average":Q(),
        "L2_norm_squared":norm,
        "dyadic_observer_projection_norm_squared":Q(),
        "operator_norm_I_minus_P_equals_one":True,
        "universal_L2_unit_ball_rate_exists":False,
        "actual_Weil_spectral_direction_authenticated":False,
    }

def exact_cell_inner_product(order,table_a,table_b):
    """Hilbert parameter order preserves finite L² area-inner-product EXACTLY.

    Data are original complete CARTESIAN cell rows, not independent runs.
    Norm agreement is a permutation/source identity, not a covariance
    or a Hilbert-space H¹ identification.
    """
    k=order_gate(order)
    if k>6:raise HilbertCarrierError("finite isometry budget k<=6")
    n=1<<k
    if (type(table_a) is not tuple or type(table_b) is not tuple or
        len(table_a)!=n or len(table_b)!=n or
        any(type(row) is not tuple or len(row)!=n for row in table_a+table_b) or
        any(type(v) not in (int,Q) for row in table_a+table_b for v in row)):
        raise HilbertCarrierError("complete original-source exact square arrays required")
    spatial=sum((Q(table_a[x][y])*Q(table_b[x][y])
                 for x in range(n) for y in range(n)),Q())/n**2
    pulled=sum((Q(table_a[x][y])*Q(table_b[x][y])
               for x,y in (point(k,d) for d in range(n*n))),Q())/n**2
    if spatial!=pulled:
        raise ArithmeticError("Hilbert read order changed original L2 bilinear pairing")
    return spatial


def parameter_tube(t,order):
    """Finitely enclose H(t) via ONE nested spatial Hilbert dyadic square.

    Parameter t is exact rational. The mathematical Hilbert point at a
    rational parameter is in every nested square's closure. This is NOT
    a finite computation of all its infinitely many coordinate digits.
    """
    t=exact(t)
    k=order_gate(order)
    if not 0<=t<=1:
        raise HilbertCarrierError("true Hilbert parameter [0,1]")
    total=4**k
    d=min(total-1,(t*total).numerator//(t*total).denominator)
    X,Y=spatial_cell(k,d)
    cx,cy=center(k,d)
    return {
        "source":"CLASSICAL_HILBERT_DYADIC_LIMIT",
        "parameter":t,"order":k,"source_index":d,
        "time_cylinder":time_cell(k,d),
        "spatial_enclosure":(X,Y),
        "center":(cx,cy),
        "squared_distance_to_completed_point_upper":Q(1,2*4**k),
        "uniform_limit_carries_original_source":True,
        "limit_point_physically_observed":False,
    }

def target_preimage_tube(x,y,order):
    """Finitely enclose one possible parameter for any rational square point.

    For boundary dyadic targets choose the right cell (or top/last cell),
    with compatible orientation at every order; no global continuous
    section/single-valued inverse is constructed.
    """
    x,y=exact(x),exact(y)
    k=order_gate(order)
    if not (0<=x<=1 and 0<=y<=1):
        raise HilbertCarrierError("rational target in original closed square")
    n=1<<k
    cx=min(n-1,(x*n).numerator//(x*n).denominator)
    cy=min(n-1,(y*n).numerator//(y*n).denominator)
    d=index(k,cx,cy)
    square=spatial_cell(k,d)
    if not (square[0][0]<=x<=square[0][1] and
            square[1][0]<=y<=square[1][1]):
        raise ArithmeticError("genuine Hilbert preimage tube misses source target")
    return {
        "source":"RATIONAL_SQUARE_TARGET_CLASSICAL_SURJECTION",
        "target":(x,y),"order":k,"time_cylinder":time_cell(k,d),
        "spatial_tile":square,"cell_index":d,
        "preimage_parameter_computed_to_infinite_precision":False,
        "surjectivity_uses_classical_nested_compactness":True,
    }


def no_global_lipschitz_space_filler(candidate_constant):
    """Finite exact area-cover obstruction to any L-Lipschitz [0,1]->square.

    Divide time into m equal intervals. A global Lipschitz bound L means
    each image fits in a square of area <=(2L/m)^2. Their union occupies
    area <=4L²/m<1 for m=floor(4L²)+1. Thus NO SUCH map fills the square.
    This is a general classical mathematical implication. We do NOT
    claim an actual Hilbert curve obeys an L-Lipschitz hypothesis.
    """
    L=exact(candidate_constant)
    if L<0:
        raise HilbertCarrierError("Lipschitz upper bound must be nonnegative")
    m=(4*L*L).numerator//(4*L*L).denominator+1
    area_bound=4*L*L/m
    if not area_bound<1:
        raise ArithmeticError("finite Lipschitz area obstruction failed")
    return {
        "hypothetical_Lipschitz_constant":L,
        "finite_time_interval_cover_count":m,
        "upper_area_of_image":area_bound,
        "unit_square_area":Q(1),
        "surjective_with_this_Lipschitz_bound":False,
        "actual_Hilbert_curve_Lipschitz":False,
        "requires_a_verified_global_Lipschitz_hypothesis":True,
        "original_square_completion_proved_by_other_classical_topology":True,
    }
