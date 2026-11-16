"""Independent closed-form two-bit gauge-quotient oracle; no imports from source module.

The source is (s,r), simultaneous-bit-flip is declared gauge, T flips s,
and emits the old XOR parity with correct probability 3/4. Computes the
observed quotient by analytic equations rather than executing source J.
"""
from fractions import Fraction as F
from itertools import product

# r is low bit; s is high bit. 0/3 have XOR=0, 1/2 have XOR=1.
counts=0
for ws in product(range(5),repeat=4):
    if sum(ws)==0:continue
    total=sum(ws)
    b0=F(ws[0]+ws[3],total)
    b1=F(ws[1]+ws[2],total)
    assert b0+b1==1
    for outcome in (0,1):
        # Read q_before, flip s => q_after=1-q_before.
        likelihood_before=(F(3,4) if outcome==0 else F(1,4),
                           F(3,4) if outcome==1 else F(1,4))
        Z=b0*likelihood_before[0]+b1*likelihood_before[1]
        predicted_after=(b1*likelihood_before[1]/Z,b0*likelihood_before[0]/Z)
        # Independently enumerate each source (s,r) and its deterministic successor.
        numerator=[F(0),F(0)]
        for x,w in enumerate(ws):
            src_parity=(x>>1)^(x&1)
            nxt_parity=1-src_parity
            likelihood=F(3,4) if src_parity==outcome else F(1,4)
            numerator[nxt_parity]+=F(w,total)*likelihood
        assert sum(numerator)==Z
        assert tuple(z/Z for z in numerator)==predicted_after
        counts+=1
print(f'INDEPENDENT ORACLE PASS: {counts} rational outcome/posterior comparisons')
