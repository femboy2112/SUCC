"""Replay preregistered development/holdout shells; exact finite certificates only."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

from observational_succ.leah_gamma_twist import (
    centered_path, shell_metrics, shell_antilock_interval,
)
from observational_succ.duck_bbp import forcing


def outward(x, lower, bits=32):
    z=x*(1<<bits)
    n=z.__floor__() if lower else -(-z).__floor__()
    return str(Q(n,1<<bits))


def main():
    shells=(8,16,32,64,97,193,389,769)
    path=centered_path(2*max(shells))
    rows=[]
    for B in shells:
        m=shell_metrics(path,B)
        lo,hi=shell_antilock_interval(path,B)
        delta=Q(15,4*B)+Q(225,4096*B**3)
        k=m['integer_energy']
        lower=Q(8,289*B)*(k-Q(17,4)-delta)-Q(22,7)/(32*B**2)
        upper=2*Q(22,7)**2/(225*B)*(k+Q(15,4)+delta)+Q(22,7)/(32*B**2)
        assert m['coercive_lower']<=m['innovation_energy']<=m['coercive_upper']
        assert abs(k-m['innovation_energy'])<=delta
        assert lower<=lo<=hi<=upper
        hcount=sum(abs(n*n*path.residuals[n]+Q(1,64))>=Q(1,8)
                   for n in range(B,2*B))
        rows.append({'B':B,'role':'development' if B<=64 else 'held_out',
                     'impulse_count':m['impulse_count'],'integer_energy':k,
                     'anti_lock_interval':[outward(lo,True),outward(hi,False)],
                     'current_bound':[outward(lower,True),outward(upper,False)],
                     'source_scale_separated_count_delta_1_over_8':hcount,
                     'exact_checks_passed':True})
    H=1600
    seed=-sum((forcing(j)/16**j for j in range(1,H+1)),Q())
    coherent=centered_path(2*max(shells),seed)
    assert all(a==0 for a in coherent.impulses)
    result={'baseline':'db9fb4b84672050efa79b13377f1e73364598a14',
            'scope':'exact finite rational certificates; not asymptotic evidence',
            'rows':rows,'finite_coherent_control':{'H':H,'tested_horizon':1538,
            'all_impulses_zero':True,'seed_is_original_zero':False},
            'R0':'OPEN','pi_normality':'OPEN'}
    target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('RESULTS.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
