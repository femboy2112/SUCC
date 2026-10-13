"""Bounded exact X02 witnesses; no repository runtime/helper imports."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import platform
import subprocess


def apply(matrix, law):
    return tuple(sum((a * b for a, b in zip(row, law)), F(0)) for row in matrix)


def push(permutation, law):
    out = [F(0)] * len(law)
    for i, j in enumerate(permutation):
        out[j] += law[i]
    return tuple(out)


def normalize(law):
    mass = sum(law, F(0))
    if mass <= 0:
        raise ValueError("zero-mass conditional law is undefined")
    return tuple(x / mass for x in law)


def group(generators):
    n = len(generators[0])
    found = {tuple(range(n))}
    while True:
        expanded = found | {tuple(g[h[i]] for i in range(n))
                            for g in generators for h in found}
        if expanded == found:
            return sorted(found)
        assert len(expanded) <= 6, "declared S3 bound exceeded"
        found = expanded


def quotient(matrix, orbits):
    columns = []
    for orbit in orbits:
        totals = {tuple(sum((matrix[y][x] for y in target), F(0))
                        for target in orbits) for x in orbit}
        if len(totals) != 1:
            raise ValueError("all-prior orbit square fails")
        columns.append(totals.pop())
    return tuple(tuple(c[j] for c in columns) for j in range(len(orbits)))


def run():
    states = list(product(range(5), range(2)))
    index = {x: i for i, x in enumerate(states)}
    source_generators = [(1, 0, 2, 4, 3), (0, 2, 1, 4, 3)]
    permutations = [tuple(index[(g[s], q)] for s, q in states)
                    for g in source_generators]
    symmetry = group(permutations)
    assert len(symmetry) == 6
    fixed = [i for i in range(10) if all(g[i] == i for g in symmetry)]
    assert fixed == []
    orbits = sorted({tuple(sorted({g[i] for g in symmetry})) for i in range(10)})
    assert sorted(map(len, orbits)) == [2, 2, 3, 3]
    r = tuple(tuple(F(i in orbit) for i in range(10)) for orbit in orbits)
    j = tuple(tuple(F(i in orbit, len(orbit)) for orbit in orbits) for i in range(10))
    prior = (F(1, 10),) * 10
    instrument = []
    for report in range(2):
        likelihood = [F(1, 2) if q else F(3 if s < 3 else 1, 4) for s, q in states]
        if report:
            likelihood = [1 - x for x in likelihood]
        instrument.append(tuple(tuple(likelihood[i] if y == (s, 0) else F(0)
                                      for i, (s, q) in enumerate(states)) for y in states))
    assert all(sum((m[y][x] for m in instrument for y in range(10)), F(0)) == 1
               for x in range(10))
    coarse = [quotient(m, orbits) for m in instrument]
    checks = 0
    for m, bar in zip(instrument, coarse):
        for i in range(10):
            delta = tuple(F(k == i) for k in range(10))
            assert apply(r, apply(m, delta)) == apply(bar, apply(r, delta))
            for g in symmetry:
                assert apply(m, push(g, delta)) == push(g, apply(m, delta))
                checks += 1
        for i in range(4):
            delta = tuple(F(k == i) for k in range(4))
            assert apply(m, apply(j, delta)) == apply(j, apply(bar, delta))
    words = []
    for length in (1, 2):
        for word in product(range(2), repeat=length):
            law, orbitlaw, likelihood = prior, apply(r, prior), F(1)
            for report in word:
                raw = apply(instrument[report], law)
                barraw = apply(coarse[report], orbitlaw)
                assert sum(raw) == sum(barraw)
                likelihood *= sum(raw)
                law, orbitlaw = normalize(raw), normalize(barraw)
                assert apply(r, law) == orbitlaw and apply(j, orbitlaw) == law
                assert all(push(g, law) == law for g in symmetry)
            words.append({"word": word, "likelihood": likelihood, "posterior": law,
                          "orbit_posterior": orbitlaw})
    first = words[0]
    assert first["likelihood"] == F(21, 40)
    assert first["posterior"] == tuple(F(5, 21) if q == 0 and s < 3 else
                                       F(1, 7) if q == 0 else F(0) for s, q in states)
    # Source-sensitive report keeps positive support but breaks holonomy.
    tri_group = group([(1, 0, 2), (0, 2, 1)])
    tri_prior = (F(1, 3),) * 3
    tri_raw = tuple(p * l for p, l in zip(tri_prior, (F(1), F(1, 2), F(1, 4))))
    hostile = normalize(tri_raw)
    assert hostile == (F(4, 7), F(2, 7), F(1, 7))
    averaged = tuple(sum((push(g, hostile)[i] for g in tri_group), F(0)) / 6
                     for i in range(3))
    assert averaged == tri_prior and push(tri_group[1], hostile) != hostile
    # Original S is singleton here; a Q three-cycle can preserve a law without naturality.
    cycle = (1, 2, 0)
    cycle_matrix = tuple(tuple(F(y == cycle[x]) for x in range(3)) for y in range(3))
    assert apply(cycle_matrix, tri_prior) == tri_prior
    assert quotient(cycle_matrix, [(0, 1, 2)]) == ((F(1),),)
    cycle_delta = (F(1), F(0), F(0))
    swap = (1, 0, 2)
    assert apply(cycle_matrix, push(swap, cycle_delta)) != push(swap, apply(cycle_matrix, cycle_delta))
    averaged_diracs = []
    for x in range(3):
        delta = tuple(F(i == x) for i in range(3))
        avg = tuple(sum((push(g, delta)[i] for g in tri_group), F(0)) / 6 for i in range(3))
        assert avg == tri_prior
        averaged_diracs.append(avg)
    # Diagonal symmetry does not license the separate source/carrier quotient.
    binary_states = list(product(range(2), repeat=2))
    flip = (3, 2, 1, 0)
    parity0 = tuple(tuple(F(y == x and sum(binary_states[x]) % 2 == 0)
                         for x in range(4)) for y in range(4))
    correlated, anticorrelated = (F(3, 8), F(1, 8), F(1, 8), F(3, 8)), (F(1, 8), F(3, 8), F(3, 8), F(1, 8))
    for i in range(4):
        delta = tuple(F(k == i) for k in range(4))
        assert apply(parity0, push(flip, delta)) == push(flip, apply(parity0, delta))
    assert push(flip, correlated) == correlated and push(flip, anticorrelated) == anticorrelated
    predictions = tuple(sum(apply(parity0, p)) for p in (correlated, anticorrelated))
    assert predictions == (F(3, 4), F(1, 4))
    try:
        quotient(parity0, [tuple(range(4))])
    except ValueError:
        product_square_rejected = True
    else:
        raise AssertionError("false product quotient accepted")
    zero = (F(0),) * 10
    zero_matrix = tuple(zero for _ in range(10))
    constant_report0 = tuple(tuple(F(y == x) for x in range(10)) for y in range(10))
    assert all(sum((m[y][x] for m in (constant_report0, zero_matrix) for y in range(10)), F(0)) == 1
               for x in range(10))
    assert apply(zero_matrix, prior) == zero
    try:
        normalize(zero)
    except ValueError:
        zero_guard = True
    else:
        raise AssertionError("impossible posterior invented")
    return {"status": "TESTED MODEL", "group_order": 6, "fixed_points": fixed,
            "states": states, "orbits": orbits, "initial_joint_law": prior,
            "reported_matrices": instrument, "coarse_matrices": coarse,
            "dirac_covariance_checks": checks, "bounded_word_count": len(words),
            "words": words, "symmetry_breaking_posterior": hostile,
            "symmetry_breaking_likelihood": (F(1), F(1, 2), F(1, 4)),
            "symmetry_breaking_report_mass": sum(tri_raw),
            "averaged_posterior": averaged, "averaged_diracs": averaged_diracs,
            "noncovariant_current_cycle": {"permutation": cycle, "uniform_preserved": True,
                                          "orbit_quotient_exists": True, "symmetry_square": False},
            "diagonal_predictions": predictions,
            "diagonal_control": {"states": binary_states, "flip": flip, "report_zero_matrix": parity0,
                                 "correlated_prior": correlated, "anticorrelated_prior": anticorrelated,
                                 "coarse_prior_for_both": (F(1),)},
            "product_square_rejected": product_square_rejected,
            "zero_output": zero, "zero_normalization_rejected": zero_guard,
            "zero_instrument": "constant report zero: T0=identity; impossible report one: T1=zero; complete rows normalized",
            "positive_only_lift_exists_over_impossible_report": False,
            "physical_law_calibration": "UNVERIFIED", "universal_proof": "paper derivation; independent acceptance pending"}


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    receipt = run()
    receipt.update({"python": platform.python_version(), "command": "python research/2026-10-13/SWARM_ATLAS/X02_probe.py",
                    "exit_code": 0, "parent_commit": "4b17f1828c3c023b95c283b25c13cf6e81d48619",
                    "observed_checkout": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
                    "artifact_hashes": {p.name: sha256(p.read_bytes()).hexdigest() for p in
                                        [Path(__file__).resolve(), here / "X02.md", here / "A04.md", here / "C17.md",
                                         here / "reviews/A04_REVIEW.md", here / "reviews/C17_PRINCIPAL_REVIEW.md"]},
                    "authority_hashes": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in
                                         [root / "AGENTS.md", root / "docs/METHOD.md", here / "PROTOCOL.md",
                                          root / "provenance/IMPORT_MANIFEST.json",
                                          root / "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md"]},
                    "native_origin_objects_inspected": ["157888335224a3a477913fa661951eb54504d4ca",
                                                        "c78c4a2a0217d08bad10ae5bcac9cebb7dabebe5",
                                                        "39cc40abda8c9cc424083472fdbd16b7aefcfa68",
                                                        "1b548be824f50f5a358e96d1d01d8047fe97eacd"],
                    "provenance_verifier": {"command": "python scripts/verify_provenance.py", "exit_code": 0,
                                            "status": "SOURCE_PROVENANCE_VERIFIED", "items": 72,
                                            "scope": "separately executed investigator baseline; not rerun by this probe"},
                    "archival_origin_object": {"sha": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
                                               "command": "git cat-file -e ba075348b7bcc66d938b3e0ca96c26e95bba340a", "exit_code": 1},
                    "primary_source_access": {"Fritz": "Example 2.5 read via arXiv HTML",
                                              "Cho_Jacobs": "sections 3, 7, 8 passages read via arXiv HTML",
                                              "Hatcher": "inherited A04 reading; web error and fresh urllib timeout exit 1"},
                    "sources_modified": False, "full_suite_run": False, "compiler_run": False})
    serialized = json.dumps(receipt, indent=2, default=lambda x: str(x) if isinstance(x, F) else x) + "\n"
    (here / "X02_RECEIPT.json").write_text(serialized)
    print(json.dumps({"status": receipt["status"], "dirac_covariance_checks": receipt["dirac_covariance_checks"],
                      "bounded_word_count": receipt["bounded_word_count"], "hostile_receipts": 4,
                      "receipt": str(here / "X02_RECEIPT.json")}))
