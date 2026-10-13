"""Independent exact X02 review: no author probe or repository modules imported."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


def zero(rows, columns=None):
    return [[F(0) for _ in range(rows if columns is None else columns)]
            for _ in range(rows)]


def identity(size):
    return [[F(i == j) for j in range(size)] for i in range(size)]


def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def apply(a, v):
    return [sum((x*y for x, y in zip(row, v)), F(0)) for row in a]


def normal(v):
    mass = sum(v, F(0))
    if mass == 0:
        raise ValueError("Zero mass has no normalized posterior")
    return [x/mass for x in v]


def matrix_permutation(p):
    result = zero(len(p))
    for x, y in enumerate(p):
        result[y][x] = F(1)
    return result


def orbit_maps(group):
    size = len(group[0])
    remaining = set(range(size))
    orbits = []
    while remaining:
        orbit = sorted({p[min(remaining)] for p in group})
        orbits.append(orbit)
        remaining.difference_update(orbit)
    r, j = zero(len(orbits), size), zero(size, len(orbits))
    for i, orbit in enumerate(orbits):
        for x in orbit:
            r[i][x], j[x][i] = F(1), F(1, len(orbit))
    assert multiply(r, j) == identity(len(orbits))
    return orbits, r, j


def transport_squares(t, r, j):
    quotient = multiply(multiply(r, t), j)
    projection = multiply(j, r)
    lumpable = multiply(r, t) == multiply(quotient, r)
    uniform_lift = multiply(t, j) == multiply(j, quotient)
    reynolds = multiply(t, projection) == multiply(projection, t)
    assert (lumpable and uniform_lift) == reynolds
    return quotient, {"all_prior_lumpability": lumpable,
                      "invariant_uniform_lift": uniform_lift,
                      "Reynolds_commutation": reynolds}


def covariance(t, group):
    return all(t[p[y]][p[x]] == t[y][x]
               for p in group for y in range(len(t)) for x in range(len(t)))


def strings(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list):
        return [strings(x) for x in value]
    if isinstance(value, dict):
        return {k: strings(v) for k, v in value.items()}
    return value


def main():
    # S3 on three natural labels and two sign labels; Q is the current bit.
    group = []
    for p in permutations(range(3)):
        odd = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2
        alpha = list(p) + ([4, 3] if odd else [3, 4])
        group.append([2*alpha[s]+q for s in range(5) for q in range(2)])
    orbits, r, j = orbit_maps(group)
    assert all(not all(p[x] == x for p in group) for x in range(10))
    likelihoods = [F(3, 4), F(1, 2)]*3 + [F(1, 4), F(1, 2)]*2
    updates = [zero(10), zero(10)]
    for s in range(5):
        for q in range(2):
            x = 2*s+q
            updates[0][2*s][x] = likelihoods[x]
            updates[1][2*s][x] = 1-likelihoods[x]
    assert all(sum(t[y][x] for t in updates for y in range(10)) == 1
               for x in range(10))
    coarse = []
    for t in updates:
        assert covariance(t, group)
        reduced, squares = transport_squares(t, r, j)
        assert all(squares.values())
        coarse.append(reduced)
    prior = [F(1, 10)]*10
    reported = apply(updates[0], prior)
    assert sum(reported) == F(21, 40)
    posterior = normal(reported)
    assert posterior == [F(5, 21), F(0)]*3 + [F(1, 7), F(0)]*2
    assert sum(posterior[:6]) == F(5, 7)
    w = [F(i, 10) for i in (1, 2, 3, 4)]
    chronological_words = 0
    for length in range(1, 5):
        for word in product(range(2), repeat=length):
            full, reduced, invariant_full, invariant_reduced = prior, apply(r, prior), apply(j, w), w
            for report in word:
                full = apply(updates[report], full)
                reduced = apply(coarse[report], reduced)
                invariant_full = apply(updates[report], invariant_full)
                invariant_reduced = apply(coarse[report], invariant_reduced)
            assert sum(full) == sum(reduced)
            assert apply(r, normal(full)) == normal(reduced)
            assert normal(invariant_full) == apply(j, normal(invariant_reduced))
            chronological_words += 1

    # All S3 permutations on three current states, with singleton original S.
    s3 = list(permutations(range(3)))
    _, r3, j3 = orbit_maps(s3)
    cycle = matrix_permutation((1, 2, 0))
    cycle_reduced, cycle_squares = transport_squares(cycle, r3, j3)
    assert all(cycle_squares.values()) and not covariance(cycle, s3)
    reset = zero(3)
    reset[0] = [F(1)]*3
    _, reset_squares = transport_squares(reset, r3, j3)
    assert reset_squares == {"all_prior_lumpability": True,
                            "invariant_uniform_lift": False,
                            "Reynolds_commutation": False}
    unequal = zero(3)
    for i, effect in enumerate((F(1), F(1, 2), F(1, 4))):
        unequal[i][i] = effect
    unequal_post = normal(apply(unequal, [F(1, 3)]*3))
    assert unequal_post == [F(4, 7), F(2, 7), F(1, 7)]
    _, unequal_squares = transport_squares(unequal, r3, j3)
    assert not any(unequal_squares.values())
    # Averaging after the update preserves its unequal likelihood function.
    averaged_after = multiply(multiply(j3, r3), unequal)
    after_dirac_likelihoods = [sum(row[x] for row in averaged_after) for x in range(3)]
    assert after_dirac_likelihoods == [F(1), F(1, 2), F(1, 4)]

    # Covariance of an unconditioned instrument does not imply covariance per report.
    flip_group = [(0, 1), (1, 0)]
    reveal0 = [[F(1), F(0)], [F(0), F(0)]]
    reveal1 = [[F(0), F(0)], [F(0), F(1)]]
    unconditioned = [[reveal0[i][k]+reveal1[i][k] for k in range(2)]
                     for i in range(2)]
    assert covariance(unconditioned, flip_group)
    assert not covariance(reveal0, flip_group)
    revealed_posterior = normal(apply(reveal0, [F(1, 2)]*2))
    assert revealed_posterior == [F(1), F(0)]

    # Diagonal symmetry preserves parity, which no separate f(S) x g(Q) can retain.
    diagonal_group = [(0, 1, 2, 3), (3, 2, 1, 0)]
    diagonal_orbits, rd, jd = orbit_maps(diagonal_group)
    parity0 = zero(4)
    for x in (0, 3):
        parity0[x][x] = F(1)
    assert covariance(parity0, diagonal_group)
    _, diagonal_squares = transport_squares(parity0, rd, jd)
    assert all(diagonal_squares.values())
    correlated_priors = [[F(3, 8), F(1, 8), F(1, 8), F(3, 8)],
                         [F(1, 8), F(3, 8), F(3, 8), F(1, 8)]]
    parity_likelihoods = [sum(apply(parity0, v)) for v in correlated_priors]
    assert parity_likelihoods == [F(3, 4), F(1, 4)]
    assert [[v[0]+v[1], v[2]+v[3]] for v in correlated_priors] == [[F(1, 2)]*2]*2
    assert [[v[0]+v[2], v[1]+v[3]] for v in correlated_priors] == [[F(1, 2)]*2]*2

    impossible = zero(10)
    zero_image = apply(impossible, prior)
    assert sum(zero_image) == 0
    try:
        normal(zero_image)
    except ValueError:
        zero_rejected = True
    else:
        raise AssertionError("An impossible report was normalized")
    # Root covariance alone does not repair independently specified leaf instruments.
    root_update, unrelated_leaf_update = identity(3), reset
    assert root_update != unrelated_leaf_update  # identity edge transport

    source = Path('/home/leah/succ_lab/swm-x02/research/2026-10-13/SWARM_ATLAS/X02.md')
    output = {
        "reviewed_commit": "090d6e593b2fa9b9ea431e898f653e72f933ab50",
        "reviewed_dossier_sha256": sha256(source.read_bytes()).hexdigest(),
        "reviewer_input": "X02.md only; author probe never read or imported",
        "independence_limit": "independent implementation after reading theorem and stated witnesses",
        "S3_informative_erasure": {"joint_orbits": orbits, "report_zero_quotient": coarse[0],
            "report_zero_likelihood": sum(reported), "posterior": posterior,
            "source_natural_orbit_prior": F(3, 5), "source_natural_orbit_posterior": F(5, 7),
            "chronological_words_checked": chronological_words,
            "holonomy_fixed_points": []},
        "strict_contract_separation": {
            "cycle": {"covariant": False, "squares": cycle_squares, "quotient": cycle_reduced},
            "reset": {"covariant": False, "squares": reset_squares},
            "unequal_likelihood": {"posterior": unequal_post, "squares": unequal_squares,
                "averaging_after_update_dirac_likelihoods": after_dirac_likelihoods},
            "unconditioned_vs_reported": {"summed_kernel_covariant": True,
                "report_zero_update_covariant": False, "posterior": revealed_posterior,
                "report_zero_likelihood": F(1, 2)}},
        "diagonal_not_product": {"orbits": diagonal_orbits, "same_two_marginals": True,
            "report_zero_likelihoods": parity_likelihoods, "orbit_squares": diagonal_squares,
            "collapsed_product_Dirac_likelihoods": [F(1), F(0)]},
        "zero_normalization": {"unnormalized_output_mass": F(0), "normalization_rejected": zero_rejected},
        "unrelated_leaf_instrument_counterexample": {"root": root_update, "leaf": unrelated_leaf_update,
            "identity_edge_square_commutes": False, "is_X02_frame_transport_construction": False},
        "physical_calibration": "UNVERIFIED", "novelty": "NOT CLAIMED",
    }
    print(json.dumps(strings(output), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
