import json
from pathlib import Path
from fractions import Fraction as F
from composition import (source,convolution_partial_fractions,log_increment_k,
    rank_harmonic_bound,harmonic,golden_excess_k,golden_interval,
    dyadic_outward,add,point,scale)
rows=[]
for k in (3,5,8):
    parts=convolution_partial_fractions(k)
    for a in (F(11,3),F(17),F(83),F(347)):
        for t in (F(0),F(2,7),F(23)):
            total=sum((c/(a+t+d)**m for d,m,c in parts),F(0))
            assert total==source(a+t)**k
        gap=add(log_increment_k(a,k),point(-harmonic(2*k-1)+1))
        bound=rank_harmonic_bound(a,k)
        assert gap[0]>bound>0
        ge=golden_interval(golden_excess_k(a,k))
        assert ge[0]>0
        rows.append({'k':k,'a':str(a),'harmonic_gap':dyadic_outward(gap),
                     'scaled_harmonic_gap':dyadic_outward(scale(gap,a*a)),
                     'harmonic_bound':str(bound),'golden_term':dyadic_outward(ge),
                     'status':'PASS'})
output={'status':'PASS','rows':rows,'exact_partial_fraction_checks':36,
        'authority':'finite rigorous rational and log-interval certificates; paper proof separate'}
p=Path(__file__).with_name('rank_receipt.json')
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
