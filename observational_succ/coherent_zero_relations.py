"""Proof-carrying multibasis zeros and exact finite dynamical coboundaries.

Classical polynomial ideal-membership and finite functional-graph cohomology.
A checked polynomial consequence is CONDITIONAL on its generators being true
under ONE compatible source interpretation; source labels are not authentication.
Rational finite tests neither settle pi normality nor certify infinite limits.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


class ZeroDomainError(ValueError):
    """A malformed or incompatible algebraic/finite dynamical context."""


def _q(x):
    if type(x) not in (int, Q):
        raise ZeroDomainError('exact integer or Fraction required')
    return Q(x)


@dataclass(frozen=True)
class Poly:
    """Sparse Q[variables], with canonical sorted monomials and exact operations."""
    variables: tuple[str, ...]
    terms: tuple[tuple[tuple[int, ...], Q], ...]

    def __post_init__(self):
        names = self.variables
        if (not names or len(names) != len(set(names)) or
                any(type(s) is not str or not s for s in names)):
            raise ZeroDomainError('nonempty distinct symbolic variables required')
        seen = set()
        for exponents, coeff in self.terms:
            if (len(exponents) != len(names) or any(type(e) is not int or e < 0 for e in exponents)
                    or exponents in seen or type(coeff) is not Q or not coeff):
                raise ZeroDomainError('canonical monomials require distinct nonzero rational coefficients')
            seen.add(exponents)
        if tuple(sorted(self.terms)) != self.terms:
            raise ZeroDomainError('sort monomials in canonical order')

    @classmethod
    def from_dict(cls, names, data):
        if type(names) is not tuple:
            raise ZeroDomainError('source variable tuple required')
        normalized = {}
        for exponent, coeff in data.items():
            v = _q(coeff)
            if v:
                normalized[tuple(exponent)] = v
        return cls(names, tuple(sorted(normalized.items())))

    @classmethod
    def const(cls, names, scalar):
        return cls.from_dict(names, {(0,) * len(names): _q(scalar)})

    @classmethod
    def var(cls, names, name):
        if name not in names:
            raise ZeroDomainError('variable absent from declared chart')
        e = [0] * len(names)
        e[names.index(name)] = 1
        return cls.from_dict(names, {tuple(e): Q(1)})

    def _same(self, other):
        if not isinstance(other, Poly) or self.variables != other.variables:
            raise ZeroDomainError('different polynomial basis: supply a declared chart transport')
        return other

    def __neg__(self):
        return Poly.from_dict(self.variables, {k: -v for k, v in self.terms})

    def __add__(self, other):
        if isinstance(other, (Q, int)) and type(other) in (Q, int):
            other = Poly.const(self.variables, other)
        self._same(other)
        d = dict(self.terms)
        for k,v in other.terms:
            d[k] = d.get(k, Q(0)) + v
        return Poly.from_dict(self.variables, d)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-self._same(other) if isinstance(other, Poly) else -_q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if type(other) in (int, Q):
            other = Poly.const(self.variables, other)
        self._same(other)
        d = {}
        for p,a in self.terms:
            for q,b in other.terms:
                e = tuple(x+y for x,y in zip(p,q))
                d[e] = d.get(e, Q(0)) + a*b
        return Poly.from_dict(self.variables, d)

    __rmul__ = __mul__

    def __pow__(self, n):
        if type(n) is not int or n < 0 or n > 64:
            raise ZeroDomainError('bounded nonnegative polynomial exponent required')
        out = Poly.const(self.variables, 1)
        base = self
        while n:
            if n&1: out = out * base
            base = base * base
            n >>= 1
        return out

    @property
    def is_zero(self):
        return not self.terms

    def substitute(self, images):
        """Exact Q-algebra homomorphism specified by ALL variable images."""
        if (type(images) is not tuple or len(images) != len(self.variables) or
                any(not isinstance(x, Poly) for x in images)):
            raise ZeroDomainError('one polynomial image per source variable required')
        names = images[0].variables
        if any(x.variables != names for x in images):
            raise ZeroDomainError('chart images must land in one ambient basis')
        out = Poly.const(names, 0)
        for exps,coeff in self.terms:
            term = Poly.const(names, coeff)
            for image,power in zip(images, exps):
                term = term * image**power
            out = out + term
        return out

    def at(self, values):
        if (type(values) is not tuple or len(values) != len(self.variables)):
            raise ZeroDomainError('evaluation must provide a coordinate per variable')
        vals = tuple(_q(x) for x in values)
        return sum((coeff * Q(1).numerator * _monomial(vals,exps)
                    for exps,coeff in self.terms),Q(0))


def _monomial(values, exponents):
    result = Q(1)
    for x,n in zip(values,exponents):
        result *= x**n
    return result


@dataclass(frozen=True)
class ZeroRelation:
    source_id: str
    chart: str
    expression: Poly

    def __post_init__(self):
        if not isinstance(self.source_id,str) or not self.source_id or not self.chart:
            raise ZeroDomainError('one declared source and chart required')


@dataclass(frozen=True)
class ZeroRoute:
    relation: ZeroRelation
    images: tuple[Poly, ...]
    multiplier: Poly

    def image(self):
        return self.relation.expression.substitute(self.images)


@dataclass(frozen=True)
class ZeroProof:
    """Certify target=sum multipliers*relations after chart transport.

    This is a *conditional* ideal-membership proof. The independent source
    truth of each defining relation and chart semantics must be established.
    """
    source_id: str
    target: Poly
    routes: tuple[ZeroRoute, ...]

    def check(self):
        if not self.routes or not self.source_id:
            raise ZeroDomainError('nonempty proof routes and named source required')
        value = Poly.const(self.target.variables, 0)
        for route in self.routes:
            if route.relation.source_id != self.source_id:
                raise ZeroDomainError('mixed original-source identities are not composable')
            if route.multiplier.variables != self.target.variables:
                raise ZeroDomainError('untransported multiplier basis')
            value = value + route.multiplier * route.image()
        if value != self.target:
            raise ZeroDomainError('declared balance is not a polynomial identity')
        return True

    @property
    def inconsistent_unit_witness(self):
        self.check()
        return self.target == Poly.const(self.target.variables,1)


def bbp_zero_balance():
    """A source-specific sum of TWO charted zeros implies the factored kernel.

    P-A=0 in signed basis, Q-B=0 in factor basis, in ambient t,P,Q:
      P-(1-t)Q = (P-A) - (1-t)(Q-B).
    Crucial separate identity A=(1-t)B holds over Q[t].
    """
    signed=('t','P')
    factor=('t','Q')
    ambient=('t','P','Q')
    t,p,q = (Poly.var(ambient,n) for n in ambient)
    ts,ps = (Poly.var(signed,n) for n in signed)
    tf,qf = (Poly.var(factor,n) for n in factor)
    A = 4-2*ts**3-ts**4-ts**5
    B = (tf**2+2)*(tf**2+2*tf+2)
    r1=ZeroRelation('Q:authentic-four-pole-BBP', 'four-signed-poles',ps-A)
    r2=ZeroRelation('Q:authentic-four-pole-BBP','positive-factor',qf-B)
    target=p-(1-t)*q
    proof=ZeroProof('Q:authentic-four-pole-BBP',target,(
        ZeroRoute(r1,(t,p),Poly.const(ambient,1)),
        ZeroRoute(r2,(t,q),-(1-t)),
    ))
    proof.check()
    # An unconditional polynomial theorem: the two chart definitions
    # are compatible; positivity additionally needs the order on [0,1].
    if (4-2*t**3-t**4-t**5) != (1-t)*(t**2+2)*(t**2+2*t+2):
        raise AssertionError('authentic BBP polynomial identity failed')
    return proof


def bbp_finite_positive_kernel(t):
    """Finite exact positivity witness, [0,1]. Full claim is paper factor proof."""
    t=_q(t)
    if not Q(0)<=t<=1:
        raise ZeroDomainError('ordered chart [0,1] required')
    a=t*t+2
    b=(t+1)**2+1
    value=(1-t)*a*b
    assert value >= 0 and (value>0 if t<1 else value==0)
    return value


@dataclass(frozen=True)
class CycleObstruction:
    cycle: tuple[int,...]
    signed_sum: Q


@dataclass(frozen=True)
class CoboundarySolution:
    potential: tuple[Q,...]
    exact: bool


def finite_coboundary(successor, observable):
    """Solve f(v)=g(v)-g(Tv) on finite functional graph, or give a cycle witness.

    Necessity: cycle sums telescope to zero. Sufficiency follows by
    setting a gauge at each cycle and propagating backward along trees.
    """
    if (type(successor) is not tuple or not successor or
            type(observable) is not tuple or len(successor)!=len(observable)):
        raise ZeroDomainError('finite source graph and aligned observable required')
    n=len(successor)
    if any(type(x) is not int or not 0<=x<n for x in successor):
        raise ZeroDomainError('total deterministic successor in graph required')
    f=tuple(_q(x) for x in observable)
    potentials={}
    for start in range(n):
        if start in potentials:
            continue
        trail=[]
        pos={}
        v=start
        while v not in potentials and v not in pos:
            pos[v]=len(trail)
            trail.append(v)
            v=successor[v]
        if v in pos:
            cycle=tuple(trail[pos[v]:])
            total=sum((f[x] for x in cycle),Q())
            if total:
                return CycleObstruction(cycle,total)
            potentials[cycle[0]]=Q(0)
            for node in cycle[:-1]:
                potentials[successor[node]]=potentials[node]-f[node]
        for node in reversed(trail):
            if node not in potentials:
                potentials[node]=f[node]+potentials[successor[node]]
    g=tuple(potentials[i] for i in range(n))
    if any(g[i]-g[successor[i]]!=f[i] for i in range(n)):
        raise AssertionError('cohomological potential construction failed')
    return CoboundarySolution(g,True)


def base16_graph(modulus):
    if type(modulus) is not int or not 2<=modulus<=10000:
        raise ZeroDomainError('finite rational-circle modulus required')
    return tuple(16*n % modulus for n in range(modulus))


def digit_discrepancy(modulus):
    """Rational-circle digit-zero indicator minus uniform 1/16.

    Not a sampled pi orbit or a claim of Haar distribution.
    """
    if type(modulus) is not int or not 2<=modulus<=10000:
        raise ZeroDomainError('positive rational-circle denominator required')
    return tuple(Q(15,16) if (16*n)//modulus==0 else Q(-1,16)
                 for n in range(modulus))


def finite_orbit_sum(successor, observable, start, horizon):
    """Exact finite additive source current, not a universal asymptotic bound."""
    if (type(horizon) is not int or horizon<0 or horizon>100000
            or type(start) is not int or not 0<=start<len(successor)):
        raise ZeroDomainError('bounded source horizon/start required')
    if len(observable)!=len(successor):
        raise ZeroDomainError('misaligned observable')
    x=start
    total=Q(0)
    for _ in range(horizon):
        total+=_q(observable[x])
        x=successor[x]
    return total,x


@dataclass(frozen=True)
class BoundaryRelation:
    """Certified finite |left-right|<=cap in one declared value/source chart.

    The finite inequality is checked exactly. A sequence of such objects
    proves a limit equality only with an independently proved cap->0.
    """
    source_id: str
    value_chart: str
    left: Q
    right: Q
    cap: Q

    def __post_init__(self):
        if not self.source_id or not self.value_chart:
            raise ZeroDomainError('source and common value chart required')
        for value in (self.left,self.right,self.cap):
            if type(value) is not Q:
                raise ZeroDomainError('all finite endpoint quantities must be Fractions')
        if self.cap<0 or abs(self.left-self.right)>self.cap:
            raise ZeroDomainError('boundary cap fails to enclose exact residual')

    def add(self, other):
        if (not isinstance(other,BoundaryRelation) or
                (self.source_id,self.value_chart)!=(other.source_id,other.value_chart)):
            raise ZeroDomainError('no cross-source or untransported-chart summation')
        return BoundaryRelation(self.source_id,self.value_chart,
                                self.left+other.left,self.right+other.right,
                                self.cap+other.cap)

    def scale(self,scalar):
        c=_q(scalar)
        return BoundaryRelation(self.source_id,self.value_chart,
                                c*self.left,c*self.right,abs(c)*self.cap)


def finite_prefix_coboundary(values):
    """Every finite current telescopes; this does NOT provide sublinear debt."""
    if not isinstance(values,tuple):
        raise ZeroDomainError('finite source-indexed observations required')
    potential=[Q(0)]
    for v in values:
        potential.append(potential[-1]+_q(v))
    assert all(potential[i+1]-potential[i]==_q(v) for i,v in enumerate(values))
    return tuple(potential)


@dataclass(frozen=True)
class MinimaxCoboundary:
    """Optimal sup residual for rational f on a finite functional graph.

    f(v)=g(v)-g(Tv)+r(v). Residual supported on cycles, constant on each.
    ||r||_infty = max_cycles |mean_cycle(f)| is a global LOWER and UPPER bound.
    """
    potential: tuple[Q,...]
    residual: tuple[Q,...]
    optimal_uniform_residual: Q
    cycle_means: tuple[tuple[tuple[int,...],Q],...]


def finite_coboundary_minimax(successor, observable):
    """Exact sharp cycle-mean obstruction; no spectral/normality claims.

    For any potential g, sum_cycle (g-gT)=0, so max |residual|
    >= max_cycle |mean f|. The constructed r achieves equality.
    """
    if (type(successor) is not tuple or not successor or
            type(observable) is not tuple or len(observable)!=len(successor)):
        raise ZeroDomainError('finite functional graph and observable required')
    n=len(successor)
    if any(type(x) is not int or not 0<=x<n for x in successor):
        raise ZeroDomainError('total deterministic finite successor required')
    f=tuple(_q(x) for x in observable)
    residual=[Q(0)]*n
    assigned=set()
    witnesses=[]
    for start in range(n):
        if start in assigned:
            continue
        history=[]
        position={}
        i=start
        while i not in position and i not in assigned:
            position[i]=len(history)
            history.append(i)
            i=successor[i]
        if i in position:
            cycle=tuple(history[position[i]:])
            mean=sum((f[j] for j in cycle),Q(0))/len(cycle)
            witnesses.append((cycle,mean))
            for j in cycle:
                residual[j]=mean
        assigned.update(history)
    difference=tuple(f[i]-residual[i] for i in range(n))
    solution=finite_coboundary(successor,difference)
    if not isinstance(solution,CoboundarySolution):
        raise AssertionError('cycle-mean subtraction must make source exact')
    cap=max((abs(m) for _,m in witnesses),default=Q(0))
    if (max(abs(x) for x in residual)!=cap or
            any(solution.potential[i]-solution.potential[successor[i]]+residual[i]!=f[i]
                for i in range(n))):
        raise AssertionError('optimal obstruction decomposition not certified')
    return MinimaxCoboundary(solution.potential,tuple(residual),cap,tuple(witnesses))
