"""Exact, zero-independent SUCC residue clocks for Nyman--Beurling probes.

Finite certificates only. RH is not proved. See the adjacent research dossier.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import lcm


class ZeroCenteredError(ValueError):
    pass


def _integer(n, lo, hi):
    if type(n) is not int or not lo <= n <= hi:
        raise ZeroCenteredError(f"expected an integer in [{lo},{hi}]")
    return n


def clock(k: int, n: int) -> Q:
    """Cell k = floor(1/x): {1/(nx)}-{1/x}/n = (k mod n)/n."""
    _integer(k, 1, 1_000_000)
    _integer(n, 2, 1_000_000)
    return Q(k % n, n)


def cell_of(x: Q) -> int:
    if type(x) not in (int, Q) or not 0 < x < 1:
        raise ZeroCenteredError("x must be an exact rational strictly in (0,1)")
    t = 1 / Q(x)
    return t.numerator // t.denominator


def direct_probe(x: Q, n: int) -> Q:
    _integer(n, 2, 1_000_000)
    k = cell_of(x)
    t = 1 / Q(x)
    u = t / n
    return u - u.numerator // u.denominator - (t - k) / n


def mobius(K: int) -> dict[int, int]:
    """True Möbius coefficients derived from integer divisibility."""
    _integer(K, 2, 512)
    mu = {1: 1}
    for n in range(2, K + 1):
        mu[n] = -sum(mu[d] for d in range(1, n) if n % d == 0)
    return mu


def coefficients(K: int, mutation: dict[int, int] | None = None) -> dict[int, Q]:
    """Finite fit; mutation deliberately changes authentic source b(n)."""
    b = mobius(K)
    if mutation:
        for n, v in mutation.items():
            _integer(n, 2, K)
            _integer(v, -3, 3)
            b[n] = v
    a = {n: Q(-b[n]) for n in range(2, K + 1)}
    a[K + 1] = (K + 1) * sum((Q(b[n], n) for n in range(1, K + 1)), Q())
    return a


def value(k: int, a: dict[int, Q]) -> Q:
    if not a:
        raise ZeroCenteredError("nonempty coefficient family required")
    return sum((Q(c) * clock(k, n) for n, c in a.items()), Q())


def arbitrary_target(target: tuple[Q, ...]) -> dict[int, Q]:
    """Unique rational interpolation of any first-K target values."""
    K = len(target)
    _integer(K, 2, 512)
    if any(type(x) not in (int, Q) for x in target):
        raise ZeroCenteredError("only exact rational targets")
    t = (Q(0),) + tuple(Q(x) for x in target)
    d = [Q(0)] + [t[k] - t[k-1] for k in range(1, K+1)]
    mu = mobius(K)
    b = {n: sum((mu[e] * d[n//e] for e in range(1,n+1) if n%e == 0), Q())
         for n in range(1,K+1)}
    a = {n:-b[n] for n in range(2,K+1)}
    a[K+1] = (K+1) * sum((b[n]/n for n in range(1,K+1)),Q())
    return a


def blackout(a: dict[int, Q]) -> dict:
    """All clocks vanish at L=lcm(moduli), hence global L2 error² >=1/L²."""
    if not a:
        raise ZeroCenteredError("nonempty coefficient family required")
    for n, c in a.items():
        _integer(n,2,1_000_000)
        if type(c) not in (int,Q):
            raise ZeroCenteredError("only exact rational coefficients")
    L = lcm(*a.keys())
    return {"lcm_cell":L,"all_clocks_vanish":True,
            "global_squared_error_lower_bound":str(Q(1,L*L)),
            "uniform_bound_in_L":False,"RH_proved":False}


def distance_interval(a: dict[int,Q], K: int = 128) -> tuple[Q,Q]:
    """Global squared L² norm in certified rational interval."""
    _integer(K,1,100_000)
    if not a or any(type(c) not in (int,Q) for c in a.values()):
        raise ZeroCenteredError("nonempty rational coefficient family required")
    lower=sum(((1-value(k,a))**2*Q(1,k*(k+1)) for k in range(1,K+1)),Q())
    A=sum((abs(Q(v)) for v in a.values()),Q())
    return lower, lower+(1+A)**2/Q(K+1)


def gram_interval(m: int,n: int,K: int = 128) -> tuple[Q,Q]:
    _integer(K,1,100_000)
    lower=sum((clock(k,m)*clock(k,n)*Q(1,k*(k+1))
               for k in range(1,K+1)),Q())
    return lower, lower+Q((m-1)*(n-1),m*n*(K+1))


def mellin_cell(s: int,k: int) -> Q:
    """Exact integral of x^(s-1) on reciprocal cell; integer s only."""
    _integer(s,1,16)
    _integer(k,1,1_000_000)
    return (Q(1,k)**s-Q(1,k+1)**s)/s


def fake_cell_delta(s: int,k: int,delta: Q) -> Q:
    if type(delta) not in (int,Q):
        raise ZeroCenteredError("only exact rational mutation")
    return Q(delta)*mellin_cell(s,k)


def receipt(K: int, mutation: dict[int,int] | None = None) -> dict:
    a=coefficients(K,mutation)
    b=mobius(K)
    if mutation:
        b.update(mutation)
    vals=[value(k,a) for k in range(1,K+1)]
    conv=[sum(b[d] for d in range(1,k+1) if k%d==0) for k in range(1,K+1)]
    if [vals[0]]+[vals[k]-vals[k-1] for k in range(1,K)] != conv:
        raise ArithmeticError("source/clock finite difference inconsistency")
    return {"K":K,"genuine_source":b==mobius(K),
            "all_prefix_cells_exact":all(v==1 for v in vals),
            "values":[str(v) for v in vals],
            "first_bad_divisor":next((i for i in range(2,K+1) if conv[i-1]),None),
            "no_zeta_zero_inputs":True,"RH_proved":False,
            "completed_Gamma_or_Weil_identified":False}
