"""Deliberately different Fraction forward-vs-modular computations; no bridge.py import."""
from __future__ import annotations
from fractions import Fraction
import json

def pole(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def modq(q,k):
    M=1<<k
    return (q.numerator*pow(q.denominator,-1,M))%M

def direct_unwrapped(upto):
    U=Fraction(0); arr=[U]
    for j in range(1,upto+1):
        U=U*16+pole(j)
        arr.append(U)
    return arr

def run():
    U=direct_unwrapped(2240)
    witnesses=[]
    for k in (9,10,11):
        Q=1<<k;found=None
        for n in range(128,192):
            a=U[n]%1;b=U[n+Q]%1
            d=(a-b)%1;gap=min(d,1-d)
            if gap>=Fraction(1,4):
                assert modq(U[n],k)==modq(U[n+Q],k)
                assert modq(a,k)!=modq(b,k)
                found={'k':k,'n':n,'Q':Q,'dist':round(float(gap),12),
                       'real_frac_residues':[modq(a,k),modq(b,k)]}
                break
        assert found is not None
        witnesses.append(found)
    nums=[]
    for n in (73,149,293,587):
        f=U[n]%1;k=f.denominator.bit_length();mod=1<<k
        # Perform the reconstruction without the bridge module:
        v=modq(U[n],k);c=U[n].numerator//U[n].denominator
        a=f.denominator*((v-c)%mod)%mod
        assert Fraction(a,f.denominator)==f
        nums.append({'n':n,'denominator_bits':k,'carry_bits':c.bit_length(),
                     'numerator_bits':a.bit_length()})
    # The two self-consistent expressions for BBP are identical at all 200 points.
    assert all(pole(n)==Fraction(120*n*n-89*n+16,
                  (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)) for n in range(1,201))
    return {'status':'PASS','source_cases':200,'fresh_witnesses':witnesses,
            'rational_reconstruction':nums,'note':'exact Fraction identities; displayed floats not certified error bounds'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
