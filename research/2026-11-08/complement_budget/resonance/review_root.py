"""Independent direct-sum and reduced-state audit of the root budget probe.

Reads the root's exported folded values but reconstructs them with SelectedOrbit.
Direct coefficient checks bypass every FFT/chirp/convolution operation. The
phase-enclosure primitive is shared and that provenance is explicit.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

from resonance import ROOT, HERE, Box, Interval, SCALE, ZERO, phase, mean
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))
from certified_fft import PrimeDFT, center
from observational_succ.selected_orbit import SelectedOrbit


def unpack(v):
    return Box(Interval(v[0], v[1]), Interval(v[2], v[3]))


def ratio(record):
    return Q(record['numerator'], record['denominator'])


def run(epochs):
    counts = Counter()
    results = []
    dependencies = {str(Path(__file__).relative_to(ROOT)): sha256(Path(__file__).read_bytes()).hexdigest()}
    for path in (PARENT/'THEOREMS.md', PARENT/'certified_fft.py', PARENT/'source_budget.py',
                 ROOT/'observational_succ/selected_orbit.py',
                 ROOT/'observational_succ/duck_bbp.py',
                 ROOT/'research/2026-11-08/covariance_forge/intervals.py'):
        dependencies[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    for A in epochs:
        source_path = PARENT/'results'/f'source_{A}.json'
        budget_path = PARENT/'results'/f'budget_{A}.json'
        data, budget = json.loads(source_path.read_text()), json.loads(budget_path.read_text())
        for path in (source_path, budget_path):
            dependencies[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
        p, m, q, L, n0 = (data[k] for k in ('p', 'm', 'q', 'L', 'n0'))
        assert m*q == L and n0+L-1 == data['last']
        orbit = SelectedOrbit()
        # A separate denominator at every time, reduced after each recurrence;
        # root instead streams unwrapped states in one global denominator.
        direct_b = {row['h']: [Box() for _ in range(m)] for row in data['rows']}
        direct_w = {h: Box() for h in direct_b}
        xs = [None]*m
        for n in range(n0, n0+L):
            state = orbit.state(n)
            assert state.denominator % p == 0 and state.denominator % (p*p) != 0
            x = state.numerator*pow(state.denominator//p, -1, p)%p
            r = (n-n0)%m
            if xs[r] is None:
                xs[r] = x
            else:
                assert xs[r] == x
            complement = state - Q(x,p)
            for h in direct_b:
                z = phase(h*complement.numerator, complement.denominator)
                direct_b[h][r] = direct_b[h][r]+z
                direct_w[h] = direct_w[h]+phase(h*state.numerator,state.denominator)
            counts['independent_reduced_source_states'] += 1
        engine = PrimeDFT(p)
        row_results = []
        for row, certificate in zip(data['rows'], budget['rows']):
            h = row['h']
            assert h == certificate['h']
            B = [unpack(v) for v in row['B']]
            for r,b in enumerate(B):
                alt = direct_b[h][r].divide(q)
                assert b.re.overlaps(alt.re) and b.im.overlaps(alt.im)
                counts['independent_folded_values'] += 1
            W = unpack(row['W'])
            altw = direct_w[h].divide(L)
            assert W.re.overlaps(altw.re) and W.im.overlaps(altw.im)
            counts['independent_source_weyl_means'] += 1
            scalars = []
            for maximum in certificate['maxima']:
                d = maximum['degree']
                scatter = [Box() for _ in range(p)]
                for x,b in zip(xs,B):
                    scatter[pow(x,d,p)] = scatter[pow(x,d,p)]+b
                inputs = [center(b) for b in scatter]
                spectrum, radius = engine.transform([v for v,_ in inputs],max(r for _,r in inputs))
                digest = sha256()
                for x,y in spectrum:
                    digest.update(f'{x},{y}\n'.encode())
                assert digest.hexdigest() == maximum['spectrum_center_sha256']
                assert radius == maximum['unnormalized_L1_radius_units']
                counts['full_spectrum_replay_hashes'] += 1
                slopes = sorted({0, 1, 7, p//2, p-1, (-h)%p,
                                 maximum['maximizing_upper_bound_slope']})
                for t in slopes:
                    direct = mean(b*phase(-t*pow(x,d,p),p) for x,b in zip(xs,B))
                    cx,cy = spectrum[t]
                    # Strong containment: the entire independently computed
                    # direct rectangle fits inside the root FFT's L1 ball.
                    distance = max(abs(Q(cx,m)-direct.re.lo),abs(Q(cx,m)-direct.re.hi))
                    distance += max(abs(Q(cy,m)-direct.im.lo),abs(Q(cy,m)-direct.im.hi))
                    assert distance <= Q(radius,m)
                    counts['direct_interval_coefficient_containments'] += 1
                    scalars.append({'degree':d,'slope':t,'direct':direct.as_dict(),
                                    'L1_containment_ratio':str(distance/Q(radius,m))})
            # Recompute the final monotone rational bound without calling the
            # root's certifier or magnitude helper.
            energy = sum((b.norm_squared() for b in B),ZERO).divide(m)
            assert energy.as_list() == certificate['energy']
            E = Q(energy.lo,SCALE)
            Wu = ratio(certificate['W_abs_upper'])
            for model in certificate['menu_certificates']:
                degree = model['maximum_monomial_degree']
                Mu = max(ratio(x['ratio_upper']) for x in certificate['maxima'][:degree])
                bound = max(Q(0),E-Wu*Wu)/(max(Q(1),Mu)+Wu)
                assert bound == ratio(model['rho_plus_budget_lower'])
                counts['independent_rational_dual_bounds'] += 1
            row_results.append({'h':h,'coefficients':scalars})
        results.append({'A':A,'p':p,'m':m,'q':q,'rows':row_results})
    return {'counts':dict(counts),'epochs':results,'dependencies':dependencies,
            'scope':'Independent reduced-state representation and direct O(m) coefficient sums; shared canonical forcing and outward phase primitive; mathematical proof separately reviewed.',
            'unresolved_findings':[], 'pi_normality':'OPEN','RH':'OPEN'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', nargs='+',type=int,default=[1103])
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.epochs)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result['counts'],sort_keys=True))
