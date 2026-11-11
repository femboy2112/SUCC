"""A typed, source-anchored finite lambda compiler with exact delta primitives.

The target uses the repaired de Bruijn beta substitution from
``c_monoid_succ_embedding``. Arithmetic is an explicit, closed set of delta
rules, not an asserted encoding of rational arithmetic in pure lambda calculus.
Every accepted source state retains its clock, unwrapped value and literal seed.
Certificate verification recomputes three exact arithmetic paths. A successful
finite reduction certifies neither statistical contraction nor pi normality.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json

from . import c_monoid_succ_embedding as lc
from .duck_bbp import forcing, source_tail_budget


SOURCE_SPEC = (
    "BBP/base=16/clock=N0/four-poles="
    "4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)/source-v1"
)
SOURCE_DIGEST = sha256(SOURCE_SPEC.encode("ascii")).hexdigest()
RAT, STATE = "Rational", "SourceState"


class CompilerError(ValueError):
    """Malformed syntax, source mismatch, or invalid finite certificate."""


def _nat(value: int, name: str = "clock", minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise CompilerError(f"{name} must be an exact integer >= {minimum}")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise CompilerError("an exact int or Fraction is required")
    return Q(value)


def _four_pole(n: int) -> Q:
    _nat(n, "source index", 1)
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def _checked_source(n: int) -> Q:
    value = forcing(n)
    if type(value) is not Q or value != _four_pole(n):
        raise CompilerError("source primitive failed four-pole authentication")
    return value


def source_prefix(clock: int) -> Q:
    """P_n, using the factored numerator/denominator source implementation."""
    _nat(clock)
    return sum((forcing(j)/16**j for j in range(1, clock+1)), Q())


@dataclass(frozen=True)
class SourceState:
    clock: int
    value: Q
    seed: Q = Q()
    source_digest: str = SOURCE_DIGEST

    def __post_init__(self) -> None:
        _nat(self.clock)
        object.__setattr__(self, "value", _rational(self.value))
        object.__setattr__(self, "seed", _rational(self.seed))
        if type(self.source_digest) is not str or self.source_digest != SOURCE_DIGEST:
            raise CompilerError("source passport does not match the fixed four-pole source")


@dataclass(frozen=True)
class SourceCertificate:
    state: SourceState
    prefix_seed: Q
    reverse_seed: Q
    forward_value: Q
    original_zero: bool
    status: str = "FINITE_SOURCE_IDENTITIES_VERIFIED"


def certify_state(state: SourceState, *, require_zero: bool = True) -> SourceCertificate:
    """Recompute three paths; a label or claimed zero is not sufficient.

    Prefix uses canonical rational-polynomial forcing; forward and reverse
    paths use the original four partial fractions. These are different
    implementations of the same identity, not independent empirical sources.
    """
    if type(state) is not SourceState or type(require_zero) is not bool:
        raise CompilerError("a SourceState and boolean zero requirement are required")
    # Revalidate even a dataclass altered through low-level object mutation.
    _nat(state.clock)
    if type(state.value) is not Q or type(state.seed) is not Q:
        raise CompilerError("stored source values and seeds must be exact Fractions")
    if type(state.source_digest) is not str or state.source_digest != SOURCE_DIGEST:
        raise CompilerError("wrong source passport")
    prefix_seed = state.value/16**state.clock-source_prefix(state.clock)
    reverse_seed = state.value
    for j in range(state.clock, 0, -1):
        reverse_seed = (reverse_seed-_four_pole(j))/16
    forward_value = state.seed
    for j in range(1, state.clock+1):
        forward_value = 16*forward_value+_four_pole(j)
    if (prefix_seed != state.seed or reverse_seed != state.seed
            or forward_value != state.value):
        raise CompilerError("source state does not agree with its declared seed and clock")
    if require_zero and state.seed != 0:
        raise CompilerError("nonzero seed: the original-zero source requirement failed")
    return SourceCertificate(state, prefix_seed, reverse_seed, forward_value,
                             state.seed == 0)


def verify_source_certificate(certificate: SourceCertificate) -> bool:
    """Replay every field; rejects a forged status or stored arithmetic value."""
    if type(certificate) is not SourceCertificate:
        raise CompilerError("a source certificate is required")
    if (any(type(value) is not Q for value in (certificate.prefix_seed,
            certificate.reverse_seed, certificate.forward_value))
            or type(certificate.original_zero) is not bool
            or type(certificate.status) is not str):
        raise CompilerError("certificate fields must have exact declared types")
    expected = certify_state(certificate.state, require_zero=False)
    if certificate != expected:
        raise CompilerError("source certificate fields do not match replay")
    return True


@dataclass(frozen=True)
class CompletionCertificate:
    state: SourceState
    horizon: int
    lower: Q
    upper: Q
    finite_tail: Q
    remainder_bound: Q
    source_certificate: SourceCertificate
    status: str = "FINITE_COMPLETION_ENCLOSURE_VERIFIED"


def complete_state(state: SourceState, horizon: int) -> CompletionCertificate:
    """Enclose U_n(s)+T_n=16^n(s+pi/16), in the unwrapped real chart.

    The upper remainder is the inherited proved monotone-source budget
    16^(n-L)*r(L+1)/15. No floating pi oracle is used. Classical BBP identifies
    the completed source sum with pi/16; this function does not reprove BBP.
    """
    cert = certify_state(state, require_zero=False)
    _nat(horizon, "horizon", state.clock)
    tail = sum((_four_pole(j)/16**(j-state.clock)
                for j in range(state.clock+1, horizon+1)), Q())
    lower = state.value+tail
    independent = 16**state.clock*(state.seed+source_prefix(horizon))
    if lower != independent:
        raise CompilerError("finite completion square does not commute")
    error = source_tail_budget(horizon)/16**(horizon-state.clock)
    if error != _four_pole(horizon+1)/(15*16**(horizon-state.clock)):
        raise CompilerError("tail budget failed independent source check")
    return CompletionCertificate(state, horizon, lower, lower+error, tail, error, cert)


def verify_completion_certificate(certificate: CompletionCertificate) -> bool:
    if type(certificate) is not CompletionCertificate:
        raise CompilerError("a completion certificate is required")
    if any(type(value) is not Q for value in (certificate.lower, certificate.upper,
            certificate.finite_tail, certificate.remainder_bound)):
        raise CompilerError("completion fields must be exact Fractions")
    if type(certificate.status) is not str:
        raise CompilerError("completion status must be an exact string")
    verify_source_certificate(certificate.source_certificate)
    expected = complete_state(certificate.state, certificate.horizon)
    if certificate != expected:
        raise CompilerError("completion certificate does not match exact replay")
    return True


@dataclass(frozen=True)
class Arrow:
    argument: object
    result: object


@dataclass(frozen=True)
class Literal:
    value: Q


@dataclass(frozen=True)
class Variable:
    index: int


@dataclass(frozen=True)
class Lambda:
    argument_type: object
    body: object


@dataclass(frozen=True)
class Apply:
    function: object
    argument: object


@dataclass(frozen=True)
class Primitive:
    name: str


def _type_valid(typ: object) -> None:
    if type(typ) is str and typ in (RAT, STATE):
        return
    if type(typ) is Arrow:
        _type_valid(typ.argument)
        _type_valid(typ.result)
        return
    raise CompilerError("unknown type")


def _forcing_index(name: str) -> int | None:
    if type(name) is not str or not name.startswith("forcing:"):
        return None
    digits = name[len("forcing:"):]
    if not digits.isascii() or not digits.isdecimal() or digits.startswith("0"):
        raise CompilerError("forcing index must be a canonical positive decimal integer")
    return int(digits)


def primitive_type(name: str) -> object:
    signatures = {"origin": Arrow(RAT, STATE), "step": Arrow(STATE, STATE),
                  "recover": Arrow(STATE, RAT), "add": Arrow(RAT, Arrow(RAT, RAT)),
                  "divide16": Arrow(RAT, RAT)}
    if type(name) is not str:
        raise CompilerError("primitive name must be text")
    if name in signatures:
        return signatures[name]
    if _forcing_index(name) is not None:
        return RAT
    raise CompilerError("unknown arithmetic primitive")


def infer(term: object, context: tuple[object, ...] = ()) -> object:
    """Simply typed source grammar; no runtime Python callbacks or eval."""
    if type(context) is not tuple:
        raise CompilerError("immutable typed context required")
    for typ in context:
        _type_valid(typ)
    if type(term) is Literal:
        _rational(term.value)
        return RAT
    if type(term) is Primitive:
        return primitive_type(term.name)
    if type(term) is Variable:
        _nat(term.index, "de Bruijn index")
        if term.index >= len(context):
            raise CompilerError("unbound variable")
        return context[term.index]
    if type(term) is Lambda:
        _type_valid(term.argument_type)
        return Arrow(term.argument_type, infer(term.body, (term.argument_type,)+context))
    if type(term) is Apply:
        fn, arg = infer(term.function, context), infer(term.argument, context)
        if type(fn) is not Arrow or fn.argument != arg:
            raise CompilerError("application type mismatch")
        return fn.result
    raise CompilerError("unknown source term")


def _rat_token(value: Q) -> str:
    value = _rational(value)
    return f"q:{value.numerator}/{value.denominator}"


def _state_token(state: SourceState) -> str:
    return "s:"+json.dumps([state.clock, str(state.value), str(state.seed),
                            state.source_digest], separators=(",", ":"))


def _decode(term: lc.T) -> Q | SourceState | None:
    if type(term) is not lc.T or term.tag != "CONST":
        return None
    token = term.name
    if token.startswith("q:"):
        try:
            result = Q(token[2:])
        except (ValueError, ZeroDivisionError) as exc:
            raise CompilerError("bad rational constant") from exc
        if token != _rat_token(result):
            raise CompilerError("noncanonical rational constant")
        return result
    if token.startswith("s:"):
        try:
            fields = json.loads(token[2:])
            if type(fields) is not list or len(fields) != 4:
                raise ValueError("wrong state arity")
            state = SourceState(fields[0], Q(fields[1]), Q(fields[2]), fields[3])
        except (TypeError, ValueError, ZeroDivisionError) as exc:
            raise CompilerError("bad source constant") from exc
        if token != _state_token(state):
            raise CompilerError("noncanonical source constant")
        certify_state(state, require_zero=False)
        return state
    return None


def _lower(term: object) -> lc.T:
    if type(term) is Literal:
        return lc.CONST(_rat_token(term.value))
    if type(term) is Variable:
        return lc.V(term.index)
    if type(term) is Lambda:
        return lc.ABS(_lower(term.body))
    if type(term) is Apply:
        return lc.APP(_lower(term.function), _lower(term.argument))
    if type(term) is Primitive:
        return lc.CONST("p:"+term.name)
    raise CompilerError("unknown source term")


@dataclass(frozen=True)
class Program:
    source: object
    code: lc.T
    result_type: object
    source_digest: str = SOURCE_DIGEST


def compile_term(term: object) -> Program:
    typ = infer(term)
    return Program(term, _lower(term), typ)


def _validate_target(term: lc.T) -> None:
    """Reject subclass equality hooks before comparing or interpreting code.

    Every field, including fields inactive for its tag, is checked. No supplied
    object can redefine equality while masquerading as a target token or node.
    """
    if type(term) is not lc.T:
        raise CompilerError("target nodes must have the exact declared type")
    if type(term.tag) is not str or type(term.name) is not str:
        raise CompilerError("target tags and tokens must be exact strings")
    _nat(term.idx, "target variable index")
    if term.tag not in ("VAR", "ABS", "APP", "CONST"):
        raise CompilerError("target tag outside the compiler fragment")
    for child in (term.body, term.f, term.a):
        if child is not None:
            _validate_target(child)
    if term.tag == "VAR":
        canonical = term.name == "" and all(x is None for x in (term.body, term.f, term.a))
    elif term.tag == "CONST":
        canonical = term.idx == 0 and all(x is None for x in (term.body, term.f, term.a))
    elif term.tag == "ABS":
        canonical = (term.idx == 0 and term.name == "" and type(term.body) is lc.T
                     and term.f is None and term.a is None)
    else:
        canonical = (term.idx == 0 and term.name == "" and term.body is None
                     and type(term.f) is lc.T and type(term.a) is lc.T)
    if not canonical:
        raise CompilerError("target node has noncanonical active or inactive fields")


def verify_program(program: Program) -> bool:
    if (type(program) is not Program or type(program.source_digest) is not str
            or program.source_digest != SOURCE_DIGEST):
        raise CompilerError("wrong compiler/source passport")
    _type_valid(program.result_type)
    _validate_target(program.code)
    # infer recursively rejects every source AST subclass and ill-typed field
    # before dataclass equality is allowed to inspect the supplied source.
    expected = compile_term(program.source)
    if program != expected:
        raise CompilerError("compiled code or type does not match its source term")
    return True


def state_term(clock: int, seed: int | Q = Q()) -> object:
    """Iterate the lambda program (lambda state. step state), from origin."""
    _nat(clock)
    value = Apply(Primitive("origin"), Literal(_rational(seed)))
    advance = Lambda(STATE, Apply(Primitive("step"), Variable(0)))
    for _ in range(clock):
        value = Apply(advance, value)
    return value


def compile_state(clock: int, seed: int | Q = Q()) -> Program:
    return compile_term(state_term(clock, seed))


def guarded_tail_term(clock: int, depth: int) -> object:
    """Finite F_r^depth(0)_clock; not a terminating untyped Y combinator.

    Builds (r(n+1)+(r(n+2)+...+r(n+depth)/16...)/16)/16
    using explicit source/add/divide primitives. Each depth is finite.
    """
    _nat(clock)
    _nat(depth, "depth")
    term: object = Literal(Q())
    for j in range(clock+depth, clock, -1):
        unfolding = Lambda(RAT, Apply(Primitive("divide16"),
                           Apply(Apply(Primitive("add"), Primitive(f"forcing:{j}")),
                                 Variable(0))))
        term = Apply(unfolding, term)
    return term


def _delta(term: lc.T) -> lc.T | None:
    if term.tag == "CONST" and term.name.startswith("p:forcing:"):
        index = _forcing_index(term.name[2:])
        return lc.CONST(_rat_token(_checked_source(index)))
    if term.tag != "APP":
        return None
    fun, arg = term.f, _decode(term.a)
    if fun.tag == "CONST" and fun.name.startswith("p:") and arg is not None:
        name = fun.name[2:]
        if name == "origin" and type(arg) is Q:
            return lc.CONST(_state_token(SourceState(0, arg, arg)))
        if name == "step" and type(arg) is SourceState:
            result = SourceState(arg.clock+1, 16*arg.value+_checked_source(arg.clock+1), arg.seed)
            return lc.CONST(_state_token(result))
        if name == "recover" and type(arg) is SourceState:
            recovered = arg.value/16**arg.clock-source_prefix(arg.clock)
            return lc.CONST(_rat_token(recovered))
        if name == "divide16" and type(arg) is Q:
            return lc.CONST(_rat_token(arg/16))
    if (fun.tag == "APP" and fun.f.tag == "CONST" and fun.f.name == "p:add"):
        left = _decode(fun.a)
        if type(left) is Q and type(arg) is Q:
            return lc.CONST(_rat_token(left+arg))
    return None


def _step(term: lc.T, strategy: str) -> tuple[lc.T, str | None]:
    """One beta/delta contraction, preserving actual reductions in the count."""
    if strategy == "normal":
        beta = lc.beta_redex(term)
        if beta is not None:
            return beta, "beta"
        delta = _delta(term)
        if delta is not None:
            return delta, "delta"
    if term.tag == "ABS":
        body, rule = _step(term.body, strategy)
        if rule:
            return lc.ABS(body), rule
    elif term.tag == "APP":
        fun, rule = _step(term.f, strategy)
        if rule:
            return lc.APP(fun, term.a), rule
        arg, rule = _step(term.a, strategy)
        if rule:
            return lc.APP(term.f, arg), rule
    elif term.tag not in ("CONST", "VAR"):
        raise CompilerError("target constructor outside this compiler fragment")
    if strategy == "applicative":
        beta = lc.beta_redex(term)
        if beta is not None:
            return beta, "beta"
        delta = _delta(term)
        if delta is not None:
            return delta, "delta"
    return term, None


@dataclass(frozen=True)
class Execution:
    status: str
    value: Q | SourceState | lc.T | None
    reduct: lc.T
    result_type: object
    beta_steps: int
    delta_steps: int
    source_digest: str = SOURCE_DIGEST
    statistical_contraction_proved: bool = False


def run(program: Program, *, max_steps: int = 10000, strategy: str = "normal") -> Execution:
    """Normalize a compiled closed term or return explicit budget-unresolved.

    The budget counts beta/delta contractions, not integer bit complexity or
    host-language recursion depth. No failed budget is a mathematical refutation.
    """
    verify_program(program)
    _nat(max_steps, "max_steps")
    if type(strategy) is not str or strategy not in ("normal", "applicative"):
        raise CompilerError("unknown reduction strategy")
    term, betas, deltas = program.code, 0, 0
    for spent in range(max_steps+1):
        next_term, rule = _step(term, strategy)
        if rule is None:
            value = _decode(term)
            if program.result_type == STATE and type(value) is not SourceState:
                raise CompilerError("ground state program did not return a source state")
            if program.result_type == RAT and type(value) is not Q:
                raise CompilerError("ground rational program did not return a rational")
            if type(value) is SourceState:
                certify_state(value, require_zero=False)
            return Execution("FINITE_REDUCTION_VERIFIED", value if value is not None else term,
                             term, program.result_type, betas, deltas)
        if spent == max_steps:
            return Execution("UNRESOLVED_BUDGET", None, term, program.result_type, betas, deltas)
        betas += int(rule == "beta")
        deltas += int(rule == "delta")
        term = next_term
    raise AssertionError("unreachable")
