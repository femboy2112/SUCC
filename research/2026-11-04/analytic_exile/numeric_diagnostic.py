"""Optional same-source high-precision complex sanity checks, NOT proof authority."""
from __future__ import annotations
from pathlib import Path
import importlib.util

HERE=Path(__file__).resolve().parent
p=importlib.util.spec_from_file_location('analytic_exile_complex_source',HERE/'analytic_exile.py')
m=importlib.util.module_from_spec(p);p.loader.exec_module(m)


def run():
    from mpmath import mp
    mp.dps=70
    report=[]
    for A in (40,96,160):
        seq=m.modular_original_phases(2*A)
        def c(h):
            result=mp.mpc(0)
            for x in seq[A:2*A]:
                y=(h*x)%1
                result+=mp.exp(2j*mp.pi*mp.mpf(y.numerator)/mp.mpf(y.denominator))
            return result/A
        worst=mp.mpf('0')
        for h in (1,3,5):
            base=c(h)
            for j in (1,2,3):
                actual=abs(c(h*16**j)-base)
                bound=m.ward_ladder_bound(A,h,j)
                if not actual<mp.mpf(bound.numerator)/mp.mpf(bound.denominator):
                    raise AssertionError(f'Ward envelope failed at A={A},h={h},j={j}')
                worst=max(worst,actual)
        report.append((A,mp.nstr(worst,13)))
    return report

if __name__=='__main__':
    print('DIAGNOSTIC ONLY, NONCERTIFYING',run())
