"""FINITE_DIAGNOSTIC_ONLY. Numeric original-source phase interactions; not proof."""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import floor
sys.path.insert(0,str(Path(__file__).resolve().parent))
from pole_interactions import channel_states, combined_states, SHIFTS,WEIGHTS
try:
 import mpmath as mp
except ImportError:
 raise SystemExit('mpmath needed only for optional finite diagnostic')

def run(N,h,precision=70):
 mp.mp.dps=precision
 channels=channel_states(N);combined=combined_states(N)
 sums={m:mp.mpc(0) for m in (3,4,5)};joint=mp.mpc(0)
 pair={(3,4):mp.mpc(0),(3,5):mp.mpc(0),(4,5):mp.mpc(0)}
 diff=mp.mpf(0)
 def phase(x):
  x=F(x)%1
  theta=mp.mpf(x.numerator)/mp.mpf(x.denominator)
  return mp.exp(2j*mp.pi*theta)
 for n in range(1,N+1):
  z={3:phase(h*2*channels[3][n]),4:phase(h*channels[4][n]),5:phase(h*channels[5][n])}
  exact=phase(h*combined[n]);zjoint=z[3]*z[4]*z[5]
  diff=max(diff,abs(exact-zjoint))
  joint+=exact
  for m in (3,4,5):sums[m]+=z[m]
  for a,b in pair:pair[a,b]+=z[a]*z[b]
 means={k:s/N for k,s in sums.items()}
 triple=joint/N
 pairmeans={k:v/N for k,v in pair.items()}
 cov2={p:pairmeans[p]-means[p[0]]*means[p[1]] for p in pair}
 triple_cumulant=triple-means[3]*means[4]*means[5]-sum(cov2[a,b]*means[next(k for k in (3,4,5) if k not in (a,b))] for a,b in pair)
 return {'N':N,'h':h,'joint_abs':float(abs(triple)),'joint_real':float(triple.real),
 'product_of_marginal_abs':float(abs(means[3]*means[4]*means[5])),
 'triple_centered_cumulant_abs':float(abs(triple_cumulant)),
 'marginal_abs':{str(k):float(abs(v)) for k,v in means.items()},
 'source_phase_product_error':mp.nstr(diff,6),
 'proof_status':'FINITE_DIAGNOSTIC_ONLY'}

if __name__=='__main__':
 ap=argparse.ArgumentParser()
 ap.add_argument('--horizons',nargs='+',type=int,default=[128,256,512]);ap.add_argument('--harmonics',nargs='+',type=int,default=[1,3,5]);a=ap.parse_args()
 print(json.dumps([run(N,h) for N in a.horizons for h in a.harmonics],sort_keys=True,indent=2))
