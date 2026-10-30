"""Independent 70-digit quadrature of source-locked gamma-rank extrusion jets."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=68
L=(mp.sqrt(5)-1)/2

def tail_q(Z,A):
    x=Z/A
    return -2*mp.expm1(-3*x)-mp.expm1(-4*x)-mp.expm1(-5*x)

def compute(n,m,j,mutant=False):
    A=8*(n+m-j)-7
    r=j+2
    def part(y):
        return mp.exp(-y)*(15*y/A if mutant else tail_q(y,A))*(-mp.expm1(-8*y/A))**j
    z=mp.quad(lambda y:part(y),[0,6,20,60,mp.inf])
    f=lambda y: mp.log(y)-mp.exp(-L*y)
    ob=mp.quad(lambda y:part(y)*f(y),[0,6,20,60,mp.inf])/z
    limit=mp.digamma(r)-L**r
    cj=4*j if mutant else mp.mpf(59)/30+4*j
    target=-cj*(1+r*L**(r+2))
    return {"n":n,"m":m,"j":j,"A":A,"mutant":mutant,
            "observed_scaled_correction":mp.nstr(A*(ob-limit),35),
            "predicted_coefficient":mp.nstr(target,35),
            "difference":mp.nstr(A*(ob-limit)-target,25)}

if __name__=='__main__':
    points=[(12,12,0),(40,40,0),(100,100,0),(20,20,1),(60,60,1),(180,180,1),(30,30,3),(80,80,3)]
    out=[compute(*p) for p in points]
    out.extend([compute(50,50,1,True),compute(160,160,1,True)])
    for o in out:
        print(f"{o['n']:>3} j={o['j']} mutant={o['mutant']} A={o['A']} actual={o['observed_scaled_correction']} target={o['predicted_coefficient']} err={o['difference']}")
    Path(__file__).with_name('oracle.json').write_text(json.dumps(out,indent=2)+'\n')