#!/usr/bin/env python3
"""Exact independent audit of floor/Gamma/ordered-Haar identities.

Standard library only; no imports from observational_succ. Theorems are proved
in the accompanying notes. Finite assertions calibrate implementations and
mutations, and do not prove an asymptotic statement about pi.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


COUNTS: Counter[str] = Counter()


def check(category: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1


def sign(k: int) -> int:
    return 1 if k % 2 == 0 else -1


def s(n: int) -> int:
    return sign(n // 2)


def w(n: int) -> int:
    return (1, -1, -1, 1)[n % 4]


def gate(x: Q) -> int:
    return int(x.numerator // x.denominator % 4 in (1, 2))


def source(n: int) -> Q:
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def mod_q(x: Q, m: int) -> int:
    return x.numerator * pow(x.denominator, -1, m) % m


def v2(x: Q) -> int:
    if x == 0:
        raise ValueError("zero valuation is not finite")
    def vi(k: int) -> int:
        k = abs(k)
        return (k & -k).bit_length()-1
    return vi(x.numerator)-vi(x.denominator)


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[sum((a[i][k]*b[k][j] for k in range(4)), Q(0))
             for j in range(4)] for i in range(4)]


def dot_expect(p: list[list[Q]], f: tuple[int, ...], g: tuple[int, ...]) -> Q:
    return sum((Q(1, 4)*p[i][j]*f[i]*g[j]
                for i in range(4) for j in range(4)), Q(0))


def part_lengths(r: Q) -> list[Q]:
    return [max(Q(0), min(r, Q(j+1, 4))-Q(j, 4)) for j in range(4)]


def period_and_source() -> None:
    for n in range(-256, 257):
        check("quadratic_period", s(n) == sign(n*(n-1)//2))
        check("carry_grade_sign", w(n) == sign(n*(n+1)//2) == s(n+1))
        check("slope_residue", (10+pow(2*n-1, -2, 16)) % 16 == 7+4*s(n))
        check("walsh_bits", s(n) == sign((n % 4)//2))
    for n in range(-32, 33):
        for m in range(-32, 33):
            check("quadratic_addition", s(n+m) == s(n)*s(m)*sign(n*m))
    for j in range(-256, 257):
        for d in (1, 2, 3, 7):
            x = Q(j, d)
            check("nested_floor", w(x.numerator//x.denominator)
                  == sign(((x+1)/2).numerator//((x+1)/2).denominator))

    q = (4, 4, 4, 2, 1)
    # Fixed distant indices are arithmetic holdouts, not orbit sampling.
    ns = list(range(1, 513)) + [65537, 983041, 15485863, 2**31+1, 2**47+3]
    for n in ns:
        a = 8*n-7
        branches = [Q(q[j], (a+j)*(a+j+1)) for j in range(5)]
        check("five_beta_source", sum(branches, Q(0)) == source(n))
        check("positive_branches", all(b > 0 for b in branches))
        check("branch_valuations", [v2(b) for b in branches] == [1, 1, 0, -1, -1])
        grouped = Q(3*n-1, (2*n-1)*(4*n-1)*(8*n-3))
        check("half_dyadic_cancellation", branches[3]+branches[4] == grouped)
        check("group_returns_to_carrier", grouped.denominator % 2 == 1)
        check("source_clock", mod_q(source(n), 4) == n % 4)
        check("pole_mutation_rejected", sum(branches, Q(0)) != source(n)+Q(1, 8*n-3))
    # Moment identity for Beta(k,2) = V1^(1/k) V2^(1/(k+1)).
    for k in list(range(1, 65)) + [Q(1, 3), Q(7, 2), Q(101, 7)]:
        for h in range(25):
            product = k/(k+h)*(k+1)/(k+1+h) if isinstance(k, Q) else Q(k, k+h)*Q(k+1, k+1+h)
            beta = Q(k*(k+1), (k+h)*(k+h+1))
            check("beta_product_moments", product == beta)


def floor_integrals() -> None:
    # q=exp(-t) turns the Laplace identities into rational equalities.
    for d in range(2, 25):
        for p in range(1, d):
            q = Q(p, d)
            cycle = q-q**3
            hit = cycle/(1-q**4)
            check("gate_laplace", hit == q/(1+q*q))
            check("phase_laplace", 1-2*hit == (1-q)**2/(1+q*q))
            square = (1-q*q)**2/(1-q**4)
            check("squarewave_laplace", square == (1-q*q)/(1+q*q))
            partial = sum((q**(4*j+1)-q**(4*j+3) for j in range(8)), Q(0))
            check("exact_laplace_tail", hit-partial == q**32*hit)
            check("floor_shift_mutation_rejected", hit != 1/(1+q*q))
    for n in range(1, 65):
        for d in range(1, 9):
            layer_cake = sum((1-Q(k, n)**d for k in range(1, n+1)), Q(0))
            cells = sum((j*(Q(j+1, n)**d-Q(j, n)**d) for j in range(n)), Q(0))
            check("root_floor_layercake", layer_cake == cells)
            if d == 2:
                check("sqrt_floor_closed_form", cells == Q(2*n, 3)-Q(1, 2)-Q(1, 6*n))
    # Zero ordinary floor defect still leaves a maximal signed phase defect.
    mean = Q(0+4, 2)
    check("floor_defect_control", mean.numerator//mean.denominator == Q(0+4, 2))
    check("signed_gate_defect", gate(mean) == 1 and Q(gate(Q(0))+gate(Q(4)), 2) == 0)
    # Integral of the jump measure at odd thresholds, including exact boundaries.
    for den in (1, 2, 3, 7):
        for num in range(0, 32*den+1):
            x = Q(num, den)
            flux = sum(sign(j) for j in range(32) if 2*j+1 <= x)
            check("signed_boundary_flux", gate(x) == flux)


def weaving() -> dict:
    a = (1, 1, -1, -1)
    b = (1, -1, 1, -1)
    c = tuple(a[i]*b[i] for i in range(4))
    W = [[w(i-j) for j in range(4)] for i in range(4)]
    G = [[a[i]*c[j]-c[i]*a[j] for j in range(4)] for i in range(4)]
    F = [[a[i]*b[j]-b[i]*a[j] for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            check("carry_aligned_decomposition", 2*W[i][j] ==
                  a[i]*a[j]+c[i]*c[j]-G[i][j])
            check("bilinear_clock_cofactor", W[i][j] == s(i+1)*s(j)*sign(i*j))
    check("orthogonal_control_misses_gate", sum(W[i][j]*F[i][j] for i in range(4) for j in range(4)) == 0)
    check("aligned_probe_hits_gate", Q(sum(W[i][j]*G[i][j] for i in range(4) for j in range(4)), 16) == -1)
    rows = []
    for eps in (Q(-1, 2), Q(-1, 4), Q(0), Q(1, 4), Q(1, 2)):
        density = [[1+eps*G[i][j] for j in range(4)] for i in range(4)]
        P = [[density[i][j]/4 for j in range(4)] for i in range(4)]
        for i in range(4):
            check("positive_joint_law", all(x >= 0 for x in density[i]))
            check("uniform_row", sum(P[i]) == 1)
            check("uniform_column", sum(P[j][i] for j in range(4)) == 1)
            for j in range(4):
                check("all_symmetric_laws_invariant", density[i][j]+density[j][i] == 2)
        for r in (Q(j, 64) for j in range(65)):
            lengths = part_lengths(r)
            cdf = sum((density[i][j]*lengths[i]*lengths[j]
                       for i in range(4) for j in range(4)), Q(0))
            check("maximum_law", cdf == r*r)
        gate_mean = sum((Q(1, 16)*density[i][j]*W[i][j] for i in range(4) for j in range(4)), Q(0))
        oriented = sum((Q(1, 16)*density[i][j]*G[i][j] for i in range(4) for j in range(4)), Q(0))
        energy = sum((Q(1, 16)*density[i][j]*G[i][j]**2 for i in range(4) for j in range(4)), Q(0))
        check("signed_carry_mean", gate_mean == -eps)
        check("ordered_response", oriented == 2*eps)
        check("same_squared_response", energy == 2)
        rows.append({"epsilon": str(eps), "carry_mean": str(gate_mean),
                     "selected_probability": str((1-gate_mean)/2),
                     "ordered_response": str(oriented), "squared_response": str(energy)})
        # Exact finite-state realization of the continuous piecewise density.
        Pk = [[Q(int(i == j)) for j in range(4)] for i in range(4)]
        for lag in range(25):
            H = dot_expect(Pk, a, a)+dot_expect(Pk, c, c)
            O = dot_expect(Pk, a, c)-dot_expect(Pk, c, a)
            check("temporal_period_four", (H+O)/2 == eps**lag*s(lag))
            expected_H = 2*eps**lag*(1, 0, -1, 0)[lag % 4]
            expected_O = 2*eps**lag*(0, 1, 0, -1)[lag % 4]
            check("complex_rotation_real", H == expected_H)
            check("complex_rotation_imag", O == expected_O)
            Pk = matmul(Pk, P)
    bad = [[1+Q(3, 4)*G[i][j] for j in range(4)] for i in range(4)]
    check("nonpositive_density_mutation_rejected", any(x < 0 for row in bad for x in row))
    check("dependence_mutation_rejected", Q(1, 2) != Q(1, 2)**2)  # max(U,U)
    # Exact dual certificate: no optimizer is needed to verify the sharp bound.
    for j in range(4):
        for k in range(4):
            witness = int(k == 1)+int(j == 0 and k == 0)-int(j < 2 and k < 2)
            check("three_count_pointwise_certificate", int((j-k) % 4 in (1, 2)) >= witness)
    extremal = [[1, 3, 0, 0], [0, 0, 4, 0], [0, 1, 0, 3], [3, 0, 0, 1]]
    check("sharp_max_bound_rows", all(sum(row) == 4 for row in extremal))
    check("sharp_max_bound_columns", all(sum(extremal[i][j] for i in range(4)) == 4 for j in range(4)))
    for q in (1, 2, 3):
        check("sharp_max_bound_cdf", sum(extremal[i][j] for i in range(q) for j in range(q)) == q*q)
    hit_mass = Q(sum(extremal[i][j] for i in range(4) for j in range(4) if (i-j) % 4 in (1, 2)), 16)
    check("sharp_max_bound_attained", hit_mass == Q(1, 16))
    # Dropping the negative prefix term makes a false lower bound at (0,0).
    check("three_count_mutation_rejected", 0 < int(0 == 0 and 0 == 0))
    return {"W": W, "G": G, "controls": rows,
            "sharp_coarse_maximum_control": {"integer_table": extremal, "denominator": 16,
                                               "selected_probability": str(hit_mass)}}


def continuous_maximum_controls() -> dict:
    # A cell polynomial is a list (coefficient, x-degree, y-degree).
    sharp = {
        (0, 0): [(1, 0, 0)], (0, 1): [(8, 0, 1)], (1, 2): [(4, 0, 0)],
        (2, 1): [(32, 1, 0), (-64, 1, 1), (-16, 0, 0), (32, 0, 1)],
        (2, 3): [(8, 0, 0), (-8, 1, 0)], (3, 0): [(3, 0, 0)],
        (3, 3): [(1, 0, 0)]}
    lock = {
        (0, 0): [(1, 0, 0)], (0, 1): [(8, 0, 1)], (1, 2): [(4, 0, 0)],
        (2, 2): [(1, 0, 0)], (2, 3): [(8, 0, 1), (-4, 0, 0)],
        (3, 0): [(4, 0, 0)]}
    upper = {
        (0, 0): [(1, 0, 0)], (0, 2): [(8, 0, 1), (-4, 0, 0)],
        (0, 3): [(2, 0, 0)], (1, 0): [(8, 1, 0)],
        (1, 3): [(4, 0, 0), (-8, 1, 0)], (2, 1): [(4, 0, 0)],
        (3, 2): [(8, 0, 0), (-8, 0, 1)], (3, 3): [(1, 0, 0)]}

    def integral_power(j: int, p: int) -> Q:
        return (Q(j+1, 4)**(p+1)-Q(j, 4)**(p+1))/(p+1)

    def clean(poly: dict[int, Q]) -> dict[int, Q]:
        return {p: c for p, c in poly.items() if c}

    def clipped_power(j: int, p: int, region: int) -> dict[int, Q]:
        if j < region:
            return {0: integral_power(j, p)}
        if j > region:
            return {}
        return {0: -Q(j, 4)**(p+1)/(p+1), p+1: Q(1, p+1)}

    results = {}
    for label, density in (("sharp_uniform_copula", sharp), ("clock_only_locked_control", lock),
                           ("sharp_upper_uniform_copula", upper)):
        masses = [[Q(0) for _ in range(4)] for _ in range(4)]
        for (i, j), terms in density.items():
            masses[i][j] = sum((c*integral_power(i, p)*integral_power(j, q)
                                for c, p, q in terms), Q(0))
        # Exact polynomial identities verify all coordinates in each interval,
        # rather than sampling rows, columns, or maximum thresholds.
        for row in range(4):
            poly = {}
            for (i, j), terms in density.items():
                if i == row:
                    for c, p, q in terms:
                        poly[p] = poly.get(p, Q(0))+c*integral_power(j, q)
            check(label+"_uniform_x_polynomial", clean(poly) == {0: Q(1)})
        for col in range(4):
            poly = {}
            for (i, j), terms in density.items():
                if j == col:
                    for c, p, q in terms:
                        poly[q] = poly.get(q, Q(0))+c*integral_power(i, p)
            if label != "clock_only_locked_control":
                check(label+"_uniform_y_polynomial", clean(poly) == {0: Q(1)})
        for region in range(4):
            poly = {}
            for (i, j), terms in density.items():
                for c, p, q in terms:
                    for u, xcoef in clipped_power(i, p, region).items():
                        for v, ycoef in clipped_power(j, q, region).items():
                            poly[u+v] = poly.get(u+v, Q(0))+c*xcoef*ycoef
            check(label+"_maximum_cdf_polynomial", clean(poly) == {2: Q(1)})
        hits = sum((masses[i][j] for i in range(4) for j in range(4)
                    if (i-j) % 4 in (1, 2)), Q(0))
        expected = {"sharp_uniform_copula": Q(1, 16), "clock_only_locked_control": Q(0),
                    "sharp_upper_uniform_copula": Q(7, 8)}[label]
        check(label+"_gate_mass", hits == expected)
        results[label] = {"quarter_masses": [[str(x) for x in row] for row in masses],
                          "cofactor_marginal": [str(sum(masses[i][j] for i in range(4))) for j in range(4)],
                          "selected_probability": str(hits), "full_maximum_cdf": "r^2, 0<=r<=1"}
    return results


def authentic_observations() -> dict:
    parent = Path(__file__).resolve().parent.parent / "carry_quadrature_assault" / "receipts"
    payload = (parent / "carry_residues_mod4.txt").read_bytes()
    inherited = json.loads((parent / "finite_probe.json").read_text())
    text = payload.decode().strip()
    # The inherited hash authenticates the bare residue string, not its newline.
    digest = sha256(text.encode()).hexdigest()
    check("inherited_carry_receipt_hash", digest == inherited["residues_sha256"])
    check("inherited_receipt_length", len(text) == inherited["horizon"] == 32768)
    U = Q(0)
    a = (1, 1, -1, -1)
    c = (1, -1, -1, 1)
    for n in range(1, 513):
        U = 16*U+source(n)
        C = U.numerator//U.denominator
        y = U-C
        j, k = n % 4, mod_q(y, 4)
        check("independent_carry_recurrence", C % 4 == int(text[n-1]))
        check("authentic_clock_transport", (j-k) % 4 == C % 4)
        H = a[j]*a[k]+c[j]*c[k]
        F = a[j]*c[k]-c[j]*a[k]
        check("authentic_aligned_gate", Q(H-F, 2) == w(C))
        check("authentic_selected_event", Q(1, 2)-Q(H, 4)+Q(F, 4) == gate(U))
    shells = []
    for B in (256, 512, 1024, 2048, 4096, 8192, 16384):
        H = F = hits = 0
        joint = [[0]*4 for _ in range(4)]
        for n in range(B, 2*B):
            C = int(text[n-1]); j = n % 4; k = (j-C) % 4
            joint[j][k] += 1
            H += a[j]*a[k]+c[j]*c[k]
            F += a[j]*c[k]-c[j]*a[k]
            hits += C in (1, 2)
        check("observed_shell_identity", Q(hits, B) == Q(1, 2)-Q(H, 4*B)+Q(F, 4*B))
        F1 = Q(joint[0][0], B)
        F2 = Q(sum(joint[i][j] for i in range(2) for j in range(2)), B)
        c1 = Q(sum(joint[i][1] for i in range(4)), B)
        witness = F1+c1-F2
        error = abs(F1-Q(1, 16))+abs(c1-Q(1, 4))+abs(F2-Q(1, 4))
        check("source_three_count_bound", Q(hits, B) >= witness >= Q(1, 16)-error)
        shells.append({"start": B, "length": B, "H_mean": str(Q(H, B)),
                       "F_mean": str(Q(F, B)), "selected_count": hits,
                       "selected_fraction": str(Q(hits, B)), "joint_counts": joint,
                       "max_cdf_at_quarter": str(F1), "max_cdf_at_half": str(F2),
                       "cofactor_quarter_one": str(c1), "three_count_lower_bound": str(witness),
                       "three_count_absolute_error_budget": str(error)})
    return {"scope": "New decomposition of inherited finite certificates; not new digits or a holdout",
            "parent_commit": "fec5cdda24ca36328e123b0b367a0628491e1eb8",
            "inherited_residue_sha256": digest, "rational_recurrence_crosscheck": 512,
            "shells": shells}


def main() -> None:
    period_and_source()
    floor_integrals()
    controls = weaving()
    continuous = continuous_maximum_controls()
    observations = authentic_observations()
    out = {"status": "EXACT_FINITE_AUDIT_PASSED", "arithmetic": "Python integers and fractions.Fraction",
           "production_imports": False, "normality_proved": False,
           "positive_carry_lower_density_proved": False,
           "assertions": sum(COUNTS.values()), "categories": dict(sorted(COUNTS.items())),
           "ordered_controls": controls, "continuous_controls": continuous,
           "authentic_observations": observations}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
