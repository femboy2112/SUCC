"""Research-local source-certified digit and finite-state entropy instruments.

Theorems live in THEOREMS.md.  Finite tests are not evidence of pi normality.
No dependencies outside the Python standard library.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import log
from typing import Callable, Iterable, Sequence


def four_pole(n: int) -> Fraction:
    """Authentic signed BBP source; n >= 1."""
    if type(n) is not int or n < 1:
        raise ValueError("n >= 1 required")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def original_states(length: int, seed: Fraction = Fraction(0)) -> tuple[Fraction, ...]:
    """Exact rational x_n={U_n(seed)} for n=0,...,length-1."""
    if type(length) is not int or length < 0:
        raise ValueError("nonnegative integer length required")
    x = Fraction(seed) % 1
    out = []
    for n in range(length):
        out.append(x)
        x = (16*x + four_pole(n+1)) % 1
    return tuple(out)


def tail_enclosure(n: int, depth: int) -> tuple[Fraction, Fraction]:
    """Rigorous T_n enclosure from authentic r(n).

    n>=0; depth>=1 ensures n+depth>=1 and remainder is bounded
    by 16^-depth / (15*(n+depth+1)^2).  This invokes the n>=2
    rational inequality r(n)<1/n^2 for remaining source terms.
    """
    if type(n) is not int or n < 0 or type(depth) is not int or depth < 1:
        raise ValueError("n>=0 and depth>=1 integers required")
    acc = Fraction(0)
    for j in range(depth, 0, -1):
        acc = (acc + four_pole(n+j))/16
    err = Fraction(1, 16**depth * 15 * (n+depth+1)**2)
    return acc, acc + err


def certified_completed_digit(x_n: Fraction, n: int, *,
                              initial_depth: int = 8, max_depth: int = 80) -> tuple[int, int]:
    """Certified floor(16*{U_n+T_n}) from a rational T_n enclosure.

    No precomputed pi digits or floating-point normality assumptions.
    Returns (digit, number of source terms used).  An unresolved cell
    explicitly fails; it is never rounded by a floating approximation.
    """
    if initial_depth < 1 or max_depth < initial_depth:
        raise ValueError("1<=initial_depth<=max_depth required")
    for depth in range(initial_depth, max_depth+1, 4):
        lo, hi = tail_enclosure(n, depth)
        qlo = (16*(x_n+lo)).numerator // (16*(x_n+lo)).denominator
        qhi = (16*(x_n+hi)).numerator // (16*(x_n+hi)).denominator
        if qlo == qhi:
            return qlo % 16, depth
    raise ArithmeticError("source interval crosses a digit boundary at declared max_depth")


def certified_source_digits(length: int, *, depth: int = 12) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """First hexadecimal digits of the original completed zero-seed BBP history."""
    states = original_states(length)
    pairs = [certified_completed_digit(x, n, initial_depth=depth)
             for n, x in enumerate(states)]
    return tuple(p[0] for p in pairs), tuple(p[1] for p in pairs)


def pole_clock(n: int, modulus: int = 7) -> int:
    """Finite original first-pole denominator clock (8*(n+1)-7) modulo modulus."""
    if type(n) is not int or n < 0 or type(modulus) is not int or modulus < 2:
        raise ValueError("n>=0 and modulus>=2 integers required")
    return (8*(n+1)-7) % modulus


def mealy_run(digits: Sequence[int], source: Sequence[int], *,
              base: int = 16, start: int = 0,
              emit: Callable[[int,int,int,int],int] | None = None,
              transition: Callable[[int,int,int,int],int] | None = None,
              states: int = 16) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Causal one-digit input/output Mealy observer; source is an explicit tape.

    State sequence includes q_0,...,q_N; caller declares state-cardinality.
    """
    if len(digits)!=len(source) or base < 2 or states < 1 or not 0<=start<states:
        raise ValueError("tape length, base, state parameter invalid")
    if emit is None:
        emit = lambda q,d,s,b: (d+s+q) % b
    if transition is None:
        transition = lambda q,d,s,b: (q+3*d+2*s) % states
    q = start
    y, qhistory = [], [q]
    for d,s in zip(digits,source):
        if not 0 <= d < base:
            raise ValueError("digit outside alphabet")
        z = emit(q,d,s,base)
        nq = transition(q,d,s,base)
        if type(z) is not int or not 0<=z<base or type(nq) is not int or not 0<=nq<states:
            raise ValueError("observer output or state outside declared finite set")
        y.append(z)
        q = nq
        qhistory.append(q)
    return tuple(y),tuple(qhistory)


def decode_reversible_observer(output: Sequence[int], source: Sequence[int], *,
                               start: int = 0) -> tuple[int, ...]:
    """Inverse of the concrete 16-state source-driven Mealy observer.

    Forward: y = d+sigma+q (mod16), q_next = q+3*d+2*sigma (mod16).
    Inverse: d = y-sigma-q (mod16), q_next = -2*q+3*y-sigma (mod16).
    The source tape and initial state are logged; neither is inferred.
    """
    if len(output) != len(source) or not 0<=start<16:
        raise ValueError("matching output/source tapes and 0<=start<16 required")
    q = start
    input_digits=[]
    for y,s in zip(output,source):
        if type(y) is not int or not 0<=y<16:
            raise ValueError("invalid output digit")
        d = (y-s-q)%16
        q = (-2*q+3*y-s)%16
        input_digits.append(d)
    return tuple(input_digits)


def block_distribution(seq: Sequence[int], length: int) -> dict[tuple[int,...],Fraction]:
    """Exact overlapping finite empirical L-block distribution."""
    if type(length) is not int or length < 1 or length > len(seq):
        raise ValueError("1 <= length <= len(seq) required")
    n = len(seq)-length+1
    counts = Counter(tuple(seq[i:i+length]) for i in range(n))
    return {k: Fraction(c,n) for k,c in counts.items()}


def entropy_of(probs: Iterable[Fraction]) -> float:
    """Shannon entropy in nats; only numerical diagnostics use this."""
    return -sum(float(p)*log(float(p)) for p in probs if p>0)


def block_entropy(seq: Sequence[int], length: int) -> float:
    return entropy_of(block_distribution(seq,length).values())


def h_binary(eps: float) -> float:
    if not 0<=eps<=1:
        raise ValueError("eps in [0,1] required")
    return 0. if eps in (0.,1.) else -eps*log(eps)-(1-eps)*log(1-eps)


def entropy_budget(digits: Sequence[int], source: Sequence[int], output: Sequence[int],
                   states: int, base: int, k: int, L: int) -> dict[str,float]:
    """Finite entropy debt theorem, exactly scoped to a path of N symbols.

    Requires L=m*k, 1<=k<=L<=N.  No assumptions on source stream.
    The inequality is derived in THEOREMS.md and holds for ANY Mealy policy.
    """
    N=len(digits)
    if (N!=len(source) or N!=len(output) or not (1<=k<=L<=N) or L%k or
            states<1 or base<2 or any(not 0<=d<base for d in digits) or
            any(not 0<=y<base for y in output)):
        raise ValueError("invalid entropy-budget arguments")
    hx = block_entropy(digits,k)
    hy = block_entropy(output,L)
    hs = block_entropy(source,L)
    eps = (L-k)/(N-k+1)
    f = h_binary(eps)+eps*k*log(base)
    dx = k*log(base)-hx
    dy = L*log(base)-hy
    bound = (k/L)*(dy+hs+log(states))+f
    return {"input_deficit":dx,"upper_bound":bound,"output_deficit":dy,
            "source_block_entropy":hs,"tv_budget":eps,"continuity_budget":f,
            "slack":bound-dx}


def rotations_for_rational_seed(seed: Fraction, length: int) -> tuple[Fraction,...]:
    """Exact 16^n seed rotation: ultimately periodic for every rational seed."""
    s = Fraction(seed)%1
    out=[]
    for _ in range(length):
        out.append(s)
        s=(16*s)%1
    return tuple(out)


def circle_joint_character(raw: Sequence[Fraction], actions: Sequence[Fraction], h: int) -> complex:
    """Finite numerical joint Weyl check; exact decoded rational phases."""
    from cmath import exp
    from math import pi
    if not raw or len(raw)!=len(actions) or type(h) is not int:
        raise ValueError("length mismatch, empty data or bad h")
    logged=[((x+a)%1,a) for x,a in zip(raw,actions)]
    return sum(exp(2j*pi*h*float((y-a)%1)) for y,a in logged)/len(raw)
