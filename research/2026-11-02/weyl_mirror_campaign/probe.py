"""Reproducible exact finite diagnostics, not a universal normality test."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from weyl_mirror import (odd_modular_lift, fraction_phases, energy, slow_mesh,
                         mirror_wasserstein, antiphase_matching_cost, rational_interval)


def digest_int(n):
    data = n.to_bytes(max(1, (n.bit_length()+7)//8), 'big', signed=False)
    return hashlib.sha256(data).hexdigest()


def run():
    last = 8191
    D, xs = odd_modular_lift(last)
    independent = fraction_phases(256)
    assert [Fraction(x,D) for x in xs[:256]] == independent
    out = {'status':'FINITE OBSERVATIONS ONLY; no asymptotic source bound',
           'source':'original four poles, literal U0=0',
           'parent_sha':'20acb35a42b6ae5fb9260c041ed3a1aa47429484',
           'last_time':last, 'modulus_bits':D.bit_length(), 'modulus_odd':bool(D%2),
           'modulus_sha256_unsigned_big_endian':digest_int(D),
           'independent_fraction_prefix_agreement':256, 'prefixes':{}, 'epochs':{}}
    for N in (512,1024,1500,3000):
        W = mirror_wasserstein(xs[:N],D)
        row = {'mirror_W1_interval':rational_interval(W),
               'mirror_W1_approx':float(W),
               'mirror_cost_numerator_sha256':digest_int(W.numerator),
               'mirror_cost_denominator_sha256':digest_int(W.denominator),
               'feasible_antiphase_costs':{}}
        for h in (1,3,5,16):
            c = antiphase_matching_cost(xs[:N],D,h)
            row['feasible_antiphase_costs'][str(h)] = {
                'interval':rational_interval(c), 'approx':float(c)}
        out['prefixes'][str(N)] = row
    for A in (1024,2048,4096):
        m = slow_mesh(A)
        counts,E = energy(xs[A-1:2*A-1],D,m)
        out['epochs'][str(A)] = {'mesh':m, 'counts':counts,
                                 'energy':[E.numerator,E.denominator]}
    return out


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    args = p.parse_args()
    path = Path(__file__).with_name('FINITE_RECEIPT.json')
    result = run()
    if args.verify:
        assert result == json.loads(path.read_text())
        print('Exact receipt replay: PASS')
    else:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print(json.dumps(result,indent=2,sort_keys=True))
