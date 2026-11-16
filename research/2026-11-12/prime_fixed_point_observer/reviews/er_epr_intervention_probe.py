"""Exact channel intervention controls; no gravitational simulation.

Reuses the reviewed Gaussian-rational matrix primitives, but constructs the
chosen-message wire, controlled channel and response experiment explicitly.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

from coherent_path_adversary_probe import (
    Q, ZERO, ONE, I, mat, eye, dagger, mul, tensor, scale, plus,
    trace, density, transform, keep_right, moment, rho_gamma,
)


def permutation_gate(count, action):
    rows = [[0] * (2 ** count) for _ in range(2 ** count)]
    for source in range(2 ** count):
        bits = [(source >> (count - 1 - j)) & 1 for j in range(count)]
        out = action(bits)
        target = sum(bit << (count - 1 - j) for j, bit in enumerate(out))
        rows[target][source] = 1
    return mat(rows)


def run():
    counts = Counter()

    def check(group, condition):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group]))

    ident = eye(2)
    x = mat([[0, 1], [1, 0]])
    y = mat([[0, -I], [I, 0]])
    z = mat([[1, 0], [0, -1]])
    phi = rho_gamma(ONE)
    wire = permutation_gate(3, lambda bits: [bits[2], bits[1], bits[0]])
    check("wire_calibration", mul(dagger(wire), wire) == eye(8))
    no_wire_outputs, wire_outputs = [], []
    for message in (0, 1):
        message_state = density([1 - message, message])
        source = tensor(message_state, phi)  # M, A, B
        local_encoding = tensor(ident, tensor(x if message else ident, ident))
        no_wire = transform(local_encoding, source)
        communicated = transform(wire, source)
        no_wire_output = keep_right(no_wire, 4, 2)
        wire_output = keep_right(communicated, 4, 2)
        no_wire_outputs.append(no_wire_output)
        wire_outputs.append(wire_output)
        check("fresh_message", no_wire_output == scale(ident, F(1, 2)))
        check("fresh_message", wire_output == message_state)
        check("fresh_message", moment(no_wire_output, z) == ZERO)
        check("fresh_message", moment(wire_output, z) == Q(1 - 2 * message))
        check("wire_coherence", trace(mul(communicated, communicated)) == ONE)
    check("fresh_message", no_wire_outputs[0] == no_wire_outputs[1])
    check("fresh_message", wire_outputs[0] != wire_outputs[1])
    check("fresh_message", mul(wire_outputs[0], wire_outputs[1]) == scale(ident, 0))

    p0, p1 = mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]])
    branches = (tensor(p0, ident), tensor(p1, x))
    controlled = plus(*branches)
    check("controlled_calibration", mul(dagger(controlled), controlled) == eye(4))

    def measured_controlled(rho):
        return plus(*(transform(branch, rho) for branch in branches))

    # Exact complete finite linear-basis check, not only fitted states.
    for row in range(4):
        for column in range(4):
            entries = [[0] * 4 for _ in range(4)]
            entries[row][column] = 1
            source = mat(entries)
            coherent = transform(controlled, source)
            measured = measured_controlled(source)
            check("receiver_channel_matrix_units", keep_right(coherent, 2, 2) == keep_right(measured, 2, 2))

    source = density([1, 0, 1, 0])
    coherent, measured = transform(controlled, source), measured_controlled(source)
    xx = tensor(x, x)
    check("joint_output_boundary", coherent == phi)
    check("joint_output_boundary", measured == rho_gamma(ZERO))
    check("joint_output_boundary", keep_right(coherent, 2, 2) == keep_right(measured, 2, 2))
    check("joint_output_boundary", moment(coherent, xx) == ONE)
    check("joint_output_boundary", moment(measured, xx) == ZERO)

    # Convention: the input intervention is exp(-i s A), hence response +i[A,B_back].
    a, b = tensor(y, ident), tensor(ident, z)
    uncoupled_commutator = plus(mul(a, b), scale(mul(b, a), -1))
    b_back = mul(mul(dagger(controlled), b), controlled)
    coupled_commutator = plus(mul(a, b_back), scale(mul(b_back, a), -1))
    check("signed_response", I * moment(source, uncoupled_commutator) == ZERO)
    check("signed_response", I * moment(source, coupled_commutator) == Q(-2))
    check("signed_response", b_back == tensor(z, z))

    return {
        "schema": "succ.er-epr-intervention.v1", "status": "PASS",
        "checks": sum(counts.values()), "checks_by_group": dict(counts),
        "message_control": {"without_wire_Z_by_message": ["0", "0"],
                            "with_wire_Z_by_message": ["1", "-1"]},
        "restricted_equivalence": "Receiver channels agree on all 16 input matrix units; joint outputs differ on a specified pure input.",
        "response_convention": "Input exp(-i s A); derivative = i Tr(rho [A,V* B V]).",
        "scope": "Exact finite quantum channel controls. No bulk metric, traversable wormhole, objective collapse or arithmetic theorem is simulated or established.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")
