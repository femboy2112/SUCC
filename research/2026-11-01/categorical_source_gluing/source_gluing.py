"""Exact research adapters for source-labelled SUCC; no new category core.

The canonical category spine remains observational_succ.operational_yoneda_descent.
All scalars below are rational. Complex phases are encoded modulo one, never
rounded. Symbolic curve certificates are generated separately with SymPy.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from typing import Callable, Hashable, Iterable

class CarrierError(ValueError):
    """A domain, composability, source, or selected-branch check failed."""


def integer(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise CarrierError(f'exact integer >= {minimum} required')
    return n


def rational(x: int | F) -> F:
    if type(x) not in (int, F):
        raise CarrierError('exact rational input required; floats and booleans forbidden')
    return F(x)


def source(z: int | F) -> F:
    z = rational(z)
    try:
        return 4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
    except ZeroDivisionError as exc:
        raise CarrierError('original source pole') from exc


def source_combined(z: int | F) -> F:
    z = rational(z)
    try:
        return (120*z*z-89*z+16)/((2*z-1)*(4*z-1)*(8*z-7)*(8*z-3))
    except ZeroDivisionError as exc:
        raise CarrierError('original source pole') from exc


def cover(z: int | F) -> F:
    z = rational(z)
    try:
        return (8*z-7)**4/((8*z-4)**2*(8*z-3)*(8*z-2))
    except ZeroDivisionError as exc:
        raise CarrierError('use the projective chart at a cover pole') from exc


def orbit(n: int, seed: int | F = 0) -> F:
    integer(n)
    out = rational(seed)
    for j in range(1, n+1):
        out = 16*out+source(j)
    return out


def orbit_convolution(n: int, seed: int | F = 0) -> F:
    integer(n)
    return 16**n*rational(seed)+sum((16**(n-j)*source_combined(j) for j in range(1,n+1)), F(0))


def source_conductor(n: int) -> int:
    integer(n)
    out = 1
    for j in range(1,n+1):
        out = lcm(out, source(j).denominator)
    return out


def cocycle(z: int | F, length: int) -> F:
    z = rational(z); integer(length)
    return sum((16**(length-j)*source(z+j) for j in range(1,length+1)), F(0))


@dataclass(frozen=True)
class LiftedState:
    """Source time AND affine state; time reconstruction does not select a seed."""
    z: F
    amplitude: F
    def __post_init__(self):
        object.__setattr__(self,'z',rational(self.z))
        object.__setattr__(self,'amplitude',rational(self.amplitude))
    def advance(self, length: int = 1) -> LiftedState:
        integer(length)
        return LiftedState(self.z+length,16**length*self.amplitude+cocycle(self.z,length))
    def delay_observation(self) -> tuple[F,F,F]:
        return cover(self.z), cover(self.z+1), self.amplitude


@dataclass(frozen=True)
class SourcePath:
    """One source-synchronized word, not an endpoint-only observation arrow."""
    states: tuple[LiftedState,...]
    def __post_init__(self):
        if type(self.states) is not tuple or not self.states or any(type(x) is not LiftedState for x in self.states):
            raise CarrierError('nonempty lifted-state path required')
        if any(a.advance()!=b for a,b in zip(self.states,self.states[1:])):
            raise CarrierError('false source seam or changed forcing')
    @classmethod
    def build(cls, start: LiftedState, length: int) -> SourcePath:
        integer(length)
        xs=[start]
        for _ in range(length):xs.append(xs[-1].advance())
        return cls(tuple(xs))
    def then(self, following: SourcePath) -> SourcePath:
        if self.states[-1]!=following.states[0]:
            raise CarrierError('composable observations are not necessarily composable source lifts')
        return SourcePath(self.states+following.states[1:])


@dataclass(frozen=True)
class AffineWord:
    """Counterfactual source-order words; chronological path is a distinguished word."""
    indices: tuple[int,...]
    def __post_init__(self):
        if type(self.indices) is not tuple:raise CarrierError('ordered tuple required')
        for n in self.indices:integer(n,1)
    def apply(self, seed: int | F = 0) -> F:
        state=rational(seed)
        for n in self.indices:state=16*state+source(n)
        return state
    def then(self, following: AffineWord) -> AffineWord:
        return AffineWord(self.indices+following.indices)


def eval_bivariate(terms: Iterable, u: F, v: F) -> F:
    u=rational(u);v=rational(v)
    return sum((F(int(c))*u**int(p[0])*v**int(p[1]) for p,c in terms),F(0))


def recover_source(u: int | F, v: int | F, certificate: dict) -> F:
    """One rational chart of the normalized delay curve; checks BOTH observations."""
    u=rational(u);v=rational(v)
    a=eval_bivariate(certificate['inverse_denominator_terms'],u,v)
    if not a:raise CarrierError('exceptional inverse chart: retain the normalized sheet')
    z=eval_bivariate(certificate['inverse_numerator_terms'],u,v)/a
    if cover(z)!=u or cover(z+1)!=v:
        raise CarrierError('not a source-realizable delayed observation pair')
    return z


def odd_register(Q: int) -> int:
    integer(Q,1)
    if gcd(16,Q)!=1:raise CarrierError('radix16 requires an odd arithmetic register')
    return Q


def address(Q: int, x: int | F) -> int:
    odd_register(Q);y=Q*rational(x)
    if y.denominator!=1:raise CarrierError('register does not contain this exact rational phase')
    return int(y)%Q


def ket_image(Q: int, n: int, x: int) -> int:
    odd_register(Q);integer(n);integer(x)
    if x>=Q:raise CarrierError('basis index outside register')
    return (16**n*x+address(Q,orbit(n)))%Q


def phase_Q(Q: int, k: int, x: int) -> F:
    integer(Q,1)
    if type(k) is not int or type(x) is not int:raise CarrierError('integer phase labels required')
    return F(k*x,Q)%1


def source_phase(n: int, h: int, seed: int | F = 0) -> F:
    if type(h) is not int:raise CarrierError('integer harmonic required')
    return (h*orbit(n,seed))%1


def dilation_embedding(Q: int, Qbig: int, x: int) -> int:
    odd_register(Q);odd_register(Qbig);integer(x)
    if Qbig%Q or x>=Q:raise CarrierError('non-divisible conductor or invalid basis')
    return (Qbig//Q)*x


def frequency_embedding_norm_squared(Q: int, Qbig: int) -> F:
    odd_register(Q);odd_register(Qbig)
    if Qbig%Q:raise CarrierError('non-divisible conductors')
    return F(Q,Qbig)


def phase_echo(Q: int, n: int, h: int, x: int) -> F:
    """Exact scalar of P* C_h P C_-h16^n on a basis vector."""
    return (phase_Q(Q,h,ket_image(Q,n,x))-phase_Q(Q,h*16**n,x))%1


# Finite characteristic controls test categorical laws, NOT real-circle arithmetic.
def prime(p: int) -> int:
    integer(p,7)
    if any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise CarrierError('prime >5 required')
    return p


def projective_cover_table(p: int) -> tuple[int,...]:
    """Point p denotes infinity; R(infinity)=1. Entire P1(F_p), no deleted poles."""
    prime(p);out=[]
    for z in range(p):
        A=(8*z-7)**4%p;D=((8*z-4)**2*(8*z-3)*(8*z-2))%p
        if not D and not A:raise CarrierError('bad reduction')
        out.append((A*pow(D,-1,p))%p if D else p)
    return tuple(out+[1])


def successor_table(p: int) -> tuple[int,...]:
    prime(p)
    return tuple((z+1)%p for z in range(p))+(p,)


def descent_obstruction(q: tuple[Hashable,...], S: tuple[int,...]) -> tuple[int,int] | None:
    if len(q)!=len(S) or any(type(t) is not int or not 0<=t<len(q) for t in S):
        raise CarrierError('invalid finite transition table')
    for x in range(len(q)):
        for y in range(x):
            if q[x]==q[y] and q[S[x]]!=q[S[y]]:return y,x
    return None


def future_partition(q: tuple[Hashable,...], S: tuple[int,...]) -> tuple[int,...]:
    """Coarsest successor-stable refinement of the declared observation kernel."""
    if len(q)!=len(S) or any(type(x) is not int or not 0<=x<len(q) for x in S):raise CarrierError('invalid finite tables')
    def labels(items):
        d={};out=[]
        for x in items:
            if x not in d:d[x]=len(d)
            out.append(d[x])
        return tuple(out)
    colors=labels(q)
    for _ in range(len(q)+1):
        new=labels(tuple((colors[x],colors[S[x]]) for x in range(len(q))))
        if new==colors:return colors
        colors=new
    raise ArithmeticError('partition refinement did not stabilize')


def false_span_gluing(p: int) -> tuple[int,int,int,int]:
    """Witness x,y: R(Sx)=R(y), but y!=Sx and R(Sy)!=R(S²x)."""
    q=projective_cover_table(p);S=successor_table(p)
    for x in range(p+1):
        for y in range(p+1):
            if q[S[x]]==q[y] and y!=S[x] and q[S[y]]!=q[S[S[x]]]:
                return x,y,q[S[S[x]]],q[S[y]]
    raise CarrierError('no witness in this finite control')


def dyadic_branch_index(Q: int, digit: int, x: int) -> int:
    integer(Q,1);integer(x);integer(digit)
    if digit>=16 or x>=Q:raise CarrierError('invalid full radix16 branch')
    return 16*x+digit


def advance_delay(u: int | F, v: int | F, certificate: dict) -> tuple[F,F]:
    """Exact rational second-order evolution; generic chart, total on n>=0."""
    z=recover_source(u,v,certificate)
    return rational(v),cover(z+2)


def advance_observed_state(u: int | F, v: int | F, amplitude: int | F, certificate: dict) -> tuple[F,F,F]:
    """Source-faithful skew product reconstructed from two adjacent snapshots."""
    z=recover_source(u,v,certificate)
    return rational(v),cover(z+2),16*rational(amplitude)+source(z+1)
