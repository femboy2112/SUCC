"""Preregistered independent selector and exact finite cap checks."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys
from explicit_selector import select, primes_to, order16_factored, classical_cap8, eighth_root_interval
from lag_instrument import HERE, ROOT, SCALE, phase, mean
sys.path.insert(0, str(ROOT/'research/2026-11-07/learning_yoneda/arithmetic'))
from prime_epochs import good_prime, order16, variation


def run():
    choices = []
    for C in (1, 2, 3):
        # Independent trial primality and orbit multiplication, not factoring.
        candidates = []
        for p in range(3, 1201, 2):
            if p % 8 != 1 or any(p % d == 0 for d in range(2, p)):
                continue
            m = order16(p)
            if m**3 > p and m*m*p.bit_length()**(2*C) > p:
                candidates.append(p)
        for A in range(5, 301):
            admissible = [p for p in candidates if p <= 4*A]
            expected = max(admissible) if admissible else None
            got = select(A, C)
            assert (got[0] if got else None) == expected
            if got:
                assert got[1] == order16(got[0])
            choices.append({'A': A, 'C': C, 'selected': got})

    cap_rows = []
    invariance_checks = 0
    for p in (17, 41, 73, 89, 97, 137, 193, 233, 281, 353, 617, 769, 1009, 1217):
        m = order16_factored(p)
        G = [pow(16, r, p) for r in range(m)]
        remaining = set(range(1, p))
        cap8 = classical_cap8(p, m)
        cap = eighth_root_interval(cap8)
        cosets = []
        phases = [phase(n, p) for n in range(p)]
        while remaining:
            xi = min(remaining)
            coset = {xi*g % p for g in G}
            for c in coset:
                assert {c*g % p for g in G} == coset
                invariance_checks += 1
            value = mean(phases[r] for r in sorted(coset))
            norm8 = value.norm_squared().square().square()
            assert Q(norm8.hi, SCALE) <= cap8
            cosets.append({'xi': xi, 'mean': value.as_dict(), 'norm8': norm8.as_list()})
            remaining -= coset
        cap_rows.append({'p': p, 'm': m, 'cap8': str(cap8), 'cap': cap.as_list(), 'cosets': cosets})

    divisibility_checks = 0
    for X in (64, 128, 256, 512, 1024, 2048):
        for Y in (1, 2, 3, 5, 8, 13, 21):
            product = 1
            for j in range(1, Y+1):
                product *= 16**j-1
            for p in primes_to(X):
                if p != 2 and order16_factored(p) <= Y:
                    assert product % p == 0
                    divisibility_checks += 1
            # Exact version of log V_Y < log16*Y(Y+1)/2.
            assert product < 16**(Y*(Y+1)//2)

    source_rows = []
    for A in (97, 307, 613, 1229):
        p, m = select(A, 2)
        prior = HERE/'receipts'/f'lag_{A}.json'
        receipt = json.loads(prior.read_text())
        assert receipt['p'] == p == good_prime(A)
        assert receipt['m'] == m
        assert receipt['epoch_gluing_l1'] == str(variation(A, p))
        # Receipt hashes link the already executed literal source/sample checks.
        source_rows.append({'A': A, 'p': p, 'm': m, 'prior_sha256': sha256(prior.read_bytes()).hexdigest(),
                            'source_unwrapped_sha256': receipt['source_unwrapped_sha256'],
                            'exact_weight_distance': str(variation(A, p)),
                            'source_checks_reused': receipt['independent_source_checks']})
    return {'selector_comparisons': len(choices), 'choices': choices, 'cap_rows': cap_rows,
            'multiplicative_invariance_checks': invariance_checks, 'order_product_checks': divisibility_checks,
            'source_rows': source_rows, 'protocol_commit': 'f6d72def', 'pi_normality': 'OPEN', 'RH': 'OPEN'}


if __name__ == '__main__':
    output = Path(sys.argv[1])
    output.write_text(json.dumps(run(), indent=2, sort_keys=True)+'\n')
