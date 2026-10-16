"""Source-indexed, simply typed finite-observation lambda calculus.

Observations are declared finite recorded rows, not an instrument that can
query an unbounded source. Projection and CRT joins are *derived* reports,
never new measurements. No primitive asserts an omega-stage or a Weil sign.
This module is independent of optional packages and operates on exact ints.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, lcm


class LambdaError(ValueError):
    """Malformed program or finite mathematical model."""


class TypeFault(LambdaError):
    """Source/type/index mismatch; never a mathematical refutation."""


class AccessGap(LambdaError):
    """Requested observation was not performed in the finite source atlas."""


class BudgetGap(LambdaError):
    """Finite execution resource exhausted; logical outcome unresolved."""


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise LambdaError(f"expected an exact integer >= {minimum}")
    return n


def _prime(p: int) -> int:
    _nat(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise LambdaError("FUCC requires a true prime generator (composites are words)")
    return p


@dataclass(frozen=True)
class Passport:
    source_id: str
    epoch: int
    basis: str = "modular-Z"

    def __post_init__(self):
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise LambdaError("declared nonempty source_id required")
        _nat(self.epoch)
        if not isinstance(self.basis, str) or not self.basis.strip():
            raise LambdaError("declared nonempty basis required")


@dataclass(frozen=True)
class Atlas:
    """Recorded finite modular observations; pairwise coherence is verified.

    A compatible finite table admits CRT solutions but does not attest a
    physical source or a single ordinary integer for an infinite tower.
    """
    passport: Passport
    rows: tuple[tuple[int, int], ...]

    def __post_init__(self):
        if not isinstance(self.passport, Passport) or type(self.rows) is not tuple:
            raise LambdaError("atlas needs a passport and immutable observation rows")
        previous = 0
        for n, r in self.rows:
            _nat(n, 2)
            _nat(r)
            if n <= previous or r >= n:
                raise LambdaError("rows must be sorted, unique, and canonical modulo n")
            previous = n
        for i, (m, a) in enumerate(self.rows):
            for n, b in self.rows[:i]:
                if (a - b) % gcd(m, n):
                    raise LambdaError("recorded source observations violate CRT coherence")

    @classmethod
    def from_integer(cls, passport: Passport, integer: int,
                     moduli: tuple[int, ...]) -> "Atlas":
        if type(integer) is not int or type(moduli) is not tuple:
            raise LambdaError("finite integer fixture and tuple of moduli required")
        if len(set(moduli)) != len(moduli):
            raise LambdaError("duplicate recorded moduli")
        return cls(passport, tuple((n, integer % n) for n in sorted(moduli)))

    def observe(self, n: int) -> int:
        _nat(n, 2)
        try:
            return dict(self.rows)[n]
        except KeyError as exc:
            raise AccessGap(f"no performed event at modulus {n}") from exc


@dataclass(frozen=True)
class BoolT:
    pass


@dataclass(frozen=True)
class ResidueT:
    modulus: int

    def __post_init__(self):
        _nat(self.modulus, 2)


@dataclass(frozen=True)
class ReportT:
    passport: Passport
    modulus: int

    def __post_init__(self):
        if not isinstance(self.passport, Passport):
            raise TypeFault("report source must be a declared passport")
        _nat(self.modulus, 2)


@dataclass(frozen=True)
class PairT:
    left: object
    right: object


@dataclass(frozen=True)
class FuncT:
    arg: object
    result: object
    latent_reads: frozenset[int]


BOOL = BoolT()


@dataclass(frozen=True)
class Var:
    index: int  # de Bruijn index: 0 is nearest binder


@dataclass(frozen=True)
class Lam:
    parameter_type: object
    body: object


@dataclass(frozen=True)
class App:
    function: object
    argument: object


@dataclass(frozen=True)
class Bool:
    value: bool


@dataclass(frozen=True)
class Residue:
    modulus: int
    value: int


@dataclass(frozen=True)
class Read:
    modulus: int


@dataclass(frozen=True)
class Project:
    report: object
    modulus: int


@dataclass(frozen=True)
class Join:
    left: object
    right: object


@dataclass(frozen=True)
class Forget:
    report: object


@dataclass(frozen=True)
class Succ:
    residue: object


@dataclass(frozen=True)
class PrimeMul:
    prime: int
    residue: object


@dataclass(frozen=True)
class Sum:
    left: object
    right: object


@dataclass(frozen=True)
class Eq:
    left: object
    right: object


@dataclass(frozen=True)
class Compatible:
    left: object
    right: object


@dataclass(frozen=True)
class Select:
    condition: object
    yes: object
    no: object


@dataclass(frozen=True)
class Pair:
    left: object
    right: object


@dataclass(frozen=True)
class First:
    pair: object


@dataclass(frozen=True)
class Second:
    pair: object


@dataclass(frozen=True)
class Judgment:
    type: object
    may_read: frozenset[int]


def _merge(*checks: Judgment) -> frozenset[int]:
    return frozenset().union(*(c.may_read for c in checks))


def _validate_type(t: object, passport: Passport) -> None:
    if isinstance(t, BoolT):
        return
    if isinstance(t, ResidueT):
        return
    if isinstance(t, ReportT):
        if t.passport != passport:
            raise TypeFault("foreign source or epoch in a bound report type")
        return
    if isinstance(t, PairT):
        _validate_type(t.left, passport)
        _validate_type(t.right, passport)
        return
    if isinstance(t, FuncT):
        if type(t.latent_reads) is not frozenset:
            raise TypeFault("function effects must be immutable finite sets")
        for n in t.latent_reads:
            _nat(n, 2)
        _validate_type(t.arg, passport)
        _validate_type(t.result, passport)
        return
    raise TypeFault("unknown or ill-formed binder type")


def check(term: object, passport: Passport,
          context: tuple[object, ...] = ()) -> Judgment:
    """Gamma |- term : type ! finite potential reads (no infinite oracle)."""
    if not isinstance(passport, Passport) or type(context) is not tuple:
        raise TypeFault("explicit source passport and typed context required")
    for t in context:
        _validate_type(t, passport)
    if isinstance(term, Var):
        _nat(term.index)
        if term.index >= len(context):
            raise TypeFault("unbound de Bruijn variable")
        return Judgment(context[term.index], frozenset())
    if isinstance(term, Lam):
        _validate_type(term.parameter_type, passport)
        b = check(term.body, passport, (term.parameter_type,) + context)
        return Judgment(FuncT(term.parameter_type, b.type, b.may_read), frozenset())
    if isinstance(term, App):
        f, a = check(term.function, passport, context), check(term.argument, passport, context)
        if not isinstance(f.type, FuncT) or f.type.arg != a.type:
            raise TypeFault("application requires a matching function argument")
        return Judgment(f.type.result, _merge(f, a) | f.type.latent_reads)
    if isinstance(term, Bool):
        if type(term.value) is not bool:
            raise TypeFault("boolean literal must be bool")
        return Judgment(BOOL, frozenset())
    if isinstance(term, Residue):
        _nat(term.modulus, 2)
        if type(term.value) is not int or not 0 <= term.value < term.modulus:
            raise TypeFault("residue literal must be canonical exact integer")
        return Judgment(ResidueT(term.modulus), frozenset())
    if isinstance(term, Read):
        _nat(term.modulus, 2)
        return Judgment(ReportT(passport, term.modulus), frozenset((term.modulus,)))
    if isinstance(term, Project):
        r = check(term.report, passport, context)
        if not isinstance(r.type, ReportT) or r.type.passport != passport:
            raise TypeFault("projection requires an indexed report from this source")
        _nat(term.modulus, 2)
        if r.type.modulus % term.modulus:
            raise TypeFault("projection must follow divisibility")
        return Judgment(ReportT(passport, term.modulus), r.may_read)
    if isinstance(term, Join):
        a, b = check(term.left, passport, context), check(term.right, passport, context)
        if (not isinstance(a.type, ReportT) or not isinstance(b.type, ReportT)
                or a.type.passport != b.type.passport or a.type.passport != passport):
            raise TypeFault("CRT join requires two reports from the identical source and epoch")
        return Judgment(ReportT(passport, lcm(a.type.modulus, b.type.modulus)), _merge(a, b))
    if isinstance(term, Forget):
        r = check(term.report, passport, context)
        if not isinstance(r.type, ReportT) or r.type.passport != passport:
            raise TypeFault("forgetting provenance requires a correctly sourced report")
        return Judgment(ResidueT(r.type.modulus), r.may_read)
    if isinstance(term, (Succ, PrimeMul)):
        a = check(term.residue, passport, context)
        if not isinstance(a.type, ResidueT):
            raise TypeFault("SUCC and FUCC act on residues, not on source records")
        if isinstance(term, PrimeMul):
            _prime(term.prime)
        return Judgment(a.type, a.may_read)
    if isinstance(term, (Sum, Eq)):
        a, b = check(term.left, passport, context), check(term.right, passport, context)
        if not isinstance(a.type, ResidueT) or a.type != b.type:
            raise TypeFault("sum/equality require residues in the same cyclic carrier")
        return Judgment(a.type if isinstance(term, Sum) else BOOL, _merge(a, b))
    if isinstance(term, Compatible):
        a, b = check(term.left, passport, context), check(term.right, passport, context)
        if (not isinstance(a.type, ReportT) or not isinstance(b.type, ReportT)
                or a.type.passport != b.type.passport or a.type.passport != passport):
            raise TypeFault("coherence comparison cannot mix sources or epochs")
        return Judgment(BOOL, _merge(a, b))
    if isinstance(term, Select):
        c, a, b = (check(x, passport, context)
                   for x in (term.condition, term.yes, term.no))
        if c.type != BOOL or a.type != b.type:
            raise TypeFault("select requires bool condition and identical branch types")
        return Judgment(a.type, _merge(c, a, b))
    if isinstance(term, Pair):
        a, b = check(term.left, passport, context), check(term.right, passport, context)
        return Judgment(PairT(a.type, b.type), _merge(a, b))
    if isinstance(term, (First, Second)):
        x = check(term.pair, passport, context)
        if not isinstance(x.type, PairT):
            raise TypeFault("projection requires a product")
        return Judgment(x.type.left if isinstance(term, First) else x.type.right,
                        x.may_read)
    raise TypeFault("unknown term constructor; untyped Python execution is forbidden")


@dataclass(frozen=True)
class Report:
    passport: Passport
    modulus: int
    value: int
    lineage: tuple[str, ...]


@dataclass(frozen=True)
class _Closure:
    body: object
    environment: tuple[object, ...]
    context_types: tuple[object, ...]
    parameter_type: object


@dataclass(frozen=True)
class Execution:
    type: object
    value: object
    may_read: frozenset[int]
    observed: tuple[int, ...]
    steps: int
    passport: Passport
    status: str = "FINITE_MODEL_EXECUTED"
    globally_complete: bool = False


def _join(x: Report, y: Report) -> Report:
    if x.passport != y.passport:
        raise TypeFault("runtime source mismatch")
    g = gcd(x.modulus, y.modulus)
    if (y.value - x.value) % g:
        raise LambdaError("CRT incompatibility: no coherent source report")
    kmod = y.modulus // g
    k = (((y.value - x.value) // g) * pow(x.modulus // g, -1, kmod)) % kmod if kmod > 1 else 0
    n = lcm(x.modulus, y.modulus)
    return Report(x.passport, n, (x.value + x.modulus*k) % n,
                  x.lineage + y.lineage + (f"derived:crt:{x.modulus},{y.modulus}->{n}",))


def execute(term: object, atlas: Atlas, *, max_steps: int = 10000,
            max_read_bits: int = 10000) -> Execution:
    """Call-by-value normalization of a closed typed term on a finite tape.

    Branch selection is lazy; static may-read is a conservative footprint.
    Budgets are execution controls, never proof that a claim is false.
    """
    if not isinstance(atlas, Atlas):
        raise LambdaError("execute needs a finite recorded source atlas")
    _nat(max_steps)
    _nat(max_read_bits)
    typing = check(term, atlas.passport)
    observed: list[int] = []
    steps = 0
    read_bits = 0

    def ev(t: object, env: tuple[object, ...], types: tuple[object, ...]) -> object:
        nonlocal steps, read_bits
        steps += 1
        if steps > max_steps:
            raise BudgetGap("evaluation fuel exhausted")
        if isinstance(t, Var):
            return env[t.index]
        if isinstance(t, Lam):
            return _Closure(t.body, env, types, t.parameter_type)
        if isinstance(t, App):
            f, a = ev(t.function, env, types), ev(t.argument, env, types)
            if not isinstance(f, _Closure):
                raise TypeFault("nonfunction reached evaluator")
            return ev(f.body, (a,) + f.environment, (f.parameter_type,) + f.context_types)
        if isinstance(t, Bool):
            return t.value
        if isinstance(t, Residue):
            return t.value
        if isinstance(t, Read):
            read_bits += t.modulus.bit_length()
            if read_bits > max_read_bits:
                raise BudgetGap("finite probing budget exhausted")
            r = atlas.observe(t.modulus)
            observed.append(t.modulus)
            return Report(atlas.passport, t.modulus, r, (f"replay:recorded:{t.modulus}",))
        if isinstance(t, Project):
            r = ev(t.report, env, types)
            return Report(r.passport, t.modulus, r.value % t.modulus,
                          r.lineage + (f"derived:project:{r.modulus}->{t.modulus}",))
        if isinstance(t, Join):
            return _join(ev(t.left, env, types), ev(t.right, env, types))
        if isinstance(t, Forget):
            return ev(t.report, env, types).value
        if isinstance(t, Succ):
            return (ev(t.residue, env, types) + 1) % check(t.residue, atlas.passport, types).type.modulus
        if isinstance(t, PrimeMul):
            return (t.prime * ev(t.residue, env, types)) % check(t.residue, atlas.passport, types).type.modulus
        if isinstance(t, Sum):
            return (ev(t.left, env, types) + ev(t.right, env, types)) % check(t.left, atlas.passport, types).type.modulus
        if isinstance(t, Eq):
            return ev(t.left, env, types) == ev(t.right, env, types)
        if isinstance(t, Compatible):
            x, y = ev(t.left, env, types), ev(t.right, env, types)
            return (x.value - y.value) % gcd(x.modulus, y.modulus) == 0
        if isinstance(t, Select):
            return ev(t.yes if ev(t.condition, env, types) else t.no, env, types)
        if isinstance(t, Pair):
            return (ev(t.left, env, types), ev(t.right, env, types))
        if isinstance(t, First):
            return ev(t.pair, env, types)[0]
        if isinstance(t, Second):
            return ev(t.pair, env, types)[1]
        raise TypeFault("missing evaluator case")

    try:
        value = ev(term, (), ())
    except RecursionError as exc:
        raise BudgetGap("Python stack exhausted; no mathematical verdict") from exc
    return Execution(typing.type, value, typing.may_read,
                     tuple(observed), steps, atlas.passport)


@dataclass(frozen=True)
class Agreement:
    footprint: frozenset[int]
    status: str
    same_output: bool | None
    globally_complete: bool = False


def _ground(t: object) -> bool:
    if isinstance(t, PairT):
        return _ground(t.left) and _ground(t.right)
    return isinstance(t, (BoolT, ResidueT, ReportT))


def compare_observers(term: object, left: Atlas, right: Atlas) -> Agreement:
    """Finite-footprint agreement theorem, *only* for closed ground results.

    If all potential primitive reads agree, structural induction and CBV
    determinism show identical outputs. Disagreement doesn't imply that the
    specific program distinguishes the candidates (unused reads are possible).
    """
    if left.passport != right.passport:
        raise TypeFault("cannot identify distinct source passports")
    judgment = check(term, left.passport)
    if not _ground(judgment.type):
        raise TypeFault("function-valued outputs have latent, unexecuted effects")
    needed = judgment.may_read
    if any(n not in dict(a.rows) for a in (left, right) for n in needed):
        return Agreement(needed, "ACCESS_GAP", None)
    if any(dict(left.rows)[n] != dict(right.rows)[n] for n in needed):
        return Agreement(needed, "NOT_CERTIFIED", None)
    a = execute(term, left)
    b = execute(term, right)
    if a.value != b.value:
        raise AssertionError("finite-support extensionality violated")
    return Agreement(needed, "CERTIFIED_FINITE_AGREEMENT", True)


@dataclass(frozen=True)
class FiniteSign:
    """Exact finite quadratic witness on a *declared* matrix, not a Weil source."""
    energy: Fraction
    status: str
    finite_only: bool = True
    source_is_authenticated: bool = False
    proves_rh: bool = False


def signed_witness(matrix: tuple[tuple[object, ...], ...],
                   vector: tuple[object, ...]) -> FiniteSign:
    """Independently replayable finite negativity; no global sign promotion."""
    if type(matrix) is not tuple or type(vector) is not tuple or not vector:
        raise LambdaError("nonempty exact finite matrix/vector required")
    n = len(vector)
    if len(matrix) != n or any(type(row) is not tuple or len(row) != n for row in matrix):
        raise LambdaError("square matrix dimensions required")
    if any(type(x) not in (int, Fraction) for row in matrix for x in row) or any(
            type(x) not in (int, Fraction) for x in vector):
        raise LambdaError("int or Fraction only; no float/bool sign certificates")
    if not any(vector):
        raise LambdaError("nonzero vector required")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise LambdaError("real symmetric matrix required")
    q = sum((Fraction(vector[i])*Fraction(matrix[i][j])*Fraction(vector[j])
             for i in range(n) for j in range(n)), Fraction(0))
    return FiniteSign(q, "EXACT_FINITE_NEGATIVE" if q < 0 else "NOT_NEGATIVE")
