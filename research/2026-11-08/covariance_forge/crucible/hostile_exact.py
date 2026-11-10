"""Exact finite controls for source isolation, growing memory and covariance.

Universal statements are proved in THEOREMS.md. This code is a bounded oracle,
not a claim of pi normality or a test of infinitely many source epochs.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from math import comb, gcd, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
PRIOR = ROOT / "research/2026-11-07/learning_yoneda/arithmetic/finite_adelic.py"
spec = importlib.util.spec_from_file_location("previous_finite_adelic_hostile", PRIOR)
prior = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = prior
spec.loader.exec_module(prior)


def literal_history(last):
    u = [Q()]
    for n in range(1, last+1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        u.append(16*u[-1]+r)
    return u


def vprime(x, p):
    if x == 0:
        return None  # infinity
    numerator, denominator = abs(x.numerator), x.denominator
    exponent = 0
    while numerator%p == 0:
        numerator //= p
        exponent += 1
    while denominator%p == 0:
        denominator //= p
        exponent -= 1
    return exponent


def source_sigma(values):
    return min((1-value%1)/16**n for n, value in enumerate(values))


def two_prime_clock(p, q):
    period = p*q
    values = [Q(n//q, p)-Q(n//p, q) for n in range(period)]
    second = sum((u*u for u in values), Q())/period
    formula = Q(2*p*p+2*q*q-3*p*q-1, 6*p*p*q*q)
    assert second == formula
    return values, second, 1-20*second


def run():
    counts = Counter()
    def check(truth, family):
        if not truth:
            raise AssertionError(family)
        counts[family] += 1

    # Sharp rational isolation with denominator height and local divisibility.
    for primes, powers in (((), ()), ((2,), (3,)), ((3, 5), (1, 0)),
                           ((2, 3, 5), (1, 1, 0))):
        divisor = prod(p**k for p, k in zip(primes, powers))
        forbidden = prod(primes)
        for bound in (7, 13, 29, 43):
            qstar = max(q for q in range(1, bound+1) if gcd(q, forbidden) == 1)
            delta = Q(divisor, qstar)
            admitted = []
            for q in range(1, bound+1):
                for a in range(-2*divisor, 2*divisor+1):
                    x = Q(a, q)
                    if x and all(vprime(x, p) >= k for p, k in zip(primes, powers)):
                        check(abs(x) >= delta, "sharp_height_isolation")
                        admitted.append(abs(x))
            check(min(admitted) == delta, "height_threshold_attained")
    # Matching every odd place alone does not exclude a dyadic denominator.
    for depth in (1, 4, 9):
        x = Q(1, 2**depth)
        check(x != 0, "omitted_two_place")
        for p in prior.primes_through(101):
            check(prior.principal(x, p) == 0, "omitted_two_place")

    # Finite denominator-support plus all its local principal parts isolates
    # integers. This explicitly refutes a universal finite-memory no-go.
    for q in range(1, 101):
        remaining = q
        for p in (3, 5):
            while remaining%p == 0:
                remaining //= p
        if remaining != 1:
            continue
        for a in range(-7, 8):
            x = Q(a, q)
            if all(prior.principal(x, p) == 0 for p in (3, 5)):
                check(x.denominator == 1, "complete_support_isolation")

    # Elementary lcm bound used for a uniform original-source carry cylinder.
    lcms = [1]
    for n in range(1, 321):
        lcms.append(lcm(lcms[-1], n))
        check(lcms[n] <= 4**n, "elementary_lcm_bound")
        if n >= 2:
            check((comb(n, n//2)*lcms[(n+1)//2])%lcms[n] == 0, "lcm_divisibility")
    values = literal_history(40)
    for J in range(41):
        sigma = source_sigma(values[:J+1])
        check(Q(1, 16**(5*J)) <= sigma <= Q(1, 16**J), "carry_cylinder_bound")
        check(all((value+16**n*sigma/2)//1 == value//1
                  for n, value in enumerate(values[:J+1])), "carry_inside")
        check(any((value+16**n*sigma)//1 != value//1
                  for n, value in enumerate(values[:J+1])), "carry_boundary_rejected")
        if J:
            check(lcms[8*J]%values[J].denominator == 0, "source_denominator_divides_lcm")

    growing = []
    for A in (43, 89, 173):
        J, B, K = (A-1)//5, 2*A-1, 2*A
        primes = prior.primes_through(8*B)
        witness = prior.construct(J, A, A, K, Q(1, 8), primes)
        original = literal_history(B)
        shadow = witness["shadow"]
        seed = witness["seed"]
        check(witness["original"] == original, "independent_literal_source")
        sigma = source_sigma(original[:J+1])
        check(0 < seed < sigma, "growing_carry_seed_inside")
        for n in range(J+1):
            check(shadow[n]//1 == original[n]//1, "growing_exact_floors")
        for n in range(1, J+1):
            check(shadow[n]//1-16*(shadow[n-1]//1) ==
                  original[n]//1-16*(original[n-1]//1), "growing_exact_carries")
        for p in primes:
            check(seed.denominator%p != 0, "all_finite_places_match_certificate")
        for n in (0, J, A, B):
            check(vprime(shadow[n]-original[n], 2) >= K+4*n, "growing_two_adic_precision")
            for p in (3, 5, 7, primes[-1]):
                check(prior.principal(shadow[n], p) == prior.principal(original[n], p),
                      "fresh_principal_spotcheck")
        error = 20*(Q(1, 225*(A+1)**4)+Q(1, 64*A)*Q(256, 255)*(1-Q(1, 256**A)))
        check(error < Q(1, 100), "coherent_epoch_lower_bound")
        growing.append({"A": A, "J": J, "B": B, "K": K,
                        "prime_count": len(primes), "seed_denominator_bits": seed.denominator.bit_length(),
                        "seed_numerator_hex": hex(seed.numerator),
                        "seed_denominator_hex": hex(seed.denominator),
                        "sigma_J": str(sigma), "prefix_error_upper": str(Q(9, 8)*Q(1, 16**(A-J))),
                        "h1_real_W_lower": str(1-error),
                        "seed_is_zero": False, "new_denominator_support": True})

    clocks = []
    for p, q in ((3, 5), (13, 17), (17, 29)):
        path, square, lower = two_prime_clock(p, q)
        check(path[0] == 0, "clock_zero_boundary")
        check(Counter(n//q for n in range(p*q)) == {j: q for j in range(p)}, "exact_local_zero_mean")
        check(Counter(n//p for n in range(p*q)) == {j: p for j in range(q)}, "exact_complement_zero_mean")
        for n, x in enumerate(path):
            check((p*q)%x.denominator == 0, "clock_fixed_denominator_support")
            check(prior.principal(x, p) == Q(n//q, p), "clock_authentic_principal_decomposition")
        check(lower > Q(1, 2), "clock_positive_signed_covariance")
        changed_forcing = path[1]-16*path[0]
        check(changed_forcing != prior.forcing(1), "wrong_four_pole_source_rejected")
        clocks.append({"p": p, "q": q, "period": p*q,
                       "mean_square_phase": str(square), "Re_covariance_lower": str(lower),
                       "both_marginals_zero_each_period": True,
                       "source_is_original_BBP": False})
    return {"status": "CERTIFIED-FINITE", "checks": dict(sorted(counts.items())),
            "total_checks": sum(counts.values()), "growing_memory": growing,
            "two_prime_clocks": clocks, "prior_module_sha256": sha256(PRIOR.read_bytes()).hexdigest(),
            "universal_proofs": "THEOREMS.md", "pi_normality": "OPEN", "RH": "OPEN"}


if __name__ == "__main__":
    receipt = run()
    (HERE/"EXACT_RECEIPTS.json").write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": receipt["status"], "total_checks": receipt["total_checks"],
                      "checks": receipt["checks"]}, sort_keys=True))
