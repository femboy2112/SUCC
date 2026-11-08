"""Frozen causal carry tables and rigorous folded-error certificates.

The carry table is fitted only on explicitly designated old times. The later
source evaluation cannot update it. QCO1 coefficients expand the prediction,
never the observed held-out complement. No masked Weil estimate is assumed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import json
from math import isqrt, lcm
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESEARCH = ROOT / 'research/2026-11-08'
sys.path[:0] = [str(ROOT), str(RESEARCH / 'covariance_forge'),
               str(RESEARCH / 'signal_frontier/prime_resonance'),
               str(RESEARCH / 'complement_budget')]
from intervals import Box, Interval, SCALE, phase, mean
from pr_resonance import select_prime, order16, source_xi, clock
from source import POLES, direct_modular_residue
from source_budget import packed, unpacked, digest_int
from observational_succ.integer_bbp_carrier import forcing_pair

TABLE_BITS = 24
TABLE_SCALE = 1 << TABLE_BITS
HS = (1, 3)
MENUS = ('zero', 'one', 'two')


def fraction_record(value):
    value = Q(value)
    return {'numerator': value.numerator, 'denominator': value.denominator,
            'decimal_diagnostic': float(value)}


def magnitude_bounds(box):
    sq = box.norm_squared()
    low = isqrt(max(0, sq.lo) * SCALE)
    upper2 = max(0, sq.hi) * SCALE
    high = isqrt(upper2)
    if high * high < upper2:
        high += 1
    return Q(low, SCALE), Q(high, SCALE)


def sqrt_bounds(value):
    value = Q(value)
    if value < 0:
        raise ValueError('nonnegative rational required')
    low = isqrt(value.numerator * SCALE * SCALE // value.denominator)
    high = low if low * low * value.denominator == value.numerator * SCALE * SCALE else low + 1
    return Q(low, SCALE), Q(high, SCALE)


def feature(previous, current, menu):
    if menu == 'one':
        return (current,)
    if menu == 'two':
        return previous, current
    if menu == 'zero':
        return ()
    raise ValueError('declared carry menu required')


def key_text(key):
    return ','.join(map(str, key))


def toward_zero(numerator, denominator):
    return numerator // denominator if numerator >= 0 else -((-numerator) // denominator)


def fitted_center(box):
    """Declare a dyadic predictor, then contract coordinates to the unit disk."""
    re = toward_zero((box.re.lo + box.re.hi) * TABLE_SCALE, 2 * SCALE)
    im = toward_zero((box.im.lo + box.im.hi) * TABLE_SCALE, 2 * SCALE)
    contractions = 0
    while re * re + im * im > TABLE_SCALE * TABLE_SCALE:
        re -= (re > 0) - (re < 0)
        im -= (im > 0) - (im < 0)
        contractions += 1
    return [re, im], contractions


def table_predict(table, h, menu, previous, current):
    if menu == 'zero':
        return (0, 0), False
    key = key_text(feature(previous, current, menu))
    row = table['tables'][str(h)][menu]
    entry = row.get(key)
    return (tuple(entry['center']) if entry else (0, 0)), entry is None


def clock_spec(A):
    p = select_prime(A)
    if p is None:
        raise ValueError('selector supplies no eligible prime')
    m, L = order16(p), (p - 1) // 4
    assert L % m == 0 and p * p > 16 * L
    return {'A': A, 'p': p, 'm': m, 'q': L // m,
            'L': L, 'n0': L + 1, 'last': 2 * L}


def denominator_for(last):
    denominator = 1
    for n in range(1, last + 1):
        for _, pole in POLES:
            denominator = lcm(denominator, 8*n-pole)
    return denominator


def authentic_stream(last, checkpoint_times=(), progress=False):
    """Exact common-denominator recurrence, retaining unwrapped/carry hashes.

    Generator results contain immutable source integers. The summary follows
    all state rows. No pi input is used. Independent modular checks use a
    separate finite power-sum algorithm from the inherited source tool.
    """
    denominator = denominator_for(last)
    unwrapped = oldfloor = oldrem = previous_carry = 0
    hd = sha256(b'BBP:4,-2,-1,-1;7,4,3,2;U0=0;unwrapped\0')
    cd = sha256(b'floor(U_n)-16floor(U_(n-1))\0')
    carries = []
    checkpoints = {}
    for n in range(1, last + 1):
        fn, fd = forcing_pair(n)
        assert denominator % fd == 0
        forcing = fn * (denominator // fd)
        unwrapped = 16 * unwrapped + forcing
        carry, rem = divmod(16 * oldrem + forcing, denominator)
        integer = 16 * oldfloor + carry
        # This exact identity simultaneously checks full state and carry.
        if n in checkpoint_times or n == last:
            assert unwrapped == integer * denominator + rem
            checkpoints[n] = rem
        digest_int(hd, unwrapped)
        cd.update(str(carry).encode() + b'\n')
        carries.append(carry)
        yield {'n': n, 'rem': rem, 'denominator': denominator,
               'previous_carry': previous_carry, 'carry': carry}
        oldrem, oldfloor, previous_carry = rem, integer, carry
        if progress and n % 10000 == 0:
            print('source_time', n, flush=True)
    independent = []
    for n, rem in checkpoints.items():
        assert rem == direct_modular_residue(n, denominator)
        independent.append(n)
    yield {'summary': {'last': last, 'denominator_bits': denominator.bit_length(),
                       'unwrapped_sha256': hd.hexdigest(), 'carry_sha256': cd.hexdigest(),
                       'modular_checkpoints': independent, 'carries': carries,
                       'source_contract': '4,-2,-1,-1; poles7,4,3,2; literal U0=0'}}


def fit(A_values=(1103, 2203)):
    specs = [clock_spec(A) for A in A_values]
    starts = min(s['n0'] for s in specs)
    last = max(s['last'] for s in specs)
    selected = lambda n: any(s['n0'] <= n <= s['last'] for s in specs)
    sums = {h: {menu: defaultdict(Box) for menu in ('one', 'two')} for h in HS}
    counts = {menu: Counter() for menu in ('one', 'two')}
    total = 0
    for row in authentic_stream(last, (starts, last)):
        if 'summary' in row:
            summary = row['summary']
            break
        if not selected(row['n']):
            continue
        total += 1
        keys = {menu: key_text(feature(row['previous_carry'], row['carry'], menu))
                for menu in counts}
        for menu, key in keys.items():
            counts[menu][key] += 1
        for h in HS:
            z = phase(h * row['rem'], row['denominator'])
            for menu, key in keys.items():
                sums[h][menu][key] = sums[h][menu][key] + z
    tables = {}
    contractions = 0
    for h in HS:
        tables[str(h)] = {}
        for menu in counts:
            tables[str(h)][menu] = {}
            for key in sorted(counts[menu]):
                count = counts[menu][key]
                average = sums[h][menu][key].divide(count)
                center, clipped = fitted_center(average)
                contractions += clipped
                tables[str(h)][menu][key] = {'count': count, 'center': center,
                                            'training_mean_box': packed(average)}
    return {'schema': 'chronology-carry-table-v1', 'table_bits': TABLE_BITS,
            'frequencies': list(HS), 'menus': list(MENUS), 'training_clocks': specs,
            'training_times_union_count': total, 'training_rule': 'union; each source time once',
            'training_source': summary, 'coordinate_contractions': contractions,
            'unseen_feature_prediction': [0, 0], 'tables': tables}


def quotient_factor_bounds(p, m):
    """No held-out B enters the a-priori canonical-prediction cost."""
    if p <= 2 or m <= 0 or (p - 1) % m:
        raise ValueError('odd prime clock parameters required')
    _, sqrtp = sqrt_bounds(p)
    beta = min(Q(1), sqrtp / m)
    d = (p - 1) // m
    _, period_l1 = sqrt_bounds(d * (p - m))
    cost_factor = Q(m, p) * beta * period_l1
    return {'resonance_factor': fraction_record(Q(m, p)),
            'nonresonant_factor_upper': fraction_record(cost_factor),
            'total_factor_upper': fraction_record(Q(m, p) + cost_factor),
            'multiplicative_cosets': d,
            'period_square_sum_exact': p - m}


def certify_fold(B, prediction_sums, p, m, q, h):
    """Certify fixed folded predictions, with all residual and resonance costs."""
    if m != order16(p) or type(q) is not int or q <= 0 or type(h) is not int:
        raise ValueError('actual clock order, positive integer fold, and integer h required')
    if len(B) != m or len(prediction_sums) != m:
        raise ValueError('complete clock arrays required')
    xs = clock(p, source_xi(p))
    model = []
    predicted = []
    for x, value in zip(xs, prediction_sums):
        g = Box(Interval.ratio(value[0], q * TABLE_SCALE),
                Interval.ratio(value[1], q * TABLE_SCALE))
        predicted.append(g)
        model.append(phase(-h*x, p) * g)
    low = high = Q(0)
    for b, v in zip(B, model):
        lo, hi = magnitude_bounds(b - v)
        low += lo
        high += hi
    low, high = low / m, high / m
    gp = mean(predicted)
    gp_low, gp_high = magnitude_bounds(gp)
    factors = quotient_factor_bounds(p, m)
    rf = Q(m, p)
    cf = Q(**{k: factors['nonresonant_factor_upper'][k] for k in ('numerator','denominator')})
    W = mean(phase(h*x, p) * b for x, b in zip(xs, B))
    wlo, whi = magnitude_bounds(W)
    direct = high + gp_high
    quotient = high + (rf + cf) * gp_high
    assert wlo <= direct, 'independent W enclosure must overlap the proved upper bound'
    return {'h': h, 'rho_lower': fraction_record(low), 'rho_upper': fraction_record(high),
            'predicted_signed_mean': packed(gp),
            'predicted_signed_abs_lower': fraction_record(gp_low),
            'predicted_signed_abs_upper': fraction_record(gp_high),
            'retained_resonance_abs_upper': fraction_record(rf * gp_high),
            'signed_orbit_cost_upper': fraction_record(cf * gp_high),
            'direct_certificate_upper': fraction_record(direct),
            'QCO1_certificate_upper': fraction_record(quotient),
            'W_abs_lower': fraction_record(wlo), 'W_abs_upper': fraction_record(whi),
            'W_box': packed(W), 'factors': factors,
            'prediction_sums_sha256': sha256(json.dumps(prediction_sums, separators=(',', ':')).encode()).hexdigest()}


def evaluate_source(table, A, progress=False):
    if table['table_bits'] != TABLE_BITS or table['frequencies'] != list(HS):
        raise ValueError('preregistered table contract mismatch')
    spec = clock_spec(A)
    p, m, q = spec['p'], spec['m'], spec['q']
    xs = clock(p, source_xi(p))
    arrays = {h: [Box() for _ in range(m)] for h in HS}
    preds = {h: {menu: [[0, 0] for _ in range(m)] for menu in MENUS} for h in HS}
    unseen = {menu: 0 for menu in MENUS}
    feature_counts = {menu: Counter() for menu in ('one', 'two')}
    direct = {h: Box() for h in HS}
    per_time = {h: [] for h in HS}
    summary = None
    checked = 0
    principal_multiplier = None
    for row in authentic_stream(spec['last'], (spec['n0'], spec['last']), progress):
        if 'summary' in row:
            summary = row['summary']
            break
        if row['n'] < spec['n0']:
            continue
        den, rem = row['denominator'], row['rem']
        if principal_multiplier is None:
            assert den % p == 0 and (den // p) % p != 0
            principal_multiplier = pow(den // p, -1, p)
        r = (row['n'] - spec['n0']) % m
        x = rem * principal_multiplier % p
        assert x == xs[r]
        checked += 1
        for menu in feature_counts:
            key = key_text(feature(row['previous_carry'], row['carry'], menu))
            feature_counts[menu][key] += 1
        cn = rem - x * (den // p)
        for h in HS:
            arrays[h][r] = arrays[h][r] + phase(h*cn, den)
            observed = phase(h*rem, den)
            direct[h] = direct[h] + observed
            per_time[h].append(packed(observed))
            for menu in MENUS:
                prediction, missed = table_predict(table, h, menu, row['previous_carry'], row['carry'])
                if h == HS[0]:
                    unseen[menu] += missed
                preds[h][menu][r][0] += prediction[0]
                preds[h][menu][r][1] += prediction[1]
    out = {**spec, 'source': summary, 'principal_parts_checked': checked,
           'feature_counts': {menu: dict(sorted(v.items())) for menu,v in feature_counts.items()},
           'unseen_feature_counts': unseen, 'rows': [],
           'per_time_phases': [{'h':h, 'start':spec['n0'], 'boxes':per_time[h]} for h in HS]}
    for h in HS:
        B = [b.divide(q) for b in arrays[h]]
        Wdirect = direct[h].divide(spec['L'])
        for menu in MENUS:
            cert = certify_fold(B, preds[h][menu], p, m, q, h)
            cert['menu'] = menu
            wc = unpacked(cert['W_box'])
            assert wc.re.overlaps(Wdirect.re) and wc.im.overlaps(Wdirect.im)
            out['rows'].append(cert)
        out.setdefault('folded_source', []).append({'h': h, 'B': [packed(b) for b in B],
                                                   'W_direct': packed(Wdirect)})
    out['frozen_table_sha256'] = sha256(json.dumps(table, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    out['scope'] = 'Finite frozen carry-table prediction and charged certificate; no asymptotic source estimate.'
    out['pi_normality'] = out['RH'] = 'OPEN'
    return out


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if path.suffix == '.gz':
        path.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
    else:
        path.write_bytes(raw)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('fit', 'evaluate'))
    parser.add_argument('--table', type=Path, required=True)
    parser.add_argument('--A', type=int)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.mode == 'fit':
        data = fit()
        dump(args.table, data)
        print('fitted', data['training_times_union_count'], data['coordinate_contractions'], flush=True)
    else:
        if args.A is None or args.output is None:
            parser.error('evaluate requires --A and --output')
        data = evaluate_source(json.loads(args.table.read_text()), args.A, True)
        data['code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        data['frozen_table_file_sha256'] = sha256(args.table.read_bytes()).hexdigest()
        dump(args.output, data)
        for row in data['rows']:
            print('certificate', row['h'], row['menu'],
                  row['rho_lower']['decimal_diagnostic'], row['rho_upper']['decimal_diagnostic'],
                  row['direct_certificate_upper']['decimal_diagnostic'],
                  row['QCO1_certificate_upper']['decimal_diagnostic'], flush=True)


if __name__ == '__main__':
    main()
