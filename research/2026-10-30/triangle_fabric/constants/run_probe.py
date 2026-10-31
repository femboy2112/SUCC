"""Preregistered exact arithmetic/interval holdouts, no universal extrapolation."""
import json
from pathlib import Path
from fractions import Fraction as F
from composition import (source,SIGMA2,proportion_moments,log_increment,
                         rational_lower_bounds,golden_excess,golden_interval,
                         dyadic_outward,add,scale,point)

rows=[]
for a in (F(3,2),1,9,49,129,505,1017,4089,37,113,389,1531):
    a=F(a)
    moments=proportion_moments(a)
    inc=log_increment(a)
    bounds=rational_lower_bounds(a)
    pgap=add(point(F(1,5)),scale(moments['EB'],-1))
    hgap=add(inc,point(-F(5,6)))
    ge=golden_interval(golden_excess(a))
    assert pgap[0]>bounds['proportion_gap']>0
    assert hgap[0]>bounds['harmonic_gap']>0
    assert ge[0]>0
    rows.append({'a':str(a),'EB':dyadic_outward(moments['EB']),
                 'scaled_covariance':dyadic_outward(scale(moments['covariance'],a*a)),
                 'scaled_proportion_gap':dyadic_outward(scale(pgap,a*a)),
                 'scaled_harmonic_gap':dyadic_outward(scale(hgap,a*a)),
                 'proportion_gap_bound':str(bounds['proportion_gap']),
                 'harmonic_gap_bound':str(bounds['harmonic_gap']),
                 'golden_positive_term':dyadic_outward(ge),
                 'rank_2_to_4_excess':dyadic_outward(add(hgap,ge))})
record={'status':'PASS','authority':'rational finite interval certificates; paper proof separate',
        'rows':rows,'limit_coefficients':{'scaled_proportion_gap':str(2*SIGMA2/35),
        'scaled_harmonic_gap':str(SIGMA2/5),'scaled_covariance':str(-4*SIGMA2/35)}}
path=Path(__file__).with_name('probe_receipt.json')
if path.exists(): raise SystemExit('refusing to overwrite receipt')
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
