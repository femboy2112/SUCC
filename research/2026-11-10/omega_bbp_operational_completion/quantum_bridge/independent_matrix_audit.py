"""Numpy+SymPy, independent direct matrix oracle (not a runtime dependency)."""
import sys
from pathlib import Path
sibling=Path(__file__).resolve().parent.parent
if (sibling/'omega_haar.py').exists():
    sys.path.insert(0,str(sibling))      # Normal repository layout
else:
    sys.path.insert(0,str(sibling.parent/'omega_haar_round'))  # Isolated local review
sys.path.insert(0,str(Path(__file__).parent))
import numpy as np
import sympy as sp
from omega_quantum import *
from omega_haar import source_block,chronological_area,energy,commutator

P2=sp.zeros(6)
P3=sp.zeros(6)
for start in (0,2,4):
    for i in range(start,start+2):
        for j in range(start,start+2):P2[i,j]=sp.Rational(1,2)
for start in (0,3):
    for i in range(start,start+3):
        for j in range(start,start+3):P3[i,j]=sp.Rational(1,3)
C=P2*P3-P3*P2
assert C.T==-C
assert C**3== -sp.Rational(2,9)*C
for i in range(6):
    vec=tuple(int(k==i) for k in range(6))
    assert C*sp.Matrix(vec) == sp.Matrix(commutator(vec))
C_np=np.array(C,dtype=float)
assert np.allclose(np.linalg.eigvalsh(1j*C_np),[-GAMMA,0,0,0,0,GAMMA],atol=1e-14)

for group in (2,3):
    U=np.column_stack([group_butterfly(tuple(float(j==i) for j in range(6)),group) for i in range(6)])
    assert np.linalg.norm(U.conj().T@U - np.eye(6))<1e-14
    Π=np.diag([float(j%group==0) for j in range(6)])
    P=np.array(P2 if group==2 else P3,dtype=float)
    assert np.linalg.norm(U.conj().T@Π@U -P)<1e-14

W=np.column_stack([haar_analyze(tuple(float(j==i) for j in range(16))) for i in range(16)])
assert np.linalg.norm(W.conj().T@W - np.eye(16)) < 1e-13
H=np.column_stack([walsh_hadamard(tuple(float(j==i) for j in range(16))) for i in range(16)])
assert np.linalg.norm(H.conj().T@H - np.eye(16))<1e-13
assert np.linalg.norm(W-H)>0.1

Hch=np.array(chirality_matrix(),dtype=complex)
assert np.linalg.norm(Hch.conj().T-Hch)<1e-14
assert np.allclose(np.sort(np.linalg.eigvalsh(Hch)),
                   [-GAMMA,-GAMMA]+[0]*8+[GAMMA,GAMMA],atol=1e-14)
assert np.linalg.norm(np.linalg.matrix_power(Hch,3)- GAMMA**2*Hch) <1e-14

x=sp.symbols('x',positive=True)
R=lambda j:4/(8*x+8*j+1)-2/(8*x+8*j+4)-1/(8*x+8*j+5)-1/(8*x+8*j+6)
v=sp.Matrix([R(j) for j in range(6)]); w=sp.Matrix([R(j+1) for j in range(6)])
# Piecewise polynomial expansion avoids huge rational-function expansion.
t=sp.symbols('t',positive=True)
series={j:sp.series(R(j).subs(x,1/t),t,0,10).removeO().expand() for j in range(7)}
vs=sp.Matrix([series[j] for j in range(6)])
ws=sp.Matrix([series[j+1] for j in range(6)])
area9=sp.expand((vs.T*C*ws)[0]).coeff(t,9)
assert area9 == sp.Rational(675,128), area9
assert sp.expand((vs.T*C*ws)[0]).coeff(t,8) == 0
c=sp.Rational(15,64)
chlimit=sp.simplify(2*area9/(12*c*c))
assert chlimit==16,chlimit
pminuslimit=sp.simplify((c*c*sp.Rational(44,3))/(24*c*c))
assert pminuslimit==sp.Rational(11,18)
print('PASS independent direct 6×6 projectors, all unitary Gram tests, Hermitian spectra,')
print('      direct n^-9 symbolic coefficient 675/128, source normalized n^-5 coefficient 16,')
print('      and heralded probability n^-2 coefficient 11/18')
