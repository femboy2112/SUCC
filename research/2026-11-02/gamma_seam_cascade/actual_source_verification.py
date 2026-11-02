"""Direct original rational U_n check, distinct from completed pi-orbit packet.

Post-hoc SOURCE-FIDELITY replication of the already preregistered N,h,L.
All verdicts use exact Fraction + inherited rational trig error enclosures.
This is finite only, not blinded independent trigonometry or an asymptotic theorem.
"""
from pathlib import Path
from fractions import Fraction
import sys,json
BASE=Path(__file__).resolve().parents[1]/'gamma_haar_window'
sys.path.insert(0,str(BASE))
from gamma_haar import original_states, source_independent_polynomial
from finite_certificate import rational_trig_approx,level_packet

H={512:(1,5,11),1024:(1,5,11)}
S={512:(16,32,64),1024:(32,64,128)}

def run():
    out=[]
    for N,hs in H.items():
        u=original_states(N)  # literal U_0=0, full 4-pole rational recurrence
        v=Fraction()
        for i,orig in enumerate(u,1):
            v=16*v+source_independent_polynomial(i)
            assert v==orig
        for h in hs:
            z=[];eps0=Fraction()
            for t in u:
                a,b,eps=rational_trig_approx((h*t)%1)
                z.append((a,b))
                eps0=max(eps0,eps)
            eta=N*eps0
            row={'N':N,'h':h,'eta_total_upper_display':float(eta),'levels':[]}
            for L in S[N]:
                E,W,_=level_packet(z,L)
                ee=2*L*eta+eta**2
                we=4*L*eta+eta**2
                margin=W-we-Fraction(1,10)*(E+ee)
                row['levels'].append({'L':L,'source_U_0_zero_pass':margin>0,
                     'ratio_approx':float(W/E),
                     'margin_lower_display':float(margin)})
            out.append(row)
            print('Actual U:',N,h,[(d['L'],d['source_U_0_zero_pass'])
                  for d in row['levels']],flush=True)
    path=Path(__file__).with_name('ACTUAL_U_HOLDOUTS.json')
    path.write_text(json.dumps({
        'description':'literal rational original U_n, no completed pi-orbit phase input',
        'status':'FINITE source verification, non-blind, no all-horizon proof',
        'results':out},indent=2)+'\n')
    return out

if __name__=='__main__':
    run()
