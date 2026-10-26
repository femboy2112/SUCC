"""Four marked projective points, exact golden j and source-typed BBP probes.

Established projective/elliptic and simplicial algebra only. The golden
reference is an explicit extra Möbius fixed-point condition, not a property
of all projective quadruples. No π normality, physical geometry or RH proof.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd

from .succ_internal_matrix_walk import authentic_r

SOURCE = 'Q:Coherent-Main-X-four-pole-BBP'


def rat(v):
    if type(v) not in (Q, int):
        raise TypeError('Exact integer or Fraction required; floats/booleans rejected')
    return Q(v)


@dataclass(frozen=True)
class Golden:
    """Exact Q[λ]/(λ²+λ−1), with λ=(sqrt(5)−1)/2 > 0."""
    a: Q
    b: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', rat(self.a))
        object.__setattr__(self, 'b', rat(self.b))

    @classmethod
    def lift(cls, value):
        return value if isinstance(value, cls) else cls(rat(value))

    def __add__(self, other):
        v = self.lift(other)
        return Golden(self.a+v.a, self.b+v.b)
    __radd__ = __add__

    def __neg__(self):
        return Golden(-self.a,-self.b)
    def __sub__(self, other):
        return self+(-self.lift(other))
    def __rsub__(self, other):
        return self.lift(other)-self
    def __mul__(self, other):
        v=self.lift(other)
        return Golden(self.a*v.a+self.b*v.b,
                      self.a*v.b+self.b*v.a-self.b*v.b)
    __rmul__=__mul__

    def conjugate(self):
        return Golden(self.a-self.b,-self.b)

    def norm(self):
        return self.a*self.a-self.a*self.b-self.b*self.b

    def reciprocal(self):
        if not self.norm():
            raise ZeroDivisionError('zero golden algebra element')
        return self.conjugate()*Q(1,self.norm())

    def __truediv__(self,other):
        return self*self.lift(other).reciprocal()
    def __rtruediv__(self,other):
        return self.lift(other)/self

    def __pow__(self,n):
        if type(n) is not int:
            raise TypeError('integer exponent required')
        if n<0:return (self.reciprocal())**(-n)
        out=Golden(1)
        value=self
        while n:
            if n&1:out=out*value
            value=value*value
            n//=2
        return out

    def to_float(self):
        return float(self.a)+float(self.b)*(5**0.5-1)/2


LAMBDA_GOLD=Golden(0,1)


def projective_point(v):
    """Homogeneous (a,b), representing a/b; None represents infinity."""
    return (Q(1),Q(0)) if v is None else (rat(v),Q(1))


def det(a,b):
    return a[0]*b[1]-a[1]*b[0]


def cross_ratio(a,b,c,d):
    """[a,c][b,d] / ([a,d][b,c]); CR(∞,0;1,λ)=λ."""
    ps=tuple(projective_point(v) for v in (a,b,c,d))
    if any(det(ps[i],ps[j]) == 0 for i in range(4) for j in range(i+1,4)):
        raise ValueError('four distinct projective points required')
    return det(ps[0],ps[2])*det(ps[1],ps[3]) / (det(ps[0],ps[3])*det(ps[1],ps[2]))


def projective_transform(v,a,b,c,d):
    a,b,c,d=map(rat,(a,b,c,d))
    if a*d-b*c==0:raise ValueError('noninvertible 2x2 transformation')
    x,y=projective_point(v)
    X=a*x+b*y;Y=c*x+d*y
    return None if Y==0 else X/Y


def legendre_j(v):
    """Exact j of y²=x(x−1)(x−v), no choice of periods encoded."""
    z= v if isinstance(v,Golden) else rat(v)
    if z==0 or z==1:raise ValueError('singular elliptic branch collision')
    return 256*(1-z+z*z)**3/(z*z*(1-z)**2)


def anharmonic_orbit(v):
    z=v if isinstance(v,Golden) else rat(v)
    if z==0 or z==1:raise ValueError('singular branch')
    return (z,1-z,1/z,1/(1-z),z/(z-1),(z-1)/z)


def weierstrass_j(a,b):
    a=rat(a);b=rat(b)
    denom=4*a**3+27*b**2
    if denom==0:raise ValueError('singular cubic')
    return Q(1728)*4*a**3/denom


def source_fourth_point(n):
    """One unwrapped, anchored genuine BBP state mapped to a marked λ.

    This map loses integer lift only for the *elliptic observable*, not for
    the authenticated recurrence; raw unwrapped U_n is also returned.
    """
    if type(n) is not int or not 1<=n<=64:
        raise ValueError('bounded ordinary positive n')
    u=Q(0)
    for k in range(1,n+1):
        u=16*u+authentic_r(k)
    lam=u-(u.numerator//u.denominator)
    if lam==0:raise ValueError('singular fourth point in selected source')
    return {'source':SOURCE,'n':n,'unwrapped_state':u,'circle_phase':lam,
            'j_invariant':legendre_j(lam),'normality_proved':False}


def oriented_triangle_boundary(face):
    """Signed undirected-edge coordinates of ∂[i,j,k]."""
    if len(face)!=3 or len(set(face))!=3:
        raise ValueError('ordered three distinct vertices')
    i,j,k=face
    out={}
    for a,b,c in ((j,k,1),(i,k,-1),(i,j,1)):
        edge=tuple(sorted((a,b)))
        sign=c if a<b else -c
        out[edge]=out.get(edge,0)+sign
    return {e:c for e,c in out.items() if c}


def tetrahedral_face_syzygy():
    """Boundary of a 3-simplex is a nonzero 2-chain with zero 1-boundary."""
    faces=((1,(1,2,3)),(-1,(0,2,3)),(1,(0,1,3)),(-1,(0,1,2)))
    result={}
    for sign,face in faces:
        for edge,c in oriented_triangle_boundary(face).items():
            result[edge]=result.get(edge,0)+sign*c
    return {'faces':faces,'edge_boundary':{e:c for e,c in result.items() if c},
            'cycle_rank_triangle':1,'cycle_rank_tetrahedron':3}


def torsion_fiber_exponents():
    """Compare circle degree-16 inverse C16 with elliptic E[4] = C4×C4."""
    def ordcyclic(a,m):return m//gcd(a,m)
    circle={ordcyclic(a,16) for a in range(16)}
    ell={ordcyclic(a,4)*ordcyclic(b,4)//gcd(ordcyclic(a,4),ordcyclic(b,4))
         for a in range(4) for b in range(4)}
    return {'circle_fiber_size':16,'elliptic_4torsion_size':16,
            'circle_element_orders':tuple(sorted(circle)),
            'elliptic_element_orders':tuple(sorted(ell)),
            'group_identification_proved':False}


def elliptic_four_torsion_pairing(v,w):
    """Abstract Weil-pairing exponent on (Z/4)^2: e4(v,w)=i^exponent.

    Requires separately proved correspondence to geometrically selected E[4].
    It does NOT authenticate any BBP phase or source intertwiner.
    """
    if (not isinstance(v,tuple) or not isinstance(w,tuple)
            or len(v)!=2 or len(w)!=2
            or any(type(a) is not int or not 0<=a<4 for a in v+w)):
        raise ValueError('two exact four-torsion residue pairs')
    return (v[0]*w[1]-v[1]*w[0])%4
