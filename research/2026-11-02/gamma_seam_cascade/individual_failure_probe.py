"""Finite exact rational refutation of a 0.1 PER-NODE loss threshold.

Does not refute smaller eventual δ or π normality. Arithmetic verdicts
are strict rational comparisons including all analytic approximation errors.
"""
from fractions import Fraction
from pathlib import Path
import sys,json
BASE=Path(__file__).resolve().parents[1]/'gamma_haar_window'
sys.path.insert(0,str(BASE))
from finite_certificate import phase_packet,sq,vecsum

def run():
    cases=((512,1,16,321),(1024,5,32,577),(256,5,128,1))
    out=[]
    for N,h,L,start in cases:
        z,eta=phase_packet(h,N)
        off=start-1
        a=vecsum(z[off:off+L])
        b=vecsum(z[off+L:off+2*L])
        E=sq(a)+sq(b)
        W=sq((a[0]-b[0],a[1]-b[1]))
        Ee=2*L*eta+eta**2
        We=4*L*eta+eta**2
        margin=Fraction(1,10)*(E-Ee)-(W+We)
        entry={'N':N,'h':h,'L':L,'start':start,'threshold':'1/10',
            'rigorously_disproves_threshold_at_finite_node':margin>0,
            'ratio_approx':float(W/E),
            'strict_certificate_rejection_margin_approx':float(margin),
            'total_l1_phase_error_approx':float(eta)}
        out.append(entry)
        print(entry,flush=True)
    Path(__file__).with_name('INDIVIDUAL_FAILURES.json').write_text(
        json.dumps(out,indent=2)+'\n')
    return out

if __name__=='__main__':
    run()
