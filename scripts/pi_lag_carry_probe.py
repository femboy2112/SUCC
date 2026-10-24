"""Exact lag, prefix and multi-clock receipts for one frozen candidate."""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_lag_carry import (
    bbp_carry_path, lag_close_counts, lag_step, close_run_interval,
    nonpositive_escape_bound,
)
from observational_succ.pi_carry_prefix_control import carry_prefix_control
from observational_succ.pi_prime_clock_conditioning import common_prime_window, conditional_cell_counts
from observational_succ.pi_source_collision import small_ball_pairs


def receipt():
    lags = []
    for p in (17, 97, 2081):
        u = (p-1)//8
        path = bbp_carry_path(4*u)
        result = lag_close_counts(path, u+1, 3*u, Q(1,16))
        independent = small_ball_pairs(path.states[u+1:], Q(1,16))
        assert result.ordered_pairs == independent
        lags.append({'prime':p,'cells':16,'canonical_scale':p>=1024,
                     'per_lag_visits':list(result.per_lag),'ordered_pairs':independent})
    boundary = lag_step(bbp_carry_path(1305),1174,130)
    assert abs(boundary.centered)<=Q(1,32) and abs(boundary.centered_next)<=Q(1,32)
    assert boundary.centered_carry==0 and boundary.source_carry_difference==15
    runs = []
    for n, lag in ((10,1),(100,3),(1000,300)):
        k = next(k for k in range(1,30) if nonpositive_escape_bound(n,lag,k,Q(1,256)))
        lo,hi = close_run_interval(n,lag,k,Q(1,256))
        assert lo>0 and hi-lo==Q(2,256*16**k)
        runs.append({'index':n,'lag':lag,'steps':k,'radius':'1/256',
                     'lower':str(lo),'upper':str(hi),'diagnostic':True})
    control = carry_prefix_control(261,1040,16,28,17**2*41)
    assert small_ball_pairs(control.phases,Q(1,16))==780**2
    clocks=[]
    for primes in ((73,97),(193,241)):
        w=common_prime_window(primes)
        clocks.append({'primes':list(primes),'start':w.start,'stop':w.stop,
                       'orders':list(w.orders),'joint_period':w.period,
                       'fiber_sizes':list(map(len,w.fibers())),
                       'conditional_cell_counts_M16':conditional_cell_counts(w,16),
                       'diagnostic_resolution':True})
    files=['observational_succ/pi_lag_carry.py','observational_succ/pi_carry_prefix_control.py',
           'observational_succ/pi_prime_clock_conditioning.py','scripts/pi_lag_carry_probe.py',
           'tests/test_pi_lag_carry.py','tests/test_pi_carry_prefix_control.py',
           'tests/test_pi_prime_clock_conditioning.py']
    return {'schema':'SUCC-PI-LAG-CARRY-1','status':'EXACT_FINITE',
            'lag_counts':lags,'directional_escape':runs,'joint_clocks':clocks,
            'authentic_boundary_carry':{'index':1174,'lag':130,'radius':'1/32',
                'literal_carry_difference':15,'eta':boundary.centering_offset,
                'eta_next':boundary.next_centering_offset,'centered_carry':0},
            'changed_initial_control':{'first':261,'last':1040,'cells':16,
                'prefix_length':28,'odd_modulus':control.odd_modulus,
                'coalescence_by':control.depth,'initial':str(control.initial),
                'initial_nonzero':control.initial!=0,'lift_lower':str(control.lift_lower),
                'lift_upper':str(control.lift_upper),'ordered_pairs':780**2,
                'scaled_collision':16,'selected_source_contract':False},
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files},
            'pi_normality':'OPEN','actual_selected_saving':'UNPROVED'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    Path(args.output).write_text(json.dumps(receipt(),indent=2,sort_keys=True)+'\n')
    print('EXACT_FINITE: lag, carry-prefix and joint-clock receipts verified')
