"""Independent exact controls for X07; no first-generation executable imported.

Finite controls are receipts, not a checker for the universal face proof.
Run from any directory; only the three scoped X07 artifacts are written.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
import json
import platform
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "19bd7ec89e88ff2b76a322a82cb9d9b606df3e41"


def mat(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def zero(n):
    return mat([[0] * n for _ in range(n)])


def add(a, b):
    return mat([[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)])


def scale(a, c):
    return mat([[Q(c) * x for x in row] for row in a])


def mul(a, b):
    return mat([[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
                 for j in range(len(b[0]))] for i in range(len(a))])


def transpose(a):
    return tuple(zip(*a))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def diag(v):
    return mat([[v[i] if i == j else 0 for j in range(len(v))]
                for i in range(len(v))])


def tensor(a, b):
    return mat([[x * y for x in ar for y in br] for ar in a for br in b])


def branch(ks, x):
    y = zero(len(ks[0]))
    for k in ks:
        y = add(y, mul(mul(k, x), transpose(k)))
    return y


def effect(ks):
    out = zero(len(ks[0][0]))
    for k in ks:
        out = add(out, mul(transpose(k), k))
    return out


EVENTS = ("a_read", "a_reset", "b_read", "b_reset")
PREDS = {"a_read": set(), "a_reset": {"a_read"},
         "b_read": set(), "b_reset": {"b_read"}}


def ideals():
    return [frozenset(c) for r in range(5) for c in combinations(EVENTS, r)
            if all(PREDS[e] <= set(c) for e in c)]


def extensions(ideal):
    return [p for p in permutations(sorted(ideal))
            if all(PREDS[e] <= set(p[:i]) for i, e in enumerate(p))]


def step(e, q):
    bit = 0 if e.startswith("a") else 1
    mask = 2 if bit == 0 else 1
    if e.endswith("read"):
        return None if q & mask else (q, Q(9, 25))
    return (q | mask, Q(16, 25))


def classical_matrix(e):
    out = [[Q(0)] * 16 for _ in range(16)]
    for s in range(4):
        for q in range(4):
            nxt = step(e, q)
            if nxt is not None:
                q1, w = nxt
                out[4 * s + q1][4 * s + q] = w
    return mat(out)


def direct_hidden_path(word, source, current):
    weight = Q(1)
    for event in word:
        nxt = step(event, current)
        if nxt is None:
            return zero(16)[0]
        current, w = nxt
        weight *= w
    result = [Q(0)] * 16
    result[4 * source + current] = weight
    return tuple(result)


def compose(word, maps, size):
    result = eye(size)
    for event in word:
        result = mul(maps[event], result)
    return result


def positive_controls():
    ms = {e: classical_matrix(e) for e in EVENTS}
    ii = ideals()
    ts = {}
    direct_points = 0
    for ideal in ii:
        words = extensions(ideal)
        ts[ideal] = compose(words[0], ms, 16)
        for word in words:
            actual = compose(word, ms, 16)
            assert actual == ts[ideal]
            for s in range(4):
                for q in range(4):
                    assert tuple(row[4 * s + q] for row in actual) == direct_hidden_path(word, s, q)
                    direct_points += 1
    zeros = {i: {j for j in range(16) if not any(row[j] for row in t)}
             for i, t in ts.items()}
    assert all(zeros[i] <= zeros[j] for i in ii for j in ii if i <= j)
    maximal = max(ii, key=lambda i: len(zeros[i]))
    assert all(zeros[i] <= zeros[maximal] for i in ii)
    assert all(any(sum(row[4*s+s] for row in ts[i]) > 0 for s in range(4)) for i in ii)
    assert all(sum(row[0] for row in ts[i]) > 0 for i in ii)
    p0, p1, ident = diag([1, 0]), diag([0, 1]), eye(2)
    reset = (mat([[0, 0], [1, 0]]), p1)
    local_read = (scale(p0, Q(3, 5)),)
    local_reset = tuple(scale(k, Q(4, 5)) for k in reset)
    assert effect(local_read + (scale(p0, Q(4, 5)), p1)) == ident
    assert effect(local_reset + tuple(scale(k, Q(3, 5)) for k in reset)) == ident
    ks = {"a_read": tuple(tensor(k, ident) for k in local_read),
          "a_reset": tuple(tensor(k, ident) for k in local_reset),
          "b_read": tuple(tensor(ident, k) for k in local_read),
          "b_reset": tuple(tensor(ident, k) for k in local_reset)}
    bases = [mat([[int(r == i and c == j) for c in range(4)] for r in range(4)])
             for i in range(4) for j in range(4)]
    square_points = 0
    for a in EVENTS[:2]:
        for b in EVENTS[2:]:
            for x in bases:
                assert branch(ks[b], branch(ks[a], x)) == branch(ks[a], branch(ks[b], x))
                square_points += 1
    # Compare each classical current transition with its diagonal CP realization.
    diagonal_points = 0
    quantum_effects = {}
    for ideal in ii:
        effect_diagonal = []
        for q in range(4):
            rho = diag([int(j == q) for j in range(4)])
            for e in extensions(ideal)[0]:
                rho = branch(ks[e], rho)
            current = [ts[ideal][j][q] for j in range(4)]
            assert rho == diag(current)
            effect_diagonal.append(trace(rho))
            diagonal_points += 1
        quantum_effects[",".join(sorted(ideal))] = effect_diagonal
    full = frozenset(EVENTS)
    weight = sum(row[0] for row in ts[full])
    assert weight == Q(20736, 390625)
    assert [j for j, row in enumerate(ts[full]) if row[0]] == [3]
    return {"ideals": len(ii), "full_linear_extensions": len(extensions(full)),
            "direct_hidden_path_points": direct_points, "CP_square_basis_points": square_points,
            "diagonal_intertwiner_points": diagonal_points,
            "local_instrument_completions": 2,
            "attained_bottleneck_ideal": sorted(maximal),
            "maximal_zero_face_coordinates": len(zeros[maximal]),
            "common_original_source": "original=00,current=00",
            "changed_terminal_current": "11", "full_likelihood": weight,
            "quantum_effect_diagonals": quantum_effects}


def hostile_controls():
    p0, p1 = diag([1, 0]), diag([0, 1])
    plus = scale(mat([[1, 1], [1, 1]]), Q(1, 2))
    minus = scale(mat([[1, -1], [-1, 1]]), Q(1, 2))
    # Individual thread compatibility is not joint-ideal compatibility.
    assert trace(branch((p0,), p0)) == trace(branch((p1,), p1)) == 1
    assert branch((p1,), branch((p0,), eye(2))) == zero(2)
    fresh = [[trace(branch((p,), x)) for x in (p0, p1)] for p in (p0, p1)]
    assert fresh == [[1, 0], [0, 1]]
    # Total Lüders channels commute, every report-indexed square is still required.
    total_z, total_x = (p0, p1), (plus, minus)
    units = [mat([[int(r == i and c == j) for c in range(2)] for r in range(2)])
             for i in range(2) for j in range(2)]
    assert all(branch(total_x, branch(total_z, x)) == branch(total_z, branch(total_x, x)) for x in units)
    zx = trace(branch((plus,), branch((p0,), p0)))
    xz = trace(branch((p0,), branch((plus,), p0)))
    assert (zx, xz) == (Q(1, 2), Q(1, 4))
    # Enabledness fails even where a vacuous endpoint comparison says nothing.
    forward = ["flip", "probe_at_zero"]
    reverse = list(reversed(forward))
    def legal(word):
        q = 0
        for e in word:
            if e == "flip":
                q = 1 - q
            elif q != 0:
                return False
        return True
    assert not legal(forward) and legal(reverse)
    # Same original/current marginals, same terminal reset, unequal original posterior.
    laws = ([Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8)],
            [Q(1, 8), Q(3, 8), Q(3, 8), Q(1, 8)])
    posts = []
    for p in laws:
        assert [p[0]+p[1], p[2]+p[3]] == [Q(1, 2)] * 2
        assert [p[0]+p[2], p[1]+p[3]] == [Q(1, 2)] * 2
        posts.append(p[0]/(p[0]+p[2]))
    assert posts == [Q(3, 4), Q(1, 4)]
    # A long plateau is not a certificate of maximal attained face.
    delayed = [eye(2)] * 23 + [p0]
    ranks = []
    accum = eye(2)
    for k in delayed:
        accum = mul(k, accum)
        ranks.append(sum(any(row[j] for row in accum) for j in range(2)))
    assert ranks == [2] * 23 + [1]
    # Hidden memory gives different likelihoods for exactly the same reduced state.
    memory_panel = [[int(k >= n) for k in range(6)] for n in range(1, 7)]
    assert memory_panel[0][0] == 0 and memory_panel[0][1] == 1
    assert all(any(row) for row in memory_panel[:-1]) and not any(memory_panel[-1])
    # Universal product copying is nonlinear; basis copying loses coherent marginals.
    avg = scale(add(p0, p1), Q(1, 2))
    clone_avg = tensor(avg, avg)
    avg_clone = scale(add(tensor(p0, p0), tensor(p1, p1)), Q(1, 2))
    assert clone_avg != avg_clone
    assert diag([plus[0][0], plus[1][1]]) != plus
    # An unfaithful mass functional can hide nonzero output later revealed.
    unfaithful_u = lambda v: v[0]
    x = (Q(0), Q(1))
    assert unfaithful_u(x) == 0 and unfaithful_u((x[1], x[0])) == 1
    # No lower bound/infinite-event probability follows from stable zero faces.
    decay = [Q(1, 2**n) for n in range(1, 13)]
    assert all(x > 0 for x in decay) and decay[-1] == Q(1, 4096)
    return {"separate_threads_supports": [[0], [1]], "union_support": [],
            "fresh_terminal_likelihood_rows": fresh,
            "summed_channels_commute_basis_points": len(units),
            "noncommuting_report_likelihoods": [zx, xz],
            "enabled_orders": {"forward": False, "reverse": True},
            "same_marginals_original_posteriors": posts,
            "late_drop_at": 24, "late_ranks": ranks,
            "omitted_memory_tail_panel": memory_panel,
            "nonlinear_copy_diagonals": [[clone_avg[i][i] for i in range(4)],
                                         [avg_clone[i][i] for i in range(4)]],
            "unfaithful_mass_zero_not_absorbing": [0, 1],
            "positive_finite_decay": decay}


def native_smoke():
    sys.path.insert(0, str(ROOT))
    from observational_succ.quantum_records import Instrument, QuantumObserver
    ins = Instrument("X07_RationalCoin", (("selected", scale(eye(2), Q(3, 5))),
                                         ("other", scale(eye(2), Q(4, 5)))))
    observer = QuantumObserver.initial_state()
    for _ in range(3):
        observer = observer.advance(ins, "selected")
    assert observer.verify({ins.name: ins})
    assert observer.joint_probability == Q(9, 25)**3
    return {"selected_simulated_events": len(observer.records),
            "joint_probability": observer.joint_probability, "replay": True,
            "hardware_contact": False}


def exact_json(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: exact_json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [exact_json(v) for v in x]
    return x


def main():
    paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
             "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
             "observational_succ/quantum_records.py", "observational_succ/noncommuting_proof_transport.py",
             "research/2026-10-13/SWARM_ATLAS/PROTOCOL.md",
             "research/2026-10-13/SWARM_ATLAS/C17.md", "research/2026-10-13/SWARM_ATLAS/C22.md",
             "research/2026-10-13/SWARM_ATLAS/C19.md", "reviews/C19_RX_REVIEW.md",
             "research/2026-10-13/SWARM_ATLAS/A07.md"]
    missing_origin = subprocess.run(["git", "cat-file", "-t",
            "ba075348b7bcc66d938b3e0ca96c26e95bba340a"], cwd=ROOT, capture_output=True, text=True)
    native_origins = {"observational_succ/quantum_records.py": "4e95c4ce9481d79fdd14a777e8eb1abb64d5b594",
                      "observational_succ/noncommuting_proof_transport.py": "89caebe3289ffd1ca97b4c30f4af00c4c990b828"}
    native_original_hashes = {}
    for path, commit in native_origins.items():
        original = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        native_original_hashes[path] = {"originating_commit": commit, "sha256": sha256(original).hexdigest(),
                                         "current_byte_identical": original == (ROOT/path).read_bytes()}
    receipt = {"schema": "X07-exact-controls-v1", "source_parent": PARENT,
               "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
               "python": platform.python_version(),
               "command": "PYTHONDONTWRITEBYTECODE=1 python research/2026-10-13/SWARM_ATLAS/X07_probe.py",
               "exit_code": 0, "proof_status": "PROVED LOCAL derivation; pending independent non-deriver review",
               "probe_status": "TESTED MODEL; finite controls do not prove universal claims",
               "independence": "Fresh exact matrix and direct hidden-path implementations; same deriver; no author probes imported",
               "positive": positive_controls(), "hostile": hostile_controls(), "native_smoke": native_smoke(),
               "source_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
               "native_origin_objects": native_original_hashes,
               "imported_origin_object": {"commit": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
                                          "exit_code": missing_origin.returncode,
                                          "stdout": missing_origin.stdout.strip(),
                                          "stderr": missing_origin.stderr.strip()},
               "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
               "dossier_sha256": sha256((HERE/"X07.md").read_bytes()).hexdigest(),
               "primary_sources_opened": ["https://arxiv.org/html/1908.07021v8",
                    "https://www.cl.cam.ac.uk/~gw104/winskel-nielsen-models-for-concurrency.pdf",
                    "https://arxiv.org/pdf/quant-ph/0107090", "https://arxiv.org/abs/1408.0049"],
               "boundaries": ["No full suite/compiler/push", "No imported or shared metadata changes",
                              "No independent acceptance yet", "No hardware/cognition/RH claim"]}
    (HERE/"X07_RECEIPT.json").write_text(json.dumps(exact_json(receipt), indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "PASS finite controls", "ideals": receipt["positive"]["ideals"],
                      "native_replay": receipt["native_smoke"]["replay"], "exit_code": 0}))


if __name__ == "__main__":
    main()
