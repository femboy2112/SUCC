"""Preserved reproduction of the incorrect fractional-state 2-adic comparison.
Unlike the first exploratory failure this run explicitly labels the wrong operation.
"""
import json
from bridge import raw_phases,mod2_fraction
x,C=raw_phases(2240)
rows=[]
for k in (9,10,11):
    n=128;Q=1<<k;M=1<<k
    f1=mod2_fraction(x[n],k);f2=mod2_fraction(x[n+Q],k)
    u1=(f1+C[n])%M;u2=(f2+C[n+Q])%M
    assert u1==u2
    assert f1!=f2
    rows.append({'k':k,'n':n,'lag':Q,'fractional_residues':[f1,f2],
                 'unwrapped_residues':[u1,u2],
                 'carry_residues':[C[n]%M,C[n+Q]%M],
                 'mistaken_fractional_equality_fails':True,
                 'correct_unwrapped_equality_passes':True})
print(json.dumps({'status':'EXPECTED_NEGATIVE_CONTROL','rows':rows},indent=2,sort_keys=True))
