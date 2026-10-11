"""Typed observational logic: syntax, Gödel codes, finite proof checking.

This is an independent *general* observational-SUCC layer. It does not
construct a PA proof or execute an ordinal computation.

What IS implemented:
  * immutable validated first-order arithmetic-like syntax;
  * injective reversible finite Gödel numbering with a reproducible codec;
  * capture-avoiding substitution, including alpha-renaming;
  * a FINITE arithmetical diagonal-lemma *syntax certificate*;
  * a small, sound finitary proof checker (axioms, assumptions,
    modus ponens, universal instantiation and restricted generalization);
  * injective encodings and decidable verification of FINITE proof codes.

The diagonal syntax certificate is conditional: the distinguished
predicate SubstGraph must be represented correctly INSIDE a sufficiently
strong arithmetic theory to obtain the actual object-level
diagonal lemma. This package does NOT establish its representability or
prove Gödel incompleteness. An ordinary observed finite sequence is never
accepted as a universal proof, and the omega rule is not a finite rule.

Source: Gödel diagonal lemma as in the Stanford Encyclopedia of Philosophy.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import re
from typing import Iterable


class LogicBoundaryError(ValueError):
    """Malformed syntax, causal/proof boundary or unproved inference."""


_IDENT = re.compile(r"^[A-Za-z_][A-Za-z_0-9]{0,63}$")
_HEX = re.compile(r"^(0|[1-9a-f][0-9a-f]*)$")


def _identifier(x: str) -> str:
    if type(x) is not str or _IDENT.fullmatch(x) is None:
        raise LogicBoundaryError("Identifiers must be short canonical ASCII names")
    return x


@dataclass(frozen=True)
class Term:
    kind: str
    args: tuple = ()

    def __post_init__(self):
        a = self.args
        if type(a) is not tuple:
            raise LogicBoundaryError("Term arguments must be immutable tuples")
        if self.kind == "zero":
            valid = len(a) == 0
        elif self.kind == "var":
            valid = len(a) == 1 and type(a[0]) is str and bool(_IDENT.fullmatch(a[0]))
        elif self.kind == "numeral":
            valid = (len(a) == 1 and type(a[0]) is str
                     and len(a[0]) <= 32768 and bool(_HEX.fullmatch(a[0])))
        elif self.kind == "succ":
            valid = len(a) == 1 and isinstance(a[0], Term)
        elif self.kind in ("add", "multiply"):
            valid = len(a) == 2 and all(isinstance(z, Term) for z in a)
        else:
            valid = False
        if not valid:
            raise LogicBoundaryError(f"Invalid term kind/arguments: {self.kind}")

    def numeral_value(self) -> int:
        if self.kind != "numeral":
            raise LogicBoundaryError("Only numerals have a numeric value")
        return int(self.args[0], 16)


@dataclass(frozen=True)
class Formula:
    kind: str
    args: tuple = ()

    def __post_init__(self):
        a = self.args
        if type(a) is not tuple:
            raise LogicBoundaryError("Formula arguments must be immutable tuples")
        if self.kind == "false":
            valid = len(a) == 0
        elif self.kind == "eq":
            valid = len(a) == 2 and all(isinstance(z, Term) for z in a)
        elif self.kind == "predicate":
            valid = (len(a) == 2 and type(a[0]) is str
                     and bool(_IDENT.fullmatch(a[0])) and type(a[1]) is tuple
                     and all(isinstance(z, Term) for z in a[1]))
        elif self.kind == "not":
            valid = len(a) == 1 and isinstance(a[0], Formula)
        elif self.kind in ("and", "implies"):
            valid = len(a) == 2 and all(isinstance(z, Formula) for z in a)
        elif self.kind in ("forall", "exists"):
            valid = (len(a) == 2 and type(a[0]) is str
                     and bool(_IDENT.fullmatch(a[0]))
                     and isinstance(a[1], Formula))
        else:
            valid = False
        if not valid:
            raise LogicBoundaryError(f"Invalid formula kind/arguments: {self.kind}")


def Var(name: str) -> Term:
    return Term("var", (_identifier(name),))


def Num(n: int) -> Term:
    if type(n) is not int or n < 0:
        raise LogicBoundaryError("Numerals must be nonnegative exact integers")
    return Term("numeral", (format(n, "x"),))


def Zero() -> Term:
    return Term("zero")


def Succ(t: Term) -> Term:
    return Term("succ", (t,))


def Add(x: Term, y: Term) -> Term:
    return Term("add", (x, y))


def Multiply(x: Term, y: Term) -> Term:
    return Term("multiply", (x, y))


def Eq(x: Term, y: Term) -> Formula:
    return Formula("eq", (x, y))


def Pred(name: str, *terms: Term) -> Formula:
    return Formula("predicate", (_identifier(name), tuple(terms)))


def Falsum() -> Formula:
    return Formula("false")


def Not(phi: Formula) -> Formula:
    return Formula("not", (phi,))


def And(phi: Formula, psi: Formula) -> Formula:
    return Formula("and", (phi, psi))


def Implies(phi: Formula, psi: Formula) -> Formula:
    return Formula("implies", (phi, psi))


def Forall(name: str, phi: Formula) -> Formula:
    return Formula("forall", (_identifier(name), phi))


def Exists(name: str, phi: Formula) -> Formula:
    return Formula("exists", (_identifier(name), phi))


def term_variables(t: Term) -> frozenset[str]:
    if not isinstance(t, Term):
        raise LogicBoundaryError("Expected term")
    if t.kind == "var":
        return frozenset((t.args[0],))
    return frozenset().union(
        *(term_variables(x) for x in t.args if isinstance(x, Term)))


def all_variable_names(phi: Formula) -> frozenset[str]:
    """Include both free and bound names, for safe freshening."""
    if not isinstance(phi, Formula):
        raise LogicBoundaryError("Expected formula")
    k, a = phi.kind, phi.args
    if k == "predicate":
        return frozenset().union(*(term_variables(t) for t in a[1]))
    if k == "eq":
        return term_variables(a[0]) | term_variables(a[1])
    if k in ("false",):
        return frozenset()
    if k == "not":
        return all_variable_names(a[0])
    if k in ("and", "implies"):
        return all_variable_names(a[0]) | all_variable_names(a[1])
    return frozenset((a[0],)) | all_variable_names(a[1])


def free_variables(phi: Formula) -> frozenset[str]:
    if not isinstance(phi, Formula):
        raise LogicBoundaryError("Expected formula")
    k, a = phi.kind, phi.args
    if k == "predicate":
        return frozenset().union(*(term_variables(t) for t in a[1]))
    if k == "eq":
        return term_variables(a[0]) | term_variables(a[1])
    if k == "false":
        return frozenset()
    if k == "not":
        return free_variables(a[0])
    if k in ("and", "implies"):
        return free_variables(a[0]) | free_variables(a[1])
    return free_variables(a[1]) - {a[0]}


def substitute_term(t: Term, name: str, replacement: Term) -> Term:
    _identifier(name)
    if not isinstance(t, Term) or not isinstance(replacement, Term):
        raise LogicBoundaryError("Substitution takes typed terms")
    if t.kind == "var" and t.args[0] == name:
        return replacement
    if t.kind in ("zero", "var", "numeral"):
        return t
    return Term(t.kind, tuple(substitute_term(z, name, replacement) for z in t.args))


def _rename_bound_body(phi: Formula, old: str, new: str) -> Formula:
    """Rename occurrences bound by an OUTER binder; respect inner shadow."""
    k, a = phi.kind, phi.args
    if k == "eq":
        return Eq(*(substitute_term(t, old, Var(new)) for t in a))
    if k == "predicate":
        return Pred(a[0], *(substitute_term(t, old, Var(new)) for t in a[1]))
    if k == "false":
        return phi
    if k == "not":
        return Not(_rename_bound_body(a[0], old, new))
    if k == "and":
        return And(_rename_bound_body(a[0], old, new),
                   _rename_bound_body(a[1], old, new))
    if k == "implies":
        return Implies(_rename_bound_body(a[0], old, new),
                       _rename_bound_body(a[1], old, new))
    if a[0] == old:
        return phi  # inner binder shadows the outer one
    return Formula(k, (a[0], _rename_bound_body(a[1], old, new)))


def substitute_formula(phi: Formula, name: str, replacement: Term) -> Formula:
    """Capture-avoiding FREE substitution, with explicit alpha-renaming."""
    _identifier(name)
    if not isinstance(phi, Formula) or not isinstance(replacement, Term):
        raise LogicBoundaryError("Substitution takes a formula and term")
    k, a = phi.kind, phi.args
    if k == "eq":
        return Eq(*(substitute_term(t, name, replacement) for t in a))
    if k == "predicate":
        return Pred(a[0], *(substitute_term(t, name, replacement) for t in a[1]))
    if k == "false":
        return phi
    if k == "not":
        return Not(substitute_formula(a[0], name, replacement))
    if k == "and":
        return And(substitute_formula(a[0], name, replacement),
                   substitute_formula(a[1], name, replacement))
    if k == "implies":
        return Implies(substitute_formula(a[0], name, replacement),
                       substitute_formula(a[1], name, replacement))
    bound, body = a
    if bound == name or name not in free_variables(body):
        return phi
    if bound in term_variables(replacement):
        taken = all_variable_names(phi) | term_variables(replacement) | {name}
        fresh = next((f"v_{i}" for i in range(10000)
                      if f"v_{i}" not in taken), None)
        if fresh is None:
            raise LogicBoundaryError("Unable to freshen bound variable")
        body = _rename_bound_body(body, bound, fresh)
        bound = fresh
    return Formula(k, (bound, substitute_formula(body, name, replacement)))


def _marshal(obj):
    if isinstance(obj, Term):
        return ["T", obj.kind, *(_marshal(x) for x in obj.args)]
    if isinstance(obj, Formula):
        return ["F", obj.kind, *(_marshal(x) for x in obj.args)]
    if isinstance(obj, tuple):
        return ["Q", *(_marshal(x) for x in obj)]
    if type(obj) in (str, int) or obj is None:
        return obj
    raise LogicBoundaryError("Only validated syntax is serializable")


def _unmarshal(x):
    if type(x) is list:
        if not x:
            raise LogicBoundaryError("Empty serialization node")
        tag = x[0]
        if tag == "T":
            return Term(x[1], tuple(_unmarshal(z) for z in x[2:]))
        if tag == "F":
            return Formula(x[1], tuple(_unmarshal(z) for z in x[2:]))
        if tag == "Q":
            return tuple(_unmarshal(z) for z in x[1:])
        raise LogicBoundaryError("Unrecognized serialization tag")
    if type(x) in (str, int) or x is None:
        return x
    raise LogicBoundaryError("Invalid untrusted serialized payload")


def _pack(tree) -> int:
    raw = json.dumps(tree, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    if len(raw) > 50000:
        raise LogicBoundaryError("Finite Gödel code exceeds resource limit")
    return int.from_bytes(b"\x01" + raw, "big")


def _unpack(code: int):
    if type(code) is not int or code <= 0 or code.bit_length() > 400008:
        raise LogicBoundaryError("Require a bounded positive Gödel number")
    raw = code.to_bytes((code.bit_length() + 7) // 8, "big")
    if not raw.startswith(b"\x01"):
        raise LogicBoundaryError("Gödel code has no codec version header")
    try:
        tree = json.loads(raw[1:].decode("ascii"))
    except (UnicodeError, ValueError, json.JSONDecodeError) as exc:
        raise LogicBoundaryError("Invalid finite Gödel serialization") from exc
    if _pack(tree) != code:
        raise LogicBoundaryError("Noncanonical Gödel serialization")
    return tree


def godel_code(ast: Term | Formula) -> int:
    """Finite reversible injection, NOT the standard PA Gödel code."""
    if not isinstance(ast, (Term, Formula)):
        raise LogicBoundaryError("Expected validated term/formula")
    return _pack(_marshal(ast))


def decode_godel(code: int) -> Term | Formula:
    term = _unmarshal(_unpack(code))
    if not isinstance(term, (Term, Formula)) or godel_code(term) != code:
        raise LogicBoundaryError("Gödel code does not encode a term or formula")
    return term


def diagonalize_formula_code(code: int, variable: str = "x") -> int:
    """Compute d(code(phi(x))) = code(phi(quote(code(phi)))).

    This operation is total on correctly coded formulas in which the
    specified variable is FREE; it is NOT an object-language PA proof
    that the substitution graph is representable by arithmetic formulas.
    """
    phi = decode_godel(code)
    if not isinstance(phi, Formula) or variable not in free_variables(phi):
        raise LogicBoundaryError("Diagonalization expects a formula with a free variable")
    return godel_code(substitute_formula(phi, variable, Num(code)))


@dataclass(frozen=True)
class DiagonalSyntaxCertificate:
    """Meta-level verified skeleton of Gödel's fixed-point construction."""
    template: Formula
    theta: Formula
    sentence: Formula
    expected_consequent: Formula
    theta_code: int
    sentence_code: int
    substitution_graph_symbol: str
    object_language_equivalence_proved: bool = False
    representability_in_PA_proved: bool = False

    def verify(self) -> bool:
        return (not free_variables(self.sentence)
                and diagonalize_formula_code(self.theta_code) == self.sentence_code
                and godel_code(self.sentence) == self.sentence_code
                and self.expected_consequent ==
                    substitute_formula(self.template, "x", Num(self.sentence_code))
                and not self.object_language_equivalence_proved
                and not self.representability_in_PA_proved)


def diagonal_syntax(template: Formula) -> DiagonalSyntaxCertificate:
    """Construct theta(x) = exists y [SubstGraph(x,y) and template(y)].

    sentence = theta(quote(theta)), with its own finite Gödel code c.
    Meta-level evaluation of SubstGraph(quote(theta),y) has the unique
    output y=c, so the *standard diagonal lemma*, GIVEN representability,
    yields T |- sentence <-> template(quote(sentence)).
    This method explicitly does NOT certify that theorem in T.
    """
    if not isinstance(template, Formula) or free_variables(template) != {"x"}:
        raise LogicBoundaryError("Diagonal template must have precisely the free variable x")
    taken = all_variable_names(template)
    y = next((f"diag_{i}" for i in range(10000)
              if f"diag_{i}" not in taken and f"diag_{i}" != "x"), None)
    if y is None:
        raise LogicBoundaryError("No fresh diagonal variable available")
    theta = Exists(y, And(Pred("SubstGraph", Var("x"), Var(y)),
                          substitute_formula(template, "x", Var(y))))
    a = godel_code(theta)
    psi = substitute_formula(theta, "x", Num(a))
    c = godel_code(psi)
    result = DiagonalSyntaxCertificate(
        template, theta, psi,
        substitute_formula(template, "x", Num(c)),
        a, c, "SubstGraph")
    if not result.verify():
        raise ArithmeticError("Gödel syntactic fixed-point codec did not commute")
    return result


@dataclass(frozen=True)
class Theory:
    """A declared FINITE axiom set; NOT implicitly PA or ZFC."""
    name: str
    axioms: frozenset[Formula]

    def __post_init__(self):
        _identifier(self.name)
        if type(self.axioms) is not frozenset or len(self.axioms) > 256:
            raise LogicBoundaryError("Require finite immutable axiom set")
        if any(not isinstance(f, Formula) or free_variables(f) for f in self.axioms):
            raise LogicBoundaryError("Only closed, typed formulas may be axioms")


@dataclass(frozen=True)
class ProofStep:
    formula: Formula
    rule: str
    refs: tuple[int, ...] = ()
    term: Term | None = None

    def __post_init__(self):
        if not isinstance(self.formula, Formula):
            raise LogicBoundaryError("Proof step must contain a formula")
        if type(self.rule) is not str or type(self.refs) is not tuple:
            raise LogicBoundaryError("Malformed finite proof rule")
        if any(type(i) is not int or i < 0 for i in self.refs):
            raise LogicBoundaryError("Proof references must be finite nonnegative indices")
        if self.term is not None and not isinstance(self.term, Term):
            raise LogicBoundaryError("Universal instantiation requires a typed term")


@dataclass(frozen=True)
class FiniteProof:
    steps: tuple[ProofStep, ...]

    def __post_init__(self):
        if type(self.steps) is not tuple or not 1 <= len(self.steps) <= 512:
            raise LogicBoundaryError("Require 1..512 finite proof steps")
        if not all(isinstance(step, ProofStep) for step in self.steps):
            raise LogicBoundaryError("All proof steps must be typed")

    @property
    def conclusion(self):
        return self.steps[-1].formula


def check_finite_proof(
    theory: Theory, proof: FiniteProof,
    *, assumptions: Iterable[Formula] = ()
) -> bool:
    """Fail-closed sound MINIMAL first-order proof-checker.

    Rules: axiom, assumption, modus_ponens, forall_elim, forall_intro.
    No omega rule; no automatic external reflection; no discharging
    assumptions or accepting all observed instances as universal.
    A proof in the empty-assumption context is a FINITE THEOREM of the
    declared axioms. This is weaker than a complete calculus for PA.
    """
    if not isinstance(theory, Theory) or not isinstance(proof, FiniteProof):
        raise LogicBoundaryError("A named theory and actual proof are required")
    context = frozenset(assumptions)
    if any(not isinstance(f, Formula) for f in context):
        raise LogicBoundaryError("Assumptions must be formulas")
    for i, step in enumerate(proof.steps):
        f, refs, rule = step.formula, step.refs, step.rule
        if any(j >= i for j in refs):
            raise LogicBoundaryError("Proof may depend only on earlier steps")
        if rule == "axiom":
            good = not refs and step.term is None and f in theory.axioms
        elif rule == "assumption":
            good = not refs and step.term is None and f in context
        elif rule == "modus_ponens":
            good = (len(refs) == 2 and step.term is None
                    and proof.steps[refs[1]].formula ==
                    Implies(proof.steps[refs[0]].formula, f))
        elif rule == "forall_elim":
            good = (len(refs) == 1 and step.term is not None
                    and proof.steps[refs[0]].formula.kind == "forall")
            if good:
                earlier = proof.steps[refs[0]].formula
                good = f == substitute_formula(
                    earlier.args[1], earlier.args[0], step.term)
        elif rule == "forall_intro":
            good = (len(refs) == 1 and step.term is None
                    and f.kind == "forall"
                    and f.args[1] == proof.steps[refs[0]].formula
                    and all(f.args[0] not in free_variables(g)
                            for g in context | theory.axioms))
        else:
            good = False  # omega, reflection, observational inference are NOT finite rules
        if not good:
            raise LogicBoundaryError(f"Unsound or unsupported finite inference at step {i}: {rule}")
    return True


def _proof_tree(proof: FiniteProof):
    return ["PROOF_1", *[
        [_marshal(s.formula), s.rule, list(s.refs),
         None if s.term is None else _marshal(s.term)]
        for s in proof.steps]]


def encode_proof(proof: FiniteProof) -> int:
    if not isinstance(proof, FiniteProof):
        raise LogicBoundaryError("Expected finite proof")
    return _pack(_proof_tree(proof))


def decode_proof(code: int) -> FiniteProof:
    tree = _unpack(code)
    if type(tree) is not list or not tree or tree[0] != "PROOF_1":
        raise LogicBoundaryError("Not a finite proof Gödel code")
    steps = []
    for item in tree[1:]:
        if (type(item) is not list or len(item) != 4
                or type(item[1]) is not str or type(item[2]) is not list):
            raise LogicBoundaryError("Malformed encoded proof step")
        f = _unmarshal(item[0])
        term = _unmarshal(item[3]) if item[3] is not None else None
        steps.append(ProofStep(f, item[1], tuple(item[2]), term))
    proof = FiniteProof(tuple(steps))
    if encode_proof(proof) != code:
        raise LogicBoundaryError("Noncanonical finite proof code")
    return proof


def verifies_proof_code(theory: Theory, proof_code: int, goal: Formula) -> bool:
    """Decidable for EACH finite code. This is not a Con(PA) algorithm."""
    if not isinstance(goal, Formula):
        raise LogicBoundaryError("Goal must be an object-language formula")
    try:
        p = decode_proof(proof_code)
        return p.conclusion == goal and check_finite_proof(theory, p)
    except (LogicBoundaryError, ValueError, TypeError):
        return False
