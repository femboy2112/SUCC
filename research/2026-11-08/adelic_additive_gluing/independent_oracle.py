"""Independent four-fraction / 110dps check for preregistered finite diagnostics.

This is an auxiliary replay (NO global pi normality inference). Uses a local
independent signed-pole source engine, not the library's combined polynomial.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

HERE=Path(__file__).resolve().parent

def pole(n):
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def orbit(N):
    x=Fraction(0);z=[x]
    for n in range(1,N+1):
        x=16*x+pole(n);z.append(x)
    return z


def ph(x,h):
    r=(h*x)%1
    return mp.exp(2j*mp.pi*mp.mpf(r.numerator)/r.denominator)


def seed(A):
    N=2*A+10;M=8*A+80
    s=sum((pole(j)/16**j for j in range(1,N+1)),Fraction())
    a=s*2**M
    return -Fraction(a.numerator//a.denominator,2**M)


def run():
    mp.mp.dps=110
    frozen=json.loads((HERE/'FINITE_DIAGNOSTICS.json').read_text())
    lines=[]
    for case in frozen['holdouts']:
        A=case['A']; states=orbit(2*A-1); wrong=seed(A)
        for sh, vals in case['h'].items():
            h=int(sh)
            val=sum((ph(states[n],h) for n in range(A,2*A)))/A
            err=max(abs(mp.re(val)-vals['zero_weyl'][0]),abs(mp.im(val)-vals['zero_weyl'][1]))
            valwrong=sum((ph(states[n]+16**n*wrong,h) for n in range(A,2*A)))/A
            errwrong=max(abs(mp.re(valwrong)-vals['dyadic_coherent_counterseed_weyl'][0]),abs(mp.im(valwrong)-vals['dyadic_coherent_counterseed_weyl'][1]))
            if err>mp.mpf('2e-15') or errwrong>mp.mpf('2e-15'):
                raise AssertionError(('110 digit independent numeric replay mismatch',A,h,err,errwrong))
            lines.append(f'A={A} h={h} independently rebuilt four signed poles; numeric display tolerance 2e-15 PASS; actual error original {mp.nstr(err,8)}; control {mp.nstr(errwrong,8)}')
    report='\n'.join(lines)+'\nALL 4 REGISTERED CASES PASS, 110dps, independent four signed poles (non-certifying finite diagnostics).\n'
    (HERE/'INDEPENDENT_ORACLE_LOG.txt').write_text(report)
    print(report)

if __name__=='__main__':
    run()
