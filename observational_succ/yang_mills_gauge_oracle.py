"""Finite exact gauge-observation and scale-gap controls for SUCC.

Z/qZ lattice gauge fields and S3 two-loop controls are *toy models*.
They are NOT a reproduction of OpenAI's 4D compact-simple-group Lean proof,
not an Osterwalder--Schrader reconstruction, and not a YM mass-gap proof.
No floats, random sources, or external theorem admissions confer authority.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations, product


class GaugeOracleError(ValueError):
    """Malformed state or invalid observer/carrier contract."""


def _int(x, lower=0):
    if type(x) is not int or x < lower:
        raise GaugeOracleError(f"expected exact integer >= {lower}")
    return x


@dataclass(frozen=True)
class AbelianGaugeGraph:
    """Connected oriented finite graph, link values in Z/qZ.

    Gauge convention: A_(u,v) -> A_(u,v) + phi(u)-phi(v) (mod q).
    Canonical zero-tree gauge and chord coordinates are exact orbit classifiers.
    No nonabelian compact-simple-group claim follows from this example.
    """
    vertices: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    q: int

    def __post_init__(self):
        _int(self.q, 2)
        if (type(self.vertices) is not tuple or len(self.vertices) < 1
                or not all(isinstance(v, str) and v for v in self.vertices)
                or len(set(self.vertices)) != len(self.vertices)):
            raise GaugeOracleError("vertices must be distinct named sites")
        if type(self.edges) is not tuple:
            raise GaugeOracleError("edge list must be a tuple")
        v = set(self.vertices)
        if any(type(e) is not tuple or len(e) != 2 or
               any(type(x) is not str or x not in v for x in e) or e[0] == e[1] for e in self.edges):
            raise GaugeOracleError("edges require two distinct declared vertices")
        if len(self.tree()) != len(self.vertices) - 1:
            raise GaugeOracleError("graph must be connected")

    def tree(self) -> tuple[tuple[str, str, int, int], ...]:
        """Breadth-first rooted spanning tree: parent, child, index, orientation sign."""
        neighbors = {v: [] for v in self.vertices}
        for i, (u, v) in enumerate(self.edges):
            neighbors[u].append((v, i, 1))
            neighbors[v].append((u, i, -1))
        seen = {self.vertices[0]}
        queue = deque([self.vertices[0]])
        result = []
        while queue:
            u = queue.popleft()
            for v, i, sign in neighbors[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
                    result.append((u, v, i, sign))
        return tuple(result)

    def _links(self, links: tuple[int, ...]) -> tuple[int, ...]:
        if (type(links) is not tuple or len(links) != len(self.edges) or
                any(type(a) is not int or not 0 <= a < self.q for a in links)):
            raise GaugeOracleError("full canonical Z/qZ link array required")
        return links

    def transform(self, links: tuple[int, ...], phi: tuple[int, ...]) -> tuple[int, ...]:
        self._links(links)
        if (type(phi) is not tuple or len(phi) != len(self.vertices) or
                any(type(a) is not int or not 0 <= a < self.q for a in phi)):
            raise GaugeOracleError("full canonical gauge potential required")
        pot = dict(zip(self.vertices, phi))
        return tuple((a + pot[u] - pot[v]) % self.q
                     for a, (u, v) in zip(links, self.edges))

    def canonical(self, links: tuple[int, ...]) -> tuple[int, ...]:
        self._links(links)
        phi = {self.vertices[0]: 0}
        for parent, child, idx, sign in self.tree():
            phi[child] = (phi[parent] + sign * links[idx]) % self.q
        return self.transform(links, tuple(phi[v] for v in self.vertices))

    def holonomies(self, links: tuple[int, ...]) -> tuple[int, ...]:
        """Wilson chord values: complete invariant of this finite abelian orbit."""
        canon = self.canonical(links)
        tree_indices = {i for _, _, i, _ in self.tree()}
        return tuple(canon[i] for i in range(len(self.edges)) if i not in tree_indices)

    def orbit_equal(self, left: tuple[int, ...], right: tuple[int, ...]) -> bool:
        return self.holonomies(left) == self.holonomies(right)

    @property
    def cycle_rank(self):
        return len(self.edges) - len(self.vertices) + 1

    @property
    def orbit_count(self):
        return self.q ** self.cycle_rank

    @property
    def orbit_size(self):
        return self.q ** (len(self.vertices) - 1)


def wilson_orbit_energy(graph: AbelianGaugeGraph, samples: tuple[tuple[int, ...], ...]) -> Q:
    """Exact finite-Haar energy on the ABELIAN gauge-orbit quotient.

    If the quotient has M=q^b elements and c_h is each measured orbit count,
    E=M * sum(c_h^2)/N^2 - 1 = sum_(nonzero k)|Fourier(mu)(k)|^2.
    This is a distributional uniformity functional, NOT a gauge-state mass gap.
    """
    if not isinstance(graph, AbelianGaugeGraph) or type(samples) is not tuple or not samples:
        raise GaugeOracleError("require nonempty exact family of gauge states")
    counts = {}
    for state in samples:
        h = graph.holonomies(state)
        counts[h] = counts.get(h, 0) + 1
    n = len(samples)
    value = Q(graph.orbit_count * sum(c*c for c in counts.values()), n*n) - 1
    if value < 0:
        raise ArithmeticError("finite Plancherel energy cannot be negative")
    return value


Site = tuple[int, int, int, int]


@dataclass(frozen=True)
class Torus4D:
    """Oriented periodic 4D Z/qZ Wilson lattice; NO continuum limit."""
    side: int
    q: int

    def __post_init__(self):
        _int(self.side, 2)
        _int(self.q, 2)

    @property
    def sites(self) -> tuple[Site, ...]:
        return tuple(product(range(self.side), repeat=4))

    @property
    def link_count(self):
        return 4 * self.side ** 4

    @property
    def plaquette_count(self):
        return 6 * self.side ** 4

    def _site(self, site: Site):
        if (type(site) is not tuple or len(site) != 4 or
                any(type(x) is not int or not 0 <= x < self.side for x in site)):
            raise GaugeOracleError("site outside finite four-torus")
        return site

    def step(self, site: Site, axis: int) -> Site:
        self._site(site)
        if type(axis) is not int or not 0 <= axis < 4:
            raise GaugeOracleError("axis must be 0..3")
        out = list(site)
        out[axis] = (out[axis] + 1) % self.side
        return tuple(out)

    def index(self, site: Site, axis: int) -> int:
        self._site(site)
        if type(axis) is not int or not 0 <= axis < 4:
            raise GaugeOracleError("axis must be 0..3")
        flat = 0
        for x in site:
            flat = flat * self.side + x
        return 4 * flat + axis

    def _links(self, links: tuple[int, ...]) -> tuple[int, ...]:
        if (type(links) is not tuple or len(links) != self.link_count or
                any(type(x) is not int or not 0 <= x < self.q for x in links)):
            raise GaugeOracleError("incomplete or out-of-range 4D link array")
        return links

    def zero(self) -> tuple[int, ...]:
        return (0,) * self.link_count

    def transform(self, links: tuple[int, ...], phi: tuple[int, ...]) -> tuple[int, ...]:
        self._links(links)
        if (type(phi) is not tuple or len(phi) != self.side ** 4 or
                any(type(x) is not int or not 0 <= x < self.q for x in phi)):
            raise GaugeOracleError("full exact 4D gauge field required")
        def read(x):
            return phi[self.index(x, 0) // 4]
        out = list(links)
        for site in self.sites:
            for a in range(4):
                i = self.index(site, a)
                out[i] = (links[i] + read(site) - read(self.step(site, a))) % self.q
        return tuple(out)

    def plaquette(self, links: tuple[int, ...], site: Site, a: int, b: int) -> int:
        self._links(links)
        if not (type(a) is int and type(b) is int and 0 <= a < b < 4):
            raise GaugeOracleError("ordered axes 0<=a<b<4 required")
        return (links[self.index(site, a)] + links[self.index(self.step(site, a), b)]
                - links[self.index(self.step(site, b), a)] - links[self.index(site, b)]) % self.q

    def curvature_signature(self, links: tuple[int, ...]) -> tuple[int, ...]:
        self._links(links)
        return tuple(self.plaquette(links, x, a, b)
                     for x in self.sites for a, b in combinations(range(4), 2))

    def cube_bianchi(self, links: tuple[int, ...], site: Site, a: int, b: int, c: int) -> int:
        """Discrete dF=0 on each 3-face, an exact mod-q consequence d^2=0."""
        self._links(links)
        if not (type(a) is int and type(b) is int and type(c) is int and 0 <= a < b < c < 4):
            raise GaugeOracleError("require ordered cube axes 0<=a<b<c<4")
        f = self.plaquette
        return (f(links, self.step(site, a), b, c) - f(links, site, b, c)
                - f(links, self.step(site, b), a, c) + f(links, site, a, c)
                + f(links, self.step(site, c), a, b) - f(links, site, a, b)) % self.q

    def wilson_cycle(self, links: tuple[int, ...], site: Site, axis: int) -> int:
        """Noncontractible Wilson angle, invariant under exact local gauge maps."""
        self._links(links)
        x = self._site(site)
        total = 0
        for _ in range(self.side):
            total += links[self.index(x, axis)]
            x = self.step(x, axis)
        return total % self.q

    def flat_nontrivial(self) -> tuple[int, ...]:
        """Curvature 0 but cycle holonomy 1; not gauge equivalent to zero."""
        out = list(self.zero())
        for x in self.sites:
            if x[0] == self.side-1:
                out[self.index(x, 0)] = 1
        return tuple(out)


def two_state_reflection_eigenvalues(w0: Q, w1: Q) -> tuple[Q, Q]:
    """Eigenvalues of q=2 kernel K(u,v)=w(u-v): (w0+w1,w0-w1).

    PSD iff w0>=abs(w1). This tests ONE finite reflection-like kernel,
    not the complete Osterwalder--Schrader axioms of four-dimensional YM.
    """
    if type(w0) is not Q or type(w1) is not Q:
        raise GaugeOracleError("exact Fraction weights required")
    return w0+w1, w0-w1


def transfer_spectral_ratio(a: Q, scaling: str = "quadratic") -> Q:
    """Exact ratio lambda-/lambda+ of 2x2 positive transfer matrix.

    quadratic: off-diagonal epsilon=a^2: normalized physical mass vanishes.
    linear: off-diagonal epsilon=a/4: normalized physical mass stays positive.
    """
    if type(a) is not Q or not 0 < a <= 1:
        raise GaugeOracleError("require exact physical mesh a in (0,1]")
    if scaling == "quadratic":
        eps = a*a
    elif scaling == "linear":
        eps = a/4
    else:
        raise GaugeOracleError("undeclared coupling schedule")
    if not 0 < eps < 1:
        raise GaugeOracleError("need strictly positive finite transfer eigenvalues")
    plus, minus = two_state_reflection_eigenvalues(Q(1), eps)
    return minus / plus


def gap_lower_from_ratio(a: Q, ratio: Q) -> Q:
    """Physical -log(ratio)/a >= (1-ratio)/a, exact rational bound."""
    if type(a) is not Q or type(ratio) is not Q or not 0 < a <= 1 or not 0 < ratio < 1:
        raise GaugeOracleError("require exact mesh and positive ratio below one")
    return (1-ratio)/a


def quadratic_mass_upper(a: Q) -> Q:
    """For r=(1-a^2)/(1+a^2), 0 < -log(r)/a <= 2a/(1-a^4)."""
    if type(a) is not Q or not 0 < a < 1:
        raise GaugeOracleError("strict fractional mesh 0<a<1 required")
    return 2*a/(1-a**4)


def finite_cutoff_twins(n: int, observed_through: int = 8) -> tuple[Q, Q]:
    """Exact matching at all observed n<=K, different continuum spectral gaps.

    (A) epsilon=a^2 for all n;
    (B) epsilon=a^2 through K, then epsilon=a/4 for n>K.
    Both retain strictly positive finite transfer eigenvalues for n>=2.
    """
    _int(n, 2)
    _int(observed_through, 2)
    a = Q(1,n)
    return transfer_spectral_ratio(a, "quadratic"), transfer_spectral_ratio(
        a, "quadratic" if n <= observed_through else "linear")


S3 = tuple[int, int, int]


def compose_s3(a: S3, b: S3) -> S3:
    if (type(a) is not tuple or type(b) is not tuple or len(a) != 3
            or len(b) != 3 or any(type(x) is not int for x in a+b)
            or set(a) != {0,1,2} or set(b) != {0,1,2}):
        raise GaugeOracleError("permutations of exactly three sites required")
    return tuple(a[b[i]] for i in range(3))


def trace_s3(a: S3) -> int:
    if (type(a) is not tuple or len(a) != 3 or
            any(type(x) is not int for x in a) or set(a) != {0,1,2}):
        raise GaugeOracleError("S3 permutation required")
    return sum(a[i] == i for i in range(3))


def nonabelian_trace_counterexample() -> dict[str, int]:
    """Individual trace channels fail to separate two-loop simultaneous conjugacy.

    For nonabelian S3, (a,a) and (a,b) have same individual traces (1,1),
    but trace(ab) differs (3 vs 0). A model control, not SU(2) proof.
    """
    a = (1,0,2)  # transposition (0 1)
    b = (0,2,1)  # transposition (1 2)
    return {
        "trace_first": trace_s3(a),
        "trace_second_control": trace_s3(a),
        "trace_second_other": trace_s3(b),
        "trace_product_control": trace_s3(compose_s3(a,a)),
        "trace_product_other": trace_s3(compose_s3(a,b)),
    }


S3_ID: S3 = (0, 1, 2)
S3_ELEMENTS: tuple[S3, ...] = tuple(permutations(range(3)))


def inverse_s3(g: S3) -> S3:
    trace_s3(g)  # validates exact permutation without accepting a surrogate
    return tuple(g.index(i) for i in range(3))


def conjugate_s3(h: S3, g: S3) -> S3:
    return compose_s3(compose_s3(h, g), inverse_s3(h))


@dataclass(frozen=True)
class S3GaugeGraph:
    """Finite genuinely nonabelian gauge quotient, not SU(2) Yang--Mills.

    A link transforms as U_(u,v) -> g(u) U_(u,v) g(v)^(-1).
    After fixing a rooted spanning tree, chords classify orbits only UP TO
    a single, simultaneous conjugation by the residual root gauge element.
    """
    vertices: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]

    def __post_init__(self):
        AbelianGaugeGraph(self.vertices, self.edges, 2)  # topology validation ONLY

    def _tree(self):
        return AbelianGaugeGraph(self.vertices, self.edges, 2).tree()

    def _links(self, links):
        if type(links) is not tuple or len(links) != len(self.edges):
            raise GaugeOracleError("complete finite S3 link tuple required")
        for g in links:
            trace_s3(g)
        return links

    def transform(self, links: tuple[S3, ...], phi: tuple[S3, ...]) -> tuple[S3, ...]:
        self._links(links)
        if type(phi) is not tuple or len(phi) != len(self.vertices):
            raise GaugeOracleError("full finite S3 gauge tuple required")
        for g in phi:
            trace_s3(g)
        pot = dict(zip(self.vertices, phi))
        return tuple(compose_s3(compose_s3(pot[u], a), inverse_s3(pot[v]))
                     for a, (u, v) in zip(links, self.edges))

    def canonical_tree(self, links: tuple[S3, ...]) -> tuple[S3, ...]:
        self._links(links)
        phi = {self.vertices[0]: S3_ID}
        for parent, child, idx, sign in self._tree():
            step = links[idx] if sign == 1 else inverse_s3(links[idx])
            phi[child] = compose_s3(phi[parent], step)
        result = self.transform(links, tuple(phi[v] for v in self.vertices))
        if any(result[idx] != S3_ID for _, _, idx, _ in self._tree()):
            raise ArithmeticError("nonabelian tree gauge did not vanish")
        return result

    def chords(self, links: tuple[S3, ...]) -> tuple[S3, ...]:
        result = self.canonical_tree(links)
        tree_indices = {i for _, _, i, _ in self._tree()}
        return tuple(result[i] for i in range(len(self.edges)) if i not in tree_indices)

    def orbit_key(self, links: tuple[S3, ...]) -> tuple[S3, ...]:
        """Complete simultaneous-conjugation invariant, not separate traces."""
        words = self.chords(links)
        return min(tuple(conjugate_s3(g, w) for w in words) for g in S3_ELEMENTS)

    def orbit_equal(self, a: tuple[S3, ...], b: tuple[S3, ...]) -> bool:
        return self.orbit_key(a) == self.orbit_key(b)


def s3_subdivision_square(a: S3, b: S3,
                          g_u: S3, g_mid: S3, g_v: S3) -> dict[str, S3 | bool]:
    """Single-edge two-step coarse holonomy commutes with arbitrary site gauge.

    Correct oriented transport is a*b.  The internal vertex cancels exactly:
    (g_u*a*g_mid^-1)(g_mid*b*g_v^-1)=g_u*(a*b)*g_v^-1.
    This is a finite graph-subdivision naturality theorem, not physical RG.
    """
    for x in (a,b,g_u,g_mid,g_v):
        trace_s3(x)
    coarse = compose_s3(a,b)
    first = compose_s3(compose_s3(g_u,a),inverse_s3(g_mid))
    second = compose_s3(compose_s3(g_mid,b),inverse_s3(g_v))
    through_refinement = compose_s3(first,second)
    direct = compose_s3(compose_s3(g_u,coarse),inverse_s3(g_v))
    if through_refinement != direct:
        raise ArithmeticError("gauge transport and source-preserving coarse path differ")
    return {"coarse":coarse,"transported_coarse":direct,
            "through_refinement":through_refinement,"commutes":True}
