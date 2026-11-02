"""Rebuild finite-only rational interval receipt; prints no asymptotic claims."""
import hashlib
import json
from pathlib import Path
from interval import prove_window,certify_both_directions

HERE=Path(__file__).resolve().parent
PRIMES=(269,373,397,509,997)

def build():
    intervals=[r for p in PRIMES for r in prove_window(p)]
    anti=certify_both_directions()
    assert len(intervals)==15 and len(anti)==2
    blobs={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
           for name in ('prime_window.py','interval.py','run_receipt.py')}
    return {'status':'CERTIFIED_FINITE_EXACT_RATIONAL_INTERVAL',
            'not_an_asymptotic_pi_normality_claim':True,
            'parent_main':'81045770234a114247e43eb08ae5c6d446e9514a',
            'stacked_on_pr459':'ec9c5a98772c60ab06bd4bb0a3d52a751a8bdc6a',
            'window_class':'p prime, p>5, p congruent 5 mod 8',
            'harmonics':[1,3,5],
            'trig_method':'exact Fraction source; exact mod1; 32-bit dyadic floor; Machin rational pi interval; Taylor/Lagrange rational error; outward 10^9 L1 ceiling',
            'cases':intervals,'rigorous_phase_comparison':anti,'program_sha256':blobs}

if __name__=='__main__':
    rec=build()
    p=HERE/'FINITE_RECEIPT.json'
    p.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print('RATIONAL_INTERVAL_CERTIFIED: %s cases; %s strict cofactor directions' %
          (len(rec['cases']),len(rec['rigorous_phase_comparison'])))
