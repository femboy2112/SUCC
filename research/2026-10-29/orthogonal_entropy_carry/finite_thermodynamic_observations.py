"""Finite descriptive observer receipt; not asymptotic normality authority."""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from orthogonal_carry import (trace, mismatch_bound, primitive_digit, circular_words,
                              entropy_deficit, debruijn16, walsh_coefficients)

cases={
  'authentic_zero_seed': [c%16 for c,d,m in trace(Q(0),2048)],
  'debruijn16_order2_periodic_negative': debruijn16(2)*8,
  'constant_zero_periodic_negative': [0]*2048,
}
result={'status':'OBSERVED at finite N=2048; not a proof of pi normality or nonnormality','N':2048,
        'correction_masks':{},'directions':{}}
for label,digits in cases.items():
    result['directions'][label]={
      'entropy_KL_1_2_3_nats':{str(k): round(entropy_deficit(circular_words(digits,k),k),12) for k in (1,2,3)},
      'q6_primitive_digit_frequency':str(Q(sum(primitive_digit(d) for d in digits),len(digits))),
      'walsh_mask_15':str(walsh_coefficients(circular_words(digits,1))[15]),
    }
for label,seed in [('authentic_zero_seed',Q(0)),('changed_seed_1_over_7',Q(1,7)),('changed_seed_1_over_15',Q(1,15))]:
 t=trace(seed,2048)
 result['correction_masks'][label]={
   'positions':[n for n,(c,d,m) in enumerate(t,1) if m],
   'count':sum(m for c,d,m in t),
   'all_seed_proved_count_bound':mismatch_bound(2048),
   'exceptional_carry16_count':sum(c==16 for c,d,m in t),
 }
print(json.dumps(result,indent=2,sort_keys=True))
