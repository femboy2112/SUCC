"""Finite checks for the paper RE1-4; computations do not prove normality."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT), str(HERE.parent/'covariance_forge'),
               str(HERE.parent/'complement_budget')]
from intervals import Interval, SCALE, phase
from source_budget import unpacked


def rec(q):
    q = Q(q)
    return {'numerator': q.numerator, 'denominator': q.denominator,
            'decimal_diagnostic': float(q)}


def critical_check(b):
    if type(b) is not int or b < 2 or b % 2:
        raise ValueError('even integer multiplier required')
    c = phase(1, 2*(b+1)).re
    angles = {Q(k, b+1) for k in range(b+1)}
    angles.update(Q(2*k+1, 2*(b-1)) for k in range(b-1))
    equality = {Q(b, 2*(b+1)), Q(b+2, 2*(b+1))}
    exact_minima = []
    for t in sorted(angles):
        p = phase(t.numerator, t.denominator).re
        pb = phase(b*t.numerator, t.denominator).re
        gap = p*Interval.ratio(b)+pb+c*Interval.ratio(b+1)
        if t in equality:
            assert gap.lo <= 0 <= gap.hi
            exact_minima.append(str(t))
        else:
            assert gap.lo > 0, (b, t, gap)
    assert len(exact_minima) == 2
    return {'b': b, 'stationary_points': len(angles),
            'exact_minimizers_turns': exact_minima}


def debruijn(base, order):
    """Euler circuit implementation; its output is checked independently."""
    if base < 2 or order < 1:
        raise ValueError('base>=2, order>=1')
    nodes = base**(order-1)
    used = [0]*nodes
    vertices, edges, output = [0], [], []
    while vertices:
        v = vertices[-1]
        if used[v] < base:
            digit = used[v]
            used[v] += 1
            vertices.append((base*v+digit) % nodes)
            edges.append(digit)
        else:
            vertices.pop()
            if edges:
                output.append(edges.pop())
    result = tuple(reversed(output))
    assert len(result) == base**order
    return result


def normal_control():
    cycles, word_checks, matching_digits = [], 0, 0
    for base, orders in ((2, range(1, 7)), (4, range(1, 5)), (16, range(1, 4))):
        for k in orders:
            digits = debruijn(base, k)
            d = len(digits)
            for j in range(1, k+1):
                counts = Counter(tuple(digits[(i+s) % d] for s in range(j))
                                 for i in range(d))
                assert len(counts) == base**j
                assert set(counts.values()) == {base**(k-j)}
                word_checks += len(counts)
            if k >= 2:
                m, previous = base**(k*k), 4*base**((k-1)**2)
                assert 2*m >= previous and m % d == 0
                for r in sorted({0, 1, m//2, m-2, m-1}):
                    n = 2*m+r
                    for offset in range(1, min(m-r, 257)+1):
                        left = digits[(n+offset-1-previous) % d]
                        right = digits[(n+m+offset-1-previous) % d]
                        assert left == right
                        matching_digits += 1
            cycles.append({'base': base, 'order': k, 'length': d,
                           'word_sha256': sha256(bytes(digits)).hexdigest()})
    # A complete finite prefix tests joins and partial stages separately.
    base, N = 2, 100000
    ds = []
    k, start = 1, 0
    while len(ds) < N:
        c = debruijn(base, k)
        end = min(N, 4*base**(k*k))
        ds.extend(c[i % len(c)] for i in range(end-start))
        start, k = end, k+1
    errors = []
    for j in (1, 2, 3):
        counts = Counter(tuple(ds[i:i+j]) for i in range(N-j+1))
        error = max(abs(Q(v)-Q(N-j+1, base**j)) for v in counts.values())
        # Conservative elementary sum of per-stage period and join errors.
        bound = 2*sum(base**i+j for i in range(1, k))+4*base**((j-1)**2)
        assert error <= bound
        errors.append({'word_length': j, 'max_count_error': rec(error),
                       'declared_bound': bound})
    return {'cycles': cycles, 'exact_word_counts_checked': word_checks,
            'matching_digit_checks': matching_digits,
            'finite_prefix_length': N, 'finite_prefix_errors': errors,
            'scope': 'finite construction checks; infinite proof is RE4'}


def source_energy():
    c = phase(1, 34).re
    s2low, s2high = Q(SCALE-c.hi, 2*SCALE), Q(SCALE-c.lo, 2*SCALE)
    rows = []
    for A in (1103, 2203, 5501, 22003):
        path = HERE.parent/f'complement_budget/results/source_{A}.json'
        data = json.loads(path.read_text())
        m, n0 = data['m'], data['n0']
        assert data['q'] == 2 and data['L'] == 2*m
        for row in data['rows']:
            total = sum((unpacked(v).norm_squared() for v in row['B']), Interval(0,0)).divide(m)
            h = row['h']
            forcing_cost = Q(330*abs(h), 119*(8*n0+1)**2)
            lower = Q(m-1, m)*(s2low-forcing_cost)
            assert Q(total.lo, SCALE) >= lower > Q(1, 300)
            rows.append({'A': A, 'p': data['p'], 'm': m, 'h': h,
                         'energy_interval': [rec(Q(total.lo,SCALE)), rec(Q(total.hi,SCALE))],
                         'RE2_lower': rec(lower), 'source_sha256': sha256(path.read_bytes()).hexdigest()})
    return {'sharp_constant_interval': [rec(s2low), rec(s2high)],
            'source_data_status': 'reused prior authentic source boxes, not fresh holdout', 'rows': rows}


def run():
    critical = [critical_check(b) for b in (2, 4, 6, 16, 32)]
    c = phase(1,34).re
    grid = 0
    for numerator in range(4093):
        gap = phase(numerator,4093).re*Interval.ratio(16)+phase(16*numerator,4093).re+c*Interval.ratio(17)
        assert gap.lo > 0  # equality angles have denominator17, absent from grid.
        grid += 1
    for b in (3, 5, 15, 17):
        cb = phase(1, 2*(b+1)).re
        assert -(b+1)*SCALE < -(b+1)*cb.hi
    return {'critical_points': critical, 'strict_interval_grid_points': grid,
            'odd_base_counterexamples': [3,5,15,17], 'normal_control': normal_control(),
            'source_energy': source_energy(), 'pi_normality': 'OPEN', 'RH': 'OPEN'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'critical_points':sum(x['stationary_points'] for x in result['critical_points']),
                      'grid':result['strict_interval_grid_points'],
                      'source_cases':len(result['source_energy']['rows']),
                      'word_counts':result['normal_control']['exact_word_counts_checked']}))
