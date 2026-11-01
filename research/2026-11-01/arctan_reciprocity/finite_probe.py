"""Original-source finite signed mirror diagnostics; independent of exact proof.

Uses exact Fraction U_n mod 1, then high-precision numerical trig.
No all-horizon normality proof and NO fixed finite sign inference.
"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("succ_arctan_local",HERE/"arctan_mirror.py")
m=importlib.util.module_from_spec(sp);sys.modules[sp.name]=m;sp.loader.exec_module(m)


def evaluate(n:int,h:int, *,dps:int=90)->dict:
    import mpmath as mp
    mp.mp.dps=dps
    q=mp.mpf(106)/819
    theta=mp.atan(q)
    gamma=(mp.mpc(819,106)/mp.mpc(819,-106))
    phi=[mp.mpf(x.numerator)/x.denominator for x in m.rational_orbit(n)]
    ah=sum((mp.exp(2j*mp.pi*h*x) for x in phi),mp.mpc(0))/n
    a16=sum((mp.exp(2j*mp.pi*16*h*x) for x in phi),mp.mpc(0))/n
    bh=sum((mp.sin(2*mp.pi*h*x-h*theta) for x in phi),mp.mpf(0))/n
    b16=sum((mp.sin(2*mp.pi*16*h*x-16*h*theta) for x in phi),mp.mpf(0))/n
    dh=ah-gamma**h*mp.conj(ah)
    d16=a16-gamma**(16*h)*mp.conj(a16)
    mirror_denom=abs(mp.sin(15*h*theta))
    exact_sq=m.mirror_sine_squared(h)
    source_bound=m.radix_discrepancy_bound(n,h)
    er=mp.mpf(source_bound.numerator)/source_bound.denominator
    predicted=(abs(bh)+abs(b16)+er)/mirror_denom
    def fmt(x):return mp.nstr(x,28)
    ok=bool(abs(ah)<=predicted and abs(a16-ah)<er and
            abs(mirror_denom**2-mp.mpf(exact_sq.numerator)/exact_sq.denominator)<mp.mpf('1e-75'))
    return {"N":n,"h":h,"actual_weyl_mean_abs":fmt(abs(ah)),
            "source_mirror_sine_h":fmt(bh),"source_mirror_sine_16h":fmt(b16),
            "exact_mirror_denominator_squared":str(exact_sq) if h<=2 else "EXACT_RATIONAL_AVAILABLE_IN_CODE",
            "mirror_denominator":fmt(mirror_denom),"actual_radix_defect":fmt(abs(a16-ah)),
            "certified_rational_radix_upper":str(source_bound),
            "conditional_weyl_upper":fmt(predicted),
            "complex_reflection_defect_h":fmt(abs(dh)),
            "complex_reflection_defect_16h":fmt(abs(d16)),
            "finite_inequality_valid_diagnostic":ok}


def run():
    # Predetermined small calibration and larger finite check points. No postselection.
    ns=(32,64,128,256)
    harmonics=(1,3,5,7)
    cases=[evaluate(n,h) for n in ns for h in harmonics]
    if not all(v["finite_inequality_valid_diagnostic"] for v in cases):
        raise ArithmeticError("finite inequality diagnostic failed")
    result={"claim":"FINITE_NUMERICAL_DIAGNOSTICS_ONLY",
            "normality_proved":False,"mpmath_precision_decimal_digits":90,
            "source":"original four signed BBP poles and literal U0=0",
            "mirror":"q=r(2)=106/819, gamma=(659525+173628i)/681997",
            "tested_N":ns,"tested_harmonics":harmonics,"cases":cases}
    dest=HERE/"FINITE_DIAGNOSTICS.json"
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("ARCTAN_MIRROR_FINITE_DIAGNOSTICS_PASS",len(cases),"cases")
    for c in cases:
        print(c["N"],c["h"],c["actual_weyl_mean_abs"][:12],c["conditional_weyl_upper"][:12])

if __name__=='__main__':run()
