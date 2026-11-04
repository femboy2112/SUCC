"""Exact finite Fourier controls for moving Pell-frame weak-Haar illusion.

Positive non-Haar circle density f(x)=1+cos(2pi x), whose only
nontrivial Fourier coefficients are 1/2 at +/-1. No floating point.
This is a UNIVERSAL probe firewall, NOT an original ×16 invariant measure.
"""
import importlib.util
from pathlib import Path
from fractions import Fraction

spec=importlib.util.spec_from_file_location(
    "pg_moving_frame",Path(__file__).with_name("pell_gamma.py"))
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def source_fourier(m):
    return Fraction(1) if m==0 else Fraction(1,2) if abs(m)==1 else Fraction()


def pushed_fourier(k,a,b):
    P=g.pell(k)[0]
    Pnext=g.pell(k+1)[0]
    return source_fourier(a*P+b*Pnext)


def fixed_mode_replay(radius=5,search_limit=75):
    examples=[]
    for a in range(-radius,radius+1):
        for b in range(-radius,radius+1):
            if (a,b)==(0,0):
                continue
            first=None
            for k in range(1,search_limit):
                if all(pushed_fourier(j,a,b)==0 for j in range(k,search_limit)):
                    first=k
                    break
            assert first is not None
            examples.append((a,b,first))
    return examples


def moving_dual_replay():
    rows=[]
    for k in (2,5,10,20,40):
        u,v=g.bezout(k)
        assert pushed_fourier(k,u,v)==Fraction(1,2)
        rows.append(dict(k=k,u=u,v=v,hidden_marginal="1/2"))
    return rows


if __name__=="__main__":
    import json
    print(json.dumps({
        "scope":"finite check of universal classical Fourier theorem, not BBP source normality",
        "fixed_test_modes_eventually_zero":len(fixed_mode_replay()),
        "moving_dual_modes":moving_dual_replay()},indent=2))
