#!/usr/bin/env python3
"""Independent bounded arithmetic audit of IA-01/02 and IA-05--09.

No observational_succ module, production test, or other-agent note is imported.
Exact checks use Fraction pairs, integer polynomial remainders and direct
finite probability censuses.  Optional mpmath quadrature is diagnostic only.
This script does not infer a universal arithmetic limit from its finite cases.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import factorial
from pathlib import Path
import json
import platform
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COUNTS: Counter[str] = Counter()
Z = tuple[F, F]
ZERO: Z = (F(0), F(0))
ONE: Z = (F(1), F(0))


def check(section: str, assertion: bool, detail: str = "") -> None:
    COUNTS[section] += 1
    if not assertion:
        raise AssertionError(f"{section}: {detail}")


def add(a: Z, b: Z) -> Z:
    return a[0] + b[0], a[1] + b[1]


def neg(a: Z) -> Z:
    return -a[0], -a[1]


def sub(a: Z, b: Z) -> Z:
    return add(a, neg(b))


def mul(a: Z, b: Z) -> Z:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def conj(a: Z) -> Z:
    return a[0], -a[1]


def scale(a: Z, c: F) -> Z:
    return a[0] * c, a[1] * c


def norm2(a: Z) -> F:
    return a[0] ** 2 + a[1] ** 2


def div(a: Z, b: Z) -> Z:
    return scale(mul(a, conj(b)), 1 / norm2(b))


def power(a: Z, n: int) -> Z:
    if n < 0:
        a, n = div(ONE, a), -n
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def zsum(values) -> Z:
    out = ZERO
    for v in values:
        out = add(out, v)
    return out


def unit_from_parameter(t: F) -> Z:
    return (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)


POOL = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1))]
POOL += [unit_from_parameter(F(j, abs(j) + 2)) for j in range(-9, 10)]


def fixtures(size: int, seed: int) -> list[Z]:
    return [POOL[(7 * i + 3 * seed) % len(POOL)] for i in range(size)]


def exact_gamma_checks() -> dict:
    # Repeated integration by parts for integral t^k exp(-2t) dt.
    laplace_moment = F(1, 2)
    raw = []
    for k in range(49):
        if k:
            laplace_moment *= F(k, 2)
        mass = laplace_moment / factorial(k)
        check("shifted_gamma", mass == F(1, 2 ** (k + 1)), str(k))
        if k in (0, 1, 2, 7, 16, 32, 48):
            raw.append({"k": k, "laplace_moment": str(laplace_moment), "probability_H_k_plus_1": str(mass)})
    for cutoff in range(129):
        p = sum((F(1, 2**h) for h in range(1, cutoff + 1)), F())
        first = sum((F(h, 2**h) for h in range(1, cutoff + 1)), F())
        second = sum((F(h*h, 2**h) for h in range(1, cutoff + 1)), F())
        check("geometric_moments", p + F(1, 2**cutoff) == 1)
        check("geometric_moments", first + F(cutoff + 2, 2**cutoff) == 2)
        check("geometric_moments", second + F(cutoff*cutoff + 4*cutoff + 6, 2**cutoff) == 6)
    check("mutation_controls", F(1, 2) != F(1, 4), "forgotten +1 gives Haar click 1/4, not 1/2")
    return {"authority": "EXACT_FINITE plus stated integration-by-parts identity", "k_range": [0, 48], "cutoff_range": [0, 128], "raw": raw,
            "wrong_unshifted_Haar_click": "1/4", "correct_shifted_Haar_click": "1/2"}


def kernel_checks() -> dict:
    cutoffs = (0, 1, 2, 3, 7, 19, 31)
    for z in POOL:
        check("unit_fixtures", norm2(z) == 1)
        geometric = div(z, sub((F(2), F(0)), z))
        closed = (2*z[0]-1)/(5-4*z[0])
        check("poisson_kernel", geometric[0] == closed)
        check("poisson_kernel", F(-1, 3) <= closed <= 1)
        for cutoff in cutoffs:
            prefix = sum((F(1, 2**h)*power(z, h)[0] for h in range(1, cutoff+1)), F())
            rem = div(power(scale(z, F(1, 2)), cutoff+1), sub(ONE, scale(z, F(1, 2))))
            check("poisson_series", closed-prefix == rem[0])
            check("poisson_series", abs(closed-prefix) <= F(1, 2**cutoff))
    raw = []
    cases = [(n, seed) for n in range(1, 9) for seed in (0, 1)]
    cases += [(n, seed) for n in (11, 13, 17) for seed in (2, 3)]
    for n, seed in cases:
        points = fixtures(n, seed)
        pair_energy = sum((div(mul(a, conj(b)), sub((F(2), F(0)), mul(a, conj(b))))[0]
                           for a in points for b in points), F()) / (n*n)
        check("pair_energy", 0 <= pair_energy <= 1)
        for cutoff in (0, 1, 3, 9, 17):
            prefix = F()
            for h in range(1, cutoff+1):
                mean = scale(zsum(power(z, h) for z in points), F(1, n))
                prefix += F(1, 2**h)*norm2(mean)
            check("pair_energy", prefix <= pair_energy <= prefix+F(1, 2**cutoff))
        if n in (1, 3, 11, 17) and seed in (0, 2):
            raw.append({"size": n, "seed": seed, "energy": str(pair_energy), "click_mean": str((1-pair_energy)/2)})
    coherent = F(1)
    antipodal = (F(1)+F(1)+F(-1, 3)+F(-1, 3))/4
    check("kernel_controls", coherent == 1 and antipodal == F(1, 3))
    check("mutation_controls", F(1, 3) != F(-1, 3), "removing diagonals from antipodal pair law changes the response")
    return {"authority": "EXACT_FINITE", "unit_pool_size": len(POOL), "cutoffs": list(cutoffs), "case_labels": cases,
            "fixture_source": "rational circle points, explicitly not BBP phases", "raw": raw,
            "coherent_energy": "1", "antipodal_energy": "1/3", "antipodal_without_diagonal": "-1/3"}


def polarization_checks() -> dict:
    cases = [(n, s) for n in range(1, 9) for s in (0, 1)]
    cases += [(n, s) for n in (11, 13, 17) for s in (2, 3)]
    raw = []
    for d, seed in cases:
        z = fixtures(d, seed)
        matrix = [[ZERO for _ in range(d)] for _ in range(d)]
        for i in range(d):
            matrix[i][i] = (F((i+seed) % 5-2, 3), F())
            for j in range(i+1, d):
                a = F(((i+1)*(j+2)+seed) % 7-3, (i+j) % 3+1)
                b = F(((i+3)*(j+1)+2*seed) % 9-4, (i+2*j) % 5+1)
                matrix[i][j] = a, b
                matrix[j][i] = a, -b
        direct = zsum(mul(conj(z[i]), mul(matrix[i][j], z[j])) for i in range(d) for j in range(d))
        response = sum((matrix[i][i][0]*norm2(z[i]) for i in range(d)), F())
        coefficient_budget = sum((abs(matrix[i][i][0]) for i in range(d)), F())
        row_count = sum(matrix[i][i][0] != 0 for i in range(d))
        for i in range(d):
            for j in range(i+1, d):
                a, b = matrix[i][j]
                plus = norm2(scale(add(z[i], z[j]), F(1, 2)))
                minus = norm2(scale(sub(z[i], z[j]), F(1, 2)))
                iz = mul((F(), F(1)), z[j])
                ip = norm2(scale(add(z[i], iz), F(1, 2)))
                im = norm2(scale(sub(z[i], iz), F(1, 2)))
                for p in (plus, minus, ip, im):
                    check("polarization_rows", 0 <= p <= 1)
                response += 2*a*(plus-minus)+2*b*(ip-im)
                coefficient_budget += 4*(abs(a)+abs(b))
                row_count += 2*(a != 0)+2*(b != 0)
        check("polarization", direct == (response, F()))
        check("polarization", row_count <= 2*d*d-d)
        if d in (1, 3, 11, 17) and seed in (0, 2):
            raw.append({"dimension": d, "seed": seed, "response": str(response), "coefficient_budget": str(coefficient_budget), "rows": row_count})
    a, b = ONE, (F(), F(1))
    cross = mul(a, conj(b))
    d1 = norm2(add(a, mul((F(), F(1)), b)))-norm2(sub(a, mul((F(), F(1)), b)))
    check("mutation_controls", cross == (F(), F(-1)) and d1 == -4)
    check("mutation_controls", scale((F(), d1), F(1, 4)) != neg(cross), "wrong imaginary sign is distinguishable")
    check("gauge_controls", mul(ONE, conj(ONE)) == mul((F(), F(1)), conj((F(), F(1)))))
    check("gauge_controls", ONE[0] != (F(), F(1))[0], "pair data preserve global gauge, reference quadrature changes")
    return {"authority": "EXACT_FINITE", "case_labels": cases, "raw": raw,
            "imaginary_sign_control": {"a": ["1", "0"], "b": ["0", "1"], "a_conjugate_b": ["0", "-1"], "D1": "-4"}}


def walsh_checks() -> dict:
    dimensions = (2, 3, 4, 5, 7)
    for d in dimensions:
        size = 1 << d
        laws = [[F(1, size)]*size,
                [F(2, size) if x.bit_count() % 2 == 0 else F() for x in range(size)]]
        coeffs = []
        for law in laws:
            fourier = [sum((p*((-1)**((mask & x).bit_count())) for x, p in enumerate(law)), F()) for mask in range(size)]
            coeffs.append(fourier)
            for x in range(size):
                back = sum((c*((-1)**((mask & x).bit_count())) for mask, c in enumerate(fourier)), F())/size
                check("finite_character_inversion", back == law[x])
            check("finite_character_inversion", sum(c*c for c in fourier) == size*sum(p*p for p in law))
        for mask in range(size-1):
            check("proper_marginal_control", coeffs[0][mask] == coeffs[1][mask])
        check("proper_marginal_control", coeffs[0][-1] == 0 and coeffs[1][-1] == 1)
    for d in range(1, 8):
        z = fixtures(d, 4)
        a = [i % 5-2 for i in range(d)]
        b = [2-(3*i % 5) for i in range(d)]
        chi = lambda v: product_z(power(zj, n) for zj, n in zip(z, v))
        check("laurent_character_closure", mul(chi(a), chi(b)) == chi([x+y for x, y in zip(a, b)]))
        check("laurent_character_closure", conj(chi(a)) == chi([-x for x in a]))
    return {"authority": "EXACT_FINITE", "Walsh_dimensions": list(dimensions), "Laurent_dimensions": [1, 7],
            "control": "uniform versus even-parity law: every proper character agrees, full interaction differs"}


def product_z(values) -> Z:
    out = ONE
    for value in values:
        out = mul(out, value)
    return out


def trim_poly(p: list[int]) -> list[int]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_rem(p: list[int], q: list[int]) -> list[int]:
    out = trim_poly(p.copy())
    assert q[-1] == 1
    while len(out) >= len(q) and out != [0]:
        c, offset = out[-1], len(out)-len(q)
        for j, x in enumerate(q):
            out[offset+j] -= c*x
        trim_poly(out)
    return out


def monic_div(p: list[int], q: list[int]) -> list[int]:
    out = p.copy()
    quot = [0]*max(1, len(p)-len(q)+1)
    assert q[-1] == 1
    while len(out) >= len(q) and out != [0]:
        c, offset = out[-1], len(out)-len(q)
        quot[offset] = c
        for j, x in enumerate(q):
            out[offset+j] -= c*x
        trim_poly(out)
    assert out == [0], out
    return trim_poly(quot)


PHI: dict[int, list[int]] = {1: [-1, 1]}


def cyclotomic(n: int) -> list[int]:
    if n not in PHI:
        p = [-1]+[0]*(n-1)+[1]
        for d in range(1, n):
            if n % d == 0:
                p = monic_div(p, cyclotomic(d))
        PHI[n] = p
    return PHI[n]


def chi_squared(p: list[F], q: list[F]) -> F:
    assert sum(p) == sum(q) == 1
    value = F()
    for a, b in zip(p, q):
        if not b:
            assert not a
        else:
            value += (a-b)**2/b
    return value


def tensor_law(p: list[F], count: int) -> list[F]:
    law = [F(1)]
    for _ in range(count):
        law = [a*b for a in law for b in p]
    return law


def coset_and_report_checks() -> dict:
    parameters = ((1, 1), (2, 1), (1, 2), (3, 1), (2, 2), (1, 3), (3, 2), (2, 3))
    raw = []
    for a, b in parameters:
        q = 3**a*5**b
        M = q//15
        orbit, n = [], 1
        while n not in orbit:
            orbit.append(n)
            n = 16*n % q
        check("actual_radix_cosets", n == 1 and len(orbit) == M)
        check("actual_radix_cosets", sorted(orbit) == [1+15*j for j in range(M)])
        for h in sorted({-M-1, -M, -1, 0, 1, 2, M-1, M, M+1, 2*M}):
            coefficients = [0]*M
            for x in orbit:
                coefficients[(h*((x-1)//15)) % M] += 1
            residual = poly_rem(coefficients, cyclotomic(M))
            expected = [M] if h % M == 0 else [0]
            check("exact_coset_characters", residual == expected, f"q={q}, h={h}")
        eps = F(1, 2**M-1)
        for cutoff in (0, 1, 7, 19, 41, 83):
            finite = sum((F(1, 2**h) for h in range(1, cutoff+1) if h % M == 0), F())
            check("coset_energy_tail", finite <= eps <= finite+F(1, 2**cutoff))
        # Categories are (nonresonant,0), (nonresonant,1), (resonant,0), (resonant,1).
        haar = [(1-eps)/2, (1-eps)/2, eps/2, eps/2]
        rival = [(1-eps)/2, (1-eps)/2, eps, F()]
        unlabelled_haar = [F(1, 2), F(1, 2)]
        unlabelled_rival = [(1+eps)/2, (1-eps)/2]
        labelled = chi_squared(rival, haar)
        forgotten = chi_squared(unlabelled_rival, unlabelled_haar)
        check("report_chi_squared", labelled == eps)
        check("report_chi_squared", forgotten == eps*eps)
        check("report_chi_squared", labelled >= forgotten)
        for count in range(5):
            check("product_report_census", chi_squared(tensor_law(rival, count), tensor_law(haar, count)) == (1+eps)**count-1)
            check("product_report_census", chi_squared(tensor_law(unlabelled_rival, count), tensor_law(unlabelled_haar, count)) == (1+eps*eps)**count-1)
            # Direct finite enumeration of all category strings without the Haar-only click.
            miss = sum((product_f(haar[i] for i in word) for word in product(range(4), repeat=count) if 3 not in word), F())
            check("product_report_census", miss == (1-eps/2)**count)
        raw.append({"a": a, "b": b, "denominator": q, "period": M, "orbit": orbit,
                    "energy": str(eps), "labelled_chi_squared": str(labelled), "forgotten_chi_squared": str(forgotten),
                    "labelled_rational_strict_trial_lower": str(F(2, 3)/eps), "forgotten_rational_strict_trial_lower": str(F(2, 3)/(eps*eps))})
    return {"authority": "EXACT_FINITE", "product_trial_counts": [0, 4], "raw": raw,
            "source_scope": "actual periodic radix16 orbits of 1/q; attachment to original forcing changes the seed and is not the zero-source orbit",
            "report_scope": "only (H,bit) or bit; no sampled clocks or full phases are reported"}


def product_f(values) -> F:
    out = F(1)
    for value in values:
        out *= value
    return out


def forcing(n: int) -> F:
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def convolution(p: list[int], q: list[int]) -> list[int]:
    out = [0]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def green_source_checks() -> dict:
    A = [4, 4, 4, 2, 1]
    check("four_pole_polynomials", convolution([1, -1], A) == [4, 0, 0, -2, -1, -1])
    check("four_pole_polynomials", convolution([1, -1], [11, 7, 3, 1]) == [11, -4, -4, -2, -1])
    check("four_pole_polynomials", sum(A) == 15 and all(c > 0 for c in A))
    for n in range(1, 130):
        positive_integral = sum((F(c, 8*n-7+i)-F(c, 8*n-6+i) for i, c in enumerate(A)), F())
        check("four_pole_source", forcing(n) == positive_integral)
        check("four_pole_source", 0 < forcing(n) < F(15, (8*n-7)*(8*n-6)))
    depth = 24
    bounds = {}
    for n in range(1, 129):
        lo = sum((F(1, 16**j)*forcing(n+j) for j in range(1, depth+1)), F())
        hi = lo+F(1, 16**depth*(8*(n+depth)+1)*(8*(n+depth)+2))
        check("Green_tail_enclosures", 0 < lo < hi < F(1, (8*n+1)*(8*n+2)) < F(1, 64*n*n))
        bounds[n] = lo, hi
    pi_lo = 16*sum((F(1, 16**j)*forcing(j) for j in range(1, depth+1)), F())
    pi_hi = pi_lo+F(16, 16**depth*(8*depth+1)*(8*depth+2))
    check("BBP_sum_enclosure", 3 < pi_lo < pi_hi < F(22, 7))
    raw = []
    for B in (1, 2, 3, 7, 11, 19, 31, 64):
        mean_hi = sum((bounds[n][1] for n in range(B, 2*B)), F())/B
        paid = 8*pi_hi*mean_hi
        target = F(11, 28*B*B)
        check("infinite_mixture_Green_budget", paid < target)
        raw.append({"B": B, "tail_mean_upper": str(mean_hi), "energy_error_certified_upper": str(paid),
                    "published_rational_budget": str(target), "click_budget": str(target/2)})
    n = 19
    positive_mutant = F(4, 8*(n+1)-7)+F(2, 8*(n+1)-4)+F(1, 8*(n+1)-3)+F(1, 8*(n+1)-2)
    one_pole_mutant = forcing(n+1)+F(1, 8*(n+1)-7)
    check("mutation_controls", positive_mutant/16 > F(1, 64*n*n), "all-positive poles fail claimed Green bound")
    check("mutation_controls", one_pole_mutant/16 > F(1, 64*n*n), "coefficient4->5 fails claimed Green bound")
    states = [F()]
    for n in range(1, 52):
        states.append(16*states[-1]+forcing(n))
    words = [[1], [-16, 1], [256, -32, 1], [0], [3, -2, 7]]
    words += [[(i+3)*(j+1) % 11-5 for j in range(i+1)] for i in range(1, 9)]
    symbols = []
    for p in words:
        p = trim_poly(p.copy())
        h = sum(c*16**j for j, c in enumerate(p))
        residual = p.copy()
        q = [0]*max(0, len(p)-1)
        for j in range(len(p)-1, 0, -1):
            q[j-1] = residual[j]
            residual[j-1] += 16*residual[j]
        check("lag_polynomial_division", residual[0] == h)
        for n in range(19, 42):
            lhs = sum((F(c)*states[n+j] for j, c in enumerate(p)), F())
            rhs = h*states[n]+sum((F(c)*forcing(n+j+1) for j, c in enumerate(q)), F())
            check("source_echo_holdout", lhs == rhs)
        symbols.append({"coefficients": p, "P16": h, "graph_Haar_benchmark": int(h == 0)})
    return {"authority": "EXACT_FINITE rational source bounds and echo checks", "forcing_n_range": [1, 129],
            "tail_n_range": [1, 128], "tail_depth": depth, "BBP_sum_interval": [str(pi_lo), str(pi_hi)],
            "BBP_identity_scope": "Encloses the original four-pole sum exactly; identification with pi uses the inherited classical BBP formula.",
            "raw_Green_budgets": raw, "echo_source_clocks": [19, 41], "lag_words": symbols,
            "source_mutations": ["all signed residues made positive", "first signed residue4 changed to5"]}


def numeric_gamma_diagnostic() -> dict:
    try:
        import mpmath as mp
    except ImportError:
        return {"authority": "NOT_RUN", "reason": "mpmath unavailable; exact checks remain separate"}
    mp.mp.dps = 65
    raw, maximum = [], mp.mpf(0)
    for k in (0, 1, 2, 5, 8, 13, 21):
        integral = mp.quad(lambda t: mp.exp(-2*t)*t**k/mp.factorial(k), [0, 1, 4, 16, mp.inf])
        exact = mp.mpf(2)**(-k-1)
        err = abs(integral-exact)
        maximum = max(maximum, err)
        raw.append({"k": k, "integral": mp.nstr(integral, 55), "error": mp.nstr(err, 8)})
    return {"authority": "NUMERIC_DIAGNOSTIC_ONLY", "mpmath_version": mp.__version__, "decimal_precision": mp.mp.dps,
            "raw": raw, "maximum_absolute_error": mp.nstr(maximum, 8), "universal_conclusion": False}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE/'receipts'/'independent.json')
    args = parser.parse_args()
    started = time.monotonic()
    sections = {
        "shifted_gamma": exact_gamma_checks(),
        "poisson_kernel": kernel_checks(),
        "polarization": polarization_checks(),
        "finite_characters": walsh_checks(),
        "periodic_cosets_and_report_models": coset_and_report_checks(),
        "original_source": green_source_checks(),
        "Gamma_integral_holdouts": numeric_gamma_diagnostic(),
    }
    hashes = {}
    for path in (Path(__file__).resolve(), HERE/'THEOREMS.md', HERE/'FRONTIER_MAP.md', HERE/'FRONTIER_TARGETS.json',
                 ROOT/'observational_succ'/'universal_interference_detector.py'):
        hashes[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    receipt = {
        "status": "PASS", "audit_version": 1, "python": platform.python_version(),
        "authority": "EXACT_FINITE with separately labelled numerical diagnostics; no universal pi estimate",
        "independence_scope": "No production imports, production test imports, other-agent notes or production outputs. Reading theorem specifications is a shared premise, not source independence.",
        "counts": dict(sorted(COUNTS.items())), "total_exact_assertions": sum(COUNTS.values()),
        "elapsed_seconds": round(time.monotonic()-started, 3), "hashes": hashes, "sections": sections,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({"status": receipt['status'], "receipt": str(args.out), "exact_assertions": receipt['total_exact_assertions'],
                      "elapsed_seconds": receipt['elapsed_seconds'], "sha256": sha256(args.out.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
