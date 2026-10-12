"""Exact finite certificates for components of periodic lattice graphs.

A finite residue graph alone does not preserve unbounded motion. Every
edge here retains its actual integer displacement, including quotient
self-loops and parallel edges. A potential integrates every edge exactly
iff all lifted components are finite. Otherwise a closed quotient word
with nonzero translation is returned. See the research dossier for the
classical covering-graph proof and the distinct-vertex walk qualification.

Gaussian norm sieves are *overapproximations* of Gaussian primes, apart
from an explicitly calculated finite exceptional set. A leaking sieve
does not certify a prime walk. No all-step existence theorem is encoded.
"""
from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, field
from hashlib import sha256
from itertools import product
import json
from math import isqrt, prod

from .residue_one_arch import prime

Vector = tuple[int, ...]


class CertificateError(ValueError):
    """Malformed input or a false/mismatched finite certificate."""


class SearchBudgetExceeded(RuntimeError):
    """A declared finite resource cap was reached; existence is unresolved."""


def _integer(value: int, name: str, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise CertificateError(f"{name} must be an exact integer >= {minimum}")
    return value


def _vector(value: Vector, dimension: int) -> Vector:
    if type(value) is not tuple or len(value) != dimension:
        raise CertificateError("Wrong integer-vector dimension or type")
    for x in value:
        _integer(x, "coordinate")
    return value


def _add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def _sub(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))


def _neg(a: Vector) -> Vector:
    return tuple(-x for x in a)


@dataclass(frozen=True)
class PeriodicGraph:
    """Graph on {x in Z^dimension: x mod period is in residues}."""

    period: int
    dimension: int
    residues: tuple[Vector, ...]
    steps: tuple[Vector, ...]
    _allowed: frozenset[Vector] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        _integer(self.period, "period", 1)
        _integer(self.dimension, "dimension", 1)
        for name, vectors in (("residues", self.residues), ("steps", self.steps)):
            if type(vectors) is not tuple:
                raise CertificateError(f"{name} must be a tuple")
            for v in vectors:
                _vector(v, self.dimension)
            if len(set(vectors)) != len(vectors):
                raise CertificateError(f"{name} must not contain duplicates")
        if any(not all(0 <= x < self.period for x in v) for v in self.residues):
            raise CertificateError("Residues must be canonical representatives")
        step_set = set(self.steps)
        if (0,) * self.dimension in step_set or any(_neg(s) not in step_set for s in step_set):
            raise CertificateError("Steps must be nonzero and symmetric")
        object.__setattr__(self, "residues", tuple(sorted(self.residues)))
        object.__setattr__(self, "steps", tuple(sorted(self.steps)))
        object.__setattr__(self, "_allowed", frozenset(self.residues))

    def residue(self, point: Vector) -> Vector:
        _vector(point, self.dimension)
        return tuple(x % self.period for x in point)

    def contains(self, point: Vector) -> bool:
        return self.residue(point) in self._allowed

    def edges(self, start: Vector):
        """Yield (target residue, true displacement); never deduplicate targets."""
        for step in self.steps:
            target = self.residue(_add(start, step))
            if target in self._allowed:
                yield target, step

    @property
    def digest(self) -> str:
        data = (self.period, self.dimension, self.residues, self.steps)
        return sha256(json.dumps(data, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class ConfinementCertificate:
    graph_digest: str
    # Potential values are actual lattice representatives, not just residues.
    potentials: tuple[tuple[Vector, Vector], ...]

    def to_dict(self) -> dict:
        return {"kind": "confinement", "graph_digest": self.graph_digest,
                "potentials": [[list(r), list(h)] for r, h in self.potentials]}


@dataclass(frozen=True)
class TranslationWitness:
    graph_digest: str
    start: Vector
    word: tuple[Vector, ...]

    def to_dict(self) -> dict:
        return {"kind": "translation", "graph_digest": self.graph_digest,
                "start": list(self.start), "word": [list(s) for s in self.word]}


def analyze_periodic(graph: PeriodicGraph) -> ConfinementCertificate | TranslationWitness:
    """Complete finite decision: potential or nonzero closed-walk translation."""
    potentials: dict[Vector, Vector] = {}
    parents: dict[Vector, tuple[Vector, Vector] | None] = {}

    def path(vertex: Vector) -> tuple[Vector, ...]:
        word = []
        while parents[vertex] is not None:
            parent, step = parents[vertex]
            word.append(step)
            vertex = parent
        return tuple(reversed(word))

    for root in graph.residues:
        if root in potentials:
            continue
        potentials[root] = root
        parents[root] = None
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, step in graph.edges(u):
                proposed = _add(potentials[u], step)
                if v not in potentials:
                    potentials[v] = proposed
                    parents[v] = (u, step)
                    queue.append(v)
                elif potentials[v] != proposed:
                    word = path(u) + (step,) + tuple(_neg(s) for s in reversed(path(v)))
                    return TranslationWitness(graph.digest, root, word)
    return ConfinementCertificate(graph.digest, tuple(sorted(potentials.items())))


class _DisjointSets:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.size = {v: 1 for v in vertices}

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def join(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.parent[v] = u
        self.size[u] += self.size[v]


def _verify_potential(graph: PeriodicGraph, certificate: ConfinementCertificate):
    """Verifier uses all regenerated edges and disjoint sets, not builder BFS."""
    if not isinstance(certificate, ConfinementCertificate) or certificate.graph_digest != graph.digest:
        raise CertificateError("Certificate does not match the declared periodic graph")
    if type(certificate.potentials) is not tuple or any(
            type(row) is not tuple or len(row) != 2 for row in certificate.potentials):
        raise CertificateError("Immutable potential rows required")
    h = {}
    for r, value in certificate.potentials:
        _vector(r, graph.dimension)
        _vector(value, graph.dimension)
        if r in h or graph.residue(value) != r:
            raise CertificateError("Repeated residue or false potential representative")
        h[r] = value
    if set(h) != graph._allowed:
        raise CertificateError("Potential does not cover exactly the source residue set")
    dsu = _DisjointSets(graph.residues)
    edges = 0
    for u in graph.residues:
        for v, step in graph.edges(u):
            edges += 1
            if _sub(h[v], h[u]) != step:
                raise CertificateError("Nonzero displacement around a quotient closed walk")
            dsu.join(u, v)
    labels = {r: dsu.find(r) for r in graph.residues}
    sizes = Counter(labels.values())
    return h, labels, sizes, edges


def verify_confinement(graph: PeriodicGraph, certificate: ConfinementCertificate) -> dict:
    _, _, sizes, edges = _verify_potential(graph, certificate)
    return {"status": "EXACT_PERIODIC_CONFINEMENT", "graph_digest": graph.digest,
            "vertices": len(graph.residues), "directed_edges": edges,
            "components": len(sizes), "maximum_component_size": max(sizes.values(), default=0),
            "component_size_histogram": dict(sorted(Counter(sizes.values()).items())),
            "scope": "all integer translates of this exact periodic graph",
            "all_walks_terminate": False}


def verify_translation(graph: PeriodicGraph, witness: TranslationWitness) -> dict:
    if not isinstance(witness, TranslationWitness) or witness.graph_digest != graph.digest:
        raise CertificateError("Witness does not match the declared periodic graph")
    _vector(witness.start, graph.dimension)
    if witness.start not in graph._allowed or not witness.word:
        raise CertificateError("Translation witness needs a nonempty legal closed word")
    point = witness.start
    for step in witness.word:
        _vector(step, graph.dimension)
        if step not in graph.steps:
            raise CertificateError("Witness uses an undeclared step")
        point = _add(point, step)
        if not graph.contains(point):
            raise CertificateError("Witness crosses an excluded residue")
    displacement = _sub(point, witness.start)
    if graph.residue(point) != witness.start or not any(displacement):
        raise CertificateError("Witness must close in the quotient with nonzero displacement")
    return {"status": "EXACT_PERIODIC_TRANSLATION", "word_length": len(witness.word),
            "displacement": list(displacement),
            "period_translation": [x // graph.period for x in displacement],
            "scope": "an infinite component of the periodic graph only",
            "gaussian_prime_walk_certified": False}


def transport_confinement(coarse: PeriodicGraph, fine: PeriodicGraph,
                          certificate: ConfinementCertificate) -> ConfinementCertificate:
    """Pull a proof through a source refinement with the same true step labels.

    Fine period must be a multiple, its source set a subset of the coarse
    set, and its step alphabet no larger. This is a checked mathematical
    source morphism, not an assertion that any new observation is sound.
    """
    h, _, _, _ = _verify_potential(coarse, certificate)
    if (fine.dimension != coarse.dimension or fine.period % coarse.period
            or not set(fine.steps) <= set(coarse.steps)
            or any(coarse.residue(r) not in coarse._allowed for r in fine.residues)):
        raise CertificateError("Source refinement does not preserve the proof hypotheses")
    lifted = []
    for r in fine.residues:
        old = h[coarse.residue(r)]
        # Along a fine edge, old - r changes by a multiple of fine.period.
        value = tuple(x - ((x-y) % fine.period) for x, y in zip(old, r))
        lifted.append((r, value))
    result = ConfinementCertificate(fine.digest, tuple(lifted))
    verify_confinement(fine, result)
    return result


def verify_finite_defects(graph: PeriodicGraph, certificate: ConfinementCertificate,
                          exceptions: tuple[Vector, ...]) -> dict:
    """Exact component maximum of A union E, from a finite weighted incidence graph.

    A is the entire periodic set; E is finite and disjoint from A. A lifted
    component is keyed by its quotient component and its integer translate.
    Only finitely many such components meet E. Untouched translates remain.
    """
    h, labels, sizes, _ = _verify_potential(graph, certificate)
    if type(exceptions) is not tuple or len(set(exceptions)) != len(exceptions):
        raise CertificateError("Exceptions must be distinct integer vectors")
    for e in exceptions:
        _vector(e, graph.dimension)
        if graph.contains(e):
            raise CertificateError("Finite defects must be disjoint from the periodic set")
    es = set(exceptions)
    weights = {("exception", e): 1 for e in exceptions}
    incidences = []
    for e in exceptions:
        node = ("exception", e)
        for step in graph.steps:
            z = _add(e, step)
            if z in es:
                incidences.append((node, ("exception", z)))
            elif graph.contains(z):
                r = graph.residue(z)
                shift = tuple(x // graph.period for x in _sub(z, h[r]))
                target = ("periodic", labels[r], shift)
                weights[target] = sizes[labels[r]]
                incidences.append((node, target))
    dsu = _DisjointSets(weights)
    for u, v in incidences:
        dsu.join(u, v)
    sums = Counter()
    for node, weight in weights.items():
        sums[dsu.find(node)] += weight
    base = max(sizes.values(), default=0)
    maximum = max(base, max(sums.values(), default=0))
    e = len(exceptions)
    crude = max(base, e + e * len(graph.steps) * base)
    return {"status": "EXACT_PERIODIC_PLUS_FINITE_DEFECT_BOUND",
            "periodic_maximum": base, "exceptions": e,
            "adjacent_periodic_components": len(weights) - e,
            "exception_cluster_sizes": sorted(sums.values()),
            "maximum_component_size": maximum,
            "coarse_degree_bound": crude}


def _prime_candidates(primes: tuple[int, ...]) -> tuple[int, ...]:
    if type(primes) is not tuple:
        raise CertificateError("Declare a tuple of rational primes")
    for p in primes:
        _integer(p, "prime", 2)
    if len(set(primes)) != len(primes):
        raise CertificateError("Declare distinct rational primes")
    return tuple(sorted(primes))


def _checked_primes(primes: tuple[int, ...]) -> tuple[int, ...]:
    candidates = _prime_candidates(primes)
    for p in candidates:
        if not prime(p):
            raise CertificateError("Composite source cannot label a prime sieve")
    return candidates


def gaussian_sieve(primes: tuple[int, ...], step_squared: int, *,
                   max_cells: int = 1_000_000, max_step_box: int = 100_000) -> PeriodicGraph:
    """Norm sieve p does not divide a^2+b^2, with all Gaussian factor types.

    step_squared is exact: edges have integer squared norm <= this value.
    The optional resource caps interrupt computation, never certify failure.
    """
    ps = _prime_candidates(primes)
    _integer(step_squared, "squared step bound", 0)
    _integer(max_cells, "cell budget", 1)
    _integer(max_step_box, "step enumeration budget", 1)
    q = prod(ps)
    radius = isqrt(step_squared)
    if q * q > max_cells or (2 * radius + 1) ** 2 > max_step_box:
        raise SearchBudgetExceeded("Finite enumeration budget reached; theorem unresolved")
    # Budget first: do not start trial division on an enormous untrusted input.
    _checked_primes(ps)
    residues = tuple((x, y) for x in range(q) for y in range(q)
                     if all((x*x + y*y) % p != 0 for p in ps))
    steps = tuple((x, y) for x in range(-radius, radius + 1)
                  for y in range(-radius, radius + 1) if 0 < x*x + y*y <= step_squared)
    expected = prod(2 if p == 2 else (p - 1)**2 if p % 4 == 1 else p*p - 1 for p in ps)
    if len(residues) != expected:
        raise ArithmeticError("Norm sieve disagrees with independent CRT survivor count")
    return PeriodicGraph(q, 2, residues, steps)


def is_gaussian_prime(point: Vector) -> bool:
    a, b = _vector(point, 2)
    if a and b:
        return prime(a*a + b*b)
    q = abs(a or b)
    return q % 4 == 3 and prime(q)


def gaussian_exceptions(primes: tuple[int, ...]) -> tuple[Vector, ...]:
    points = set()
    for p in _checked_primes(primes):
        if p % 4 == 3:
            points.update(((p, 0), (-p, 0), (0, p), (0, -p)))
        else:
            for a in range(1, isqrt(p) + 1):
                b = isqrt(p - a*a)
                if b > 0 and a*a + b*b == p:
                    for s, t in product((-1, 1), repeat=2):
                        points.add((s*a, t*b))
                        points.add((s*b, t*a))
    expected = sum(4 if p == 2 or p % 4 == 3 else 8 for p in primes)
    if len(points) != expected or not all(is_gaussian_prime(z) for z in points):
        raise ArithmeticError("Gaussian exceptional-prime classification failed")
    return tuple(sorted(points))


def gaussian_bound(primes: tuple[int, ...], step_squared: int,
                   certificate: ConfinementCertificate, *, max_cells: int = 1_000_000) -> dict:
    """Verified source containment plus finite-defect transport to all primes."""
    graph = gaussian_sieve(primes, step_squared, max_cells=max_cells)
    base = verify_confinement(graph, certificate)
    defects = verify_finite_defects(graph, certificate, gaussian_exceptions(primes))
    return {"status": "CERTIFIED_GAUSSIAN_PRIME_COMPONENT_UPPER_BOUND",
            "rational_primes": list(_checked_primes(primes)), "period": graph.period,
            "step_squared": step_squared, "sieve": base, "finite_defects": defects,
            "prime_component_upper_bound": defects["maximum_component_size"],
            "prime_bound_is_optimal": False,
            "all_step_existence_used_by_verifier": False}


def search_split_prime_prefix(step_squared: int, *, prime_limit: int,
                              max_cells: int = 1_000_000) -> dict:
    """Bounded executable version of the conditional terminating search.

    Without caps, totality follows from the EXTERNAL finite-sieve theorem.
    This bounded run returns unresolved when either cap stops the search.
    A positive output is verified without invoking that external theorem.
    """
    _integer(step_squared, "squared step bound", 0)
    _integer(prime_limit, "prime search limit", 2)
    _integer(max_cells, "cell budget", 1)
    primes = []
    attempts = []
    for p in range(5, prime_limit + 1, 4):
        # If the next integer is already too large for the product, any
        # subsequent split prime is too large as well; no primality work needed.
        if (prod(primes) * p) ** 2 > max_cells:
            return {"status": "UNRESOLVED_RESOURCE_LIMIT", "attempts": attempts,
                    "prime_limit": prime_limit, "max_cells": max_cells}
        if not prime(p):
            continue
        primes.append(p)
        try:
            graph = gaussian_sieve(tuple(primes), step_squared, max_cells=max_cells)
        except SearchBudgetExceeded:
            return {"status": "UNRESOLVED_RESOURCE_LIMIT", "attempts": attempts,
                    "prime_limit": prime_limit, "max_cells": max_cells}
        proof = analyze_periodic(graph)
        if isinstance(proof, ConfinementCertificate):
            bound = gaussian_bound(tuple(primes), step_squared, proof, max_cells=max_cells)
            return {"status": "CERTIFICATE_FOUND", "rational_primes": primes,
                    "certificate": proof.to_dict(), "bound": bound, "attempts": attempts}
        attempts.append({"rational_primes": list(primes),
                         "witness": verify_translation(graph, proof)})
    return {"status": "UNRESOLVED_PRIME_LIMIT", "attempts": attempts,
            "prime_limit": prime_limit, "max_cells": max_cells}


def certificate_from_dict(data: dict) -> ConfinementCertificate | TranslationWitness:
    """Parse JSON data; verify against a reconstructed graph before use."""
    if not isinstance(data, dict):
        raise CertificateError("Expected a certificate object")
    try:
        if data.get("kind") == "confinement" and set(data) == {"kind", "graph_digest", "potentials"}:
            if not isinstance(data["potentials"], (list, tuple)):
                raise CertificateError("Potential rows must be an array")
            if any(not isinstance(pair, (tuple, list)) or len(pair) != 2
                   for pair in data["potentials"]):
                raise CertificateError("Malformed potential row")
            return ConfinementCertificate(data["graph_digest"],
                tuple((tuple(pair[0]), tuple(pair[1])) for pair in data["potentials"]))
        if data.get("kind") == "translation" and set(data) == {"kind", "graph_digest", "start", "word"}:
            if not isinstance(data["word"], (list, tuple)):
                raise CertificateError("Translation word must be an array")
            return TranslationWitness(data["graph_digest"], tuple(data["start"]),
                                      tuple(tuple(s) for s in data["word"]))
    except (TypeError, KeyError, IndexError) as exc:
        raise CertificateError("Malformed certificate data") from exc
    raise CertificateError("Unknown certificate kind or fields")
