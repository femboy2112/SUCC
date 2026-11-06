"""Source-preregistered active shell observer, not a source-normality proof.

Candidate selection only uses source windows. Actual source history is read
AFTER selecting (m,k). Individual forecasts are not independent over time.
"""
import math
from fractions import Fraction as Q
try:
    from history_shell_probe import block, original_epoch
except ImportError:
    import sys
    from pathlib import Path
    sys.path.insert(0,str(Path(__file__).resolve().parent))
    from history_shell_probe import block, original_epoch

def binary_entropy(d):
    p=float(Q(d))
    return 0.0 if p in (0.0,1.0) else -p*math.log2(p)-(1-p)*math.log2(1-p)

def source_only_candidates(A,d,ks=(1,2,3)):
    out=[]
    for k in ks:
        m=d-k
        if m<1:continue
        raw=[16**m*block(n,k) for n in range(A,2*A)]
        if not all(Q(0)<q<Q(1) for q in raw):continue
        H=sum(binary_entropy(delta) for delta in raw)/A
        out.append((H,-k,m,k,raw))
    assert out,'no source-admissible binary candidate'
    out.sort(reverse=True,key=lambda z:(z[0],z[1]))
    return out

def choose_then_observe(A,d):
    options=source_only_candidates(A,d)
    H,negk,m,k,deltas=options[0]
    # Observation gate: the chosen m,k are fixed BEFORE this call reads U_n.
    actual=original_epoch(A,m,k)
    assert [z['source_fraction'] for z in actual['items']]==deltas
    expected=sum(deltas,Q())
    selected=sum(x['selected_bit'] for x in actual['items'])
    selected_brier=sum(((x['selected_bit']-x['source_fraction'])**2
                        for x in actual['items']),Q())/A
    coherent_brier=sum((q*q for q in deltas),Q())/A
    reference_brier=sum((q*(1-q) for q in deltas),Q())/A
    coherent_certified=16**d<(8*A+1)*(8*A+2)
    return dict(A=A,depth=d,m=m,k=k,entropy_bits=H,
                runner_up_entropy=options[1][0],selected=selected,
                expected=expected,selected_innovation=(Q(selected)-expected)/A,
                brier_selected=selected_brier,brier_coherent=coherent_brier,
                brier_reference=reference_brier,coherent_certified=coherent_certified,
                n_options=len(options))

def main():
    for A,d in ((211,5),(419,5),(829,6)):
        p=choose_then_observe(A,d)
        print('POLICY',A,'d',d,'chosen m/k',p['m'],p['k'],
              'entropy bits',round(p['entropy_bits'],9),
              'runner up',round(p['runner_up_entropy'],9),
              'branch count',p['selected'],'forecast',round(float(p['expected']),7),
              'innovation',round(float(p['selected_innovation']),9),
              'selected Brier',round(float(p['brier_selected']),9),
              'coherent Brier',round(float(p['brier_coherent']),9),
              'reference Brier',round(float(p['brier_reference']),9),
              'coherent certified',p['coherent_certified'])
    print('HISTORY_FIRST_POLICY_PASS')
if __name__=='__main__':main()
