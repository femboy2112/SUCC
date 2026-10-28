"""Independent deterministic source/rank-r exact diagnostics (not a pi proof)."""
import json
import sys
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.pi_rank_lattice import (
    authentic_r, canceled_r, original_state, pi_source_prefix,
    finite_green_tail, green_tail_upper, flat_square,
    certified_rank_transport_bound,transverse_trace_recovery)


def main():
    pole_checks=0
    for n in range(1,151):
        assert authentic_r(n)==canceled_r(n)
        pole_checks+=1
    green_checks=0
    L=45
    PiL=pi_source_prefix(L)
    for n in range(1,L+1):
        assert (16**(n-1))*PiL-original_state(n)==finite_green_tail(n,L)
        assert 0<=finite_green_tail(n,L)<green_tail_upper(n)
        green_checks+=1
    squares=0
    for mult in [(3,),(3,5),(3,5,7)]:
        for n in range(1,15):
            for idx in product(range(3),repeat=len(mult)):
                for axis in range(len(mult)):
                    a,b=flat_square(n,idx,mult,axis)
                    assert a==b
                    squares+=1
    transport={}
    for (N,widths,bases) in [(100,(5,),(3,)),(100,(5,3),(3,5)),(100,(3,3,2),(3,5,7))]:
        bound=certified_rank_transport_bound(N,widths,bases,1)
        transport[f'N{N}-q{bases}-width{widths}']={'numerator':bound.numerator,'denominator':bound.denominator}
    avg,defect,head=transverse_trace_recovery((Q(1),Q(-1)))
    assert (avg,defect,head)==(Q(0),Q(1),Q(1))
    print(json.dumps({'status':'PASS','source_checks':pole_checks,
         'exact_green_checks':green_checks,'exact_flat_square_checks':squares,
         'certified_rank_transport_bounds':transport,
         'trace_countermodel':{'rank2_average':0,'transverse_defect':1,'rank1_slice':1},
         'authority':'finite exact rational diagnostics; no infinite normality proof'},
         indent=2,sort_keys=True))
if __name__=='__main__':main()
