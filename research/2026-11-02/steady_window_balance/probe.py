"""Reproduce original BBP preregistered windows with exact integer oracles.

Default JSON is compact and contains certified rational 1e-10 enclosures
and sha256 digests of entire exact numerator/denominator pairs.
--raw explicitly emits the full rational numerator/denominator in hex.
--verify checks saved compact receipt independently of float displays.
"""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

P=Path(__file__).with_name('steady_windows.py')
S=importlib.util.spec_from_file_location('steady_window_module',P)
w=importlib.util.module_from_spec(S);S.loader.exec_module(w)


def checksum(N,D):
    data=N.to_bytes((N.bit_length()+7)//8 or 1,'big')+b'|'+D.to_bytes((D.bit_length()+7)//8 or 1,'big')
    return hashlib.sha256(data).hexdigest()


def run(epochs=(2048,4096), raw=False):
    D,arr=w.common_odd_modular_lift(2*max(epochs)-1)
    report=[]
    for A in epochs:
        temporal={}
        for h in (1,2,16):
            num,den=w.modular_time_pair_cost(D,arr,A,A//2,h)
            scaled=10**10*num//den
            entry={'numerator_denominator_sha256':checksum(num,den),
                   'certified_interval_1e10':[scaled,scaled+1],
                   'diagnostic_pass':18*den<100*num<32*den}
            if raw:
                entry['exact_numerator_hex']=hex(num)
                entry['exact_denominator_hex']=hex(den)
            temporal[str(h)]=entry
        windows={}
        for M in (16,64,256):
            counts=w.modular_bins(D,arr,A,A,M)
            vals={}
            for h in (1,2,16):
                try:q=w.antipodal_imbalance(counts,h)
                except ValueError:continue
                vals[str(h)]=str(q)
            windows[str(M)]={'collision_energy':str(w.histogram_energy(counts)),
                             'antiphase':vals}
        checks={'spatial_h1_M64_below_0p2':Fraction(windows['64']['antiphase']['1'])<Fraction(2,10),
                'spatial_h1_M256_below_0p35':Fraction(windows['256']['antiphase']['1'])<Fraction(35,100)}
        report.append({'A':A,'temporal':temporal,'spatial':windows,
                       'spatial_diagnostic_checks':checks})
    return report


if __name__=='__main__':
    result=run(raw='--raw' in sys.argv)
    if '--verify' in sys.argv:
        frozen=json.loads(Path(__file__).with_name('HOLDOUTS_SUMMARY.json').read_text())['epochs']
        assert frozen==result, 'Exact source/certificate receipt mismatch'
        print('2/2 original-source fresh epoch receipts VERIFY PASS')
    print(json.dumps({'original_source':'original 4 signed BBP poles; literal U0=0',
                      'test_type':'exact modular original phase, rational bin/cost comparison',
                      'status':'finite observations, NOT pi normality or all-horizon matching',
                      'epochs':result},indent=2))
