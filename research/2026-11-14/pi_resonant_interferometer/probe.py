"""Reproducible finite source-sensitive phase-collision report (NOT asymptotics)."""
from __future__ import annotations
from decimal import Decimal, getcontext
import json
from pathlib import Path
from observational_succ.pi_resonant_interferometer import (
    critical_lag, innovation_leading, shell_click_interval,
)

def format_fraction(f):
    getcontext().prec=28
    return str(Decimal(f.numerator)/Decimal(f.denominator))

def build_report():
    rows=[]
    for B in (4,8,16,32):
        ell=critical_lag(B)
        innovation,leading,cap=innovation_leading(B,ell)
        lo,hi=shell_click_interval(B,1,completed=True)
        rows.append({"B":B,"ell":ell,"source_innovation":format_fraction(innovation),
                     "leading":format_fraction(leading),"rigorous_error_upper":format_fraction(cap),
                     "finite_completed_pi_click_lower":format_fraction(lo),
                     "finite_completed_pi_click_upper":format_fraction(hi),
                     "claim":"FINITE CERTIFICATE; NO ASYMPTOTIC R0 CLAIM"})
    return {"source":"original BBP, U0=0", "harmonic":1,
            "resonance":"16^ell/(64B^2)~1", "finite_shells":rows,
            "pi_normality":"OPEN", "R0":"OPEN"}

if __name__=='__main__':
    doc=build_report()
    print(json.dumps(doc,sort_keys=True,indent=2))
    Path(__file__).with_name('receipts').joinpath('FINITE_SHELLS.json').write_text(json.dumps(doc,sort_keys=True,indent=2)+'\n')
