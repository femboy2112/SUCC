"""Pre-registered finite Gamma-Haar **aggregate** holdouts.

Run from repository checkout. Each PASS uses exact Fraction comparison after
the inherited Machin/Taylor/Gamma total-ℓ¹ error bound, never float verdicts.
This is NOT an all-horizon asymptotic certificate.
"""
import sys,json
from pathlib import Path
from fractions import Fraction
BASE=Path(__file__).resolve().parents[1]/'gamma_haar_window'
sys.path.insert(0,str(BASE))
from finite_certificate import phase_packet,level_packet

CASES={512:(1,5,11),1024:(1,5,11)}
LEVELS={512:(16,32,64),1024:(32,64,128)}
DELTA=Fraction(1,10)

def execute():
    results=[]
    for M,modes in CASES.items():
        for h in modes:
            z,eta=phase_packet(h,M)
            row={'N':M,'h':h,'eta_upper_float_for_display':float(eta),'levels':[]}
            for L in LEVELS[M]:
                E,W,P=level_packet(z,L)
                Ee=2*L*eta+eta**2
                We=4*L*eta+eta**2
                margin=W-We-DELTA*(E+Ee)
                ambiguous=margin<=0 and W+We-DELTA*(E-Ee)>=0
                row['levels'].append({
                    'L':L,'delta':str(DELTA),'pass':margin>0,
                    'ambiguous':ambiguous,
                    'ratio_approx':float(W/E) if E else None,
                    'certificate_margin_lower_float':float(margin),
                    'energy_approx':float(E),
                    'signed_energy_approx':float(W)})
            results.append(row)
            print(f'N={M},h={h}: '+', '.join(
                f"L={x['L']}:{'PASS' if x['pass'] else 'AMBIG' if x['ambiguous'] else 'FAIL'}"
                for x in row['levels']),flush=True)
    p=Path(__file__).with_name('FINITE_HOLDOUTS.json')
    p.write_text(json.dumps({
        'status':'finite rational signed comparisons; no asymptotic proof',
        'preregistration':'PREREGISTRATION.md','results':results
        },indent=2)+'\n')
    return results

if __name__=='__main__':
    execute()
