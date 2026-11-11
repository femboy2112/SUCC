"""Zero-Anchored Lambda--Haar Compiler: scoped finite research instrument.

A small simply-typed de Bruijn lambda calculus with total, exact BBP source
primitives. Closed well-typed source programs reduce to exact rational states;
all intermediate types are checked. Source zero is an independently recovered
invariant, not a claim that beta reduction proves digit equidistribution.

Haar diagnostics use *certified* completed BBP intervals and interval W1.
The unproved arithmetic gate remains a zero-seed selected signed cancellation
(or an equivalent Haar defect contraction) as documented in the research dossier.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from math import floor, comb, isqrt

from observational_succ import duck_bbp


@dataclass(frozen=True)
class Ty:
    name: str
    domain: "Ty | None" = None
    result: "Ty | None" = None


NAT = Ty("Nat")
RAT = Ty("Rat")
STATE = Ty("BBPState")
INTERVAL = Ty("BBPInterval")


def arrow(domain: Ty, result: Ty) -> Ty:
    return Ty("Arrow", domain, result)


@dataclass(frozen=True)
class State:
    n: int
    u: Q

    def __post_init__(self) -> None:
        if type(self.n) is not int or self.n < 0:
            raise ValueError("state clock must be a natural number")
        if type(self.u) not in (int, Q):
            raise TypeError("state lift must be an exact rational")
        object.__setattr__(self, "u", Q(self.u))


@dataclass(frozen=True)
class RationalInterval:
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if type(self.lo) not in (int, Q) or type(self.hi) not in (int, Q):
            raise TypeError("exact rational interval endpoints required")
        object.__setattr__(self, "lo", Q(self.lo))
        object.__setattr__(self, "hi", Q(self.hi))
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    def shifted(self, x: Q) -> "RationalInterval":
        return RationalInterval(self.lo + Q(x), self.hi + Q(x))


@dataclass(frozen=True)
class Lit:
    ty: Ty
    value: int | Q | State | RationalInterval

    def __post_init__(self) -> None:
        if self.ty == NAT and type(self.value) is int and self.value >= 0:
            return
        if self.ty == RAT and type(self.value) in (int, Q):
            object.__setattr__(self, "value", Q(self.value))
            return
        if self.ty == STATE and type(self.value) is State:
            return
        if self.ty == INTERVAL and type(self.value) is RationalInterval:
            return
        raise TypeError("inconsistent literal type or inexact literal")


@dataclass(frozen=True)
class Var:
    index: int

    def __post_init__(self) -> None:
        if type(self.index) is not int or self.index < 0:
            raise ValueError("de Bruijn indices must be natural numbers")


@dataclass(frozen=True)
class Lam:
    arg_type: Ty
    body: "Term"


@dataclass(frozen=True)
class App:
    fn: "Term"
    arg: "Term"


@dataclass(frozen=True)
class Prim:
    name: str
    args: tuple["Term", ...]


Term = Lit | Var | Lam | App | Prim

# The source is fixed, not passed in as a caller-supplied forcing function.
_PRIMS: dict[str, tuple[tuple[Ty, ...], Ty]] = {
    "step": ((STATE,), STATE),
    "recover": ((STATE,), RAT),
    "prefix": ((NAT,), RAT),
    "from_prefix": ((NAT, RAT), STATE),
    "tail": ((NAT, NAT), INTERVAL),
    "complete": ((STATE, NAT), INTERVAL),
}


def type_of(t: Term, context: tuple[Ty, ...] = ()) -> Ty:
    if isinstance(t, Lit):
        return t.ty
    if isinstance(t, Var):
        if t.index >= len(context):
            raise TypeError("unbound de Bruijn index")
        return context[t.index]
    if isinstance(t, Lam):
        return arrow(t.arg_type, type_of(t.body, (t.arg_type,) + context))
    if isinstance(t, App):
        ftype = type_of(t.fn, context)
        if ftype.name != "Arrow" or ftype.domain != type_of(t.arg, context):
            raise TypeError("application domain mismatch")
        assert ftype.result is not None
        return ftype.result
    if isinstance(t, Prim):
        if t.name not in _PRIMS:
            raise TypeError("unknown source primitive")
        args, result = _PRIMS[t.name]
        if len(t.args) != len(args) or tuple(type_of(a, context) for a in t.args) != args:
            raise TypeError("primitive domain mismatch")
        return result
    raise TypeError("not a lambda compiler term")


def shift(t: Term, amount: int, cutoff: int = 0) -> Term:
    """Usual capture-avoiding de Bruijn shifting, including under binders."""
    if isinstance(t, Var):
        k = t.index + amount if t.index >= cutoff else t.index
        if k < 0:
            raise ValueError("negative de Bruijn index")
        return Var(k)
    if isinstance(t, Lam):
        return Lam(t.arg_type, shift(t.body, amount, cutoff + 1))
    if isinstance(t, App):
        return App(shift(t.fn, amount, cutoff), shift(t.arg, amount, cutoff))
    if isinstance(t, Prim):
        return Prim(t.name, tuple(shift(a, amount, cutoff) for a in t.args))
    return t


def substitute(t: Term, index: int, value: Term, depth: int = 0) -> Term:
    if isinstance(t, Var):
        return shift(value, depth) if t.index == index + depth else t
    if isinstance(t, Lam):
        return Lam(t.arg_type, substitute(t.body, index, value, depth + 1))
    if isinstance(t, App):
        return App(substitute(t.fn, index, value, depth),
                   substitute(t.arg, index, value, depth))
    if isinstance(t, Prim):
        return Prim(t.name, tuple(substitute(a, index, value, depth) for a in t.args))
    return t


def beta(body: Term, arg: Term) -> Term:
    return shift(substitute(body, 0, shift(arg, 1)), -1)


def prefix(n: int) -> Q:
    """Original-source rational P_n; no real/pi oracle."""
    if type(n) is not int or n < 0:
        raise ValueError("prefix horizon must be a natural number")
    return sum((duck_bbp.forcing(j) / 16**j for j in range(1, n + 1)), Q())


def recover(s: State) -> Q:
    return s.u / 16**s.n - prefix(s.n)


def step(s: State) -> State:
    return State(s.n + 1, 16*s.u + duck_bbp.forcing(s.n + 1))


def from_prefix(n: int, seed: Q) -> State:
    return State(n, 16**n * (Q(seed) + prefix(n)))


def authenticate(s: State) -> bool:
    return recover(s) == 0


def guarded_tail(n: int, depth: int) -> RationalInterval:
    """Independent guarded unfolding with the source's analytic tail boundary.

    At depth 0, T_n lies in [0,r(n+1)/15]. Repeated unfoldings of
    X_n=(r(n+1)+X_(n+1))/16 produce nested certified enclosures.
    Their widths shrink geometrically; the unique bounded solution is T.
    """
    if type(n) is not int or n < 0 or type(depth) is not int or depth < 0:
        raise ValueError("natural n and depth required")
    result = RationalInterval(0, duck_bbp.source_tail_budget(n+depth))
    for clock in range(n + depth - 1, n - 1, -1):
        f = duck_bbp.forcing(clock + 1)
        result = RationalInterval((f + result.lo)/16, (f + result.hi)/16)
    return result


def complete(s: State, depth: int) -> RationalInterval:
    return guarded_tail(s.n, depth).shifted(s.u)


def _primitive(name: str, values: tuple[Lit, ...]) -> Lit:
    args = tuple(v.value for v in values)
    if name == "step":
        return Lit(STATE, step(args[0]))
    if name == "recover":
        return Lit(RAT, recover(args[0]))
    if name == "prefix":
        return Lit(RAT, prefix(args[0]))
    if name == "from_prefix":
        return Lit(STATE, from_prefix(args[0], args[1]))
    if name == "tail":
        return Lit(INTERVAL, guarded_tail(args[0], args[1]))
    if name == "complete":
        return Lit(INTERVAL, complete(args[0], args[1]))
    raise ValueError("unknown primitive")


def reduce_once(t: Term) -> tuple[Term, str | None]:
    """Normal-order beta + total primitive reductions, including under lambdas."""
    if isinstance(t, App):
        if isinstance(t.fn, Lam):
            return beta(t.fn.body, t.arg), "beta"
        f, rule = reduce_once(t.fn)
        if rule:
            return App(f, t.arg), rule
        a, rule = reduce_once(t.arg)
        return (App(t.fn, a), rule) if rule else (t, None)
    if isinstance(t, Lam):
        body, rule = reduce_once(t.body)
        return (Lam(t.arg_type, body), rule) if rule else (t, None)
    if isinstance(t, Prim):
        for i, a in enumerate(t.args):
            if not isinstance(a, Lit):
                new, rule = reduce_once(a)
                if rule:
                    args = list(t.args)
                    args[i] = new
                    return Prim(t.name, tuple(args)), rule
                return t, None
        return _primitive(t.name, t.args), "source:" + t.name
    return t, None


def reduce_innermost_once(t: Term) -> tuple[Term, str | None]:
    """Independent eager/rightmost-first strategy for terminating typed terms."""
    if isinstance(t, App):
        arg, rule = reduce_innermost_once(t.arg)
        if rule:
            return App(t.fn,arg),rule
        fn, rule = reduce_innermost_once(t.fn)
        if rule:
            return App(fn,t.arg),rule
        if isinstance(t.fn,Lam):
            return beta(t.fn.body,t.arg),"beta"
        return t,None
    if isinstance(t, Lam):
        body, rule=reduce_innermost_once(t.body)
        return (Lam(t.arg_type,body),rule) if rule else (t,None)
    if isinstance(t, Prim):
        for i in range(len(t.args)-1,-1,-1):
            if not isinstance(t.args[i],Lit):
                arg,rule=reduce_innermost_once(t.args[i])
                if rule:
                    args=list(t.args)
                    args[i]=arg
                    return Prim(t.name,tuple(args)),rule
                return t,None
        return _primitive(t.name,t.args),"source:"+t.name
    return t,None


@dataclass(frozen=True)
class ReductionReceipt:
    value: Term
    result_type: Ty
    rules: tuple[str, ...]


def normalize(t: Term, max_steps: int = 10000,
              strategy: str = "normal") -> ReductionReceipt:
    """Finite evaluator, with two independent reduction orders.

    Both use capture-avoiding de Bruijn substitution and total primitives.
    Exhaustion is UNKNOWN; finite two-strategy agreement is not a universal
    Church-Rosser proof or a theorem about untyped fixed-point combinators.
    """
    if type(max_steps) is not int or max_steps < 0:
        raise ValueError("max_steps must be a natural number")
    if strategy not in ("normal", "innermost"):
        raise ValueError("strategy must be normal or innermost")
    reducer = reduce_once if strategy == "normal" else reduce_innermost_once
    target = type_of(t)
    rules: list[str] = []
    for _ in range(max_steps + 1):
        newer, rule = reducer(t)
        if rule is None:
            return ReductionReceipt(t, target, tuple(rules))
        if len(rules) >= max_steps:
            raise RuntimeError("reduction budget exhausted; no normal-form claim")
        if type_of(newer) != target:
            raise AssertionError("type-preservation contract violated")
        t = newer
        rules.append(rule)
    raise AssertionError("unreachable")


def serial_program(n: int, seed: Q = Q(0)) -> Term:
    """Actual lambda beta-redexes wrapping each canonical BBP step."""
    if type(n) is not int or n < 0:
        raise ValueError("natural source time required")
    expr: Term = Lit(STATE, State(0, Q(seed)))
    fn = Lam(STATE, Prim("step", (Var(0),)))
    for _ in range(n):
        expr = App(fn, expr)
    return expr


def prefix_program(n: int, seed: Q = Q(0)) -> Term:
    return Prim("from_prefix", (Lit(NAT, n), Lit(RAT, Q(seed))))


def anchor_program(n: int, seed: Q = Q(0)) -> Term:
    return App(Lam(STATE, Prim("recover", (Var(0),))), serial_program(n, seed))


def completion_program(n: int, seed: Q = Q(0), depth: int = 16) -> Term:
    """Beta-compiled completed-state interval, no infinite Y reduction."""
    return App(Lam(STATE, Prim("complete", (Var(0), Lit(NAT, depth)))),
               serial_program(n, seed))


@dataclass(frozen=True)
class PhaseCertificate:
    n: int
    lo: Q
    hi: Q
    digit: int
    midpoint: Q
    depth_used: int

    @property
    def width(self) -> Q:
        return self.hi - self.lo


def certified_phase(s: State, depth: int = 16, max_depth: int = 256) -> PhaseCertificate:
    """Certified phase in a radix cylinder, adaptively bounded by max_depth.

    Exact rational wrong-seed shadows can lie exponentially close to a
    boundary; fixed depth must not be misreported as a digit certificate.
    """
    if type(depth) is not int or depth < 0 or type(max_depth) is not int or max_depth < depth:
        raise ValueError("require 0 <= depth <= max_depth")
    current = depth
    while True:
        enclosure = complete(s, current)
        lo, hi = enclosure.lo, enclosure.hi
        if floor(16*lo) == floor(16*hi):
            return PhaseCertificate(s.n, lo, hi, floor(16*lo) % 16,
                                    ((lo + hi) / 2) % 1, current)
        if current == max_depth:
            raise ValueError("unresolved digit boundary within precision budget")
        current = min(max_depth, max(current + 1, 2*current))


def certified_digits(n: int, seed: Q = Q(0), depth: int = 16) -> tuple[int, ...]:
    state = State(0, Q(seed))
    digits = []
    for _ in range(n):
        digits.append(certified_phase(state, depth).digit)
        state = step(state)
    return tuple(digits)


def interval_w1(positive: tuple[tuple[Q, Q], ...],
                negative: tuple[tuple[Q, Q], ...]) -> Q:
    """Exact W1 on [0,1] using cumulative differences of atomic measures."""
    masses: dict[Q, Q] = defaultdict(Q)
    for point, mass in positive:
        if not 0 <= point <= 1 or mass < 0:
            raise ValueError("invalid positive probability atom")
        masses[point] += mass
    for point, mass in negative:
        if not 0 <= point <= 1 or mass < 0:
            raise ValueError("invalid negative probability atom")
        masses[point] -= mass
    if sum((w for _, w in positive), Q()) != 1 or \
       sum((w for _, w in negative), Q()) != 1:
        raise ValueError("both measures must have mass exactly one")
    cumulative = Q()
    previous = Q()
    distance = Q()
    for point in sorted(masses):
        distance += abs(cumulative) * (point - previous)
        cumulative += masses[point]
        previous = point
    if cumulative != 0:
        raise AssertionError("mass conservation failure")
    return distance


def exact_haar_defect(points: tuple[Q, ...]) -> Q:
    """W1(empirical real phases, conditional first-digit Haar projector)."""
    if not points or any(type(x) not in (Q, int) or not 0 <= x < 1 for x in points):
        raise ValueError("nonempty exact phases in [0,1) required")
    count = len(points)
    actual = tuple((Q(x), Q(1, count)) for x in points)
    virtual = []
    for x in points:
        y = (16*x) % 1
        virtual.extend(((Q(a) + y) / 16, Q(1, 16*count)) for a in range(16))
    return interval_w1(actual, tuple(virtual))


@dataclass(frozen=True)
class DefectCertificate:
    count: int
    midpoint_defect: Q
    error: Q
    lower: Q
    upper: Q


def _certified_series(count: int, seed: Q, depth: int) -> tuple[PhaseCertificate, ...]:
    if type(count) is not int or count < 1:
        raise ValueError("count must be a positive integer")
    state = State(0, Q(seed))
    certs = []
    for _ in range(count):
        certs.append(certified_phase(state,depth))
        state = step(state)
    return tuple(certs)


def certified_haar_defect(count: int, seed: Q = Q(0), depth: int = 16) -> DefectCertificate:
    """Rigorous interval W1 enclosure for exact BBP-selected *completed* phases.

    Each real phase and rational midpoint share their 1/16 cylinder; their
    Q-projections can be coupled using the same branch digit. The two W1
    perturbations cost at most sum(width_i)/N in total.
    """
    certs = _certified_series(count, seed, depth)
    mid = exact_haar_defect(tuple(c.midpoint for c in certs))
    err = sum((c.width for c in certs), Q()) / count
    return DefectCertificate(count, mid, err, max(Q(0), mid - err), mid + err)


def cyclic_defect(digits: tuple[int, ...], depth: int = 0) -> Q:
    """Exact future-conditioned sixteen-child L1 defect delta_depth.

    Cyclic words deliberately use wraparound; unlike an actual orbit law,
    these are periodic finite-string diagnostics, not asymptotic evidence.
    """
    if not digits or type(depth) is not int or depth < 0:
        raise ValueError("nonempty digits and nonnegative depth required")
    if any(type(x) is not int or not 0 <= x < 16 for x in digits):
        raise ValueError("hexadecimal digits required")
    N = len(digits)
    contexts = Counter(tuple(digits[(i+j+1) % N] for j in range(depth)) for i in range(N))
    pairs = Counter((digits[i], tuple(digits[(i+j+1) % N] for j in range(depth)))
                    for i in range(N))
    return sum((abs(Q(pairs[a, w], N) - Q(contexts[w], 16*N))
                for w in contexts for a in range(16)), Q())


def cyclic_energy(digits: tuple[int, ...], width: int) -> Q:
    """Exact E_k=16^k sum p_k(w)^2-1 for cyclic k-word counts."""
    if not digits or type(width) is not int or width < 0:
        raise ValueError("nonempty digits and nonnegative width required")
    if any(type(x) is not int or not 0 <= x < 16 for x in digits):
        raise ValueError("hexadecimal digits required")
    if width == 0:
        return Q(0)
    N = len(digits)
    counts = Counter(tuple(digits[(i+j) % N] for j in range(width)) for i in range(N))
    return 16**width * sum((Q(v, N)**2 for v in counts.values()), Q()) - 1


def parity_pin(digits: tuple[int, ...]) -> Q:
    if not digits or any(type(a) is not int or not 0 <= a < 16 for a in digits):
        raise ValueError("nonempty hexadecimal word required")
    return Q(sum(1 if a % 2 == 0 else -1 for a in digits), len(digits))


def formal_character_pin(digits: tuple[int, ...], h: int, future: tuple[int, ...] = ()) -> tuple[Q, ...]:
    """Exactly evaluate conditional sum of zeta_16^(h*d) in Q[zeta_16].

    Uses basis 1,zeta,...,zeta^7 and zeta^8=-1; no floating DFT.
    ``future`` selects the immediately following cyclic digits.
    """
    if type(h) is not int or not 1 <= h <= 15 or not digits:
        raise ValueError("character h in 1..15 and nonempty digits required")
    if any(type(a) is not int or not 0 <= a < 16 for a in digits + future):
        raise ValueError("hexadecimal digits required")
    N = len(digits)
    coefficients = [0] * 8
    for i, a in enumerate(digits):
        if all(digits[(i+j+1) % N] == x for j, x in enumerate(future)):
            power = (h*a) % 16
            coefficients[power % 8] += 1 if power < 8 else -1
    return tuple(Q(x, N) for x in coefficients)


def contraction_excess(current: DefectCertificate, earlier: DefectCertificate,
                       theta: Q) -> tuple[Q, Q]:
    """Certified interval for D_N - theta D_M, NOT a proof of o(1)."""
    if type(theta) not in (int, Q) or not Q(0) <= theta < 1:
        raise ValueError("contraction constant must belong to [0,1)")
    return current.lower - Q(theta)*earlier.upper, current.upper - Q(theta)*earlier.lower


@dataclass(frozen=True)
class PascalPinCertificate:
    """A rigorous cyclotomic-coefficient approximation, not a sign claim."""
    count: int
    h: int
    m: int
    j: int
    coefficients: tuple[Q, ...]  # Q[zeta_16], degree < 8
    complex_error_bound: Q


def _pin_from_series(certs: tuple[PhaseCertificate, ...], m: int, j: int,
                     h: int) -> PascalPinCertificate:
    if type(m) is not int or m < 0 or type(j) is not int or not 0 <= j <= m or \
       type(h) is not int or not 1 <= h <= 15:
        raise ValueError("0<=j<=m, 1<=h<=15 required")
    count=len(certs)
    coeff = [Q(0)] * 8
    widths = Q(0)
    for c in certs:
        y = (16*c.midpoint) % 1
        weight = Q(comb(m,j),count) * y**j * (1-y)**(m-j)
        power = (h*c.digit) % 16
        coeff[power % 8] += weight if power < 8 else -weight
        widths += c.width
    return PascalPinCertificate(count,h,m,j,tuple(coeff),Q(8*m,count)*widths)


def pascal_fourier_pin(count: int, m: int, j: int, h: int,
                       seed: Q = Q(0), depth: int = 16) -> PascalPinCertificate:
    """Certified G_(h;m,j) for real BBP orbit via rational midpoint Bernstein.

    In each certified first-digit cell, y=T(x) is 16-Lipschitz.
    |B'_(m,j)|<=m on [0,1]. Midpoint error <= width/2, hence
    complex error <=8*m*average(width). Coefficients are exact in Q[zeta16].
    A small finite error is not evidence of asymptotic cancellation.
    """
    return _pin_from_series(_certified_series(count,seed,depth),m,j,h)


def pascal_haar_upper(count: int, m: int, seed: Q = Q(0),
                      depth: int = 16) -> Q:
    """Rigorous, generally loose *rational* upper bound on D_N.

    For each 1-Lipschitz f on [0,1], approximate its 16 inverse-branch
    functions by Bernstein degree m: error <=1/(32 sqrt(m)) per branch.
    D_N <= sum_(h=1..15,j=0..m) |G_(h;m,j)|+1/(16 sqrt(m)).
    Each exact Q[zeta16] midpoint has abs <= coefficient l1, and each
    actual pin differs by <= its certified complex error. isqrt(m) gives
    a conservative rational replacement for sqrt(m).
    """
    if type(m) is not int or m < 1:
        raise ValueError("positive Bernstein degree required")
    result = Q(1,16*isqrt(m))
    certs = _certified_series(count,seed,depth)
    for h in range(1,16):
        for j in range(m+1):
            cert = _pin_from_series(certs,m,j,h)
            result += sum((abs(v) for v in cert.coefficients),Q())
            result += cert.complex_error_bound
    return result
