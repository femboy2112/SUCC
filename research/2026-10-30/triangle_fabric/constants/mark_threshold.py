"""Exact finite sharp-mark calibration; thresholds are proved in the dossier."""
from fractions import Fraction as F
from pathlib import Path
import json
from composition import source

def polynomial(t,k):return sum((t**j for j in range(k-1,2*k-1)),F(0))-1

def bracket(k):
    lo,hi=F(0),F(1)
    for _ in range(96):
        mid=(lo+hi)/2
        if polynomial(mid,k)<0:lo=mid
        else:hi=mid
    assert polynomial(lo,k)<0<polynomial(hi,k)
    return lo,hi

def correction(a,t,k):
    l=source(a/t)/source(a)
    assert t*t<l<t
    direct=l-l**k-t*t+t**(2*k)
    endpoint=t-t**k-t*t+t**(2*k)
    assert endpoint==-t*(1-t)*polynomial(t,k)
    return direct

rows=[]
for k in (2,3,5,8):
    lo,hi=bracket(k)
    below=lo-F(1,1000);above=hi+F(1,1000)
    positives=[]
    for a in (F(1,1000),F(1),F(37)):
        value=correction(a,below,k)
        assert value>0
        positives.append({'a':str(a),'sign':1})
    negative=None
    for j in range(1,13):
        a=F(1,10**j);value=correction(a,above,k)
        if value<0:
            negative={'a':str(a),'sign':-1,'value':str(value)}
            break
    assert negative is not None,'finite search ambiguous'
    rows.append({'k':k,'t_threshold_interval':list(map(str,(lo,hi))),
                 't_below':str(below),'t_above':str(above),
                 'positive_checks':positives,'counterexample':negative})
record={'status':'PASS','rows':rows,'exact_positive_checks':12,
        'exact_above_threshold_counterexamples':4,
        'authority':'finite rational calibration; universal classification is paper proof'}
p=Path(__file__).with_name('mark_receipt.json')
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
