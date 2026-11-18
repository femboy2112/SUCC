"""Bounded FQR arithmetic audit, not a replay of the upstream suite."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def prime(p):
    return p >= 2 and all(p%d for d in range(2, isqrt(p)+1))


# Prediction: the printed FQR-05 normalization fails its own denominator
# certificate at p=13,n=8; EPS's correct F=16*C satisfies the certificate.
p, n, j0, c = 13, 8, 7, F(7, 32)
printed_F = 8*F(2)**(4*j0-4*n)*c
correct_F = 16*c
K = (8*n-2)//p
lane_denominator_bound = 2**(K//2)  # S_odd(4,1) = {1}
assert printed_F == F(7, 64)
assert lane_denominator_bound % printed_F.denominator != 0
assert lane_denominator_bound % correct_F.denominator == 0
assert r(1) == F(47, 15)

# Prediction: the derivation of FQR-10 (equation label, within theorem07)
# must include cyclic wrap. Check exactly B=1..32 for an authentic witness.
# No witness in this finite set would not establish the unqualified formula.
u=F(0)
records=[]
wraps=[]
for h in range(1, 65):
    u=16*u+r(h)
    if h%2:
        continue
    B=h//2
    Q=u.denominator
    q=1
    for pp in range(2, max(6,isqrt(16*B))+1):
        if not prime(pp):
            continue
        qq=Q
        while qq%pp == 0:
            q*=pp
            qq//=pp
    Pi=Q//q
    radix=16**B
    length=((q-1).bit_length()+3)//4
    if length>B:
        records.append({'B':B,'top_length_negative':True})
        continue
    C=u.numerator//Q
    residue=u.numerator%Q
    rt=u.numerator%Pi
    m=(residue-rt)//Pi
    Z=(u.numerator//Pi)%radix
    X=(q*C)%radix
    H=16**length
    topmod=radix//H
    eps=((X%H)+m)//H
    assert 0<=m<q<=H
    assert eps in (0,1)
    assert (Z//H-X//H-eps)%topmod == 0
    rec={'B':B,'Q_ram':str(q),'L_ram':length,'X':str(X),'m':str(m),
         'Z':str(Z),'top_X':str(X//H),'top_Z':str(Z//H),
         'top_difference':str(Z//H-X//H),'epsilon':eps,'top_modulus':str(topmod)}
    records.append(rec)
    if Z//H-X//H not in (0,1):
        wraps.append(rec)

receipt={
 'pin':'9ff8544c799b5e4c8eb1db33127438bc3f221045',
 'scope':'two exact small witnesses and a bounded B=1..32 cyclic-wrap probe',
 'FQR01_valuation_counterexample':{'N':1,'p':47,'U':'47/15','valuation':1},
 'FQR05_printed_normalization_counterexample':{'p':13,'n':8,'j0':7,'C':str(c),
   'K':K,'printed_F':str(printed_F),'printed_F_denominator':printed_F.denominator,
   'correct_F':str(correct_F),'claimed_denominator_bound':lane_denominator_bound},
 'wrap_probe_B':[1,32],'authentic_wrap_witnesses':wraps,'all_modular_repairs_pass':True,
 'finite_no_witness_does_not_prove_original_formula':True,
 'records':records,
}
Path(__file__).with_name('minimal_arithmetic_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='records'},indent=2))
