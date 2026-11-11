"""Proof-oriented exact arithmetic for the source-zero BBP/Dedekind fingerprint.

Original four-pole BBP is immutable; geometric pi and pi irrationality are
classical mathematical imports.  No normality, cancellation, Lean, or CI claim.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q


class Unresolved(RuntimeError):
    """Finite budget exhausted; epistemic result is UNKNOWN, never FALSE."""


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self):
        if type(self.lo) is not Q or type(self.hi) is not Q or not self.lo < self.hi:
            raise ValueError("strict rational interval required")

    @property
    def width(self) -> Q:
        return self.hi-self.lo

    @property
    def mid(self) -> Q:
        return (self.lo+self.hi)/2

    def scale(self, a: Q) -> Interval:
        if type(a) is not Q or a <= 0:
            raise ValueError("strictly positive Fraction scale required")
        return Interval(a*self.lo,a*self.hi)


def _natural(n: int, label: str, minimum: int=0):
    if type(n) is not int or n < minimum:
        raise ValueError(f"{label}: exact integer >= {minimum} required")
    return n


def r(n: int) -> Q:
    """Original four signed poles; n>=1. No mutable source callback."""
    _natural(n,"forcing clock",1)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def r_factored(n: int) -> Q:
    """Separately factored canonical identity from duck_bbp.py."""
    _natural(n,"forcing clock",1)
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def P(n: int) -> Q:
    _natural(n,"prefix depth")
    return sum((r(j)/16**j for j in range(1,n+1)),Q(0))


def bbp_x(n: int) -> Interval:
    """Source-derived strict interval for x=pi/16, selected seed exactly zero."""
    _natural(n,"depth")
    low=P(n)
    return Interval(low,low+r(n+1)/Q(15*16**n))


def circle_x(k: int) -> Interval:
    """Independent circle-beta algorithm for pi/16; relies on Euclidean arclength."""
    _natural(k,"circle stage")
    term=Q(1)
    total=Q(0)
    for j in range(k):
        total+=2*term
        term*=Q(j+1,2*j+3)
    return Interval((total+3*term)/16,(total+4*term)/16)


@dataclass(frozen=True)
class AffineX:
    """Formal const + coeff*x, x=pi/16. Pair equality uses pi irrationality."""
    const: Q
    coeff: Q

    def __post_init__(self):
        if type(self.const) is not Q or type(self.coeff) is not Q:
            raise TypeError("seed normal form must be exact Fraction coordinates")

    def __add__(self, other: AffineX) -> AffineX:
        if type(other) is not AffineX:
            return NotImplemented
        return AffineX(self.const+other.const,self.coeff+other.coeff)

    def __sub__(self, other: AffineX) -> AffineX:
        if type(other) is not AffineX:
            return NotImplemented
        return AffineX(self.const-other.const,self.coeff-other.coeff)

    def scale(self, factor: Q) -> AffineX:
        if type(factor) is not Q:
            raise TypeError("rational factor required")
        return AffineX(factor*self.const,factor*self.coeff)

    def bounds(self, x_interval: Interval) -> Interval:
        if self.coeff > 0:
            return Interval(self.const+self.coeff*x_interval.lo,
                            self.const+self.coeff*x_interval.hi)
        if self.coeff < 0:
            return Interval(self.const+self.coeff*x_interval.hi,
                            self.const+self.coeff*x_interval.lo)
        # For rational values return equality as a rational scalar, not a false strict interval.
        raise ValueError("rational affine value is exact, not a nondegenerate interval")

    @property
    def is_zero(self) -> bool:
        return self.const == 0 and self.coeff == 0


ZERO=AffineX(Q(0),Q(0))
COHERENT_WRONG=AffineX(Q(0),Q(-1))
RATIONAL_ALIAS=AffineX(Q(1,16),Q(0))


def state(n: int,seed: AffineX=ZERO) -> AffineX:
    """Unwrapped U_n(s)=16^n(s+P_n) in the Q-span of 1 and x."""
    _natural(n,"clock")
    if type(seed) is not AffineX:
        raise TypeError("explicit, exact rational-affine seed needed")
    return AffineX(16**n*(seed.const+P(n)),16**n*seed.coeff)



def affine_clock(n: int,u: AffineX,a: int,b: int) -> tuple[int,AffineX]:
    """Source-faithful arithmetic clock arrow n->a*n+b retaining the seed.

    Composition: (a,b) o (c,d)=(a*c,a*d+b). D_p S=S^p D_p.
    This is a typed map of *indexed* source states, not multiplication of u.
    """
    _natural(n,"clock")
    _natural(a,"clock dilation",1)
    _natural(b,"clock translation")
    if type(u) is not AffineX:
        raise TypeError("symbolic source state required")
    m=a*n+b
    return m,state(m,recovered_seed(n,u))


def next_state(n: int,u: AffineX) -> AffineX:
    _natural(n,"clock")
    if type(u) is not AffineX:
        raise TypeError("symbolic state required")
    return u.scale(Q(16))+AffineX(r(n+1),Q(0))


def recovered_seed(n: int,u: AffineX) -> AffineX:
    _natural(n,"clock")
    if type(u) is not AffineX:
        raise TypeError("symbolic state required")
    return u.scale(Q(1,16**n))-AffineX(P(n),Q(0))


def complete(n: int,seed: AffineX=ZERO) -> AffineX:
    """The *real* completed phase before fractional reduction: 16^n(x+seed)."""
    _natural(n,"clock")
    if type(seed) is not AffineX:
        raise TypeError("symbolic seed required")
    return AffineX(16**n*seed.const,16**n*(seed.coeff+1))


def future_tail(n: int) -> AffineX:
    """Exact symbolic T_n=16^n(x-P_n), positive via source bounds."""
    _natural(n,"clock")
    return AffineX(-16**n*P(n),Q(16**n))


def eventual_phase_alias(a: AffineX,b: AffineX) -> int | None:
    """Least n such that {16^k(x+a)}={16^k(x+b)} for all k>=n.

    For rational-affine seeds, pi irrationality eliminates any nonzero x coefficient.
    None means no such finite n, not a finite runtime budget expiration.
    """
    if type(a) is not AffineX or type(b) is not AffineX:
        raise TypeError("exact seed pairs required")
    delta=a-b
    if delta.coeff:
        return None
    denom=delta.const.denominator
    exponent=0
    while denom%2==0:
        denom//=2
        exponent+=1
    return (exponent+3)//4 if denom==1 else None


def certify_root(epsilon: Q, *, max_depth: int=200) -> dict:
    """Two-source interval pullback; identity of their limits is an imported theorem."""
    if type(epsilon) is not Q or epsilon <= 0:
        raise ValueError("strict positive rational tolerance needed")
    _natural(max_depth,"budget")
    for n in range(max_depth+1):
        source=bbp_x(n)
        geometry=circle_x(n)
        low=max(source.lo,geometry.lo)
        high=min(source.hi,geometry.hi)
        if not low < high:
            raise ValueError("independent source intervals conflict at a common stage")
        if high-low<epsilon:
            return {"depth":n,"bbp":source,"geometry":geometry,
                    "intersection":Interval(low,high)}
    raise Unresolved("UNKNOWN: requested precision beyond finite budget")


def rational_probe(q: Q, *, max_depth: int=200) -> tuple[str,int]:
    """Total for rational q on the authenticated irrational root, given enough depth."""
    if type(q) is not Q:
        raise TypeError("a rational probe is required")
    _natural(max_depth,"budget")
    for n in range(max_depth+1):
        interval=bbp_x(n)
        if q <= interval.lo:
            return ("BELOW_ROOT",n)
        if q >= interval.hi:
            return ("ABOVE_ROOT",n)
    raise Unresolved("UNKNOWN: unresolved comparison in finite budget")


@dataclass(frozen=True)
class PhaseCertificate:
    n: int
    depth: int
    k: int
    phase: Interval
    source_lift: Interval
    future_tail: Interval

    @property
    def midpoint_error(self)->Q:
        return self.phase.width/2


def certify_phase(n: int, *, seed: AffineX=ZERO, max_depth: int=200,
                  digit_chart: bool=True) -> PhaseCertificate:
    """Exactly certify z_n={16^n*x}, including carry and branch chart.

    Rejects wrong seeds rather than quietly re-using the origin-selected bounds.
    """
    _natural(n,"clock")
    _natural(max_depth,"budget")
    if type(seed) is not AffineX or not seed.is_zero:
        raise ValueError("nonzero seed: authenticated zero-root certificate cannot be re-used")
    unwrapped=state(n,seed)
    assert unwrapped.coeff==0
    for depth in range(n,max_depth+1):
        box=bbp_x(depth)
        lo,hi=16**n*box.lo,16**n*box.hi
        k=lo.numerator//lo.denominator
        if k!=hi.numerator//hi.denominator or not Q(k)<lo<hi<Q(k+1):
            continue
        p=Interval(lo-k,hi-k)
        if digit_chart:
            low16=16*p.lo
            hi16=16*p.hi
            if low16.numerator//low16.denominator!=hi16.numerator//hi16.denominator:
                continue
        tail=Interval(lo-unwrapped.const,hi-unwrapped.const)
        if not tail.lo>0:
            continue
        return PhaseCertificate(n,depth,k,p,Interval(lo,hi),tail)
    raise Unresolved("UNKNOWN: source precision not enough for winding and digit chart")


def certify_phase_window(N: int, *, max_depth: int=250) -> tuple[PhaseCertificate,...]:
    """All zero-seed phases carry certified real/digit-branch charts."""
    _natural(N,"window length",1)
    return tuple(certify_phase(n,max_depth=max_depth) for n in range(N))


def exact_hex_prefix(digits: int, *, max_depth: int=200) -> tuple[int,...]:
    _natural(digits,"hex digits",1)
    _natural(max_depth,"budget")
    for n in range(max(1,digits),max_depth+1):
        box=bbp_x(n)
        scale=16**digits
        low,hi=scale*box.lo,scale*box.hi
        a=low.numerator//low.denominator
        b=hi.numerator//hi.denominator
        if a==b:
            return tuple((a//16**(digits-i-1))%16 for i in range(digits))
    raise Unresolved("UNKNOWN: finite digit prefix not certified")


def finite_word_counts(N: int, k: int) -> Counter:
    """Actual source-selected finite word counts; does NOT claim asymptotic limits."""
    _natural(N,"observation count",1)
    _natural(k,"word length",1)
    digits=exact_hex_prefix(N+k-1,max_depth=max(200,N+k+6))
    return Counter(tuple(digits[n:n+k]) for n in range(N))


def weyl_budget(N: int, h: int, depth: int) -> Q:
    """Certified |W_N,h(x) - W_N,h(mid I_depth)| bound for e(t)=exp(2pi i t).

    Uses only 2pi<8 and exact source width, not any asymptotic cancellation.
    """
    _natural(N,"N",1)
    _natural(depth,"depth")
    if type(h) is not int:
        raise TypeError("integer Fourier frequency required")
    return Q(4*abs(h)*(16**N-1),15*N)*bbp_x(depth).width


def epoch_weyl_budget(A: int,h: int,depth: int)->Q:
    _natural(A,"epoch",1)
    _natural(depth,"depth")
    if type(h) is not int:
        raise TypeError("integer Fourier frequency required")
    return Q(4*abs(h)*(16**(2*A)-16**A),15*A)*bbp_x(depth).width


def ratio_fiber_budget(A: int,h: int,depth: int)->Q:
    """Approximation budget for #593's h*(16^(3l)-16^(2l))*x phase."""
    _natural(A,"epoch",2)
    _natural(depth,"depth")
    if type(h) is not int:
        raise TypeError("integer Fourier frequency required")
    j=range(max(1,(A+1)//2),(2*A-1)//3+1)
    coefficients=[16**(3*l)-16**(2*l) for l in j]
    if not coefficients:
        raise ValueError("ratio fiber requires a nonempty genuine 2:3 epoch")
    return Q(4*abs(h)*sum(coefficients),len(coefficients))*bbp_x(depth).width


def source_completion_budget(N: int,h: int)->Q:
    """Certified |mean e(h*U_n)-mean e(h*16^n*x)|; n in [0,N)."""
    _natural(N,"N",1)
    if type(h) is not int:
        raise TypeError("integer Fourier frequency required")
    return Q(8*abs(h),15*N)*sum((r(n+1) for n in range(N)),Q(0))


def _cdf_distance(positive: tuple[Q,...],negative: tuple[Q,...]) -> Q:
    """Exact 1-Wasserstein on [0,1] via the signed CDF of rational atomic laws."""
    m=len(positive)
    if not m or len(negative)!=m:
        raise ValueError("nonempty equal-weight probability laws required")
    signed=defaultdict(Q)
    for x in positive:
        if type(x) is not Q or not 0<=x<1:
            raise ValueError("unit-interval Fraction atom required")
        signed[x]+=Q(1,m)
    for x in negative:
        if type(x) is not Q or not 0<=x<1:
            raise ValueError("unit-interval Fraction atom required")
        signed[x]-=Q(1,m)
    cdf=Q(0)
    old=Q(0)
    value=Q(0)
    for x in sorted(signed):
        value+=abs(cdf)*(x-old)
        cdf+=signed[x]
        old=x
    assert cdf==0
    return value


def haar_defect(phases: tuple[Q,...]) -> Q:
    """Exact D_N=W1(mu_N,Qmu_N) for rational phases in [0,1)."""
    if not phases:
        raise ValueError("nonempty phase sequence")
    shifted=tuple((z+Q(a,16))%1 for z in phases for a in range(16))
    return _cdf_distance(tuple(z for z in phases for _ in range(16)),shifted)


@dataclass(frozen=True)
class SignedOverlapReceipt:
    early: Q
    late: Q
    entire: Q
    overlap: Q
    overlap_error: Q
    midpoint_depths: tuple[int,...]

    @property
    def certified_lower(self)->Q:
        return max(Q(0),self.overlap-self.overlap_error)

    @property
    def certified_upper(self)->Q:
        return self.overlap+self.overlap_error


def signed_overlap_receipt(M: int, *, max_depth: int=250) -> SignedOverlapReceipt:
    """Exact rational midpoint overlap + certified absolute error for true π zero orbit.

    Branch-chart verified phases ensure each Q translation is isometric on its
    local cell. Therefore |D_true-D_mid|<= 2*mean midpoint phase errors.
    Formula is the exact #591 signed adjacent-block CDF identity.
    """
    _natural(M,"half-window",1)
    certs=certify_phase_window(2*M,max_depth=max_depth)
    mids=tuple(c.phase.mid for c in certs)
    early=haar_defect(mids[:M])
    late=haar_defect(mids[M:])
    entire=haar_defect(mids)
    overlap=(early+late)/2-entire
    if overlap<0:
        raise AssertionError("exact signed overlap cannot be negative")
    error_early=Q(2,M)*sum((c.midpoint_error for c in certs[:M]),Q(0))
    error_late=Q(2,M)*sum((c.midpoint_error for c in certs[M:]),Q(0))
    error_entire=Q(1,M)*sum((c.midpoint_error for c in certs),Q(0))
    error=(error_early+error_late)/2+error_entire
    return SignedOverlapReceipt(early,late,entire,overlap,error,tuple(c.depth for c in certs))
