"""Exact finite controls for COLD_SHELL_EXCEPTIONAL_SET.md; no asymptotic claims."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def nearest(x):
    y = x + F(1, 2)
    return y.numerator // y.denominator


def check(x, B, M):
    q = [nearest(16**n * x) for n in range(B, M + 1)]
    t = [16**n * x - q[n - B] for n in range(B, M + 1)]
    a = [q[j + 1] - 16*q[j] for j in range(M - B)]
    assert all(-8 <= v <= 8 for v in a)
    energy = sum(v*v for v in t[:-1])
    rhs = 289*energy + 17*(t[-1]**2 - t[0]**2)
    assert rhs - sum(v*v for v in a) == 16*sum(
        (t[j] + t[j + 1])**2 for j in range(M - B))
    assert sum(v != 0 for v in a) <= sum(v*v for v in a)
    assert sum(v*v for v in a) <= 289*energy + F(17, 4)
    reconstruction = q[0]
    for v in a:
        reconstruction = 16*reconstruction + v
    assert reconstruction == q[-1]
    assert abs(x - F(reconstruction, 16**M)) <= F(1, 2*16**M)
    return energy, a


def main():
    cases = 0
    for denominator in (2, 3, 7, 15, 17, 31, 127):
        for numerator in range(denominator + 1):
            for B, M in ((1, 2), (3, 7), (8, 16), (11, 17)):
                check(F(numerator, denominator), B, M)
                cases += 1
    energy, a = check(F(8, 17), 4, 20)
    assert sum(v*v for v in a) == 289*energy
    assert sum(v*v for v in a) > 288*energy
    energy, a = check(F(1, 15), 4, 20)
    assert energy / 16 == F(1, 225)
    forced = []
    for B, M in ((4, 8), (5, 12), (7, 21), (16, 32)):
        x = F(3, 16**B) + F(14, 16**(M + 1)) + F(9, 16**(M + 3))
        energy, a = check(x, B, M)
        assert energy/(M - B) < F(1, 255*(M - B))
        forced.append({'B': B, 'M': M, 'energy': str(energy/(M - B))})
    result = {
        'rational_case_checks': cases,
        'all_exact_checks_passed': True,
        'sharp_289_control': '8/17, alternating residual +/-8/17 and |a|=8',
        'mutant_288_rejected': True,
        'fixed_nonunit_energy': '1/225',
        'forced_zero_cases': forced,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Finite calibration; dimension and residuality rest on paper proof',
    }
    Path(__file__).with_name('finite_cover_receipt.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
