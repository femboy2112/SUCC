"""Independent symbolic/congruence audit. Does not import dual_radix.py.

Model validation only: primary proofs remain in THEOREMS.md. No global
Collatz or pi normality inference.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
from itertools import product
import json
import sympy as sp

z,n=sp.symbols('z n', integer=True, positive=True)
assert sp.simplify(3*(16**n-1)/3+1-16**n)==0
assert sp.simplify(5*(16**n-1)/5+1-16**n)==0
assert sp.expand((z-3)*(z-5))==z*z-8*z+15

count={"collatz_3_5_symbols":3,"q_identity_clock":0,"two_three_five_adic":0,"valuation_suffix":0,"mirror_gauges":0,"joint_crt_digit":0,"bbp_poles":0,"two_adic_noncontinuity":0,"first_mismatch":0,"wave_mirror":0,"source_digit_shadow":0}

def valuation(v,p):
    v=abs(int(v))
    if v==0:return None
    k=0
    while v%p==0:
        k+=1;v//=p
    return k

for k in range(1,80):
    b=16**k;J=(b-1)//15
    for q,d in ((3,5),(5,3),(15,1)):
        D=d*J
        assert q*D+1==b
        assert f'{D:x}'==f'{d:x}'*k
        assert valuation(q*D+1,2)==4*k
        count['q_identity_clock']+=3
    A=5*J
    assert 3*A+1==b
    assert 3*(A+2*b)+1==7*b
    assert valuation((A+2*b)-A,2)==4*k+1
    count['two_adic_noncontinuity']+=3

for m in range(1,60):
    for k in range(m):
        jm=(16**m-1)//15
        jk=(16**k-1)//15
        for p in (3,5):
            assert valuation(jm-jk,p)==valuation(m-k,p)
            assert valuation(5*(jm-jk),p)==valuation(m-k,p)+(p==5)
            assert valuation(3*(jm-jk),p)==valuation(m-k,p)+(p==3)
            count['two_three_five_adic']+=3

for k in (1,2,3):
    mod=16**k
    root=5*(mod-1)//15
    assert (3*root+1)%mod==0
    for d in range(mod):
        assert ((3*d+1)%mod==0)==(d==root)
        count['valuation_suffix']+=1
    for a in (0,1,2,3,5,11,17):
        D=mod*a+root
        assert (3*D+1)==mod*(3*a+1)
        count['valuation_suffix']+=1

for n in range(1,31):
    radix=16**n
    for digit in (0,1,3,5,10,12,14,15):
        reg=digit*((radix-1)//15)
        mirrored=radix-1-reg
        assert mirrored==(15-digit)*((radix-1)//15)
        assert reg+mirrored==radix-1
        count['mirror_gauges']+=2

for previous in range(15):
    for digit in range(16):
        nxt=(previous+digit)%15
        candidates=[i for i in range(16) if (previous+i)%3==nxt%3 and (previous+i)%5==nxt%5 and i%2==digit%2]
        assert candidates==[digit]
        count['joint_crt_digit']+=1

for j in range(1,128):
    a=(Fraction(4,8*j-7)-Fraction(2,8*j-4)-Fraction(1,8*j-3)-Fraction(1,8*j-2))
    b=Fraction(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
    assert a==b
    count['bbp_poles']+=1

# Independently recover the original BBP 12-digit certificate.
terms=12
x0=sum((Fraction(4,8*j-7)-Fraction(2,8*j-4)-Fraction(1,8*j-3)-Fraction(1,8*j-2))/16**j for j in range(1,terms+1))
nextj=terms+1
rnext=Fraction(4,8*nextj-7)-Fraction(2,8*nextj-4)-Fraction(1,8*nextj-3)-Fraction(1,8*nextj-2)
assert int(x0*16**terms)==int((x0+rnext/(15*16**terms))*16**terms)==int('3243F6A8885A',16)
pihex='3243F6A8885A'
y_shadow=int(pihex[::-1],16)
assert y_shadow%256==0x23
assert valuation(5*y_shadow+1,2)==4
assert valuation(3*y_shadow+1,2)==1
assert ((5*y_shadow+1)//16)%16==11
count['source_digit_shadow']+=6

for q in (3,5,15):
    d=15//q
    for k in range(0,17):
        for nxt in range(16):
            if nxt==d:continue
            y=d*((16**k-1)//15)+nxt*16**k+9*16**(k+1)+7*16**(k+2)
            assert valuation(q*y+1,2)==4*k+valuation(nxt-d,2)
            count['first_mismatch']+=1

for d in range(16):
    for r in (Fraction(1,11),Fraction(2,7),Fraction(4,9)):
        x=Fraction(d,16)+r/16
        f=lambda t: t**4-Fraction(5,2)*t**2+Fraction(13,7)
        assert f(1-x)/4 == f((15-d+1-r)/16)/4
        count['wave_mirror']+=1

out={"checks":count,"total":sum(count.values()),"result":"PASS","scope":"Exact finite corroboration of elementary theorems; independent Python/SymPy derivations; no all-input Collatz or pi result","sympy":sp.__version__}
p=Path(__file__).with_name('independent_audit_receipt.json')
p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
