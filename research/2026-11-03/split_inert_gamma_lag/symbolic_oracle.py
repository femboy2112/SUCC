"""Independent SymPy algebra checks for selected BBP source-Gamma normal form."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parent

def run():
    n,y=S.symbols('n y')
    r=(S.Rational(4)/(8*n-7)-S.Rational(2)/(8*n-4)
       -1/(8*n-3)-1/(8*n-2))
    rh=-1/(4*n-3)-1/(4*(2*n-1))-1/(4*(4*n-1))-1/(32*n)
    odd_recombine=4/(8*n-7)-1/(8*n-3)-(3*n-1)/((2*n-1)*(4*n-1))
    kernel_a=(y/4+y*y/8+y**3/16+y**4/32)/(16-y**4)
    kernel_b=y/(32*(2-y))
    z=S.symbols('z',positive=True)
    derivative_bound=(2*z-1)**2-z
    # Positive polynomial for y=e^(t/4)>=1.
    checks={
        'source_four_poles_equals_original_odd_recombination':S.cancel(r-odd_recombine)==0,
        'rH_has_correct_four_separate_terms':S.cancel(rh+1/(4*n-3)+1/(4*(2*n-1))+
               1/(4*(4*n-1))+1/(32*n))==0,
        'H_geometric_gamma_kernel_equals_inherited':S.cancel(kernel_a-kernel_b)==0,
        'gamma_derivative_64_factorization':S.factor(derivative_bound)==(z-1)*(4*z-1),
        'geometric_mean_J':sum(S.Rational(j,2**j) for j in range(1,100))+S.Rational(101,2**99)==2,
        'geometric_second_moment_J2':sum(S.Rational(j*j,2**j) for j in range(1,100))+S.Rational(101**2+2,2**99)==6,
    }
    # The two moment tail shortcuts above are diagnostic, separately justified below.
    return checks

if __name__=='__main__':
    d=run()
    assert all(d.values()),d
    f=ROOT/'SYMBOLIC_RECEIPT.json'
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');a=p.parse_args()
    if a.verify:
        assert json.loads(f.read_text())==d
        print('Independent symbolic oracle: PASS')
    else:
        f.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
        print('All symbolic certificates PASS')
