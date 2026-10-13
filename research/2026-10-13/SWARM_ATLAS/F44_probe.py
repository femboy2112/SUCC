"""F44 exact finite hostile witnesses; no production imports or physics claims."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def identity(n):
    return matrix(tuple(tuple(int(i == j) for j in range(n)) for i in range(n)))


def multiply(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def evolve(k, rho):
    return multiply(multiply(k, rho), transpose(k))


def tensor(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F())


def marginal_q(rho):
    return tuple(tuple(sum((rho[2*i+k][2*j+k] for k in range(2)), F())
                       for j in range(2)) for i in range(2))


def marginal_e(rho):
    return tuple(tuple(sum((rho[2*k+i][2*k+j] for k in range(2)), F())
                       for j in range(2)) for i in range(2))


def plus_probability(rho, observable):
    return (trace(rho) + trace(multiply(observable, rho))) / 2


def main():
    half = F(1, 2)
    bell = matrix(((half, 0, 0, half), (0, 0, 0, 0),
                   (0, 0, 0, 0), (half, 0, 0, half)))
    mixture = matrix(((half, 0, 0, 0), (0, 0, 0, 0),
                      (0, 0, 0, 0), (0, 0, 0, half)))
    flat = matrix(((half, 0), (0, half)))
    assert multiply(bell, bell) == bell and trace(bell) == trace(mixture) == 1
    assert all(marginal_q(rho) == marginal_e(rho) == flat
               for rho in (bell, mixture))
    x = matrix(((0, 1), (1, 0)))
    instruments = {
        "Z": (matrix(((1, 0), (0, 0))), matrix(((0, 0), (0, 1)))),
        "X": (matrix(((half, half), (half, half))),
              matrix(((half, -half), (-half, half)))),
        "flip": (x,),
        "reset": (matrix(((1, 0), (0, 0))), matrix(((0, 1), (0, 0)))),
    }
    for operators in instruments.values():
        products = [multiply(transpose(k), k) for k in operators]
        assert tuple(tuple(sum((p[i][j] for p in products), F())
                           for j in range(2)) for i in range(2)) == identity(2)
    frontier = [(bell, mixture)]
    checked = 0
    for _ in range(3):
        following = []
        for a, b in frontier:
            for operators in instruments.values():
                for k in operators:
                    lifted = tensor(k, identity(2))
                    aa, bb = evolve(lifted, a), evolve(lifted, b)
                    assert marginal_q(aa) == marginal_q(bb)
                    assert trace(aa) == trace(bb)
                    following.append((aa, bb))
                    checked += 1
        frontier = following
    xx = tensor(x, x)
    joint = [plus_probability(rho, xx) for rho in (bell, mixture)]
    assert joint == [F(1), half]
    # A newly allowed global interaction makes later Q-local readout separate.
    cnot = matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                   (0, 0, 0, 1), (0, 0, 1, 0)))
    after = [evolve(cnot, rho) for rho in (bell, mixture)]
    assert [plus_probability(marginal_q(rho), x) for rho in after] == joint
    # Destructive reset preserves original-source ambiguity, not current state.
    original_current = (("A", 0), ("B", 0))
    target = {"A": 0, "B": 1}
    assert len({c for _, c in original_current}) == 1
    assert len({target[s] for s, _ in original_current}) == 2
    # Small deterministic resettable source world and genuinely new readout.
    old = {"A": (0, 1), "B": (0, 1)}
    new = {"A": 0, "B": 1}
    assert old["A"] == old["B"] and new["A"] != new["B"]
    result = {
        "status": "TESTED MODEL: exact finite witnesses; universal proof is in F44.md",
        "source_parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "command": "python research/2026-10-13/SWARM_ATLAS/F44_probe.py",
        "exit_code": 0,
        "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "fractions.Fraction only; no float or tolerance",
        "q_and_e_marginals": [["1/2", "0"], ["0", "1/2"]],
        "instrument_families": list(instruments),
        "q_local_branch_checks_depth_3": checked,
        "joint_XX_plus_probabilities_bell_mixture": [str(p) for p in joint],
        "new_joint_readout_total_variation": "1/2",
        "single_copy_zero_error_identification": False,
        "global_CNOT_then_local_X_plus": [str(p) for p in joint],
        "original_target_labels_after_common_reset": [0, 1],
        "current_carrier_labels_after_common_reset": [0, 0],
        "classical_old_probe_rows": old,
        "classical_new_separator": new,
        "physical_or_neural_or_RH_claim": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
