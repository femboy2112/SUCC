"""Stream authentic zero-source phases and certify a complete finite menu.

No pi digits enter the construction. Large rational states are streamed and
hashed instead of retaining quadratic-size lists of common-denominator states.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt, lcm
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT), str(HERE.parent/'covariance_forge'),
               str(HERE.parent/'signal_frontier/prime_resonance')]
from certified_fft import PrimeDFT, center, ceildiv
from intervals import Box, Interval, SCALE, phase, mean
from pr_resonance import select_prime, order16, source_xi, clock, eligible
from source import POLES, direct_modular_residue, principal_pair
from observational_succ.integer_bbp_carrier import forcing_pair


def digest_int(digest, n):
    raw = n.to_bytes(max(1, (n.bit_length()+7)//8), 'big')
    digest.update(len(raw).to_bytes(8, 'big') + raw)


def packed(box):
    return [box.re.lo, box.re.hi, box.im.lo, box.im.hi]


def unpacked(a):
    return Box(Interval(a[0], a[1]), Interval(a[2], a[3]))


def fraction_record(q):
    return {'numerator':q.numerator, 'denominator':q.denominator,
            'decimal_diagnostic':float(q)}


def stream_source(A):
    p = select_prime(A)
    if p is None:
        raise ValueError('no eligible prime for this finite selector')
    m = order16(p)
    L = (p-1)//4
    q = L//m
    n0, last = L+1, 2*L
    assert eligible(p) and L % m == 0 and p*p > 8*last
    xs = clock(p, source_xi(p))
    den = 1
    for n in range(1, last+1):
        for _, pole in POLES:
            den = lcm(den, 8*n-pole)
    unwrapped, oldfloor = 0, 0
    hd = sha256(b'BBP:4,-2,-1,-1;7,4,3,2;U0=0;unwrapped\0')
    cd = sha256(b'floor(U_n)-16floor(U_(n-1))\0')
    arrays = {h:[Box() for _ in range(m)] for h in (1,3)}
    sums = {h:Box() for h in arrays}
    checkpoints = {}
    for n in range(1, last+1):
        fn, fd = forcing_pair(n)
        assert den % fd == 0
        unwrapped = 16*unwrapped + fn*(den//fd)
        floor, rem = divmod(unwrapped, den)
        carry = floor-16*oldfloor
        oldfloor = floor
        digest_int(hd, unwrapped)
        cd.update(str(carry).encode()+b'\n')
        if n in {n0, n0+L//2, last}:
            checkpoints[n] = rem
        if n < n0:
            continue
        r = (n-n0) % m
        x, pe = principal_pair(rem, den, p)
        assert pe == p and x == xs[r]
        complement_numerator = rem-x*(den//p)
        for h in arrays:
            b = phase(h*complement_numerator, den)
            arrays[h][r] = arrays[h][r]+b
            sums[h] = sums[h]+phase(h*rem, den)
    independent = []
    for n, rem in checkpoints.items():
        assert rem == direct_modular_residue(n, den)
        independent.append(n)
    return {'A':A, 'p':p, 'm':m, 'q':q, 'L':L, 'n0':n0, 'last':last,
            'source_contract':'4,-2,-1,-1; poles7,4,3,2; literal U0=0',
            'unwrapped_sha256':hd.hexdigest(), 'carry_sha256':cd.hexdigest(),
            'denominator_bits':den.bit_length(), 'modular_checkpoints':independent,
            'fresh_after_20017':n0>20017, 'principal_parts_checked':L,
            'rows':[{'h':h, 'B':[packed(b.divide(q)) for b in arrays[h]],
                     'W':packed(sums[h].divide(L))} for h in arrays]}


def magnitude_upper(value, radius=0):
    return Q(isqrt(value[0]**2+value[1]**2)+1+radius, SCALE)


def box_magnitude_upper(value):
    v, r = center(value)
    return magnitude_upper(v, r)


def certify(data):
    p, m = data['p'], data['m']
    xs = clock(p, source_xi(p))
    engine = PrimeDFT(p)
    sqrtp_lower = Q(isqrt(p*SCALE*SCALE), SCALE)
    result = {k:v for k,v in data.items() if k != 'rows'}
    result['rows'] = []
    for row in data['rows']:
        h = row['h']
        B = [unpacked(v) for v in row['B']]
        W = unpacked(row['W'])
        Wcheck = mean(b*phase(h*x,p) for x,b in zip(xs,B))
        assert W.re.overlaps(Wcheck.re) and W.im.overlaps(Wcheck.im)
        energy = sum((b.norm_squared() for b in B), Interval(0,0)).divide(m)
        elow = Q(energy.lo,SCALE)
        wup = box_magnitude_upper(W)
        maxima = []
        for d in (1,2,3):
            scatter = [Box() for _ in range(p)]
            for x,b in zip(xs,B):
                y = pow(x,d,p)
                scatter[y] = scatter[y]+b
            centered = [center(v) for v in scatter]
            spectrum, radius = engine.transform([v for v,r in centered], max(r for v,r in centered))
            best = (Q(0), 0)
            for t, value in enumerate(spectrum):
                if (d == 1 and (t+h) % p == 0) or (d > 1 and t == 0):
                    continue
                upper = magnitude_upper(value,radius)/m
                if upper > best[0]:
                    best = (upper,t)
            weight_lower = min(Q(1), d*sqrtp_lower/m)
            sd = sha256()
            for x,y in spectrum:
                sd.update(f'{x},{y}\n'.encode())
            maxima.append({'degree':d,'max_correlation_upper':fraction_record(best[0]),
                           'maximizing_upper_bound_slope':best[1],
                           'weight_lower':fraction_record(weight_lower),
                           'ratio_upper':fraction_record(best[0]/weight_lower),
                           'spectrum_center_sha256':sd.hexdigest(),
                           'unnormalized_L1_radius_units':radius,
                           'normalized_L1_radius':fraction_record(Q(radius,m*SCALE)),
                           'all_slopes_evaluated':p})
            print('menu',data['A'],h,d,'max',float(best[0]),'radius',float(Q(radius,m*SCALE)),flush=True)
        rows = []
        for degree in (1,2,3):
            M = max(Q(v['ratio_upper']['numerator'],v['ratio_upper']['denominator']) for v in maxima[:degree])
            lower = max(Q(0),elow-wup*wup)/(max(Q(1),M)+wup)
            rows.append({'maximum_monomial_degree':degree,'M_upper':fraction_record(M),
                         'rho_plus_budget_lower':fraction_record(lower)})
        result['rows'].append({'h':h,'energy':energy.as_list(),'W':W.as_dict(),
                               'W_abs_upper':fraction_record(wup),'maxima':maxima,
                               'menu_certificates':rows})
    result['scope'] = 'Outward finite lower bounds for specified monomial menus, with arbitrary free resonance; no asymptotic assertion.'
    result['pi_normality'] = 'OPEN'
    result['RH'] = 'OPEN'
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--A', type=int, required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source-only',action='store_true')
    parser.add_argument('--reuse-source',type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    source = json.loads(args.reuse_source.read_text()) if args.reuse_source else stream_source(args.A)
    if source['A'] != args.A:
        raise ValueError('source selector mismatch')
    sp = args.output/f'source_{args.A}.json'
    sp.write_text(json.dumps(source,sort_keys=True,separators=(',',':'))+'\n')
    print('source',args.A,source['p'],source['m'],source['q'],flush=True)
    if not args.source_only:
        result = certify(source)
        result['source_receipt_sha256'] = sha256(sp.read_bytes()).hexdigest()
        result['code_sha256'] = {p.name:sha256(p.read_bytes()).hexdigest()
                                 for p in (Path(__file__),HERE/'certified_fft.py')}
        (args.output/f'budget_{args.A}.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
