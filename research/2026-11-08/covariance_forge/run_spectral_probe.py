"""Certified best-sparse residual and signed Fourier reconstruction probe."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from intervals import SCALE, BITS, Box, Interval, phase, mean, ZERO
from source import common_history, principal_pair, matched_seed
from prime_epochs import order16


def dft(values, roots):
    m = len(values)
    return [mean(values[j]*roots[(-k*j) % m] for j in range(m)) for k in range(m)]


def sparse_record(values, transforms, s):
    norm = ZERO
    for value in values:
        norm = norm+value.norm_squared()
    norm = norm.divide(len(values))
    energies = [value.norm_squared() for value in transforms]
    # The sum of the largest upper endpoints bounds every s-element support.
    top_upper = sum(sorted((e.hi for e in energies), reverse=True)[:s])
    top_lower = sum(sorted((e.lo for e in energies), reverse=True)[:s])
    residual = Interval(max(0, norm.lo-top_upper), max(0, norm.hi-top_lower))
    verdict = ('REFUTED_FINITE' if residual.lo > SCALE//4 else
               'PASS_FINITE' if residual.hi <= SCALE//4 else 'INCONCLUSIVE')
    return {'norm_squared': norm.as_list(), 'best_sparse_residual_squared': residual.as_list(),
            'hypothesis_error_at_most_half': verdict,
            'coefficients': [t.as_dict() for t in transforms]}


def probe(p):
    started = time.monotonic()
    L = (p-1)//4
    A, B = L+1, 2*L
    m = order16(p)
    assert p % 8 == 1 and L % m == 0 and m**3 > p
    cycles = L//m
    data = common_history(B, A)
    D = data['denominator']
    seed, _, _ = matched_seed(data, A, 32, Q(1, 2**20), (3, 5, 7, 11, p))
    q = seed.denominator
    roots = [phase(j, m) for j in range(m)]
    rows = []
    for h in (1, 2):
        a, folded, shadow_folded, full, shadow_full = [], [Box() for _ in range(m)], [Box() for _ in range(m)], [], []
        shift = seed.numerator*pow(16, A, q) % q
        for j, residue in enumerate(data['residues']):
            an, ad = principal_pair(residue, D, p)
            aa = phase(h*an, ad)
            if j < m:
                a.append(aa)
            else:
                assert aa == a[j % m]
            b = phase(h*(residue*ad-an*D), D*ad)
            shadow = residue*q+shift*D
            sb = phase(h*(shadow*ad-an*D*q), D*q*ad)
            folded[j % m] = folded[j % m]+b
            shadow_folded[j % m] = shadow_folded[j % m]+sb
            full.append(phase(h*residue, D))
            shadow_full.append(phase(h*shadow, D*q))
            shift = 16*shift % q
        folded = [b.divide(cycles) for b in folded]
        shadow_folded = [b.divide(cycles) for b in shadow_folded]
        ahat, bhat, shat = dft(a, roots), dft(folded, roots), dft(shadow_folded, roots)
        cross = [ahat[k]*bhat[-k % m] for k in range(m)]
        shadow_cross = [ahat[k]*shat[-k % m] for k in range(m)]
        transformed = Box()
        shadow_transformed = Box()
        for c, sc in zip(cross, shadow_cross):
            transformed = transformed+c
            shadow_transformed = shadow_transformed+sc
        w, sw = mean(full), mean(shadow_full)
        assert w.re.overlaps(transformed.re) and w.im.overlaps(transformed.im)
        assert sw.re.overlaps(shadow_transformed.re) and sw.im.overlaps(shadow_transformed.im)
        s = isqrt(m)
        rows.append({'h': h, 's': s, 'W': w.as_dict(), 'shadow_W': sw.as_dict(),
                     'prime_max_bin_energy': [max(t.norm_squared().lo for t in ahat),
                                              max(t.norm_squared().hi for t in ahat)],
                     'original': sparse_record(folded, bhat, s),
                     'shadow': sparse_record(shadow_folded, shat, s),
                     'signed_cross_spectrum': [c.as_dict() for c in cross],
                     'shadow_signed_cross_spectrum': [c.as_dict() for c in shadow_cross],
                     'transformed_W': transformed.as_dict(),
                     'shadow_transformed_W': shadow_transformed.as_dict()})
    return {'p': p, 'A': A, 'length': L, 'order': m, 'cycles': cycles,
            'unwrapped_sha256': data['unwrapped_sha256'], 'carry_sha256': data['carry_sha256'],
            'rows': rows, 'seconds': time.monotonic()-started}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    for p in (281, 617, 1009, 1601, 2017):
        row = probe(p)
        print(p, row['order'], round(row['seconds'], 3),
              [(r['original']['hypothesis_error_at_most_half'],
                r['shadow']['hypothesis_error_at_most_half']) for r in row['rows']], flush=True)
        path = args.output/f'spectral_{p}.json'
        path.write_text(json.dumps(row, separators=(',', ':'), sort_keys=True)+'\n')
        results.append({'p': p, 'file': path.name, 'sha256': sha256(path.read_bytes()).hexdigest()})
    files = ('intervals.py', 'source.py', 'run_spectral_probe.py', 'SPECTRAL_PREREGISTRATION.md')
    result = {'bits': BITS, 'scale': SCALE, 'preregistered_at': '42f9ed6d',
              'hashes': {f: sha256((HERE/f).read_bytes()).hexdigest() for f in files},
              'primes': results, 'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (args.output/'spectral_probe.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
