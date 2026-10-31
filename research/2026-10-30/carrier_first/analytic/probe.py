"""Preserve exact data for source-specific resolvent certificates."""
import json
from fractions import Fraction as Q
from resolvent import certificate, moments, atomic_tail_budget, source

rows=[]
for d in (1,2,3,4,5,6,7,8,11,14,19):
    c=certificate(d)
    scaled=c['upper']-c['lower']
    N=0
    while scaled*16**(N+1)<Q(1,16):N+=1
    rows.append({key:([str(x) for x in val] if isinstance(val,list) else str(val))
                 for key,val in c.items()} |
                {'phase_width_below_1_over_16_through_N':N,
                 'center_denominator_bits':c['center'].denominator.bit_length(),
                 'same_prefix_raw_tail_budget':str(source(2*d+1)/(15*16**(2*d))),
                 'atomic_coherence_tail_sum':str(atomic_tail_budget(moments(2*d+1),d))})
print(json.dumps({'status':'PASS','authority':'exact rational finite outputs; all-order proof separate',
                  'discovery_orders':list(range(1,9)),'fresh_orders':[11,14,19],
                  'rows':rows},indent=2))
