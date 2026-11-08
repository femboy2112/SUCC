"""Source-faithful finite quotient probe, with outward integer endpoints."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ROUND2 = HERE.parent / 'signed_covariance_round2'
sys.path.insert(0, str(ROUND2))
from lag_instrument import Box, Interval, SCALE, ZERO, ONE, phase, mean
from explicit_selector import select
from source import common_history, direct_modular_residue, principal_pair, matched_seed


def project(values, labels):
    if not values or len(values) != len(labels):
        raise ValueError('equal nonempty values and labels required')
    buckets = {}
    for value, label in zip(values, labels):
        buckets.setdefault(label, []).append(value)
    averages = {key: mean(bucket) for key, bucket in buckets.items()}
    return [averages[label] for label in labels]


def norm2(values):
    return sum((x.norm_squared() for x in values), ZERO).divide(len(values))


def overlap(a, b):
    return a.re.overlaps(b.re) and a.im.overlaps(b.im)


def nonnegative(x):
    """Intersect with a mathematically justified nonnegative domain."""
    if x.hi < 0:
        raise AssertionError('negative enclosure of a squared norm')
    return Interval(max(0, x.lo), x.hi)


def diagnostics(a, b, z, labels):
    """Requires exact unit a and exact z=ab, checked by the caller."""
    pa, pb, pz = (project(v, labels) for v in (a, b, z))
    da, db = ([x-y for x, y in zip(v, pv)] for v, pv in ((a, pa), (b, pb)))
    w = mean(z)
    coarse = mean(x*y for x, y in zip(pa, pb))
    residual = mean(x*y for x, y in zip(da, db))
    va, vb = nonnegative(norm2(da)), nonnegative(norm2(db))
    lifted = [x*y for x, y in zip(a, pb)]
    gap = nonnegative(norm2([x-y for x, y in zip(lifted, pz)]))
    model_error = nonnegative(norm2([x-y for x, y in zip(z, lifted)]))
    marginal = mean(a)*mean(b)
    assert overlap(w, coarse+residual)
    assert overlap(coarse, mean(lifted))
    assert model_error.overlaps(vb)
    assert residual.norm_squared().lo <= (va*vb).hi
    assert gap.lo <= va.hi
    return {'W': w.as_dict(), 'coarse_signal': coarse.as_dict(),
            'residual': residual.as_dict(), 'Va': va.as_list(), 'Vb': vb.as_list(),
            'demodulation_gap_squared': gap.as_list(), 'model_error_squared': model_error.as_list(),
            'total_covariance': (w-marginal).as_dict(),
            'coarse_covariance': (coarse-marginal).as_dict(),
            'marginal_product': marginal.as_dict(),
            'cauchy_bound_squared': (va*vb).as_list()}


def run(A):
    p, order = select(A)
    data = common_history(2*A-1, A)
    den, residues = data['denominator'], data['residues']
    for n in (A, A+A//2, 2*A-1):
        assert residues[n-A] == direct_modular_residue(n, den)
    local_pairs = [principal_pair(r, den, p) for r in residues]
    assert all(d == p for _, d in local_pairs)
    local = [r for r, _ in local_pairs]
    matched_primes = tuple(sorted({3, 5, 7, 11, p}))
    seed, _, _ = matched_seed(data, A, 32, Q(1, 2**20), matched_primes)
    shift = seed.numerator*pow(16, A, seed.denominator) % seed.denominator
    shadow = []
    for r in residues:
        shadow.append(r*seed.denominator+shift*den)
        shift = 16*shift % seed.denominator
    shadow_den = den*seed.denominator
    assert all(principal_pair(r, shadow_den, p) == pair
               for r, pair in zip(shadow, local_pairs))
    rows = []
    phase_checks = 0
    for h in (1, 3):
        a = [phase(h*r, p) for r in local]
        original = [phase(h*r, den) for r in residues]
        shadow_z = [phase(h*r, shadow_den) for r in shadow]
        for family, z in (('original_zero', original), ('matched_wrong_seed', shadow_z),
                          ('synthetic_conjugate', [Box(ONE)]*A)):
            b = [v*x.conjugate() for v, x in zip(z, a)]
            if family == 'original_zero':
                for j in (0, A//2, A-1):
                    q = h*(Q(residues[j], den)-Q(local[j], p))
                    assert overlap(b[j], phase(q.numerator, q.denominator))
                    phase_checks += 1
            for theta in (Q(0), Q(1, 32)):
                previous_vb = None
                for depth in range(5):
                    M = 16**depth
                    labels = [(M*((Q(r, p)+theta) % 1)).numerator //
                              (M*((Q(r, p)+theta) % 1)).denominator for r in local]
                    record = diagnostics(a, b, z, labels)
                    if previous_vb is not None:
                        assert record['Vb'][0] <= previous_vb[1]
                    previous_vb = record['Vb']
                    # The bound pi²<10 is rational; h fixed, all fibers genuine.
                    assert record['Va'][0]*M*M <= 10*h*h*SCALE
                    if M >= p:
                        # Uniform rational grid spacing 1/p implies exact measurability.
                        assert record['residual']['re'][0] <= 0 <= record['residual']['re'][1]
                        assert record['residual']['im'][0] <= 0 <= record['residual']['im'][1]
                        assert record['Va'][0] == 0
                    sizes = Counter(labels)
                    record.update({'family': family, 'h': h, 'depth': depth,
                                   'cells': M, 'cell_origin': str(theta),
                                   'occupied_cells': len(sizes),
                                   'occupancy_histogram': dict(sorted(Counter(sizes.values()).items())),
                                   'exact_local_measurability': M >= p})
                    rows.append(record)
    return {'A': A, 'p': p, 'order16': order, 'scale': SCALE,
            'source': {k: data[k] for k in ('last', 'unwrapped_sha256', 'carry_sha256')},
            'denominator_bits': den.bit_length(), 'independent_modular_checks': 3,
            'independent_phase_checks': phase_checks,
            'shadow': {'seed_numerator_hex': hex(seed.numerator),
                       'seed_denominator_hex': hex(seed.denominator),
                       'literal_zero': False, 'fixed_seed_across_epochs': False,
                       'matched_primes': list(matched_primes)}, 'rows': rows}


def summarize(output):
    summaries = []
    cases = 0
    epochs = 0
    for path in sorted(output.glob('quotient_*.json')):
        data = json.loads(path.read_text())
        cases += len(data['rows'])
        epochs += 1
        for row in data['rows']:
            if row['depth'] == 4 and row['cell_origin'] == '0':
                summaries.append({'A': data['A'], 'p': data['p'], 'h': row['h'],
                                  'family': row['family'],
                                  'W_abs_squared': row['W']['abs_squared'],
                                  'exact_local_measurability': row['exact_local_measurability'],
                                  'complement_variance': row['Vb']})
    (output/'SUMMARY.json').write_text(json.dumps({
        'scale': SCALE, 'cases': cases, 'epochs': epochs,
        'claims': 'Finite interval enclosures and consistency checks; no asymptotic decay estimate',
        'fine_rows': summaries}, indent=2, sort_keys=True)+'\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stage', choices=('development', 'holdout'), required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    index = []
    epochs = {'development': (137, 271), 'holdout': (547, 1093, 2203)}[args.stage]
    for A in epochs:
        row = run(A)
        path = args.output/f'quotient_{A}.json'
        path.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
        index.append({'A': A, 'file': path.name, 'sha256': sha256(path.read_bytes()).hexdigest()})
        print(A, row['p'], len(row['rows']), 'outward quotient cases pass', flush=True)
    (args.output/f'{args.stage}.json').write_text(json.dumps({
        'protocol_commit': '143fe29d', 'stage': args.stage, 'epochs': index,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_normality': 'OPEN', 'RH': 'OPEN'}, indent=2, sort_keys=True)+'\n')
    summarize(args.output)


if __name__ == '__main__':
    main()
