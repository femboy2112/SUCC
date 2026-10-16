"""A bounded rational experiment: coordinate observations and Schur envelopes.

The matrices define whole finite models. No matrix is identified with Suzuki's
source. Exact receipts instantiate the paper rules OD-01--04; finite searches
never prove a universally quantified candidate. See OBSERVER_DISCOVERY_EXPERIMENT.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product as cartesian
import json

from .minimal_observation import (
    FiniteObservation, compile_factorization, replay_factorization,
)
from .recursive_operator_gluing import matrix, psd


class DiscoveryError(ValueError):
    pass


def _digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                             default=str).encode()).hexdigest()


def _axes(axes):
    if (type(axes) is not tuple or not 1 <= len(axes) <= 4 or
            any(type(a) is not str or not a.strip() for a in axes) or
            len(set(axes)) != len(axes)):
        raise DiscoveryError("Declare 1..4 distinct ordered coordinate names")


@dataclass(frozen=True)
class RationalForm:
    """A whole symmetric form over Q, also interpreted on R in the paper.

    Coordinates are Euclidean orthonormal. A digest binds this actual matrix,
    basis, source name and epoch; it does not authenticate an external source.
    """
    source_id: str
    epoch: int
    axes: tuple[str, ...]
    coefficients: tuple[tuple[Q, ...], ...]

    def __post_init__(self):
        _axes(self.axes)
        if (type(self.source_id) is not str or not self.source_id.strip() or
                type(self.epoch) is not int or self.epoch < 0):
            raise DiscoveryError("Declare source identity and nonnegative integer epoch")
        n = len(self.axes)
        if (type(self.coefficients) is not tuple or len(self.coefficients) != n or
                any(type(r) is not tuple or len(r) != n for r in self.coefficients)):
            raise DiscoveryError("Whole square form required")
        if any(type(v) not in (int, Q) for row in self.coefficients for v in row):
            raise DiscoveryError("Exact integer/Fraction entries only")
        a = matrix(self.coefficients)
        if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
            raise DiscoveryError("Real symmetric form required")
        object.__setattr__(self, "coefficients", a)

    @property
    def digest(self):
        return _digest((self.source_id, self.epoch, self.axes, self.coefficients))

    def energy(self, vector):
        if (type(vector) is not tuple or len(vector) != len(self.axes) or
                any(type(x) not in (int, Q) for x in vector)):
            raise DiscoveryError("Exact vector in the declared coordinate carrier required")
        return sum((vector[i]*self.coefficients[i][j]*vector[j]
                    for i in range(len(vector)) for j in range(len(vector))), Q())


@dataclass(frozen=True)
class CoordinateObservation:
    form_digest: str
    retained_axes: tuple[str, ...]

    def __post_init__(self):
        _axes(self.retained_axes)
        if (type(self.form_digest) is not str or len(self.form_digest) != 64 or
                any(c not in "0123456789abcdef" for c in self.form_digest)):
            raise DiscoveryError("Exact source form digest required")

    @classmethod
    def on(cls, form, retained_axes):
        if type(form) is not RationalForm:
            raise DiscoveryError("A rational source form is required")
        observation = cls(form.digest, retained_axes)
        observation.positions(form)
        return observation

    def positions(self, form):
        if type(form) is not RationalForm or self.form_digest != form.digest:
            raise DiscoveryError("SOURCE_MISMATCH: observation belongs to another full form")
        if any(a not in form.axes for a in self.retained_axes):
            raise DiscoveryError("Observation reads an unrepresented coordinate")
        positions = tuple(form.axes.index(a) for a in self.retained_axes)
        if positions != tuple(sorted(positions)):
            raise DiscoveryError("Coordinate coarsening must preserve the declared basis order")
        return positions


def _solve(a, c):
    """Exact Gauss-Jordan range test; free coordinates set to zero, no inverse."""
    n, width = len(a), len(c[0])
    rows = [list(a[i]) + list(c[i]) for i in range(n)]
    pivots, r = [], 0
    for col in range(n):
        pivot = next((i for i in range(r, n) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        divisor = rows[r][col]
        rows[r] = [v/divisor for v in rows[r]]
        for i in range(n):
            if i != r:
                factor = rows[i][col]
                rows[i] = [v-factor*w for v, w in zip(rows[i], rows[r])]
        pivots.append(col)
        r += 1
    if any(any(row[n:]) for row in rows[r:]):
        raise DiscoveryError("RANGE_CONDITION_FAILED: D X = C has no solution")
    result = [[Q() for _ in range(width)] for _ in range(n)]
    for i, col in enumerate(pivots):
        result[col] = rows[i][n:]
    return tuple(tuple(row) for row in result)


@dataclass(frozen=True)
class EnvelopeCertificate:
    observation: CoordinateObservation
    response: tuple[tuple[Q, ...], ...]
    result: RationalForm
    authority: str = "EXACT_FINITE_CHECK"
    rule: str = "OD-01"


def _blocks(form, observation):
    if type(observation) is not CoordinateObservation:
        raise DiscoveryError("Typed coordinate observation required")
    low = observation.positions(form)
    high = tuple(i for i in range(len(form.axes)) if i not in low)
    a = tuple(tuple(form.coefficients[i][j] for j in low) for i in low)
    d = tuple(tuple(form.coefficients[i][j] for j in high) for i in high)
    c = tuple(tuple(form.coefficients[i][j] for j in low) for i in high)
    return a, d, c


def schur_envelope(form, observation):
    """Finite quadratic envelope only: check D >= 0 and solve D X = C.

    Singular valid blocks are allowed. Refusal does NOT identify every fiber's
    infimum with -infinity; that requires a fiber-specific witness.
    """
    a, d, c = _blocks(form, observation)
    if d and not psd(d):
        raise DiscoveryError("HIGH_PSD_FAILED: finite envelope rule unavailable")
    response = _solve(d, c) if d else ()
    short = tuple(tuple(a[i][j] - sum((c[k][i]*response[k][j]
                                      for k in range(len(d))), Q())
                        for j in range(len(a))) for i in range(len(a)))
    result = RationalForm(form.source_id, form.epoch, observation.retained_axes, short)
    certificate = EnvelopeCertificate(observation, response, result)
    if not replay_envelope(form, certificate):
        raise ArithmeticError("Produced an invalid finite envelope certificate")
    return certificate


def replay_envelope(form, certificate):
    """Check DX=C and S=A-X'DX without re-running the producer's solve.

    This is exact algebra for the whole declared finite form, not Lean replay
    or source authentication. The all-vector consequence uses paper OD-01.
    """
    if (type(certificate) is not EnvelopeCertificate or
            certificate.authority != "EXACT_FINITE_CHECK" or certificate.rule != "OD-01"):
        return False
    try:
        a, d, c = _blocks(form, certificate.observation)
        out, x = certificate.result, certificate.response
        if (type(out) is not RationalForm or
                (out.source_id, out.epoch, out.axes) !=
                (form.source_id, form.epoch, certificate.observation.retained_axes)):
            return False
        if (type(x) is not tuple or len(x) != len(d) or
                any(type(row) is not tuple or len(row) != len(a) or
                    any(type(v) not in (int, Q) for v in row) for row in x)):
            return False
        if d and not psd(d):
            return False
        for k in range(len(d)):
            for j in range(len(a)):
                if sum((d[k][l]*x[l][j] for l in range(len(d))), Q()) != c[k][j]:
                    return False
        return all(out.coefficients[i][j] == a[i][j] -
                   sum((x[k][i]*d[k][l]*x[l][j]
                        for k in range(len(d)) for l in range(len(d))), Q())
                   for i in range(len(a)) for j in range(len(a)))
    except (DiscoveryError, TypeError, AttributeError):
        return False


def nested_envelope(form, fine_axes, coarse_axes):
    """Generate envelope(envelope(form, fine), coarse) and the direct route."""
    first = schur_envelope(form, CoordinateObservation.on(form, fine_axes))
    second = schur_envelope(first.result, CoordinateObservation.on(first.result, coarse_axes))
    direct = schur_envelope(form, CoordinateObservation.on(form, coarse_axes))
    if direct.result != second.result:
        raise ArithmeticError("Nested envelope identity failed")
    return {"source_digest": form.digest, "first": first, "second": second,
            "direct": direct, "equal": True, "authority": "EXACT_FINITE_CHECK",
            "paper_rule": "OD-02", "external_source_identified": False,
            "dependency_graph": (
                {"node": "fine", "rule": "OD-01", "input": form.digest,
                 "output": first.result.digest, "depends_on": ()},
                {"node": "coarse-after-fine", "rule": "OD-01",
                 "input": first.result.digest, "output": second.result.digest,
                 "depends_on": ("fine",)},
                {"node": "coarse-direct", "rule": "OD-01", "input": form.digest,
                 "output": direct.result.digest, "depends_on": ()},
                {"node": "nested-identity", "rule": "OD-02",
                 "depends_on": ("coarse-after-fine", "coarse-direct")})}


_RULES = {
    "OD-01": (
        "finite Schur envelope by completed square",
        ("real symmetric finite source form in an orthonormal basis",
         "D is positive semidefinite", "D X = C for every low column"),
        "inf_y Q(x,y) = x'(A-X'DX)x; a minimizer is y=-Xx"),
    "OD-02": (
        "compatible nested envelopes associate",
        ("same source form and nested coordinate observations",
         "both staged eliminated blocks are positive semidefinite",
         "both staged cross-column range equations have solutions"),
        "Schur_coarse(Schur_fine(G)) = Schur_coarse(G)"),
    "OD-03": (
        "extended-real nested infima associate",
        ("one fixed real-valued source function on a nonempty product fiber",
         "nested observations identify the SAME union of source fibers",
         "use extended-real infima, never subtract infinity"),
        "inf_(y,z) q(x,y,z) = inf_y inf_z q(x,y,z)"),
    "OD-04": (
        "joint probe minimality from complete tables and ablation pairs",
        ("entire declared finite source is enumerated",
         "only deterministic functions of the declared menu are allowed",
         "all subsets of the declared menu are tested; ablation alone proves only irredundancy"),
        "minimum cardinality among the declared fixed probe subsets is certified"),
}


def conditional_rule(rule_id):
    """A predeclared paper theorem schema; no input can erase its hypotheses."""
    if type(rule_id) is not str or rule_id not in _RULES:
        raise DiscoveryError("Unknown conditional proof rule")
    name, hypotheses, conclusion = _RULES[rule_id]
    return {"rule": rule_id, "name": name, "retained_hypotheses": hypotheses,
            "conclusion": conclusion, "recorded_authority": "PAPER_PROVED",
            "proof_location": "research/2026-10-16/OBSERVER_DISCOVERY_EXPERIMENT.md#" + rule_id.lower(),
            "runtime_issued_universal_proof": False, "Lean_kernel_replayed": False,
            "external_source_identified": False,
            "outstanding_application_obligations": (
                "identify the actual target/source with these declared finite objects",
                "supply and replay every retained hypothesis on that application") +
                (("extended-real infima are a paper rule, not a matrix output in this grammar",)
                 if rule_id == "OD-03" else ())}


def joint_probe_minima(problem, menu):
    """Exhaust the <=8-probe powerset on <=64 source states, reusing coimages.

    Report minimum cardinality and all inclusion-minimal sufficient subsets.
    These are different notions; no adaptive worst-case optimum is asserted.
    """
    if (type(problem) is not FiniteObservation or len(problem.target) > 64 or
            type(menu) is not tuple or len(menu) > 8):
        raise DiscoveryError("Whole source <=64 states and menu <=8 probes required")
    for row in menu:
        FiniteObservation(problem.source_id, problem.epoch, row, problem.target,
                          problem.laws, problem.proof_theory, problem.cost_model)
    rows, sufficient, certificates = [], [], {}
    for size in range(len(menu)+1):
        for subset in combinations(range(len(menu)), size):
            observations = tuple(tuple(menu[j][s] for j in subset)
                                 for s in range(len(problem.target)))
            p = FiniteObservation(problem.source_id, problem.epoch, observations, problem.target,
                                  problem.laws, problem.proof_theory, problem.cost_model)
            certificate = compile_factorization(p)
            if not replay_factorization(p, certificate):
                raise ArithmeticError("Inherited coimage certificate failed independent replay")
            rows.append({"subset": subset, "problem_digest": p.digest,
                         "certificate": asdict(certificate)})
            certificates[subset] = certificate
            if certificate.outcome == "PROVEN_FACTORIZATION":
                sufficient.append(subset)
    minimal = tuple(s for s in sufficient if not any(set(t) < set(s) for t in sufficient))
    lower_bounds = []
    for subset in minimal:
        for j in subset:
            reduced = tuple(k for k in subset if k != j)
            pair = certificates[reduced].collision
            if pair is None:
                raise ArithmeticError("Missing indispensable-probe collision")
            lower_bounds.append({"subset": subset, "removed_probe": j, "source_pair": pair,
                                 "target_values": tuple(problem.target[s] for s in pair)})
    minimum = min(map(len, sufficient)) if sufficient else None
    return {"source_digest": problem.digest, "menu_digest": _digest(menu),
            "authority": "EXACT_FINITE_CHECK", "rule": "OD-04",
            "outcome": "PROVEN_MINIMUM_IN_POWERSET" if sufficient else "PROVEN_JOINT_OBSTRUCTION",
            "minimum_cardinality": minimum,
            "minimum_subsets": tuple(s for s in sufficient if len(s) == minimum),
            "inclusion_minimal_subsets": minimal, "ablation_pairs": lower_bounds,
            "all_subset_receipts": rows, "adaptive_optimality_claimed": False,
            "external_source_identified": False}


FALSE_CANDIDATES = (
    ("ZERO_HIDDEN_ENERGY_IMPLIES_FACTORIZATION", ("D=0",)),
    ("POSITIVE_DIAGONAL_BLOCKS_IMPLIES_POSITIVE_SHORT", ("A>0", "D>0")),
    ("COMPRESSION_EQUALS_ENVELOPE", ("D>0",)),
    ("COARSENING_PRESERVES_FINE_ENVELOPE_VALUE", ("fine observation is identity", "D>0")),
    ("SINGULAR_PSD_ALONE_ENSURES_FINITE_ENVELOPE", ("D=0>=0",)),
)


def _counterexample(candidate, a, b, d):
    form = RationalForm("declared-rational-countermodel", 0, ("x", "y"), ((a, b), (b, d)))
    if candidate in (FALSE_CANDIDATES[0][0], FALSE_CANDIDATES[4][0]):
        if d != 0 or b == 0:
            return None
        if candidate == FALSE_CANDIDATES[0][0]:
            return {"form": asdict(form), "vectors": ((1, 0), (1, 1)),
                    "energies": (a, a+2*b), "observation": "x",
                    "hidden_kernel_energy": 0}
        return {"form": asdict(form), "fiber_x": 1, "ray_y": -1 if b > 0 else 1,
                "energy_along_ray": {"constant": a, "linear": -2*abs(b), "quadratic": 0},
                "infimum": "-infinity", "x_zero_fiber_infimum": "0"}
    if d <= 0:
        return None
    short = a-Q(b*b, d)
    if candidate == FALSE_CANDIDATES[1][0] and a > 0 and short < 0:
        vector = (Q(1), -Q(b, d))
        return {"form": asdict(form), "vector": vector, "energy": form.energy(vector),
                "short": short, "A_positive": True, "D_positive": True}
    if candidate == FALSE_CANDIDATES[2][0] and b != 0:
        return {"form": asdict(form), "fiber_x": 1, "minimizer_y": -Q(b, d),
                "compression": a, "envelope": short}
    if candidate == FALSE_CANDIDATES[3][0]:
        return {"form": asdict(form), "source_vector": (0, 1),
                "fine_envelope": d, "coarse_envelope_at_x_zero": 0}
    return None


def discover(matrix_budget=125):
    """Predeclared grammar + deterministic countermodels, NOT open-ended search.

    Search 2x2 symmetric integer forms (a,b;b,d), alphabet (0,1,-1,2,-2),
    product lexicographic order. 'Smallest' means first in THIS finite order.
    Exhaustion without a witness stays UNRESOLVED, never PAPER_PROVED.
    """
    if type(matrix_budget) is not int or not 0 <= matrix_budget <= 125:
        raise DiscoveryError("Matrix search budget must be an integer 0..125")
    alphabet = (0, 1, -1, 2, -2)
    matrices = tuple(cartesian(alphabet, repeat=3))[:matrix_budget]
    candidates = []
    for name, assumptions in FALSE_CANDIDATES:
        witness, checked = None, 0
        for checked, (a, b, d) in enumerate(matrices, 1):
            witness = _counterexample(name, a, b, d)
            if witness is not None:
                break
        candidates.append({"candidate": name, "assumptions": assumptions,
                           "outcome": "REFUTED" if witness else "UNRESOLVED",
                           "authority": "EXACT_FINITE_CHECK" if witness else "UNVERIFIED",
                           "matrices_examined": checked, "witness": witness,
                           "universal_truth_inferred_from_search": False})
    # A source-signed family with a PSD (possibly singular) eliminated block.
    # Direct and staged derivations use different eliminated coordinate blocks.
    checked, rejected = 0, 0
    for a, b, c in cartesian((0, 1, -1), repeat=3):
        form = RationalForm("declared-nested-envelope-model", 0, ("x", "y", "z"),
                            ((a, b, c), (b, 2, 1), (c, 1, 2)))
        nested_envelope(form, ("x", "y"), ("x",))
        checked += 1
    singular = RationalForm("declared-singular-nested-model", 0, ("x", "y", "z"),
                            ((-1, 1, 1), (1, 1, 1), (1, 1, 1)))
    nested = nested_envelope(singular, ("x", "y"), ("x",))
    # Deliberately incompatible coordinate transport is refused before arithmetic.
    try:
        nested_envelope(singular, ("x", "y"), ("z",))
    except DiscoveryError:
        rejected += 1
    else:
        raise ArithmeticError("Non-nested observation was accepted")
    rules = [conditional_rule(key) for key in _RULES]
    return {"grammar": "RationalForm -> CoordinateObservation -> FiniteSchurEnvelope -> Coarsen",
            "candidate_generation": "predeclared classical identities and deliberate false weakenings",
            "search_order": {"dimension": 2, "upper_triangle_order": ("a", "b", "d"),
                             "alphabet": alphabet, "matrix_budget": matrix_budget,
                             "smallest_witness_scope": "first matrix in the declared finite order only"},
            "refutation_candidates": candidates,
            "surviving_rules": sorted(rules, key=lambda r: (
                len(r["outstanding_application_obligations"]), r["rule"])),
            "ranking_rule": "number of explicit outstanding application obligations, then rule ID",
            "nested_exact_instances": checked+1, "singular_nested_instance": nested,
            "illegal_compositions_rejected": rejected,
            "search_proves_universal_theorems": False, "RH_proved": False,
            "authentic_Weil_source_loaded": False, "Lean_kernel_replayed": False}
