"""E39: bounded exact arithmetic cut and source-faithful transport probe.

Independent of every observational_succ module. Integer certificates use trial
division; a separate Eratosthenes oracle and pairwise edge checker audit them.
Run directly; stdout is the deterministic JSON receipt. No external writes.
"""
from collections import deque
from copy import deepcopy
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
if not __debug__:
    raise RuntimeError("E39 exact checks require assertions; optimized Python is refused")


def norm(z):
    return z[0] ** 2 + z[1] ** 2


def integer_source(z):
    return norm(z) if z[0] and z[1] else abs(z[0] or z[1])


def integer_certificate(n):
    if n < 2:
        return {"kind": "small"}
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return {"kind": "composite", "divisor": d}
    return {"kind": "prime", "remainders": [n % d for d in range(2, isqrt(n) + 1)]}


def verify_integer(n, c):
    if c["kind"] == "small":
        assert n < 2, "false small-integer certificate"
        return False
    if c["kind"] == "composite":
        d = c["divisor"]
        assert type(d) is int and 1 < d < n and n % d == 0, "false divisor"
        return False
    assert c["kind"] == "prime" and n >= 2, "false primality type"
    rs = c["remainders"]
    assert len(rs) == isqrt(n) - 1, "incomplete trial-division coverage"
    assert all(type(r) is int and r == n % d and r > 0
               for d, r in enumerate(rs, 2)), "false primality remainder"
    return True


def gaussian(z, certificates):
    n = integer_source(z)
    assert str(n) in certificates, "missing arithmetic certificate"
    rational_prime = verify_integer(n, certificates[str(n)])
    return rational_prime and (bool(z[0] and z[1]) or n % 4 == 3)


def steps(k):
    assert type(k) is int and 0 <= k <= 4, "bounded exact probe domain"
    r = isqrt(k)
    return [(a, b) for a in range(-r, r + 1) for b in range(-r, r + 1)
            if 0 < a * a + b * b <= k]


def component(vertices, edges, root):
    adjacency = {v: [] for v in vertices}
    for u, v, _ in edges:
        adjacency[u].append(v)
    seen = {root}
    queue = deque([root])
    while queue:
        for v in adjacency[queue.popleft()]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


def verify_window(c):
    r, k = c["radius"], c["squared_step"]
    assert type(r) is int and 0 <= r <= 12, "bounded complete window"
    assert type(k) is int and 0 <= k <= 4, "integer squared-distance bound"
    expected = {(a, b) for a in range(-r, r + 1) for b in range(-r, r + 1)
                if gaussian((a, b), c["integer_certificates"])}
    vertices = [tuple(v) for v in c["vertices"]]
    assert all(len(v) == 2 and all(type(x) is int for x in v) for v in vertices), "integer source coordinates"
    assert len(vertices) == len(set(vertices)) and set(vertices) == expected, "vertex completeness"
    # Independent of the generator's step lookup: inspect all ordered pairs.
    edges = [(tuple(u), tuple(v), tuple(s)) for u, v, s in c["darts"]]
    oracle = {(u, v, (v[0] - u[0], v[1] - u[1]))
              for u in expected for v in expected
              if 0 < norm((v[0] - u[0], v[1] - u[1])) <= k}
    assert len(edges) == len(set(edges)) and set(edges) == oracle, "edge or voltage completeness"
    return expected, edges


def verify_cut(c):
    vertices, edges = verify_window(c)
    root = tuple(c["root"])
    assert root in vertices, "root is not a verified Gaussian prime"
    cc = {tuple(z) for z in c["component"]}
    assert cc == component(vertices, edges, root), "component connectivity/completeness"
    boundary = {(u[0] + a, u[1] + b) for u in cc for a, b in steps(c["squared_step"])} - cc
    for v in boundary:
        assert not gaussian(v, c["integer_certificates"]), "unblocked prime neighbor"
    assert boundary == {tuple(z) for z in c["boundary"]}, "boundary completeness"
    return cc, boundary


def replay(path, k, certificates, radius=None):
    for z in path:
        assert gaussian(z, certificates), "nonprime source point"
        if radius is not None:
            assert max(map(abs, z)) <= radius, "path leaves declared window"
    for u, v in zip(path, path[1:]):
        assert 0 < norm((v[0] - u[0], v[1] - u[1])) <= k, "illegal squared-distance edge"
    return (path[-1][0] - path[0][0], path[-1][1] - path[0][1])


def rejected(call):
    try:
        call()
    except (AssertionError, KeyError) as exc:
        return {"rejected": True, "reason": str(exc)}
    raise AssertionError("mutation escaped the verifier")


def main():
    r, k = 12, 2
    window = [(a, b) for a in range(-r, r + 1) for b in range(-r, r + 1)]
    certs = {str(n): integer_certificate(n) for n in sorted({integer_source(z) for z in window})}
    vertices = sorted(z for z in window if gaussian(z, certs))
    vv = set(vertices)
    darts = [(u, (u[0] + a, u[1] + b), (a, b)) for u in vertices for a, b in steps(k)
             if (u[0] + a, u[1] + b) in vv]
    cc = component(vv, darts, (1, 1))
    boundary = {(u[0] + a, u[1] + b) for u in cc for a, b in steps(k)} - cc
    for z in boundary:
        certs.setdefault(str(integer_source(z)), integer_certificate(integer_source(z)))
    c = {"radius": r, "squared_step": k, "root": (1, 1), "vertices": vertices,
         "darts": darts, "component": sorted(cc), "boundary": sorted(boundary),
         "integer_certificates": certs}
    checked, halo = verify_cut(c)
    assert len(checked) == 100 and len(halo) == 265
    # Separate integer sieve: no certificate/remainder-generation call.
    prime_flags = [True] * (max(map(int, certs)) + 1)
    prime_flags[0] = prime_flags[1] = False
    for p in range(2, len(prime_flags)):
        if prime_flags[p]:
            for multiple in range(p * p, len(prime_flags), p):
                prime_flags[multiple] = False
    assert all(verify_integer(int(n), proof) == prime_flags[int(n)] for n, proof in certs.items())
    controls = {}
    broken = deepcopy(c)
    broken["vertices"].remove((3, 0))
    controls["missing_vertex_axis_norm9"] = rejected(lambda: verify_window(broken))
    broken = deepcopy(c)
    broken["darts"].pop()
    controls["missing_edge"] = rejected(lambda: verify_window(broken))
    broken = deepcopy(c)
    broken["vertices"].append((3, 4))
    controls["fake_gaussian_prime_norm25"] = rejected(lambda: verify_window(broken))
    broken = deepcopy(c)
    u, v, s = broken["darts"][0]
    broken["darts"][0] = (u, v, (-s[0], -s[1]))
    controls["voltage_reversed"] = rejected(lambda: verify_window(broken))
    broken = deepcopy(c)
    broken["integer_certificates"]["25"] = {"kind": "prime", "remainders": [1, 1, 1, 1]}
    controls["forged_rational_primality"] = rejected(lambda: verify_window(broken))
    broken = deepcopy(c)
    broken["boundary"].pop()
    controls["missing_boundary_point"] = rejected(lambda: verify_cut(broken))
    broken = deepcopy(c)
    broken["component"].remove((11, 4))
    controls["missing_component_vertex"] = rejected(lambda: verify_cut(broken))
    reentry = [(1, 1), (1, 2), (0, 3), (-1, 2), (-1, 1)]
    assert replay(reentry, k, certs) == (-2, 0)
    small_vertices = {(a, b) for a in range(-1, 2) for b in range(-1, 2) if gaussian((a, b), certs)}
    assert len(small_vertices) == 4 and all(norm((u[0] - v[0], u[1] - v[1])) > k
                                         for u in small_vertices for v in small_vertices if u != v)
    controls["path_outside_window_and_reentry"] = rejected(lambda: replay(reentry, k, certs, radius=1))
    truncated = deepcopy(c)
    truncated.update(radius=1, vertices=sorted(small_vertices), darts=[], component=[(1, 1)],
                     boundary=sorted({(1 + a, 1 + b) for a, b in steps(k)} - {(1, 1)}))
    controls["finite_window_component_is_global"] = rejected(lambda: verify_cut(truncated))
    controls["illegal_edge_threshold"] = rejected(lambda: replay([reentry[0], reentry[-1]], k, certs))
    loop = [(1, 1), (1, 2), (0, 3), (-1, 2), (-2, 1), (-3, 0), (-4, 1)]
    displacement = replay(loop, k, certs)
    assert displacement == (-5, 0) and tuple(t % 5 for t in loop[0]) == tuple(t % 5 for t in loop[-1])
    rotated = [(-z[1], z[0]) for z in loop]
    assert replay(rotated, k, certs) == (0, -5)
    assert replay([(z[0], -z[1]) for z in rotated], k, certs) == (0, 5)
    shifted = [(z[0] + displacement[0], z[1] + displacement[1]) for z in loop]
    controls["repeated_residue_loop_not_prime_path"] = rejected(lambda: replay(shifted, k, certs))
    for q in (23, 29):
        observed = {(z[0] % q, z[1] % q): z for z in cc}
        assert len(observed) == len(cc)
        assert all((observed[(v[0] % q, v[1] % q)][0] - observed[(u[0] % q, u[1] % q)][0],
                    observed[(v[0] % q, v[1] % q)][1] - observed[(u[0] % q, u[1] % q)][1]) == s
                   for u, v, s in darts if u in cc)
    # Static certificate restriction/union maps; no fabricated network events.
    shards = [{n: proof for n, proof in certs.items() if int(n) % 6 == lane} for lane in range(6)]
    merged = {}
    for shard in reversed(shards):
        for n, proof in shard.items():
            assert n not in merged or merged[n] == proof, "incompatible source certificate"
            merged[n] = proof
    assert merged == certs
    descended = deepcopy(c)
    descended["integer_certificates"] = merged
    verify_cut(descended)
    descended["integer_certificates"] = {n: proof for shard in shards[:-1] for n, proof in shard.items()}
    controls["missing_certificate_shard"] = rejected(lambda: verify_cut(descended))
    repo = Path(__file__).resolve().parents[2]
    source_files = ["provenance/IMPORT_MANIFEST.json", "research/2026-10-12/GAUSSIAN_SOURCE_MANIFEST.json",
                    "research/2026-10-12/GAUSSIAN_MOAT_SUCC.md",
                    "research/2026-10-12/DIAGONAL_TOWER_AND_GAUSSIAN_HOLONOMY.md",
                    "research/2026-10-12/FIELD_RELATIVE_CLOSURE_AND_OBSTRUCTION_CALCULUS.md"]
    receipt = {"schema": "succ-e39-exact-cut-v1", "immutable_parent": BASE,
               "command": "python research/2026-10-13/E39_gaussian_cut_probe.py", "exit_code": 0,
               "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
               "frozen_inputs_sha256": {p: sha256((repo / p).read_bytes()).hexdigest() for p in source_files},
               "certificate": c, "summary": {"window_points": len(window), "gaussian_primes": len(vertices),
               "directed_edges": len(darts), "global_root_component": len(cc), "nonprime_boundary": len(boundary),
               "integer_certificate_count": len(certs), "independent_integer_sieve_verified": True,
               "component_max_coordinate": max(max(map(abs, z)) for z in cc),
               "complete_small_window_components": 4, "genuine_exterior_reentry_path": reentry,
               "mod5_source_open_residue_closed_path": loop, "true_voltage": displacement,
               "failed_translated_point": (-4, 2), "failed_translated_norm": 20,
               "rotation_voltage": (0, -5), "rotation_then_conjugation_voltage": (0, 5),
               "injective_refinements": [23, 29], "static_shard_sizes": list(map(len, shards)),
               "static_restriction_union_roundtrip": True, "actual_network_run": False,
               "outside_other_components": "UNVERIFIED",
               "all_K_or_RH_claim": False}, "negative_controls": controls}
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
