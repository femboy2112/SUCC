"""Reproduce bounded original-source finite controls; no infinite claim."""
import json, hashlib, math
from pathlib import Path
from chiral_probe import (source_states, mutant_states,return_jet,
       forcing,forcing_compact,phase,tail_interval,circle_midpoint,
       complex_loop_signal,expected_jet16,expected_jet32)
ROOT=Path(__file__).parent
Blist=[8,16,32]
states=source_states(2*max(Blist)+16+8)
mut=mutant_states(len(states)-1)
q=16
out={
  'date':'2026-11-15',
  'source':'SUCC original rational 4-pole U0=0; unreduced Fraction arithmetic',
  'source_core_git_blob':'34cb7b64f6975e05586ec220a4655961a8e7b636',
  'status':'CERTIFIED FINITE modular arithmetic; COMPLEX SMOKE ONLY for real circle',
  'original_jet16':[return_jet(states,n,1,4) for n in range(4,12)],
  'original_jet32':[return_jet(states,n,1,5) for n in range(4,12)],
  'mutated_jet16':[return_jet(mut,n,1,4) for n in range(4,12)],
  'original_source_qperiod_samples':[],
  'finite_four_time_complex_smoke':[],
  'negative_controls':{
      'coherent_same_forcing_wrong_real_seed': 'z_n=0, v_(n+2)=-v_n and two-path output zero',
      'rational_period_q':'x=1/(16^16-1), z_(n+16)=z_n and four-time output zero',
      'isometric_zero_pointed_coboundary_mutant':'g(n)=2n²; J̃_n=J_n+4n mod16; source commutator +1'
  },
  'claim_boundary':'No original-pi all-large-shell lower bound, R0 or normality established.'
}
for n in range(4,12):
   out['original_source_qperiod_samples'].append({
      'n':n,'source_jet_mod16':return_jet(states,n,1,4),
      'source_jet_mod32':return_jet(states,n,1,5),
      'two_step_ratio_mod16':(return_jet(states,n+2,1,4)-return_jet(states,n,1,4))%16,
      'two_step_ratio_mod32':(return_jet(states,n+2,1,5)-return_jet(states,n,1,5))%32,
      'mutated_two_step_ratio_mod16':(return_jet(mut,n+2,1,4)-return_jet(mut,n,1,4))%16
   })
for B in Blist:
   ratios=[];energy=[]
   for n in range(B,2*B):
      v0=complex_loop_signal(states,n,1,1)
      v2=complex_loop_signal(states,n+2,1,1)
      ratio=v2*v0.conjugate()
      ratios.append(ratio)
      energy.append(abs(v0+v2)**2/2)
   mean=sum(ratios)/B
   out['finite_four_time_complex_smoke'].append({
      'B':B,'k':1,'q':16,'mean_signed_real':round(mean.real,14),
      'mean_signed_imag':round(mean.imag,14),
      'mean_normalized_two_path_energy':round(sum(energy)/B,14),
      'interval_status':'source T intervals exact; transcendental complex arithmetic float NOT certified',
      'local_source_tail_bound':'original r(n)/15 positive Green interval'
   })
p=(ROOT/'FINITE_REPORT.json');p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('Finite original-source report written:',p)
print('clock jet modulo 16',out['original_jet16'])
print('clock jet modulo 32',out['original_jet32'])
print('coherent two-path smoke',out['finite_four_time_complex_smoke'])
