"""Exact-origin integration of authenticated signed phase observations.

The event sweep integrates every rotated partition with rational lengths;
complex values use the inherited outward 80-bit interval engine.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE.parent/'signed_covariance_round2'))
from lag_instrument import Box, Interval, SCALE, ZERO, ONE, phase, mean
from intervals import pi_box
from explicit_selector import select
from source import common_history, direct_modular_residue, principal_pair, matched_seed


def origin_average(local, p, M, a, b, *, zero=None, divide=None):
    """Exact event integral; works for Fraction values or interval Boxes."""
    if not local or len(local) != len(a) or len(a) != len(b):
        raise ValueError('equal nonempty arrays required')
    if type(p) is not int or p < 1 or type(M) is not int or M < 1:
        raise ValueError('positive integer grid and cell counts required')
    if any(type(r) is not int or not 0 <= r < p for r in local):
        raise ValueError('canonical grid residues required')
    zero = Q(0) if zero is None else zero
    divide = (lambda x, n: x/n) if divide is None else divide
    N = len(local)
    counts, sa, sb = [0]*M, [zero]*M, [zero]*M
    events = defaultdict(list)
    labels = []
    for j, r in enumerate(local):
        k, t = divmod(M*r, p)
        label = (k-(t == 0)) % M  # open interval immediately after theta=0
        labels.append(label)
        counts[label] += 1
        sa[label] = sa[label]+a[j]
        sb[label] = sb[label]+b[j]
        if t:
            events[t].append(j)

    def contribution(k):
        return divide(sa[k]*sb[k], N*counts[k]) if counts[k] else zero

    current = sum((contribution(k) for k in range(M)), zero)
    result, previous = zero, 0
    for t in sorted(events):
        result = result+divide(current*(t-previous), p) if isinstance(current, Q) else result+divide(current*Box(Interval.ratio(t-previous)), p)
        affected = {k for j in events[t] for k in (labels[j], (labels[j]-1) % M)}
        for k in affected:
            current = current-contribution(k)
        for j in events[t]:
            old, new = labels[j], (labels[j]-1) % M
            counts[old] -= 1
            sa[old], sb[old] = sa[old]-a[j], sb[old]-b[j]
            counts[new] += 1
            sa[new], sb[new] = sa[new]+a[j], sb[new]+b[j]
            labels[j] = new
        for k in affected:
            current = current+contribution(k)
        previous = t
    result = result+divide(current*(p-previous), p) if isinstance(current, Q) else result+divide(current*Box(Interval.ratio(p-previous)), p)
    return result


def circular_discrepancy(local, p):
    """Exact sup over circle half-open intervals, including endpoint limits."""
    N = len(local)
    low = high = cumulative = 0
    for r, count in sorted(Counter(local).items()):
        low = min(low, p*cumulative-r*N)
        cumulative += count
        high = max(high, p*cumulative-r*N)
    return Q(high-low, p*N)


def sinc_squared(h, M):
    if not h:
        return ONE
    sine = phase(h, 2*M).im
    t = pi_box()*Interval.ratio(abs(h), M)
    t2 = t.square()
    reciprocal = Interval(SCALE*SCALE//t2.hi, -((-SCALE*SCALE)//t2.lo))
    return sine.square()*reciprocal


def run(A):
    p, order = select(A)
    data = common_history(2*A-1, A)
    den, residues = data['denominator'], data['residues']
    for n in (A, A+A//2, 2*A-1):
        assert residues[n-A] == direct_modular_residue(n, den)
    pairs = [principal_pair(r, den, p) for r in residues]
    assert all(d == p for _, d in pairs)
    local = [r for r, _ in pairs]
    D = circular_discrepancy(local, p)
    primes = tuple(sorted({3, 5, 7, 11, p}))
    seed, _, _ = matched_seed(data, A, 32, Q(1, 2**20), primes)
    shift = seed.numerator*pow(16, A, seed.denominator) % seed.denominator
    shadow = []
    for r in residues:
        shadow.append(r*seed.denominator+shift*den)
        shift = 16*shift % seed.denominator
    shadow_den = den*seed.denominator
    assert all(principal_pair(r, shadow_den, p) == q for r, q in zip(shadow, pairs))
    rows = []
    for h in (1, 3):
        a = [phase(h*r, p) for r in local]
        families = [('original_zero', [phase(h*r, den) for r in residues]),
                    ('matched_wrong_seed', [phase(h*r, shadow_den) for r in shadow]),
                    ('synthetic_conjugate', [Box(ONE)]*A)]
        for family, z in families:
            b = [v*x.conjugate() for v, x in zip(z, a)]
            W = mean(z)
            marginal = mean(a)*mean(b)
            bound = pi_box()*Interval.ratio(2*abs(h)*D.numerator, D.denominator)
            for M in (4, 16, 64):
                F = origin_average(local, p, M, a, b, zero=Box(), divide=lambda x,n:x.divide(n))
                lam = sinc_squared(h, M)
                error = F-W*Box(lam)
                assert error.norm_squared().hi <= bound.square().lo
                removed = W-F
                rows.append({'family': family, 'h': h, 'M': M,
                             'lambda': lam.as_list(), 'W': W.as_dict(),
                             'origin_average': F.as_dict(),
                             'calibration_error': error.as_dict(),
                             'bound': bound.as_list(), 'certified_within_bound': True,
                             'removed': removed.as_dict(),
                             'normalized_removed': (removed*Box(Interval.ratio(M*M))).as_dict(),
                             'covariance': (W-marginal).as_dict(),
                             'averaged_coarse_covariance': (F-marginal).as_dict()})
    return {'A': A, 'p': p, 'order16': order, 'scale': SCALE,
            'circular_discrepancy': str(D), 'independent_modular_checks': 3,
            'source': {k: data[k] for k in ('last', 'unwrapped_sha256', 'carry_sha256')},
            'denominator_bits': den.bit_length(),
            'shadow': {'seed_numerator_hex': hex(seed.numerator),
                       'seed_denominator_hex': hex(seed.denominator),
                       'fixed_seed_across_epochs': False, 'literal_zero': False,
                       'matched_primes': list(primes)}, 'rows': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stage', choices=('development', 'holdout'), required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    epochs = {'development': (149,331), 'holdout': (673,1361,10009)}[args.stage]
    index = []
    for A in epochs:
        result = run(A)
        path = args.output/f'origin_{A}.json'
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
        index.append({'A': A, 'file': path.name, 'sha256':sha256(path.read_bytes()).hexdigest()})
        print(A, result['p'], len(result['rows']), 'full-origin interval calibrations pass', flush=True)
    (args.output/f'{args.stage}.json').write_text(json.dumps({
        'protocol_commit':'d08c0f17', 'stage':args.stage, 'epochs':index,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_normality':'OPEN', 'RH':'OPEN'}, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
