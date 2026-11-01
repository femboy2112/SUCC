"""Emit finite exact rational and certified radical probes; no numerical π as authority."""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('circle_ratio_probe_module',ROOT/'circle_ratio.py')
m=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=m
spec.loader.exec_module(m)


def outward(q, places=22, up=False):
    q=Fraction(q)
    s=10**places
    a=q.numerator*s//q.denominator
    if up and Fraction(a,s)<q:a+=1
    return f'{a//s}.{a%s:0{places}d}'


def compute():
    rows=[]
    for n in range(1,11):
        c=m.bridge_certificate(n,110)
        rows.append({
        'n':n,'geom_refinement_depth':4*n,'arc_chords':16**n,
        'bbp_source_lower_exact':str(c['bbp_lower']),
        'bbp_source_lower_decimal_floor':outward(c['bbp_lower']),
        'geom_inscribed_floor':outward(c['polygon_lower_interval'].lo),
        'geom_inscribed_ceil':outward(c['polygon_lower_interval'].hi,up=True),
        'geom_circumscribed_ceil':outward(c['polygon_upper'],up=True),
        'wilson_source_upper_exact':str(c['wilson_upper']),
        'wilson_source_upper_decimal_ceil':outward(c['wilson_upper'],up=True),
        'certified_pi_upper':outward(c['certified_upper'],up=True),
        'geometric_error_upper':str(c['polygon_error']),
        'source_tail_upper':str(c['bbp_tail_upper']),
        'strict_B_less_P_less_W':True,
        'universal_tail_separation':n>=2,
        'source_odd_conductor':str(m.odd_bbp_conductor(n))
        })
    return rows

if __name__=='__main__':
    print(json.dumps(compute(),indent=2))
