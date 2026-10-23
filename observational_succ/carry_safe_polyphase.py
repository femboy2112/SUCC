"""Exact general-radix polyphase SUCC/FUCC algebra (carry-safe observer core).

Scope and provenance
--------------------
The arithmetic *prime* carry layer already exists in
``observational_succ.reciprocal_succ_fucc`` (PR #236): ``residue_clock``,
``from_residue_clock``, ``clock_succ`` and the mixed-radix / adjoint-braid
machinery, all restricted to ``genuine_prime`` moduli. This module does **not**
duplicate it. It adds the *delta* the carry-safe round needs:

  * the **general composite modulus** ``q >= 2`` polyphase decomposition
    ``n = q(m-1) + r + 1`` (CSA-01), its controlled-carry successor, and the
    tensor relabelling ``W_q |n> = |m> ⊗ |r>``;
  * the explicit **residue isometries** ``U_{q,r}`` as exact 0/1 partial
    isometries, with the Cuntz relations ``U_{q,r}^* U_{q,s} = δ_{rs} I`` and
    ``Σ_r U_{q,r} U_{q,r}^* = I`` verified exactly, and the **finite-horizon
    completeness defect** of a finite compression quantified as an exact
    projection (CSA-02);
  * the authentic prime-FUCC embedding ``V_p = U_{p,p-1}`` and the source
    affine braid ``V_p S = S^p V_p`` (CSA-03);
  * the **mixed-radix composition** ``U_{p,r} U_{q,s} = U_{pq, ps+r}`` for
    *arbitrary* (not necessarily coprime, not necessarily prime) moduli, its
    reversed-order form, the explicit digit permutation between conventions,
    and the n-factor little-endian law with associativity (CSA-04).

Ledger discipline
-----------------
``U_{q,r}`` generates a representation of the Cuntz algebra ``O_q`` on the full
``l^2(N_{>=1})``; that the relations below hold on the *infinite* carrier is
CLASSICAL (Cuntz 1977). The contribution here is the **exact one-based
arithmetic realization** and the **exact finite-horizon defect calculus** that
keeps a finite compression from silently inheriting the infinite relation. No
Weil/RH positivity, no physical observer realization, and no CRT decomposition
for non-coprime moduli is asserted anywhere.

All arithmetic is exact (int / Fraction); no float is ever used as evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import prod
from typing import Mapping

from observational_succ.reciprocal_succ_fucc import (
    ReciprocalSourceError,
    from_residue_clock,
    genuine_prime,
    residue_clock,
)


class PolyphaseError(ValueError):
    """Wrong modulus, residue, dimension, or a violated carry contract."""


def _integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise PolyphaseError(f"exact integer >= {minimum} required, got {x!r}")
    return x


def _modulus(q):
    if type(q) is not int or q < 2:
        raise PolyphaseError("radix modulus q >= 2 required")
    return q


def _residue(r, q):
    _modulus(q)
    if type(r) is not int or not 0 <= r < q:
        raise PolyphaseError(f"residue in [0,{q}) required, got {r!r}")
    return r


# ---------------------------------------------------------------------------
# CSA-01 : general-radix polyphase coordinates and controlled-carry successor
# ---------------------------------------------------------------------------

def polyphase_coords(n, q):
    """One-based decomposition n = q(m-1) + r + 1, returning (m, r).

    m = floor((n-1)/q) + 1 >= 1 is the quotient block; r = (n-1) mod q is the
    residue. For a genuine prime modulus this agrees with
    ``reciprocal_succ_fucc.residue_clock`` (asserted in the tests).
    """
    _integer(n, 1)
    _modulus(q)
    return ((n - 1) // q + 1, (n - 1) % q)


def from_polyphase_coords(m, r, q):
    """Inverse of :func:`polyphase_coords`: n = q(m-1) + r + 1."""
    _integer(m, 1)
    _residue(r, q)
    return q * (m - 1) + r + 1


def polyphase_succ(m, r, q):
    """The controlled-carry automaton for the global successor S.

    (m, r) -> (m, r+1) if r < q-1, else (m+1, 0). This is exactly one additive
    successor n -> n+1 in coordinates, carry included.
    """
    _integer(m, 1)
    _residue(r, q)
    return (m, r + 1) if r < q - 1 else (m + 1, 0)


def carry_successor_holds(n, q):
    """CSA-01 check: coords(n+1) equals the carry automaton applied to coords(n).

    Returns True; raises if the carry boundary is wrong (origin and first wrap
    included when iterated from n=1).
    """
    m, r = polyphase_coords(n, q)
    advanced = polyphase_succ(m, r, q)
    if polyphase_coords(n + 1, q) != advanced:
        raise PolyphaseError(f"carry mismatch at n={n}, q={q}")
    if from_polyphase_coords(*advanced, q) != n + 1:
        raise PolyphaseError(f"carry does not reconstruct n+1 at n={n}, q={q}")
    return True


@dataclass(frozen=True)
class TensorUnitary:
    """W_q on a finite prefix {1..N}: n |-> (m, r), m in [1..M], r in [0..q).

    Flattened tensor index (m-1)*q + r + 1 equals n, so W_q is the identity
    permutation under the natural flattening; its non-trivial content is that
    the successor S becomes the carry automaton. ``onto`` records whether the
    prefix is a clean multiple of q (no partial final block).
    """

    q: int
    prefix: int          # N
    blocks: int          # M = ceil(N / q)
    onto: bool           # True iff N == q*M (no horizon slack)
    unhit: tuple         # tensor slots (m, r) with 1<=index<=q*M but > N


def tensor_unitary(N, q):
    """Build W_q over the prefix {1..N} and certify it is an isometry.

    When N is a multiple of q the map is a bijection onto {1..M} x {0..q-1}
    (an exact unitary). Otherwise the final block is partial: W_q is an
    isometry whose range misses ``unhit`` tensor slots (a horizon defect).
    """
    _integer(N, 1)
    _modulus(q)
    M = (N + q - 1) // q
    forward = {n: polyphase_coords(n, q) for n in range(1, N + 1)}
    # injectivity + residue/block ranges
    images = set(forward.values())
    if len(images) != N:
        raise PolyphaseError("W_q is not injective on the prefix (bug)")
    full = {(m, r) for m in range(1, M + 1) for r in range(q)}
    unhit = tuple(sorted(full - images))
    onto = not unhit
    if onto and N != q * M:
        raise PolyphaseError("onto/defect bookkeeping disagreement")
    return TensorUnitary(q, N, M, onto, unhit)


# ---------------------------------------------------------------------------
# exact 0/1 partial isometries (columns carry weight 1; adjoint, compose)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PartialIsometry:
    """A 0/1 partial isometry: column (source basis) -> row (target basis).

    ``cols[j] = i`` means the operator sends |j> to |i> (weight 1); columns not
    present map to 0. Columns are orthonormal iff the targets are distinct,
    which is enforced at construction, so U^*U = I on the stored domain.
    """

    cols: Mapping[int, int]

    def __post_init__(self):
        if type(self.cols) is not dict:
            object.__setattr__(self, "cols", dict(self.cols))
        for j, i in self.cols.items():
            if type(j) is not int or j < 1 or type(i) is not int or i < 1:
                raise PolyphaseError("partial isometry uses 1-based int indices")
        if len(set(self.cols.values())) != len(self.cols):
            raise PolyphaseError("non-orthonormal columns (repeated target)")

    def apply(self, j):
        """U|j> as a target index, or None if |j> is outside the domain."""
        return self.cols.get(j)

    def adjoint(self):
        """U^* : row -> column (well defined since targets are distinct)."""
        return PartialIsometry({i: j for j, i in self.cols.items()})

    def compose(self, other):
        """self ∘ other : (other first, then self). Exact partial composition."""
        if type(other) is not PartialIsometry:
            raise PolyphaseError("can only compose PartialIsometry")
        out = {}
        for j, mid in other.cols.items():
            tgt = self.cols.get(mid)
            if tgt is not None:
                out[j] = tgt
        return PartialIsometry(out)

    def gram_is_identity_on(self, domain):
        """U^*U = I on ``domain`` (every listed column is present)."""
        return all(j in self.cols for j in domain)

    def range_support(self):
        return frozenset(self.cols.values())


# ---------------------------------------------------------------------------
# CSA-02 : residue isometries U_{q,r} and the Cuntz relations
# ---------------------------------------------------------------------------

def u_image(n, q, r):
    """U_{q,r} |n> = |q(n-1) + r + 1> (closed form, the source-coordinate map)."""
    _integer(n, 1)
    _residue(r, q)
    return q * (n - 1) + r + 1


def residue_isometry(q, r, source_dim):
    """Exact U_{q,r} on the source prefix {1..source_dim}.

    Targets land in {1..q*source_dim}; the operator is a genuine isometry
    (orthonormal columns) by construction.
    """
    _residue(r, q)
    _integer(source_dim, 1)
    return PartialIsometry({n: u_image(n, q, r) for n in range(1, source_dim + 1)})


@dataclass(frozen=True)
class CuntzDefect:
    """Exact finite-compression report for the residue family {U_{q,r}}.

    ``isometry_exact`` : U_{q,r}^* U_{q,s} = δ_{rs} I held for every r,s.
    ``clean`` : the completeness relation Σ_r U_{q,r} U_{q,r}^* = I held exactly.
    ``defect_rank`` : rank of I - Σ_r U_{q,r} U_{q,r}^* on the target prefix.
    ``defect_support`` : the target indices the completeness relation misses.
    """

    q: int
    source_dim: int
    target_dim: int
    isometry_exact: bool
    clean: bool
    defect_rank: int
    defect_support: tuple


def cuntz_relations(q, source_dim, target_dim=None):
    """Verify the Cuntz relations for {U_{q,r}} and quantify the horizon defect.

    * Isometry / orthogonality: U_{q,r}^* U_{q,s} = δ_{rs} I on {1..source_dim}
      is EXACT and carries no horizon defect (checked directly).
    * Completeness: Σ_r U_{q,r} U_{q,r}^* projects onto {1..q*source_dim}.
      On a target prefix of dimension target_dim >= q*source_dim the defect is
      the exact projection onto {q*source_dim + 1 .. target_dim}, of rank
      target_dim - q*source_dim. When target_dim == q*source_dim the defect is
      zero (the finite compression already satisfies the infinite relation).
    """
    _modulus(q)
    _integer(source_dim, 1)
    if target_dim is None:
        target_dim = q * source_dim
    _integer(target_dim, 1)
    if target_dim < q * source_dim:
        raise PolyphaseError("target prefix too small to hold all U_{q,r} images")
    isos = [residue_isometry(q, r, source_dim) for r in range(q)]
    domain = range(1, source_dim + 1)

    # U_{q,r}^* U_{q,s} = δ_{rs} I  (exact, no horizon defect)
    isometry_exact = True
    for r in range(q):
        for s in range(q):
            comp = isos[r].adjoint().compose(isos[s])  # U_r^* U_s
            if r == s:
                if not comp.gram_is_identity_on(domain) or len(comp.cols) != source_dim:
                    isometry_exact = False
            else:
                if comp.cols:  # must be the zero operator
                    isometry_exact = False

    # Σ_r U_{q,r} U_{q,r}^* projects onto the union of ranges
    covered = set()
    for r in range(q):
        covered |= set(isos[r].range_support())
    expected = set(range(1, q * source_dim + 1))
    if covered != expected:
        raise PolyphaseError("range union is not the clean prefix {1..q*source_dim}")
    defect_support = tuple(range(q * source_dim + 1, target_dim + 1))
    defect_rank = len(defect_support)
    clean = defect_rank == 0
    return CuntzDefect(q, source_dim, target_dim, isometry_exact, clean,
                       defect_rank, defect_support)


# ---------------------------------------------------------------------------
# CSA-03 : authentic prime-FUCC embedding V_p = U_{p,p-1}
# ---------------------------------------------------------------------------

def prime_fucc_embedding(p, dim):
    """Certify V_p = U_{p,p-1} and the braid V_p S = S^p V_p on {1..dim}.

    The terminal residue p-1 is essential for the one-based convention:
    u_image(n, p, p-1) = p*n exactly. Returns a dict of exact checks; raises on
    any failure. A composite ``p`` is rejected (genuine prime passport).
    """
    genuine_prime(p)
    _integer(dim, 1)
    # V_p = U_{p,p-1}
    embedding = all(u_image(n, p, p - 1) == p * n for n in range(1, dim + 1))
    # V_p S = S^p V_p on basis:  V_p S|n> = |p(n+1)> = |pn+p> = S^p V_p|n>
    braid = all(p * (n + 1) == p * n + p for n in range(1, dim + 1))
    # cross-check against the prime residue clock: block q, residue p-1
    clock = all(residue_clock(p * n, p) == (n, p - 1) for n in range(1, dim + 1))
    inverse_clock = all(from_residue_clock(n, p - 1, p) == p * n
                        for n in range(1, dim + 1))
    if not (embedding and braid and clock and inverse_clock):
        raise PolyphaseError("prime-FUCC embedding/braid failed (bug)")
    return {"V_p=U_{p,p-1}": embedding, "V_pS=S^pV_p": braid,
            "residue_clock_terminal": clock, "inverse_clock": inverse_clock}


# ---------------------------------------------------------------------------
# CSA-04 : mixed-radix composition for arbitrary moduli
# ---------------------------------------------------------------------------

def mixed_radix_compose(factors):
    """U_{q1,r1} U_{q2,r2} ... U_{qk,rk} = U_{Q, R} (little-endian mixed radix).

    ``factors`` is a sequence of (q_i, r_i) applied left-to-right as operator
    composition. Returns (Q, R) with Q = prod q_i and
    R = sum_i r_i * prod_{j<i} q_j, the composed modulus and residue. Moduli
    need NOT be prime or coprime.
    """
    factors = tuple(factors)
    if not factors:
        raise PolyphaseError("at least one (q, r) factor required")
    Qtot = 1
    R = 0
    for q, r in factors:
        _residue(r, q)
        R += r * Qtot        # prod of earlier moduli is current Qtot
        Qtot *= q
    return Qtot, R


def two_factor_compose(p, r, q, s):
    """U_{p,r} U_{q,s} = U_{pq, ps+r}; returns (pq, ps+r). r in [0,p), s in [0,q)."""
    _residue(r, p)
    _residue(s, q)
    return p * q, p * s + r


def reversed_two_factor(p, r, q, s):
    """U_{q,s} U_{p,r} = U_{qp, qr+s}; returns (qp, qr+s)."""
    _residue(r, p)
    _residue(s, q)
    return q * p, q * r + s


def digit_convention_permutation(p, q):
    """The bijection {0..p-1}x{0..q-1} -> {0..pq-1} comparison of both orders.

    Returns a dict mapping (r, s) -> (forward, reversed) where
    forward = ps + r  (digit of U_{p,r}U_{q,s}) and
    reversed = qr + s  (digit of U_{q,s}U_{p,r}). Both are bijections onto
    {0..pq-1}; they coincide iff p == q == 1 (excluded) -- i.e. composition
    order genuinely matters. This is NOT a CRT isomorphism unless gcd(p,q)=1,
    and even then the two orderings differ.
    """
    _modulus(p)
    _modulus(q)
    out = {}
    for r in range(p):
        for s in range(q):
            out[(r, s)] = (p * s + r, q * r + s)
    fwd = {v[0] for v in out.values()}
    rev = {v[1] for v in out.values()}
    if fwd != set(range(p * q)) or rev != set(range(p * q)):
        raise PolyphaseError("a mixed-radix digit convention was not a bijection")
    return out


def is_crt_decomposition(p, q):
    """Honest flag: the pair (p,q) supports a CRT split iff gcd(p,q)=1.

    Mixed-radix reordering is a base change, never a CRT decomposition for
    non-coprime moduli. Returns (coprime, note).
    """
    from math import gcd
    _modulus(p)
    _modulus(q)
    coprime = gcd(p, q) == 1
    note = ("coprime: a CRT iso Z/pq ~ Z/p x Z/q exists, but still differs "
            "from the mixed-radix digit order" if coprime else
            "NOT coprime: no CRT split; mixed radix is a base change only")
    return coprime, note


# ---------------------------------------------------------------------------
# independent reference oracle (second blind route for the closed forms)
# ---------------------------------------------------------------------------

def compose_on_basis(factors, n):
    """Apply U_{q1,r1} ... U_{qk,rk} to |n> by literal successive u_image.

    Independent of :func:`mixed_radix_compose`; the tests require
    compose_on_basis(factors, n) == u_image(n, *mixed_radix_compose(factors)).
    """
    _integer(n, 1)
    factors = tuple(factors)
    # apply right-most factor first (operator composition order)
    value = n
    for q, r in reversed(factors):
        value = u_image(value, q, r)
    return value


def closed_form_matches(factors, dim):
    """Check the mixed-radix closed form against the literal basis action."""
    Qtot, R = mixed_radix_compose(factors)
    return all(compose_on_basis(factors, n) == u_image(n, Qtot, R)
               for n in range(1, dim + 1))
