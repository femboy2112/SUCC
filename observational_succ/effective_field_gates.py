"""Effective Simple/IdealHard/Fucked SUCC interfaces (classical, relative).

A finite monitor is not a proof checker for global computation. Computability
of a source-dependent limit, source-realization, observational uniqueness,
and formal mathematical provability must stay separately typed.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


class FieldGateError(ValueError):
    """Malformed source/program/probe or a false finite-certification premise."""


def _natural(n: int, name: str, ceiling: int | None = None) -> int:
    if type(n) is not int or n < 0 or (ceiling is not None and n > ceiling):
        raise FieldGateError(f"{name} must be an exact nonnegative integer in budget")
    return n


def cantor_pair(a: int, b: int) -> int:
    _natural(a, "first paired integer")
    _natural(b, "second paired integer")
    return (a + b) * (a + b + 1) // 2 + b


def cantor_unpair(z: int) -> tuple[int, int]:
    from math import isqrt
    _natural(z, "paired integer")
    w = (isqrt(8*z + 1) - 1)//2
    t = w * (w + 1)//2
    b = z - t
    return w - b, b


def encode_counter_program(program: tuple[tuple[int, ...], ...]) -> int:
    """Explicit surjection N -> all finite 2-counter instructions/programs.

    Opcode: 0 HALT, 1/2 INC0/1(next), 3/4 DECJZ0/1(ifpos,ifzero).
    Code is a natural-number nested Cantor-cons list. Decoding arbitrary
    nonnegative codes always halts, including malformed index targets.
    """
    if type(program) is not tuple:
        raise FieldGateError("Program must be a finite tuple")
    code = 0
    for op in reversed(program):
        if type(op) is not tuple or not op or type(op[0]) is not int:
            raise FieldGateError("Malformed instruction")
        kind = op[0]
        if kind == 0 and len(op) == 1:
            word = 0
        elif kind in (1, 2) and len(op) == 2:
            word = kind + 5*_natural(op[1], "next instruction")
        elif kind in (3, 4) and len(op) == 3:
            word = kind + 5*cantor_pair(_natural(op[1], "positive jump"),
                                         _natural(op[2], "zero jump"))
        else:
            raise FieldGateError("Malformed instruction arity")
        code = 1 + cantor_pair(word, code)
    return code


def decode_counter_program(index: int) -> tuple[tuple[int, ...], ...]:
    """All positive program codes decode finitely; 0 is empty/implicit halt."""
    _natural(index, "program index")
    operations = []
    while index:
        word, index = cantor_unpair(index - 1)
        kind, value = word % 5, word // 5
        if kind == 0:
            operations.append((0,))
        elif kind in (1, 2):
            operations.append((kind, value))
        else:
            pos, zero = cantor_unpair(value)
            operations.append((kind, pos, zero))
    return tuple(operations)


def bounded_self_output(index: int, steps: int) -> int | None:
    """Simulate indexed two-counter program on its *own* natural index.

    If it halts within steps transitions, output R0 modulo 2. Unbounded
    indexed code family is universal (classical two-counter theorem); a
    bounded run is only a finite observation, never a halting oracle.
    """
    _natural(index, "program index", 2**60)
    _natural(steps, "finite simulation budget", 2000)
    program = decode_counter_program(index)
    pc, c = 0, [index, 0]
    for tick in range(steps + 1):
        if pc >= len(program):
            return c[0] % 2
        op = program[pc]
        if op[0] == 0:
            return c[0] % 2
        if tick == steps:
            return None
        if op[0] in (1, 2):
            c[op[0]-1] += 1
            pc = op[1]
        else:
            reg = op[0]-3
            if c[reg]:
                c[reg] -= 1
                pc = op[1]
            else:
                pc = op[2]
    return None


def diagonal_tree_admissible(bits: tuple[int, ...]) -> bool:
    """Decidable membership in a finite level of an infinite computable tree.

    T={sigma : for e<|sigma|, if machine e(e) halts by |sigma|
    transitions with bit b, then sigma[e]!=b}. Prefix closed.
    """
    if (type(bits) is not tuple or len(bits)>48 or
            any(type(b) is not int or b not in (0,1) for b in bits)):
        raise FieldGateError("Bounded binary prefix required")
    n = len(bits)
    return all((out := bounded_self_output(e,n)) is None or bits[e] != out
               for e in range(n))


def diagonal_tree_level_witness(depth: int) -> tuple[int, ...]:
    """Computes SOME node at finite depth; NOT compatible chosen global path."""
    _natural(depth,"tree horizon",48)
    word=tuple(0 if (bit:=bounded_self_output(e,depth)) is None else 1-bit
               for e in range(depth))
    assert diagonal_tree_admissible(word)
    return word


def tree_level_report(depth: int) -> dict:
    """No path returned, no false 'computably realized' certificate."""
    word=diagonal_tree_level_witness(depth)
    return {"finite_depth":depth,"finite_node":list(word),
            "finite_node_is_admissible":True,
            "prefix_consistency_with_previous_level_asserted":False,
            "infinite_path_constructed_by_code":False,
            "mathematical_existence_requires_classical_tree_argument":True,
            "any_infinite_path_computable":False}


@dataclass(frozen=True)
class AutomaticSource:
    """A genuinely finite generator, giving proof by exhaustion of its orbit."""
    outputs: tuple[int, ...]
    next_state: tuple[int, ...]
    initial: int = 0

    def __post_init__(self) -> None:
        if (type(self.outputs) is not tuple or not self.outputs or
            len(self.outputs)>512 or type(self.next_state) is not tuple or
            len(self.next_state)!=len(self.outputs) or
            any(type(x) is not int or x not in (0,1) for x in self.outputs) or
            any(type(j) is not int or not 0<=j<len(self.outputs) for j in self.next_state) or
            type(self.initial) is not int or not 0<=self.initial<len(self.outputs)):
            raise FieldGateError("Finite total deterministic source is required")

    def global_zero_certificate(self) -> dict:
        """Finite graph closure proves output bit zero at *all* SUCC stages."""
        seen, order, state = set(), [], self.initial
        while state not in seen:
            seen.add(state)
            order.append(state)
            state = self.next_state[state]
        bad=next((j for j in order if self.outputs[j]!=0),None)
        return {"cycle_entry":state,"reachable_states":order,
                "first_bad_state":bad,"all_future_outputs_zero":bad is None,
                "proof_rule":"finite deterministic reachable-orbit closure",
                "infinite_physical_execution_claimed":False}


def finite_support_shadow(horizon: int) -> dict:
    """Every finite all-ones report is realized by a *different* finite source.

    Source X=c00({0,1}) (eventually zero). Ideal all-ones report has
    compatible finite prefixes but no member in the declared X.
    """
    _natural(horizon,"source horizon",10000)
    return {"formal_prefix":[1]*horizon,
            "realizing_eventually_zero_source":"1^n 0^omega",
            "realizing_source_n":horizon,
            "global_all_ones_source_realized":False,
            "every_finite_prefix_source_realized":True,
            "compactness_of_source_class_assumed":False}


def dark_pair(horizon: int, *, odd_bit_probe_enabled: bool=False) -> dict:
    """Two original source profiles share every even-index probe forever."""
    _natural(horizon, "observer horizon",10000)
    left=(0,)*(2*horizon+2)
    right=list(left)
    right[1]=1
    even_left=left[::2]
    even_right=tuple(right)[::2]
    assert even_left==even_right
    return {"finite_even_probe_prefix":list(even_left),
            "all_even_probes_forever_equal":True,
            "target_bit_one_equal":False,
            "odd_bit_probe_enabled":odd_bit_probe_enabled,
            "conditional_repair_available":odd_bit_probe_enabled,
            "source_identified_from_even_probes":False}


def pulse_finite_adversary(horizon: int) -> dict:
    """Uniformly later pulse defeats 'no pulse' at ANY finite queried horizon."""
    _natural(horizon,"observation horizon",10000)
    return {"all_zero_prefix":[0]*horizon,
            "counterexample_pulse_position":horizon,
            "counterexample_same_observations":True,
            "counterexample_different_ever_pulse_target":True,
            "finite_observation_proves_absence":False}


def halting_gated_pair(program: tuple[tuple, ...], horizon: int) -> dict:
    """Actual bounded machine steps separate two source bits iff HALT seen.

    Detecting whether *some* horizon ever separates the pair is the
    halting problem: no uniform algorithm can classify all such programs.
    """
    from .godel_succ import halted_by, validate_program
    _natural(horizon,"probe horizon",100000)
    normalized=validate_program(program)
    found=halted_by(normalized,horizon)
    return {"finite_horizon":horizon,
            "source_bit_0_observation":0,
            "source_bit_1_observation":int(found),
            "distinguished_by_this_horizon":found,
            "dark_forever_proved_by_failed_prefix":False,
            "full_source_classification_decided":False}


def effective_field_demo() -> dict:
    """Stable exact model receipt; universal statements justified separately."""
    from .godel_succ import delayed_halt, two_counter_loop
    machine=AutomaticSource((0,0,0), (1,2,1),0)
    self_index=encode_counter_program(((0,),))
    n1=diagonal_tree_level_witness(1)
    assert self_index==1 and bounded_self_output(1,2)==1 and n1==(1,)
    mutated=(0,)+n1[1:]
    assert not diagonal_tree_admissible(mutated)
    assert machine.global_zero_certificate()["all_future_outputs_zero"]
    assert not halting_gated_pair(delayed_halt(5),4)["distinguished_by_this_horizon"]
    assert halting_gated_pair(delayed_halt(5),5)["distinguished_by_this_horizon"]
    return {"status":"CLASSICAL_EFFECTIVE_FIELD_GATES_RECEIPT",
            "simple_finite_generator_all_future_zero":True,
            "idealhard_decidable_tree_each_level_nonempty":True,
            "idealhard_computable_infinite_path_constructed":False,
            "idealhard_diagonal_forbidden_program_one_index":self_index,
            "idealhard_first_level_witness":list(n1),
            "fucked_no_source_global_shadow":finite_support_shadow(3)["global_all_ones_source_realized"] is False,
            "fucked_even_probe_dark_pair":dark_pair(2)["all_even_probes_forever_equal"],
            "fucked_pulse_delay_unbounded":pulse_finite_adversary(8)["counterexample_pulse_position"]==8,
            "conditional_halting_probe_delayed":True,
            "conditional_loop_not_certified_nonhalting_by_finite_prefix":not halting_gated_pair(two_counter_loop(),100)["dark_forever_proved_by_failed_prefix"],
            "requires_genuine_original_source_authentication":True,
            "classification_from_finite_survey_only":False,
            "global_weil_sign_or_RH_proved":False}
