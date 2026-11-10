"""Independent numerical/symbolic oracle, NOT a proof of zero-seed normality.

Requires numpy and sympy (in SUCC research/test extras); math module has none.
"""
from pathlib import Path
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
D=np.array([int(ch,16) for ch in (HERE/'REUSED_HEX_40960.txt').read_text().strip()],dtype=int)
n=len(D)
C=np.zeros((16,16),dtype=int)
np.add.at(C,(D,np.roll(D,-1)),1)
P=C/n
W=np.exp(-2j*np.pi*np.outer(np.arange(16),np.arange(16))/16)
Z=W@P@W.T
Zfft=np.fft.fft2(P)
assert np.max(abs(Z-Zfft))<1e-12
E2=np.sum(np.abs(Zfft)**2)-1
E2_direct=256*np.sum((P-1/256)**2)
assert abs(E2-E2_direct)<1e-12
basis=sum(abs(Zfft[u,v])**2 for u in range(16) for v in range(16) if (u+v)%16)
rel=sum(abs(Zfft[u,(-u)%16])**2 for u in range(1,16))
assert abs(E2-basis-rel)<1e-12

x=sp.symbols('x')
Q=4-2*sp.exp(-3*x)-sp.exp(-4*x)-sp.exp(-5*x)
for g in (1,2,3,4):
    B=sum(16**(g-1-j)*sp.exp(-8*j*x) for j in range(g))
    first=sp.simplify(sp.diff(Q*B,x).subs(x,0))
    second=sp.simplify(sp.diff(Q*B,x,2).subs(x,0))
    pred_second=-59*sum(16**(g-1-j) for j in range(g))-240*sum(j*16**(g-1-j) for j in range(g))
    assert first==16**g-1 and second==pred_second

r=lambda n:4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
k=sp.symbols('k',integer=True,positive=True)
a=16*k-15
r_block=16*r(2*k-1)+r(2*k)
laplace=16*r(2*k-1)+r(2*k)  # check independent symbolic four-pole expansion
laplace_direct=sum(w*(16/sp.sympify(a+d)+1/(a+8+d))
                   for w,d in [(4,0),(-2,3),(-1,4),(-1,5)])
assert sp.simplify(r_block-laplace_direct)==0
print('INDEPENDENT ORACLE PASS: NumPy fft2 vs direct DFT; orthogonal sector split;')
print('SymPy all Gamma endpoint jets g=1..4; two-block original rational poles.')
print(f'N={n}, E2={E2:.12f}, basis={basis:.12f}, relative={rel:.12f}')
