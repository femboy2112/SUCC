"""Exploratory, PRESEEN signed prime/complement time-spectrum diagnostics."""
from __future__ import annotations
import cmath, json, math
from pathlib import Path
from observational_succ.laplace_critical_source import lifted_phases,p_fractional_part,signed_overlap_certificate


def calculate():
    rows=[]
    for A,p in ((32,73),(80,193),(192,457),(320,769)):
        x=lifted_phases(2*A)
        a=tuple(cmath.exp(2j*math.pi*float(p_fractional_part(x[n],p))) for n in range(A,2*A))
        b=tuple(cmath.exp(2j*math.pi*float((x[n]-p_fractional_part(x[n],p))%1)) for n in range(A,2*A))
        v=signed_overlap_certificate(a,b,8,0.)
        w=sum((a[i]*b[i] for i in range(A)),0j)/A
        assert abs(w-v['signed_total'])<1e-10
        rows.append({'A':A,'prime_p':p,'frequency_h':1,'cutoff_K':8,'tau':0,
                     'abs_W':round(abs(w),12),'abs_prime_mean':round(abs(sum(a)/A),12),
                     'high_complement_power':round(v['high_upper']**2,12),
                     'abs_signed_high_overlap':round(abs(v['signed_high']),12),
                     'low_bound':round(v['low_upper'],12),
                     'status':'PRESEEN / DOUBLE FLOAT DIAGNOSTIC; NOT A CERTIFICATE'})
    return {'schema':'SUCC-LAPLACE-SPECTRUM-01','rows':rows,'p_selection':'finite examples; no asymptotic onset','scope':'preseen exploratory only'}


def main():
    p=Path(__file__).with_name('SPECTRAL_DIAGNOSTICS.json')
    payload=json.dumps(calculate(),sort_keys=True,indent=2)+'\n'
    import sys
    if '--verify' in sys.argv:
        assert p.read_text()==payload
        print('PASS exploratory spectral payload replay')
    else:
        p.write_text(payload)
        print('wrote',p)

if __name__=='__main__':main()
