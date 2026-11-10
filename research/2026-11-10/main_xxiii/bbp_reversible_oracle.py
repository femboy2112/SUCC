"""Exact finite BBP carry oracle with a retained reversible gate history."""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import lcm


Gate = tuple[int, ...]  # X, CNOT or Toffoli, with the target last.


@dataclass(frozen=True)
class CarryOracle:
    denominator: int
    qubits: int
    gates: tuple[Gate, ...]
    seed_residue: tuple[int, ...]
    quotients: tuple[tuple[int, ...], ...]
    remainders: tuple[tuple[int, ...], ...]

    def simulate(self, basis: int, *, inverse: bool = False) -> int:
        """Apply the gate permutation, or its inverse, to a basis state."""
        gates = reversed(self.gates) if inverse else self.gates
        for *controls, target in gates:
            if all((basis >> control) & 1 for control in controls):
                basis ^= 1 << target
        return basis

    def encode_seed(self, seed: Fraction) -> int:
        """Use qubit 0 for the negative integer part and encode the residue."""
        seed = Fraction(seed)
        integral = seed.numerator // seed.denominator
        residue = (seed - integral) * self.denominator
        if integral not in (-1, 0) or residue.denominator != 1:
            raise ValueError("seed must belong to [-1, 1) on the oracle lattice")
        return (-integral) | sum(
            ((residue.numerator >> bit) & 1) << wire
            for bit, wire in enumerate(self.seed_residue)
        )

    def decode_history(self, basis: int) -> tuple[tuple[int, int, int], ...]:
        """Return (integer part, winding residue, chronological carry) per step."""
        integral = -(basis & 1)
        history = []
        for quotient, remainder in zip(self.quotients, self.remainders, strict=True):
            carry = _read(basis, quotient)
            integral = 16 * integral + carry
            history.append((integral, _read(basis, remainder), carry))
        return tuple(history)

    def completed_phase(self, basis: int, n: int) -> Fraction:
        """Decode the exact finite completed phase at index n in [0, L]."""
        if not 0 <= n <= len(self.quotients):
            raise ValueError("completed index must belong to [0, L]")
        integral, residue, _ = self.decode_history(basis)[-1]
        return Fraction(
            integral * self.denominator + residue,
            self.denominator * 16 ** (len(self.quotients) - n),
        )

    def gate_counts(self) -> dict[str, int]:
        names = ("X", "CNOT", "Toffoli")
        counts = Counter(len(gate) for gate in self.gates)
        return {name: counts[arity] for arity, name in enumerate(names, 1)}


def _read(basis: int, wires: tuple[int, ...]) -> int:
    return sum(((basis >> wire) & 1) << bit for bit, wire in enumerate(wires))


class _Circuit:
    def __init__(self):
        self.qubits = 1  # Qubit 0 retains the integer part of the seed.
        self.gates = []

    def allocate(self) -> int:
        wire = self.qubits
        self.qubits += 1
        return wire

    def emit(self, target: int, *controls: int | None) -> None:
        if None not in controls:  # None represents a hardwired zero.
            self.gates.append((*controls, target))

    def add_constant(self, value: tuple[int | None, ...], constant: int) -> tuple[int, ...]:
        """Out-of-place ripple addition with every carry stored in a new wire."""
        carry = None
        outputs = []
        for bit, input_wire in enumerate(value):
            out = self.allocate()
            next_carry = self.allocate()
            self.emit(out, input_wire)
            self.emit(out, carry)
            self.emit(next_carry, input_wire, carry)
            if (constant >> bit) & 1:
                self.emit(out)
                self.emit(next_carry, input_wire)
                self.emit(next_carry, carry)
            outputs.append(out)
            carry = next_carry
        return tuple(outputs)

    def subtract_if_nonnegative(self, value: tuple[int, ...], divisor: int):
        width = len(value)
        trial = self.add_constant(value, (1 << width) - divisor)
        take = self.allocate()
        self.emit(take)
        self.emit(take, trial[-1])
        selected = []
        for original, alternative in zip(value, trial, strict=True):
            out = self.allocate()
            self.emit(out, original)
            self.emit(out, take, original)
            self.emit(out, take, alternative)
            selected.append(out)
        return tuple(selected), take


def build_oracle(length: int) -> CarryOracle:
    if type(length) is not int or length < 1:
        raise ValueError("oracle length must be a positive integer")
    poles = tuple(tuple(8 * j + shift for shift in (1, 4, 5, 6)) for j in range(length))
    denominator = 16 ** length * lcm(*(pole for row in poles for pole in row))
    residue_width = denominator.bit_length()
    width = residue_width + 6
    circuit = _Circuit()
    seed = tuple(circuit.allocate() for _ in range(residue_width))
    residue = seed
    quotients = []
    remainders = []
    for row in poles:
        forcing = sum(
            coefficient * (denominator // pole)
            for coefficient, pole in zip((4, -2, -1, -1), row, strict=True)
        )
        shifted = (None,) * 4 + residue + (None,) * (width - residue_width - 4)
        value = circuit.add_constant(shifted, forcing)
        carry = []
        for bit in reversed(range(5)):
            value, flag = circuit.subtract_if_nonnegative(value, denominator << bit)
            carry.append(flag)
        residue = value[:residue_width]
        quotients.append(tuple(reversed(carry)))
        remainders.append(residue)
    return CarryOracle(
        denominator, circuit.qubits, tuple(circuit.gates), seed,
        tuple(quotients), tuple(remainders),
    )
