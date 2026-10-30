"""Write new exact receipts only; never overwrite preserved evidence."""
from pathlib import Path
from fractions import Fraction as F
from fib_composition import *
import json,time
root=Path(__file__).resolve().parent
rows=[]
for k,a in [(13,19),(13,149),(21,29),(21,233),(34,43),(34,377),(55,89),(55,705)]:
    start=time.monotonic()
    gap=harmonic_gap_interval(a,k,512)
    scaled=iscale(gap,F(a*a));center=uniform_center(k);err=uniform_error(a)
    assert gap[0]>0 and scaled[0]>=center-err and scaled[1]<=center+err
    rows.append({'k':k,'a':a,'gap':dyadic(gap),'scaled_gap':dyadic(scaled),
                 'center':str(center),'uniform_error':str(err),'seconds':time.monotonic()-start,'status':'PASS'})
    print('exact rank',k,'age',a,'PASS',flush=True)
paths=[]
for a in [F(7,3),F(17),F(233),F(4093)]:
    paths.append({'a':str(a),'mean':str(moment(a,1)),'variance':str(variance(a)),
        'n4_laplace_difference':str(reused_laplace(a,F(3,7),4)-fresh_laplace(a,F(3,7),4)),
        'jensen_lower_Qlambda':[str(x) for x in jensen_lower(a)],
        'jensen_lower_interval':dyadic(golden_interval(jensen_lower(a)))})
record={'status':'PASS','authority':'exact rational log intervals and finite source identities; universal proof separate',
        'uniform_rows':rows,'source_arrow_rows':paths,'reciprocal_F_cutoff':80,
        'reciprocal_F_interval':dyadic(reciprocal_interval(80)),
        'gamma_memory_gap_interval':dyadic(gamma_gap_interval())}
p=root/'exact_receipt.json'
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
