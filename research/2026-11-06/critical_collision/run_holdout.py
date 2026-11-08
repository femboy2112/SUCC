import time,json,sys
from experiment import original
from shell_certified import radius_census
from fractions import Fraction
start=time.monotonic()
print('start',flush=True)
s=sorted(original(4096))
print('source_sorted_sec',round(time.monotonic()-start,2),flush=True)
r=Fraction(1,4097);rows=[]
while True:
 a=radius_census(s,r)
 print('radius',len(rows),'A',a,'seconds',round(time.monotonic()-start,2),flush=True)
 if (a-4096)*4*r.denominator>9*4096**2*r.numerator:
  with open('HOLDOUT_N4096.generated.json','w') as f:json.dump({'N':4096,'radii':rows,'failed_radius':str(r),'A':a,'passed':False},f,indent=2)
  print('FAIL threshold',flush=True);sys.exit(1)
 rows.append({'radius':str(r),'A':a})
 if r==Fraction(1,2):
  with open('HOLDOUT_N4096.generated.json','w') as f:json.dump({'N':4096,'radii':rows,'passed':True},f,indent=2)
  print('DONE PASS',flush=True);break
 r=min(r*Fraction(4,3),Fraction(1,2))
