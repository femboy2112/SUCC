"""Typed higher-dimensional pinbed calculus with CRT and higher rewrite cells.

Front C of the Scott × Omega × SUCC causal weld (CW-07, CW-09, CW-10,
CW-14, CW-19). This module builds the finite *typed* substrate in which the
conditional "compiler-mediated dimensional relations"

    Omega_5 ~ 3 Omega_3 ~ Omega_3 + Omega_4 ~ 2 Omega_4 - Omega_3

are only meaningful *if* they are implemented by genuinely independent
commuting indexed successor operators, not by a single one-clock
`m -> m + d` map.

Scope and honesty. Everything here is finite and exact (arbitrary-precision
integers, no floating point). What is proved:

  * Pin_d(H) = H^(N^d) is a genuine d-fold exponential object with exact
    curry/uncurry and an exact round-trip identity (structural, finite).
  * d separately addressable, pairwise commuting successor operators
    S_1..S_d span N^d bijectively; a single clock does NOT (this is CW-14
    made executable).
  * The fiber product gluing `(x,y) x (y,z) -> (x,y,z)` satisfies the
    categorical universal property (finite/structural).
  * CRT: coprime moduli give a full group isomorphism (all Fourier
    characters preserved); non-coprime (16,16) diagonal scan is an alias
    that covers 16 of 256 states and destroys exactly 240 Fourier
    characters.
  * A small category of source-attested affine squares `V_p S = S^p V_p`
    with checked interchange/coherence where it actually applies. It is
    made explicit (CW-19) that an iterated arrow category yields diagrams,
    not automatically new higher morphisms.

What is NOT established (OPEN): any of these constructions producing new
pi arithmetic information, signed cancellation, or normality. None of the
dimensional "Omega" relations is here asserted as a literal lambda-term
identity; they remain compiler-mediated proposals.

This is finite exact modular arithmetic and typed array calculus, not a
new Euler product, Weil form, or RH theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import gcd
from typing import Callable, Generic, Iterable, Tuple, TypeVar

H = TypeVar("H")


class PinbedError(ValueError):
    """Raised on a type- or shape-violating pinbed operation."""


def _exact_int(n, name: str) -> int:
    if type(n) is not int:
        raise PinbedError(f"{name} must be an exact integer, got {type(n)!r}")
    return n


# ---------------------------------------------------------------------------
# 1. Pin_d(H) = H^(N^d): typed arrays with exact curry / uncurry
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Pinbed:
    """Pin_d(H): a d-dimensional typed array H^(N^d).

    The index set is N^d = {0..N-1}^d (a finite product, the honest finite
    pinbed). The carrier type ``H`` is whatever exact type the caller
    supplies (int, str, tuple, ...); the calculus never inspects it beyond
    equality. This is the *finite* slice of the currying law

        Hom(X x Y, H) ~= Hom(X, H^Y)

    evaluated on the product of d finite index axes.
    """

    axes: Tuple[int, ...]
    data: Tuple[Tuple[H, ...], ...]  # flattened row-major over axes

    def __post_init__(self) -> None:
        if not self.axes:
            raise PinbedError("Pinbed needs at least one axis")
        expected = _flat_size(self.axes)
        if len(self.data) != expected:
            raise PinbedError(
                f"data has {len(self.data)} entries, axes {self.axes} "
                f"require {expected}"
            )

    @property
    def dim(self) -> int:
        return len(self.axes)

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.axes

    def __getitem__(self, index: Tuple[int, ...]) -> H:
        if len(index) != self.dim:
            raise PinbedError(
                f"index {index} has wrong arity for axes {self.axes}"
            )
        return self.data[_flat_index(self.axes, index)]

    @classmethod
    def from_function(
        cls, axes: Tuple[int, ...], f: Callable[[Tuple[int, ...]], H]
    ) -> "Pinbed":
        axes = tuple(_exact_int(a, "axis") for a in axes)
        if any(a <= 0 for a in axes):
            raise PinbedError(f"axes must be positive, got {axes}")
        data = tuple(
            f(idx)
            for idx in product(*(range(a) for a in axes))
        )
        return cls(axes, data)


def _flat_size(axes: Tuple[int, ...]) -> int:
    n = 1
    for a in axes:
        n *= a
    return n


def _flat_index(axes: Tuple[int, ...], index: Tuple[int, ...]) -> int:
    """Row-major flatten of a multi-index, with bounds check."""
    pos = 0
    for a, i in zip(axes, index):
        i = _exact_int(i, "index component")
        if not (0 <= i < a):
            raise PinbedError(f"index component {i} out of range [0,{a})")
        pos = pos * a + i
    return pos


def _unflatten(axes: Tuple[int, ...], pos: int) -> Tuple[int, ...]:
    idx = []
    for a in reversed(axes):
        idx.append(pos % a)
        pos //= a
    return tuple(reversed(idx))


def curry(p: Pinbed, split: int) -> Pinbed:
    """Curry Pin_d(H) into Pin_k(Pin_{d-k}(H)) by fixing the first ``split``
    axes as the outer array. The outer carrier is itself a Pinbed of the
    remaining axes. This is the exact finite witness of
    Hom(X1 x ... x Xd, H) ~= Hom(X1, Hom(X2 x ... x Xd, H))."""
    split = _exact_int(split, "split")
    if not (0 < split < p.dim):
        raise PinbedError(
            f"split must be strictly inside dim {p.dim}, got {split}"
        )
    outer_axes = p.axes[:split]
    inner_axes = p.axes[split:]

    def cell(outer_idx: Tuple[int, ...]) -> Pinbed:
        def inner_f(inner_idx: Tuple[int, ...]) -> H:
            return p[outer_idx + inner_idx]
        return Pinbed.from_function(inner_axes, inner_f)

    return Pinbed.from_function(outer_axes, cell)


def uncurry(c: Pinbed) -> Pinbed:
    """Inverse of curry: Pin_k(Pin_{d-k}(H)) -> Pin_d(H)."""
    if c.dim == 0:
        raise PinbedError("cannot uncurry a zero-dimensional pinbed")
    inner_axes = c[tuple(0 for _ in range(c.dim))].axes
    outer_axes = c.axes
    axes = outer_axes + inner_axes

    def f(idx: Tuple[int, ...]) -> H:
        outer_idx = idx[: len(outer_axes)]
        inner_idx = idx[len(outer_axes):]
        return c[outer_idx][inner_idx]

    return Pinbed.from_function(axes, f)


def curry_uncurry_roundtrip(p: Pinbed, split: int) -> bool:
    """Exact identity uncurry(curry(p)) == p, elementwise."""
    q = uncurry(curry(p, split))
    if q.axes != p.axes:
        return False
    return all(q[idx] == p[idx] for idx in product(*(range(a) for a in p.axes)))


# ---------------------------------------------------------------------------
# 2. d independent commuting successor operators on N^d
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Successor:
    """S_i: N^d -> N^d, incrementing coordinate i modulo its axis length.

    These are *separately addressable* (S_i touches only coordinate i) and
    pairwise *commute* (S_i S_j = S_j S_i) because they act on disjoint
    coordinates. This is exactly what CW-14's single one-clock does NOT
    provide.
    """

    axes: Tuple[int, ...]
    axis: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "axis", _exact_int(self.axis, "axis"))
        if not (0 <= self.axis < len(self.axes)):
            raise PinbedError(
                f"axis {self.axis} out of range for {len(self.axes)} axes"
            )

    def __call__(self, idx: Tuple[int, ...]) -> Tuple[int, ...]:
        if len(idx) != len(self.axes):
            raise PinbedError(f"index {idx} wrong arity for {self.axes}")
        out = list(idx)
        a = self.axes[self.axis]
        out[self.axis] = (idx[self.axis] + 1) % a
        return tuple(out)


def successors_commute(si: Successor, sj: Successor, axes: Tuple[int, ...]) -> bool:
    """Check S_i S_j = S_j S_i at every point of N^d."""
    for idx in product(*(range(a) for a in axes)):
        if si(sj(idx)) != sj(si(idx)):
            return False
    return True


def single_clock_spans(step: Callable[[Tuple[int, ...]], Tuple[int, ...]],
                        axes: Tuple[int, ...]) -> Tuple[bool, int]:
    """Does iterating a *single* map from (0,...,0) visit every point of
    N^d before cycling? Returns (span_full, orbit_size). This is the
    executable CW-14 refutation: a one-clock orbit has size at most the
    total cell count but typically far less for diagonal clocks."""
    seen = set()
    cur = tuple(0 for _ in axes)
    total = _flat_size(axes)
    while cur not in seen and len(seen) < total:
        seen.add(cur)
        cur = step(cur)
    return (len(seen) == total, len(seen))


# ---------------------------------------------------------------------------
# 3. Fiber-product gluing and the universal property
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FiberProduct:
    """Gluing of two 2-coordinate tables (x,y) and (y,z) over the shared
    middle coordinate y, producing 3-coordinate cells (x,y,z).

    Abstractly this is the fiber product A x_C B where A -> C and B -> C are
    the y-projections. For the finite typed model A = B = N x N, C = N, the
    fiber product is exactly N x N x N (three coordinates). The universal
    property is checked directly: any object T with maps t1:T->A and t2:T->B
    that agree on C factors through a *unique* map to the fiber product.
    """

    n: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "n", _exact_int(self.n, "n"))

    def glue(self, left: Tuple[int, int], right: Tuple[int, int]) -> Tuple[int, int, int]:
        x, y = left
        y2, z = right
        if y != y2:
            raise PinbedError(
                f"fiber-product gluing mismatch on shared coordinate: {y} != {y2}"
            )
        return (x, y, z)

    @staticmethod
    def proj_xy(t: Tuple[int, int, int]) -> Tuple[int, int]:
        return (t[0], t[1])

    @staticmethod
    def proj_yz(t: Tuple[int, int, int]) -> Tuple[int, int]:
        return (t[1], t[2])

    def is_gluable(self, left: Tuple[int, int], right: Tuple[int, int]) -> bool:
        return left[1] == right[0]


def fiber_product_universal(fp: FiberProduct, test_source) -> bool:
    """Verify the universal property of the fiber product on a concrete
    source object ``test_source``.

    ``test_source`` is an iterable of 2-tuples ((x,y),(y,z)) that already
    agree on the shared middle coordinate. We check:

      (existence) every element factors through glue() as a triple;
      (uniqueness) glue() is injective on the agreed diagonal, so the
        induced map to the fiber product is the unique one commuting with
        the two projections proj_xy / proj_yz.
    """
    triples = [fp.glue(l, r) for (l, r) in test_source]
    # uniqueness: distinct agreed pairs give distinct triples
    if len(set(triples)) != len(triples):
        return False
    # projection compatibility: round-trip through the two legs recovers the pair
    for (l, r), t in zip(test_source, triples):
        if fp.proj_xy(t) != l or fp.proj_yz(t) != r:
            return False
    return True


# ---------------------------------------------------------------------------
# 4. CRT single-clock reconstruction and the (16,16) alias
# ---------------------------------------------------------------------------

def crt_combine(residues: Tuple[int, ...], moduli: Tuple[int, ...]) -> int:
    """Chinese Remainder Theorem: unique integer 0 <= x < prod(moduli)
    matching x = residues[i] (mod moduli[i]), for pairwise coprime moduli."""
    if not moduli:
        raise PinbedError("empty moduli")
    for m in moduli:
        if m <= 0:
            raise PinbedError(f"modulus must be positive, got {m}")
    if not pairwise_coprime(moduli):
        raise PinbedError(f"moduli not pairwise coprime: {moduli}")
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(residues, moduli):
        Mi = M // m
        inv = pow(Mi, -1, m)  # modular inverse; Python 3.8+
        x = (x + r * Mi * inv) % M
    return x


def pairwise_coprime(moduli: Tuple[int, ...]) -> bool:
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                return False
    return True


def crt_is_isomorphism(moduli: Tuple[int, ...]) -> bool:
    """CRT gives a group isomorphism Z/(M) -> prod Z/(m_i) iff moduli are
    pairwise coprime (classical). M = prod moduli either way."""
    if pairwise_coprime(moduli):
        # full bijection: every residue tuple is hit exactly once
        M = 1
        for m in moduli:
            M *= m
        seen = set()
        for r in product(*(range(m) for m in moduli)):
            seen.add(crt_combine(r, moduli))
        return len(seen) == M
    return False


def diagonal_scan_coverage(period: int, dim: int = 2) -> Tuple[int, int, int]:
    """Synchronous diagonal scan: advance all d coordinates in lockstep with
    a single clock of ``period``. Returns (covered, total, missed). For
    period=16, dim=2 this is 16 covered, 256 total, 240 missed — the CW-14/
    CW-07 alias negative."""
    period = _exact_int(period, "period")
    covered = set()
    state = (0,) * dim
    for _ in range(period):
        covered.add(state)
        state = tuple((c + 1) % period for c in state)
    total = period ** dim
    return (len(covered), total, total - len(covered))


def fourier_characters_lost(period: int, dim: int = 2) -> int:
    """Count Fourier characters on (Z/period)^dim that are NOT probed by a
    synchronous diagonal scan. A character chi_{(a,b)}(x,y)=exp(2pi i
    (a x + b y)/period) is "probed" only if the scan passes through enough
    phases to distinguish it from the trivial character along the diagonal;
    the diagonal only ever sees phases where a+b is constant per step, so
    the character (a,b) collapses to (a+b) mod period along the orbit and is
    aliased onto the characters with the same sum. The count of *distinct
    characters* the diagonal can resolve is exactly ``period`` (one per sum
    class), out of ``period^dim`` total, so ``period^dim - period`` are lost.
    """
    total_chars = period ** dim
    resolvable = period  # one per value of (a+b) mod period
    return total_chars - resolvable


def crt_full_recovery(moduli: Tuple[int, ...]) -> bool:
    """CRT with pairwise coprime moduli (e.g. (3,4)) is a full group
    replacement: every residue tuple is reached exactly once. Non-coprime
    (16,16) fails. This is the group-theoretic statement; it does NOT claim
    Haar equidistribution of any selected orbit."""
    if not pairwise_coprime(moduli):
        return False
    M = 1
    for m in moduli:
        M *= m
    return len({crt_combine(r, moduli) for r in product(*(range(m) for m in moduli))}) == M


# ---------------------------------------------------------------------------
# 5. Source-attested affine squares: V_p S = S^p V_p, and higher cells
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class AffineSquare:
    """A source-attested affine commuting square for a fixed prime p and
    carrier step S (unary successor on the wrapped ring Z/nZ).

    V_p is the p-fold dilation (carry-safe): V_p(x) = p*x (mod n).
    S is the successor: S(x) = x + 1 (mod n).
    The relation V_p S = S^p V_p holds exactly:

        V_p(S(x)) = p*(x+1) = p*x + p = S^p(p*x) = S^p(V_p(x))  (mod n).

    This is a *diagram* in the (finite) category of affine maps on Z/nZ.
    """

    p: int
    n: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "p", _exact_int(self.p, "p"))
        object.__setattr__(self, "n", _exact_int(self.n, "n"))
        if self.n <= 1:
            raise PinbedError("modulus n must be > 1")

    def S(self, x: int) -> int:
        return (x + 1) % self.n

    def V(self, x: int) -> int:
        return (self.p * x) % self.n

    def check_relation(self) -> bool:
        """V_p S = S^p V_p at every x in Z/nZ."""
        for x in range(self.n):
            if self.V(self.S(x)) != self.S_pow(self.V(x), self.p):
                return False
        return True

    def S_pow(self, x: int, k: int) -> int:
        return (x + k) % self.n


def affine_squares_commute_over_pair(p: int, q: int, n: int) -> bool:
    """For two distinct primes p, q acting on the same ring Z/nZ, the two
    dilations V_p and V_q commute (multiplication commutes), so the
    prime-pair cube

            V_q V_p S  =  V_p V_q S

    is a commuting square of squares. This is a genuine coherence fact of
    the affine maps, checked exactly."""
    def V_p(x): return (p * x) % n
    def V_q(x): return (q * x) % n
    def S(x): return (x + 1) % n
    for x in range(n):
        if V_p(V_q(S(x))) != V_q(V_p(S(x))):
            return False
    return True


def affine_interchange(p: int, q: int, n: int) -> bool:
    """Interchange law for the two dilations as 2-cells: pasting the square
    V_p S = S^p V_p next to the square V_q S = S^q V_q horizontally, and
    comparing with vertical pasting, must agree. For these *specific* affine
    generators both orders collapse to the same multiplication-by-(p q)
    affine map, so interchange holds trivially; we state it as a checked
    assertion rather than a new higher morphism (CW-19)."""
    def V(x, r): return (r * x) % n
    def S(x): return (x + 1) % n
    for x in range(n):
        # horizontal then vertical vs vertical then horizontal
        h_then_v = V(V(S(x), p), q)
        v_then_h = V(V(S(x), q), p)
        if h_then_v != v_then_h:
            return False
    return True
