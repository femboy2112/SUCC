"""Outward finite QCO4 replay on previously certified source boxes.

This reuses data and FFT machinery; it is not an independent source check,
fresh holdout, or all-epoch cancellation estimate.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BUDGET = HERE.parents[1]/'complement_budget'
sys.path.insert(0, str(BUDGET))
from source_budget import unpacked, magnitude_upper, box_magnitude_upper, fraction_record
from certified_fft import PrimeDFT, center
from intervals import Box, Interval, SCALE, phase
from pr_resonance import clock, source_xi
sys.path.insert(0, str(HERE))
from qco_oracle import cosets


def worst_l1(box, point):
    return (max(abs(box.re.lo-point[0]),abs(box.re.hi-point[0]))+
            max(abs(box.im.lo-point[1]),abs(box.im.hi-point[1])))


def lower_magnitude(v, radius):
    return F(max(0,isqrt(v[0]**2+v[1]**2)-radius),SCALE)


def run(A):
    source_path = BUDGET/'results'/f'source_{A}.json'
    raw = source_path.read_bytes()
    data = json.loads(raw)
    p,m = data['p'],data['m']
    xi = source_xi(p)
    xs = clock(p,xi)
    cycles = cosets(p)
    assert all(len(c)==m for c in cycles)
    beta_lo = min(F(1),F(isqrt(p*SCALE*SCALE),SCALE*m))
    beta_hi = min(F(1),F(isqrt(p*SCALE*SCALE)+1,SCALE*m))
    engine = PrimeDFT(p)
    periods = [sum((phase(-d*xi,p) for d in ds),Box()) for ds in cycles]
    rows = []
    for row in data['rows']:
        h = row['h']
        B = [unpacked(b) for b in row['B']]
        W = unpacked(row['W'])
        scattered = [Box() for _ in range(p)]
        for x,b in zip(xs,B):
            scattered[x] = b
        points = [center(b) for b in scattered]
        spectrum,rad = engine.transform([v for v,r in points],max(r for v,r in points))
        raw_r = spectrum[(-h)%p]
        direct_r = W*Box(Interval.ratio(m))
        assert worst_l1(direct_r,raw_r) <= rad
        r_upper = magnitude_upper(raw_r,rad)/p
        old_lower = beta_lo*sum(lower_magnitude(v,rad) for t,v in enumerate(spectrum) if (t+h)%p)/p
        old_upper = beta_hi*sum(magnitude_upper(v,rad) for t,v in enumerate(spectrum) if (t+h)%p)/p
        qcost = F(0)
        orbit_rows = []
        for ds,period in zip(cycles,periods):
            total = tuple(sum(spectrum[(d-h)%p][j] for d in ds) for j in (0,1))
            predicted_raw = W*period*Box(Interval.ratio(m))
            containment = worst_l1(predicted_raw,total)
            assert containment <= m*rad
            upper = magnitude_upper(total,m*rad)/p
            qcost += beta_hi*upper
            orbit_rows.append({'coset_representative':ds[0],
                               'coefficient_abs_upper':fraction_record(upper),
                               'direct_box_inside_fft_l1_ball':True,
                               'containment_margin_units':m*rad-containment})
        rows.append({'h':h,'W_upper':fraction_record(box_magnitude_upper(W)),
                     'retained_resonance_upper':fraction_record(r_upper),
                     'atomwise_nonresonant_cost_lower':fraction_record(old_lower),
                     'atomwise_nonresonant_cost_upper':fraction_record(old_upper),
                     'quotient_nonresonant_cost_upper':fraction_record(qcost),
                     'quotient_total_upper':fraction_record(qcost+r_upper),
                     'orbit_coefficients':orbit_rows,
                     'normalized_fft_error':fraction_record(F(rad,p*SCALE)),
                     'canonical_rank_one_warning':'All quotient coefficients are known multiples of W; this is not an independent decay premise.'})
    return {'A':A,'p':p,'m':m,'q':data['q'],
            'source_path':str(source_path.relative_to(HERE.parents[3])),
            'source_sha256':sha256(raw).hexdigest(),
            'source_unwrapped_sha256':data['unwrapped_sha256'],
            'source_carry_sha256':data['carry_sha256'],
            'data_scope':'Reused development data; no fresh holdout',
            'rows':rows}


if __name__=='__main__':
    result={'status':'CERTIFIED_FINITE_REPLAY',
            'theorem':'QCO4, canonical zero-extension rank-one quotient',
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'inputs':[run(A) for A in (1103,2203)],
            'normality':'OPEN','RH':'OPEN'}
    path=HERE/'SOURCE_QUOTIENT.json'
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'output':str(path),
                      'rows':[{'A':d['A'],'h':r['h'],
                               'atomwise_lower':float(F(r['atomwise_nonresonant_cost_lower']['numerator'],r['atomwise_nonresonant_cost_lower']['denominator'])),
                               'quotient_total_upper':float(F(r['quotient_total_upper']['numerator'],r['quotient_total_upper']['denominator']))}
                              for d in result['inputs'] for r in d['rows']]},indent=2))
