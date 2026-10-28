"""Reproducible finite checks for a wavefront/Gamma information interface."""
from __future__ import annotations
import json
from fractions import Fraction as F
from observational_succ.causal_wavefront_gamma import (
    finite_beta_jet_kl,near_null_lag_discrete,near_null_lag_continuous,
    sampled_clock_gap,pell_boost_certificate,uniform_frontier_residual_bound,
)

def main():
    diag=[]
    for n in (1,2,4,16,128,1024):
        a,b,j=finite_beta_jet_kl(n)
        diag.append(dict(n=n,kl_order0_to_order1=a,kl_order1_to_order0=b,
                         exact_jeffreys_fraction=f'{j.numerator}/{j.denominator}',
                         chaser_discrete_gap=float(near_null_lag_discrete(n)),
                         chaser_continuum_gap=near_null_lag_continuous(n),
                         sampling_defect=sampled_clock_gap(n)))
    boosts={str(m):tuple(map(str,pell_boost_certificate(m))) for m in (1,2,3,5)}
    report={'scope':'finite arithmetic checks; gamma/causal theorems documented separately',
            'source':'original Oily R=(1-x)L, L(1)=1; order-zero is declared deflation',
            'edge_cases':{'deterministic_frontier_residual_bits':0,
                          'fresh_independent_fair_bit_residual_bits':1,
                          'uniform_8_bit_frontier_three_queries_lower_bound':uniform_frontier_residual_bound(8,3)},
            'pisot_null_frame_boost_exact_invariants':boosts,
            'rows':diag,'pi_normality':'OPEN','physical_gravity':'UNVERIFIED'}
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
