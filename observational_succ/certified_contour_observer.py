"""Exact rational complex-contour winding with source uniform error contracts.

The polynomial certifier is conditional on a trusted bound |F-P|<=E on disk.
The theta adapter obtains E only by replay of the authentic source jet oracle.
No zero coordinates or numerical zeta oracle are used.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

class ContourError(ValueError):
    pass

def rat(x):
    if type(x) not in (Q,int): raise ContourError('non-exact scalar')
    return Q(x)

def point(x,y=0): return (rat(x),rat(y))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,t):return a[0]*t,a[1]*t

def ceval(coeffs,z):
    ans=point(0)
    for a in reversed(coeffs):ans=add(mul(ans,z),a)
    return ans

def cabs1(z):return abs(z[0])+abs(z[1])
def lower_abs(z):return max(abs(z[0]),abs(z[1]))

def square(h):
    h=rat(h)
    if h<=0:raise ContourError('positive halfwidth required')
    return (point(-h,-h),point(h,-h),point(h,h),point(-h,h))


def validate_polynomial(coeffs):
    if not coeffs or any(type(v) not in (tuple,list) or len(v)!=2 for v in coeffs):
        raise ContourError('exact complex coefficient pairs required')
    return tuple(point(*x) for x in coeffs)


def derivative_L1(coeffs,R):
    """If |z|<=R, then |P'(z)|<=L via coefficient triangle inequality."""
    return sum((j*cabs1(v)*R**(j-1) for j,v in enumerate(coeffs) if j),Q())


def segment_adaptive(coeffs,start,end,L,E,max_depth):
    """Cover exact P(edge), F(edge) AND polygon chord inside nonzero balls."""
    todo=[(start,end,0)]
    accepted=[]
    while todo:
        x,y,level=todo.pop()
        c=ceval(coeffs,x)
        delta=cabs1((y[0]-x[0],y[1]-x[1]))
        clearance=lower_abs(c)-L*delta-E
        if clearance>0:
            accepted.append((x,y,clearance))
        else:
            if level>=max_depth:
                raise ContourError('not certified: contour possibly zero or grid under-resolved')
            midpoint=point((x[0]+y[0])/2,(x[1]+y[1])/2)
            todo.append((midpoint,y,level+1))
            todo.append((x,midpoint,level+1))
    return accepted


def winding_of_polygon(path):
    """Winding of exact rational piecewise-linear P contour around origin."""
    w=0
    for a,b in zip(path,path[1:]+path[:1]):
        x0,y0=a;x1,y1=b
        if (y0<=0<y1) or (y1<=0<y0):
            crossx=x0+(x1-x0)*(-y0)/(y1-y0)
            if crossx==0:raise ContourError('polygon touches origin')
            if crossx>0:w+=1 if y0<=0<y1 else -1
        elif y0==y1==0 and min(x0,x1)<=0<=max(x0,x1):
            raise ContourError('polygon passes through zero')
    return w


@dataclass(frozen=True)
class Certificate:
    count: int
    sample_count: int
    lower_clearance: Q
    polynomial_degree: int
    uniform_error: Q
    contour_bound_radius: Q
    source_status: str
    is_zero_lookup: bool = False
    is_weil_positivity: bool = False


def certified_contour(coefficients, contour, R, error=Q(), max_depth=15):
    """Conditional theorem: if |F-P|<=error on |z|<=R, count F zeros.

    This method validates the inequality for P itself and topology only.
    The supplied error is NOT automatically a verified original-source fact.
    """
    coeffs=validate_polynomial(coefficients)
    vertices=tuple(point(*v) for v in contour)
    R=rat(R);E=rat(error)
    if (R<=0 or E<0 or len(vertices)<3 or len(set(vertices))<3
        or type(max_depth) is not int or max_depth<0 or max_depth>22):
        raise ContourError('invalid bounded contour contract')
    if any(z[0]*z[0]+z[1]*z[1]>R*R for z in vertices):
        raise ContourError('contour escapes certified analytic disk')
    L=derivative_L1(coeffs,R)
    pieces=[]
    for start,end in zip(vertices,vertices[1:]+vertices[:1]):
        pieces.extend(segment_adaptive(coeffs,start,end,L,E,max_depth))
    vertex_sequence=tuple(piece[0] for piece in pieces)
    points=tuple(ceval(coeffs,z) for z in vertex_sequence)
    count=winding_of_polygon(points)
    if count<0:raise ContourError('clockwise/invalid contour or nonholomorphic model')
    return Certificate(count,len(points),min(x[2] for x in pieces),len(coeffs)-1,E,R,
                       'CONDITIONAL_SUPPLIED_ERROR')


def authentic_theta_square(theta_data,halfwidth=Q(3),R=Q(11,2),comparison=13):
    """Source-lift: exact zeta theta-moment replay, zero-reading-free contour.

    Constructs polynomial+uniform disk interval from theta_taylor_jets.
    Returns CERTIFIED_THETA_SOURCE only on strict verified contour.
    """
    from .theta_taylor_jets import certified_midpoint_polynomial
    obs=certified_midpoint_polynomial(theta_data,R,comparison)
    even=obs['coefficient_midpoints']
    coeffs=tuple(point(even[j//2] if j%2==0 else 0) for j in range(2*len(even)-1))
    base=certified_contour(coeffs,square(halfwidth),R,obs['uniform_complex_error'])
    return Certificate(base.count,base.sample_count,base.lower_clearance,
                       base.polynomial_degree,base.uniform_error,base.contour_bound_radius,
                       'AUTHENTIC_REPLAYED_INTEGER_THETA')
