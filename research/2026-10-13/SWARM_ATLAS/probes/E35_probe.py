"""Bounded E35 exact witnesses; no floating-point or completion inference."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, gcd
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from observational_succ.clock_mahler_interpolation import (
    ClockInterpolationError, local_euler_from_mahler_truncation,
    kummer_clock_witness,
)
from observational_succ.prime_clock_yoneda import (
    ArithmeticFunctorError, PrimeClockSource, verify_arithmetic_source_signature,
)

PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
SOURCE_PATHS = (
    "observational_succ/clock_mahler_interpolation.py",
    "observational_succ/prime_clock_yoneda.py",
    "observational_succ/coverage_sieve_crt.py",
    "observational_succ/arithmetic.py",
    "provenance/IMPORT_MANIFEST.json",
)


def v(value, p):
    value = Q(value)
    if not value:
        return None  # positive infinity; JSON null is declared explicitly
    num, den, out = abs(value.numerator), value.denominator, 0
    while num % p == 0:
        num //= p
        out += 1
    while den % p == 0:
        den //= p
        out -= 1
    return out


def choose(x, j):
    value = Q(1)
    for k in range(j):
        value *= Q(x-k, k+1)
    return value


def differences(values):
    row, out = list(map(Q, values)), []
    while row:
        out.append(row[0])
        row = [b-a for a, b in zip(row, row[1:])]
    return out


def digit_spread(n):
    out, j = 0, 0
    while n:
        out += (n % 2) * 2**(2*j)
        n //= 2
        j += 1
    return out


def crt(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + m * ((b-a) * pow(m, -1, n) % n)) % (m*n)


def rejected(call, exception):
    try:
        call()
    except exception:
        return True
    raise AssertionError("Negative source control was admitted")


def main():
    sources = {}
    for name in SOURCE_PATHS:
        frozen = subprocess.check_output(["git", "show", f"{PARENT}:{name}"], cwd=ROOT)
        live = (ROOT/name).read_bytes()
        assert live == frozen, name
        sources[name] = sha256(live).hexdigest()
    manifest = json.loads((ROOT/"provenance/IMPORT_MANIFEST.json").read_text())
    origin_check = subprocess.run(
        ["git", "cat-file", "-t", manifest["source_commit"]], cwd=ROOT,
        capture_output=True, text=True,
    )
    archival_path = "provenance/origins/fuckingrh/research/2026-10-10/CERTIFIED_FINITE_PRIME_TRANSPORT.md"
    archival_blob = subprocess.check_output(["git", "hash-object", archival_path], cwd=ROOT, text=True).strip()
    assert archival_blob == "738a5f9884bbd6d49c26ef1a685e3c50bb8eb58e"

    coefficients = differences([(-2)**n for n in range(11)])
    assert coefficients == [Q((-3)**j) for j in range(11)]
    assert all(sum(coefficients[j]*choose(n,j) for j in range(n+1)) == (-2)**n
               for n in range(11))
    torsion = differences([(-1)**n for n in range(11)])
    assert torsion == [Q((-2)**j) for j in range(11)]
    parity = [{"r":r, "input":3**r, "output_difference":-2,
               "v3_output_difference":v(-2,3)} for r in range(1,7)]
    assert all((-1)**row["input"] == -1 for row in parity)

    assert choose(0,2) == 0 and choose(2,2) == 1
    delayed = []
    for r in range(1,7):
        for x in range(2**(r+2)):
            defect = choose(x+2**(r+1),2)-choose(x,2)
            assert defect.denominator == 1 and defect.numerator % 2**r == 0
        delayed.append({"output_depth":r, "input_depth":r+1})

    spread = []
    for j in range(7):
        assert digit_spread(2**j) == 4**j
        assert digit_spread(3*2**j) == 5*4**j
        spread.append({"j":j, "first_quadratic_ratio":"1",
                       "second_quadratic_ratio":str(Q(digit_spread(3*2**j),(3*2**j)**2))})
    for r in range(1,7):
        for n in range(128):
            assert (digit_spread(n+2**r)-digit_spread(n)) % 2**(2*r) == 0

    prefix = [choose(n,3) for n in range(3)]
    assert prefix == [0,0,0] and choose(-1,3) == -1
    bad_values = [sum(comb(n,j) for j in range(3,n+1)) for n in range(11)]
    assert differences(bad_values) == [0,0,0]+[1]*8
    assert all(sum(comb(2**r,j) for j in range(3,2**r+1)) % 2 == 1
               for r in range(2,7))

    sync, old = [], 0
    for r in range(1,7):
        a = crt(0,2**r,1,3**r)
        assert a % 2**r == 0 and a % 3**r == 1
        if r > 1:
            assert a % 6**(r-1) == old
        sync.append({"r":r, "residue":a, "modulus":6**r})
        old = a
    assert not any(n % 2 == 0 and n % 4 == 1 for n in range(4))
    assert 1 % 2 != 0  # independent constants at depth 1/2 fail reduction

    fine = PrimeClockSource(2,2,1,1,3)
    alias = PrimeClockSource(2,1,1,1,5)
    assert all(3*n % 2 == 5*n % 2 for n in range(2))
    assert rejected(lambda: verify_arithmetic_source_signature(fine,alias), ArithmeticFunctorError)
    assert rejected(lambda: PrimeClockSource(2,2,1,1,6), ArithmeticFunctorError)
    assert rejected(lambda: local_euler_from_mahler_truncation(6,4), ClockInterpolationError)
    assert Q(1,1-6)-sum((Q(6)**j for j in range(4)),Q()) == Q(6**4,1-6)

    receipt = {
        "investigator":"E35", "status":"TESTED MODEL; proofs are in E35.md",
        "source_parent":PARENT, "source_sha256":sources,
        "import_provenance":{"declared_origin_commit":manifest["source_commit"],
                             "local_origin_object_check_exit":origin_check.returncode,
                             "archival_source_git_blob":archival_blob},
        "primary_pdf_sha256":{
            "https://carmamaths.org/resources/mahler/docs/139.pdf":"a44c323551af254685774dfb604193342f326c21eb3b3935b9ee1e9774e0baef",
            "https://numdam.org/article/BSMF_1964__92__117_0.pdf":"897dbb6a77b3a97ce0672279f16e58c95f7ced384bfcb7fb5c3b0b2fba3b5523",
        },
        "command":"python research/2026-10-13/SWARM_ATLAS/probes/E35_probe.py",
        "exit_code":0, "arithmetic":"integers and Fractions only",
        "bounds":{"difference_order":10,"clock_depth":6,"digit_inputs":128},
        "zero_valuation_encoding":"null means positive infinity",
        "mahler_exponential_coefficients":[str(a) for a in coefficients],
        "odd_prime_parity_counterclock":parity,
        "two_adic_parity_coefficient_valuations":[v(a,2) for a in torsion],
        "smallest_polynomial_counterclock":{"p":2,"depth":1,"inputs":[0,2],"outputs":[0,1],"degree":2},
        "delayed_precision_control":delayed,
        "compatible_nonanalytic_digit_map":spread,
        "finite_prefix_ambiguity":{"known_values":[0,0,0],"alternative_at_minus_one":"-1","discontinuous_tail_coefficients":[1]*8},
        "crt_synchronized_two_place_sequence":sync,
        "unit_period_generalized_crt_failure":{"periods":[2,4],"residues":[0,1]},
        "incoherent_finite_tower":{"depth_one_value":0,"depth_two_value":1},
        "native_local_euler":local_euler_from_mahler_truncation(3,4),
        "native_kummer_control":kummer_clock_witness(5,2,2),
        "native_composite_rejection":True,"native_true_prime_alias_rejection":True,
        "fake_composite_geometric_identity_still_holds":True,
        "non_euler_control":"digit-spread has all clock coherence without analytic source identity",
        "physical_source_authentication":False,"p_adic_measure_constructed":False,
        "analytic_completion_constructed":False,"nontrivial_zero_inputs":False,"RH_claimed":False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
