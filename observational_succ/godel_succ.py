"""Finite observational SUCC for Pi^0_1 sentences; NOT an infinite truth oracle.

A two-counter program has INC(register,next_pc), DECJZ(register,positive_pc,zero_pc),
and HALT. It starts at pc=0 with both counters zero. Survival for n steps is
decidable, while survival for *every* n is a nonhalting statement.

There is no infinite elapsed computation, PA proof checker, or arithmetic
Weil-form construction in this toy. An all-clear prefix is never "proved".
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

Instruction = tuple
Program = tuple[Instruction, ...]


class GodelSuccError(ValueError):
    """Invalid finite observation or two-counter program."""


@dataclass(frozen=True)
class PrefixVerdict:
    horizon: int
    status: str
    first_counterexample: int | None

    @property
    def universal_claim_proved(self) -> bool:
        return False  # observation, however long, is not a universal proof


def _budget(horizon: int) -> int:
    if type(horizon) is not int or not 0 <= horizon <= 100_000:
        raise GodelSuccError("horizon must be an integer in [0,100000]")
    return horizon


def observe_pi1_prefix(predicate: Callable[[int], bool], horizon: int) -> PrefixVerdict:
    """Check P(0),...,P(horizon), never treating a pass as universal closure."""
    _budget(horizon)
    for n in range(horizon + 1):
        result = predicate(n)
        if type(result) is not bool:
            raise GodelSuccError("predicate must return an exact Boolean")
        if not result:
            return PrefixVerdict(horizon, "refuted", n)
    return PrefixVerdict(horizon, "unresolved", None)


def validate_program(program: Sequence[Instruction]) -> Program:
    """Fully validate reachable *and* unreachable instructions before execution."""
    if type(program) not in (tuple, list) or not 1 <= len(program) <= 4096:
        raise GodelSuccError("program must have 1..4096 instructions")
    p = tuple(program)
    for pc, op in enumerate(p):
        if type(op) is not tuple or not op:
            raise GodelSuccError(f"invalid instruction at {pc}")
        if op[0] == "HALT":
            valid = len(op) == 1
        elif op[0] == "INC":
            valid = (len(op) == 3 and type(op[1]) is int and op[1] in (0, 1)
                     and type(op[2]) is int and 0 <= op[2] < len(p))
        elif op[0] == "DECJZ":
            valid = (len(op) == 4 and type(op[1]) is int and op[1] in (0, 1)
                     and all(type(x) is int and 0 <= x < len(p) for x in op[2:]))
        else:
            valid = False
        if not valid:
            raise GodelSuccError(f"invalid instruction at {pc}: {op!r}")
    return p


def _first_halt_validated(p: Program, transitions: int) -> int | None:
    """One bounded run. Return first HALT transition count, else None."""
    _budget(transitions)
    pc = 0
    counters = [0, 0]
    for tick in range(transitions + 1):
        op = p[pc]
        if op[0] == "HALT":
            return tick
        if tick == transitions:
            break
        if op[0] == "INC":
            _, reg, next_pc = op
            counters[reg] += 1
            pc = next_pc
        else:
            _, reg, if_positive, if_zero = op
            if counters[reg] > 0:
                counters[reg] -= 1
                pc = if_positive
            else:
                pc = if_zero
    return None


def halted_by(program: Sequence[Instruction], transitions: int) -> bool:
    """Decide whether the two-counter program halts within n transitions."""
    return _first_halt_validated(validate_program(program), transitions) is not None


def machine_prefix(program: Sequence[Instruction], horizon: int) -> PrefixVerdict:
    """Observe nonhalting up to n with one run, not quadratic resimulation."""
    first = _first_halt_validated(validate_program(program), horizon)
    return PrefixVerdict(horizon, "refuted" if first is not None else "unresolved", first)


def delayed_halt(transitions: int) -> Program:
    """A controlled failure first appearing at exactly n transitions."""
    if type(transitions) is not int or not 1 <= transitions <= 4095:
        raise GodelSuccError("delay must be an integer in [1,4095]")
    return tuple(("INC", 0, pc + 1) for pc in range(transitions)) + (("HALT",),)


def two_counter_loop() -> Program:
    """Known elementary loop; its nonhalting proof is not the finite monitor."""
    return (("INC", 0, 1), ("DECJZ", 0, 0, 0))


def rational_kernel(psi: Callable[[int], int], t: int, u: int) -> int:
    """Exact finite toy screw-kernel: this is NOT Suzuki's Psi."""
    if type(t) is not int or type(u) is not int:
        raise GodelSuccError("integer toy probe times required")
    return psi(t) + psi(u) - psi(t-u)  # assumes even psi, psi(0)=0


def delayed_ramp(base: Callable[[int], int], threshold: int, amplitude: int):
    """Toy delayed impulse, with integer threshold instead of Suzuki's log(m)."""
    if type(threshold) is not int or threshold <= 0 or type(amplitude) is not int:
        raise GodelSuccError("positive integer threshold and integer amplitude required")
    return lambda t: base(t) - amplitude * max(0, abs(t) - threshold)


if __name__ == "__main__":
    import json
    loop = two_counter_loop()
    delayed = delayed_halt(25)
    print(json.dumps({
        "loop_through_7": machine_prefix(loop, 7).__dict__,
        "delayed_through_7": machine_prefix(delayed, 7).__dict__,
        "delayed_through_25": machine_prefix(delayed, 25).__dict__,
        "performed_infinite_execution": False,
        "RH_proved": False, "PA_consistency_proved": False,
    }, indent=2))
