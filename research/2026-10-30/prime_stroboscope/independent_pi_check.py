"""Numerical HOLDOUT only: compare exact Fraction-selected bins with mpmath pi.

The exact certification of bins comes from the BBP series and the analytic
Green-tail bound, NOT from the high-precision numerical pi reference.
"""
import json
import mpmath as mp
from fractions import Fraction
from prime_stroboscope import source_term
from selected_occupancy import certified_bin


def main():
    mp.mp.dps=410
    u=Fraction()
    digit_counts=[0]*16
    checked=0
    for n in range(1,257):
        u=16*u+source_term(n)
        computed,_,_=certified_bin(u,n,16)
        assert computed is not None
        reference=int(mp.floor(16*mp.frac(mp.mpf(16)**(n-1)*mp.pi)))
        assert computed==reference, (n,computed,reference)
        digit_counts[reference]+=1
        checked+=1
    print(json.dumps({"status":"PASS","decimal_precision":410,"positions_checked":checked,
         "independent_reference":"mpmath high precision pi",
         "certification_source":"exact native fractions + proven analytic BBP positive tail",
         "bin_counts":digit_counts},indent=2))

if __name__=='__main__':main()
