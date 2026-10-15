"""Exact-rational complementary Wold shells on the zero-centered SUCC Hilbert carrier.

The real-q dilation U_q is isometric but non-surjective. Its range projections
P_n have exact rational matrix elements. Q_n=P_n-P_(n+1) are orthogonal shells.
This is a Wold realization, NOT an RH / physics theorem.
"""
from __future__ import annotations
from fractions import Fraction as Q


class DualShellError(ValueError):
    pass


def _check_sequence(values: dict[int, Q]) -> dict[int, Q]:
    if type(values) is not dict or len(values) > 10_000:
        raise DualShellError("bounded finite dictionary required")
    result = {}
    for k, v in values.items():
        if type(k) is not int or not 1 <= k <= 100_000:
            raise DualShellError("positive bounded source cell required")
        if type(v) not in (int, Q):
            raise DualShellError("exact rational cell values only")
        if v:
            result[k] = Q(v)
    return result


def weight(k: int) -> Q:
    if type(k) is not int or not 1 <= k <= 100_000:
        raise DualShellError("cell index exceeds budget")
    return Q(1, k * (k + 1))


def inner(f: dict[int, Q], g: dict[int, Q]) -> Q:
    return sum((f[k] * g[k] * weight(k) for k in f.keys() & g.keys()), Q())


def add(f: dict[int, Q], g: dict[int, Q], sign: int = 1) -> dict[int, Q]:
    h = f.copy()
    for k, v in g.items():
        h[k] = h.get(k, Q()) + sign * v
        if h[k] == 0:
            del h[k]
    return h


def project_level(f: dict[int, Q], q: int, level: int) -> dict[int, Q]:
    """P_level = U_q^level (U_q*)^level, no square roots in block averages."""
    source = _check_sequence(f)
    if type(q) is not int or not 2 <= q <= 50:
        raise DualShellError("invalid bounded multiplier")
    if type(level) is not int or not 0 <= level <= 16:
        raise DualShellError("invalid depth")
    if level == 0:
        return source
    m = q ** level
    if m > 100_000:
        raise DualShellError("projection block exceeds budget")
    sums: dict[int, Q] = {}
    for k, v in source.items():
        j = k // m
        if j >= 1:
            sums[j] = sums.get(j, Q()) + weight(k) * v
    out: dict[int, Q] = {}
    for j, weighted_total in sums.items():
        value = m * weighted_total / weight(j)
        if value:
            if m * (j + 1) - 1 > 100_000:
                raise DualShellError("projected support exceeds budget")
            for k in range(m * j, m * (j + 1)):
                out[k] = value
    return out


def decompose_shells(f: dict[int, Q], q: int) -> dict:
    source = _check_sequence(f)
    if type(q) is not int or not 2 <= q <= 50:
        raise DualShellError("invalid dilation")
    if not source:
        return {"depth": 0, "shells": [], "squared_norms": [],
                "source_squared_norm": Q(), "reconstruction_exact": True,
                "orthogonal": True, "Parseval_exact": True, "RH_proved": False}
    power, depth = 1, 0
    while power <= max(source):
        power *= q
        depth += 1
    if power > 100_000 or depth > 16:
        raise DualShellError("excessive observer depth")
    projections = [project_level(source, q, j) for j in range(depth + 1)]
    if projections[-1]:
        raise ArithmeticError("top range did not vanish")
    shells = [add(projections[j], projections[j + 1], -1) for j in range(depth)]
    reconstructed = {}
    for shell in shells:
        reconstructed = add(reconstructed, shell)
    norms = [inner(s, s) for s in shells]
    orthogonal = all(inner(shells[i], shells[j]) == 0
                     for i in range(len(shells)) for j in range(i + 1, len(shells)))
    source_norm = inner(source, source)
    if reconstructed != source or not orthogonal or sum(norms, Q()) != source_norm:
        raise ArithmeticError("dual-shell proof receipt failed")
    return {"depth": depth, "shells": shells, "squared_norms": norms,
            "source_squared_norm": source_norm, "reconstruction_exact": True,
            "orthogonal": True, "Parseval_exact": True,
            "zero_locations_read": False, "RH_proved": False}


def meeting_certificate(f: dict[int, Q], q: int, level: int) -> dict:
    """Finite gluing f = recovered dual shells + unresolved P_level f."""
    source = _check_sequence(f)
    if type(level) is not int or not 0 <= level <= 16:
        raise DualShellError("invalid boundary level")
    projections = [project_level(source, q, j) for j in range(level + 1)]
    resolved = {}
    for j in range(level):
        resolved = add(resolved, add(projections[j], projections[j + 1], -1))
    tail = projections[-1]
    if add(resolved, tail) != source or inner(resolved, tail) != 0:
        raise ArithmeticError("observer boundary fails orthogonal gluing")
    if inner(source, source) != inner(resolved, resolved) + inner(tail, tail):
        raise ArithmeticError("energy receipt failed")
    return {"level": level, "resolved": resolved, "tail": tail,
            "resolved_squared_norm": inner(resolved, resolved),
            "tail_squared_norm": inner(tail, tail),
            "source_squared_norm": inner(source, source),
            "boundary_glued_exactly": True, "tail_proved_zero": not tail,
            "zero_locations_read": False, "RH_proved": False}


def late_hidden_source(q: int, depth: int) -> dict[int, Q]:
    """Nonzero source invisible to all first depth shell observations."""
    if type(q) is not int or not 2 <= q <= 20:
        raise DualShellError("invalid q")
    if type(depth) is not int or not 1 <= depth <= 8:
        raise DualShellError("invalid depth")
    m = q ** depth
    if 2 * m > 100_000:
        raise DualShellError("hidden source exceeds budget")
    return {k: Q(1) for k in range(m, 2 * m)}


def shift_pullback(f: dict[int, Q]) -> dict[int, Q]:
    return {k - 1: v for k, v in _check_sequence(f).items() if k > 1}


def noncommuting_boundary_witness() -> dict:
    f = {2: Q(1)}
    lhs = shift_pullback(project_level(f, 2, 1))
    rhs = project_level(shift_pullback(f), 2, 1)
    comm = add(lhs, rhs, -1)
    if comm.get(1) != Q(2, 3):
        raise ArithmeticError("additive/dilation obstruction changed")
    return {"q": 2, "f_cell": 2, "commutator_at_cell_1": str(comm[1]),
            "naive_additive_gluing_commutes": False,
            "dual_shells_recover_lost_dilation_information": True,
            "zero_locations_read": False, "RH_proved": False}
