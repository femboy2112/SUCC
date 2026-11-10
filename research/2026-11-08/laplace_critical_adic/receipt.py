"""Preregistered finite critical source-only Laplace diagnostics (NOT asymptotic proof).

Reads authentic source via canonical duck_bbp API; independent four-pole oracle
in this script uses exact Fraction algebra and 60-digit mpmath complex phases.
Float displays are not interval-certified; complete truncation bound is analytic.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from observational_succ.duck_bbp import forcing
from observational_succ.laplace_critical_source import source_twist,source_twist_tail_bound


def explicit_four_poles(n: int) -> Fraction:
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def one(A: int, num: int, den: int) -> dict:
    t=Fraction(1,A)
    h=round(num*A*A/den)
    N=18*A
    assert num*A*A%den==0, 'use exact registered integer h'
    assert h>0
    with mp.workdps(60):
        tau=mp.mpf(1)/A
        z=mp.exp(-tau)
        total=mp.mpc(0)
        for n in range(N):
            r=explicit_four_poles(n+1)
            assert r==forcing(n+1)
            phase=(h*r)%1
            arg=2*mp.pi*(mp.mpf(phase.numerator)/phase.denominator)
            total += tau*mp.power(z,n)*(mp.exp(mp.j*arg)-1)
        fast=source_twist(float(t),h,N)
        val=complex(float(mp.re(total)),float(mp.im(total)))
        err=abs(val-fast)
        tail=source_twist_tail_bound(1./A,N)
        assert err<2e-10,(A,num,den,err)
        return {'A':A,'lambda':f'{num}/{den}','h':h,'terms':N,
                'real_mp60':mp.nstr(mp.re(total),25),
                'imag_mp60':mp.nstr(mp.im(total),25),
                'float_independent_difference':f'{err:.6e}',
                'omitted_abs_tail_upper':f'{tail:.12e}',
                'status':'finite diagnostic only'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',action='store_true')
    o=ap.parse_args()
    p=Path(__file__).with_name('FINITE_RECEIPT.json')
    out={'schema':'SUCC-LAPLACE-CRITICAL-01',
         'parent_pr':558,'source_sha':'34cb7b64f6975e05586ec220a4655961a8e7b636',
         'scope':'finite source-only critical h=lambda*A^2; no pi normality claim',
         'rows':[one(A,n,d) for A in (160,320,640) for n,d in ((1,64),(1,8),(1,1))]}
    payload=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if o.verify:
        assert p.read_text()==payload,'finite receipt mismatch'
        print('PASS exact source checks, MP60 independent oracle, receipt identical')
    else:
        p.write_text(payload)
        print('wrote',p,'rows',len(out['rows']))

if __name__=='__main__':main()
