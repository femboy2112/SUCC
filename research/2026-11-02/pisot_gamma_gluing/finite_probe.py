"""Finite exact rational/regulator diagnostics. Not a π-normality probe."""
import importlib.util
from pathlib import Path
from fractions import Fraction

spec=importlib.util.spec_from_file_location(
    "pg_finite",Path(__file__).with_name("pell_gamma.py"))
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def produce():
    rows=[]
    for a in (10,64,100,256,512,1024,4096):
        k=g.regulator_integer_scale(a)
        n=a+1
        b=n+31
        P,Q=g.pell(k)
        e=g.phase_error_rational_upper(n,b,k)
        assert e>0
        assert e < Fraction(1,a)
        assert g.signed_sheet_coefficient(k)==(1,0)
        assert g.signed_sheet_coefficient(k,True)==(1,0)
        assert g.exact_seam_verify(n,b,b+1)
        rows.append({
            "a":a,"n":n,"cutoff":b,"pell_level":k,
            "P_k":P,"Q_k":Q,"trace_integer_harmonic":2*P,
            "strict_rational_upper_for_abs_exponent_error_approx":float(e),
            "rational_comparison_error_lt_1/a":True
        })
    return rows


if __name__=="__main__":
    import json
    print(json.dumps({
        "status":"FINITE diagnostics only. All sign/cutoff comparisons exact rational and Qsqrt2.",
        "rows":produce()
    },indent=2))
