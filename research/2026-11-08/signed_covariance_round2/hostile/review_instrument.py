"""Independent exact oracle versus root's interval energy/covariance path."""
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import exact_oracle as exact
spec = importlib.util.spec_from_file_location("hostile_review_lag_instrument", ROOT/"lag_instrument.py")
instrument = importlib.util.module_from_spec(spec)
spec.loader.exec_module(instrument)


def box(value):
    re, im = map(Q, value)
    return instrument.Box(instrument.Interval.ratio(re.numerator,re.denominator),
                          instrument.Interval.ratio(im.numerator,im.denominator))


def contains(interval, value):
    value = Q(value)
    return interval.lo*value.denominator <= value.numerator*instrument.SCALE <= interval.hi*value.denominator


def mean(values):
    total = exact.gsum(values)
    return Q(total[0],len(values)), Q(total[1],len(values))


def run():
    energy_checks = 0
    covariance_checks = 0
    for length in range(1,5):
        for values in product(exact.UNITS,repeat=length):
            boxes = list(map(box,values))
            lags = instrument.lag_means(boxes,length)
            for h in range(1,length+1):
                truth = exact.direct_energy(values,h)
                assert contains(instrument.sliding_energy(boxes,h),truth)
                energy, unsigned = instrument.energy_from_lags(lags,h)
                assert contains(energy,truth)
                assert contains(unsigned,exact.pair_energy(values,h,absolute=True))
                energy_checks += 3
            local = [exact.UNITS[(j*j+1)%4] for j in range(length)]
            comp = [exact.mul(z,exact.conj(a)) for a,z in zip(local,values)]
            prod = exact.mul(mean(local),mean(comp))
            mean_full = mean(values)
            cov = mean_full[0]-prod[0],mean_full[1]-prod[1]
            got_cov, got_prod = instrument.signed_transport(list(map(box,local)),boxes)
            assert contains(got_cov.re,cov[0]) and contains(got_cov.im,cov[1])
            assert contains(got_prod.re,prod[0]) and contains(got_prod.im,prod[1])
            covariance_checks += 4
    bounded = ((Q(1,3),Q(1,4)), (Q(3,5),Q(4,5)), (Q(-2,7),0))
    boxes = list(map(box,bounded))
    diagonal = Q(sum(exact.norm2(v) for v in bounded),len(bounded))
    di = instrument.Interval.ratio(diagonal.numerator,diagonal.denominator)
    for h in range(1,4):
        lags = instrument.lag_means(boxes,h)
        energy,_ = instrument.energy_from_lags(lags,h,di)
        assert contains(energy,exact.direct_energy(bounded,h))
        energy_checks += 1
    sys.path.insert(0,str(ROOT))
    import explicit_selector
    # Trial-division prime list and literal multiplication orbits differ from
    # the production sieve and factor-stripping multiplicative-order routine.
    primes = [p for p in range(3,513)
              if all(p % d for d in range(2,isqrt(p)+1))]
    orders = {p:exact.order16(p) for p in primes}
    selector_checks = 0
    for a in range(1,129):
        for c in (1,2,3):
            candidates = [(p,orders[p]) for p in primes
                          if p <= 4*a and p % 8 == 1
                          and orders[p]**3 > p
                          and orders[p]**2 * p.bit_length()**(2*c) > p]
            expected = max(candidates,default=None)
            assert explicit_selector.select(a,c) == expected
            selector_checks += 1
    reviewed = (ROOT/"chronology/THEOREMS.md",ROOT/"cube/THEOREMS.md",
                ROOT/"EXPLICIT_CLOCKS.md",ROOT/"explicit_selector.py",ROOT/"lag_instrument.py",
                ROOT/"run_lag_probe.py",HERE/"THEOREMS.md",HERE/"exact_oracle.py")
    return {"status":"CERTIFIED-FINITE",
            "energy_containments":energy_checks,"covariance_containments":covariance_checks,
            "independent_selector_maximality_checks":selector_checks,
            "review":"Independent Gaussian-rational oracle; root interval implementation tested without phase evaluation",
            "hashes":{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in reviewed},
            "pi_base16_normality":"OPEN","RH":"OPEN"}


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,sort_keys=True))
