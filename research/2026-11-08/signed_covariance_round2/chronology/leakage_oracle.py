"""Finite CH7 checks: exact source, rational geometry, certified phase boxes.

The phase enclosure engine is reused from covariance_forge; source reconstruction
and rational conditional-variance checks come from this front independently.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


o = load('round2_chronology_leakage_source', HERE/'oracle.py')
iv = load('round2_chronology_leakage_intervals',
          ROOT/'research/2026-11-08/covariance_forge/intervals.py')


def partition(points, digits):
    o.integer(digits, 1)
    if not points or any(type(x) is not Q or not 0 <= x < 1 for x in points):
        raise ValueError('nonempty exact circle sample required')
    cells = defaultdict(list)
    M = 16**digits
    for i, x in enumerate(points):
        cells[M*x.numerator//x.denominator].append(i)
    return dict(cells)


def rational_residual_variance(points, cells):
    n = len(points)
    result = Q(0)
    for indices in cells.values():
        center = sum((points[i] for i in indices), Q(0))/len(indices)
        result += sum(((points[i]-center)**2 for i in indices), Q(0))/n
    return result


def conditional_means(values, cells):
    out = [None]*len(values)
    for indices in cells.values():
        cell_mean = iv.mean(values[i] for i in indices)
        for i in indices:
            out[i] = cell_mean
    return out


def unit_phase_cell_energy(values, cells):
    """Requires certified unit-phase inputs; phase() is the sole caller source."""
    if all(len(indices) == 1 for indices in cells.values()):
        return iv.ONE  # exact unit modulus, not a rounded multiplication
    energy = iv.ZERO
    for indices in cells.values():
        square = (iv.ONE if len(indices) == 1 else
                  iv.mean(values[i] for i in indices).norm_squared())
        energy = energy + square*iv.Interval.ratio(len(indices), len(values))
    return energy


def q_upper(interval):
    return Q(interval.hi, iv.SCALE)


def q_lower(interval):
    return Q(interval.lo, iv.SCALE)


def run_checks():
    pi_upper = iv.pi_box().hi
    assert 7*pi_upper < 22*iv.SCALE
    assert pi_upper*pi_upper < 10*iv.SCALE*iv.SCALE
    counts = Counter()
    rows = []
    for p in o.PRIMES:
        L, np, m = (p-1)//4, (p+7)//8, o.order(p)
        states = o.source_history(L+m)
        clean_states = states[L+1:L+1+m]
        points = [o.principal(u, p) for u in clean_states]
        assert len(points) == m
        for d in range(1, 5):
            M = 16**d
            cells = partition(points, d)
            real_variance = rational_residual_variance(points, cells)
            assert 0 <= real_variance <= Q(1, 4*M*M)
            counts['exact_real_variance_checks'] += 1
            for h in (1, 2, 3, 5):
                a = [iv.phase(h*x.numerator, x.denominator) for x in points]
                complement = [u-x for u, x in zip(clean_states, points)]
                b = [iv.phase(h*y.numerator, y.denominator) for y in complement]
                pa, pb = conditional_means(a, cells), conditional_means(b, cells)
                energy = unit_phase_cell_energy(a, cells)
                residual = iv.ONE-energy
                data_bound = 40*h*h*real_variance
                grid_bound = Q(10*h*h, M*M)
                assert q_upper(residual) <= data_bound
                assert data_bound <= grid_bound
                counts['certified_phase_variance_bounds'] += 1
                mean_a2 = iv.mean(a).norm_squared()
                leakage = energy-mean_a2
                lower = 1-q_upper(mean_a2)-grid_bound
                assert q_lower(leakage) >= lower
                counts['certified_leakage_lower_bounds'] += 1
                raw = iv.mean(x*y for x, y in zip(a, b))
                coarse = iv.mean(x*y for x, y in zip(pa, pb))
                residual_product = iv.mean((x-px)*(y-py)
                                           for x, px, y, py in zip(a, pa, b, pb))
                reconstructed = coarse+residual_product
                assert raw.re.overlaps(reconstructed.re)
                assert raw.im.overlaps(reconstructed.im)
                signed_residual = raw-coarse
                assert q_upper(signed_residual.norm_squared()) <= Q(22*h, 7*M)**2
                counts['authentic_signed_projection_checks'] += 1
                # Hostile changed complement: b=conj(a). These are identities,
                # not a replacement of the authentic source above.
                maximal_covariance = iv.ONE-mean_a2
                projected_covariance = energy-mean_a2
                reconstructed_max = projected_covariance+residual
                assert maximal_covariance.overlaps(reconstructed_max)
                counts['conjugate_complement_controls'] += 1
                rows.append({'p': p, 'm': m, 'digits': d, 'h': h,
                             'word_cells': len(cells), 'real_residual_variance': str(real_variance),
                             'phase_residual_interval': residual.as_list(),
                             'phase_residual_data_upper': str(data_bound),
                             'phase_residual_grid_upper': str(grid_bound),
                             'leakage_interval': leakage.as_list(),
                             'leakage_proved_lower': str(lower),
                             'authentic_signed_residual': signed_residual.as_dict(),
                             'authentic_signed_residual_upper': str(Q(22*h, 7*M)),
                             'changed_complement_covariance': maximal_covariance.as_list()})
    return {'status': 'certified_finite_CH7_checks', 'source': 'four original poles, U0=0',
            'phase_engine': 'covariance_forge/intervals.py; reused calibrated instrument',
            'phase_scale': iv.SCALE, 'pi_squared_bound': 'pi^2<10',
            'pi_bound': 'pi<22/7', 'floating_point': False,
            'counts': dict(sorted(counts.items())), 'cases': rows,
            'total_counted_instances': sum(counts.values()),
            'pi_normality': 'OPEN', 'RH': 'OPEN'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = run_checks()
    payload = json.dumps(receipt, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
        print(json.dumps({'output': str(args.output), 'counts': receipt['counts'],
                          'total_counted_instances': receipt['total_counted_instances']}, sort_keys=True))
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
