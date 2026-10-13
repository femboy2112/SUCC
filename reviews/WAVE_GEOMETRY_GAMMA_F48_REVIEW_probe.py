"""Tiny independent exact witnesses; author dossiers only, no helper imports."""
from fractions import Fraction
from hashlib import sha256
from math import comb, factorial, prod
from pathlib import Path
import json
import subprocess
import time


SOURCES = [
    ("D29", "/home/leah/succ_lab/swm-d29", "0054cb46ebe3ae5286aca12a7a7f38095da78dea",
     "research/2026-10-13/SWARM_ATLAS/D29_ATTRACTORS_CONLEY_SELF_UPDATE.md"),
    ("E37", "/home/leah/succ_lab/swm-e37", "80914ab3728479d5ef83c0e8fd6935f0bf901c41",
     "research/2026-10-13/E37_ARCHIMEDEAN_GAMMA_BOUNDARY.md"),
    ("F48", "/home/leah/succ_lab/swm-f48", "6e751c0d996de3d27a91b09f44dc2d534db09c73",
     "research/2026-10-13/F48/F48_LAWFUL_HISTORY_FIBRATION.md"),
]


def cycle_states(f):
    result = set()
    for start in range(len(f)):
        current = f[start]
        for _ in range(len(f)):
            if current == start:
                result.add(start)
                break
            current = f[current]
    return result


def gamma_rational(n, q):
    return Fraction(factorial(n) * n**q, prod(q + j for j in range(n + 1)))


def main():
    started = time.monotonic()
    f, g, pi = (1, 1), (0,), (0, 0)
    assert all(pi[f[x]] == g[pi[x]] for x in range(2))
    source_inv = cycle_states(f)
    target_inv = cycle_states(g)
    pullback = {x for x in range(2) if pi[x] in target_inv}
    assert {pi[x] for x in source_inv} == target_inv
    assert source_inv != pullback
    f6, g3, pi6 = tuple((x + 1) % 6 for x in range(6)), (1, 2, 0), tuple(x % 3 for x in range(6))
    assert all(pi6[f6[x]] == g3[pi6[x]] for x in range(6))
    assert len(cycle_states(f6)) == 6 and len(cycle_states(g3)) == 3

    gamma_cases = 0
    for n in range(1, 5):
        for q in range(1, 5):
            integrated = n**q * sum(Fraction((-1)**k * comb(n, k), q + k)
                                    for k in range(n + 1))
            gn = gamma_rational(n, q)
            assert integrated == gn
            assert gamma_rational(n, q + 1) / gn == Fraction(n * q, n + q + 1)
            assert 0 < factorial(q - 1) - gn <= Fraction(factorial(q - 1) * q * (q + 1), 2 * n)
            gamma_cases += 1
    assert gamma_rational(2, 1) == Fraction(2, 3)
    assert gamma_rational(2, 2) == Fraction(1, 3)

    # A real symmetric entire fake agrees with 1 to first order at 0,1,1/2,
    # but has prescribed fixed off-line roots 1/4 and 3/4. No zeta zero input.
    def perturbation(s):
        return (s * (s - 1))**2 * prod(((s - a) * (s - (1 - a)))**2
                                     for a in (Fraction(0), Fraction(1), Fraction(1, 2)))
    epsilon = -1 / perturbation(Fraction(1, 4))
    fake = lambda s: 1 + epsilon * perturbation(s)
    assert all(fake(s) == 1 for s in (Fraction(0), Fraction(1), Fraction(1, 2)))
    assert fake(Fraction(1, 4)) == fake(Fraction(3, 4)) == 0

    left, right = {("a", 0)}, {(1, "b")}
    exact = {(a, x, b) for a, x in left for y, b in right if x == y}
    reported = {(a, "o", b) for a, x in left for y, b in right}
    assert exact == set() and reported == {("a", "o", "b")}
    private = {("sigma", "P", "L", "Z"), ("sigma", "P", "R", "Z")}
    endpoints = {(p[0], p[-1]) for p in private}
    assert len(private) == 2 and len(endpoints) == 1
    incidence_cells = {"v0", "v1", "e1"}
    vertex_family_union = {"v0"} | {"v1"}
    covers_edge = incidence_cells <= vertex_family_union
    assert not covers_edge

    source_maps = []
    for label, directory, commit, path in SOURCES:
        data = subprocess.check_output(["git", "-C", directory, "show", f"{commit}:{path}"])
        source_maps.append({"candidate": label, "commit": commit, "path": path,
                            "sha256": sha256(data).hexdigest()})
    result = {
        "review": "WAVE_GEOMETRY_GAMMA_F48_REVIEW",
        "scope": "Tiny exact finite countermodels; analytic/topological claims use paper reconstruction",
        "author_helpers_imported": False, "source_dossiers": source_maps,
        "D29": {"source_biinfinite_states": sorted(source_inv),
                "target_biinfinite_states": sorted(target_inv),
                "target_pullback": sorted(pullback), "image_equality": True,
                "strong_pullback_equality": False, "period_collapse": [6, 3]},
        "E37": {"exact_beta_polynomial_cases": gamma_cases,
                "G2_at_1": "2/3", "G2_at_2": "1/3", "finite_ratio": "1/2",
                "symmetric_fake_sample_values": ["1", "1", "1"],
                "fake_off_line_roots": ["1/4", "3/4"], "real_epsilon": str(epsilon),
                "non_Euler_connected_coefficient_at_6": 2 - 1 * 1},
        "F48": {"exact_join": [], "projected_join": sorted(reported),
                "private_path_count": len(private), "endpoint_count": len(endpoints),
                "vertex_only_family_covers_transition_edge": covers_edge},
        "elapsed_seconds": round(time.monotonic() - started, 6), "exit_code": 0,
        "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
