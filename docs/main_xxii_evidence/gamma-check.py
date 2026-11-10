import sys,json,platform
sys.path.insert(0,'/home/leah/SUCC')
import observational_succ
observational_succ.__path__.insert(0,'/home/leah/succ-main-xxii-evidence/gamma-source/observational_succ')
from observational_succ.duck_bbp import forcing
from observational_succ import bbp_euler_mascheroni as em, bbp_gamma_matrix_deformation as gd, balanced_prime_clock as bc
from fractions import Fraction as F
import mpmath as mp
checks={}
for n in range(1,101): assert em.forcing(n)==forcing(n) and gd.rational_pole_step(n)==n*forcing(n)
checks['rational_source_and_partial_fraction_1_100']=True
for g in range(1,9):
 expected=sum((16**(g-j)*forcing(j) for j in range(1,g+1)),F())
 assert em.block_source(g)==expected
 assert em.bbp_gamma_log_argument(g)==64*expected/(16**g-1)
 assert em.mellin_first_jet_coefficient(g)==F(5,2)-F(8*g,16**g-1)
checks['block_source_constants_and_mellin_jets_g1_8']=True
with mp.workdps(70):
 def cv(x):return mp.mpf(x.numerator)/x.denominator
 dig=-sum(cv(w)*mp.digamma(cv(a)) for w,a in zip(gd.POLE_WEIGHTS,gd.POLE_SHIFTS))
 s=mp.sqrt(2);closed=mp.mpf(15)/64*mp.euler+(27+31*s)*mp.pi/128+mp.mpf(39)/32*mp.log(2)+31*s/64*mp.log(1+s)
 assert abs(dig-closed)<mp.mpf('1e-65')
 checks['gamma_BBP_digamma_vs_closed_abs_error']=str(abs(dig-closed))
 checks['gamma_BBP_70_digit_diagnostic']=str(dig)
 checks['gamma_block_clock_g1_diagnostic']=str(mp.euler-mp.log(cv(em.bbp_gamma_log_argument(1)))/2)
 checks['gamma_q_1_16_diagnostic']=str(mp.log(mp.mpf(15)/16)+mp.log(16)*mp.fsum(1/(mp.mpf(16)**n-1) for n in range(1,100)))
A,p=80,193
assert bc.epoch_stage_boundaries(A,p)
for mode in ((1,-1,0),(1,0,-1),(0,1,-1)):
 assert bc.epoch_mode_resonance_mass(A,p,p,mode)==1
 assert bc.epoch_histogram_from_stage(A,p,p,mode)=={0:A}
checks['BEC05_counterexample_h_equal_p']='A=80,p=193,h=193: every offdiagonal histogram is {0:80}, Gram=J, min eigenvalue0; claimed fixed target only valid p not dividing h'
u=(1,-1)+(0,)*14;v=(1,1,-2)+(0,)*13
assert sum(u)==sum(v)==sum(x*y for x,y in zip(u,v))==0
X=tuple(tuple(F(x*y,64) for y in v) for x in u)
assert all(sum(X[i][k]*X[k][j] for k in range(16))==0 for i in range(16) for j in range(16))
assert sum(x*x for row in X for x in row)==F(3,1024)
assert min(F(1,16)+x for row in X for x in row)>0
checks['nilpotent_counterexample_exact_energy']='3/1024; X!=0, X^2=0, positive doubly stochastic H+X'
print(json.dumps({'python':platform.python_version(),'mpmath':mp.__version__,'scope':'manual exact finite identities; MP agreement diagnostic only; no all-epoch certificate','checks':checks},indent=2))
