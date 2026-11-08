"""Execute the preregistered finite covariance experiment; exact endpoints."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from intervals import SCALE, BITS, Box, phase
from source import common_history, direct_modular_residue, principal_pair, matched_seed
from prime_epochs import good_prime, order16, variation

HARMONICS = (1, 2, 3, 5)


def epoch(A):
    start = time.monotonic()
    p = good_prime(A)
    if p is None:
        raise ValueError('preregistered prime selector undefined at this epoch')
    data = common_history(2*A-1, A)
    D, residues = data['denominator'], data['residues']
    checks = (A, A+A//2, 2*A-1)
    for n in checks:
        assert residues[n-A] == direct_modular_residue(n, D)
    primes = tuple(sorted({3, 5, 7, 11, p}))
    seed, center, M = matched_seed(data, A, 32, Q(1, 2**20), primes)
    q = seed.denominator
    shift = seed.numerator*pow(16, A, q) % q
    totals = {h: [Box() for _ in range(5)] for h in HARMONICS}
    # Columns: original W, common a, original b, shadow W, shadow b.
    for residue in residues:
        an, ad = principal_pair(residue, D, p)
        shadow = residue*q+shift*D
        for h, columns in totals.items():
            phases = ((h*residue, D), (h*an, ad),
                      (h*(residue*ad-an*D), D*ad),
                      (h*shadow, D*q),
                      (h*(shadow*ad-an*D*q), D*q*ad))
            for j, (num, den) in enumerate(phases):
                columns[j] = columns[j]+phase(num, den)
        # q is p-coprime, so this is an exact matched principal-part control.
        assert q % p
        shift = 16*shift % q
    rows = []
    for h, columns in totals.items():
        w, a, b, sw, sb = [c.divide(A) for c in columns]
        cov, shadow_cov = w-a*b, sw-a*sb
        square = cov.norm_squared()
        limit = Q(16, A)
        verdict = ('PASS_FINITE' if Q(square.hi, SCALE) <= limit else
                   'REFUTED_FINITE' if Q(square.lo, SCALE) > limit else 'INCONCLUSIVE')
        assert sw.re.lo > SCALE*99//100
        rows.append({'h': h, 'W': w.as_dict(), 'a': a.as_dict(), 'b': b.as_dict(),
                     'covariance': cov.as_dict(), 'shadow_W': sw.as_dict(),
                     'shadow_b': sb.as_dict(), 'shadow_covariance': shadow_cov.as_dict(),
                     'R4_status': verdict})
    J = min(16, A-1)
    prefix = common_history(J)
    prefix_ok = all((r*seed.denominator+16**n*seed.numerator*prefix['denominator'])
                    // (prefix['denominator']*seed.denominator) == 0
                    for n, r in enumerate(prefix['residues']))
    assert prefix_ok
    return {'A': A, 'p': p, 'order': order16(p), 'epoch_gluing_l1': str(variation(A, p)),
            'source_denominator_bits': D.bit_length(),
            'source_denominator_sha256': sha256(D.to_bytes((D.bit_length()+7)//8, 'big')).hexdigest(),
            'unwrapped_sha256': data['unwrapped_sha256'], 'carry_sha256': data['carry_sha256'],
            'independent_modular_checks': list(checks),
            'shadow': {'seed_numerator_hex': hex(seed.numerator), 'seed_denominator_hex': hex(q),
                       'J': J, 'K': 32, 'eta': '1/1048576', 'matched_primes': list(primes),
                       'exact_prefix_carries_preserved': prefix_ok,
                       'literal_zero_authenticated': False,
                       'source_support_authenticated': False},
            'rows': rows, 'seconds': time.monotonic()-start}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stage', choices=('pilot', 'holdout', 'stress'), required=True)
    args = parser.parse_args()
    epochs = {'pilot': (32, 64, 128), 'holdout': (257, 509, 1021, 2039), 'stress': (4093,)}[args.stage]
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    for A in epochs:
        row = epoch(A)
        path = args.output/f'epoch_{A}.json'
        path.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
        results.append({'A': A, 'file': path.name, 'sha256': sha256(path.read_bytes()).hexdigest()})
        print(A, row['p'], round(row['seconds'], 3), [r['R4_status'] for r in row['rows']], flush=True)
    files = [HERE/'intervals.py', HERE/'source.py', HERE/'run_experiment.py', HERE/'PREREGISTRATION.md']
    result = {'stage': args.stage, 'bits': BITS, 'scale': SCALE,
              'source_head': '47ec1ccf9d3579897abb94c047f3b4dc13b4cb70',
              'preregistration_commit': 'fd925707',
              'hashes': {p.name: sha256(p.read_bytes()).hexdigest() for p in files},
              'epochs': results, 'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (args.output/f'{args.stage}.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
