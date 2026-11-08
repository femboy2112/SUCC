"""Independent interval direct-DFT and exact rational dual-bound checks."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(BASE))
from certified_fft import PrimeDFT, SCALE


def dual_checks():
    rng=random.Random(20261108)
    n=8
    atoms=[[1 if (r&k).bit_count()%2==0 else -1 for r in range(n)] for k in range(1,n)]
    assert all(sum(atom)==0 for atom in atoms)
    count=0
    for _ in range(240):
        B=[F(rng.randrange(-2,3),2) for _ in range(n)]
        E=sum(x*x for x in B)/n
        W=sum(B)/n
        w=F(1,4)
        M=max(abs(sum(F(x)*y for x,y in zip(atom,B))/n)/w for atom in atoms)
        lower=(E-W*W)/(max(F(1),M)+abs(W))
        R=F(rng.randrange(-6,7),3)
        coefficients=[F(rng.randrange(-4,5),5) for _ in atoms]
        V=[R+sum(c*atom[r] for c,atom in zip(coefficients,atoms)) for r in range(n)]
        rho=sum(abs(b-v) for b,v in zip(B,V))/n
        K=w*sum(abs(c) for c in coefficients)
        assert rho+K>=lower
        count+=1
    return count


def fft_checks():
    from mpmath.ctx_iv import MPIntervalContext
    from mpmath.libmp import to_rational
    iv=MPIntervalContext();iv.dps=65
    count=0; sign_failures=0; scale_failures=0; rows=[]
    for p in (3,7,13,17,25):
        centers=[((j*j-7*j+3)*SCALE//11,(2*j*j+3*j-8)*SCALE//17) for j in range(p)]
        # Exact perturbations with complex L1 size2/SCALE; bound supplied is3.
        actual=[(x+(-1)**j,y+(-1)**(j//2)) for j,(x,y) in enumerate(centers)]
        out,rad=PrimeDFT(p).transform(centers,3)
        largest=F()
        for k,(cx,cy) in enumerate(out):
            real,imag=iv.mpf(0),iv.mpf(0)
            wrongreal,wrongimag=iv.mpf(0),iv.mpf(0)
            for j,(x,y) in enumerate(actual):
                angle=-2*iv.pi*j*k/p
                c,s=iv.cos(angle),iv.sin(angle)
                real+=(iv.mpf(x)*c-iv.mpf(y)*s)/SCALE
                imag+=(iv.mpf(x)*s+iv.mpf(y)*c)/SCALE
                wrongreal+=(iv.mpf(x)*c+iv.mpf(y)*s)/SCALE
                wrongimag+=(-iv.mpf(x)*s+iv.mpf(y)*c)/SCALE
            err=abs(real-iv.mpf(cx)/SCALE)+abs(imag-iv.mpf(cy)/SCALE)
            upper=F(*to_rational(err._mpi_[1]))
            assert upper<=F(rad,SCALE)
            largest=max(largest,upper/F(rad,SCALE))
            wrong=abs(wrongreal-iv.mpf(cx)/SCALE)+abs(wrongimag-iv.mpf(cy)/SCALE)
            sign_failures+=F(*to_rational(wrong._mpi_[0]))>F(rad,SCALE)
            scaled=abs(real-iv.mpf(2*cx)/SCALE)+abs(imag-iv.mpf(2*cy)/SCALE)
            scale_failures+=F(*to_rational(scaled._mpi_[0]))>F(rad,SCALE)
            count+=1
        rows.append({"length":p,"radius_integer":rad,"largest_certified_radius_fraction":float(largest)})
    assert sign_failures>0 and scale_failures>0
    return {"independent_interval_DFT_outputs":count,"rows":rows,
            "wrong_sign_rejections":sign_failures,"wrong_scaling_rejections":scale_failures,
            "method":"mpmath interval direct sums, independent of inherited Taylor/Machin FFT phase engine",
            "precision_decimal_digits":65}


def run():
    payload={"exact_rational_CB1_checks":dual_checks(),"fft":fft_checks(),
             "scope":"finite independent checks and separately recorded paper review, not global certification"}
    dependencies=[BASE/'THEOREMS.md',BASE/'certified_fft.py',BASE/'resonance/THEOREMS.md',BASE/'model/THEOREMS.md',HERE/'THEOREMS.md',Path(__file__)]
    payload['reviewed_hashes']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies}
    return payload


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    encoded=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(encoded)
    else:print(encoded,end='')
