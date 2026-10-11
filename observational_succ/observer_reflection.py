"""Observer-relative closure: finite proof support, ordinal reflection, intervals.

The crucial finitary omega theorem, valid for any increasing theory chain:

  (union_(n<omega) T_n) |-_finitary phi
        iff  (exists n) T_n |- _finitary phi.

Every individual finite derivation uses finitely many nonlogical
axioms, so they already occur at a common finite stage. This is a
theorem about FINITARY inference, not a claim about Gödel incompleteness
or the semantic truth of phi. The omega rule and adding Con(T) are
separate stronger commitments; neither is a consequence of mere SUCC.

Second independent deliverable: rational interval Gram certificates.
A STRICTLY negative *certified interval upper bound* on some c^T K c
is a finite counterexample to positive semidefiniteness. No affirmative
finite search verdict claims universal positivity. Arbitrary mpmath
point evaluations must NOT masquerade as rigorous enclosures.

For the actual Suzuki kernel, an independent rigorous Gamma interval
oracle and source-admissible test-domain matching are still REQUIRED.
The current exact polynomial controls do not prove or refute RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from .observer_logic import (
    Formula, Pred, Num, Var, Forall, Theory, FiniteProof,
    LogicBoundaryError, check_finite_proof, free_variables,
)


class ReflectionBoundaryError(ValueError):
    """Mixing observation, proof, limit report or untrusted bound."""


def _fraction(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise ReflectionBoundaryError("Strict source certificates require exact rational numbers")


@dataclass(frozen=True)
class FinitarySupportWitness:
    """A finite proof at the omega union already belongs to stage n."""
    earliest_stage: int
    total_stages_inspected: int
    used_axioms: tuple[Formula, ...]
    conclusion: Formula
    finite_proof_verified: bool
    omega_rule_used: bool = False
    physical_infinite_process_executed: bool = False


@dataclass(frozen=True)
class IncreasingTheoryChain:
    """A finite prefix of an inductive omega chain; never a run of omega."""
    stages: tuple[Theory, ...]

    def __post_init__(self):
        if type(self.stages) is not tuple or not self.stages or len(self.stages) > 256:
            raise ReflectionBoundaryError("Need a nonempty finite theory-stage tuple")
        if not all(isinstance(t, Theory) for t in self.stages):
            raise ReflectionBoundaryError("Every stage must be a typed theory")
        for before, after in zip(self.stages, self.stages[1:]):
            if not before.axioms.issubset(after.axioms):
                raise ReflectionBoundaryError("Successor theories must preserve earlier axioms")

    @property
    def last(self) -> Theory:
        return self.stages[-1]

    def successor(self, extra_axiom: Formula, *, label: str) -> "IncreasingTheoryChain":
        """Add a DECLARED external axiom, not an internally proven report."""
        if not isinstance(extra_axiom, Formula) or free_variables(extra_axiom):
            raise ReflectionBoundaryError("A successor axiom must be a closed formula")
        if type(label) is not str or not label or len(label) > 128:
            raise ReflectionBoundaryError("Every new logical authority needs provenance")
        if len(self.stages) >= 256:
            raise ReflectionBoundaryError("Finite theory resource limit reached")
        old = self.last
        new = Theory(f"T{len(self.stages)}", old.axioms | {extra_axiom})
        return IncreasingTheoryChain(self.stages + (new,))

    def omega_finitary_support(self, proof: FiniteProof) -> FinitarySupportWitness:
        """Find the stage already containing every NONLOGICAL axiom in proof.

        This executable lemma is the finitary compactness of a directed
        UNION of theories, specialized to a finite observed prefix.
        Generalizing to all finite prefixes is a direct mathematical
        argument, not a computational execution of the limit ordinal.
        """
        if not isinstance(proof, FiniteProof):
            raise ReflectionBoundaryError("Only FINITE checked proof objects count")
        try:
            check_finite_proof(self.last, proof)
        except LogicBoundaryError as exc:
            raise ReflectionBoundaryError("Not a proof from the declared omega-prefix union") from exc
        used = frozenset(step.formula for step in proof.steps if step.rule == "axiom")
        if not used.issubset(self.last.axioms):
            raise ReflectionBoundaryError("Proof uses a nonexistent future axiom")
        earliest = next(
            (i for i, t in enumerate(self.stages) if used.issubset(t.axioms)),
            None)
        if earliest is None:
            raise ArithmeticError("Compatible finite proof lacks a finite support stage")
        check_finite_proof(self.stages[earliest], proof)
        return FinitarySupportWitness(
            earliest, len(self.stages), tuple(sorted(used, key=repr)),
            proof.conclusion, True)

    def semantic_omega_report(self, predicate: str, horizon: int):
        """Report what was OBSERVED; never return a proof or truth oracle."""
        if type(horizon) is not int or not 0 <= horizon <= 100000:
            raise ReflectionBoundaryError("Bounded finite observer horizon required")
        if type(predicate) is not str or not predicate.isidentifier():
            raise ReflectionBoundaryError("Predicate name required")
        return {
            "observed_through": horizon,
            "intended_global_formula": Forall("n", Pred(predicate, Var("n"))),
            "proof_status": "UNRESOLVED",
            "omega_not_executed": True,
            "finite_proof_manufactured": False,
            "scope": "a universal semantic REPORT, not proof in T or T_omega",
        }


def external_consistency_step(
    chain: IncreasingTheoryChain, *, evidence_label: str
) -> tuple[IncreasingTheoryChain, dict]:
    """An HONEST simulated Turing/Feferman successor.

    Con_T is intentionally a PROPOSITIONAL PLACEHOLDER, not PA's
    arithmetically represented proof predicate. Appending it can
    strictly strengthen the theory but requires an EXTERNAL assumption.
    """
    if not isinstance(chain, IncreasingTheoryChain):
        raise ReflectionBoundaryError("Need a theory chain")
    if type(evidence_label) is not str or not evidence_label:
        raise ReflectionBoundaryError("Specify explicit metatheoretic evidence")
    candidate = Pred(f"AssumedConsistencyT{len(chain.stages)-1}")
    newer = chain.successor(candidate, label=evidence_label)
    return newer, {
        "new_axiom": candidate,
        "axiom_status": "EXTERNAL_ASSUMPTION_ONLY",
        "claimed_truth_of_axiom": None,
        "verified_in_predecessor": False,
        "reflective_successor_is_ordinary_observation": False,
        "metatheoretic_basis": evidence_label,
    }


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self):
        a, b = _fraction(self.lower), _fraction(self.upper)
        if a > b:
            raise ReflectionBoundaryError("Interval lower bound exceeds upper")
        object.__setattr__(self, "lower", a)
        object.__setattr__(self, "upper", b)

    @classmethod
    def exact(cls, x):
        a = _fraction(x)
        return cls(a, a)

    def __add__(self, other):
        if not isinstance(other, RationalInterval):
            raise ReflectionBoundaryError("Interval arithmetic requires intervals")
        return RationalInterval(self.lower + other.lower,
                                self.upper + other.upper)

    def __neg__(self):
        return RationalInterval(-self.upper, -self.lower)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, q):
        s = _fraction(q)
        return RationalInterval(*(sorted((s*self.lower, s*self.upper))))

    def __mul__(self, other):
        if not isinstance(other, RationalInterval):
            raise ReflectionBoundaryError("Interval products require intervals")
        values = tuple(x*y for x in (self.lower, self.upper)
                             for y in (other.lower, other.upper))
        return RationalInterval(min(values), max(values))

    def intersects(self, other):
        return isinstance(other, RationalInterval) and (
            max(self.lower, other.lower) <= min(self.upper, other.upper))


@dataclass(frozen=True)
class GramCertificate:
    times: tuple[Fraction, ...]
    coefficients: tuple[Fraction, ...]
    enclosure: RationalInterval
    result: str
    oracle_provenance: str
    relies_on_oracle_soundness: bool = True
    universal_positivity_proved: bool = False


def rational_gram_certificate(times, coefficients, oracle, *, provenance):
    """Find a STRICT negative witness, conditional on sound interval oracle.

    This routine does NOT independently verify that the supplied
    oracle contains the analytic kernel's true values. To apply it to
    Suzuki, derive a trusted interval oracle from prime/Gamma bounds
    first. An untrusted mpmath approximation cannot become one simply
    by putting a tiny interval around its output.
    """
    ts = tuple(_fraction(t) for t in times)
    cs = tuple(_fraction(c) for c in coefficients)
    if not ts or len(ts) > 16 or len(ts) != len(cs) or not any(cs):
        raise ReflectionBoundaryError("Require 1..16 times and a nonzero coefficient vector")
    if len(set(ts)) != len(ts):
        raise ReflectionBoundaryError("Observation times must be distinct")
    if type(provenance) is not str or not provenance or len(provenance) > 256:
        raise ReflectionBoundaryError("Oracle must name its mathematical provenance")
    matrix = []
    for t in ts:
        row = []
        for u in ts:
            z = oracle(t, u)
            if not isinstance(z, RationalInterval):
                raise ReflectionBoundaryError(
                    "Reject untrusted scalar evaluation: need rational upper/lower bounds")
            row.append(z)
        matrix.append(tuple(row))
    for i in range(len(ts)):
        for j in range(len(ts)):
            if not matrix[i][j].intersects(matrix[j][i]):
                raise ReflectionBoundaryError("Purported Hermitian real kernel intervals disagree")
    total = RationalInterval.exact(0)
    for i in range(len(ts)):
        for j in range(len(ts)):
            total += matrix[i][j].scale(cs[i]*cs[j])
    status = ("STRICT_NEGATIVE_WITNESS_CONDITIONAL_ON_INTERVAL_ORACLE"
              if total.upper < 0 else "FINITE_PROBE_UNRESOLVED")
    return GramCertificate(ts, cs, total, status, provenance)


def exact_quartic_screw(t, u):
    """A fully auditable exact rational adversarial oracle, NOT Suzuki."""
    t, u = _fraction(t), _fraction(u)
    return RationalInterval.exact(t**4 + u**4 - (t-u)**4)


def exact_quadratic_screw(t, u):
    """PSD exact rational control Psi(t)=t², K(t,u)=2tu."""
    t, u = _fraction(t), _fraction(u)
    return RationalInterval.exact(2*t*u)


def bounded_gram_search(oracle, *, points=(-1, 0, 1), budget=256,
                        provenance="DECLARED_INTERVAL_ORACLE"):
    """Finite deterministic search for a negative 2x2 Gram direction.

    A finite no-find is UNRESOLVED, not global PSD. It is intentionally
    not a search over actual zeta zeros or spectral ordinates.
    """
    if type(budget) is not int or not 1 <= budget <= 1024:
        raise ReflectionBoundaryError("Finite search budget must be 1..1024")
    grid = tuple(_fraction(x) for x in points)
    if len(set(grid)) != len(grid) or len(grid) < 2 or len(grid) > 12:
        raise ReflectionBoundaryError("Need 2..12 distinct exact rational points")
    inspected = 0
    for pair in combinations(grid, 2):
        for cs in product((-1, 0, 1), repeat=2):
            if not any(cs):
                continue
            inspected += 1
            if inspected > budget:
                return {"status":"UNRESOLVED", "inspected":budget,
                        "universal_positivity_proved":False}
            result = rational_gram_certificate(
                pair, cs, oracle, provenance=provenance)
            if result.enclosure.upper < 0:
                return {"status":"STRICT_NEGATIVE_WITNESS",
                        "inspected":inspected,
                        "certificate":result,
                        "universal_positivity_proved":False}
    return {"status":"UNRESOLVED", "inspected":inspected,
            "universal_positivity_proved":False}



@dataclass(frozen=True)
class UnnamedElementOmegaCountermodel:
    """A FIRST-ORDER semantic model separating all named finite instances
    from their universal closure WITHOUT appealing to incompleteness.

    Language: exactly ONE unary predicate P (no equality or arithmetic),
    plus numeral-like constant names 0,1,... and bound variables.
    Domain: N disjoint union {UNNAMED}. All numerals denote their
    distinct standard n. P(n) holds for EVERY named natural number,
    P(UNNAMED) is FALSE.

    The full infinite theory {P(0),P(1),...} is TRUE in this model, but
    forall x P(x) is false. This is a genuine semantic non-entailment
    theorem for this weak unary language; it is NOT a model of PA or
    a proof of Gödel incompleteness. First-order induction and a
    standard-domain assumption would change the situation.

    Because this language has no equality or arithmetic, every
    ordinary natural has the same atomic P-type, so all quantifiers
    can be evaluated by testing two representative types NAT/UNNAMED.
    """
    predicate: str = "Observed"

    def __post_init__(self):
        if type(self.predicate) is not str or not self.predicate.isidentifier():
            raise ReflectionBoundaryError("A well-formed unary predicate name is required")

    def named_instance(self, n: int) -> bool:
        if type(n) is not int or n < 0:
            raise ReflectionBoundaryError("Instance index must be an exact natural")
        return True

    def universal_claim(self) -> Formula:
        return Forall("x", Pred(self.predicate, Var("x")))

    def evaluate(self, formula: Formula) -> bool:
        """Decide the equality-free unary language by finite types."""
        if not isinstance(formula, Formula):
            raise ReflectionBoundaryError("Only typed formulas can be interpreted")
        if free_variables(formula):
            raise ReflectionBoundaryError("A semantic claim must be a closed sentence")

        def interpret_term(t, env):
            # Every arithmetic numeral names its own natural, but in
            # the equality-free P-only language all share atomic type NAT.
            if t.kind == "numeral" or t.kind == "zero":
                return "NAT"
            if t.kind == "var":
                return env[t.args[0]]
            raise ReflectionBoundaryError(
                "This model has NO arithmetic operations or equality symbols")

        def rec(f,env):
            if f.kind == "predicate":
                name, ts = f.args
                if name != self.predicate or len(ts) != 1:
                    raise ReflectionBoundaryError("Only the named unary predicate is modeled")
                return interpret_term(ts[0],env) == "NAT"
            if f.kind == "false":
                return False
            if f.kind == "not":
                return not rec(f.args[0],env)
            if f.kind == "and":
                return rec(f.args[0],env) and rec(f.args[1],env)
            if f.kind == "implies":
                return (not rec(f.args[0],env)) or rec(f.args[1],env)
            if f.kind == "forall":
                var,body=f.args
                return all(rec(body,{**env,var:z}) for z in ("NAT","UNNAMED"))
            if f.kind == "exists":
                var,body=f.args
                return any(rec(body,{**env,var:z}) for z in ("NAT","UNNAMED"))
            raise ReflectionBoundaryError(
                "This is an equality-free unary countermodel, not a PA model")
        return rec(formula,{})

    def structural_report(self):
        global_claim=self.universal_claim()
        return {
            "language":"equality-free monadic first-order predicate + named numerals",
            "domain":"standard naturals with one extra unnamed element",
            "all_named_ground_instances_true":True,
            "global_universal_claim":global_claim,
            "global_universal_claim_true":self.evaluate(global_claim),
            "uses_omega_rule":False,
            "applies_to_PA":False,
            "RH_independence_inferred":False,
        }
