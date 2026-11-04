"""Post-hoc floating discovery scan; NOT a proof or preregistered holdout."""
from fractions import Fraction as F
import numpy as np

N=4096;Q=16
u=F();phases=[]
for n in range(N):
    if n:
        a=120*n*n-89*n+16
        d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        u=16*u+F(a,d)
    phases.append(float(u%1))
p=np.asarray(phases)

failures=[]
for start in range(1,4097,128):
    h=np.arange(start,min(start+128,4097),dtype=np.int64)
    Z=np.exp(2j*np.pi*h[:,None]*p[None,:])
    B=Z.reshape(len(h),N//Q,Q).sum(axis=1)
    ratios=(np.abs(B)**2).sum(axis=1)/N
    failures.extend((int(hj),float(ratio)) for hj,ratio in zip(h,ratios) if ratio>2)
print("POSTHOC exploratory failures:",failures)
assert set(h for h,_ in failures)=={1203,1800,3576}
print("FLOAT SEARCH ONLY; posthoc_falsifier.py has the exact rigorous followup")
