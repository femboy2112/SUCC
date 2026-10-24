"""Exact prime-Haar/Ramanujan controls for the BBP forcing (no π normality)."""
from __future__ import annotations

from fractions import Fraction as Q
import cmath
import json
from math import pi, log
from pathlib import Path

from observational_succ.pi_joint_prime_carrier import (
    forcing, forcing_local_haar_character, forcing_haar_shell_oracle,
    forcing_haar_product, joint_primary, local_primary, primes_through,
)


def char(frac: Q, h: int = 1) -> complex:
    return cmath.exp(2j*pi*float((h*frac)%1))


def main() -> None:
    checks=0
    primes=(7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    hvalues=(1,2,7,49,11,121)
    local={}
    for p in primes:
        local[str(p)]={}
        for h in hvalues:
            a=forcing_local_haar_character(p,h)
            b=forcing_haar_shell_oracle(p,h)
            assert a==b
            assert 0<a<=1
            checks+=2
            local[str(p)][str(h)]=str(a)

    product={}
    for h in (1,7):
        history=[]
        for m in (1,2,3,4,7,10,14,18,len(primes)):
            val=forcing_haar_product(primes[:m],h)
            assert 0<val<=1
            checks+=1
            history.append({'first_m_primes':m,'cutoff':primes[m-1],
                            'mean_product_exact':str(val),
                            'mean_product_float_noncertifying':round(float(val),9),
                            'scaled_by_log4_noncertifying':round(float(val)*(log(primes[m-1])**4),6)})
        product[str(h)]=history

    # Negative control: a finite 10-prime product fails the over-strong <1/30.
    ten=forcing_haar_product(primes[:10],1)
    assert Q(1,30)<ten<Q(1,20)
    checks+=2

    actual={}
    for N in (64,256,1024,4096):
        source=[forcing(n) for n in range(1,N+1)]
        for x in source[:min(64,N)]:
            assert sum((v for _,v in joint_primary(x)),Q())%1 == x%1
            checks+=1
        global_mean=sum(char(x) for x in source)/N
        # The limit of actual real character means is 1 (not 0).
        fixed_p_mean=sum(char(local_primary(x,7)) for x in source)/N
        fixed_two_mean=sum(char((local_primary(x,7)+local_primary(x,11))%1) for x in source)/N
        actual[str(N)]={
            'source_e_r_mean_real_noncertifying':round(global_mean.real,9),
            'source_e_r_mean_imag_noncertifying':round(global_mean.imag,9),
            'p7_mean_real_noncertifying':round(fixed_p_mean.real,9),
            'p7p11_mean_real_noncertifying':round(fixed_two_mean.real,9),
            'theory_p7':str(forcing_local_haar_character(7,1)),
            'theory_p7p11':str(forcing_haar_product((7,11),1)),
            'global_real_mean_error_bound':'<32*pi/N (paper inequality)',
        }

    payload={
        'schema':1,'source':'unaltered rational BBP four-pole forcing',
        'exact_formula':'m_p(h)=1-4/p^(v_p(h)+1)-4/p^(v_p(h)+2), p>=7, h!=0',
        'limit_order_paper_claim':{
           'average_time_then_add_primes':'0',
           'add_all_primes_per_source_time_then_average_time':'1',
           'scope':'one-step forcing r(n) only; not source U_n or pi normality'},
        'local_haar_exact':local,
        'finite_prime_mean_products':product,
        'negative_control_first_ten_product':str(ten),
        'negative_control_rejected_threshold':'<1/30 is FALSE; actual >1/30 and <1/20',
        'noncertifying_actual_prefix_averages':actual,
        'exact_assertions':checks,
        'notes':['Local multiplier is proved using p-adic shells and Ramanujan sums, not finite sampling.',
                 'Numerical phases here use cmath for adversarial diagnostics only.',
                 'The full original forcing mean tends to one, while fixed-place Haar products damp as cutoff increases.']}
    out=Path(__file__).resolve().parents[1]/'research'/'2026-10-24'/'PI_JOINT_LIMIT_ORDER_RECEIPT.json'
    out.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'exact_assertions':checks,'p7_h1':local['7']['1'],
                      'p11_h1':local['11']['1'],
                      'ten_prime_product':str(ten),
                      'outer_limits':'0 versus 1, proved in paper',
                      'output':str(out)},indent=2))

if __name__=='__main__':main()
