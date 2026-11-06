"""Deterministic predeclared source/odd-place diagnostics; floats are not proof."""
import json
from adelic_triangle import local_cycle_probe, prime_phase_covariance, hostile_compensation, state, global_odd_fraction

cal=local_cycle_probe(149)
holdouts=[]
for p in [181,197,269,293]:
    row=local_cycle_probe(p)
    row['cross_prime']=prime_phase_covariance(p)
    holdouts.append(row)
comp=hostile_compensation(149,1009)
receipts=[]
for n in (1,2,5,13,21,29,37,40):
    x=state(n)
    receipts.append({'n':n,'odd_denominator_digits':len(str(x.denominator)),
                     'adelic_crt_exact':global_odd_fraction(x)==x%1})
print(json.dumps({'status':'OBSERVED-FINITE','p149_preseen_calibration':cal,
                  'preregistered_prime_cycles':holdouts,
                  'hostile_second_prime':comp,'crt_receipts':receipts,
                  'pi_normality':'OPEN','selected_signed_Weyl':'OPEN'},
                 indent=2,sort_keys=True))
