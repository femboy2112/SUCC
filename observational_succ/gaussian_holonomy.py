"""Arithmetic SUCC/FUCC sieve paths as finite voltage-groupoid data.

A true split rational prime contributes its TWO Gaussian factor reductions;
each SUCC edge keeps its original displacement. Finite quotient cycles
therefore retain holonomy in Z^2. A spanning forest plus lattice Hermite
reduction constructs the entire holonomy subgroup without assuming it
vanishes. One new prime kills repetition of a fixed nonzero loop when
its residue displacement is nonzero; this does NOT eliminate all detours.

All finite reports are exact integer computations, not an all-D sieve theorem.
The classical voltage graph theorem remains an external attribution.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import gcd, isqrt, prod
from typing import Iterable

from .coverage_lower_bounds import gaussian_coordinate, is_prime

Vec2 = tuple[int, int]


class HolonomyError(ValueError):
    """Missing true arithmetic source, unlawful step, or false path certificate."""


def plus(a: Vec2, b: Vec2) -> Vec2:
    return a[0] + b[0], a[1] + b[1]


def neg(a: Vec2) -> Vec2:
    return -a[0], -a[1]


def minus(a: Vec2, b: Vec2) -> Vec2:
    return a[0] - b[0], a[1] - b[1]


def sqnorm(a: Vec2) -> int:
    return a[0]*a[0]+a[1]*a[1]


def gaussian_prime(z: Vec2) -> bool:
    """Structural irreducibility in Z[i], including inert axis primes.

    For nonzero off-axis a+bi, irreducible iff norm is rational prime;
    on the axes |a| (or |b|) must be rational prime congruent to 3 mod 4.
    This is a classical norm/Euclidean-domain classification, not a
    discovery of the prime distribution by walking.
    """
    if type(z) is not tuple or len(z) != 2 or any(type(c) is not int for c in z):
        raise HolonomyError("Gaussian source must have integral coordinates")
    x,y=z
    if not x and not y:
        return False
    if not x or not y:
        t=abs(x or y)
        return is_prime(t) and t % 4 == 3
    return is_prime(sqnorm(z))


def fucc_path_observations(sieve: GaussianSieve, points: Iterable[Vec2]) -> tuple[dict, ...]:
    """Probe finite SUCC-carrier points for true Gaussian primes and sieve status.

    This is a decidable, pointwise classification; it does not by itself
    force bounded component sizes for the whole infinite prime graph.
    """
    result=[]
    for z in points:
        prime=gaussian_prime(z)
        result.append({'point':z,'gaussian_prime':prime,
                       'sieve_allowed':sieve.allowed(z),
                       'exceptional_prime':prime and not sieve.allowed(z)})
    return tuple(result)


@dataclass(frozen=True)
class GaussianSieve:
    """Source is BOTH Gaussian conjugates over distinct p=1 mod 4 primes."""
    factors: tuple[Vec2, ...]  # (a,b) means a+bi and a-bi, a,b>0

    def __post_init__(self) -> None:
        if type(self.factors) is not tuple or len(set(self.factors)) != len(self.factors):
            raise HolonomyError("Distinct, typed Gaussian split-prime pairs required")
        primes = []
        for v in self.factors:
            if (type(v) is not tuple or len(v) != 2
                    or any(type(x) is not int or x <= 0 for x in v)):
                raise HolonomyError("Positive integral factor coordinates required")
            p = sqnorm(v)
            if not is_prime(p) or p % 4 != 1 or p in primes:
                raise HolonomyError("Composite, duplicate or non-split prime factor")
            primes.append(p)

    @property
    def primes(self) -> tuple[int, ...]:
        return tuple(sqnorm(p) for p in self.factors)

    @property
    def period(self) -> int:
        return prod(self.primes)

    def allowed(self, v: Vec2) -> bool:
        return all(gaussian_coordinate(v, (a, b)) != 0
                   and gaussian_coordinate(v, (a, -b)) != 0
                   for a, b in self.factors)

    def residue(self, v: Vec2) -> Vec2:
        q = self.period
        return v[0] % q, v[1] % q

    def refines(self, other: GaussianSieve) -> bool:
        """The receiver's finer sieve filters all of other's split primes."""
        return set(other.primes).issubset(self.primes)

    def allowed_residues(self, *, max_cells: int = 100_000) -> tuple[Vec2, ...]:
        q = self.period
        if q*q > max_cells:
            raise HolonomyError("Declared finite enumeration budget exhausted")
        return tuple((x,y) for x in range(q) for y in range(q)
                     if self.allowed((x,y)))


@dataclass(frozen=True)
class LiftedLoop:
    start: Vec2
    steps: tuple[Vec2, ...]

    @property
    def displacement(self) -> Vec2:
        x = y = 0
        for a, b in self.steps:
            x += a
            y += b
        return x,y

    @property
    def points(self) -> tuple[Vec2, ...]:
        v = self.start
        pts = [v]
        for step in self.steps:
            v = plus(v, step)
            pts.append(v)
        return tuple(pts)

    def verify(self, sieve: GaussianSieve, squared_step_bound: int) -> None:
        if (type(squared_step_bound) is not int or squared_step_bound < 1
                or not self.steps or any(type(x) is not int for s in self.steps for x in s)):
            raise HolonomyError("Invalid finite path/step budget")
        if any(sqnorm(s) == 0 or sqnorm(s) > squared_step_bound for s in self.steps):
            raise HolonomyError("A step is not in the allowed SUCC alphabet")
        if any(not sieve.allowed(p) for p in self.points):
            raise HolonomyError("Path passes through a forbidden FUCC factor")
        if self.displacement == (0,0) or sieve.residue(self.points[0]) != sieve.residue(self.points[-1]):
            raise HolonomyError("Not a nonzero-holonomy quotient loop")


@dataclass(frozen=True)
class HolonomyReport:
    period: int
    surviving_residues: int
    quotient_components: int
    largest_finite_quotient_component: int
    rank: int
    hermite_basis: tuple[Vec2, ...]
    subgroup_index: int | None
    nonzero_cycle: LiftedLoop | None

    @property
    def confined(self) -> bool:
        return self.rank == 0


def _bezout(a: int, b: int) -> tuple[int,int,int]:
    """g>0,s,t with s*a+t*b=g, for a>0 and any signed b."""
    if a <= 0:
        raise HolonomyError("Internal Bezout input must be positive")
    old_r,r = a,abs(b)
    old_s,s = 1,0
    old_t,t = 0,1
    while r:
        q = old_r // r
        old_r,r = r,old_r-q*r
        old_s,s = s,old_s-q*s
        old_t,t = t,old_t-q*t
    return old_r, old_s, (old_t if b >= 0 else -old_t)


class _LatticeHNF:
    """Incremental 2D subgroup Hermite reduction, exact integer algebra."""
    def __init__(self):
        self.a = 0  # horizontal lattice generator a*e1
        self.b = 0  # x-coordinate paired with vertical gcd d
        self.d = 0  # vertical-coordinate gcd

    def add(self, v: Vec2) -> None:
        x,y = v
        if not y:
            self.a = gcd(self.a,abs(x))
        elif not self.d:
            self.b = x if y > 0 else -x
            self.d = abs(y)
        else:
            old_d, old_b = self.d, self.b
            g,s,t = _bezout(old_d,y)
            horizontal = (old_d//g)*x - (y//g)*old_b
            self.a = gcd(self.a,abs(horizontal))
            self.b = s*old_b + t*x
            self.d = g

    @property
    def rank(self) -> int:
        return int(self.a != 0) + int(self.d != 0)

    @property
    def basis(self) -> tuple[Vec2, ...]:
        if self.a and self.d:
            return ((self.a,0),(self.b % self.a,self.d))
        if self.a:
            return ((self.a,0),)
        if self.d:
            return ((self.b,self.d),)
        return ()

    @property
    def index(self) -> int | None:
        return self.a*self.d if self.a and self.d else None


def _steps(k: int) -> tuple[Vec2, ...]:
    if type(k) is not int or k < 1:
        raise HolonomyError("Squared Euclidean step bound must be a positive integer")
    n = isqrt(k)
    return tuple((dx,dy) for dx in range(-n,n+1)
                 for dy in range(-n,n+1) if 0 < dx*dx+dy*dy <= k)


def quotient_holonomy(sieve: GaussianSieve, squared_step_bound: int,
                      *, max_cells: int = 100_000) -> HolonomyReport:
    """Explore ALL surviving quotient vertices, retaining every dart voltage.

    Produces a finite complete subgroup basis and a concrete escaping witness
    when nonzero. This is a fixed-instance decision, NOT an all-K construction.
    """
    vertices = sieve.allowed_residues(max_cells=max_cells)
    allowed = set(vertices)
    q = sieve.period
    steps = _steps(squared_step_bound)
    potentials: dict[Vec2, Vec2] = {}
    parent: dict[Vec2, tuple[Vec2,Vec2]] = {}
    count = largest = 0
    lattice = _LatticeHNF()
    witness = None

    def route(v: Vec2) -> tuple[Vec2, ...]:
        backward = []
        while v in parent:
            v, s = parent[v]
            backward.append(s)
        return tuple(reversed(backward))

    for root in vertices:
        if root in potentials:
            continue
        count += 1
        potentials[root] = root
        queue = deque((root,))
        size = 0
        while queue:
            src = queue.popleft()
            size += 1
            for d in steps:
                dst = ((src[0]+d[0])%q,(src[1]+d[1])%q)
                if dst not in allowed:
                    continue
                new_lift = plus(potentials[src],d)
                if dst not in potentials:
                    potentials[dst] = new_lift
                    parent[dst] = (src,d)
                    queue.append(dst)
                else:
                    diff = minus(new_lift,potentials[dst])
                    lattice.add(diff)
                    if diff != (0,0) and witness is None:
                        inverse_route = tuple(neg(s) for s in reversed(route(dst)))
                        candidate = LiftedLoop(root, route(src)+(d,)+inverse_route)
                        candidate.verify(sieve,squared_step_bound)
                        if candidate.displacement != diff:
                            raise AssertionError("Cycle reconstruction lost its actual displacement")
                        witness = candidate
        largest = max(largest,size)
    if len(potentials) != len(vertices):
        raise AssertionError("Quotient graph search omitted a residue")
    return HolonomyReport(q,len(vertices),count,largest,lattice.rank,
                          lattice.basis,lattice.index,witness)


@dataclass(frozen=True)
class LoopElimination:
    new_factor: Vec2
    norm: int
    displacement: Vec2
    forbidden_repetition_index: int
    cycle_length: int

    @property
    def maximum_completed_cycles_before_forbidden(self) -> int:
        # The forbidden point at index k is itself the END of cycle k.
        # Therefore k complete cycles cannot be certified when k>=1.
        return max(0, self.forbidden_repetition_index - 1)


def certify_single_loop_elimination(sieve: GaussianSieve, loop: LiftedLoop,
                                      step_squared: int, factor: Vec2) -> LoopElimination:
    """One authentic prime forbids repeating this EXACT old quotient loop p times.

    This does not imply that every other escaping cycle is eliminated.
    """
    loop.verify(sieve,step_squared)
    if sqnorm(factor) in sieve.primes:
        raise HolonomyError("New factor must be a new prime source")
    a,b = factor
    if any(type(x) is not int or x <= 0 for x in factor):
        raise HolonomyError("Positive Gaussian prime coordinates required")
    p = sqnorm(factor)
    if not is_prime(p) or p % 4 != 1:
        raise HolonomyError("Only true split Gaussian prime norms permitted")
    h = gaussian_coordinate(loop.displacement,factor)
    if h == 0:
        raise HolonomyError("This prime cannot distinguish repetition along that displacement")
    initial = gaussian_coordinate(loop.start,factor)
    k = (-initial * pow(h,-1,p)) % p
    if (initial + k*h)%p != 0:
        raise AssertionError("Predicted forbidden repeated source residue is incorrect")
    for j in range(p):
        if ((initial+j*h)%p==0) != (j==k):
            raise AssertionError("Residue traversal must hit zero exactly once")
    return LoopElimination(factor,p,loop.displacement,k,len(loop.steps))


def certify_simultaneous_elimination(sieve: GaussianSieve, loops: Iterable[LiftedLoop],
                                      squared_step: int, factor: Vec2) -> tuple[LoopElimination, ...]:
    loops = tuple(loops)
    if not loops:
        raise HolonomyError("A nonempty finite witness catalogue is required")
    return tuple(certify_single_loop_elimination(sieve,loop,squared_step,factor)
                 for loop in loops)


def verify_refinement_commutes(coarse: GaussianSieve, fine: GaussianSieve,
                                path: Iterable[Vec2], squared_step: int) -> dict:
    """Verify concrete source/FUCC projection naturality on a finite path.

    The corresponding universal commuting square follows from Q|Q' and
    factor inclusion; the finite test catches bad source maps/labels.
    """
    if not fine.refines(coarse) or fine.period % coarse.period:
        raise HolonomyError("Source refinement does not contain the coarse prime factors")
    pts = tuple(path)
    if len(pts) < 2:
        raise HolonomyError("At least one actual SUCC edge required")
    for a,b in zip(pts,pts[1:]):
        d = minus(b,a)
        if sqnorm(d)==0 or sqnorm(d)>squared_step:
            raise HolonomyError("Bad actual source transition")
        if not fine.allowed(a) or not fine.allowed(b) or not coarse.allowed(a) or not coarse.allowed(b):
            raise HolonomyError("Projected path leaves its declared sieve")
        af,bf = fine.residue(a),fine.residue(b)
        ac,bc = coarse.residue(a),coarse.residue(b)
        if (af[0]%coarse.period,af[1]%coarse.period)!=ac or \
           (bf[0]%coarse.period,bf[1]%coarse.period)!=bc or \
           fine.residue(plus(a,d))!=bf or coarse.residue(plus(a,d))!=bc:
            raise AssertionError("Commuting arithmetic source square failed")
    return {'fine_period':fine.period,'coarse_period':coarse.period,
            'edges':len(pts)-1,'covariant':True}


def limit_holonomy_warning(periods: Iterable[int]) -> dict:
    """For unrestricted Z², H_Q=QZ²; vanishing intersection is not finite confinement."""
    ps = tuple(periods)
    if not ps or any(type(q) is not int or q<1 for q in ps):
        raise HolonomyError("Positive integer periods required")
    if any(b % a for a,b in zip(ps,ps[1:])):
        raise HolonomyError("Need an honest nested divisibility chain")
    return {'all_finite_stages_escaping': True,
            'proven_formula': 'H_Q = Q Z^2 for unrestricted unit-step Z^2',
            'intersection_zero_if_periods_unbounded': 'UNVERIFIED for this finite prefix',
            'periods':ps}


def construct_confinement_potential(sieve: GaussianSieve, squared_step_bound: int,
                                    *, max_cells: int = 100_000) -> tuple[tuple[Vec2,Vec2],...]:
    """Prover-side candidate construction; throws for any nonzero closed voltage.

    This searches a FIXED declared sieve; it is not an existence constructor
    that will succeed for every step bound. A separate checker must verify
    all actual source edges before E accepts the mathematical certificate.
    """
    vertices=sieve.allowed_residues(max_cells=max_cells)
    allowed=set(vertices)
    q=sieve.period
    steps=_steps(squared_step_bound)
    lifts={}
    for root in vertices:
        if root in lifts:continue
        lifts[root]=root
        todo=deque((root,))
        while todo:
            src=todo.popleft()
            for d in steps:
                dst=((src[0]+d[0])%q,(src[1]+d[1])%q)
                if dst not in allowed:continue
                actual=plus(lifts[src],d)
                if dst not in lifts:
                    lifts[dst]=actual
                    todo.append(dst)
                elif lifts[dst]!=actual:
                    raise HolonomyError("Nonzero quotient holonomy: no source-compatible potential")
    return tuple(sorted(lifts.items()))
