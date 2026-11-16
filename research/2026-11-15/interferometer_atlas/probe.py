"""Reproduce rigorously enclosed finite original-π interferometer responses.

All intervals are outward-rounded from exact rational computations, including
Machin/alternating-series pi enclosure, Taylor remainder, original Green
transport and infinite Oily harmonic tail. A finite plot is never an
asymptotic theorem.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
from observational_succ.interferometer_atlas import (
    source_shell_words,haar_volume_energy,certified_original_oily_energy,
    oily_tail,source_all_mode_transfer_budget)

D=10**10

def outward(q:Q,upper=False):
    integer=q.numerator*D//q.denominator
    if upper and q.numerator*D%q.denominator:
        integer+=1
    return f"{integer//D}.{integer%D:010d}"


def run():
    cases=[]
    for B in (4,8,16,32):
        haars=source_shell_words(B,8)
        H,tail=haar_volume_energy(haars,8)
        oily=certified_original_oily_energy(B,16,machin_terms=11,taylor_degree=12)
        cases.append({
            'B':B,'Haar_exact_depth':8,
            'Haar_lower_outward':outward(H),'Haar_upper_outward':outward(H+tail,True),
            'Haar_unseen_bound':'1/256',
            'Oily_harmonics':16,
            'Oily_lower_outward':outward(oily['lower']),
            'Oily_upper_outward':outward(oily['upper'],True),
            'Oily_harmonic_tail':'%s/%s'%(oily_tail(16).numerator,oily_tail(16).denominator),
            'Oily_source_rational_to_pi_error':'%s/%s'%(
                source_all_mode_transfer_budget(B).numerator,
                source_all_mode_transfer_budget(B).denominator),
            'Oily_Taylor_Machin_error_lt_1e-12':oily['trigonometric_error']<Q(1,10**12),
            'strict_global_conclusion':'UNVERIFIED'})
    return {'claim':'CERTIFIED-FINITE original four-pole BBP U0=0 only',
            'pi_normality':'OPEN','RH':'OPEN',
            'original_source':'four poles + exact rational BBP tail, Machin & Taylor outward bounds',
            'all_frequency_scanning_source':'Oily2 nonzero conditional grade, not an authenticated physical BBP oscillator',
            'certified_shells':cases}

if __name__=='__main__':
    report=run()
    print(json.dumps(report,indent=2))
