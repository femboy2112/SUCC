"""Independent exact edge audit for the effective BBP prime-survival lemma.

No imports from the prime-survival author's implementation. These finite
cases supplement the separate paper proof; they do not prove the all-n claim.
"""
from fractions import Fraction as F
from math import comb, lcm


def audit():
    principal_part_cases = 0
    prime_records = []
    for p in (11, 13, 17, 23):
        U = F(0)
        prime_cases = 0
        for n in range(1, (p*p-1)//8+1):
            # Direct original four-pole state, not the collapsed source formula.
            U = (16*U + F(4, 8*n-7) - F(2, 8*n-4)
                 - F(1, 8*n-3) - F(1, 8*n-2))
            terms = []
            chi = 1 if p % 8 in (1, 7) else -1
            for a, b in ((8, 7), (8, 3), (4, 1), (2, 1)):
                for j in range(1, n+1):
                    den = a*j-b
                    if den % p:
                        continue
                    k = den//p
                    if a == 8 and b == 7:
                        value = F(4, k)*chi*F(2)**((1-k)//2)
                    elif a == 8:
                        value = F(-1, k)*chi*F(2)**((5-k)//2)
                    elif a == 4:
                        value = -F(2)**(2-k)/k
                    else:
                        value = -F(2)**(1-2*k)/k
                    terms.append(value)
            if not terms:
                continue

            coefficient = sum(terms, F())
            K = (8*n-2)//p
            principal = p*U
            lhs = principal.numerator*pow(principal.denominator, -1, p) % p
            rhs = (pow(16, n-(p+1)//2, p)*coefficient.numerator
                   * pow(coefficient.denominator, -1, p)) % p
            assert lhs == rhs, (p, n, 'principal-part normalization')
            assert (coefficient > 0) == (p % 4 == 1), (p, n, 'rational sign')
            assert abs(coefficient) < F(64, 15), (p, n, 'absolute bound')
            Lambda = lcm(*range(1, K+1))
            assert (2**(K//2)*Lambda) % coefficient.denominator == 0, (p, n, 'height')
            if p*p >= 19*32**K:
                assert U.denominator % p == 0, (p, n, 'certified survival')
            principal_part_cases += 1
            prime_cases += 1
        prime_records.append((p, prime_cases))

    lcm_cases = 0
    for K in (1, 2, 3, 4, 5, 7, 8, 9, 15, 16, 17, 31, 32, 33, 63, 64, 65):
        t = (K+1)//2
        top = lcm(*range(1, K+1))
        half = lcm(*range(1, t+1))
        assert comb(K, K//2) % (top//half) == 0, (K, 'LCM quotient divisibility')
        assert top <= 4**K, (K, 'LCM height')
        lcm_cases += 1

    assert principal_part_cases == 128
    assert lcm_cases == 17
    print(f'PASS: {principal_part_cases} exact principal-part cases, '
          f'{lcm_cases} LCM cases; {principal_part_cases+lcm_cases} total cases.')
    print(f'Born-time cases by prime: {prime_records}')
    print('Each principal-part case checks direct original recurrence, four-lane '
          'normalization, rational sign, absolute bound and denominator height; '
          'certified cases also check survival.')
    print('Scope: same-model independent implementation; finite edge audit, '
          'not a universal proof or external mathematical referee.')


if __name__ == '__main__':
    audit()
