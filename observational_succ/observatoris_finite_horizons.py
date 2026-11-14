"""Exact finite-horizon completeness / impossibility laboratory (OPUS III).

Companion to research/2026-11-14/principia_observatoris_second_forge/agents/
OPUS_III_HORIZON_HUNTER.md (theorems FH-1 ... FH-14).  Everything here is
exact (``fractions.Fraction`` or prime-field integers); floats are refused.

What the code CAN do: decide exact finite statements about declared model
classes (linear recurrences, LTI Markov sequences, finite-state machines,
weighted / probabilistic automata, modulus classes, the founding pair
a(n)=1/(n+1), b_H) and run exhaustive small-model searches that could have
falsified each horizon bound.  What it can NOT do: certify that any physical
source, arithmetic object, RH quantity or pi digit stream belongs to a
declared class.  A finite search is evidence about the declared finite
models only; the general statements are proved (or cited) in the report.

Classical sources are attributed in the report (Kronecker, Cayley-Hamilton,
Ho-Kalman, Moore 1956, Fine-Wilf 1965, Schutzenberger 1961, Carlyle-Paz,
Paz 1971, Tzeng 1992, Berlekamp-Massey, Gold 1967, Kelly 1996, Cauchy).
Related project machinery: carrier_hankel_bounds (Hankel minors, delayed
impulse), nerode_probe_growth (delayed signal chain), future_safe_quotient
(Moore minimisation), CARRIER_RELATIVE_TARGETS sections 4-5 (oscillation,
error radius omega/2, prefix-topology discontinuity).
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product
from math import comb, factorial, gcd
from typing import Callable, Iterable, Sequence


class HorizonError(ValueError):
    """Malformed or non-exact input, or a declared budget exceeded."""


# ---------------------------------------------------------------- fields

def _q(x: object) -> Fraction:
    if type(x) is bool or type(x) not in (int, Fraction):
        raise HorizonError("exact int/Fraction required (no floats, no bools)")
    return Fraction(x)


class RationalField:
    """The field Q with exact Fraction arithmetic."""
    name = "Q"
    characteristic = 0
    zero = Fraction(0)
    one = Fraction(1)

    def coerce(self, x: object) -> Fraction:
        return _q(x)

    def inv(self, a: Fraction) -> Fraction:
        if a == 0:
            raise ZeroDivisionError("inverse of zero")
        return 1 / a

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


class PrimeField:
    """GF(p), p a (small) prime; elements are ints in 0..p-1."""

    def __init__(self, p: int):
        if type(p) is not int or p < 2 or p > 10007 or any(p % d == 0 for d in range(2, int(p ** 0.5) + 1)):
            raise HorizonError("small prime modulus required")
        self.p = p
        self.name = f"GF({p})"
        self.characteristic = p
        self.zero = 0
        self.one = 1

    def coerce(self, x: object) -> int:
        if type(x) is Fraction:
            if x.denominator % self.p == 0:
                raise HorizonError("denominator not invertible mod p")
            return x.numerator * pow(x.denominator, self.p - 2, self.p) % self.p
        if type(x) is not int:
            raise HorizonError("exact integers required in a prime field")
        return x % self.p

    def inv(self, a: int) -> int:
        if a % self.p == 0:
            raise ZeroDivisionError("inverse of zero")
        return pow(a, self.p - 2, self.p)

    def add(self, a, b):
        return (a + b) % self.p

    def sub(self, a, b):
        return (a - b) % self.p

    def mul(self, a, b):
        return a * b % self.p


QQ = RationalField()


def GF(p: int) -> PrimeField:
    return PrimeField(p)


def _vec(xs: Iterable, field) -> tuple:
    return tuple(field.coerce(x) for x in xs)


# ------------------------------------------------- linear recurrences (FH-3)

def generate(coeffs: Sequence, init: Sequence, length: int, field=QQ) -> tuple:
    """s[k+L] = sum_j coeffs[j] s[k+j]  (monic order L = len(coeffs))."""
    c = _vec(coeffs, field)
    s = list(_vec(init, field))
    if len(c) != len(s) or type(length) is not int or length < 0:
        raise HorizonError("order mismatch or bad length")
    L = len(c)
    while len(s) < length:
        k = len(s) - L
        if L == 0:
            s.append(field.zero)
            continue
        acc = field.zero
        for j in range(L):
            acc = field.add(acc, field.mul(c[j], s[k + j]))
        s.append(acc)
    return tuple(s[:length])


def char_poly(coeffs: Sequence, field=QQ) -> tuple:
    """Monic characteristic polynomial, low->high: x^L - sum c_j x^j."""
    c = _vec(coeffs, field)
    return tuple(field.sub(field.zero, x) for x in c) + (field.one,)


def berlekamp_massey(seq: Sequence, field=QQ) -> tuple[int, tuple]:
    """Exact Berlekamp-Massey (Massey 1969).

    Returns (L, coeffs) with seq[k+L] = sum_j coeffs[j] seq[k+j] for every
    k with k+L < len(seq); L is the linear complexity of the FINITE prefix.
    """
    s = _vec(seq, field)
    C = [field.one]
    B = [field.one]
    L, m, b = 0, 1, field.one
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            if i < len(C):
                d = field.add(d, field.mul(C[i], s[n - i]))
        if d == field.zero:
            m += 1
            continue
        coef = field.mul(d, field.inv(b))
        T = C[:]
        need = len(B) + m
        if len(C) < need:
            C = C + [field.zero] * (need - len(C))
        for i, bi in enumerate(B):
            C[i + m] = field.sub(C[i + m], field.mul(coef, bi))
        if 2 * L <= n:
            L, B, b, m = n + 1 - L, T, d, 1
        else:
            m += 1
    C = C + [field.zero] * max(0, L + 1 - len(C))
    coeffs = tuple(field.sub(field.zero, C[L - j]) for j in range(L))
    return L, coeffs


def _rank(rows: Sequence[Sequence], field=QQ) -> int:
    A = [list(r) for r in rows]
    if not A:
        return 0
    ncol = len(A[0])
    r = 0
    for j in range(ncol):
        piv = next((i for i in range(r, len(A)) if A[i][j] != field.zero), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = field.inv(A[r][j])
        A[r] = [field.mul(x, inv) for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j] != field.zero:
                f = A[i][j]
                A[i] = [field.sub(x, field.mul(f, y)) for x, y in zip(A[i], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def det(rows: Sequence[Sequence], field=QQ):
    A = [list(_vec(r, field)) for r in rows]
    n = len(A)
    if any(len(r) != n for r in A):
        raise HorizonError("square matrix required")
    out = field.one
    for j in range(n):
        piv = next((i for i in range(j, n) if A[i][j] != field.zero), None)
        if piv is None:
            return field.zero
        if piv != j:
            A[j], A[piv] = A[piv], A[j]
            out = field.sub(field.zero, out)
        out = field.mul(out, A[j][j])
        inv = field.inv(A[j][j])
        for i in range(j + 1, n):
            if A[i][j] != field.zero:
                f = field.mul(A[i][j], inv)
                A[i] = [field.sub(x, field.mul(f, y)) for x, y in zip(A[i], A[j])]
    return out


def hankel(seq: Sequence, rows: int, cols: int, field=QQ) -> tuple:
    s = _vec(seq, field)
    if rows < 0 or cols < 0 or len(s) < rows + cols - 1:
        raise HorizonError("not enough samples for this Hankel block")
    return tuple(tuple(s[i + j] for j in range(cols)) for i in range(rows))


def hankel_rank(seq: Sequence, size: int, field=QQ) -> int:
    return _rank(hankel(seq, size, size, field), field)


def linear_complexity_bruteforce(seq: Sequence, field=QQ) -> int:
    """Smallest r admitting a monic order-r recurrence on the finite prefix.

    Independent of Berlekamp-Massey: solvability test rank[A]=rank[A|b].
    """
    s = _vec(seq, field)
    t = len(s)
    for r in range(t + 1):
        eqs = [list(s[k:k + r]) for k in range(t - r)]
        rhs = [s[k + r] for k in range(t - r)]
        if not eqs:
            return r
        if r == 0:
            if all(v == field.zero for v in rhs):
                return 0
            continue
        if _rank(eqs, field) == _rank([e + [b] for e, b in zip(eqs, rhs)], field):
            return r
    return t


def annihilates(poly: Sequence, seq: Sequence, field=QQ) -> bool:
    """poly (low->high) applied to the shift kills every complete window."""
    p = _vec(poly, field)
    s = _vec(seq, field)
    D = len(p) - 1
    for k in range(len(s) - D):
        acc = field.zero
        for i, pi in enumerate(p):
            acc = field.add(acc, field.mul(pi, s[k + i]))
        if acc != field.zero:
            return False
    return True


# polynomials over a field, coefficient tuples low->high, trimmed

def _trim(p: list, field) -> list:
    while p and p[-1] == field.zero:
        p.pop()
    return p


def poly_mul(p: Sequence, q: Sequence, field=QQ) -> tuple:
    out = [field.zero] * (len(p) + len(q) - 1) if p and q else []
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = field.add(out[i + j], field.mul(a, b))
    return tuple(_trim(out, field))


def _poly_divmod(p: Sequence, q: Sequence, field) -> tuple[list, list]:
    p = _trim(list(p), field)
    q = _trim(list(q), field)
    if not q:
        raise ZeroDivisionError("division by zero polynomial")
    quo = [field.zero] * max(0, len(p) - len(q) + 1)
    inv = field.inv(q[-1])
    while len(p) >= len(q) and p:
        f = field.mul(p[-1], inv)
        sh = len(p) - len(q)
        quo[sh] = f
        for i, qi in enumerate(q):
            p[i + sh] = field.sub(p[i + sh], field.mul(f, qi))
        p = _trim(p, field)
    return quo, p


def poly_gcd(p: Sequence, q: Sequence, field=QQ) -> tuple:
    a, b = _trim(list(p), field), _trim(list(q), field)
    while b:
        _, r = _poly_divmod(a, b, field)
        a, b = b, r
    if not a:
        return ()
    inv = field.inv(a[-1])
    return tuple(field.mul(x, inv) for x in a)


def poly_lcm_degree(p: Sequence, q: Sequence, field=QQ) -> int:
    dp = len(_trim(list(p), field)) - 1
    dq = len(_trim(list(q), field)) - 1
    return dp + dq - (len(poly_gcd(p, q, field)) - 1)


def monic_polys(degree: int, field: PrimeField, *, invertible: bool = False) -> list[tuple]:
    out = []
    for low in product(range(field.p), repeat=degree):
        if invertible and degree > 0 and low[0] == 0:
            continue
        out.append(tuple(low) + (1,))
    return out


def recurrence_class_gf(field: PrimeField, order: int, length: int, *,
                        invertible: bool = False) -> set[tuple]:
    """All prefixes of sequences annihilated by a monic poly of degree <= order.

    invertible=True demands nonzero constant term (no nilpotent part); then
    every degree 0..order is enumerated (padding by x is not allowed).
    """
    out = set()
    degrees = range(order + 1) if invertible else [order]
    for D in degrees:
        for poly in monic_polys(D, field, invertible=invertible):
            coeffs = tuple((-c) % field.p for c in poly[:-1])
            for init in product(range(field.p), repeat=D):
                out.add(generate(coeffs, init, length, field))
    return out


def lcp(x: Sequence, y: Sequence) -> int:
    k = 0
    for u, v in zip(x, y):
        if u != v:
            break
        k += 1
    return k


def max_agreement_of_distinct(S: Iterable[tuple], T: Iterable[tuple]) -> int:
    """Largest common-prefix length over pairs of DISTINCT finite tuples.

    Uses the lexicographic fact that, for fixed x, lcp(x, y) over a sorted
    list is maximised at x's nearest neighbours; cross-checked against
    ``max_agreement_bruteforce`` in the tests.
    """
    from bisect import bisect_left
    Ts = sorted(set(T))
    best = -1
    for x in set(S):
        i = bisect_left(Ts, x)
        for j in (i - 1, i, i + 1):
            if 0 <= j < len(Ts) and Ts[j] != x:
                best = max(best, lcp(x, Ts[j]))
    return best


def max_agreement_bruteforce(S: Iterable[tuple], T: Iterable[tuple]) -> int:
    S, T = list(set(S)), list(set(T))
    return max((lcp(x, y) for x in S for y in T if x != y), default=-1)


def gen_binom(x: int, r: int) -> int:
    """Generalised binomial C(x, r) = x(x-1)...(x-r+1)/r! for any int x."""
    if r < 0:
        raise HorizonError("r >= 0 required")
    num = 1
    for i in range(r):
        num *= x - i
    return num // factorial(r)


def extremal_linear_pair(n: int, m: int, length: int, field=QQ) -> dict:
    """FH-3 sharpness pair: orders <= n and <= m agreeing on n+m-1 terms.

    a is annihilated by x^n (support in [0,n-1]); b(k)=C(k-n,m-1) by (x-1)^m.
    Integer-valued, hence valid over EVERY field (coprime: 0 != 1).
    m=0: a(k)=C(k,n-1), b=0.  (n,m)=(0,0): no pair exists (horizon 0).
    """
    if type(n) is not int or type(m) is not int or n < 0 or m < 0:
        raise HorizonError("orders must be nonnegative ints")
    if n == m == 0:
        raise HorizonError("(0,0): both sequences are zero; no extremal pair")
    if m >= 1:
        b = [gen_binom(k - n, m - 1) for k in range(length)]
        a = [b[k] if k < n else 0 for k in range(length)]
        pa = (0,) * n + (1,)
        pb = tuple(comb(m, i) * (-1) ** (m - i) for i in range(m + 1))
    else:
        a = [gen_binom(k, n - 1) if k >= 0 else 0 for k in range(length)]
        b = [0] * length
        pa = tuple(comb(n, i) * (-1) ** (n - i) for i in range(n + 1))
        pb = (1,)
    return {"a": _vec(a, field), "b": _vec(b, field),
            "poly_a": _vec(pa, field), "poly_b": _vec(pb, field),
            "agree_terms": n + m - 1, "first_difference_index": n + m - 1}


# ------------------------------------------- founding pair inside LR (FH-6)

def harmonic(length: int) -> tuple:
    return tuple(Fraction(1, k + 1) for k in range(length))


def founding_b(H: int, length: int) -> tuple:
    return tuple(Fraction(1, k + 1) if k <= H else Fraction(1) for k in range(length))


def founding_b_order(H: int) -> int:
    """Exact minimal recurrence order of b_H (proved in FH-6)."""
    if type(H) is not int or H < 0:
        raise HorizonError("H >= 0")
    return 1 if H == 0 else H + 2


def hilbert_det_closed_form(N: int) -> Fraction:
    """Cauchy: det[1/(i+j+1)]_{i,j<N} = c_N^4 / c_{2N}, c_N = prod_{k<N} k!."""
    def c(M):
        out = 1
        for k in range(M):
            out *= factorial(k)
        return out
    return Fraction(c(N) ** 4, c(2 * N))


def harmonic_mimic(n: int, length: int) -> tuple:
    """Unique order-n recurrence sequence agreeing with 1/(k+1) on 0..2n-1."""
    a = harmonic(max(length, 2 * n))
    if n == 0:
        return tuple(Fraction(0) for _ in range(length))
    M = [list(a[i:i + n]) for i in range(n)]
    rhs = [a[i + n] for i in range(n)]
    # Gauss-Jordan on the (invertible, Hilbert) system M c = rhs
    for j in range(n):
        p = next(i for i in range(j, n) if M[i][j] != 0)
        M[j], M[p] = M[p], M[j]
        rhs[j], rhs[p] = rhs[p], rhs[j]
        inv = 1 / M[j][j]
        M[j] = [x * inv for x in M[j]]
        rhs[j] *= inv
        for i in range(n):
            if i != j and M[i][j] != 0:
                f = M[i][j]
                M[i] = [x - f * y for x, y in zip(M[i], M[j])]
                rhs[i] -= f * rhs[j]
    return generate(rhs, a[:n], length)


def harmonic_mimic_deviation(n: int) -> Fraction:
    """a(2n) - x_n(2n) = det H_{n+1}/det H_n = (n!)^4 / ((2n)! (2n+1)!)."""
    return Fraction(factorial(n) ** 4, factorial(2 * n) * factorial(2 * n + 1))


# ------------------------------------------------ learner / certifier (FH-5)

def conservative_learner_trace(prefix: Sequence, field=QQ) -> list[tuple]:
    """Conjecture after reading t terms, t=0..len(prefix).

    Keeps its (minimal-order) conjecture while consistent; otherwise jumps
    to the Berlekamp-Massey minimal recurrence with the observed initial
    values.  A conjecture is (coeffs, init): it names an infinite sequence.
    """
    s = _vec(prefix, field)
    hyp = ((), ())
    trace = [hyp]
    for t in range(1, len(s) + 1):
        coeffs, init = hyp
        if generate(coeffs, init, t, field) != s[:t]:
            L, c = berlekamp_massey(s[:t], field)
            hyp = (c, s[:L])
        trace.append(hyp)
    return trace


def mind_changes(trace: list) -> list[int]:
    return [t for t in range(1, len(trace)) if trace[t] != trace[t - 1]]


def impulse(N: int, length: int, field=QQ) -> tuple:
    return tuple(field.one if k == N else field.zero for k in range(length))


def certifier_counterexample(x: Sequence, t: int, field=QQ) -> tuple:
    """x + delta_t: still linearly recurrent (order <= ord(x)+t+1), same
    t-prefix as x, different at index t.  Refutes any certifier halting at t."""
    s = _vec(x, field)
    if type(t) is not int or not 0 <= t < len(s):
        raise HorizonError("0 <= t < len(x)")
    return tuple(field.add(v, field.one) if k == t else v for k, v in enumerate(s))


# --------------------------------------------- finite-state machines (FH-7)

def machine_rho(delta: Sequence[int], out: Sequence, start: int = 0) -> tuple[tuple, tuple]:
    """Output sequence of an autonomous machine as (preperiod, cycle)."""
    seen = {}
    q, k, outs = start, 0, []
    while q not in seen:
        seen[q] = k
        outs.append(out[q])
        q = delta[q]
        k += 1
    t = seen[q]
    return canonical_rho(tuple(outs[:t]), tuple(outs[t:]))


def canonical_rho(pre: tuple, cyc: tuple) -> tuple[tuple, tuple]:
    if not cyc:
        raise HorizonError("nonempty cycle required")
    p = len(cyc)
    for d in range(1, p + 1):
        if p % d == 0 and cyc == cyc[:d] * (p // d):
            cyc = cyc[:d]
            break
    while pre and pre[-1] == cyc[-1]:
        pre = pre[:-1]
        cyc = (cyc[-1],) + cyc[:-1]
    return pre, cyc


def rho_term(rho: tuple, k: int):
    pre, cyc = rho
    return pre[k] if k < len(pre) else cyc[(k - len(pre)) % len(cyc)]


def rho_prefix(rho: tuple, length: int) -> tuple:
    return tuple(rho_term(rho, k) for k in range(length))


def rho_first_difference(r1: tuple, r2: tuple) -> int | None:
    """First index where two ultimately periodic words differ (None: equal).

    Elementary bound, independent of FH-7: both are periodic after
    max(preperiods) with common period lcm(periods).
    """
    span = max(len(r1[0]), len(r2[0])) + (len(r1[1]) * len(r2[1]) // gcd(len(r1[1]), len(r2[1])))
    for k in range(span):
        if rho_term(r1, k) != rho_term(r2, k):
            return k
    return None


def all_rhos(n: int, alphabet: Sequence) -> set[tuple]:
    """Canonical outputs of all autonomous machines with <= n states."""
    out = set()
    for size in range(1, n + 1):
        for t in range(size):
            p = size - t
            for word in product(alphabet, repeat=size):
                out.add(canonical_rho(tuple(word[:t]), tuple(word[t:])))
    return out


def all_machine_rhos(n: int, alphabet: Sequence) -> set[tuple]:
    """Same set by brute machine enumeration (independent cross-check)."""
    out = set()
    for size in range(1, n + 1):
        for delta in product(range(size), repeat=size):
            for lam in product(alphabet, repeat=size):
                out.add(machine_rho(delta, lam, 0))
    return out


def max_first_difference(S: Iterable, T: Iterable) -> int:
    best = -1
    S, T = list(S), list(T)
    for x in S:
        for y in T:
            k = rho_first_difference(x, y)
            if k is not None:
                best = max(best, k)
    return best


def extremal_machine_pair(n: int, m: int) -> dict:
    """FH-7 sharpness: n-state chain vs m-cycle, first difference at n+m-2."""
    if type(n) is not int or type(m) is not int or n < 1 or m < 1:
        raise HorizonError("n, m >= 1")
    cyc_out = [1 if (k - (n - 2)) % m == 0 else 0 for k in range(m)]
    delta2 = [(k + 1) % m for k in range(m)]
    delta1 = [min(k + 1, n - 1) for k in range(n)]
    out1 = [cyc_out[k % m] if k < n - 1 else 0 for k in range(n)]
    return {"machine_n": (tuple(delta1), tuple(out1)),
            "machine_m": (tuple(delta2), tuple(cyc_out)),
            "first_difference_index": n + m - 2}


def counter_gate(k: int) -> tuple[tuple, tuple]:
    """k-bit saturating counter; outputs 1 only once the counter is all ones."""
    if type(k) is not int or not 0 <= k <= 12:
        raise HorizonError("0 <= k <= 12 bits")
    N = 2 ** k
    return tuple(min(c + 1, N - 1) for c in range(N)), tuple(int(c == N - 1) for c in range(N))


def symbol_ever_appears(delta, out, start, symbol) -> bool:
    """Exact orbit search; FH-13 says the first n outputs already decide it."""
    pre, cyc = machine_rho(delta, out, start)
    return symbol in pre or symbol in cyc


# ------------------------------------------------ Moore / Mealy (FH-8)

def shortest_distinguishing_length(delta, out, s: int, t: int, kind: str = "moore") -> int | None:
    """BFS on state pairs.  Moore: out[state]; Mealy: out[state][letter].

    Returns the length of a shortest input word separating s and t
    (Moore counts the empty word as length 0), or None if equivalent.
    """
    letters = range(len(delta[0]))
    if kind == "moore" and out[s] != out[t]:
        return 0
    seen = {(s, t)}
    frontier = deque([(s, t, 0)])
    while frontier:
        p, q, d = frontier.popleft()
        for a in letters:
            if kind == "mealy" and out[p][a] != out[q][a]:
                return d + 1
            pp, qq = delta[p][a], delta[q][a]
            if kind == "moore" and out[pp] != out[qq]:
                return d + 1
            if (pp, qq) not in seen:
                seen.add((pp, qq))
                frontier.append((pp, qq, d + 1))
    return None


def moore_exhaustive_max(N: int, letters: int, outputs: int, kind: str = "moore") -> int:
    """Max over all N-state machines and state pairs of the shortest separator."""
    best = -1
    for flat in product(range(N), repeat=N * letters):
        delta = [flat[i * letters:(i + 1) * letters] for i in range(N)]
        if kind == "moore":
            outs = product(range(outputs), repeat=N)
        else:
            outs = (tuple(o[i * letters:(i + 1) * letters] for i in range(N))
                    for o in product(range(outputs), repeat=N * letters))
        for out in outs:
            for s in range(N):
                for t in range(s + 1, N):
                    d = shortest_distinguishing_length(delta, out, s, t, kind)
                    if d is not None and d > best:
                        best = d
    return best


# --------------------------------------- weighted / probabilistic automata (FH-9)

class WeightedAutomaton:
    """f(w) = alpha M_{w1} ... M_{wk} beta over Q (row-vector convention)."""

    def __init__(self, alpha: Sequence, mats: dict, beta: Sequence):
        self.alpha = tuple(_q(x) for x in alpha)
        n = len(self.alpha)
        if n < 1:
            raise HorizonError("at least one state")
        self.mats = {a: tuple(tuple(_q(x) for x in row) for row in M) for a, M in mats.items()}
        self.beta = tuple(_q(x) for x in beta)
        if len(self.beta) != n or any(len(M) != n or any(len(r) != n for r in M) for M in self.mats.values()):
            raise HorizonError("dimension mismatch")
        self.n = n

    def value(self, word: Sequence) -> Fraction:
        v = self.alpha
        for a in word:
            M = self.mats[a]
            v = tuple(sum((v[i] * M[i][j] for i in range(self.n)), Fraction(0)) for j in range(self.n))
        return sum((x * y for x, y in zip(v, self.beta)), Fraction(0))

    def is_rabin_pa(self) -> bool:
        nonneg = all(x >= 0 for x in self.alpha) and sum(self.alpha) == 1
        return nonneg and all(all(x >= 0 for x in r) and sum(r) == 1 for M in self.mats.values() for r in M)

    def is_generative_hmm(self) -> bool:
        if not (all(x >= 0 for x in self.alpha) and sum(self.alpha) == 1 and all(b == 1 for b in self.beta)):
            return False
        if any(x < 0 for M in self.mats.values() for r in M for x in r):
            return False
        return all(sum(M[i][j] for M in self.mats.values() for j in range(self.n)) == 1 for i in range(self.n))


def wa_first_difference(A: WeightedAutomaton, B: WeightedAutomaton) -> tuple[int | None, tuple | None]:
    """Shortest differing word length via the forward-span chain (FH-9 proof).

    BFS over words, keeping only words whose difference vector is new to the
    span; the minimal differing length is attained by a kept word.
    """
    letters = sorted(set(A.mats) | set(B.mats), key=repr)
    if set(A.mats) != set(B.mats):
        raise HorizonError("alphabets differ")
    n, m = A.n, B.n
    beta = A.beta + tuple(-x for x in B.beta)
    start = A.alpha + B.alpha
    basis: list[tuple] = []  # echelon rows (vector, pivot)

    def reduce(v):
        v = list(v)
        for row, piv in basis:
            if v[piv] != 0:
                f = v[piv]
                v = [x - f * y for x, y in zip(v, row)]
        return v

    def add(v):
        v = reduce(v)
        piv = next((i for i, x in enumerate(v) if x != 0), None)
        if piv is None:
            return False
        inv = 1 / v[piv]
        v = [x * inv for x in v]
        for idx, (row, p) in enumerate(basis):
            if row[piv] != 0:
                f = row[piv]
                basis[idx] = ([x - f * y for x, y in zip(row, v)], p)
        basis.append((v, piv))
        return True

    def step(v, a):
        MA, MB = A.mats[a], B.mats[a]
        left = [sum((v[i] * MA[i][j] for i in range(n)), Fraction(0)) for j in range(n)]
        right = [sum((v[n + i] * MB[i][j] for i in range(m)), Fraction(0)) for j in range(m)]
        return left + right

    best = None
    queue = deque()
    if add(start):
        queue.append((start, ()))
    while queue:
        v, w = queue.popleft()
        if best is None and sum((x * y for x, y in zip(v, beta)), Fraction(0)) != 0:
            best = (len(w), w)
        for a in letters:
            nv = step(v, a)
            if add(nv):
                queue.append((nv, w + (a,)))
    return best if best is not None else (None, None)


def wa_first_difference_bruteforce(A, B, max_len: int) -> int | None:
    letters = sorted(A.mats, key=repr)
    for L in range(max_len + 1):
        for w in product(letters, repeat=L):
            if A.value(w) != B.value(w):
                return L
    return None


def companion_automaton(coeffs: Sequence, init: Sequence) -> WeightedAutomaton:
    """One-letter weighted automaton with f('x'^k) = s_k (s from coeffs, init)."""
    c = [_q(x) for x in coeffs]
    L = len(c)
    if L == 0:
        return WeightedAutomaton([0], {"x": [[0]]}, [0])
    M = [[Fraction(0)] * L for _ in range(L)]
    for j in range(L - 1):
        M[j + 1][j] = Fraction(1)
    for i in range(L):
        M[i][L - 1] = c[i]
    return WeightedAutomaton(list(init), {"x": M}, [1] + [0] * (L - 1))


def deterministic_pa(delta, out_values, start: int = 0) -> WeightedAutomaton:
    """Autonomous Moore machine as a one-letter Rabin PA, f(x^k)=output_k."""
    N = len(delta)
    M = [[Fraction(int(delta[i] == j)) for j in range(N)] for i in range(N)]
    return WeightedAutomaton([int(i == start) for i in range(N)], {"x": M}, list(out_values))


def deterministic_generative_hmm(delta, out_symbols, alphabet, start: int = 0) -> WeightedAutomaton:
    """Autonomous machine as a generative HMM emitting its output sequence."""
    N = len(delta)
    mats = {s: [[Fraction(int(delta[i] == j and out_symbols[i] == s)) for j in range(N)]
                for i in range(N)] for s in alphabet}
    return WeightedAutomaton([int(i == start) for i in range(N)], mats, [1] * N)


# ------------------------------------------------------ modulus (FH-10)

def modulus_prefix_consistent(prefix: Sequence, mu: Callable[[int], Fraction]) -> bool:
    p = [_q(x) for x in prefix]
    return all(abs(p[i] - p[j]) <= _q(mu(i)) for i in range(len(p)) for j in range(i + 1, len(p)))


def modulus_limit_interval(prefix: Sequence, mu: Callable[[int], Fraction]):
    """Exact set of limits over the fibre {e in C_mu : e|N = prefix}.

    C_mu: |e_i - e_j| <= mu(min(i,j)), mu nonincreasing.  The set is the
    closed interval cap_j [p_j - mu(j), p_j + mu(j)]; None if fibre empty.
    """
    p = [_q(x) for x in prefix]
    if not p:
        raise HorizonError("nonempty prefix required (empty prefix: unbounded)")
    if not modulus_prefix_consistent(p, mu):
        return None
    lo = max(p[j] - _q(mu(j)) for j in range(len(p)))
    hi = min(p[j] + _q(mu(j)) for j in range(len(p)))
    return lo, hi


def eventually_constant_in_class(prefix: Sequence, tail: object, mu) -> bool:
    """Exact membership in C_mu of prefix followed by the constant tail."""
    p = [_q(x) for x in prefix]
    L = _q(tail)
    return modulus_prefix_consistent(p, mu) and all(abs(p[i] - L) <= _q(mu(i)) for i in range(len(p)))


def worst_case_limit_oscillation(N: int, mu) -> Fraction:
    if type(N) is not int or N < 1:
        raise HorizonError("N >= 1 observed terms")
    return 2 * _q(mu(N - 1))


# ------------------------------------- adaptive / randomised protocols (FH-1/2)

def run_protocol(protocol: Callable, oracle: Callable[[int], object], coins: tuple = ()) -> tuple:
    """Run protocol(ask, coins) -> decision; returns (decision, queried indices)."""
    asked: list[int] = []

    def ask(i: int):
        if type(i) is not int or i < 0:
            raise HorizonError("queries are nonnegative int indices")
        asked.append(i)
        return oracle(i)
    return protocol(ask, coins), tuple(asked)


def fool_protocol_on_founding_pair(protocol: Callable) -> dict:
    """Run on a=1/(n+1); return b_H with H = max query, same transcript."""
    a = lambda i: Fraction(1, i + 1)
    dec_a, qa = run_protocol(protocol, a)
    H = max(qa, default=0)
    b = lambda i: Fraction(1, i + 1) if i <= H else Fraction(1)
    dec_b, qb = run_protocol(protocol, b)
    return {"H": H, "decision_a": dec_a, "decision_b": dec_b,
            "same_transcript": qa == qb and dec_a == dec_b}


def randomized_error_sum(protocol: Callable, x, y, target_x, target_y, coin_bits: int) -> Fraction:
    """Exact err(x)+err(y) over uniformly random coin strings."""
    tot = Fraction(0)
    for coins in product((0, 1), repeat=coin_bits):
        tot += int(run_protocol(protocol, x, coins)[0] != target_x)
        tot += int(run_protocol(protocol, y, coins)[0] != target_y)
    return tot / 2 ** coin_bits


def pointer_member(k: int, bit: int) -> Callable[[int], int]:
    """Pointer class: x(0)=k, x(k+1)=bit, zeros elsewhere; target = bit."""
    return lambda i: k if i == 0 else (bit if i == k + 1 else 0)


def pointer_protocol(ask, coins=()):
    k = ask(0)
    return ask(k + 1)


# ---------------------------------------- polynomial recurrences (FH-14)

def poly_orbit_gf(field: PrimeField, poly: Sequence[int], x0: int, length: int) -> tuple:
    out, x = [], x0 % field.p
    for _ in range(length):
        out.append(x)
        x = sum(c * pow(x, i, field.p) for i, c in enumerate(poly)) % field.p
    return tuple(out)


def poly_recurrence_class_gf(field: PrimeField, d: int, length: int) -> set[tuple]:
    out = set()
    for poly in product(range(field.p), repeat=d + 1):
        for x0 in range(field.p):
            out.add(poly_orbit_gf(field, poly, x0, length))
    return out


def poly_recurrence_extremal(d: int, length: int) -> tuple[tuple, tuple]:
    """Over Q: x_{k+1}=f(x_k), y_{k+1}=g(y_k), deg<=d, agree on d+1 terms only.

    x_k = k for k<=d (f(t)=t+1); g(t) = t+1 + t(t-1)...(t-d+1).
    """
    if type(d) is not int or d < 1:
        raise HorizonError("d >= 1")
    f = lambda t: t + 1
    g = lambda t: t + 1 + gen_binom(t, d) * factorial(d)
    xs, ys = [0], [0]
    while len(xs) < length:
        xs.append(f(xs[-1]))
        ys.append(g(ys[-1]))
    return tuple(xs), tuple(ys)
