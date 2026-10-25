"""Seinfeld SUCC: exact zero witnesses, inverse fibers, and source falsifiers.

This is a finite/exact mathematics lab, not a randomness or normality theorem.
A witness's formal provenance is retained separately from its evaluation.
No floats, assumptions about Galois independence, or pi-digit inputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, isqrt
from typing import Callable, Mapping


class NullSourceError(ValueError):
    """Invalid arithmetic scope or an attempted quotient without its witness."""


def _nat(n: int, lower: int = 0) -> int:
    if type(n) is not int or n < lower:
        raise NullSourceError(f"integer >= {lower} required")
    return n


def _rational(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise NullSourceError("integer/Fraction required; no floats")
    return Q(x)


@dataclass(frozen=True)
class ZeroWitness:
    """A formal linear relation, NOT its scalar value.

    A relation may evaluate to zero while its formal support is nonempty.
    Terms can be combined/cancelled ONLY by explicit formal operations.
    """
    name: str
    terms: tuple[tuple[str, Q], ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise NullSourceError("witness must have a provenance name")
        for key, coefficient in self.terms:
            if not isinstance(key, str) or not key:
                raise NullSourceError("nonempty formal generator label required")
            _rational(coefficient)

    def coefficients(self) -> dict[str, Q]:
        out: dict[str, Q] = {}
        for name, value in self.terms:
            out[name] = out.get(name, Q()) + _rational(value)
        return {name: value for name, value in sorted(out.items()) if value}

    def evaluate(self, values: Mapping[str, int | Q]) -> Q:
        coefficients = self.coefficients()
        if not coefficients.keys() <= values.keys():
            raise NullSourceError("missing declared source generator")
        return sum((coeff * _rational(values[name])
                    for name, coeff in coefficients.items()), Q())

    def scaled(self, factor: int | Q, label: str) -> ZeroWitness:
        c = _rational(factor)
        return ZeroWitness(label, tuple((name, c * value) for name, value in self.terms))

    def plus(self, other: ZeroWitness, label: str) -> ZeroWitness:
        return ZeroWitness(label, self.terms + other.terms)


def step_witness(n: int) -> ZeroWitness:
    """E_n=U_n-16 U_(n-1)-r_n, retaining three named source generators."""
    _nat(n, 1)
    return ZeroWitness(f"step@{n}", ((f"U:{n}", Q(1)),
                                      (f"U:{n-1}", Q(-16)),
                                      (f"r:{n}", Q(-1))))


def macro_witness(start: int, length: int) -> ZeroWitness:
    """A k-step zero E_(n,k), valid as a relation for ANY forcing."""
    _nat(start); _nat(length, 1)
    k = length
    return ZeroWitness(f"macro@{start}+{k}",
                       ((f"U:{start+k}", Q(1)),
                        (f"U:{start}", Q(-16**k))) +
                       tuple((f"r:{start+j}", Q(-16**(k-j)))
                             for j in range(1, k + 1)))


def telescope_witness(start: int, length: int) -> tuple[ZeroWitness, ZeroWitness]:
    """Formal syzygy: E_(n,k)=sum_j 16^(k-j) E_(n+j), not independent laws."""
    macro = macro_witness(start, length)
    rhs = ZeroWitness(f"step-combination@{start}+{length}", ())
    for j in range(1, length + 1):
        rhs = rhs.plus(step_witness(start + j).scaled(16**(length-j), f"step-term:{j}"),
                       f"partial:{start}:{j}")
    if macro.coefficients() != rhs.coefficients():
        raise ArithmeticError("noncommuting source square / missing carry")
    return macro, rhs


def rational_rank(matrix: tuple[tuple[int | Q, ...], ...]) -> int:
    """Exact Q-Gaussian elimination. Fixed rectangular domain, no tolerance."""
    if not matrix:
        return 0
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise NullSourceError("nonempty rectangular coefficient matrix required")
    a = [[_rational(value) for value in row] for row in matrix]
    pivot_row = 0
    for col in range(width):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [v / scale for v in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                c = a[i][col]
                a[i] = [v - c*w for v, w in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def recurrence_rank_receipt(depth: int) -> dict[str, int]:
    """Macro zeros add no rank; anchoring U0 raises rank from N to N+1.

    This is the coefficient matrix on (U0,...,UN) with forcing specified.
    """
    _nat(depth, 1)
    if depth > 64:
        raise NullSourceError("finite exact rank probe capped at 64 steps")
    steps = []
    for n in range(1, depth + 1):
        row = [0] * (depth + 1)
        row[n-1], row[n] = -16, 1
        steps.append(tuple(row))
    macro = []
    for k in range(2, depth + 1):
        row = [0] * (depth + 1)
        row[0], row[k] = -16**k, 1
        macro.append(tuple(row))
    anchor = (1,) + (0,) * depth
    return {"depth": depth, "step_rank": rational_rank(tuple(steps)),
            "with_macro_rank": rational_rank(tuple(steps + macro)),
            "with_anchor_rank": rational_rank(tuple(steps + macro + [anchor]))}


def bbp_forcing(n: int) -> Q:
    """Original signed four-pole BBP forcing, no pi-digit oracle."""
    _nat(n, 1)
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def source_states(depth: int, forcing: Callable[[int], Q] = bbp_forcing) -> tuple[Q, ...]:
    _nat(depth)
    u = [Q()]
    for n in range(1, depth + 1):
        f = _rational(forcing(n))
        u.append(16*u[-1]+f)
    return tuple(u)


def source_values(depth: int, forcing: Callable[[int], Q] = bbp_forcing) -> dict[str, Q]:
    states = source_states(depth, forcing)
    result = {f"U:{n}": states[n] for n in range(depth+1)}
    result.update({f"r:{n}": _rational(forcing(n)) for n in range(1, depth+1)})
    return result


def _frac_part(y: int | Q) -> Q:
    return _rational(y) % 1


def circle_backward_fiber(target: int | Q, forcing_steps: tuple[Q, ...]) -> tuple[Q, ...]:
    """Exactly 16^k predecessors in T for a specified k-step forcing history.

    Returns sorted fractions in [0,1). Limit depth to keep the lab finite.
    """
    k = len(forcing_steps)
    if not 1 <= k <= 4:
        raise NullSourceError("1..4 actual forcing transitions required")
    terms = tuple(_rational(f) for f in forcing_steps)
    accumulated = sum((16**(k-j) * f for j, f in enumerate(terms, 1)), Q())
    target = _frac_part(target)
    return tuple(sorted(((target-accumulated+j)/16**k) % 1
                        for j in range(16**k)))


def odd_torsion_inverse(target: int | Q, forcing: int | Q) -> Q:
    """The unique inverse of x->16x+forcing on odd-denominator Q/Z.

    Rejects non-source-typed even denominators rather than choosing one of
    sixteen arbitrary circle inverses.
    """
    y, f = _frac_part(target), _rational(forcing)
    if y.denominator % 2 == 0 or f.denominator % 2 == 0:
        raise NullSourceError("target and forcing must be odd-torsion rationals")
    z = (y-f) % 1
    if z == 0:
        return Q()
    a, q = z.numerator, z.denominator
    return Q((a*pow(16, -1, q)) % q, q)


def backward_odd_history(target: int | Q, forcing_steps: tuple[Q, ...]) -> tuple[Q, ...]:
    """Chronological unique odd-torsion history from known final phase."""
    if not forcing_steps:
        raise NullSourceError("at least one source transition is required")
    current = _frac_part(target)
    history = [current]
    for f in reversed(forcing_steps):
        current = odd_torsion_inverse(current, f)
        history.append(current)
    return tuple(reversed(history))


def inverse_discontinuity(k: int) -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    """Targets 1/(16k±1)->0 but their odd inverses ->1/16,15/16."""
    _nat(k, 1)
    q_minus, q_plus = 16*k-1, 16*k+1
    return ((Q(1,q_minus), odd_torsion_inverse(Q(1,q_minus), 0)),
            (Q(1,q_plus), odd_torsion_inverse(Q(1,q_plus), 0)))


def _prime(p: int) -> int:
    _nat(p, 2)
    if any(p%d == 0 for d in range(2, isqrt(p)+1)):
        raise NullSourceError("prime characteristic required, not composite")
    return p


def frobenius_carry(p: int, x: int | Q, y: int | Q) -> Q:
    """C_p(x,y)=((x+y)^p-x^p-y^p)/p via *integral* binomial coefficients."""
    _prime(p)
    x, y = _rational(x), _rational(y)
    return sum((Q(comb(p,j)//p)*x**j*y**(p-j) for j in range(1,p)), Q())


def frobenius_relation(p: int, x: int | Q, y: int | Q) -> dict[str, Q | bool]:
    """Integer/rational Frobenius zero and typed permission to reduce mod p."""
    p = _prime(p)
    x, y = _rational(x), _rational(y)
    c = frobenius_carry(p,x,y)
    residual = (x+y)**p - x**p - y**p - p*c
    return {"zero": residual, "carry": c,
            "p_integral": x.denominator % p != 0 and y.denominator % p != 0}


def bbp_frobenius_relation(n: int, p: int) -> dict[str, Q | bool]:
    _nat(n, 1)
    prev = source_states(n-1)[-1]
    return frobenius_relation(p, 16*prev, bbp_forcing(n))


def counterfeit_tail(n: int) -> Q:
    """Positive odd-denominator T_n = 1/[(8n+1)(8n+3)]."""
    _nat(n)
    return Q(1, (8*n+1)*(8*n+3))


def counterfeit_forcing(n: int) -> Q:
    """Different FOUR-pole positive forcing, asymptotic 15/(64n^2)."""
    _nat(n, 1)
    return 16*counterfeit_tail(n-1) - counterfeit_tail(n)


def counterfeit_closed_state(n: int) -> Q:
    """U*_n=16^n/3-T_n, anchored zero; alpha*=1/3 is base-16 periodic."""
    _nat(n)
    return Q(16**n,3)-counterfeit_tail(n)


def counterfeit_phase(n: int) -> Q:
    _nat(n, 1)
    return counterfeit_closed_state(n) % 1


def counterfeit_is_confined(n: int) -> bool:
    """Every n>=1 phase lies in (1/4,1/3); an exact nonnormal witness."""
    return Q(1,4) < counterfeit_phase(_nat(n,1)) < Q(1,3)

# A second, categorical kind of zero: a nonzero path chain with zero boundary.
# Distinct parallel edges retain their source labels.  This is elementary graph
# homology / exact cochains, not a physical quantum superposition.
Edge = tuple[str, int, int]  # ('S', source, 1) or ('V', source, prime)


def edge_endpoints(edge: Edge) -> tuple[int, int]:
    kind, source, modulus = edge
    _nat(source, 1)
    if kind == 'S' and modulus == 1:
        return source, source + 1
    if kind == 'V':
        return source, source * _prime(modulus)
    raise NullSourceError("invalid labelled successor or primitive prime edge")


def affine_null_loop(n: int, p: int) -> dict[Edge, int]:
    """Nonzero 1-cycle: S then Vp minus Vp then p times S.

    Its boundary is identically zero but its labelled edges are retained.
    """
    _nat(n, 1); _prime(p)
    result: dict[Edge, int] = {}
    route_a = [(('S', n, 1), 1), (('V', n+1, p), 1)]
    route_b = [(('V', n, p), -1)] + [(('S', p*n+j, 1), -1) for j in range(p)]
    for edge, sign in route_a + route_b:
        result[edge] = result.get(edge, 0) + sign
    return {edge: c for edge, c in result.items() if c}


def chain_boundary(chain: Mapping[Edge, int | Q]) -> dict[int, Q]:
    """Exact boundary ∂(source->target)=target-source."""
    out: dict[int, Q] = {}
    for edge, coefficient in chain.items():
        a, b = edge_endpoints(edge)
        c = _rational(coefficient)
        out[a] = out.get(a, Q()) - c
        out[b] = out.get(b, Q()) + c
    return {node: c for node,c in sorted(out.items()) if c}


def chain_holonomy(chain: Mapping[Edge, int | Q],
                   weights: Mapping[Edge, int | Q]) -> Q:
    """1-cochain pairing: a zero boundary need not have zero edge holonomy."""
    if not chain.keys() <= weights.keys():
        raise NullSourceError("all labelled edge transports must be supplied")
    return sum((_rational(c)*_rational(weights[e]) for e,c in chain.items()),Q())


def gradient_transport(chain: Mapping[Edge,int | Q], potential: Mapping[int,int | Q]) -> Q:
    """Exact potential differences have zero circulation on every 1-cycle."""
    weights = {}
    for edge in chain:
        a,b = edge_endpoints(edge)
        if a not in potential or b not in potential:
            raise NullSourceError("missing genuine source potential value")
        weights[edge] = _rational(potential[b])-_rational(potential[a])
    return chain_holonomy(chain,weights)
