"""Bounded combinatorial shadows; the Euler logarithm is ONE projection.

All occurrence counts and coefficient arithmetic are exact. A shadow is not
an observed event, a probability, a quantum state, or a certified Weil sign.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, lcm, prod
from typing import Mapping
from types import MappingProxyType

from .core import (ActualizationError, BudgetExceeded, DomainError,
                   IncompleteObservation, Scalar, ZERO, ONE, I)


def positive_int(x, name="integer"):
    if type(x) is not int or x < 1:
        raise DomainError(f"{name} must be a positive integer")
    return x


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    positive_int(n)
    if n > 1_000_000:
        raise BudgetExceeded("Trial-factorization input exceeds the declared finite bound")
    out, p = [], 2
    while p*p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            out.append((p, k))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def structure_birth(n: int) -> int:
    return max((p**k for p, k in factorization(n)), default=1)


def divisors(n: int) -> tuple[int, ...]:
    out = [1]
    for p, k in factorization(n):
        out = [d*p**j for d in out for j in range(k+1)]
    return tuple(sorted(out))


@dataclass(frozen=True)
class Limits:
    max_target: int = 64
    max_depth: int = 8
    max_records: int = 1024
    max_witnesses: int = 128
    max_probe_cells: int = 4096
    max_trace_bytes: int = 8_000_000

    def __post_init__(self):
        for name, value, lower, upper in (
            ("max_target", self.max_target, 2, 2048),
            ("max_depth", self.max_depth, 1, 32),
            ("max_records", self.max_records, 2, 8192),
            ("max_witnesses", self.max_witnesses, 1, 10000),
            ("max_probe_cells", self.max_probe_cells, 1, 100000),
            ("max_trace_bytes", self.max_trace_bytes, 1024, 32_000_000)):
            if type(value) is not int or not lower <= value <= upper:
                raise BudgetExceeded(f"{name} must be in {lower}..{upper}")

    def data(self):
        return dict(vars(self))

    @classmethod
    def from_data(cls, d):
        if not isinstance(d, dict) or set(d) != set(cls().data()):
            raise DomainError("Malformed resource limits")
        return cls(**d)


@dataclass(frozen=True)
class ShadowEntry:
    target: int
    counts: tuple[tuple[int, int], ...]
    products: tuple[tuple[int, Scalar], ...]
    weight: Scalar
    complete: bool
    longest_history: int
    integrated: bool

    @property
    def occurrences(self):
        return sum(n for _, n in self.counts)

    def exact_weight(self):
        if not self.complete:
            raise IncompleteObservation("The depth budget omitted realizable histories")
        return self.weight

    def data(self):
        return {"target": self.target, "occurrences_by_depth": [list(x) for x in self.counts],
                "coefficient_products_by_depth": [[d, v.data()] for d, v in self.products],
                "weight": self.weight.data(), "complete": self.complete,
                "longest_history": self.longest_history, "integrated": self.integrated,
                "occurrences": self.occurrences,
                "meaning": "Dirichlet-log projection of retained structural paths, not an encounter"}


class ShadowIndex:
    """Compressed, exact ordered-factor history DAG, built ONLY from supplied data.

    known contains actually integrated observations. No source provider is
    consulted by this class. Counts are retained even when amplitudes cancel.
    A target outside max_target raises; truncation is never silently zero.
    """
    def __init__(self, known: Mapping[int, Scalar], limits: Limits = Limits()):
        self.limits = limits
        self.known = {}
        for n, v in known.items():
            positive_int(n, "source label")
            if n > limits.max_target:
                raise BudgetExceeded("Observed label outside the arithmetic target bound")
            self.known[n] = Scalar.of(v)
        if 1 in self.known and self.known[1] != ONE:
            raise DomainError("The Dirichlet-log chart requires a(1)=1")
        self.known = MappingProxyType(self.known)
        size, depth = limits.max_target+1, limits.max_depth
        self._counts = [[0]*(depth+1) for _ in range(size)]
        self._products = [[ZERO]*(depth+1) for _ in range(size)]
        self._longest = [0]*size
        for n in range(2, size):
            if n in self.known:
                self._counts[n][1] = 1
                self._products[n][1] = self.known[n]
                self._longest[n] = 1
            for f in divisors(n):
                if f < 2 or f == n or f not in self.known:
                    continue
                r = n//f
                if self._longest[r]:
                    self._longest[n] = max(self._longest[n], 1+self._longest[r])
                for k in range(2, depth+1):
                    self._counts[n][k] += self._counts[r][k-1]
                    self._products[n][k] += self.known[f]*self._products[r][k-1]

    def entry(self, target: int) -> ShadowEntry:
        positive_int(target, "target")
        if not 2 <= target <= self.limits.max_target:
            raise BudgetExceeded("Shadow target is outside the declared observation window")
        counts = tuple((k, c) for k, c in enumerate(self._counts[target]) if k >= 2 and c)
        products = tuple((k, self._products[target][k]) for k, _ in counts)
        weight = sum((v*Q((-1)**(k+1), k) for k, v in products), ZERO)
        return ShadowEntry(target, counts, products, weight,
                           self._longest[target] <= self.limits.max_depth,
                           self._longest[target], target in self.known)

    def connected(self, target: int):
        if target not in self.known or 1 not in self.known:
            raise IncompleteObservation("Connected value needs its direct event and the unit event")
        e = self.entry(target)
        return self.known[target]+e.exact_weight()

    def witnesses(self, target: int):
        """Bounded witness expansion; completeness is distinct from aggregate exactness."""
        e = self.entry(target)
        paths = []
        alphabet = tuple(sorted(n for n in self.known if n >= 2))

        def visit(rem, path):
            if len(paths) >= self.limits.max_witnesses:
                return
            if rem == 1:
                if len(path) >= 2:
                    paths.append(path)
                return
            if len(path) == self.limits.max_depth:
                return
            for f in alphabet:
                if f > rem:
                    break
                if rem % f == 0:
                    visit(rem//f, path+(f,))

        visit(target, ())
        return {"target": target, "paths": [list(x) for x in paths],
                "expanded": len(paths), "retained_occurrences": e.occurrences,
                "expansion_complete": e.complete and len(paths) == e.occurrences,
                "aggregate_complete": e.complete}


def source_at(n: int, kind="zeta", overrides: Mapping[int, Scalar] | None = None):
    """A deterministic fixture/provider; call at the encounter, never in ShadowIndex.

    'chi5' is the quartic mod-5 character; 'chi5_bar' its conjugate.
    'mixture5' is their exact positive equal mixture, NOT Davenport-Heilbronn.
    """
    positive_int(n)
    if overrides is not None and n in overrides:
        return Scalar.of(overrides[n])
    if kind == "zeta":
        return ONE
    z = (ZERO, ONE, I, -I, -ONE)[n % 5]
    if kind == "chi5":
        return z
    if kind == "chi5_bar":
        return z.conjugate()
    if kind == "mixture5":
        return (z+z.conjugate())/2
    raise DomainError("Unknown source fixture")


def connected_audit(index: ShadowIndex, n: int, conductor: int | None = None):
    """Finite degree-one Euler tests; passing is not proof of a global character."""
    if conductor is not None:
        positive_int(conductor, "conductor")
    e = index.entry(n)
    if not e.complete or 1 not in index.known or n not in index.known:
        return {"status": "incomplete", "target": n}
    # Do not confuse missing a divisor's event with a measured zero coefficient.
    missing = [d for d in divisors(n) if d not in index.known]
    if missing:
        return {"status": "unobserved_divisors", "target": n, "missing": missing}
    c = index.connected(n)
    fs = factorization(n)
    if len(fs) == 1:
        p, k = fs[0]
        expected = index.known[p]**k/k
        status = "consistent" if c == expected else "prime_ray_defect"
        allowed = {Q(0), Q(1)} if conductor is None else ({Q(1)} if gcd(p, conductor) == 1 else {Q(0)})
        if index.known[p].norm2() not in allowed:
            status = "nonunit_local_factor" if conductor is None or gcd(p, conductor) == 1 else "ramification_defect"
    else:
        expected = ZERO
        status = "consistent" if c == ZERO else "mixed_composite_defect"
    return {"target": n, "connected": c.data(), "expected": expected.data(), "status": status,
            "log_degree": [[p, k] for p, k in fs], "half_density": "1/2",
            "symbolic_response": f"({c})*log({n})/sqrt({n})",
            "scope": "coefficient-level degree-one source consistency, not Weil positivity"}


def clock_contract(n: int, degree, half_density=Q(1, 2)):
    """Compare symbolic log-prime coordinates; no floating tolerances or fake clocks."""
    expected = tuple((p, Q(k)) for p, k in factorization(n))
    seen = tuple(sorted((positive_int(p), Q(k)) for p, k in degree))
    if seen != expected or Q(half_density) != Q(1, 2):
        raise DomainError("Physical logarithmic degree or half-density was changed")
    return True


def conductor_growth(n: int, max_divisors=10000):
    positive_int(n)
    if n > 256:
        raise BudgetExceeded("Conductor-growth metadata supports horizons <=256")
    old = lcm(*range(1, n)) if n > 1 else 1
    new = lcm(old, n)
    # Rank and modulus are cheap. Never materialize all L_N residue states.
    fs = {}
    for j in range(2, n+1):
        for p, k in factorization(j):
            fs[p] = max(k, fs.get(p, 0))
    count = prod(k+1 for k in fs.values())
    born = None
    if count <= max_divisors:
        ds = [1]
        for p, k in fs.items():
            ds = [d*p**j for d in ds for j in range(k+1)]
        born = sorted(d for d in ds if old % d)
    return {"horizon": n, "old_modulus": old, "modulus": new,
            "innovation_rank": new-old, "born_conductors": born,
            "enumeration_complete": born is not None,
            "structural_only": True}


def mixed_probe(primes: tuple[int, ...], limits=Limits()):
    if not primes or len(set(primes)) != len(primes) or any(factorization(p) != ((p, 1),) for p in primes):
        raise DomainError("Joint CRT probe requires distinct primes")
    d = prod(primes)
    if d > limits.max_probe_cells:
        raise BudgetExceeded("Finite CRT probe would exceed cell budget")
    values = tuple(prod((Q(int(n % p == 0))-Q(1, p) for p in primes), start=Q(1)) for n in range(d))
    return values


def conditional_mean(values, modulus: int):
    positive_int(modulus, "conditional modulus")
    if not values or len(values) % modulus:
        raise DomainError("Conditional modulus must divide the finite clock")
    return tuple(sum(values[r::modulus], Q(0))/(len(values)//modulus) for r in range(modulus))
