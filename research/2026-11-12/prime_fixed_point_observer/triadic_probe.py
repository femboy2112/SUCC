"""Finite exact controls for triangular transport and anchored contraction.

Run from any directory; the only output is a JSON receipt on stdout.  A U(1)
phase is explicitly assigned to each oriented edge.  These phases are model
data, not inferred physical phases or automatic attributes of prime labels.
The finite checks below accompany the separate proofs in TRIADIC_TRANSPORT.md.
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def incidence(u, v, w):
    """Rows encode u*x1-x2, v*x2-x3, w*x3-x1; det=uvw-1."""
    return sp.Matrix([[u, -1, 0], [0, v, -1], [-1, 0, w]])


def boundary(u, v, w):
    """Vertex-by-edge convention of the proof note: transported edge currents."""
    return sp.Matrix([[-1, 0, w], [u, -1, 0], [0, v, -1]])


def triangle_receipt() -> dict:
    u, v, w = sp.symbols("u v w", nonzero=True)
    g1, g2, g3 = sp.symbols("g1 g2 g3", nonzero=True)
    symbolic = incidence(u, v, w)
    require(sp.expand(symbolic.det() - (u*v*w - 1)) == 0,
            "twisted determinant sign")
    require(sp.expand(boundary(u, v, w).det() - (u*v*w - 1)) == 0,
            "boundary convention has the same determinant")
    gauged = incidence(g2*u/g1, g3*v/g2, g1*w/g3)
    require(sp.simplify((g2*u/g1)*(g3*v/g2)*(g1*w/g3) - u*v*w) == 0,
            "symbolic holonomy gauge invariance")
    require(sp.simplify(gauged * sp.diag(g1, g2, g3) -
                        sp.diag(g2, g3, g1) * symbolic) == sp.zeros(3),
            "incidence gauge covariance")

    roots = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
    flat_count = nonflat_count = 0
    for phases in product(roots, repeat=3):
        matrix = incidence(*phases)
        holonomy = sp.simplify(sp.prod(phases))
        edge_boundary = boundary(*phases)
        require(matrix == -sp.diag(*phases) * edge_boundary.H,
                "unitary vertex/edge transport conventions agree")
        gram = edge_boundary.H * edge_boundary
        require(sp.simplify(gram.det() - (holonomy-1)*sp.conjugate(holonomy-1)) == 0,
                "edge Laplacian determinant is the squared loop defect")
        require(sp.simplify(matrix.det() - holonomy + 1) == 0,
                "finite twisted determinant")
        kernel = matrix.nullspace()
        if holonomy == 1:
            flat_count += 1
            expected = sp.Matrix([1, phases[0], phases[0]*phases[1]])
            require(matrix.rank() == 2 and len(kernel) == 1,
                    "flat triangle has one-dimensional kernel")
            require(matrix * expected == sp.zeros(3, 1),
                    "flat transported vector")
            require(sp.simplify(kernel[0] - kernel[0][0]*expected) == sp.zeros(3, 1),
                    "computed kernel has the transported span")
        else:
            nonflat_count += 1
            require(matrix.rank() == 3 and not kernel,
                    "nontrivial holonomy destroys the fixed vector")

    for gauges in product(roots, repeat=3):
        a, b, c = gauges
        pure = tuple(sp.simplify(phase) for phase in (b/a, c/b, a/c))
        require(sp.prod(pure) == 1 and incidence(*pure).rank() == 2,
                "pure gauge is flat")

    # If the direct chord is defined to equal the composite path, reversing
    # that chord supplies its inverse: the resulting triangle is flat by
    # construction.  An independent chord can supply extra holonomy data.
    for a, b in product(roots, repeat=2):
        chord = a*b
        require(sp.simplify(a*b/chord) == 1,
                "composed chord must have trivial holonomy")
        require(incidence(a, b, 1/chord).rank() == 2,
                "composed-chord triangle has its fixed vector")

    examples = []
    for phases in ((1, 1, 1), (1, 1, -1), (sp.I, 1, 1), (-1, sp.I, sp.I)):
        matrix = incidence(*phases)
        holonomy = sp.simplify(sp.prod(phases))
        examples.append({
            "phases": [str(value) for value in phases],
            "holonomy": str(holonomy),
            "determinant": str(sp.simplify(matrix.det())),
            "rank": matrix.rank(),
            "kernel_dimension": len(matrix.nullspace()),
        })
    return {
        "orientation": "1->2->3->1; rows u*x1-x2, v*x2-x3, w*x3-x1",
        "symbolic_determinant": "u*v*w - 1",
        "symbolic_gauge_covariance": True,
        "boundary_and_vertex_conventions_checked": True,
        "edge_gram_determinant": "abs(holonomy - 1)**2",
        "phase_banks_checked": flat_count + nonflat_count,
        "flat_banks": flat_count,
        "nonflat_banks": nonflat_count,
        "pure_gauge_banks_checked": len(roots)**3,
        "composed_chords_checked": len(roots)**2,
        "examples": examples,
    }


def omega(n: int) -> int:
    """Elementary multiplicity count for the declared finite positive labels."""
    count, divisor = 0, 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            n //= divisor
            count += 1
        divisor += 1
    return count + int(n > 1)


def prime_graph_receipt(limit: int = 500) -> dict:
    primes = (2, 3, 5, 7)
    require(all(sp.isprime(p) for p in primes), "prime edge labels")
    edges = [(n, p*n, p) for p in primes for n in range(1, limit//p + 1)]
    for a, b, p in edges:
        require(omega(b) == omega(a) + 1, "prime edge changes multiplicity by one")
        require((omega(a) - omega(b)) % 2 == 1, "prime-edge bipartite coloring")
    square = (1, 2, 6, 3, 1)
    square_labels = (2, 3, 2, 3)
    for a, b, p in zip(square, square[1:], square_labels):
        require(max(a, b) == p*min(a, b), "square edge has its authentic prime ratio")
    require(omega(1) % 2 == omega(6) % 2 == 0 and
            omega(2) % 2 == omega(3) % 2 == 1,
            "square alternates the parity coloring")
    return {
        "maximum_label": limit,
        "prime_multipliers": list(primes),
        "edges_checked": len(edges),
        "all_edges_flip_Omega_parity": True,
        "square_vertices": list(square),
        "square_prime_labels": list(square_labels),
        "square_Omega_parities": [omega(n) % 2 for n in square],
        "mixed_triangle_vertices": [1, 2, 3, 1],
        "mixed_triangle_edges": ["S", "S", "V_3^*"],
        "scope": "A triangle uses additive edges; the prime-multiplication graph is bipartite.",
    }


def anchored_word(d: int, n: int | None, repetitions: int = 1) -> int | None:
    """Evaluate (V_d^* S^(d-1))^r on a basis label; None denotes the zero vector."""
    for _ in range(repetitions):
        if n is None:
            return None
        shifted = n + d - 1
        n = shifted // d if shifted % d == 0 else None
    return n


def anchored_formula(d: int, n: int, repetitions: int = 1) -> int | None:
    scale = d**repetitions
    return 1 + (n - 1)//scale if (n - 1) % scale == 0 else None


def anchor_receipt() -> dict:
    cases = 0
    witnesses = []
    for d in range(2, 8):
        for repetitions in range(1, 5):
            require(anchored_word(d, 1, repetitions) == 1, "the unit is fixed")
            witness = 1 + d**repetitions
            require(anchored_word(d, witness, repetitions) == 2,
                    "operator norm error has an exact unit-vector witness")
            witnesses.append({"d": d, "power": repetitions,
                              "input": witness, "output": 2, "E11_output": 0})
            for n in range(1, 501):
                require(anchored_word(d, n, repetitions) ==
                        anchored_formula(d, n, repetitions),
                        "word agrees with shifted divisibility")
                cases += 1
    for n in range(1, 501):
        require(anchored_word(2, anchored_word(3, n)) == anchored_word(6, n),
                "A2*A3=A6")
        require(anchored_word(3, anchored_word(2, n)) == anchored_word(6, n),
                "A3*A2=A6")
    return {
        "definition": "A_d=V_d^* S^(d-1)",
        "basis_cases_checked": cases,
        "d_range": [2, 7], "label_range": [1, 500], "power_range": [1, 4],
        "A2_A3_and_A3_A2_equal_A6_cases": 500,
        "unit_fixed_for_every_checked_d_and_power": True,
        "norm_error_one_witnesses": witnesses,
        "scope": "Finite exact word controls; global fixed-space and strong-limit proofs are separate.",
    }


def counterfeit_receipt() -> dict:
    def f(n):
        return 7 if n == 5 else 5 if n == 7 else n

    def multiplier(d, n):
        return f(d*f(n))

    def multiplier_adjoint(d, n):
        source = f(n)
        return f(source//d) if source % d == 0 else None

    def mixed_adjoint(d, n):
        # B_d^*=(S^*)^(d-1) V_d^f, with the unilateral boundary retained.
        if n is None:
            return None
        shifted = multiplier(d, n) - (d - 1)
        return shifted if shifted >= 1 else None

    require(all(f(n) == n for n in (1, 2, 3)), "local anchors survive the relabeling")
    require(all(f(f(n)) == n for n in range(1, 501)), "counterfeit is an involution")
    require(multiplier_adjoint(2, 2) == multiplier_adjoint(3, 3) == 1,
            "both mixed unit loops survive")
    left = multiplier(2, 4 + 1)
    right = multiplier(2, 4) + 2
    require((left, right) == (14, 10), "authentic successor braid fails at label four")
    mixed = mixed_adjoint(3, mixed_adjoint(2, 3))
    direct = mixed_adjoint(6, 3)
    require((mixed, direct) == (19, 13),
            "third-route coherence detects the transported mixed inconsistency")
    return {
        "permutation": "(5 7)", "fixed_local_labels": [1, 2, 3],
        "transported_multiplier": "V_d^f=U_f V_d U_f^*",
        "A2f_e1": 1, "A3f_e1": 1,
        "braid_input": 4, "V2f_S_output": left, "S_squared_V2f_output": right,
        "B2_B3_adjoint_input": 3, "B2_B3_adjoint_output": mixed,
        "B6_adjoint_output": direct,
        "mixed_definition": "B_d=(V_d^f)^* S^(d-1); (B2 B3)^*=B3^* B2^*",
        "conclusion": "Local triangle closure alone does not certify the ordinary source braid.",
    }


def run_probe() -> dict:
    return {
        "schema": "succ-triadic-transport-probe-v1",
        "status": "PASS: finite exact controls",
        "triangle": triangle_receipt(),
        "prime_graph": prime_graph_receipt(),
        "anchored_contraction": anchor_receipt(),
        "counterfeit": counterfeit_receipt(),
    }


if __name__ == "__main__":
    print(json.dumps(run_probe(), indent=2, sort_keys=True))
