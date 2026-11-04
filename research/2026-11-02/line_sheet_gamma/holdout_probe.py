"""Exact preregistered dyadic original BBP collision replay (no pi digits).

Usage: python research/2026-11-02/line_sheet_gamma/holdout_probe.py
       python research/2026-11-02/line_sheet_gamma/holdout_probe.py --verify

Counts are exact integers/Fractions. Log10 Galois values are floating displays.
Numerical/finite matching does not imply a universal selected bound.
"""
from fractions import Fraction
from math import log10
from pathlib import Path
import json
import sys
from line_sheet import original_states, source_selfscale_collision, epoch_prime_family

EXPECTED={
    512:(970,Fraction(485,256),4,338,64),
    1024:(2026,Fraction(1013,512),5,643,115),
    2048:(4050,Fraction(2025,1024),6,1300,216),
}


def run():
    all_states=original_states(4095)
    observations=[]
    for A in (512,1024,2048):
        counts,C=source_selfscale_collision(A,all_states)
        ps=epoch_prime_family(A)
        assert all((p-1)//8+1<=A and 4*((p-1)//8)>=2*A-1 for p in ps)
        s=sum(x*x for x in counts)
        observations.append({
            "A":A, "collision_integer":s,
            "exact_C_A":str(C.numerator)+"/"+str(C.denominator),
            "max_occupancy":max(counts),
            "occupied_bins":sum(v>0 for v in counts),
            "newborn_prime_count":len(ps),
            "pass":C<Fraction(7,2),
            "galois_d1_log10_abs_float":sum(-log10(p-1) for p in ps if pow(16,1,p)!=1),
            "galois_d4_log10_abs_float":sum(-log10(p-1) for p in ps if pow(16,4,p)!=1)
        })
    return observations


def main():
    rows=run()
    if '--verify' in sys.argv:
        recorded=json.loads(Path(__file__).with_name('FRESH_HOLDOUTS.json').read_text())['rows']
        for row,reference in zip(rows,recorded):
            expected=EXPECTED[row['A']]
            assert (row['collision_integer'],Fraction(row['exact_C_A']),
                    row['max_occupancy'],row['occupied_bins'],
                    row['newborn_prime_count'])==expected
            assert all(row[k]==reference[k] for k in (
                'A','collision_integer','exact_C_A','max_occupancy',
                'occupied_bins','newborn_prime_count','pass'))
            for k in ('galois_d1_log10_abs_float','galois_d4_log10_abs_float'):
                assert abs(row[k]-reference[k])<1e-8
        print('3/3 preregistered source-exact holdouts REPLAY PASS')
    print(json.dumps(rows,indent=2))


if __name__=='__main__':
    main()
