"""Independent exact SymPy derivation: chiral oscillator and invariant observer graph.

The original linear source T, b, ell are transcribed from SUCC's verified
rank-two chiral source realization, not inferred from positive packets.
Q=sqrt(2)*T is an explicitly *normalized new oscillator*, not original T.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

Q=s.Rational
sqrt2=s.sqrt(2)
g=s.Matrix([[Q(1,2),-Q(1,2)],[Q(1,2),Q(1,2)]])
# Standard orthonormal (Re,Im) odd-sector basis. The source paper also
# displays a different *nonorthonormal* rational basis with H=[[0,1],[1/2,0]].
# Using that displayed basis as Euclidean would incorrectly claim Q is not
# orthogonal. The coordinate change is essential for a valid metric statement.
h=s.Matrix([[Q(1,2),Q(1,2)],[Q(1,2),-Q(1,2)]])
T=s.diag(g,h)
phase=sqrt2*T
J=s.diag(1,1,-1,-1)
b=s.Matrix([1,0,1,0]);ell=s.Matrix([[4,0,0,-4]])
assert s.simplify(T**8-s.eye(4))!=s.zeros(4) # it contracts
assert T**8==s.eye(4)/16
assert T**4==-J/4
assert s.simplify(phase.T*phase-s.eye(4))==s.zeros(4)
assert s.simplify(phase**8-s.eye(4))==s.zeros(4)
assert s.det(phase)==-1
assert s.simplify(phase**4+J)==s.zeros(4)
taps=[s.simplify((ell*T**n*b)[0]) for n in range(8)]
assert taps==[4,0,0,-2,-1,-1,0,0]
normalized=[s.simplify((ell*phase**n*b)[0]) for n in range(8)]
assert normalized==[4,0,0,-4*sqrt2,-4,-4*sqrt2,0,0]

A=s.Matrix([[Q(1,2),0],[Q(1,2),Q(1,2)]])
B=s.Matrix([Q(1,2),0])
# h(phase*q)=A*h(q)+B*ell(q), h(q)=G*q, using cyclic backwards input.
G=(s.eye(2)-A**8).inv()*sum((A**j*B*ell*phase**(8-j-1) for j in range(8)),s.zeros(2,4))
G=s.simplify(G)
assert s.simplify(G*phase-A*G-B*ell)==s.zeros(2,4)
root=s.simplify(G*b)
# Confirm with a completely independent direct periodic orbit solving y8=y0.
a=s.Matrix([0,0])
for v in normalized:a=A*a+B*v
root2=s.simplify((s.eye(2)-A**8).inv()*a)
assert s.simplify(root-root2)==s.zeros(2,1)
phase_mean=s.simplify(sum(normalized)/8)
assert phase_mean==-sqrt2

# One-step transfer to an observer is a unique source- and phase-indexed
# linear graph. The attractor is periodic but nonconstant, not full W recovery.
assert s.simplify(G*(phase**8)-G)==s.zeros(2,4)
assert s.simplify(G*phase-G)!=s.zeros(2,4)

out={
 'T_eight_step':'T^8=I/16',
 'Q_phase_eight_step':'(sqrt2 T)^8=I',
 'Q_phase_orthogonal': True,
 'Q_orientation_reversing': True,
 'signed_original_taps':list(map(str,taps)),
 'normalized_chiral_driver':list(map(str,normalized)),
 'normalized_chiral_driver_mean':str(phase_mean),
 'invariant_linear_graph_2x4': [[str(s.factor(z)) for z in row] for row in G.tolist()],
 'selected_seed_invariant_state':list(map(str,root)),
 'check':'G Q = A G + B ell (all 4D source states), exact',
 'status':'exact symbolic model, not pi normality or physical GR'
}
path=Path(__file__).resolve().parents[1]/'receipts'/'chiral_invariant_graph_sympy.json'
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2))
