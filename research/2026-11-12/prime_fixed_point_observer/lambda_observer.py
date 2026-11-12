"""A finite, productive prime observer executed by beta and arithmetic delta.

This dossier module reuses SUCC's repaired de Bruijn ``T`` and
``beta_redex`` implementation.  It is an untyped, weak-head language with
general recursion; it is not the simply typed Lambda--Haar compiler.

The program contains two ordinary fixed-point expressions: trial division
and an increasing stream scan.  There is no primality primitive.  The only
arithmetic primitives are successor, multiplication, remainder, greater-than
and equality.  Church booleans choose branches without evaluating the unused
branch.  Lazy pairs expose a stream head without normalizing its infinite tail.

The budget counts beta/delta contractions, not CPU instructions or bit
operations.  Exhaustion returns UNKNOWN with the already observed prefix.
Finite receipts do not establish Goldbach or an infinite execution result.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Any

from observational_succ.c_monoid_succ_embedding import (
    ABS, APP, CONST, FST, PAIR, SND, T, V, beta_redex,
)


def _nonnegative_int(value: int, name: str) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be an exact nonnegative int")


def nat(value: int) -> T:
    _nonnegative_int(value, "natural literal")
    return CONST(f"nat:{value}")


def _nat_value(term: T) -> int | None:
    if term.tag != "CONST" or not term.name.startswith("nat:"):
        return None
    suffix = term.name[4:]
    if not suffix or not suffix.isascii() or not suffix.isdecimal():
        raise ValueError("malformed natural literal")
    value = int(suffix)
    if str(value) != suffix:
        raise ValueError("noncanonical natural literal")
    return value


# A tiny named *construction* DSL.  Execution uses only inherited T nodes.
def _app(*terms: Any) -> Any:
    result = terms[0]
    for term in terms[1:]:
        result = ("app", result, term)
    return result


def _lam(names: tuple[str, ...], body: Any) -> Any:
    for name in reversed(names):
        body = ("lam", name, body)
    return body


def _compile(term: Any, environment: tuple[str, ...] = ()) -> T:
    if isinstance(term, str):
        if term not in environment:
            raise ValueError(f"unbound program variable: {term}")
        return V(environment.index(term))
    tag, *args = term
    if tag == "lam":
        name, body = args
        return ABS(_compile(body, (name,) + environment))
    if tag == "app":
        return APP(_compile(args[0], environment),
                   _compile(args[1], environment))
    if tag == "pair":
        return PAIR(_compile(args[0], environment),
                    _compile(args[1], environment))
    if tag == "nat":
        return nat(args[0])
    if tag == "prim":
        if args[0] not in _PRIMITIVE_ARITY:
            raise ValueError("unknown arithmetic primitive")
        return CONST(args[0])
    raise ValueError(f"unknown construction tag: {tag}")


_PRIMITIVE_ARITY = {"succ": 1, "mul": 2, "mod": 2, "gt": 2, "eq": 2}
_TRUE = _lam(("yes", "no"), "yes")
_FALSE = _lam(("yes", "no"), "no")
TRUE = _compile(_TRUE)
FALSE = _compile(_FALSE)
_SELF = _lam(("x",), _app("f", _app("x", "x")))
_Y = _lam(("f",), _app(_SELF, _SELF))
Y = _compile(_Y)


def _op(name: str, *arguments: Any) -> Any:
    return _app(("prim", name), *arguments)


# trial n d = if d*d > n then true
#             else if n mod d == 0 then false
#             else trial n (d+1).
_TRIAL_FUNCTIONAL = _lam(
    ("trial", "n", "d"),
    _app(
        _op("gt", _op("mul", "d", "d"), "n"),
        _TRUE,
        _app(
            _op("eq", _op("mod", "n", "d"), ("nat", 0)),
            _FALSE,
            _app("trial", "n", _op("succ", "d")),
        ),
    ),
)
TRIAL_FUNCTIONAL = _compile(_TRIAL_FUNCTIONAL)
_TRIAL = _app(_Y, _TRIAL_FUNCTIONAL)
TRIAL = _compile(_TRIAL)


# scan n = if trial n 2 then Pair(n, scan(n+1)) else scan(n+1).
# PAIR is a lazy constructor.  An observer requests only a finite prefix.
_STREAM_FUNCTIONAL = _lam(
    ("scan", "n"),
    _app(
        _app(_TRIAL, "n", ("nat", 2)),
        ("pair", "n", _app("scan", _op("succ", "n"))),
        _app("scan", _op("succ", "n")),
    ),
)
STREAM_FUNCTIONAL = _compile(_STREAM_FUNCTIONAL)
PRIME_PROGRAM = _compile(_app(_app(_Y, _STREAM_FUNCTIONAL), ("nat", 2)))


def term_data(term: T) -> Any:
    """Canonical finite syntax; no pretty-printer equivalence is assumed."""
    if type(term) is not T:
        raise TypeError("expected the exact inherited term type")
    if term.tag == "VAR":
        return ["VAR", term.idx]
    if term.tag == "CONST":
        return ["CONST", term.name]
    if term.tag == "ABS":
        return ["ABS", term_data(term.body)]
    if term.tag in ("APP", "PAIR"):
        return [term.tag, term_data(term.f), term_data(term.a)]
    if term.tag in ("FST", "SND"):
        return [term.tag, term_data(term.f)]
    raise ValueError(f"unknown term tag: {term.tag}")


def program_sha256(term: T = PRIME_PROGRAM) -> str:
    payload = {
        "language": "prime-observer-beta-delta-v1",
        "primitive_meanings": {
            "succ": "n -> n+1",
            "mul": "a,b -> a*b",
            "mod": "a,b -> a%b, b>0",
            "gt": "a,b -> Church(a>b)",
            "eq": "a,b -> Church(a==b)",
            "FST": "Pair(a,b) -> a without forcing b",
            "SND": "Pair(a,b) -> b without forcing a",
        },
        "syntax": term_data(term),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


class _BudgetExhausted(Exception):
    pass


@dataclass
class _Machine:
    max_steps: int
    beta_steps: int = 0
    delta_steps: int = 0

    def spend(self, kind: str) -> None:
        if self.beta_steps + self.delta_steps >= self.max_steps:
            raise _BudgetExhausted
        if kind == "beta":
            self.beta_steps += 1
        elif kind == "delta":
            self.delta_steps += 1
        else:
            raise ValueError("unknown contraction kind")

    def one(self, term: T) -> T | None:
        """One contraction in a weak-head evaluation context, if available."""
        if term.tag == "APP":
            if term.f.tag == "ABS":
                self.spend("beta")
                return beta_redex(term)

            arguments = []
            head = term
            while head.tag == "APP":
                arguments.append(head.a)
                head = head.f
            arguments.reverse()

            if head.tag == "CONST" and head.name in _PRIMITIVE_ARITY:
                arity = _PRIMITIVE_ARITY[head.name]
                if len(arguments) < arity:
                    return None
                values = []
                for index in range(arity):
                    value = _nat_value(arguments[index])
                    if value is None:
                        reduced = self.one(arguments[index])
                        if reduced is None:
                            raise ValueError("arithmetic operand is not a natural literal")
                        arguments[index] = reduced
                        return _apply_terms(head, arguments)
                    values.append(value)

                self.spend("delta")
                operation = head.name
                if operation == "succ":
                    result = nat(values[0] + 1)
                elif operation == "mul":
                    result = nat(values[0] * values[1])
                elif operation == "mod":
                    if values[1] == 0:
                        raise ValueError("remainder by zero")
                    result = nat(values[0] % values[1])
                elif operation == "gt":
                    result = TRUE if values[0] > values[1] else FALSE
                elif operation == "eq":
                    result = TRUE if values[0] == values[1] else FALSE
                else:
                    raise AssertionError("unreachable arithmetic primitive")
                return _apply_terms(result, arguments[arity:])

            reduced = self.one(term.f)
            return APP(reduced, term.a) if reduced is not None else None

        if term.tag in ("FST", "SND"):
            if term.f.tag == "PAIR":
                self.spend("delta")
                return term.f.f if term.tag == "FST" else term.f.a
            reduced = self.one(term.f)
            if reduced is None:
                raise ValueError("projection operand is not a lazy pair")
            return FST(reduced) if term.tag == "FST" else SND(reduced)

        if term.tag in ("VAR", "CONST", "ABS", "PAIR"):
            return None
        raise ValueError(f"unknown term tag: {term.tag}")

    def weak_head(self, term: T) -> T:
        while True:
            reduced = self.one(term)
            if reduced is None:
                return term
            term = reduced


def _apply_terms(head: T, arguments: list[T]) -> T:
    for argument in arguments:
        head = APP(head, argument)
    return head


@dataclass(frozen=True)
class PrefixReceipt:
    requested_count: int
    values: tuple[int, ...]
    beta_steps: int
    delta_steps: int
    max_steps: int
    status: str
    program_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def run_stream_prefix(program: T, count: int, max_steps: int = 1_000_000) -> PrefixReceipt:
    """Observe a generic program.  This function does not assert primality."""
    _nonnegative_int(count, "count")
    _nonnegative_int(max_steps, "max_steps")
    if type(program) is not T:
        raise TypeError("program must be the exact inherited term type")
    fingerprint = program_sha256(program)
    machine = _Machine(max_steps)
    observed: list[int] = []
    current = program
    status = "COMPLETE"
    try:
        for _ in range(count):
            pair = machine.weak_head(current)
            if pair.tag != "PAIR":
                raise ValueError("stream computation did not expose a lazy pair")
            head = machine.weak_head(FST(pair))
            value = _nat_value(head)
            if value is None:
                raise ValueError("stream head is not a natural literal")
            observed.append(value)
            current = SND(pair)
    except _BudgetExhausted:
        status = "UNKNOWN"
    return PrefixReceipt(count, tuple(observed), machine.beta_steps,
                         machine.delta_steps, max_steps, status, fingerprint)


def prime_prefix(count: int, max_steps: int = 1_000_000) -> PrefixReceipt:
    """The first requested primes, or an explicitly incomplete prefix."""
    return run_stream_prefix(PRIME_PROGRAM, count, max_steps)


def reduce_term(term: T, max_steps: int = 1_000_000) -> tuple[T | None, int, int, str]:
    """Small public probe interface for the stated beta/delta semantics."""
    _nonnegative_int(max_steps, "max_steps")
    if type(term) is not T:
        raise TypeError("term must be the exact inherited term type")
    machine = _Machine(max_steps)
    try:
        result = machine.weak_head(term)
    except _BudgetExhausted:
        return None, machine.beta_steps, machine.delta_steps, "UNKNOWN"
    return result, machine.beta_steps, machine.delta_steps, "COMPLETE"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--max-steps", type=int, default=1_000_000)
    arguments = parser.parse_args()
    print(json.dumps(prime_prefix(arguments.count, arguments.max_steps).as_dict(),
                     indent=2, sort_keys=True))
