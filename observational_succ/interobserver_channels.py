"""Exact one-shot zero-error inter-observer channel with receiver side information.

The finite coloring theorem is classical (Witsenhausen 1976). This module
implements a new-to-project finite exact exhaustive reference solver, NOT a
new coding theorem or a practical optimizer for large graphs.

A source x has (sender observation u(x), receiver side information v(x),
target report t(x)). The sender transmits only e(u), not v. The receiver
decodes target from (e(u), v). Feasibility and authentication of observations
are premises, not established by this graph-theoretic solver.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product


class ZeroErrorChannelError(ValueError):
    pass


@dataclass(frozen=True)
class InterobserverWorld:
    sources: tuple[str, ...]
    sender_views: tuple[str, ...]
    receiver_views: tuple[str, ...]
    targets: tuple[str, ...]

    def __post_init__(self):
        if type(self.sources) is not tuple or not 1 <= len(self.sources) <= 24:
            raise ZeroErrorChannelError("Finite source alphabet required")
        if len(set(self.sources)) != len(self.sources) or any(
            type(s) is not str or not s for s in self.sources
        ):
            raise ZeroErrorChannelError("Source identifiers must be distinct nonempty labels")
        for name, values in (("Sender", self.sender_views), ("Receiver", self.receiver_views),
                             ("Target", self.targets)):
            if type(values) is not tuple or len(values) != len(self.sources) or any(
                type(v) is not str or not v for v in values
            ):
                raise ZeroErrorChannelError(f"{name} must label every source exactly")
        if len(set(self.sender_views)) > 12:
            raise ZeroErrorChannelError("Exhaustive coloring budget: <= 12 sender observations")

    def sender_alphabet(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(self.sender_views))

    def feasibility_conflicts(self) -> tuple[tuple[str, str], ...]:
        """Any same sender-view AND same receiver-view needing distinct target."""
        return tuple(sorted({
            (self.sender_views[i], self.receiver_views[i])
            for i in range(len(self.sources))
            for j in range(i + 1, len(self.sources))
            if self.sender_views[i] == self.sender_views[j]
            and self.receiver_views[i] == self.receiver_views[j]
            and self.targets[i] != self.targets[j]
        }))

    def edges(self) -> tuple[tuple[str, str], ...]:
        """Confusable sender observations when receiver side labels coincide."""
        order = {a: i for i, a in enumerate(self.sender_alphabet())}
        pairs = set()
        for i in range(len(self.sources)):
            for j in range(i + 1, len(self.sources)):
                a, b = self.sender_views[i], self.sender_views[j]
                if (a != b and self.receiver_views[i] == self.receiver_views[j]
                        and self.targets[i] != self.targets[j]):
                    pairs.add((a,b) if order[a] < order[b] else (b,a))
        return tuple(sorted(pairs, key=lambda ab: (order[ab[0]], order[ab[1]])))


@dataclass(frozen=True)
class ExactChannel:
    sender_alphabet: tuple[str, ...]
    colors: tuple[int, ...]
    receiver_decoder: tuple[tuple[int, str, str], ...]
    codewords: int
    fixed_width_bits: int
    confusability_edges: tuple[tuple[str, str], ...]
    exhaustive_minimum_proved: bool

    def encode(self, sender_view: str) -> int:
        if sender_view not in self.sender_alphabet:
            raise ZeroErrorChannelError("Unknown sender observation")
        return self.colors[self.sender_alphabet.index(sender_view)]

    def decode(self, color: int, side_info: str) -> str:
        for a, b, target in self.receiver_decoder:
            if a == color and b == side_info:
                return target
        raise ZeroErrorChannelError("No valid target decoding for message and side information")


def exact_minimum_channel(world: InterobserverWorld) -> ExactChannel:
    """Exhaustively color the confusability graph, proving minimum codewords.

    Enumerates all canonical color assignments for k=1,...,|U|, with
    first-use symmetry breaking. If no valid decoder can exist even with
    a unique code per sender observation, reject as an access gap.
    """
    if not isinstance(world, InterobserverWorld):
        raise ZeroErrorChannelError("A typed finite communication world is required")
    conflicts = world.feasibility_conflicts()
    if conflicts:
        raise ZeroErrorChannelError(
            "Sender plus receiver observation cannot identify target: " + repr(conflicts))
    alphabet = world.sender_alphabet()
    positions = {u:i for i,u in enumerate(alphabet)}
    adjacent = {(positions[a],positions[b]) for a,b in world.edges()}
    adjacent |= {(b,a) for a,b in adjacent}

    def search(k: int):
        solution = [0] * len(alphabet)
        def backtrack(index: int, used_colors: int) -> tuple[int, ...] | None:
            if index == len(alphabet):
                return tuple(solution)
            for color in range(min(used_colors + 1, k)):
                if any((index, j) in adjacent and solution[j] == color
                       for j in range(index)):
                    continue
                solution[index] = color
                candidate = backtrack(index + 1, max(used_colors, color + 1))
                if candidate is not None:
                    return candidate
            return None
        return backtrack(0, 0)

    for count in range(1, len(alphabet) + 1):
        colors = search(count)
        if colors is None:
            continue
        decoder = {}
        for u, v, t in zip(world.sender_views, world.receiver_views, world.targets):
            key = (colors[positions[u]], v)
            if key in decoder and decoder[key] != t:
                raise ArithmeticError("Proper coloring failed to separate target observations")
            decoder[key] = t
        code = ExactChannel(alphabet, colors,
                            tuple(sorted((color, side, value)
                                         for (color, side), value in decoder.items())),
                            len(set(colors)),
                            (len(set(colors)) - 1).bit_length(),
                            world.edges(), True)
        for u, v, t in zip(world.sender_views, world.receiver_views, world.targets):
            if code.decode(code.encode(u), v) != t:
                raise ArithmeticError("Incorrect zero-error encoder/decoder")
        return code
    raise ArithmeticError("A finite graph always has a proper coloring")


def chromatic_channel_demo() -> dict:
    # Receiver context r_ab/r_bc allows ambiguity only along A-B and B-C.
    # A-C never occur with the same receiver view; two colors suffice.
    world = InterobserverWorld(
        ("A_at_ab", "B_at_ab", "B_at_bc", "C_at_bc"),
        ("A", "B", "B", "C"),
        ("ab", "ab", "bc", "bc"),
        ("A", "B", "B", "C"),
    )
    code = exact_minimum_channel(world)
    assert code.codewords == 2 and code.fixed_width_bits == 1
    return {
        "status": "EXACT_INTEROBSERVER_ZERO_ERROR_CHANNEL",
        "sender_view_count": len(code.sender_alphabet),
        "minimum_codewords": code.codewords,
        "minimum_fixed_width_bits": code.fixed_width_bits,
        "naive_sender_id_fixed_width_bits": (len(code.sender_alphabet) - 1).bit_length(),
        "edges": [list(p) for p in code.confusability_edges],
        "decoder_reconstructs_all_targets": True,
        "physical_source_authentication_claimed": False,
        "optimal_variable_length_bits_claimed": False,
        "RH_claimed": False,
    }
