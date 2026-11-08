"""Outward signed residual windows and exact frozen carry Poisson accounting.

The window identity is inherited from signed_covariance_round2. No iid law is
imposed on the selected carry trajectory. All learned coefficients are frozen.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import itertools
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE/'model'), str(HERE.parent/'signed_covariance_round2')]
import carry_model as cm
from lag_instrument import sliding_energy

H_VALUES = (32, 128, 512)


def qrecord(x):
    return cm.fraction_record(x)


def cadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def csub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def cscale(a, q):
    return (a[0]*q, a[1]*q)


def csum(values):
    return tuple(map(sum, zip(*values)))


def cbox(v):
    return cm.Box(*(cm.Interval.ratio(x.numerator, x.denominator) for x in v))


def crecord(v):
    lo, hi = cm.magnitude_bounds(cbox(v))
    return {'re':qrecord(v[0]), 'im':qrecord(v[1]),
            'abs_lower':qrecord(lo), 'abs_upper':qrecord(hi)}


def table_value(table, h, menu, word):
    previous, current = (0, word[0]) if menu == 'one' else word
    value, _ = cm.table_predict(table, h, menu, previous, current)
    return tuple(Q(v, cm.TABLE_SCALE) for v in value)


def poisson_audit(table, h, menu, states):
    """Last term stays explicit, so no future source carry is requested."""
    if menu not in ('one','two') or len(states) < 2:
        raise ValueError('carry depth one/two and at least two states required')
    k = 1 if menu == 'one' else 2
    regular = list(itertools.product(range(16), repeat=k))
    g = {w:table_value(table,h,menu,w) for w in regular}
    mu = cscale(csum(g.values()), Q(1,len(g)))
    def P(values):
        return {w:cscale(csum(values[w[1:]+(d,)] for d in range(16)),Q(1,16))
                for w in regular}
    z = (Q(0),Q(0))
    centered = {w:csub(g[w],mu) for w in regular}
    psi = dict.fromkeys(regular,z)
    power = centered
    for _ in range(k):
        psi = {w:cadd(psi[w],power[w]) for w in regular}
        power = P(power)
    assert all(v==z for v in power.values())
    Ppsi = P(psi)
    assert all(csub(psi[w],Ppsi[w])==centered[w] for w in regular)
    N = len(states)
    innovation = z
    defect = z
    exceptional = 0
    values = [table_value(table,h,menu,w) for w in states]
    # The original literal words and predictions remain intact. Only the
    # declared reference operator uses digit residues; pay their difference.
    residue_states=[tuple(d % 16 for d in w) for w in states]
    for i in range(N-1):
        w, v = residue_states[i],residue_states[i+1]
        pw, ppw = psi[w],Ppsi[w]
        innovation = cadd(innovation,csub(psi[v],ppw))
        defect = cadd(defect,csub(values[i],g[w]))
        exceptional += states[i] != w
    boundary = csub(psi[residue_states[0]],psi[residue_states[-1]])
    pieces = [cscale(mu,Q(N-1,N)),cscale(boundary,Q(1,N)),
              cscale(innovation,Q(1,N)),cscale(defect,Q(1,N)),
              cscale(values[-1],Q(1,N))]
    target = cscale(csum(values),Q(1,N))
    assert csum(pieces)==target
    return {'uniform_table_mean':crecord(mu), 'pieces':dict(zip(
        ('interior_mean','boundary','signed_innovation','exception_defect','last_prediction'),
        map(crecord,pieces))), 'mean_prediction':crecord(target),
        'exceptional_interior_states':exceptional,
        'poisson_identity_exact':True, 'finite_sum_identity_exact':True,
        'scope':'Reference P is uniform append; actual transitions are measured, not assumed iid.'}


def window_receipts(values, apertures=H_VALUES):
    N = len(values)
    diagonal = sum((v.norm_squared() for v in values),cm.Interval(0,0)).divide(N)
    mean = cm.mean(values)
    rows = []
    for H in apertures:
        unscaled = sliding_energy(values,H)
        factor = cm.Interval.ratio(N+H-1,N)
        V = unscaled*factor
        dl = diagonal.divide(H)*factor
        signed = V-dl
        lower, upper = cm.sqrt_bounds(Q(max(0,V.hi),cm.SCALE))
        # Only upper is used in the certificate; V may have a negative lower
        # endpoint from interval dependency, despite its exact Gram positivity.
        rows.append({'H':H, 'V_interval':V.as_list(),
                     'diagonal_interval':dl.as_list(),
                     'signed_cross_term_interval':signed.as_list(),
                     'sqrt_V_upper':qrecord(upper)})
    return {'length':N,'mean':cm.packed(mean),'diagonal':diagonal.as_list(),
            'rows':rows}


def run(table, source):
    n0,last,N = source['n0'],source['last'],source['L']
    carries = source['source']['carries']
    assert len(carries)==last and last-n0+1==N
    assert source['frozen_table_sha256']==sha256(json.dumps(table,sort_keys=True,
        separators=(',',':')).encode()).hexdigest()
    records=[]
    for phase_row in source['per_time_phases']:
        h=phase_row['h']
        f=[cm.unpacked(v) for v in phase_row['boxes']]
        assert len(f)==N and phase_row['start']==n0
        for menu in cm.MENUS:
            g=[]
            states=[]
            for n in range(n0,last+1):
                previous,current=carries[n-2],carries[n-1]
                word=cm.feature(previous,current,menu)
                states.append(word)
                value,_=cm.table_predict(table,h,menu,previous,current)
                g.append(cm.Box(*(cm.Interval.ratio(v,cm.TABLE_SCALE) for v in value)))
            residual=[x-y for x,y in zip(f,g)]
            windows=window_receipts(residual)
            model_mean=cm.mean(g)
            mean_lower,mean_upper=cm.magnitude_bounds(model_mean)
            for row in windows['rows']:
                radius=Q(row['sqrt_V_upper']['numerator'],row['sqrt_V_upper']['denominator'])
                total=mean_upper+radius
                row['certificate_upper']=qrecord(total)
                # Refute threshold only when the rigorous lower bound on
                # THIS expression exceeds it; failure of an upper bound is
                # not a lower bound on either expression or Weyl modulus.
                vlo=max(0,row['V_interval'][0])
                vlow,_=cm.sqrt_bounds(Q(vlo,cm.SCALE))
                row['certificate_lower']=qrecord(mean_lower+vlow)
                row['threshold_one_quarter']=('PASS_FINITE' if total<=Q(1,4) else
                    'REFUTED_CERTIFICATE' if mean_lower+vlow>Q(1,4) else 'INCONCLUSIVE')
            record={'h':h,'menu':menu,'windows':windows,
                    'model_mean':cm.packed(model_mean),
                    'poisson':poisson_audit(table,h,menu,states) if menu!='zero' else None}
            records.append(record)
            print('signed',h,menu,[(r['H'],r['certificate_upper']['decimal_diagnostic'])
                                  for r in windows['rows']],flush=True)
    return {'source_clock':{k:source[k] for k in ('A','p','m','q','L','n0','last')},
            'rows':records,'interval_scale':cm.SCALE,
            'scope':'Finite signed residual certificate; actual all-epoch source estimates OPEN.',
            'pi_normality':'OPEN','RH':'OPEN'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',type=Path,required=True)
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    raw=args.source.read_bytes()
    source=json.loads(gzip.decompress(raw) if args.source.suffix=='.gz' else raw)
    result=run(json.loads(args.table.read_text()),source)
    result['source_file_sha256']=sha256(raw).hexdigest()
    result['table_file_sha256']=sha256(args.table.read_bytes()).hexdigest()
    result['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':main()
