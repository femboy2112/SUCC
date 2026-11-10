"""Preregistered N=40960 zero-source BBP holdout (protocol committed before access).

For each digit: rational four-pole source; rational positive BBP tail enclosure;
no external pi digit strings, float decisions, fitted thresholds, or changes to U0.
"""
from __future__ import annotations
import argparse, hashlib, json, random, sys, time
from collections import Counter
from fractions import Fraction
from pathlib import Path

from observational_succ.lambert_entropy_forge import (
    lambert_clock, entropy_diagnostics, entropy_amplification_bound,
    exact_overlap_returns, complete_coverage_reference, EULER_GAMMA,
)

OUT=Path(__file__).resolve().parent
REF_DIGITS=OUT.parents[0]/'zero_origin_spectral_flux/CERTIFIED_HEX_16384.txt'
CHECKPOINTS=(16384,20480,32768,36864,40960)
KMAX=4


def source(n:int)->Fraction:
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def canonical_source(n:int)->Fraction:
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def certified_digits(count:int)->tuple[str,int,int]:
    """Exact *bulk* rational BBP enclosure, equivalent to the authentic source.

    A prior per-step Fraction replay was abandoned after n=12,288 due to
    O(n)-size denominators and superlinear runtime; no digit-statistical holdout
    was inspected before replacing it. The frozen horizon and observables stay.
    The independent first16,384 per-step certificate is compared afterward.
    """
    from pathlib import Path
    import sys
    # This file's own directory is importable in standalone research execution.
    sys.path.insert(0,str(Path(__file__).parent))
    from bbp_bulk_certificate import certified_hex
    result, meta=certified_hex(count,guard=24)
    print('bulk BBP integer certificate',meta,flush=True)
    # Verify all original signed source identities independently in Fraction.
    for n in range(1,count+25):
        if source(n)!=canonical_source(n):
            raise AssertionError(f'four-pole/canonical source mismatch n={n}')
    return result,24,0


def canon(x):
    if isinstance(x,Fraction):return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,dict):return {str(k):canon(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [canon(v) for v in x]
    return x


def summary(ds,k):
    x=entropy_diagnostics(ds,k)
    return {q:x[q] for q in ('types','unique','missing','max_count','energy','D','D_div_n',
        'collision_sum','renyi_deficit','shannon_deficit','max_count_over_average','signed_collision_term')}


def run(n=40960,shuffles=16):
    if n!=40960:raise ValueError('Frozen protocol requires N=40960')
    s,maxdepth,refinements=certified_digits(n)
    old=REF_DIGITS.read_text(encoding='ascii').strip().upper()
    if len(old)!=16384 or s[:16384]!=old:
        raise AssertionError('NEW BBP SOURCE DOES NOT MATCH old independently certified baseline')
    (OUT/'CERTIFIED_HEX_40960.txt').write_text(s+'\n',encoding='ascii')
    digits=tuple(int(v,16) for v in s)
    checkpoints={}
    for i in CHECKPOINTS:
        xs=digits[:i]
        clock=lambert_clock(i)
        checkpoints[str(i)]={'clock':vars(clock),
             'depth':{str(k):summary(xs,k) for k in (1,2,3,4)},
             'entropy_bounds':[entropy_amplification_bound(xs,t,clock.integer_depth)
                               for t in range(1,clock.integer_depth+1)]}
        print(f'check {i} kW={clock.integer_depth} Dk/N={float(checkpoints[str(i)]["depth"][str(clock.integer_depth)]["D_div_n"]):.6f}',flush=True)
    rng=random.Random(20261108)
    controls=[]
    for j in range(shuffles):
        arr=list(digits);rng.shuffle(arr)
        controls.append({'index':j,**summary(arr,3)})
    sorted_arr=tuple(sorted(digits))
    period16=(tuple(range(16))*(n//16))
    const=(0,)*n
    baselines={'sorted':summary(sorted_arr,3),
               'period16':summary(period16,3),
               'constant':summary(const,3)}
    # Genuine signed collision lag: zeroed chronological time starts, no cyclic wrap.
    lags={'authentic': exact_overlap_returns(digits,3,64),
          'shuffled_0':exact_overlap_returns(_one_shuffle(digits),3,64),
          'sorted':exact_overlap_returns(sorted_arr,3,64),
          'period16':exact_overlap_returns(period16,3,64),
          'constant':exact_overlap_returns(const,3,64)}
    # Do not include per-lag charts until exact receipt checks finish.
    output={'schema':'SUCC-LW-HOLDOUT-1', 'scope':'OBSERVED FINITE; pi base16 normality OPEN',
        'parent':'44a4a96d2180a66524f882e4a1d50309fc8c97a9',
        'protocol_commit':'c207e377143818f95ec12957849834e1d3113661',
        'source':'original four signed rational BBP poles and U0=0',
        'digit_count':n,'digit_sha256':hashlib.sha256((s+'\n').encode('ascii')).hexdigest(),
        'old_baseline_sha256':hashlib.sha256((old+'\n').encode('ascii')).hexdigest(),
        'max_tail_refinement':maxdepth,'refinements':refinements,
        'checkpoints':checkpoints, 'shuffle_seed':20261108,'shuffled_controls':controls,
        'baseline_controls':baselines,'lag_observations':lags,
        'coupon_reference':[complete_coverage_reference(k) for k in (1,2,3)],
        'caveat':'Shuffles/ iid coupons are reference models, not source-derived distributions'}
    target=OUT/'FINITE_RECEIPT_40960.json'
    target.write_text(json.dumps(canon(output),indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('receipt sha256',hashlib.sha256(target.read_bytes()).hexdigest(),'digits sha256',output['digit_sha256'],flush=True)
    return output


def _one_shuffle(digits):
    xs=list(digits);random.Random(20261108).shuffle(xs)
    return xs


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=40960)
    a=ap.parse_args();run(a.n)
