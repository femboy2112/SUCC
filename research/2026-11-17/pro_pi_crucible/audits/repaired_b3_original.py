"""One exact repaired ANC-12 witness; no asymptotic test is claimed."""

from fractions import Fraction
from math import gcd, prod
import json
from pathlib import Path


def source_r(n):
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def factor(n):
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


# Preregistered repair target: preserve reduced Q, the modulus-16^B
# 2-adic projection and each selected p-principal part, and force D=J=0.
# Fail on any mismatch. This is one finite exact check, not an all-B test.
B = 3
u = Fraction(0)
for n in range(1, 2*B+1):
    u = 16*u + source_r(n)
N, Q = u.numerator, u.denominator
selected_primes = (19, 23, 29, 37, 41)
pi_star = prod(selected_primes)
q = Q // pi_star
radix_modulus = 16**B
M = radix_modulus*pi_star
R0 = N % M
C = N // Q
C_zero = radix_modulus*(C // radix_modulus)
assert (N, Q, pi_star, M, R0) == (
    80827484660698633414, 24536311574775, 19224941,
    78745358336, 67379365062,
)
assert gcd(M, q) == 1
assert gcd(R0, Q) == 3  # preserve the original failure

# Search only the candidates that actually fit inside [0,Q).
candidate_count = (Q-1-R0)//M + 1
t = next(t for t in range(candidate_count) if gcd(R0+t*M, q) == 1)
R = R0+t*M
v = C_zero + Fraction(R, Q)
delta = v-u
assert 0 <= R < Q
assert v.denominator == Q
assert delta.numerator % radix_modulus == 0
assert gcd(delta.denominator, 2) == 1
assert v.numerator // v.denominator == C_zero
assert C_zero % radix_modulus == 0
projection_2adic = lambda z: (z.numerator * pow(z.denominator, -1, radix_modulus)) % radix_modulus
assert projection_2adic(u) == projection_2adic(v)
principal_records = []
for p in selected_primes:
    assert Q % p == 0 and Q % (p*p) != 0
    assert delta.denominator % p != 0
    old, new = p*u, p*v
    residue = lambda z: (z.numerator * pow(z.denominator, -1, p)) % p
    assert residue(old) == residue(new) != 0
    principal_records.append({"p": p, "old_residue": residue(old),
                              "repaired_residue": residue(new)})
energy = sum((v/16**k - (v/16**k).__floor__())**2 for k in range(1, B+1))/B
expected = Fraction(R, Q)**2 * (1-Fraction(1, 256**B))/(255*B)
assert energy == expected < Fraction(1, 255*B)
receipt = {
    "scope": "one exact B=3 repaired clone; no all-B assertion",
    "pin_audited": "97c7433371feca631991a1b8227b656e92e4abcb",
    "B": B, "N": str(N), "Q": str(Q), "Pi_star": str(pi_star),
    "M": str(M), "Q_coll": str(q), "Q_coll_factorization": factor(q),
    "R_original": str(R0), "original_gcd_R_Q": gcd(R0, Q),
    "original_reduced_denominator": str((C_zero + Fraction(R0, Q)).denominator),
    "candidate_count_that_fit": candidate_count,
    "first_coprime_t": t, "R_repaired": str(R),
    "C_original": str(C), "C_zero": str(C_zero),
    "repaired_numerator": str(v.numerator), "repaired_denominator": str(v.denominator),
    "repaired_gcd_R_Q": gcd(R, Q),
    "2adic_mod_16B_original": projection_2adic(u),
    "2adic_mod_16B_repaired": projection_2adic(v),
    "prime_principal_parts": principal_records,
    "low_B_digits": "0"*B, "D_B": 0, "J_B": 0,
    "terminal_norm": str(energy), "terminal_norm_upper_bound": str(Fraction(1, 255*B)),
    "all_assertions_passed": True,
}
out = json.dumps(receipt, indent=2)
Path(__file__).with_name("repaired_b3_receipt.json").write_text(out + "\n")
print(out)
