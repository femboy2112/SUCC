"""Proof-access compilation on declared finite sources and periodic integers.

Finite tables denote the WHOLE finite mathematical source, never a sample of
an unknown infinite one. Universal periodic/Newton claims depend on the paper
proof PT-C in MINIMAL_OBSERVATION_CARRIER_THEOREMS.md. This is not a Lean checker.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from math import gcd
import json

from .covariant_proof_descent import OriginalSourceSquare
from .source_character_interaction import character_four
from .tate_chi4 import Chi4TateSource


class ObservationError(ValueError):
    pass


def _integer(n, minimum=None):
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ObservationError("Exact integer in the declared domain required")
    return n


def _label(x):
    # Restrict to canonical, immutable labels: no bool/int alias or repr hooks.
    if type(x) in (str, int):
        return
    if type(x) is tuple:
        for v in x:
            _label(v)
        return
    raise ObservationError("Labels must be integers, strings or tuples thereof")


@dataclass(frozen=True)
class FiniteObservation:
    source_id: str
    epoch: int
    observation: tuple
    target: tuple
    laws: tuple[str, ...] = ("source is exactly Fin(len(target))",)
    proof_theory: str = "classical finite sets; exact equality"
    cost_model: str = "finite table, unit-cost label comparisons"

    def __post_init__(self):
        if type(self.source_id) is not str or not self.source_id.strip():
            raise ObservationError("Declare source identity")
        _integer(self.epoch, 0)
        if (type(self.target) is not tuple or type(self.observation) is not tuple
                or len(self.target) != len(self.observation) or len(self.target) > 4096):
            raise ObservationError("Whole finite source tables, size <=4096, required")
        for x in self.target + self.observation:
            _label(x)
        if (type(self.laws) is not tuple or not self.laws or
                any(type(x) is not str or not x.strip() for x in self.laws) or
                type(self.proof_theory) is not str or not self.proof_theory.strip() or
                type(self.cost_model) is not str or not self.cost_model.strip()):
            raise ObservationError("Source laws, proof theory and cost model required")

    @property
    def digest(self):
        data = (self.source_id, self.epoch, self.observation, self.target,
                self.laws, self.proof_theory, self.cost_model)
        return sha256(json.dumps(data, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


@dataclass(frozen=True)
class FactorizationCertificate:
    source_digest: str
    outcome: str
    decoder: tuple[tuple[object, object], ...] = ()
    collision: tuple[int, int] | None = None
    authority: str = "EXACT_FINITE_CHECK"


def compile_factorization(problem: FiniteObservation) -> FactorizationCertificate:
    """Reuse SUCC's coimage/fiber implementation; decode reachable artifacts only."""
    if not problem.target:
        return FactorizationCertificate(problem.digest, "PROVEN_FACTORIZATION")
    square = OriginalSourceSquare(problem.source_id, tuple(range(len(problem.target))),
                                  problem.observation, problem.observation, problem.target)
    result = square.decoder()
    if result["factors"]:
        return FactorizationCertificate(problem.digest, "PROVEN_FACTORIZATION", result["decoder"])
    return FactorizationCertificate(problem.digest, "REFUTED", collision=result["collision"])


def replay_factorization(problem: FiniteObservation, certificate: FactorizationCertificate) -> bool:
    """Independent pairwise verifier; no trust in a producer's success flag."""
    if (certificate.source_digest != problem.digest or
            certificate.authority != "EXACT_FINITE_CHECK"):
        return False
    if certificate.outcome == "REFUTED":
        if certificate.decoder or type(certificate.collision) is not tuple or len(certificate.collision) != 2:
            return False
        i, j = certificate.collision
        return (type(i) is int and type(j) is int and 0 <= i < len(problem.target)
                and 0 <= j < len(problem.target) and
                problem.observation[i] == problem.observation[j] and
                problem.target[i] != problem.target[j])
    if certificate.outcome != "PROVEN_FACTORIZATION" or certificate.collision is not None:
        return False
    try:
        if type(certificate.decoder) is not tuple:
            return False
        for row in certificate.decoder:
            if type(row) is not tuple or len(row) != 2:
                return False
            _label(row[0]); _label(row[1])
        decoder = dict(certificate.decoder)
    except (TypeError, ValueError):
        return False
    if len(decoder) != len(certificate.decoder) or set(decoder) != set(problem.observation):
        return False
    for i, (observed, wanted) in enumerate(zip(problem.observation, problem.target)):
        if decoder[observed] != wanted:
            return False
        for j in range(i):
            if observed == problem.observation[j] and wanted != problem.target[j]:
                return False
    return True


def decode(certificate: FactorizationCertificate, observation):
    """Only the observation is an input. The caller must replay the certificate."""
    _label(observation)
    if certificate.outcome != "PROVEN_FACTORIZATION":
        raise ObservationError("No decoder certified")
    for seen, value in certificate.decoder:
        if seen == observation:
            return value
    raise ObservationError("Unreachable/unobserved artifact: no extension was certified")


def minimum_in_menu(problem: FiniteObservation, menu: tuple[tuple, ...]) -> dict:
    """Least sufficient observation under partition refinement, among this menu.

    If none is sufficient individually, joint observations may still suffice.
    A toolkit obstruction is returned only for a collision of the entire joint
    readout, whose deterministic postprocessing/adaptive rereads add no data.
    """
    if type(menu) is not tuple or not menu or len(menu) > 32:
        raise ObservationError("Nonempty finite menu (<=32) required")
    problems = tuple(FiniteObservation(problem.source_id, problem.epoch, row, problem.target,
                                      problem.laws, problem.proof_theory, problem.cost_model)
                     for row in menu)
    certificates = tuple(compile_factorization(p) for p in problems)
    sufficient = [i for i, c in enumerate(certificates) if c.outcome == "PROVEN_FACTORIZATION"]
    n = len(problem.target)
    least = tuple(i for i in sufficient if all(
        all(menu[j][s] != menu[j][t] or menu[i][s] == menu[i][t]
            for s in range(n) for t in range(s)) for j in sufficient))
    joint = tuple(tuple(row[s] for row in menu) for s in range(n))
    joint_problem = FiniteObservation(problem.source_id, problem.epoch, joint, problem.target,
                                     problem.laws, problem.proof_theory, problem.cost_model)
    joint_certificate = compile_factorization(joint_problem)
    return {"outcome": "PROVEN_MINIMUM_IN_MENU" if least else
            "PROVEN_TOOLKIT_OBSTRUCTION" if joint_certificate.outcome == "REFUTED" else
            "UNRESOLVED_MINIMUM_IN_MENU",
            "least_indices": least, "sufficient_indices": tuple(sufficient),
            "certificates": certificates, "joint_problem": joint_problem,
            "joint_certificate": joint_certificate, "authority": "EXACT_FINITE_CHECK",
            "toolkit": "deterministic functions of declared joint finite readout"}


def chi4_observation(modulus: int, source: Chi4TateSource = Chi4TateSource()) -> dict:
    """PT-C02: chi4: Z->Z factors modulo n iff 4|n. No input-size sampling.

    The existing bounded character_four is used only on residues 0..3; the
    integer extension is defined by this periodic table, even for large n.
    """
    n = _integer(modulus, 1)
    if type(source) is not Chi4TateSource:
        raise ObservationError("Authentic Chi4TateSource declaration required")
    witness = None if n % 4 == 0 else ((0, n) if n % 2 else (1, n + 1))
    values = None if witness is None else tuple(character_four(x % 4) for x in witness)
    return {"source_id": source.source_id, "epoch": source.epoch, "modulus": n,
            "source_domain": "Z", "target": "chi4(x mod 4)",
            "outcome": "PROVEN_FACTORIZATION" if witness is None else "REFUTED",
            "decoder_rule": "chi4(r mod 4)" if witness is None else None,
            "collision": witness, "target_values": values,
            "minimal_modulus_under_divisibility": 4,
            "proof": "PT-C02", "authority": "PAPER_PROVED",
            "finite_check_authority": "EXACT_FINITE_CHECK",
            "local_idele_character_is_zero_on_even_integers": False}


@dataclass(frozen=True)
class PrimitiveRealCharacter:
    """Exact primitive Dirichlet character in a bounded real-valued family.

    Primitivity tests induction of the UNIT character, not just the integer
    table's period (a principal character mod p is the counterexample).
    """
    values: tuple[int, ...]

    def __post_init__(self):
        q = len(self.values)
        if type(self.values) is not tuple or not 2 <= q <= 128:
            raise ObservationError("Real Dirichlet character table of modulus 2..128")
        if any(type(v) is not int or v not in (-1, 0, 1) for v in self.values):
            raise ObservationError("Exact real character values required")
        if self.values[1] != 1 or any((self.values[x] != 0) != (gcd(x, q) == 1) for x in range(q)):
            raise ObservationError("Character support must be precisely the units")
        if any(self.values[a*b % q] != self.values[a]*self.values[b]
               for a in range(q) for b in range(q)):
            raise ObservationError("Nonmultiplicative character table")
        units = tuple(x for x in range(q) if gcd(x, q) == 1)
        for d in range(1, q):
            if q % d == 0 and all(a % d != b % d or self.values[a] == self.values[b]
                                 for a in units for b in units):
                raise ObservationError("Imprimitive unit character; declared modulus is not conductor")

    @property
    def conductor(self):
        return len(self.values)

    def observation(self, n: int) -> dict:
        n = _integer(n, 1)
        q = self.conductor
        witness = next(((x, x+n) for x in range(q)
                        if self.values[x] != self.values[(x+n) % q]), None)
        return {"modulus": n, "conductor": q, "collision": witness,
                "outcome": "PROVEN_FACTORIZATION" if witness is None else "REFUTED",
                "decoder_table": self.values if witness is None else None,
                "decoder_rule": "table[r mod conductor]" if witness is None else None,
                "authority": "PAPER_PROVED", "finite_table_authority": "EXACT_FINITE_CHECK",
                "proof": "PT-C03", "scope": "periodic integer values, not idele-local components"}


def binomial_integer(x: int, degree: int) -> int:
    """Generalized binomial for ALL integer x, via exact falling factorial."""
    _integer(x); _integer(degree, 0)
    v = 1
    for j in range(1, degree+1):
        v = v*(x-j+1)//j
    return v


def newton_coefficients(values: tuple[int, ...]) -> tuple[int, ...]:
    if type(values) is not tuple or not values or len(values) > 65:
        raise ObservationError("1..65 integer observations at consecutive inputs 0..d")
    for value in values:
        _integer(value)
    result, row = [], values
    while row:
        result.append(row[0])
        row = tuple(b-a for a, b in zip(row, row[1:]))
    return tuple(result)


def newton_value(coefficients: tuple[int, ...], x: int) -> int:
    if type(coefficients) is not tuple or not coefficients or len(coefficients) > 65:
        raise ObservationError("Declared finite integer Newton coefficients required")
    _integer(x)
    for c in coefficients:
        _integer(c)
    return sum(c*binomial_integer(x, j) for j, c in enumerate(coefficients))


def polynomial_descent(coefficients: tuple[int, ...], n: int) -> dict:
    """PT-C04: period n iff Δ_n P vanishes mod n at 0..d-1.

    Integer-valued P of degree <=d is supplied in the Newton basis. Agreement
    tests certify this restricted class; they do not recognize arbitrary functions.
    """
    n = _integer(n, 1)
    newton_value(coefficients, 0)  # Validate even the constant case.
    d = len(coefficients)-1
    differences = tuple((newton_value(coefficients, x+n)-newton_value(coefficients, x)) % n
                        for x in range(d))
    bad = next((x for x, value in enumerate(differences) if value), None)
    return {"modulus": n, "degree_bound": d, "difference_observations": differences,
            "outcome": "PROVEN_DESCENT" if bad is None else "REFUTED",
            "collision": None if bad is None else (bad, bad+n),
            "authority": "PAPER_PROVED", "finite_check_authority": "EXACT_FINITE_CHECK",
            "proof": "PT-C04"}
