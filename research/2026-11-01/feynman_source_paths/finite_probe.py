"""Optional finite original-source diagnostics; proof lives in PROOFS.md.
Run with python finite_probe.py. mpmath check is optional; arithmetic always exact.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import json
p=Path(__file__).with_name('feynman_source.py')
spec=importlib.util.spec_from_file_location('source_feynman_probe_20261101',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def diagnostics():
    ans={"status":"FINITE_DIAGNOSTIC_ONLY","source":"original 4 signed BBP poles; U_0=0",
         "hbar_physical_value_claimed":False,"pi_normality_claimed":False,
         "r1":str(m.source(1)),"r2":str(m.source(2)),
         "source_order_delta":str(m.two_order_offset()),
         "horizons":[]}
    for n in (1,2,4,8,16):
        e=F(1,1000);hbar=F(1);K=F(3,2)
        ans["horizons"].append({"N":n,"U_N":str(m.orbit(n)),
              "A_N":str(m.weighted_action(n)),
              "Fresnel_C_N":str(m.variance_clock(n)),
              "bandlimited_error_bound":str(m.bandlimited_error_bound(n,e,hbar,K)),
              "all_N_error_cap":str(m.uniform_bandlimited_bound(e,hbar,K))})
    return ans


def optional_gaussian_quadrature():
    try:
        import mpmath as mp
    except ImportError:
        return {"status":"NOT_RUN_mpmath_unavailable"}
    mp.mp.dps=60
    a=mp.mpf(256);sig=mp.mpf(1)/8;p0=mp.mpf(3);hbar=mp.mpf(2)
    r1=mp.mpf(47)/15;r2=mp.mpf(106)/819
    first=a/16*r1+r2
    second=a/16*r2+r1
    delta=first-second
    final_sigma=a*sig; final_p=p0/a
    normalization=(2*mp.pi*final_sigma**2)**(-mp.mpf(1)/4)
    def psi(y,center):
        return normalization*mp.exp(-(y-center)**2/(4*final_sigma**2)
                                    +1j*final_p*(y-center)/hbar)
    measured=mp.quad(lambda x:mp.conj(psi(x,second))*psi(x,first),
                [min(first,second)-40*final_sigma,max(first,second)+40*final_sigma])
    expected=mp.exp(-delta**2/(8*final_sigma**2)-1j*final_p*delta/hbar)
    return {"status":"NUMERICAL_ONLY_NOT_PROOF","precision_digits":60,
            "quad_real":mp.nstr(measured.real,50),"quad_imag":mp.nstr(measured.imag,50),
            "error_abs":mp.nstr(abs(measured-expected),12),
            "gaussian_formula_derived_independently":True}

if __name__=='__main__':
    print(json.dumps({"exact":diagnostics(),"interferometer":optional_gaussian_quadrature()},
                     sort_keys=True,indent=2))
