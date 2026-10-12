"""Exact finite certificates for a circle-indexed family of ObsSUCC E towers.

Only finite-level arithmetic is executed. Infinite Lipschitz completion and
harmonic/holomorphic extension are proven separately in the research dossier.
Source identities, actual physical origins and observation independence cannot
be authenticated by this finite checker.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Mapping


class BoundaryError(ValueError):
    """Malformed observation, lost source identity, or unsupported gluing."""


def rational(x: object) -> F:
    if type(x) is int or type(x) is F:
        return F(x)
    raise BoundaryError("Only exact ints/Fractions accepted; floats are not certificates")


@dataclass(frozen=True)
class BoundaryLevel:
    """One finite E-tower ring; sample k is at coordinate k/2**level."""
    depth: int
    source_id: str
    basis_id: str
    values: tuple[F, ...]

    def __post_init__(self) -> None:
        if type(self.depth) is not int or not (1 <= self.depth <= 20):
            raise BoundaryError("Supported finite depth 1..20")
        if not self.source_id or not self.basis_id:
            raise BoundaryError("Source and probe/basis identities required")
        if type(self.values) is not tuple or len(self.values) != 1 << self.depth:
            raise BoundaryError("Must declare all 2**depth boundary E readings")
        object.__setattr__(self, "values", tuple(rational(v) for v in self.values))

    @property
    def count(self) -> int:
        return 1 << self.depth

    def at(self, t: F) -> F:
        """Cyclic piecewise-linear interpolation at normalized circle time."""
        t = rational(t) % 1
        x = t * self.count
        k = x.numerator // x.denominator
        alpha = x - k
        return (1 - alpha) * self.values[k] + alpha * self.values[(k + 1) % self.count]

    def verify_lipschitz_edges(self, bound: F) -> None:
        bound = rational(bound)
        if bound < 0:
            raise BoundaryError("Negative Lipschitz budget")
        step = F(bound, self.count)
        for k, y in enumerate(self.values):
            if abs(y - self.values[(k + 1) % self.count]) > step:
                raise BoundaryError(f"Unpaid horizontal communication at edge {k}")


def verify_ring_tower(levels: tuple[BoundaryLevel, ...], bound: F) -> dict:
    """Exact cross-floor consistency and stage-n worst-case approximation error.

    The certified ERROR is conditional on an L-Lipschitz true boundary trace
    agreeing with the sampled points; it does NOT authenticate such a source.
    """
    bound = rational(bound)
    if not levels or levels[0].depth != 1:
        raise BoundaryError("Start at dyadic depth 1")
    sid, bid = levels[0].source_id, levels[0].basis_id
    for j, frame in enumerate(levels):
        if frame.depth != j + 1 or (frame.source_id, frame.basis_id) != (sid, bid):
            raise BoundaryError("Unpaid level or mismatched source/basis")
        frame.verify_lipschitz_edges(bound)
        if j:
            parent = levels[j-1]
            if any(frame.values[2*k] != v for k,v in enumerate(parent.values)):
                raise BoundaryError("Vertical base-change square fails")
    return {"source_id":sid, "basis_id":bid, "levels":len(levels),
            "sample_count":levels[-1].count,
            "boundary_sup_error_budget": bound / (2 * levels[-1].count),
            "interior_sup_error_budget": bound / (2 * levels[-1].count),
            "interior_budget_depends_on": "classical positive unit-mass Poisson kernel"}


def refine_piecewise_linear(level: BoundaryLevel) -> BoundaryLevel:
    """One source-faithful refinement without new measured information."""
    finer = tuple(level.at(F(k, 2*level.count)) for k in range(2*level.count))
    return BoundaryLevel(level.depth+1, level.source_id,level.basis_id,finer)


def circle_distance(u: F, v: F) -> F:
    u,v=rational(u)%1,rational(v)%1
    d=abs(u-v)
    return min(d,1-d)


@dataclass(frozen=True)
class PhaseRing:
    """A DECLARED piecewise-shortest-arc phase map S1->S1, not raw probes alone."""
    depth: int
    phases: tuple[F,...]

    def __post_init__(self)->None:
        if type(self.depth) is not int or not(1<=self.depth<=20):
            raise BoundaryError("Supported finite phase depth 1..20")
        if len(self.phases)!=1<<self.depth:
            raise BoundaryError("Need every phase sample")
        object.__setattr__(self,"phases",tuple(rational(x)%1 for x in self.phases))

    def winding(self)->int:
        total=F(0)
        for a,b in zip(self.phases, self.phases[1:]+self.phases[:1]):
            d=(b-a)%1
            if d==F(1,2):
                raise BoundaryError("Antipodal samples have ambiguous shortest lift")
            if d>F(1,2): d-=1
            total+=d
        if total.denominator != 1:
            raise AssertionError("Cyclic phase winding must be integral")
        return int(total)


def prime(n:int)->bool:
    if type(n) is not int or n<2:return False
    k=2
    while k*k<=n:
        if n%k==0:return False
        k+=1
    return True


def normalized_finite_valuations(q:F)->dict[int,int]:
    """Finite-place FUCC exponents for a declared nonzero rational q."""
    q=rational(q)
    if q==0:raise BoundaryError("Product formula requires q != 0")
    result={}
    for sign,n in ((1,abs(q.numerator)),(-1,q.denominator)):
        p=2
        while p*p<=n:
            if n%p:
                p+=1
                continue
            while n%p==0:
                result[p]=result.get(p,0)+sign
                n//=p
            p+=1
        if n>1:result[n]=result.get(n,0)+sign
    return {p:e for p,e in sorted(result.items()) if e}


def arch_abs_from_places(exponents:Mapping[int,int])->F:
    """Normalized Q product formula: |q|_infty=product p**v_p(q).

    Gives magnitude, NOT order/sign, Gamma completion or source attestation.
    """
    result=F(1)
    for p,e in exponents.items():
        if not prime(p) or type(e) is not int:
            raise BoundaryError("Only genuine finite rational places/exact valuations")
        result*=F(p)**e
    return result


def check_rational_product_formula(q:F)->dict:
    q=rational(q)
    valuations=normalized_finite_valuations(q)
    abs_inf=arch_abs_from_places(valuations)
    if abs_inf!=abs(q):
        raise AssertionError("Classical product formula failed")
    return {"original_rational":q,"finite_exponents":valuations,
            "arch_magnitude":abs_inf,
            "sign_reconstructed":False,"analytic_gamma_reconstructed":False}


def order_of_limits_countermodel(resolution:int, tower_depth:int)->int:
    """a[n,m]=1_{m>=n}; lim_n lim_m=1, lim_m lim_n=0."""
    if type(resolution) is not int or type(tower_depth) is not int or min(resolution,tower_depth)<0:
        raise BoundaryError("Nonnegative integer indices")
    return int(tower_depth>=resolution)


def complex_mul(a:tuple[F,F],b:tuple[F,F])->tuple[F,F]:
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def harmonic_laurent_eval(modes:Mapping[int,tuple[F,F]],x:F,y:F)->tuple[F,F]:
    """Exact harmonic extension of a finite complex Laurent boundary polynomial.

    ζ^k on |ζ|=1 extends as z^k for k>=0 and conjugate(z)^(-k)
    for k<0. Computes exactly at rational interior z=x+iy.
    """
    x,y=rational(x),rational(y)
    if x*x+y*y>=1:
        raise BoundaryError("Inside open disk required")
    out=(F(0),F(0))
    for k,coeff in modes.items():
        if type(k) is not int or len(coeff)!=2:
            raise BoundaryError("Exact Laurent modes required")
        c=tuple(rational(v) for v in coeff)
        base=(x,y if k>=0 else -y)
        power=(F(1),F(0))
        for _ in range(abs(k)):power=complex_mul(power,base)
        term=complex_mul(c,power)
        out=(out[0]+term[0],out[1]+term[1])
    return out


def holomorphic_boundary_admissible(modes:Mapping[int,tuple[F,F]])->bool:
    """For finite Laurent traces, negative-frequency vanishing iff holomorphic."""
    return all(k>=0 or all(rational(v)==0 for v in coeff) for k,coeff in modes.items())


def monodromy_section_report(permutation:tuple[int,...],claim:tuple[str,...]) -> dict:
    """Exact S1 path-groupoid descent: Nat(1,F) is the holonomy fixed set.

    CLAIM descending to the orbit quotient is weaker than the existence of
    a global parallel source state. Only this finite group action is tested.
    """
    if type(permutation) is not tuple or not permutation or set(permutation)!=set(range(len(permutation))):
        raise BoundaryError("Holonomy must be an exact permutation of all source fibers")
    if type(claim) is not tuple or len(claim)!=len(permutation) or any(type(x) is not str for x in claim):
        raise BoundaryError("Claim must label each original fiber exactly")
    seen=set()
    orbits=[]
    for v in range(len(permutation)):
        if v in seen:continue
        cycle=[]
        x=v
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x=permutation[x]
        if x != v:
            raise AssertionError("A permutation orbit must close at its own start")
        orbits.append(tuple(cycle))
    fixed=tuple(i for i,j in enumerate(permutation) if i==j)
    return {"parallel_global_states":fixed, "orbits":tuple(orbits),
            "claim_descends":all(len({claim[i] for i in orbit})==1 for orbit in orbits),
            "nontrivial_holonomy":any(i!=j for i,j in enumerate(permutation))}
