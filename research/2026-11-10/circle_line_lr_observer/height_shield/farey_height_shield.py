"""Exact finite-height Farey shields for a source-certified irrational (pi).

A finite algorithm emits a certificate excluding ALL rationals with denominator
<= H at once, then a strictly positive rational distance lower bound.
The existence proof imports pi irrationality and source enclosure theorems.
This does NOT prove digit statistics, pi irrationality, or RH.

Independent, minimal source implementations: a Euclidean circle-beta contraction
(from SUCC circle_line_lr_observer) and the original four-pole BBP source.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial
from typing import Literal

SourceKind = Literal["circle_beta", "bbp_four_pole", "sparse_nonnormal"]


def _integer(x: int, name: str, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return x


def four_pole(j: int) -> Q:
    _integer(j, "clock", 1)
    return Q(4, 8*j-7)-Q(2, 8*j-4)-Q(1, 8*j-3)-Q(1, 8*j-2)


@dataclass(frozen=True)
class RationalInterval:
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if type(self.lo) is not Q or type(self.hi) is not Q or not self.lo < self.hi:
            raise ValueError("require exact Fraction endpoints lo<hi")


class CircleBetaSource:
    """Independent rational recurrence for geometry's pi=2 sum W_n.

    W_0=1, W_(n+1)=W_n*(n+1)/(2*n+3);
    I_k=(2 sum_(n<k) W_n + 3 W_k, ...+4 W_k), width W_k<2^-k.
    Classically, geometric circle/line calculus identifies the limit with pi.
    """
    kind: SourceKind = "circle_beta"

    def __init__(self) -> None:
        self.stage = 0
        self.prefix = Q(0)
        self.term = Q(1)
        self.interval = RationalInterval(Q(3), Q(4))

    def refine(self) -> None:
        k = self.stage
        self.prefix += 2*self.term
        self.term *= Q(k+1, 2*k+3)
        self.stage += 1
        self.interval = RationalInterval(self.prefix+3*self.term,
                                          self.prefix+4*self.term)


class BBPFourPoleSource:
    """Original signed r(j), literal zero seed, positive source tail.

    Pi= sum_(j>=1) 16^(1-j) r(j); residual after stage k is bounded
    by 16^(1-k)*r(k+1)/15 using positivity and monotonicity.
    The classical BBP evaluation of this series as pi is an import.
    """
    kind: SourceKind = "bbp_four_pole"

    def __init__(self) -> None:
        self.stage = 0
        self.prefix = Q(0)
        self.interval = RationalInterval(Q(3), Q(4))

    def refine(self) -> None:
        j = self.stage + 1
        self.prefix += four_pole(j) / 16**(j-1)
        self.stage += 1
        self.interval = RationalInterval(
            self.prefix,
            self.prefix + four_pole(j+1)*Q(16, 15*16**j),
        )


class SparseNonnormalSource:
    """Hostile computable irrational: 3 + sum_(j>=1)16^(-j!).

    Its base-16 expansion has ones exactly at factorial places. Infinitely
    many ones with growing zero gaps prove non-eventual-periodicity (and
    irrationality), while the density of ones is zero (not normal).
    """
    kind: SourceKind = "sparse_nonnormal"

    def __init__(self) -> None:
        self.stage = 0
        self.prefix = Q(3)
        self.interval = RationalInterval(Q(3), Q(4))

    def refine(self) -> None:
        j = self.stage + 1
        self.prefix += Q(1, 16**factorial(j))
        self.stage += 1
        next_place = factorial(j+1)
        self.interval = RationalInterval(
            self.prefix, self.prefix+Q(16, 15*16**next_place))


def source(kind: SourceKind):
    if kind == "circle_beta":
        return CircleBetaSource()
    if kind == "bbp_four_pole":
        return BBPFourPoleSource()
    if kind == "sparse_nonnormal":
        return SparseNonnormalSource()
    raise ValueError("unknown source kind")


@dataclass(frozen=True)
class FareyBracket:
    a: int = 3
    b: int = 1
    c: int = 4
    d: int = 1

    def __post_init__(self):
        if any(type(v) is not int for v in (self.a,self.b,self.c,self.d)):
            raise ValueError("Farey matrix requires integer fields")
        if self.b < 1 or self.d < 1 or self.b*self.c-self.a*self.d != 1:
            raise ValueError("positive-denominator Farey neighbors required")

    @property
    def lo(self) -> Q:
        return Q(self.a, self.b)

    @property
    def hi(self) -> Q:
        return Q(self.c, self.d)

    @property
    def denominator_threshold(self) -> int:
        return self.b + self.d

    @property
    def width(self) -> Q:
        return Q(1, self.b*self.d)

    @property
    def tuple(self) -> tuple[int,int,int,int]:
        return self.a,self.b,self.c,self.d

    def run(self, arrow: str, count: int) -> FareyBracket:
        _integer(count, "count", 1)
        if arrow == "L":
            return FareyBracket(self.a, self.b,
                                self.c+count*self.a, self.d+count*self.b)
        if arrow == "R":
            return FareyBracket(self.a+count*self.c,
                                self.b+count*self.d, self.c, self.d)
        raise ValueError("arrow must be L or R")


@dataclass(frozen=True)
class RunCertificate:
    before: tuple[int,int,int,int]
    after: tuple[int,int,int,int]
    arrow: str
    count: int
    complete_run: bool
    source_stage: int
    source_lo: Q
    source_hi: Q
    ratio_lower: Q
    ratio_upper: Q


@dataclass(frozen=True)
class ShieldCertificate:
    source_kind: str
    height: int
    steps: int
    runs: tuple[RunCertificate,...]
    final: tuple[int,int,int,int]
    final_source_stage: int
    final_source_lo: Q
    final_source_hi: Q
    uniform_margin: Q

    def classify(self, candidate: Q) -> str:
        """Compare the selected real with any rational denominator <= height."""
        if type(candidate) is not Q or candidate.denominator > self.height:
            raise ValueError("candidate must be a Fraction with denominator <= height")
        b = FareyBracket(*self.final)
        if candidate <= b.lo:
            return "BELOW_TARGET"
        if candidate >= b.hi:
            return "ABOVE_TARGET"
        raise ValueError("certificate invariant violated: small denominator inside")


class BudgetExhausted(RuntimeError):
    """A finite computation has not resolved the query: UNKNOWN, not FALSE."""


class MacroObserver:
    def __init__(self, kind: SourceKind):
        self.kind = kind
        self.s = source(kind)
        self.b = FareyBracket()
        self.steps = 0

    def refine_to_interior(self, max_refinements: int = 1024) -> None:
        """Get a rational source interval strictly inside current Farey bracket."""
        _integer(max_refinements, "max_refinements")
        count = 0
        while not (self.b.lo < self.s.interval.lo < self.s.interval.hi < self.b.hi):
            if count >= max_refinements:
                raise BudgetExhausted("UNKNOWN: insufficient source refinement")
            self.s.refine()
            count += 1

    def next_run(self, target_height: int | None = None,
                 max_refinements: int = 1024) -> RunCertificate:
        """Output a certified R^k/L^k block; truncate at height H if requested.

        For a truncated run, only the lower bound on the residual quotient
        is necessary. A complete run additionally certifies the upper bound.
        """
        if target_height is not None:
            _integer(target_height,"target_height",1)
            if self.b.denominator_threshold > target_height:
                raise ValueError("height already shielded")
        self.refine_to_interior(max_refinements)
        count = 0
        while True:
            lo, hi = self.s.interval.lo, self.s.interval.hi
            a,b,c,d = self.b.tuple
            u_lo, v_lo = b*lo-a, c-d*lo
            u_hi, v_hi = b*hi-a, c-d*hi
            assert min(u_lo,v_lo,u_hi,v_hi) > 0
            right_min, right_max = u_lo/v_lo, u_hi/v_hi
            left_min, left_max = v_hi/u_hi, v_lo/u_lo
            arrow = None
            for direction, lower, upper, gain in (
                ("R",right_min,right_max,d), ("L",left_min,left_max,b)):
                if lower < 1:
                    continue
                k = lower.numerator // lower.denominator
                # Enough consecutive steps to shield all height-H rationals.
                need = None if target_height is None else (
                    (target_height-(b+d))//gain + 1)
                if need is not None and k >= need:
                    n = need
                    complete = bool(n==k and upper<=k+1)
                    arrow, ratio_min, ratio_max = direction, lower, upper
                    break
                if upper <= k+1:
                    n = k
                    complete = True
                    arrow, ratio_min, ratio_max = direction, lower, upper
                    break
            if arrow is not None:
                old = self.b
                self.b = old.run(arrow, n)
                self.steps += n
                return RunCertificate(old.tuple, self.b.tuple, arrow, n,
                    complete, self.s.stage, lo, hi, ratio_min, ratio_max)
            if count >= max_refinements:
                raise BudgetExhausted("UNKNOWN: run length unresolved at depth budget")
            self.s.refine()
            count += 1

    def shield(self, height: int, max_refinements: int = 1024) -> ShieldCertificate:
        _integer(height,"height",1)
        runs=[]
        while self.b.denominator_threshold <= height:
            run=self.next_run(target_height=height, max_refinements=max_refinements)
            runs.append(run)
        self.refine_to_interior(max_refinements)
        gap = min(self.s.interval.lo-self.b.lo, self.b.hi-self.s.interval.hi)
        assert gap>0 and self.b.denominator_threshold>height
        return ShieldCertificate(self.kind,height,self.steps,tuple(runs),self.b.tuple,
            self.s.stage,self.s.interval.lo,self.s.interval.hi,gap)


def certify_height(height: int, kind: SourceKind="circle_beta",
                   max_refinements: int=1024) -> ShieldCertificate:
    return MacroObserver(kind).shield(height,max_refinements)


def verify_height_certificate(cert: ShieldCertificate) -> bool:
    """Independent replay of all arrow and source data, no floating-point values.

    The source arithmetic is recalculated at the claimed stage. Its semantic
    link to geometric pi and pi irrationality is a written-proof dependency.
    """
    if type(cert) is not ShieldCertificate:
        raise ValueError("invalid certificate")
    _integer(cert.height,"height",1)
    src=source(cert.source_kind)
    cur=FareyBracket()
    steps=0
    last_stage=0
    for run in cert.runs:
        if type(run) is not RunCertificate or run.before!=cur.tuple:
            raise ValueError("broken arrow ancestry")
        _integer(run.source_stage,"source_stage")
        if run.source_stage < last_stage:
            raise ValueError("source precision moved backward")
        while src.stage < run.source_stage:
            src.refine()
        if (run.source_lo,run.source_hi)!=(src.interval.lo,src.interval.hi):
            raise ValueError("detached/forged source interval")
        if not (cur.lo < src.interval.lo < src.interval.hi < cur.hi):
            raise ValueError("source not inside Farey bracket")
        a,b,c,d=cur.tuple
        lo,hi=run.source_lo,run.source_hi
        ulo,vlo,uhi,vhi=b*lo-a,c-d*lo,b*hi-a,c-d*hi
        if min(ulo,vlo,uhi,vhi)<=0:
            raise ValueError("invalid residual sign")
        if run.arrow=="R":
            low, high=ulo/vlo,uhi/vhi
        elif run.arrow=="L":
            low, high=vhi/uhi,vlo/ulo
        else:
            raise ValueError("invalid arrow")
        if (low,high)!=(run.ratio_lower,run.ratio_upper):
            raise ValueError("forged ratio interval")
        _integer(run.count,"run.count",1)
        if low<run.count or (run.complete_run and high>run.count+1):
            raise ValueError("source does not certify macro arrows")
        cur=cur.run(run.arrow,run.count)
        if run.after!=cur.tuple:
            raise ValueError("forged Farey successor")
        steps+=run.count
        last_stage=src.stage
    if steps!=cert.steps or cert.final!=cur.tuple:
        raise ValueError("total step count or endpoint invalid")
    if steps>max(0,cert.height-1) or cur.denominator_threshold<=cert.height:
        raise ValueError("invalid bounded-height proof")
    if cert.final_source_stage<last_stage:
        raise ValueError("source stage regressed")
    while src.stage<cert.final_source_stage:
        src.refine()
    if (src.interval.lo,src.interval.hi)!=(cert.final_source_lo,cert.final_source_hi):
        raise ValueError("forged final source")
    if not(cur.lo<src.interval.lo<src.interval.hi<cur.hi):
        raise ValueError("final source not inside final bracket")
    delta=min(src.interval.lo-cur.lo,cur.hi-src.interval.hi)
    if delta<=0 or cert.uniform_margin!=delta:
        raise ValueError("invalid separation margin")
    return True



class TranslatedSource:
    """Adversary name: a correct real interval oracle shifted by exact rational."""

    def __init__(self, original, translation: Q):
        if type(translation) is not Q:
            raise ValueError("translation must be an exact Fraction")
        self.original = original
        self.translation = translation
        self.stage = original.stage
        self.interval = RationalInterval(original.interval.lo+translation,
                                          original.interval.hi+translation)

    def refine(self) -> None:
        self.original.refine()
        self.stage = self.original.stage
        self.interval = RationalInterval(
            self.original.interval.lo+self.translation,
            self.original.interval.hi+self.translation)


@dataclass(frozen=True)
class PairwiseSeparation:
    """An actual rational probe that differs for two source-certified cuts."""
    stage: int
    relation: str
    rational_probe: Q
    first: RationalInterval
    second: RationalInterval


def separate_named_reals(first, second, budget: int = 256) -> PairwiseSeparation:
    """Semidecide inequality by disjoint shrinking exact rational intervals.

    If the named reals differ and both correct intervals shrink to points,
    the algorithm halts. At equal values it may return UNKNOWN forever.
    """
    _integer(budget,"budget")
    for depth in range(budget+1):
        a,b=first.interval,second.interval
        if a.hi < b.lo:
            q=(a.hi+b.lo)/2
            return PairwiseSeparation(depth,"FIRST_BELOW_SECOND",q,a,b)
        if b.hi < a.lo:
            q=(b.hi+a.lo)/2
            return PairwiseSeparation(depth,"FIRST_ABOVE_SECOND",q,a,b)
        if depth<budget:
            first.refine();second.refine()
    raise BudgetExhausted("UNKNOWN: interval names not yet separated")


def certificate_summary(cert: ShieldCertificate) -> dict:
    b=FareyBracket(*cert.final)
    return {"source":cert.source_kind,"height":cert.height,
        "steps":cert.steps,"run_counts": [(r.arrow,r.count) for r in cert.runs],
        "denominator_threshold":b.denominator_threshold,
        "lower":str(b.lo),"upper":str(b.hi),
        "source_stage":cert.final_source_stage,
        "uniform_margin":str(cert.uniform_margin)}


if __name__=="__main__":
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("height",type=int)
    parser.add_argument("--source",choices=("circle_beta","bbp_four_pole","sparse_nonnormal"),default="circle_beta")
    args=parser.parse_args()
    c=certify_height(args.height,args.source)
    verify_height_certificate(c)
    print(json.dumps(certificate_summary(c),indent=2))
